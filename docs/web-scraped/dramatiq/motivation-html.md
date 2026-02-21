# Source: https://dramatiq.io/motivation.html

Title: Motivation — Dramatiq 2.0.1 documentation

URL Source: https://dramatiq.io/motivation.html

Markdown Content:
Dramatiq’s primary reason for being is the fact that I wanted a distributed task queueing library that is simple and has sane defaults for most SaaS workloads. In that sense, it draws a lot of inspiration from [GAE Push Queues](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/) and [Sidekiq](http://sidekiq.org/).

Dramatiq’s driving principles are as follows:

*   high reliability and performance

*   simple and easy to understand core

*   convention over configuration

If you’ve ever had to use Celery in anger, Dramatiq could be the tool for you.

Compared to *[¶](https://dramatiq.io/motivation.html#compared-to "Link to this heading")
----------------------------------------------------------------------------------------

Note

This section was last updated in 2019. It’s possible that various bits of the table below are now outdated. Clarifications in PR form are always welcome!

I’ve used [Celery](http://celeryproject.org/) professionally for years and my growing frustration with it is one of the reasons why I developed dramatiq. Here are some of the main differences between Dramatiq, Celery, Huey and RQ:

Dramatiq[Celery](http://celeryproject.org/)[Huey](https://huey.readthedocs.io/)[RQ](http://python-rq.org/)
Python 2 support No Yes Yes Yes
Windows support Yes No Yes No
Simple implementation Yes No [[3]](https://dramatiq.io/motivation.html#sim)Yes Yes
Automatic retries Yes No Yes No
Reliable delivery Yes Optional [[1]](https://dramatiq.io/motivation.html#id7)No No
Locks and rate limiting Yes No Yes No
Task prioritization Yes [[4]](https://dramatiq.io/motivation.html#prio)No [[4]](https://dramatiq.io/motivation.html#prio)Yes Yes
Delayed tasks Yes Yes [[2]](https://dramatiq.io/motivation.html#id8)Yes No
Cronlike scheduling No [[5]](https://dramatiq.io/motivation.html#cron)Yes Yes No
Chaining / Pipelining Yes Yes Yes No
Result storage Yes Yes Yes Yes
Code auto-reload Yes No No No
RabbitMQ support Yes Yes Yes No
Redis support Yes Yes Yes Yes
In-memory broker support Yes No Yes No
Greenlet support Yes Yes Yes No
