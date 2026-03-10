# Automate Design Generation

Automating design generation simplifies workflows and allows you to create dynamic, personalized designs at scale. By combining design templates with external data or user-provided input, you can quickly generate professional outputs for various use cases, from banner ads to direct mail.

With IMG.LY, you can use templates to define dynamic elements such as text, images, or other assets. These elements are populated with real-time data or user inputs during the generation process. This guide will walk you through the process of using the CE.SDK for programmatic design generation.

[

Launch Web Demo

](https://img.ly/showcases/cesdk/headless-design/web)

## Populating a Template[#](#populating-a-template)

A design template is a pre-configured layout that includes placeholders for dynamic elements such as text, images, or other assets. These placeholders define where and how specific content will appear in the final design. During the generation process, the placeholders are replaced with actual data to create a completed output.

*   **Creating or Editing Templates:** Design templates can be created or edited directly within the CE.SDK using our UI or programmatically. Learn more in the [Create Templates guide](vue/create-templates-3aef79/) .
*   **Dynamic Content Sources:** Templates can be populated with data from various sources, such as:
    *   **JSON files:** Useful for batch operations where data is pre-prepared.
    *   **External APIs:** Ideal for real-time updates and dynamic integrations.
    *   **User Input:** Data provided directly by the user through a UI.

For detailed information on using and managing templates, see [Use Templates](vue/use-templates/overview-ae74e1/) .

Below is a diagram illustrating how data is merged into a template to produce a final design:

![Template data merge process diagram showing how variables and assets flow into the final output](/docs/cesdk/_astro/schema.excalidraw.CEnF4vNU_GsqTX.svg)

## Example Workflow[#](#example-workflow)

### 1\. Prepare the Template[#](#1-prepare-the-template)

Start by designing a template with text variables. Here’s an example postcard template with placeholders for the recipient’s details:

![Example postcard template with highlighted variable placeholders for name and address](/docs/cesdk/_astro/scene-example-backside.DrVrBaSF_ZWnyVB.webp)

### 2\. Load the Template into the Editor[#](#2-load-the-template-into-the-editor)

Initialize the CE.SDK and load your prepared template:

```
// Load a template from your server or a CDNconst sceneUrl =  'https://cdn.img.ly/assets/demo/v3/ly.img.template/templates/cesdk_postcard_2.scene';await engine.scene.loadFromURL(sceneUrl);
```

### 3\. Provide Data to Populate the Template[#](#3-provide-data-to-populate-the-template)

Populate your template with data from your chosen source:

```
// Option 1: Prepare your data as a javascript objectconst data = {  textVariables: {    first_name: 'John',    last_name: 'Doe',    address: '123 Main St.',    city: 'Anytown',  },};// Option 2: Fetch from an API// const data = await fetch('https://api.example.com/design-data').then(res => res.json());engine.variable.setString('first_name', data.textVariables.first_name);engine.variable.setString('last_name', data.textVariables.last_name);engine.variable.setString('address', data.textVariables.address);engine.variable.setString('city', data.textVariables.city);
```

### 4\. Export the Final Design[#](#4-export-the-final-design)

Once the template is populated, export the final design in your preferred format:

```
const output = await engine.block.export(engine.scene.get(), {  mimeType: 'application/pdf',});// Success: 'output' contains your generated design as a PDF Blob// You can now save it or display it in your application
```

Here’s what your final output should look like:

![Exported postcard design showing populated name and address fields](/docs/cesdk/_astro/scene-example-backside-export.CaGuyU7v_1hqBcg.webp)

Need help with exports? Check out the [Export Guide](vue/export-save-publish/export-82f968/) for detailed instructions and options.

## Troubleshooting[#](#troubleshooting)

If you encounter issues during the generation process:

*   Verify that all your variable names exactly match those in your template
*   Ensure your template is accessible from the provided URL
*   Check that your data values are in the correct format (strings for text variables)
*   Monitor the console for detailed error messages from the CE.SDK

---



[Source](https:/img.ly/docs/cesdk/vue/automation/data-merge-ae087c)