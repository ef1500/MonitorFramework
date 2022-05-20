# Monitor Framework
# Written By EF1500
# Purpose of the Monitor Framework: To interact with a given API so that we can watch for a specified object.
# Example of what I want to be able to do:
# MonitorFor(Object, Query, Interval, ReturnObject)
# Or... MonitorFor(Object, Function, Interval, ReturnObject)
# This is an interface that directly interfaces with an API so that one can efficently monitor for something
# This is mainly because I would like to monitor things and download them to my PC without having to constantly make sure that they are still running
# Or to wake up only to see that my program has errored out
# There are also decorator functions, that you can use if you'd like, they act as "partial" monitors almost, simply watching for an event to take place
# The primary purpose of the decorators is so that you don't have to spend as much time rewriting code trying to integrate this library
# And you can focus more on what it is you want to accomplish- think of this just as a simple supplement

# DECORATORS
# What do we do when the monitor succesfully picks something up?
# How do we process that? These Decorators will aid in monitoring for various things
# That a function might return. 
# An example: I'm writing a manga downloader, and I'm getting tired of the threadpool saying that its lost connection,
# failed, or timeouted too many times. I needed an easier way to just monitor for chapters only when I needed to.
# I simply added the @onBool decorator with the sendDiscordMessage variable and then it sent the webhook without 
# Getting timeouted by the API or making unnecessary requests.
from inspect import getargvalues


def onObject(task):
    """
    Decorator to run a task when the API object we were monitoring for was found.
    Called like @onObject(sendDiscordEmbed) or @onObject(downloadManga)
    """
    def runTaskOnObject(func, *args, **kwargs):
        isObject = func(*args, **kwargs)
        if isObject != None:
            task(isObject)
            return isObject
        else:
            pass
    return runTaskOnObject

def onObjectFail(task):
    """
    Decorator to run a task when the monitor does not return the obejct we anticipated.
    Called Like @onObjectFail(sendDiscordMessage) or @onObjectFail(sendFailureMessage)
    """
    def runTaskOnObjectFail(func, *args, **kwargs):
        isObject = func(*args, **kwargs)
        if isObject == None:
            task()
            return isObject
        if isObject != None:
            return isObject
    return runTaskOnObjectFail

def onGlobal(task, globalvar, condition):
    """
    Decorator to check a global variable instead of a return object
    Usage: @onGlobal(sendDiscordEmbed, Chapter_Name, "Chapter 1")
    You can use this function to run a task if the check variable matches the test variable
    """
    
    def onglobal(func, globalvar=globalvar, condition=condition, *args, **kwargs):
        func(*args, **kwargs) 
        if globalvar == condition:
            task()
        else:
            pass
    return onglobal

def notOnGlobal(task, globalvar, condition):
    """
    Decorator to check a global variable instead of a return object
    Usage: @notOnGlobal(sendNoChapterMessage, newChapter, "Chapter2")
    You can use this function to run a task if the condition matches the global var
    """
    def notonglobal(func, globalvar=globalvar, condition=condition, *args, **kwargs):
        func(*args, **kwargs) 
        if globalvar != condition:
            task()
        else:
            pass
    return notonglobal

def onGlobalBool(task, globalvar, condition):
    """
    Decorator to check a bool, and do work if the bool is true
    (I Didn't know you couldn't update decorator values and I got shadowbanned on stackoverflow for asking)
    Usage: @onBool(sendDiscordMessage, isNewChapter, True)
    This will send a discord message as soon as isNewChapter is set to True, and then it will finally reset the variable
    """
    def onglobalbool(func, globalvar=globalvar, condition=condition, *args, **kwargs):
        func(*args, **kwargs)
        if globalvar == condition:
            task()
        else:
            pass
    return onglobalbool

def onLocalBool(task, condition):
    """
    Decorator to check the return value (bool) of a function
    and then to run a task if it matches our value
    Usage: @onLocalBool(sendEmbed, True)
    """
    def onlocalbool(func, condition=condition, *args, **kwargs):
        localvar = func(*args, **kwargs)
        if localvar == condition:
            task()
        else:
            pass
    return onlocalbool   

def delay(interval):
    """
    Decorator for timed check.
    Runs a task in x time
    Example Usage: @delay(5)
    """
    def runfunc(func,  *args, **kwargs):
        import time
        time.sleep(interval)
        return func(*args, **kwargs)
    return runfunc

def onVarType(task, globalvar, vartype):
    """
    Decorator to compare typenames. If the globalvar's type is the same as 
    the vartype, then run the task.
    Example Usage: @onVarType(downloadChapter, isNewChapter, str)
    """
    def onvartype(func, globalvar=globalvar, *args, **kwargs):
        func(*args, **kwargs)
        if type(globalvar) == vartype:
            task()
        else:
            pass

    return onvartype

def onObjectType(task, vartype):
    """
    Decorator to run a task based on the returned object type. If the type matches, then run the task.
    Usage: @onObjectType(sendMessage, str)
    """
    def onobjecttype(func, *args, **kwargs):
        object = func(*args, **kwargs)
        if type(object) == vartype:
            task()
        else:
            pass
    return onobjecttype

def executeReturn(task):
    """
    Decorator to run a function, then run the value that it returns.
    This is useful if you have a monitor that returns something when it exists,
    and you wanted to download that thing when it exists, for example.
    This will not check before executing, it will execute the return regardless
    This Decorator will run the return object as a parameter to the task
    specified
    """
    def executereturn(func, *args, **kwargs):
        object = func(*args, **kwargs)
        return task(object)
    
    return executeReturn

def c_executeReturn(task, condition):
    """
    This decorator will Execute a return object on condition/Value.
    This will not check types, that is reserved for another decorator.
    This Decorator will run the return object as a parameter to the task
    specified
    """
    def c_executereturn(func, *args, **kwargs):
        object = func(*args, **kwargs)
        if object == condition:
            return task(object)
        else:
            pass
    return c_executereturn 

def ct_executeReturn(task, vartype):
    """
    This Decorator will run the return object as a parameter to the task
    specified if the condition is met
    """
    def ct_executereturn(func, *args, **kwargs):
        object = func(*args, **kwargs)
        if type(object) == vartype:
            return task(object)
        else:
            pass
    return ct_executereturn

