# Source: https://maven.apache.org/extensions/index.html

Title: Available Extensions – Maven

URL Source: https://maven.apache.org/extensions/index.html

Markdown Content:
[](https://maven.apache.org/extensions/index.html)
Maven is - at its heart - a plugin execution framework; most work is done by plugins. However, with extensions it is possible to hook into Maven, e.g. to manipulate the lifecycle.

* [Configure Extensions](https://maven.apache.org/guides/mini/guide-using-extensions.html)
* [Write Extensions](https://maven.apache.org/examples/maven-3-lifecycle-extensions.html)

[](https://maven.apache.org/extensions/index.html)
Maintained By The Maven Project[](https://maven.apache.org/extensions/index.html#maintained-by-the-maven-project)
-----------------------------------------------------------------------------------------------------------------

| Extension | Version | Release Date | Description | Source Repository | Issue Tracker |
| --- | --- | --- | --- | --- | --- |
| [Build Cache](https://maven.apache.org/extensions/maven-build-cache-extension/) | 1.2.2 | 2026-01-27 | Maven Incremental Build and Cache (local and remote). | [Git](https://gitbox.apache.org/repos/asf/maven-build-cache-extension.git) / [GitHub](https://github.com/apache/maven-build-cache-extension/) | [GitHub Issues](https://github.com/apache/maven-build-cache-extension/issues) |
| [Enforcer](https://maven.apache.org/enforcer/maven-enforcer-extension/) | 3.5.0 | 2024-05-26 | Environmental constraint checking (Maven Version, JDK etc), User Custom Rule Execution. | [Git](https://gitbox.apache.org/repos/asf/maven-enforcer.git) / [GitHub](https://github.com/apache/maven-enforcer/) | [GitHub Issues](https://github.com/apache/maven-enforcer/issues) |
[](https://maven.apache.org/extensions/index.html)
Outside The Maven Land[](https://maven.apache.org/extensions/index.html#outside-the-maven-land)

-----------------------------------------------------------------------------------------------

A number of other projects provide their own Maven extensions. This includes:

[](https://maven.apache.org/extensions/index.html)

### Open Source[](https://maven.apache.org/extensions/index.html#open-source)

| Extension | Maintainer | Description |
| --- | --- | --- |
| [notifier](https://github.com/jcgay/maven-notifier) | Jean-Christophe Gay | A status notification will be send at the end of a Maven build. |
| [polyglot](https://github.com/takari/polyglot-maven) | Takari | Polyglot for Maven is a set of extensions that allows the POM model to be written in dialects other than XML. |
| [profiler](https://github.com/jcgay/maven-profiler) | Jean-Christophe Gay | A time execution recorder for Maven which log time taken by each mojo in your build lifecycle. |
| [profiler](https://github.com/takari/maven-profiler) | Takari | The Tesla profiler is a simple EventSpy implementation that gathers timing information. |
| [smart-builder](https://github.com/takari/takari-smart-builder) | Takari | The Takari Smart Builder is a replacement scheduling projects builds in a Maven multi-module build. |
| [opentelemetry-maven-extension](https://github.com/open-telemetry/opentelemetry-java-contrib/tree/main/maven-extension) | The OpenTelemetry project | The OpenTelemetry Maven Extension instruments builds to gather execution details as traces for build performance optimization and for troubleshooting. OpenTelemetry traces can be visualized in open source observability solutions such as [Jaeger Tracing](https://www.jaegertracing.io/) as well as in commercial solutions. |
[](https://maven.apache.org/extensions/index.html)

### Commercial[](https://maven.apache.org/extensions/index.html#commercial)

| Extension | Maintainer | Description |
| --- | --- | --- |
| [Develocity](https://docs.gradle.com/develocity/maven-extension/) | Gradle Inc. | Captures Maven build insights that can be viewed for free on [scans.gradle.com](https://gradle.com/scans/maven/). Provides local and remote build caching, distributed test execution and predictive test selection for Maven builds connected to a Develocity installation. |
