# Source: https://docs.confluent.io/cloud/current/client-apps/vs-code-extension.md

<a id="cc-vscode-extension"></a>

# Confluent for VS Code for Confluent Cloud

<!-- WARNING: THIS IS A SHARED FILE AND THE SOURCE IS LOCATED IN DOCS-COMMON. DO NOT ADD TO ANY OTHER REPO. -->

Confluent for VS Code makes it easy for you to build stream processing
applications using Confluent technology. This extension provides a robust,
delightful experience for Confluent Cloud and Confluent Platform features from within the
[Visual Studio Code (VS Code)](https://code.visualstudio.com) editor desktop
environment.

Confluent for VS Code is open-source and is available in
[this GitHub repo](https://github.com/confluentinc/vscode).

<!-- Visit the [Confluent Developer site](https://developer.confluent.io/) for more about developing with -->
<!-- Confluent, and read the docs at the [Confluent documentation](docs.confluent.io) site. -->

<a id="vscode-installation"></a>

## Installation

### From the VS Code Extension Marketplace

In your browser, go to the
[VS Code Marketplace](https://marketplace.visualstudio.com)
to view, download, and install
[Confluent for VS Code](https://marketplace.visualstudio.com/items?itemName=confluentinc.vscode-confluent).

### From within VS Code

1. Open VS Code.
2. In the Activity Bar, click **Extensions** (Cmd+Shift+X/Ctrl+Shift+X).
3. In the **Extensions** view, search for âConfluentâ.
4. Click **Install**.

#### From a VSIX file

Confluent provides these VSIX files via
[GitHub releases](https://github.com/confluentinc/vscode/releases):

- MacOS with Apple Silicon: `vscode-confluent-darwin-arm64-x.x.x.vsix`
- MacOS with Intel processors: `vscode-confluent-darwin-x64-x.x.x.vsix`
- Linux on ARM-64 processors: `vscode-confluent-linux-arm64-x.x.x.vsix`
- Linux on x86 processors: `vscode-confluent-linux-x64-x.x.x.vsix`
- Windows on x64 processors: `vscode-confluent-windows-x64-x.x.x.vsix`

Replace `x.x.x`  with the actual version number you want to use.

You can install Confluent for VS Code from a VSIX file by using the
VS Code UI or by using the `code --install-extension` command in the terminal.

To install by using the UI, follow these steps:

1. Download the VSIX file appropriate for your machine.
2. Open VS Code, and in the Activity Bar, click **Extensions**.
3. At the top of the **Extensions** view, click **â¦**, and in the context
   menu, click **Install
   from VSIXâ¦**
4. Navigate to your downloaded `vscode-confluent-vX.X.X.vsix` file and click
   **Install**.

To install in the terminal, run the following command:

```bash
code --install-extension /path/to/vscode-confluent-vX.X.X.vsix
```

## Features

Confluent for VS Code provides a number of features for working with
Kafka clusters, Schema registries, and Confluent Cloud for Apache FlinkÂ®.

### Smart Project Templates

Confluent for VS Code offers Smart Project Templates that accelerate project
setup by providing ready-to-use templates tailored for common development
patterns. Examples include client applications for various programming
languages, Kafka Streams applications, and Flink Table API apps. These templates
enable you to quickly launch new projects with minimal configuration,
significantly reducing setup time.

You can access them through the Command Palette or from the
**Generate Project from Template** action in the **Help Center** panel.

These templates incorporate best practices to help teams maintain high
standards and avoid repetitive setup tasks so you can focus on building and
innovating.

### Command Palette

Most of the features are available in the VS Code Command Palette. Press
Cmd+Shift+P/Ctrl+Shift+P and type âconfluentâ to show the Confluent commands.

Some commands are associated with view actions, which are the simple buttons,
usually icons. next to items in the Activity Bar. For example, **play** (open
Message Viewer and start consuming messages), **sync** (refresh), and
**ellipsis** (extra actions) are all view actions associated with commands
available in the Command Palette.

### Activity Bar

In the Activity Bar, click the Confluent logo to open the extension and show the
following sections.

### Connect to your streams

Confluent for VS Code supports connecting to Confluent Cloud, connecting to any other
Kafka cluster using the Kafka native protocol, and working with local Kafka and
Schema Registry containers running in Docker:

- To connect to Confluent Cloud, click the âSign in to Confluent Cloudâ icon next to
  **Confluent Cloud** in the **Resources** view.
- To connect to Kafka clusters or schema registries by using the native APIs,
  click the **+** icon in the **Resources** view.
- To run Confluent Platform Docker images, click the âplayâ icon next to **Local** in the
  **Resources** view.

### Resources

The **Resources** view lists Confluent Cloud environments and associated resources,
like Kafka clusters and schema registries, and Flink compute pools. It also
provides access to Kafka clusters and schema registries from Local or Direct
connections.

- Click a Kafka cluster to load the topics created in that cluster in the
  **Topics** view.
- Click a Schema Registry cluster to load the associated schemas for that registry in the
  **Schemas** view.
- Click a Flink compute pool to load the Flink SQL statements in that pool in
  the **Flink Statements** view.

### Topics

Click the **play** icon next to the topic name to open the **Message Viewer**,
which enables searching and exploring messages in a topic. Within Message
Viewer, you can:

- page through and search for specific values within the list of all the
  messages
- double-click a single message to explore its entire payload encoded in JSON
- pause and resume consuming at any time
- see aggregate counts of messages over time from the histogram view and brush
  to filter messages by timestamp
- toggle partitions on and off to show and hide messages from specific
  partitions

### Schemas

The **Schemas** view displays all the schemas available for the current Confluent Cloud
environmentâs Schema Registry.  Also, schemas are shown in the **Topics** view by expanding
a topic item if they match the
[TopicNameStrategy](/platform/current/schema-registry/fundamentals/serdes-develop/index.html#overview),
and you have the appropriate permissions.

You can view schema definitions by expanding the schema subject to see a
specific schema version and clicking the **View Schema** icon.

### Flink

The **Flink Statements** view displays all Flink SQL statements available for
the selected Flink compute pool in Confluent Cloud. Click on a Flink statement to view
its definition in an editor. View the results of a Flink statement by clicking
on the âView Flink Statement Resultsâ icon next to the statement name in the
**Flink Statements** view.

The **Flink Database** view displays these resources in a selected Flink
database (or Kafka cluster):

- AI Agents
- AI Models
- AI Tools
- Artifacts
- Connections
- UDFs
- Tables and views

You can also use the **Flink Database** view to create and upload new artifacts,
and to register them as UDFs with a selected Flink database.

### Help Center

The **Help Center** panel provides links to the extension walkthrough, issue
reporting, general feedback, and options to generate Kafka projects by using
a template.

## Outputs

Once Confluent for VS Code is activated, you can view extension logs in these
separate Output Channels:

- **Confluent:** logs for the VS Code extension itself
- **Confluent (Sidecar):** logs from the
  [Sidecar process](https://github.com/confluentinc/ide-sidecar)
- **Confluent Flink SQL Language Server:** logs from the language server for Flink SQL

## Telemetry

Gathering usage and error data helps Confluent develop a more resilient and
user-friendly application. Confluent enables telemetry only in official
production releases. Confluent respects your preferences for sending
telemetry data. If you have turned off telemetry in your VS Code settings, the
extension doesnât send any events or data.

### Segment for user actions

The extension uses [Segment](https://segment.com) to log extension usage.
See [telemetry.ts](https://github.com/confluentinc/vscode/blob/main/src/telemetry.ts)
for implementation and how it is used in the codebase. The
extension sends events when you perform major actions in the extension, such as
using any of the registered commands. This helps Confluent see what commands
are popular and helps to answer other questions about how the extension is
used, so Confluent can make it even more useful.

### Sentry for error tracing

The extension uses [Sentry](https://sentry.io) to capture and analyze
errors, which enables more robust and friendly error debugging. It is the first
item initialized in
[extension.ts](https://github.com/confluentinc/vscode/blob/main/src/extension.ts),
so it can send any uncaught exceptions globally, and itâs invoked in certain
catch blocks to send specific errors. The Sentry rollup-plugin is used to
upload source maps.

## Known limitations

- Confluent Cloud connections require reauthenticating after four hours, and you will
  be prompted to reauthenticate.
- Preview links for non-default organizations work only after switching to the
  non-default organization in the Confluent Cloud Console in your browser.

For open issues and feature ideas, see
[issues](https://github.com/confluentinc/vscode/issues) in the repo.

## Support

To report an issue, within VS Code, open the **Help Center** panel in the
extension and click **Report an issue**.

If you have questions, comments, or you run into any issues, feel free to post
a message in a GitHub [discussion](https://github.com/confluentinc/vscode/discussions)
or create an [issue](https://github.com/confluentinc/vscode/issues).

For general feedback, fill out and submit the
[survey](https://www.surveymonkey.com/r/NYVKQD6).

<a id="cc-vscode-extension-login"></a>

## Log in to Confluent Cloud

1. Install [Confluent for VS Code for Confluent Cloud](#cc-vscode-extension).
2. In the VS Code Activity Bar, click the Confluent icon. If you have
   many extensions installed, you may need to click **â¦** to access
   **Additional Views** and select **Confluent** from the context menu.
3. In the Side Bar, click **Connect to Confluent Cloud**, and in the
   permission dialog, click **Allow**.

   The web browser opens to the Confluent Cloud login page.
4. Enter your credentials and click **Log in**.

   The web browser shows the **Authentication Complete** page.
5. Return to VS Code and confirm that your Confluent Cloud resources are
   displayed in the Side Bar.

## Related content

- [Kafka IntelliJ IDEA Plugin](kafka-plugin-for-jetbrains-ides.md#cc-intellij-idea-plugin)
- [Quick Start for Confluent Cloud](../get-started/index.md#cloud-quickstart)
- [Client Applications](overview.md#client-overview)

#### NOTE
This website includes content developed at the [Apache Software Foundation](https://www.apache.org/)
under the terms of the [Apache License v2](https://www.apache.org/licenses/LICENSE-2.0.html).
