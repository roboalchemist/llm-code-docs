# Source: https://boltons.readthedocs.io/en/latest/mathutils.html

Title: Mathematical functions — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/mathutils.html

Markdown Content:
`mathutils` - Mathematical functions[](https://boltons.readthedocs.io/en/latest/mathutils.html#module-boltons.mathutils "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

This module provides useful math functions on top of Python’s built-in [`math`](https://docs.python.org/3/library/math.html#module-math "(in Python v3.14)") module.

_class_ boltons.mathutils.Bits(_val=0_, _len\_=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits "Link to this definition")
An immutable bit-string or bit-array object. Provides list-like access to bits as bools, as well as bitwise masking and shifting operators. Bits also make it easy to convert between many different useful representations:

*   bytes – good for serializing raw binary data

*   int – good for incrementing (e.g. to try all possible values)

*   list of bools – good for iterating over or treating as flags

*   hex/bin string – good for human readability

as_bin()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.as_bin)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.as_bin "Link to this definition")as_bytes()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.as_bytes)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.as_bytes "Link to this definition")as_hex()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.as_hex)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.as_hex "Link to this definition")as_int()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.as_int)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.as_int "Link to this definition")as_list()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.as_list)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.as_list "Link to this definition")_classmethod_ from_bin(_bin_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.from_bin)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.from_bin "Link to this definition")_classmethod_ from_bytes(_bytes\__)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.from_bytes)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.from_bytes "Link to this definition")_classmethod_ from_hex(_hex_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.from_hex)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.from_hex "Link to this definition")_classmethod_ from_int(_int\__, _len\_=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.from_int)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.from_int "Link to this definition")_classmethod_ from_list(_list\__)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#Bits.from_list)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.from_list "Link to this definition")len[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.len "Link to this definition")val[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.Bits.val "Link to this definition")
Alternative Rounding Functions[](https://boltons.readthedocs.io/en/latest/mathutils.html#alternative-rounding-functions "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

boltons.mathutils.clamp(_x_, _lower=-inf_, _upper=inf_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#clamp)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.clamp "Link to this definition")
Limit a value to a given range.

Parameters:
*   **x** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_or_[_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Number to be clamped.

*   **lower** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_or_[_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Minimum value for x.

*   **upper** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_or_[_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Maximum value for x.

The returned value is guaranteed to be between _lower_ and _upper_. Integers, floats, and other comparable types can be mixed.

>>> clamp(1.0, 0, 5)
1.0
>>> clamp(-1.0, 0, 5)
0
>>> clamp(101.0, 0, 5)
5
>>> clamp(123, upper=5)
5

Similar to [numpy’s clip](http://docs.scipy.org/doc/numpy/reference/generated/numpy.clip.html) function.

boltons.mathutils.ceil(_x_, _options=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#ceil)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.ceil "Link to this definition")
Return the ceiling of _x_. If _options_ is set, return the smallest integer or float from _options_ that is greater than or equal to _x_.

Parameters:
*   **x** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_or_[_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Number to be tested.

*   **options** (_iterable_) – Optional iterable of arbitrary numbers (ints or floats).

>>> VALID_CABLE_CSA = [1.5, 2.5, 4, 6, 10, 25, 35, 50]
>>> ceil(3.5, options=VALID_CABLE_CSA)
4
>>> ceil(4, options=VALID_CABLE_CSA)
4

boltons.mathutils.floor(_x_, _options=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/mathutils.html#floor)[](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.floor "Link to this definition")
Return the floor of _x_. If _options_ is set, return the largest integer or float from _options_ that is less than or equal to _x_.

Parameters:
*   **x** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")_or_[_float_](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – Number to be tested.

*   **options** (_iterable_) – Optional iterable of arbitrary numbers (ints or floats).

>>> VALID_CABLE_CSA = [1.5, 2.5, 4, 6, 10, 25, 35, 50]
>>> floor(3.5, options=VALID_CABLE_CSA)
2.5
>>> floor(2.5, options=VALID_CABLE_CSA)
2.5

Note: [`ceil()`](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.ceil "boltons.mathutils.ceil") and [`floor()`](https://boltons.readthedocs.io/en/latest/mathutils.html#boltons.mathutils.floor "boltons.mathutils.floor") functions are based on [this example](https://docs.python.org/3/library/bisect.html#searching-sorted-lists) using from the [`bisect`](https://docs.python.org/3/library/bisect.html#module-bisect "(in Python v3.14)") module in the standard library. Refer to this [StackOverflow Answer](http://stackoverflow.com/a/12141511/811740) for further information regarding the performance impact of this approach.
