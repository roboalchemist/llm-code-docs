# Source: https://posthog.com/docs/web-analytics/installation/gtm.md

# Google Tag Manager web analytics installation - Docs

1.  1

    ## Create a custom HTML tag

    Required

    Google Tag Manager (GTM) lets you manage tracking scripts without code changes. You can add PostHog to your site using a custom HTML tag.

    1.  Log into your Google Tag Manager account and open your container.
    2.  Click **Tags** > **New** > **Tag Configuration** > **Custom HTML**.
    3.  Paste the following code:

    Custom HTML Tag

    PostHog AI

    ```html
    <script>
        !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group identify setPersonProperties setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags resetGroups onFeatureFlags addFeatureFlagsHandler onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
        posthog.init('<ph_project_token>', {
            api_host: 'https://us.i.posthog.com',
            defaults: '2026-01-30'
        })
    </script>
    ```

2.  2

    ## Configure the trigger

    Required

    1.  Under **Triggering**, select **All Pages** to load PostHog on every page.
    2.  Save the tag, then click **Submit** to publish your changes.

    Once published, PostHog will automatically capture pageviews, clicks, and other events on your site.

3.  3

    ## Send events

    Click around and view a couple pages to generate some events. PostHog automatically captures pageviews, clicks, and other interactions for you.

    If you'd like, you can also manually capture custom events:

    JavaScript

    PostHog AI

    ```javascript
    posthog.capture('my_custom_event', { property: 'value' })
    ```

4.  4

    ## Next steps

    Recommended

    After installing PostHog and ensuring [autocapture](/docs/data/autocapture.md) is enabled, head to your [web analytics dashboard](/docs/web-analytics/dashboard.md) to see your data. And then check out our [getting started](/docs/web-analytics/getting-started.md) guide.

    > **PostHog tip:** Web analytics works with [anonymous events](/docs/data/anonymous-vs-identified-events.md). This means if you are primarily using PostHog for web analytics, it can be significantly cheaper for you.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better