# Source: https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started

Title: React Agentic UI Generator Getting Started - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started

Markdown Content:
New to KendoReact?[Start a free 30-day trial](https://www.telerik.com/try/kendo-react-ui)

[Getting Started with the Agentic UI Generator Premium](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#getting-started-with-the-agentic-ui-generator)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Updated

on Feb 27, 2026

The Agentic UI Generator is an intelligent development tool delivered through the [KendoReact MCP server](https://www.npmjs.com/package/@progress/kendo-react-mcp) that enables UI generation from natural language prompts. It includes a comprehensive orchestrator that coordinates five specialized assistants working together to deliver complete, beautiful, on-brand, and enterprise-ready UIs.

This article describes how to install and use the KendoReact Agentic UI Generator in AI-powered IDEs like Visual Studio Code and Cursor.

[Quick Start](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#quick-start)
--------------------------------------------------------------------------------------------------------------------------

> If you have already completed the [Installation Guide](https://www.telerik.com/kendo-react-ui/components/ai-tools/installation) and configured your license key, skip directly to **step 3** to start using the Agentic UI Generator.

Follow these steps to set up the Agentic UI Generator:

1.   To add the MCP server to your IDE, create an `mcp.json` file in your workspace. For Visual Studio Code, use the following configuration to `.vscode/mcp.json`:

json 
```
{
    "servers": {
        "kendo-react-mcp-server": {
            "type": "stdio",
            "command": "npx",
            "args": ["-y", "@progress/kendo-react-mcp@latest"]
            // set an `env` parameter only if you haven't set a license key globally on your machine
            //   "env": {
            //     "TELERIK_LICENSE_PATH": "THE_PATH_TO_YOUR_LICENSE_FILE"
            //   }
        }
    }
}
``` 
The server name `kendo-react-mcp-server` can be customized as desired. The name helps distinguish the MCP server in your configuration and does not affect how you invoke the Agentic UI Generator tool in your prompt.

> For IDE-specific setup instructions and advanced configuration options, see [MCP Server Configuration](https://www.telerik.com/kendo-react-ui/components/ai-tools/installation#mcp-server-configuration).

2.   Ensure you have a [supported license](https://www.telerik.com/kendo-react-ui/components/ai-tools#license-requirements) and set up your Telerik license key globally on your machine or in the `mcp.json` configuration. The server automatically recognizes and your license and activates the available MCP tools.

> Refer to the [License Key Setup](https://www.telerik.com/kendo-react-ui/components/ai-tools/installation#license-key-setup) section for detailed instructions.

3.   Open the AI chat interface of your IDE and start your prompt with the `#kendo_ui_generator` handle to invoke the Agentic UI Generator orchestrator:

prompt `#kendo_ui_generator Create a dashboard page with a grid showing sales data and a chart visualizing monthly trends.` 

[Using the Agentic UI Generator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#using-the-agentic-ui-generator)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

Once installed, start a new chat session in your IDE to begin interacting with the Agentic UI Generator via natural language prompts. The Agentic UI Generator can be used in two primary modes: basic usage through [the Agentic UI Generator orchestrator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#call-the-agentic-ui-generator), or advanced usage by [calling specific MCP assistants directly](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#target-the-assistants-advanced).

### [Call the Agentic UI Generator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#call-the-agentic-ui-generator)

1.   Open the AI chat interface in your IDE—Start a new chat session to begin interacting with the Agentic UI Generator.
2.   Start your prompt with the `#kendo_ui_generator` handle—this invokes the orchestrator tool that uses an agentic flow to analyze and process your request. 
> Using the `#kendo_ui_generator` handle ensures the Agentic UI Generator is called. Alternatively, you can use natural language without the handle. Make sure to mention the "kendo" keyword in your natural language prompt, so that the AI model can automatically recognize when to call the generator.

3.   Inspect the output and verify that the `kendo-react-mcp-server` MCP server (or the one with your custom server name) is called. Look for a similar statement in the output:

![Image 1: MCP Server uses Kendo UI Generator in VS Code](https://www.telerik.com/kendo-react-ui/components/assets/5f5b2cdd3605b588c7c4c550ff7cb4a2/generator-confirmation.png)

1.   If prompted, grant the MCP server permission to run for this session, workspace, or always.

### [Target the Assistants (Advanced)](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#target-the-assistants-advanced)

For more precise control over the generation process, you can invoke the specialized assistants individually using their dedicated handles. Each assistant focuses on a specific aspect of UI development:

| Assistant | Handle | Purpose |
| --- | --- | --- |
| **Layout Assistant** | `#kendo_layout_assistant` | Applies suitable [CSS utility classes](https://www.telerik.com/design-system/docs/utils/get-started/introduction/) from the Progress Design System for styling and positioning elements. Use this assistant when you need help with spacing, typography, colors, layout structure, or transforms. |
| **Component Assistant** | `#kendo_component_assistant` | Answers questions and generates code related to KendoReact components. Use this assistant when you need to implement or configure specific KendoReact components like Grid, Charts, Forms, etc. |
| **Styling Assistant** | `#kendo_style_assistant` | Generates custom styles and theme configurations for your application. Use this assistant when you need to apply brand-specific colors, create custom themes, or modify the overall visual design of your UI. |
| **Icon Assistant** | `#kendo_icon_assistant` | Searches and retrieves icons from the [Progress Design System iconography](https://www.telerik.com/design-system/docs/foundation/iconography/icon-list/) by name, category, or keywords. Use this assistant when you need to find and add specific icons for your UI components or design elements. |
| **Accessibility Assistant** | `#kendo_accessibility_assistant` | Provides WCAG 2.2 Level AA guidance and component-specific accessibility implementation details. Use this assistant to ensure your UI meets compliance standards, implement correct ARIA roles, and retrieve accessibility API references for KendoReact components. |

For examples of how to use each specialized assistant, see the [Assistant-Specific Prompts](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#assistant-specific-prompts) section in the Prompt Library article.

This approach allows you to focus the AI agent on specific tasks when you need targeted assistance with layout, components, styling, icons, and accessibility.

### [Best Practices](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#best-practices)

To get the best results from the Agentic UI Generator:

*   Start with a focused prompt, then iterate by adding requirements step by step.
*   Be explicit about layout, behavior, data structure, and acceptance criteria.
*   Reference existing components, styling, or patterns to match (for example the [Progress Design System](https://www.telerik.com/design-system/docs/)).
*   Attach relevant files so the generator can align with your current project structure.
*   Use `#kendo_ui_generator` when you want coordinated output across layout, components, styling, icons, and accessibility.
*   Specify responsive behavior for desktop, tablet, and mobile.
*   Keep your React project structure and naming conventions consistent.
*   Review, test, and validate generated code before using it in production.
*   While the Agentic UI Generator performs close to parity with Copilot when paired with powerful models like **Claude Sonnet 4.5**, **GPT-5.2**, or **Gemini 3 Pro**, its differentiated value emerges with smaller models as well (such as **Haiku** and **GPT 5.1 mini**).

[Use Cases](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#use-cases)
----------------------------------------------------------------------------------------------------------------------

The Agentic UI Generator is designed to help with various development scenarios:

#### [Create Individual Components](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#create-individual-components)

Build specific KendoReact components with particular configurations and features like filtering, validation, and data binding.

prompt

`#kendo_ui_generator Create a DropDownList component with filtering and the option to add new items.`

#### [Create Full Responsive Pages](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#create-full-responsive-pages)

*   Build complete dashboards, landing pages, and listing pages in existing applications.
*   Generate pages similar to the [Progress Design System page templates](https://www.telerik.com/design-system/docs/ui-templates/overview/).

prompt

`#kendo_ui_generator I have created an empty application that now needs a login screen and an admin dashboard. Create a new PoC.`

#### [Modify Existing Pages](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#modify-existing-pages)

*   Enhance existing dashboards by adding new sections.
*   Insert new sections that match existing layout style and responsiveness.

prompt

`#kendo_ui_generator Insert a new section in the middle of an existing page. In that added section, a Dashboard Card displays summary KPIs (revenue, active users, growth rate), next to a Compact Card showing a recent alert or message.`

#### [Create and Modify Themes](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#create-and-modify-themes)

*   Generate new themes inside existing applications. Add dark mode or high-contrast themes.

prompt

`#kendo_ui_generator Generate a complete dark theme for my app based on a prompt so my UI looks on-brand in dark mode as well.`

#### [Implement Responsive Layout](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#implement-responsive-layout)

*   Create new responsive pages and sections.
*   Convert existing pages to be responsive for mobile and tablet views.

prompt

`#kendo_ui_generator Update the existing page layout to make it responsive.`

> For a comprehensive collection of sample prompts covering general UI tasks, layout organization, component implementation, styling, accessibility, and icon selection, see the [Agentic UI Generator Prompt Library](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library).

[Privacy](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#privacy)
------------------------------------------------------------------------------------------------------------------

The KendoReact MCP server operates under the following conditions:

*   The MCP server does not have access to your workspace and application code. Note that when using the KendoReact MCP server (or any other MCP server), the LLM generates parameters for the MCP server request, which may include parts of your application code.
*   The MCP server does not use your prompts to train Telerik AI models.
*   The MCP server does not generate the actual responses and has no access to these responses. The MCP server only provides a better context that helps your selected model (for example, GPT, Gemini, Claude) provide better responses.
*   The MCP server does not associate your prompts to your Telerik user account. Your prompts and generated context are anonymized and stored for statistical and troubleshooting purposes.
*   The MCP server stores metrics about how often and how much you use it in order to ensure compliance with the [allowed number of requests that correspond to your current license](https://www.telerik.com/kendo-react-ui/components/ai-tools#license-requirements).

Make sure to also get familiar with the terms and privacy policy of your selected AI model and AI client.

[Usage Limits](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#usage-limits)
----------------------------------------------------------------------------------------------------------------------------

*   Subscription licenses include virtually unlimited requests with fair usage applied.
*   Trial access provides the same virtually unlimited requests during the 30-day trial period.
*   Re-activating the same trial for a new release does not grant additional requests.
*   Requests count toward your account's usage quota.
*   One prompt may trigger multiple requests depending on complexity.

[See Also](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started#see-also)
--------------------------------------------------------------------------------------------------------------------

*   [Agentic UI Generator Prompt Library](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library)
*   [KendoReact MCP Server Overview](https://www.telerik.com/kendo-react-ui/components/ai-tools)
*   [Installing the KendoReact MCP Server](https://www.telerik.com/kendo-react-ui/components/ai-tools/installation)
*   [Progress Design System](https://www.telerik.com/design-system/docs/)
