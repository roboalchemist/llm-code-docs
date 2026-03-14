# Source: https://docs.statsig.com/server-core/java-core.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Java Server SDK

> Statsig's next-gen Java Server SDK built on our [Server Core](/server-core) framework

<Callout icon="github">
  <a href="https://github.com/statsig-io/statsig-server-core/tree/main/statsig-java" target="_blank" rel="noreferrer">Java Core on Github</a>
</Callout>

<Tip>Migrating from the Legacy Java SDK? See our [Migration Guide](/server-core/migration-guides/java).</Tip>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    ## Requirements

    * Java 8 or higher (Java 8 support added in version 0.4.3)
    * Compatible with all platforms listed in the Supported OS and Architecture Combinations section, including:
      * macOS (x86\_64, arm64)
      * Windows (x86\_64)
      * Amazon Linux 2 and 2023 (x86\_64, arm64)

    ## Overview

    The Statsig Java SDK can be installed in two ways:

    **Recommended: Single JAR installation** (since version 0.4.0)

    * Use the "uber" JAR which contains both the core library and popular platform-specific native libraries in a single package
    * Simplifies dependency management and deployment across different environments

    **Advanced: Two-part installation**

    1. The platform-independent core library
    2. An OS/architecture-specific native library for your specific platform

    ## Installation Steps

    ### Recommended: Using the Uber JAR (All-in-One)

    Since version 0.4.0, Statsig provides an "uber" JAR that contains both the core library and native libraries for popular supported platforms in a single package. This is the recommended approach for most users.

    <CodeGroup>
      ```groovy Gradle theme={null}
      repositories {
          mavenCentral()
      }

      dependencies {
          implementation 'com.statsig:javacore:X.X.X:uber' // Uber JAR with all native libraries
      }
      ```

      ```xml Maven theme={null}
      <dependencies>
          <dependency>
              <groupId>com.statsig</groupId>
              <artifactId>javacore</artifactId>
              <version>X.X.X</version>
              <classifier>uber</classifier>
          </dependency>
      </dependencies>
      ```
    </CodeGroup>

    You can find the latest version on [Maven Central](https://central.sonatype.com/artifact/com.statsig/javacore).

    The uber JAR includes native libraries for:

    * Linux (x86\_64, arm64)
    * macOS (x86\_64, arm64)
    * Windows (x86\_64)

    This approach eliminates the need to specify the exact platform and simplifies deployment across different environments.

    ### Advanced: Platform-Specific Installation

    If you need more control over dependencies or want to minimize the JAR size for a specific platform, you can use the platform-specific installation approach.

    <Steps>
      <Step title="Install Core Library">
        <CodeGroup>
          ```groovy Gradle theme={null}
          repositories {
              mavenCentral()
          }

          dependencies {
              implementation 'com.statsig:javacore:X.X.X'  // Replace X.X.X with the latest version
          }
          ```

          ```xml Maven theme={null}
          <dependencies>
              <dependency>
                  <groupId>com.statsig</groupId>
                  <artifactId>javacore</artifactId>
                  <version>X.X.X</version>  <!-- Replace X.X.X with the latest version -->
              </dependency>
          </dependencies>
          ```
        </CodeGroup>

        You can find the latest version on [Maven Central](https://central.sonatype.com/artifact/com.statsig/javacore).
      </Step>

      <Step title="Install Platform-Specific Library">
        You need to add the appropriate OS/architecture-specific dependency. Choose one of the following methods:

        **Method 1: Automatic Detection**

        Run the following code to detect your system and get the appropriate dependency:

        ```java  theme={null}
        import com.statsig.*;

        // All StatsigOptions are optional, feel free to adjust them as needed
        StatsigOptions options = new StatsigOptions.Builder().build();

        Statsig statsig = new Statsig("your-secret-key", options);
        ```

        You'll receive output similar to:

        ```
        For Linux with arm64 architecture, add the following to build.gradle:
          implementation 'com.statsig:javacore:<version>:aarch64-unknown-linux-gnu'

        For Linux with x86_64 architecture, add the following to build.gradle:
          implementation 'com.statsig:javacore:<version>:x86_64-unknown-linux-gnu'
        ```

        **Method 2: Manual Configuration**

        <CodeGroup>
          ```groovy Gradle theme={null}
          dependencies {
              implementation 'com.statsig:javacore:X.X.X'  // Core SDK (from Step 1)
              implementation 'com.statsig:javacore:X.X.X:YOUR-OS-ARCHITECTURE' // OS/architecture-specific dependency
          }
          ```

          ```xml Maven theme={null}
          <dependencies>
              <dependency>
                  <groupId>com.statsig</groupId>
                  <artifactId>javacore</artifactId>
                  <version>X.X.X</version>
              </dependency>
              <dependency>
                  <groupId>com.statsig</groupId>
                  <artifactId>javacore</artifactId>
                  <version>X.X.X</version>
                  <classifier>YOUR-OS-ARCHITECTURE</classifier>
              </dependency>
          </dependencies>
          ```
        </CodeGroup>

        Replace `YOUR-OS-ARCHITECTURE` with one of the supported combinations from the Supported OS and Architecture Combinations section.
      </Step>
    </Steps>

    <Warning>
      **Docker Considerations for Alpine Linux**

      When using Alpine Linux or other musl-based Docker containers, you need to install additional compatibility packages for the native libraries to work properly. Add the following to your Dockerfile:

      ```dockerfile  theme={null}
      RUN apk add --no-cache libgcc gcompat
      ```

      The Statsig Java Core SDK automatically detects musl-based systems and will use the appropriate musl-compatible native libraries (e.g., `x86_64-unknown-linux-musl`, `aarch64-unknown-linux-musl`).
    </Warning>

    <Accordion title="Tested Platforms">
      Docker base images where the Java Core SDK has been tested and verified:

      | Docker Base Image                           | Description                            |
      | ------------------------------------------- | -------------------------------------- |
      | amazoncorretto:21                           | Amazon Corretto 21 JDK                 |
      | amazoncorretto:21-alpine-jdk                | Amazon Corretto 21 JDK on Alpine Linux |
      | amazonlinux:2                               | Amazon Linux 2                         |
      | public.ecr.aws/amazonlinux/amazonlinux:2023 | Amazon Linux 2023                      |
      | azul/zulu-openjdk-alpine:21                 | Azul Zulu OpenJDK 21 on Alpine Linux   |
      | azul/zulu-openjdk:21                        | Azul Zulu OpenJDK 21                   |
      | eclipse-temurin:21-jdk                      | Eclipse Temurin 21 JDK                 |
      | eclipse-temurin:21-jdk-alpine               | Eclipse Temurin 21 JDK on Alpine Linux |
    </Accordion>
  </Step>

  <Step title="Initialize the SDK">
    After installation, you will need to initialize the SDK using a [Server Secret Key from the Statsig console](https://console.statsig.com/api_keys).

    <Warning>
      Server Secret Keys should always be kept private. If you expose one, you can disable and recreate it in the Statsig console.
    </Warning>

    There is also an optional parameter named `options` that allows you to pass in a StatsigOptions to customize the SDK.

    <CodeGroup>
      ```java Java theme={null}
      import com.statsig.*;

      // All StatsigOptions are optional, feel free to adjust them as needed
      StatsigOptions options = new StatsigOptions.Builder()
                          .setSpecsSyncIntervalMs(10000)
                          .setEventLoggingFlushIntervalMs(10000)
                          .setOutputLoggerLevel(OutputLogger.LogLevel.INFO)
                          .build();

      Statsig myStatsigServer = new Statsig(SECRET_KEY, options);
      myStatsigServer.initialize().get();
      ```

      ```kotlin Kotlin theme={null}
      import com.statsig.*

      // All StatsigOptions are optional, feel free to adjust them as needed
      val options = StatsigOptions.Builder()
          .setSpecsSyncIntervalMs(10000)
          .setEventLoggingFlushIntervalMs(10000)
          .setOutputLoggerLevel(OutputLogger.LogLevel.INFO)
          .build()

      val myStatsigServer = Statsig(SECRET_KEY, options)
      myStatsigServer.initialize().get()
      ```
    </CodeGroup>

    `initialize` will perform a network request. After `initialize` completes, virtually all SDK operations will be synchronous (See [Evaluating Feature Gates in the Statsig SDK](https://blog.statsig.com/evaluating-feature-gates-in-the-statsig-sdk-a6f8881a1ad8)). The SDK will fetch updates from Statsig in the background, independently of your API calls.
  </Step>
</Steps>

## Getting Started

### Quick Start Example

<Steps>
  <Step title="Create a new Java project">
    Create a new Gradle or Maven project with the following structure:

    ```
    my-statsig-app/
    ├── build.gradle (or pom.xml)
    └── src/main/java/ExampleApp.java
    ```
  </Step>

  <Step title="Add Statsig dependency">
    <CodeGroup>
      ```groovy build.gradle theme={null}
      plugins {
          id 'java'
          id 'application'
      }

      repositories {
          mavenCentral()
      }

      dependencies {
          implementation 'com.statsig:javacore:X.X.X:uber'
      }

      application {
          mainClass = 'ExampleApp'
      }
      ```

      ```xml pom.xml theme={null}
      <project>
          <modelVersion>4.0.0</modelVersion>
          <groupId>com.example</groupId>
          <artifactId>my-statsig-app</artifactId>
          <version>1.0-SNAPSHOT</version>
          
          <dependencies>
              <dependency>
                  <groupId>com.statsig</groupId>
                  <artifactId>javacore</artifactId>
                  <version>X.X.X</version>
                  <classifier>uber</classifier>
              </dependency>
          </dependencies>
          
          <build>
              <plugins>
                  <plugin>
                      <groupId>org.codehaus.mojo</groupId>
                      <artifactId>exec-maven-plugin</artifactId>
                      <version>3.0.0</version>
                      <configuration>
                          <mainClass>ExampleApp</mainClass>
                      </configuration>
                  </plugin>
              </plugins>
          </build>
      </project>
      ```
    </CodeGroup>

    Replace `X.X.X` with the latest version from [Maven Central](https://central.sonatype.com/artifact/com.statsig/javacore).
  </Step>

  <Step title="Write your application code">
    <CodeGroup>
      ```java ExampleApp.java theme={null}
      import com.statsig.*;

      public class ExampleApp {
          public static void main(String[] args) throws Exception {
              // Initialize Statsig
              StatsigOptions options = new StatsigOptions.Builder().build();
              Statsig statsig = new Statsig("YOUR_SERVER_SECRET_KEY", options);
              statsig.initialize().get();
              
              try {
                  // Check a feature gate
                  boolean isEnabled = statsig.checkGate("user123", "my_feature_gate");
                  System.out.println("Feature gate is " + (isEnabled ? "enabled" : "disabled"));
                  
                  // Get a config
                  DynamicConfig config = statsig.getConfig("user123", "my_config");
                  System.out.println("Config value: " + config.getString("some_parameter", "default_value"));
              } finally {
                  // Always shutdown Statsig when done
                  statsig.shutdown();
              }
          }
      }
      ```

      ```kotlin ExampleApp.kt theme={null}
      import com.statsig.*

      fun main() {
          // Initialize Statsig
          val options = StatsigOptions.Builder().build()
          val statsig = Statsig("YOUR_SERVER_SECRET_KEY", options)
          statsig.initialize().get()
          
          try {
              // Check a feature gate
              val isEnabled = statsig.checkGate("user123", "my_feature_gate")
              println("Feature gate is ${if (isEnabled) "enabled" else "disabled"}")
              
              // Get a config
              val config = statsig.getConfig("user123", "my_config")
              println("Config value: ${config.getString("some_parameter", "default_value")}")
          } finally {
              // Always shutdown Statsig when done
              statsig.shutdown().get()
          }
      }
      ```
    </CodeGroup>

    Replace `YOUR_SERVER_SECRET_KEY` with your actual server secret key from the [Statsig Console](https://console.statsig.com/).
  </Step>

  <Step title="Run the application">
    <CodeGroup>
      ```bash Gradle theme={null}
      ./gradlew run
      ```

      ```bash Maven theme={null}
      mvn compile exec:java
      ```
    </CodeGroup>

    If everything is set up correctly, you should see output related to your feature gate and configuration.
  </Step>
</Steps>

## Working with the SDK

### Checking a Feature Flag/Gate

Now that your SDK is initialized, let's fetch a [**Feature Gate**](/feature-flags/overview). Feature Gates can be used to create logic branches in code that can be rolled out to different users from the Statsig Console. Gates are always **CLOSED** or **OFF** (think `return false;`) by default.

From this point on, all APIs will require you to specify the user (see [Statsig user](#statsig-user)) associated with the request. For example, check a gate for a certain user like this:

<CodeGroup>
  ```java Java theme={null}
  String userID = "user_id";
  boolean result = statsig.checkGate(userID, "my_feature_gate");

  // with StatsigUser
  StatsigUser user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build();
  boolean gateResult = statsig.checkGate(user, "my_feature_gate");
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"
  val result = statsig.checkGate(userID, "my_feature_gate")

  // with StatsigUser
  val user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build()
  val gateResult = statsig.checkGate(user, "my_feature_gate")
  ```
</CodeGroup>

### Reading a Dynamic Config

Feature Gates can be very useful for simple on/off switches, with optional but advanced user targeting. However, if you want to be send a different set of values (strings, numbers, and etc.) to your clients based on specific user attributes, e.g. country, [**Dynamic Configs**](/dynamic-config) can help you with that. The API is very similar to Feature Gates, but you get an entire json object you can configure on the server and you can fetch typed parameters from it. For example:

<CodeGroup>
  ```java Java theme={null}
  String userID = "user_id";
  DynamicConfig config = statsig.getConfig(userID, "my_config");

  String name = config.getString("name", "");
  int size = config.getInt("size", 10);

  // with StatsigUser
  StatsigUser user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build();
  DynamicConfig dynamicConfig = statsig.getConfig(user, "my_config");
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"
  val config = statsig.getConfig(userID, "my_config")

  val name = config.getString("name", "")
  val size = config.getInt("size", 10)

  // with StatsigUser
  val user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build()
  val dynamicConfig = statsig.getConfig(user, "my_config")
  ```
</CodeGroup>

### Getting a Layer/Experiment

Then we have **Layers/Experiments**, which you can use to run A/B/n experiments. We offer two APIs, but often recommend the use of [layers](/layers), which make parameters reusable and let you run mutually exclusive experiments.

<CodeGroup>
  ```java Java theme={null}
  String userID = "user_id";

  // Getting an Experiment
  Experiment experiment = statsig.getExperiment(userID, "my_experiment");
  String expName = experiment.getString("experiment_param", "");

  // Getting a Layer
  Layer layer = statsig.getLayer(userID, "my_layer");
  String layerValue = layer.getString("layer_param", "default");

  // with StatsigUser
  StatsigUser user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build();
      
  Experiment experimentWithUser = statsig.getExperiment(user, "my_experiment");
  Layer layerWithUser = statsig.getLayer(user, "my_layer");
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"

  // Getting an Experiment
  val experiment = statsig.getExperiment(userID, "my_experiment")
  val expName = experiment.getString("experiment_param", "")

  // Getting a Layer
  val layer = statsig.getLayer(userID, "my_layer")
  val layerValue = layer.getString("layer_param", "default")

  // with StatsigUser
  val user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build()
      
  val experimentWithUser = statsig.getExperiment(user, "my_experiment")
  val layerWithUser = statsig.getLayer(user, "my_layer")
  ```
</CodeGroup>

### Retrieving Feature Gate Metadata

In certain scenarios, you may need more information about a gate evaluation than just a boolean value. For additional metadata about the evaluation, use the Get Feature Gate API, which returns a FeatureGate object:

<CodeGroup>
  ```java Java theme={null}
  String userID = "user_id";
  FeatureGate gate = statsig.getFeatureGate(userID, "my_feature_gate");

  System.out.println("Gate name: " + gate.name);
  System.out.println("Gate value: " + gate.value);
  System.out.println("Rule ID: " + gate.ruleID);

  // with StatsigUser
  StatsigUser user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build();
  FeatureGate gateWithUser = statsig.getFeatureGate(user, "my_feature_gate");
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"
  val gate = statsig.getFeatureGate(userID, "my_feature_gate")

  println("Gate name: ${gate.name}")
  println("Gate value: ${gate.value}")
  println("Rule ID: ${gate.ruleID}")

  // with StatsigUser
  val user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build()
  val gateWithUser = statsig.getFeatureGate(user, "my_feature_gate")
  ```
</CodeGroup>

### Parameter Stores

Sometimes you don't know whether you want a value to be a Feature Gate, Experiment, or Dynamic Config yet. If you want on-the-fly control of that outside of your deployment cycle, you can use Parameter Stores to define a parameter that can be changed into at any point in the Statsig console. Parameter Stores are optional, but parameterizing your application can prove very useful for future flexibility and can even allow non-technical Statsig users to turn parameters into experiments.

<CodeGroup>
  ```java Java theme={null}
  String userID = "user_id";
  ParameterStore store = statsig.getParameterStore(userID, "my_param_store");

  String stringValue = store.getString("string_param", "default");
  int intValue = store.getInt("int_param", 0);
  boolean boolValue = store.getBoolean("bool_param", false);
  double doubleValue = store.getDouble("double_param", 0.0);

  // with StatsigUser
  StatsigUser user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build();
  ParameterStore storeWithUser = statsig.getParameterStore(user, "my_param_store");
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"
  val store = statsig.getParameterStore(userID, "my_param_store")

  val stringValue = store.getString("string_param", "default")
  val intValue = store.getInt("int_param", 0)
  val boolValue = store.getBoolean("bool_param", false)
  val doubleValue = store.getDouble("double_param", 0.0)

  // with StatsigUser
  val user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build()
  val storeWithUser = statsig.getParameterStore(user, "my_param_store")
  ```
</CodeGroup>

### Logging an Event

Now that you have a Feature Gate or an Experiment set up, you may want to track some custom events and see how your new features or different experiment groups affect these events. This is super easy with Statsig—simply call the Log Event API and specify the user and event name to log; you additionally provide some value and/or an object of metadata to be logged together with the event:

<CodeGroup>
  ```java Java theme={null}
  import java.util.HashMap;
  import java.util.Map;

  String userID = "user_id";
  String eventName = "my_custom_event";

  // Simple event
  statsig.logEvent(userID, eventName);

  // Event with value
  statsig.logEvent(userID, eventName, 10.5);

  // Event with metadata
  Map<String, String> metadata = new HashMap<>();
  metadata.put("key1", "value1");
  metadata.put("key2", "value2");
  statsig.logEvent(userID, eventName, metadata);

  // Event with value and metadata
  statsig.logEvent(userID, eventName, 10.5, metadata);

  // with StatsigUser
  StatsigUser user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build();
  statsig.logEvent(user, eventName, 10.5, metadata);
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"
  val eventName = "my_custom_event"

  // Simple event
  statsig.logEvent(userID, eventName)

  // Event with value
  statsig.logEvent(userID, eventName, 10.5)

  // Event with metadata
  val metadata = mapOf(
      "key1" to "value1",
      "key2" to "value2"
  )
  statsig.logEvent(userID, eventName, metadata)

  // Event with value and metadata
  statsig.logEvent(userID, eventName, 10.5, metadata)

  // with StatsigUser
  val user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build()
  statsig.logEvent(user, eventName, 10.5, metadata)
  ```
</CodeGroup>

### Sending Events to Log Explorer

You can forward logs to Logs Explorer for convenient analysis using the Forward Log Line Event API. This lets you include custom metadata and event values with each log.

<CodeGroup>
  ```java Java theme={null}
  import java.util.HashMap;
  import java.util.Map;

  String userID = "user_id";

  Map<String, Object> payload = new HashMap<>();
  payload.put("log_level", "error");
  payload.put("message", "Something went wrong");
  payload.put("timestamp", System.currentTimeMillis());

  statsig.forwardLogLineEvent(userID, payload);

  // with StatsigUser
  StatsigUser user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build();
  statsig.forwardLogLineEvent(user, payload);
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"

  val payload = mapOf(
      "log_level" to "error",
      "message" to "Something went wrong",
      "timestamp" to System.currentTimeMillis()
  )

  statsig.forwardLogLineEvent(userID, payload)

  // with StatsigUser
  val user = StatsigUser.builder()
      .userID("user_id")
      .email("my_user@example.com")
      .build()
  statsig.forwardLogLineEvent(user, payload)
  ```
</CodeGroup>

## Using Shared Instance

In some applications, you may want to create a single Statsig instance that can be accessed globally throughout your codebase. The shared instance functionality provides a singleton pattern for this purpose:

<CodeGroup>
  ```java Java theme={null}
  import com.statsig.*;

  // Create a shared instance that can be accessed globally
  StatsigServer statsig = Statsig.newShared("secret-key");
  statsig.initialize().get();

  // Access the shared instance from anywhere in your code
  StatsigServer sharedStatsig = Statsig.shared();
  boolean isFeatureEnabled = sharedStatsig.checkGate(user, "feature_name");

  // Check if a shared instance exists
  if (Statsig.hasSharedInstance()) {
    // Use the shared instance
  }

  // Remove the shared instance when no longer needed
  Statsig.removeShared();
  ```

  ```kotlin Kotlin theme={null}
  import com.statsig.*

  // Create a shared instance that can be accessed globally
  val statsig = Statsig.newShared("secret-key")
  statsig.initialize().get()

  // Access the shared instance from anywhere in your code
  val sharedStatsig = Statsig.shared()
  val isFeatureEnabled = sharedStatsig.checkGate(user, "feature_name")

  // Check if a shared instance exists
  if (Statsig.hasSharedInstance()) {
    // Use the shared instance
  }

  // Remove the shared instance when no longer needed
  Statsig.removeShared()
  ```
</CodeGroup>

The shared instance functionality provides a singleton pattern where a single Statsig instance can be created and accessed globally throughout your application. This is useful for applications that need to access Statsig functionality from multiple parts of the codebase without having to pass around a Statsig instance.

* `Statsig.newShared(sdkKey, options)`: Creates a new shared instance of Statsig that can be accessed globally
* `Statsig.shared()`: Returns the shared instance
* `Statsig.hasSharedInstance()`: Checks if a shared instance exists (useful when you aren't sure if the shared instance is ready yet)
* `Statsig.removeShared()`: Removes the shared instance (useful when you want to switch to a new shared instance)

<Note>
  `hasSharedInstance()` and `removeShared()` are helpful in specific scenarios but aren't required in most use cases where the shared instance is set up near the top of your application.

  Also note that only one shared instance can exist at a time. Attempting to create a second shared instance will result in an error.
</Note>

## Manual Exposures

By default, the SDK will automatically log an exposure event when you check a gate, get a config, get an experiment, or call get() on a parameter in a layer. However, there are times when you may want to log an exposure event manually. For example, if you're using a gate to control access to a feature, but you don't want to log an exposure until the user actually uses the feature, you can use manual exposures.

Manual exposures allow you to control when exposure events are logged. This is useful when you want to delay exposure logging until certain conditions are met.

<CodeGroup>
  ```java Java theme={null}
  String userID = "user_id";

  // Check gate without logging exposure
  boolean result = statsig.checkGateWithExposureLoggingDisabled(userID, "my_feature_gate");

  // Manually log the exposure when ready
  statsig.manuallyLogGateExposure(userID, "my_feature_gate");

  // Works with configs too
  DynamicConfig config = statsig.getConfigWithExposureLoggingDisabled(userID, "my_config");
  statsig.manuallyLogConfigExposure(userID, "my_config");

  // And with experiments/layers
  Experiment experiment = statsig.getExperimentWithExposureLoggingDisabled(userID, "my_experiment");
  statsig.manuallyLogExperimentExposure(userID, "my_experiment");

  Layer layer = statsig.getLayerWithExposureLoggingDisabled(userID, "my_layer");
  statsig.manuallyLogLayerParameterExposure(userID, "my_layer", "parameter_name");
  ```

  ```kotlin Kotlin theme={null}
  val userID = "user_id"

  // Check gate without logging exposure
  val result = statsig.checkGateWithExposureLoggingDisabled(userID, "my_feature_gate")

  // Manually log the exposure when ready
  statsig.manuallyLogGateExposure(userID, "my_feature_gate")

  // Works with configs too
  val config = statsig.getConfigWithExposureLoggingDisabled(userID, "my_config")
  statsig.manuallyLogConfigExposure(userID, "my_config")

  // And with experiments/layers
  val experiment = statsig.getExperimentWithExposureLoggingDisabled(userID, "my_experiment")
  statsig.manuallyLogExperimentExposure(userID, "my_experiment")

  val layer = statsig.getLayerWithExposureLoggingDisabled(userID, "my_layer")
  statsig.manuallyLogLayerParameterExposure(userID, "my_layer", "parameter_name")
  ```
</CodeGroup>

## Statsig User

The `StatsigUser` object represents a user in Statsig. You must provide a `userID` or at least one of the `customIDs` to identify the user.

When calling APIs that require a user, you should pass as much information as possible in order to take advantage of advanced gate and config conditions (like country or OS/browser level checks), and correctly measure impact of your experiments on your metrics/events. As explained [here](/sdks/user#why-is-an-id-always-required-for-server-sdks), at least one identifier (userID or customID) is required to provide a consistent experience for a given user.

Besides userID, we also have email, ip, userAgent, country, locale and appVersion as top-level fields on StatsigUser. In addition, you can pass any key-value pairs in an object/dictionary to the custom field and be able to create targeting based on them.

### Private Attributes

Private attributes are user attributes that are used for evaluation but are not forwarded to any integrations. They are useful for PII or sensitive data that you don't want to send to third-party services.

The `StatsigUser` object represents a user in your application and contains fields used for feature evaluation.

<CodeGroup>
  ```java Java theme={null}
  import com.statsig.*;
  import java.util.HashMap;
  import java.util.Map;

  // Build a user with various fields
  Map<String, Object> customFields = new HashMap<>();
  customFields.put("plan", "premium");
  customFields.put("age", 25);

  Map<String, String> privateAttributes = new HashMap<>();
  privateAttributes.put("internal_id", "123456");

  StatsigUser user = StatsigUser.builder()
      .userID("user_123")
      .email("user@example.com")
      .ip("192.168.1.1")
      .userAgent("Mozilla/5.0...")
      .country("US")
      .locale("en_US")
      .appVersion("1.2.3")
      .custom(customFields)
      .privateAttributes(privateAttributes)
      .build();

  // Use the user for evaluation
  boolean result = statsig.checkGate(user, "my_feature_gate");
  ```

  ```kotlin Kotlin theme={null}
  import com.statsig.*

  // Build a user with various fields
  val customFields = mapOf(
      "plan" to "premium",
      "age" to 25
  )

  val privateAttributes = mapOf(
      "internal_id" to "123456"
  )

  val user = StatsigUser.builder()
      .userID("user_123")
      .email("user@example.com")
      .ip("192.168.1.1")
      .userAgent("Mozilla/5.0...")
      .country("US")
      .locale("en_US")
      .appVersion("1.2.3")
      .custom(customFields)
      .privateAttributes(privateAttributes)
      .build()

  // Use the user for evaluation
  val result = statsig.checkGate(user, "my_feature_gate")
  ```
</CodeGroup>

## Private Attributes

Private attributes are fields that will be used for evaluation but will not be logged in events sent to Statsig servers.

<CodeGroup>
  ```java Java theme={null}
  Map<String, String> privateAttributes = new HashMap<>();
  privateAttributes.put("sensitive_field", "sensitive_value");

  StatsigUser user = StatsigUser.builder()
      .userID("user_123")
      .privateAttributes(privateAttributes)
      .build();
  ```

  ```kotlin Kotlin theme={null}
  val privateAttributes = mapOf(
      "sensitive_field" to "sensitive_value"
  )

  val user = StatsigUser.builder()
      .userID("user_123")
      .privateAttributes(privateAttributes)
      .build()
  ```
</CodeGroup>

## Statsig Options

You can pass in an optional parameter `options` in addition to `sdkKey` during initialization to customize the Statsig client. Here are the available options that you can configure.

<Accordion title="StatsigOptions">
  <ResponseField name="environment" type="string">
    Environment parameter for evaluation.
  </ResponseField>

  <ResponseField name="specsUrl" type="string">
    Custom URL for fetching feature specifications.
  </ResponseField>

  <ResponseField name="specsSyncIntervalMs" type="long">
    How often the SDK updates specifications from Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="fallbackToStatsig" type="boolean" default="false">
    Turn this on if you are proxying `download_config_specs` / `get_id_lists` and want to fall back to the default Statsig endpoint to increase reliability.
  </ResponseField>

  <ResponseField name="logEventUrl" type="string">
    Custom URL for logging events.
  </ResponseField>

  <ResponseField name="disableAllLogging" type="boolean" default="false">
    If true, the SDK will not collect any logging within the session, including custom events and config check exposure events.
  </ResponseField>

  <ResponseField name="enableIDLists" type="boolean" default="false">
    Required to be `true` when using segments with more than 1000 IDs.
  </ResponseField>

  <ResponseField name="disableUserAgentParsing" type="boolean" default="false">
    If true, the SDK will not parse User-Agent strings into `browserName`, `browserVersion`, `systemName`, `systemVersion`, and `appVersion` when needed for evaluation.
  </ResponseField>

  <ResponseField name="disableUserCountryLookup" type="boolean" default="false">
    If true, the SDK will not parse IP addresses (from `user.ip`) into country codes when needed for evaluation.
  </ResponseField>

  <ResponseField name="eventLoggingFlushIntervalMs" type="long">
    How often events are flushed to Statsig servers (in milliseconds).
  </ResponseField>

  <ResponseField name="eventLoggingMaxQueueSize" type="int">
    Maximum number of events to queue before forcing a flush.
  </ResponseField>

  <ResponseField name="dataStore" type="DataStore">
    An adapter with custom storage behavior for config specs. Can also continuously fetch updates in place of the Statsig network.
  </ResponseField>

  <ResponseField name="persistentStorage" type="PersistentStorage">
    Interface to use persistent storage within the SDK.
  </ResponseField>

  <ResponseField name="outputLoggerLevel" type="OutputLogger.LogLevel">
    Set the logging level for the SDK. Options: `NONE`, `ERROR`, `WARN`, `INFO`, `DEBUG`.
  </ResponseField>

  <ResponseField name="observabilityClient" type="ObservabilityClient">
    Interface to integrate observability metrics exposed by the SDK.
  </ResponseField>

  ***

  <CodeGroup>
    ```java Java theme={null}
    // Example usage
    StatsigOptions options = new StatsigOptions.Builder()
        .setEnvironment("staging")
        .setSpecsSyncIntervalMs(10000)
        .setEventLoggingFlushIntervalMs(5000)
        .setOutputLoggerLevel(OutputLogger.LogLevel.INFO)
        .build();

    Statsig statsig = new Statsig("secret-key", options);
    statsig.initialize().get();
    ```

    ```kotlin Kotlin theme={null}
    // Example usage
    val options = StatsigOptions.Builder()
        .setEnvironment("staging")
        .setSpecsSyncIntervalMs(10000)
        .setEventLoggingFlushIntervalMs(5000)
        .setOutputLoggerLevel(OutputLogger.LogLevel.INFO)
        .build()

    val statsig = Statsig("secret-key", options)
    statsig.initialize().get()
    ```
  </CodeGroup>
</Accordion>

## Shutting Statsig Down

Because we batch and periodically flush events, some events may not have been sent when your app/server shuts down. To make sure all logged events are properly flushed, you should call `shutdown()` before your app/server shuts down:

<CodeGroup>
  ```java Java theme={null}
  // Shutdown flushes all pending events and stops background tasks
  statsig.shutdown();

  // Or with a timeout (blocks until shutdown completes or timeout)
  statsig.shutdown().get(5, TimeUnit.SECONDS);
  ```

  ```kotlin Kotlin theme={null}
  // Shutdown flushes all pending events and stops background tasks
  statsig.shutdown()

  // Or with a timeout (blocks until shutdown completes or timeout)
  statsig.shutdown().get(5, TimeUnit.SECONDS)
  ```
</CodeGroup>

## Local Overrides

Local Overrides are a way to override the values of gates, configs, experiments, and layers for testing purposes. This is useful for local development or testing scenarios where you want to force a specific value without having to change the configuration in the Statsig console.

Local overrides allow you to override feature gate and config values for testing purposes.

<CodeGroup>
  ```java Java theme={null}
  import java.util.HashMap;
  import java.util.Map;

  // Override a gate
  statsig.overrideGate("my_feature_gate", true);

  // Override a config
  Map<String, Object> configOverride = new HashMap<>();
  configOverride.put("key", "value");
  configOverride.put("number", 42);
  statsig.overrideConfig("my_config", configOverride);

  // Override an experiment
  Map<String, Object> experimentOverride = new HashMap<>();
  experimentOverride.put("variant", "test");
  statsig.overrideExperiment("my_experiment", experimentOverride);

  // Override a layer
  Map<String, Object> layerOverride = new HashMap<>();
  layerOverride.put("layer_param", "override_value");
  statsig.overrideLayer("my_layer", layerOverride);

  // Clear all overrides
  statsig.clearAllOverrides();

  // Clear specific override
  statsig.clearGateOverride("my_feature_gate");
  statsig.clearConfigOverride("my_config");
  ```

  ```kotlin Kotlin theme={null}
  // Override a gate
  statsig.overrideGate("my_feature_gate", true)

  // Override a config
  val configOverride = mapOf(
      "key" to "value",
      "number" to 42
  )
  statsig.overrideConfig("my_config", configOverride)

  // Override an experiment
  val experimentOverride = mapOf(
      "variant" to "test"
  )
  statsig.overrideExperiment("my_experiment", experimentOverride)

  // Override a layer
  val layerOverride = mapOf(
      "layer_param" to "override_value"
  )
  statsig.overrideLayer("my_layer", layerOverride)

  // Clear all overrides
  statsig.clearAllOverrides()

  // Clear specific override
  statsig.clearGateOverride("my_feature_gate")
  statsig.clearConfigOverride("my_config")
  ```
</CodeGroup>

## Persistent Storage

The Persistent Storage interface allows you to implement custom storage for user-specific configurations. This enables you to persist user assignments across sessions, ensuring consistent experiment groups even when the user returns later. This is particularly useful for client-side A/B testing where you want to ensure users always see the same variant.

Persistent storage allows the SDK to persist sticky experiment assignments for users, ensuring they see consistent experiment variants across sessions.

<CodeGroup>
  ```java Java theme={null}
  import com.statsig.*;
  import java.util.HashMap;
  import java.util.Map;

  class MyPersistentStorage implements PersistentStorage {
      private Map<String, Map<String, StickyValues>> storage = new HashMap<>();

      @Override
      public Map<String, StickyValues> load(String key) {
          // Load persisted sticky values for the given key
          // Key format is "{userId}:userID" or "{customId}:{idType}"
          return storage.get(key);
      }

      @Override
      public void save(String key, String configName, StickyValues data) {
          // Save sticky values for a specific experiment/config
          storage.computeIfAbsent(key, k -> new HashMap<>()).put(configName, data);
      }

      @Override
      public void delete(String key, String configName) {
          // Delete sticky values for a specific experiment/config
          Map<String, StickyValues> values = storage.get(key);
          if (values != null) {
              values.remove(configName);
          }
      }
  }

  // Use persistent storage
  StatsigOptions options = new StatsigOptions.Builder()
      .setPersistentStorage(new MyPersistentStorage())
      .build();

  Statsig statsig = new Statsig("secret-key", options);
  statsig.initialize().get();
  ```

  ```kotlin Kotlin theme={null}
  import com.statsig.*

  class MyPersistentStorage : PersistentStorage {
      private val storage = mutableMapOf<String, MutableMap<String, StickyValues>>()

      override fun load(key: String): Map<String, StickyValues>? {
          // Load persisted sticky values for the given key
          // Key format is "{userId}:userID" or "{customId}:{idType}"
          return storage[key]
      }

      override fun save(key: String, configName: String, data: StickyValues) {
          // Save sticky values for a specific experiment/config
          storage.getOrPut(key) { mutableMapOf() }[configName] = data
      }

      override fun delete(key: String, configName: String) {
          // Delete sticky values for a specific experiment/config
          storage[key]?.remove(configName)
      }
  }

  // Use persistent storage
  val options = StatsigOptions.Builder()
      .setPersistentStorage(MyPersistentStorage())
      .build()

  val statsig = Statsig("secret-key", options)
  statsig.initialize().get()
  ```
</CodeGroup>

### Helper methods

The `PersistentStorage` interface provides helper methods for working with user-based storage keys:

```java  theme={null}
// Get persisted values for a user using the helper method
Map<String, StickyValues> values = persistentStorage.getValuesForUser(user, "userID");

// Generate a storage key from a user and ID type
String key = PersistentStorage.getStorageKey(user, "userID");  // Returns "{userId}:userID"
String customKey = PersistentStorage.getStorageKey(user, "companyID");  // Returns "{companyId}:companyID"
```

## Data Store

The Data Store interface allows you to implement custom storage for Statsig configurations. This enables advanced caching strategies and integration with your preferred storage systems.

Data stores allow you to customize how the SDK fetches and caches feature specifications, enabling advanced use cases like using Redis or other distributed caches.

<CodeGroup>
  ```java Java theme={null}
  import com.statsig.*;

  class MyDataStore implements DataStore {
      @Override
      public String getDataSync(String key) {
          // Synchronously fetch data for the given key
          // This is called during SDK evaluation
          return null;
      }

      @Override
      public CompletableFuture<Void> setData(String key, String data) {
          // Store data for the given key
          // Called when SDK receives updates from Statsig
          return CompletableFuture.completedFuture(null);
      }

      @Override
      public CompletableFuture<Void> initialize() {
          // Perform any initialization needed for your data store
          return CompletableFuture.completedFuture(null);
      }

      @Override
      public void shutdown() {
          // Clean up resources
      }
  }

  // Use data store
  StatsigOptions options = new StatsigOptions.Builder()
      .setDataStore(new MyDataStore())
      .build();

  Statsig statsig = new Statsig("secret-key", options);
  statsig.initialize().get();
  ```

  ```kotlin Kotlin theme={null}
  import com.statsig.*
  import java.util.concurrent.CompletableFuture

  class MyDataStore : DataStore {
      override fun getDataSync(key: String): String? {
          // Synchronously fetch data for the given key
          // This is called during SDK evaluation
          return null
      }

      override fun setData(key: String, data: String): CompletableFuture<Void> {
          // Store data for the given key
          // Called when SDK receives updates from Statsig
          return CompletableFuture.completedFuture(null)
      }

      override fun initialize(): CompletableFuture<Void> {
          // Perform any initialization needed for your data store
          return CompletableFuture.completedFuture(null)
      }

      override fun shutdown() {
          // Clean up resources
      }
  }

  // Use data store
  val options = StatsigOptions.Builder()
      .setDataStore(MyDataStore())
      .build()

  val statsig = Statsig("secret-key", options)
  statsig.initialize().get()
  ```
</CodeGroup>

## Custom Output Logger

The Output Logger interface allows you to customize how the SDK logs messages. This enables integration with your own logging system and control over log verbosity.

Custom output logger allows you to redirect SDK logs to your own logging system.

<CodeGroup>
  ```java Java theme={null}
  import com.statsig.*;

  class MyOutputLogger implements OutputLogger {
      @Override
      public void log(LogLevel level, String message) {
          // Route SDK logs to your logging system
          switch (level) {
              case ERROR:
                  System.err.println("[ERROR] " + message);
                  break;
              case WARN:
                  System.out.println("[WARN] " + message);
                  break;
              case INFO:
                  System.out.println("[INFO] " + message);
                  break;
              case DEBUG:
                  System.out.println("[DEBUG] " + message);
                  break;
          }
      }
  }

  // Use custom output logger
  StatsigOptions options = new StatsigOptions.Builder()
      .setOutputLogger(new MyOutputLogger())
      .setOutputLoggerLevel(OutputLogger.LogLevel.INFO)
      .build();

  Statsig statsig = new Statsig("secret-key", options);
  statsig.initialize().get();
  ```

  ```kotlin Kotlin theme={null}
  import com.statsig.*

  class MyOutputLogger : OutputLogger {
      override fun log(level: OutputLogger.LogLevel, message: String) {
          // Route SDK logs to your logging system
          when (level) {
              OutputLogger.LogLevel.ERROR -> println("[ERROR] $message")
              OutputLogger.LogLevel.WARN -> println("[WARN] $message")
              OutputLogger.LogLevel.INFO -> println("[INFO] $message")
              OutputLogger.LogLevel.DEBUG -> println("[DEBUG] $message")
              else -> {}
          }
      }
  }

  // Use custom output logger
  val options = StatsigOptions.Builder()
      .setOutputLogger(MyOutputLogger())
      .setOutputLoggerLevel(OutputLogger.LogLevel.INFO)
      .build()

  val statsig = Statsig("secret-key", options)
  statsig.initialize().get()
  ```
</CodeGroup>

## Observability Client

The Observability Client interface allows you to monitor the health of the SDK by integrating with your own observability systems. This enables tracking metrics, errors, and performance data. For more information on the metrics emitted by Statsig SDKs, see the [Monitoring documentation](/sdk_monitoring).

Observability client allows you to monitor SDK performance and emit custom metrics.

<CodeGroup>
  ```java Java theme={null}
  import com.statsig.*;

  class MyObservabilityClient implements ObservabilityClient {
      @Override
      public void emitMetric(String metricName, double value, Map<String, String> tags) {
          // Send metric to your monitoring system
          System.out.println("Metric: " + metricName + " = " + value + ", tags: " + tags);
      }

      @Override
      public void startTimer(String operationName) {
          // Start timing an operation
      }

      @Override
      public void endTimer(String operationName, Map<String, String> tags) {
          // End timing and emit duration metric
      }
  }

  // Use observability client
  StatsigOptions options = new StatsigOptions.Builder()
      .setObservabilityClient(new MyObservabilityClient())
      .build();

  Statsig statsig = new Statsig("secret-key", options);
  statsig.initialize().get();
  ```

  ```kotlin Kotlin theme={null}
  import com.statsig.*

  class MyObservabilityClient : ObservabilityClient {
      override fun emitMetric(metricName: String, value: Double, tags: Map<String, String>) {
          // Send metric to your monitoring system
          println("Metric: $metricName = $value, tags: $tags")
      }

      override fun startTimer(operationName: String) {
          // Start timing an operation
      }

      override fun endTimer(operationName: String, tags: Map<String, String>) {
          // End timing and emit duration metric
      }
  }

  // Use observability client
  val options = StatsigOptions.Builder()
      .setObservabilityClient(MyObservabilityClient())
      .build()

  val statsig = Statsig("secret-key", options)
  statsig.initialize().get()
  ```
</CodeGroup>

## FAQ

<AccordionGroup>
  <Accordion title="What Java versions are supported?">
    The Java Core SDK supports Java 8 and higher. Java 8 support was added in version 0.4.3.
  </Accordion>

  <Accordion title="Which platforms are supported?">
    The SDK supports:

    * Linux (x86\_64, arm64, musl variants)
    * macOS (x86\_64, arm64)
    * Windows (x86\_64)

    See the Tested Platforms section for verified Docker images.
  </Accordion>

  <Accordion title="Should I use the uber JAR or platform-specific JARs?">
    The uber JAR is recommended for most use cases as it includes native libraries for all popular platforms and simplifies deployment. Use platform-specific JARs only if you need to minimize JAR size or have specific dependency requirements.
  </Accordion>

  <Accordion title="How do I use this with Alpine Linux?">
    For Alpine Linux (musl-based systems), install compatibility packages:

    ```dockerfile  theme={null}
    RUN apk add --no-cache libgcc gcompat
    ```

    The SDK will automatically use musl-compatible native libraries.
  </Accordion>

  <Accordion title="How do I handle initialization in production?">
    The SDK initialization is asynchronous. Use `.get()` on the CompletableFuture to wait for initialization:

    ```java  theme={null}
    Statsig statsig = new Statsig("secret-key", options);
    statsig.initialize().get(); // Blocks until initialized
    ```

    Always call `shutdown()` when your application terminates to flush pending events.
  </Accordion>

  <Accordion title="Can I use multiple Statsig instances?">
    Yes, you can create multiple Statsig instances with different configurations. You can also use the global singleton with `Statsig.getGlobalSingleton()` for convenience.
  </Accordion>

  <Accordion title="How do I debug SDK issues?">
    Set the output logger level to DEBUG to see detailed logs:

    ```java  theme={null}
    StatsigOptions options = new StatsigOptions.Builder()
        .setOutputLoggerLevel(OutputLogger.LogLevel.DEBUG)
        .build();
    ```
  </Accordion>
</AccordionGroup>

## Reference

### FeatureGate Class

```java  theme={null}
class FeatureGate {
    String name;                      // Gate name
    boolean value;                    // Evaluation boolean result
    String ruleID;                    // Rule ID for this gate
    EvaluationDetails evaluationDetails; // Evaluation details
    String rawJson;                   // Raw JSON string representation
}
```

### Experiment Class

```java  theme={null}
class Experiment {
    String name;                      // Name of the experiment
    String ruleID;                    // ID of the rule used in the experiment
    Map<String, JsonElement> value;   // Configuration values specific to the experiment
    String groupName;                 // The group name the user falls into
    EvaluationDetails evaluationDetails; // Details about how the experiment was evaluated
    String rawJson;                   // Raw JSON representation of the experiment
}
```

**Methods for Experiment:**

```java  theme={null}
public String getString(String key, String fallbackValue)
public boolean getBoolean(String key, Boolean fallbackValue)
public double getDouble(String key, double fallbackValue)
public int getInt(String key, int fallbackValue)
public long getLong(String key, long fallbackValue)
public Object[] getArray(String key, Object[] fallbackValue)
public Map<String, Object> getMap(String key, Map<String, Object> fallbackValue)
```

### DynamicConfig Class

```java  theme={null}
class DynamicConfig {
    String name;                      // Name of the config
    String ruleID;                    // ID of the rule used
    Map<String, JsonElement> value;   // Configuration values
    EvaluationDetails evaluationDetails; // Details about how the config was evaluated
    String rawJson;                   // Raw JSON representation
}
```

**Methods for DynamicConfig:**

```java  theme={null}
public String getString(String key, String fallbackValue)
public boolean getBoolean(String key, Boolean fallbackValue)
public double getDouble(String key, double fallbackValue)
public int getInt(String key, int fallbackValue)
public long getLong(String key, long fallbackValue)
public Object[] getArray(String key, Object[] fallbackValue)
public Map<String, Object> getMap(String key, Map<String, Object> fallbackValue)
```

### Layer Class

```java  theme={null}
class Layer {
    String name;                      // Layer name
    String ruleID;                    // Rule ID for this layer
    String groupName;                 // Group name
    Map<String, JsonElement> value;   // Layer values
    String allocatedExperimentName;   // Allocated experiment name
    EvaluationDetails evaluationDetails; // Evaluation details
    String rawJson;                   // Raw JSON string representation
}
```

**Methods for Layer:**

```java  theme={null}
public String getString(String key, String fallbackValue)
public boolean getBoolean(String key, Boolean fallbackValue)
public double getDouble(String key, double fallbackValue)
public int getInt(String key, int fallbackValue)
public long getLong(String key, long fallbackValue)
public Object[] getArray(String key, Object[] fallbackValue)
public Map<String, Object> getMap(String key, Map<String, Object> fallbackValue)
```

### Fields Needed Methods (Enterprise Only)

<Info>
  This is available for Enterprise contracts. Please reach out to our support team, your sales contact, or via our [Slack community](https://statsig.com/slack) if you want this enabled.
</Info>

These methods allow you to retrieve a list of user fields that are used in the targeting rules for gates, configs, experiments, and layers.

```java  theme={null}
// Get user fields needed for a gate evaluation
List<String> getFieldsNeededForGate(String gateName)

// Get user fields needed for a dynamic config evaluation
List<String> getFieldsNeededForDynamicConfig(String configName)

// Get user fields needed for an experiment evaluation
List<String> getFieldsNeededForExperiment(String experimentName)

// Get user fields needed for a layer evaluation
List<String> getFieldsNeededForLayer(String layerName)
```

**Field Mapping**

The fields returned by these methods correspond to the following user properties:

```java  theme={null}
// Field mapping between user properties and internal field names
userID -> "u"
email -> "e"
ip -> "i"
userAgent -> "ua"
country -> "c"
locale -> "l"
appVersion -> "a"
time -> "t"
stableID -> "s"
environment -> "en"
targetApp -> "ta"

// Custom fields are prefixed with "cf:"
// Example: "cf:plan", "cf:age"
```


Built with [Mintlify](https://mintlify.com).