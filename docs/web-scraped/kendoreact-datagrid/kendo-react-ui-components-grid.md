# Source: https://www.telerik.com/kendo-react-ui/components/grid

Title: React Data Grid Overview - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid

Published Time: Fri, 27 Feb 2026 12:51:43 GMT

Markdown Content:
Updated

on Feb 26, 2026

React Data Grid is a powerful component for creating responsive, accessible, and customizable applications that require the displaying and management of large datasets.

> **Jumpstart Your Grid**
> 
> 
> With the Agentic UI Generator, you can build components and layouts using natural language prompts — directly inside AI-powered IDEs like VS Code and Cursor. Get intelligent assistance with component implementation, styling, layout design, and iconography powered by our documentation and APIs.
> 
> 
> [Try the Agentic UI Generator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started)

The following example demonstrates the React Data Grid component and its key features in action.

Loading ...

[What is the React Data Grid?](https://www.telerik.com/kendo-react-ui/components/grid#what-is-the-react-data-grid)
------------------------------------------------------------------------------------------------------------------

The React Grid component is a native KendoReact component built specifically for the React ecosystem and distributed via npm.

> [@progress/kendo-react-grid](https://www.npmjs.com/package/@progress/kendo-react-grid)

The KendoReact Data Grid lets you build business applications that **manage and display large sets of data efficiently**. With it, you can structure and present your data in rows and columns, paired with a user-friendly interface for editing and analysis.

The built-in paging, sorting, and filtering enable you to meet your business requirements for **data navigation and analysis**. For more advanced data analysis, the React Grid component offers grouping and aggregation to categorize and summarize data.

The grid’s editing capabilities support in-cell and inline editing, allowing your end users to **modify data directly within the data table**. The options to export to PDF or Excel help with **reporting and data sharing**.

With the row and column virtualization, you can render only the visible data. This lets you **optimize performance and boost efficiency and responsiveness**.

### [Anatomy](https://www.telerik.com/kendo-react-ui/components/grid#anatomy)

A fully featured React Grid might have the following elements inside your app:

![Image 1: "Anatomy and elements of a KendoReact Data Grid component"](https://www.telerik.com/kendo-react-ui/components/assets/641535d1ff0cc413aa95c17662492f87/grid-overview-anatomy.avif)

1.   Toolbar
2.   Grouping header
3.   Grid
4.   Status bar
5.   Pager
6.   Sorted column
7.   Column menu
8.   Grid header
9.   Filter row
10.   Group header
11.   Grid row
12.   Grid alternate row
13.   Group aggregate footer
14.   Group with selected rows
15.   Checkbox row selection

[What is the RSC Mode of KendoReact Data Grid](https://www.telerik.com/kendo-react-ui/components/grid#what-is-the-rsc-mode-of-kendoreact-data-grid)
---------------------------------------------------------------------------------------------------------------------------------------------------

KendoReact Data Grid supports React Server Components (RSC), providing a modern approach to rendering and handling data operations on the server-side. The RSC mode of the Grid leverages server-side execution to improve performance, reduce client-side JavaScript, and enhance application scalability.

The RSC mode of the Grid is implemented on top of the [React Server Components (or RSC)](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components) architecture and enables server-side and hybrid rendering and operations. Unlike traditional client-side grids, the KendoReact Grid in RSC mode minimizes bundle size by executing data operations on the server while keeping interactivity seamless on the client.

[Read mode about the KendoReact Data Grid Server Capabilities here...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode)

### [Benefits of Using the RSC Mode](https://www.telerik.com/kendo-react-ui/components/grid#benefits-of-using-the-rsc-mode)

*   **Optimized Performance:** By offloading expensive operations to the server, the RSC mode reduces the JavaScript executed on the client, improving load times and responsiveness.

*   **Reduced Bundle Size:** Since only essential JavaScript is shipped to the client, applications using the RSC mode benefit from smaller bundles and faster rendering.

*   **Hybrid Data Operations:** The Grid can seamlessly switch between server-side and client-side data handling, allowing flexible implementation based on project requirements.

*   **Better Scalability:** By processing data on the server, applications using the RSC mode can handle large datasets more efficiently.

> You can accelerate your Grid journey with the [KendoReact Agentic UI Generator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started) and the [Component Assistant prompts](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#component-assistant).

[Key Features](https://www.telerik.com/kendo-react-ui/components/grid#key-features)
-----------------------------------------------------------------------------------

The KendoReact Data Grid provides the following key features. Note that this is not an exhaustive list.

*   Data binding

    *   [Streaming data](https://www.telerik.com/kendo-react-ui/components/grid/data-operations/binding-to-remote-data)
    *   [Remote data](https://www.telerik.com/kendo-react-ui/components/grid/data-operations/binding-to-remote-data)

*   Data analysis and review

    *   [Filtering](https://www.telerik.com/kendo-react-ui/components/grid/filtering)
    *   [Sorting](https://www.telerik.com/kendo-react-ui/components/grid/sorting)
    *   [Grouping](https://www.telerik.com/kendo-react-ui/components/grid/grouping)

*   Data exporting

    *   [Exporting to PDF](https://www.telerik.com/kendo-react-ui/components/grid/export/pdf-export)
    *   [Exporting to Excel](https://www.telerik.com/kendo-react-ui/components/grid/export/excel-export)

*   Data visualization

    *   [Scrolling](https://www.telerik.com/kendo-react-ui/components/grid/scroll-modes)
    *   [Paging](https://www.telerik.com/kendo-react-ui/components/grid/paging)

*   Data editing

    *   [Inline](https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-inline) and [in-cell](https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-in-cell) editing
    *   [Validation](https://www.telerik.com/kendo-react-ui/components/grid/editing/editing-validation)

*   [Prompt-Controlled DataGrid](https://www.telerik.com/kendo-react-ui/components/grid/smart)

*   [Custom cells](https://www.telerik.com/kendo-react-ui/components/grid/cells)

*   Columns and rows

    *   [Locking](https://www.telerik.com/kendo-react-ui/components/grid/columns/locked)
    *   [Resizing](https://www.telerik.com/kendo-react-ui/components/grid/columns/resizing)
    *   Spanning [columns](https://www.telerik.com/kendo-react-ui/components/grid/columns/spanned) and [rows](https://www.telerik.com/kendo-react-ui/components/grid/rows/row-span)
    *   Reordering [columns](https://www.telerik.com/kendo-react-ui/components/grid/columns/reordering) and [rows](https://www.telerik.com/kendo-react-ui/components/grid/rows/row-reordering)
    *   [Virtualization](https://www.telerik.com/kendo-react-ui/components/grid/optimization/column-virtualization)
    *   [Master-detail layout](https://www.telerik.com/kendo-react-ui/components/grid/hierarchy)

*   User interactivity

    *   [Selection](https://www.telerik.com/kendo-react-ui/components/grid/selection)
    *   [Context](https://www.telerik.com/kendo-react-ui/components/grid/interactivity/context-menu) and [column](https://www.telerik.com/kendo-react-ui/components/grid/columns/column-menu) menus
    *   [Clipboard](https://www.telerik.com/kendo-react-ui/components/grid/interactivity/clipboard)
    *   [Keyboard navigation](https://www.telerik.com/kendo-react-ui/components/grid/accessibility/keyboard-navigation)

*   Styling

    *   [Customizations](https://www.telerik.com/kendo-react-ui/components/grid/styling/basics)
    *   [Default themes](https://www.telerik.com/kendo-react-ui/components/styling)
    *   [ThemeBuilder](https://www.telerik.com/kendo-react-ui/components/styling/theme-builder)

*   Additional features

    *   [Accessibility](https://www.telerik.com/kendo-react-ui/components/grid/accessibility)
    *   [Globalization](https://www.telerik.com/kendo-react-ui/components/grid/globalization)

[How Does the React Data Grid Work?](https://www.telerik.com/kendo-react-ui/components/grid#how-does-the-react-data-grid-work)
------------------------------------------------------------------------------------------------------------------------------

> Using the KendoReact Data Grid requires either a commercial license key or an active trial license key. Follow the instructions on the KendoReact [My License page](https://www.telerik.com/kendo-react-ui/components/my-license) to activate your license.

The KendoReact Data Grid is built natively for React, with no dependencies. It leverages key React concepts such as a component-based architecture, props and state management, and conditional rendering.

Every React DataGrid is defined as a set of `<GridColumn>`s. You have complete control over your React grid and you can extend or override its default behaviors and appearance via props, templates, and event handlers.

### [Choosing Between the Native React Data Grid and its RSC mode](https://www.telerik.com/kendo-react-ui/components/grid#choosing-between-the-native-react-data-grid-and-its-rsc-mode)

Choosing between the regular client-side KendoReact Data Grid and the [server-side RSC Data Grid](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode) depends largely on the requirements and goals of your application.

You might find **the Native mode of KendoReact Data Grid** helpful for:

*   Highly interactive applications where most of the user interactions happen after the initial load.
*   Applications where the initial load can be optimized by code splitting and lazy loading.
*   Scenarios where SEO is less critical or handled through other means (for example, pre-rendering).

You might find the [**RSC mode of the Grid**](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode) helpful for:

*   Content-heavy applications where initial content needs to be quickly visible to the user.
*   Improving performance on slower devices and networks by offloading initial rendering to the server.
*   Applications where SEO is crucial since the content is available in the initial HTML.
*   Applications where privacy and security need to be handled on the server.
*   Applications that need bundle size optimization.
*   Next.js applications.

You can also consider a hybrid approach where you use server-side rendering for critical or sensitive content and logic, and client-side rendering for user interactions.

### [React Data Grid with Other KendoReact Components](https://www.telerik.com/kendo-react-ui/components/grid#react-data-grid-with-other-kendoreact-components)

Combine multiple KendoReact components with the React grid in the same application to extend its data management and visualization capabilities:

*   Add custom filtering and editing with KendoReact [Inputs](https://www.telerik.com/kendo-react-ui/components/inputs), [Dropdowns](https://www.telerik.com/kendo-react-ui/components/dropdowns), and [Date Inputs](https://www.telerik.com/kendo-react-ui/components/dateinputs).
*   Create buttons within your grid header or grid rows using KendoReact [Buttons](https://www.telerik.com/kendo-react-ui/components/buttons).
*   Prompt users for confirmation or show additional information with KendoReact [Dialogs](https://www.telerik.com/kendo-react-ui/components/dialogs).
*   Show success and error messages with KendoReact [Notification](https://www.telerik.com/kendo-react-ui/components/notification).
*   Add custom forms with KendoReact [Form](https://www.telerik.com/kendo-react-ui/components/form).
*   Extend the Data Grid with appointment scheduling and timeline views using the KendoReact [Scheduler](https://www.telerik.com/kendo-react-ui/components/scheduler).
*   Represent hierarchical data with the KendoReact [TreeView](https://www.telerik.com/kendo-react-ui/components/treeview).
*   Visualize data trends next to your data with KendoReact [Charts](https://www.telerik.com/kendo-react-ui/components/charts).

[Frequently Asked Questions](https://www.telerik.com/kendo-react-ui/components/grid#frequently-asked-questions)
---------------------------------------------------------------------------------------------------------------

### [Is the KendoReact Grid Free to Use](https://www.telerik.com/kendo-react-ui/components/grid#is-the-kendoreact-grid-free-to-use)

The React Grid component provides both free and premium features which require a commercial license key or an active trial license key.

You can start using the free feature of the Grid without any license or registration with Progress or Telerik.

### [What is the RSC Mode of the KendoReact Grid?](https://www.telerik.com/kendo-react-ui/components/grid#what-is-the-rsc-mode-of-the-kendoreact-grid)

The RSC mode is a server-side version of the React DataGrid, designed for React Server Components (RSC) compatible environments [Next.JS](https://nextjs.org/) with [app router](https://nextjs.org/docs/app). Rendered on the server-side, it enables server-side and hybrid data operations, reducing client-side JavaScript execution while maintaining interactivity.

### [How to Add a Grid in React?](https://www.telerik.com/kendo-react-ui/components/grid#how-to-add-a-grid-in-react)

To create a Grid in React, you need to install the KendoReact Grid package and then import the `Grid` component in your application. After that, you can use the grid component in your React application. For more information, refer to the [Getting Started with the KendoReact Grid](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started) article.

### [How to Upgrade to the Premium Grid](https://www.telerik.com/kendo-react-ui/components/grid#how-to-upgrade-to-the-premium-grid)

If you want to use any of the premium Grid features, you need a valid commercial license or an active trial license. A [free trial](https://www.telerik.com/try/kendo-react-ui) is available, if you want to try out the premium features before purchase.

### [What are the Available Support Options](https://www.telerik.com/kendo-react-ui/components/grid#what-are-the-available-support-options)

For any questions about the use of KendoReact Inputs, or any other [KendoReact components](https://www.telerik.com/kendo-react-ui/components/), there are [several support options available](https://www.telerik.com/kendo-react-ui/support):

*   The [KendoReact forums](https://www.telerik.com/forums/kendo-ui-react) are part of the free support you can get from the community and from the KendoReact team on all kinds of general issues.
*   [KendoReact Feedback Portal](https://feedback.telerik.com/kendo-react-ui) and [KendoReact Roadmap](https://www.telerik.com/support/whats-new/kendo-react-ui/roadmap/) provide information on the features in discussion and also those planned for release.
*   KendoReact uses [GitHub Issues](https://github.com/telerik/kendo-react) as its bug tracker, and you can submit any related reports there. Also, check out the [closed list](https://github.com/telerik/kendo-react/issues?q=is%3Aissue+is%3Aclosed).

> KendoReact license holders and anyone in an active trial can also take advantage of the outstanding KendoReact customer support delivered by the developers who built the library. To submit a support ticket, use the [Telerik support system](https://www.telerik.com/account/support-tickets).

Need something unique that is tailor-made for your project? Progress offers its [Progress Services](https://www.progress.com/services) group that can work with you to create any customized solution that you might need.

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid#suggested-links)
-----------------------------------------------------------------------------------------

*   [Getting Started with the KendoReact Free Components](https://www.telerik.com/kendo-react-ui/components/free)
*   [Getting Started with the KendoReact Grid](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started)
*   [Getting Started with the RSC mode of KendoReact Grid](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode)
*   [API Reference of the KendoReact Data Grid (Table)](https://www.telerik.com/kendo-react-ui/components/grid/api/gridprops)
*   [Control the Grid with natural language prompts](https://www.telerik.com/kendo-react-ui/components/grid/smart)
*   [Prompt Library for the Grid](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#component-assistant)
*   [Getting Started with the KendoReact Grid (Video Tutorial)](https://www.telerik.com/videos/how-to-implement-a-react-data-grid-getting-started-with-the-kendoreact-grid)
*   [Getting Started with KendoReact](https://www.telerik.com/try/kendo-react-ui)
*   [React Data Grid High-Level Overview](https://www.telerik.com/kendo-react-ui/grid)
*   [React UI Components](https://www.telerik.com/kendo-react-ui/)
*   [Getting Started with the KendoReact Free Components](https://www.telerik.com/kendo-react-ui/components/free)
*   [Explore the Free Project Tracker Sample Application](https://www.telerik.com/kendo-react-ui/components/sample-applications/project-tracker-with-free-components)
*   [Free Project Tracker app page template (built with free components)](https://www.telerik.com/design-system/docs/ui-templates/templates/project-tracker/)
