# Source: https://developers.webflow.com/designer/reference/elements/styles.mdx

***

title: Styles
slug: designer/reference/elements/styles
description: ''
hidden: false
'og:title': 'Webflow Designer API: Styling Elements'
'og:description': >-
The methods described below give you direct control over which styles are
applied to elements, letting you change a page's appearance and layout as
needed. To directly manage CSS properties within a Style Object, use the Style
Methods.
--------

Styles are key to creating dynamic and responsive designs in Webflow.

Styles are managed through [Classes](https://university.webflow.com/lesson/style-panel-overview?topics=layout-design#classes-overview) in the Designer interface. When working with the API, these Classes are represented as [Style Objects](/designer/reference/styles-overview) that contain CSS properties. The methods in this section allow you to programmatically control which styles are applied to elements.

<Card
  title="Style Objects"
  href="/designer/reference/styles-overview"
  icon={
        <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/48px/Styles.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/48px/Styles.svg" alt="" className="block dark:hidden" />
        </>
    }
  iconPosition="left"
>
  Learn more about managing CSS properties with [Style Methods](/designer/reference/styles-overview)
</Card>

## Methods

The Styles property supports the following methods:

<CardGroup>
  <Card title="Get styles" href="/designer/reference/element-styles/getStyles">
    Retrieve the current style properties of the element for analysis or changes.
  </Card>

  <Card title="Set styles" href="/designer/reference/element-styles/setStyles">
    Set styles on an element.
  </Card>
</CardGroup>
