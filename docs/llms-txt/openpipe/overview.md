# Source: https://docs.openpipe.ai/overview.md

# Source: https://docs.openpipe.ai/features/evaluations/overview.md

# Source: https://docs.openpipe.ai/features/dpo/overview.md

# Source: https://docs.openpipe.ai/features/datasets/overview.md

# Source: https://docs.openpipe.ai/features/criteria/overview.md

# Source: https://docs.openpipe.ai/features/chat-completions/overview.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat Completions

Once your fine-tuned model is deployed, you're ready to start generating chat completions.

First, make sure you've set up the SDK properly. See the [OpenPipe SDK](/getting-started/openpipe-sdk) section for more details. Once the SDK is installed and you've added the right
`OPENPIPE_API_KEY` to your environment variables, you're almost done.

The last step is to update the model that you're querying to match the ID of your new fine-tuned model.

<Tabs>
  <Tab title="Python">
    ```python  theme={null}
    from openpipe import OpenAI

    # Find the config values in "Installing the SDK"
    client = OpenAI()

    completion = client.chat.completions.create(
        # model="gpt-4o", - original model
        model="openpipe:your-fine-tuned-model-id",
        messages=[{"role": "system", "content": "count to 10"}],
        metadata={"prompt_id": "counting", "any_key": "any_value"},
    )
    ```
  </Tab>

  <Tab title="NodeJS">
    ```typescript  theme={null}
    import OpenAI from "openpipe/openai";

    // Find the config values in "Installing the SDK"
    const client = OpenAI();

    const completion = await client.chat.completions.create({
      // model: "gpt-4o", - original model
      model: "openpipe:your-fine-tuned-model-id",
      messages: [{ role: "user", content: "Count to 10" }],
      metadata: {
        prompt_id: "counting",
        any_key: "any_value",
      },
    });
    ```
  </Tab>
</Tabs>

Queries to your fine-tuned models will now be shown in the [Request Logs](/features/request-logs) panel.

<Frame><img src="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/running-inference-logs.png?fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=9793a1cf9b93f47f780dbb5511db13ea" alt="" data-og-width="2246" width="2246" data-og-height="1084" height="1084" data-path="images/features/running-inference-logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/running-inference-logs.png?w=280&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=b6a26c678ae6926fad357248886ad4b0 280w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/running-inference-logs.png?w=560&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=cba67de1872e47766d203c7fc0db4129 560w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/running-inference-logs.png?w=840&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=33e0faca772dd1316c2467887bb8625d 840w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/running-inference-logs.png?w=1100&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=bead6f5bf0bc44768f3cd9ecc2f37505 1100w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/running-inference-logs.png?w=1650&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=0ddfcb40319668e83ddfb62c52775fe2 1650w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/running-inference-logs.png?w=2500&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=07498ed95d5d073f0d9be10d46949f1f 2500w" /></Frame>

Feel free to run some sample inference on the [PII Redaction model](https://app.openpipe.ai/p/BRZFEx50Pf/fine-tunes/efb0d474-97b6-4735-a0af-55643b50600a/general) in our public project.
