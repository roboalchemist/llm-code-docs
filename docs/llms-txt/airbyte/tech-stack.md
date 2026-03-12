# Source: https://docs.airbyte.com/platform/understanding-airbyte/tech-stack.md

# Source: https://docs.airbyte.com/platform/2.0/understanding-airbyte/tech-stack.md

# Source: https://docs.airbyte.com/platform/1.8/understanding-airbyte/tech-stack.md

# Source: https://docs.airbyte.com/platform/1.7/understanding-airbyte/tech-stack.md

# Source: https://docs.airbyte.com/platform/1.6/understanding-airbyte/tech-stack.md

# Technical Stack

Copy Page

## Airbyte Core Backend[​](#airbyte-core-backend "Direct link to Airbyte Core Backend")

* [Java 21](https://jdk.java.net/archive/)
* Framework: [Micronaut](https://micronaut.io/)
* API: [OAS3](https://www.openapis.org/)
* Databases: [PostgreSQL](https://www.postgresql.org/)
* Unit & E2E testing: [JUnit 5](https://junit.org/junit5)
* Orchestration: [Temporal](https://temporal.io)

## Connectors[​](#connectors "Direct link to Connectors")

Connectors can be written in any language. However the most common languages are:

* Python 3.9 or higher
* [Java 21](https://jdk.java.net/archive/)

## **Frontend**[​](#frontend "Direct link to frontend")

* [Node.js](https://nodejs.org/en/)
* [TypeScript](https://www.typescriptlang.org/)
* Web Framework/Library: [React](https://reactjs.org/)

## Additional Tools[​](#additional-tools "Direct link to Additional Tools")

* CI/CD: [GitHub Actions](https://github.com/features/actions)
* Containerization: [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
* Linter (Frontend): [ESLint](https://eslint.org/)
* Formatter (Frontend & Backend): [Prettier](https://prettier.io/)
* Formatter (Backend): [Spotless](https://github.com/diffplug/spotless)

## FAQ[​](#faq "Direct link to FAQ")

### *Why do we write most destination/database connectors in Java?*[​](#why-do-we-write-most-destinationdatabase-connectors-in-java "Direct link to why-do-we-write-most-destinationdatabase-connectors-in-java")

JDBC makes writing reusable database connector frameworks fairly easy, saving us a lot of development time.

### *Why are most REST API connectors written in Python?*[​](#why-are-most-rest-api-connectors-written-in-python "Direct link to why-are-most-rest-api-connectors-written-in-python")

Most contributors felt comfortable writing in Python, so we created a [Python CDK](/platform/1.6/connector-development/cdk-python/.md) to accelerate this development. You can write a connector from scratch in any language as long as it follows the [Airbyte Specification](/platform/1.6/understanding-airbyte/airbyte-protocol.md).

### *Why did we choose to build the server with Java?*[​](#why-did-we-choose-to-build-the-server-with-java "Direct link to why-did-we-choose-to-build-the-server-with-java")

Simply put, the team has more experience writing production Java code.

### *Why do we use* [*Temporal*](https://temporal.io) *for orchestration?*[​](#why-do-we-use-temporal-for-orchestration "Direct link to why-do-we-use-temporal-for-orchestration")

Temporal solves the two major hurdles that exist in orchestrating hundreds to thousands of jobs simultaneously: scaling state management and proper queue management. Temporal solves this by offering primitives that allow serialising the jobs' current runtime memory into a DB. Since a job's entire state is stored, it's trivial to recover from failures, and it's easy to determine if a job was assigned correctly.
