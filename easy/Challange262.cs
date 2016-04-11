using System;
using System.Collections.Generic;
using System.Diagnostics;

namespace DailyProgrammer
{
    public class Challenge262
    {


        public Challenge262()
        {
        }


        public static void MaybeNumeric (string input)
        {
            KeyValuePair<bool, object> result;
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

            foreach (string testCase in test)
            {
                Challenge262.MaybeNumeric(test);
            }                
        }
    }
}
