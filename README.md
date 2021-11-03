# Utilities

Provides basic utilities such as timing of functions 
with negligible overhead and simple usage

1. Installation

`> git clone https://github.com/vigneshpai2003/viggy-utilities.git`

`> cd viggy-utilities`

`> pip install .`

2. Import

`from viggy_utilities import Timer`

3. Usage

```
class MyClass:
    ...
    
    @Timer()
    def MyFunction(self, *args, **kwargs):
        <code>
        return stuff


@Timer()
def MyOtherFunction(*args, **kwargs):
    <code>
    return stuff
```

Call your functions, write your code as you normally do
```
Obj1 = MyClass(...)
Obj2 = MyClass(...)


Obj1.MyFunction(...)
Obj2.MyFunction(...)

MyOtherFunction(...)
```

Print or get statistics regarding function execution
```
print(*Timer.logSpeed(MyClass.MyFunction, MyOtherFunction), sep="\n")
```
