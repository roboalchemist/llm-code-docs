# Source: https://developers.webflow.com/browser/optimize/onVariationRecorded.mdx

***

title: Recording Variations
slug: optimize/onVariationRecorded
description: Get recorded variations and send them to an external service
hidden: false
'og:title': Recording Variations
'og:description': Get recorded variations and send them to an external service
------------------------------------------------------------------------------

## `wf.onVariationRecorded()`

Registers a callback function that executes whenever a variation runs successfully on your page. This is useful for integrating Webflow Optimize's experiment data with external analytics services.

{/* <!-- vale off --> */}

<Note>
  Before using this method, make sure you've [created and published at least one variation in Webflow.](https://help.webflow.com/hc/en-us/articles/33776880496275-Create-or-edit-optimization-variations)
</Note>

{/* <!-- vale on --> */}

### Syntax

```javascript
wf.onVariationRecorded(function(result))
```

### Parameters

* **`function(result)`**: *function* - A callback function that receives a `result` object containing information about the variation.
  {/* <!-- vale off --> */}
  <Warning>
    The callback function will only trigger for variations that run after it has been registered on the page.
  </Warning>
  {/* <!-- vale on --> */}

### Example implementation

```javascript
// Call wf.ready() to ensure the Browser API is available
wf.ready(function(){
    // Register the callback function inside wf.ready()
    wf.onVariationRecorded(function(result){
      console.log(result) // Log the result to the console
    })
})
```

### Returns

A success callback which includes the results of the successful variation.

**Object properties**

| Property         | Type                       | Description                                                                                                              |
| ---------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| `experienceId`   | `string`                   | Unique identifier for the experience/experiment                                                                          |
| `experienceName` | `string`                   | Display name of the experience/experiment                                                                                |
| `experienceType` | `'ab' \| 'rbp' \| 'cc'`    | Type of experience: A/B Test (`ab`), Rules-Based Personalization (`rbp`), or Content Configuration (`cc`)                |
| `variationId`    | `string`                   | Unique identifier for the specific variation                                                                             |
| `variationName`  | `string`                   | Display name of the variation                                                                                            |
| `ccStatus`       | `'holdout' \| 'optimized'` | For Content Configuration experiences only: indicates if the user is in the holdout group or receiving optimized content |

#

### Example

```json
{
    "experienceId": "417228929",
    "experienceName": "Hero Optimization",
    "experienceType": "rbp",
    "variationId": "617106113",
    "variationName": "Desktop",
    "ccStatus": "optimized"
}
```

## FAQs

{/* <!-- vale off --> */}

<AccordionGroup>
  <Accordion title="When should you call `onVariationRecorded()`?">
    {/* <!-- vale on --> */}

    To make sure your callback fires, call `onVariationRecorded()` as early as possible to guarantee it's registered before Webflow returns any recorded variations. Preferably, before the DOM starts rendering. This prevents the callback from missing any variations. To illustrate:

    <Frame>
      <img src="https://files.buildwithfern.com/https://webflow.docs.buildwithfern.com/a76a5dbf7d3368d177cfaa848d9753c3eabca61b88a0796be9bffdc7249bbf7d/products/browser/pages/Optimize/variations/assets/optimize-diagram.png" alt="Timing your script to run after a variation is recorded" />
    </Frame>

    We recommend adding the API call in before the closing `</head>` tag of your site or page using Webflow's [Custom Code](https://help.webflow.com/hc/en-us/articles/33961357265299-Custom-code-in-head-and-body-tags) feature. Or, if using a tool like Google Tag Manager, add the API call when configuring the tag.

    {/* <!-- vale off --> */}
  </Accordion>

  <Accordion title="When is a variation considered recorded?">
    {/* <!-- vale on --> */}

    A variation is considered recorded when the page loads and the variation has been displayed to the user. You can review the full logic that leads up to a recorded variation [in this help article](https://help.webflow.com/hc/en-us/articles/33776880496275-Create-or-edit-variations). A simplified version of the logic is as follows:

    * A variation is selected by Webflow Optimize
    * That variation is applied to the page
    * Events, like the selected variation and integrated analytics, are sent asynchronously
    * Webflow Optimize records the variation

    {/* <!-- vale off --> */}
  </Accordion>

  <Accordion title="How often do callbacks fire?">
    {/* <!-- vale on --> */}

    Each time a variation is recorded, the callback fires. You may have multiple variations on a page, so the callback will fire once for each variation.

    {/* <!-- vale off --> */}
  </Accordion>
</AccordionGroup>

{/* <!-- vale on --> */}
