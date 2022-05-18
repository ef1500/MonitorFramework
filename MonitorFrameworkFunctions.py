# Monitor Framework Function Library
# Written by ef1500
# Purpose: To provide functions similar to the decorators that allow you to check for things
# Without having to use the decorators

class BasicMonitor:
    def __init__(self, APIFunction, args=None):
        """
        This function outlines what we are monitoring for.
        APIObj is the API object that we are monitoring for,
        APIFunction is the function that we should run to check for that
        object, and the return object is the object we should return if
        the conditions are met. The APIargs are the arguments that should be
        passed to the APIFunction, if any. Defaults to None.
        """
        self.task = APIFunction

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
        Exact opposite of onObject.
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
        """
        func(*args, **kwargs) 
        if globalvar == condition:
            self.task()

    def NotOnGlobal(self, globalvar, condition, func, *args, **kwargs):
        """
        Exact Oppisite of onGlobal
        """
        func(*args, **kwargs) 
        if globalvar != condition:
            self.task()

    def onBool(self, globalvar, condition, func,*args, **kwargs):
        """
        Check a bool, and if it meets our condition, then run the task
        """
        func(*args, **kwargs)
        if globalvar == condition:
            self.task()

    def delay(self, interval, func,  *args, **kwargs):
        """
        Generic delay for any function.
        """
        import time
        time.sleep(interval)
        return func(*args, **kwargs)

    def onVarType(self, globalvar, vartype, func, *args, **kwargs):
        """
        Check a variable's type, and then if it matches our condition, then run the task
        """
        func(*args, **kwargs)
        if type(globalvar) == vartype:
            self.task()