# Monitor Framework Function Library
# Written by ef1500
# Purpose: To provide functions similar to the decorators that allow you to check for things
# Without having to use the decorators
# There's also some extended functionality here. 
# You can monitor for certain objects to become true, unlike with the decorators, which is quite nice.

class BasicMonitor:
    """
    Basic Monitor Class. Allows for simple things, like monitoring for a bool to become true
    or for an object to have a certain value before running the task.
    """
    def __init__(self, task, condition=None, value=None, type_=None):
        """
        This outlines what we are monitoring for.
        OnMonitor is the function that we want to run whenever our
        other cases succeed.
        """
        self.task = task
        self.Auxililary = None
        
        self.condition = condition      # If we want to monitor for a condition, we set this
        self.value = value              # If we want to monitor for a value, we set this
        self.type = type_               # If we want to monitor for a type, we set this

    def onObject(self, func, *args, **kwargs):
        """
        Run a task when ANY API object was returned.
        This will Monitor for ANY type except None. You may want to use a different function to
        narrow down what you're monitoring for. 
        example usage: onObject(checkForChapter, "Citrus") 
        """
        isObject = func(*args, **kwargs)
        if isObject != None:
            self.task()
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

    def onLocal(self, condition, func,*args, **kwargs):
        """
        Check the return value of the function, then run the task if the conditions are met.
        Example usage: onBool(isNewChapter, True, downloadChapter, path)
        """
        object = func(*args, **kwargs)
        if object == condition:
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
    
    def executeReturn(self, func, *args, **kwargs):
        """
        Run a task when ANY API object was returned.
        This will Monitor for ANY type except None. You may want to use a different function to
        narrow down what you're monitoring for. 
        example usage: onObject(checkForChapter, "Citrus")
        Note: This will run the task with the object as the params.
        """
        isObject = func(*args, **kwargs)
        if isObject != None:
            self.task(isObject)
            return isObject
        if isObject == None:
            return isObject