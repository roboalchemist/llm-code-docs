# Testcontainers Documentation

Source: https://testcontainers.gitbook.io/llms-full.txt

---

# Introduction

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://github.com/codespaces/new?hide_repo_select=true\&ref=master\&repo=140400673\&machine=standardLinux32gb\&location=WestEurope)

## Introduction

This workshop will explain how to use Testcontainers ( <https://www.testcontainers.org> ) in your Java applications.

### Table of contents

* [Introduction](https://testcontainers.gitbook.io/workshop/readme)
* [Step 1: Getting Started](https://testcontainers.gitbook.io/workshop/step-1-getting-started)
* [Step 2: Exploring the app](https://testcontainers.gitbook.io/workshop/step-2-exploring-the-app)
* [Step 3: Adding some tests](https://testcontainers.gitbook.io/workshop/step-3-adding-some-tests)
* [Step 4: Your first Testcontainers integration](https://testcontainers.gitbook.io/workshop/step-4-your-first-testcontainers-integration)
* [Step 5: Hello, r u 200 OK?](https://testcontainers.gitbook.io/workshop/step-5-dude-r-u-200-ok)
* [Step 6: Adding Redis](https://testcontainers.gitbook.io/workshop/step-6-adding-redis)
* [Step 7: Test the API](https://testcontainers.gitbook.io/workshop/step-7-test-the-api)
* [Step 8: Edge cases](https://testcontainers.gitbook.io/workshop/step-8-edge-cases)
* [Step 9: Data initialization strategies](https://testcontainers.gitbook.io/workshop/step-9-data-init-strategies)
* [Step 10: Migrating from Docker Compose](https://testcontainers.gitbook.io/workshop/step-10-migrating-from-docker-compose)


# Step 1: Getting Started

## Check Docker

Make sure you have Docker available on your machine by running the following command:

```
$ docker version

Client:
 Cloud integration: v1.0.22
 Version:           20.10.11
 API version:       1.41
 Go version:        go1.16.10
 Git commit:        dea9396
 Built:             Thu Nov 18 00:42:51 2021
 OS/Arch:           windows/amd64
 Context:           default
Server: Docker Engine - Community
 Engine:
  Version:          20.10.11
  API version:      1.41 (minimum version 1.12)
  Go version:       go1.16.9
  Git commit:       847da18
  Built:            Thu Nov 18 00:35:39 2021
  OS/Arch:          linux/amd64
  Experimental:     false
  ...
```

## Download the project

Clone the following project from GitHub to your computer:\
<https://github.com/testcontainers/workshop>

## Build the project to download the dependencies

With Gradle:

```
# -x check - skips the tests
./gradlew build -x check
```

## (optionally) Pull the required images before doing the workshop

This might be helpful if the internet connection at the workshop venue is somewhat slow.

```
docker pull postgres:14-alpine
docker pull redis:6-alpine
docker pull openjdk:8-jre-alpine
docker pull confluentinc/cp-kafka:6.2.1
```


# Step 2: Exploring the app

The app is a simple microservice based on Spring Boot for rating conference talks. It provides an API to track the ratings of the talks in real time.

## Storage

### SQL database with the talks

When a rating is submitted, we must verify that the talk for the given ID is present in our database.

Our database of choice is PostgreSQL, accessed with Spring JDBC.

Check `com.example.demo.repository.TalksRepository`.

### Redis

We store the ratings in Redis database with Spring Data Redis.

Check `com.example.demo.repository.RatingsRepository`.

### Kafka

We use ES/CQRS to materialize the events into the state. Kafka acts as a broker and we use Spring Kafka.

Check `com.example.demo.streams.RatingsListener`.

## API

The API is a Spring Web REST controller (`com.example.demo.api.RatingsController`) and exposes two endpoints:

* `POST /ratings { "talkId": ?, "value": 1-5 }` to add a rating for a talk
* `GET /ratings?talkId=?` to get the histogram of ratings of the given talk


# Step 3: Adding some tests

The app doesn't have any tests yet. But before we write our first test, let's create an abstract test class for the things which are common between the tests.

## Abstract class

Add `com.example.demo.support.AbstractIntegrationTest` class to `src/test/java` sourceset. It should be an abstract class with standard Spring Boot's testing framework annotations on it:

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT)
```

## Our very first test

Now we need to test that the context starts.\
Add `com.example.demo.DemoApplicationTest`, extend it from your base class you just created and add a dummy test:

```java
@Test
public void contextLoads() {
}
```

Run it and verify that the application starts and the test passes. Spring will detect H2 on the classpath and use it as an embedded DB.

This is already a useful smoke test since it ensures, that Spring Boot is able to initialize the application context successfully.

## Populate the database

The context starts. However, we need to populate the database with some data before we can write the tests.

Let's add a `src/test/resources/schema.sql` file with the following content:

```sql
CREATE TABLE IF NOT EXISTS talks(
  id    VARCHAR(64)  NOT NULL,
  title VARCHAR(255) NOT NULL,
  PRIMARY KEY (id)
);

INSERT
  INTO talks (id, title)
  VALUES ('testcontainers-integration-testing', 'Modern Integration Testing with Testcontainers')
  ON CONFLICT do nothing;

INSERT
  INTO talks (id, title)
  VALUES ('flight-of-the-flux', 'A look at Reactor execution model')
  ON CONFLICT do nothing;
```

Now run the test again. Oh no, it fails!

```
...
Caused by: org.h2.jdbc.JdbcSQLException: Syntax error in SQL statement "INSERT INTO TALKS (ID, TITLE) VALUES ('testcontainers-integration-testing', 'Modern Integration Testing with Testcontainers') ON[*] CONFLICT DO NOTHING";
...
```

It seems that H2 does not support the PostgreSQL SQL syntax, at least not by default.


# Step 4: Your first Testcontainers integration

From the Testcontainers website, we learn that there is a simple way of running different supported JDBC databases with Docker:\
<https://www.testcontainers.org/usage/database_containers.html>

An especially interesting part are JDBC-URL based containers:\
<https://www.testcontainers.org/usage/database_containers.html#jdbc-url>

It means that starting to use Testcontainers in our project (once we add a dependency) is as simple as changing a few properties in Spring Boot:

```java
@SpringBootTest(webEnvironment = WebEnvironment.RANDOM_PORT, properties = {
 "spring.datasource.url=jdbc:tc:postgresql:14-alpine://testcontainers/workshop"
})
```

If we split the magical JDBC url, we see:

* `jdbc:tc:` - this part says that we should use Testcontainers as JDBC provider
* `postgresql:14-alpine://` - we use a PostgreSQL database, and we select the correct PostgreSQL image from the Docker Hub as the image
* `testcontainers/workshop` - the host name (can be anything) is `testcontainers` and the database name is `workshop`. Your choice!

After adding the properties and run the test again. Fixed? Good!

Check the logs.

```
    13:30:59.352  INFO   --- [    Test worker] o.t.d.DockerClientProviderStrategy       : Found Docker environment with local Npipe socket (npipe:////./pipe/docker_engine)
    13:30:59.369  INFO   --- [    Test worker] org.testcontainers.DockerClientFactory   : Docker host IP address is localhost
    13:30:59.431  INFO   --- [    Test worker] org.testcontainers.DockerClientFactory   : Connected to docker: 
      Server Version: 20.10.11
      API Version: 1.41
      Operating System: Docker Desktop
      Total Memory: 3929 MB
    13:31:03.294  INFO   --- [    Test worker] org.testcontainers.DockerClientFactory   : Ryuk started - will monitor and terminate Testcontainers containers on JVM exit
    13:31:03.295  INFO   --- [    Test worker] org.testcontainers.DockerClientFactory   : Checking the system...
    13:31:03.296  INFO   --- [    Test worker] org.testcontainers.DockerClientFactory   : ✔ Docker server version should be at least 1.6.0
    13:31:03.588  INFO   --- [    Test worker] org.testcontainers.DockerClientFactory   : ✔ Docker environment should have more than 2GB free disk space
```

As you can see, Testcontainers quickly discovered your environment and connected to Docker. It did some pre-flight checks as well to ensure that you have a valid environment.

## Hint 1:

Add the following line to your `~/.testcontainers.properties` file to disable these checks and speed up the tests:

```
checks.disable=true
```

## Hint 2:

Changing the PostgreSQL version is as simple as replacing `14-alpine` with, for example, `10-alpine`. Try it, but don't forget that it will download the new image from the internet, if it's not already present on your computer.


# Step 5: Hello, r u 200 OK?

One of the great features of Spring Boot is the Actuator and its health endpoint. It gives you an overview how healthy your app is.

The context starts, but what's about the health of the app?

## Configure Rest Assured

To check the health endpoint of our app, we will use the [RestAssured](http://rest-assured.io/) library.

However, before using it, we first need to configure it. Add the following to your abstract test class since we will share it between all tests:

```java
protected RequestSpecification requestSpecification;

@LocalServerPort
protected int localServerPort;

@BeforeEach
public void setUpAbstractIntegrationTest() {
    RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();
    requestSpecification = new RequestSpecBuilder()
            .setPort(localServerPort)
            .addHeader(
                    HttpHeaders.CONTENT_TYPE,
                    MediaType.APPLICATION_JSON_VALUE
            )
            .build();
}
```

Here we ask Spring Boot to inject the random port it received at the start of the app, so that we can pre-configure RestAssured's requestSpecification.

## Call the endpoint

Now let's check if the app is actually healthy by doing the following in our `DemoApplicationTest`:

```java
@Test
public void healthy() {
    given(requestSpecification)
            .when()
            .get("/actuator/health")
            .then()
            .statusCode(200)
            .log().ifValidationFails(LogDetail.ALL);
}
```

If we run the test, it will fail:

```
...
HTTP/1.1 503 Service Unavailable
transfer-encoding: chunked
Content-Type: application/vnd.spring-boot.actuator.v2+json;charset=UTF-8

{
    "status": "DOWN",
    "details": {
        "diskSpace": { ... },
        "redis": {
            "status": "DOWN",
            "details": {
                "error": "org.springframework.data.redis.RedisConnectionFailureException: Unable to connect to Redis; nested exception is io.lettuce.core.RedisConnectionException: Unable to connect to localhost:6379"
            }
        },
        "db": {
            "status": "UP",
            "details": {
                "database": "PostgreSQL",
                "hello": 1
            }
        }
    }
}
... 
Expected status code <200> but was <503>.
```

It seems that it couldn't find Redis and there is no autoconfigurable option for it.


# Step 6: Adding Redis

The simplest way to provide a Redis instance for your tests is to use `GenericContainer` with a Redis Docker image: <https://www.testcontainers.org/usage/generic_containers.html> The integration between the tests code and Testcontainers is straightforward.

## Rules? No thanks!

Testcontainers comes with first class support for JUnit, but in our app we want to have a single Redis instance shared between **all** tests. Luckily, there are the `.start()`/`.stop()` methods of `GenericContainer` to start or stop it manually.

Just add the following code to your `AbstractIntegrationTest` with the following code:

```java
static final GenericContainer redis = new GenericContainer("redis:6-alpine")
                                            .withExposedPorts(6379);

@DynamicPropertySource
public static void configureRedis(DynamicPropertyRegistry registry) {
  redis.start();
  registry.add("spring.redis.host", redis::getHost);
  registry.add("spring.redis.port", redis::getFirstMappedPort);
}
```

Simple and beautiful, huh?

Run the tests, now they should all pass.


# Step 7: Test the API

Now let's create a test for our API which will verify the business logic.

```java
package com.example.demo.api;

import com.example.demo.model.Rating;
import com.example.demo.support.AbstractIntegrationTest;
import org.junit.jupiter.api.Test;

import static io.restassured.RestAssured.given;
import static org.awaitility.Awaitility.await;
import static org.hamcrest.Matchers.is;

public class RatingsControllerTest extends AbstractIntegrationTest {

    @Test
    public void testRatings() {
        String talkId = "testcontainers-integration-testing";

        given(requestSpecification)
                .body(new Rating(talkId, 5))
                .when()
                .post("/ratings")
                .then()
                .statusCode(202);

        await().untilAsserted(() -> {
            given(requestSpecification)
                    .queryParam("talkId", talkId)
                    .when()
                    .get("/ratings")
                    .then()
                    .body("5", is(1));
        });

        for (int i = 1; i <= 5; i++) {
            given(requestSpecification)
                    .body(new Rating(talkId, i))
                    .when()
                    .post("/ratings");
        }

        await().untilAsserted(() -> {
            given(requestSpecification)
                    .queryParam("talkId", talkId)
                    .when()
                    .get("/ratings")
                    .then()
                    .body("1", is(1))
                    .body("2", is(1))
                    .body("3", is(1))
                    .body("4", is(1))
                    .body("5", is(2));
        });
    }

    @Test
    public void testUnknownTalk() {
        String talkId = "cdi-the-great-parts";

        given(requestSpecification)
                .body(new Rating(talkId, 5))
                .when()
                .post("/ratings")
                .then()
                .statusCode(404);
    }
}
```

Run it, and it will fail.

Why?

There is no Kafka!

Running Kafka in Docker is easy with Testcontainers. There is a Testcontainers module providing integration with Kafka and the `KafkaContainer` abstraction for your code.

Just add it the same way as you added Redis and set the `spring.kafka.bootstrap-servers` system property.

## Hint 1:

Some containers expose helper methods. Check if there is one on `KafkaContainer` which might help you.

## Hint 2:

You can start several containers in parallel by doing:

```java
Stream.of(redis, kafka).parallel().forEach(GenericContainer::start);
```


# Step 8: Edge cases

Redis has its own limits. Are there any limits of Hash's increment? Let's figure out!

## `RatingsRepositoryTest`

We're going to create an isolated test for the Redis-based repository and verify our edge cases.

```java
package com.example.demo.repository;

import org.junit.jupiter.api.Test;

import static org.assertj.core.api.Assertions.assertThat;

public class RatingsRepositoryTest {

    final String talkId = "testcontainers";

    RatingsRepository repository;

    @Test
    public void testEmptyIfNoKey() {
        assertThat(repository.findAll(talkId)).isEmpty();
    }

    @Test
    public void testLimits() {
        repository.redisTemplate.opsForHash()
                .put(repository.toKey(talkId), "5", Long.MAX_VALUE + "");

        repository.add(talkId, 5);
    }
}
```

But since we're not using Spring Context here, we need to create an instance of our repository ourselves:

```java
    @BeforeEach
    public void setUp() {
        LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory(
                ?,
                ?
        );
        connectionFactory.afterPropertiesSet();
        repository = new RatingsRepository(new StringRedisTemplate(connectionFactory));
    }
```

The only missing part is `LettuceConnectionFactory`'s arguments, Redis' host and port.

We will use Testcontainers' JUnit Jupiter extension for starting Redis:

```java
    @Container
    public GenericContainer redis = new GenericContainer("redis:3-alpine")
            .withExposedPorts(6379);
```

And add the `@Testcontainers` annotation to the class:

```java
@Testcontainers
public class RatingsRepositoryTest {
```

And the code for initializing the connection factory:

```java
LettuceConnectionFactory connectionFactory = new LettuceConnectionFactory(
        redis.getHost(),
        redis.getFirstMappedPort()
);
```

The test should fail with a somewhat cryptic error:

```
Error in execution; nested exception is io.lettuce.core.RedisCommandExecutionException: ERR increment or decrement would overflow
```

And there's nothing on your side to fix, the test is pushing the boundaries of Redis.\
But on the bright side we learned how to use Testcontainers outside of the Spring Framework. We also saw how we can utilize to learn about the limitations and behavior of extra components.

Delete the test before anyone notices. Just kidding, let's turn this into a useful test by asserting we throw a custom exception `MaxRatingsAddedException`, which indicates that our repository recorded the maximum amount of ratings. In the future we can still make a different decision of how our business logic should deal with this (and if this is even an edge-case worth solving), but with this test, we consciously documented our knowledge of the limitations of the systems we integrate against.

```java
@Test
public void testLimits() {
    repository.redisTemplate.opsForHash()
        .put(repository.toKey(talkId), "5", Long.MAX_VALUE + "");

        Assertions.assertThrows(MaxRatingsAddedException.class, () ->  repository.add(talkId, 5));
}
```

The final exercise is now to adapt the implementation of `RatingsRepository.add()` accordingly, to make the test pass.


# Step 9: Data initialization strategies

Initializing data using Spring is neat, but sometimes you might need alternative solutions.

In this step we're going to turn off the Spring's database initialization, and explore how we can initialize the database using container specific configuration, followed by switching to using the [Flyway](https://flywaydb.org/) migrations.

## Assert the data is really there

To make the task run or fail faster, add a testcase to `DemoApplicationTest` which checks that the data from `schema.sql` is loaded into the database properly. For that you can `@Autowire` the `talks` repository into the test class and use it to verify that a talk with a given ID can be found in the database.

```java
Assertions.assertTrue(talks.exists("testcontainers-integration-testing"));
```

## Running PostgreSQL explicitly

First of all, we'll remove the Testcontainers "modified JDBC URL" approach and create an explicit PostgreSQL container object to simplify further configuration.

In the `AbstractIntegratonTest` please remove `properties` from `@SpringBootTest(...)` altogether.

Then you can instantiate a PostgreSQL container using:

```java
PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:14-alpine");
```

Additionally, we need to start `postgres` container similar to the other service dependencies and configure our application to use that containerized database which can be done by setting the following properties in the `@DynamicPropertySource` annotated method:

```
spring.datasource.url
spring.datasource.username
spring.datasource.password
```

Use the values provided by the `postgres` object to fill the required configuration.

Running the test added in the beginning of this Step should pass now.

## Initialize the DB without Spring

It might happen that loading `schema.sql` is not enough to fully initialize the database. We are going to simulate that by circumventing the Spring's convention. Please rename `schema.sql` to `talks-schema.sql`. The test should fail now since the schema isn't initialized in the database container and without it the app cannot function properly.

Make the database initialization work again (and the test pass) by initializing the DB directly in the container.

### Hint

Most database containers have functionality to initialize the Database from the script files provided in the container.\
The PostgreSQL container happens to run all SQL files from `/docker-entrypoint-initdb.d/` directory, as described in the *Initialization scripts* chapter of the [Postgres container](https://hub.docker.com/_/postgres/) docs.

Configure the `postgres` object using the `withCopyToContainer` method and `MountableFile.forClasspathResource(String path)` to configure the database schema. After you initialize the DB correctly, the test should work again (despite *not* having the `schema.sql` file).

## Migrating the DB with Flyway

Next, we're going to remove the data initialization queries from the `talks-schema.sql` file and use [Flyway](https://flywaydb.org/) for populating the DB with actual data. Liquibase or other database migration tools would work similarly.

Please add the Flyway dependency in `build.gradle`:

```
implementation 'org.flywaydb:flyway-core'
```

or `pom.xml`:

```
<dependency>
    <groupId>org.flywaydb</groupId>
    <artifactId>flyway-core</artifactId>
</dependency>
```

Next, move all the `INSERT ...` statements from the `talks-schema.sql` to `src/main/resources/db/migration/V1_1__talks.sql` file.

Note that the migrations file is not on the **test** classpath, as Flyway is likely to be used for production schema management as well.

For Flyway not to complain that it can't store its data in the DB, we need to configure it to create its missing database management tables and data.

This can be done in `application.yml` with:

```yaml
  flyway:
    baseline-on-migrate: true
```

Note that `spring.flyway.locations=classpath:db/migration` is the default location for the migration files used by Flyway so we don't need to configure that explicitly. For more details on Spring Boot and Flyway integration please refer to [Spring manual](https://docs.spring.io/spring-boot/docs/2.6.7/reference/htmlsingle/#howto.data-initialization.migration-tool.flyway).

The test verifying that the data is correctly initialized in the Database should pass after we configure Flyway to run the migrations correctly.


# Step 10: Migrating from Docker Compose

We don't always encounter green field projects. Maybe you are already invested some time in using Docker Compose to spin up your test environment and are wondering how to get started from here?

Let's look into how Testcontainers can support you on this journey.

## `Dockerfile` and `docker-compose.yml`

Let's assume we did start out with running our application as a Docker container as well, using the following, pretty standard, Dockerfile:

```
FROM openjdk:8-jre-alpine
RUN addgroup -S spring && adduser -S spring -G spring
USER spring:spring
ARG JAR_FILE=build/libs/*.jar
COPY ${JAR_FILE} app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
```

We also need to make sure the Spring-Boot jar has been built:

```bash
./gradlew bootJar
```

Finally, we have a Docker Compose file, that automatically builds the app image and spins it up, together with all dependencies:

```yaml
version: "2.4"
services:
  app:
    build: .
    environment:
      SPRING_REDIS_HOST: "redis"
      SPRING_REDIS_PORT: "6379"
      SPRING_KAFKA_BOOTSTRAP_SERVERS: "PLAINTEXT://kafka:9093"
      SPRING_DATASOURCE_URL: "jdbc:postgresql://db:5432/workshop"
      SPRING_DATASOURCE_USERNAME: "postgres"
      SPRING_DATASOURCE_PASSWORD: "example"
    ports:
      - "8080:8080"
  db:
    image: "postgres:14-alpine"
    environment:
      POSTGRES_PASSWORD: example
      POSTGRES_DB: workshop
    volumes:
      - "./src/test/resources/talks-schema.sql:/docker-entrypoint-initdb.d/schema.sql"
  redis:
    image: "redis:6-alpine"
  kafka:
    image: "confluentinc/cp-kafka:6.2.1"
    environment:
      KAFKA_ZOOKEEPER_CONNECT: 'zookeeper:2181'
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://kafka:9093
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: "1"
      KAFKA_OFFSETS_TOPIC_NUM_PARTITIONS: "1"
  zookeeper:
    image: confluentinc/cp-zookeeper:7.1.1
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

```

We have a traditional JUnit Jupiter test `DockerComposeApplicationTest`, which assumes the application is running at `localhost:8080`:

```java
package com.example.demo;

import com.example.demo.model.Rating;
import io.restassured.RestAssured;
import io.restassured.builder.RequestSpecBuilder;
import io.restassured.filter.log.LogDetail;
import io.restassured.specification.RequestSpecification;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;

import static io.restassured.RestAssured.given;
import static org.awaitility.Awaitility.await;
import static org.hamcrest.Matchers.is;

public class DockerComposeApplicationTest  {

    protected RequestSpecification requestSpecification;

    @BeforeEach
    public void setUpAbstractIntegrationTest() {
        RestAssured.enableLoggingOfRequestAndResponseIfValidationFails();
        requestSpecification = new RequestSpecBuilder()
                .setPort(8080)
                .addHeader(
                        HttpHeaders.CONTENT_TYPE,
                        MediaType.APPLICATION_JSON_VALUE
                )
                .build();
    }

    @Test
    public void healthy() {
        given(requestSpecification)
                .when()
                .get("/actuator/health")
                .then()
                .statusCode(200)
                .log().ifValidationFails(LogDetail.ALL);
    }

    @Test
    public void testRatings() {
        String talkId = "testcontainers-integration-testing";

        given(requestSpecification)
                .body(new Rating(talkId, 5))
                .when()
                .post("/ratings")
                .then()
                .statusCode(202);

        await().untilAsserted(() -> {
            given(requestSpecification)
                    .queryParam("talkId", talkId)
                    .when()
                    .get("/ratings")
                    .then()
                    .body("5", is(1));
        });

        for (int i = 1; i <= 5; i++) {
            given(requestSpecification)
                    .body(new Rating(talkId, i))
                    .when()
                    .post("/ratings");
        }

        await().untilAsserted(() -> {
            given(requestSpecification)
                    .queryParam("talkId", talkId)
                    .when()
                    .get("/ratings")
                    .then()
                    .body("1", is(1))
                    .body("2", is(1))
                    .body("3", is(1))
                    .body("4", is(1))
                    .body("5", is(2));
        });
    }

}
```

To run this rest, make sure the Docker Compose setup is running:

```bash
docker compose up
```

You can run the tests directly from the IDE.

Afterwards, you can stop the Docker Compose services again:

```bash
docker compose down -v
```

## Migrating to `DockerComposeContainer`

In order to tightly integrate the lifecycle of our test environment with the lifecycle of our tests, we can already integrate Testcontainers and still make use of our existing `docker-compose.yml`:

```java
@Container
static DockerComposeContainer composeContainer = new DockerComposeContainer(new File("docker-compose.yml"))
        .withLocalCompose(true)
        .withExposedService("app_1", 8080)
        .waitingFor("app_1", Wait.forHttp("/actuator/health"));
```

You also need to add the `@Testcontainers` annotation to the test class, if you want the [Testcontainers-JUnit-Jupiter extension](https://www.testcontainers.org/test_framework_integration/junit_5/) to manage the container lifecycle (similar to how we did in step 8).

Finally, make sure to configure RestAssured to access the dynamic port exposed by Testcontainers:

```java
requestSpecification = new RequestSpecBuilder()
    .setBaseUri(String.format("http://%s:%d", composeContainer.getHost(), composeContainer.getServicePort("app_1", 8080)))
    .addHeader(
            HttpHeaders.CONTENT_TYPE,
            MediaType.APPLICATION_JSON_VALUE
    )
    .build();
```

Run the test from the IDE, it works! Note how you don't need to run `docker compose` before the test, or manually clean up the environment after.

## Migrating to individual Testcontainers objects

Instead of defining the necessary services in the `docker-compose.yml` file, we will now declare them as Java objects. Furthermore, we make use of the Docker networking feature, so that we can hardcode connection URLs and leverage the Docker DNS features.

```java
static Network network = Network.newNetwork();

@Container
static final GenericContainer redis = new GenericContainer("redis:6-alpine")
        .withExposedPorts(6379)
        .withNetwork(network)
        .withNetworkAliases("redis");

@Container
static final KafkaContainer kafka = new KafkaContainer (
        DockerImageName.parse("confluentinc/cp-kafka:6.2.1"))
        .withNetwork(network)
        .withNetworkAliases("kafka");


@Container
static final PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>("postgres:14-alpine")
        .withCopyFileToContainer(MountableFile.forClasspathResource("/talks-schema.sql"), "/docker-entrypoint-initdb.d/")
        .withNetwork(network)
        .withNetworkAliases("db");
```

Testcontainers also allows to build images as part of the test execution and run the corresponding container. We will use this for our Spring-Boot application:

```java
@Container
static final GenericContainer appContainer = new GenericContainer<>(
        new ImageFromDockerfile()
                .withFileFromPath("Dockerfile", Paths.get("Dockerfile"))
                .withFileFromPath("build/libs/workshop.jar", Paths.get("build/libs/workshop.jar"))
)
    .withExposedPorts(8080)
    .withEnv("SPRING_REDIS_HOST", "redis")
    .withEnv("SPRING_REDIS_PORT", "6379")
    .withEnv("SPRING_KAFKA_BOOTSTRAP_SERVERS", "BROKER://kafka:9092")
    .withEnv("SPRING_DATASOURCE_URL", "jdbc:postgresql://db:5432/test")
    .withEnv("SPRING_DATASOURCE_USERNAME", "test")
    .withEnv("SPRING_DATASOURCE_PASSWORD", "test")
    .withNetwork(network)
    .waitingFor(Wait.forHttp("/actuator/health"))
    .dependsOn(redis, kafka, postgres);
```

Notice that we can also use the `dependsOn()` method, to control the startup order of our containers. As compared to the `dependsOn` config in Docker Compose, this will fully utilize Testcontainers' `WaitStrategy` support, to ensure the applications in the container are in a ready-to-use state.

Don't forget to configure RestAssured accordingly to use the `appContainer` details:

```java
requestSpecification = new RequestSpecBuilder()
    .setBaseUri(String.format("http://%s:%d", appContainer.getHost(), appContainer.getFirstMappedPort()))
    .addHeader(
            HttpHeaders.CONTENT_TYPE,
            MediaType.APPLICATION_JSON_VALUE
    )
    .build();
```

Now let's run the test again.

## Moving back to `@SpringBootTest`

From this point, is just a small step to move our setup back to a `@SpringBootTest`. But why would we want to do this? Using `@SpringBootTest` bring a couple quality-of-life improvements for us as developers, such as faster feedback cycles (we don't have to rebuild the whole application and the image) or much easier debugging of the Java process.

So let's make our test a `@SpringBootTest` again, by annotating it:

```java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
```

We will also use the random local port:

```java
@LocalServerPort
protected int localServerPort;
```

And now we can use the `@DynamicPropertySource` method to comfortably configure the Spring-Boot application to use the containerized service dependencies.

```java
@DynamicPropertySource
public static void configureRedis(DynamicPropertyRegistry registry){
    Stream.of(redis,kafka,postgres).parallel().forEach(GenericContainer::start);
    registry.add("spring.redis.host",redis::getHost);
    registry.add("spring.redis.port",redis::getFirstMappedPort);
    registry.add("spring.kafka.bootstrap-servers",kafka::getBootstrapServers);
    registry.add("spring.datasource.url",postgres::getJdbcUrl);
    registry.add("spring.datasource.username",postgres::getUsername);
    registry.add("spring.datasource.password",postgres::getPassword);
}
```

Note that our test now looks very similar to the tests that we created when following the best practices of using Testcontainers from scratch.


