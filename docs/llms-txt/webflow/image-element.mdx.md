# Source: https://developers.webflow.com/designer/reference/image-element.mdx

***

title: Image Element
slug: designer/reference/image-element
description: ''
hidden: false
-------------

The Image element represents an [image](https://university.webflow.com/lesson/image?topics=elements) in the Webflow Designer. Create an Image element using the [Image element preset](/designer/reference/element-presets).

## Methods

You can get and set the asset and alt text of an image element using the following methods:

<CardGroup>
  <Card title="Get Asset" href="/designer/reference/image-element/getAsset">
    Retrieve an asset from an Image element.
  </Card>

  <Card title="Set Asset" href="/designer/reference/image-element/setAsset">
    Add an asset to an Image element.
  </Card>

  <Card title="Get Alt Text" href="/designer/reference/image-element/getAltText">
    Retrieve the alt text for an Image element on the canvas.
  </Card>

  <Card title="Set Alt Text" href="/designer/reference/image-element/setAltText">
    Set the Alt Text for an Image element on the canvas.
  </Card>
</CardGroup>

{" "}

# Properties

| Property           | Description                                                                                               | Type      | Example                                                 |
| :----------------- | :-------------------------------------------------------------------------------------------------------- | :-------- | :------------------------------------------------------ |
| `id`               | Unique identifier for the element composed of two identifiers, the `component `and the `element`.         | `object`  | `{component: "64c813...", element: "5edf8e59-71f9..."}` |
| `type`             | Specifies the type of the element.                                                                        | `string`  | "Image"                                                 |
| `children`         | Indicates whether the element can contain child elements.                                                 | `boolean` | `false`                                                 |
| `customAttributes` | Indicates whether the element can have custom attributes.                                                 | `boolean` | `true`                                                  |
| `styles`           | Indicates whether the element can contain styles.                                                         | `boolean` | `true`                                                  |
| `textContent`      | Indicates whether the element can contain text content                                                    | `boolean` | `false`                                                 |
| `appConnections`   | Indicates whether the element supports [App Connections](/designer/reference/app-intents-and-connections) | `boolean` | `true`                                                  |
