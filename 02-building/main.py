import platform
import argparse

print("Hello world!")
print(platform.processor())
print(platform.system())
print(platform.version())
print(platform.architecture())


parser = argparse.ArgumentParser()
parser.add_argument("--target", default=argparse.SUPPRESS)
ns = parser.parse_args()

print("Parsed arguments: {}".format(ns))