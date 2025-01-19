import functools



class SubparserBuilder:
    """
    class as Decorator

    When a function is decorated , it is added to '_decoratess'
    and can be enumerated later by the 'decoratess()' function
    Ref: https://realpython.com/primer-on-python-decorators/#classes-as-decorators

    python
        @SubpraserBuilder
        def build_subparsers(parser):
            subparsers = []
            ...
            retuen subparsers

    """

    # keep track of decoratees
    _decoratees = set()

    def __init__(self, func):
        # if not callable(func) or isinstance(func , type):
        #     raise ValueError(f'Not Callable : {func}')
        self._decoratees.add(func)
        functools.update_wrapper(self , func)
        self.func = func


    def __call__(self, *args , **kwargs):
            return self.func(*args , **kwargs)

    @classmethod
    def decoratees(cls):
          return list(cls._decoratees)



