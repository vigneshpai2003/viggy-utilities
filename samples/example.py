from viggy_utilities import Timer


@Timer()
def print_something():
    print("Hello World")


for i in range(100):
    print_something()

print(Timer.logSpeed(print_something))
