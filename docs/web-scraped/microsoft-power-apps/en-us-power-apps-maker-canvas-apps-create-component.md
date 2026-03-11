# Source: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-component

Title: Canvas component overview - Power Apps

URL Source: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-component

Markdown Content:
Note

*   This section explains canvas components that encompass low-code UI extensibility capabilities. Professional developers can also use the [Power Apps component framework](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/component-framework-for-canvas-apps) to build code components.
*   You can also use canvas components in model-driven apps by using custom pages and the component library. For more information, see [Add canvas components to a custom page in a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/page-canvas-components).

Components are reusable building blocks for canvas apps. App makers can create custom controls to use inside an app, or across apps by using a [component library](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library). Components can use advanced features such as custom properties and enable complex capabilities. This article introduces component concepts and some examples.

Components are useful when building larger apps that have similar control patterns. If you update a component definition inside the app, all instances in the app reflect your changes. Components also reduce duplication of effort by eliminating the need to copy and paste controls and improve performance. When you use a [component library](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library), components help create collaborative development and standardize the look and feel in an organization.

To learn how to use components in canvas apps, watch this video:

You can create a component from within an app as explained in this article, or by creating a new component inside a [component library](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library). Use a component library when you need to use components across multiple app screens. You can also copy existing components into an existing or a new component library.

To create a component within an app, go to **Tree View**, select the **Components** tab, and then select **New component**:

![Image 1: Create new custom component using tree view.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/insert-new-component-treeview.png)

Selecting **New component** opens an empty canvas. Add controls as part of the component definition on the canvas. If you edit a component in the canvas, you update instances of the same component in other app screens. Apps that reuse an already created component can also receive component updates after you publish component changes.

You can select a component from the list of existing components in the left pane after you select a screen. When you select a component, you insert an instance of that component onto the screen, just as you insert a control.

Components available inside the app appear under the **Custom** category in a list of components inside the tree view. Components imported from component libraries appear under the **Library components** category:

![Image 2: Insert components to the app.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/insert-components.png)

Note

The components discussed in this article are different from the Power Apps component framework that enables developers and makers to create code components for model-driven and canvas apps. For more information, see [Power Apps component framework overview](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview).

A component can receive input values and emit data if you create one or more custom properties. These scenarios are advanced and require you to understand [formulas](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/formula-reference) and binding contracts.

Note

An experimental feature for enhanced component properties provides even more options for properties, including functions and behavior functions. For more information, see [Canvas component properties (experimental)](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-properties)

**Input property** is how a component receives data to be used in the component. Input properties appear in the **Properties** tab of the right-hand pane if an instance of the component is selected. You can configure input properties with expressions or formulas, just as you configure standard properties in other controls. Other controls have input properties, such as the **Default** property of a **Text input** control.

**Output property** is used to emit data or component state. For example, the **Selected** property on a **Gallery** control is an output property. When you create an output property, you can determine what other controls can refer to the component state.

The following walk-through further explains these concepts.

In this example, you'll create a menu component that resembles the following graphic. And you can change the text later to use it in multiple screens, apps, or both:

![Image 3: Final gallery.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/menu-instance-new.png)

Note

We recommend that you use a [component library](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library) when creating components for reuse. Updating components inside an app only makes the component updates available inside the app. When using a component library, you get prompted to update components if components inside a library are updated and published.

1.   Create a [blank canvas app](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-blank-app).

2.   In the **Tree View**, select **Components** and then select **New component** to create a new component.

![Image 4: Create new custom component using tree view.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/insert-new-component-treeview.png)

3.   Select the new component in the left pane, select the ellipsis (**...**), and then select **Rename**. Type or paste the name as **MenuComponent**.

4.   In the right-hand pane, set the component's width as **150** and its height as **250**, and then select **New custom property**. You can also set the height and width to any other value as appropriate.

![Image 5: New property.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/new-property.png)

5.   In the **Display name**, **Property name**, and **Description** boxes, type or paste text as _Items_.

![Image 6: Display name, property name, description boxes.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/property-names.png)

Don't include spaces in the property name because you'll refer to the component by this name when you write a formula. For example, **ComponentName.PropertyName**.

The display name appears on the **Properties** tab of the right-hand pane if you select the component. A descriptive display name helps you and other makers understand the purpose of this property. The **Description** appears in a tooltip if you hover over the display name of this property in the **Properties** tab.

6.   In the **Data type** list, select **Table**, and then select **Create**.

![Image 7: Data type of the property.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/property-data-type.png)

The **Items** property is set to a default value based on the data type that you specified. You can set it to a value that suits your needs. If you specified a data type of **Table** or **Record**, you might want to change the value of the **Items** property to match the data schema that you want to input to the component. In this case, you'll change it to a list of strings.

You can set the property's value in the formula bar if you select the name of the property on the **Properties** tab of the right-hand pane.

![Image 8: Custom input property on the Properties tab.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/properties-tab.png)

As the next graphic shows, you can also edit the property's value on the **Advanced** tab of the right-hand pane.

7.   Set the component's **Items** property to this formula:

```
Table({Item:"SampleText"})
```

![Image 9: Formula.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/set-component-items.png)

8.   In the component, insert a blank vertical **Gallery** control and select **Layout** on the property pane as **Title**.

9.   Make sure that the property list shows the **Items** property (as it does by default). Then set the value of that property to this expression:

```
MenuComponent.Items
```

This way, the **Items** property of the **Gallery** control reads and depends on the **Items** input property of the component.

10.   (Optional) Set the **Gallery** control's **BorderThickness** property to **1** and its **TemplateSize** property to **50**. You can also update values for border thickness and template size to any other value as appropriate.

Next, add the component to a screen and specify a table of strings for the component to show.

1.   In the left pane, select the list of screens, and then select the default screen.

![Image 10: Default screen.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/default-screen.png)

2.   On the **Insert** tab, open the **Components** menu, and then select **MenuComponent**.

![Image 11: Insert component.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/insert.png)

The new component is named **MenuComponent_1** by default.

3.   Set the **Items** property of **MenuComponent_1** to this formula:

```
Table({Item:"Home"}, {Item:"Admin"}, {Item:"About"}, {Item:"Help"})
```

This instance resembles this graphic, but you can customize the text and other properties of each instance.

![Image 12: Final gallery.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/menu-instance-new.png)

So far, you created a component and added it to an app. Next, create an output property that reflects the item that the user selects in the menu.

1.   Open the list of components, and then select **MenuComponent**.

2.   In the right-hand pane, select the **Properties** tab, and then select **New custom property**.

3.   In the **Display name**, **Property name**, and **Description** boxes, type or paste **Selected**.

4.   Under **Property type**, select **Output**, and then select **Create**.

![Image 13: Property type as output.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/output-property-type.png)

5.   On the **Advanced** tab, set the value of the **Selected** property to this expression, adjusting the numeral in the gallery name if necessary:

```
Gallery1.Selected.Item
```

![Image 14: Advanced pane.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/advance.png)

6.   On the default screen of the app, add a label, and set its **Text** property to this expression, adjusting the numeral in the component name if necessary:

```
MenuComponent_1.Selected
```

**MenuComponent_1** is the default name of an instance, not the name of the component definition. You can rename any instance.

7.   While holding down the Alt key, select each item in the menu.

The **Label** control reflects the menu item that you selected most recently.

Input and output properties clearly define the interface between a component and its host app. By default, the component is encapsulated so that it's easier to reuse the component across apps, requiring the use of the properties to pass the information in and out of the component. Scope restrictions keep the data contract of a component simple and cohesive, and it helps enable component-definition updates—especially across apps with component libraries.

But there are times when a component might want to share a data source or a variable with its host. This sharing is especially useful when the component is only intended for use in one particular app. For these cases, you can directly access app level information by turning on the **Access app scope** switch in the component's property pane:

![Image 15: Access app scope switch in component property pane](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/access-app-scope.png)

When you turn on **Access app scope**, the following items are accessible from within a component:

*   Global variables
*   Collections
*   Controls and components on screens, such as a TextInput control
*   Tabular data sources, such as Dataverse tables

When you turn this setting off, the component can't access any of the preceding items.[**Set**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-set) and [**Collect**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-clear-collect-clearcollect) functions are still available but the resulting variables and collections are scoped to the component instance and aren't shared with the app.

Non-tabular data sources, such as Azure Blob Storage or a custom connector, are available whether this setting is turned on or off.Think of these data sources more like referencing an environment resource rather than an app resource.When a component is brought into an app from a component library, these data sources from the environment are also brought in.

Components in a component library can never access app scope, as there's no single app scope to refer to. So, this setting isn't available in this context, and is effectively off.Once imported into an app, and if customization is allowed by the component maker, the switch can be enabled, and the component can be modified to use the app scope.

Note

*   You can insert instances of components into a screen within a component library, and preview that screen for testing purposes.
*   Component library doesn't display when using [Power Apps Mobile](https://powerapps.microsoft.com/downloads/).

Note

This feature is retired. [Component libraries](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library) are the recommended way to reuse the components across the apps. When using component library, an app maintains dependencies on the components it uses. The app maker is alerted when the updates to dependent components become available. Hence, all new reusable components should be created within the component libraries instead.

The ability to import and export components is disabled by default since this feature is retired. While the recommended method to work with components is to use [component libraries](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library), you can still enable this feature on a per-app basis as an exception until the feature is removed. To do this, [edit your app](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/edit-app) in Power Apps Studio and then, go to **Settings**>**Upcoming features**>**Retired**> Set **Export and import components** to On.

![Image 16: Enable export and import of components.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/settings-enable-import-export.png)

After you enable this feature, you can use the following capabilities to import and export components.

To import one or more components from one app into another app, select **Import components** from the **Insert** menu and then use the **Custom** drop-down menu. Or use **Components** in the tree view on the left pane.

A dialog box lists all apps that contain components that you have permission to edit. Select an app, and then select **Import** to import the most recent published version of all of the components in that app. After you import at least one component, you can edit your copy and delete any that you don't need.

![Image 17: Import components dialog box.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/import-component-screen.png)

You can save an app with existing components to a file locally and then reuse the file by importing it. You can use the file to import components to another app.

If the app contains a modified version of the same component, you're prompted to decide whether to replace the modified version or cancel the import.

After you create components in an app, other apps can consume the components from this app by importing them.

Note

If a component that you imported from another app is modified in the original app, you must manually import the component again in the consuming app to receive latest component changes. Use component libraries instead to work with [component updates](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library#update-a-component-library) more efficiently.

You can export components to a file and download them for import to another app.

Select the **Export components** option from the **Components** section in the tree view on the left pane:

![Image 18: Export components tree view.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/export-components-treeview.png)

You can also use the **Insert** menu and then select the **Custom** drop-down menu instead.

![Image 19: Export components insert menu.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/export-components-insert-menu.png)

Selecting **Export components** downloads the components to a file:

![Image 20: Download component.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/download-component.png)

The downloaded component file uses the _.msapp_ file name extension.

To import components from an exported components file, select **Import components** from either **Insert** menu and then use the **Custom** drop-down menu or use **Components** in the tree view on the left pane. From the components dialog box, select **Upload file** instead of selecting any other components or apps:

![Image 21: Import component file.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/import-component-file.png)

From the **Open** dialog box, browse to the location of the component file and select **Open** to import components inside the app.

You can save an app locally by selecting **File**>**Save As**:

![Image 22: Save app.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/create-component/save-app-locally.png)

After you save the app, you can reuse its components by importing them from a file. For more information, see the previous section on importing components from an exported components file.

*   When you have two or more instances of the same component in an app, you can't configure a custom input property to a custom output property value across same or different instances. This action results in a circular reference warning message. To work around this limitation, create a copy of the component inside your app.
*   Adding and running Power Automate flows in component libraries isn't supported.
*   You can't save data sources or controls that include data from those data sources (such as forms, fluid grids, or data tables) with components.
*   You can't insert a component into a gallery or a form (including SharePoint form).
*   Components don't support the [**UpdateContext**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-updatecontext) function, but you can create and update variables in a component by using the [**Set**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-set) function. The scope of these variables is limited to the component, but you can access them from outside the component through custom output properties.

Learn to use a [component library](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library) to create a repository of reusable components.

*   [Component library](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library)
*   [Component library application lifecycle management (ALM)](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-library-alm)
*   [Map input fields of a component](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/map-component-input-fields)
*   [Add multimedia to a component](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-multimedia)
*   [Behavior formulas for components](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/component-behavior)
*   [Power Apps component framework](https://learn.microsoft.com/en-us/power-apps/developer/component-framework/component-framework-for-canvas-apps)
*   [Add canvas components to a custom page in a model-driven app](https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/page-canvas-components)
