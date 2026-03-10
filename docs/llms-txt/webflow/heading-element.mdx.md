# Source: https://developers.webflow.com/designer/reference/heading-element.mdx

***

title: Heading Element
slug: designer/reference/heading-element
description: ''
hidden: false
'og:title': 'Webflow Designer API: Heading Element'
'og:description': >-
The Heading element represents an element within the Webflow Designer. The
following methods are specific to Heading elements.
---------------------------------------------------

The Heading element represents an Headings the Webflow Designer. Create a Heading element using the [Heading element preset](/designer/reference/element-presets).

## Methods

You can get and set the heading level of a heading element using the following methods:

<CardGroup>
  <Card title="Get Heading Level" href="/designer/reference/heading-element/getHeadingLevel">
    Retrieves the heading level of a heading element.
  </Card>

  <Card title="Set Heading Level" href="/designer/reference/heading-element/setHeadingLevel">
    Set the heading level of a heading element.
  </Card>
</CardGroup>

{" "}

## Properties

| Property           | Description                                                                                       | Type      | Example                                                 |
| :----------------- | :------------------------------------------------------------------------------------------------ | :-------- | :------------------------------------------------------ |
| `id`               | Unique identifier for the element composed of two identifiers, the `component `and the `element`. | `object`  | `{component: "64c813...", element: "5edf8e59-71f9..."}` |
| `type`             | Specifies the type of the element.                                                                | 'string'  | 'Heading'                                               |
| `children`         | Indicates if the element can contain child elements.                                              | `boolean` | `true`                                                  |
| `customAttributes` | Indicates if the element can contain custom attributes.                                           | `boolean` | `true`                                                  |
| `styles`           | Indicates if the element can contain styles.                                                      | `boolean` | `true`                                                  |
| `textContent`      | Indicates if the element can contain text content                                                 | `boolean` | `true`                                                  |
