# Source: https://developers.webflow.com/designer/reference/variables-detail-overview.mdx

***

title: Variables
slug: designer/reference/variables-detail-overview
description: Learn how to create and manage variables with the Designer API.
hidden: false
max-toc-depth: 3
'og:title': 'Webflow Designer API: Variables'
'og:description': Learn how to create and manage variables with the Designer API.
---------------------------------------------------------------------------------

Variables are reusable design tokens that let you [define and manage values across your Webflow projects](https://university.webflow.com/lesson/variables?topics=layout-design). They enable you to create a single source of truth for common values like colors, spacing, and typography. When you update a variable's value, that change automatically propagates everywhere the variable is used, making it easy to maintain consistency and make global design updates.

Assign variables to any compatible [style property](/designer/reference/style-properties). For example, you can use color variables for background colors, size variables for padding and margins, or font variables for typography. When the variable's value changes, all style properties using that variable will automatically update, providing a powerful way to maintain design consistency and make global updates efficiently.

## Variable types

Webflow currently supports five types of variables:

<CardGroup cols={3}>
  <Card
    title="Color"
    href="/designer/reference/create-color-variable"
    iconPosition="left"
    iconSize="10"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Variable.svg"
          alt=""
          className="dark-icon"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Variable.svg"
          alt=""
          className="light-icon"
        />
      </>
    }
  >
    <p>
      Define colors.
    </p>
  </Card>

  <Card
    title="Size"
    href="/designer/reference/create-size-variable"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/GlobalCDN.svg"
          alt=""
          className="dark-icon"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/GlobalCDN.svg"
          alt=""
          className="light-icon"
        />
      </>
    }
  >
    <p>
      Define sizes and spacing.
    </p>
  </Card>

  <Card
    title="Font"
    href="/designer/reference/create-font-family-variable"
    iconPosition="left"
    iconSize="12"
    icon={
      <>
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Typography.svg"
          alt=""
          className="dark-icon"
        />
        <img
          src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Typography.svg"
          alt=""
          className="light-icon"
        />
      </>
    }
  >
    <p>
      Define fonts.
    </p>
  </Card>

  <Card title="Number" href="/designer/reference/create-number-variable" iconPosition="left" iconSize="7" icon={"fa-thin fa-hashtag"}>
    <p>
      Define number.
    </p>
  </Card>

  <Card title="Percentage" href="/designer/reference/create-percentage-variable" iconPosition="left" iconSize="7" icon={"fa-thin fa-percent"}>
    <p>
      Define percentages.
    </p>
  </Card>
</CardGroup>

## Creating a variable

Variables belong to a collection. To create a variable, you need to get the collection first.

```typescript
const collection = await webflow.getVariableCollectionById(
  "Your Collection ID"
);
```

Each variable type has its own creation function. Below are the available variable types and how to create them:

{/* <!-- vale off --> */}

<Tabs>
  <Tab title="Color">
    ```typescript
    collection.createColorVariable(name: string, value: string | ColorVariable | CustomValue): Promise<ColorVariable>
    ```

    | Accepted Formats for Value | Examples                                                 |
    | -------------------------- | -------------------------------------------------------- |
    | Color name                 | `collection.createColorVariable("primary", "red");`      |
    | RGB Hex                    | `collection.createColorVariable("primary", "#ffcc11");`  |
    | RGBA Hex                   | `collection.createColorVariable("primary", "#fffcc11");` |
  </Tab>

  <Tab title="Size">
    ```typescript
    collection.createSizeVariable(name: string, value: SizeValue | SizeVariable | CustomValue): Promise<SizeVariable>
    ```

    | Format                | Unit  | Examples                        |
    | --------------------- | ----- | ------------------------------- |
    | Pixels                | `px`  | `{ unit: "px", value: 50 });`   |
    | Root EM               | `rem` | `{ unit: "rem", value: 2 });`   |
    | EM Units              | `em`  | `{ unit: "em", value: 1.5 });`  |
    | Viewport Width        | `vw`  | `{ unit: "vw", value: 100 });`  |
    | Viewport Height       | `vh`  | `{ unit: "vh", value: 100 });`  |
    | Small Viewport Height | `svh` | `{ unit: "svh", value: 100 });` |
    | Small Viewport Width  | `svw` | `{ unit: "svw", value: 100 });` |
    | Character Units       | `ch`  | `{ unit: "ch", value: 80 });`   |
  </Tab>

  <Tab title="Number & Percentage">
    ```typescript
    collection.createNumberVariable(name: string, value: number | NumberVariable | CustomValue): Promise<NumberVariable>
    ```

    | Accepted Formats for Value     | Examples                                              |
    | ------------------------------ | ----------------------------------------------------- |
    | Number value between 0 and 100 | `collection.createPercentageVariable("opacity", 50);` |
  </Tab>

  <Tab title="FontFamily">
    ```typescript
    collection.createFontFamilyVariable(name: string, value: string | FontFamilyVariable | CustomValue): Promise<FontFamilyVariable>
    ```

    | Accepted Formats for Value                       | Examples                                                         |
    | ------------------------------------------------ | ---------------------------------------------------------------- |
    | String of the font family name (e.g., "Verdana") | `collection.createFontFamilyVariable("defaultFont", "Verdana");` |
  </Tab>
</Tabs>

{/* <!-- vale on --> */}

### Variable aliases

Variable aliases allow you to create references between variables, making it easier to maintain consistent design systems and create dynamic relationships between your variables. When you update the original variable, all aliases automatically reflect the change.

```typescript
// Get the default variable collection
const collection = await webflow.getDefaultVariableCollection();

// Create primary brand color variable
const primaryColor = await collection.createColorVariable(
  "primary-brand",
  "#0066FF"
);

// Create aliases that reference the primary color
const buttonColor = await collection.createColorVariable(
  "button-primary",
  primaryColor
);
const linkColor = await collection.createColorVariable(
  "link-color",
  primaryColor
);

// When primaryColor changes, buttonColor and linkColor will automatically update
await primaryColor.set("#FF0066");
```

### Custom values

Webflow's variable system supports a limited set of CSS functions, enabling you to create dynamic, responsive, and mathematically derived values.

#### Available functions

Webflow supports these CSS functions in variables:

<div id="available-functions">
  | Function                                                                                | Purpose                                 | Example                                         |
  | --------------------------------------------------------------------------------------- | --------------------------------------- | ----------------------------------------------- |
  | [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/calc\(\))                   | Perform mathematical calculations       | `calc(100vh - var(--header-height))`            |
  | [`clamp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/clamp\(\))                 | Create fluid values with min/max bounds | `clamp(1rem, 5vw, 3rem)`                        |
  | [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/min\(\))                     | Use the smallest of multiple values     | `min(50%, 300px)`                               |
  | [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/max\(\))                     | Use the largest of multiple values      | `max(100px, 20%)`                               |
  | [`color-mix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value/color-mix) | Blend colors together                   | `color-mix(in srgb, var(--primary) 75%, white)` |
</div>

#### Using functions with custom values

To use functions in variables, you need to create or set them as custom values. Custom values work with any variable type.

<Note title="Variable References">
  When using functions, you can reference other variables using the `var()` syntax. This allows you to create dynamic relationships between your design tokens. To dynamically get this syntax, you can use the [`getBinding()`](/designer/reference/get-variable-binding) method on a variable.

  ```typescript
  variable.set({
    type: "custom",
    value: "calc(var(--spacing-base) * 2)",
  });
  ```
</Note>

{/* <!-- vale off --> */}

<Tabs>
  <Tab title="Create a custom value" id="createCustomValue">
    ```typescript
    // Get collection
    const collection = await webflow.getDefaultVariableCollection()

    // Create a Color Variable
    const colorVariable = await collection.createColorVariable("blue-500", "#146EF5")

    // Get the binding for the variable
    const binding = await colorVariable.getBinding()

    // Create a Color Variable with a custom value
    await colorVariable.set({
        type: "custom",
        value: `color-mix(in srgb, ${binding}, white 75%)`
    });
    ```
  </Tab>

  <Tab title="Set a custom value" id="setCustomValue">
    ```typescript
    variable.set({
        type: "custom",
        value: "clamp(1rem, 2vw, 2rem)"
    });
    ```
  </Tab>
</Tabs>

{/* <!-- vale on --> */}

## Selecting variables

Select variables from their Collection by their name or ID.

{/* <!-- vale off --> */}

```typescript
// Get Default Collection
const collection = await webflow.getDefaultVariableCollection();

// Get variable by ID
const variableById = await collection?.getVariable("id-123");

// Get Variable by Name
const variableByName = await collection?.getVariableByName("Space Cadet");
```

{/* <!-- vale on --> */}

## Updating variables

Renaming and setting new values on a variable.

### Renaming variables

Variables in Webflow can be renamed for better clarity or organization. After you've successfully renamed a variable, all instances where this variable is used will automatically reference the new name.

{/* <!-- vale off --> */}

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection();

if (collection) {
  // Get variable and reset name
  const variable = await collection.getVariableByName("Space Cadet");
  await variable?.setName("Our awesome bg color");
}
```

{/* <!-- vale on --> */}

### Setting variable values

You can't change a variable's type once it's created. However, you can change its value. The format for updating the value is consistent with its initial declaration.

{/* <!-- vale off --> */}

```typescript
// Get Collection
const collection = await webflow.getDefaultVariableCollection();

// Get Variable
const variable = await collection?.getVariable("id-123");

// Check Variable type and set color
if (variable?.type === "Color") await variable.set("#fffcc11");
```

{/* <!-- vale on --> */}

## Applying variables to styles

After defining your variables, you can incorporate them into your styles. To do this, simply use the variable as the property value in the style you're customizing.

{/* <!-- vale off --> */}

```typescript
// Get collection
const collection = await webflow.getDefaultVariableCollection();

// Get Style and desired variable
const style = await webflow.getStyleByName(styleName);
const variable = await collection?.getVariablebyName(variableName);

// Check variable type and set property
if (variable?.type === "Size")
  await style?.setProperties({ "font-size": variable });
```

{/* <!-- vale on --> */}
