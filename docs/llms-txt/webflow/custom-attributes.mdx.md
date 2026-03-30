# Source: https://developers.webflow.com/designer/reference/elements/custom-attributes.mdx

***

title: Custom Attributes
slug: designer/reference/elements/custom-attributes
description: 'Attach additional, specialized data to elements with custom attributes.'
hidden: false
'og:title': 'Webflow Designer API: Custom Attributes'
'og:description': 'Attach additional, specialized data to elements with custom attributes.'
-------------------------------------------------------------------------------------------

In Webflow, you can use native elements, styles, and settings to create standard HTML attributes like `href`, `class`, and `id`.

However, [Custom Attributes](https://university.webflow.com/lesson/custom-attributes?topics=elements) extend this capability. Custom attributes allow developers to attach additional, specialized data to elements, helping broaden the scope of a site's functionality and interactivity. In Webflow,  they are especially useful for enriching custom code, [particularly when integrated with CMS data.](https://university.webflow.com/lesson/custom-attributes?topics=elements#how-to-use-cms-data-in-custom-attributes)

To use the methods below, choose an element with a `CustomAttributes` property of `true`. Using these methods with elements that don't have this property will return an error.

## Methods

<CardGroup>
  <Card title="Get All Custom Attributes" href="/designer/reference/custom-attributes/getAllCustomAttributes">
    Get all custom attributes for an element.
  </Card>

  <Card title="Get Custom Attribute" href="/designer/reference/custom-attributes/getCustomAttribute">
    Get a custom attribute for an element by name.
  </Card>

  <Card title="Set Custom Attribute" href="/designer/reference/custom-attributes/setCustomAttribute">
    Set a custom attribute for an element.
  </Card>

  <Card title="Remove Custom Attribute" href="/designer/reference/custom-attributes/removeCustomAttribute">
    Remove a custom attribute from an element.
  </Card>
</CardGroup>
