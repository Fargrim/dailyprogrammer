"""
Most programming languages understand the concept of escaping strings. For example, if you wanted to put a double-quote " into a string that is delimited by double quotes, you can't just do this:
'this string contains ' a quote.'
That would end the string after the word contains, causing a syntax error. To remedy this, you can prefix the quote with a backslash \ to escape the character
'this string really does \' contain a quote.'
However, what if you wanted to type a backslash instead? For example:
'the end of this string contains a backslash. \'
The parser would think the string never ends, as that last quote is escaped! The obvious fix is to also escape the back-slashes, like so.
'lorem ipsum dolor sit amet \\\\'
The same goes for putting newlines in strings. To make a string that spans two lines, you cannot put a line break in the string literal:
'this string...
...spans two lines!'
The parser would reach the end of the first line and panic! This is fixed by replacing the newline with a special escape code, such as \n:
'a new line \n hath begun.'
Your task is, given an escaped string, un-escape it to produce what the parser would understand.
"""

"""
Input:

You will accept a string literal, surrounded by quotes, like the following:
'A random\nstring\\\''
If the string is valid, un-escape it. If it's not (like if the string doesn't end), throw an error!
"""

"""
Output:

Expand it into its true form, for example:
A random
string\'
"""

import sys


escape_chars = {
    'n': chr(10),
    '\"': '\"',
    '\'': '\'',
    '\\': '\\',
    'a': chr(7),
    'b': chr(8),
    'f': chr(12),
    'r': chr(13),
    't': chr(9),
    'v': chr(11),
    '0': chr(0)
}


"""
Handle bad input
"""

def bad_input(reason):
    sys.stdout.write("Bad input! ")
    sys.stdout.write(reason)
    exit(1)



"""
Search the string
"""

def string_check(input_string):
    result = ''
    escape_flag = False
    quote_count = 0
    for each in input_string:
        if not escape_flag and each == '\"':
            quote_count += 1
        elif not escape_flag and each == '\\':
            escape_flag = True
        elif not escape_flag:
            result += each
        elif escape_flag and each in escape_chars:
            result += escape_chars[each]
            escape_flag = False
        else:
            bad_input('Bad escape character!')
    
            
    if quote_count % 2 != 0:
        bad_input('Invalid string!')
    
    return result  


"""
TODO Update code to handle multiple command line inputs
"""

test_string = raw_input('Enter string: ')
sys.stdout.write(string_check(test_string))