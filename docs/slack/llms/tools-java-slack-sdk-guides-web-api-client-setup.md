Source: https://docs.slack.dev/tools/java-slack-sdk/guides/web-api-client-setup

# API Client Installation

The first step to using the Slack API client is installing the `slack-api-client` module. This guide shows you how to set up using [Maven](https://maven.apache.org/), [Gradle](https://gradle.org/), or by building from source on your own.

* * *

## Prerequisites {#prerequisites}

[Installing OpenJDK 8 or higher LTS version](https://openjdk.java.net/install/) beforehand is required. As long as you are using a supported JDK version, this SDK should work with any OpenJDK distributions.

* * *

## Maven {#maven}

As `slack-api-client` is a library dependency, there is no requirement of Maven versions.

### pom.xml {#pomxml}

Save `pom.xml` with the following XML definition in the root directory of your Java project. As you see, this is a commonplace Maven project. No specific settings are needed to load the project on your favorite IDE.

```text
<project xmlns="http://maven.apache.org/POM/4.0.0"         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd">  <modelVersion>4.0.0</modelVersion>  <groupId>com.example</groupId>  <artifactId>awesome-slack-app</artifactId>  <version>0.1-SNAPSHOT</version>  <packaging>jar</packaging>  <properties>    <maven.compiler.target>1.8</maven.compiler.target>    <maven.compiler.source>1.8</maven.compiler.source>  </properties>  <dependencies>    <dependency>      <groupId>com.slack.api</groupId>      <artifactId>slack-api-client</artifactId>      <version>1.48.0</version>    </dependency>  </dependencies></project>
```

### src/main/java/Example.java {#srcmainjavaexamplejava}

Create a new Java class named `Example` that has a `main` method to run. Place the following code in the method for verifying the build settings are valid.

```text
import com.slack.api.Slack;import com.slack.api.methods.response.api.ApiTestResponse;public class Example {  public static void main(String[] args) throws Exception {    Slack slack = Slack.getInstance();    ApiTestResponse response = slack.methods().apiTest(r -> r.foo("bar"));    System.out.println(response);  }}
```

Run the `Example.main(String[])` method from your IDE or by running the following command in your terminal.

```text
mvn compile exec:java \  -Dexec.cleanupDaemonThreads=false \  -Dexec.mainClass="Example"
```

If you see the following `stdout`, your installation has succeeded!

```text
ApiTestResponse(ok=true, args=ApiTestResponse.Args(foo=bar, error=null), warning=null, error=null, needed=null, provided=null)
```

In summary, the things you've done here are:

* ✅ Installed JDK 8 or higher (if not, run `brew install openjdk@11` for macOS / visit [OpenJDK website](https://openjdk.java.net/install/) for others)
* ✅ Installed Maven (if not, run `brew install maven` for macOS / visit [their website](https://maven.apache.org/) for others)
* ✅ Updated the `pom.xml` file to have `slack-api-client` as a dependency
* ✅ Added a `main` method to the `src/main/java/Example.java` file

* * *

## Gradle {#gradle}

If you prefer using Gradle, the steps are similar to Maven, but there are some differences.

### build.gradle {#buildgradle}

Place `build.gradle` in the root directory of your Java project. We don't have any requirements for Gradle versions.

```text
plugins {  id("application")}repositories {  mavenCentral()}dependencies {  implementation("com.slack.api:slack-api-client:1.48.0")}application {  mainClassName = "Example"}
```

As with Maven, create a class named `Example` with a `main` method. Then, run it from your IDE or execute the `gradle run` command in your terminal. You'll see the same `stdout`.

In summary, the things you've done here are:

* ✅ Installed JDK 8 or higher (if not, run `brew install openjdk@11` for macOS / visit [OpenJDK website](https://openjdk.java.net/install/) for others)
* ✅ Installed Gradle (if not, run `brew install gradle` for macOS / visit [their website](https://gradle.org/) for others)
* ✅ Added `build.gradle` to have `slack-api-client` as a dependency
* ✅ Added a `main` method to the `src/main/java/Example.java` file

* * *

## Gradle for Kotlin {#gradle-for-kotlin}

In this guide, we sometimes use Kotlin code examples for simplicity. To try those examples, set up a Kotlin project with Gradle as below.

### build.gradle {#buildgradle-1}

The build settings are almost the same as above except for some Kotlin-specific parts.

```text
plugins {  id("org.jetbrains.kotlin.jvm") version "1.7.21" // use the latest Kotlin version  id("application")}repositories {  mavenCentral()}dependencies {  implementation(platform("org.jetbrains.kotlin:kotlin-bom"))  implementation("org.jetbrains.kotlin:kotlin-stdlib-jdk8")  implementation("com.slack.api:slack-api-client:1.48.0")  // Add these dependencies if you want to use the Kotlin DSL for building rich messages  implementation("com.slack.api:slack-api-model-kotlin-extension:1.48.0")  implementation("com.slack.api:slack-api-client-kotlin-extension:1.48.0")}application {  mainClassName = "ExampleKt" // add "Kt" suffix for main function source file}
```

### src/main/kotlin/Example.kt {#srcmainkotlinexamplekt}

As you see, the code using `slack-api-client` in Kotlin is much more concise than in Java. Run the following code from your IDE or by executing the `gradle run` command in your terminal.

```text
import com.slack.api.Slackfun main() {  val slack = Slack.getInstance()  val response = slack.methods().apiTest { it.foo("bar") }  println(response)}
```

Tip

A name of a source file in Kotlin needs to end with `.kt`, not `.java`.

In summary, the things you've done here are:

* ✅ Installed JDK 8 or higher (if not, run `brew install openjdk@11` for macOS / visit [OpenJDK website](https://openjdk.java.net/install/) for others)
* ✅ Installed Gradle (if not, run `brew install gradle` for macOS / visit [their website](https://gradle.org/) for others)
* ✅ Updated `build.gradle` to have valid Kotlin language settings and `slack-api-client` as a dependency
* ✅ Added a `main` method to the `src/main/kotlin/Example.kt` file

* * *

## Build from source {#build-from-source}

You may want to build the latest revision on your own. In the case of building from source, execute the following commands in your terminal.

```text
git clone git@github.com:slackapi/java-slack-sdk.gitcd java-slack-sdkmvn install -Dmaven.test.skip=true
```

All of the SDK modules will be available under `$HOME/.m2/repository`, so that you can now use them on the machine. If you're using Gradle, make sure to add `mavenLocal()` to `repositories` in your `build.gradle`.

```text
repositories {  mavenLocal()}
```
