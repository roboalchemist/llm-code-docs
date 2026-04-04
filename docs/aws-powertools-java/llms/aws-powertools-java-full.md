# Aws Powertools Java Documentation

Source: https://docs.aws.amazon.com/powertools/java/1.x.x/llms-full.txt

---

# Powertools for AWS Lambda (Java)

> Powertools for AWS Lambda (Java)

Powertools for AWS Lambda (Java) is a developer toolkit to implement Serverless best practices and increase developer velocity. It provides a suite of utilities for AWS Lambda Functions that makes tracing with AWS X-Ray, structured logging and creating custom metrics asynchronously easier.

# Project Overview

Powertools for AWS Lambda (Java) is a suite of utilities for AWS Lambda Functions that makes tracing with AWS X-Ray, structured logging and creating custom metrics asynchronously easier.

Tip

Powertools for AWS Lambda is also available for [Python](https://docs.aws.amazon.com/powertools/python/latest/), [TypeScript](https://docs.aws.amazon.com/powertools/typescript/latest/), and [.NET](https://docs.aws.amazon.com/powertools/dotnet/)

Looking for a quick run through of the core utilities?

Check out [this detailed blog post](https://aws.amazon.com/blogs/opensource/simplifying-serverless-best-practices-with-aws-lambda-powertools-java/) with a practical example. To dive deeper, the [Powertools for AWS Lambda (Java) workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/a7011c82-e4af-4a52-80fa-fcd61f1dacd9/en-US/introduction) is a great next step.

## Tenets

This project separates core utilities that will be available in other runtimes vs general utilities that might not be available across all runtimes.

- **AWS Lambda only** â We optimise for AWS Lambda function environments and supported runtimes only. Utilities might work with web frameworks and non-Lambda environments, though they are not officially supported.
- **Eases the adoption of best practices** â The main priority of the utilities is to facilitate best practices adoption, as defined in the AWS Well-Architected Serverless Lens; all other functionality is optional.
- **Keep it lean** â Additional dependencies are carefully considered for security and ease of maintenance, and prevent negatively impacting startup time.
- **We strive for backwards compatibility** â New features and changes should keep backwards compatibility. If a breaking change cannot be avoided, the deprecation and migration process should be clearly defined.
- **We work backwards from the community** â We aim to strike a balance of what would work best for 80% of customers. Emerging practices are considered and discussed via Requests for Comment (RFCs)
- **Progressive** - Utilities are designed to be incrementally adoptable for customers at any stage of their Serverless journey. They follow language idioms and their communityâs common practices.

## Install

**Quick hello world example using SAM CLI**

You can use [SAM](https://aws.amazon.com/serverless/sam/) to quickly setup a serverless project including Powertools for AWS Lambda (Java).

```
sam init

Which template source would you like to use?
    1 - AWS Quick Start Templates
    2 - Custom Template Location
Choice: 1

Choose an AWS Quick Start application template
    1 - Hello World Example
    2 - Data processing
    3 - Hello World Example with Powertools for AWS Lambda
    4 - Multi-step workflow
    5 - Scheduled task
    6 - Standalone function
    7 - Serverless API
    8 - Infrastructure event management
    9 - Lambda Response Streaming
    10 - Serverless Connector Hello World Example
    11 - Multi-step workflow with Connectors
    12 - Full Stack
    13 - Lambda EFS example
    14 - DynamoDB Example
    15 - Machine Learning
Template: 3

Which runtime would you like to use?
    1 - dotnet6
    2 - java17
    3 - java11
    4 - java8.al2
    5 - java8
    6 - nodejs18.x
    7 - nodejs16.x
    8 - nodejs14.x
    9 - python3.9
    10 - python3.8
    11 - python3.7
    12 - python3.10
Runtime: 2, 3, 4 or 5

```

**Manual installation** Powertools for AWS Lambda (Java) dependencies are available in Maven Central. You can use your favourite dependency management tool to install it

- [Maven](https://maven.apache.org/)
- [Gradle](https://gradle.org)

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-tracing</artifactId>
        <version>1.20.2</version>
    </dependency>
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-logging</artifactId>
        <version>1.20.2</version>
    </dependency>
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-metrics</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-tracing</artifactId>
                     </aspectLibrary>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-logging</artifactId>
                     </aspectLibrary>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-metrics</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-tracing</artifactId>
        <version>1.20.2</version>
    </dependency>
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-logging</artifactId>
        <version>1.20.2</version>
    </dependency>
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-metrics</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-tracing</artifactId>
                     </aspectLibrary>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-logging</artifactId>
                     </aspectLibrary>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-metrics</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.2.2'
    }

    // the freefair aspect plugins targets gradle 8.2.1
    // https://docs.freefair.io/gradle-plugins/8.2.2/reference/
    wrapper {
        gradleVersion = "8.2.1"
    }        

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-logging:1.20.2'
        aspect 'software.amazon.lambda:powertools-tracing:1.20.2'
        aspect 'software.amazon.lambda:powertools-metrics:1.20.2'
    }

    sourceCompatibility = 11
    targetCompatibility = 11

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    // the freefair aspect plugins targets gradle 7.6.1
    // https://docs.freefair.io/gradle-plugins/6.6.3/reference/
    wrapper {
        gradleVersion = "7.6.1"
    }


    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-logging:1.20.2'
        aspect 'software.amazon.lambda:powertools-tracing:1.20.2'
        aspect 'software.amazon.lambda:powertools-metrics:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

Why a different configuration?

Powertools for AWS Lambda (Java) is using [AspectJ](https://eclipse.dev/aspectj/doc/released/progguide/starting.html) internally to handle annotations. Recently, in order to support Java 17 we had to move to `dev.aspectj:aspectj-maven-plugin` because\
`org.codehaus.mojo:aspectj-maven-plugin` does not support Java 17. Under the hood, `org.codehaus.mojo:aspectj-maven-plugin` is based on AspectJ 1.9.7, while `dev.aspectj:aspectj-maven-plugin` is based on AspectJ 1.9.8, compiled for Java 11+.

### Java Compatibility

Powertools for AWS Lambda (Java) supports all Java version from 8 up to 21 as well as the [corresponding Lambda runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html).

For the following modules, Powertools for AWS Lambda (Java) leverages the **aspectj** library to provide annotations:

- Logging
- Metrics
- Tracing
- Parameters
- Idempotency
- Validation
- Large messages

You may need to add the good version of `aspectjrt` to your dependencies based on the jdk used for building your function:

```
<dependency>
    <groupId>org.aspectj</groupId>
    <artifactId>aspectjrt</artifactId>
    <version>1.9.??</version>
</dependency>

```

Use the following [dependency matrix](https://github.com/eclipse-aspectj/aspectj/blob/master/docs/dist/doc/JavaVersionCompatibility.md) between this library and the JDK:

| JDK version | aspectj version | | --- | --- | | `1.8` | `1.9.7` | | `11-17` | `1.9.20.1` | | `21` | `1.9.21` |

## Environment variables

Info

**Explicit parameters take precedence over environment variables.**

| Environment variable | Description | Utility | | --- | --- | --- | | **POWERTOOLS_SERVICE_NAME** | Sets service name used for tracing namespace, metrics dimension and structured logging | All | | **POWERTOOLS_METRICS_NAMESPACE** | Sets namespace used for metrics | [Metrics](./core/metrics) | | **POWERTOOLS_LOGGER_SAMPLE_RATE** | Debug log sampling | [Logging](./core/logging) | | **POWERTOOLS_LOG_LEVEL** | Sets logging level | [Logging](./core/logging) | | **POWERTOOLS_LOGGER_LOG_EVENT** | Enables/Disables whether to log the incoming event when using the aspect | [Logging](./core/logging) | | **POWERTOOLS_TRACER_CAPTURE_RESPONSE** | Enables/Disables tracing mode to capture method response | [Tracing](./core/tracing) | | **POWERTOOLS_TRACER_CAPTURE_ERROR** | Enables/Disables tracing mode to capture method error | [Tracing](./core/tracing) |

## How can I use Powertools for AWS Lambda (Java) with Lombok?

Powertools uses `aspectj-maven-plugin` to compile-time weave (CTW) aspects into the project. In case you want to use `Lombok` or other compile-time preprocessor for your project, it is required to change `aspectj-maven-plugin` configuration to enable in-place weaving feature. Otherwise, the plugin will ignore changes introduced by `Lombok` and will use `.java` files as a source.

To enable in-place weaving feature you need to use following `aspectj-maven-plugin` configuration:

```
<configuration>
    <forceAjcCompile>true</forceAjcCompile> 
    <sources/>
    <weaveDirectories>
        <weaveDirectory>${project.build.directory}/classes</weaveDirectory>
    </weaveDirectories>
    ...
    <aspectLibraries>
        <aspectLibrary>
            <groupId>software.amazon.lambda</groupId>
            <artifactId>powertools-logging</artifactId>
        </aspectLibrary>
    </aspectLibraries>
</configuration>

```

## How can I use Powertools for AWS Lambda (Java) with Kotlin projects?

Powertools uses `aspectj-maven-plugin` to compile-time weave (CTW) aspects into the project. When using it with Kotlin projects, it is required to `forceAjcCompile`. No explicit configuration should be required for gradle projects.

To enable `forceAjcCompile` you need to use following `aspectj-maven-plugin` configuration:

```
<configuration>
    <forceAjcCompile>true</forceAjcCompile> 
    ...
    <aspectLibraries>
        <aspectLibrary>
            <groupId>software.amazon.lambda</groupId>
            <artifactId>powertools-logging</artifactId>
        </aspectLibrary>
    </aspectLibraries>
</configuration>

```

# Changelog

All notable changes to this project will be documented in this file.

This project follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format for changes and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.20.1] - 2025-04-08

- docs: fix 2 typos (#1739) by @ntestor
- docs: Correct XML formatting for Maven configuration in Large Messages utility docs (#1796) by @jreijn
- fix: Load version.properties file as resource stream to fix loading when packaged as jar (#1813) by @phipag

## [1.20.0] - 2025-03-25

- feat(cfn-custom-resource): Add optional 'reason' field for detailed failure reporting (#1758) by @moizsh

## [1.19.0] - 2025-03-07

- chore(deps): Update deps for jackson ([#1793](https://github.com/aws-powertools/powertools-lambda-java/pull/1793)) by [@sthulb](https://github.com/sthulb)
- build(deps): bump log4j.version from 2.22.1 to 2.24.3 ([#1777](https://github.com/aws-powertools/powertools-lambda-java/pull/1777)) by [@dependabot](https://github.com/dependabot)
- chore(deps): update JSII to 1.108 ([#1791](https://github.com/aws-powertools/powertools-lambda-java/pull/1791)) by [@sthulb](https://github.com/sthulb)
- build(deps): bump jinja2 from 3.1.5 to 3.1.6 in /docs ([#1789](https://github.com/aws-powertools/powertools-lambda-java/pull/1789)) by [@dependabot](https://github.com/dependabot)
- chore: Update netty version ([#1768](https://github.com/aws-powertools/powertools-lambda-java/pull/1768)) by [@sthulb](https://github.com/sthulb)
- chore: Set versions of transitive dependencies ([#1767](https://github.com/aws-powertools/powertools-lambda-java/pull/1767)) by [@sthulb](https://github.com/sthulb)
- chore: update Jackson in examples ([#1766](https://github.com/aws-powertools/powertools-lambda-java/pull/1766)) by [@sthulb](https://github.com/sthulb)
- build(deps): bump org.apache.maven.plugins:maven-jar-plugin from 3.4.1 to 3.4.2 ([#1731](https://github.com/aws-powertools/powertools-lambda-java/pull/1731)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.xray.recorder.version from 2.15.3 to 2.18.1 ([#1726](https://github.com/aws-powertools/powertools-lambda-java/pull/1726)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.26.29 to 2.27.12 ([#1724](https://github.com/aws-powertools/powertools-lambda-java/pull/1724)) by [@dependabot](https://github.com/dependabot)
- fix: Allow empty responses as well as null response in AppConfig ([#1673](https://github.com/aws-powertools/powertools-lambda-java/pull/1673)) by [@chrisclayson](https://github.com/chrisclayson)
- build(deps): bump aws.sdk.version from 2.27.2 to 2.27.7 ([#1715](https://github.com/aws-powertools/powertools-lambda-java/pull/1715)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.26.29 to 2.27.2 ([#1714](https://github.com/aws-powertools/powertools-lambda-java/pull/1714)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.25.26 to 2.26.29 ([#1713](https://github.com/aws-powertools/powertools-lambda-java/pull/1713)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.26.25 to 2.26.29 ([#1712](https://github.com/aws-powertools/powertools-lambda-java/pull/1712)) by [@dependabot](https://github.com/dependabot)
- chore: deprecate java1.8 al1 ([#1706](https://github.com/aws-powertools/powertools-lambda-java/pull/1706)) by [@jeromevdl](https://github.com/jeromevdl)
- chore: java 1.8 AL1 is deprecated, fix E2E tests ([#1692](https://github.com/aws-powertools/powertools-lambda-java/pull/1692)) by [@jeromevdl](https://github.com/jeromevdl)
- build(deps): bump aws.sdk.version from 2.26.21 to 2.26.25 ([#1703](https://github.com/aws-powertools/powertools-lambda-java/pull/1703)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.26.3 to 2.26.21 ([#1697](https://github.com/aws-powertools/powertools-lambda-java/pull/1697)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump jackson.version from 2.17.0 to 2.17.2 ([#1696](https://github.com/aws-powertools/powertools-lambda-java/pull/1696)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.commons:commons-lang3 from 3.13.0 to 3.14.0 ([#1694](https://github.com/aws-powertools/powertools-lambda-java/pull/1694)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump commons-io:commons-io from 2.15.1 to 2.16.1 ([#1691](https://github.com/aws-powertools/powertools-lambda-java/pull/1691)) by [@dependabot](https://github.com/dependabot)
- docs: improve tracing doc for sdk instrumentation ([#1687](https://github.com/aws-powertools/powertools-lambda-java/pull/1687)) by [@jeromevdl](https://github.com/jeromevdl)
- docs: fix tracing links for xray ([#1686](https://github.com/aws-powertools/powertools-lambda-java/pull/1686)) by [@jeromevdl](https://github.com/jeromevdl)
- build(deps): bump org.apache.maven.plugins:maven-failsafe-plugin from 3.2.5 to 3.3.0 ([#1679](https://github.com/aws-powertools/powertools-lambda-java/pull/1679)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.25.69 to 2.26.3 ([#1658](https://github.com/aws-powertools/powertools-lambda-java/pull/1658)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump com.github.spotbugs:spotbugs-maven-plugin from 4.7.3.6 to 4.8.5.0 ([#1657](https://github.com/aws-powertools/powertools-lambda-java/pull/1657)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-checkstyle-plugin from 3.3.0 to 3.4.0 ([#1653](https://github.com/aws-powertools/powertools-lambda-java/pull/1653)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.25.50 to 2.25.69 ([#1652](https://github.com/aws-powertools/powertools-lambda-java/pull/1652)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-source-plugin from 3.3.0 to 3.3.1 ([#1646](https://github.com/aws-powertools/powertools-lambda-java/pull/1646)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.assertj:assertj-core from 3.25.3 to 3.26.0 ([#1644](https://github.com/aws-powertools/powertools-lambda-java/pull/1644)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.xray.recorder.version from 2.15.1 to 2.15.3 ([#1643](https://github.com/aws-powertools/powertools-lambda-java/pull/1643)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.25.35 to 2.25.50 ([#1642](https://github.com/aws-powertools/powertools-lambda-java/pull/1642)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump com.amazonaws:aws-lambda-java-events from 3.11.2 to 3.11.4 ([#1597](https://github.com/aws-powertools/powertools-lambda-java/pull/1597)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.24.10 to 2.25.6 ([#1603](https://github.com/aws-powertools/powertools-lambda-java/pull/1603)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-surefire-plugin from 3.1.2 to 3.2.5 ([#1596](https://github.com/aws-powertools/powertools-lambda-java/pull/1596)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.codehaus.mojo:exec-maven-plugin from 3.1.0 to 3.2.0 ([#1585](https://github.com/aws-powertools/powertools-lambda-java/pull/1585)) by [@dependabot](https://github.com/dependabot)
- build(deps-dev): bump software.amazon.awscdk:aws-cdk-lib from 2.100.0 to 2.130.0 ([#1586](https://github.com/aws-powertools/powertools-lambda-java/pull/1586)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump io.burt:jmespath-jackson from 0.5.1 to 0.6.0 ([#1587](https://github.com/aws-powertools/powertools-lambda-java/pull/1587)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.21.0 to 2.24.10 ([#1581](https://github.com/aws-powertools/powertools-lambda-java/pull/1581)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump commons-io:commons-io from 2.13.0 to 2.15.1 ([#1584](https://github.com/aws-powertools/powertools-lambda-java/pull/1584)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.xray.recorder.version from 2.14.0 to 2.15.1 ([#1583](https://github.com/aws-powertools/powertools-lambda-java/pull/1583)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-shade-plugin from 3.5.0 to 3.5.2 ([#1582](https://github.com/aws-powertools/powertools-lambda-java/pull/1582)) by [@dependabot](https://github.com/dependabot)
- build(deps-dev): bump org.yaml:snakeyaml from 2.1 to 2.2 ([#1400](https://github.com/aws-powertools/powertools-lambda-java/pull/1400)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump log4j.version from 2.20.0 to 2.22.1 ([#1547](https://github.com/aws-powertools/powertools-lambda-java/pull/1547)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-artifact-plugin from 3.4.1 to 3.5.0 ([#1485](https://github.com/aws-powertools/powertools-lambda-java/pull/1485)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump com.amazonaws:aws-lambda-java-serialization from 1.1.2 to 1.1.5 ([#1573](https://github.com/aws-powertools/powertools-lambda-java/pull/1573)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.jacoco:jacoco-maven-plugin from 0.8.10 to 0.8.11 ([#1509](https://github.com/aws-powertools/powertools-lambda-java/pull/1509)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aspectj to 1.9.21 for jdk21 ([#1536](https://github.com/aws-powertools/powertools-lambda-java/pull/1536)) by [@jeromevdl](https://github.com/jeromevdl)
- docs: HelloWorldStreamFunction in examples fails with sam ([#1532](https://github.com/aws-powertools/powertools-lambda-java/pull/1532)) by [@jasoniharris](https://github.com/jasoniharris)
- chore: Testing java21 aspectj pre-release ([#1519](https://github.com/aws-powertools/powertools-lambda-java/pull/1519)) by [@scottgerring](https://github.com/scottgerring)
- fix: LargeMessageIdempotentE2ET Flaky ([#1518](https://github.com/aws-powertools/powertools-lambda-java/pull/1518)) by [@scottgerring](https://github.com/scottgerring)
- build(deps): bump software.amazon.payloadoffloading:payloadoffloading-common from 2.1.3 to 2.2.0 ([#1639](https://github.com/aws-powertools/powertools-lambda-java/pull/1639)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-jar-plugin from 3.3.0 to 3.4.1 ([#1638](https://github.com/aws-powertools/powertools-lambda-java/pull/1638)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump jackson.version from 2.15.3 to 2.17.0 ([#1637](https://github.com/aws-powertools/powertools-lambda-java/pull/1637)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.25.31 to 2.25.35 ([#1629](https://github.com/aws-powertools/powertools-lambda-java/pull/1629)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.25.16 to 2.25.31 ([#1625](https://github.com/aws-powertools/powertools-lambda-java/pull/1625)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.21.1 to 2.25.26 ([#1622](https://github.com/aws-powertools/powertools-lambda-java/pull/1622)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-failsafe-plugin from 3.1.2 to 3.2.5 ([#1619](https://github.com/aws-powertools/powertools-lambda-java/pull/1619)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump com.fasterxml.jackson.datatype:jackson-datatype-joda from 2.15.2 to 2.17.0 ([#1616](https://github.com/aws-powertools/powertools-lambda-java/pull/1616)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump aws.sdk.version from 2.25.6 to 2.25.16 ([#1613](https://github.com/aws-powertools/powertools-lambda-java/pull/1613)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.apache.maven.plugins:maven-gpg-plugin from 3.1.0 to 3.2.1 ([#1610](https://github.com/aws-powertools/powertools-lambda-java/pull/1610)) by [@dependabot](https://github.com/dependabot)
- build(deps): bump org.assertj:assertj-core from 3.24.2 to 3.25.3 ([#1609](https://github.com/aws-powertools/powertools-lambda-java/pull/1609)) by [@dependabot](https://github.com/dependabot)

## [1.18.0] - 2023-11-16

### Added

- feat: add support for [Lambda Advanced Logging Controls (ALC)](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-advanced) (#1514) by @jeromevdl
- feat: Add support for POWERTOOLS_LOGGER_LOG_EVENT (#1510) by @AlexeySoshin

### Maintenance

- fix: json schema 403 error (#1457) by @jeromevdl
- fix: array jmespath fail in idempotency module (#1420) by @jeromevdl
- chore: java21 support in our build (#1488) by @jeromevdl
- chore: Addition of Warn Message If Invalid Annotation Key While Tracing #1511 (#1512) by @jdoherty
- fix: null namespace should fallback to default namespace (#1506) by @jeromevdl
- fix: get trace id from system property when env var is not set (#1503) by @mriccia
- chore: artifacts size on good branches (#1493) by @jeromevdl
- fix: enforce jackson databind version (#1472) by @jeromevdl
- chore: add missing projects and improve workflow (#1487) by @jeromevdl
- chore: Reporting size of the jars in GitHub comments (#1196) by @jeromevdl
- Deps: Bump third party dependencies to the latest versions.

### Documentation

- docs(customer-reference): add Vertex Pharmaceuticals as a customer reference (#1486) by @scottgerring
- docs: Adding Kotlin example. (#1454) by @jasoniharris
- docs: Terraform example (#1478) by @skal111
- docs: Add Serveless Framework example (#1363) by @AlexeySoshin
- docs: Fix link to SQS large message migration guide (#1422) by @scottgerring
- docs(logging): correct log example keys (#1411) by @walmsles
- docs: Update gradle configuration readme (#1359) by @scottgerring

## [1.17.0] - 2023-08-21

### Added

- Feat: Add Batch Processor module in (#1317) by @scottgerring
- Feat: Add SNS+SQS large messages module (#1310) by @jeromevdl

### Maintenance

- fix: use default credentials provider for all provided SDK clients in (#1303) by @roamingthings
- Chore: Make request for Logger explicitly for current class in (#1307) by @jreijn
- Chore: checkstyle formater & linter in (#1316) by @jeromevdl
- Chore: Add powertools specific user-agent-suffix to the AWS SDK v2 clients by @eldimi in (#1306)
- Chore: Add 'v2' branch to build workflows to prepare for v2 work in (#1341) by @scottgerring
- Deps: Bump third party dependencies to the latest versions.

### Documentation

- Docs: Add maintainers guide in (#1326) by @scottgerring
- Docs: improve contributing guide in (#1334) by @jeromevdl
- Docs: Improve example documentation in (#1291) by @scottgerring
- Docs: Add discord + sec disclosure links to readme in (#1311) by @scottgerring
- Docs: Add external examples from AWS SAM CLI App Templates in (#1318) by @AlexeySoshin
- Docs: Add CDK example in (#1321) by @AlexeySoshin

## [1.16.1] - 2023-07-19

- Fix: idempotency timeout bug (#1285) by @scottgerring
- Fix: ParamManager cannot provide default SSM & Secrets providers (#1282) by @jeromevdl
- Fix: Handle batch failures in FIFO queues correctly (#1183) by @scottgerring
- Deps: Bump third party dependencies to the latest versions.

## [1.16.0] - 2023-06-29

### Added

- Feature: Add AppConfig provider to parameters module (#1104) by @scottgerring

### Maintenance

- Fix: missing idempotency key should not persist any data (#1201) by @jeromevdl
- Fix:Removing env var credentials provider as default. (#1161) by @msailes
- Chore: Swap implementation of `aspectj-maven-plugin` to support Java 17 (#1172) by @mriccia
- Test: end-to-end tests for core modules and idempotency (#970) by @jeromevdl
- Chore: cleanup spotbugs maven profiles (#1236) by @jeromevdl
- Chore: removing logback from all components (#1227) by @jeromevdl
- Chore: Roll SLF4J log4j bindings to v2 (#1190) by @scottgerring
- Deps: Bump third party dependencies to the latest versions.

## [1.15.0] - 2023-03-20

### Added

- Feature: Add DynamoDB provider to parameters module (#1091) by @scottgerring
- Feature: Update to powertools-cloudformation to deprecate `Response.success()` and `Response.failed()` methods. New helper methods are added to make it easier to follow best practices `Response.success(String physicalResourceId)` and `Response.failed(String physicalResourceId)`. For a detailed explanation please read the [powertools-cloudformation documentation page](https://docs.aws.amazon.com/powertools/java/utilities/custom_resources/). (#1082) by @msailes
- Update how a Lambda request handler method is identified (#1058) by @humanzz

### Maintenance

- Deps: Bump third party dependencies to the latest versions.
- Examples: Import examples from aws-samples/aws-lambda-powertools-examples (#1051) by @scottgerring
- Deprecate withMetricLogger in favor of withMetricsLogger (#1060) by @humanzz
- Update issue templates (#1062) by @machafer
- Send code coverage report (jacoco) to codecov (#1094) by @jeromevdl

### Documentation

- Improve `powertools-cloudformation` docs (#1090) by @mriccia
- Add link to Powertools for AWS Lambda (Java) workshop (#1095) by @scottgerring
- Fix mdocs and git revision plugin integration (#1066) by @machafer

## [1.14.0] - 2023-02-17

### Added

- Feature: Introduce `MetricsUtils.withMetricsLogger()` utility method (#1000) by @humanzz

#### Maintenance

- Update logic for recording documentation pages views to use correct runtime name (#1047) by @kozub
- Deps: Bump third party dependencies to the latest versions.

### Documentation

- Docs: Update Powertools for AWS Lambda (Java) definition by @heitorlessa
- Docs: Add information about other supported langauges to README and docs (#1033) by @kozub

## [1.13.0] - 2022-12-14

### Added

- Feature: Idempotency - Handle Lambda timeout scenarios for INPROGRESS records (#933) by @jeromevdl

### Bug Fixes

- Fix: Envelope is not taken into account with built-in types (#960) by @jeromevdl
- Fix: Code suggestion from CodeGuru (#984) by @kozub
- Fix: Compilation warning with SqsLargeMessageAspect on gradle (#998) by @jeromevdl
- Fix: Log message processing exceptions as occur (#1011) by @nem0-97

### Documentation

- Docs: Add missing grammar article (#976) by @fsmiamoto

## [1.12.3] - 2022-07-12

#### Maintenance

- Fixes to resolve vulnerable transitive dependencies ([919](https://github.com/aws-powertools/powertools-lambda-java/issues/919))

## [1.12.2] - 2022-04-29

### Bug Fixes

- **SQS Large message processing**: Classpath conflict on `PayloadS3Pointer` when consumer application depends on `payloadoffloading-common`, introduced in [v1.8.0](https://github.com/aws-powertools/powertools-lambda-java/releases/tag/v1.8.0). ([#851](https://github.com/aws-powertools/powertools-lambda-java/pull/851))

## [1.12.1] - 2022-04-21

### Bug Fixes

- **Idempotency**: thread-safety issue of MessageDigest ([#817](https://github.com/aws-powertools/powertools-lambda-java/pull/817))
- **Idempotency**: disable dynamodb client creation in persistent store when disabling idempotency ([#796](https://github.com/aws-powertools/powertools-lambda-java/pull/796))

### Maintenance

- **deps**: Bump third party dependencies to the latest versions.

## [1.12.0] - 2022-03-01

### Added

- **Easy Event Deserialization**: Extraction and deserialization of the main content of events (body, messages, ...) [#757](https://github.com/aws-powertools/powertools-lambda-java/pull/757)

### Bug Fixes

- Different behavior while using SSMProvider with or without trailing slash in parameter names [#758](https://github.com/aws-powertools/powertools-lambda-java/issues/758)

## [1.11.0] - 2022-02-16

### Added

- Powertools for AWS Lambda (Java) Idempotency module: New module to get your Lambda function [Idempotent](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) (#717)
- Powertools for AWS Lambda (Java) Serialization module: New module to handle JSON (de)serialization (Jackson ObjectMapper, JMESPath functions)

## [1.10.3] - 2022-02-01

### Bug Fixes

- **SQS Batch processing**: Prevent message to be marked as success if failed sending to DLQ for non retryable exceptions. [#731](https://github.com/aws-powertools/powertools-lambda-java/pull/731)

### Documentation

- **SQS Batch processing**: Improve [documentation](https://docs.aws.amazon.com/powertools/java/utilities/batch/#iam-permissions) on IAM premissions required by function when using utility with an encrypted SQS queue with customer managed KMS keys.

## [1.10.2] - 2022-01-07

- **Tracing**: Ability to override object mapper used for serializing method response as trace metadata when enabled. This provides users ability to customize how and what you want to capture as metadata from method response object. [#698](https://github.com/aws-powertools/powertools-lambda-java/pull/698)

## [1.10.1] - 2022-01-06

- **Logging**: Upgrade Log4j to version 2.17.1 for [CVE-2021-44832](https://nvd.nist.gov/vuln/detail/CVE-2021-44832)

## [1.10.0] - 2021-12-27

- **Logging**: Modern log4j configuration to customise structured logging. Refer [docs](https://docs.aws.amazon.com/powertools/java/core/logging/#upgrade-to-jsontemplatelayout-from-deprecated-lambdajsonlayout-configuration-in-log4j2xml) to start using new config. [#670](https://github.com/aws-powertools/powertools-lambda-java/pull/670)
- **SQS Batch**: Support batch size greater than 10. [#667](https://github.com/aws-powertools/powertools-lambda-java/pull/667)

## [1.9.0] - 2021-12-21

- **Logging**: Upgrade Log4j to version 2.17.0 for [CVE-2021-45105](https://nvd.nist.gov/vuln/detail/CVE-2021-45105)
- **Tracing**: add `Service` annotation. [#654](https://github.com/aws-powertools/powertools-lambda-java/issues/654)

## [1.8.2] - 2021-12-15

## Security

- Upgrading Log4j to version 2.16.0 for [CVE-2021-45046](https://nvd.nist.gov/vuln/detail/CVE-2021-45046)

## [1.8.1] - 2021-12-10

## Security

- Upgrading Log4j to version 2.15.0 for [CVE-2021-44228](https://nvd.nist.gov/vuln/detail/CVE-2021-44228)

## [1.8.0] - 2021-11-05

### Added

- **Powertools for AWS Lambda (Java) Cloudformation module (NEW)**: New module simplifying [AWS Lambda-backed custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html) written in Java. [#560](https://github.com/aws-powertools/powertools-lambda-java/pull/560)
- **SQS Large message processing**: Ability to override the default `S3Client` use to fetch payload from S3. [#602](https://github.com/aws-powertools/powertools-lambda-java/pull/602)

### Regression

- **Logging**: `@Logging` annotation now works with `@Tracing` annotation on `RequestStreamHandler` when used in `logEvent` mode. [#567](https://github.com/aws-powertools/powertools-lambda-java/pull/567)

### Maintenance

- **deps**: Bump third party dependencies to the latest versions.

## [1.7.3] - 2021-09-14

- **SQS Batch processing**: Ability to move non retryable message to configured dead letter queue(DLQ). [#500](https://github.com/aws-powertools/powertools-lambda-java/pull/500)

## [1.7.2] - 2021-08-03

- **Powertools for AWS Lambda (Java) All Modules**: Upgrade to the latest(1.14.0) aspectj-maven-plugin which also supports Java 9 and newer versions. Users no longer need to depend on [com.nickwongdev](https://mvnrepository.com/artifact/com.nickwongdev/aspectj-maven-plugin/1.12.6) as a workaround. [#489](https://github.com/aws-powertools/powertools-lambda-java/pull/489)
- **Logging**: Performance optimisation to improve cold start. [#484](https://github.com/aws-powertools/powertools-lambda-java/pull/484)
- **SQS Batch processing/Large message**: Module now lazy loads default SQS client. [#484](https://github.com/aws-powertools/powertools-lambda-java/pull/484)

## [1.7.1] - 2021-07-06

- **Powertools for AWS Lambda (Java) All Modules**: Fix static code analysis violations done via [spotbugs](https://github.com/spotbugs/spotbugs) ([#458](https://github.com/aws-powertools/powertools-lambda-java/pull/458)).

## [1.7.0] - 2021-07-05

### Added

- **Logging**: Support for extracting Correlation id using `@Logging` annotation via `correlationIdPath` attribute and `setCorrelationId()` method in `LoggingUtils`([#448](https://github.com/aws-powertools/powertools-lambda-java/pull/448)).
- **Logging**: New `clearState` attribute on `@Logging` annotation to clear previously added custom keys upon invocation([#453](https://github.com/aws-powertools/powertools-lambda-java/pull/453)).

### Maintenance

- **deps**: Bump third party dependencies to the latest versions.

## [1.6.0] - 2021-06-21

### Added

- **Tracing**: Support for Boolean and Number type as value in `TracingUtils.putAnnotation()`([#423](https://github.com/aws-powertools/powertools-lambda-java/pull/432)).
- **Logging**: API to remove any additional custom key from logger entry using `LoggingUtils.removeKeys()`([#395](https://github.com/aws-powertools/powertools-lambda-java/pull/395)).

### Maintenance

- **deps**: Bump third party dependencies to the latest versions.

## [1.5.0] - 2021-03-30

- **Metrics**: Ability to set multiple dimensions as default dimensions via `MetricsUtils.defaultDimensions()`. Introduced in [v1.4.0](https://github.com/aws-powertools/powertools-lambda-java/releases/tag/v1.4.0) `MetricsUtils.defaultDimensionSet()` is deprecated now for better user experience.

## [1.4.0] - 2021-03-11

- **Metrics**: Ability to set default dimension for metrics via `MetricsUtils.defaultDimensionSet()`.

**Note**: If your monitoring depends on [default dimensions](https://github.com/awslabs/aws-embedded-metrics-java/blob/main/src/main/java/software/amazon/cloudwatchlogs/emf/logger/MetricsLogger.java#L173) captured before via [aws-embedded-metrics-java](https://github.com/awslabs/aws-embedded-metrics-java), those either need to be updated or has to be explicitly captured via `MetricsUtils.defaultDimensionSet()`.

- **Metrics**: Remove validation of having minimum one dimension. EMF now support [Dimension set being empty](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html) as well.

## [1.3.0] - 2021-03-05

- **Powertools**: It now works out of the box with [code guru profile handler implementation](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/lambda-custom.html).
- **Logging**: Ability to override object mapper used for logging event. This provides customers ability to customize how and what they want to log from event.
- **Metrics**: Module now by default captures AWS Request id as property if used together with Metrics annotation. It will also capture Xray Trace ID as property if tracing is enabled. This ensures good observability and tracing.
- **Metrics**:`withSingleMetric` from \`MetricsUtils can now pick the default namespace specified either on Metrics annotation or via POWERTOOLS_METRICS_NAMESPACE env var, without need to specify explicitly for each call.
- **Metrics**:`Metrics` annotation captures metrics even in case of unhandled exception from Lambda function.
- **Docs**: Migrated from Gatsby to MKdocs documentation system

## Overview

Our public roadmap outlines the high level direction we are working towards. We update this document when our priorities change: security and stability are our top priority.

### Key areas

Security and operational excellence take precedence above all else. This means bug fixing, stability, customer's support, and internal compliance may delay one or more key areas below.

We may choose to re-prioritize or defer items based on customer feedback, security, and operational impacts, and business value.

#### Release Security (p0)

Our top priority is to establish the processes and infrastructure needed for a fully automated and secure end-to-end release process of new versions to Maven Central.

- Implement GitHub workflows and create infrastructure to release to Maven Central
- [Implement end-to-end tests](https://github.com/aws-powertools/powertools-lambda-java/issues/1815)
- Implement [OpenSSF Scorecard](https://openssf.org/projects/scorecard/)

#### `v2` Release: Consistency and Ecosystem (p1)

As part of a new major version `v2` release, we prioritize the Java project's consistency of core utilities (Logging, Metrics, Tracing) with the other runtimes (Python, TypeScript, .NET). Additionally, we will focus on integrating the library with popular technologies and frameworks from the Java and AWS ecosystem. Particularly, we aim at leveraging new techniques to allow customers to reduce Lambda cold-start time. The `v2` release will also drop support for Java 8 moving to Java 11 as the baseline.

##### Core Utilities

- [Review public interfaces and reduce public API surface area](https://github.com/aws-powertools/powertools-lambda-java/issues/1283)
- [Release Logging `v2` module](https://github.com/aws-powertools/powertools-lambda-java/issues/965) allowing customers to choose the logging framework and adding support for logging deeply nested objects as JSON
- [Support high resolution metrics](https://github.com/aws-powertools/powertools-lambda-java/issues/1041)

##### Ecosystem

- [Add GraalVM support for core utilities](https://github.com/aws-powertools/powertools-lambda-java/issues/764)
- [Implement priming using CRaC to improve AWS Snapstart support](https://github.com/aws-powertools/powertools-lambda-java/issues/1588)
- [Evaluate integration with popular Java frameworks such as Micronaut, Spring Cloud Function, or Quarkus](https://github.com/aws-powertools/powertools-lambda-java/issues/1701)

##### Other

- [Validation module integration with HTTP requests](https://github.com/aws-powertools/powertools-lambda-java/issues/1298)
- [Support validation module from within the batch module](https://github.com/aws-powertools/powertools-lambda-java/issues/1496)
- [Add support for parallel processing in Batch Processing utility](https://github.com/aws-powertools/powertools-lambda-java/issues/1540)
- [Documentation: Review and improve documentation to be consistent with other runtimes](https://github.com/aws-powertools/powertools-lambda-java/issues/1352)

#### Feature Parity (p2)

If priorities `p0` and `p1` are addressed, we will also focus on feature parity of non-core utilities. This allows customers to achieve better standardization of their development processes across different Powertools runtimes.

- [Re-evaluate if there is a need for adding a lightweight customer Powertools event handler](https://github.com/aws-powertools/powertools-lambda-java/issues/1103)
- Add comprehensive GraalVM support for all utilities
- [Add Feature Flags module](https://github.com/aws-powertools/powertools-lambda-java/issues/1086)
- [Add S3 Streaming module](https://github.com/aws-powertools/powertools-lambda-java/issues/1085)
- Add support for Data Masking during JSON serialization

### Missing something?

You can help us prioritize by [upvoting existing feature requests](https://github.com/aws-powertools/powertools-lambda-java/issues?q=is%3Aissue%20state%3Aopen%20label%3Aenhancement), leaving a comment on what use cases it could unblock for you, and by joining our discussions on Discord.

### Roadmap status definition

```
graph LR
    Ideas --> Backlog --> Work["Working on it"] --> Merged["Coming soon"] --> Shipped
```

*Visual representation*

Within our [public board](https://github.com/orgs/aws-powertools/projects/4/), you'll see the following values in the `Status` column:

- **Ideas**. Incoming and existing feature requests that are not being actively considered yet. These will be reviewed when bandwidth permits.
- **Backlog**. Accepted feature requests or enhancements that we want to work on.
- **Working on it**. Features or enhancements we're currently either researching or implementing it.
- **Coming soon**. Any feature, enhancement, or bug fixes that have been merged and are coming in the next release.
- **Shipped**. Features or enhancements that are now available in the most recent release.

> Tasks or issues with empty `Status` will be categorized in upcoming review cycles.

### Process

```
graph LR
    PFR[Feature request] --> Triage{Need RFC?}
    Triage --> |Complex/major change or new utility?| RFC[Ask or write RFC] --> Approval{Approved?}
    Triage --> |Minor feature or enhancement?| NoRFC[No RFC required] --> Approval
    Approval --> |Yes| Backlog
    Approval --> |No | Reject["Inform next steps"]
    Backlog --> |Prioritized| Implementation
    Backlog --> |Defer| WelcomeContributions["help-wanted label"]
```

*Visual representation*

Our end-to-end mechanism follows four major steps:

- **Feature Request**. Ideas start with a [feature request](https://github.com/aws-powertools/powertools-lambda-java/issues/new?template=feature_request.md) to outline their use case at a high level. For complex use cases, maintainers might ask for/write a RFC.
- Maintainers review requests based on [project tenets](../#tenets), customers reaction (ð), and use cases.
- **Request-for-comments (RFC)**. Design proposals use our [RFC template](https://github.com/aws-powertools/powertools-lambda-java/issues/new?q=is%3Aissue+state%3Aopen+label%3Aenhancement&template=rfc.md) to describe its implementation, challenges, developer experience, dependencies, and alternative solutions.
- This helps refine the initial idea with community feedback before a decision is made.
- **Decision**. After carefully reviewing and discussing them, maintainers make a final decision on whether to start implementation, defer or reject it, and update everyone with the next steps.
- **Implementation**. For approved features, maintainers give priority to the original authors for implementation unless it is a sensitive task that is best handled by maintainers.

See [Maintainers](../processes/maintainers/) document to understand how we triage issues and pull requests, labels and governance.

### Disclaimer

The Powertools for AWS Lambda (Java) team values feedback and guidance from its community of users, although final decisions on inclusion into the project will be made by AWS.

We determine the high-level direction for our open roadmap based on customer feedback and popularity (ðð½ and comments), security and operational impacts, and business value. Where features donât meet our goals and longer-term strategy, we will communicate that clearly and openly as quickly as possible with an explanation of why the decision was made.

### FAQs

**Q: Why did you build this?**

A: We know that our customers are making decisions and plans based on what we are developing, and we want to provide our customers the insights they need to plan.

**Q: Why are there no dates on your roadmap?**

A: Because job zero is security and operational stability, we can't provide specific target dates for features. The roadmap is subject to change at any time, and roadmap issues in this repository do not guarantee a feature will be launched as proposed.

**Q: How can I provide feedback or ask for more information?**

A: For existing features, you can directly comment on issues. For anything else, please open an issue.
# Core Utilities

Logging provides an opinionated logger with output structured as JSON.

**Key features**

- Capture key fields from Lambda context, cold start and structures logging output as JSON
- Log Lambda event when instructed, disabled by default, can be enabled explicitly via annotation param
- Append additional keys to structured log at any point in time

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-logging</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-logging</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-logging</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-logging</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-logging:1.20.2'
    }

    sourceCompatibility = 11
    targetCompatibility = 11

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-logging:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Initialization

Powertools for AWS Lambda (Java) extends the functionality of Log4J. Below is an example `log4j2.xml` file, with the `JsonTemplateLayout` using `LambdaJsonLayout.json` configured.

LambdaJsonLayout is now deprecated

Configuring utility using `<LambdaJsonLayout/>` plugin is deprecated now. While utility still supports the old configuration, we strongly recommend upgrading the `log4j2.xml` configuration to `JsonTemplateLayout` instead. [JsonTemplateLayout](https://logging.apache.org/log4j/2.x/manual/json-template-layout.html) is recommended way of doing structured logging.

Please follow [this guide](#upgrade-to-jsontemplatelayout-from-deprecated-lambdajsonlayout-configuration-in-log4j2xml) for upgrade steps.

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <JsonTemplateLayout eventTemplateUri="classpath:LambdaJsonLayout.json" />
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

You can also override log level by setting **`POWERTOOLS_LOG_LEVEL`** env var. Here is an example using AWS Serverless Application Model (SAM)

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11
        Environment:
            Variables:
                POWERTOOLS_LOG_LEVEL: DEBUG
                POWERTOOLS_SERVICE_NAME: example

```

You can also explicitly set a service name via **`POWERTOOLS_SERVICE_NAME`** env var. This sets **service** key that will be present across all log statements.

## Standard structured keys

Your logs will always include the following keys to your structured logging:

| Key | Type | Example | Description | | --- | --- | --- | --- | | **timestamp** | String | "2020-05-24 18:17:33,774" | Timestamp of actual log statement | | **level** | String | "INFO" | Logging level | | **coldStart** | Boolean | true | ColdStart value. | | **service** | String | "payment" | Service name defined. "service_undefined" will be used if unknown | | **samplingRate** | int | 0.1 | Debug logging sampling rate in percentage e.g. 10% in this case | | **message** | String | "Collecting payment" | Log statement value. Unserializable JSON values will be casted to string | | **functionName** | String | "example-powertools-HelloWorldFunction-1P1Z6B39FLU73" | | | **functionVersion** | String | "12" | | | **functionMemorySize** | String | "128" | | | **functionArn** | String | "arn:aws:lambda:eu-west-1:012345678910:function:example-powertools-HelloWorldFunction-1P1Z6B39FLU73" | | | **xray_trace_id** | String | "1-5759e988-bd862e3fe1be46a994272793" | X-Ray Trace ID when Lambda function has enabled Tracing | | **function_request_id** | String | "899856cb-83d1-40d7-8611-9e78f15f32f4"" | AWS Request ID from lambda context |

## Capturing context Lambda info

When debugging in non-production environments, you can instruct Logger to log the incoming event with `@Logger(logEvent = true)` or via `POWERTOOLS_LOGGER_LOG_EVENT=true` environment variable.

Warning

Log event is disabled by default to prevent sensitive info being logged.

```
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import software.amazon.lambda.powertools.logging.LoggingUtils;
import software.amazon.lambda.powertools.logging.Logging;
...

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
     ...
    }
}

```

```
/**
 * Handler for requests to Lambda function.
 */
public class AppLogEvent implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(AppLogEvent.class);

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
     ...
    }
}

```

### Customising fields in logs

- Utility by default emits `timestamp` field in the logs in format `yyyy-MM-dd'T'HH:mm:ss.SSSZz` and in system default timezone. If you need to customize format and timezone, you can do so by configuring `log4j2.component.properties` and configuring properties as shown in example below:

```
log4j.layout.jsonTemplate.timestampFormatPattern=yyyy-MM-dd'T'HH:mm:ss.SSSZz
log4j.layout.jsonTemplate.timeZone=Europe/Oslo

```

- Utility also provides sample template for [Elastic Common Schema(ECS)](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) layout. The field emitted in logs will follow specs from [ECS](https://www.elastic.co/guide/en/ecs/current/ecs-reference.html) together with field captured by utility as mentioned [above](#standard-structured-keys).

  Use `LambdaEcsLayout.json` as `eventTemplateUri` when configuring `JsonTemplateLayout`.

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <JsonTemplateLayout eventTemplateUri="classpath:LambdaEcsLayout.json" />
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

## Setting a Correlation ID

You can set a Correlation ID using `correlationIdPath` attribute by passing a [JSON Pointer expression](https://datatracker.ietf.org/doc/html/draft-ietf-appsawg-json-pointer-03).

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(correlationIdPath = "/headers/my_request_id_header")
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        log.info("Collecting payment")
        ...
    }
}

```

```
{
  "headers": {
    "my_request_id_header": "correlation_id_value"
  }
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72",
    "correlation_id": "correlation_id_value"
}

```

We provide [built-in JSON Pointer expression](https://datatracker.ietf.org/doc/html/draft-ietf-appsawg-json-pointer-03) for known event sources, where either a request ID or X-Ray Trace ID are present.

```
import software.amazon.lambda.powertools.logging.CorrelationIdPathConstants;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(correlationIdPath = CorrelationIdPathConstants.API_GATEWAY_REST)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        log.info("Collecting payment")
        ...
    }
}

```

```
{
  "requestContext": {
    "requestId": "correlation_id_value"
  }
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72",
    "correlation_id": "correlation_id_value"
}

```

## Appending additional keys

Custom keys are persisted across warm invocations

```
Always set additional keys as part of your handler to ensure they have the latest value, or explicitly clear them with [`clearState=true`](#clearing-all-state).

```

You can append your own keys to your existing logs via `appendKey`.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        LoggingUtils.appendKey("test", "willBeLogged");
        ...

        ...
         Map<String, String> customKeys = new HashMap<>();
         customKeys.put("test", "value");
         customKeys.put("test1", "value1");

         LoggingUtils.appendKeys(customKeys);
        ...
    }
}

```

### Removing additional keys

You can remove any additional key from entry using `LoggingUtils.removeKeys()`.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        LoggingUtils.appendKey("test", "willBeLogged");
        ...
        Map<String, String> customKeys = new HashMap<>();
        customKeys.put("test1", "value");
        customKeys.put("test2", "value1");

        LoggingUtils.appendKeys(customKeys);
        ...
        LoggingUtils.removeKey("test");
        LoggingUtils.removeKeys("test1", "test2");
        ...
    }
}

```

### Clearing all state

Logger is commonly initialized in the global scope. Due to [Lambda Execution Context reuse](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html), this means that custom keys can be persisted across invocations. If you want all custom keys to be deleted, you can use `clearState=true` attribute on `@Logging` annotation.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(clearState = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
        if(input.getHeaders().get("someSpecialHeader")) {
            LoggingUtils.appendKey("specialKey", "value");
        }

        log.info("Collecting payment");
        ...
    }
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72",
    "specialKey": "value"
}

```

```
{
    "level": "INFO",
    "message": "Collecting payment",
    "timestamp": "2021-05-03 11:47:12,494+0200",
    "service": "payment",
    "coldStart": true,
    "functionName": "test",
    "functionMemorySize": 128,
    "functionArn": "arn:aws:lambda:eu-west-1:12345678910:function:test",
    "function_request_id": "52fdfc07-2182-154f-163f-5f0f9a621d72"
}

```

## Override default object mapper

You can optionally choose to override default object mapper which is used to serialize lambda function events. You might want to supply custom object mapper in order to control how serialisation is done, for example, when you want to log only specific fields from received event due to security.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    static {
        ObjectMapper objectMapper = new ObjectMapper();
        LoggingUtils.defaultObjectMapper(objectMapper);
    }

    @Logging(logEvent = true)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
    }
}

```

## Sampling debug logs

You can dynamically set a percentage of your logs to **DEBUG** level via env var `POWERTOOLS_LOGGER_SAMPLE_RATE` or via `samplingRate` attribute on annotation.

Info

Configuration on environment variable is given precedence over sampling rate configuration on annotation, provided it's in valid value range.

```
/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    Logger log = LogManager.getLogger(App.class);

    @Logging(samplingRate = 0.5)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
     ...
    }
}

```

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11
        Environment:
            Variables:
                POWERTOOLS_LOGGER_SAMPLE_RATE: 0.5

```

## AWS Lambda Advanced Logging Controls (ALC)

When is it useful?

When you want to set a logging policy to drop informational or verbose logs for one or all AWS Lambda functions, regardless of runtime and logger used.

With [AWS Lambda Advanced Logging Controls (ALC)](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-advanced), you can enforce a minimum log level that Lambda will accept from your application code.

When enabled, you should keep `Logger` and ALC log level in sync to avoid data loss.

Here's a sequence diagram to demonstrate how ALC will drop both `INFO` and `DEBUG` logs emitted from `Logger`, when ALC log level is stricter than `Logger`.

```
sequenceDiagram
    participant Lambda service
    participant Lambda function
    participant Application Logger

    Note over Lambda service: AWS_LAMBDA_LOG_LEVEL="WARN"
    Note over Application Logger: POWERTOOLS_LOG_LEVEL="DEBUG"

    Lambda service->>Lambda function: Invoke (event)
    Lambda function->>Lambda function: Calls handler
    Lambda function->>Application Logger: logger.error("Something happened")
    Lambda function-->>Application Logger: logger.debug("Something happened")
    Lambda function-->>Application Logger: logger.info("Something happened")
    Lambda service--xLambda service: DROP INFO and DEBUG logs
    Lambda service->>CloudWatch Logs: Ingest error logs
```

### Priority of log level settings in Powertools for AWS Lambda

We prioritise log level settings in this order:

1. `AWS_LAMBDA_LOG_LEVEL` environment variable
1. `POWERTOOLS_LOG_LEVEL` environment variable

If you set `Logger` level lower than ALC, we will emit a warning informing you that your messages will be discarded by Lambda.

> **NOTE**
>
> With ALC enabled, we are unable to increase the minimum log level below the `AWS_LAMBDA_LOG_LEVEL` environment variable value, see [AWS Lambda service documentation](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-cloudwatchlogs.html#monitoring-cloudwatchlogs-log-level) for more details.

### Timestamp format

When the Advanced Logging Controls feature is enabled, Powertools for AWS Lambda must comply with the timestamp format required by AWS Lambda, which is [RFC3339](https://www.rfc-editor.org/rfc/rfc3339). In this case the format will be `yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`.

## Upgrade to JsonTemplateLayout from deprecated LambdaJsonLayout configuration in log4j2.xml

Prior to version [1.10.0](https://github.com/aws-powertools/powertools-lambda-java/releases/tag/v1.10.0), only supported way of configuring `log4j2.xml` was via `<LambdaJsonLayout/>`. This plugin is deprecated now and will be removed in future version. Switching to `JsonTemplateLayout` is straight forward.

Below examples shows deprecated and new configuration of `log4j2.xml`.

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <LambdaJsonLayout compact="true" eventEol="true"/>
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

```
<?xml version="1.0" encoding="UTF-8"?>
<Configuration>
    <Appenders>
        <Console name="JsonAppender" target="SYSTEM_OUT">
            <JsonTemplateLayout eventTemplateUri="classpath:LambdaJsonLayout.json" />
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="JsonLogger" level="INFO" additivity="false">
            <AppenderRef ref="JsonAppender"/>
        </Logger>
        <Root level="info">
            <AppenderRef ref="JsonAppender"/>
        </Root>
    </Loggers>
</Configuration>

```

Metrics creates custom metrics asynchronously by logging metrics to standard output following Amazon CloudWatch Embedded Metric Format (EMF).

These metrics can be visualized through [Amazon CloudWatch Console](https://console.aws.amazon.com/cloudwatch/).

**Key features**

- Aggregate up to 100 metrics using a single CloudWatch EMF object (large JSON blob).
- Validate against common metric definitions mistakes (metric unit, values, max dimensions, max metrics, etc).
- Metrics are created asynchronously by the CloudWatch service, no custom stacks needed.
- Context manager to create a one off metric with a different dimension.

## Terminologies

If you're new to Amazon CloudWatch, there are two terminologies you must be aware of before using this utility:

- **Namespace**. It's the highest level container that will group multiple metrics from multiple services for a given application, for example `ServerlessEcommerce`.
- **Dimensions**. Metrics metadata in key-value format. They help you slice and dice metrics visualization, for example `ColdStart` metric by Payment `service`.

Metric terminology, visually explained

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-metrics</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-metrics</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-metrics</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-metrics</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-metrics:1.20.2'
    }

    sourceCompatibility = 11
    targetCompatibility = 11

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-metrics:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Getting started

Metric has two global settings that will be used across all metrics emitted:

| Setting | Description | Environment variable | Constructor parameter | | --- | --- | --- | --- | | **Metric namespace** | Logical container where all metrics will be placed e.g. `ServerlessAirline` | `POWERTOOLS_METRICS_NAMESPACE` | `namespace` | | **Service** | Optionally, sets **service** metric dimension across all metrics e.g. `payment` | `POWERTOOLS_SERVICE_NAME` | `service` |

Use your application or main service as the metric namespace to easily group all metrics

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11
        Environment:
            Variables:
                POWERTOOLS_SERVICE_NAME: payment
                POWERTOOLS_METRICS_NAMESPACE: ServerlessAirline

```

```
import software.amazon.lambda.powertools.metrics.Metrics;

public class MetricsEnabledHandler implements RequestHandler<Object, Object> {

    MetricsLogger metricsLogger = MetricsUtils.metricsLogger();

    @Override
    @Metrics(namespace = "ExampleApplication", service = "booking")
    public Object handleRequest(Object input, Context context) {
        ...
    }
}

```

You can initialize Metrics anywhere in your code as many times as you need - It'll keep track of your aggregate metrics in memory.

## Creating metrics

You can create metrics using `putMetric`, and manually create dimensions for all your aggregate metrics using `putDimensions`.

```
import software.amazon.lambda.powertools.metrics.Metrics;
import software.amazon.cloudwatchlogs.emf.logger.MetricsLogger;

public class MetricsEnabledHandler implements RequestHandler<Object, Object> {

    MetricsLogger metricsLogger = MetricsUtils.metricsLogger();

    @Override
    @Metrics(namespace = "ExampleApplication", service = "booking")
    public Object handleRequest(Object input, Context context) {
        metricsLogger.putDimensions(DimensionSet.of("environment", "prod"));
        metricsLogger.putMetric("SuccessfulBooking", 1, Unit.COUNT);
        ...
    }
}

```

The `Unit` enum facilitate finding a supported metric unit by CloudWatch.

Metrics overflow

CloudWatch EMF supports a max of 100 metrics. Metrics utility will flush all metrics when adding the 100th metric while subsequent metrics will be aggregated into a new EMF object, for your convenience.

### Flushing metrics

The `@Metrics` annotation **validates**, **serializes**, and **flushes** all your metrics. During metrics validation, if no metrics are provided no exception will be raised. If metrics are provided, and any of the following criteria are not met, `ValidationException` exception will be raised.

Metric validation

- Maximum of 9 dimensions

If you want to ensure that at least one metric is emitted, you can pass `raiseOnEmptyMetrics = true` to the **@Metrics** annotation:

```
import software.amazon.lambda.powertools.metrics.Metrics;

public class MetricsRaiseOnEmpty implements RequestHandler<Object, Object> {

    @Override
    @Metrics(raiseOnEmptyMetrics = true)
    public Object handleRequest(Object input, Context context) {
    ...
    }
}

```

## Capturing cold start metric

You can capture cold start metrics automatically with `@Metrics` via the `captureColdStart` variable.

```
import software.amazon.lambda.powertools.metrics.Metrics;

public class MetricsColdStart implements RequestHandler<Object, Object> {

    @Override
    @Metrics(captureColdStart = true)
    public Object handleRequest(Object input, Context context) {
    ...
    }
}

```

If it's a cold start invocation, this feature will:

- Create a separate EMF blob solely containing a metric named `ColdStart`
- Add `FunctionName` and `Service` dimensions

This has the advantage of keeping cold start metric separate from your application metrics.

## Advanced

## Adding metadata

You can use `putMetadata` for advanced use cases, where you want to metadata as part of the serialized metrics object.

Info

**This will not be available during metrics visualization, use `dimensions` for this purpose.**

```
import software.amazon.lambda.powertools.metrics.Metrics;
import software.amazon.cloudwatchlogs.emf.logger.MetricsLogger;

public class App implements RequestHandler<Object, Object> {

    @Override
    @Metrics(namespace = "ServerlessAirline", service = "payment")
    public Object handleRequest(Object input, Context context) {
        metricsLogger().putMetric("CustomMetric1", 1, Unit.COUNT);
        metricsLogger().putMetadata("booking_id", "1234567890");
        ...
    }
}

```

This will be available in CloudWatch Logs to ease operations on high cardinal data.

## Overriding default dimension set

By default, all metrics emitted via module captures `Service` as one of the default dimension. This is either specified via `POWERTOOLS_SERVICE_NAME` environment variable or via `service` attribute on `Metrics` annotation. If you wish to override the default Dimension, it can be done via `MetricsUtils.defaultDimensions()`.

```
import software.amazon.lambda.powertools.metrics.Metrics;
import static software.amazon.lambda.powertools.metrics.MetricsUtils;

public class App implements RequestHandler<Object, Object> {

    MetricsLogger metricsLogger = MetricsUtils.metricsLogger();

    static {
        MetricsUtils.defaultDimensions(DimensionSet.of("CustomDimension", "booking"));
    }

    @Override
    @Metrics(namespace = "ExampleApplication", service = "booking")
    public Object handleRequest(Object input, Context context) {
        ...
        MetricsUtils.withSingleMetric("Metric2", 1, Unit.COUNT, log -> {});
    }
}

```

## Creating a metric with a different dimension

CloudWatch EMF uses the same dimensions across all your metrics. Use `withSingleMetric` if you have a metric that should have different dimensions.

Info

Generally, this would be an edge case since you [pay for unique metric](https://aws.amazon.com/cloudwatch/pricing/). Keep the following formula in mind: **unique metric = (metric_name + dimension_name + dimension_value)**

```
import static software.amazon.lambda.powertools.metrics.MetricsUtils.withSingleMetric;

public class App implements RequestHandler<Object, Object> {

    @Override
    public Object handleRequest(Object input, Context context) {
         withSingleMetric("CustomMetrics2", 1, Unit.COUNT, "Another", (metric) -> {
            metric.setDimensions(DimensionSet.of("AnotherService", "CustomService"));
        });
    }
}

```

## Creating metrics with different configurations

Use `withMetricsLogger` if you have one or more metrics that should have different configurations e.g. dimensions or namespace.

```
import static software.amazon.lambda.powertools.metrics.MetricsUtils.withMetricsLogger;

public class App implements RequestHandler<Object, Object> {

    @Override
    public Object handleRequest(Object input, Context context) {
         withMetricsLogger(logger -> {
            // override default dimensions
            logger.setDimensions(DimensionSet.of("AnotherService", "CustomService"));
            // add metrics
            logger.putMetric("CustomMetrics1", 1, Unit.COUNT);
            logger.putMetric("CustomMetrics2", 5, Unit.COUNT);
        });
    }
}

```

Powertools tracing is an opinionated thin wrapper for [AWS X-Ray Java SDK](https://github.com/aws/aws-xray-sdk-java/) a provides functionality to reduce the overhead of performing common tracing tasks.

**Key Features**

- Capture cold start as annotation, and responses as well as full exceptions as metadata
- Helper methods to improve the developer experience of creating new X-Ray subsegments.
- Better developer experience when developing with multiple threads.
- Auto patch supported modules by AWS X-Ray

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-tracing</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-tracing</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-tracing</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-tracing</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-tracing:1.20.2'
    }

    sourceCompatibility = 11
    targetCompatibility = 11

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-tracing:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Initialization

Before your use this utility, your AWS Lambda function [must have permissions](https://docs.aws.amazon.com/lambda/latest/dg/services-xray.html#services-xray-permissions) to send traces to AWS X-Ray.

> Example using AWS Serverless Application Model (SAM)

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11

        Tracing: Active
        Environment:
            Variables:
                POWERTOOLS_SERVICE_NAME: example

```

The Powertools for AWS Lambda (Java) service name is used as the X-Ray namespace. This can be set using the environment variable `POWERTOOLS_SERVICE_NAME`

### Lambda handler

To enable Powertools for AWS Lambda (Java) tracing to your function add the `@Tracing` annotation to your `handleRequest` method or on any method will capture the method as a separate subsegment automatically. You can optionally choose to customize segment name that appears in traces.

```
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        businessLogic1();

        businessLogic2();
    }

    @Tracing
    public void businessLogic1(){

    }

    @Tracing
    public void businessLogic2(){

    }
}

```

```
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing(segmentName="yourCustomName")
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
    ...
    }

```

When using this `@Tracing` annotation, Utility performs these additional tasks to ease operations:

- Creates a `ColdStart` annotation to easily filter traces that have had an initialization overhead.
- Creates a `Service` annotation if service parameter or `POWERTOOLS_SERVICE_NAME` is set.
- Captures any response, or full exceptions generated by the handler, and include as tracing metadata.

By default, this annotation will automatically record method responses and exceptions. You can change the default behavior by setting the environment variables `POWERTOOLS_TRACER_CAPTURE_RESPONSE` and `POWERTOOLS_TRACER_CAPTURE_ERROR` as needed. Optionally, you can override behavior by different supported `captureMode` to record response, exception or both.

Returning sensitive information from your Lambda handler or functions, where `Tracing` is used?

You can disable annotation from capturing their responses and exception as tracing metadata with **`captureMode=DISABLED`** or globally by setting environment variables **`POWERTOOLS_TRACER_CAPTURE_RESPONSE`** and **`POWERTOOLS_TRACER_CAPTURE_ERROR`** to **`false`**

```
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing(captureMode=CaptureMode.DISABLED)
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
    ...
    }

```

```
Resources:
    HelloWorldFunction:
        Type: AWS::Serverless::Function
        Properties:
        ...
        Runtime: java11

        Tracing: Active
        Environment:
            Variables:
                POWERTOOLS_TRACER_CAPTURE_RESPONSE: false
                POWERTOOLS_TRACER_CAPTURE_ERROR: false

```

### Annotations & Metadata

**Annotations** are key-values associated with traces and indexed by AWS X-Ray. You can use them to filter traces and to create [Trace Groups](https://aws.amazon.com/about-aws/whats-new/2018/11/aws-xray-adds-the-ability-to-group-traces/) to slice and dice your transactions.

**Metadata** are key-values also associated with traces but not indexed by AWS X-Ray. You can use them to add additional context for an operation using any native object.

You can add annotations using `putAnnotation()` method from TracingUtils

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        TracingUtils.putAnnotation("annotation", "value");
    }
}

```

You can add metadata using `putMetadata()` method from TracingUtils

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Tracing
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        TracingUtils.putMetadata("content", "value");
    }
}

```

## Override default object mapper

You can optionally choose to override default object mapper which is used to serialize method response and exceptions when enabled. You might want to supply custom object mapper in order to control how serialisation is done, for example, when you want to log only specific fields from received event due to security.

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;
import static software.amazon.lambda.powertools.tracing.CaptureMode.RESPONSE;

/**
 * Handler for requests to Lambda function.
 */
public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> { 
    static {
        ObjectMapper objectMapper = new ObjectMapper();
        SimpleModule simpleModule = new SimpleModule();
        objectMapper.registerModule(simpleModule);

        TracingUtils.defaultObjectMapper(objectMapper);
    }

    @Tracing(captureMode = RESPONSE)
    public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent input, final Context context) {
        ...
    }
}

```

## Utilities

Tracing modules comes with certain utility method when you don't want to use annotation for capturing a code block under a subsegment, or you are doing multithreaded programming. Refer examples below.

```
import software.amazon.lambda.powertools.tracing.Tracing;
import software.amazon.lambda.powertools.tracing.TracingUtils;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
         TracingUtils.withSubsegment("loggingResponse", subsegment -> {
            // Some business logic
         });

         TracingUtils.withSubsegment("localNamespace", "loggingResponse", subsegment -> {
            // Some business logic
         });
    }
}

```

```
import static software.amazon.lambda.powertools.tracing.TracingUtils.withEntitySubsegment;

public class App implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        // Extract existing trace data
        Entity traceEntity = AWSXRay.getTraceEntity();

        Thread anotherThread = new Thread(() -> withEntitySubsegment("inlineLog", traceEntity, subsegment -> {
            // Business logic in separate thread
        }));
    }
}

```

## Instrumenting SDK clients and HTTP calls

Powertools for Lambda (Java) cannot intercept SDK clients instantiation to add X-Ray instrumentation. You should make sure to instrument the SDK clients explicitly. Refer details on [how to instrument SDK client with Xray](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java.html#xray-sdk-java-awssdkclients) and [outgoing http calls](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java.html#xray-sdk-java-httpclients). For example:

```
import com.amazonaws.xray.AWSXRay;
import com.amazonaws.xray.handlers.TracingHandler;

public class LambdaHandler {
    private AmazonDynamoDB client = AmazonDynamoDBClientBuilder.standard()
        .withRegion(Regions.fromName(System.getenv("AWS_REGION")))
        .withRequestHandlers(new TracingHandler(AWSXRay.getGlobalRecorder()))
        .build();
    // ...
}

```

## Testing your code

When using `@Tracing` annotation, your Junit test cases needs to be configured to create parent Segment required by [AWS X-Ray SDK for Java](https://docs.aws.amazon.com/xray/latest/devguide/xray-sdk-java.html).

Below are two ways in which you can configure your tests.

#### Configure environment variable on project level (Recommended)

You can choose to configure environment variable on project level for your test cases run. This is recommended approach as it will avoid the need of configuring each test case specifically.

Below are examples configuring your maven/gradle projects. You can choose to configure it differently as well as long as you are making sure that environment variable `LAMBDA_TASK_ROOT` is set. This variable is used internally via AWS X-Ray SDK to configure itself properly for lambda runtime.

```
<build>
    ...
  <plugins>
    <!--  Configures environment variable to avoid initialization of AWS X-Ray segments for each tests-->
      <plugin>
          <groupId>org.apache.maven.plugins</groupId>
          <artifactId>maven-surefire-plugin</artifactId>
          <configuration>
              <environmentVariables>
                  <LAMBDA_TASK_ROOT>handler</LAMBDA_TASK_ROOT>
              </environmentVariables>
          </configuration>
      </plugin>
  </plugins>
</build>

```

```
// Configures environment variable to avoid initialization of AWS X-Ray segments for each tests
test {
    environment "LAMBDA_TASK_ROOT", "handler"
}

```

#### Configure test cases (Not Recommended)

You can choose to configure each of your test case instead as well if you choose not to configure environment variable on project level. Below is an example configuration needed for each test case.

```
import com.amazonaws.xray.AWSXRay;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class AppTest {

    @Before
    public void setup() {
        if(null == System.getenv("LAMBDA_TASK_ROOT")) {
            AWSXRay.beginSegment("test");
        }
    }

    @After
    public void tearDown() {
        // Needed when using sam build --use-container
        if (AWSXRay.getCurrentSubsegmentOptional().isPresent()) {
            AWSXRay.endSubsegment();
        }

        if(null == System.getenv("LAMBDA_TASK_ROOT")) {
          AWSXRay.endSegment();
        }
    }

    @Test
    public void successfulResponse() {
        // test logic
    }

```
# Utilities

The batch processing utility provides a way to handle partial failures when processing batches of messages from SQS queues, SQS FIFO queues, Kinesis Streams, or DynamoDB Streams.

```
stateDiagram-v2
    direction LR
    BatchSource: Amazon SQS <br/><br/> Amazon Kinesis Data Streams <br/><br/> Amazon DynamoDB Streams <br/><br/>
    LambdaInit: Lambda invocation
    BatchProcessor: Batch Processor
    RecordHandler: Record Handler function
    YourLogic: Your logic to process each batch item
    LambdaResponse: Lambda response
    BatchSource --> LambdaInit
    LambdaInit --> BatchProcessor
    BatchProcessor --> RecordHandler
    state BatchProcessor {
        [*] --> RecordHandler: Your function
        RecordHandler --> YourLogic
    }
    RecordHandler --> BatchProcessor: Collect results
    BatchProcessor --> LambdaResponse: Report items that failed processing
```

**Key Features**

- Reports batch item failures to reduce number of retries for a record upon errors
- Simple interface to process each batch record
- Integrates with Java Events library and the deserialization module
- Build your own batch processor by extending primitives

**Background**

When using SQS, Kinesis Data Streams, or DynamoDB Streams as a Lambda event source, your Lambda functions are triggered with a batch of messages. If your function fails to process any message from the batch, the entire batch returns to your queue or stream. This same batch is then retried until either condition happens first: **a)** your Lambda function returns a successful response, **b)** record reaches maximum retry attempts, or **c)** records expire.

```
journey
  section Conditions
    Successful response: 5: Success
    Maximum retries: 3: Failure
    Records expired: 1: Failure
```

This behavior changes when you enable Report Batch Item Failures feature in your Lambda function event source configuration:

- [**SQS queues**](#sqs-standard). Only messages reported as failure will return to the queue for a retry, while successful ones will be deleted.
- [**Kinesis data streams**](#kinesis-and-dynamodb-streams) and [**DynamoDB streams**](#kinesis-and-dynamodb-streams). Single reported failure will use its sequence number as the stream checkpoint. Multiple reported failures will use the lowest sequence number as checkpoint.

With this utility, batch records are processed individually â only messages that failed to be processed return to the queue or stream for a further retry. You simply build a `BatchProcessor` in your handler, and return its response from the handler's `processMessage` implementation. Exceptions are handled internally and an appropriate partial response for the message source is returned to Lambda for you.

Warning

While this utility lowers the chance of processing messages more than once, it is still not guaranteed. We recommend implementing processing logic in an idempotent manner wherever possible, for instance, by taking advantage of [the idempotency module](../idempotency/). More details on how Lambda works with SQS can be found in the [AWS documentation](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)

## Install

We simply add `powertools-batch` to our build dependencies. Note - if you are using other Powertools modules that require code-weaving, such as `powertools-core`, you will need to configure that also.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-batch</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>

```

```
    repositories {
        mavenCentral()
    }

    dependencies {
        implementation 'software.amazon.lambda:powertools-batch:1.20.2'
    }

```

## Getting Started

For this feature to work, you need to **(1)** configure your Lambda function event source to use `ReportBatchItemFailures`, and **(2)** return a specific response to report which records failed to be processed.

You can use your preferred deployment framework to set the correct configuration while this utility, while the `powertools-batch` module handles generating the response, which simply needs to be returned as the result of your Lambda handler.

A complete [Serverless Application Model](https://aws.amazon.com/serverless/sam/) example can be found [here](https://github.com/aws-powertools/powertools-lambda-java/tree/main/examples/powertools-examples-batch) covering all of the batch sources.

For more information on configuring `ReportBatchItemFailures`, see the details for [SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-batchfailurereporting), [Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-batchfailurereporting),and [DynamoDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-batchfailurereporting).

You do not need any additional IAM permissions to use this utility, except for what each event source requires.

### Processing messages from SQS

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.SQSBatchResponse;
import com.amazonaws.services.lambda.runtime.events.SQSEvent;
import software.amazon.lambda.powertools.batch.BatchMessageHandlerBuilder;
import software.amazon.lambda.powertools.batch.handler.BatchMessageHandler;

public class SqsBatchHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {

    private final BatchMessageHandler<SQSEvent, SQSBatchResponse> handler;

    public SqsBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withSqsBatchHandler()
                .buildWithMessageHandler(this::processMessage, Product.class);
    }

    @Override
    public SQSBatchResponse handleRequest(SQSEvent sqsEvent, Context context) {
        return handler.processBatch(sqsEvent, context);
    }


    private void processMessage(Product p, Context c) {
        // Process the product
    }

}

```

```
public class Product {
    private long id;

    private String name;

    private double price;

    public Product() {
    }

    public Product(long id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

```

```
    {
        "Records": [
        {
            "messageId": "d9144555-9a4f-4ec3-99a0-34ce359b4b54",
            "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
            "body": "{\n  \"id\": 1234,\n  \"name\": \"product\",\n  \"price\": 42\n}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1601975706495",
                "SenderId": "AROAIFU437PVZ5L2J53F5",
                "ApproximateFirstReceiveTimestamp": "1601975706499"
            },
            "messageAttributes": {
            },
            "md5OfBody": "13e7f7851d2eaa5c01f208ebadbf1e72",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:eu-central-1:123456789012:TestLambda",
            "awsRegion": "eu-central-1"
        },
        {
            "messageId": "e9144555-9a4f-4ec3-99a0-34ce359b4b54",
            "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
            "body": "{\n  \"id\": 12345,\n  \"name\": \"product5\",\n  \"price\": 45\n}",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1601975706495",
                "SenderId": "AROAIFU437PVZ5L2J53F5",
                "ApproximateFirstReceiveTimestamp": "1601975706499"
            },
            "messageAttributes": {
            },
            "md5OfBody": "13e7f7851d2eaa5c01f208ebadbf1e72",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:eu-central-1:123456789012:TestLambda",
            "awsRegion": "eu-central-1"
        }]
    }

```

### Processing messages from Kinesis Streams

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.KinesisEvent;
import com.amazonaws.services.lambda.runtime.events.StreamsEventResponse;
import software.amazon.lambda.powertools.batch.BatchMessageHandlerBuilder;
import software.amazon.lambda.powertools.batch.handler.BatchMessageHandler;

public class KinesisBatchHandler implements RequestHandler<KinesisEvent, StreamsEventResponse> {

    private final BatchMessageHandler<KinesisEvent, StreamsEventResponse> handler;

    public KinesisBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withKinesisBatchHandler()
                .buildWithMessageHandler(this::processMessage, Product.class);
    }

    @Override
    public StreamsEventResponse handleRequest(KinesisEvent kinesisEvent, Context context) {
        return handler.processBatch(kinesisEvent, context);
    }

    private void processMessage(Product p, Context c) {
        // process the product
    }

}

```

```
public class Product {
    private long id;

    private String name;

    private double price;

    public Product() {
    }

    public Product(long id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

```

```
    {
      "Records": [
        {
          "kinesis": {
            "partitionKey": "partitionKey-03",
            "kinesisSchemaVersion": "1.0",
            "data": "eyJpZCI6MTIzNCwgIm5hbWUiOiJwcm9kdWN0IiwgInByaWNlIjo0Mn0=",
            "sequenceNumber": "49545115243490985018280067714973144582180062593244200961",
            "approximateArrivalTimestamp": 1428537600,
            "encryptionType": "NONE"
          },
          "eventSource": "aws:kinesis",
          "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",
          "invokeIdentityArn": "arn:aws:iam::EXAMPLE",
          "eventVersion": "1.0",
          "eventName": "aws:kinesis:record",
          "eventSourceARN": "arn:aws:kinesis:EXAMPLE",
          "awsRegion": "eu-central-1"
        },
        {
          "kinesis": {
            "partitionKey": "partitionKey-03",
            "kinesisSchemaVersion": "1.0",
            "data": "eyJpZCI6MTIzNDUsICJuYW1lIjoicHJvZHVjdDUiLCAicHJpY2UiOjQ1fQ==",
            "sequenceNumber": "49545115243490985018280067714973144582180062593244200962",
            "approximateArrivalTimestamp": 1428537600,
            "encryptionType": "NONE"
          },
          "eventSource": "aws:kinesis",
          "eventID": "shardId-000000000000:49545115243490985018280067714973144582180062593244200961",
          "invokeIdentityArn": "arn:aws:iam::EXAMPLE",
          "eventVersion": "1.0",
          "eventName": "aws:kinesis:record",
          "eventSourceARN": "arn:aws:kinesis:EXAMPLE",
          "awsRegion": "eu-central-1"
        }
      ]
    }

```

### Processing messages from DynamoDB Streams

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;
import com.amazonaws.services.lambda.runtime.events.DynamodbEvent;
import com.amazonaws.services.lambda.runtime.events.StreamsEventResponse;
import software.amazon.lambda.powertools.batch.BatchMessageHandlerBuilder;
import software.amazon.lambda.powertools.batch.handler.BatchMessageHandler;

public class DynamoDBStreamBatchHandler implements RequestHandler<DynamodbEvent, StreamsEventResponse> {

    private final BatchMessageHandler<DynamodbEvent, StreamsEventResponse> handler;

    public DynamoDBStreamBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withDynamoDbBatchHandler()
                .buildWithRawMessageHandler(this::processMessage);
    }

    @Override
    public StreamsEventResponse handleRequest(DynamodbEvent ddbEvent, Context context) {
        return handler.processBatch(ddbEvent, context);
    }

    private void processMessage(DynamodbEvent.DynamodbStreamRecord dynamodbStreamRecord, Context context) {
        // Process the change record
    }
}

```

```
    {
      "Records": [
        {
          "eventID": "c4ca4238a0b923820dcc509a6f75849b",
          "eventName": "INSERT",
          "eventVersion": "1.1",
          "eventSource": "aws:dynamodb",
          "awsRegion": "eu-central-1",
          "dynamodb": {
            "Keys": {
              "Id": {
                "N": "101"
              }
            },
            "NewImage": {
              "Message": {
                "S": "New item!"
              },
              "Id": {
                "N": "101"
              }
            },
            "ApproximateCreationDateTime": 1428537600,
            "SequenceNumber": "4421584500000000017450439091",
            "SizeBytes": 26,
            "StreamViewType": "NEW_AND_OLD_IMAGES"
          },
          "eventSourceARN": "arn:aws:dynamodb:eu-central-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899",
          "userIdentity": {
            "principalId": "dynamodb.amazonaws.com",
            "type": "Service"
          }
        },
        {
          "eventID": "c81e728d9d4c2f636f067f89cc14862c",
          "eventName": "MODIFY",
          "eventVersion": "1.1",
          "eventSource": "aws:dynamodb",
          "awsRegion": "eu-central-1",
          "dynamodb": {
            "Keys": {
              "Id": {
                "N": "101"
              }
            },
            "NewImage": {
              "Message": {
                "S": "This item has changed"
              },
              "Id": {
                "N": "101"
              }
            },
            "OldImage": {
              "Message": {
                "S": "New item!"
              },
              "Id": {
                "N": "101"
              }
            },
            "ApproximateCreationDateTime": 1428537600,
            "SequenceNumber": "4421584500000000017450439092",
            "SizeBytes": 59,
            "StreamViewType": "NEW_AND_OLD_IMAGES"
          },
          "eventSourceARN": "arn:aws:dynamodb:eu-central-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899"
        }
      ]
    }

```

## Handling Messages

### Raw message and deserialized message handlers

You must provide either a raw message handler, or a deserialized message handler. The raw message handler receives the envelope record type relevant for the particular event source - for instance, the SQS event source provides [SQSMessage](https://javadoc.io/doc/com.amazonaws/aws-lambda-java-events/2.2.2/com/amazonaws/services/lambda/runtime/events/SQSEvent.html) instances. The deserialized message handler extracts the body from this envelope, and deserializes it to a user-defined type. Note that deserialized message handlers are not relevant for the DynamoDB provider, as the format of the inner message is fixed by DynamoDB.

In general, the deserialized message handler should be used unless you need access to information on the envelope.

```
public void setup() {
    BatchMessageHandler<SQSEvent, SQSBatchResponse> handler = new BatchMessageHandlerBuilder()
            .withSqsBatchHandler()
            .buildWithRawMessageHandler(this::processRawMessage);
}

private void processRawMessage(SQSEvent.SQSMessage sqsMessage) {
    // Do something with the raw message
}

```

```
public void setup() {
    BatchMessageHandler<SQSEvent, SQSBatchResponse> handler = new BatchMessageHandlerBuilder()
            .withSqsBatchHandler()
            .buildWitMessageHandler(this::processRawMessage, Product.class);
}

private void processMessage(Product product) {
    // Do something with the deserialized message
}

```

### Success and failure handlers

You can register a success or failure handler which will be invoked as each message is processed by the batch module. This may be useful for reporting - for instance, writing metrics or logging failures.

These handlers are optional. Batch failures are handled by the module regardless of whether or not you provide a custom failure handler.

Handlers can be provided when building the batch processor and are available for all event sources. For instance for DynamoDB:

```
BatchMessageHandler<DynamodbEvent, StreamsEventResponse> handler = new BatchMessageHandlerBuilder()
            .withDynamoDbBatchHandler()
            .withSuccessHandler((m) -> {
                // Success handler receives the raw message
                LOGGER.info("Message with sequenceNumber {} was successfully processed",
                    m.getDynamodb().getSequenceNumber());
            })
            .withFailureHandler((m, e) -> {
                // Failure handler receives the raw message and the exception thrown.
                LOGGER.info("Message with sequenceNumber {} failed to be processed: {}"
                , e.getDynamodb().getSequenceNumber(), e);
            })
            .buildWithMessageHander(this::processMessage);

```

Info

If the success handler throws an exception, the item it is processing will be marked as failed by the batch processor. If the failure handler throws, the batch processing will continue; the item it is processing has already been marked as failed.

### Lambda Context

Both raw and deserialized message handlers can choose to take the Lambda context as an argument if they need it, or not:

```
    public class ClassWithHandlers {

        private void processMessage(Product product) {
            // Do something with the raw message
        }

        private void processMessageWithContext(Product product, Context context) {
            // Do something with the raw message and the lambda Context
        }
    }

```

[CloudFormation Custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources.html) provide a way for [AWS Lambda functions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html) to execute provisioning logic whenever CloudFormation stacks are created, updated, or deleted.

Powertools-cloudformation makes it easy to write Lambda functions in Java that are used as CloudFormation custom resources.\
The utility reads incoming CloudFormation events, calls your custom code depending on the operation (CREATE, UPDATE or DELETE) and sends responses back to CloudFormation.\
By using this library you do not need to write code to integrate with CloudFormation, and you only focus on writing the custom provisioning logic inside the Lambda function.

## Install

To install this utility, add the following dependency to your project.

```
<dependency>
    <groupId>software.amazon.lambda</groupId>
    <artifactId>powertools-cloudformation</artifactId>
    <version>1.20.2</version>
</dependency>

```

```
 dependencies {
    ...
    implementation 'software.amazon.lambda:powertools-cloudformation:1.20.2'
}

```

## Usage

To utilise the feature, extend the `AbstractCustomResourceHandler` class in your Lambda handler class.\
Next, implement and override the following 3 methods: `create`, `update` and `delete`. The `AbstractCustomResourceHandler` invokes the right method according to the CloudFormation [custom resource request event](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-requests.html) it receives.\
Inside the methods, implement your custom provisioning logic, and return a `Response`. The `AbstractCustomResourceHandler` takes your `Response`, builds a [custom resource responses](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/crpg-ref-responses.html) and sends it to CloudFormation automatically.

Custom resources notify cloudformation either of `SUCCESS` or `FAILED` status. You have 2 utility methods to represent these responses: `Response.success(physicalResourceId)` and `Response.failed(physicalResourceId)`.\
The `physicalResourceId` is an identifier that is used during the lifecycle operations of the Custom Resource.\
You should generate a `physicalResourceId` during the `CREATE` operation, CloudFormation stores the `physicalResourceId` and includes it in `UPDATE` and `DELETE` events.

Here an example of how to implement a Custom Resource using the powertools-cloudformation library:

```
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.events.CloudFormationCustomResourceEvent;
import software.amazon.lambda.powertools.cloudformation.AbstractCustomResourceHandler;
import software.amazon.lambda.powertools.cloudformation.Response;

public class MyCustomResourceHandler extends AbstractCustomResourceHandler {

    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "sample-resource-id-" + UUID.randomUUID(); //Create a unique ID for your resource
        ProvisioningResult provisioningResult = doProvisioning(physicalResourceId);
        if(provisioningResult.isSuccessful()){ //check if the provisioning was successful
            return Response.success(physicalResourceId);
        }else{
            return Response.failed(physicalResourceId);
        }
    }

    @Override
    protected Response update(CloudFormationCustomResourceEvent updateEvent, Context context) {
        String physicalResourceId = updateEvent.getPhysicalResourceId(); //Get the PhysicalResourceId from CloudFormation
        UpdateResult updateResult = doUpdates(physicalResourceId);
        if(updateResult.isSuccessful()){ //check if the update operations were successful
            return Response.success(physicalResourceId);
        }else{
            return Response.failed(physicalResourceId);
        }
    }

    @Override
    protected Response delete(CloudFormationCustomResourceEvent deleteEvent, Context context) {
        String physicalResourceId = deleteEvent.getPhysicalResourceId(); //Get the PhysicalResourceId from CloudFormation
        DeleteResult deleteResult = doDeletes(physicalResourceId);
        if(deleteResult.isSuccessful()){ //check if the delete operations were successful
            return Response.success(physicalResourceId);
        }else{
            return Response.failed(physicalResourceId);
        }
    }
}

```

### Missing `Response` and exception handling

If a `Response` is not returned by your code, `AbstractCustomResourceHandler` defaults the response to `SUCCESS`.\
If your code raises an exception (which is not handled), the `AbstractCustomResourceHandler` defaults the response to `FAILED`.

In both of the scenarios, powertools-java will return the `physicalResourceId` to CloudFormation based on the following logic:

- For CREATE operations, the `LogStreamName` from the Lambda context is used.
- For UPDATE and DELETE operations, the `physicalResourceId` provided in the `CloudFormationCustomResourceEvent` is used.

#### Why do you need a physicalResourceId?

It is recommended that you always explicitly provide a `physicalResourceId` in your response rather than letting Powertools for AWS Lambda (Java) generate if for you because `physicalResourceId` has a crucial role in the lifecycle of a CloudFormation custom resource. If the `physicalResourceId` changes between calls from Cloudformation, for instance in response to an `Update` event, Cloudformation [treats the resource update as a replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cfn-customresource.html).

### Customising a response

As well as the `Response.success(physicalResourceId)` and `Response.failed(physicalResourceId)`, you can customise the `Response` by using the `Response.builder()`. You customise the responses when you need additional attributes to be shared with other parts of the CloudFormation stack.

In the example below, the Lambda function creates a [Chime AppInstance](https://docs.aws.amazon.com/chime/latest/dg/create-app-instance.html) and maps the returned ARN to a "ChimeAppInstanceArn" attribute.

```
public class ChimeAppInstanceHandler extends AbstractCustomResourceHandler {
    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "my-app-name-" + UUID.randomUUID(); //Create a unique ID 
        CreateAppInstanceRequest chimeRequest = CreateAppInstanceRequest.builder()
                .name(physicalResourceId)
                .build();
        CreateAppInstanceResponse chimeResponse = ChimeClient.builder()
                .region("us-east-1")
                .createAppInstance(chimeRequest);

        Map<String, String> chimeAtts = Map.of("ChimeAppInstanceArn", chimeResponse.appInstanceArn());
        return Response.builder()
                .value(chimeAtts)
                .status(Response.Status.SUCCESS)
                .physicalResourceId(physicalResourceId)
                .build();
    }
}

```

For the example above the following response payload will be sent.

```
{
  "Status": "SUCCESS",
  "PhysicalResourceId": "2021/10/01/e3a37e552eff4718a5675c1e31f0649e",
  "StackId": "arn:aws:cloudformation:us-east-1:123456789000:stack/Custom-stack/59e4d2d0-2fe2-10ec-b00e-124d7c1c5f15",
  "RequestId": "7cae0346-0359-4dff-b80a-a82f247467b6",
  "LogicalResourceId:": "ChimeTriggerResource",
  "PhysicalResourceId:": "my-app-name-db4a47b9-0cac-45ba-8cc4-a480490c5779",
  "NoEcho": false,
  "Data": {
    "ChimeAppInstanceArn": "arn:aws:chime:us-east-1:123456789000:app-instance/150972c2-5490-49a9-8ba7-e7da4257c16a"
  }
}

```

Once the custom resource receives this response, its "ChimeAppInstanceArn" attribute is set and the [Fn::GetAtt function](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html) may be used to retrieve the attribute value and make it available to other resources in the stack.

#### Sensitive Response Data

If any attributes are sensitive, enable the "noEcho" flag to mask the output of the custom resource when it's retrieved with the Fn::GetAtt function.

```
public class SensitiveDataHandler extends AbstractResourceHandler {
    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "my-sensitive-resource-" + UUID.randomUUID(); //Create a unique ID 
        return Response.builder()
                .status(Response.Status.SUCCESS)
                .physicalResourceId(physicalResourceId)
                .value(Map.of("SomeSecret", sensitiveValue))
                .noEcho(true)
                .build();
    }
}

```

#### Customizing Serialization

Although using a `Map` as the Response's value is the most straightforward way to provide attribute name/value pairs, any arbitrary `java.lang.Object` may be used. By default, these objects are serialized with an internal Jackson `ObjectMapper`. If the object requires special serialization logic, a custom `ObjectMapper` can be specified.

```
public class CustomSerializationHandler extends AbstractResourceHandler {
    /**
     * Type representing the custom response Data. 
     */
    static class Policy {
        public ZonedDateTime getExpires() {
            return ZonedDateTime.now().plusDays(10);
        }
    }

    /**
     * Mapper for serializing Policy instances.
     */
    private final ObjectMapper policyMapper = new ObjectMapper()
            .registerModule(new JavaTimeModule())
            .disable(SerializationFeature.WRITE_DATES_AS_TIMESTAMPS);

    @Override
    protected Response create(CloudFormationCustomResourceEvent createEvent, Context context) {
        String physicalResourceId = "my-policy-name-" + UUID.randomUUID(); //Create a unique ID 
        Policy policy = new Policy();
        return Response.builder()
                .status(Response.Status.SUCCESS)
                .physicalResourceId(physicalResourceId)
                .value(policy)
                .objectMapper(policyMapper) // customize serialization
                .build();
    }
}

```

## Advanced

### Understanding the CloudFormation custom resource lifecycle

While the library provides an easy-to-use interface, we recommend that you understand the lifecycle of CloudFormation custom resources before using them in production.

#### Creating a custom resource

When CloudFormation issues a CREATE on a custom resource, there are 2 possible states: `CREATE_COMPLETE` and `CREATE_FAILED`

```
stateDiagram
    direction LR
    createState: Create custom resource
    [*] --> createState
    createState --> CREATE_COMPLETE 
    createState --> CREATE_FAILED
```

If the resource is created successfully, the `physicalResourceId` is stored by CloudFormation for future operations.\
If the resource failed to create, CloudFormation triggers a rollback operation by default (rollback can be disabled, see [stack failure options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-failure-options.html))

#### Updating a custom resource

CloudFormation issues an UPDATE operation on a custom resource only when one or more custom resource properties change. During the update, the custom resource may update successfully, or may fail the update.

```
stateDiagram
    direction LR
    updateState: Update custom resource
    [*] --> updateState
    updateState --> UPDATE_COMPLETE 
    updateState --> UPDATE_FAILED
```

In both of these scenarios, the custom resource can return the same `physicalResourceId` it received in the CloudFormation event, or a different `physicalResourceId`.\
Semantically an `UPDATE_COMPLETE` that returns the same `physicalResourceId` it received indicates that the existing resource was updated successfully.\
Instead, an `UPDATE_COMPLETE` with a different `physicalResourceId` means that a new physical resource was created successfully.

```
flowchart BT
    id1(Logical resource)
    id2(Previous physical Resource)
    id3(New physical Resource)
    id2 --> id1 
    id3 --> id1 
```

Therefore, after the custom resource update completed or failed, there may be other cleanup operations by Cloudformation during the rollback, as described in the diagram below:

```
stateDiagram
    state if_state <<choice>>
    updateState: Update custom resource
    deletePrev: DELETE resource with previous physicalResourceId
    updatePrev: Rollback - UPDATE resource with previous properties
    noOp: No further operations
    [*] --> updateState
    updateState --> UPDATE_COMPLETE
    UPDATE_COMPLETE --> if_state
    if_state --> noOp : Same physicalResourceId
    if_state --> deletePrev : Different physicalResourceId
    updateState --> UPDATE_FAILED
    UPDATE_FAILED --> updatePrev
```

#### Deleting a custom resource

CloudFormation issues a DELETE on a custom resource when:

- the CloudFormation stack is being deleted
- a new `physicalResourceId` was received during an update, and CloudFormation proceeds to rollback(DELETE) the custom resource with the previous `physicalResourceId`.

```
stateDiagram
    direction LR
    deleteState: Delete custom resource
    [*] --> deleteState
    deleteState --> DELETE_COMPLETE 
    deleteState --> DELETE_FAILED
```

The idempotency utility provides a simple solution to convert your Lambda functions into idempotent operations which are safe to retry.

## Terminology

The property of idempotency means that an operation does not cause additional side effects if it is called more than once with the same input parameters.

**Idempotent operations will return the same result when they are called multiple times with the same parameters**. This makes idempotent operations safe to retry. [Read more](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) about idempotency.

**Idempotency key** is a hash representation of either the entire event or a specific configured subset of the event, and invocation results are **JSON serialized** and stored in your persistence storage layer.

## Key features

- Prevent Lambda handler function from executing more than once on the same event payload during a time window
- Ensure Lambda handler returns the same result when called with the same payload
- Select a subset of the event as the idempotency key using JMESPath expressions
- Set a time window in which records with the same payload should be considered duplicates

## Getting started

### Installation

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-idempotency</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-idempotency</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-idempotency</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-idempotency</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-idempotency:1.20.2'
    }

    sourceCompatibility = 11 // or higher
    targetCompatibility = 11 // or higher

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-idempotency:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

### Required resources

Before getting started, you need to create a persistent storage layer where the idempotency utility can store its state - your Lambda functions will need read and write access to it.

As of now, Amazon DynamoDB is the only supported persistent storage layer, so you'll need to create a table first.

**Default table configuration**

If you're not [changing the default configuration for the DynamoDB persistence layer](#dynamodbpersistencestore), this is the expected default configuration:

| Configuration | Value | Notes | | --- | --- | --- | | Partition key | `id` | | | TTL attribute name | `expiration` | This can only be configured after your table is created if you're using AWS Console |

Tip: You can share a single state table for all functions

You can reuse the same DynamoDB table to store idempotency state. We add your function name in addition to the idempotency key as a hash key.

```
Resources:
  IdempotencyTable:
    Type: AWS::DynamoDB::Table
    Properties:
      AttributeDefinitions:
        - AttributeName: id
          AttributeType: S
      KeySchema:
        - AttributeName: id
          KeyType: HASH
      TimeToLiveSpecification:
        AttributeName: expiration
        Enabled: true
      BillingMode: PAY_PER_REQUEST

  IdempotencyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: Function
      Handler: helloworld.App::handleRequest
      Policies:
        - DynamoDBCrudPolicy:
            TableName: !Ref IdempotencyTable
      Environment:
        Variables:
          IDEMPOTENCY_TABLE: !Ref IdempotencyTable

```

Warning: Large responses with DynamoDB persistence layer

When using this utility with DynamoDB, your function's responses must be [smaller than 400KB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Limits.html#limits-items). Larger items cannot be written to DynamoDB and will cause exceptions.

Info: DynamoDB

Each function invocation will generally make 2 requests to DynamoDB. If the result returned by your Lambda is less than 1kb, you can expect 2 WCUs per invocation. For retried invocations, you will see 1WCU and 1RCU. Review the [DynamoDB pricing documentation](https://aws.amazon.com/dynamodb/pricing/) to estimate the cost.

### Idempotent annotation

You can quickly start by initializing the `DynamoDBPersistenceStore` and using it with the `@Idempotent` annotation on your Lambda handler.

Important

Initialization and configuration of the `DynamoDBPersistenceStore` must be performed outside the handler, preferably in the constructor.

```
public class App implements RequestHandler<Subscription, SubscriptionResult> {

  public App() {
    // we need to initialize idempotency store before the handleRequest method is called
    Idempotency.config().withPersistenceStore(
      DynamoDBPersistenceStore.builder()
        .withTableName(System.getenv("TABLE_NAME"))
        .build()
      ).configure();
  }

  @Idempotent
  public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    SubscriptionPayment payment = createSubscriptionPayment(
      event.getUsername(),
      event.getProductId()
    );

    return new SubscriptionResult(payment.getId(), "success", 200);
  }
}

```

```
{
  "username": "xyz",
  "product_id": "123456789"
}

```

#### Idempotent annotation on another method

You can use the `@Idempotent` annotation for any synchronous Java function, not only the `handleRequest` one.

When using `@Idempotent` annotation on another method, you must tell which parameter in the method signature has the data we should use:

- If the method only has one parameter, it will be used by default.
- If there are 2 or more parameters, you must set the `@IdempotencyKey` on the parameter to use.

The parameter must be serializable in JSON. We use Jackson internally to (de)serialize objects

This example also demonstrates how you can integrate with [Batch utility](../batch/), so you can process each record in an idempotent manner.

```
public class AppSqsEvent implements RequestHandler<SQSEvent, String> {

  public AppSqsEvent() {
    Idempotency.config()
      .withPersistenceStore(
          DynamoDBPersistenceStore.builder()
            .withTableName(System.getenv("TABLE_NAME"))
            .build()
      ).withConfig(
           IdempotencyConfig.builder()
             .withEventKeyJMESPath("messageId") // see Choosing a payload subset section
             .build()
      ).configure();
    }

  @Override
  @SqsBatch(SampleMessageHandler.class)
  public String handleRequest(SQSEvent input, Context context) {
    dummy("hello", "world");
    return "{\"statusCode\": 200}";
  }

  @Idempotent
  private String dummy(String argOne, @IdempotencyKey String argTwo) {
    return "something";
  }

  public static class SampleMessageHandler implements SqsMessageHandler<Object> {
    @Override
    @Idempotent
    // no need to use @IdempotencyKey as there is only one parameter
    public String process(SQSMessage message) {
      String returnVal = doSomething(message.getBody());
      return returnVal;
    }
  }
}

```

```
{
    "Records": [
        {
            "messageId": "059f36b4-87a3-44ab-83d2-661975830a7d",
            "receiptHandle": "AQEBwJnKyrHigUMZj6rYigCgxlaS3SLy0a...",
            "body": "Test message.",
            "attributes": {
                "ApproximateReceiveCount": "1",
                "SentTimestamp": "1545082649183",
                "SenderId": "AIDAIENQZJOLO23YVJ4VO",
                "ApproximateFirstReceiveTimestamp": "1545082649185"
            },
            "messageAttributes": {
                "testAttr": {
                "stringValue": "100",
                "binaryValue": "base64Str",
                "dataType": "Number"
                }
            },
            "md5OfBody": "e4e68fb7bd0e697a0ae8f1bb342846b3",
            "eventSource": "aws:sqs",
            "eventSourceARN": "arn:aws:sqs:us-east-2:123456789012:my-queue",
            "awsRegion": "us-east-2"
        }
    ]
}

```

### Choosing a payload subset for idempotency

Tip: Dealing with always changing payloads

When dealing with an elaborate payload (API Gateway request for example), where parts of the payload always change, you should configure the **`EventKeyJMESPath`**.

Use [`IdempotencyConfig`](#customizing-the-default-behavior) to instruct the Idempotent annotation to only use a portion of your payload to verify whether a request is idempotent, and therefore it should not be retried.

> **Payment scenario**

In this example, we have a Lambda handler that creates a payment for a user subscribing to a product. We want to ensure that we don't accidentally charge our customer by subscribing them more than once.

Imagine the function executes successfully, but the client never receives the response due to a connection issue. It is safe to retry in this instance, as the idempotent decorator will return a previously saved response.

Warning: Idempotency for JSON payloads

The payload extracted by the `EventKeyJMESPath` is treated as a string by default, so will be sensitive to differences in whitespace even when the JSON payload itself is identical.

To alter this behaviour, you can use the [JMESPath built-in function](../serialization/#jmespath-functions) `powertools_json()` to treat the payload as a JSON object rather than a string.

```
public class PaymentFunction implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

  public PaymentFunction() {
    Idempotency.config()
    .withConfig(
        IdempotencyConfig.builder()
          .withEventKeyJMESPath("powertools_json(body)")
          .build())
    .withPersistenceStore(
        DynamoDBPersistenceStore.builder()
          .withTableName(System.getenv("TABLE_NAME"))
          .build())
    .configure();
}

@Idempotent
public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent event, final Context context) {
  APIGatewayProxyResponseEvent response = new APIGatewayProxyResponseEvent();

  try {
    Subscription subscription = JsonConfig.get().getObjectMapper().readValue(event.getBody(), Subscription.class);

    SubscriptionPayment payment = createSubscriptionPayment(
         subscription.getUsername(),
         subscription.getProductId()
    );

    return response
             .withStatusCode(200)
             .withBody(String.format("{\"paymentId\":\"%s\"}", payment.getId()));

  } catch (JsonProcessingException e) {
    return response.withStatusCode(500);
  }
}

```

```
{
  "version":"2.0",
  "body":"{\"username\":\"xyz\",\"productId\":\"123456789\"}",
  "routeKey":"ANY /createpayment",
  "rawPath":"/createpayment",
  "rawQueryString":"",
  "headers": {
    "Header1": "value1",
    "Header2": "value2"
  },
  "requestContext":{
    "accountId":"123456789012",
    "apiId":"api-id",
    "domainName":"id.execute-api.us-east-1.amazonaws.com",
    "domainPrefix":"id",
    "http":{
      "method":"POST",
      "path":"/createpayment",
      "protocol":"HTTP/1.1",
      "sourceIp":"ip",
      "userAgent":"agent"
    },
    "requestId":"id",
    "routeKey":"ANY /createpayment",
    "stage":"$default",
    "time":"10/Feb/2021:13:40:43 +0000",
    "timeEpoch":1612964443723
  },
  "isBase64Encoded":false
}

```

### Idempotency request flow

This sequence diagram shows an example flow of what happens in the payment scenario:

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        activate Persistence Layer
        Note right of Persistence Layer: Locked to prevent concurrent<br/>invocations with <br/> the same payload.
        Lambda-->>Lambda: Call handler (event)
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record with result
        Lambda-->>Client: Response sent to client
    else retried request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        Persistence Layer-->>Lambda: Already exists in persistence layer. Return result
        Lambda-->>Client: Response sent to client
    end
```

*Idempotent sequence*

The client was successful in receiving the result after the retry. Since the Lambda handler was only executed once, our customer hasn't been charged twice.

Note

Bear in mind that the entire Lambda handler is treated as a single idempotent operation. If your Lambda handler can cause multiple side effects, consider splitting it into separate functions.

#### Lambda timeouts

This is automatically done when you annotate your Lambda handler with [@Idempotent annotation](#idempotent-annotation).

To prevent against extended failed retries when a [Lambda function times out](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-verify-invocation-timeouts/), Powertools for AWS Lambda (Java) calculates and includes the remaining invocation available time as part of the idempotency record.

Example

If a second invocation happens **after** this timestamp, and the record is marked as `INPROGRESS`, we will execute the invocation again as if it was in the `EXPIRED` state. This means that if an invocation expired during execution, it will be quickly executed again on the next retry.

Important

If you are using the [@Idempotent annotation on another method](#idempotent-annotation-on-another-method) to guard isolated parts of your code, you must use `registerLambdaContext` method available in the `Idempotency` object to benefit from this protection.

Here is an example on how you register the Lambda context in your handler:

```
public class PaymentHandler implements RequestHandler<SQSEvent, List<String>> {

    public PaymentHandler() {
        Idempotency.config()
                .withPersistenceStore(
                        DynamoDBPersistenceStore.builder()
                                .withTableName(System.getenv("IDEMPOTENCY_TABLE"))
                                .build())
                .configure();
    }

    @Override
    public List<String> handleRequest(SQSEvent sqsEvent, Context context) {
        Idempotency.registerLambdaContext(context);
        return sqsEvent.getRecords().stream().map(record -> process(record.getMessageId(), record.getBody())).collect(Collectors.toList());
    }

    @Idempotent
    private String process(String messageId, @IdempotencyKey String messageBody) {
        logger.info("Processing messageId: {}", messageId);
        PaymentRequest request = extractDataFrom(messageBody).as(PaymentRequest.class);
        return paymentService.process(request);
    }

}

```

#### Lambda timeout sequence diagram

This sequence diagram shows an example flow of what happens if a Lambda function times out:

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Persistence Layer
    alt initial request
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        activate Persistence Layer
        Note right of Persistence Layer: Locked to prevent concurrent<br/>invocations with <br/> the same payload.
        Note over Lambda: Time out
        Lambda--xLambda: Call handler (event)
        Lambda-->>Client: Return error response
        deactivate Persistence Layer
    else concurrent request before timeout
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        Persistence Layer-->>Lambda: Request already INPROGRESS
        Lambda--xClient: Return IdempotencyAlreadyInProgressError
    else retry after Lambda timeout
        Client->>Lambda: Invoke (event)
        Lambda->>Persistence Layer: Get or set (id=event.search(payload))
        activate Persistence Layer
        Note right of Persistence Layer: Locked to prevent concurrent<br/>invocations with <br/> the same payload.
        Lambda-->>Lambda: Call handler (event)
        Lambda->>Persistence Layer: Update record with result
        deactivate Persistence Layer
        Persistence Layer-->>Persistence Layer: Update record with result
        Lambda-->>Client: Response sent to client
    end
```

*Idempotent sequence for Lambda timeouts*

### Handling exceptions

If you are using the `@Idempotent` annotation on your Lambda handler or any other method, any unhandled exceptions that are thrown during the code execution will cause **the record in the persistence layer to be deleted**. This means that new invocations will execute your code again despite having the same payload. If you don't want the record to be deleted, you need to catch exceptions within the idempotent function and return a successful response.

```
sequenceDiagram
    participant Client
    participant Lambda
    participant Persistence Layer
    Client->>Lambda: Invoke (event)
    Lambda->>Persistence Layer: Get or set (id=event.search(payload))
    activate Persistence Layer
    Note right of Persistence Layer: Locked during this time. Prevents multiple<br/>Lambda invocations with the same<br/>payload running concurrently.
    Lambda--xLambda: Call handler (event).<br/>Raises exception
    Lambda->>Persistence Layer: Delete record (id=event.search(payload))
    deactivate Persistence Layer
    Lambda-->>Client: Return error response
```

*Idempotent sequence exception*

If an Exception is raised *outside* the scope of a decorated method and after your method has been called, the persistent record will not be affected. In this case, idempotency will be maintained for your decorated function. Example:

```
  public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    // If an exception is thrown here, no idempotent record will ever get created as the
    // idempotent function does not get called 
    doSomeStuff();

    result = idempotentMethod(event);

    // This exception will not cause the idempotent record to be deleted, since it
    // happens after the decorated function has been successfully called    
    throw new Exception();
  }

  @Idempotent
  private String idempotentMethod(final Subscription subscription) {
    // perform some operation with no exception thrown
  }

```

Warning

**We will throw an `IdempotencyPersistenceLayerException`** if any of the calls to the persistence layer fail unexpectedly.

As this happens outside the scope of your decorated function, you are not able to catch it.

### Persistence stores

#### DynamoDBPersistenceStore

This persistence store is built-in, and you can either use an existing DynamoDB table or create a new one dedicated for idempotency state (recommended).

Use the builder to customize the table structure:

```
DynamoDBPersistenceStore.builder()
                        .withTableName(System.getenv("TABLE_NAME"))
                        .withKeyAttr("idempotency_key")
                        .withExpiryAttr("expires_at")
                        .withStatusAttr("current_status")
                        .withDataAttr("result_data")
                        .withValidationAttr("validation_key")
                        .build()

```

When using DynamoDB as a persistence layer, you can alter the attribute names by passing these parameters when initializing the persistence layer:

| Parameter | Required | Default | Description | | --- | --- | --- | --- | | **TableName** | Y | | Table name to store state | | **KeyAttr** | | `id` | Partition key of the table. Hashed representation of the payload (unless **SortKeyAttr** is specified) | | **ExpiryAttr** | | `expiration` | Unix timestamp of when record expires | | **StatusAttr** | | `status` | Stores status of the Lambda execution during and after invocation | | **DataAttr** | | `data` | Stores results of successfully idempotent methods | | **ValidationAttr** | | `validation` | Hashed representation of the parts of the event used for validation | | **SortKeyAttr** | | | Sort key of the table (if table is configured with a sort key). | | **StaticPkValue** | | `idempotency#{LAMBDA_FUNCTION_NAME}` | Static value to use as the partition key. Only used when **SortKeyAttr** is set. |

## Advanced

### Customizing the default behavior

Idempotency behavior can be further configured with **`IdempotencyConfig`** using a builder:

```
IdempotencyConfig.builder()
                .withEventKeyJMESPath("id")
                .withPayloadValidationJMESPath("paymentId")
                .withThrowOnNoIdempotencyKey(true)
                .withExpiration(Duration.of(5, ChronoUnit.MINUTES))
                .withUseLocalCache(true)
                .withLocalCacheMaxItems(432)
                .withHashFunction("SHA-256")
                .build()

```

These are the available options for further configuration:

| Parameter | Default | Description | | --- | --- | --- | | **EventKeyJMESPath** | `""` | JMESPath expression to extract the idempotency key from the event record. See available [built-in functions](serialization) | | **PayloadValidationJMESPath** | `""` | JMESPath expression to validate whether certain parameters have changed in the event | | **ThrowOnNoIdempotencyKey** | `False` | Throw exception if no idempotency key was found in the request | | **ExpirationInSeconds** | 3600 | The number of seconds to wait before a record is expired | | **UseLocalCache** | `false` | Whether to locally cache idempotency results (LRU cache) | | **LocalCacheMaxItems** | 256 | Max number of items to store in local cache | | **HashFunction** | `MD5` | Algorithm to use for calculating hashes, as supported by `java.security.MessageDigest` (eg. SHA-1, SHA-256, ...) |

These features are detailed below.

### Handling concurrent executions with the same payload

This utility will throw an **`IdempotencyAlreadyInProgressException`** if we receive **multiple invocations with the same payload while the first invocation hasn't completed yet**.

Info

If you receive `IdempotencyAlreadyInProgressException`, you can safely retry the operation.

This is a locking mechanism for correctness. Since we don't know the result from the first invocation yet, we can't safely allow another concurrent execution.

### Using in-memory cache

**By default, in-memory local caching is disabled**, to avoid using memory in an unpredictable way.

Warning

Be sure to configure the Lambda memory according to the number of records and the potential size of each record.

You can enable it as seen before with:

```
    IdempotencyConfig.builder()
        .withUseLocalCache(true)
        .build()

```

When enabled, we cache a maximum of 256 records in each Lambda execution environment - You can change it with the **`LocalCacheMaxItems`** parameter.

Note: This in-memory cache is local to each Lambda execution environment

This means it will be effective in cases where your function's concurrency is low in comparison to the number of "retry" invocations with the same payload, because cache might be empty.

### Expiring idempotency records

Note

By default, we expire idempotency records after **an hour** (3600 seconds).

In most cases, it is not desirable to store the idempotency records forever. Rather, you want to guarantee that the same payload won't be executed within a period of time.

You can change this window with the **`ExpirationInSeconds`** parameter:

```
IdempotencyConfig.builder()
    .withExpiration(Duration.of(5, ChronoUnit.MINUTES))
    .build()

```

Records older than 5 minutes will be marked as expired, and the Lambda handler will be executed normally even if it is invoked with a matching payload.

Note: DynamoDB time-to-live field

This utility uses **`expiration`** as the TTL field in DynamoDB, as [demonstrated in the SAM example earlier](#required-resources).

### Payload validation

Question: What if your function is invoked with the same payload except some outer parameters have changed?

Example: A payment transaction for a given productID was requested twice for the same customer, **however the amount to be paid has changed in the second transaction**.

By default, we will return the same result as it returned before, however in this instance it may be misleading; we provide a fail fast payload validation to address this edge case.

With **`PayloadValidationJMESPath`**, you can provide an additional JMESPath expression to specify which part of the event body should be validated against previous idempotent invocations

```
public App() {
  Idempotency.config()
    .withPersistenceStore(DynamoDBPersistenceStore.builder()
        .withTableName(System.getenv("TABLE_NAME"))
        .build())
    .withConfig(IdempotencyConfig.builder()
        .withEventKeyJMESPath("[userDetail, productId]")
        .withPayloadValidationJMESPath("amount")
        .build())
    .configure();
}

@Idempotent
public SubscriptionResult handleRequest(final Subscription input, final Context context) {
    // Creating a subscription payment is a side
    // effect of calling this function!
    SubscriptionPayment payment = createSubscriptionPayment(
      input.getUserDetail().getUsername(),
      input.getProductId(),
      input.getAmount()
    )
    // ...
    return new SubscriptionResult(
        "success", 200,
        payment.getId(),
        payment.getAmount()
    );
}

```

```
{
    "userDetail": {
        "username": "User1",
        "user_email": "user@example.com"
    },
    "productId": 1500,
    "charge_type": "subscription",
    "amount": 500
}

```

```
{
    "userDetail": {
        "username": "User1",
        "user_email": "user@example.com"
    },
    "productId": 1500,
    "charge_type": "subscription",
    "amount": 1
}

```

In this example, the **`userDetail`** and **`productId`** keys are used as the payload to generate the idempotency key, as per **`EventKeyJMESPath`** parameter.

Note

If we try to send the same request but with a different amount, we will raise **`IdempotencyValidationException`**.

Without payload validation, we would have returned the same result as we did for the initial request. Since we're also returning an amount in the response, this could be quite confusing for the client.

By using **`withPayloadValidationJMESPath("amount")`**, we prevent this potentially confusing behavior and instead throw an Exception.

### Making idempotency key required

If you want to enforce that an idempotency key is required, you can set **`ThrowOnNoIdempotencyKey`** to `true`.

This means that we will throw **`IdempotencyKeyException`** if the evaluation of **`EventKeyJMESPath`** is `null`.

When set to `false` (the default), if the idempotency key is null, then the data is not persisted in the store.

```
public App() {
  Idempotency.config()
    .withPersistenceStore(DynamoDBPersistenceStore.builder()
        .withTableName(System.getenv("TABLE_NAME"))
        .build())
    .withConfig(IdempotencyConfig.builder()
        // Requires "user"."uid" and "orderId" to be present
        .withEventKeyJMESPath("[user.uid, orderId]")
        .withThrowOnNoIdempotencyKey(true)
        .build())
    .configure();
}

@Idempotent
public OrderResult handleRequest(final Order input, final Context context) {
  // ...
}

```

```
{
    "user": {
        "uid": "BB0D045C-8878-40C8-889E-38B3CB0A61B1",
        "name": "Foo"
    },
    "orderId": 10000
}

```

Notice that `orderId` is now accidentally within `user` key

```
{
    "user": {
        "uid": "DE0D000E-1234-10D1-991E-EAC1DD1D52C8",
        "name": "Joe Bloggs",
        "orderId": 10000
    },
}

```

### Customizing DynamoDB configuration

When creating the `DynamoDBPersistenceStore`, you can set a custom [`DynamoDbClient`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/dynamodb/DynamoDbClient.html) if you need to customize the configuration:

```
public App() {
    DynamoDbClient customClient = DynamoDbClient.builder()
        .region(Region.US_WEST_2)
        .overrideConfiguration(ClientOverrideConfiguration.builder()
            .addExecutionInterceptor(new TracingInterceptor())
            .build()
        )
        .build();

    Idempotency.config().withPersistenceStore(
      DynamoDBPersistenceStore.builder()
            .withTableName(System.getenv("TABLE_NAME"))
            .withDynamoDbClient(customClient)
            .build()
  ).configure();
}

```

Default configuration is the following:

```
DynamoDbClient.builder()
    .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
    .httpClient(UrlConnectionHttpClient.builder().build())
    .region(Region.of(System.getenv(AWS_REGION_ENV)))
    .build();

```

### Using a DynamoDB table with a composite primary key

When using a composite primary key table (hash+range key), use `SortKeyAttr` parameter when initializing your persistence store.

With this setting, we will save the idempotency key in the sort key instead of the primary key. By default, the primary key will now be set to `idempotency#{LAMBDA_FUNCTION_NAME}`.

You can optionally set a static value for the partition key using the `StaticPkValue` parameter.

```
Idempotency.config().withPersistenceStore(
     DynamoDBPersistenceStore.builder()
       .withTableName(System.getenv("TABLE_NAME"))
       .withSortKeyAttr("sort_key")
       .build())
   .configure();

```

Data would then be stored in DynamoDB like this:

| id | sort_key | expiration | status | data | | --- | --- | --- | --- | --- | | idempotency#MyLambdaFunction | 1e956ef7da78d0cb890be999aecc0c9e | 1636549553 | COMPLETED | {"id": 12391, "message": "success"} | | idempotency#MyLambdaFunction | 2b2cdb5f86361e97b4383087c1ffdf27 | 1636549571 | COMPLETED | {"id": 527212, "message": "success"} | | idempotency#MyLambdaFunction | f091d2527ad1c78f05d54cc3f363be80 | 1636549585 | IN_PROGRESS | |

### Bring your own persistent store

This utility provides an abstract base class, so that you can implement your choice of persistent storage layer.

You can extend the `BasePersistenceStore` class and implement the abstract methods `getRecord`, `putRecord`, `updateRecord` and `deleteRecord`. You can have a look at [`DynamoDBPersistenceStore`](https://github.com/aws-powertools/powertools-lambda-java/blob/master/powertools-idempotency/src/main/java/software/amazon/lambda/powertools/idempotency/persistence/DynamoDBPersistenceStore.java) as an implementation reference.

Danger

Pay attention to the documentation for each method - you may need to perform additional checks inside these methods to ensure the idempotency guarantees remain intact.

For example, the `putRecord` method needs to throw an exception if a non-expired record already exists in the data store with a matching key.

## Compatibility with other utilities

### Validation utility

The idempotency utility can be used with the `@Validation` annotation from the [validation module](../validation/). Ensure that idempotency is the innermost annotation.

```
@Validation(inboundSchema = "classpath:/schema_in.json")
@Idempotent
public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
  // ...
}

```

Tip: JMESPath Powertools for AWS Lambda (Java) functions are also available

Built-in functions like `powertools_json`, `powertools_base64`, `powertools_base64_gzip` are also available to use in this utility. See [JMESPath Powertools for AWS Lambda (Java) functions](../serialization/)

## Testing your code

The idempotency utility provides several routes to test your code.

### Disabling the idempotency utility

When testing your code, you may wish to disable the idempotency logic altogether and focus on testing your business logic. To do this, you can set the environment variable `POWERTOOLS_IDEMPOTENCY_DISABLED` to true. If you prefer setting this for specific tests, and are using JUnit 5, you can use [junit-pioneer](https://junit-pioneer.org/docs/environment-variables/) library:

```
@Test
@SetEnvironmentVariable(key = Constants.IDEMPOTENCY_DISABLED_ENV, value = "true")
public void testIdempotencyDisabled_shouldJustRunTheFunction() {
    MyFunction func = new MyFunction();
    func.handleRequest(someInput, mockedContext);
}

```

You can also disable the idempotency for all tests using `maven-surefire-plugin` and adding the environment variable:

```
<plugin>
    <groupId>org.apache.maven.plugins</groupId>
    <artifactId>maven-surefire-plugin</artifactId>
    <configuration>
        <environmentVariables>
            <POWERTOOLS_IDEMPOTENCY_DISABLED>true</POWERTOOLS_IDEMPOTENCY_DISABLED>
        </environmentVariables>
    </configuration>
</plugin>

```

### Testing with DynamoDB Local

#### Unit tests

To unit test your function with DynamoDB Local, you can refer to this guide to [setup with Maven](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#apache-maven).

```
<dependencies>
    <!-- maven dependency for DynamoDB local -->
    <dependency>
       <groupId>com.amazonaws</groupId>
       <artifactId>DynamoDBLocal</artifactId>
       <version>[1.12,2.0)</version>
        <scope>test</scope>
    </dependency>
    <!-- Needed when building locally on M1 Mac -->
    <dependency>
        <groupId>io.github.ganadist.sqlite4java</groupId>
        <artifactId>libsqlite4java-osx-aarch64</artifactId>
        <version>1.0.392</version>
        <scope>test</scope>
        <type>dylib</type>
    </dependency>
</dependencies>
<repositories>
    <!-- custom repository to get the dependency -->
    <!-- see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBLocal.DownloadingAndRunning.html#apache-maven -->
    <repository>
       <id>dynamodb-local-oregon</id>
       <name>DynamoDB Local Release Repository</name>
       <url>https://s3-us-west-2.amazonaws.com/dynamodb-local/release</url>
    </repository>
</repositories>
<plugins>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.0.0-M5</version>
        <configuration>
            <!-- need sqlite native libs -->
            <systemPropertyVariables>
                <sqlite4java.library.path>${project.build.directory}/native-libs</sqlite4java.library.path>
            </systemPropertyVariables>
            <!-- environment variables for the tests -->
            <environmentVariables>
                <IDEMPOTENCY_TABLE_NAME>idempotency</IDEMPOTENCY_TABLE_NAME>
                <AWS_REGION>eu-central-1</AWS_REGION>
            </environmentVariables>
        </configuration>
    </plugin>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-dependency-plugin</artifactId>
        <executions>
            <execution>
                <id>copy</id>
                <phase>test-compile</phase>
                <goals>
                    <goal>copy-dependencies</goal>
                </goals>
                <configuration>
                    <includeScope>test</includeScope>
                    <includeTypes>so,dll,dylib</includeTypes>
                    <outputDirectory>${project.build.directory}/native-libs</outputDirectory>
                </configuration>
            </execution>
        </executions>
    </plugin>
</plugins>

```

```
public class AppTest {
    @Mock
    private Context context;
    private App app;
    private static DynamoDbClient client;

    @BeforeAll
    public static void setupDynamoLocal() {
        int port = getFreePort();

        // Initialize DynamoDBLocal
        try {
            DynamoDBProxyServer dynamoProxy = ServerRunner.createServerFromCommandLineArgs(new String[]{
                    "-inMemory",
                    "-port",
                    Integer.toString(port)
            });
            dynamoProxy.start();
        } catch (Exception e) {
            throw new RuntimeException();
        }

        // Initialize DynamoDBClient
        client = DynamoDbClient.builder()
                .httpClient(UrlConnectionHttpClient.builder().build())
                .region(Region.EU_WEST_1)
                .endpointOverride(URI.create("http://localhost:" + port))
                .credentialsProvider(StaticCredentialsProvider.create(
                        AwsBasicCredentials.create("FAKE", "FAKE")))
                .build();

        // create the table (use same table name as in pom.xml)
        client.createTable(CreateTableRequest.builder()
                .tableName("idempotency")
                .keySchema(KeySchemaElement.builder().keyType(KeyType.HASH).attributeName("id").build())
                .attributeDefinitions(
                        AttributeDefinition.builder().attributeName("id").attributeType(ScalarAttributeType.S).build()
                )
                .billingMode(BillingMode.PAY_PER_REQUEST)
                .build());
    }

    private static int getFreePort() {
        try {
            ServerSocket socket = new ServerSocket(0);
            int port = socket.getLocalPort();
            socket.close();
            return port;
        } catch (IOException ioe) {
            throw new RuntimeException(ioe);
        }
    }

    @BeforeEach
    void setUp() {
        MockitoAnnotations.openMocks(this);
        app = new App(client);
    }

    @Test
    public void testApp() {
        app.handleRequest(..., context);
        // ... assert
    }
}

```

```
public class App implements RequestHandler<Subscription, SubscriptionResult> {

public App(DynamoDbClient ddbClient) {
    Idempotency.config().withPersistenceStore(
            DynamoDBPersistenceStore.builder()
                    .withTableName(System.getenv("IDEMPOTENCY_TABLE_NAME"))
                    .withDynamoDbClient(ddbClient)
                    .build()
    ).configure();
}

public App() {
    this(null);
}

@Idempotent
public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    // ...
}

```

#### SAM Local

```
public class App implements RequestHandler<Subscription, SubscriptionResult> {

  public App() {
    DynamoDbClientBuilder ddbBuilder = DynamoDbClient.builder()
       .credentialsProvider(EnvironmentVariableCredentialsProvider.create())
       .httpClient(UrlConnectionHttpClient.builder().build());

    if (System.getenv("AWS_SAM_LOCAL") != null) {
      ddbBuilder.endpointOverride(URI.create("http://dynamo:8000"));
    } else {
      ddbBuilder.region(Region.of(System.getenv("AWS_REGION")));
    }

    Idempotency.config().withPersistenceStore(
       DynamoDBPersistenceStore.builder()
          .withTableName(System.getenv("IDEMPOTENCY_TABLE_NAME"))
          .withDynamoDbClient(ddbBuilder.build())
          .build()
    ).configure();
  }

  @Idempotent
  public SubscriptionResult handleRequest(final Subscription event, final Context context) {
    // ...
  }
}

```

```
# use or create a docker network 
docker network inspect sam-local || docker network create sam-local

# start dynamodb-local with docker
docker run -d --rm -p 8000:8000 \
    --network sam-local \
    --name dynamo \
    amazon/dynamodb-local

# create the idempotency table
aws dynamodb create-table 
    --table-name idempotency \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --key-schema AttributeName=id,KeyType=HASH \
    --billing-mode PAY_PER_REQUEST \
    --endpoint-url http://localhost:8000

# invoke the function locally
sam local invoke IdempotentFunction \
    --event event.json \
    --env-vars env.json \
    --docker-network sam-local

```

```
{
    "IdempotentFunction": {
        "IDEMPOTENCY_TABLE_NAME": "idempotency"
    }
}

```

## Extra resources

If you're interested in a deep dive on how Amazon uses idempotency when building our APIs, check out [this article](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/).

The large message utility handles SQS and SNS messages which have had their payloads offloaded to S3 if they are larger than the maximum allowed size (256 KB).

Notice

The large message utility (available in the `powertools-sqs` module for versions v1.16.1 and earlier) is now deprecated and replaced by the `powertools-large-messages` described in this page. You can still get the documentation [here](../sqs_large_message_handling/) and the migration guide [here](#migration-from-the-sqs-large-message-utility).

## Features

- Automatically retrieve the content of S3 objects when SQS or SNS messages have been offloaded to S3.
- Automatically delete the S3 Objects after processing succeeds.
- Compatible with the batch module (with SQS).

## Background

```
stateDiagram-v2
    direction LR
    Function : Lambda Function

    state Application {
        direction TB
        sendMsg: sendMessage(QueueUrl, MessageBody)
        extendLib: extended-client-lib
        [*] --> sendMsg
        sendMsg --> extendLib
        state extendLib {
            state if_big <<choice>>
            bigMsg: MessageBody > 256KB ?
            putObject: putObject(S3Bucket, S3Key, Body)
            updateMsg: Update MessageBody<br>with a pointer to S3<br>and add a message attribute
            bigMsg --> if_big
            if_big --> [*]: size(body) <= 256kb
            if_big --> putObject: size(body) > 256kb
            putObject --> updateMsg
            updateMsg --> [*]
        }
    }

    state Function {
        direction TB
        iterateMsgs: Iterate over messages
        ptLargeMsg: powertools-large-messages
        [*] --> Handler
        Handler --> iterateMsgs
        iterateMsgs --> ptLargeMsg
        state ptLargeMsg {
            state if_pointer <<choice>>
            pointer: Message attribute <br>for large message ?
            normalMsg: Small message,<br>body left unchanged
            getObject: getObject(S3Pointer)
            deleteObject: deleteObject(S3Pointer)
            updateBody: Update message body<br>with content from S3 object<br>and remove message attribute
            updateMD5: Update MD5 of the body<br>and attributes (SQS only)
            yourcode: <b>YOUR CODE HERE!</b>
            pointer --> if_pointer
            if_pointer --> normalMsg : False
            normalMsg --> [*]
            if_pointer --> getObject : True
            getObject --> updateBody
            updateBody --> updateMD5
            updateMD5 --> yourcode
            yourcode --> deleteObject
            deleteObject --> [*]
        }
    }

    [*] --> Application
    Application --> Function : Lambda Invocation
    Function --> [*]

```

SQS and SNS message payload is limited to 256KB. If you wish to send messages with a larger payload, you can leverage the [amazon-sqs-java-extended-client-lib](https://github.com/awslabs/amazon-sqs-java-extended-client-lib) or [amazon-sns-java-extended-client-lib](https://github.com/awslabs/amazon-sns-java-extended-client-lib) which offload the message to Amazon S3. See documentation ([SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-s3-messages.html) / [SNS](https://docs.aws.amazon.com/sns/latest/dg/large-message-payloads.html))

When offloaded to S3, the message contains a specific message attribute and the payload only contains a pointer to the S3 object (bucket and object key).

This utility automatically retrieves messages which have been offloaded to S3 using the extended client libraries. Once a message's payload has been processed successfully, the utility deletes the payload from S3.

This utility is compatible with versions *[1.1.0+](https://github.com/awslabs/amazon-sqs-java-extended-client-lib/releases/tag/1.1.0)* of amazon-sqs-java-extended-client-lib and *[1.0.0+](https://github.com/awslabs/amazon-sns-java-extended-client-lib/releases/tag/1.0.0)* of amazon-sns-java-extended-client-lib.

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-large-messages</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
            <groupId>dev.aspectj</groupId>
            <artifactId>aspectj-maven-plugin</artifactId>
            <version>1.13.1</version>
            <configuration>
                <source>11</source> <!-- or higher -->
                <target>11</target> <!-- or higher -->
                <complianceLevel>11</complianceLevel> <!-- or higher -->
                <aspectLibraries>
                    <aspectLibrary>
                        <groupId>software.amazon.lambda</groupId>
                        <artifactId>powertools-large-messages</artifactId>
                    </aspectLibrary>
                </aspectLibraries>
            </configuration>
            <executions>
                <execution>
                    <goals>
                        <goal>compile</goal>
                    </goals>
                </execution>
            </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-large-messages</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-large-messages</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-large-messages:1.20.2'
    }

    sourceCompatibility = 11 // or higher
    targetCompatibility = 11 // or higher

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-large-messages:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Permissions

As the utility interacts with Amazon S3, the lambda function must have the following permissions on the S3 bucket used for the large messages offloading:

- `s3:GetObject`
- `s3:DeleteObject`

## Annotation

The annotation `@LargeMessage` can be used on any method where the *first* parameter is one of:

- `SQSEvent.SQSMessage`
- `SNSEvent.SNSRecord`

```
import software.amazon.lambda.powertools.largemessages.LargeMessage;

public class SqsMessageHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {

    @Override
    public SQSBatchResponse handleRequest(SQSEvent event, Context context) {
        for (SQSMessage message: event.getRecords()) {
            processRawMessage(message, context);
        }
        return SQSBatchResponse.builder().build();
    }

    @LargeMessage
    private void processRawMessage(SQSEvent.SQSMessage sqsMessage, Context context) {
        // sqsMessage.getBody() will contain the content of the S3 object
    }
}

```

```
import software.amazon.lambda.powertools.largemessages.LargeMessage;

public class SnsRecordHandler implements RequestHandler<SNSEvent, String> {

    @Override
    public String handleRequest(SNSEvent event, Context context) {
        processSNSRecord(event.records.get(0)); // there are always only one message 
        return "Hello World";
    }

    @LargeMessage
    private void processSNSRecord(SNSEvent.SNSRecord snsRecord) {
        // snsRecord.getSNS().getMessage() will contain the content of the S3 object
    }
}

```

When the Lambda function is invoked with a SQS or SNS event, the utility first checks if the content was offloaded to S3. In the case of a large message, there is a message attribute specifying the size of the offloaded message and the message contains a pointer to the S3 object.

If this is the case, the utility will retrieve the object from S3 using the `getObject(bucket, key)` API, and place the content of the object in the message payload. You can then directly use the content of the message. If there was an error during the S3 download, the function will fail with a `LargeMessageProcessingException`.

After your code is invoked and returns without error, the object is deleted from S3 using the `deleteObject(bucket, key)` API. You can disable the deletion of S3 objects with the following configuration:

```
@LargeMessage(deleteS3Object = false)
private void processRawMessage(SQSEvent.SQSMessage sqsMessage) {
    // do something with the message
}

```

Use together with batch module

This utility works perfectly together with the batch module (`powertools-batch`), especially for SQS:

```
public class SqsBatchHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {
    private final BatchMessageHandler<SQSEvent, SQSBatchResponse> handler;

    public SqsBatchHandler() {
        handler = new BatchMessageHandlerBuilder()
                .withSqsBatchHandler()
                .buildWithRawMessageHandler(this::processMessage);
    }

    @Override
    public SQSBatchResponse handleRequest(SQSEvent sqsEvent, Context context) {
        return handler.processBatch(sqsEvent, context);
    }

    @LargeMessage
    private void processMessage(SQSEvent.SQSMessage sqsMessage) {
        // do something with the message
    }
}

```

Use together with idempotency module

This utility also works together with the idempotency module (`powertools-idempotency`). You can add both the `@LargeMessage` and `@Idempotent` annotations, in any order, to the same method. The `@Idempotent` takes precedence over the `@LargeMessage` annotation. It means Idempotency module will use the initial raw message (containing the S3 pointer) and not the large message.

```
public class SqsBatchHandler implements RequestHandler<SQSEvent, SQSBatchResponse> {

    public SqsBatchHandler() {
        Idempotency.config().withConfig(
                    IdempotencyConfig.builder()
                            .withEventKeyJMESPath("body") // get the body of the message for the idempotency key
                            .build())
            .withPersistenceStore(
                    DynamoDBPersistenceStore.builder()
                            .withTableName(System.getenv("IDEMPOTENCY_TABLE"))
                            .build()
            ).configure();
    }

    @Override
    public SQSBatchResponse handleRequest(SQSEvent sqsEvent, Context context) {
        for (SQSMessage message: event.getRecords()) {
            processRawMessage(message, context);
        }
        return SQSBatchResponse.builder().build();
    }

    @Idempotent
    @LargeMessage
    private String processRawMessage(@IdempotencyKey SQSEvent.SQSMessage sqsMessage, Context context) {
        // do something with the message
    }
}

```

## Customizing S3 client configuration

To interact with S3, the utility creates a default S3 Client :

```
S3Client client = S3Client.builder()
                    .httpClient(UrlConnectionHttpClient.builder().build())
                    .region(Region.of(System.getenv(AWS_REGION_ENV)))
                    .build();

```

If you need to customize this `S3Client`, you can leverage the `LargeMessageConfig` singleton:

```
import software.amazon.lambda.powertools.largemessages.LargeMessage;

public class SnsRecordHandler implements RequestHandler<SNSEvent, String> {

    public SnsRecordHandler() {
        LargeMessageConfig.init().withS3Client(/* put your custom S3Client here */);
    }

    @Override
    public String handleRequest(SNSEvent event, Context context) {
        processSNSRecord(event.records.get(0)); 
        return "Hello World";
    }

    @LargeMessage
    private void processSNSRecord(SNSEvent.SNSRecord snsRecord) {
        // snsRecord.getSNS().getMessage() will contain the content of the S3 object
    }
}

```

## Migration from the SQS Large Message utility

- Replace the dependency in maven / gradle: `powertools-sqs` ==> `powertools-large-messages`
- Replace the annotation: `@SqsLargeMessage` ==> `@LargeMessage` (the new module handles both SQS and SNS)
- Move the annotation away from the Lambda `handleRequest` method and put it on a method with `SQSEvent.SQSMessage` or `SNSEvent.SNSRecord` as first parameter.
- The annotation now handles a single message, contrary to the previous version that was handling the complete batch. It gives more control, especially when dealing with partial failures with SQS (see the batch module).
- The new module only provides an annotation, an equivalent to the `SqsUtils` class is not available anymore in this new version.

Finally, if you are still using the `powertools-sqs` library for batch processing, consider moving to `powertools-batch` at the same time to remove the dependency on this library completely; it has been deprecated and will be removed in v2.

The parameters utility provides a way to retrieve parameter values from [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), or [Amazon DynamoDB](https://aws.amazon.com/dynamodb/). It also provides a base class to create your parameter provider implementation.

**Key features**

- Retrieve one or multiple parameters from the underlying provider
- Cache parameter values for a given amount of time (defaults to 5 seconds)
- Transform parameter values from JSON or base 64 encoded strings

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-parameters</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-parameters</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-parameters</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-parameters</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-parameters:1.20.2'
    }

    sourceCompatibility = 11 // or higher
    targetCompatibility = 11 // or higher

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-parameters:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

**IAM Permissions**

This utility requires additional permissions to work as expected. See the table below:

| Provider | Function/Method | IAM Permission | | --- | --- | --- | | SSM Parameter Store | `SSMProvider.get(String)` `SSMProvider.get(String, Class)` | `ssm:GetParameter` | | SSM Parameter Store | `SSMProvider.getMultiple(String)` | `ssm:GetParametersByPath` | | Secrets Manager | `SecretsProvider.get(String)` `SecretsProvider.get(String, Class)` | `secretsmanager:GetSecretValue` | | DynamoDB | `DynamoDBProvider.get(String)` `DynamoDBProvider.getMultiple(string)` | `dynamodb:GetItem` `dynamoDB:Query` |

## SSM Parameter Store

You can retrieve a single parameter using SSMProvider.get() and pass the key of the parameter. For multiple parameters, you can use SSMProvider.getMultiple() and pass the path to retrieve them all.

Alternatively, you can retrieve an instance of a provider and configure its underlying SDK client, in order to get data from other regions or use specific credentials.

```
import software.amazon.lambda.powertools.parameters.SSMProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSSM implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the SSM Provider
    SSMProvider ssmProvider = ParamManager.getSsmProvider();

    // Retrieve a single parameter
    String value = ssmProvider.get("/my/parameter");

    // Retrieve multiple parameters from a path prefix
    // This returns a Map with the parameter name as key
    Map<String, String> values = ssmProvider.getMultiple("/my/path/prefix");

}

```

```
import software.amazon.lambda.powertools.parameters.SSMProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSSM implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    SsmClient client = SsmClient.builder().region(Region.EU_CENTRAL_1).build();
    // Get an instance of the SSM Provider
    SSMProvider ssmProvider = ParamManager.getSsmProvider(client);

    // Retrieve a single parameter
    String value = ssmProvider.get("/my/parameter");

    // Retrieve multiple parameters from a path prefix
    // This returns a Map with the parameter name as key
    Map<String, String> values = ssmProvider.getMultiple("/my/path/prefix");

}

```

### Additional arguments

The AWS Systems Manager Parameter Store provider supports two additional arguments for the `get()` and `getMultiple()` methods:

| Option | Default | Description | | --- | --- | --- | | **withDecryption()** | `False` | Will automatically decrypt the parameter. | | **recursive()** | `False` | For `getMultiple()` only, will fetch all parameter values recursively based on a path prefix. |

**Example:**

```
import software.amazon.lambda.powertools.parameters.SSMProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSSM implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the SSM Provider
    SSMProvider ssmProvider = ParamManager.getSsmProvider();

    // Retrieve a single parameter and decrypt it
    String value = ssmProvider.withDecryption().get("/my/parameter");

    // Retrieve multiple parameters recursively from a path prefix
    Map<String, String> values = ssmProvider.recursive().getMultiple("/my/path/prefix");

}

```

## Secrets Manager

For secrets stored in Secrets Manager, use `getSecretsProvider`.

Alternatively, you can retrieve an instance of a provider and configure its underlying SDK client, in order to get data from other regions or use specific credentials.

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the Secrets Provider
    SecretsProvider secretsProvider = ParamManager.getSecretsProvider();

    // Retrieve a single secret
    String value = secretsProvider.get("/my/secret");

}

```

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    SecretsManagerClient client = SecretsManagerClient.builder().region(Region.EU_CENTRAL_1).build();
    // Get an instance of the Secrets Provider
    SecretsProvider secretsProvider = ParamManager.getSecretsProvider(client);

    // Retrieve a single secret
    String value = secretsProvider.get("/my/secret");

}

```

## DynamoDB

To get secrets stored in DynamoDB, use `getDynamoDbProvider`, providing the name of the table that contains the secrets. As with the other providers, an overloaded methods allows you to retrieve a `DynamoDbProvider` providing a client if you need to configure it yourself.

```
import software.amazon.lambda.powertools.parameters.DynamoDbProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithDynamoDbParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the DynamoDbProvider
    DynamoDbProvider ddbProvider = ParamManager.getDynamoDbProvider("my-parameters-table");

    // Retrieve a single parameter
    String value = ddbProvider.get("my-key"); 
} 

```

```
import software.amazon.lambda.powertools.parameters.DynamoDbProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;
import software.amazon.awssdk.services.dynamodb.DynamoDbClient;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;

public class AppWithDynamoDbParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get a DynamoDB Client with an explicit region
    DynamoDbClient ddbClient = DynamoDbClient.builder()
            .httpClientBuilder(UrlConnectionHttpClient.builder())
            .region(Region.EU_CENTRAL_2)
            .build();

    // Get an instance of the DynamoDbProvider
    DynamoDbProvider provider = ParamManager.getDynamoDbProvider(ddbClient, "test-table");

    // Retrieve a single parameter
    String value = ddbProvider.get("my-key"); 
} 

```

## AppConfig

To get parameters stored in AppConfig, use `getAppConfigProvider`, providing the application and environment name to retrieve configuration from. As with the other providers, an overloaded method allows you to retrieve an `AppConfigProvider` providing a client if you need to configure it yourself.

```
import software.amazon.lambda.powertools.parameters.AppConfigProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWitAppConfigParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the AppConfigProvider
    AppConfigProvider appConfigProvider = ParamManager.getAppConfigProvider("my-environment", "my-app");

    // Retrieve a single parameter
    String value = appConfigProvider.get("my-key"); 
} 

```

```
import software.amazon.lambda.powertools.parameters.AppConfigProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;
import software.amazon.awssdk.services.appconfigdata.AppConfigDataClient;
import software.amazon.awssdk.http.urlconnection.UrlConnectionHttpClient;
import software.amazon.awssdk.regions.Region;

public class AppWithDynamoDbParameters implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an AppConfig Client with an explicit region
    AppConfigDataClient appConfigDataClient = AppConfigDataClient.builder()
            .httpClientBuilder(UrlConnectionHttpClient.builder())
            .region(Region.EU_CENTRAL_2)
            .build();

    // Get an instance of the DynamoDbProvider
    AppConfigProvider appConfigProvider = ParamManager.getAppConfigProvider(appConfigDataClient, "my-environment", "my-app");

    // Retrieve a single parameter
    String value = appConfigProvider.get("my-key"); 
} 

```

## Advanced configuration

### Caching

By default, all parameters and their corresponding values are cached for 5 seconds.

You can customize this default value using `defaultMaxAge`. You can also customize this value for each parameter using `withMaxAge`.

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    // Get an instance of the Secrets Provider
    SecretsProvider secretsProvider = ParamManager.getSecretsProvider()
                                                  .defaultMaxAge(10, ChronoUnit.SECONDS);

    String value = secretsProvider.get("/my/secret");

}

```

```
import software.amazon.lambda.powertools.parameters.SecretsProvider;
import software.amazon.lambda.powertools.parameters.ParamManager;

public class AppWithSecrets implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {
    SecretsManagerClient client = SecretsManagerClient.builder().region(Region.EU_CENTRAL_1).build();

    SecretsProvider secretsProvider = ParamManager.getSecretsProvider(client);

    String value = secretsProvider.withMaxAge(10, ChronoUnit.SECONDS).get("/my/secret");

}

```

### Transform values

Parameter values can be transformed using `withTransformation(transformerClass)`. Base64 and JSON transformations are provided. For more complex transformation, you need to specify how to deserialize-

`SSMProvider.getMultiple()` does not support transformation and will return simple Strings.

```
   String value = provider
                    .withTransformation(Transformer.base64)
                    .get("/my/parameter/b64");

```

```
   MyObj object = provider
                    .withTransformation(Transformer.json)
                    .get("/my/parameter/json", MyObj.class);

```

## Write your own Transformer

You can write your own transformer, by implementing the `Transformer` interface and the `applyTransformation()` method. For example, if you wish to deserialize XML into an object.

```
public class XmlTransformer<T> implements Transformer<T> {

    private final XmlMapper mapper = new XmlMapper();

    @Override
    public T applyTransformation(String value, Class<T> targetClass) throws TransformationException {
        try {
            return mapper.readValue(value, targetClass);
        } catch (IOException e) {
            throw new TransformationException(e);
        }
    }
}

```

```
    MyObj object = provider
                        .withTransformation(XmlTransformer.class)
                        .get("/my/parameter/xml", MyObj.class);

```

### Fluent API

To simplify the use of the library, you can chain all method calls before a get.

```
    ssmProvider
      .defaultMaxAge(10, SECONDS)     // will set 10 seconds as the default cache TTL
      .withMaxAge(1, MINUTES)         // will set the cache TTL for this value at 1 minute
      .withTransformation(json)       // json is a static import from Transformer.json
      .withDecryption()               // enable decryption of the parameter value
      .get("/my/param", MyObj.class); // finally get the value

```

## Create your own provider

You can create your own custom parameter store provider by inheriting the `BaseProvider` class and implementing the `String getValue(String key)` method to retrieve data from your underlying store. All transformation and caching logic is handled by the get() methods in the base class.

```
public class S3Provider extends BaseProvider {

    private final S3Client client;
    private String bucket;

    S3Provider(CacheManager cacheManager) {
        this(cacheManager, S3Client.create());
    }

    S3Provider(CacheManager cacheManager, S3Client client) {
        super(cacheManager);
        this.client = client;
    }

    public S3Provider withBucket(String bucket) {
        this.bucket = bucket;
        return this;
    }

    @Override
    protected String getValue(String key) {
        if (bucket == null) {
            throw new IllegalStateException("A bucket must be specified, using withBucket() method");
        }

        GetObjectRequest request = GetObjectRequest.builder().bucket(bucket).key(key).build();
        ResponseBytes<GetObjectResponse> response = client.getObject(request, ResponseTransformer.toBytes());
        return response.asUtf8String();
    }

    @Override
    protected Map<String, String> getMultipleValues(String path) {
        if (bucket == null) {
            throw new IllegalStateException("A bucket must be specified, using withBucket() method");
        }

        ListObjectsV2Request listRequest = ListObjectsV2Request.builder().bucket(bucket).prefix(path).build();
        List<S3Object> s3Objects = client.listObjectsV2(listRequest).contents();

        Map<String, String> result = new HashMap<>();
        s3Objects.forEach(s3Object -> {
            result.put(s3Object.key(), getValue(s3Object.key()));
        });

        return result;
    }

    @Override
    protected void resetToDefaults() {
        super.resetToDefaults();
        bucket = null;
    }

}

```

```
    S3Provider provider = new S3Provider(ParamManager.getCacheManager());

    provider.setTransformationManager(ParamManager.getTransformationManager());

    String value = provider.withBucket("myBucket").get("myKey");

```

## Annotation

You can make use of the annotation `@Param` to inject a parameter value in a variable.

By default, it will use `SSMProvider` to retrieve the value from AWS System Manager Parameter Store. You could specify a different provider as long as it extends `BaseProvider` and/or a `Transformer`.

```
public class AppWithAnnotation implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Param(key = "/my/parameter/json")
    ObjectToDeserialize value;

}

```

```
public class AppWithAnnotation implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Param(key = "/my/parameter/json" provider = SecretsProvider.class, transformer = JsonTransformer.class)
    ObjectToDeserialize value;

}

```

In this case `SecretsProvider` will be used to retrieve a raw value that is then transformed into the target Object by using `JsonTransformer`. To show the convenience of the annotation compare the following two code snippets.

### Install

If you want to use the `@Param` annotation in your project add configuration to compile-time weave (CTW) the powertools-parameters aspects into your project.

```
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 ...
                 <aspectLibraries>
                     ...
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-parameters</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
plugins{
    id 'java'
    id 'io.freefair.aspectj.post-compile-weaving' version '6.3.0'
}

repositories {
    mavenCentral()
}

dependencies {
    ...
    aspect 'software.amazon.lambda:powertools-parameters:1.20.2'
    implementation 'org.aspectj:aspectjrt:1.9.19'
}

```

This module contains a set of utilities you may use in your Lambda functions, to manipulate JSON.

## Easy deserialization

### Key features

- Easily deserialize the main content of an event (for example, the body of an API Gateway event)
- 15+ built-in events (see the [list below](#built-in-events))

### Getting started

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-serialization</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>

```

```
implementation 'software.amazon.lambda:powertools-serialization:1.20.2'

```

### EventDeserializer

The `EventDeserializer` can be used to extract the main part of an event (body, message, records) and deserialize it from JSON to your desired type.

It can handle single elements like the body of an API Gateway event:

```
import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;

public class APIGWHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    public APIGatewayProxyResponseEvent handleRequest(
            final APIGatewayProxyRequestEvent event, 
            final Context context) {

        Product product = extractDataFrom(event).as(Product.class);

    }

```

```
public class Product {
    private long id;
    private String name;
    private double price;

    public Product() {
    }

    public Product(long id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public long getId() {
        return id;
    }

    public void setId(long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

```

```
{
    "body": "{\"id\":1234, \"name\":\"product\", \"price\":42}",
    "resource": "/{proxy+}",
    "path": "/path/to/resource",
    "httpMethod": "POST",
    "isBase64Encoded": false,
    "queryStringParameters": {
        "foo": "bar"
    },
    "pathParameters": {
        "proxy": "/path/to/resource"
    },
    "stageVariables": {
        "baz": "qux"
    },
    "headers": {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "en-US,en;q=0.8",
        "Cache-Control": "max-age=0",
        "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Custom User Agent String",
        "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
        "X-Amz-Cf-Id": "cDehVQoZnx43VYQb9j2-nvCh-9z396Uhbp027Y2JvkCPNLmGJHqlaA==",
        "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
        "X-Forwarded-Port": "443",
        "X-Forwarded-Proto": "https"
    },
    "requestContext": {
        "accountId": "123456789012",
        "resourceId": "123456",
        "stage": "prod",
        "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
        "requestTime": "09/Apr/2015:12:34:56 +0000",
        "requestTimeEpoch": 1428582896000,
        "identity": {
        "cognitoIdentityPoolId": null,
        "accountId": null,
        "cognitoIdentityId": null,
        "caller": null,
        "accessKey": null,
        "sourceIp": "127.0.0.1",
        "cognitoAuthenticationType": null,
        "cognitoAuthenticationProvider": null,
        "userArn": null,
        "userAgent": "Custom User Agent String",
        "user": null
    },
    "path": "/prod/path/to/resource",
    "resourcePath": "/{proxy+}",
    "httpMethod": "POST",
    "apiId": "1234567890",
    "protocol": "HTTP/1.1"
    }
}

```

It can also handle a collection of elements like the records of an SQS event:

```
import static software.amazon.lambda.powertools.utilities.EventDeserializer.extractDataFrom;

public class SQSHandler implements RequestHandler<SQSEvent, String> {

    public String handleRequest(
            final SQSEvent event, 
            final Context context) {

        List<Product> products = extractDataFrom(event).asListOf(Product.class);

    }

```

```
{
    "Records": [
      {
        "messageId": "d9144555-9a4f-4ec3-99a0-34ce359b4b54",
        "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
        "body": "{  \"id\": 1234,  \"name\": \"product\",  \"price\": 42}",
        "attributes": {
            "ApproximateReceiveCount": "1",
            "SentTimestamp": "1601975706495",
            "SenderId": "AROAIFU437PVZ5L2J53F5",
            "ApproximateFirstReceiveTimestamp": "1601975706499"
        },
        "messageAttributes": {
        },
        "md5OfBody": "13e7f7851d2eaa5c01f208ebadbf1e72",
        "eventSource": "aws:sqs",
        "eventSourceARN": "arn:aws:sqs:eu-central-1:123456789012:TestLambda",
        "awsRegion": "eu-central-1"
      },
      {
        "messageId": "d9144555-9a4f-4ec3-99a0-34ce359b4b54",
        "receiptHandle": "13e7f7851d2eaa5c01f208ebadbf1e72==",
        "body": "{  \"id\": 12345,  \"name\": \"product5\",  \"price\": 45}",
        "attributes": {
          "ApproximateReceiveCount": "1",
          "SentTimestamp": "1601975706495",
          "SenderId": "AROAIFU437PVZ5L2J53F5",
          "ApproximateFirstReceiveTimestamp": "1601975706499"
        },
        "messageAttributes": {

        },
        "md5OfBody": "13e7f7851d2eaa5c01f208ebadbf1e72",
        "eventSource": "aws:sqs",
        "eventSourceARN": "arn:aws:sqs:eu-central-1:123456789012:TestLambda",
        "awsRegion": "eu-central-1"
      }
    ]
}

```

Tip

In the background, `EventDeserializer` is using Jackson. The `ObjectMapper` is configured in `JsonConfig`. You can customize the configuration of the mapper if needed: `JsonConfig.get().getObjectMapper()`. Using this feature, you don't need to add Jackson to your project and create another instance of `ObjectMapper`.

### Built-in events

| Event Type | Path to the content | List | | --- | --- | --- | | `APIGatewayProxyRequestEvent` | `body` | | | `APIGatewayV2HTTPEvent` | `body` | | | `SNSEvent` | `Records[0].Sns.Message` | | | `SQSEvent` | `Records[*].body` | x | | `ScheduledEvent` | `detail` | | | `ApplicationLoadBalancerRequestEvent` | `body` | | | `CloudWatchLogsEvent` | `powertools_base64_gzip(data)` | | | `CloudFormationCustomResourceEvent` | `resourceProperties` | | | `KinesisEvent` | `Records[*].kinesis.powertools_base64(data)` | x | | `KinesisFirehoseEvent` | `Records[*].powertools_base64(data)` | x | | `KafkaEvent` | `records[*].values[*].powertools_base64(value)` | x | | `ActiveMQEvent` | `messages[*].powertools_base64(data)` | x | | `RabbitMQEvent` | `rmqMessagesByQueue[*].values[*].powertools_base64(data)` | x | | `KinesisAnalyticsFirehoseInputPreprocessingEvent` | `Records[*].kinesis.powertools_base64(data)` | x | | `KinesisAnalyticsStreamsInputPreprocessingEvent` | `Records[*].kinesis.powertools_base64(data)` | x |

## JMESPath functions

Tip

[JMESPath](https://jmespath.org/) is a query language for JSON used by AWS CLI and Powertools for AWS Lambda (Java) to get a specific part of a json.

### Key features

- Deserialize JSON from JSON strings, base64, and compressed data
- Use JMESPath to extract and combine data recursively

### Getting started

You might have events that contain encoded JSON payloads as string, base64, or even in compressed format. It is a common use case to decode and extract them partially or fully as part of your Lambda function invocation.

You will generally use this in combination with other Powertools for AWS Lambda (Java) modules ([validation](../validation/) and [idempotency](../idempotency/)) where you might need to extract a portion of your data before using them.

### Built-in functions

Powertools for AWS Lambda (Java) provides the following JMESPath Functions to easily deserialize common encoded JSON payloads in Lambda functions:

#### powertools_json function

Use `powertools_json` function to decode any JSON string anywhere a JMESPath expression is allowed.

Below example use this function to load the content from the body of an API Gateway request event as a JSON object and retrieve the id field in it:

```
public class MyHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

  public MyHandler() {
    Idempotency.config()
    .withConfig(
        IdempotencyConfig.builder()
          .withEventKeyJMESPath("powertools_json(body).id")
          .build())
    .withPersistenceStore(
        DynamoDBPersistenceStore.builder()
          .withTableName(System.getenv("TABLE_NAME"))
          .build())
    .configure();
}

@Idempotent
public APIGatewayProxyResponseEvent handleRequest(final APIGatewayProxyRequestEvent event, final Context context) {
}

```

```
{
  "body": "{\"message\": \"Lambda rocks\", \"id\": 43876123454654}",
  "resource": "/{proxy+}",
  "path": "/path/to/resource",
  "httpMethod": "POST",
  "queryStringParameters": {
    "foo": "bar"
  },
  "headers": {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "en-US,en;q=0.8",
    "Cache-Control": "max-age=0",
  },
  "requestContext": {
    "accountId": "123456789012",
    "resourceId": "123456",
    "stage": "prod",
    "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
    "requestTime": "09/Apr/2015:12:34:56 +0000",
    "requestTimeEpoch": 1428582896000,
    "identity": {
      "cognitoIdentityPoolId": null,
      "accountId": null,
      "cognitoIdentityId": null,
      "caller": null,
      "accessKey": null,
      "sourceIp": "127.0.0.1",
      "cognitoAuthenticationType": null,
      "cognitoAuthenticationProvider": null,
      "userArn": null,
      "userAgent": "Custom User Agent String",
      "user": null
    },
    "path": "/prod/path/to/resource",
    "resourcePath": "/{proxy+}",
    "httpMethod": "POST",
    "apiId": "1234567890",
    "protocol": "HTTP/1.1"
  }
}

```

#### powertools_base64 function

Use `powertools_base64` function to decode any base64 data.

Below sample will decode the base64 value within the `data` key, and decode the JSON string into a valid JSON before we can validate it.

```
import software.amazon.lambda.powertools.validation.ValidationUtils;

public class MyEventHandler implements RequestHandler<MyEvent, String> {

    @Override
    public String handleRequest(MyEvent myEvent, Context context) {
        validate(myEvent, "classpath:/schema.json", "powertools_base64(data)");
        return "OK";
   }
}

```

```
{
"data" : "ewogICJpZCI6IDQzMjQyLAogICJuYW1lIjogIkZvb0JhciBYWSIsCiAgInByaWNlIjogMjU4Cn0="
}

```

#### powertools_base64_gzip function

Use `powertools_base64_gzip` function to decompress and decode base64 data.

Below sample will decompress and decode base64 data.

```
import software.amazon.lambda.powertools.validation.ValidationUtils;

public class MyEventHandler implements RequestHandler<MyEvent, String> {

    @Override
    public String handleRequest(MyEvent myEvent, Context context) {
        validate(myEvent, "classpath:/schema.json", "powertools_base64_gzip(data)");
        return "OK";
   }
}

```

```
{
   "data" : "H4sIAAAAAAAA/6vmUlBQykxRslIwMTYyMdIBcfMSc1OBAkpu+flOiUUKEZFKYOGCosxkkLiRqQVXLQDnWo6bOAAAAA=="
}

```

### Bring your own JMESPath function

Warning

This should only be used for advanced use cases where you have special formats not covered by the built-in functions. Please open an issue in Github if you need us to add some common functions.

Your function must extend `io.burt.jmespath.function.BaseFunction`, take a String as parameter and return a String. You can read the [doc](https://github.com/burtcorp/jmespath-java#adding-custom-functions) for more information.

Below is an example that takes some xml and transform it into json. Once your function is created, you need to add it to powertools.You can then use it to do your validation or in idempotency module.

```
public class XMLFunction extends BaseFunction {
    public Base64Function() {
        super("powertools_xml", ArgumentConstraints.typeOf(JmesPathType.STRING));
    }

    @Override
    protected <T> T callFunction(Adapter<T> runtime, List<FunctionArgument<T>> arguments) {
        T value = arguments.get(0).value();
        String xmlString = runtime.toString(value);

        String jsonString =  // ... transform xmlString to json

        return runtime.createString(jsonString);
    }
}

```

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.ValidationUtils.validate;

static {
    JsonConfig.get().addFunction(new XMLFunction());
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        validate(myEvent, "classpath:/schema.json", "powertools_xml(path.to.xml_data)");
        return "OK";
   }
}

```

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.Validation;

static {
    JsonConfig.get().addFunction(new XMLFunction());
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    @Validation(inboundSchema="classpath:/schema.json", envelope="powertools_xml(path.to.xml_data)")
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        return "OK";
   }
}

```

This utility provides JSON Schema validation for payloads held within events and response used in AWS Lambda.

**Key features**

- Validate incoming events and responses
- Built-in validation for most common events (API Gateway, SNS, SQS, ...)
- JMESPath support validate only a sub part of the event

## Install

Depending on your version of Java (either Java 1.8 or 11+), the configuration slightly changes.

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-validation</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>dev.aspectj</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.13.1</version>
             <configuration>
                 <source>11</source> <!-- or higher -->
                 <target>11</target> <!-- or higher -->
                 <complianceLevel>11</complianceLevel> <!-- or higher -->
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-validation</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
<dependencies>
    ...
    <dependency>
        <groupId>software.amazon.lambda</groupId>
        <artifactId>powertools-validation</artifactId>
        <version>1.20.2</version>
    </dependency>
    ...
</dependencies>
...
<!-- configure the aspectj-maven-plugin to compile-time weave (CTW) the aws-lambda-powertools-java aspects into your project -->
<build>
    <plugins>
        ...
        <plugin>
             <groupId>org.codehaus.mojo</groupId>
             <artifactId>aspectj-maven-plugin</artifactId>
             <version>1.14.0</version>
             <configuration>
                 <source>1.8</source>
                 <target>1.8</target>
                 <complianceLevel>1.8</complianceLevel>
                 <aspectLibraries>
                     <aspectLibrary>
                         <groupId>software.amazon.lambda</groupId>
                         <artifactId>powertools-validation</artifactId>
                     </aspectLibrary>
                 </aspectLibraries>
             </configuration>
             <executions>
                 <execution>
                     <goals>
                         <goal>compile</goal>
                     </goals>
                 </execution>
             </executions>
        </plugin>
        ...
    </plugins>
</build>

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '8.1.0'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-validation:1.20.2'
    }

    sourceCompatibility = 11 // or higher
    targetCompatibility = 11 // or higher

```

```
    plugins {
        id 'java'
        id 'io.freefair.aspectj.post-compile-weaving' version '6.6.3'
    }

    repositories {
        mavenCentral()
    }

    dependencies {
        aspect 'software.amazon.lambda:powertools-validation:1.20.2'
    }

    sourceCompatibility = 1.8
    targetCompatibility = 1.8

```

## Validating events

You can validate inbound and outbound events using `@Validation` annotation.

You can also use the `Validator#validate()` methods, if you want more control over the validation process such as handling a validation error.

We support JSON schema version 4, 6, 7 and 201909 (from [jmespath-jackson library](https://github.com/burtcorp/jmespath-java)).

### Validation annotation

`@Validation` annotation is used to validate either inbound events or functions' response.

It will fail fast with `ValidationException` if an event or response doesn't conform with given JSON Schema.

While it is easier to specify a json schema file in the classpath (using the notation `"classpath:/path/to/schema.json"`), you can also provide a JSON String containing the schema.

```
import software.amazon.lambda.powertools.validation.Validation;

public class MyFunctionHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Override
    @Validation(inboundSchema = "classpath:/schema_in.json", outboundSchema = "classpath:/schema_out.json")
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        // ...
        return something;
    }
}

```

Note

It is not a requirement to validate both inbound and outbound schemas - You can either use one, or both.

### Validate function

Validate standalone function is used within the Lambda handler, or any other methods that perform data validation.

You can also gracefully handle schema validation errors by catching `ValidationException`.

```
import static software.amazon.lambda.powertools.validation.ValidationUtils.*;

public class MyFunctionHandler implements RequestHandler<APIGatewayProxyRequestEvent, APIGatewayProxyResponseEvent> {

    @Override
    public APIGatewayProxyResponseEvent handleRequest(APIGatewayProxyRequestEvent input, Context context) {
        try {
            validate(input, "classpath:/schema.json");
        } catch (ValidationException ex) {
            // do something before throwing it
            throw ex;
        }

        // ...
        return something;
    }
}

```

Note

Schemas are stored in memory for re-use, to avoid loading them from file each time.

## Built-in events and responses

For the following events and responses, the Validator will automatically perform validation on the content.

**Events**

| Type of event | Class | Path to content | | --- | --- | --- | | API Gateway REST | APIGatewayProxyRequestEvent | `body` | | API Gateway HTTP | APIGatewayV2HTTPEvent | `body` | | Application Load Balancer | ApplicationLoadBalancerRequestEvent | `body` | | Cloudformation Custom Resource | CloudFormationCustomResourceEvent | `resourceProperties` | | CloudWatch Logs | CloudWatchLogsEvent | `awslogs.powertools_base64_gzip(data)` | | EventBridge / Cloudwatch | ScheduledEvent | `detail` | | Kafka | KafkaEvent | `records[*][*].value` | | Kinesis | KinesisEvent | `Records[*].kinesis.powertools_base64(data)` | | Kinesis Firehose | KinesisFirehoseEvent | `Records[*].powertools_base64(data)` | | Kinesis Analytics from Firehose | KinesisAnalyticsFirehoseInputPreprocessingEvent | `Records[*].powertools_base64(data)` | | Kinesis Analytics from Streams | KinesisAnalyticsStreamsInputPreprocessingEvent | `Records[*].powertools_base64(data)` | | SNS | SNSEvent | `Records[*].Sns.Message` | | SQS | SQSEvent | `Records[*].body` |

**Responses**

| Type of response | Class | Path to content (envelope) | | --- | --- | --- | | API Gateway REST | APIGatewayProxyResponseEvent} | `body` | | API Gateway HTTP | APIGatewayV2HTTPResponse} | `body` | | API Gateway WebSocket | APIGatewayV2WebSocketResponse} | `body` | | Load Balancer | ApplicationLoadBalancerResponseEvent} | `body` | | Kinesis Analytics | KinesisAnalyticsInputPreprocessingResponse} | \`Records[\*].powertools_base64(data)\`\` |

## Custom events and responses

You can also validate any Event or Response type, once you have the appropriate schema.

Sometimes, you might want to validate only a portion of it - This is where the envelope parameter is for.

Envelopes are [JMESPath expressions](https://jmespath.org/tutorial.html) to extract a portion of JSON you want before applying JSON Schema validation.

```
import software.amazon.lambda.powertools.validation.Validation;

public class MyCustomEventHandler implements RequestHandler<MyCustomEvent, String> {

    @Override
    @Validation(inboundSchema = "classpath:/my_custom_event_schema.json",
                envelope = "basket.products[*]")
    public String handleRequest(MyCustomEvent input, Context context) {
        return "OK";
    }
}

```

```
{
  "basket": {
    "products" : [
      {
        "id": 43242,
        "name": "FooBar XY",
        "price": 258
      },
      {
        "id": 765,
        "name": "BarBaz AB",
        "price": 43.99
      }
    ]
  }
}

```

This is quite powerful because you can use JMESPath Query language to extract records from [arrays, slice and dice](https://jmespath.org/tutorial.html#list-and-slice-projections), to [pipe expressions](https://jmespath.org/tutorial.html#pipe-expressions) and [function](https://jmespath.org/tutorial.html#functions) expressions, where you'd extract what you need before validating the actual payload.

## Change the schema version

By default, powertools-validation is configured with [V7](https://json-schema.org/draft-07/json-schema-release-notes.html). You can use the `ValidationConfig` to change that behaviour.

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.Validation;

static {
    ValidationConfig.get().setSchemaVersion(SpecVersion.VersionFlag.V4);
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    @Validation(inboundSchema="classpath:/schema.json", envelope="powertools_xml(path.to.xml_data)")
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        return "OK";
   }
}

```

## Advanced ObjectMapper settings

If you need to configure the Jackson ObjectMapper, you can use the `ValidationConfig`:

```
...
import software.amazon.lambda.powertools.validation.ValidationConfig;
import software.amazon.lambda.powertools.validation.Validation;

static {
    ObjectMapper objectMapper= ValidationConfig.get().getObjectMapper();
    // update (de)serializationConfig or other properties
}

public class MyXMLEventHandler implements RequestHandler<MyEventWithXML, String> {

    @Override
    @Validation(inboundSchema="classpath:/schema.json", envelope="powertools_xml(path.to.xml_data)")
    public String handleRequest(MyEventWithXML myEvent, Context context) {
        return "OK";
   }
}

```
# Processes

## Overview

Please treat this content as a living document.

This is document explains who the maintainers are, their responsibilities, and how they should be doing it. If you're interested in contributing, see [CONTRIBUTING](https://github.com/aws-powertools/powertools-lambda-java/blob/main/CONTRIBUTING.md).

## Current Maintainers

| Maintainer | GitHub ID | Affiliation | | --- | --- | --- | | Jerome Van Der Linden | [jeromevdl](https://github.com/jeromevdl) | Amazon | | Michele Ricciardi | [mriccia](https://github.com/mriccia) | Amazon | | Scott Gerring | [scottgerring](https://github.com/scottgerring) | Amazon |

## Emeritus

Previous active maintainers who contributed to this project.

| Maintainer | GitHub ID | Affiliation | | --- | --- | --- | | Mark Sailes | [msailes](https://github.com/msailes) | Amazon | | Pankaj Agrawal | [pankajagrawal16](https://github.com/pankajagrawal16) | Former Amazon | | Steve Houel | [stevehouel](https://github.com/stevehouel) | Amazon |

## Labels

These are the most common labels used by maintainers to triage issues, pull requests (PR), and for project management:

| Label | Usage | Notes | | --- | --- | --- | | triage | New issues that require maintainers review | Issue template | | bug | Unexpected, reproducible and unintended software behavior | PR/Release automation; Doc snippets are excluded; | | documentation | Documentation improvements | PR/Release automation; Doc additions, fixes, etc.; | | duplicate | Dupe of another issue | | | enhancement | New or enhancements to existing features | Issue template | | RFC | Technical design documents related to a feature request | Issue template | | help wanted | Tasks you want help from anyone to move forward | Bandwidth, complex topics, etc. | | feature-parity | Adding features present in other Powertools for Lambda libraries | | | good first issue | Somewhere for new contributors to start | | | governance | Issues related to project governance - contributor guides, automation, etc. | | | question | Issues that are raised to ask questions | | | maven | Related to the build system | | | need-more-information | Missing information before making any calls | | | status/staged-next-release | Changes are merged and will be available once the next release is made. | | | status/staged-next-major-release | Contains breaking changes - merged changes will be available once the next major release is made. | | | blocked | Issues or PRs that are blocked for varying reasons | Timeline is uncertain | | priority:1 | Critical - needs urgent attention | | | priority:2 | High - core feature, or affects 60%+ of users | | | priority:3 | Neutral - not a core feature, or affects < 40% of users | | | priority:4 | Low - nice to have | | | priority:5 | Low - idea for later | | | invalid | This doesn't seem right | | | size/XS | PRs between 0-9 LOC | PR automation | | size/S | PRs between 10-29 LOC | PR automation | | size/M | PRs between 30-99 LOC | PR automation | | size/L | PRs between 100-499 LOC | PR automation | | size/XL | PRs between 500-999 LOC, often PRs that grown with feedback | PR automation | | size/XXL | PRs with 1K+ LOC, largely documentation related | PR automation | | dependencies | Changes that touch dependencies, e.g. Dependabot, etc. | PR/ automation | | maintenance | Address outstanding tech debt | |

## Maintainer Responsibilities

Maintainers are active and visible members of the community, and have [maintain-level permissions on a repository](https://docs.github.com/en/organizations/managing-access-to-your-organizations-repositories/repository-permission-levels-for-an-organization). Use those privileges to serve the community and evolve code as follows.

Be aware of recurring ambiguous situations and [document them](#common-scenarios) to help your fellow maintainers.

### Uphold Code of Conduct

Model the behavior set forward by the [Code of Conduct](https://github.com/aws-powertools/powertools-lambda-java/blob/main/CODE_OF_CONDUCT.md) and raise any violations to other maintainers and admins. There could be unusual circumstances where inappropriate behavior does not immediately fall within the [Code of Conduct](https://github.com/aws-powertools/powertools-lambda-java/blob/main/CODE_OF_CONDUCT.md).

These might be nuanced and should be handled with extra care - when in doubt, do not engage and reach out to other maintainers and admins.

### Prioritize Security

Security is your number one priority. Maintainer's Github keys must be password protected securely and any reported security vulnerabilities are addressed before features or bugs.

Note that this repository is monitored and supported 24/7 by Amazon Security, see [Security disclosures](https://github.com/aws-powertools/powertools-lambda-java/) for details.

### Review Pull Requests

Review pull requests regularly, comment, suggest, reject, merge and close. Accept only high quality pull-requests. Provide code reviews and guidance on incoming pull requests.

PRs are [labeled](#labels) based on file changes and semantic title. Pay attention to whether labels reflect the current state of the PR and correct accordingly.

Use and enforce [semantic versioning](https://semver.org/) pull request titles, as these will be used for [CHANGELOG](https://github.com/aws-powertools/powertools-lambda-java/blob/main/CHANGELOG.md) and [Release notes](https://github.com/aws-powertools/powertools-lambda-java/releases) - make sure they communicate their intent at the human level.

For issues linked to a PR, make sure `status/staged-next-release` label is applied to them when merging. [Upon release](#releasing-a-new-version), these issues will be notified which release version contains their change.

See [Common scenarios](#common-scenarios) section for additional guidance.

### Triage New Issues

Manage [labels](#labels), review issues regularly, and create new labels as needed by the project. Remove `triage` label when you're able to confirm the validity of a request, a bug can be reproduced, etc. Give priority to the original author for implementation, unless it is a sensitive task that is best handled by maintainers.

Make sure issues are assigned to our [board of activities](https://github.com/orgs/aws-powertools/projects/4).

Use our [labels](#labels) to signal good first issues to new community members, and to set expectation that this might need additional feedback from the author, other customers, experienced community members and/or maintainers.

Be aware of [casual contributors](https://opensource.com/article/17/10/managing-casual-contributors) and recurring contributors. Provide the experience and attention you wish you had if you were starting in open source.

See [Common scenarios](#common-scenarios) section for additional guidance.

### Triage Bug Reports

Be familiar with [our definition of bug](#is-that-a-bug). If it's not a bug, you can close it or adjust its title and labels - always communicate the reason accordingly.

For bugs caused by upstream dependencies, replace `bug` with `bug-upstream` label. Ask the author whether they'd like to raise the issue upstream or if they prefer us to do so.

Assess the impact and make the call on whether we need an emergency release. Contact other [maintainers](#current-maintainers) when in doubt.

See [Common scenarios](#common-scenarios) section for additional guidance.

### Triage RFCs

RFC is a collaborative process to help us get to the most optimal solution given the context. Their purpose is to ensure everyone understands what this context is, their trade-offs, and alternative solutions that were part of the research before implementation begins.

Make sure you ask these questions in mind when reviewing:

- Does it use our [RFC template](https://github.com/aws-powertools/powertools-lambda-java/issues/new?assignees=&labels=RFC%2C+triage&projects=&template=rfc.md&title=RFC%3A+)?
- Does it match our [Tenets](https://docs.aws.amazon.com/powertools/java/latest/#tenets)?
- Does the proposal address the use case? If so, is the recommended usage explicit?
- Does it focus on the mechanics to solve the use case over fine-grained implementation details?
- Can anyone familiar with the code base implement it?
- If approved, are they interested in contributing? Do they need any guidance?
- Does this significantly increase the overall project maintenance? Do we have the skills to maintain it?
- If we can't take this use case, are there alternative projects we could recommend? Or does it call for a new project altogether?

When necessary, be upfront that the time to review, approve, and implement a RFC can vary - see [Contribution is stuck](#contribution-is-stuck). Some RFCs may be further updated after implementation, as certain areas become clearer.

Some examples using our initial and new RFC templates: #92, #94, #95, #991, #1226

### Releasing a new version

The release process is currently a long, multi-step process. The team is in the process of automating at it.

Firstly, make sure the commit history in the `main` branch **(1)** it's up to date, **(2)** commit messages are semantic, and **(3)** commit messages have their respective area, for example `feat: <change>`, `chore: ...`).

**Looks good, what's next?**

Kickoff the `Prepare for maven central release` workflow with the intended rekease version. Once this has completed, it will draft a Pull Request named something like `chore: Prep release 1.19.0`. the PR will **(1)** roll all of the POM versions forward to the new release version and **(2)** release notes.

Once this is done, check out the branch and clean up the release notes. These will be used both in the [CHANGELOG.md file](https://github.com/aws-powertools/powertools-lambda-java/blob/main/CHANGELOG.md) file and the [published github release information](https://github.com/aws-powertools/powertools-lambda-java/releases), and you can use the existing release notes to see how changes are summarized.

Next, commit and push, wait for the build to complete, and merge to main. Once main has built successfully (i.e. build, tests and end-to-end tests should pass), create a tagged release from the Github UI, using the same release notes.

Next, run the `Publish package to the Maven Central Repository` action to release the library.

Finally, by hand, create a PR rolling all of the POMs onto the next snapshot version (e.g. `1.20.0-SNAPSHOT`).

### Add Continuous Integration Checks

Add integration checks that validate pull requests and pushes to ease the burden on Pull Request reviewers. Continuously revisit areas of improvement to reduce operational burden in all parties involved.

### Negative Impact on the Project

Actions that negatively impact the project will be handled by the admins, in coordination with other maintainers, in balance with the urgency of the issue. Examples would be [Code of Conduct](https://github.com/aws-powertools/powertools-lambda-java/blob/main/CODE_OF_CONDUCT.md) violations, deliberate harmful or malicious actions, spam, monopolization, and security risks.

## Common scenarios

These are recurring ambiguous situations that new and existing maintainers may encounter. They serve as guidance. It is up to each maintainer to follow, adjust, or handle in a different manner as long as [our conduct is consistent](#uphold-code-of-conduct)

### Contribution is stuck

A contribution can get stuck often due to lack of bandwidth and language barrier. For bandwidth issues, check whether the author needs help. Make sure you get their permission before pushing code into their existing PR - do not create a new PR unless strictly necessary.

For language barrier and others, offer a 1:1 chat to get them unblocked. Often times, English might not be their primary language, and writing in public might put them off, or come across not the way they intended to be.

In other cases, you may have constrained capacity. Use `help wanted` label when you want to signal other maintainers and external contributors that you could use a hand to move it forward.

### Insufficient feedback or information

When in doubt, use the `need-more-information` label to signal more context and feedback are necessary before proceeding.

### Crediting contributions

We credit all contributions as part of each [release note](https://github.com/aws-powertools/powertools-lambda-java/releases) as an automated process. If you find contributors are missing from the release note you're producing, please add them manually.

### Is that a bug?

A bug produces incorrect or unexpected results at runtime that differ from its intended behavior. Bugs must be reproducible. They directly affect customers experience at runtime despite following its recommended usage.

Documentation snippets, use of internal components, or unadvertised functionalities are not considered bugs.

### Mentoring contributions

Always favor mentoring issue authors to contribute, unless they're not interested or the implementation is sensitive (*e.g., complexity, time to release, etc.*).

Make use of `help wanted` and `good first issue` to signal additional contributions the community can help.

### Long running issues or PRs

Try offering a 1:1 call in the attempt to get to a mutual understanding and clarify areas that maintainers could help.

In the rare cases where both parties don't have the bandwidth or expertise to continue, it's best to use the `revisit-in-3-months` label. By then, see if it's possible to break the PR or issue in smaller chunks, and eventually close if there is no progress.

### Overview

This document outlines the maintenance policy for Powertools for AWS Lambda and their underlying dependencies. AWS regularly provides Powertools for AWS Lambda with updates that may contain new features, enhancements, bug fixes, security patches, or documentation updates. Updates may also address changes with dependencies, language runtimes, and operating systems. Powertools for AWS Lambda is published to package managers (e.g. PyPi, NPM, Maven, NuGet), and are available as source code on GitHub.

We recommend users to stay up-to-date with Powertools for AWS Lambda releases to keep up with the latest features, security updates, and underlying dependencies. Continued use of an unsupported Powertools for AWS Lambda version is not recommended and is done at the userâs discretion.

For brevity, we will interchangeably refer to Powertools for AWS Lambda as "SDK" *(Software Development Toolkit)*.

### Versioning

Powertools for AWS Lambda release versions are in the form of X.Y.Z where X represents the major version. Increasing the major version of an SDK indicates that this SDK underwent significant and substantial changes to support new idioms and patterns in the language. Major versions are introduced when public interfaces *(e.g. classes, methods, types, etc.)*, behaviors, or semantics have changed. Applications need to be updated in order for them to work with the newest SDK version. It is important to update major versions carefully and in accordance with the upgrade guidelines provided by AWS.

### SDK major version lifecycle

The lifecycle for major Powertools for AWS Lambda versions consists of 5 phases, which are outlined below.

- **Developer Preview** (Phase 0) - During this phase, SDKs are not supported, should not be used in production environments, and are meant for early access and feedback purposes only. It is possible for future releases to introduce breaking changes. Once AWS identifies a release to be a stable product, it may mark it as a Release Candidate. Release Candidates are ready for GA release unless significant bugs emerge, and will receive full AWS support.
- **General Availability (GA)** (Phase 1) - During this phase, SDKs are fully supported. AWS will provide regular SDK releases that include support for new features, enhancements, as well as bug and security fixes. AWS will support the GA version of an SDK for *at least 24 months*, unless otherwise specified.
- **Maintenance Announcement** (Phase 2) - AWS will make a public announcement at least 6 months before an SDK enters maintenance mode. During this period, the SDK will continue to be fully supported. Typically, maintenance mode is announced at the same time as the next major version is transitioned to GA.
- **Maintenance** (Phase 3) - During the maintenance mode, AWS limits SDK releases to address critical bug fixes and security issues only. An SDK will not receive API updates for new or existing services, or be updated to support new regions. Maintenance mode has a *default duration of 6 months*, unless otherwise specified.
- **End-of-Support** (Phase 4) - When an SDK reaches end-of support, it will no longer receive updates or releases. Previously published releases will continue to be available via public package managers and the code will remain on GitHub. The GitHub repository may be archived. Use of an SDK which has reached end-of-support is done at the userâs discretion. We recommend users upgrade to the new major version.

Please note that the timelines shown below are illustrative and not binding

### Dependency lifecycle

Most AWS SDKs have underlying dependencies, such as language runtimes, AWS Lambda runtime, or third party libraries and frameworks. These dependencies are typically tied to the language community or the vendor who owns that particular component. Each community or vendor publishes their own end-of-support schedule for their product.

The following terms are used to classify underlying third party dependencies:

- [**AWS Lambda Runtime**](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html): Examples include `java17`, `nodejs20.x`, `python3.13`, etc.
- **Language Runtime**: Examples include Java 17, Python 3.13, NodeJS 20, .NET Core, etc.
- **Third party Library**: Examples include Jackson Project, AWS X-Ray SDK, AWS Encryption SDK, etc.

Powertools for AWS Lambda follows the [AWS Lambda Runtime deprecation policy cycle](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html#runtime-support-policy), when it comes to Language Runtime. This means we will stop supporting their respective deprecated Language Runtime *(e.g., `java8`)* without increasing the major SDK version.

AWS reserves the right to stop support for an underlying dependency without increasing the major SDK version

### Communication methods

Maintenance announcements are communicated in several ways:

- A pinned GitHub Request For Comments (RFC) issue indicating the campaign for the next major version. The RFC will outline the path to end-of-support, specify campaign timelines, and upgrade guidance.
- AWS SDK documentation, such as API reference documentation, user guides, SDK product marketing pages, and GitHub readme(s) are updated to indicate the campaign timeline and provide guidance on upgrading affected applications.
- Deprecation warnings are added to the SDKs, outlining the path to end-of-support and linking to the upgrade guide.

To see the list of available major versions of Powertools for AWS Lambda and where they are in their maintenance lifecycle, see the [version support matrix](#version-support-matrix).

### Version support matrix

| SDK | Major version | Current Phase | General Availability Date | Notes | | --- | --- | --- | --- | --- | | Powertools for AWS Lambda (Java) | 1.x | General Availability | 11/04/2020 | See [Release notes](https://github.com/aws-powertools/powertools-lambda-java/releases/tag/v1.0.0) |
