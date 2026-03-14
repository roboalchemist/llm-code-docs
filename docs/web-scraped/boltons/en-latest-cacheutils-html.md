# Source: https://boltons.readthedocs.io/en/latest/cacheutils.html

Title: Caches and caching — boltons 25.0.0 documentation

URL Source: https://boltons.readthedocs.io/en/latest/cacheutils.html

Markdown Content:
`cacheutils` - Caches and caching[](https://boltons.readthedocs.io/en/latest/cacheutils.html#module-boltons.cacheutils "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

`cacheutils` contains consistent implementations of fundamental cache types. Currently there are two to choose from:

> *   [`LRI`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI "boltons.cacheutils.LRI") - Least-recently inserted
> 
> *   [`LRU`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRU "boltons.cacheutils.LRU") - Least-recently used

Both caches are [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") subtypes, designed to be as interchangeable as possible, to facilitate experimentation. A key practice with performance enhancement with caching is ensuring that the caching strategy is working. If the cache is constantly missing, it is just adding more overhead and code complexity. The standard statistics are:

> *   `hit_count` - the number of times the queried key has been in the cache
> 
> *   `miss_count` - the number of times a key has been absent and/or fetched by the cache
> 
> *   `soft_miss_count` - the number of times a key has been absent, but a default has been provided by the caller, as with [`dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get "(in Python v3.14)") and [`dict.setdefault()`](https://docs.python.org/3/library/stdtypes.html#dict.setdefault "(in Python v3.14)"). Soft misses are a subset of misses, so this number is always less than or equal to `miss_count`.

Additionally, `cacheutils` provides [`ThresholdCounter`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter "boltons.cacheutils.ThresholdCounter"), a cache-like bounded counter useful for online statistics collection.

Learn more about [caching algorithms on Wikipedia](https://en.wikipedia.org/wiki/Cache_algorithms#Examples).

Least-Recently Inserted (LRI)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#least-recently-inserted-lri "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------

The [`LRI`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI "boltons.cacheutils.LRI") is the simpler cache, implementing a very simple first-in, first-out (FIFO) approach to cache eviction. If the use case calls for simple, very-low overhead caching, such as somewhat expensive local operations (e.g., string operations), then the LRI is likely the right choice.

_class_ boltons.cacheutils.LRI(_max\_size=128_, _values=None_, _on\_miss=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI "Link to this definition")
The `LRI` implements the basic _Least Recently Inserted_ strategy to caching. One could also think of this as a `SizeLimitedDefaultDict`.

_on\_miss_ is a callable that accepts the missing key (as opposed to [`collections.defaultdict`](https://docs.python.org/3/library/collections.html#collections.defaultdict "(in Python v3.14)")’s “default_factory”, which accepts no arguments.) Also note that, like the [`LRI`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI "boltons.cacheutils.LRI"), the `LRI` is instrumented with statistics tracking.

>>> cap_cache = LRI(max_size=2)
>>> cap_cache['a'], cap_cache['b'] = 'A', 'B'
>>> from pprint import pprint as pp
>>> pp(dict(cap_cache))
{'a': 'A', 'b': 'B'}
>>> [cap_cache['b'] for i in range(3)][0]
'B'
>>> cap_cache['c'] = 'C'
>>> print(cap_cache.get('a'))
None
>>> cap_cache.hit_count, cap_cache.miss_count, cap_cache.soft_miss_count
(3, 1, 1)

clear()→None.Remove all items from D.[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI.clear)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI.clear "Link to this definition")copy()→a shallow copy of D[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI.copy)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI.copy "Link to this definition")get(_key_, _default=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI.get)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI.get "Link to this definition")
Return the value for key if key is in the dictionary, else default.

pop(_k_[, _d_])→v,remove specified key and return the corresponding value.[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI.pop)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI.pop "Link to this definition")
If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI.popitem)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI.popitem "Link to this definition")
Remove and return a (key, value) pair as a 2-tuple.

Pairs are returned in LIFO (last-in, first-out) order. Raises KeyError if the dict is empty.

setdefault(_key_, _default=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI.setdefault)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI.setdefault "Link to this definition")
Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update([_E_, ]_**F_)→None.Update D from dict/iterable E and F.[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRI.update)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI.update "Link to this definition")
If E is present and has a .keys() method, then does: for k in E: D[k] = E[k] If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v In either case, this is followed by: for k in F: D[k] = F[k]

Least-Recently Used (LRU)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#least-recently-used-lru "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The [`LRU`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRU "boltons.cacheutils.LRU") is the more advanced cache, but it’s still quite simple. When it reaches capacity, a new insertion replaces the least-recently used item. This strategy makes the LRU a more effective cache than the LRI for a wide variety of applications, but also entails more operations for all of its APIs, especially reads. Unlike the [`LRI`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI "boltons.cacheutils.LRI"), the LRU has threadsafety built in.

_class_ boltons.cacheutils.LRU(_max\_size=128_, _values=None_, _on\_miss=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#LRU)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRU "Link to this definition")
The `LRU` is [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") subtype implementation of the _Least-Recently Used_ caching strategy.

Parameters:
*   **max_size** ([_int_](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – Max number of items to cache. Defaults to `128`.

*   **values** (_iterable_) – Initial values for the cache. Defaults to `None`.

*   **on_miss** (_callable_) – a callable which accepts a single argument, the key not present in the cache, and returns the value to be cached.

>>> cap_cache = LRU(max_size=2)
>>> cap_cache['a'], cap_cache['b'] = 'A', 'B'
>>> from pprint import pprint as pp
>>> pp(dict(cap_cache))
{'a': 'A', 'b': 'B'}
>>> [cap_cache['b'] for i in range(3)][0]
'B'
>>> cap_cache['c'] = 'C'
>>> print(cap_cache.get('a'))
None

This cache is also instrumented with statistics collection. `hit_count`, `miss_count`, and `soft_miss_count` are all integer members that can be used to introspect the performance of the cache. (“Soft” misses are misses that did not raise [`KeyError`](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)"), e.g., `LRU.get()` or `on_miss` was used to cache a default.

>>> cap_cache.hit_count, cap_cache.miss_count, cap_cache.soft_miss_count
(3, 1, 1)

Other than the size-limiting caching behavior and statistics, `LRU` acts like its parent class, the built-in Python [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)").

Automatic function caching[](https://boltons.readthedocs.io/en/latest/cacheutils.html#automatic-function-caching "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

Continuing in the theme of cache tunability and experimentation, `cacheutils` also offers a pluggable way to cache function return values: the [`cached()`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.cached "boltons.cacheutils.cached") function decorator and the [`cachedmethod()`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.cachedmethod "boltons.cacheutils.cachedmethod") method decorator.

boltons.cacheutils.cached(_cache_, _scoped=True_, _typed=False_, _key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#cached)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.cached "Link to this definition")
Cache any function with the cache object of your choosing. Note that the function wrapped should take only [hashable](https://docs.python.org/2/glossary.html#term-hashable) arguments.

Parameters:
*   **cache** (_Mapping_) – Any [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")-like object suitable for use as a cache. Instances of the [`LRU`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRU "boltons.cacheutils.LRU") and [`LRI`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.LRI "boltons.cacheutils.LRI") are good choices, but a plain [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") can work in some cases, as well. This argument can also be a callable which accepts no arguments and returns a mapping.

*   **scoped** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether the function itself is part of the cache key. `True` by default, different functions will not read one another’s cache entries, but can evict one another’s results. `False` can be useful for certain shared cache use cases. More advanced behavior can be produced through the _key_ argument.

*   **typed** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to factor argument types into the cache check. Default `False`, setting to `True` causes the cache keys for `3` and `3.0` to be considered unequal.

>>> my_cache = LRU()
>>> @cached(my_cache)
... def cached_lower(x):
...     return x.lower()
...
>>> cached_lower("CaChInG's FuN AgAiN!")
"caching's fun again!"
>>> len(my_cache)
1

boltons.cacheutils.cachedmethod(_cache_, _scoped=True_, _typed=False_, _key=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#cachedmethod)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.cachedmethod "Link to this definition")
Similar to [`cached()`](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.cached "boltons.cacheutils.cached"), `cachedmethod` is used to cache methods based on their arguments, using any [`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")-like _cache_ object.

Parameters:
*   **cache** (_str/Mapping/callable_) – Can be the name of an attribute on the instance, any Mapping/[`dict`](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")-like object, or a callable which returns a Mapping.

*   **scoped** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether the method itself and the object it is bound to are part of the cache keys. `True` by default, different methods will not read one another’s cache results. `False` can be useful for certain shared cache use cases. More advanced behavior can be produced through the _key_ arguments.

*   **typed** ([_bool_](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Whether to factor argument types into the cache check. Default `False`, setting to `True` causes the cache keys for `3` and `3.0` to be considered unequal.

*   **key** (_callable_) – A callable with a signature that matches `make_cache_key()` that returns a tuple of hashable values to be used as the key in the cache.

>>> class Lowerer(object):
...     def  __init__ (self):
...         self.cache = LRI()
...
...     @cachedmethod('cache')
...     def lower(self, text):
...         return text.lower()
...
>>> lowerer = Lowerer()
>>> lowerer.lower('WOW WHO COULD GUESS CACHING COULD BE SO NEAT')
'wow who could guess caching could be so neat'
>>> len(lowerer.cache)
1

Similar functionality can be found in Python 3.4’s [`functools.lru_cache()`](https://docs.python.org/3/library/functools.html#functools.lru_cache "(in Python v3.14)") decorator, but the functools approach does not support the same cache strategy modification, nor does it support sharing the cache object across multiple functions.

boltons.cacheutils.cachedproperty(_func_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#cachedproperty)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.cachedproperty "Link to this definition")
The `cachedproperty` is used similar to [`property`](https://docs.python.org/3/library/functions.html#property "(in Python v3.14)"), except that the wrapped method is only called once. This is commonly used to implement lazy attributes.

After the property has been accessed, the value is stored on the instance itself, using the same name as the cachedproperty. This allows the cache to be cleared with [`delattr()`](https://docs.python.org/3/library/functions.html#delattr "(in Python v3.14)"), or through manipulating the object’s `__dict__`.

Threshold-bounded Counting[](https://boltons.readthedocs.io/en/latest/cacheutils.html#threshold-bounded-counting "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

_class_ boltons.cacheutils.ThresholdCounter(_threshold=0.001_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter "Link to this definition")
A **bounded** dict-like Mapping from keys to counts. The ThresholdCounter automatically compacts after every (1 / _threshold_) additions, maintaining exact counts for any keys whose count represents at least a _threshold_ ratio of the total data. In other words, if a particular key is not present in the ThresholdCounter, its count represents less than _threshold_ of the total data.

>>> tc = ThresholdCounter(threshold=0.1)
>>> tc.add(1)
>>> tc.items()
[(1, 1)]
>>> tc.update([2] * 10)
>>> tc.get(1)
0
>>> tc.add(5)
>>> 5 in tc
True
>>> len(list(tc.elements()))
11

As you can see above, the API is kept similar to [`collections.Counter`](https://docs.python.org/3/library/collections.html#collections.Counter "(in Python v3.14)"). The most notable feature omissions being that counted items cannot be set directly, uncounted, or removed, as this would disrupt the math.

Use the ThresholdCounter when you need best-effort long-lived counts for dynamically-keyed data. Without a bounded datastructure such as this one, the dynamic keys often represent a memory leak and can impact application reliability. The ThresholdCounter’s item replacement strategy is fully deterministic and can be thought of as _Amortized Least Relevant_. The absolute upper bound of keys it will store is _(2/threshold)_, but realistically _(1/threshold)_ is expected for uniformly random datastreams, and one or two orders of magnitude better for real-world data.

This algorithm is an implementation of the Lossy Counting algorithm described in “Approximate Frequency Counts over Data Streams” by Manku & Motwani. Hat tip to Kurt Rose for discovery and initial implementation.

add(_key_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.add)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.add "Link to this definition")
Increment the count of _key_ by 1, automatically adding it if it does not exist.

Cache compaction is triggered every _1/threshold_ additions.

elements()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.elements)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.elements "Link to this definition")
Return an iterator of all the common elements tracked by the counter. Yields each key as many times as it has been seen.

get(_key_, _default=0_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.get)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.get "Link to this definition")
Get count for _key_, defaulting to 0.

get_common_count()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.get_common_count)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.get_common_count "Link to this definition")
Get the sum of counts for keys exceeding the configured data threshold.

get_commonality()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.get_commonality)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.get_commonality "Link to this definition")
Get a float representation of the effective count accuracy. The higher the number, the less uniform the keys being added, and the higher accuracy and efficiency of the ThresholdCounter.

If a stronger measure of data cardinality is required, consider using hyperloglog.

get_uncommon_count()[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.get_uncommon_count)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.get_uncommon_count "Link to this definition")
Get the sum of counts for keys that were culled because the associated counts represented less than the configured threshold. The long-tail counts.

most_common(_n=None_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.most_common)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.most_common "Link to this definition")
Get the top _n_ keys and counts as tuples. If _n_ is omitted, returns all the pairs.

update(_iterable_, _**kwargs_)[[source]](https://boltons.readthedocs.io/en/latest/_modules/boltons/cacheutils.html#ThresholdCounter.update)[](https://boltons.readthedocs.io/en/latest/cacheutils.html#boltons.cacheutils.ThresholdCounter.update "Link to this definition")
Like dict.update() but add counts instead of replacing them, used to add multiple items in one call.

Source can be an iterable of keys to add, or a mapping of keys to integer counts.
