# Monitor Framework
## What is this?
This is a framework that is meant to serve as a faster way to code monitors.

If that doesn't make sense, let me give you an actual example. Let's say you have a manga that you really like, so you decide to write a program that monitors for a new chapter. You can use this framework to run a task when specific conditions are met, like for example, a new chapter of your favorite manga.

Example

```python
from MonitorFramework import onGlobalBool

checkForChapters = True # Should we check for chapters?

def apiCall():
    print("Querying Api....")

def printQuery():
    print("ApiQuery")

# Will Check the variable checkForChapters for the True condition
# And if the condition is true, it will then run the function
@onGlobalBool(printQuery, checkForChapters, True)
def CheckForChapter():
    apiCall()

```

I was getting frustrated and fed up with having to code a specific monitor every single time I wrote a new program, so I wrote this.
