# Source: https://posthog.com/docs/web-analytics/installation/html-snippet.md

# Source: https://posthog.com/docs/session-replay/installation/html-snippet.md

# HTML snippet session replay installation - Docs

1.  1

    ## Choose an installation method

    Required

    You can either add the JavaScript snippet directly to your HTML or install the JavaScript SDK via your package manager.

    ## HTML snippet

    Add this snippet to your website within the `<head>` tag. This can also be used in services like Google Tag Manager:

    HTML

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

    ## JavaScript SDK

    Install the PostHog JavaScript library using your package manager. Then, import and initialize the PostHog library with your project token and host:

    PostHog AI

    ### npm

    ```bash
    npm install posthog-js
    ```

    ### yarn

    ```bash
    yarn add posthog-js
    ```

    ### pnpm

    ```bash
    pnpm add posthog-js
    ```

    JavaScript

    PostHog AI

    ```javascript
    import posthog from 'posthog-js'
    posthog.init('<ph_project_token>', {
        api_host: 'https://us.i.posthog.com',
        defaults: '2026-01-30'
    })
    ```

2.  2

    ## Watch session recordings

    Recommended

    Visit your site or app and interact with it for at least 10 seconds to generate a recording. Navigate between pages, click buttons, and fill out forms to capture meaningful interactions.

    [Watch your first recording →](/replay/home.md)

3.  3

    ## Next steps

    Recommended

    Now that you're recording sessions, continue with the resources below to learn what else Session Replay enables within the PostHog platform.

    | Resource | Description |
    | --- | --- |
    | [Watching recordings](/docs/session-replay/how-to-watch-recordings.md) | How to find and watch session recordings |
    | [Privacy controls](/docs/session-replay/privacy.md) | How to mask sensitive data in recordings |
    | [Network recording](/docs/session-replay/network-recording.md) | How to capture network requests in recordings |
    | [Console log recording](/docs/session-replay/console-log-recording.md) | How to capture console logs in recordings |
    | [More tutorials](/docs/session-replay/tutorials.md) | Other real-world examples and use cases |

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better