# Source: https://developers.webflow.com/designer/reference/component-element.mdx

***

title: Component Instances
slug: designer/reference/component-element
description: ''
hidden: false
'og:title': 'Webflow Designer API: Component Element'
'og:description': >-
The Component element represents a component instance within the Webflow
Designer.
---------

The component element represents a [component instance](/designer/reference/components-overview#component-instance) within the Webflow Designer.

## Methods

You can get the associated component definition of a component instance using the following method:

<Card title="Get Component" href="/designer/reference/component-element/getComponent">
  Retrieves the associated component definition of the component instance.
</Card>

<Card
  title="Creating & managing components"
  href="/designer/reference/components-overview"
  icon={
    <>
    <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Components.svg" alt="" className="hidden dark:block" />
    <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Components.svg" alt="" className="block dark:hidden" />
    </>
  }
  iconPosition="left"
  iconSize="12"
>
  Learn more about creating and managing component definitions in the [Components Overview](/designer/reference/components-overview).
</Card>

## Properties

| Property           | Description                                                                                       | Type      | Example                                                 |
| :----------------- | :------------------------------------------------------------------------------------------------ | :-------- | :------------------------------------------------------ |
| `id`               | Unique identifier for the element composed of two identifiers, the `component `and the `element`. | `object`  | `{component: "64c813...", element: "5edf8e59-71f9..."}` |
| `type`             | Specifies the type of the element.                                                                | `string`  | "ComponentInstance"                                     |
| `children`         | Indicates whether the element can contain child elements.                                         | `boolean` | `false`                                                 |
| `customAttributes` | Indicates whether the element can have custom attributes.                                         | `boolean` | `false`                                                 |
| `styles`           | Indicates whether the element can contain styles.                                                 | `boolean` | `false`                                                 |
| `textContent`      | Indicates whether the element can contain text content                                            | `boolean` | `false`                                                 |
