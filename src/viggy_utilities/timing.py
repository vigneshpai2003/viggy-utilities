from time import perf_counter


class _Timer:
    def __init__(self):
        self.p = 10

    def setPrecision(self, p):
        self.p = p

    def __call__(self):
        def timerDecorator(foo):
            def timerWrapper(*args, **kwargs):
                t = perf_counter()
                result = foo(*args, **kwargs)
                timerWrapper.time += perf_counter() - t
                timerWrapper.count += 1
                return result

            timerWrapper.__name__ = foo.__name__
            timerWrapper.__module__ = foo.__module__
            timerWrapper.__qualname__ = foo.__qualname__
            timerWrapper.__doc__ = foo.__doc__
            timerWrapper.__annotations__ = foo.__annotations__
            timerWrapper.__defaults__ = foo.__defaults__
            timerWrapper.__kwdefaults__ = foo.__kwdefaults__
            timerWrapper.__dict__ = foo.__dict__

            timerWrapper.time = 0
            timerWrapper.count = 0

            return timerWrapper

        return timerDecorator

    def getTime(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(round(function.time, self.p))
            except AttributeError:
                lst.append(-1)
        return lst

    def getCount(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(round(function.count, self.p))
            except AttributeError:
                lst.append(-1)
        return lst

    def getAvg(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(round(function.time / function.count, self.p))
            except AttributeError:
                lst.append(-1)
            except ZeroDivisionError:
                lst.append(round(0.0, self.p))
        return lst

    def getSpeed(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(round(function.count / function.time, self.p))
            except AttributeError:
                lst.append(-1)
            except ZeroDivisionError:
                lst.append(round(0.0, self.p))
        return lst

    def logTime(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(f"{function.__qualname__} was executed in {round(function.time, self.p)} sec")
            except AttributeError:
                lst.append(f"{function.__qualname__} is not timed")
        return lst

    def logCount(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(f"{function.__qualname__} was executed {round(function.count, self.p)} times")
            except AttributeError:
                lst.append(f"{function.__qualname__} is not timed")
        return lst

    def logAvg(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(f"{function.__qualname__} takes {round(function.time / function.count, self.p)} "
                           f"sec per execution")
            except AttributeError:
                lst.append(f"{function.__qualname__} is not timed")
            except ZeroDivisionError:
                lst.append(f"{function.__qualname__} takes {round(0.0, self.p)} sec per execution")
        return lst

    def logSpeed(self, *functions):
        lst = []
        for function in functions:
            try:
                lst.append(f"{function.__qualname__} executes {round(function.count / function.time, self.p)} "
                           f"times per sec")
            except AttributeError:
                lst.append(f"{function.__qualname__} is not timed")
            except ZeroDivisionError:
                lst.append(f"{function.__qualname__} executes {round(0.0, self.p)} times per sec")
        return lst


Timer = _Timer()
