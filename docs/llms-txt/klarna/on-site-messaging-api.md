# Source: https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-api.md

# On-site messaging API integration

## This document describes the integration steps needed to make use of the Klarna On-site messaging API.

To integrate On-site messaging on your site please make sure you meet the prerequisites as well as you follow steps in this page.


![ Diagram of an example of integration](0b161090-f957-4249-aa52-100bdbab83ad_745fe1e3a1f5f69b15886c268961574c.jpeg)
*Diagram of an example of integration*

## Prerequisites

- On-site messaging is already activated for your e-store. [How to activate On-site messaging](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/integrate-using-klarna-web-sdk/#step-1-activation)?. 
- On-site messaging API access is enabled for your e-store. The API is not activated by default, you need to request access. Please reach out to your Klarna account manager. Otherwise the OSM API backend will return a **403 - Forbidden** response.

**If you are looking forward to integrate On-site messaging in your e-commerce, please integrate OSM with our plugins or via Web SDK always that possible.** API integration enables limited capabilities and should only be used as an alternative in case Web SDK integration is not possible.

## Step 1: Obtain your OSM client-id

Get your client-id from the On-site messaging section in the Klarna Merchant Portal (if you don't have access to Merchant Portal please ask your account manager for it). This client-id is used by OSM to identify your e-store in multiple regions.

## Step 2: Make HTTPS GET call

You will need to make https GET call to OSM API, how this is done depends on your programming language of choice. The endpoints are different per environment, make sure you are calling the right endpoint: **Testing (playground)**

- Europe: [<https: api.playground.klarna.com="" messaging=""></https:>](https://api.playground.klarna.com/messaging/v3){version}
- North America: [<https: api-na.playground.klarna.com="" messaging=""></https:>](https://api-na.playground.klarna.com/messaging/v3){version}
- Oceania: [<https: api-oc.playground.klarna.com="" messaging=""></https:>](https://api-oc.playground.klarna.com/messaging/v3){version}

**Production**

- Europe: [<https: api.klarna.com="" messaging=""></https:>](https://api.klarna.com/messaging/v3){version}
- North America: [<https: api-na.klarna.com="" messaging=""></https:>](https://api-na.klarna.com/messaging/v3){version}
- Oceania: [<https: api-oc.klarna.com="" messaging=""></https:>](https://api-oc.klarna.com/messaging/v3){version}

For more information please check the [OSM API reference page.](https://docs.klarna.com/conversion-boosters/on-site-messaging/integrate-on-site-messaging/on-site-messaging-api-reference/) The endpoint response will look like:

###### *Example of API response*

``` json
{
 "content": {
   "nodes": [
     {
       "type": "TEXT",
       "name": "TEXT_MAIN",
       "value": "Make 4 payments of $128.67. No fees."
     },
     {
       "type": "ACTION",
       "name": "ACTION_LEARN_MORE",
       "label": "Learn more",
       "url": "https://us-assets.playground.klarnaservices.com/learn-more/index.html?..."
     },
     {
       "type": "IMAGE",
       "name": "KLARNA_BADGE",
       "alt": "Klarna",
       "url": "http://us-assets.klarnaservices.com/.../badges/generic/klarna.svg"
     }
   ]
 },
 "impression_url": "https://evt-us.playground.klarnaservices.com/v1/osm-client-script/..."
}
```

**Do not** rely on the presence or absence of fields that are not publicly documented in our API. While we strive to maintain backwards compatibility and stability for publicly documented fields, additional fields may be added or removed in the future. Please ensure that any validation of API responses is limited to the publicly documented fields.

## Step 3: Render Ad

You can now use the content payload inside the response to render the ad using the language or framework of your choice. For examples on how placements might look, see below.

## Step 4: Register Impression event

As per [IAB definition](https://www.iab.com/wp-content/uploads/2015/06/Ad-Impression-Measurment-Guideline-US.pdf): “*An impression is a measurement of responses from an ad delivery system to an ad request from the user's browser, which is filtered from robotic activity and is recorded at a point as late as possible in the process of delivery of the creative material to the user's browser — therefore closest to actual opportunity to see by the user”.* When integrating the OSM API you must trigger a call to register the impression of the ad. The response from the OSM API will contain an impression_url key that can be used to track the impression of this specific ad. If this is not respected, OSM team has the right to stop the integration any time. There are multiple ways of making this call:

- On the web: Through a web beacon by creating an <img/> tag and using the impression_url as the source of the image. This will generate a call to our servers and the impression will be recorded.
- If a web beacon can’t be created you can trigger a HTTP GET call from your application. This call can originate from the frontend or backend of your application.

The impression event endpoint will return a 2XX response status code.\|collapsed=true}}

## Step 5: Cache the response when possible

The endpoint will return a `cache-control` header that you should honor when possible. In the case of a web integration frontend-side, this header will be handled by the browser. On mobile or backend integrations that will depend on the characteristics of the platform.

## Handling product purchase amount changes

When using credit-promotion placements on product pages, the case when the product/s purchase amount changes must be handled by the integrator.  Whenever the purchase amount changes, a new request to the endpoint must be made to refresh the messaging according to the new purchase amount, the ad should be re-render and a new impression event registered.