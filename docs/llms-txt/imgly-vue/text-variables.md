# Text Variables

Text variables enable data-driven template personalization in CE.SDK. Insert placeholder tokens like `{{firstName}}` into text blocks, then populate them with actual values programmatically. This separates design from content, enabling automated document generation, batch processing, and mass personalization workflows.

![Text Variables example showing personalized text with dynamic data](/docs/cesdk/_astro/browser.hero.XpZwp4B9_2jn2Pq.webp)

10 mins

estimated time

Live Demo[

Download](https://github.com/imgly/cesdk-web-examples/archive/refs/heads/main.zip)[

StackBlitz](https://stackblitz.com/~/github.com/imgly/cesdk-web-examples/tree/main/guides-create-templates-dynamic-content-text-variables-browser)[

GitHub](https://github.com/imgly/cesdk-web-examples/tree/main/guides-create-templates-dynamic-content-text-variables-browser)

```
import type { EditorPlugin, EditorPluginContext } from '@cesdk/cesdk-js';import packageJson from './package.json';
/** * CE.SDK Plugin: Text Variables Guide * * Demonstrates text variable management in CE.SDK with a single comprehensive example: * - Discovering variables with findAll() * - Creating and updating variables with setString() * - Reading variable values with getString() * - Binding variables to text blocks with {{variable}} tokens * - Detecting variable references with referencesAnyVariables() * - Removing variables with remove() * - Localizing variable labels */class Example implements EditorPlugin {  name = packageJson.name;
  version = packageJson.version;
  async initialize({ cesdk }: EditorPluginContext): Promise<void> {    if (!cesdk) {      throw new Error('CE.SDK instance is required for this plugin');    }
    // Initialize CE.SDK with Design mode and load asset sources    await cesdk.addDefaultAssetSources();    await cesdk.addDemoAssetSources({      sceneMode: 'Design',      withUploadAssetSources: true    });    await cesdk.createDesignScene();
    const engine = cesdk.engine;    const page = engine.block.findByType('page')[0];
    // Set page dimensions for consistent layout    engine.block.setWidth(page, 800);    engine.block.setHeight(page, 600);
    const pageWidth = engine.block.getWidth(page);    const pageHeight = engine.block.getHeight(page);
    // Localize variable labels that appear in the Variables panel UI    cesdk.i18n.setTranslations({      en: {        'variables.firstName.label': 'First Name',        'variables.lastName.label': 'Last Name',        'variables.email.label': 'Email Address',        'variables.company.label': 'Company Name',        'variables.title.label': 'Job Title'      }    });
    // Pattern 1: Discover all existing variables in the scene    // This is useful when loading templates to see what variables need values    const existingVariables = engine.variable.findAll();    console.log('Existing variables:', existingVariables); // []
    // Pattern 2: Create and update text variables    // If a variable doesn't exist, setString() creates it    // If it already exists, setString() updates its value    engine.variable.setString('firstName', 'Alex');    engine.variable.setString('lastName', 'Smith');    engine.variable.setString('email', 'alex.smith@example.com');    engine.variable.setString('company', 'IMG.LY');    engine.variable.setString('title', 'Creative Developer');
    // Pattern 3: Read variable values at runtime    const firstName = engine.variable.getString('firstName');    console.log('First name variable:', firstName); // 'Alex'
    // Create a single comprehensive text block demonstrating all variable patterns    const textBlock = engine.block.create('text');
    // Multi-line text combining:    // - Single variable ({{firstName}})    // - Multiple variables ({{firstName}} {{lastName}})    // - Variables in context (Email: {{email}})    const textContent = `Hello, {{firstName}}!
Full Name: {{firstName}} {{lastName}}Email: {{email}}Position: {{title}}Company: {{company}}`;
    engine.block.replaceText(textBlock, textContent);    engine.block.setWidthMode(textBlock, 'Auto');    engine.block.setHeightMode(textBlock, 'Auto');    engine.block.setFloat(textBlock, 'text/fontSize', 52);    engine.block.appendChild(page, textBlock);
    // Center the text block on the page (after font size is set)    // Get the actual frame dimensions of the block (including its bounds)    const frameX = engine.block.getFrameX(textBlock);    const frameY = engine.block.getFrameY(textBlock);    const frameWidth = engine.block.getFrameWidth(textBlock);    const frameHeight = engine.block.getFrameHeight(textBlock);
    // Calculate centered position accounting for frame offset    engine.block.setPositionX(textBlock, (pageWidth - frameWidth) / 2 - frameX);    engine.block.setPositionY(      textBlock,      (pageHeight - frameHeight) / 2 - frameY    );
    // Check if the block contains variable references    const hasVariables = engine.block.referencesAnyVariables(textBlock);    console.log('Text block has variables:', hasVariables); // true
    // Create and then remove a temporary variable to demonstrate removal    engine.variable.setString('tempVariable', 'Temporary Value');    console.log('Variables before removal:', engine.variable.findAll());
    // Remove the temporary variable    engine.variable.remove('tempVariable');    console.log('Variables after removal:', engine.variable.findAll());
    // Select the text block to show the Variables panel    engine.block.setSelected(textBlock, true);
    // Final check: List all variables in the scene    const finalVariables = engine.variable.findAll();    console.log('Final variables in scene:', finalVariables);    // Expected: ['firstName', 'lastName', 'email', 'company', 'title']  }}
export default Example;
```

This guide covers how to discover, create, update, and manage text variables both through the UI and programmatically using the Variables API.

## Introduction[#](#introduction)

Text variables allow you to design templates once and personalize them with different content for each use. At render time, CE.SDK replaces variable tokens with actual values provided through the Variables API. This approach is ideal for:

*   **Automated document generation** - Certificates, invoices, reports
*   **Mass personalization** - Marketing materials with recipient data
*   **Data-driven design** - Templates populated from JSON, CSV, or APIs
*   **Form-based editing** - Expose variables through custom interfaces

## Using the Built-in Variables UI[#](#using-the-built-in-variables-ui)

CE.SDK includes a Variables panel where template authors can create and manage variables visually. To access this panel, ensure you’re using CE.SDK (not engine-only) and that the Variables feature is enabled.

The Variables panel allows you to:

*   **Create new variables** with descriptive names
*   **Insert tokens** into text blocks using `{{variableName}}` syntax
*   **Preview** how the final design looks with different values
*   **Manage** all variables defined in the current scene

Variables appear in the inspector panel with localized labels when you configure translations through the i18n API.

## Discovering Variables[#](#discovering-variables)

When working with templates that already contain variables, discover what variables exist before populating them with values.

```
// Pattern 1: Discover all existing variables in the scene// This is useful when loading templates to see what variables need valuesconst existingVariables = engine.variable.findAll();console.log('Existing variables:', existingVariables); // []
```

The `findAll()` method returns an array of all variable keys defined in the scene. This is essential when loading templates to understand what data needs to be provided.

## Creating and Updating Variables[#](#creating-and-updating-variables)

Create or update variables using `setString()`. If the variable doesn’t exist, it will be created. If it already exists, its value will be updated.

```
// Pattern 2: Create and update text variables// If a variable doesn't exist, setString() creates it// If it already exists, setString() updates its valueengine.variable.setString('firstName', 'Alex');engine.variable.setString('lastName', 'Smith');engine.variable.setString('email', 'alex.smith@example.com');engine.variable.setString('company', 'IMG.LY');engine.variable.setString('title', 'Creative Developer');
```

Variable keys are case-sensitive. `{{Name}}` and `{{name}}` are different variables.

## Reading Variable Values[#](#reading-variable-values)

Retrieve the current value of a variable at runtime using `getString()`. This is useful for validation or displaying current values in custom UI.

```
// Pattern 3: Read variable values at runtimeconst firstName = engine.variable.getString('firstName');console.log('First name variable:', firstName); // 'Alex'
```

## Binding Variables to Text Blocks[#](#binding-variables-to-text-blocks)

Insert variable tokens directly into text block content using the `{{variableName}}` syntax. CE.SDK automatically detects and resolves these tokens at render time.

### Single Variable[#](#single-variable)

```
    // Create a single comprehensive text block demonstrating all variable patterns    const textBlock = engine.block.create('text');
    // Multi-line text combining:    // - Single variable ({{firstName}})    // - Multiple variables ({{firstName}} {{lastName}})    // - Variables in context (Email: {{email}})    const textContent = `Hello, {{firstName}}!
Full Name: {{firstName}} {{lastName}}Email: {{email}}Position: {{title}}Company: {{company}}`;
    engine.block.replaceText(textBlock, textContent);    engine.block.setWidthMode(textBlock, 'Auto');    engine.block.setHeightMode(textBlock, 'Auto');    engine.block.setFloat(textBlock, 'text/fontSize', 52);    engine.block.appendChild(page, textBlock);
```

### Multiple Variables[#](#multiple-variables)

Combine multiple variables in a single text block:

```
    // Create a single comprehensive text block demonstrating all variable patterns    const textBlock = engine.block.create('text');
    // Multi-line text combining:    // - Single variable ({{firstName}})    // - Multiple variables ({{firstName}} {{lastName}})    // - Variables in context (Email: {{email}})    const textContent = `Hello, {{firstName}}!
Full Name: {{firstName}} {{lastName}}Email: {{email}}Position: {{title}}Company: {{company}}`;
    engine.block.replaceText(textBlock, textContent);    engine.block.setWidthMode(textBlock, 'Auto');    engine.block.setHeightMode(textBlock, 'Auto');    engine.block.setFloat(textBlock, 'text/fontSize', 52);    engine.block.appendChild(page, textBlock);
```

The variables resolve in place, maintaining the surrounding text and formatting.

## Detecting Variable References[#](#detecting-variable-references)

Check if a block contains variable references using `referencesAnyVariables()`. This returns `true` if the block’s text contains any `{{variable}}` tokens.

```
// Check if the block contains variable referencesconst hasVariables = engine.block.referencesAnyVariables(textBlock);console.log('Text block has variables:', hasVariables); // true
```

This is useful for identifying which blocks need variable values before export or for implementing validation logic.

## Removing Variables[#](#removing-variables)

Remove unused variables from the scene with `remove()`. This cleans up the variable store when certain variables are no longer needed.

```
// Create and then remove a temporary variable to demonstrate removalengine.variable.setString('tempVariable', 'Temporary Value');console.log('Variables before removal:', engine.variable.findAll());
// Remove the temporary variableengine.variable.remove('tempVariable');console.log('Variables after removal:', engine.variable.findAll());
```

After removal, the variable no longer exists in the scene. Text blocks that reference removed variables will display the token literally (e.g., `{{removedVar}}`).

## Localizing Variable Labels[#](#localizing-variable-labels)

In CE.SDK (with UI), display friendly labels for variables in the inspector panel using i18n translations. Map variable keys to human-readable names that appear in the UI.

```
// Localize variable labels that appear in the Variables panel UIcesdk.i18n.setTranslations({  en: {    'variables.firstName.label': 'First Name',    'variables.lastName.label': 'Last Name',    'variables.email.label': 'Email Address',    'variables.company.label': 'Company Name',    'variables.title.label': 'Job Title'  }});
```

Without localization, the Variables panel shows the technical variable key (e.g., `firstName`). With localization, it shows the friendly label (e.g., “First Name”).

## Combining with Other Features[#](#combining-with-other-features)

Text variables work seamlessly with other CE.SDK template features:

### With Placeholders[#](#with-placeholders)

Use **placeholders** for dynamic images and videos while **variables** personalize text content. This combination enables fully dynamic templates where both visuals and copy change per use case.

### With Editing Constraints[#](#with-editing-constraints)

Lock layout elements while allowing only variable token editing. This ensures brand consistency while enabling content personalization.

### With Role-Based Editing[#](#with-role-based-editing)

Show the Variables panel only to template authors (Creator role) and hide it from end users (Adopter role). This guides the editing experience based on user permissions.

## API Reference[#](#api-reference)

| Method | Description |
| --- | --- |
| `engine.variable.findAll()` | Get array of all variable keys in the scene |
| `engine.variable.setString()` | Create or update a text variable |
| `engine.variable.getString()` | Read the current value of a variable |
| `engine.variable.remove()` | Delete a variable from the scene |
| `engine.block.referencesAnyVariables()` | Check if a block contains variable tokens |
| `engine.block.replaceText()` | Set text content (supports variable tokens) |
| `cesdk.i18n.setTranslations()` | Set UI labels for variable names |

---



[Source](https:/img.ly/docs/cesdk/vue/create-templates/add-dynamic-content/set-editing-constraints-c892c0)