# Source: https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started

Title: React Data Grid Getting Started Getting Started - KendoReact

URL Source: https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started

Markdown Content:
Updated

on Feb 26, 2026

This guide provides essential information about using the KendoReact Grid package—you will learn how to install the package and add a free React Grid component to your project. The steps demonstrated in this guide are applicable to all features of the Grid (free and premium).

Use This React Data Grid for Free You can use the [free feature set](https://www.telerik.com/kendo-react-ui/components/free#react-data-grid) of the Data Grid in production—no sign-up or license required. It’s part of KendoReact, an enterprise-grade UI library with 120+ [free](https://www.telerik.com/kendo-react-ui/components/free) and premium components. To test-drive premium Data Grid functionality, such as inline editing, chart integration and React Server Components mode, [start a 30-day trial](https://www.telerik.com/try/kendo-react-ui).

After completing this tutorial, you will have a free React [Grid](https://www.telerik.com/kendo-react-ui/components/grid) up and running.

> If you prefer video, watch the [React Data Grid Video Tutorial](https://www.telerik.com/videos/how-to-implement-a-react-data-grid-getting-started-with-the-kendoreact-grid).

[Before You Begin](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#before-you-begin)
-----------------------------------------------------------------------------------------------------------------------

sh

`npm create vite@latest my-app -- --template react`

This guide requires that you have **basic knowledge of React and TypeScript**, and that you have already created [**a blank React project**](https://www.telerik.com/kendo-react-ui/components/getting-started).

> You can accelerate your Grid journey with the [KendoReact Agentic UI Generator](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/getting-started) and the [Component Assistant prompts](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#component-assistant).

[Install the Component](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#install-the-component)
---------------------------------------------------------------------------------------------------------------------------------

shell

`npm i @progress/kendo-react-grid`

Run these commands in the root of your React project to install the KendoReact Data Grid and its [dependencies](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#kendoreact-data-grid-dependencies).

[Import the Component](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#import-the-component)
-------------------------------------------------------------------------------------------------------------------------------

tsx

`import { Grid, GridColumn as Column } from '@progress/kendo-react-grid';`

Place the `import` statements in the App component file (for example: `src/App.tsx`) for your project.

Note that you are also importing the `GridColumn` component, but under the `Column` alias.

[Use the Component](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#use-the-component)
-------------------------------------------------------------------------------------------------------------------------

> Using the free features of KendoReact Data Grid Using the free KendoReact Inputs components does not require a license, even in production. To work with any of the premium features of the component, you need a [commercial license key or an active trial license key](https://www.telerik.com/kendo-react-ui/components/my-license).

The KendoReact Data Grid is a powerful tool for creating responsive, accessible, and customizable applications that require the displaying and management of large datasets. This section will take you through a basic Data Grid setup workflow, starting with the column definition and ending with some basic styling.

### [Load and Show Data](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#load-and-show-data)

tsx

```
import products from './gd-products';

const App = () => {
    return <Grid data={products}></Grid>;
};

export default App;
```

1.   Use the dataset from the demo source files at the top of the guide to create a `gd-products.json` file locally in your project.
2.   Use an `import` statement to reference the data file.
3.   Add a `<Grid>` definition.
4.   Use the `data` prop to load the data in your Data Grid.

You now have a simple grid that shows all the data from `gd-products.json`.

### [Define Columns](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#define-columns)

tsx

```
<Grid data={products}>
    <Column field="ProductID" title="ID" />
    <Column field="ProductName" title="Name" />
    <Column field="Category.CategoryName" title="Category" />
    <Column field="UnitPrice" title="Price" />
    <Column field="UnitsInStock" title="In stock" />
    <Column field="Discontinued" title="Discontinued" />
</Grid>
```

1.   For every column that you want to show, add a `<Column>` definition. Note that `Column` is an alias for `GridColumn`.
2.   Use the `field` prop to bind the column to the respective data field in your data set. For nested fields, use a `parent.child` notation (for example: `Category.CategoryName`).
3.   Use the `title` prop to set a custom title for the column. If not set, the title defaults to the name of the field.

You now have a grid that shows a sub-set of the data and has custom column names.

### [Enable the Built-in State Management of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#enable-the-built-in-state-management-of-the-grid)

tsx

```
<Grid
    data={data}
    dataItemKey="ProductID"
    autoProcessData={true}
>
```

1.   Enable the `autoProcessData` prop of the Grid to allow the component to handle the data state management internally.

2.   Set the `dataItemKey` prop to an unique value field from the bound to the Grid data.

tsx

```
<Grid
    data={data}
    dataItemKey="ProductID"
    autoProcessData={true}
    pageable={true}
    defaultSkip={0}
    defaultTake={10}
>
```

1.   Enable the `pageble` prop of the Grid to enable pagination.
2.   Configure the `defaultTake` and `defaultSkip` props to specify the initially loaded page.

### [Enable Filtering](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#enable-filtering)

tsx

```
<Grid
    data={data}
    dataItemKey="ProductID"
    autoProcessData={true}
    filterable={true}
>
```

1.   Configure the `<Grid>` props to enable filtering. 
    *   `filterable` enables the built-in filter row, rendered right below the column titles.
    *   `defaultFilter` (optional) is the descriptor by which the data is filtered initially.

### [Enable Sorting](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#enable-sorting)

tsx

```
<Grid
    data={data}
    dataItemKey="ProductID"
    autoProcessData={true}
    sortable={true}
>
```

1.   Configure the `<Grid>` props to enable sorting. 
    *   `sortable` enables the built-in sorting which triggers when you click the column title. When the column is sorted, an arrow indicating the sorting direction shows next to the column title.
    *   `defaultSort`(optional) is the descriptor by which the data is sorted initially.

### [Enable In-cell Editing](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#enable-in-cell-editing)

tsx

```
<Grid
    data={data}
    dataItemKey="ProductID"
    autoProcessData={true}
    editable={{ mode: 'incell' }}
    onItemChange={handleItemChange}
>
```

1.   Set the `editable` prop of the Grid either to `true` or by defining its editing mode. We will set it to `incell` for the purpose of this tutorial.

2.   Add logic that handles the item editing.

tsx 
```
const [data, setData] = useState<Array<Product>>(products);

const handleItemChange = (event: GridItemChangeEvent) => {
    const newData = data.map((item) =>
        item.ProductID === event.dataItem.ProductID ? { ...item, [event.field!]: event.value } : item
    );
    setData(newData);
};
``` 
3.   Configure the `<Grid>` props to enable editing.

    *   Update your data binding.
    *   Set the `onItemChange` prop to finish your event handling.

4.   Update your `<Column>` definitions.

    *   Set `editable={false}` for the ID and Category columns. This disables editing for the cells in the respective columns.
    *   Set the `editor` prop for the other `<Column>`s.

tsx

```
<Column field="ProductID" title="ID" editable={false} filterable={false} width="75px" />
<Column field="ProductName" title="Name" editor="text" />
<Column field="Category.CategoryName" title="Category" editable={false} width="300px"></Column>
<Column field="UnitPrice" title="Price" editor="numeric" width="150px" />
<Column field="UnitsInStock" title="In stock" editor="numeric" width="150px" />
<Column field="Discontinued" title="Discontinued" editor="boolean" width="150px" />
```

You now have a grid with enabled editing.

[Style the Component](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#style-the-component)
-----------------------------------------------------------------------------------------------------------------------------

> Are you looking for guidance around how to create visually appealing and consistent user interfaces with Telerik UI components? Check out the [Progress Design System](https://www.telerik.com/design-system/docs/).

To use the built-in styling of the components, start by installing a theme:

sh

`npm i @progress/kendo-theme-default`

With the `import "@progress/kendo-theme-default/dist/all.css";` statement present in your code, you already have professionally designed styling applied to your app out-of-box. You can also try any of the other available [Kendo UI Themes](https://www.telerik.com/design-system/docs/themes/get-started/introduction/#available-themes).

[Next Steps](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#next-steps)
-----------------------------------------------------------------------------------------------------------

Now try to enable another feature of the Grid package yourself. The procedures for [installing](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#install-the-components), [importing](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#import-the-component), and [using](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#use-the-component) the Grid features are identical for all features in the package.

[KendoReact Data Grid APIs](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#kendoreact-data-grid-apis)
-----------------------------------------------------------------------------------------------------------------------------------------

[Grid API](https://www.telerik.com/kendo-react-ui/components/grid/api)

[KendoReact Data Grid Dependencies](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#kendoreact-data-grid-dependencies)
---------------------------------------------------------------------------------------------------------------------------------------------------------

The Grid package requires you to install the following [peer dependencies](https://nodejs.org/en/blog/npm/peer-dependencies/) in your application:

| Package Name | Description |
| --- | --- |
| react 18.0.0* | Contains the functionality necessary to define React components. |
| react-dom | Contains the React renderer for the web. |
| @progress/kendo-licensing | Contains the internal infrastructure related to licensing. |
| @progress/kendo-react-intl | Contains the KendoReact Internationalization package that applies the desired cultures by providing services and pipes for the parsing and formatting of dates and numbers. |
| @progress/kendo-data-query | Applies sorting, filtering, grouping, and aggregate data operations. |
| @progress/kendo-react-animation | Enables the animations in the KendoReact components. |
| @progress/kendo-react-data-tools | Delivers components required to manage and control the data in the application. |
| @progress/kendo-react-dateinputs | Contains the KendoReact Date Inputs components that are used to select the date and time for an appointment. |
| @progress/kendo-react-dropdowns | Contains the KendoReact Dropdowns, which allows users to choose from a predefined list of options. |
| @progress/kendo-react-inputs | Contains the KendoReact Inputs, which the input of data, based on a specific and predefined format. |
| @progress/kendo-drawing | Contains the Drawing library, which provides interactive vector graphics. |
| @progress/kendo-react-buttons | Contains the KendoReact Buttons library, which provides buttons. |
| @progress/kendo-react-treeview | Contains the KendoReact TreeView package that is used in the DropDowns. |
| @progress/kendo-react-popup | Contains the KendoReact Popup components. |
| @progress/kendo-svg-icons | Contains the KendoReact SVG icons. |

[Activating Your License Key](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#activating-your-license-key)
---------------------------------------------------------------------------------------------------------------------------------------------

**Important**: The KendoReact Grid has both free and premium features that require a license key file to be installed in your project. This applies to both trial and commercial usage:

*   **Trial usage**: [Start a free trial](https://www.telerik.com/try/kendo-react-ui) and download a trial license key file
*   **Commercial usage**: [Purchase a license](https://www.telerik.com/kendo-react-ui/pricing) and download a commercial license key file

Without a valid license key file, the premium features will display licensing warnings and watermarks.

Follow the instructions on the KendoReact [My License page](https://www.telerik.com/kendo-react-ui/components/my-license) to download and install your license key file. You can skip this step if your application already contains a KendoReact license file.

[Suggested Links](https://www.telerik.com/kendo-react-ui/components/grid/getting-started/get-started#suggested-links)
---------------------------------------------------------------------------------------------------------------------

*   [React Data Grid](https://www.telerik.com/kendo-react-ui/components/grid)
*   [Setting Up Local Data Operations](https://www.telerik.com/kendo-react-ui/components/grid/data-operations/local-operations)
*   [Applying Data Operations on the Server](https://www.telerik.com/kendo-react-ui/components/grid/data-operations/odata-server-operations)
*   [Editing Grid Data Records](https://www.telerik.com/kendo-react-ui/components/grid/editing)
*   [Using Locked Columns](https://www.telerik.com/kendo-react-ui/components/grid/columns/locked)
*   [Exporting to PDF](https://www.telerik.com/kendo-react-ui/components/grid/export/pdf-export)
*   [Styling the Grid](https://www.telerik.com/kendo-react-ui/components/grid/styling/basics)
*   [API Reference of the Grid](https://www.telerik.com/kendo-react-ui/components/grid/api)
*   [Prompt Library for the Grid](https://www.telerik.com/kendo-react-ui/components/ai-tools/agentic-ui-generator/prompt-library#component-assistant)
*   [Virtual Classroom (Introductory Course Available to Trial and Commercial License Holders)](https://learn.telerik.com/learn/course/external/view/elearning/14/kendoreact)
*   [Explore the Finance Portfolio Sample Application](https://www.telerik.com/kendo-react-ui/components/sample-applications/finance-application/)
*   [Explore the Coffee Warehouse Sample Application](https://www.telerik.com/kendo-react-ui/components/sample-applications/react-coffee-warehouse-dashboard/)
*   [Explore the GitHub Issues Grid Sample Application](https://www.telerik.com/kendo-react-ui/components/sample-applications/issues-grid/)
