# Source: https://developers.webflow.com/designer/reference/dom-element.mdx

***

title: DOM Element
slug: designer/reference/dom-element
description: >-
The custom element, also known as the DOM Element, is a placeholder element
that you can add any HTML custom attribute, tag, or text to — thereby
“creating” that element on the canvas.
hidden: false
'og:title': 'Webflow Designer API: DOM Element'
'og:description': >-
The custom element, also known as the DOM Element, is a placeholder element
that you can add any HTML custom attribute, tag, or text to — thereby
“creating” that element on the canvas.
--------------------------------------

The [custom element](https://university.webflow.com/lesson/custom-element?topics=elements), also known as the DOM Element, is a placeholder element that you can add any HTML custom attribute, tag, or text to — thereby "creating" that element on the canvas. This is useful for adding HTML elements to the canvas that aren't available as native Webflow elements.

Once you add the custom element to the canvas, you're able to use the below methods, which are only available to the DOM element, as well as the more general element methods to manage children, styles, and text content.

## Methods

The DOM Element supports the following specific methods:

<CardGroup>
  <Card title="Get HTML Tag" href="/designer/reference/dom-element/getTag">
    Retrieve the HTML tag of the element.
  </Card>

  <Card title="Set HTML Tag" href="/designer/reference/dom-element/setTag">
    Set the value of the specified HTML tag of the DOMElement.
  </Card>

  <Card title="Get All Attributes" href="/designer/reference/dom-element/getAllAttributes">
    Retrieve all HTML attributes for the DOMElement.
  </Card>

  <Card title="Get Attribute" href="/designer/reference/dom-element/getAttribute">
    Retrieve the value of the named HTML attribute of the DOMElement.
  </Card>

  <Card title="Set Attribute" href="/designer/reference/dom-element/setAttribute">
    Set the value of the specified HTML attribute of the DOMElement.
  </Card>

  <Card title="Remove Attribute" href="/designer/reference/dom-element/removeAttribute">
    Remove the specified HTML attribute from the DOMElement.
  </Card>
</CardGroup>

## Properties

| Property           | Description                                                                                       | Type      | Example                                                 |
| :----------------- | :------------------------------------------------------------------------------------------------ | :-------- | :------------------------------------------------------ |
| `id`               | Unique identifier for the element composed of two identifiers, the `component `and the `element`. | `object`  | `{component: "64c813...", element: "5edf8e59-71f9..."}` |
| `type`             | Specifies the type of the element.                                                                | `string`  | "DOM"                                                   |
| `styles`           | Indicates whether the element can contain styles.                                                 | `boolean` | `true`                                                  |
| `children`         | Indicates whether an element can contain child elements.                                          | `boolean` | `true`                                                  |
| `textContent`      | Indicates whether an element can contain text content.                                            | `boolean` | `true`                                                  |
| `customAttributes` | Indicates whether an element can contain custom attributes.                                       | `boolean` | `false`                                                 |
