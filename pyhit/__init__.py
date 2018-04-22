import inspect
import sys

def HitCount(func):
    #print("Frame: \n")
    #print(frame)
    #print("Caller: {}".format(frame[0][3]))


    print("The function {} was called in module {} -- {}".format(func.__name__, sys.modules[func.__module__],
                                                                 func.__))

class HitCounter(object):

    def __init__(self, f):
        print("inside HitCounter.__init__()")
        self.f = f

    def __call__(self, *args, **kwargs):
        #HitCount(inspect.getouterframes(inspect.currentframe(), 2))
        HitCount(self.f)
        print("Running {} with {} and {}".format(self.f, args, kwargs))
        self.f(*args, **kwargs)
        print("Exited", self.f.__name__)

@HitCounter
def innerFunction(a, b="None"):
    print("Inner Function")

def outerFunction(message):
    print("OuterFuction")
    print("Message: {}".format(message))
    innerFunction("333", b="TEST")

if __name__ == '__main__':
    outerFunction('Hey!')