# Source: https://docs.asapp.com/generativeagent/configuring/previewer.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Previewer

> Learn how to use the Previewer in AI Console to test and refine your GenerativeAgent's behavior

The Previewer is a testing and simulation tool that allows you to try out different configurations of your GenerativeAgent's behavior.

The Previewer makes it easy to rapidly iterate on GenerativeAgent's design and provides a quick tool to test GenerativeAgent's capabilities.

<Frame>
  <img src="https://mintcdn.com/asapp/c-LDHupSgFxlqz3x/images/generativeagent/configuring/Opening-previewer.gif?s=aa9783ca3216467cff3c1d8e01c939a3" alt="Opening the Previewer in AI Console" data-og-width="1532" width="1532" data-og-height="1062" height="1062" data-path="images/generativeagent/configuring/Opening-previewer.gif" data-optimize="true" data-opv="3" />
</Frame>

## Using Previewer

To use the Previewer, select one of two modes:

1. **"Talk to GenerativeAgent"** to manually interact with GenerativeAgent by typing out messages as the customer.
2. **"Simulate a customer and conversation"** to automatically generate a conversation from a Test Scenario. This is useful when you want to test GenerativeAgent's behavior with a specific set of data.

   Starting the conversation will run the Test scenario.

   <Tip>
     To use 'Simulate a customer and conversation' the goals need to be populated in your selected [Test Scenario](/generativeagent/configuring/tasks-and-functions/test-scenarios).
   </Tip>

You can also select the [previewing environment](#previewer-environment) that GenerativeAgent uses to test and preview a conversation with GenerativeAgent. This defaults to Draft.

### Previewer Environment

Choose the [Environment](/generativeagent/configuring/deploying-to-generativeagent#environments) that GenerativeAgent uses to test and preview a conversation with GenerativeAgent.

Choose between:

* Draft
* Sandbox
* Production

<Frame>
  <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ChooseEnvironment.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=4c9127763a6606028bcd6502d849de27" data-og-width="306" width="306" data-og-height="209" height="209" data-path="images/generativeagent/ChooseEnvironment.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ChooseEnvironment.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=961c81a47e1116cbcffa53bd0b2e34be 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ChooseEnvironment.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=27c1ab67ee2cabebb2fa4cdbaef8f146 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ChooseEnvironment.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=c538592f8a373727d40ea7c758cde235 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ChooseEnvironment.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=d7019da0c6a25a103c2f8f63cd218207 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ChooseEnvironment.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=be8a781f2152e419af550ccd8e86ce8b 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/ChooseEnvironment.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=3b81bfcc1d9acffd8efd2c1c5a3abfa6 2500w" />
</Frame>

## Talk to GenerativeAgent

"Talk to GenerativeAgent" enables you to manually interact with GenerativeAgent. This is useful for initial testing of your task and function configurations.

### Test Scenario Type

When directly talking to GenerativeAgent, you can choose what kind of data GenerativeAgent will use for its function calls by selecting the "Scenario type":

* **Test Scenario**: This uses the data from a previously created [Test Scenario](/generativeagent/configuring/tasks-and-functions/test-scenarios) where you have already defined a simulated mock data that a function would return. This allows you to try out different Tasks and iterate on tasks definitions or on Functions without concern of hitting actual APIs.
* **External Endpoint**: This will use the actual API Connections, allowing you to test GenerativeAgent using real APIs and data.

Most preview testing uses test scenarios as it is faster to design iterations. The External Endpoint is helpful for final QA testing and pre-launch validation.

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioTypePreviewer.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=60b04263cd03b89ef988049ca781f4b6" data-og-width="1402" width="1402" data-og-height="1270" height="1270" data-path="images/generativeagent/TestScenarioTypePreviewer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioTypePreviewer.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ca202c87ff6f3a930e18385432deae45 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioTypePreviewer.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=ab857e005efee3d7234b9426137e6390 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioTypePreviewer.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=c6dbbd9f274586f1da45fa40c4003d12 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioTypePreviewer.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=0ba19b7be2f0cae8a7fd1d63302be793 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioTypePreviewer.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=cb3513c41abd5bb94ab895877c6a3a27 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TestScenarioTypePreviewer.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=d41cfd316523ff63063e73139f04b5a1 2500w" />
</Frame>

### External Endpoint

When using the External Endpoint, you can provide:

* User ID: This is an id of the user for the conversation. This is needed as ASAPP's APIs require it and many APIs rely on it.
* Task Name: The [specific task for GenerativeAgent to enter](/generativeagent/configuring/tasks-and-functions/enter-specific-task).
* Input Variables: This is the [input variables data](/generativeagent/configuring/tasks-and-functions/input-variables) that GenerativeAgent will use to perform the Task.

  <Note>
    Input variables can be submitted as key-value pairs in JSON format.
  </Note>

  <Frame>
    <img src="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=867cfca044e67cb9cefc81e0a4c6fdfd" data-og-width="534" width="534" data-og-height="1236" height="1236" data-path="images/generativeagent/InputVariables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=280&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=8ee07535e7db6ee619d91355d00fbdac 280w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=560&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=55028fab1a5c01bb0f5127e56aef2a61 560w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=840&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=e4fcdb030d1a64324a53638c1ae63370 840w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=1100&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=82aa95bed8e5003ce1beb742fd773ac8 1100w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=1650&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=cfe3e3b949cc960abb902c9d0b5ae153 1650w, https://mintcdn.com/asapp/oWc-pd36yCvpD40u/images/generativeagent/InputVariables.png?w=2500&fit=max&auto=format&n=oWc-pd36yCvpD40u&q=85&s=da9555c5f20c726e502624d0b4f67fad 2500w" />
  </Frame>

## Observing GenerativeAgent's Behavior

Previewer gives you insight into the actions that GenerativeAgent is taking with the **Turn inspector**. This includes its thoughts during the conversation, the Knowledge Base articles it references, and the API calls it makes.

Use the Turn Inspector to examine how instructions are processed within GenerativeAgent.

Turn Inspector includes detailed visibility into:

* Active Task Configuration
* Current reference variables
* Precise instruction parsing
* Function call context and parameters
* Execution state at each conversational turn

<Frame>
  <img src="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=a9786a9830cb1ef62896cf38fadf9b5c" data-og-width="598" width="598" data-og-height="919" height="919" data-path="images/generativeagent/TurnInspector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=280&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5412035082402d7db9fc291547ada4c9 280w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=560&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=328366cd8d46b62a62963b463e5a0cd6 560w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=840&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3d9df75c9e2cc2ca3c09539c97569d5a 840w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=1100&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=7d49297d2d6cee7f9998b57642135d7f 1100w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=1650&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=3c2fd6930b78ed835e4c6efec5ec1eb5 1650w, https://mintcdn.com/asapp/5vfIXwfnKhACH2a_/images/generativeagent/TurnInspector.png?w=2500&fit=max&auto=format&n=5vfIXwfnKhACH2a_&q=85&s=5a15c51f78cab842527b72035732b48b 2500w" />
</Frame>

### Using Live Preview

The Live Preview feature allows you to test changes in real-time during a conversation. You have the ability to:

* **Regenerate a response**: For a given bot response, regenerate it using the latest state of the draft settings.
* **Send a different message**: For a given customer message, change what is sent to see how GenerativeAgent would respond with that conversation context.

<Frame>
  <img src="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png?fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=c31e197a6fecc753cff1d3a4edfca28f" alt="Live Preview feature in AI Console Previewer" data-og-width="762" width="762" data-og-height="703" height="703" data-path="image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png?w=280&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=1df1c83860ba8e6a5e01be694ca32841 280w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png?w=560&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=9ce71da9e8ab71bf0021646988fbeda0 560w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png?w=840&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=d29630c158217c26031c400e03eb8cda 840w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png?w=1100&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=9280ea5dc141770b2e24a2ebf6586f7d 1100w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png?w=1650&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=4233092ca6f3afe6ff099441f284a72a 1650w, https://mintcdn.com/asapp/aK0YOQVZSULmKYJl/image/uuid-7e037841-239a-0b66-6c05-f1f301ed206f.png?w=2500&fit=max&auto=format&n=aK0YOQVZSULmKYJl&q=85&s=9f3f278c16a1a89cc236991e7e17ea9f 2500w" />
</Frame>

### Replaying Conversations

During testing and configuration, you may want to replay conversations while trying out changes or validating GenerativeAgent across new versions. In Previewer, you can save the conversation to replay it again in the future.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=e83152be80e7941fb6f530439186e018" alt="Save conversation option in AI Console Previewer" data-og-width="561" width="561" data-og-height="986" height="986" data-path="image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=b56b11494ade863b4bfee4c71d61015f 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=6d6156cc85a638b1e5eebe15e186e2ef 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=393265c4e6811a31392866eb1be6dc29 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=20ad988c9fe00d4537e081d5d8bf60d6 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=1e5a1a834c959f7b35f4d62d119f96d6 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-8bbbdf91-7ce0-1426-fa95-abc8dc1c17fe.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=40763ca3371bce10d4942e40a05b7ceb 2500w" />
</Frame>

## Next Steps

You may find one of the following sections helpful in advancing your integration:

<CardGroup>
  <Card title="Integrate GenerativeAgent" href="/generativeagent/integrate" />

  <Card title="Safety and Troubleshooting" href="/generativeagent/configuring/safety-and-troubleshooting" />

  <Card title="Go Live" href="/generativeagent/go-live" />
</CardGroup>
