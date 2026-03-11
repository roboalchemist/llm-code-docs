# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html

Title: style Utilities - kombu.utils.functional — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.functional.html).

Functional Utilities.

_class_ kombu.utils.functional.LRUCache(_limit=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#LRUCache)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache "Link to this definition")
LRU Cache implementation using a doubly linked list to track access.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#arguments "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

> limit (int): The maximum number of keys to keep in the cache.
> When a new key is inserted and the limit has been exceeded, the _Least Recently Used_ key will be discarded from the cache.

incr(_key_, _delta=1_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#LRUCache.incr)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.incr "Link to this definition")items()→a set-like object providing a view on D's items[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.items "Link to this definition")iteritems()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.iteritems "Link to this definition")iterkeys()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.iterkeys "Link to this definition")itervalues()[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.itervalues "Link to this definition")keys()→a set-like object providing a view on D's keys[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.keys "Link to this definition")popitem()→(k,v),remove and return some(key,value)pair[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#LRUCache.popitem)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.popitem "Link to this definition")
as a 2-tuple; but raise KeyError if D is empty.

update([_E_, ]_**F_)→None.Update D from mapping/iterable E and F.[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#LRUCache.update)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.update "Link to this definition")
If E present and has a .keys() method, does: for k in E: D[k] = E[k] If E present and lacks .keys() method, does: for (k, v) in E: D[k] = v In either case, this is followed by: for k, v in F.items(): D[k] = v

values()→an object providing a view on D's values[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.LRUCache.values "Link to this definition")kombu.utils.functional.dictfilter(_d=None_, _**kw_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#dictfilter)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.dictfilter "Link to this definition")
Remove all keys from dict `d` whose value is `None`.

kombu.utils.functional.is_list(_obj_, _scalars=(<class'collections.abc.Mapping'>_, _<class'str'>)_, _iters=(<class'collections.abc.Iterable'>_, _)_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#is_list)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.is_list "Link to this definition")
Return true if the object is iterable.

Note:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#note "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

> Returns false if object is a mapping or string.

_class_ kombu.utils.functional.lazy(_fun_, _*args_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#lazy)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.lazy "Link to this definition")
Holds lazy evaluation.

Evaluated when called or if the [`evaluate()`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.lazy.evaluate "kombu.utils.functional.lazy.evaluate") method is called. The function is re-evaluated on every call.

Overloaded operations that will evaluate the promise:
`__str__()`, `__repr__()`, `__cmp__()`.

evaluate()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#lazy.evaluate)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.lazy.evaluate "Link to this definition")kombu.utils.functional.maybe_evaluate(_value_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#maybe_evaluate)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.maybe_evaluate "Link to this definition")
Evaluate value only if value is a [`lazy`](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.lazy "kombu.utils.functional.lazy") instance.

kombu.utils.functional.maybe_list(_obj_, _scalars=(<class'collections.abc.Mapping'>_, _<class'str'>)_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#maybe_list)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.maybe_list "Link to this definition")
Return list of one element if `l` is a scalar.

kombu.utils.functional.memoize(_maxsize=None_, _keyfun=None_, _Cache=<class'kombu.utils.functional.LRUCache'>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#memoize)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.memoize "Link to this definition")
Decorator to cache function return value.

kombu.utils.functional.retry_over_time(_fun_, _catch_, _args=None_, _kwargs=None_, _errback=None_, _max\_retries=None_, _interval\_start=2_, _interval\_step=2_, _interval\_max=30_, _callback=None_, _timeout=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/functional.html#retry_over_time)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#kombu.utils.functional.retry_over_time "Link to this definition")
Retry the function over and over until max retries is exceeded.

For each retry we sleep a for a while before we try again, this interval is increased for every retry until the max seconds is reached.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#id1 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

> fun (Callable): The function to try catch (Tuple[BaseException]): Exceptions to catch, can be either
> 
> 
> > tuple or a single exception class.

Keyword Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.functional.html#keyword-arguments "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

> args (Tuple): Positional arguments passed on to the function. kwargs (Dict): Keyword arguments passed on to the function. errback (Callable): Callback for when an exception in `catch`
> 
> 
> > is raised. The callback must take three arguments: `exc`, `interval_range` and `retries`, where `exc` is the exception instance, `interval_range` is an iterator which return the time in seconds to sleep next, and `retries` is the number of previous retries.
> 
> max_retries (int): Maximum number of retries before we give up.
> If neither of this and timeout is set, we will retry forever. If one of this and timeout is reached, stop.
> 
> interval_start (float): How long (in seconds) we start sleeping
> between retries.
> 
> interval_step (float): By how much the interval is increased for
> each retry.
> 
> interval_max (float): Maximum number of seconds to sleep
> between retries.
> 
> 
> timeout (int): Maximum seconds waiting before we give up.
