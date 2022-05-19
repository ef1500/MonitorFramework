# Monitor Framework
## What is this?
This is a framework that is meant to serve as a faster way to code monitors.

If that doesn't make sense, let me give you an actual example. Let's say you have a manga that you really like, so you decide to write a program that monitors for a new chapter. You can use this framework to run a task when specific conditions are met, like for example, a new chapter of your favorite manga.

Example

```
from MonitorFramework import onBool

bool newChapter = False

def chapterAlert():
    print("New Chapter Found!")

# Will Monitor the variable newChapter for the True condition
# And once the condition is true, it will then run the function
@onBool(chapterAlert, newChapter, True)
def CheckForChapter():
    newChapter = True

```

I was getting frustrated and fed up with having to code a specific monitor every single time I wrote a new program, so I wrote this.