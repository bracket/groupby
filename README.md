# groupby
simple grouping operations in Python

There's really only one right way to implement them, but they're never there when you need them.

Examples:

```python
from groupby import *

>>> count_groupby((i % 3, i) for i in range(5))
{0: 2, 1: 2, 2: 1}

>>> sum_groupby((i % 3, i) for i in range(5))
{0: 3, 1: 5,  2: 2}

>>> list_groupby((i % 3, i) for i in range(5))
{0: [ 0, 3 ], 1: [ 1, 4 ], 2: [2]}

>>> set_groupby((i % 2, i % 3) for i in range(100))
{0: {0, 1, 2}, 1: {0, 1, 2}}
```
