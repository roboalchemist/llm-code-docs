# Source: https://docs.mystic.ai/docs/overview.md

# Overview

Mystic's BYOC is the easiest way to deploy ML models on your cloud account

Serverless endpoints for AI models are great when getting started but when scaling they can provide several challenges. The two biggest ones are:

1. Cost - Getting compute in serverless is more expensive than running on dedicated machines
2. Cold start times - This is a prominent problem for many products, especially when their traffic is sporadic

This is where Bring your own Cloud (BYOC) can help!

Mystic's BYOC allows you to use the same models and API endpoints as you normally would on serverless, but using GPUs on your own cloud account. We use OAuth (sign-in with Google) to deploy the models on your account and then automatically handle auto-scaling along with a bunch more features! This solves the two problems of serverless compute:

1. Get compute at cost - You can even use your cloud credits
2. You have complete control over how the system scales

Read more about the features in BYOC [below](#features).

Here's a video walkthrough of the platform.

[block:embed]
{
  "html": "<iframe class=\"embedly-embed\" src=\"//cdn.embedly.com/widgets/media.html?src=https%3A%2F%2Fwww.youtube.com%2Fembed%2Fbd8lv7o3R3U&display_name=YouTube&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dbd8lv7o3R3U&image=http%3A%2F%2Fi.ytimg.com%2Fvi%2Fbd8lv7o3R3U%2Fhqdefault.jpg&key=7788cb384c9f4d5dbbdbeffd9fe4b92f&type=text%2Fhtml&schema=youtube\" width=\"854\" height=\"480\" scrolling=\"no\" title=\"YouTube embed\" frameborder=\"0\" allow=\"autoplay; fullscreen; encrypted-media; picture-in-picture;\" allowfullscreen=\"true\"></iframe>",
  "url": "https://www.youtube.com/watch?v=bd8lv7o3R3U",
  "favicon": "http://www.google.com/favicon.ico",
  "image": "http://i.ytimg.com/vi/bd8lv7o3R3U/hqdefault.jpg",
  "provider": "youtube.com",
  "href": "https://www.youtube.com/watch?v=bd8lv7o3R3U",
  "typeOfEmbed": "youtube"
}
[/block]

# Features

* Scaling ([read more here](https://docs.mystic.ai/docs/scaling-configuration))
  * Define minimum and maximum replicas
  * Responsiveness of scale up / down control
  * Warm up / Cool down. Notify the API ahead of time that you want a model ready in advance, then notify the system that you're down to spin it down to 0 ([read more here](https://docs.mystic.ai/docs/warmup-cooldown))
  * **Scale down to 0**
* Cost savings - Get compute at cost, and use your own cloud credits
* One click deploy - Deploy any model to your cluster already on Mystic through one click
* Standard SaaS billing - We do not charge more based on your usage regardless of wether you need 1 or 100 GPUs
* Run custom models - BYOC works with all of your private models created on Mystic and supports programatic deployment
* No code setup - You can start using BYOC without writing any code, all through our dashboard!

# How get started

You can start using BYOC today! You can go to the onboarding right now to get setup: [Cloud Integrations dashboard](https://www.mystic.ai/cloud-integrations).