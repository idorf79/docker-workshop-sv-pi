#include <iostream>
#include <string>
#include <sstream>

int main(int argc, char *argv[])
{
    if (argc != 4)
    {
        std::cout << "Usage: calculator <num1> <op> <num2>\n";
        return 1;
    }

    double num1 = std::stod(argv[1]);
    double num2 = std::stod(argv[3]);
    char op = argv[2][0];

    double result;
    switch (op)
    {
    case '+':
        result = num1 + num2;
        break;
    case '-':
        result = num1 - num2;
        break;
    case '*':
        result = num1 * num2;
        break;
    case '/':
        result = num1 / num2;
        break;
    default:
        std::cout << "Invalid operator\n";
        return 1;
    }

    std::cout << num1 << " " << op << " " << num2 << " = " << result << "\n";
    return 0;
}