# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html

Title: kombu.utils.scheduling — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html

Published Time: Mon, 29 Dec 2025 20:31:32 GMT

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.utils.scheduling.html).

Scheduling Utilities.

_class_ kombu.utils.scheduling.FairCycle(_fun_, _resources_, _predicate=<class'Exception'>_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#FairCycle)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.FairCycle "Link to this definition")
Cycle between resources.

Consume from a set of resources, where each resource gets an equal chance to be consumed from.

Arguments:[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#arguments "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

> fun (Callable): Callback to call. resources (Sequence[Any]): List of resources. predicate (type): Exception predicate.

close()[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#FairCycle.close)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.FairCycle.close "Link to this definition")
Close cycle.

get(_callback_, _**kwargs_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#FairCycle.get)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.FairCycle.get "Link to this definition")
Get from next resource.

_class_ kombu.utils.scheduling.priority_cycle(_it=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#priority_cycle)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.priority_cycle "Link to this definition")
Cycle that repeats items in order.

rotate(_last\_used_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#priority_cycle.rotate)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.priority_cycle.rotate "Link to this definition")
Unused in this implementation.

_class_ kombu.utils.scheduling.round_robin_cycle(_it=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#round_robin_cycle)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.round_robin_cycle "Link to this definition")
Iterator that cycles between items in round-robin.

consume(_n_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#round_robin_cycle.consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.round_robin_cycle.consume "Link to this definition")
Consume n items.

rotate(_last\_used_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#round_robin_cycle.rotate)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.round_robin_cycle.rotate "Link to this definition")
Move most recently used item to end of list.

update(_it_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#round_robin_cycle.update)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.round_robin_cycle.update "Link to this definition")
Update items from iterable.

_class_ kombu.utils.scheduling.sorted_cycle(_it=None_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#sorted_cycle)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.sorted_cycle "Link to this definition")
Cycle in sorted order.

consume(_n_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/utils/scheduling.html#sorted_cycle.consume)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.utils.scheduling.html#kombu.utils.scheduling.sorted_cycle.consume "Link to this definition")
Consume n items.
