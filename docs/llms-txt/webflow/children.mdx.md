# Source: https://developers.webflow.com/designer/reference/elements/children.mdx

***

title: Children
slug: designer/reference/elements/children
description: >-
Retrieve and insert child elements, offering programmatic ways to change page
structure.
hidden: false
'og:title': 'Webflow Designer APIs: Element children'
'og:description': >-
Retrieve and insert child elements, offering programmatic ways to change page
structure.
----------

Correctly handling an element's child elements is crucial for keeping the [element hierarchy](https://university.webflow.com/lesson/element-hierarchy?topics=getting-started) organized. These Element methods let you retrieve and insert child elements, offering programmatic ways to change page structure.

To effectively use these methods, check if an element has its `Children` property set to `true`. This property is read-only, so it's important to use elements that have this attribute. Using these methods with elements that don't have this property will return an error.

<video autoplay loop muted>
    

  <source src="https://dhygzobemt712.cloudfront.net/Web/developers/videos/24005_API%20Documentation_Children.webm" type="video/webm" />

    Your browser does not support HTML video.
</video>

## Methods

The Children property supports the following methods:

<CardGroup>
  <Card title="Get children" href="/designer/reference/element-children/getChildren">
    Get child elements from a parent element in the element hierarchy.
  </Card>

  <Card title="Prepend" href="/designer/reference/element-children/prepend">
    Insert a new element onto the page as the first child of the target element.
  </Card>

  <Card title="Append" href="/designer/reference/element-children/append">
    Insert a new element onto the page as the last child of the target element.
  </Card>
</CardGroup>
