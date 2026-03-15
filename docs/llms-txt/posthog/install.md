# Source: https://posthog.com/docs/getting-started/install.md

# Install PostHog - Docs

## AI wizard

Install PostHog in minutes with our wizard by running this command in your project directory:

`npx @posthog/wizard@latest`

[Learn more](/wizard.md)

Wait for it to finish and test the setup once the wizard is complete.

## Frameworks and languages

The wizard supports the following frameworks and languages:

-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Android_robot_bec2fb7318.svg)Android (Kotlin)](/docs/libraries/android.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/angular.svg)Angular](/docs/libraries/angular.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/astro_icon_dark_23a13977ad.svg)Astro](/docs/libraries/astro.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/django.svg)Django](/docs/libraries/django.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/python.svg)FastAPI](https://github.com/PostHog/wizard)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/flask.svg)Flask](/docs/libraries/flask.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/laravel.svg)Laravel](/docs/libraries/laravel.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nextjs.svg)Next.js](/docs/libraries/next-js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nuxt.svg)Nuxt](/docs/libraries/nuxt.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/python.svg)Python](/docs/libraries/python.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React Native](/docs/libraries/react-native.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React](/docs/libraries/react.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/ruby.svg)Ruby](/docs/libraries/ruby.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/rails_581d31c82d.svg)Ruby on Rails](/docs/libraries/rails.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/rr_logo_light_970950178e.svg)React Router](/docs/libraries/react-router.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/svelte.svg)SvelteKit](/docs/libraries/svelte.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/ios.svg)Swift (iOS/macOS)](/docs/libraries/ios.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/logo_color_600_391d28faae.png)TanStack Start](https://github.com/PostHog/wizard)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/vue.svg)Vue](/docs/libraries/vue-js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/elixir.svg)ElixirComing soon](/docs/libraries/elixir.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/flutter.svg)FlutterComing soon](/docs/libraries/flutter.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/go.svg)GoComing soon](/docs/libraries/go.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/java.svg)JavaComing soon](/docs/libraries/java.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/rust.svg)RustComing soon](/docs/libraries/rust.md)

We've got more on the way.

Check out the wizard's [GitHub repo](https://github.com/PostHog/wizard) for more details.

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

## JS snippet

This is the simplest way to get PostHog up and running. It only takes a few minutes.

Copy the snippet below and replace `<ph_project_token>` and `<ph_client_api_host>` with your project's values, then add it within the `<head>` tags at the base of your product - ideally just before the closing `</head>` tag. This ensures PostHog loads on any page users visit.

You can find the snippet pre-filled with this data in [your project settings](https://app.posthog.com/settings/project#snippet).

HTML

PostHog AI

```html
<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('<ph_project_token>',{api_host:'https://us.i.posthog.com', defaults:'2026-01-30'})
</script>
```

Once the snippet is added, PostHog automatically captures `$pageview` and [other events](/docs/data/autocapture.md) like button clicks. You can then enable other products, such as session replays, within [your project settings](https://app.posthog.com/settings).

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

Include ES5 support (optional)

If you need ES5 support for example to track Internet Explorer 11 replace `/static/array.js` in the snippet with `/static/array.full.es5.js`

Working with AI code editors?

If you’re working with AI code editors (like Lovable, Bolt.new, Replit, and others), it’s easy to install PostHog. Just give it this prompt: `npx -y @posthog/wizard@latest`

## Libraries14

Custom-built libraries for integrating PostHog with popular client and server-side langauges.

-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/js.svg)JavaScript web](/docs/libraries/js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React Native](/docs/libraries/react-native.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/react.svg)React](/docs/libraries/react.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/nodejs.svg)Node.js](/docs/libraries/node.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/ios.svg)iOS](/docs/libraries/ios.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/flutter.svg)Flutter](/docs/libraries/flutter.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/python.svg)Python](/docs/libraries/python.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Android_robot_bec2fb7318.svg)Android](/docs/libraries/android.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/php.svg)PHP](/docs/libraries/php.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/java.svg)Java](/docs/libraries/java.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/go.svg)Go](/docs/libraries/go.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/ruby.svg)Ruby](/docs/libraries/ruby.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/rust.svg)Rust](/docs/libraries/rust.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/elixir.svg)Elixir](/docs/libraries/elixir.md)

## Framework guides22

Framework-specific guides that cover our recommended approach to installing PostHog in a number of popular environments.

-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/angular.svg)Angular](/docs/libraries/angular.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/astro_icon_dark_23a13977ad.svg)Astro](/docs/libraries/astro.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/bubble.svg)Bubble](/docs/libraries/bubble.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/django.svg)Django](/docs/libraries/django.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/docusaurus.svg)Docusaurus](/docs/libraries/docusaurus.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/flask.svg)Flask](/docs/libraries/flask.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/framer_logo_icon_169149_d72b90e48e.svg)Framer](/docs/libraries/framer.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/gatsby.svg)Gatsby](/docs/libraries/gatsby.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/gtm.svg)Google Tag Manager](/docs/libraries/google-tag-manager.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/laravel.svg)Laravel](/docs/libraries/laravel.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nextjs.svg)Next.js](/docs/libraries/next-js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/nuxt.svg)Nuxt.js](/docs/libraries/nuxt-js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Phoenix_Framework_81f5da0296.svg)Phoenix](/docs/libraries/phoenix.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/remix_letter_glowing_49183adce2.svg)Remix](/docs/libraries/remix.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/retool.svg)Retool](/docs/libraries/retool.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/rudderstack.svg)RudderStack](/docs/libraries/rudderstack.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/segment.svg)Segment](/docs/libraries/segment.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/shopify_glyph_5a3ad7459b.svg)Shopify](/docs/libraries/shopify.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Symbol_1_ac11ac22f6.svg)Slack](/docs/libraries/slack.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/docs/integrate/frameworks/svelte.svg)Svelte](/docs/libraries/svelte.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/vue.svg)Vue.js](/docs/libraries/vue-js.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/webflow_63b6678590.svg)Webflow](/docs/libraries/webflow.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/Woo_Commerce_logo_1b49a43cb1.svg)WooCommerce](/docs/libraries/woocommerce.md)
-   [![](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/integrate/frameworks/wordpress.svg)WordPress](/docs/libraries/wordpress.md)

## API

Events can be ingested directly using our API and the [`/i/v0/e`](/docs/api/capture.md) endpoint, which is the same endpoint that all of our libraries use behind the scenes.

Generally, this isn't something you'll need to use when integrating PostHog, but if you're working with a language or framework that PostHog doesn't support yet, this will allow you to still send events.

> **Note:** For this API, you should use your 'Project token' from the 'Project' page in PostHog. This is the same token used in your frontend snippet.

## Sending events

Events can be sent either one at a time, or together in a batch. There is no limit on the number of events you can send in a batch, but the entire request body must be less than `20MB` by default.

PostHog AI

### Single

```shell
POST https://[your-instance].com/i/v0/e/
Content-Type: application/json
Body:
{
    "token": "<ph_project_token>",
    "event": "event_name",
    "properties": {
        "distinct_id": "distinct_id_of_your_user",
        "key1": "value1",
        "key2": "value2"
    },
    "timestamp": "[optional timestamp in ISO 8601 format]"
}
```

### Batch

```shell
POST https://[your-instance].com/batch/
Content-Type: application/json
Body:
{
    "token": "<ph_project_token>",
    "batch": [
        {
            "event": "event_name",
            "properties": {
                "distinct_id": "distinct_id_of_your_user",
                "key1": "value1",
                "key2": "value2"
            },
            "timestamp": "[optional timestamp in ISO 8601 format]"
        },
        ...
    ]
}
```

> **Note:** Timestamp is optional. If not set, it'll automatically be set to the current time.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better