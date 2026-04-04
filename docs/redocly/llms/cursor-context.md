# Source: https://redocly.com/docs/vscode/cursor-context.md

# Interactive forms and context-aware help for OpenAPI authoring

To help you write valid, specification-compliant API definitions, the Redocly OpenAPI VS Code extension provides dynamic descriptions of OpenAPI features in the cursor context panel.

Access the cursor context in any of the following ways:

- Select the **Open cursor context** button in the upper right section of your VS Code window.
- Open the *Command Palette*, start typing `redocly`, then select **Redocly OpenAPI: Open cursor context**.


Both actions open the *Cursor context* panel.

As you place your cursor into different sections of your OpenAPI document, the context-aware descriptions in the panel change to match the exact object or property you're editing.

![Using the cursor context panel](/assets/openapi-vscode-context-explorer.a30f811cb29b75bbb87b2f03b1430cd8d92eaa49cd9ba1f143d633debec54407.289fb047.png)

For supported sections, the *Cursor context* panel can also display a visual editor where you can change the contents of your API definition through interactive forms.

![Using the visual editor](/assets/redocly-vscode-visual-editor.42515a92f21b39d9c975aca89b421b9ac04e3b2c97d3e31b52c558b0eb174879.289fb047.gif)

Depending on the selected section in the OpenAPI document, the *Cursor context* panel may show triple bar ("hamburger") icons to the left of each input field in the visual editor.
Use these icons to change the order of fields in the panel.
To reorder a field, select the triple bar icon next to it, then drag it up or down in the panel.

To exit, close the *Cursor context* panel. You can open it again at any point.