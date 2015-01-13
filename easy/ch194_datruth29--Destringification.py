from cStringIO import StringIO

completed_string = StringIO()
escaped = False
balanced_quotes = True
string = raw_input("Enter your string: ")
escaped_characters = {
        "\\" : "\\",
        "b" : "\b",
        "f" : "\f",
        "n" : "\n",
        "r" : "\r",
        "t" : "\t",
        "v" : "\v",
        "\'": "\'",
        "\"": "\""
        }

for character in string:
    if not escaped and character == "\"":
        balanced_quotes = not balanced_quotes
    elif not escaped and character == "\\":
        escaped = True
    elif not escaped:
        completed_string.write(character)
    elif escaped and character in escaped_characters:
        completed_string.write(escaped_characters.get(character))
        escaped = False
    elif escaped:
        completed_string.close()
        raise Exception("Invalid String")

if balanced_quotes:
    print(completed_string.getvalue())
else:
    completed_string.close()
    raise Exception("Invalid String")