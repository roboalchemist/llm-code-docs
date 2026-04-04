# Source: https://docs.upsun.com/languages/java.md

# Java


p:last-child]:mb-0 [&>h3]:mt-0 rounded-lg" >

### Note
You can now use composable image to install runtimes and tools in your application container. To find out more, see the [Composable image](https://docs.upsun.com/create-apps/app-reference/composable-image.md) topic.

Java is a general-purpose programming language, and one of the most popular in the world today. Upsun supports Java runtimes that can be used with build management tools such as Gradle, Maven, and Ant.

## Supported versions

You can select the major version. But the latest compatible minor version is applied automatically and can’t be overridden.

Patch versions are applied periodically for bug fixes and the like. When you deploy your app, you always get the latest available patches.

### OpenJDK versions:

   - 21

   - 17

These versions refer to the headless packages of OpenJDK.
To save space and reduce potential vulnerabilities, they don't contain GUI classes, which can't be used on the server.

### Specify the language

To use Java, specify `java` as your [app's `type`](https://docs.upsun.com/create-apps/app-reference/single-runtime-image.md#types):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  <APP_NAME>:
    type: 'java:<VERSION_NUMBER>'
```

For example:

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'java:21'
```

## Support build automation

Upsun supports the most common project management tools in the Java ecosystem, including:

* [Gradle](https://gradle.org/)
* [Maven](https://maven.apache.org/)
* [Ant](https://ant.apache.org/)

### Manage Maven versions

Java containers come with a version of Maven already installed.
You may need to use a specific different version to manage your project.
If the version you need differs from the version on your container, you can install the specific version that you need.

Add something like the following to your [app configuration](https://docs.upsun.com../../create-apps/_index.md):

```yaml  {location=".upsun/config.yaml"}
applications:
  # The app's name, which must be unique within the project.
  myapp:
    type: 'java:21'

    variables:
      env:
        MAVEN_VERSION: <DESIRED_VERSION_NUMBER>

    hooks:
      build: |
        curl -sfLO "https://dlcdn.apache.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz"
        tar -zxf apache-maven-$MAVEN_VERSION-bin.tar.gz
        export PATH="$PWD/apache-maven-$MAVEN_VERSION/bin:$PATH"
        mvn --version
        mvn clean package
```
## Other JVM languages

It’s worth remembering that the JVM by its specification [doesn't read Java code](https://docs.oracle.com/javase/specs/jvms/se8/html/index.md), but bytecode. So within the JVM, it’s possible to [run several languages](https://en.wikipedia.org/wiki/List_of_JVM_languages). Upsun supports several of them, such as Kotlin, Groovy, and Scala, so long as that language works with any build automation that Upsun supports.

| Article                                                      | Link                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [Kotlin and Spring](https://devcenter.upsun.com/posts/ready-to-have-fun-try-kotlin-and-spring/) | [Source](https://github.com/platformsh-templates/spring-kotlin) |
| [Scala and Spring](https://dzone.com/articles/spring-scala-cloud-psh) | [Source](https://github.com/platformsh-examples/scala)       |

**Note**: 

While the table above shows examples for Upsun Fixed rather than for Upsun, the same rules apply with only slight changes in configuration.

## Accessing services

You can access service credentials to connect to [managed services](https://docs.upsun.com/add-services/) from environment variables present in the application container.
Consult each of the individual service documentation to see how to retrieve and surface credentials into your application.

- [Chroma](https://docs.upsun.com/add-services/chroma.md#3-use-the-relationship-in-your-application)

- [ClickHouse](https://docs.upsun.com/add-services/clickhouse.md#usage-example)

- [Elasticsearch](https://docs.upsun.com/add-services/elasticsearch.md#use-in-app)

- [Edgee (Edge Analytics)](https://docs.upsun.com/add-services/edgee.md#setup-edgee)

- [Gotenberg](https://docs.upsun.com/add-services/gotenberg.md#usage-example)

- [Headless Chrome](https://docs.upsun.com/add-services/headless-chrome.md#use-in-app)

- [InfluxDB](https://docs.upsun.com/add-services/influxdb.md#use-in-app)

- [Kafka](https://docs.upsun.com/add-services/kafka.md#use-in-app)

- [MariaDB/MySQL](https://docs.upsun.com/add-services/mysql.md#use-in-app)

- [Memcached](https://docs.upsun.com/add-services/memcached.md#use-in-app)

- [Mercure](https://docs.upsun.com/add-services/mercure.md#use-in-app)

- [MongoDB](https://docs.upsun.com/add-services/mongodb.md#use-in-app)

- [Network Storage](https://docs.upsun.com/add-services/network-storage.md#usage-example)

- [OpenSearch](https://docs.upsun.com/add-services/opensearch.md#use-in-app)

- [PostgreSQL](https://docs.upsun.com/add-services/postgresql.md#use-in-app)

- [Qdrant](https://docs.upsun.com/add-services/qdrant.md#4-use-the-relationship-in-your-application)

- [RabbitMQ](https://docs.upsun.com/add-services/rabbitmq.md#use-in-app)

- [Redis](https://docs.upsun.com/add-services/redis.md#use-in-app)

- [Solr](https://docs.upsun.com/add-services/solr.md#use-in-app)

- [Valkey](https://docs.upsun.com/add-services/valkey.md#use-in-app)

- [Varnish](https://docs.upsun.com/add-services/varnish.md#usage-example)

- [Vault KMS](https://docs.upsun.com/add-services/vault.md#use-vault-kms)


