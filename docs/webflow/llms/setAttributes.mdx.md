# Source: https://developers.webflow.com/browser/optimize/setAttributes.mdx

***

title: Set attributes
slug: optimize/setAttributes
description: Set attributes for the current user or page view
hidden: false
'og:title': Set attributes
'og:description': Set attributes on for the current user or page view
---------------------------------------------------------------------

## `wf.setAttributes(scope, attributes)`

Set custom attributes for the current user or page view.

<Note title="Create a custom attribute in Webflow Optimize">
  Before setting a custom attribute and sending it to Webflow Optimize, you need to create the attribute in the **Insights > Integrations > Custom JavaScript attributes** section of your site. See [Creating custom attributes in Webflow Optimize](/browser/optimize/attributes#configuring-custom-attributes) for more information.
</Note>

### Syntax

```typescript
wf.setAttributes(scope: 'user' | 'pageview', attributes: {[attributeName: string]: attributeValue: string})
```

### Parameters

* **scope**: `'user'` | `'pageview'` - The scope of the attributes. You can choose to set attributes for the current user or the current page view.
* **attributes**: `{[attributeName: string]: attributeValue: string}` - An object containing key-value pairs of attributes to set. The attribute name must be less than 40 characters long and may not contain a “=” character

### Example implementation

```javascript
// Call the wf.ready() function to ensure the script is loaded before setting attributes
wf.ready(function() {
  // Set attributes for the current user
  wf.setAttributes('user', {
    userSegment: 'enterprise'
  })
})
```

### Returns

This method doesn't return a value to the client. Instead, it sends the attributes to Webflow Optimize, which records in the user or page view data in the dashboard. See more on [using custom attributes](/browser/optimize/attributes#targeting-visitors-with-custom-attributes) in the Optimize documentation.

### FAQs

{/* <!-- vale off --> */}

<AccordionGroup>
  <Accordion title="Can I use boolean and number values for attribute values?">
    {/* <!-- vale on --> */}

    `wf.setAttributes()` attempts to convert values from types like boolean and number into strings for convenience. Don't rely on this conversion and always pass in string values for attributes.

    {/* <!-- vale off --> */}
  </Accordion>

  <Accordion title="Why am I not seeing my attributes in my audience data?">
    {/* <!-- vale on --> */}

    Be sure to create the attribute in the **Insights > Integrations > Custom JavaScript attributes** section of your site before sending custom attributes to Webflow Optimize. See [Creating custom attributes in Webflow Optimize](/browser/optimize/attributes#creating-custom-attributes-in-webflow-optimize) for more information.

    <Note title="Enterprise sites only">
      This method is only available on enterprise sites.
    </Note>

    {/* <!-- vale off --> */}
  </Accordion>
</AccordionGroup>

{/* <!-- vale on --> */}
