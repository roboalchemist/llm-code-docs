# Source: https://docs.statsig.com/client/Roku.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Roku Client SDK

> Statsig's SDK for Experimentation and Feature Flags in Roku applications.

<Callout icon="github">
  Source code: <a href="https://github.com/statsig-io/roku-sdk" target="_blank" rel="noreferrer">statsig-io/roku-sdk</a>
</Callout>

## Setup the SDK

<Steps>
  <Step title="Install the SDK">
    You can start by downloading a copy of [the GitHub repository](https://github.com/statsig-io/roku-sdk). Roku does not have a package manager where we could release an SDK, so instead, you will copy over the implementation from this repository to integrate Statsig in your Roku app.

    You will need the following files:

    ```
    Statsig
      -- components
        -- statsigsdk
          -- StatsigTask.brs
          -- StatsigTask.xml
      -- source
        -- DynamicConfig.brs
        -- Statsig.brs
        -- StatsigClient.brs
        -- StatsigUser.brs
    ```

    The library consists of two main parts:

    * **source/Statsig** - an object used by SceneGraph components that connects a StatsigClient with the background StatsigTask.
    * **components/StatsigTask** - a SceneGraph Task to do work in the background for integrating with Statsig like batching events and fetching values from Statsig servers.

    The "components" folder contains SceneGraph components and the "source" folder contains BrightScript files. All of these files must be included in their respective folders of the application. Note that if you change the file paths, you will need to update the file references in `StatsigTask.xml`. You will also need to include those references in your main XML file.
  </Step>

  <Step title="Initialize the SDK">
    Next, initialize the SDK with a client SDK key from the ["API Keys" tab on the Statsig console](https://console.statsig.com/api_keys). These keys are safe to embed in a client application.

    Along with the key, pass in a [User Object](#statsig-user) with the attributes you'd like to target later on in a gate or experiment.

    To Initialize the SDK, you first need to integrate the SDK files into your application.

    Include `StatsigClient.brs`, `StatsigUser.brs`, `DynamicConfig.brs`, and `Statsig.brs`:

    ```xml  theme={null}
    <script type="text/brightscript" uri="pkg:/source/Statsig.brs" />
    <script type="text/brightscript" uri="pkg:/source/StatsigClient.brs" />
    <script type="text/brightscript" uri="pkg:/source/StatsigUser.brs" />
    <script type="text/brightscript" uri="pkg:/source/DynamicConfig.brs" />
    ```

    Next, you can initialize the library in your init() function, and add a listener for when gates/experiments have been fetched:

    ```xml  theme={null}
    <!-- in component xml -->
    <StatsigTask id="statsigTask" />
    ```

    ```brightscript  theme={null}
        statsigTask = m.top.findNode("statsigTask")
        statsigTask.observeField("initializeValues", "onStatsigReady")
        m.statsig = Statsig(statsigTask)

        user = StatsigUser()
        user.setUserID("456")
        m.statsig.initialize("<STATSIG_CLIENT_SDK_KEY>", user)
    ```

    For more information on all of the user fields you can use, see the [StatsigUser docs](/concepts/user).

    Before the SDK has loaded the updated values, all APIs will return default values (false for gates, empty configs and experiments).

    To implement a callback handler for Statsig being ready, and tell the SDK to load the updated values in the `onStatsigReady` function observed above:

    ```brightscript  theme={null}
    function onStatsigReady() as void
        m.statsig.load()

        // Check gates, log events, check experiments, etc
        gate = m.statsig.checkGate("gate_id")
        config = m.statsig.getConfig("config_id")
        experiment = m.statsig.getExperiment("experiment_id")
        m.statsig.logEvent("event_name", "event_value", {metadata: "event_metadata"})
    end function
    ```

    If you need to update the user, `m.statsig.updateUser(newUser)` will trigger the same `onStatsigReady` callback once the new gate/config/experiment values have been fetched from Statsig servers.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).