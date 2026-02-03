# Source: https://docs.lunary.ai/docs/integrations/javascript/anthropic.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JS Anthropic integration

Our SDKs include automatic integration with Anthropic's modules.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to set up the JS SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor OpenAI">
    With our SDKs, tracking Anthropic calls is super simple.

    ```js  theme={null}
    import Anthropic from "@anthropic-ai/sdk"
    import { monitorAnthropic } from "lunary/anthropic"

    // Simply call monitor() on the Anthropic class to automatically track requests
    const anthropic = monitorAnthropic(new Anthropic())
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    You can now tag requests and identify users.

    ```js  theme={null}
    const result = await anthropic.messages.create({
      model: "claude-3-5-sonnet-20240620",
      temperature: 0.9,
      tags: ["chat", "support"],  // Optional: tags
      userId: "user_123",  // Optional: user ID
      userProps: { name: "John Doe" },  // Optional: user properties
      system: "You are an helpful assistant",
      messages: [
        { role: "user", content: "Hello friend" },
      ],
    })
    ```
  </Step>
</Steps>
