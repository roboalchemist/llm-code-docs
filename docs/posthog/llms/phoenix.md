# Source: https://posthog.com/docs/web-analytics/installation/phoenix.md

# Source: https://posthog.com/docs/libraries/phoenix.md

# Phoenix - Docs

PostHog makes it easy to get data about traffic and usage of your [Phoenix](https://www.phoenixframework.org/) projects. Integrating PostHog into your site enables analytics about user behavior, custom events capture, session recordings, feature flags, and more.

This guide walks you through integrating PostHog into your Phoenix app using the [JavaScript Web SDK](/docs/libraries/js.md).

You might also be interested in our [Elixir SDK](/docs/libraries/elixir.md) for capturing events from your servers.

## Installation

Go to your [project settings](https://us.posthog.com/settings/project#snippet) and copy your web snippet. It looks like this:

JavaScript

PostHog AI

```javascript
<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.crossOrigin="anonymous",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister unregister_for_session getFeatureFlag getFeatureFlagPayload isFeatureEnabled reloadFeatureFlags updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures on onFeatureFlags onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep identify setPersonProperties group resetGroups setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags reset get_distinct_id getGroups get_session_id get_session_replay_url alias set_config startSessionRecording stopSessionRecording sessionRecordingStarted captureException loadToolbar get_property getSessionProperty createPersonProfile opt_in_capturing opt_out_capturing has_opted_in_capturing has_opted_out_capturing clear_opt_in_out_capturing debug".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('<ph_project_token>',{api_host:'https://us.i.posthog.com', defaults:'2026-01-30'})
</script>
```

With the JavaScript snippet copied, add it to your main layout file, usually located in `lib/<app>/templates/layouts/app.html.eex` at the bottom of the `<head>` tag.

## Identifying users

> **Identifying users is required.** Backend events need a `distinct_id` that matches the ID your frontend uses when calling `posthog.identify()`. Without this, backend events are orphaned — they can't be linked to frontend event captures, [session replays](/docs/session-replay.md), [LLM traces](/docs/ai-engineering.md), or [error tracking](/docs/error-tracking.md).
>
> See our guide on [identifying users](/docs/getting-started/identify-users.md) for how to set this up.

### LiveView installation

PostHog also supports Phoenix LiveView with a small tweak to your configuration as the JavaScript snippet doesn't track LiveView's navigation by default.

To properly capture LiveView pageviews/navigation, you need to add an `phx:navigate` event listener to the bottom of the `<head>` tag in your main layout file, usually located in `lib/<app>/templates/layouts/app.html.eex`:

JavaScript

PostHog AI

```javascript
window.addEventListener("phx:navigate", ({ detail: { href } }) =>
  posthog.capture('$pageview', {
    '$current_url': href
  })
 )
```

This captures a `$pageview` event any time the browser's URL bar is programmatically changed by Phoenix or the user. You can learn more about the `phx:navigate` event in the [Phoenix LiveView documentation](https://hexdocs.pm/phoenix_live_view/Phoenix.LiveView.html#navigate/2).

## Capture custom events

To [capture custom events](/docs/product-analytics/capture-events.md), you can use `posthog.capture()` in your LiveView or regular Phoenix views. Here are some examples:

### Basic event capture

JavaScript

PostHog AI

```javascript
// Capture a simple event
posthog.capture('button_clicked')
```

### Event capture with properties

JavaScript

PostHog AI

```javascript
// Capture an event with additional properties
posthog.capture('form_submitted', {
    form_name: 'contact',
    form_fields: ['name', 'email', 'message'],
    submission_time: new Date().toISOString()
})
```

### Capturing events in LiveView

In your LiveView, you can capture events in response to user interactions:

JavaScript

PostHog AI

```javascript
// In your LiveView JavaScript hooks
let Hooks = {
    Form: {
        mounted() {
            this.el.addEventListener('submit', (e) => {
                e.preventDefault()
                posthog.capture('form_submitted', {
                    form_id: this.el.id,
                    form_data: new FormData(this.el)
                })
                // Handle form submission
            })
        }
    }
}
let liveSocket = new LiveSocket("/live", Socket, {
    params: {_csrf_token: csrfToken},
    hooks: Hooks
})
```

### Capturing events in regular Phoenix views

For regular Phoenix views, you can add event tracking to your templates:

HTML

PostHog AI

```html
<!-- In your template -->
<button phx-click="track_button_click" data-event-name="signup_button">
    Sign Up
</button>
<!-- In your JavaScript -->
document.addEventListener('phx:click', (e) => {
    if (e.target.dataset.eventName) {
        posthog.capture(e.target.dataset.eventName)
    }
})
```

## Next steps

Installing the JavaScript Web SDK or snippet means all of its functionality is available in your Phoenix project. To learn more about this, have a look at our [JavaScript Web SDK docs](/docs/libraries/js/features.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better