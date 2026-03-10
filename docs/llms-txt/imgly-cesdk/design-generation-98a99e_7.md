# Source: https://img.ly/docs/cesdk/nextjs/automation/design-generation-98a99e/

---
title: "Automate Design Generation"
description: "Generate on-brand designs programmatically using templates, variables, and CE.SDK’s headless API."
platform: nextjs
url: "https://img.ly/docs/cesdk/nextjs/automation/design-generation-98a99e/"
---

> This is one page of the CE.SDK Next.js documentation. For a complete overview, see the [Next.js Documentation Index](https://img.ly/docs/cesdk/nextjs.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/nextjs/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/nextjs/guides-8d8b00/) > [Automate Workflows](https://img.ly/docs/cesdk/nextjs/automation-715209/) > [Design Generation](https://img.ly/docs/cesdk/nextjs/automation/design-generation-98a99e/)

---

Automating design generation simplifies workflows and allows you to create
dynamic, personalized designs at scale. By combining design templates with
external data or user-provided input, you can quickly generate professional
outputs for various use cases, from banner ads to direct mail.

With IMG.LY, you can use templates to define dynamic elements such as text, images, or other assets. These elements are populated with real-time data or user inputs during the generation process. This guide will walk you through the process of using the CE.SDK for programmatic design generation.

[Launch Web Demo](https://img.ly/showcases/cesdk/headless-design/web)

## Populating a Template

A design template is a pre-configured layout that includes placeholders for dynamic elements such as text, images, or other assets. These placeholders define where and how specific content will appear in the final design. During the generation process, the placeholders are replaced with actual data to create a completed output.

- **Creating or Editing Templates:** Design templates can be created or edited directly within the CE.SDK using our UI or programmatically. Learn more in the [Create Templates guide](https://img.ly/docs/cesdk/nextjs/create-templates-3aef79/).
- **Dynamic Content Sources:** Templates can be populated with data from various sources, such as:
  - **JSON files:** Useful for batch operations where data is pre-prepared.
  - **External APIs:** Ideal for real-time updates and dynamic integrations.
  - **User Input:** Data provided directly by the user through a UI.

For detailed information on using and managing templates, see [Use Templates](https://img.ly/docs/cesdk/nextjs/use-templates/overview-ae74e1/).

Below is a diagram illustrating how data is merged into a template to produce a final design:

![Template data merge process diagram showing how variables and assets flow into the final output](./assets/schema.excalidraw.svg)

## Example Workflow

### 1. Prepare the Template

Start by designing a template with text variables. Here's an example postcard template with placeholders for the recipient's details:

![Example postcard template with highlighted variable placeholders for name and address](./assets/scene-example-backside.png)

### 2. Load the Template into the Editor

Initialize the CE.SDK and load your prepared template:

```ts example=basic-scene marker=cesdk-init-after
// Load a template from your server or a CDN
const sceneUrl =
  'https://cdn.img.ly/assets/demo/v4/ly.img.template/templates/cesdk_postcard_2.scene';
await engine.scene.loadFromURL(sceneUrl);
```

### 3. Provide Data to Populate the Template

Populate your template with data from your chosen source:

```ts example=basic-scene marker=cesdk-init-after
// Option 1: Prepare your data as a javascript object
const data = {
  textVariables: {
    first_name: 'John',
    last_name: 'Doe',
    address: '123 Main St.',
    city: 'Anytown',
  },
};
// Option 2: Fetch from an API
// const data = await fetch('https://api.example.com/design-data').then(res => res.json());
engine.variable.setString('first_name', data.textVariables.first_name);
engine.variable.setString('last_name', data.textVariables.last_name);
engine.variable.setString('address', data.textVariables.address);
engine.variable.setString('city', data.textVariables.city);
```

### 4. Export the Final Design

Once the template is populated, export the final design in your preferred format:

```ts example=basic-scene marker=cesdk-init-after
const output = await engine.block.export(engine.scene.get(), {
  mimeType: 'application/pdf',
});
// Success: 'output' contains your generated design as a PDF Blob
// You can now save it or display it in your application
```

Here's what your final output should look like:

![Exported postcard design showing populated name and address fields](./assets/scene-example-backside-export.png)

Need help with exports? Check out the [Export Guide](https://img.ly/docs/cesdk/nextjs/export-save-publish/export-82f968/) for detailed instructions and options.

## Troubleshooting

If you encounter issues during the generation process:

- Verify that all your variable names exactly match those in your template
- Ensure your template is accessible from the provided URL
- Check that your data values are in the correct format (strings for text variables)
- Monitor the console for detailed error messages from the CE.SDK



---

## More Resources

- **[Next.js Documentation Index](https://img.ly/docs/cesdk/nextjs.md)** - Browse all Next.js documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/nextjs/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/nextjs/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
