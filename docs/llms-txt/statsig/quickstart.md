# Source: https://docs.statsig.com/sdks/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Get started with the Statsig SDK

> Get data flowing into Statsig with only a few lines of code.

If you're looking for a more detailed guide, check out the [SDK Overview](/sdks/getting-started) or read about choosing between [client or server SDKs](/sdks/client-vs-server).

<Tabs>
  <Tab title="React" icon="react">
    <Steps>
      <Step title="Install Statsig packages">
        ```bash  theme={null}
        npm install @statsig/react-bindings
        ```
      </Step>

      <Step title="Wrap child components">
        Next, update your app's default function (Usually App.tsx or Layout.tsx) so that the StatsigProvider wraps around all child components.

        ```tsx  theme={null}
        import { StatsigProvider } from "@statsig/react-bindings"; // [!code ++]

        export default function RootLayout({ children }: { children: React.ReactNode }) {
          return (
            <StatsigProvider // [!code ++]
              sdkKey={"client-MY-STATSIG-CLIENT-KEY"} // [!code ++]
              user={{ userID: "quickstart-user" }} // [!code ++]
              loadingComponent={<div>Loading...</div>}> // [!code ++]
              {children}
            </StatsigProvider> // [!code ++]
          );
        }
        ```

        <Note>
          This example assumes you're using client-side React, if you're Server-Side Rendering, you'd be better served by our [Next.js docs](/client/Next).
        </Note>
      </Step>

      <Step title="Add client key">
        Create a client API key in the [Statsig console Settings](https://console.statsig.com/api_keys). Copy and paste it to replace `<REPLACE_WITH_YOUR_CLIENT_KEY>` in the code snippet from the previous step.
      </Step>

      <Step title="Basic Usage">
        <Tabs>
          <Tab title="Check a Gate">
            First, create a gate on the [Feature Gates page](https://console.statsig.com/gates) in console, then check it in-code:

            ```jsx  theme={null}
            const { client } = useStatsigClient();
            return (
              <div>Gate is {client.checkGate('check_user') ? 'passing' : 'failing'}.</div>
            );
            ```
          </Tab>

          <Tab title="Get an Experiment Value">
            First, create an Experiment on the [Experiments page](https://console.statsig.com/experiments) in console

            ```jsx  theme={null}
            const { client } = useStatsigClient();
            const experiment = client.getExperiment('my_experiment_name');

            return (
              <div>Headline Parameter: {experiment.get('my_experiment_parameter_name', 'fallback_value')}.</div>
            );
            ```
          </Tab>

          <Tab title="Log an Event">
            You can use Events to power metrics in your experiment or gates. Events don't need to be set up in console first, just add to your code:

            ```jsx  theme={null}
            const { client } = useStatsigClient();
            return <button onClick={() => client.logEvent("button_click")}>Click Me</button>
            ```
          </Tab>
        </Tabs>
      </Step>
    </Steps>

    ## Next steps

    Congratulations! You've successfully set up the Statsig SDK in React. Continue on to the tutorials, or jump in to the full [Next.js](/client/Next) or [React](/client/React) SDK libraries.
  </Tab>

  <Tab title="JS snippet" icon="js">
    <Steps>
      <Step title="Paste the code snippet">
        In the `<head>` section of your website, paste the following code snippet:

        ```html  theme={null}
        <script src="https://cdn.jsdelivr.net/npm/@statsig/js-client@3/build/statsig-js-client+session-replay+web-analytics.min.js?apikey=<REPLACE_WITH_YOUR_CLIENT_KEY>"></script>
        ```
      </Step>

      <Step title="Add client key">
        Create a client API key in the [Statsig console Settings](https://console.statsig.com/api_keys). Copy and paste it to replace `<REPLACE_WITH_YOUR_CLIENT_KEY>` in the code snippet from the previous step.
      </Step>

      <Step title="Basic usage">
        <Tabs>
          <Tab title="Check a Gate">
            First, create a gate on the [Feature Gates page](https://console.statsig.com/gates) in console, then check it in-code:

            ```jsx  theme={null}
            window.Statsig.instance().checkGate("my_feature_gate_name");
            ```

            <Note>
              You'll want to wait for the SDK to initialize before checking a gate to ensure it has fresh values, one way to accomplish this is waiting for the ["values\_updated"](/client/javascript-sdk#client-event-emitter) event.
            </Note>
          </Tab>

          <Tab title="Get an Experiment Value">
            First, create an Experiment on the [Experiments page](https://console.statsig.com/experiments) in console

            ```jsx  theme={null}
            window.Statsig.instance().getExperiment("my_experiment_name").get('my_experiment_parameter_name');
            ```

            <Note>
              You'll want to wait for the SDK to initialize before getting an experiment to ensure it has fresh values, one way to accomplish this is waiting for the ["values\_updated"](/client/javascript-sdk#client-event-emitter) event.
            </Note>
          </Tab>

          <Tab title="Log an Event">
            You can use Events to power metrics in your experiment or gates. Events don't need to be set up in console first, just add to your code:

            ```jsx  theme={null}
            window.Statsig.instance().logEvent("my_checkout_event_name", "event_value_item_1234", {"event_metadata": "my_metadata"})
            ```
          </Tab>
        </Tabs>
      </Step>
    </Steps>

    ## Next steps

    Congratulations! You've set up the Statsig JavaScript snippet. You can now start:

    * Start [recording events](/webanalytics/overview)
    * Watch [session replays](/session-replay/overview)
    * Run [experiments](/experiments/overview)
    * Use [feature flags](/feature-flags/overview)

    See the [Javascript SDK reference](/client/javascript-sdk) for more info.
  </Tab>

  <Tab title="Python" icon="python">
    <Steps>
      <Step title="Install the Statsig package">
        ```shell  theme={null}
        pip install statsig-python-core
        ```
      </Step>

      <Step title="Initialize the Statsig SDK">
        ```python  theme={null}
        from statsig_python_core import Statsig, StatsigOptions

        options = StatsigOptions()
        options.environment = "development"

        statsig = Statsig("<REPLACE_WITH_YOUR_SERVER_SECRET_KEY>", options)
        statsig.initialize().wait()

        statsig.shutdown().wait()
        ```
      </Step>

      <Step title="Add server secret key">
        Create a server secret key in the [Statsig console Settings](https://console.statsig.com/api_keys). Copy and paste it to replace `<REPLACE_WITH_YOUR_SERVER_SECRET_KEY>` in the code snippet from the previous step.
      </Step>

      <Step title="Basic Usage">
        <Tabs>
          <Tab title="Check a Gate">
            First, create a gate on the [Feature Gates page](https://console.statsig.com/gates) in console, then check it in-code:

            ```python  theme={null}
            user_object = StatsigUser(user_id="123", email="testuser@statsig.com") //add any number of other attributes
            gate_value = statsig.check_gate(user_object, "my_feature_gate_name"):
            ```
          </Tab>

          <Tab title="Get an Experiment Value">
            First, create an Experiment on the [Experiments page](https://console.statsig.com/experiments) in console

            ```python  theme={null}
            user_object = StatsigUser(user_id="123", email="testuser@statsig.com"
            my_experiment_object = statsig.get_experiment(user_object, "my_experiment_name")
            my_experiment_parameter_value = my_experiment_object.get_string('my_experiment_parameter_name')
            ```
          </Tab>

          <Tab title="Log an Event">
            You can use Events to power metrics in your experiment or gates. Events don't need to be set up in console first, just add to your code:

            ```python  theme={null}
            user_object = StatsigUser(user_id="123", email="testuser@statsig.com"

            statsig.log_event(
              user=user_object,
              event_name="my_checkout_event_name",
              value="SKU_12345"
            )
            ```
          </Tab>
        </Tabs>
      </Step>
    </Steps>

    ## Next steps

    Congratulations! You've set up the Statsig SDK in Python. Continue on to our tutorials, or jump in to the full [Python SDK Reference.](/server-core/python-core)
  </Tab>

  <Tab title="Node" icon="node-js">
    <Steps>
      <Step title="Install the Statsig package">
        ```bash  theme={null}
        npm i @statsig/statsig-node-core
        ```
      </Step>

      <Step tite="Initialize the Statsig SDK">
        ```jsx  theme={null}
        // Basic initialization
        const statsig = new Statsig("<REPLACE_WITH_YOUR_SERVER_SECRET_KEY>");
        await statsig.initialize();

        // or with StatsigOptions
        const options: StatsigOptions = { environment: "staging" };

        const statsigWithOptions = new Statsig("secret-key", options);
        await statsigWithOptions.initialize();
        ```
      </Step>

      <Step title="Add server secret key">
        Create a server secret key in the [Statsig console Settings](https://console.statsig.com/api_keys). Copy and paste it to replace `<REPLACE_WITH_YOUR_SERVER_SECRET_KEY>` in the code snippet from the previous step.
      </Step>

      <Step title="Basic Usage">
        <Tabs>
          <Tab title="Check a Gate">
            First, create a gate on the [Feature Gates page](https://console.statsig.com/gates) in console, then check it in-code:

            ```js  theme={null}
            const userObject = new StatsigUser({ userID: "123", email="testuser@statsig.com" });
            const is_gate_enabled = statsig.checkGate(userObject, "my_feature_gate_name"):
            ```
          </Tab>

          <Tab title="Get an Experiment Value">
            First, create an Experiment on the [Experiments page](https://console.statsig.com/experiments) in console

            ```js  theme={null}
            const userObject = new StatsigUser({ userID: "123", email="testuser@statsig.com" });
            const myExperimentObject = statsig.getExperiment(userObject, "my_experiment_name")
            const myExperimentParameterValue = myExperimentObject.getValue('my_experiment_parameter_name')
            ```
          </Tab>

          <Tab title="Log an Event">
            You can use Events to power metrics in your experiment or gates. Events don't need to be set up in console first, just add to your code:

            ```js  theme={null}
            userObject = StatsigUser(user_id="123", email="testuser@statsig.com"

            statsig.logEvent(
              userObject,
              "my_checkout_event_name",
              "SKU_12345" //value for the event
            );
            ```
          </Tab>
        </Tabs>
      </Step>
    </Steps>

    ## Next steps

    Congratulations! You've successfully set up the Statsig SDK in Node.js. Continue on to the tutorials, or jump in to the full [Node.js](/server-core/node-core) SDK library.
  </Tab>

  <Tab title="+24 more SDKs">
    ## Explore SDKs

    Statsig offers SDKs for a wide variety of platforms to suit any codebase or deployment preference:

    ### Client SDKs

    <Columns cols={3}>
      <Card title="JavaScript" icon="js" href="/client/javascript-sdk" horizontal>
        Browser JavaScript
      </Card>

      <Card title="React" icon="react" href="/client/React" horizontal>
        Client-Side React
      </Card>

      <Card title="React Native" icon="react" href="/client/ReactNative" horizontal>
        Bare React Native SDK
      </Card>

      <Card title="Next.js" icon="n" href="/client/Next" horizontal>
        Next.js SSR, SSG & Client-Side
      </Card>

      <Card title="Angular" icon="angular" href="/client/Angular" horizontal>
        Angular bindings for Javascript SDK
      </Card>

      <Card title="Swift" icon="swift" href="/client/iosClientSDK" horizontal>
        iOS, MacOS, tvOS SDK
      </Card>

      <Card title="Android" icon="android" href="/client/Android" horizontal>
        Android Kotlin/Java SDK
      </Card>

      <Card title=".NET Client" icon="https://mintcdn.com/statsig-4b2ff144/JFwxhctmU_iFZGG5/images/dotnet.svg?fit=max&auto=format&n=JFwxhctmU_iFZGG5&q=85&s=5b8bdbe4fc323f611d34001e982d8181" href="/client/DotNet" horizontal width="456" height="456" data-path="images/dotnet.svg">
        Client SDK for .NET framework
      </Card>

      <Card title="Roku" icon="r" href="/client/Roku" horizontal>
        Roku Brightscript SDK
      </Card>

      <Card title="Unity" icon="unity" href="/client/Unity" horizontal>
        Unity game engine SDK
      </Card>

      <Card title="Dart/Flutter" icon="mobile-screen" href="/client/Dart" horizontal>
        Flutter/Dart Mobile App SDK
      </Card>

      <Card title="C++ Client" icon="code" href="/client/CPP" horizontal>
        C++ client-side SDK
      </Card>
    </Columns>

    ### Server Side SDKs

    <Columns cols={3}>
      <Card title="Node.js" icon="node-js" href="/server-core/node-core" horizontal>
        Node.js server SDK
      </Card>

      <Card title="Java" icon="java" href="/server-core/java-core" horizontal>
        Java server SDK
      </Card>

      <Card title="Python" icon="python" href="/server-core/python-core" horizontal>
        Python server SDK
      </Card>

      <Card title="Go" icon="golang" href="/server/golangSDK" horizontal>
        Go server SDK
      </Card>

      <Card title="Ruby" icon="gem" href="/server/rubySDK" horizontal>
        Ruby server SDK
      </Card>

      <Card title=".NET Server" icon="microsoft" href="/server-core/dotnetCoreSDK" horizontal>
        .NET server SDK
      </Card>

      <Card title="PHP" icon="php" href="/server-core/php-core" horizontal>
        PHP server SDK
      </Card>

      <Card title="Rust" icon="rust" href="/server-core/rust-core" horizontal>
        Rust server SDK
      </Card>

      <Card title="C++ Server" icon="code" href="/server-core/cpp-core" horizontal>
        C++ server SDK
      </Card>
    </Columns>

    ### Integrations

    <Columns cols={3}>
      <Card title="Webflow" icon="w" href="/guides/webflow-sidecar-ab-test" horizontal>
        Webflow integration
      </Card>

      <Card title="Shopify" icon="shopify" href="/guides/shopify-ab-test" horizontal>
        Shopify integration
      </Card>

      <Card title="Segment" icon="chart-pie" href="/integrations/data-connectors/segment" horizontal>
        Segment data connector
      </Card>

      <Card title="Rudderstack" icon="layer-group" href="/integrations/data-connectors/rudderstack" horizontal>
        Rudderstack connector
      </Card>

      <Card title="Hightouch" icon="cloud-arrow-up" href="/integrations/data-connectors/hightouch" horizontal>
        Hightouch integration
      </Card>

      <Card title="mParticle" icon="share-nodes" href="/integrations/data-connectors/mparticle" horizontal>
        mParticle connector
      </Card>

      <Card title="Framer" icon="f" href="/guides/framer-analytics" horizontal>
        Framer integration
      </Card>

      <Card title="Slack" icon="slack" href="/integrations/slack" horizontal>
        Slack notifications
      </Card>

      <Card title="Integrations" icon="puzzle" href="/integrations/introduction" horizontal>
        View more integrations
      </Card>
    </Columns>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).