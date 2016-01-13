def test_count_groupby():
    from groupby import count_groupby

    pairs = [ (3, 1), (1, 1), (2, 1), (3, 1), (2, 1), (3, 1) ]

    actual = count_groupby(pairs)
    expected = { 1 : 1, 2 : 2, 3 : 3 }

    assert actual == expected

    data = [ 1, 3, 1, 2, 3, 2, 3, 4 ]

    actual = count_groupby(data, key=lambda x: x % 3)
    expected = { 0: 3 , 1 : 3, 2 :2 }
    assert actual == expected


def test_sum_groupby():
    from groupby import sum_groupby

    pairs = [ (3, .5), (1, .5), (3, 1.), (2, .5), (1, .5), (2, 1.5), (3, 1.5) ]

    actual = sum_groupby(pairs)
    expected = { 1 : 1., 2 : 2., 3 : 3. }

    assert actual == expected

    data = map(float, range(5))

    actual = sum_groupby(data, key=lambda x: x % 3)
    expected = { 0. : 3., 1. : 5., 2. : 2. }

    assert actual == expected


def test_list_groupby():
    from groupby import list_groupby

    pairs = [ (2, 'zwei'), (1, 'one'),  (2, 'two'), (3, 'three'), (3, 'drei'), (1, 'ein') ]

    actual = list_groupby(pairs)
    expected = { 1 : [ 'one', 'ein' ], 2 : [ 'zwei', 'two' ], 3 : [ 'three', 'drei' ] }

    assert actual == expected

    data = 'apple banana orange apricot blueberry weasel apple'.split()

    actual = list_groupby(data, key=lambda x: x[0])
    expected = {
        'a' : [ 'apple', 'apricot', 'apple' ],
        'b' : [ 'banana', 'blueberry' ],
        'o' : [ 'orange' ],
        'w' : [ 'weasel' ]
    }

    assert actual == expected


def test_set_groupby():
    from groupby import set_groupby

    pairs = [ ('x', 'apple'), ('y', 'banana'), ('x', 'apple'), ('x', 'banana') ]

    actual = set_groupby(pairs)
    expected = { 'x' : { 'apple', 'banana' }, 'y' : { 'banana' } }

    assert actual == expected

    data = 'apple banana orange apricot blueberry weasel apple'.split()

    actual = set_groupby(data, key=lambda x:x[0])
    expected = {
        'a' : { 'apple', 'apricot' },
        'b' : { 'banana', 'blueberry' },
        'o' : { 'orange' },
        'w' : { 'weasel' },
    }

    assert actual == expected


def test_generic_groupby():
    from groupby import generic_groupby, set_groupby

    data = 'apple banana orange apricot blueberry weasel apple'.split()
    pairs = [ (x[0], x) for x in data ]

    def accumulate(accumulator, value):
        if accumulator is None:
            return { value }
        else:
            accumulator.add(value)
            return accumulator

    actual = generic_groupby(pairs, accumulate)
    expected = set_groupby(pairs)

    assert actual == expected

    actual = generic_groupby(data, accumulate, key=lambda x:x[0])

    assert actual == expected


