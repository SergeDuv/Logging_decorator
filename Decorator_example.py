import logging


logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    stream=sys.stdout,
)
logger = logging.getLogger("notebook")

def log(func):
    def wrapper(*args, **kwargs):
        output = func(*args, **kwargs)
        msg = f"{func.__name__} was run with the following args: {args} and the following kwargs {kwargs}"
        logger.info(msg)
        return output
    return wrapper


@log
def print_args(*args, **kwargs):
    print(args)
    print(kwargs)


>>> print_args(10, a=2, b="test")
(10,)
{'a': 2, 'b': 'test'}
2022-03-06 18:07:05,248 - notebook - INFO - print_args was run with the following args: (10,) and the following kwargs {'a': 2, 'b': 'test'}

>>> print_args(10, 100, a=2, b="test")
(10, 100)
{'a': 2, 'b': 'test'}
2022-03-06 18:07:05,562 - notebook - INFO - print_args was run with the following args: (10, 100) and the following kwargs {'a': 2, 'b': 'test'}
