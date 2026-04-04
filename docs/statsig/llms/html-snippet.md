# Source: https://docs.statsig.com/client/html-snippet.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# HTML Snippet

> Add Statsig to web pages with an HTML script tag

## Set Up the SDK

<Steps>
  <Step title="Install the SDK">
    You can install the Statsig SDK by putting a script tag in the head of your HTML file:

    ```js  theme={null}
    <script
      src="https://cdn.jsdelivr.net/npm/@statsig/js-client@3/build/statsig-js-client+session-replay+web-analytics.min.js?apikey=YOUR_CLIENT_API_KEY"
      crossorigin="anonymous"
    >
    </script>
    ```

    Note that you need to replace `YOUR_CLIENT_API_KEY` with your actual client API key from the [Project Settings > API Keys](https://console.statsig.com/api_keys).
  </Step>

  <Step title="Initialize the SDK">
    The HTML snippet we provide wraps an instance of the statsig javascript sdk.  Simply providing your client API key in the url is enough to auto initialize the SDK, as the installation step recommends.

    However, you should likely move to a manual initialization if you need any of the following:

    * custom user properties
    * custom initialization options
    * check gates, configs, experiments, or log events

    To manually initialize an instance of the sdk, remove the key parameter from the script tag, and do the following:

    ```js  theme={null}
    const { StatsigClient, runStatsigAutoCapture, runStatsigSessionReplay } = window.Statsig;
        
    const client = new StatsigClient(
        '<CLIENT-SDK-KEY>', 
        { userID: 'a-user' }
    );

    runStatsigSessionReplay(client);
    runStatsigAutoCapture(client);

    await client.initializeAsync();

    // check gates, configs, experiments, or log events
    ```

    The `StatsigClient` instance you create is also available via `window.Statsig`, so you can reference it globally.

    At this point, you have access to all of the methods available in the [Javascript SDK](/client/javascript-sdk) via your instance of the `StatsigClient`.  Refer to that documentation for initialization details and core methods.
  </Step>
</Steps>

#### I want to customize the initialization logic, can I do that?

Yes, you can remove the client API key from the url and see the [Javascript SDK Getting Started Guide](/client/javascript-sdk#getting-started) for more information.
The HTML snippet is just our javascript SDK - providing an api key in the url will auto initialize an instance for you, but if you don't want that, you can use it just like the javascript SDK.

You will need to create your own instance differently than if you were installing the SDK via npm:

```js  theme={null}
const { StatsigClient, runStatsigAutoCapture, runStatsigSessionReplay } = window.Statsig;
    
const client = new StatsigClient(
    '<CLIENT-SDK-KEY>', 
    { userID: 'a-user' }
);

runStatsigSessionReplay(client);
runStatsigAutoCapture(client);

await client.initializeAsync();

// check gates, configs, experiments, or log events
```


Built with [Mintlify](https://mintlify.com).