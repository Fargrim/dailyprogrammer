using System;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace DailyProgrammer
{
    public class Challenge262
    {
        public Challenge262()
        {
        }

        public static void MaybeNumeric(string input)
        {
            double test;
            if (double.TryParse(input, out test))
            {
                Debug.WriteLine(test + "(number)");
            }
            else
            {
                Debug.WriteLine(input + "(string)");
            }
        }

        public static void Main(string[] args)
        {
            string[] test = { "123", "44.234", "0x123N" };
            int x = 1;
            foreach (string testCase in test)
            {
                Debug.Write("Test " + x + ": ");
                Challenge262.MaybeNumeric(testCase);
                x++;
            }
        }
    }
}

