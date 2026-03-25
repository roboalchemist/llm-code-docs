# Source: https://www.telerik.com/kendo-react-ui/components/grid/smart

Title: React Data Grid Smart Grid Overview - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/smart

Markdown Content:
[KendoReact Smart DataGrid Premium](https://www.telerik.com/kendo-react-ui/components/grid/smart#kendoreact-smart-datagrid)
---------------------------------------------------------------------------------------------------------------------------

Updated

on Feb 10, 2026

The KendoReact Smart Grid enhances the traditional data grid with AI-powered capabilities that make data exploration more intuitive and efficient. By leveraging artificial intelligence, the Smart Grid can automatically analyze data patterns, suggest relevant operations, and provide intelligent insights to help users discover meaningful information faster.

![Image 1: ninja-icon](https://www.telerik.com/kendo-react-ui/components/static/d2ecd6c1a01f6b1598a481623b8f4389/start-free-trial-icon.inline.svg)The Smart Grid is part of [KendoReact](https://www.telerik.com/kendo-react-ui) premium, an enterprise-grade UI library with 120+ [free](https://www.telerik.com/kendo-react-ui/components/free) and premium components for building polished, performant apps. Test-drive all features with a free 30-day trial.[Start Free Trial](https://www.telerik.com/try/kendo-react-ui)

[Smart Features in the KendoReact Data Grid](https://www.telerik.com/kendo-react-ui/components/grid/smart#smart-features-in-the-kendoreact-data-grid)
-----------------------------------------------------------------------------------------------------------------------------------------------------

Explore the Smart Grid capabilities through the following examples:

[Supported Operations](https://www.telerik.com/kendo-react-ui/components/grid/smart#supported-operations)
---------------------------------------------------------------------------------------------------------

The AI Assistant toolbar tool currently supports applying the following Grid operations through natural language prompts:

| Category | Operations |
| --- | --- |
| **Data Operations** | * **Filtering**—Filter data based on specific criteria. * **Sorting**—Sort data by one or multiple columns. * **Grouping**—Group data by specific fields. |
| **Column Operations** | * **Resize**—Resize columns to specific widths. * **Reorder**—Change the order of columns. * **Show/Hide**—Show or hide specific columns. * **Lock/Unlock**—Lock or unlock columns to keep them visible while scrolling. |
| **Highlighting and Selection** | * **Row/Cell Highlighting**—Highlight specific rows or cells that meet certain conditions. * **Row/Cell Selection**—Select/deselect rows or cells based on criteria, or select/deselect all items. |
| **Export** | * **Excel/PDF Export**—Export Grid data to Excel or PDF format. |

[Smart Grid Tools](https://www.telerik.com/kendo-react-ui/components/grid/smart#smart-grid-tools)
-------------------------------------------------------------------------------------------------

The Smart Grid provides the following specialized toolbar tools that enable natural language interaction with your Grid data.

### [AI Smart Box](https://www.telerik.com/kendo-react-ui/components/grid/smart#ai-smart-box)

The [AI Smart Box](https://www.telerik.com/kendo-react-ui/components/grid/smart/basic-operations) is a versatile search box that combines traditional search functionality with AI-powered capabilities. It provides three distinct modes that you can enable independently or in combination:

*   [Search Mode](https://www.telerik.com/kendo-react-ui/components/grid/smart/basic-operations)—Traditional keyword-based filtering across the Grid columns.
*   [Semantic Search Mode](https://www.telerik.com/kendo-react-ui/components/grid/smart/basic-operations)—Enhanced search that interprets user intent and matches related terms, synonyms, and contextual meanings to find semantically relevant data in the Grid.
*   [AI Assistant Mode](https://www.telerik.com/kendo-react-ui/components/grid/smart/basic-operations)—Full AI-powered Grid control with the same capabilities as the [AI Toolbar Assistant](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-toolbar-assistant). Users can perform any [supported Grid operation](https://www.telerik.com/kendo-react-ui/components/grid/smart#supported-operations) through natural language prompts entered in the AI Assistant mode of the Smart Box.

The AI Smart Box is ideal when you want to provide a unified search and AI interaction experience in a single Grid toolbar control.

### [AI Toolbar Assistant](https://www.telerik.com/kendo-react-ui/components/grid/smart#ai-toolbar-assistant)

> For an enhanced user experience with additional search capabilities, prompt suggestions, and streamlined UI, we recommend using the [AI Smart Box](https://www.telerik.com/kendo-react-ui/components/grid/smart/basic-operations). The AI Smart Box combines traditional search, semantic search, and AI-powered operations in a single, unified interface.

The [AI Toolbar Assistant](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-toolbar-assistant) is a dedicated toolbar button with a distinctive AI sparkles icon that provides a streamlined interface for AI-powered Grid control, allowing users to enter natural language prompts to perform Grid operations.

This tool is ideal when you want to provide AI capabilities as a dedicated feature in your Grid toolbar, separate from other Grid controls. It offers a focused user experience specifically designed for performing [supported Grid operations](https://www.telerik.com/kendo-react-ui/components/grid/smart#supported-operations) through natural language prompts.

> For more information about setting up and integrating these tools, refer to the [AI Assistant Tools Setup](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-assistant-tools-setup) article.

[AI Service Configuration](https://www.telerik.com/kendo-react-ui/components/grid/smart#ai-service-configuration)
-----------------------------------------------------------------------------------------------------------------

The [Smart Grid AI Assistant tools](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-assistant-tools-setup) require a backend AI service that you must implement to process natural language prompts and return structured Grid operation commands. This service acts as the bridge between user prompts and Grid operations.

When a user interacts with the Smart Grid, your React application sends the prompt to your backend, which should process it using your configured AI provider, and return structured commands that the Grid can apply automatically.

### [Smart Extensions](https://www.telerik.com/kendo-react-ui/components/grid/smart#smart-extensions)

To simplify your backend implementation, we provide the `Telerik.AI.SmartComponents.Extensions` library for .NET applications. This library handles the complexity of interpreting natural language and generating Grid-compatible responses.

The library integrates with `Microsoft.Extensions.AI` and supports Azure OpenAI, OpenAI API, or local LLM models. It provides pre-built functionality for processing Grid-specific prompts and formatting responses correctly.

> For detailed implementation instructions, including package installation, AI provider configuration, and controller setup, see [AI Service Setup](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-service-setup).

### [Custom Implementation](https://www.telerik.com/kendo-react-ui/components/grid/smart#custom-implementation)

If you use a non-.NET backend (such as Node.js, Python, or Java) or have specific requirements that Smart Extensions does not cover, you can build your own AI service implementation.

Your custom backend must:

*   Accept requests with the user's prompt and Grid column information.
*   Process the prompt using your chosen AI provider or LLM.
*   Return responses in the format that the KendoReact Grid expects.

Use the detailed information about the expected request and response structures from the [AI Service Setup](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-service-setup#request-and-response-format) article to build a compatible custom service.

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/smart#suggested-links)
-----------------------------------------------------------------------------------------------

*   [AI Assistant Tools Setup](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-assistant-tools-setup)
*   [AI Service Setup](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-service-setup)
*   [AI Toolbar Assistant](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-toolbar-assistant)
*   [AI Chat Assistant](https://www.telerik.com/kendo-react-ui/components/grid/smart/ai-chat-assistant)
*   [AI Column Assistant](https://www.telerik.com/kendo-react-ui/components/grid/smart/custom-column)
*   [AI-Powered Highlighting](https://www.telerik.com/kendo-react-ui/components/grid/smart/highlight)
*   [AI-Powered Selection](https://www.telerik.com/kendo-react-ui/components/grid/smart/selection)
*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [Custom Cells Overview](https://www.telerik.com/kendo-react-ui/components/grid/cells)
