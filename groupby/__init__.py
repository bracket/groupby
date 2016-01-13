'''groupby - simple grouping operations in python

Each groupby function takes a sequence of key/value pairs.  If a key function
is supplied then the sequence need not be key value/pairs, as the key function
will be applied to each element of the sequence to extract a key from the value
directly.

The function will return a dictionary object, the keys of which are the first elements
of the key/value pairs, and the values of which are determined by the name of
the function but will in some way depend on second elements of the key/value
pairs.
'''


__version__ = '1.0'


def count_groupby(seq, key=None):
    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        accumulator = out.get(k)
        if accumulator is None:
            out[k] = 1
        else:
            out[k] += 1

    return out


def sum_groupby(seq, key=None):
    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        accumulator = out.get(k)
        if accumulator is None:
            out[k] = v
        else:
            out[k] += v

    return out


def list_groupby(seq, key=None):
    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        accumulator = out.get(k)
        if accumulator is None:
            out[k] = [ v ]
        else:
            accumulator.append(v)

    return out


def set_groupby(seq, key=None):
    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        accumulator = out.get(k)
        if accumulator is None:
            out[k] = { v }
        else:
            accumulator.add(v)

    return out


def generic_groupby(seq, accumulate, key=None):
    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        out[k] = accumulate(out.get(k), v)

    return out
