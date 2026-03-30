# Source: https://developers.webflow.com/browser/optimize/introduction.mdx

***

title: Optimize methods in the Browser API
slug: optimize/introduction
layout: overview
description: Introduction to the Optimize methods in the Browser API
hidden: true
'og:title': Optimize methods in the Browser API
'og:description': Introduction to the Optimize methods in the Browser API
-------------------------------------------------------------------------

{/* Optimize Hero Image */}

<div class="features-hero_bottom-img">
  <img src="https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero.webp" loading="lazy" sizes="(max-width: 479px) 85vw, 90vw" srcset="https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero-p-500.webp 500w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero-p-800.webp 800w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero-p-1080.webp 1080w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero-p-1600.webp 1600w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero-p-2000.webp 2000w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero-p-2600.webp 2600w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero-p-3200.webp 3200w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707da8cde91dd9813b4aaba_hero.webp 4320w" alt="" class="u-img-cover cc-top" />

  <img src="https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707dbd2416640c50f680a46_successrate.webp" loading="lazy" sizes="(max-width: 479px) 25vw, 27vw" srcset="https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707dbd2416640c50f680a46_successrate-p-500.webp 500w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/6707dbd2416640c50f680a46_successrate.webp 782w" alt="" class="optimize_conversions u-mega-shadow-light-bg" />

  <img src="https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/672296f31b581bfa0c5cc890_performancechart.webp" loading="lazy" sizes="(max-width: 479px) 34vw, 36vw" srcset="https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/672296f31b581bfa0c5cc890_performancechart-p-500.webp 500w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/672296f31b581bfa0c5cc890_performancechart-p-800.webp 800w, https://cdn.prod.website-files.com/650311fc2ebc7fe34237a592/672296f31b581bfa0c5cc890_performancechart.webp 1182w" alt="" class="optimize_performance u-mega-shadow-light-bg" />
</div>

#

[Webflow Optimize](https://webflow.com/optimize) enables you to customize the version of a page shown to visitors based on their characteristics. Think of it as a supercharged A/B testing tool that enables you to test numerous variations of your site to dynamically personalize a visitor's experience based on their attributes.

## Optimize methods in the Browser API

The Browser API includes Optimize-specific methods that enable you to extend this functionality to incorporate other tools you may use to track audiences and goals. With these Optimize methods, you can:

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

## Get started with the Optimize in the Browser API

<Card
  title="Get started with Optimize"
  href="/browser/optimize/quickstart"
  iconPosition="left"
  icon={
            <>
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Dark/64px/CirclePlay.svg" alt="" className="hidden dark:block" />
                <img src="https://dhygzobemt712.cloudfront.net/Icons/Light/64px/CirclePlay.svg" alt="" className="block dark:hidden" />
            </>
        }
>
  Use the Quickstart guide to learn how to use the Optimize methods to track variations and set custom attributes.

  <br />

  <a href="/browser/optimize/quickstart">
    <button class="button cc-primary">Get started</button>
  </a>
</Card>

## FAQs

{/* <!-- vale off --> */}

<AccordionGroup>
  <Accordion title="What are the Optimize methods?">
    {/* <!-- vale on --> */}

    The Optimize methods are JavaScript functions available through the Webflow Browser API's `wf` namespace that enable you to track optimization variations and manage custom user attributes.

    You can use methods like [`wf.onVariationRecorded()`](/browser/optimize/onVariationRecorded) and [`wf.setAttributes()`](/browser/optimize/setAttributes) to send Webflow Optimize data to third-party analytics and marketing tools, helping you better understand user behavior and personalize experiences.

    {/* <!-- vale off --> */}
  </Accordion>

  <Accordion title="Is the Browser API already installed on my site?">
    {/* <!-- vale on --> */}

    The Webflow Browser APIs and Optimize methods are automatically available on all Webflow Optimize enabled sites with no manual installation required. See the [Quickstart guide](/browser/optimize/quickstart) for more information.

    {/* <!-- vale off --> */}
  </Accordion>

  <Accordion title="How can I use the Optimize methods?">
    {/* <!-- vale on --> */}

    The Optimize methods are available through the global `wf` object in your browser. You can access them through custom code in your site's pages or through services like Google Tag Manager. The APIs can be called from any JavaScript code running on your site. See the [Quickstart guide](/browser/optimize/quickstart) for more information.

    {/* <!-- vale off --> */}
  </Accordion>
</AccordionGroup>

{/* <!-- vale on --> */}

## Looking for more information?

Visit the [Webflow Help Center](https://help.webflow.com/hc/en-us/articles/33609390628243-Intro-to-Webflow-Optimize) to learn more about Optimize features, including experiments, personalization, and analytics. The Help Center provides detailed guides on:

* Setting up and configuring Optimize experiments
* Creating and managing audience segments
* Analyzing test results and insights
* Best practices for running effective experiments
* Enterprise-specific features and capabilities

You can also explore [Webflow University](https://university.webflow.com/videos/start-optimizing-your-site-with-webflow-optimize) for additional tutorials and resources on making the most of Webflow Optimize.
