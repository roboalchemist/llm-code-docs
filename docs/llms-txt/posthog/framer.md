# Source: https://posthog.com/docs/web-analytics/installation/framer.md

# Source: https://posthog.com/docs/session-replay/installation/framer.md

# Source: https://posthog.com/docs/experiments/installation/framer.md

# Source: https://posthog.com/docs/libraries/framer.md

# Framer - Docs

PostHog makes it easy to get data about traffic and usage of your [Framer](https://www.framer.com/) app. Integrating PostHog into your site enables analytics about user behavior, custom events capture, session recordings, feature flags, and more.

This guide walks you through integrating PostHog into your Framer app using the [JavaScript Web SDK](/docs/libraries/js.md).

## Installation

Go to your [project settings](https://app.posthog.com/settings/project#snippet) and copy your web snippet. It looks like this:

JavaScript

PostHog AI

```javascript
<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('<ph_project_token>',{api_host:'https://us.i.posthog.com', defaults:'2026-01-30'})
</script>
```

With the JavaScript snippet copied, go to your Framer project and click the gear in the top right to go to your site settings. If you haven’t already, sign up for the "Mini" site plan. This enables you to add custom code.

Once on a paid plan, go to the **General** tab in site settings and scroll down to the **Custom Code** section. Under **End of `<head>` tag**, paste your PostHog JavaScript snippet. Make sure to press **Save** next to the **Custom Code** heading.

Finally, **publish** your site to have PostHog automatically start capturing events.

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

To [capture custom events](/docs/product-analytics/capture-events.md), you call `posthog.capture()` using [custom code components in Framer](https://www.framer.com/developers/components/introduction).

Go to the **Assets** tab in the top left of your Framer project, and click the **plus icon** next to the Code tab. This will show a pop up to create a new code file. Name the file `CaptureButton`, set it as a "New component" and press **Create**.

In the new code file, delete the existing code and replace it with the following:

JavaScript

PostHog AI

```javascript
export default function CaptureButton() {
    const handleClick = () => {
        window.posthog.capture("clicked_button", {
            $set_once: { clicked_homepage_button: true },
        })
    }
    return (
        <button id="capture-button" onClick={handleClick}>
            Click me
        </button>
    )
}
```

Press `Cmd/Ctrl + s` to save your changes. Then press the **Home** button to go back to the home page. Add your new `CaptureButton` to your page by dragging it from the Code tab.

Publish your site and then click your new button to [see the event in PostHog](https://us.posthog.com/activity/explore).

## Next steps

For any technical questions for how to integrate specific PostHog features into Framer (such as analytics, feature flags, A/B testing, surveys, etc.), have a look at our [JavaScript Web SDK docs](/docs/libraries/js/features.md).

Alternatively, the following tutorials can help you get started:

-   [How to set up Framer analytics, session replays, and feature flags](/tutorials/framer-analytics.md)
-   [How to run A/B tests in Framer](/tutorials/framer-ab-tests.md)
-   [How to create surveys in Framer](/tutorials/framer-surveys.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better