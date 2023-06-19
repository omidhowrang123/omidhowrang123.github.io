using System;

class Calculator
{
    static double Add(double x, double y)
    {
        return x + y;
    }

    static double Subtract(double x, double y)
    {
        return x - y;
    }

    static double Multiply(double x, double y)
    {
        return x * y;
    }

    static double Divide(double x, double y)
    {
        if (y != 0)
        {
            return x / y;
        }
        else
        {
            Console.WriteLine("Error: Division by zero");
            return double.NaN; // Return NaN (Not-a-Number) to represent invalid result
        }
    }

    static double GetUserInput(string prompt)
    {
        double userInput;
        while (true)
        {
            Console.Write(prompt);
            if (double.TryParse(Console.ReadLine(), out userInput)) // Validates user input as double
            {
                return userInput;
            }
            else
            {
                Console.WriteLine("Invalid input. Please enter a valid number.");
            }
        }
    }

    static Func<double, double, double> GetOperatorChoice()
    {
        Console.WriteLine("Select operation:");
        Console.WriteLine("1. Add");
        Console.WriteLine("2. Subtract");
        Console.WriteLine("3. Multiply");
        Console.WriteLine("4. Divide");

        while (true)
        {
            Console.Write("Enter choice (1/2/3/4): ");
            string choice = Console.ReadLine();

            switch (choice)
            {
                case "1":
                    return Add;
                case "2":
                    return Subtract;
                case "3":
                    return Multiply;
                case "4":
                    return Divide;
                default:
                    Console.WriteLine("Invalid choice. Please enter a valid operator.");
                    break;
            }
        }
    }

    static void Main()
    {
        double num1 = GetUserInput("Enter first number: ");
        double num2 = GetUserInput("Enter second number: ");
        Func<double, double, double> operatorFunc = GetOperatorChoice();

        double result = operatorFunc(num1, num2);
        Console.WriteLine("Result: " + result);
    }
}
