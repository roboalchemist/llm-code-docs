# Source: https://docs.linkup.so/pages/integrations/friendliai/friendliai.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# FriendliAI

> Use Linkup as a web search tool for LLMs served by FriendliAI

FriendliAI provides fast, efficient and reliable AI inference. Linkup provides real-time web search capabilities that can be seamlessly integrated with models served by FriendliAI. This combination allows your AI applications to access up-to-date information beyond the model's training data, enabling you to create applications that retrieve current facts, information, and events with accurate citations.

## FriendliAI's Playground

Linkup's web search can be turned on directly in FriendliAI's API playground.

<img src="https://mintcdn.com/linkup-8b5c238e/NgcY_e-KwQ9dAfRR/pages/integrations/friendliai/assets/playground.png?fit=max&auto=format&n=NgcY_e-KwQ9dAfRR&q=85&s=eca45271a2fe0c2f3c8cf55812667f7d" alt="Playground" width="1814" height="1061" data-path="pages/integrations/friendliai/assets/playground.png" />

## FriendliAI's API Integitgration

Linkup's web search can be integrated as a default tool in calls made to the FriendliAI serverless APIs, simply by adding `"tools": [{ "type": "linkup:search" }]` in your OpenAI format API call.

To that end, follow these steps:

<Steps>
  <Step title="Create your FriendliAI account">
    Create a new [FriendliAI account](https://friendli.ai/) if you don't have one yet.
  </Step>

  <Step title="Subscribe to the free trial">
    You need to enroll in the Serverless Endpoints product free trial. Information can be found [here](https://friendli.ai/docs/guides/free_credits?_gl=1*12pdpy8*_gcl_au*MTMwNDY4MzczNS4xNzU1MDc1NDA5#receiving-when-you-start).
  </Step>

  <Step title="Add your Linkup API key to your FriendliAI account">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>

    In Friendli Suite, open Personal settings > Integrations and add your Linkup API key.
  </Step>

  <Step title="Make your first API call">
    In the following code snippet, `FRIENDLI_TOKEN` refers to your Personal Access Token, which you can obtain from Personal settings > Settings > Tokens [(guide)](https://friendli.ai/docs/guides/personal_access_tokens?_gl=1*bqbtwa*_gcl_au*MTMwNDY4MzczNS4xNzU1MDc1NDA5).
    <Note>Make sure your Linkup integration is enabled in your Friendli account before calling the API — otherwise the `linkup:search` tool will error.</Note>

    <CodeGroup>
      ```python python theme={null}
      import os
      from openai import OpenAI

      client = OpenAI(
          api_key=os.getenv("FRIENDLI_TOKEN"),
          base_url="https://api.friendli.ai/serverless/tools/v1",
      )

      completion = client.chat.completions.create(
          model="meta-llama-3.1-8b-instruct",
          messages=[
              {
                  "role": "user",
                  "content": "Find information on the popular movies currently showing in theaters and provide their ratings."
              }
          ],
          tools=[{"type": "linkup:search"}],
          stream=False
      )

      print(completion.choices[0].message.content)
      ```

      ```shell curl theme={null}
      curl --request POST \
        --url https://api.friendli.ai/serverless/tools/v1/chat/completions \
        --header 'Authorization: Bearer <FRIENDLI_TOKEN>' \
        --header 'Content-Type: application/json' \
        --data '{
          "model": "meta-llama-3.1-8b-instruct",
          "messages": [
            {
              "content": "Find information on the popular movies currently showing in theaters and provide their ratings.",
              "role": "user"
            }
          ],
          "tools": [
            { "type": "linkup:search" }
          ]
        }'
      ```
    </CodeGroup>
  </Step>
</Steps>

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).