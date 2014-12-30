"""
Most programming languages understand the concept of escaping strings. For example, if you wanted to put a double-quote " into a string that is delimited by double quotes, you can't just do this:
"this string contains " a quote."
That would end the string after the word contains, causing a syntax error. To remedy this, you can prefix the quote with a backslash \ to escape the character.
"this string really does \" contain a quote."
However, what if you wanted to type a backslash instead? For example:
"the end of this string contains a backslash. \"
The parser would think the string never ends, as that last quote is escaped! The obvious fix is to also escape the back-slashes, like so.
"lorem ipsum dolor sit amet \\\\"
The same goes for putting newlines in strings. To make a string that spans two lines, you cannot put a line break in the string literal:
"this string...
...spans two lines!"
The parser would reach the end of the first line and panic! This is fixed by replacing the newline with a special escape code, such as \n:
"a new line \n hath begun."
Your task is, given an escaped string, un-escape it to produce what the parser would understand.
"""

"""
Input:

You will accept a string literal, surrounded by quotes, like the following:
"A random\nstring\\\""
If the string is valid, un-escape it. If it's not (like if the string doesn't end), throw an error!
"""

"""
Output:

Expand it into its true form, for example:
A random
string\"
"""


"""
https://docs.python.org/2.0/ref/strings.html

\newline	Ignored
\\	Backslash (\)
\'	Single quote (')
\"	Double quote (")
\a	ASCII Bell (BEL)
\b	ASCII Backspace (BS)
\f	ASCII Formfeed (FF)
\n	ASCII Linefeed (LF)
\r	ASCII Carriage Return (CR)
\t	ASCII Horizontal Tab (TAB)
\v	ASCII Vertical Tab (VT)
"""

import sys


escape_chars = {
    "n": chr(10),
    "\"": "\\\"",
    "\'": "\\'",
    "a": chr(7),
    "b": chr(8),
    "f": chr(12),
    "r": chr(13),
    "t": chr(9),
    "v": chr(11),
    "0": chr(0)
}