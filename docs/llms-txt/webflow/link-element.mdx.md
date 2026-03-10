# Source: https://developers.webflow.com/designer/reference/link-element.mdx

***

title: Link Element
slug: designer/reference/link-element
description: ''
hidden: false
-------------

The Link element represents a [Link Block](https://university.webflow.com/lesson/link-block?topics=elements) in the Webflow Designer. Create a link element using any of the listed presets.

## Supported presets

The following presets create link elements.

* [LinkBlock](/designer/reference/element-presets)
* [TextLink](/designer/reference/element-presets)
* [Button](/designer/reference/element-presets)
* [LinkBlock](/designer/reference/element-presets)

## Methods

You can get and set the target value of a link element using the following methods.

<CardGroup>
  <Card title="Get Link Target" href="/designer/reference/link-element/getTarget">
    Get the target value of the link block element.
  </Card>

  <Card title="Set Link Settings" href="/designer/reference/link-element/setSettings">
    Apply settings for a Link Block element.
  </Card>
</CardGroup>

{" "}

# Properties

| Property           | Description                                                                                       | Type      | Example                                                 |
| :----------------- | :------------------------------------------------------------------------------------------------ | :-------- | :------------------------------------------------------ |
| `id`               | Unique identifier for the element composed of two identifiers, the `component `and the `element`. | `object`  | `{component: "64c813...", element: "5edf8e59-71f9..."}` |
| `type`             | Specifies the type of the element.                                                                | `string`  | "Link"                                                  |
| `children`         | Indicates whether the element can contain child elements.                                         | `boolean` | `false`                                                 |
| `customAttributes` | Indicates whether the element can have custom attributes.                                         | `boolean` | `true`                                                  |
| `styles`           | Indicates whether the element can contain styles.                                                 | `boolean` | `true`                                                  |
| `textContent`      | Indicates whether the element can contain text content                                            | `boolean` | `false`                                                 |
