# Source: https://posthog.com/docs/web-analytics/installation/bubble.md

# Source: https://posthog.com/docs/session-replay/installation/bubble.md

# Source: https://posthog.com/docs/experiments/installation/bubble.md

# Source: https://posthog.com/docs/libraries/bubble.md

# Bubble - Docs

PostHog makes it easy to get data about traffic and usage of your [Bubble](https://bubble.io/) app. Integrating PostHog into your site enables analytics about user behavior, custom events capture, session recordings, feature flags, and more.

This guide walks you through integrating PostHog into your Bubble app using the [JavaScript Web SDK](/docs/libraries/js.md).

## Installation

First, [sign up to PostHog](https://app.posthog.com/signup). Then, go to your [project settings](https://app.posthog.com/settings/project) and copy your [web snippet](https://app.posthog.com/settings/project#snippet). It looks like this:

JavaScript

PostHog AI

```javascript
<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys getNextSurveyStep onSessionId".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('<ph_project_token>',{api_host:'https://us.i.posthog.com', defaults:'2026-01-30'})
</script>
```

With the snippet copied, go to your Bubble site settings by clicking on the icon in the left-hand menu. If you haven’t already, sign up for at least the **Starter** site plan. This enables you to add custom code.

Go to the **SEO / metatags** tab in site settings. Paste your PostHog snippet in the **Script/meta tags in header** section. Then, deploy your site to live.

Set up a reverse proxy (recommended)

We recommend [setting up a reverse proxy](/docs/advanced/proxy.md), so that events are less likely to be intercepted by tracking blockers.

We have our [own managed reverse proxy service](/docs/advanced/proxy/managed-reverse-proxy.md), which is free for all PostHog Cloud users, routes through our infrastructure, and makes setting up your proxy easy.

If you don't want to use our managed service then there are several other options for creating a reverse proxy, including using [Cloudflare](/docs/advanced/proxy/cloudflare.md), [AWS Cloudfront](/docs/advanced/proxy/cloudfront.md), and [Vercel](/docs/advanced/proxy/vercel.md).

Grouping products in one project (recommended)

If you have multiple customer-facing products (e.g. a marketing website + mobile app + web app), it's best to install PostHog on them all and [group them in one project](/docs/settings/projects.md).

This makes it possible to track users across their entire journey (e.g. from visiting your marketing website to signing up for your product), or how they use your product across multiple platforms.

Add IPs to Firewall/WAF allowlists (recommended)

For certain features like [heatmaps](/docs/toolbar/heatmaps.md), your Web Application Firewall (WAF) may be blocking PostHog’s requests to your site. Add these IP addresses to your WAF allowlist or rules to let PostHog access your site.

**EU**: `3.75.65.221`, `18.197.246.42`, `3.120.223.253`

**US**: `44.205.89.55`, `52.4.194.122`, `44.208.188.173`

These are public, stable IPs used by PostHog services (e.g., Celery tasks for snapshots).

## Capture custom events

To capture custom events, you need to install the [Bubble Toolbox plugin](https://bubble.io/plugin/toolbox-1488796042609x768734193128308700). This enables you to run custom JavaScript code.

Below is an example of how to capture an event when a button is pressed:

1.  Add a new button to your Bubble site. Click on the button and then on **Add workflow** in the popup menu.

2.  Click on **add an action**. In the menu that appears, click on **Plugins** and then **Run javascript**. This will open a new menu where you can add JavaScript code.

3.  Add the following code under the **Script** heading:

JavaScript

PostHog AI

```javascript
window.posthog.capture("button_clicked")
```

## Next steps

For any technical questions for how to integrate specific PostHog features into Bubble (such as analytics, feature flags, A/B testing, surveys, etc.), have a look at our [JavaScript Web SDK docs](/docs/libraries/js/features.md).

Alternatively, the following tutorials can help you get started:

-   [How to set up Bubble analytics, session replays, and more](/tutorials/bubble-analytics.md)
-   [How to create surveys in Bubble](/tutorials/bubble-surveys.md)
-   [How to run A/B tests in Bubble](/tutorials/bubble-ab-tests.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better