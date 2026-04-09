# Source: https://dramatiq.io/changelog.html

Title: Changelog — Dramatiq 2.0.1 documentation

URL Source: https://dramatiq.io/changelog.html

Markdown Content:
All notable changes to this project will be documented in this file.

[Unreleased](https://github.com/Bogdanp/dramatiq/compare/v2.0.1...HEAD)[¶](https://dramatiq.io/changelog.html#unreleased "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

[2.0.1](https://github.com/Bogdanp/dramatiq/compare/v2.0.0...v2.0.1) – 2026-01-12[¶](https://dramatiq.io/changelog.html#id1 "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#fixed "Link to this heading")

*   Fixed infinite loop when an async actor function raises a `TimeoutError`. ([#791](https://github.com/Bogdanp/dramatiq/issues/791), [#801](https://github.com/Bogdanp/dramatiq/pull/801), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   Fixed the [`group`](https://dramatiq.io/reference.html#dramatiq.group "dramatiq.group")`completed_count` property to return the correct value, regardless of what order the tasks in the group finish. ([#452](https://github.com/Bogdanp/dramatiq/issues/452), [#814](https://github.com/Bogdanp/dramatiq/pull/814), [@ABolouk](https://github.com/ABolouk))

*   Fixed type hints of [`actor`](https://dramatiq.io/reference.html#dramatiq.actor "dramatiq.actor") decorator. ([#795](https://github.com/Bogdanp/dramatiq/issues/795), [#796](https://github.com/Bogdanp/dramatiq/pull/796), [@janek-cosmose](https://github.com/janek-cosmose), [#804](https://github.com/Bogdanp/dramatiq/pull/804), [@LincolnPuzey](https://github.com/LincolnPuzey))

### Documentation[¶](https://dramatiq.io/changelog.html#documentation "Link to this heading")

*   Fixed Installation page so it lists all installable extras. ([#797](https://github.com/Bogdanp/dramatiq/issues/797), [#808](https://github.com/Bogdanp/dramatiq/pull/808), [@synweap15](https://github.com/synweap15))

[2.0.0](https://github.com/Bogdanp/dramatiq/compare/v1.18.0...v2.0.0) – 2025-11-18[¶](https://dramatiq.io/changelog.html#id11 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Breaking Changes[¶](https://dramatiq.io/changelog.html#breaking-changes "Link to this heading")

#### Major Breaking Changes[¶](https://dramatiq.io/changelog.html#major-breaking-changes "Link to this heading")

These are breaking changes we believe are most likely to effect your project.

*   The `fail_fast` argument to [`StubBroker.join`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker.join "dramatiq.brokers.stub.StubBroker.join") now defaults to True. This means that calling [`StubBroker.join`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker.join "dramatiq.brokers.stub.StubBroker.join"), will by default, re-raise any Exceptions that caused messages to get dead-lettered (i.e. any uncaught Exceptions in your actor functions). You may need to explicitly catch these exception in your tests (e.g. with [`unittest.TestCase.assertRaises()`](https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertRaises "(in Python v3.14)") or [`pytest.raises()`](https://docs.pytest.org/en/stable/reference/reference.html#pytest.raises "(in pytest v9.0.2)")).

Alternatively, you can revert to the old behavior by passing `fail_fast_default=False` to [`StubBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker "dramatiq.brokers.stub.StubBroker").

However, we think the new default behavior is best, because it makes exceptions happening in your actor functions obvious in your tests. Previsouly, exceptions in your actor functions could pass silently, and potentially unnoticed unless you checked the side-effects of the actor. ([#739](https://github.com/Bogdanp/dramatiq/issues/739), [#758](https://github.com/Bogdanp/dramatiq/pull/758), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   The [`Prometheus`](https://dramatiq.io/reference.html#dramatiq.middleware.prometheus.Prometheus "dramatiq.middleware.prometheus.Prometheus") middleware is no longer in the default middleware list. To keep exporting the Prometheus statistics, you must now install the `prometheus` extra (e.g. `pip install 'dramatiq[prometheus]'`) and add the [`Prometheus`](https://dramatiq.io/reference.html#dramatiq.middleware.prometheus.Prometheus "dramatiq.middleware.prometheus.Prometheus") middleware (see [Customizing Middleware](https://dramatiq.io/advanced.html#customizing-middleware)). If you are not using the Promotheus statistics, no action is needed. ([#95](https://github.com/Bogdanp/dramatiq/issues/95), [#345](https://github.com/Bogdanp/dramatiq/issues/345), [#688](https://github.com/Bogdanp/dramatiq/pull/688), [@azmeuk](https://github.com/azmeuk))

*   The `backend` argument to the [`Results`](https://dramatiq.io/reference.html#dramatiq.results.Results "dramatiq.results.Results") middleware is now required. Previously, not supplying this argument would result in a non-functional [`Results`](https://dramatiq.io/reference.html#dramatiq.results.Results "dramatiq.results.Results") middleware. ([#728](https://github.com/Bogdanp/dramatiq/pull/728), [@LincolnPuzey](https://github.com/LincolnPuzey))

#### Minor Breaking Changes[¶](https://dramatiq.io/changelog.html#minor-breaking-changes "Link to this heading")

These are changes that while technically breaking, we believe are unlikely to effect your project.

*   Removed `URLRabbitmqBroker`. This has been deprecated since version 1.1.0. Use [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker") with `url` as a keyword argument instead. ([#786](https://github.com/Bogdanp/dramatiq/pull/786), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   Removed the `dev` installable extra from the project metadata. Instead the development dependencies are defined in a [PEP-735](https://peps.python.org/pep-0735/)`[dependency-groups]` table in `pyproject.toml`. These can be installed in development environments with `pip install --group dev`. ([#766](https://github.com/Bogdanp/dramatiq/pull/766), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   The `keys` argument to `RateLimiterBackend.incr_and_sum` must now be a callable that returns a list of keys. This is only relevant if you have written custom code (such as a custom Rate Limiter) that uses a `RateLimiterBackend`. ([#741](https://github.com/Bogdanp/dramatiq/issues/741), [#772](https://github.com/Bogdanp/dramatiq/pull/772), [@mikeroll](https://github.com/mikeroll))

*   The deprecated `requeue_deadline` and `requeue_interval` arguments of [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker") have been removed. These have been deprecated and have had no effect since version 1.2.0. ([#782](https://github.com/Bogdanp/dramatiq/pull/782), [@mikeroll](https://github.com/mikeroll))

*   [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker"): The code for compatibility with pre-v1.2.0 acks has been removed. If you are using the [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker"), you must first upgrade Dramatiq to a version >=1.2.0, <2.0.0, and run it for some time, before upgrading to a version >=2.0.0. This is to allow Dramatiq to migrate the pre-v1.2.0 ack data structures in redis to the v1.2.0+ versions. This migration code is what has been removed in version 2.0.0. ([#771](https://github.com/Bogdanp/dramatiq/pull/771), [@mikeroll](https://github.com/mikeroll))

### Fixed[¶](https://dramatiq.io/changelog.html#id24 "Link to this heading")

*   Fixed the way that backoff time is calculated for retries so that the first backoff is not less than `min_backoff`. This means that each retry backoff is now, on average, twice as long. To avoid this effect, you can halve your `min_backoff` (which should now be correctly observed). ([#651](https://github.com/Bogdanp/dramatiq/issues/651), [#721](https://github.com/Bogdanp/dramatiq/pull/721), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   Fixed the RabbitMQ broker making 1 more retry than configured when declaring queues or enqueueing messages fail due to connection errors. 1 fewer retries are now made. This fixes a regression introduced by [#669](https://github.com/Bogdanp/dramatiq/pull/669) released in `1.18.0`. ([#734](https://github.com/Bogdanp/dramatiq/pull/734), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   When adding middleware to a Broker that already has actors declared, call the `after_declare_actor` middleware hook with the correct argument. ([#743](https://github.com/Bogdanp/dramatiq/pull/743), [@jenstroeger](https://github.com/jenstroeger))

*   Made dramatiq robust against non-numeric values for the `eta` option. This should only be necessary when manually enqueuing messages. ([#759](https://github.com/Bogdanp/dramatiq/issues/759), [#761](https://github.com/Bogdanp/dramatiq/pull/761), [@gurelkaynak](https://github.com/gurelkaynak))

*   Fixed edge case where the [`StubBroker.join`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker.join "dramatiq.brokers.stub.StubBroker.join") would try to raise `None` as an exception. ([#763](https://github.com/Bogdanp/dramatiq/pull/763), [@LincolnPuzey](https://github.com/LincolnPuzey))

### Added[¶](https://dramatiq.io/changelog.html#added "Link to this heading")

*   Add Python 3.14 to test matrix and project classifiers. ([#751](https://github.com/Bogdanp/dramatiq/pull/751), [@LincolnPuzey](https://github.com/LincolnPuzey)) Things to be aware of when upgrading to Python 3.14:

    *   Python 3.14 [changes](https://docs.python.org/3.14/whatsnew/3.14.html#whatsnew314-multiprocessing-start-method) the default multiprocessing [start method](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods) to [forkserver](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-forkserver) on some platforms. Dramatiq Workers use multiprocessing and will be effected by this change. `forkserver` should be less bug-prone than the old default `fork`. However, if you run into weird issues, using the existing `--use-spawn` flag when starting Dramatiq to set the start method to `spawn`, might solve them.

    *   The free-threaded build of Python is now [officially supported](https://docs.python.org/3.14/whatsnew/3.14.html#free-threaded-python-is-officially-supported) by Python. Dramatiq is not yet unit-tested with free-threaded Python, but we hope to do so soon. In the meantime, if you have any success or problems running Dramatiq with free-threaded Python, we would love to hear about it.

*   Added type annotations for the external API of the [`Worker`](https://dramatiq.io/reference.html#dramatiq.Worker "dramatiq.Worker") and [`Broker`](https://dramatiq.io/reference.html#dramatiq.Broker "dramatiq.Broker") classes. ([#727](https://github.com/Bogdanp/dramatiq/issues/727), [#731](https://github.com/Bogdanp/dramatiq/pull/731), [#744](https://github.com/Bogdanp/dramatiq/pull/744), [@jenstroeger](https://github.com/jenstroeger))

*   Added type annotations for the external API of the [`Middleware`](https://dramatiq.io/reference.html#dramatiq.Middleware "dramatiq.Middleware") class and its subclasses. ([#521](https://github.com/Bogdanp/dramatiq/issues/521), [#735](https://github.com/Bogdanp/dramatiq/pull/735), [@jenstroeger](https://github.com/jenstroeger))

*   Added `message_datetime` property to the `Message` class to retrieve `message_timestamp` as an aware `datetime.datetime` instance. ([#736](https://github.com/Bogdanp/dramatiq/pull/736), [@karolinepauls](https://github.com/karolinepauls))

*   Added `dramatiq_worker_timeout` environment variable. ([#773](https://github.com/Bogdanp/dramatiq/pull/773), [@ksoviero-zengrc](https://github.com/ksoviero-zengrc))

### Changed[¶](https://dramatiq.io/changelog.html#changed "Link to this heading")

*   Promoted `ConsumerThread` and `WorkerThread` classes to public names, since they are used in the [`Middleware`](https://dramatiq.io/reference.html#dramatiq.Middleware "dramatiq.Middleware") interface type hints. The previous names `_ConsumerThread` and `_WorkerThread` are still available for backwards compatibility. ([#760](https://github.com/Bogdanp/dramatiq/pull/760), [@synweap15](https://github.com/synweap15))

*   Increased the minimum `redis-py` library version to `4.0.0`. ([#738](https://github.com/Bogdanp/dramatiq/issues/738), [#764](https://github.com/Bogdanp/dramatiq/pull/764), [@LincolnPuzey](https://github.com/LincolnPuzey))

### Removed[¶](https://dramatiq.io/changelog.html#removed "Link to this heading")

*   Removed support for Python 3.9. ([#784](https://github.com/Bogdanp/dramatiq/pull/784), [@LincolnPuzey](https://github.com/LincolnPuzey))

### Packaging[¶](https://dramatiq.io/changelog.html#packaging "Link to this heading")

*   The project now defines a PEP-518 build backend in the `pyproject.toml` file. ([#750](https://github.com/Bogdanp/dramatiq/pull/750), [@LincolnPuzey](https://github.com/LincolnPuzey))

### Documentation[¶](https://dramatiq.io/changelog.html#id45 "Link to this heading")

*   Improved documentation relating to middleware. ([#718](https://github.com/Bogdanp/dramatiq/pull/718), [@LincolnPuzey](https://github.com/LincolnPuzey), [#723](https://github.com/Bogdanp/dramatiq/pull/723), [@karolinepauls](https://github.com/karolinepauls))

*   Add documentation section about asyncio support. ([#595](https://github.com/Bogdanp/dramatiq/issues/595), [#719](https://github.com/Bogdanp/dramatiq/pull/719), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   Improved documentation about prioritizing messages with the `priority` argument of an [`actor`](https://dramatiq.io/reference.html#dramatiq.actor "dramatiq.actor"). ([#724](https://github.com/Bogdanp/dramatiq/issues/724), [#725](https://github.com/Bogdanp/dramatiq/pull/725), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   Add documentation section about environment variables. ([#720](https://github.com/Bogdanp/dramatiq/pull/720), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   Improve documentation for `before_enqueue` and `after_enqueue`[`Middleware`](https://dramatiq.io/reference.html#dramatiq.Middleware "dramatiq.Middleware") hooks. ([#753](https://github.com/Bogdanp/dramatiq/pull/753), [@karolinepauls](https://github.com/karolinepauls))

[1.18.0](https://github.com/Bogdanp/dramatiq/compare/v1.17.1...v1.18.0) – 2025-05-29[¶](https://dramatiq.io/changelog.html#id54 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id55 "Link to this heading")

*   Correct typing on signal handler. ([#664](https://github.com/Bogdanp/dramatiq/pull/664), [@igor47](https://github.com/igor47))

*   Make sure RabbitMQ Broker enqueue() attempts the correct number of preset retries. ([#668](https://github.com/Bogdanp/dramatiq/issues/668), [#669](https://github.com/Bogdanp/dramatiq/pull/669), [@jenstoeger](https://github.com/jenstoeger))

*   Fix `Message` Result type variable to be covariant. ([#685](https://github.com/Bogdanp/dramatiq/pull/685), [@alecbarber](https://github.com/alecbarber))

*   Fix flushing of RabbitMQ queues. ([#687](https://github.com/Bogdanp/dramatiq/pull/687), [@olii](https://github.com/olii))

*   Fixed unexpected restarts when using `--watch` option. ([#654](https://github.com/Bogdanp/dramatiq/issues/654), [#696](https://github.com/Bogdanp/dramatiq/pull/696), [@LincolnPuzey](https://github.com/LincolnPuzey))

*   Fixed using actor decorator in the interactive shell. ([#694](https://github.com/Bogdanp/dramatiq/issues/694), [#695](https://github.com/Bogdanp/dramatiq/pull/695), [@bartvanandel](https://github.com/bartvanandel))

*   Fix `join_queue` (and `StubBroker`) compatibility with gevent 25.4.1. ([#699](https://github.com/Bogdanp/dramatiq/pull/699), [@synweap15](https://github.com/synweap15))

*   Close write_pipe after forking to fix hangs on Worker shutdown. ([#693](https://github.com/Bogdanp/dramatiq/issues/693), [#707](https://github.com/Bogdanp/dramatiq/pull/707), [@dansimko](https://github.com/dansimko))

### Added[¶](https://dramatiq.io/changelog.html#id68 "Link to this heading")

*   Add repr to `MessageProxy` class. ([#690](https://github.com/Bogdanp/dramatiq/pull/690), [@karolinepauls](https://github.com/karolinepauls))

*   Add `--worker-fork-timeout` command-line argument to configure time to wait for the worker processes to come online after forking. ([#706](https://github.com/Bogdanp/dramatiq/pull/706), [@guedesfelipe](https://github.com/guedesfelipe))

*   Log a warning when added a duplicate middleware class, since this can lead to unexpected behavior. ([#709](https://github.com/Bogdanp/dramatiq/pull/709), [@synweap15](https://github.com/synweap15))

### Changed[¶](https://dramatiq.io/changelog.html#id72 "Link to this heading")

*   Extend version limit on `redis-py` to version 6.X. ([#711](https://github.com/Bogdanp/dramatiq/pull/711), [@dbowring](https://github.com/dbowring))

### Removed[¶](https://dramatiq.io/changelog.html#id74 "Link to this heading")

*   Remove support for end-of-life Python 3.8. ([#662](https://github.com/Bogdanp/dramatiq/pull/662), [@amureki](https://github.com/amureki))

### Documentation[¶](https://dramatiq.io/changelog.html#id76 "Link to this heading")

*   Add Podcatcher sponsor.

*   Add link to `dramatiq-workflow`. ([#667](https://github.com/Bogdanp/dramatiq/pull/667), [@pencil](https://github.com/pencil))

*   Update Sentry docs to reference `sentry-sdk`. ([#675](https://github.com/Bogdanp/dramatiq/pull/675), [@DHUKK](https://github.com/DHUKK))

[1.17.1](https://github.com/Bogdanp/dramatiq/compare/v1.17.0...v1.17.1) – 2024-10-26[¶](https://dramatiq.io/changelog.html#id79 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id80 "Link to this heading")

*   TimeLimit middleware support for Python 3.13. ([#656](https://github.com/Bogdanp/dramatiq/issues/656), [#659](https://github.com/Bogdanp/dramatiq/pull/659), [@amureki](https://github.com/amureki))

### Added[¶](https://dramatiq.io/changelog.html#id83 "Link to this heading")

*   The Retries middleware now supports an `on_retries_exhausted` target actor to execute when retries on a message have been exhausted. ([#630](https://github.com/Bogdanp/dramatiq/pull/630), [@dbowring](https://github.com/dbowring))

### Changed[¶](https://dramatiq.io/changelog.html#id85 "Link to this heading")

*   The actor decorator now checks for duplicate actor names. ([#640](https://github.com/Bogdanp/dramatiq/issues/640), [#641](https://github.com/Bogdanp/dramatiq/pull/641), [@z0z0r4](https://github.com/z0z0r4))

*   The Retries middleware now tracks when a message was last requeued on retry. ([#629](https://github.com/Bogdanp/dramatiq/pull/629), [@kuba-lilz](https://github.com/kuba-lilz))

[1.17.0](https://github.com/Bogdanp/dramatiq/compare/v1.16.0...v1.17.0) – 2024-05-09[¶](https://dramatiq.io/changelog.html#id89 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id90 "Link to this heading")

*   Middleware hooks for after consumer & worker thread boot. ([#619](https://github.com/Bogdanp/dramatiq/pull/619), [@kamalmarhubi](https://github.com/kamalmarhubi))

*   Type hints for awaitable actors. ([#621](https://github.com/Bogdanp/dramatiq/pull/621), [@DABND19](https://github.com/DABND19))

### Changed[¶](https://dramatiq.io/changelog.html#id93 "Link to this heading")

*   The =watch= extras now require Watchdog version 4.0+.

### Fixed[¶](https://dramatiq.io/changelog.html#id94 "Link to this heading")

*   The `python_requires` version in `setup.py`. ([#606](https://github.com/Bogdanp/dramatiq/pull/606), [@niccodemus](https://github.com/nicoddemus))

*   The result middleware now takes message options into account. ([#612](https://github.com/Bogdanp/dramatiq/pull/612), [@huwylphimet](https://github.com/huwylphimet))

[1.16.0](https://github.com/Bogdanp/dramatiq/compare/v1.15.0...v1.16.0) – 2024-01-25[¶](https://dramatiq.io/changelog.html#id97 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id98 "Link to this heading")

*   The `CurrentMessage` middleware now works under AsyncIO. ([#586](https://github.com/Bogdanp/dramatiq/issues/586), [#593](https://github.com/Bogdanp/dramatiq/pull/593), [@pahrohfit](https://github.com/pahrohfit))

*   Improved logging behavior under different buffer modes. ([#596](https://github.com/Bogdanp/dramatiq/pull/596), [@5tefan](https://github.com/5tefan))

### Added[¶](https://dramatiq.io/changelog.html#id102 "Link to this heading")

*   CLI watcher now supports setting include and exclude patterns ([#594](https://github.com/Bogdanp/dramatiq/issues/594), [@nhairs](https://github.com/nhairs))

[1.15.0](https://github.com/Bogdanp/dramatiq/compare/v1.14.2...v1.15.0) – 2023-10-23[¶](https://dramatiq.io/changelog.html#id104 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id105 "Link to this heading")

*   The `global_broker` variable is now type hinted. ([@jenstroeger](https://github.com/jenstroeger))

*   Pipeline result retrieval works with non-default brokers. ([#563](https://github.com/Bogdanp/dramatiq/pull/563), [#564](https://github.com/Bogdanp/dramatiq/issues/564), [@DiegoPomares](https://github.com/DiegoPomares))

### Added[¶](https://dramatiq.io/changelog.html#id108 "Link to this heading")

*   Asyncio support. ([#536](https://github.com/Bogdanp/dramatiq/pull/536), [@caspervdw](https://github.com/caspervdw))

*   Timedelta support for delay arguments. ([#569](https://github.com/Bogdanp/dramatiq/pull/569), [@h3nnn4n](https://github.com/h3nnn4n))

### Changed[¶](https://dramatiq.io/changelog.html#id111 "Link to this heading")

*   Filesystem watcher no longer reloads dramatiq on file open events. ([#552](https://github.com/Bogdanp/dramatiq/pull/552), [@seanpile](https://github.com/seanpile))

*   The version bound on `redis-py` has been increased to include version 5.0. ([#567](https://github.com/Bogdanp/dramatiq/pull/567), [@scott-8](https://github.com/scott-8))

[1.14.2](https://github.com/Bogdanp/dramatiq/compare/v1.14.1...v1.14.2) – 2023-03-25[¶](https://dramatiq.io/changelog.html#id114 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id115 "Link to this heading")

*   Restored `namedtuple` instance methods on `Message`. ([#538](https://github.com/Bogdanp/dramatiq/pull/538))

[1.14.1](https://github.com/Bogdanp/dramatiq/compare/v1.14.0...v1.14.1) – 2023-02-25[¶](https://dramatiq.io/changelog.html#id117 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id118 "Link to this heading")

*   Added missing `py.typed` file to distributions. ([#531](https://github.com/Bogdanp/dramatiq/pull/531))

[1.14.0](https://github.com/Bogdanp/dramatiq/compare/v1.13.0...v1.14.0) – 2023-02-05[¶](https://dramatiq.io/changelog.html#id120 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Removed[¶](https://dramatiq.io/changelog.html#id121 "Link to this heading")

*   Dropped Python 3.6 support as it reached end-of-life

### Changed[¶](https://dramatiq.io/changelog.html#id122 "Link to this heading")

*   Added Python 3.11 support to CI builds. ([#511](https://github.com/Bogdanp/dramatiq/pull/511), [@FinnLidbetter](https://github.com/FinnLidbetter))

*   Improved typing support. `Message` is now a dataclass, but it should be compatible with the previous namedtuple-based implementation. ([#512](https://github.com/Bogdanp/dramatiq/pull/512), [#513](https://github.com/Bogdanp/dramatiq/pull/513), [#515](https://github.com/Bogdanp/dramatiq/pull/515), [#516](https://github.com/Bogdanp/dramatiq/pull/516), [@orsinium](https://github.com/orsinium))

[1.13.0](https://github.com/Bogdanp/dramatiq/compare/v1.12.3...v1.13.0) – 2022-04-02[¶](https://dramatiq.io/changelog.html#id130 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id131 "Link to this heading")

*   A race condition in the Redis broker’s `join` method. ([#480](https://github.com/Bogdanp/dramatiq/issues/480), [#481](https://github.com/Bogdanp/dramatiq/pull/481), [@CaselIT](https://github.com/CaselIT))

*   Skipped messages and messages failed due to [`AgeLimit`](https://dramatiq.io/reference.html#dramatiq.middleware.AgeLimit "dramatiq.middleware.AgeLimit") now store results more consistently. ([#440](https://github.com/Bogdanp/dramatiq/issues/440), [#449](https://github.com/Bogdanp/dramatiq/pull/449), [@FinnLidbetter](https://github.com/FinnLidbetter))

### Changed[¶](https://dramatiq.io/changelog.html#id136 "Link to this heading")

*   Typing support has been improved. ([#482](https://github.com/Bogdanp/dramatiq/issues/482), [@staticdev](https://github.com/staticdev))

*   The default broker now falls back to Redis if the RabbitMQ extras are not installed, in an attempt to make the getting started process easier. ([#483](https://github.com/Bogdanp/dramatiq/issues/483), [#486](https://github.com/Bogdanp/dramatiq/pull/486), [@kurtmckee](https://github.com/kurtmckee))

[1.12.3](https://github.com/Bogdanp/dramatiq/compare/v1.12.2...v1.12.3) – 2022-01-16[¶](https://dramatiq.io/changelog.html#id140 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id141 "Link to this heading")

*   An issue where signals remained blocked after worker process boot. ([#465](https://github.com/Bogdanp/dramatiq/issues/465), [#466](https://github.com/Bogdanp/dramatiq/pull/466), [@FinnLidbetter](https://github.com/FinnLidbetter))

[1.12.2](https://github.com/Bogdanp/dramatiq/compare/v1.12.1...v1.12.2) – 2022-01-14[¶](https://dramatiq.io/changelog.html#id144 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id145 "Link to this heading")

*   An issue where stopping the process too quickly after boot could lead to an `AttributeError`. ([#463](https://github.com/Bogdanp/dramatiq/issues/463), [#464](https://github.com/Bogdanp/dramatiq/pull/464), [@FinnLidbetter](https://github.com/FinnLidbetter))

[1.12.1](https://github.com/Bogdanp/dramatiq/compare/v1.12.0...v1.12.1) – 2021-12-19[¶](https://dramatiq.io/changelog.html#id148 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id149 "Link to this heading")

*   Actors and messages can now specify 0 backoff. ([@FinnLidbetter](https://github.com/FinnLidbetter), [#438](https://github.com/Bogdanp/dramatiq/pull/438))

*   An issue where Redis message ids could be put back onto the queue after ack/nack. ([#442](https://github.com/Bogdanp/dramatiq/issues/442), [#444](https://github.com/Bogdanp/dramatiq/pull/444))

### Removed[¶](https://dramatiq.io/changelog.html#id153 "Link to this heading")

*   Dropped Python 3.5 support as it reached end-of-life

[1.12.0](https://github.com/Bogdanp/dramatiq/compare/v1.11.0...v1.12.0) – 2021-10-23[¶](https://dramatiq.io/changelog.html#id154 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id155 "Link to this heading")

*   RabbitMQ messages now have a `redelivered` flag. ([#405](https://github.com/Bogdanp/dramatiq/pull/405), [@nffdiogosilva](https://github.com/nffdiogosilva))

*   Time limits now work under gevent. ([#408](https://github.com/Bogdanp/dramatiq/pull/408), [@FinnLidbetter](https://github.com/FinnLidbetter))

*   Shutdown notifications now work under gevent. ([#426](https://github.com/Bogdanp/dramatiq/pull/426), [@FinnLidbetter](https://github.com/FinnLidbetter))

### Changed[¶](https://dramatiq.io/changelog.html#id159 "Link to this heading")

*   The `watchdog` library is no longer being pinned to a specific version. ([#428](https://github.com/Bogdanp/dramatiq/pull/428))

*   The redis broker now limits unpacks to half the size of the Lua stack. ([#433](https://github.com/Bogdanp/dramatiq/issues/433), [#434](https://github.com/Bogdanp/dramatiq/pull/434), [@ethervoid](https://github.com/ethervoid))

### Fixed[¶](https://dramatiq.io/changelog.html#id163 "Link to this heading")

*   Async exceptions now correctly set the thread id on Python 3.7 and up. ([#419](https://github.com/Bogdanp/dramatiq/pull/419), [#420](https://github.com/Bogdanp/dramatiq/pull/420), [@FinnLidbetter](https://github.com/FinnLidbetter))

[1.11.0](https://github.com/Bogdanp/dramatiq/compare/v1.10.0...v1.11.0) – 2021-05-22[¶](https://dramatiq.io/changelog.html#id167 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id168 "Link to this heading")

*   [`decode`](https://dramatiq.io/reference.html#dramatiq.Message.decode "dramatiq.Message.decode") now raises a new error, [`DecodeError`](https://dramatiq.io/reference.html#dramatiq.DecodeError "dramatiq.DecodeError"), on exception. ([#375](https://github.com/Bogdanp/dramatiq/pull/375), [@thomazthz](https://github.com/thomazthz))

### Changed[¶](https://dramatiq.io/changelog.html#id169 "Link to this heading")

*   The RabbitMQ broker moves messages that fail to decode to the DLQ. ([#375](https://github.com/Bogdanp/dramatiq/pull/375), [@thomazthz](https://github.com/thomazthz))

### Fixed[¶](https://dramatiq.io/changelog.html#id171 "Link to this heading")

*   The Redis broker is now more defensive in how it handles re-enqueueing messages. This should fix a potential race condition where a worker could hit its heartbeat timeout but still end up re-enqueueing messages (thus ending up with the same message id enqueued multiple times). ([#266](https://github.com/Bogdanp/dramatiq/issues/266), [#395](https://github.com/Bogdanp/dramatiq/pull/395))

*   A code path that could lead to an unbound variable error has now been fixed. ([#382](https://github.com/Bogdanp/dramatiq/issue/382))

*   Deleting the connection off of a `RabbitMQ` broker now correctly closes it and its associated channel (if any) before removing it from the broker. ([#381](https://github.com/Bogdanp/dramatiq/issue/381), [#384](https://github.com/Bogdanp/dramatiq/issue/384))

[1.10.0](https://github.com/Bogdanp/dramatiq/compare/v1.9.0...v1.10.0) – 2020-12-21[¶](https://dramatiq.io/changelog.html#id177 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id178 "Link to this heading")

*   The RabbitMQ broker dead message TTL can now be configured via the `dramatiq_dead_message_ttl` environment variable. ([#354](https://github.com/Bogdanp/dramatiq/pull/354), [@evstratbg](https://github.com/evstratbg))

*   The CLI now supports referencing a callable to set up the broker on worker startup. ([#350](https://github.com/Bogdanp/dramatiq/pull/350))

*   The `--worker-shutdown-timeout` flag. ([#330](https://github.com/Bogdanp/dramatiq/pull/330), [@mic47](https://github.com/mic47))

### Changed[¶](https://dramatiq.io/changelog.html#id182 "Link to this heading")

*   The CLI raises an error when the `--watch` flag is set on unsupported platforms. ([#326](https://github.com/Bogdanp/dramatiq/pull/326), [#328](https://github.com/Bogdanp/dramatiq/pull/328), [@CaselIT](https://github.com/CaselIT))

### Fixed[¶](https://dramatiq.io/changelog.html#id183 "Link to this heading")

*   The CLI now returns code `1` when one of the workers is killed by an unhandled signal. ([#334](https://github.com/Bogdanp/dramatiq/pull/334), [@omegacoleman](https://github.com/omegacoleman))

*   The results middleware now gracefully handles actor-not-found errors during nack. ([#336](https://github.com/Bogdanp/dramatiq/pull/336), [#337](https://github.com/Bogdanp/dramatiq/pull/337), [@AndreCimander](https://github.com/AndreCimander))

*   A memory bloat issue with tasks that raise exceptions. ([#351](https://github.com/Bogdanp/dramatiq/pull/351))

*   CI on Windows. ([#371](https://github.com/Bogdanp/dramatiq/pull/371), [@gdvalle](https://github.com/gdvalle))

[1.9.0](https://github.com/Bogdanp/dramatiq/compare/v1.8.1...v1.9.0) – 2020-06-08[¶](https://dramatiq.io/changelog.html#id192 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id193 "Link to this heading")

*   A custom Redis connection can now be passed to the Redis broker via the new `client` keyword argument. ([#274](https://github.com/Bogdanp/dramatiq/issues/274), [@davidt99](https://github.com/davidt99))

*   Message priority can now be changed in `before_enqueue` hooks. ([#313](https://github.com/Bogdanp/dramatiq/issues/313), [@thomazthz](https://github.com/thomazthz))

*   Support for storing actor exceptions. ([#156](https://github.com/Bogdanp/dramatiq/issues/156))

*   Support for silent [`Retries`](https://dramatiq.io/reference.html#dramatiq.Retry "dramatiq.Retry"). ([#295](https://github.com/Bogdanp/dramatiq/issues/295))

*   Support for expected exceptions via the `throws` actor option. ([#303](https://github.com/Bogdanp/dramatiq/issues/303), [@takhs91](https://github.com/takhs91))

*   Support for changing the consumer class in the RabbitMQ and Redis brokers. ([#316](https://github.com/Bogdanp/dramatiq/issues/316), [@AndreCimander](https://github.com/AndreCimander))

### Changed[¶](https://dramatiq.io/changelog.html#id202 "Link to this heading")

*   Worker processes are no longer daemons. ([#289](https://github.com/Bogdanp/dramatiq/pull/289), [#294](https://github.com/Bogdanp/dramatiq/pull/294), [@takhs91](https://github.com/takhs91))

### Fixed[¶](https://dramatiq.io/changelog.html#id205 "Link to this heading")

*   A race condition during command line startup where the wrong exit codes could be returned when subprocesses failed. ([#286](https://github.com/Bogdanp/dramatiq/issues/286))

*   A race condition between worker processes and fork processes during boot. ([#297](https://github.com/Bogdanp/dramatiq/pull/297))

*   A logging race condition on Linux. ([#171](https://github.com/Bogdanp/dramatiq/issues/286), [#286](https://github.com/Bogdanp/dramatiq/issues/286))

*   `fileno` has been added to `StreamablePipe`. ([#291](https://github.com/Bogdanp/dramatiq/pull/291), [@takhs91](https://github.com/takhs91))

[1.8.1](https://github.com/Bogdanp/dramatiq/compare/v1.8.0...v1.8.1) – 2020-02-02[¶](https://dramatiq.io/changelog.html#id211 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id212 "Link to this heading")

*   An issue where an `IndexError` would be raised when multiple middlewre containing fork functions were defined. ([#271](https://github.com/Bogdanp/dramatiq/issues/271))

[1.8.0](https://github.com/Bogdanp/dramatiq/compare/v1.7.0...v1.8.0) – 2020-02-02[¶](https://dramatiq.io/changelog.html#id214 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id215 "Link to this heading")

*   Support for forking and running arbitrary functions (so-called “fork functions”). ([#127](https://github.com/Bogdanp/dramatiq/issues/127), [#230](https://github.com/Bogdanp/dramatiq/pull/230))

*   The `--fork-function` flag.

*   The `--skip-logging` flag. ([#263](https://github.com/Bogdanp/dramatiq/pull/263), [@whalesalad](https://github.com/whalesalad))

### Fixed[¶](https://dramatiq.io/changelog.html#id217 "Link to this heading")

*   An issue where the `max_age` parameter to [`AgeLimit`](https://dramatiq.io/reference.html#dramatiq.middleware.AgeLimit "dramatiq.middleware.AgeLimit") was being ignored. ([#240](https://github.com/Bogdanp/dramatiq/pull/240), [@evstratbg](https://github.com/evstratbg))

*   An issue with delaying pipelines. ([#264](https://github.com/Bogdanp/dramatiq/pull/264), [@synweap15](https://github.com/synweap15))

*   An issue where the master process would sometimes hang when stopped. ([#260](https://github.com/Bogdanp/dramatiq/pull/260), [@asavoy](https://github.com/asavoy))

*   An issue where the [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker") could sometimes prefetch more messages than it was configured to. ([#262](https://github.com/Bogdanp/dramatiq/pull/262), [@benekastah](https://github.com/benekastah))

*   The [`StubBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker "dramatiq.brokers.stub.StubBroker") now flushes its dead letter queue when its `flush_all` method is called. ([#247](https://github.com/Bogdanp/dramatiq/pull/247), [@CapedHero](https://github.com/CapedHero))

*   The [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker") now takes the max lua stack size into account. This should fix certain heisenbugs that folks have encountered with that broker. ([#259](https://github.com/Bogdanp/dramatiq/pull/259), [@benekastah](https://github.com/benekastah))

### Changed[¶](https://dramatiq.io/changelog.html#id225 "Link to this heading")

*   The [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker") now creates its queues lazily. ([#163](https://github.com/Bogdanp/dramatiq/issues/163), [#270](https://github.com/Bogdanp/dramatiq/pull/270), [@timdrijvers](https://github.com/timdrijvers))

*   The [`Prometheus`](https://dramatiq.io/reference.html#dramatiq.middleware.prometheus.Prometheus "dramatiq.middleware.prometheus.Prometheus") middleware no longer depends on file locking to start its exposition server. Instead, it uses the new fork functions functionality to start the server in a separate, unique process. The middleware no longer takes any parameters. While this would normally be a breaking change, it appears those parameters were previously ignored anyway. ([#127](https://github.com/Bogdanp/dramatiq/issues/127), [#230](https://github.com/Bogdanp/dramatiq/pull/230))

[1.7.0](https://github.com/Bogdanp/dramatiq/compare/v1.6.1...v1.7.0) – 2019-09-22[¶](https://dramatiq.io/changelog.html#id230 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id231 "Link to this heading")

*   Generic actors can now be passed custom actor registires. ([#223](https://github.com/Bogdanp/dramatiq/pull/223), [@jonathanlintott](https://github.com/jonathanlintott))

*   `--use-spawn` command line argument. ([#227](https://github.com/Bogdanp/dramatiq/pull/227), [#228](https://github.com/Bogdanp/dramatiq/pull/228), [@jrusso1020](https://github.com/jrusso1020))

### Changed[¶](https://dramatiq.io/changelog.html#id232 "Link to this heading")

*   Uncaught exceptions within workers are now logged as errors rather than warnings. ([#221](https://github.com/Bogdanp/dramatiq/pull/221), [@th0th](https://github.com/th0th))

[1.6.1](https://github.com/Bogdanp/dramatiq/compare/v1.6.0...v1.6.1) – 2019-07-24[¶](https://dramatiq.io/changelog.html#id237 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id238 "Link to this heading")

*   [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker") now supports multiple connection uris to be passed in via its `url` parameter. ([#216](https://github.com/Bogdanp/dramatiq/pull/216), [@wsantos](https://github.com/wsantos))

### Changed[¶](https://dramatiq.io/changelog.html#id239 "Link to this heading")

*   Updated allowed version range for prometheus-client. ([#219](https://github.com/Bogdanp/dramatiq/pull/219), [@robinro](https://github.com/robinro))

[1.6.0](https://github.com/Bogdanp/dramatiq/compare/v1.5.0...v1.6.0) – 2019-05-02[¶](https://dramatiq.io/changelog.html#id242 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id243 "Link to this heading")

*   dramatiq_queue_prefetch environment variable to control the number of messages to prefetch per worker process. ([#183](https://github.com/Bogdanp/dramatiq/issues/183), [#184](https://github.com/Bogdanp/dramatiq/issues/184), [@xelhark](https://github.com/xelhark))

*   The RabbitMQ broker now retries the queue declaration process if an error occurs. ([#179](https://github.com/Bogdanp/dramatiq/issues/179), [@davidt99](https://github.com/davidt99))

*   Support for accessing nested broker instances from the CLI. ([#191](https://github.com/Bogdanp/dramatiq/pull/191), [@bersace](https://github.com/bersace))

*   Support for eagerly raising actor exceptions in the joining thread with the [`StubBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker "dramatiq.brokers.stub.StubBroker"). ([#195](https://github.com/Bogdanp/dramatiq/issues/195), [#203](https://github.com/Bogdanp/dramatiq/pull/203))

*   Support for accessing the current message from an actor via [`CurrentMessage`](https://dramatiq.io/reference.html#dramatiq.middleware.CurrentMessage "dramatiq.middleware.CurrentMessage"). ([#208](https://github.com/Bogdanp/dramatiq/issues/208))

### Changed[¶](https://dramatiq.io/changelog.html#id252 "Link to this heading")

*   Pinned pika version >1.0,<2.0. ([#202](https://github.com/Bogdanp/dramatiq/pull/202))

### Fixed[¶](https://dramatiq.io/changelog.html#id254 "Link to this heading")

*   An issue where workers would fail and never recover after the connection to Redis was severed. ([#207](https://github.com/Bogdanp/dramatiq/issues/207))

*   `pipe_ignore` has been fixed to apply to the next message in line within a pipeline. ([#194](https://github.com/Bogdanp/dramatiq/pull/194), [@metheoryt](https://github.com/metheoryt))

[1.5.0](https://github.com/Bogdanp/dramatiq/compare/v1.4.3...v1.5.0) – 2019-02-18[¶](https://dramatiq.io/changelog.html#id257 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id258 "Link to this heading")

*   The RabbitMQ broker now supports native message priorities. ([#157](https://github.com/Bogdanp/dramatiq/pull/157), [@davidt99](https://github.com/davidt99))

*   Support for specifying the actor class to [`actor`](https://dramatiq.io/reference.html#dramatiq.actor "dramatiq.actor"). ([#169](https://github.com/Bogdanp/dramatiq/pull/169), [@gilbsgilbs](https://github.com/gilbsgilbs))

### Changed[¶](https://dramatiq.io/changelog.html#id262 "Link to this heading")

*   Pika 0.13 is now required.

### Fixed[¶](https://dramatiq.io/changelog.html#id263 "Link to this heading")

*   Consumers are now stopped after workers finish running their tasks. ([#160](https://github.com/Bogdanp/dramatiq/pull/160), [@brownan](https://github.com/brownan))

*   Worker logging on Python 3.7 is no longer delayed.

[1.4.3](https://github.com/Bogdanp/dramatiq/compare/v1.4.2...v1.4.3) – 2019-01-08[¶](https://dramatiq.io/changelog.html#id265 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id266 "Link to this heading")

*   Changed license classifier to the correct license. This is why you shouldn’t publish changed before you’ve had coffee, folks!

[1.4.2](https://github.com/Bogdanp/dramatiq/compare/v1.4.1...v1.4.2) – 2019-01-08[¶](https://dramatiq.io/changelog.html#id267 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id268 "Link to this heading")

*   License classifier in PyPI package. There were no source code changes for this release.

[1.4.1](https://github.com/Bogdanp/dramatiq/compare/v1.4.0...v1.4.1) – 2018-12-30[¶](https://dramatiq.io/changelog.html#id269 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id270 "Link to this heading")

*   Support for redis-py 3.x. ([#142](https://github.com/Bogdanp/dramatiq/pull/142), [@maerteijn](https://github.com/maerteijn))

### Fixed[¶](https://dramatiq.io/changelog.html#id272 "Link to this heading")

*   Workers wait for RMQ messages to be acked upon shutdown. ([#148](https://github.com/Bogdanp/dramatiq/issues/148))

*   Pipelines no longer continue when a message is failed. ([#151](https://github.com/Bogdanp/dramatiq/issues/151), [@davidt99](https://github.com/davidt99))

*   Log files now work under Windows. ([#141](https://github.com/Bogdanp/dramatiq/pull/141), [@ryansm1](https://github.com/ryansm1))

[1.4.0](https://github.com/Bogdanp/dramatiq/compare/v1.3.0...v1.4.0) – 2018-11-25[¶](https://dramatiq.io/changelog.html#id277 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id278 "Link to this heading")

*   [`Barriers`](https://dramatiq.io/reference.html#dramatiq.rate_limits.Barrier "dramatiq.rate_limits.Barrier").

### Changed[¶](https://dramatiq.io/changelog.html#id279 "Link to this heading")

*   `cli.main` now takes an optional argument namespace so that users may define their own entrypoints. ([#140](https://github.com/Bogdanp/dramatiq/issues/140), [@maerteijn](https://github.com/maerteijn))

*   Actor “message received” and “completed in x ms” log messages are now logged with the `DEBUG` level instead of `INFO` level. This improves throughput and makes logging much less verbose.

*   The [`TimeLimit`](https://dramatiq.io/reference.html#dramatiq.middleware.TimeLimit "dramatiq.middleware.TimeLimit") middleware no longer uses signals to trigger time limit handling. Instead it uses a background thread per worker process.

*   Dramatiq now shuts itself down if any of the workers die unexpectedly (for example, if one of them is killed by the OOM killer).

*   Windows is now supported (with some caveats)! ([#119](https://github.com/Bogdanp/dramatiq/issues/119), [@ryansm1](https://github.com/ryansm1))

### Fixed[¶](https://dramatiq.io/changelog.html#id280 "Link to this heading")

*   Allow `pipe_ignore` option to be set at the actor level. ([#100](https://github.com/Bogdanp/dramatiq/issues/100))

*   Result encoder now defaults to the global encoder. ([#108](https://github.com/Bogdanp/dramatiq/issues/108), [@xdmiodz](https://github.com/xdmiodz))

*   Dot characters are now allowed in queue names. ([#111](https://github.com/Bogdanp/dramatiq/issues/111))

*   Tests are now run on Windows. ([#113](https://github.com/Bogdanp/dramatiq/issues/113), [@ryansm1](https://github.com/ryansm1))

[1.3.0](https://github.com/Bogdanp/dramatiq/compare/v1.2.0...v1.3.0) – 2018-07-05[¶](https://dramatiq.io/changelog.html#id289 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Changed[¶](https://dramatiq.io/changelog.html#id290 "Link to this heading")

*   Upgraded prometheus_client to 0.2.x.

*   Bumped pika to version 0.12. Because of this change, the `interrupt` method on [`Broker`](https://dramatiq.io/reference.html#dramatiq.Broker "dramatiq.Broker") and its usages within [`Worker`](https://dramatiq.io/reference.html#dramatiq.Worker "dramatiq.Worker") have been dropped.

*   There is no longer a max message delay.

### Fixed[¶](https://dramatiq.io/changelog.html#id291 "Link to this heading")

*   [`Brokers`](https://dramatiq.io/reference.html#dramatiq.Broker "dramatiq.Broker") can now be passed an empty list of middleware. ([#90](https://github.com/Bogdanp/dramatiq/issues/90))

*   Potential stack overflow when restarting Consumer threads. ([#89](https://github.com/Bogdanp/dramatiq/issues/89))

[1.2.0](https://github.com/Bogdanp/dramatiq/compare/v1.1.0...v1.2.0) – 2018-05-24[¶](https://dramatiq.io/changelog.html#id294 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id295 "Link to this heading")

*   Support for worker heartbeats to [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker").

*   `maintenance_chance` and `heartbeat_timeout` parameters to [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker").

*   [`Interrupt`](https://dramatiq.io/reference.html#dramatiq.middleware.Interrupt "dramatiq.middleware.Interrupt") base class for thread-interrupting exceptions. ([@rpkilby](https://github.com/rpkilby))

*   [`ShutdownNotifications`](https://dramatiq.io/reference.html#dramatiq.middleware.ShutdownNotifications "dramatiq.middleware.ShutdownNotifications") middleware. ([@rpkilby](https://github.com/rpkilby))

### Changed[¶](https://dramatiq.io/changelog.html#id296 "Link to this heading")

*   [`TimeLimitExceeded`](https://dramatiq.io/reference.html#dramatiq.middleware.TimeLimitExceeded "dramatiq.middleware.TimeLimitExceeded") is now a subclass of [`Interrupt`](https://dramatiq.io/reference.html#dramatiq.middleware.Interrupt "dramatiq.middleware.Interrupt").

### Fixed[¶](https://dramatiq.io/changelog.html#id297 "Link to this heading")

*   [`StubBroker.join`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker.join "dramatiq.brokers.stub.StubBroker.join") and [`Worker.join`](https://dramatiq.io/reference.html#dramatiq.Worker.join "dramatiq.Worker.join") are now more reliable.

*   Module import path is now prepended to search path rather than appended. This fixes an issue where importing modules with the same name as modules from site-packages would end up importing the modules from site-packages. ([#88](https://github.com/Bogdanp/dramatiq/issues/88))

*   [`Prometheus`](https://dramatiq.io/reference.html#dramatiq.middleware.prometheus.Prometheus "dramatiq.middleware.prometheus.Prometheus") middleware no longer wipes the prometheus data directory on startup. This fixes an issue with exporting application metrics along with worker metrics.

### Deprecated[¶](https://dramatiq.io/changelog.html#deprecated "Link to this heading")

*   `requeue_{deadline,interval}` parameters to [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker"). These two parameters no longer have any effect.

[1.1.0](https://github.com/Bogdanp/dramatiq/compare/v1.0.0...v1.1.0) – 2018-04-17[¶](https://dramatiq.io/changelog.html#id299 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id300 "Link to this heading")

*   `confirm_delivery` parameter to [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker").

*   `dead_message_ttl`, `requeue_deadline` and `requeue_interval` parameters to [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker").

*   `url` parameter to [`Redis`](https://dramatiq.io/reference.html#dramatiq.rate_limits.backends.RedisBackend "dramatiq.rate_limits.backends.RedisBackend") rate limiter backend.

*   `url` parameter to [`Redis`](https://dramatiq.io/reference.html#dramatiq.results.backends.RedisBackend "dramatiq.results.backends.RedisBackend") result backend.

*   `timeout` parameter to all the brokers’ `join` methods. ([#57](https://github.com/Bogdanp/dramatiq/issues/57))

*   `flush` and `flush_all` methods to [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker"). ([#62](https://github.com/Bogdanp/dramatiq/issues/62))

*   `flush` and `flush_all` methods to [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker"). ([#62](https://github.com/Bogdanp/dramatiq/issues/62))

### Changed[¶](https://dramatiq.io/changelog.html#id301 "Link to this heading")

*   Cleaned up command line argument descriptions.

### Deprecated[¶](https://dramatiq.io/changelog.html#id302 "Link to this heading")

*   `URLRabbitmqBroker` is deprecated. The [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker") takes a `url` parameter so use that instead. `URLRabbitmqBroker` will be removed in version 2.0.

### Fixed[¶](https://dramatiq.io/changelog.html#id303 "Link to this heading")

*   `rabbitmq` and `watch` extra dependencies are only installed when they are explicitly required now. ([#60](https://github.com/Bogdanp/dramatiq/issues/60), [@rpkilby](https://github.com/rpkilby))

*   signal handling from the master process on FreeBSD 10.3. ([#66](https://github.com/Bogdanp/dramatiq/issues/66))

*   reloading now uses `sys.executable` when exec’ing workers that were started with `python -m dramatiq`.

*   an issue that caused logging to fail when non-utf-8 characters were printed to stdout/err. ([#63](https://github.com/Bogdanp/dramatiq/issues/63))

*   an issue with potentially drifting keys in the [`WindowRateLimiter`](https://dramatiq.io/reference.html#dramatiq.rate_limits.WindowRateLimiter "dramatiq.rate_limits.WindowRateLimiter"). ([#69](https://github.com/Bogdanp/dramatiq/issues/69), [@gdvalle](https://github.com/gdvalle))

[1.0.0](https://github.com/Bogdanp/dramatiq/compare/v0.20.0...v1.0.0) – 2018-03-31[¶](https://dramatiq.io/changelog.html#id312 "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id313 "Link to this heading")

*   `--log-file` command line argument. ([#43](https://github.com/Bogdanp/dramatiq/issues/43), [@najamansari](https://github.com/najamansari))

*   `--pid-file` command line argument. ([#43](https://github.com/Bogdanp/dramatiq/issues/43), [@najamansari](https://github.com/najamansari))

### Changed[¶](https://dramatiq.io/changelog.html#id315 "Link to this heading")

*   Dramatiq is now licensed under the LGPL.

### Fixed[¶](https://dramatiq.io/changelog.html#id316 "Link to this heading")

*   Passing `time_limit` in `send_with_options`. ([#44](https://github.com/Bogdanp/dramatiq/issues/44))

[0.20.0](https://github.com/Bogdanp/dramatiq/compare/v0.19.1...v0.20.0) – 2018-03-17[¶](https://dramatiq.io/changelog.html#id318 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id319 "Link to this heading")

*   `--queues` CLI argument. ([#35](https://github.com/Bogdanp/dramatiq/pull/35))

### Changed[¶](https://dramatiq.io/changelog.html#id321 "Link to this heading")

*   Unhandled errors within workers now print the full stack trace. ([#42](https://github.com/Bogdanp/dramatiq/pull/42))

[0.19.1](https://github.com/Bogdanp/dramatiq/compare/v0.19.0...v0.19.1) – 2018-03-08[¶](https://dramatiq.io/changelog.html#id323 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id324 "Link to this heading")

*   Calling `str` on [`actor`](https://dramatiq.io/reference.html#dramatiq.actor "dramatiq.actor"). ([#40](https://github.com/Bogdanp/dramatiq/pull/40), [@aequitas](https://github.com/aequitas))

[0.19.0](https://github.com/Bogdanp/dramatiq/compare/v0.19.0...v0.19.0) – 2018-01-17[¶](https://dramatiq.io/changelog.html#id326 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id327 "Link to this heading")

*   [`group`](https://dramatiq.io/reference.html#dramatiq.group "dramatiq.group") and [`pipeline`](https://dramatiq.io/reference.html#dramatiq.pipeline "dramatiq.pipeline").

*   `retry_when` parameter to [`Retries`](https://dramatiq.io/reference.html#dramatiq.middleware.Retries "dramatiq.middleware.Retries").

### Changed[¶](https://dramatiq.io/changelog.html#id328 "Link to this heading")

*   [`RateLimitExceeded`](https://dramatiq.io/reference.html#dramatiq.RateLimitExceeded "dramatiq.RateLimitExceeded") errors no longer log the full stack trace when raised within workers.

*   Consumer connection errors no longer dump a stack trace.

*   Consumers now wait exactly 3 seconds between retries after a connection error, rather than using exponential backoff.

[0.18.0](https://github.com/Bogdanp/dramatiq/compare/v0.17.0...v0.18.0) – 2018-01-06[¶](https://dramatiq.io/changelog.html#id329 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id330 "Link to this heading")

*   `pip install dramatiq[all]` installs all deps.

*   `--path` command line argument. ([#27](https://github.com/Bogdanp/dramatiq/issues/27))

### Changed[¶](https://dramatiq.io/changelog.html#id331 "Link to this heading")

*   `pip install dramatiq` now installs RabbitMQ and watch deps.

[0.17.0](https://github.com/Bogdanp/dramatiq/compare/v0.16.0...v0.17.0) – 2017-12-30[¶](https://dramatiq.io/changelog.html#id333 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id334 "Link to this heading")

*   [`Callbacks`](https://dramatiq.io/reference.html#dramatiq.middleware.Callbacks "dramatiq.middleware.Callbacks") middleware.

*   `asdict` method to [`Messages`](https://dramatiq.io/reference.html#dramatiq.Message "dramatiq.Message").

### Fixed[¶](https://dramatiq.io/changelog.html#id335 "Link to this heading")

*   Pinned pika version 0.11 to avoid an issue where passing `heartbeat` to `RabbitmqBroker` in `get_broker` would raise a `TypeError`. ([#23](https://github.com/Bogdanp/dramatiq/pull/23), [@chen2aaron](https://github.com/chen2aaron))

[0.16.0](https://github.com/Bogdanp/dramatiq/compare/v0.15.1...v0.16.0) – 2017-12-25[¶](https://dramatiq.io/changelog.html#id337 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id338 "Link to this heading")

*   `long_running` example.

*   `scheduling` example.

*   [`Messages`](https://dramatiq.io/reference.html#dramatiq.Message "dramatiq.Message") now support pluggable [`Encoders`](https://dramatiq.io/reference.html#dramatiq.Encoder "dramatiq.Encoder").

*   [`ResultBackends`](https://dramatiq.io/reference.html#dramatiq.results.ResultBackend "dramatiq.results.ResultBackend") now support pluggable [`Encoders`](https://dramatiq.io/reference.html#dramatiq.Encoder "dramatiq.Encoder").

### Changed[¶](https://dramatiq.io/changelog.html#id339 "Link to this heading")

*   [`Redis`](https://dramatiq.io/reference.html#dramatiq.results.backends.RedisBackend "dramatiq.results.backends.RedisBackend") result backend is now considerably more resource-efficient (it no longer polls).

*   `sys.std{err,out}` are now redirected to stderr and line-buffered.

### Fixed[¶](https://dramatiq.io/changelog.html#id340 "Link to this heading")

*   [`TimeLimit`](https://dramatiq.io/reference.html#dramatiq.middleware.TimeLimit "dramatiq.middleware.TimeLimit") middleware now uses a monotonic clock.

[0.15.1](https://github.com/Bogdanp/dramatiq/compare/v0.15.0...v0.15.1) – 2017-12-08[¶](https://dramatiq.io/changelog.html#id341 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id342 "Link to this heading")

*   Autoreload now works under gevent.

[0.15.0](https://github.com/Bogdanp/dramatiq/compare/v0.14.0...v0.15.0) – 2017-11-24[¶](https://dramatiq.io/changelog.html#id343 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id344 "Link to this heading")

*   Support for [`Results`](https://dramatiq.io/reference.html#dramatiq.results.Results "dramatiq.results.Results").

*   `pool` parameter to the [`Memcached`](https://dramatiq.io/reference.html#dramatiq.rate_limits.backends.MemcachedBackend "dramatiq.rate_limits.backends.MemcachedBackend") rate limiter backend.

*   `client` parameter to the [`Redis`](https://dramatiq.io/reference.html#dramatiq.rate_limits.backends.RedisBackend "dramatiq.rate_limits.backends.RedisBackend") rate limiter backend.

*   `--watch-use-polling` command line argument.

### Fixed[¶](https://dramatiq.io/changelog.html#id345 "Link to this heading")

*   Fixed bad file descriptor issue during RMQ broker shutdown under gevent.

[0.14.0](https://github.com/Bogdanp/dramatiq/compare/v0.13.1...v0.14.0) – 2017-11-21[¶](https://dramatiq.io/changelog.html#id346 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id347 "Link to this heading")

*   [`dramatiq.Actor.logger`](https://dramatiq.io/reference.html#dramatiq.Actor.logger "dramatiq.Actor.logger").

*   Logging statements before and after an actor is called.

### Fixed[¶](https://dramatiq.io/changelog.html#id348 "Link to this heading")

*   [`class-based actors`](https://dramatiq.io/reference.html#dramatiq.GenericActor "dramatiq.GenericActor") behave more like normal Python classes now. ([#15](https://github.com/Bogdanp/dramatiq/issues/15))

[0.13.1](https://github.com/Bogdanp/dramatiq/compare/v0.13.0...v0.13.1) – 2017-11-17[¶](https://dramatiq.io/changelog.html#id350 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Changed[¶](https://dramatiq.io/changelog.html#id351 "Link to this heading")

*   Connection and import errors that occur during process boot now log stack traces ([@rakanalh](https://github.com/rakanalh)).

*   Added support for Python **3.5** ([#7](https://github.com/Bogdanp/dramatiq/issues/7) by [@jssuzanne](https://github.com/jssuzanne)).

[0.13.0](https://github.com/Bogdanp/dramatiq/compare/v0.12.1...v0.13.0) – 2017-11-15[¶](https://dramatiq.io/changelog.html#id353 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id354 "Link to this heading")

*   Support for [`class-based actors`](https://dramatiq.io/reference.html#dramatiq.GenericActor "dramatiq.GenericActor") ([#9](https://github.com/Bogdanp/dramatiq/issues/9)).

[0.12.1](https://github.com/Bogdanp/dramatiq/compare/v0.12.0...v0.12.1) – 2017-11-15[¶](https://dramatiq.io/changelog.html#id356 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id357 "Link to this heading")

*   An `AssertionError` after starting the consumer if RabbitMQ is not running ([#10](https://github.com/Bogdanp/dramatiq/issues/10)).

[0.12.0](https://github.com/Bogdanp/dramatiq/compare/v0.11.0...v0.12.0) – 2017-11-14[¶](https://dramatiq.io/changelog.html#id359 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id360 "Link to this heading")

*   [`Worker.pause`](https://dramatiq.io/reference.html#dramatiq.Worker.pause "dramatiq.Worker.pause") and [`Worker.resume`](https://dramatiq.io/reference.html#dramatiq.Worker.resume "dramatiq.Worker.resume").

*   `url` parameter to [`RedisBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.redis.RedisBroker "dramatiq.brokers.redis.RedisBroker").

### Fixed[¶](https://dramatiq.io/changelog.html#id361 "Link to this heading")

*   Pending interrupt messages are now removed from pika’s queue before cancel is called. This fixes an issue where an `AtrributeError` was sometimes raised on worker shutdown.

*   Pika connection reset logs from the main thread are now hidden.

*   Distribution of `dramatiq-gevent` ([#2](https://github.com/Bogdanp/dramatiq/issues/2)).

[0.11.0](https://github.com/Bogdanp/dramatiq/compare/v0.10.2...v0.11.0) – 2017-11-09[¶](https://dramatiq.io/changelog.html#id363 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id364 "Link to this heading")

*   [`SkipMessage`](https://dramatiq.io/reference.html#dramatiq.middleware.SkipMessage "dramatiq.middleware.SkipMessage") middleware error.

*   [`after_skip_message`](https://dramatiq.io/reference.html#dramatiq.Middleware.after_skip_message "dramatiq.Middleware.after_skip_message") middleware hook.

*   [`join`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker.join "dramatiq.brokers.rabbitmq.RabbitmqBroker.join") now takes optional `min_successes` and `idle_time` parameters.

### Changed[¶](https://dramatiq.io/changelog.html#id365 "Link to this heading")

*   Consumer reconnect backoff factor has been lowered from 10s to 100ms.

*   `URLRabbitmqBroker` is now a factory function that creates instances of [`RabbitmqBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.rabbitmq.RabbitmqBroker "dramatiq.brokers.rabbitmq.RabbitmqBroker").

### Fixed[¶](https://dramatiq.io/changelog.html#id366 "Link to this heading")

*   Worker processes no longer use a spinlock to consume messages.

*   Consumers now use the same idle timeout as workers.

*   [`StubBroker`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker "dramatiq.brokers.stub.StubBroker") no longer declares dead letter queues.

[0.10.2](https://github.com/Bogdanp/dramatiq/compare/v0.10.1...v0.10.2) – 2017-11-06[¶](https://dramatiq.io/changelog.html#id367 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Changed[¶](https://dramatiq.io/changelog.html#id368 "Link to this heading")

*   `pika` is now pinned to `>=0.10,<0.12`.

[0.10.1](https://github.com/Bogdanp/dramatiq/compare/v0.10.0...v0.10.1) – 2017-11-04[¶](https://dramatiq.io/changelog.html#id369 "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id370 "Link to this heading")

*   More benchmarks.

### Fixed[¶](https://dramatiq.io/changelog.html#id371 "Link to this heading")

*   [`StubBroker.flush_all`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker.flush_all "dramatiq.brokers.stub.StubBroker.flush_all") now flushes delay queues.

[0.10.0](https://github.com/Bogdanp/dramatiq/compare/v0.9.0...v0.10.0) – 2017-10-30[¶](https://dramatiq.io/changelog.html#id372 "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id373 "Link to this heading")

*   `URLRabbitmqbroker` ([@whalesalad](https://github.com/whalesalad)).

*   StubBroker [`StubBroker.flush`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker.flush "dramatiq.brokers.stub.StubBroker.flush") and [`StubBroker.flush_all`](https://dramatiq.io/reference.html#dramatiq.brokers.stub.StubBroker.flush_all "dramatiq.brokers.stub.StubBroker.flush_all").

*   [`before_consumer_thread_shutdown`](https://dramatiq.io/reference.html#dramatiq.Middleware.before_consumer_thread_shutdown "dramatiq.Middleware.before_consumer_thread_shutdown") middleware hook.

*   [`before_worker_thread_shutdown`](https://dramatiq.io/reference.html#dramatiq.Middleware.before_worker_thread_shutdown "dramatiq.Middleware.before_worker_thread_shutdown") middleware hook.

### Changed[¶](https://dramatiq.io/changelog.html#id374 "Link to this heading")

*   Implementation of the window rate limiter has been streamlined.

*   Redis requeue is now more efficient.

*   RabbitMQ enqueue is now resilient to disconnects.

### Fixed[¶](https://dramatiq.io/changelog.html#id375 "Link to this heading")

*   `dramatiq-gevent` packaging ([@bendemaree](https://github.com/bendemaree)).

[0.9.0](https://github.com/Bogdanp/dramatiq/compare/v0.8.0...v0.9.0) – 2017-10-20[¶](https://dramatiq.io/changelog.html#id377 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Changed[¶](https://dramatiq.io/changelog.html#id378 "Link to this heading")

*   Messages are no longer assigned new ids when they are re-enqueued. This makes tracking messages using middleware significantly easier.

*   The RedisBroker now assigns its own internal message ids.

[0.8.0](https://github.com/Bogdanp/dramatiq/compare/v0.7.1...v0.8.0) – 2017-10-19[¶](https://dramatiq.io/changelog.html#id379 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Changed[¶](https://dramatiq.io/changelog.html#id380 "Link to this heading")

*   RabbitmqBroker no longer takes a ConnectionParameters param as input. Instead, it builds one based on kwargs.

*   `exec` is now used to reload the main process on source code changes when the `--watch` flag is enabled.

[0.7.1](https://github.com/Bogdanp/dramatiq/compare/v0.7.0...v0.7.1) – 2017-10-08[¶](https://dramatiq.io/changelog.html#id381 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id382 "Link to this heading")

*   Lua files are now properly distributed with the package.

[0.7.0](https://github.com/Bogdanp/dramatiq/compare/v0.6.1...v0.7.0) – 2017-09-13[¶](https://dramatiq.io/changelog.html#id383 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Changed[¶](https://dramatiq.io/changelog.html#id384 "Link to this heading")

*   Reworked scheduled messages to improve fairness. Messages are now re-enqueued on the broker once they hit their eta.

*   `prometheus-client` has been pinned to version `0.0.20`.

[0.6.1](https://github.com/Bogdanp/dramatiq/compare/v0.6.0...v0.6.1) – 2017-07-20[¶](https://dramatiq.io/changelog.html#id385 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Fixed[¶](https://dramatiq.io/changelog.html#id386 "Link to this heading")

*   A race condition with calls to `cas` in the memcached rate limiter backend.

[0.6.0](https://github.com/Bogdanp/dramatiq/compare/v0.5.2...v0.6.0) – 2017-07-09[¶](https://dramatiq.io/changelog.html#id387 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id388 "Link to this heading")

*   `before` and `after` arguments to [`add_middleware`](https://dramatiq.io/reference.html#dramatiq.Broker.add_middleware "dramatiq.Broker.add_middleware").

*   Support for [`RateLimiters`](https://dramatiq.io/reference.html#dramatiq.rate_limits.RateLimiter "dramatiq.rate_limits.RateLimiter").

[0.5.2](https://github.com/Bogdanp/dramatiq/compare/v0.5.1...v0.5.2) – 2017-06-29[¶](https://dramatiq.io/changelog.html#id389 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Changed[¶](https://dramatiq.io/changelog.html#id390 "Link to this heading")

*   Changed the default max retries value from `None` to `20`, meaning tasks are now retried for up to about 30 days before they’re dead-lettered by default.

[0.5.1](https://github.com/Bogdanp/dramatiq/compare/v0.5.0...v0.5.1) – 2017-06-28[¶](https://dramatiq.io/changelog.html#id391 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Removed[¶](https://dramatiq.io/changelog.html#id392 "Link to this heading")

*   Dropped RabbitMQ heartbeat to avoid spurious disconnects.

[0.5.0](https://github.com/Bogdanp/dramatiq/compare/v0.4.1...v0.5.0) – 2017-06-27[¶](https://dramatiq.io/changelog.html#id393 "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

### Added[¶](https://dramatiq.io/changelog.html#id394 "Link to this heading")

*   Added `dramatiq-gevent` script.

### Changed[¶](https://dramatiq.io/changelog.html#id395 "Link to this heading")

*   Capped prefetch counts to 65k.
