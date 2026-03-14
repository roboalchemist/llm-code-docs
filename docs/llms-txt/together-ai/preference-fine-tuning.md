# Source: https://docs.together.ai/docs/preference-fine-tuning.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.together.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Preference Fine-Tuning

> Learn how to use preference fine-tuning on Together Fine-Tuning Platform

Preference fine-tuning allows you to train models using pairs of preferred and non-preferred examples. This approach is more effective than standard fine-tuning when you have paired examples that show which responses your model should generate and which it should avoid.

We use [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290) for this type of fine-tuning.

Before proceeding: Review our [How-to: Fine-tuning](/docs/fine-tuning-quickstart) guide for an overview of the fine-tuning process.

## Data Preparation

Your dataset should contain examples with:

* An `input` field with messages in in the [conversational format](/docs/fine-tuning-data-preparation#conversational-data).
* A `preferred_output` field with the ideal assistant response
* A `non_preferred_output` field with a suboptimal assistant response

Both outputs must contain exactly one message from the assistant role.

Format your data in `JSONL`, with each line structured as:

<CodeGroup>
  ```json JSON theme={null}
  {
    "input": {
      "messages": [
        {
          "role": "assistant",
          "content": "Hello, how can I assist you today?"
        },
        {
          "role": "user",
          "content": "Can you tell me about the rise of the Roman Empire?"
        }
      ]
    },
    "preferred_output": [
      {
        "role": "assistant",
        "content": "The Roman Empire rose from a small city-state founded in 753 BCE. Through military conquests and strategic alliances, Rome expanded across the Italian peninsula. After the Punic Wars, it grew even stronger, and in 27 BCE, Augustus became the first emperor, marking the start of the Roman Empire. This led to a period of peace and prosperity known as the Pax Romana."
      }
    ],
    "non_preferred_output": [
      {
        "role": "assistant",
        "content": "The Roman Empire rose due to military strength and strategic alliances."
      }
    ]
  }
  ```
</CodeGroup>

<Note>
  Preference-tuning does not support pretokenized datasets. [Contact us](https://www.together.ai/contact) if you need to use them for preference training.
</Note>

## Launching preference fine-tuning

### Hyperparameters

* Set `--training-method="dpo"`

* The `--dpo-beta` parameter controls how much the model is allowed to deviate from its reference (or pre-tuned) model during fine-tuning. The default value is `0.1` but you can experiment with values between `0.05-0.9`

  * A lower value of beta (e.g., 0.1) allows the model to update more aggressively toward preferred responses
  * A higher value of beta(e.g., 0.7) keeps the updated model closer to the reference behavior.

* The `--dpo-normalize-logratios-by-length` parameter (optional, default is False) enables normalization of log ratios by sample length during the DPO loss calculation.

* The `--rpo-alpha` coefficient (optional, default is 0.0) incorporates the NLL loss on selected samples with the corresponding weight.

* The `--simpo-gamma` coefficient (optional, default is 0.0) adds a margin to the loss calculation, force-enables log ratio normalization (--dpo-normalize-logratios-by-length), and excludes reference logits from the loss computation. The resulting loss function is equivalent to the one used in the [SimPO](https://arxiv.org/pdf/2405.14734) paper.

<CodeGroup>
  ```shell CLI theme={null}
  together fine-tuning create \
    --training-file $FILE_ID \
    --model "meta-llama/Llama-3.2-3B-Instruct" \
    --wandb-api-key $WANDB_API_KEY \
    --lora \
    --training-method "dpo" \
    --dpo-beta 0.2
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))
  file_id = "your-training-file"

  response = client.fine_tuning.create(
      training_file=file_id,
      model="meta-llama/Llama-3.2-3B-Instruct",
      lora=True,
      training_method="dpo",
      dpo_beta=0.2,
      rpo_alpha=1.0,
      simpo_gamma=1.0,
  )

  print(response)
  ```
</CodeGroup>

<Note>
  **Note**

  * For [LoRA Long-context fine-tuning](/docs/fine-tuning-models#lora-long-context-fine-tuning) we currently use half of the context length for the preferred response and half for the non-preferred response. So, if you are using a 32K model, the effective context length will be 16K.
  * Preference fine-tuning calculates loss based on the preferred and non-preferred outputs. Therefore, the `--train-on-inputs` flag is ignored with preference fine-tuning.
</Note>

## Metrics

In addition to standard metrics like losses, for DPO we report:

* Accuracies — percentage of times the reward for the preferred response is greater than the reward for the non-preferred response.
* KL Divergence — similarity of output distributions between the trained model and the reference model, calculated as:

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=b8b1d25445ba1bba2b9030465513163f" alt="" width="1576" height="224" data-path="images/docs/c022c68159e4bcdf1259286862bcee5746caa48e79e29946172d1c257af9920d-image.png" />
</Frame>

## Combining methods: supervised fine-tuning & preference fine-tuning

Supervised fine-tuning (SFT) is the default method on our platform. The recommended approach is to first perform SFT followed up by preference tuning as follows:

1. First perform [supervised fine-tuning (SFT)](/docs/finetuning) on your data.
2. Then refine with preference fine-tuning using [continued fine-tuning](/docs/finetuning#continue-a-fine-tuning-job) on your SFT checkpoint.

Performing SFT on your dataset prior to DPO can significantly increase the resulting model quality, especially if your training data differs significantly from the data the base model observed during pretraining. To perform SFT, you can concatenate the context with the preferred output and use one of our [SFT data formats](/docs/fine-tuning-data-preparation#data-formats) .


Built with [Mintlify](https://mintlify.com).