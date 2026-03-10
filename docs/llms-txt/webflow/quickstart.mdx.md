# Source: https://developers.webflow.com/browser/optimize/quickstart.mdx

***

title: Quickstart
subtitle: Making requests to Optimize via the Browser API
slug: optimize/quickstart
description: 'Quickstart: Making requests to the Webflow Optimize via the Browser API'
hidden: false
hide-nav-links: true
'og:title': 'Quickstart: Making requests to Optimize via the Browser API'
'og:description': 'Quickstart: Making requests to Webflow Optimize via the Browser API'
---------------------------------------------------------------------------------------

This guide will help you get started making requests to Webflow Optimize through the Browser API. It will walk you through the process of creating a script and adding Optimize methods as callbacks.

<Note title="No installation required">
  The Browser API is automatically enabled on your site with no manual installation required. The Optimize methods are available through the global 

  `wf`

   object in your browser.
</Note>

## Prerequisites

* A Webflow site with [Optimize enabled](https://university.webflow.com/videos/start-optimizing-your-site-with-webflow-optimize)
* Ability to add [custom JavaScript](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags) to your site or use a tool like [Google Tag Manager](https://support.google.com/tagmanager/answer/6107167?hl=en)

## Getting started with the Optimize Browser APIs

There are two main approaches to implementing your Optimize code:

1. **Add code directly to your site**: Place your script in the `<head>` section of your site using Webflow's [Custom Code](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags) feature.
2. **Use Google Tag Manager**: Add the API call when configuring a custom tag

<Steps>
  ### Call `wf.ready()`

  Since the Webflow Browser API loads asynchronously, you need to ensure your code runs at the right time by using `wf.ready()`.

  ```javascript
  // Call wf.ready() to ensure the Browser API is available
  wf.ready(function() {
      // Your code here
  });
  ```

  Add this call to the `<head>` section of your site or page using Webflow's [Custom Code](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags) feature. Or, if using a tool like Google Tag Manager, add the API call when configuring the tag. Adding the call early ensures you won't miss any events on the page.

  {/* <!-- vale off --> */}

  <Accordion title="When should you call wf.ready() ?">
    {/* <!-- vale on --> */}

    To make sure your callback fires, call `wf.ready()` as early as possible to guarantee it's registered before Webflow Optimize returns any time sensitive events. Preferably, before the DOM starts rendering. This prevents the callback from missing any events. To illustrate:

    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/a76a5dbf7d3368d177cfaa848d9753c3eabca61b88a0796be9bffdc7249bbf7d/products/browser/pages/Optimize/variations/assets/optimize-diagram.png" alt="Timing your script to run after a variation is recorded" />
    </Frame>

    We recommend adding the API call in before the closing `</head>` tag on your site or page using Webflow's [Custom Code](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags) feature. Or, if using a tool like Google Tag Manager, add the API call when configuring the tag.

    {/* <!-- vale off --> */}
  </Accordion>

  {/* <!-- vale on --> */}

  ### Add callbacks to `wf.ready()`

  Now you can start adding callbacks to your script to [retrieve variations](/browser/optimize/variations) and [set custom attributes.](/browser/optimize/attributes)

  <Tabs>
    <Tab title="Multiple callbacks">
      You can add multiple callbacks in `wf.ready()` to handle different Optimize functionality in a single script. This enables you to efficiently manage multiple operations like retrieving variations and setting attributes in one place. Each callback will execute once the Webflow Browser API is ready.

      **Example:**

      ```javascript
      // Call wf.ready() to ensure the Browser API is available
      wf.ready(function() {
          // Retrieve variations
          wf.onVariationRecorded(function(result){
              // Do something with the result
              console.log(result);
          });

          // Set custom attributes
          wf.setAttributes("user",{
              userSegment: 'enterprise',
              userRole: 'technicalBuyer'
          });
      });
      ```
    </Tab>

    <Tab title="Multiple API calls per page">
      You can include multiple `wf.ready()` API calls on the same page to organize your code and handle different Optimize functionality separately. Each callback will execute in the order they appear, allowing you to intersperse other page code between API calls. This gives you flexibility in structuring your code while maintaining proper execution order.

      **Example:**

      ```javascript
      // Call wf.ready() to ensure the Browser API is available
      wf.ready(function() {
          wf.onVariationRecorded(function(result) {
              // do something with result
              console.log(result);
      }, function(error) {
          // do something with error
          console.error(error);
      });
      });

      // Other page code
      wf.ready(function() {
          wf.setAttributes(scope, attributes);
      });
      ```
    </Tab>
  </Tabs>
</Steps>

## Next steps

Now that you're familiar with making requests to the Browser API, you can learn more about Optimize methods to add to your callbacks:

<CardGroup>
  <Card
    title="Track variations"
    iconPosition="left"
    href="/browser/optimize/variations"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Test.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Test.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Send variations from Optimize experiments to third-party tools
  </Card>

  <Card
    title="Personalize experiences with custom attributes"
    iconPosition="left"
    href="/browser/optimize/attributes"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/OptimizeUser.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/OptimizeUser.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Set custom attributes to personalize experiences based on user behavior and data
  </Card>
</CardGroup>
