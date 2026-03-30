# Source: https://developers.webflow.com/designer/reference/elements-overview.mdx

***

title: Elements
slug: designer/reference/elements-overview
description: >-
Comprehensive guide to creating and managing elements in the Webflow Designer
with the Designer API
hidden: false
'og:title': 'Webflow Designer APIs: Elements'
'og:description': >-
Element APIs allow you to create and manage Elements in the Designer. Learn
about element types, properties, methods, and best practices.
-------------------------------------------------------------

The Element APIs allow apps to programmatically create and manage elements. Through these APIs, you can dynamically build and modify a site's structure, apply styles to elements, and control their behavior.

<video autoplay loop muted>
    

  <source src="https://dhygzobemt712.cloudfront.net/Web/developers/videos/24005_API%20Documentation_Get%20Selected%20Element.webm" type="video/webm" />

    Your browser doesn't support HTML video.
</video>

## What Are Elements?

Elements are the building blocks of Webflow designs. Each element represents a component in your design, from basic structural elements like sections and containers to content elements like text and images.

The Designer API gives you programmatic control over these elements, allowing you to:

* Create new elements and add them to the canvas
* Select and manipulate existing elements
* Apply styles and customize element properties
* Build and modify complex element hierarchies

## Getting Started with Elements

Working with elements in the Designer API involves three main concepts:

<CardGroup>
  <Card
    title="Creating & retrieving elements"
    href="/designer/reference/creating-retrieving-elements"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Flexbox.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Flexbox.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Learn how to create, select, and manipulate elements in the Webflow Designer.
  </Card>

  <Card
    title="Element properties & methods"
    href="/designer/reference/element-properties-methods"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Controls.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Controls.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Explore the properties of each element and the methods associated with them.
  </Card>

  <Card
    title="Element types & methods"
    href="/designer/reference/element-types-methods"
    icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Responsive.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Responsive.svg" alt="" className="block dark:hidden" />
        </>
    }
    iconSize="12"
    iconPosition="left"
  >
    Discover the different element types and their specific methods.
  </Card>
</CardGroup>
