Source: https://docs.slack.dev/tools/java-slack-sdk/reference

# Reference

The table below shows all of the available modules in the Java Slack SDK. All of them have the same latest version as we release at the same time, even in the case that some don't have any changes apart from updates on their dependency side.

All released versions are available on the Maven Central repositories. The latest version is `1.48.0`.

## Bolt & Built-in Extensions {#bolt--built-in-extensions}

groupId:artifactId

Javadoc

Description

[`com.slack.api:bolt`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt/1.48.0/bolt-1.48.0-javadoc.jar/!/index.html#package)

Bolt is a framework that offers an abstraction layer to build Slack apps safely and quickly.

[`com.slack.api:bolt-socket-mode`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-socket-mode)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-socket-mode/1.48.0/bolt-socket-mode-1.48.0-javadoc.jar/!/index.html#package)

This module offers a handy way to run Bolt apps through [Socket Mode](/apis/events-api/using-socket-mode) connections.

[`com.slack.api:bolt-jakarta-socket-mode`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jakarta-socket-mode)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jakarta-socket-mode/1.48.0/bolt-jakarta-socket-mode-1.48.0-javadoc.jar/!/index.html#package)

This module offers a handy way to run Bolt apps through [Socket Mode](/apis/events-api/using-socket-mode) connections (Jakarta EE compatible).

[`com.slack.api:bolt-servlet`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-servlet)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-servlet/1.48.0/bolt-servlet-1.48.0-javadoc.jar/!/index.html)

This module offers a handy way to run Bolt apps on the Java EE Servlet environments.

[`com.slack.api:bolt-jetty`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jetty)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jetty/1.48.0/bolt-jetty-1.48.0-javadoc.jar/!/index.html)

This module offers a handy way to run Bolt apps on the [Java EE compatible Jetty HTTP server (9.x)](https://www.eclipse.org/jetty/).

[`com.slack.api:bolt-jakarta-servlet`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jakarta-servlet)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jakarta-servlet/1.48.0/bolt-jakarta-servlet-1.48.0-javadoc.jar/!/index.html)

This module offers a handy way to run Bolt apps on the Jakarta EE Servlet environments.

[`com.slack.api:bolt-jakarta-jetty`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-jakarta-jetty)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-jakarta-jetty/1.48.0/bolt-jakarta-jetty-1.48.0-javadoc.jar/!/index.html)

This module offers a handy way to run Bolt apps on the [Jakarta EE compatible Jetty HTTP server](https://www.eclipse.org/jetty/).

[`com.slack.api:bolt-aws-lambda`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-aws-lambda)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-aws-lambda/1.48.0/bolt-aws-lambda-1.48.0-javadoc.jar/!/index.html)

This module offers a handy way to run Bolt apps on AWS [API Gateway](https://aws.amazon.com/api-gateway/) + [Lambda](https://aws.amazon.com/lambda/).

[`com.slack.api:bolt-google-cloud-functions`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-google-cloud-functions)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-google-cloud-functions/1.48.0/bolt-google-cloud-functions-1.48.0-javadoc.jar/!/index.html)

This module offers a handy way to run Bolt apps on [Google Cloud Functions](https://cloud.google.com/functions).

[`com.slack.api:bolt-micronaut`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-micronaut)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-micronaut/1.48.0/bolt-micronaut-1.48.0-javadoc.jar/!/index.html)

This is an adapter for [Micronaut](https://micronaut.io/) to run Bolt apps on top of it.

[`com.slack.api:bolt-helidon`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-helidon)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-helidon/1.48.0/bolt-helidon-1.48.0-javadoc.jar/!/index.html)

This is an adapter for [Helidon SE](https://helidon.io/docs/latest/) to run Bolt apps on top of it.

[`com.slack.api:bolt-http4k`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-http4k)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-http4k/1.48.0/bolt-http4k-1.48.0-javadoc.jar/!/index.html)

This is an adapter for [http4k](https://http4k.org/) to run Bolt apps on top of any of the multiple server backends that the library supports.

[`com.slack.api:bolt-ktor`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:bolt-ktor)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/bolt-ktor/1.48.0/bolt-ktor-1.48.0-javadoc.jar/!/index.html)

This is an adapter for [Ktor](https://ktor.io/) to run Bolt apps on top of it.

## Foundation Modules {#foundation-modules}

groupId:artifactId

Javadoc

Description

[`com.slack.api:slack-api-model`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-model)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-model/1.48.0/slack-api-model-1.48.0-javadoc.jar/!/index.html)

This is a collection of the classes representing the [Slack core objects](/reference/objects) such as conversations, messages, users, blocks, and surfaces. As this is an essential part of the SDK, all other modules depend on this.

[`com.slack.api:slack-api-model-kotlin-extension`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-model-kotlin-extension)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-model-kotlin-extension/1.48.0/slack-api-model-kotlin-extension-1.48.0-javadoc.jar/!/index.html)

This contains the Block Kit Kotlin DSL builder, which allows you to define block kit structures via a Kotlin-native DSL.

[`com.slack.api:slack-api-client`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-client)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-client/1.48.0/slack-api-client-1.48.0-javadoc.jar/!/index.html)

This is a collection of the Slack API clients. The supported are Basic API Methods, Socket Mode API, RTM API, SCIM API, Audit Logs API, and Status API.

[`com.slack.api:slack-api-client-kotlin-extension`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-api-client-kotlin-extension)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-api-client-kotlin-extension/1.48.0/slack-api-client-kotlin-extension-1.48.0-javadoc.jar/!/index.html)

This contains extension methods for various slack client message builders so you can seamlessly use the Block Kit Kotlin DSL directly on the Java message builders.

[`com.slack.api:slack-jakarta-socket-mode-client`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-jakarta-socket-mode-client)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-jakarta-socket-mode-client/1.48.0/slack-jakarta-socket-mode-client-1.48.0-javadoc.jar/!/index.html)

This is an option to switch to Jakarta EE compatible Socket Mode client.

[`com.slack.api:slack-app-backend`](https://search.maven.org/search?q=g:com.slack.api%20AND%20a:slack-app-backend)

[Javadoc](https://oss.sonatype.org/service/local/repositories/releases/archive/com/slack/api/slack-app-backend/1.48.0/slack-app-backend-1.48.0-javadoc.jar/!/index.html)

This module is a set of Slack app server-side handlers and data classes for Events API, Interactive Components, Slash Commands, Actions, and OAuth flow. These are used by Bolt framework as the foundation of it in primitive layers.
