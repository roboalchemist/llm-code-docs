# Source: https://docs.earthly.dev/docs/guides/integration.md

# Source: https://docs.earthly.dev/earthly-0.7/docs/guides/integration.md

# Source: https://docs.earthly.dev/earthly-0.6/docs/guides/integration.md

# Integration Testing

Running unit tests in a build pipeline is relatively simple. By definition, unit tests have no external dependencies. Things get more interesting when we want to test how our service integrates with other services and external systems. A service may have dependencies on external file systems, on databases, on external message queues, or other services. An ergonomic and effective development environment should have simple ways to construct and run integration tests. It should be easy to run these tests locally on the developer machine and in the build pipeline.

\*\* This guide will take an existing application with integration tests and show how they can be easily run inside earthly, both in the local development environment as well as in the build pipeline. \*\*

## Prerequisites

*This integration approach can work with most applications and development stacks. See* [*examples*](https://github.com/earthly/earthly/tree/main/examples) *for guidance on using earthly in other languages.*

### Our Application

The application we start with is simple. It returns the first 5 countries alphabetically via standard out. It has unit tests and integration tests. The integration tests require a datastore with the correct data in place.

### The Basic Earthfile

We start with a simple Earthfile that can build and create a docker image for our app. See the [Basics guide](https://docs.earthly.dev/earthly-0.6/basics) for more details, as well as examples in many programming languages.

See the [Basics Guide](https://docs.earthly.dev/earthly-0.6/basics) for more details on these steps, including how they might differ in Go, JavaScript, Java, and Python.

## In-App Integration Testing

Since our service has a docker-compose file of dependencies, running integration tests is easy.

Our integration target needs to copy in our source code and our Dockerfile and then inside a `WITH DOCKER` start the tests:

```Dockerfile
integration-test:
    FROM +project-files
    COPY src src
    COPY docker-compose.yml ./ 
    WITH DOCKER --compose docker-compose.yml
        RUN while ! pg_isready --host=localhost --port=5432 --dbname=iso3166 --username=postgres; do sleep 1; done ;\
            sbt it:test
    END
```

The `WITH DOCKER` has a `--compose` flag that we use to start up our docker-compose and run our integration tests in that context.

We can now run our tests both locally and in the CI pipeline, in a reproducible way:

```bash
> earthly -P +integration-test
+integration-test | Creating local-postgres ... done
+integration-test | Creating local-postgres-ui ... done
+integration-test | +integration-test | [info] Loading settings for project scala-example-build from plugins.sbt ...
+integration-test | [info] DatabaseIntegrationTest:
+integration-test | [info] A table
+integration-test | [info] - should have country data
+integration-test | [info] Run completed in 7 seconds, 923 milliseconds.
+integration-test | [info] Tests: succeeded 1, failed 0, canceled 0, ignored 0, pending 0
+integration-test | Stopping local-postgres-ui ... done
+integration-test | Stopping local-postgres    ... done
+integration-test | Removing local-postgres-ui ... done
+integration-test | Removing local-postgres    ... done
+integration-test | Removing network scala-example_default
+integration-test | Target github.com/earthly/earthly-example-scala/integration:main+integration-test built successfully
...
```

This means that if an integration test fails in the build pipeline, you can easily reproduce it locally.

## End to End Integration Tests

Our first integration test used was part of the service we were testing. This is one way to exercise integration code paths. Another useful form of integration testing is end-to-end testing. In this form of integration testing, we start up the application and test it from the outside.

In our simplified case example, with a single code path, a test that verifies the application starts and produces the desired output is sufficient.

Output: We can then run this and check that our application with its dependencies, produces the correct output.

```Dockerfile
> earthly -P +smoke-test
+smoke-test | --> WITH DOCKER RUN for i in {1..30}; do nc -z localhost 5432 && break; sleep 1; done; docker run --network=host earthly/examples:integration
+smoke-test | Loading images...
+smoke-test | Loaded image: aa8y/postgres-dataset:iso3166
+smoke-test | Loaded image: adminer:latest
+smoke-test | Loaded image: earthly/examples:integration
+smoke-test | ...done
+smoke-test | Creating network "scala-example_default" with the default driver
+smoke-test | Creating local-postgres ... done
+smoke-test | Creating local-postgres-ui ... done
+smoke-test | +smoke-test | The first 5 countries alphabetically are: Afghanistan, Albania, Algeria, American Samoa, Andorra
+smoke-test | Stopping local-postgres-ui ... done
+smoke-test | Stopping local-postgres    ... done
+smoke-test | Removing local-postgres-ui ... done
+smoke-test | Removing local-postgres    ... done
+smoke-test | Removing network scala-example_default
+smoke-test | Target github.com/earthly/earthly-example-scala/integration:main+smoke-test built successfully
=========================== SUCCESS ===========================
...
```

## Bringing It All Together

Adding these testing targets to an all target, we now can unit test, integration test, and dockerize and push our software in a single command. Using this approach, integration tests that fail sporadically for environmental reasons and can't be reproduced consistently should be a thing of the past.

```Dockerfile
all:
  BUILD +build
  BUILD +unit-test
  BUILD +integration-test
  BUILD +smoke-test
```

```bash
> earthly -P +all
...
+all | Target github.com/earthly/earthly-example-scala/integration:main+all built successfully
=========================== SUCCESS ===========================
```

There we have it, a reproducible integration process. If you have questions about the example, [ask](https://gitter.im/earthly-room/community)

## See also

* [Docker In Earthly](https://docs.earthly.dev/earthly-0.6/docs/guides/docker-in-earthly)
* [Source code for example](https://github.com/earthly/earthly/tree/main/examples/integration-test)
* [Integration Testing vs Unit Testing](https://blog.earthly.dev/unit-vs-integration/)
