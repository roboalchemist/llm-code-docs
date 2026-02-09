# Source: https://docs.upsun.com/languages/java/migration.md

# Moving a Java application to Upsun Fixed


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

It is common to have a Java application that you want to migrate to Upsun.
Upsun supports several styles of Java application, such as monolith, microservices, stateful, and stateless.

## Minimum Requirement

To run a Java application at Upsun you need:

* [A supported Java version](https://docs.upsun.com/languages/java.md#supported-versions)
* [A build management tool](https://docs.upsun.com/languages/java.md#support-build-automation)
  * [Gradle](https://docs.gradle.org/current/userguide/gradle_wrapper.md)
  * [Maven](https://maven.apache.org/)
  * [Maven Wrapper](https://www.baeldung.com/maven-wrapper)
  * [Ant](https://ant.apache.org/)
* A Git Repository:
  * [GitHub](https://docs.upsun.com/integrations/source/github.md)
  * [BitBucket](https://docs.upsun.com/integrations/source/bitbucket.md)
  * [GitLab](https://docs.upsun.com/integrations/source/gitlab.md)
  * The default Git repository provided by Upsun

**Note**: 

A container application can’t be bigger than **8 GB** of memory.
For more details, see [tuning](https://docs.upsun.com/languages/java/tuning.md).

## Monolith/Single Application

To start a Java application, you need to understand the [Upsun structure](https://docs.upsun.com/learn/overview/structure.md).
You will need to configure your [application](https://docs.upsun.com../../create-apps/_index.md), [routes](https://docs.upsun.com../../define-routes.md),
and [services](https://docs.upsun.com../../add-services.md).

### Application

```yaml  {location=".upsun/config.yaml"}
applications:
  myapp:
    type: 'java:<VERSION>'

    hooks:
      build: [2]
    web:
      commands:
        start: [3]
```
1. [A Java version](https://docs.upsun.com/languages/java.md#supported-versions), e,g.: `java:21`
2. [Hooks define what happens when building the application](https://docs.upsun.com../../create-apps/hooks.md). This build process typically generates an executable file such as a uber-jar. For example, `mvn clean package`.
3. [The commands key defines the command to launch the application](create-apps/image-properties/web.md#web-commands). For example,  `java -jar file.jar`.
4. In the start's command needs to receive the port where the application will execute thought the `PORT` environment. That's best when your app follows the port bind principle. For example, `java -jar jar --port=$PORT`.

**Note**: 

Be aware that after the build, it creates a read-only system. You have the [mount option to create a writable folder](https://docs.upsun.com/create-apps/image-properties/mounts.md).

### Route

```yaml  {location=".upsun/config.yaml"}
routes:
  "https://{default}/":
    type: upstream
    upstream: "myapp:http" [1]
  "https://www.{default}/":
    type: redirect
    to: "https://{default}/"

applications:
  myapp:
    type: 'java:<VERSION>'

    hooks:
      build: [2]
    web:
      commands:
        start: [3]
```
1. It defines the application will link in the route. For example,`"myapp:http"`.

**Note**: 

Application instances have a limited amount of memory at build time, which has a maximum of 8 GB.
At runtime that limit depends on [the resources you have defined for your application container](https://docs.upsun.com/manage-resources.md) using ``upsun resources:set``.
A stateless application can be scaled horizontally to multiple application instances with ``upsun resources:set`` or by using Varnish in a [load balancer](https://support.platform.sh/hc/en-us/community/posts/16439676899474) configuration.

## Microservices

You have the option to use several languages in microservices. If you're using Java there are several options to aggregate these services into a microservices:

* [Maven Modules](https://maven.apache.org/guides/mini/guide-multiple-modules.md)
* [Gradle Multi-project](https://guides.gradle.org/creating-multi-project-builds/)
* [Git submodules](https://docs.upsun.com/development/submodules.md)

[Upsun supports multiple applications](https://docs.upsun.com../../create-apps/multi-app.md) and there are two options:

* One application YAML file to each application
* Aggregate all applications in a single file with an `.upsun/config.yaml` file

| Article                                                      | Content                                                      |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Microservices in the cloud, part two](https://devcenter.upsun.com/posts/microservices-in-the-cloud-part-two/) | [Source](https://github.com/EventosJEspanol/latin-america-micro-profile) |
| [Microservices in the cloud, part one](https://upsun.com/blog/) | [Source](https://github.com/EventosJEspanol/latin-america-micro-profile) |
| [Multiple Applications](https://support.platform.sh/hc/en-us/community/posts/16439649733010) | [Source](https://github.com/platformsh-examples/tomcat-multi-app) |
| [Configure multi-applications with `.upsun/config.yaml`](https://support.platform.sh/hc/en-us/community/posts/16439676928274) | [Source](https://github.com/platformsh-examples/tomcat-multi-app-applications) |

**Note**: 

You can load balance to some or [all applications in the project cluster](https://support.platform.sh/hc/en-us/community/posts/16439662235026).

While the table above shows examples for Upsun Fixed rather than for Upsun Flex, the same rules apply with only slight changes in configuration.

## Access to managed services

Upsun provides [managed services](https://docs.upsun.com/add-services.md) such as databases, cache and search engines.
However, you can use a database or any services such as a transition process, just be aware of the [firewall](https://docs.upsun.com/create-apps/image-properties/firewall.md).

When applications need to access a service, it is important to include the [`relationships` key](https://docs.upsun.com/create-apps/image-properties/relationships.md).
By default an application may not talk to any other container without a `relationship` explicitly allowing access.

To connect to a service from your deployed application, you need to pass the relationships information into your application's configuration.
The way to do so varies with the application.
The most common mechanisms are listed below.

### Overwrite

If you are using a framework that follows the [Twelve-Factor App](https://12factor.net/) methodology, particularly the [third point](https://12factor.net/config), you can configure the application directly from environment variables.
Examples of such frameworks include Spring, Eclipse MicroProfile Config, Quarkus, and Micronauts.

Service credentials are available within the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables), or the [`PLATFORM_RELATIONSHIPS` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

```bash {}
export DB_HOST="$POSTGRESQL_HOST"
```

This sets environment variables with the names your app needs,
and the values from [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).
This variable is a base64-encoded JSON object with keys of the relationship name and values of arrays of relationship endpoint definitions.
Upsun supports the [jq](https://stedolan.github.io/jq/), which allows to extract information from this JSON.

    .environment

```bash {}
export DB_HOST="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq -r '.postgresql[0].host')"
```

This sets environment variables with names your app needs and the values from [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

| Article                                                      | Source                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Spring Data MongoDB](https://support.platform.sh/hc/en-us/community/posts/16439654854802) | [Source](https://github.com/platformsh-examples/java-overwrite-configuration/tree/master/spring-mongodb) |
| [Jakarta EE/MicroProfile Config](https://support.platform.sh/hc/en-us/community/posts/16439700735122) | [Source](https://github.com/platformsh-examples/java-overwrite-configuration/tree/master/jakarta-nosql) |
| [Spring Data JPA](https://support.platform.sh/hc/en-us/community/posts/16439669562130) | [Source](https://github.com/platformsh-examples/java-overwrite-configuration/tree/master/spring-jpa) |
| [Payara JPA](https://support.platform.sh/hc/en-us/community/posts/16439658290194) | [Source](https://github.com/platformsh-examples/java-overwrite-configuration/blob/master/payara/README.md) |

**Note**: 

While the table above shows examples for Upsun Fixed rather than for Upsun Flex, the same rules apply with only slight changes in configuration.

To reduce the number of lines in the application file and to make it cleaner,
you have the option to move the variable environment to another file: a [`.environment` file](https://docs.upsun.com../../development/variables/set-variables.md#set-variables-via-script).

**Example:**

You can obtain relationship information through the [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables) themselves,
or through the [`PLATFORM_RELATIONSHIPS` environment variable](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).
Say your application has a relationship named ``postgresql`` to a database service named `postgresql`:

```bash {}
export DB_HOST="${POSTGRESQL_HOST}"
export DB_PASSWORD="${POSTGRESQL_PASSWORD}"
export DB_USER="${POSTGRESQL_USERNAME}"
export DB_DATABASE="${POSTGRESQL_PATH}"
export JDBC="jdbc:postgresql://${HOST}/${DATABASE}"
export JAVA_MEMORY="-Xmx$(jq .info.limits.memory /run/config.json)m"
export JAVA_OPTS="$JAVA_MEMORY -XX:+ExitOnOutOfMemoryError"
```

This sets environment variables with the names your app needs,
and the values from [service environment variables](https://docs.upsun.com/development/variables.md#service-environment-variables).This ``PLATFORM_RELATIONSHIPS`` variable is a base64-encoded JSON object with keys of the relationship name and values of arrays of relationship endpoint definitions.
Upsun supports the [jq](https://stedolan.github.io/jq/), which allows to extract information from this JSON.

    .environment

```bash {}
export DB_HOST="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq -r ".postgresql[0].host')"
export DB_PASSWORD="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq -r ".postgresql[0].password')"
export DB_USER="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq -r ".postgresql[0].username')"
export DB_DATABASE="$(echo "$PLATFORM_RELATIONSHIPS" | base64 --decode | jq -r ".postgresql[0].path')"
export JDBC="jdbc:postgresql://${HOST}/${DATABASE}"
export JAVA_MEMORY="-Xmx$(jq .info.limits.memory /run/config.json)m"
export JAVA_OPTS="$JAVA_MEMORY -XX:+ExitOnOutOfMemoryError"
```

This sets environment variables with names your app needs and the values from [PLATFORM_RELATIONSHIPS](https://docs.upsun.com/development/variables/use-variables.md#use-provided-variables).

This `.environment` file can interact to each application file.

**Example:**

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'java:21'
    hooks:
      build: ./mvnw package -DskipTests -Dquarkus.package.uber-jar=true
    relationships:
      postgresql:
    web:
      commands:
        start: java -jar $JAVA_OPTS $CREDENTIAL -Dquarkus.http.port=$PORT jarfile.jar
```

