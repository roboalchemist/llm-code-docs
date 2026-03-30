# Source: https://developers.webflow.com/browser/custom-goals.mdx

***

title: Custom Goals
slug: custom-goals
description: Track on-site and off-site conversion goals in Analyze and Optimize
hidden: false
'og:title': Custom Goals
'og:description': Track on-site and off-site conversion goals in Analyze and Optimize
-------------------------------------------------------------------------------------

Custom goals let you track conversions beyond standard clicks or page views. Whether your conversions happen directly on your Webflow site or further downstream outside your website, custom goals help you measure what matters most to your business.

<Note title="Analyze or Optimize required">
  Custom goals are only available to Webflow Analyze and Optimize customers.
</Note>

## Custom goal types

There are two types of custom goals, depending on where the conversion happens:

### On-site conversions

Use on-site conversions when the conversion happens on your Webflow site. Examples include:

* Form submissions from embedded third-party forms (like HubSpot)
* Bookings from meeting scheduling tools (like Calendly)
* Clicks on Webflow elements that aren't standard buttons or links (like Tabs or Sliders)

On-site conversions use the [`wf.sendEvent()`](/browser/custom-goals/on-site-conversions/sendEvent) client-side API to trigger goal events.

### Off-site conversions

Use off-site conversions when the actual conversion happens outside your Webflow site. Examples include:

* CRMs or other internal systems
* Product signups, or other in-app events
* Mobile app downloads

Off-site conversions utilize:

* [`wf.setUserId()`](/browser/custom-goals/off-site-conversions/setUserId) — Client-side API to identify visitors
* [Server-side API](/browser/custom-goals/off-site-conversions/server-api) — HTTPS endpoint to send conversion data

## Get started

<CardGroup>
  <Card
    title="On-site conversions"
    href="/browser/custom-goals/on-site-conversions"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/Test.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/Test.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Track custom conversions directly on your Webflow site
  </Card>

  <Card
    title="Off-site conversions"
    href="/browser/custom-goals/off-site-conversions"
    icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/SitePersonalization.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/SitePersonalization.svg" alt="" className="block dark:hidden" />
            </>
        }
  >
    Track conversions that happen outside your Webflow site
  </Card>
</CardGroup>

<Warning title="Compliance considerations">
  Your organization is responsible for ensuring your use of custom goals complies with applicable privacy and data protection laws (such as GDPR, CCPA, and other regional regulations). This includes:

  * Obtaining appropriate consent from visitors before tracking conversions
  * Providing clear disclosures in your privacy policy about data collection
  * Ensuring your data handling practices meet legal requirements

  We recommend consulting with your legal and privacy teams to assess your specific obligations before implementing custom goal tracking.
</Warning>
