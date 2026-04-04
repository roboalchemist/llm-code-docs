# Source: https://blog.ag-grid.com/whats-new-in-ag-grid-34-3/

Title: What's New in AG Grid 34.3

URL Source: https://blog.ag-grid.com/whats-new-in-ag-grid-34-3/

Published Time: 2025-10-22T08:53:16.000Z

Markdown Content:
*   [![Image 1: James Swinton-Bland](https://blog.ag-grid.com/content/images/size/w100/2024/08/me.jpeg)James Swinton-Bland](https://blog.ag-grid.com/author/james/)
*   [![Image 2: Kiril Matev](https://blog.ag-grid.com/content/images/size/w100/2024/12/Kiril-Matev-2.jpg)Kiril Matev](https://blog.ag-grid.com/author/kiril/)

22 October 2025|[Releases](https://blog.ag-grid.com/tag/version-release/)

![Image 3: What's New in AG Grid 34.3 - AI Features, React 19.2 Support](https://blog.ag-grid.com/content/images/2025/10/Whats-New-in-AG-Grid-34.3---AI-Features--React-19.2-Support-4.png)
AG Grid 34.3 introduces powerful new AI features, enhancements to column auto-sizing and pivoting, and official support for React 19.2:

1.   [AI Toolkit](https://www.ag-grid.com/data-grid/ai-toolkit/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog) - Generate structured outputs to use with LLMs, allowing end users to manipulate grid state with natural language. 
2.   [MCP Server](https://www.ag-grid.com/data-grid/mcp-server/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog) - More efficiently and accurately implement, maintain and upgrade AG Grid with your favourite LLM. 
3.   [Scaled Column Auto-Sizing](https://www.ag-grid.com/data-grid/column-sizing/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog#auto-size-columns-to-fit-cell-contents) - Automatically scale column widths to fit available space while maintaining relative sizing. 
4.   [Date and Time Pivoting](https://www.ag-grid.com/data-grid/pivoting-column-groups/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog#pivoting-by-dates-and-times) - Pivot data by time-based fields (e.g. day, week, month, year) for enhanced temporal analysis. 
5.   [React 19.2 Support](https://www.ag-grid.com/data-grid/compatibility/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog#ag-grid--react-compatibility-chart) - Official support for React 19.2 with improved compatibility and performance. 

💡

This is a ****non-breaking release****. Projects using AG Grid 33.x can upgrade to 34.3 without code changes.

AI Toolkit
----------

Our new [AI Toolkit](https://www.ag-grid.com/data-grid/ai-toolkit/?ref=blog.ag-grid.com) allows you to easily integrate AG Grid with your own LLM, enabling end users to query and manipulate grid state via natural language.

[Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs?ref=blog.ag-grid.com)is an LLM feature that ensures model responses adhere to a supplied[JSON Schema](https://json-schema.org/?ref=blog.ag-grid.com). Structured Outputs are supported by many LLMs, including [ChatGPT](https://platform.openai.com/docs/guides/structured-outputs?ref=blog.ag-grid.com) and [Gemini](https://ai.google.dev/gemini-api/docs/structured-output?ref=blog.ag-grid.com).

The AI Toolkit provides a`getStructuredSchema`API that generates a structured schema, based on[Grid State](https://ag-grid.com/archive/34.3.0/react-data-grid/grid-state/?ref=blog.ag-grid.com). These outputs can be passed to an LLM, which can then generate valid responses that can be passed directly to the`setState`API method. This ensures reliable, schema-aligned instructions for updating or manipulating the grid based on natural language input:

```
// Get Structured Schema representation of Grid State
const gridSchema = gridApi.getStructuredSchema();

// Send User Request, Current State & Schema to LLM
const response = await callLLM(userRequest, gridApi.getState(), gridSchema)

// Update State with LLM Response
gridApi.setState(response.newGridState);
```

This feature allows users to more effictively and efficiently interrogate their data by performing complex state configurations with natural language.

0:00

/0:18

![Image 4](https://blog.ag-grid.com/content/media/2025/10/AI-Toolkit_thumb.jpg)

MCP Server
----------

Our [Model Context Protocol (MCP) server](https://www.ag-grid.com/data-grid/mcp-server/?ref=blog.ag-grid.com) provides AI Agents with framework and version-specific knowledge to help developers integrate and maintain their AG Grid code.

To [install AG MCP](https://ag-grid.com/data-grid/mcp-server/?ref=blog.ag-grid.com#installation) in your LLM, use the `npx ag-mcp` command during the MCP install process, as defined by your LLM; for example, to add `ag-mcp` to Claude Code, run the following command:

`claude mcp add ag-mcp npx ag-mcp`

Once the MCP is installed, your LLM will automatically leverage the AG MCP Server to access additional context, based on your prompt.

Whilst this feature is primarily aimed at developers, users will benefit from developers being able to more quickly adopt new AG Grid features and perform version upgrades.

Scaled Column Auto Sizing
-------------------------

AG Grid 34.3 introduces a [new column auto-sizing mode](https://www.ag-grid.com/data-grid/column-sizing/?ref=blog.ag-grid.com#auto-size-columns-to-fit-cell-contents) that auto-sizes columns first, and if there's leftover space, it scales them proportionally to fill the grid width. This ensures columns fit neatly inside the grid width and no column is significantly wider than its cell values.

This new column auto-sizing mode can be activated using the `scaleUpToFitGridWidth`option to the`autoSizeStrategy`params or the `autoSizeColumns` API method:

```
gridRef.current!.api.autoSizeColumns({ skipHeader, scaleUpToFitGridWidth });
```

This feature is particularly useful when columns are generated dynamically from a data set and developers can't know ahead of time how large the columns should be:

0:00

/0:17

![Image 5](https://blog.ag-grid.com/content/media/2025/10/Auto-Size-Column_thumb.jpg)

Date & Time Pivoting
--------------------

Pivoting now supports [Date & Time values](https://www.ag-grid.com/data-grid/pivoting-column-groups/?ref=blog.ag-grid.com#pivoting-by-dates-and-times), and the grid can optionally generate pivot group columns based on components of the date/time.

To enable this for a particular column, use the`groupHierarchy`property of the[Column Definition](https://ag-grid.com/archive/34.3.0/react-data-grid/column-properties/?ref=blog.ag-grid.com#reference-grouping-groupHierarchy):

```
const [columnDefs, setColumnDefs] = useState([
    {
        field: 'date',
        pivot: true,
        groupHierarchy: ['year', 'month']
    },
    // ...other column definitions
]);

<AgGridReact columnDefs={columnDefs} />
```

This enables richer temporal analysis directly in the grid:

0:00

/0:20

![Image 6](https://blog.ag-grid.com/content/media/2025/10/Date-Time-Pivot_thumb.jpg)

React 19.2 Support
------------------

AG Grid 34.3 comes with [official support for React 19.2](https://www.ag-grid.com/react-data-grid/compatibility/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog#top), just three weeks after its release. All of our docs examples have been updated to and tested against React 19.2, so you can start taking advantage of all the [latest React features](https://react.dev/blog/2025/10/01/react-19-2?ref=blog.ag-grid.com#new-react-features), today.

Summary
-------

AG Grid 34.3 introduces powerful new AI features, enhancements to column auto-sizing and pivoting, and official support for React 19.2.

As always, we're here to help you upgrade, and we're keen to hear your feedback. Enterprise customers can contact us via [Zendesk](https://ag-grid.zendesk.com/hc/en-us?ref=blog.ag-grid.com); Alternatively, please submit a [GitHub issue](https://github.com/ag-grid/ag-grid/issues?ref=blog.ag-grid.com).

Next Steps
----------

New to AG Grid? Get started in minutes, for free:

[![Image 7: React Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg)](https://www.ag-grid.com/react-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog)[![Image 8: Angular Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/c/cf/Angular_full_color_logo.svg)](https://www.ag-grid.com/angular-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog)[![Image 9: Vue Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/9/95/Vue.js_Logo_2.svg)](https://www.ag-grid.com/vue-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog)[![Image 10: Javascript Data Grid - AG Grid Documentation](https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png)](https://www.ag-grid.com/javascript-data-grid/getting-started/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog)

Considering AG Grid Enterprise? [Request a free two-week trial licence](https://www.ag-grid.com/react-data-grid/community-vs-enterprise/?utm_source=blog.ag-grid.com&utm_medium=blog&utm_campaign=ag-grid-34-3-release-blog#request-an-enterprise-bundle-trial-licence) to test your application in production and get direct access to our support team.

Happy coding!

Read more posts about...
