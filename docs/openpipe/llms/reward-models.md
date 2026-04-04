# Source: https://docs.openpipe.ai/features/fine-tuning/reward-models.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.openpipe.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Reward Models (Beta)

>  Train reward models to judge the quality of LLM responses based on preference data.

In addition to training models to generate completions, OpenPipe allows you to train reward models to judge the quality of LLM responses based on preference data.

### Preparing preference data

Currently, OpenPipe supports training reward models from preference data (training reward models based on rewards directly is in the works). Preference data is a dataset of pairs of responses in which one response is better than another.

One way to gather such a dataset is to present users with two LLM completions and ask them to select the better one. Another way is to allow users to regenerate a response until they are satisfied with the output, then associate the original and final generated responses as a pair, with the final response being the preferred one. Whether you gather your preference data from your users or through a different process, it needs to match the JSONL preference data format shown below:

```jsonl  theme={null}
...
{"messages":[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"What is the capital of Tasmania?"},{"role":"assistant","content":"Hobart"}], "rejected_message":{"role": "assistant", "content": "Paris"}, "split": "TRAIN"}
{"messages":[{"role":"system","content":"You are a helpful assistant"},{"role":"user","content":"What is the capital of Sweden?"},{"role":"assistant","content":"Stockholm"}], "rejected_message":{"role": "assistant", "content": "London"}, "split": "TRAIN"}
...
```

Note that the `rejected_message` field should contain the rejected response, and the final `assistant` message should be the preferred response. Conveniently, this is the same data format used for [DPO](/features/dpo/overview), which allows you to train both reward and completion models from the same dataset.

### Training a reward model

Once you've added your preference data to a dataset, you can train a reward model by opening the "Reward Model" modal on the dataset page.

<Frame><img src="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning/reward-model-button.png?fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=5df401591ca94b8a82cc98f9ef38236d" alt="" data-og-width="2996" width="2996" data-og-height="1708" height="1708" data-path="images/features/fine-tuning/reward-model-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning/reward-model-button.png?w=280&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=b582d9352f969f0a2d70859f1d39a882 280w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning/reward-model-button.png?w=560&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=c1c21844d4988fda5431b6a0364bc2bf 560w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning/reward-model-button.png?w=840&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=fe0031892c5a705edaa43b24f1ddcbc2 840w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning/reward-model-button.png?w=1100&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=e2372e9a01360dac1159c255249a3ee4 1100w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning/reward-model-button.png?w=1650&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=c353abf2ca9d19826ea361c47f70b56d 1650w, https://mintcdn.com/openpipe/yLyh_RHELnvU-7tP/images/features/fine-tuning/reward-model-button.png?w=2500&fit=max&auto=format&n=yLyh_RHELnvU-7tP&q=85&s=30a1c78402dff5630a2b792a108289cf 2500w" /></Frame>

Select a base model and optionally configure hyperparameters, then click "Start Training".

<Frame><img src="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-modal.png?fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=17b00298afe4336e393481477efe1e3c" alt="" data-og-width="2992" width="2992" data-og-height="1714" height="1714" data-path="images/features/fine-tuning/reward-model-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-modal.png?w=280&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=1af9da8bf54ba997ce0de60824124e2b 280w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-modal.png?w=560&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=19eeb5a7c267639d3725ade8749a3453 560w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-modal.png?w=840&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=24ec2518d6554d5a3b031322b7fc39f7 840w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-modal.png?w=1100&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=6de696338422d8b079ca9cd7a9e944aa 1100w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-modal.png?w=1650&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=fa1382c5faa256f28ef9050af30125ac 1650w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-modal.png?w=2500&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=8ba3466e6579df9a7fe5eaed3d378eb0 2500w" /></Frame>

Your reward model will be trained in the background. You can check the status of your model by navigating to the Fine Tunes page and selecting your model.

<Frame><img src="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-status.png?fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=6ac6aaab9e105de3826faeb8c7459046" alt="" data-og-width="2996" width="2996" data-og-height="1714" height="1714" data-path="images/features/fine-tuning/reward-model-status.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-status.png?w=280&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=d5d58e3cae0f4a101fdb99d037f9fe3f 280w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-status.png?w=560&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=bd1c2d8129a2d9326df1b9fdd5dfa0f9 560w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-status.png?w=840&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=cda99111db69a328dc6842522dc27e0f 840w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-status.png?w=1100&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=2c4b467e45da456ace948e6da07b4023 1100w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-status.png?w=1650&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=3cd3ccdf0ed0008b3b19f9e6d06e6351 1650w, https://mintcdn.com/openpipe/ODS5wc6pSZpoOUK8/images/features/fine-tuning/reward-model-status.png?w=2500&fit=max&auto=format&n=ODS5wc6pSZpoOUK8&q=85&s=9af5f315b87f5043ee419eb62405834e 2500w" /></Frame>

### Using a reward model

Like criteria, reward models can be used for best of N sampling and offline evaluation. Reward model slugs can be specified independently or in conjunction with criteria, as shown below:

```bash  theme={null}
curl --request POST \
--url https://app.openpipe.ai/api/v1/chat/completions \
--header "Authorization: Bearer $OPENPIPE_API_KEY" \
--header 'Content-Type: application/json' \
--header 'op-criteria: ["<reward-model-slug>"]' \
--data '{
"model": "openai:gpt-4o-mini",
"messages": [
    {
        "role": "user",
        "content": "Count to 10"
    },
],
"store": true,
"n": 5,
"metadata": {
    "prompt_id": "counting",
    "any_key": "any_value",
}
}'
```

For more details on how to use reward models and criteria, see the [criteria API docs](/features/criteria/api).

<Info>Want to learn more about reward models? Send questions to [support@openpipe.ai](mailto:support@openpipe.ai).</Info>
