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


__version__ = '1.1'


def count_groupby(seq, key=None):
    '''Iterate over sequence and count occurrences of each key.

        Parameters:
            seq:
                Iterable[Tuple[Hashable, Any] | Any]

                Sequence of pairs to iterate over, or any sequence at all
                provided the key function is supplied.

            key:
                None | Callable

                If provided, seq may be an arbitrary sequence.  key will be
                applied to each element to determine the key to group on.

        Returns:
            Dict[Hashable, int]

            Counts of occurences of each key.
    '''

    seq = iter(seq)

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
    '''Iterate over sequence of pairs and sum second elements grouped by first elements

        Parameters:
            seq:
                Iterable[Tuple[Hashable, Any] | Any]

                Sequence of pairs to iterate over, or any sequence at all
                provided the key function is supplied.

            key:
                None | Callable

                If provided, seq may be an arbitrary sequence.  key will be
                applied to each element to determine the key to group on.

        Returns:
            Dict[Hashable, Any]

            Sums of elements grouped by key.
    '''

    seq = iter(seq)

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


def avg_groupby(seq, key=None):
    '''Iterate over sequence of pairs and take average of second elements grouped by first elements

        Parameters:
            seq:
                Iterable[Tuple[Hashable, Any] | Any]

                Sequence of pairs to iterate over, or any sequence at all
                provided the key function is supplied.

            key:
                None | Callable

                If provided, seq may be an arbitrary sequence.  key will be
                applied to each element to determine the key to group on.

        Returns:
            Dict[Hashable, Any]

            Averages of elements grouped by key.
    '''

    seq = iter(seq)

    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }
    counts = { }

    for k, v in seq:
        accumulator = out.get(k)
        if accumulator is None:
            out[k] = v
            counts[k] = 1
        else:
            out[k] += v
            counts[k] += 1

    for k in out:
        out[k] /= counts[k]

    return out


def list_groupby(seq, key=None):
    '''Iterate over sequence of pairs and construct lists of second elements grouped by first elements.

        Parameters:
            seq:
                Iterable[Tuple[Hashable, Any] | Any]

                Sequence of pairs to iterate over, or any sequence at all
                provided the key function is supplied.

            key:
                None | Callable

                If provided, seq may be an arbitrary sequence.  key will be
                applied to each element to determine the key to group on.

        Returns:
            Dict[Hashable, List[Any]]

            Lists of elements grouped by key.
    '''

    seq = iter(seq)

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
    '''Iterate over sequence of pairs and construct sets of second elements grouped by first elements.

        Parameters:
            seq:
                Iterable[Tuple[Hashable, Any] | Any]

                Sequence of pairs to iterate over, or any sequence at all
                provided the key function is supplied.

            key:
                None | Callable

                If provided, seq may be an arbitrary sequence.  key will be
                applied to each element to determine the key to group on.

        Returns:
            Dict[Hashable, Set[Any]]

            Sets of elements grouped by key.
    '''

    seq = iter(seq)

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


def unique_groupby(seq, key=None):
    '''Iterate over sequence of pairs and construct lists of uniqued second elements grouped by first elements.

        Parameters:
            seq:
                Iterable[Tuple[Hashable, Any] | Any]

                Sequence of pairs to iterate over, or any sequence at all
                provided the key function is supplied.

            key:
                None | Callable

                If provided, seq may be an arbitrary sequence.  key will be
                applied to each element to determine the key to group on.

        Returns:
            Dict[Hashable, List[Any]]

            Lists of distinct elements grouped by key.
    '''

    seq = iter(seq)

    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        accumulator = out.get(k)

        if accumulator is None:
            out[k] = [ v ]
        else:
            for x in accumulator:
                if x == v: break
            else:
                accumulator.apppend(v)

    return out


def generic_groupby(seq, accumulate, key=None):
    seq = iter(seq)

    if key is not None:
        seq = ((key(x), x) for x in seq)

    out = { }

    for k, v in seq:
        out[k] = accumulate(out.get(k), v)

    return out
