# Source: https://docs.lunary.ai/docs/features/prompts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.lunary.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Prompt Templates

Prompt templates are a way to store, version and collaborate on prompts.

Developers use prompt templates to:

* clean up their source code
* make edits to prompts without re-deploying code
* collaborate with non-technical teammates
* A/B test prompts

## Creating a template

You can create a prompt template by clicking on the "Create prompt template" button in the Prompts section of the dashboard.

## Usage with OpenAI

You can use templates seamlessly with OpenAI's API with our SDKs.

This will make sure the tracking of the prompt is done automatically.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    import OpenAI from "openai";
    import lunary from "lunary"
    import { monitorOpenAI } from "lunary/openai";

    // Make sure your OpenAI instance is wrapped with `monitorOpenAI`
    const openai = monitorOpenAI(new OpenAI())

    const template = await lunary.renderTemplate("template-slug", {
    name: "John", // Inject variables
    })

    const result = await openai.chat.completions.create(template)

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary
    from openai import OpenAI

    client = OpenAI()

    # Make sure your OpenAI instance is monitored
    lunary.monitor(client)

    template = lunary.render_template("template-slug", {
      "name": "John", # Inject variables
    })

    result = client.chat.completions.create(**template)
    ```
  </Tab>
</Tabs>

## Usage with LangChain's templates

You can pull templates in the LangChain format and use them directly as PromptTemplate and ChatPromptTemplate classes.

Example with simple text template:

<Tabs>
  <Tab title="Javascript">
    The `getLangChainTemplate` method returns a `PromptTemplate` object for simple templates, which can be used directly in chains or to format prompts.

    ```js  theme={null}
    import { getLangChainTemplate } from "lunary/langchain";

    const prompt = await getLangChainTemplate("icecream-prompt");

    const promptValue = await prompt.invoke({ topic: "ice cream" });

    console.log(promptValue);
    ```
  </Tab>

  <Tab title="Python">
    The `get_langchain_template` method returns a `PromptTemplate` object for simple templates, which can be used directly in chains or to format prompts.

    ```py  theme={null}
    import lunary

    template = lunary.get_langchain_template("my-template")

    prompt = template.format(question="What is the capital of France?")
    ```
  </Tab>
</Tabs>

Example with a Chat template (ChatPromptTemplate):

<Tabs>
  <Tab title="Javascript">
    The `getLangChainTemplate` function directly returns a `ChatPromptTemplate` object for chat messages templates, which can be used to format messages.

    ```js  theme={null}
    import { getLangChainTemplate } from "lunary/langchain";

    const prompt = await getLangChainTemplate("context-prompt");

    const promptValue = await prompt.invoke({ topic: "ice cream" });

    console.log(promptValue);
    /**
    ChatPromptValue {
      messages: [
        HumanMessage {
          content: 'Tell me a short joke about ice cream',
          name: undefined,
          additional_kwargs: {}
        }
      ]
    }
    */
    ```
  </Tab>

  <Tab title="Python">
    The `get_langchain_template` method returns a `ChatPromptTemplate` object for chat messages templates, which can be directly in chains or to format messages.

    ```py  theme={null}
    template = lunary.get_langchain_template("my-template")

    messages = lc_template.format_messages(question="What is the capital of France?")
    ```
  </Tab>
</Tabs>

## Manual LangChain Usage with LLM Classes

Using with LangChain LLM Classes is similar to using with OpenAI, but requires you to format the messages in the LangChain format as well as pass the template id in the metadata.

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    Coming soon
    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    from langchain_openai import ChatOpenAI
    from langchain_community.adapters.openai import convert_openai_messages
    from lunary import render_template, LunaryCallbackHandler

    template = render_template("template-slug", {
    "name": "John", # Inject variables
    })

    chat_model = ChatOpenAI(
    model=template["model"],
    metadata={
    "templateId": template["templateId"] # Optional: this allows to reconcile the logs with the template
    },

    # add any other parameters here...

    temperature=template["temperature"],
    callbacks=[LunaryCallbackHandler()]
    )

    # Convert messages to LangChain format

    messages = convert_openai_messages(template["messages"])

    result = chat_model.invoke(messages)

    ```
  </Tab>
</Tabs>

## Manual usage

You can also use templates manually with any LLM API by accessing the relevant fields (returned in OpenAI's format).

<Tabs>
  <Tab title="Javascript">
    ```js  theme={null}
    import lunary from "lunary"

    const {
      messages,
      model,
      temperature,
      max_tokens
    } = await lunary.renderTemplate("template-slug", {
      name: "John", // Inject variables
    })


    // ... use the fields like you want

    ```
  </Tab>

  <Tab title="Python">
    ```py  theme={null}
    import lunary

    template = lunary.render_template("template-slug", {
    "name": "John", # Inject variables
    })

    messages = template["messages"]
    model = template["model"]
    temperature = template["temperature"]
    max_tokens = template["max_tokens"]

    # ... use the fields like you want

    ```
  </Tab>
</Tabs>

## Testing Prompts

The Prompt Playground provides a powerful interactive environment for testing and refining your prompts. You can experiment with different models, parameters, and even test against custom API endpoints.

[Learn more about the Prompt Playground →](/docs/features/prompt-playground)
