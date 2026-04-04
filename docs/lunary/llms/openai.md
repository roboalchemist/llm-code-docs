# Source: https://docs.lunary.ai/docs/integrations/python/openai.md

# Source: https://docs.lunary.ai/docs/integrations/openai.md

# Source: https://docs.lunary.ai/docs/integrations/javascript/openai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# JS OpenAI integration

Our SDKs include automatic integration with OpenAI's modules.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={1}>
      <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to set up the JS SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Monitor OpenAI">
    With our SDKs, tracking OpenAI calls is super simple.

    ```js  theme={null}
    import OpenAI from "openai";
    import { monitorOpenAI } from "lunary/openai";

    // Simply call monitor() on the OpenAIApi class to automatically track requests
    const openai = monitorOpenAI(new OpenAI());
    ```
  </Step>

  <Step n="3" title="Tag requests and identify users">
    You can now tag requests and identify users.

    ```js  theme={null}
    const result = await openai.chat.completions.create({
      model: "gpt-4o",
      temperature: 0.9,
      tags: ["chat", "support"], // Optional: tags
      user: "user_123", // Optional: user ID
      userProps: { name: "John Doe" }, // Optional: user properties
      messages: [
        { role: "system", content: "You are an helpful assistant" },
        { role: "user", content: "Hello friend" },
      ],
    });
    ```
  </Step>
</Steps>
