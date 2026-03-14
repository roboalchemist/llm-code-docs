# Source: https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode

Title: React Data Grid RSC Mode Overview - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode

Markdown Content:
[Grid RSC Mode Overview Premium](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#grid-rsc-mode-overview)
------------------------------------------------------------------------------------------------------------------------

Updated

on Dec 19, 2025

The RSC mode of the KendoReact Grid is a modern, high-performance implementation built on top of the [React Server Components (or RSC)](https://react.dev/blog/2023/03/22/react-labs-what-we-have-been-working-on-march-2023#react-server-components) architecture allowing you to perform server and hybrid data operations.

![Image 1: ninja-icon](https://www.telerik.com/kendo-react-ui/components/static/d2ecd6c1a01f6b1598a481623b8f4389/start-free-trial-icon.inline.svg)The RSC Mode of the Grid is part of [KendoReact](https://www.telerik.com/kendo-react-ui) premium, an enterprise-grade UI library with 120+ [free](https://www.telerik.com/kendo-react-ui/components/free) and premium components for building polished, performant apps. Test-drive all features with a free 30-day trial.[Start Free Trial](https://www.telerik.com/try/kendo-react-ui)

The server-side mode of the Grid is part of the default `@progress/kendo-react-grid` package and is optimized for both client environments and RSC-compatible frameworks like [Next.JS](https://nextjs.org/) with [app router](https://nextjs.org/docs/app). A crucial part of the RSC Grid usage is avoiding the usage of `"use client"` directive on top of the page where the component is defined:

jsx

`import { Grid as ServerGrid } from '@progress/kendo-react-grid';`

Loading ...

[Hybrid Data Operations](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#hybrid-data-operations)
----------------------------------------------------------------------------------------------------------------

To use enable the RSC mode of the Grid and utilize its hybrid data operations, you need to simply add it to a page inside a Next.js app (or in another RSC-compatible frameworks) and **skip** the `"use client"` directive on top. You should also use `'use server';` added in the beginning of each callback to instruct the Grid that it should perform on the server.

jsx

```
import { Grid } from '@progress/kendo-react-grid';

const onDataStateChange = async (event: ServerEvent<GridDataStateChangeEvent>) => {
    'use server';

    saveState(event.dataState);
};

return <Grid data={dataResult} onDataStateChange={onDataStateChange} />;
```

[Bundle size](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#bundle-size)
------------------------------------------------------------------------------------------

Unlike regular React components that execute on both server and client (hydration), the server mode of the Grid operates exclusively on the server. You can [optimize the performance](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/performance) of the RSC Mode Grid even more by specifying the loading of the modules that are actually used which his results in a significant reduction in the total bundle size of your application.

By using the RSC mode of the KendoReact Grid only the essential JavaScript is shipped to the client, which is only the code needed to hydrate the component and add interactivity. The architecture retains most of the virtual DOM on the client side, allowing you to execute expensive operations solely on the server, without the need to ship your code to the client.

[Key Features](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#key-features)
--------------------------------------------------------------------------------------------

The KendoReact Server Data Grid offers an extensive and continuously expanding set of built-in features that isn't limited by the list in this section. What makes the `Grid` truly exceptional is its flexibility—it allows you to seamlessly blend both server-side and client-side operations, adapting to your application's unique requirements.

### [Data Operations](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#data-operations)

Delve into the intricacies of executing basic data operations, including server-side `filtering`, `sorting`, `paging`, etc. Understand how these operations can be performed either on the client or the server.

[Read more about React Data Grid RSC Mode data operations...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/data-operations)

### [Server Actions](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#server-actions)

Explore how to handle various Grid events on the server, enabling seamless interaction tracking, user input handling, and custom logic execution.

[Read more about React Data Grid RSC Mode server actions...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/server-actions)

### [Server Templates](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#server-templates)

Learn the art of customization by providing unique views to the Grid. Explore the creation of custom `cells` and `rows` templates to your application's specific needs.

[Read more about React Data Grid RSC Mode templates...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/templates)

### [Selection](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#selection)

Learn how to implement row and cell selection in the Grid, allowing users to interact with data efficiently through multiple selection modes.

[Read more about React Data Grid RSC Mode selection...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/selection)

### [Filtering](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#filtering)

Discover how to enable powerful filtering options in the Grid, allowing users to refine displayed data with intuitive filter controls.

[Read more about React Data Grid RSC Mode filtering...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/filtering)

### [Sorting](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#sorting)

Learn how to enable dynamic sorting in the Grid, giving users the ability to organize data by columns in ascending or descending order.

[Read more about React Data Grid RSC Mode sorting...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/sorting)

### [Grouping](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#grouping)

Learn how to enable data grouping in the Grid, allowing users to organize and visualize data more effectively by grouping rows based on specific columns.

[Read more about React Data Grid RSC Mode grouping...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/grouping)

### [Paging](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#paging)

Understand how to implement paging in the Grid to efficiently handle large datasets by loading and displaying data in manageable chunks.

[Read more about React Data Grid RSC Mode paging...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/paging)

### [Globalization](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#globalization)

Configure internationalization and localization features in the RSC mode of the Grid to adapt it to different languages and cultures.

[Read more about React Data Grid RSC Mode globalization...](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode/globalization)

[Next Steps](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#next-steps)
----------------------------------------------------------------------------------------

*   [Getting Started with KendoReact Data Grid RSC Mode](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started-rsc)

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/rsc-mode#suggested-links)
--------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [Getting Started with КendoReact Grid RSC Mode](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started-rsc)
