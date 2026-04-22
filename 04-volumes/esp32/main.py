#!/usr/bin/env python3
"""
serial_bridge.py — Pipe stdin → serial port and serial port → stdout.

Usage:
    python serial_bridge.py --port /dev/ttyUSB0 --baud 115200

Press Ctrl+C to exit.
"""

import argparse
import sys
import threading
import serial


def stdin_to_serial(ser: serial.Serial, stop_event: threading.Event) -> None:
    """Read lines from stdin and write them to the serial port."""
    try:
        for line in sys.stdin:
            if stop_event.is_set():
                break
            ser.write(line.encode())
            ser.flush()
    except (OSError, serial.SerialException) as exc:
        if not stop_event.is_set():
            print(f"\n[stdin→serial error] {exc}", file=sys.stderr)
    finally:
        stop_event.set()


def serial_to_stdout(ser: serial.Serial, stop_event: threading.Event) -> None:
    """Read bytes from the serial port and write them to stdout."""
    try:
        while not stop_event.is_set():
            if ser.in_waiting:
                data = ser.read(ser.in_waiting)
                sys.stdout.write(data.decode(errors="replace"))
                sys.stdout.flush()
    except (OSError, serial.SerialException) as exc:
        if not stop_event.is_set():
            print(f"\n[serial→stdout error] {exc}", file=sys.stderr)
    finally:
        stop_event.set()


def main() -> None:
    parser = argparse.ArgumentParser(description="Bridge stdin/stdout to a serial port.")
    parser.add_argument("--port", required=True, help="Serial port (e.g. /dev/ttyUSB0 or COM3)")
    parser.add_argument("--baud", type=int, default=115200, help="Baud rate (default: 9600)")
    parser.add_argument("--bytesize", type=int, default=8, choices=[5, 6, 7, 8])
    parser.add_argument("--parity", default="N", choices=["N", "E", "O", "M", "S"])
    parser.add_argument("--stopbits", type=float, default=1.0, choices=[1, 1.5, 2])
    parser.add_argument("--timeout", type=float, default=0.1,
                        help="Read timeout in seconds (default: 0.1)")
    args = parser.parse_args()

    try:
        ser = serial.Serial(
            port=args.port,
            baudrate=args.baud,
            bytesize=args.bytesize,
            parity=args.parity,
            stopbits=args.stopbits,
            timeout=args.timeout,
        )
    except serial.SerialException as exc:
        sys.exit(f"Could not open serial port '{args.port}': {exc}")

    print(f"[serial_bridge] Connected to {ser.name} @ {args.baud} baud. Press Ctrl+C to quit.",
          file=sys.stderr)

    stop_event = threading.Event()

    reader_thread = threading.Thread(
        target=serial_to_stdout, args=(ser, stop_event), daemon=True
    )
    writer_thread = threading.Thread(
        target=stdin_to_serial, args=(ser, stop_event), daemon=True
    )

    reader_thread.start()
    writer_thread.start()

    try:
        stop_event.wait()
    except KeyboardInterrupt:
        print("\n[serial_bridge] Interrupted by user.", file=sys.stderr)
    finally:
        stop_event.set()
        ser.close()
        reader_thread.join(timeout=1)
        writer_thread.join(timeout=1)
        print("[serial_bridge] Connection closed.", file=sys.stderr)


if __name__ == "__main__":
    main()