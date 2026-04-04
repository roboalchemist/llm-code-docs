# Source: https://developers.webflow.com/browser/introduction.mdx

***

title: Browser API
slug: introduction
layout: overview
description: Introduction to the Webflow Browser API
hidden: true
hide-toc: true
'og:title': 'Introduction: Webflow Browser API'
'og:description': Introduction to the Webflow Browser API
subtitle: Introduction to the Webflow Browser API
-------------------------------------------------

The Browser API lets you control Webflow Analyze and Optimize features directly from your site's JavaScript. Use it to manage consent, track experiments, and personalize user experiences.

<Note title="Analyze or Optimize required">
  The Browser API is available only on sites with Webflow Analyze or Optimize enabled and tracking turned on.
  To enable tracking, open the **Insights** tab. Under **Settings**, click **Tracking**, then turn on the **Start tracking visitor data** toggle.
</Note>

## What you can do with the Browser API

<CardGroup>
  <Card
    title="Manage consent"
    iconPosition="left"
    href="/browser/reference/consent-management"
    iconSize="12"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/OptimizeUser.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/OptimizeUser.svg" alt="" className="light-icon" />
            </>
        }
  >
    Manage user consent and privacy preferences in real time
  </Card>

  <Card
    title="Track variations"
    iconPosition="left"
    href="/browser/optimize/variations"
    iconSize="12"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Test.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Test.svg" alt="" className="light-icon" />
            </>
        }
  >
    Send optimization variations from experiments to third-party tools
  </Card>

  <Card
    title="Personalize experiences with custom attributes"
    iconPosition="left"
    iconSize="12"
    href="/browser/optimize/attributes"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/SitePersonalization.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/SitePersonalization.svg" alt="" className="light-icon" />
            </>
        }
  >
    Set custom attributes based on user behavior and data
  </Card>

  <Card
    title="Track custom goals"
    iconPosition="left"
    iconSize="12"
    href="/browser/custom-goals"
    icon={  
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Test.svg" alt="" className="dark-icon" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Test.svg" alt="" className="light-icon" />
            </>
        }
  >
    Track on-site and off-site conversions with custom goals
  </Card>
</CardGroup>

## Getting started

<Steps>
  ### Choose where to add your code

  You can use the Browser API by adding JavaScript in one of two ways:

  * **Directly in your site**
    Add a script before the closing `</head>` tag using Webflow's [custom code settings](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags).
    *Best for simple use cases.*

  * **With Google Tag Manager (or similar)**
    Add a script as a [custom tag](https://support.google.com/tagmanager/answer/6107167?hl=en).
    *Recommended for advanced tracking or integrations.*

  ### Wait for the API to be ready

  Wrap your code in [`wf.ready()`](/browser/reference/wf-ready) to ensure the API has loaded before you call any methods:

  ```javascript
  wf.ready(function() {
    // Your code here
  });
  ```

  ### Start building

  Once inside `wf.ready()`, you can call any Browser API methods to manage consent, track variations, set custom attributes, or track custom goals.

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
      // Track a custom goal
      wf.sendEvent('purchase', { value: 149.99 });
  });
  ```
</Steps>

## FAQs

{/* <!-- vale off --> */}

<Accordion title="What is the Browser API?">
  {/* <!-- vale on --> */}

  The Browser API is a JavaScript API that allows you to interact with Webflow features directly in the browser. It provides methods to retrieve Optimize variations, set custom attributes, and handle other Webflow features.

  {/* <!-- vale off --> */}
</Accordion>

<Accordion title="How do I add the Browser API to my site?">
  {/* <!-- vale on --> */}

  The Browser API is automatically included on all Webflow sites with Analyze and Optimize enabled, and handles loading the necessary code in an optimized way to minimize impact on page performance.

  {/* <!-- vale off --> */}
</Accordion>

<Accordion title="How do I use the Browser API?">
  {/* <!-- vale on --> */}

  The Browser API is available through the global `wf` object in your browser. You can access the API by adding a script using [custom code](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags) on your sites and pages or through external services that load scripts on your site like Google Tag Manager.

  The API can be called from any JavaScript code running on your site.

  {/* <!-- vale off --> */}
</Accordion>
