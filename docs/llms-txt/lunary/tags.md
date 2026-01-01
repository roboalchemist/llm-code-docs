# Source: https://docs.lunary.ai/docs/features/tags.md

# Tagging

Tags allow you to label queries and completions.

This is useful to further segment your data. For example, you can label all the queries that are related to a specific feature or a specific company.

Later on, this can also be useful for creating fine-tune datasets.

<Steps>
  <Step n="1" title="Setup the SDK">
    <CardGroup cols={2}>
      <Card title="Python" icon="python" href="/docs/integrations/python/installation">
        Learn how to install the Python SDK.
      </Card>

      <Card title="JavaScript" icon="js" href="/docs/integrations/javascript/installation">
        Learn how to install the JS SDK.
      </Card>
    </CardGroup>
  </Step>

  <Step n="2" title="Simplest: Identify OpenAI calls">
    The easiest way to get started adding tags is to send them when doing your OpenAI API calls.

    <Tabs>
      <Tab title="Javascript">
        ```js  theme={null}
        const res = await openai.chat.completions.create({
          model: "gpt-4o",
          messages: [{ role: "user", content: "Hello" }],
          tags: ["some-tag"]
        })
        ```
      </Tab>

      <Tab title="Python">
        ```py  theme={null}
        chat_completion = client.chat.completions.create(
          messages=[{"role": "user", "content": "Say this is a test"}],
          model="gpt-4o",
          tags=["some-tag"],
        )
        ```
      </Tab>
    </Tabs>

    If you're using LangChain, you can similarly pass the tags on any LangChain object.

    <Tabs>
      <Tab title="Javascript">
        ```js  theme={null}
        const chat = new ChatOpenAI({
          callbacks: [new LunaryHandler()],
        });

        const res = await chat.call([new HumanMessage("Hello!")], {
        tags: ["some-tag"],
        });

        ```
      </Tab>

      <Tab title="Python">
        ```py  theme={null}
        handler = LunaryCallbackHandler()

        chat = ChatOpenAI(
          callbacks=[handler],
          tags=["some-tag"],
        )
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step n="3" title="Advanced: Inject tag into context">
    You can also inject tags into the context of your code. This is useful if you want to tag all the queries that are related to a specific feature or a specific company.

    <Tabs>
      <Tab title="Javascript">
        ```js  theme={null}
        Coming soon
        ```
      </Tab>

      <Tab title="Python">
        ```py  theme={null}
        import lunary
        # Method 2: everything inside the with statement will have tags2 and tags3
        with lunary.tags(["tag2", "tag3"]):
          my_agent()
        ```
      </Tab>
    </Tabs>
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt