# Source: https://docs.datadoghq.com/feature_flags/server/java.md

# Source: https://docs.datadoghq.com/security/code_security/software_composition_analysis/setup_runtime/compatibility/java.md

# Source: https://docs.datadoghq.com/security/code_security/iast/setup/compatibility/java.md

# Source: https://docs.datadoghq.com/security/code_security/iast/setup/java.md

# Source: https://docs.datadoghq.com/security/application_security/setup/gcp/cloud-run/java.md

# Source: https://docs.datadoghq.com/security/application_security/setup/aws/lambda/java.md

# Source: https://docs.datadoghq.com/security/application_security/setup/compatibility/java.md

# Source: https://docs.datadoghq.com/security/application_security/setup/java.md

# Source: https://docs.datadoghq.com/data_streams/setup/language/java.md

# Source: https://docs.datadoghq.com/profiler/profiler_troubleshooting/java.md

# Source: https://docs.datadoghq.com/profiler/enabling/java.md

# Source: https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/java.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/enabling/java.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dynamic_instrumentation/symdb/java.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/library_config/java.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/compatibility/java.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/opentracing/java.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/java.md

# Source: https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java.md

---
title: Tracing Java Applications
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > APM > Application Instrumentation > Add the Datadog Tracing Library >
  Tracing Java Applications
---

# Tracing Java Applications

## Compatibility requirements{% #compatibility-requirements %}

The latest Java Tracer supports all JVMs version 8 and higher. For additional information about JVM versions below 8, read [Supported JVM runtimes](https://docs.datadoghq.com/tracing/trace_collection/compatibility/java/#supported-jvm-runtimes).

For a full list of Datadog's Java version and framework support (including legacy and maintenance versions), read [Compatibility Requirements](https://docs.datadoghq.com/tracing/compatibility_requirements/java).

## Getting started{% #getting-started %}

Before you begin, make sure you've already [installed and configured the Agent](https://docs.datadoghq.com/tracing/trace_collection/automatic_instrumentation/?tab=datadoglibraries#install-and-configure-the-agent).

### Instrument your application{% #instrument-your-application %}

After you install and configure your Datadog Agent, the next step is to add the tracing library directly in the application to instrument it. Read more about [compatibility information](https://docs.datadoghq.com/tracing/compatibility_requirements/java).

To begin tracing your applications:

1. Download `dd-java-agent.jar` that contains the latest tracer class files, to a folder that is accessible by your Datadog user:

{% tab title="Wget" %}

```shell
wget -O dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'
```

{% /tab %}

{% tab title="cURL" %}

```shell
curl -Lo dd-java-agent.jar 'https://dtdg.co/latest-java-tracer'
```

{% /tab %}

{% tab title="Dockerfile" %}

```dockerfile
ADD 'https://dtdg.co/latest-java-tracer' dd-java-agent.jar
```

{% /tab %}

**Note:** To download the latest build of a specific **major** version, use the `https://dtdg.co/java-tracer-vX` link instead, where `X` is the desired major version. For example, use `https://dtdg.co/java-tracer-v1` for the latest version 1 build. Minor version numbers must not be included. Alternatively, see Datadog's [Maven repository](https://repo1.maven.org/maven2/com/datadoghq/dd-java-agent) for any specific version.

**Note**: Release Candidate versions are made available in GitHub [DataDog/dd-trace-java releases](https://github.com/DataDog/dd-trace-java/releases). These have "RC" in the version and are recommended for testing outside of your production environment. You can [subscribe to GitHub release notifications](https://docs.github.com/en/account-and-profile/managing-subscriptions-and-notifications-on-github/managing-subscriptions-for-activity-on-github/viewing-your-subscriptions) to be informed when new Release Candidates are available for testing. If you experience any issues with Release Candidates, reach out to [Datadog support](https://docs.datadoghq.com/getting_started/support/).

To run your app from an IDE, Maven or Gradle application script, or `java -jar` command, with the Continuous Profiler, deployment tracking, and logs injection (if you are sending logs to Datadog), add the `-javaagent` JVM argument and the following configuration options, as applicable:

```text
java -javaagent:/path/to/dd-java-agent.jar -Ddd.profiling.enabled=true -Ddd.logs.injection=true -Ddd.service=my-app -Ddd.env=staging -Ddd.version=1.0 -jar path/to/your/app.jar
```

**Note**: If you have a strong need to reduce the size of your image and omit modules, you can use the [`jdeps`](https://docs.oracle.com/en/java/javase/11/tools/jdeps.html) command to identify dependencies. However, required modules can change over time, so do this at your own risk.

**Note**: When running the tracer with Java 24+, you may see warnings related to JNI native access. Suppress these warnings by adding the `--enable-native-access=ALL-UNNAMED` flag. See [JEP 472](https://openjdk.org/jeps/472) for more details.

{% alert level="warning" %}
Enabling profiling may impact your bill depending on your APM bundle. See the [pricing page](https://docs.datadoghq.com/account_management/billing/apm_tracing_profiler/) for more information.
{% /alert %}

| Environment Variable      | System Property           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------- | ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DD_ENV`                  | `dd.env`                  | Your application environment (`production`, `staging`, etc.)                                                                                                                                                                                                                                                                                                                                                                                    |
| `DD_LOGS_INJECTION`       | `dd.logs.injection`       | Enable automatic MDC key injection for Datadog trace and span IDs. See [Advanced Usage](https://docs.datadoghq.com/tracing/other_telemetry/connect_logs_and_traces/java/) for details.Starting in version 1.18.3, if [Agent Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) is enabled where this service runs, you can set `DD_LOGS_INJECTION` in the [Software Catalog](https://app.datadoghq.com/services) UI. |
| `DD_PROFILING_ENABLED`    | `dd.profiling.enabled`    | Enable the [Continuous Profiler](https://docs.datadoghq.com/profiler/)                                                                                                                                                                                                                                                                                                                                                                          |
| `DD_SERVICE`              | `dd.service`              | The name of a set of processes that do the same job. Used for grouping stats for your application.                                                                                                                                                                                                                                                                                                                                              |
| `DD_TRACE_SAMPLE_RATE`    | `dd.trace.sample.rate`    | Set a sampling rate at the root of the trace for all services.Starting in version 1.18.3, if [Agent Remote Configuration](https://docs.datadoghq.com/tracing/guide/remote_config) is enabled where this service runs, you can set `DD_TRACE_SAMPLE_RATE` in the [Software Catalog](https://app.datadoghq.com/services) UI.                                                                                                                      |
| `DD_TRACE_SAMPLING_RULES` | `dd.trace.sampling.rules` | Set a sampling rate at the root of the trace for services that match the specified rule.                                                                                                                                                                                                                                                                                                                                                        |
| `DD_VERSION`              | `dd.version`              | Your application version (for example, `2.5`, `202003181415`, or `1.3-alpha`)                                                                                                                                                                                                                                                                                                                                                                   |

Additional configuration options are described below.

### Add the Java Tracer to the JVM{% #add-the-java-tracer-to-the-jvm %}

Use the documentation for your application server to figure out the right way to pass in `-javaagent` and other JVM arguments. Here are instructions for some commonly used frameworks:

{% tab title="Spring Boot" %}
If your app is called `my_app.jar`, create a `my_app.conf`, containing:

```text
JAVA_OPTS=-javaagent:/path/to/dd-java-agent.jar
```

For more information, see the [Spring Boot documentation](https://docs.spring.io/spring-boot/docs/current/reference/html/deployment.html#deployment-script-customization-when-it-runs).
{% /tab %}

{% tab title="Tomcat" %}
#### Linux{% #linux %}

To enable tracing when running Tomcat on Linux:

1. Open your Tomcat startup script file, for example `setenv.sh`.
1. Add the following to `setenv.sh`:
   ```text
   CATALINA_OPTS="$CATALINA_OPTS -javaagent:/path/to/dd-java-agent.jar"
   ```

#### Windows (Tomcat as a Windows service){% #windows-tomcat-as-a-windows-service %}

To enable tracing when running Tomcat as a Windows service:

1. Open the "tomcat@VERSION_[MAJOR@w.exe](mailto:MAJOR@w.exe)" maintenance utility located in the `./bin` directory of the Tomcat project folder.
1. Navigate to the **Java** tab, and add the following to `Java Options`:

```text
-javaagent:C:\path\to\dd-java-agent.jar
```
Restart your Tomcat services for changes to take effect.
{% /tab %}

{% tab title="JBoss" %}

- In standalone mode:

Add the following line to the end of `standalone.conf`:

```text
JAVA_OPTS="$JAVA_OPTS -javaagent:/path/to/dd-java-agent.jar"
```

- In standalone mode and on Windows, add the following line to the end of `standalone.conf.bat`:

```text
set "JAVA_OPTS=%JAVA_OPTS% -javaagent:X:/path/to/dd-java-agent.jar"
```

- In domain mode:

Add the following line in the file `domain.xml`, under the tag server-groups.server-group.jvm.jvm-options:

```text
<option value="-javaagent:/path/to/dd-java-agent.jar"/>
```

For more details, see the [JBoss documentation](https://access.redhat.com/documentation/en-us/red_hat_jboss_enterprise_application_platform/7.0/html/configuration_guide/configuring_jvm_settings).
{% /tab %}

{% tab title="Jetty" %}
If you use `jetty.sh` to start Jetty as a service, edit it to add:

```text
JAVA_OPTIONS="${JAVA_OPTIONS} -javaagent:/path/to/dd-java-agent.jar"
```

If you use `start.ini` to start Jetty, add the following line (under `--exec`, or add `--exec` line if it isn't there yet):

```text
-javaagent:/path/to/dd-java-agent.jar
```

{% /tab %}

{% tab title="WebSphere" %}
In the administrative console:

1. Select **Servers**. Under **Server Type**, select **WebSphere application servers** and select your server.
1. Select **Java and Process Management > Process Definition**.
1. In the **Additional Properties** section, click **Java Virtual Machine**.
1. In the **Generic JVM arguments** text field, enter:

```text
-javaagent:/path/to/dd-java-agent.jar
```

For additional details and options, see the [WebSphere docs](https://www.ibm.com/support/pages/setting-generic-jvm-arguments-websphere-application-server).
{% /tab %}

**Note**

- If you're adding the `-javaagent` argument to your `java -jar` command, it needs to be added *before* the `-jar` argument, as a JVM option, not as an application argument. For example:

  ```text
  java -javaagent:/path/to/dd-java-agent.jar -jar my_app.jar
  ```

For more information, see the [Oracle documentation](https://docs.oracle.com/javase/7/docs/technotes/tools/solaris/java.html).

- Never add `dd-java-agent` to your classpath. It can cause unexpected behavior.

## Automatic instrumentation{% #automatic-instrumentation %}

Automatic instrumentation for Java uses the `java-agent` instrumentation capabilities [provided by the JVM](https://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html). When a `java-agent` is registered, it can modify class files at load time.

**Note:** Classes loaded with remote ClassLoader are not instrumented automatically.

Instrumentation may come from auto-instrumentation, the OpenTracing API, or a mixture of both. Instrumentation generally captures the following info:

- Timing duration is captured using the JVM's NanoTime clock unless a timestamp is provided from the OpenTracing API
- Key/value tag pairs
- Errors and stack traces which are unhandled by the application
- A total count of traces (requests) flowing through the system

## Configuration{% #configuration %}

If needed, configure the tracing library to send application performance telemetry data as you require, including setting up Unified Service Tagging. Read [Library Configuration](https://docs.datadoghq.com/tracing/trace_collection/library_config/java/) for details.

### Remote configuration{% #remote-configuration %}

Remote Configuration allows the Datadog Agent to dynamically configure tracing settings without requiring application restarts. By default, Remote Configuration is enabled. To disable it, set the environment variable:

```
DD_REMOTE_CONFIG_ENABLED=false
```

Or add the JVM system property:

```
-Ddd.remote_config.enabled=false
```

## Further Reading{% #further-reading %}

- [Datadog Java APM source code](https://github.com/DataDog/dd-trace-java)
- [Explore your services, resources, and traces](https://docs.datadoghq.com/tracing/glossary/)
