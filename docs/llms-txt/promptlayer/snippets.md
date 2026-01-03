# Source: https://docs.promptlayer.com/features/prompt-registry/snippets.md

# Snippets

Snippets allow you to modularize and reuse pieces of your prompt templates, much like using building blocks to create a larger structure. This feature enables you to compose complex templates by referencing other prompt templates within a parent template.

<div style={{ position: 'relative', paddingBottom: '50.72916666666667%', height: 0 }}>
  <iframe src="https://www.loom.com/embed/9ed20506d19e43f5812f22ccc5fd830e?sid=4fc7a099-e325-42b3-971a-2a1d82bfe7d7" frameBorder="0" allowFullScreen style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%' }} />
</div>

## How Snippets Work

### Adding Snippets via the Dashboard

To add a new snippet while writing a template in the Dashboard:

1. Tap the `/` symbol.
2. Select `Snippets` from the dropdown menu.
3. A dialog box will appear, guiding you through the insertion of your snippet.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/snippet-modal.gif?s=33d40c09b47a34900a4f3ffe63f1cbb8" alt="Inserting a snippet" data-og-width="868" width="868" data-og-height="480" height="480" data-path="images/snippet-modal.gif" data-optimize="true" data-opv="3" />

*Inserting a snippet from the Dashboard*

### Creating Snippets Programmatically

A snippet is a reference to a prompt template that can be inserted into another template. You can reference templates in three ways:

1. **By Template Name**: `@@@template_name@@@` - This will automatically use the latest version of the referenced template.
2. **By Template Version Number**: `@@@template_name@version_number:{number}@@@` - This points to a specific version of the template.
3. **By Template Label**: `@@@template_name@label:{label_name}@@@` - This uses the version of the template that has the specified label.

### Restrictions

It's important to note that only completion templates can be used as snippets.

## Rendering Snippets

When you run a parent template that contains snippets, the system 'renders' the template, replacing the snippet references with their actual content. This transpilation occurs whether you run the template from the Playground, use the Evaluation functionality, or retrieve it through the SDKs, providing you with a fully realized version of your prompt.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/playground-snippets.gif?s=a6724049e91b98d3db3b768c50a8246d" alt="Rendering snippets" data-og-width="868" width="868" data-og-height="480" height="480" data-path="images/playground-snippets.gif" data-optimize="true" data-opv="3" />

*Rendering snippets from the Playground*

### Webhooks

When you update a snippet, there will be a webhook of type `prompt_template_updated` for all of the templates that import the snippet.

## Visualizing Snippets in Templates

When editing a prompt that contains snippets, you'll see the snippet references as strings in the format described above, depending on how you've chosen to reference them.

When you open a prompt template from the Registry, you'll see it as a clickable pill that will take you to the referenced version.

<img src="https://mintcdn.com/promptlayer/jUVR1Bx755pIFGwB/images/snippet-pill.gif?s=75aca77b3d8d398dfea40d78559ace9d" alt="Clicking a snippet" data-og-width="704" width="704" data-og-height="480" height="480" data-path="images/snippet-pill.gif" data-optimize="true" data-opv="3" />

*Navigating to a snippet*

## Why snippets?

By leveraging snippets, you can create a more maintainable and scalable prompt management system, allowing for greater flexibility and efficiency in your prompt template creation process.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.promptlayer.com/llms.txt