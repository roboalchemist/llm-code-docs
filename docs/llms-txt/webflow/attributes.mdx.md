# Source: https://developers.webflow.com/browser/optimize/attributes.mdx

***

title: Custom attributes
slug: optimize/attributes
description: An overview of custom attributes in Webflow Optimize
hidden: false
'og:title': Custom attributes
'og:description': An overview of custom attributes in Webflow Optimize
----------------------------------------------------------------------

Attributes are different characteristics associated with your visitors (for example, demographics, behavior, etc.).

If you want to target anything that isn't available by default, you can use custom attributes to store and retrieve data about your visitors. Once a custom attribute is defined and set on a page visit, you can leverage it to [define a rules-based audience](https://help.webflow.com/hc/en-us/articles/34167397653523-Create-or-edit-a-rules-based-audience) or [filter optimization results by the attribute](https://help.webflow.com/hc/en-us/articles/34167118964883-Review-your-optimization-results).

## How custom attributes work

Custom attributes are first defined in Webflow Optimize, and then set for a user or pageview by using the [`wf.setAttributes()`](/browser/optimize/setAttributes) method of the Browser API. By setting an attribute, you're sending data to Webflow Optimize that can be used to [create a rules-based audience](https://help.webflow.com/hc/en-us/articles/34167397653523-Create-or-edit-a-rules-based-audience) or [filter optimization results](https://help.webflow.com/hc/en-us/articles/34167118964883-Review-your-optimization-results#01J9WN67STDYG61SRKX2HEAZZE).

## Configuring custom attributes

<Steps>
  ### Create a custom attribute in Webflow Optimize

  If you have an enterprise site, navigate to the **Insights** tab on your site and click **Integrations**. Find the **Custom JavaScript attributes** section and create a new entry.

  <Frame>
    ![Custom JavaScript attributes](https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/b87e2da2c34a5d54d8dcb5f2898143a627b333aa19f3c4cc08cffaa0e26c53bf/products/browser/pages/Optimize/attributes/assets/custom-attributes.png)
  </Frame>

  <Note title="Enterprise sites only">
    This method is only available on enterprise sites.
  </Note>

  ### Set a custom attribute using the Browser API

  Once configured, you can set custom attributes when a user visits your site by using [`wf.setAttributes()`](/browser/optimize/setAttributes). See the example below, and the [documentation for more details.](/browser/optimize/setAttributes)

  #### Scopes

  Custom attributes can be set for a specific scope, which determines the lifetime of the attribute.

  * **Pageview**: The attribute is available for the duration of a pageview.
  * **User**: The attribute is available for the duration of a user's session. A session begins when the visitor arrives on your site and ends after 30 minutes of sustained inactivity (like when the visitor stops engaging with your website).

  **Example:**

  ```javascript
  // Call wf.ready() to ensure the Browser API is available
  wf.ready(function() {
      // Set custom attributes
      wf.setAttributes("user", {
          customerSegment: 'enterprise',
          userRole: 'technicalBuyer'
      });
  });
  ```
</Steps>

## Using custom attributes in Optimize

Once you've created and set a custom attribute, you can use it to create a rules-based audience or filter optimization results.

<CardGroup>
  <Card
    title="Create a rules-based audience"
    href="https://help.webflow.com/hc/en-us/articles/34167397653523-Create-or-edit-a-rules-based-audience"
    icon={
    <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/TeamLarge.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/TeamLarge.svg" alt="" className="block dark:hidden" />
    </>
}
  >
    Create a rules-based audience to target visitors based on their custom attributes.
  </Card>

  <Card
    title="Filter optimization results"
    href="https://help.webflow.com/hc/en-us/articles/34167118964883-Review-your-optimization-results#01J9WN67STDYG61SRKX2HEAZZE"
    icon={
    <>
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Test.svg" alt="" className="hidden dark:block" />
        <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Test.svg" alt="" className="block dark:hidden" />
    </>
}
  >
    Filter optimization results by custom attributes.
  </Card>
</CardGroup>

## Looking for more information?

Visit the [Webflow Help Center](https://help.webflow.com/hc/en-us/articles/34167397653523-Create-or-edit-a-rules-based-audience) to learn more about custom attributes and audiences in Webflow Optimize, including:

* Creating and managing custom attributes
* Building rules-based audiences
* Targeting visitors with custom attributes
* Best practices for audience segmentation
* Enterprise-specific features and capabilities

You can also explore [Webflow University](https://university.webflow.com/videos/start-optimizing-your-site-with-webflow-optimize) for additional tutorials and resources on making the most of Webflow Optimize's personalization features.
