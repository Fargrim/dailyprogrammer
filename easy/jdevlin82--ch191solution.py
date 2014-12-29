from urllib2 import urlopen


class Word(object):

    def __init__(self):
        self.word_count = {}

    @staticmethod
    def alpha_only(word):
        """Converts word to lowercase and removes any non-alphabetic characters."""
        x = ''
        for letter in word:
            s = letter.lower()
            if s in 'abcdefghijklmnopqrstuvwxyz':
                x += s
        if len(x) > 0:
            return x

    def count(self, line):
        """Takes a line from the file and builds a list of lowercased words containing only alphabetic chars.
            Adds each word to word_count if not already present, if present increases the count by 1."""
        words = [self.alpha_only(x) for x in line.split(' ') if self.alpha_only(x) is not None]
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            elif word is not None:
                self.word_count[word] = 1


class File(object):

    def __init__(self, book):
        self.book = urlopen(book)
        self.word = Word()

    def strip_line(self, line):
        """Strips newlines, tabs, and return characters from beginning and end of line. If remaining string > 1,
        splits up the line and passes it along to the count method of the word object."""
        s = line.strip('\n\r\t')
        if s > 1:
            self.word.count(s)

    def process_book(self):
        """Main processing loop, will not begin processing until the first line after the line containing "START".
        After processing it will close the file."""
        begin = False
        for line in self.book:
            if begin:
                self.strip_line(line)
            elif 'START' in line:
                begin = True
        self.book.close()

book_content = File('http://www.gutenberg.org/cache/epub/47498/pg47498.txt')

book_content.process_book()

count = sorted(book_content.word.word_count.items(), key=lambda c: c[1], reverse=True)

for each in count:
    print each
# Delete the original dict, it is no longer needed
del book_content.word.word_count
