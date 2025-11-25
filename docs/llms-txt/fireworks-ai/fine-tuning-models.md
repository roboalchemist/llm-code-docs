# Source: https://docs.fireworks.ai/fine-tuning/fine-tuning-models.md

# Supervised Fine Tuning - Text

This guide will focus on using supervised fine-tuning to fine-tune and deploy a model with on-demand and serverless hosting.

## Fine-tuning a model using SFT

<Steps>
  <Step title="Confirm model support for fine-tuning">
    You can confirm that a base model is available to fine-tune by looking for the `Tunnable` tag in the model library or by using:

    ```bash  theme={null}
    firectl get model -a fireworks <MODEL-ID>
    ```

    And looking for `Tunable: true`.

    <Note>
      Some base models cannot be tuned on Fireworks (`Tunable: false`) but still list support for LoRA (`Supports Lora: true`). This means that users can tune a LoRA for this base model on a separate platform and upload it to Fireworks for inference. Consult [importing fine-tuned models](/models/uploading-custom-models#importing-fine-tuned-models) for more information.
    </Note>
  </Step>

  <Step title="Prepare a dataset">
    Datasets must be in JSONL format, where each line represents a complete JSON-formatted training example. Make sure your data conforms to the following restrictions:

    * **Minimum examples:** 3
    * **Maximum examples:** 3 million per dataset
    * **File format:** `.jsonl`
    * **Message schema:** Each training sample must include a messages array, where each message is an object with two fields:
      * `role`: one of `system`, `user`, or `assistant`. A message with the `system` role is optional, but if specified, it must be the first message of the conversation
      * `content`: a string representing the message content
      * `weight`: optional key with value to be configured in either 0 or 1. message will be skipped if value is set to 0
    * **Sample weight:** Optional key `weight` at the root of the JSON object. It can be any floating point number (positive, negative, or 0) and is used as a loss multiplier for tokens in that sample. If used, this field must be present in all samples in the dataset.

    Here is an example conversation dataset:

    ```json  theme={null}
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "Paris."}
      ]
    }
    {
      "messages": [
        {"role": "user", "content": "What is 1+1?"},
        {"role": "assistant", "content": "2", "weight": 0},
        {"role": "user", "content": "Now what is 2+2?"},
        {"role": "assistant", "content": "4"}
      ]
    }
    ```

    Here is an example conversation dataset with sample weights:

    ```json  theme={null}
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "Paris."}
      ],
      "weight": 0.5
    }
    {
      "messages": [
        {"role": "user", "content": "What is 1+1?"},
        {"role": "assistant", "content": "2", "weight": 0},
        {"role": "user", "content": "Now what is 2+2?"},
        {"role": "assistant", "content": "4"}
      ],
      "weight": 1.0
    }
    ```

    We also support function calling dataset with a list of tools. An example would look like:

    ```json  theme={null}
    {
      "tools": [
        {
          "type": "function",
          "function": {
            "name": "get_car_specs",
            "description": "Fetches detailed specifications for a car based on the given trim ID.",
            "parameters": {
              "trimid": {
                "description": "The trim ID of the car for which to retrieve specifications.",
                "type": "int",
                "default": ""
              }
            }
          }
        },
    ],
      "messages": [
        {
          "role": "user",
          "content": "What is the specs of the car with trim 121?"
        },
        {
          "role": "assistant",
          "tool_calls": [
            {
              "type": "function",
              "function": {
                "name": "get_car_specs",
                "arguments": "{\"trimid\": 121}"
              }
            }
          ]
        }
      ]
    }
    ```

    For the subset of models that supports thinking (e.g. DeepSeek R1, GPT OSS models and Qwen3 thinking models), we also support fine tuning with thinking traces. If you wish to fine tune with thinking traces, the dataset could also include thinking traces for assistant turns. Though optional, ideally each assistant turn includes a thinking trace. For example:

    ```json  theme={null}
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is the capital of France?"},
        {"role": "assistant", "content": "Paris.", "reasoning_content": "The user is asking about the capital city of France, it should be Paris."}
      ]
    }
    {
      "messages": [
        {"role": "user", "content": "What is 1+1?"},
        {"role": "assistant", "content": "2", "weight": 0, "reasoning_content": "The user is asking about the result of 1+1, the answer is 2."},
        {"role": "user", "content": "Now what is 2+2?"},
        {"role": "assistant", "content": "4", "reasoning_content": "The user is asking about the result of 2+2, the answer should be 4."}
      ]
    }
    ```

    Note that when fine tuning with intermediate thinking traces, the number of total tuned tokens could exceed the number of total tokens in the dataset. This is because we perform preprocessing and expand the dataset to ensure train-inference consistency.
  </Step>

  <Step title="Create and upload a dataset">
    There are a couple ways to upload the dataset to Fireworks platform for fine tuning: `firectl`, `Restful API` , `builder SDK` or `UI`.

    <Tabs>
      <Tab title="UI">
        * You can simply navigate to the dataset tab, click `Create Dataset` and follow the wizard.

          <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=33255bb2d9afefc697230a6f4e723577" alt="Dataset Pn" data-og-width="2972" width="2972" data-og-height="2060" height="2060" data-path="images/fine-tuning/dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=e1f7631eedf19be2ffe910e931734378 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5148e67713f7a207c47a73da1fa56658 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=dde9343748034e1d13ae4fbc1ad4aecf 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a4a99ce824157064f5cbbdfdf0953c0d 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=699fd69866de9383a06dc08a5139cb69 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=b55ed77bc807c1ebf00223fff2997342 2500w" />
      </Tab>

      <Tab title="firectl">
        ```bash  theme={null}
        firectl create dataset <DATASET_ID> /path/to/jsonl/file
        ```
      </Tab>

      <Tab title="Restful API">
        You need to make two separate HTTP requests. One for creating the dataset entry and one for uploading the dataset. Full reference here: [Create dataset](/api-reference/create-dataset). Note that the `exampleCount` parameter needs to be provided by the client.

        ```jsx  theme={null}
        // Create Dataset Entry
        const createDatasetPayload = {
          datasetId: "trader-poe-sample-data",
          dataset: { userUploaded: {} }
          // Additional params such as exampleCount
        };
        const urlCreateDataset = `${BASE_URL}/datasets`;
        const response = await fetch(urlCreateDataset, {
          method: "POST",
          headers: HEADERS_WITH_CONTENT_TYPE,
          body: JSON.stringify(createDatasetPayload)
        });
        ```

        ```jsx  theme={null}
        // Upload JSONL file
        const urlUpload = `${BASE_URL}/datasets/${DATASET_ID}:upload`;
        const files = new FormData();
        files.append("file", localFileInput.files[0]);

        const uploadResponse = await fetch(urlUpload, {
          method: "POST",
          headers: HEADERS,
          body: files
        });
        ```
      </Tab>
    </Tabs>

    While all of the above approaches should work, `UI` is more suitable for smaller datasets `< 500MB` while `firectl` might work better for bigger datasets.

    Ensure the dataset ID conforms to the [resource id restrictions](/getting-started/concepts#resource-names-and-ids).
  </Step>

  <Step title="Launch a fine-tuning job">
    There are also a couple ways to launch the fine-tuning jobs. We highly recommend creating supervised fine tuning jobs via `UI` .

    <Tabs>
      <Tab title="UI">
        Simply navigate to the `Fine-Tuning` tab, click `Fine-Tune a Model` and follow the wizard from there. You can even pick a LoRA model to start the fine-tuning for continued training.

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4c2ad94681a8327cb870c5f92c1cf5d7" alt="Fine Tuning Pn" data-og-width="2966" width="2966" data-og-height="2052" height="2052" data-path="images/fine-tuning/fine-tuning.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=67e542c9ea90128f6cd1b53ff8c92aed 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=deef7708b9713cce4afd4cf7744df559 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=f99d019df0142144114475ce9e7c7729 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=bca80f9c479e23ed45e8c51374ac71bb 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5835f9d2a269326985b00cb9b15f12e6 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=040f237a22bd3109c36acaad9c15907f 2500w" />

                <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=102b729d2d50fd9466d3b36606992443" alt="Create Sftj Pn" data-og-width="2970" width="2970" data-og-height="2048" height="2048" data-path="images/fine-tuning/create-sftj.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=eabe188f029777c24abd5c3d9787c1da 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5fd4390ff45d3412c1b0cc687392d054 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=add5687145f89362ce42a171136b2639 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=d074f5e4c69f9fed3644d9cdd637570d 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=d4830964471e8e7450fcbfad39a54269 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/create-sftj.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=2635d10a906f4c5b75899f41e8f1bf6c 2500w" />
      </Tab>

      <Tab title="firectl">
        Ensure the fine tuned model ID conforms to the [resource id restrictions](/getting-started/concepts#resource-names-and-ids). This will return a fine-tuning job ID. For a full explanation of the settings available to control the fine-tuning process, including learning rate and epochs, consult [additional SFT job settings](#additional-sft-job-settings).

        ```bash  theme={null}
        firectl create sftj --base-model <MODEL_ID> --dataset <DATASET_ID> --output-model <FINE_TUNED_MODEL_ID>
        ```

        <Tip>
          Similar to UI, instead of tuning a base model, you can also start tuning from a previous LoRA model using

          ```bash  theme={null}
          firectl create sftj --warm-start-from <FINE_TUNED_MODEL_ID> --dataset <DATASET_ID> --output-model <FINE_TUNED_MODEL_ID>
          ```

          Notice that we use `--warm-start-from` instead of `--base-model` when creating this job.
        </Tip>
      </Tab>
    </Tabs>

    With `UI`, once the job is created, it will show in the list of jobs. Clicking to view the job details to monitor the job progress.

        <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/sftj-details.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=acfecc07e34d6992ba64f171469c62db" alt="Sftj Details Pn" data-og-width="2960" width="2960" data-og-height="1938" height="1938" data-path="images/fine-tuning/sftj-details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/sftj-details.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=2fa38f207d49f54a0cecd6b5e2ab1a9c 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/sftj-details.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=f780b120ceb0e9ffe136f2874c9e2e9a 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/sftj-details.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=916b78d429f9fe7d7a819e576fa0cf42 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/sftj-details.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=deb16417332fa2237a7c3ba7c0c8b0a9 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/sftj-details.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=0a0155fbf12d2a2b7265d7a49c93925c 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/sftj-details.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=7e7aceaff30008e0d3fe2792db8260ed 2500w" />

    With `firectl`, you can monitor the progress of the tuning job by running

    ```bash  theme={null}
    firectl get sftj <DATASET_ID>
    ```

    Once the job successfully completes, you will see the new LoRA model in your model list

    ```bash  theme={null}
    firectl list models
    ```
  </Step>
</Steps>

## Deploying a fine-tuned model

After fine-tuning completes, deploy your model to make it available for inference:

```bash  theme={null}
firectl create deployment <FINE_TUNED_MODEL_ID>
```

This creates a dedicated deployment with performance matching the base model.

<Tip>
  For more details on deploying fine-tuned models, including multi-LoRA and serverless deployments, see the [Deploying Fine Tuned Models guide](/fine-tuning/deploying-loras).
</Tip>

## Additional SFT job settings

Additional tuning settings are available when starting a fine-tuning job. All of the below settings are optional and will have reasonable defaults if not specified. For settings that affect tuning quality like `epochs` and `learning rate`, we recommend using default settings and only changing hyperparameters if results are not as desired.

<AccordionGroup>
  <Accordion title="Evaluation">
    By default, the fine-tuning job will run evaluation by running the fine-tuned model against an evaluation set that's created by automatically carving out a portion of your training set. You have the option to explicitly specify a separate evaluation dataset to use instead of carving out training data.

    `evaluation_dataset`: The ID of a separate dataset to use for evaluation. Must be pre-uploaded via firectl

    ```shell  theme={null}
    firectl create sftj \
      --evaluation-dataset my-eval-set \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Max Context Length">
    Depending on the size of the model, the default context size will be different. For most models, the default context size is >= 32768. Training examples will be cut-off at 32768 tokens. Usually you do not need to set the max context length unless out of memory error is encountered with higher lora rank and large max context length.

    ```shell  theme={null}
    firectl create sftj \
      --max-context-length 65536 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Batch Size">
    Batch size is the number of tokens packed into one forward step during training. One batch could consist of multiple training samples. We do sequence packing on the training samples, and batch size controls how many total tokens will be packed into each batch.

    ```shell  theme={null}
    firectl create sftj \
      --batch-size 65536 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Epochs">
    Epochs are the number of passes over the training data. Our default value is 1. If the model does not follow the training data as much as expected, increase the number of epochs by 1 or 2. Non-integer values are supported.

    **Note: we set a max value of 3 million dataset examples × epochs**

    ```shell  theme={null}
    firectl create sftj \
      --epochs 2.0 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Learning rate">
    Learning rate controls how fast the model updates from data. We generally do not recommend changing learning rate. The default value is automatically based on your selected model.

    ```shell  theme={null}
    firectl create sftj \
      --learning-rate 0.0001 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Learning rate warmup steps">
    Learning rate warmup steps controls the number of training steps during which the learning rate will be linearly ramped up to the set learning rate.

    ```shell  theme={null}
    firectl create sftj \
      --learning-rate 0.0001 \
      --learning-rate-warmup-steps 200 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Gradient accumlation steps">
    Gradient accumulation steps controls the number of forward steps and backward steps to take (gradients are accumulated) before optimizer.step() is taken. Gradient accumulation steps > 1 increases effective batch size.

    ```shell  theme={null}
    firectl create sftj \
      --gradient-accumulation-steps 4 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="LoRA Rank">
    LoRA rank refers to the number of parameters that will be tuned in your LoRA add-on. Higher LoRA rank increases the amount of information that can be captured while tuning. LoRA rank must be a power of 2 up to 64. Our default value is 8.

    ```shell  theme={null}
    firectl create sftj \
      --lora-rank 16 \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Training progress and monitoring">
    The fine-tuning service integrates with Weights & Biases to provide observability into the tuning process. To use this feature, you must have a Weights & Biases account and have provisioned an API key.

    ```shell  theme={null}
    firectl create sftj \
      --wandb-entity my-org \
      --wandb-api-key xxx \
      --wandb-project "My Project" \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>

  <Accordion title="Model ID">
    By default, the fine-tuning job will generate a random unique ID for the model. This ID is used to refer to the model at inference time. You can optionally specify a custom ID, within [ID constraints](/getting-started/concepts#resource-names-and-ids).

    ```shell  theme={null}
    firectl create sftj \
      --output-model my-model \
      --base-model MY_BASE_MODEL \
      --dataset cancerset
    ```
  </Accordion>

  <Accordion title="Job ID">
    By default, the fine-tuning job will generate a random unique ID for the fine-tuning job. You can optionally choose a custom ID.

    ```shell  theme={null}
    firectl create sftj \
      --job-id my-fine-tuning-job \
      --base-model MY_BASE_MODEL \
      --dataset cancerset \
      --output-model my-tuned-model
    ```
  </Accordion>
</AccordionGroup>

## Appendix

`Python builder SDK` [references](/tools-sdks/python-client/sdk-introduction)

`Restful API`[ references](/api-reference/introduction)

`firectl` [references](/tools-sdks/firectl/firectl)
