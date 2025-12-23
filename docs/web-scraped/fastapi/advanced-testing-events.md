# Source: https://fastapi.tiangolo.com/advanced/testing-events/

# Testing Events: lifespan and startup - shutdown[&para;](#testing-events-lifespan-and-startup-shutdown)

When you need `lifespan` to run in your tests, you can use the `TestClient` with a `with` statement:

Python 3.9+

You can read more details about the ["Running lifespan in tests in the official Starlette documentation site."](https://www.starlette.dev/lifespan/#running-lifespan-in-tests)

For the deprecated `startup` and `shutdown` events, you can use the `TestClient` as follows:

Python 3.9+