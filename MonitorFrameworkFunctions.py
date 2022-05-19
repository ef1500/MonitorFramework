# Monitor Framework Function Library
# Written by ef1500
# Purpose: To provide functions similar to the decorators that allow you to check for things
# Without having to use the decorators

class BasicMonitor:
    def __init__(self, onMonitor, args=None):
        """
        This function outlines what we are monitoring for.
        OnMonitor is the function that we want to run whenever our
        other cases succeed. The functions that are taken as arguments
        elsewhere in this class are the queries to the API/things that we
        are monitoring for.
        """
        self.task = onMonitor

    def onObject(self, func, *args, **kwargs):
        """
        Run a task when the API object we were monitoring for was found.
        example usage: onObject(checkForChapter, "Citrus")
        """
        isObject = func(*args, **kwargs)
        if isObject != None:
            self.task(isObject)
            return isObject
        if isObject == None:
            return isObject
        
    def onObjectFail(self, func, *args, **kwargs):
        """
        Exact opposite of onObject. If the object was not found, then nothing will be
        returned.
        """
        isObject = func(*args, **kwargs)
        if isObject == None:
            self.task()
            return isObject
        if isObject != None:
            return isObject

    def onGlobal(self, globalvar, condition, func, *args, **kwargs):
        """
        Check a Variable and if it matches out condition, then run the task
        Example Usage: onGlobal(newChapter, "Chapter 91", downloadChapter)
        """
        func(*args, **kwargs) 
        if globalvar == condition:
            self.task()
        else:
            pass

    def NotOnGlobal(self, globalvar, condition, func, *args, **kwargs):
        """
        Exact Oppisite of onGlobal.
        Example usage: NotOnGlobal(fail, False, sendFailureMessage)
        """
        func(*args, **kwargs) 
        if globalvar != condition:
            self.task()
        else:
            pass

    def onBool(self, globalvar, condition, func,*args, **kwargs):
        """
        Check a bool, and if it meets our condition, then run the task.
        Example usage: onBool(isNewChapter, True, downloadChapter, path)
        """
        func(*args, **kwargs)
        if globalvar == condition:
            self.task()
        else:
            pass

    def delay(self, interval, func,  *args, **kwargs):
        """
        Generic delay for any function.
        Example usage: delay(3, printHello)
        """
        import time
        time.sleep(interval)
        return func(*args, **kwargs)

    def onVarType(self, globalvar, vartype, func, *args, **kwargs):
        """
        Check a variable's type, and then if it matches our condition, then run the task
        Example usage: onVarType(chapter, str, downloadChapter)
        """
        func(*args, **kwargs)
        if type(globalvar) == vartype:
            self.task()
        else:
            pass