# Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html

Title: Event Loop Debugging Utils - kombu.asynchronous.debug — Kombu 5.6.2 documentation

URL Source: https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html

Markdown Content:
This document is for Kombu's development version, which can be significantly different from previous releases. Get the stable docs here: [5.3](https://kombu.readthedocs.io/en/latest/reference/kombu.asynchronous.debug.html).

Event-loop debugging tools.

kombu.asynchronous.debug.callback_for(_h_, _fd_, _flag_, _*default_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/debug.html#callback_for)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html#kombu.asynchronous.debug.callback_for "Link to this definition")
Return the callback used for hub+fd+flag.

kombu.asynchronous.debug.repr_active(_h_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/debug.html#repr_active)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html#kombu.asynchronous.debug.repr_active "Link to this definition")
Return description of active readers and writers.

kombu.asynchronous.debug.repr_events(_h_, _events_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/debug.html#repr_events)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html#kombu.asynchronous.debug.repr_events "Link to this definition")
Return description of events returned by poll.

kombu.asynchronous.debug.repr_flag(_flag_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/debug.html#repr_flag)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html#kombu.asynchronous.debug.repr_flag "Link to this definition")
Return description of event loop flag.

kombu.asynchronous.debug.repr_readers(_h_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/debug.html#repr_readers)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html#kombu.asynchronous.debug.repr_readers "Link to this definition")
Return description of pending readers.

kombu.asynchronous.debug.repr_writers(_h_)[[source]](https://docs.celeryq.dev/projects/kombu/en/stable/_modules/kombu/asynchronous/debug.html#repr_writers)[¶](https://docs.celeryq.dev/projects/kombu/en/stable/reference/kombu.asynchronous.debug.html#kombu.asynchronous.debug.repr_writers "Link to this definition")
Return description of pending writers.
