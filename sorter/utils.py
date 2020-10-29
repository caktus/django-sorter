from itertools import tee, chain


def cycle_pairs(iterable):
    """
    Cycles through the given iterable, returning an iterator which
    returns the current and the next item. When reaching the end
    it returns the last and the first item.
    """
    first, last = iterable[0], iterable[-1]
    a, b = tee(iterable)
    next(iter(b))
    return chain(zip(a, b), [(last, first)])
