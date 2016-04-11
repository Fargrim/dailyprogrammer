using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace DailyProgrammer
{
    public class Challenge262
    {
        // www.reddit.com/r/dailyprogrammer
        // Challenge #262 [Easy] MaybeNumeric

        // MaybeNumeric is a function that returns either a number or a string depending on whether the 
        // input(string) is a valid description of a number.

        // Sample input (string)
        // 123
        // 44.234
        // 0x123N

        // Sample output (any)
        // 123 (number)
        // 44.234 (number)
        // 0x123N (string)

        public Challenge262()
        {
        }

        public static object MaybeNumeric(string input)
        {
            // Checks if input parses to a double and returns an object of the result.

            double doubleTest;
            object result = input;
            if (double.TryParse(input, out doubleTest))
            {
                result = new double();
                result = doubleTest;
            }

            return result;
        }

        public static void Main(string[] args)
        {
            object result;
            string[] tests = { "123", "44.234", "0x123N" };
            int x = 1;
            foreach (string testCase in tests)
            {
                result = Challenge262.MaybeNumeric(testCase);
                Debug.WriteLine("Test " + x + ": " + result + " (" + result.GetType() + ")");
                x++;
            }
        }
    }
}

