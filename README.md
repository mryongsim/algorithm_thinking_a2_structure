# algorithm_thinking_a2_structure

## Intro
This provides some basic structure for those trying to get assessment 2 working.

## Requirements
If running locally you will need:
1. [python](https://www.python.org/downloads/) installed - I suggest python 3+

2. either just write your code with an online editor (eg https://python-playground.com/) or

3. Get an IDE, [vscode](https://code.visualstudio.com/) is very good. if you use vscode i suggest you install some extensions such as Python, Python debugger, Pylance, it'll make your coding experience better

4. Get familiar with the command line if you're using an IDE so you can run your code from there

## File structure
It's pretty clear from the list but if not we have:
* generator - the generator code for generating the data + writing to file
* competitor - the competitor code
* max_heap - the max heap code
* experiment_1.py - the first experiment with some basic setup

For each experiment you should write a different file so it's easy to keep them separated

## How to
1. I suggest you write the code for generator, competitor, max_heap first
2. Then write experiment 1 and test them out
3. To test, in your command line/terminal you can run (in vs code you can open it up from the menu, and it should open in the current directory)
```
python3 experiment_1.py
```


## python basics
[CodeDex](https://www.codedex.io/python) or [grok](https://groklearning.com/course/python-for-beginners/)
If you don't know python it's probably a good idea to do some basic lessons. if you're using the above lessons i suggest you at least learn about:
- basic
- variable
- loop
- list
- functions
- classes - this last bit is how I've kind of structured the code.

### tips
- python really cares about indents. if you're code doesn't look right you're probably not indenting correctly.
- import is used to import code from another file or modules (which is basically just a group of files). There's some prebuilt ones and I think in here i've used `random` and `pathlib` only.
