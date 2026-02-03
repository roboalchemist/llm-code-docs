# Source: https://docs.datadoghq.com/developers/ide_plugins/vscode.md

---
title: Datadog Extension for VS Code & Cursor
description: >-
  Integrate Datadog telemetry and insights into your source code in VS Code and
  other code editors.
breadcrumbs: >-
  Docs > Developers > Datadog IDE Plugins > Datadog Extension for VS Code &
  Cursor
---

# Datadog Extension for VS Code & Cursor

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com



{% alert level="danger" %}
The Datadog extension for Visual Studio Code is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site) ().
{% /alert %}


{% /callout %}

## Overview{% #overview %}

The Datadog extension for VS Code and Cursor brings Datadog to your code editor to accelerate your development.

{% image
   source="https://datadog-docs.imgix.net/images/developers/ide_plugins/vscode/datadog-vscode-3.8c4c5fcdbd039c2dbe27432da26f3267.png?auto=format"
   alt="Datadog extension for VS Code and Cursor" /%}

The extension includes these features:

- **Model Context Protocol (MCP) Server**: Connect the editor's AI agent to production telemetry, tools, and contexts from Datadog.

- **Log Annotations**: Gauge log volumes and search logs from your code.

- **Code Insights**: Stay informed about runtime errors, vulnerabilities, and flaky tests without leaving the code.

- **View in IDE**: Jump directly from code references in Datadog to your source files.

- **Static Code Analysis**: Detect and fix problems before you commit changes.

- **Exception Replay**: Debug your production code.

- **Fix in Chat**: Fix code errors, vulnerabilities, and flaky tests with AI-powered suggestions and explanations.

{% alert level="info" %}
Unless stated otherwise, all extension features are available for both VS Code and any other IDEs based on VS Code forks, such as Cursor.
{% /alert %}

## Requirements{% #requirements %}

- **Datadog account**: Most features require a Datadog account.

  - New to Datadog? [Learn more](https://www.datadoghq.com/) about Datadog's monitoring and security tools and sign up for a free trial.
  - If your organization uses a [custom sub-domain](https://docs.datadoghq.com/account_management/multi_organization/#custom-sub-domains) such as `myorg.datadoghq.com`, you must indicate it using the `datadog.connection.oauth.setup.domain` setting in the IDE.

- **Git**: The extension works better when Git is enabled in the IDE. Ensure this is enabled by checking the `git.enabled` setting.

## Installation{% #installation %}

Installation procedures may vary among other integrated development environments (IDEs).

{% tab title="VS Code" %}
Install the extension either directly in the IDE, or from the web:

- **In VS Code**: Open the Extensions view (`Shift` + `Cmd/Ctrl` + `X`), search for `datadog`, and select the official extension from Datadog.

- **From the web**: Install from the extension's page on [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=Datadog.datadog-vscode).

### MCP Server setup{% #mcp-server-setup %}

{% alert level="info" %}
The Datadog MCP Server is in Preview. Complete [this form](https://www.datadoghq.com/product-preview/datadog-mcp-server) to request access.
{% /alert %}

The extension includes access to the [Datadog Model Context Protocol (MCP) Server](https://docs.datadoghq.com/bits_ai/mcp_server/). Ensure the MCP Server is enabled to enhance the editor's AI capabilities with your specific Datadog environment:

1. Open the chat panel, select agent mode, and click the **Configure Tools** button.

   {% image
      source="https://datadog-docs.imgix.net/images/bits_ai/mcp_server/vscode_configure_tools_button.7aad216e77d1a7d4648e55299f613f04.png?auto=format"
      alt="Configure Tools button in VS Code" /%}

1. Find the Datadog server and tools in the list and check the boxes to enable them (expand or refresh if necessary).

{% /tab %}

{% tab title="Cursor" %}
Install the extension either directly in the IDE, or from the web:

- **In Cursor**: Open the Extensions view (`Shift` + `Cmd/Ctrl` + `X`), search for `datadog`, and select the official extension from Datadog.

- **From the web**: Download the VSIX file from [Open VSX Registry](https://open-vsx.org/extension/datadog/datadog-vscode), and install with `Extensions: Install from VSIX` in the command palette (`Shift` + `Cmd/Ctrl` + `P`).

### MCP Server setup{% #mcp-server-setup %}

{% alert level="info" %}
The Datadog MCP Server is in Preview. Complete [this form](https://www.datadoghq.com/product-preview/datadog-mcp-server) to request access.
{% /alert %}

The extension includes access to the [Datadog Model Context Protocol (MCP) Server](https://docs.datadoghq.com/bits_ai/mcp_server/). Ensure the MCP Server is enabled to enhance the editor's AI capabilities with your specific Datadog environment:

1. Go to **Cursor Settings** (`Shift` + `Cmd/Ctrl` + `J`), and select the **MCP** tab.
1. Find the Datadog server and turn on the toggle to enable it. A list of available tools is displayed (expand or refresh if necessary).

{% /tab %}

## Log annotations{% #log-annotations %}

Use **Log Annotations** to gauge the volume of logs generated by a given log line in your code. The extension adds annotations above your code to detected logging patterns that match log records in Datadog. Click an annotation to open the [Log Explorer](https://docs.datadoghq.com/logs/explorer/) in Datadog and view the matching logs.

{% video
   url="https://datadog-docs.imgix.net/images//developers/ide_plugins/vscode/logs_navigation.mp4" /%}

You can also search Datadog logs from within the IDE. Select any text in the code editor, then right-click and select **Datadog > Search Logs With Selected Text**.

{% image
   source="https://datadog-docs.imgix.net/images/developers/ide_plugins/vscode/log_search.0baaca20e4ba51ea77a1d4be99600772.png?auto=format"
   alt="Using the Datadog Log explorer feature" /%}

## Code insights{% #code-insights %}

**Code insights** keep you informed with Datadog-generated insights that are relevant to your code base:

- Runtime errors collected by [Error Tracking](https://docs.datadoghq.com/tracing/error_tracking/)
- Code and library vulnerabilities reported by [Code Security](https://docs.datadoghq.com/security/code_security/)
- Flaky tests detected by [Test Optimization](https://docs.datadoghq.com/tests/explorer/)

The extension identifies errors and vulnerabilities in the code with colored squiggles; hover over the line for more details.

{% video
   url="https://datadog-docs.imgix.net/images//developers/ide_plugins/vscode/code-insights-inline-hover.mp4" /%}

The **Code Insights** view in the Datadog sidebar lists all the issues found in the repository. Select an item to view the full insight, and use the links to jump to the related source code location or open the code insight in Datadog.

You can group code insights by kind, file, priority, or service. You can also ignore individual code insights and set filters to view the ones you're most interested in.

{% image
   source="https://datadog-docs.imgix.net/images/developers/ide_plugins/vscode/code-insights-2.cd9cbbf80e91d4be930f0706593da3e7.png?auto=format"
   alt="The Code Insights view." /%}

For specific insights about the file currently open in the active editor, check the **File Insights** view in the IDE's file explorer. This view also lists issues discovered by Static Code Analysis within the file.

{% video
   url="https://datadog-docs.imgix.net/images//developers/ide_plugins/vscode/file_insights_view.mp4" /%}

## View in IDE{% #view-in-ide %}

{% alert level="info" %}
This feature is only available for VS Code and Cursor. Other forks of VS Code are not supported.
{% /alert %}

The **View in VS Code** or **View in Cursor** feature provides a link from Datadog directly to your source files. Look for the button next to frames in stack traces displayed in the UI (for example, in [Error Tracking](https://docs.datadoghq.com/tracing/error_tracking/)):

{% image
   source="https://datadog-docs.imgix.net/images/developers/ide_plugins/vscode/view-in-vscode-2.e38c2373b437f01c847673b86bf8ec41.png?auto=format"
   alt="A stack trace in Datadog showing the View in VS Code button" /%}

You can also use this feature to open your source files from an insight (such as an error from Error Tracking):

{% image
   source="https://datadog-docs.imgix.net/images/developers/ide_plugins/vscode/view-in-vscode-error.e772031d2373555fe33be8e8c9a87a5e.png?auto=format"
   alt="An Error Tracking issue in the Datadog showing the View in VS Code button" /%}

{% alert level="info" %}
To use this feature, first configure [source code integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/) for your service.
{% /alert %}

## Static Code Analysis{% #static-code-analysis %}

[Static Code Analysis](https://docs.datadoghq.com/continuous_integration/static_analysis/?tab=githubactions) analyzes your code (locally) against predefined rules to detect and fix problems.

The extension runs Static Code Analysis rules on the source files you have open in your workspace. This allows you to detect and fix problems such as maintainability issues, bugs, or security vulnerabilities in the code before you commit your changes.

Static Code Analysis supports scanning for many programming languages. For a complete list, see [Static Code Analysis Rules](https://docs.datadoghq.com/security/code_security/static_analysis/static_analysis_rules/). For file types belonging to supported languages, issues are shown in the source code editor, and you can directly apply suggested fixes.

{% video
   url="https://datadog-docs.imgix.net/images//developers/ide_plugins/vscode/static_analysis.mp4" /%}

### Get started with Static Code Analysis{% #get-started-with-static-code-analysis %}

When you start editing a source file, the extension checks for [`static-analysis.datadog.yml`](https://docs.datadoghq.com/security/code_security/static_analysis/setup/) at your source repository's root. It prompts you to create it if necessary.

{% image
   source="https://datadog-docs.imgix.net/images/developers/ide_plugins/vscode/static-analysis-onboard.ef32fc573882fe234b1353ef48eaadfe.png?auto=format"
   alt="Onboarding banner for setting up Static Code Analysis with Python files" /%}

After you create the configuration file, the analyzer runs automatically in the background whenever you open a file. If you need to enable Static Code Analysis for a particular language, search for the command `Datadog: Configure Static Analysis Languages` in the command palette (`Shift` + `Cmd/Ctrl` + `P`).

You can also run a batch analysis for individual folders and even the entire workspace. In the IDE's file explorer view, right-click a folder and select **Datadog Static Analysis > Analyze Folder** or **Analyze Workspace**.

{% alert level="info" %}
Static Code Analysis does not require a Datadog account, as source files are analyzed locally.
{% /alert %}

## Exception Replay{% #exception-replay %}

**Exception Replay** allows you to inspect the stack trace frames of any Error Tracking code insight and get information about the values of the variables of the code running in production.

To access this feature, you must enable [Error Tracking Exception Replay](https://docs.datadoghq.com/tracing/error_tracking/exception_replay) on Datadog.

After the feature has been enabled, you can see an **Exception Replay** button next to the stack trace section of any instrumented Error Tracking code insight. Click the button to:

- Access all the information Datadog has about the different frames.
- Navigate through the production code.
- Review the value of the different variables involved.

Select an Error Tracking code insight from the Code Insights view. Go to the stack trace and click the Exception Replay button. The IDE shows a new activity with two new views:

- **Variables**: Displays the variables related to a particular stack trace frame.
- **Stack Trace**: Lists the stack frames for navigation.

Select a stack trace frame and inspect the values of all the variables that Datadog captured from your production code.

{% video
   url="https://datadog-docs.imgix.net/images//developers/ide_plugins/vscode/exception_replay.mp4" /%}

## Fix in Chat{% #fix-in-chat %}

The **Fix in Chat** button appears in several contexts when the extension identifies errors or issues. Click the button to generate an AI chat prompt that summarizes the problem, includes relevant details and context, and gives specific instructions for the agent.

{% video
   url="https://datadog-docs.imgix.net/images//developers/ide_plugins/vscode/cursor_fix_in_chat.mp4" /%}

## License{% #license %}

Read the [End-User License Agreement](https://www.datadoghq.com/legal/eula/) carefully before downloading or using this extension.

## Data and telemetry{% #data-and-telemetry %}

Datadog collects certain information about your usage of this IDE, including how you interact with it, whether errors occurred while using it, what caused those errors, and user identifiers in accordance with the [Datadog Privacy Policy](https://www.datadoghq.com/legal/privacy/) and Datadog's [VS Code extension EULA](https://www.datadoghq.com/legal/eula/). This data is used to help improve the extension's performance and features, including transitions to and from the extension and the applicable Datadog login page for accessing the Services.

If you don't wish to send this data to [Datadog](https://www.datadoghq.com/), you can disable this at any time in the extension's settings: `Datadog > Telemetry > Setup > Enable Telemetry` and select `disabled`.

{% alert level="info" %}
The Datadog extension also honors the [VS Code telemetry](https://code.visualstudio.com/docs/configure/telemetry#_output-channel-for-telemetry-events) setting.
{% /alert %}

## Help and feedback{% #help-and-feedback %}

To share your feedback, email [team-ide-integration@datadoghq.com](mailto:team-ide-integration@datadoghq.com) or create an issue in the extension's [public repository](https://github.com/DataDog/datadog-for-vscode).

Check out the [issues](https://github.com/DataDog/datadog-for-vscode/issues?q=is%3Aissue+label%3A%22known+issue%22) section to discover known issues.

Do you use [Cursor](https://www.cursor.com/), or another fork of VS Code? Find the extension on the [Open VSX Registry](https://open-vsx.org/extension/datadog/datadog-vscode).

## Further Reading{% #further-reading %}

- [Learn about Continuous Testing](https://docs.datadoghq.com/continuous_testing/)
- [Learn about Source Code Integration](https://docs.datadoghq.com/integrations/guide/source-code-integration/)
- [Learn about the Datadog Model Context Protocol (MCP) Server](https://docs.datadoghq.com/bits_ai/mcp_server/)
- [Reduce context switching while troubleshooting with Datadog's IDE plugins](https://www.datadoghq.com/blog/datadog-ide-plugins/)
- [Simplify production debugging with Datadog Exception Replay](https://www.datadoghq.com/blog/exception-replay-datadog/)
- [Debug live production issues with the Datadog Cursor extension](https://www.datadoghq.com/blog/datadog-cursor-extension/)
