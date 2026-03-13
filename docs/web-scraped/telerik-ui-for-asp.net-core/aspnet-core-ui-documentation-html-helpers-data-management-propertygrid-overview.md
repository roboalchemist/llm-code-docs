# Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview

Title: ASP.NET Core Data Management PropertyGrid Overview - Telerik UI for ASP.NET Core

URL Source: https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview

Markdown Content:
New to Telerik UI for ASP.NET Core?[Start a free 30-day trial](https://www.telerik.com/try/aspnet-core-ui)

Updated

on Dec 11, 2025

The Telerik UI PropertyGrid TagHelper and HtmlHelper for ASP.NET Core are server-side wrappers for the Kendo UI PropertyGrid widget.

The PropertyGrid allows you to display and edit properties and attributes of objects. You can bind the component to a Model, edit its nested properties, specify the desired editor and customized template, group, sort, search, or navigate through the data or export it in Excel and PDF.

* [Demo page for the PropertyGrid HtmlHelper](https://demos.telerik.com/aspnet-core/propertygrid)

* [Demo page for the PropertyGrid TagHelper](https://demos.telerik.com/aspnet-core/propertygrid)

[Initializing the PropertyGrid](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#initializing-the-propertygrid)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

The following example demonstrates how to define the PropertyGrid.

Razor

```
@model PropertyViewModel

    @(Html.Kendo().PropertyGrid<PropertyViewModel>()
        .Name("propertyGrid")
        .Model(Model)
        .Columns(columns => 
        {
            columns.FieldColumn(fieldCol => fieldCol.Width(200));
            columns.ValueColumn(valueCol => valueCol.Width(250));
        })
    )
```

[Basic Configuration](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#basic-configuration)
--------------------------------------------------------------------------------------------------------------------------------------------------

The PropertyGrid provides a variety of options for the items configuration, toolbar, context menu, and appearance options like width, height, resizability, and more. The following example demonstrates the basic configuration of the PropertyGrid.

Razor

```
@model PropertyViewModel

    @(Html.Kendo().PropertyGrid<PropertyViewModel>()
        .Name("propertyGrid")
        .Model(Model)
        .EditMode(true)
        .ContextMenu(true)
        .Columns(columns => 
        {
            columns.FieldColumn(fieldCol => fieldCol.Width(200));
            columns.ValueColumn(valueCol => valueCol.Width(250));
        })
        .Items(items =>
        {
             
            items.Add().Field(f => f.Width)
                .Editor(editor => editor.NumericTextBox().Step(1).Min(1).Max(1000));
            items.Add().Field(f => f.Height)
                .Editor(editor => editor.NumericTextBox().Step(1).Min(1).Max(1000));
            items.Add().Field(f => f.Icon)
                .Editor(editor => editor
                    .DropDownList()
                    .DataTextField("Text")
                    .DataValueField("Value")
                    .BindTo(new List<SelectListItem>() {
                        new SelectListItem() {
                            Text = "search", Value = "search"
                        },
                        new SelectListItem() {
                            Text = "user", Value = "user"
                        },
                        new SelectListItem() {
                            Text = "folder", Value = "folder"
                        }
                    }));
        })
    )
```

[Toolbar](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#toolbar)
--------------------------------------------------------------------------------------------------------------------------

The [`Toolbar()`](https://www.telerik.com/aspnet-core-ui/documentation/api/kendo.mvc.ui.fluent/propertygridtoolbarfactory) configuration option of the PropertyGrid allows you to add command buttons and allow the user to invoke built-in PropertyGrid functionalities. You can also define custom commands or use templates to customize the Toolbar of the Telerik UI for ASP.NET Core PropertyGrid.

### [Built-In Commands](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#built-in-commands)

You can configure the Toolbar and include any of the built-in commands:

Razor

```
.Toolbar(t => 
    {
        t.Group();
        t.Separator();
        t.Details();
        t.Search();
        t.Spacer();
        t.Sort();
    })
```

Starting with version 2025 Q2, an alternative way to configure the tools of the PropertyGrid HtmlHelper is to use the `Items()` configuration of the Toolbar:

Razor

```
.Toolbar(toolbar =>toolbar
        .Items(item=>{
            item.Group();
            item.Separator();
            item.Details();
            item.Search();
            item.Spacer();
            item.Sort();
        })
        .Overflow(overflow => overflow
            .Mode(ToolBarOverflowMode.Scroll)
            .ScrollButtons(ScrollButtonsType.Visible)
            .ScrollButtonsPosition(ScrollButtonsPositionType.Split)
        )
    )
```

| Command | Description |
| --- | --- |
| Group | Adds a toggle button to show the items in Groups or a List. |
| Details | Adds an info button for additional details. |
| Sort | Adds a DropDownList to control the order of the items. |
| Search | Adds a built-in Search input for the PropertyGrid. |
| Spacer | Moves the tools that are declared after it to the right side of the Toolbar. |
| Separator | Acts as a delimiter between the Toolbar commands. |

#### [Overview](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#overview)

The built-in Toolbar provides properties for customizing its overflow behavior and appearance.

The following example demonstrates how to modify the default overflow settings of the Toolbar through the `Oveflow()` configuration.

Razor

```
@(Html.Kendo().PropertyGrid<PropertyViewModel>()
        .Name("propertyGrid")
        .Toolbar(t => t.Items(item =>
        {
            item.Spacer();
            item.Search();
        })
        .Overflow(o => o
            .Mode(ToolBarOverflowMode.Scroll)
            .ScrollButtons(ScrollButtonsType.Auto)
            .ScrollButtonsPosition(ScrollButtonsPositionType.Start)
            .ScrollDistance(50))
        )
            ... // Additional configuration.
         )
```

For more information on the available overflow options, refer to the [Appearance documentation of the ToolBar component](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/navigation/toolbar/appearance).

[Functionality and Features](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#functionality-and-features)
----------------------------------------------------------------------------------------------------------------------------------------------------------------

* [Columns](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/columns)—The PropertyGrid displays fields and values in columns.
* [Items](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/items)—The configuration of the PropertyGrid items allows you to customize their appearance and behavior.
* [Templates](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/templates)—The available templates allow you to control the rendering of the items and toolbar.
* [Events](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/events)—The component emits a variety of events that allow you to implement custom functionality.
* [Accessibility](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/accessibility/overview)—The PropertyGrid is accessible for screen readers, supports WAI-ARIA attributes, and delivers [keyboard shortcuts](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/accessibility/keyboard-navigation) for faster navigation.

[Next Steps](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#next-steps)
--------------------------------------------------------------------------------------------------------------------------------

* [Getting Started with the PropertyGrid](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/getting-started)

* [Basic Usage of the PropertyGrid HtmlHelper for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/propertygrid)

* [Basic Usage of the PropertyGrid TagHelper for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/propertygrid)

[See Also](https://www.telerik.com/aspnet-core-ui/documentation/html-helpers/data-management/propertygrid/overview#see-also)
----------------------------------------------------------------------------------------------------------------------------

* [Using the API of the PropertyGrid for ASP.NET Core (Demo)](https://demos.telerik.com/aspnet-core/propertygrid/api)

* [Server-Side API of the PropertyGrid HtmlHelper](https://www.telerik.com/aspnet-core-ui/documentation/api/propertygrid)

* [Server-Side API of the PropertyGrid TagHelper](https://www.telerik.com/aspnet-core-ui/documentation/api/taghelpers/propertygrid)

* [Client-Side API of the PropertyGrid](https://docs.telerik.com/kendo-ui/api/javascript/ui/propertygrid)
