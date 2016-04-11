using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Diagnostics;

namespace DailyProgrammer
{
    class Challenge261
    {

        // [8, 1, 6, 3, 5, 7, 4, 9, 2] => true
        // [2, 7, 6, 9, 5, 1, 4, 3, 8] => true
        // [3, 5, 7, 8, 1, 6, 4, 9, 2] => false
        // [8, 1, 6, 7, 5, 3, 4, 9, 2] => false
        // [1, 14, 8, 11, 15, 4, 10, 5, 12, 7, 13, 2, 6, 9, 3, 16]
        // [1, 8, 12, 13, 14, 11, 7, 2, 15, 10, 6, 3, 4, 5, 9, 16]
        // [1, 8, 12, 13, 14, 11, 7, 15, 2, 10, 6, 3, 4, 5, 9, 16]

        public int Length { get; set; }
        public int MagicVal { get; set; }
        public int SideLen { get; set; }
        public int[] Square { get; set; }
        

        public Challenge261(int[] array)
        {
            this.Length = array.Length;
            this.SideLen = (int)Math.Sqrt(array.Length);
            this.MagicVal = (SideLen * ((SideLen*SideLen)+ 1)) / 2;
            this.Square = array;
        }

        public bool checkSum(int sum)
        {
            return sum == MagicVal ? true : false;
        }

        public bool checksRows()
        {
            bool result = false;
            int sum;
            for (int index = 0; index < Length; index += SideLen)
            {
                sum = 0;
                for (int rowModifier = 0; rowModifier < SideLen; rowModifier++)
                {
                    sum += Square[index + rowModifier];
                }
                result = checkSum(sum);
            }
            return result;
        }

        public bool checkCols()
        {
            bool result = false;
            int sum;
            for (int index = 0; index < SideLen; index++)
            {
                sum = 0;
                for (int colModifier = 0; colModifier < Length; colModifier += SideLen)
                {
                    sum += Square[index + colModifier];
                }
                result = checkSum(sum);
            }
            return result;
        }

        public bool checkDiags()
        {
            int sum = 0;
            for (int index = 0; index < Length; index += SideLen + 1)
            {
                sum += Square[index];
            }
            return checkSum(sum);
        }

        public static void printResult(int[] grid, bool result)
        {
            Debug.WriteLine("[" + string.Join(",", grid) + "] => " + result);
        }

        static void Main(string[] args)
        {
            int[][] tests = { new int[] { 8, 1, 6, 3, 5, 7, 4, 9, 2 },
                              new int[] { 2, 7, 6, 9, 5, 1, 4, 3, 8 },
                              new int[] { 3, 5, 7, 8, 1, 6, 4, 9, 2 },
                              new int[] { 8, 1, 6, 7, 5, 3, 4, 9, 2 },
                              new int[] { 1, 14, 8, 11, 15, 4, 10, 5, 12, 7, 13, 2, 6, 9, 3, 16 },
                              new int[] { 1, 8, 12, 13, 14, 11, 7, 2, 15, 10, 6, 3, 4, 5, 9, 16 },
                              new int[] { 1, 8, 12, 13, 14, 11, 7, 15, 2, 10, 6, 3, 4, 5, 9, 16 } };

            foreach (int[] test in tests)
            {
                Challenge261 testSquare = new Challenge261(test);
                if (!testSquare.checksRows() || !testSquare.checkCols() || !testSquare.checkDiags())
                {
                    Debug.WriteLine("[" + string.Join(",", testSquare.Square) + "] => " + false);
                }
                else
                {
                    Debug.WriteLine("[" + string.Join(",", testSquare.Square) + "] => " + true);
                }
            }

        }
    }
}
