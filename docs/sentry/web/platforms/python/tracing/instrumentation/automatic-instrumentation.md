---
---
title: Automatic Instrumentation
description: "Learn what instrumentation automatically captures transactions."
---

Many integrations for popular frameworks automatically capture transactions. If you already have any of the following frameworks set up for Sentry error reporting, you will start to see traces immediately:

- All WSGI-based web frameworks (Django, Flask, Pyramid, Falcon, Bottle)
- Celery
- AIOHTTP web apps
- Redis Queue (RQ)

Spans are instrumented for the following operations within a transaction:

- Database queries that use SQLAlchemy or the Django ORM
- HTTP requests made with HTTPX, requests, or the stdlib
- Spawned subprocesses
- Redis operations

Spans are only created within an existing transaction. If you're not using any of the supported frameworks, you'll need to create transactions manually.
