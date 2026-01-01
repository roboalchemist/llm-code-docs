# Source: https://docs.together.ai/docs/lora-training-and-inference.md

# LoRA Fine-Tuning and Inference

> Fine-tune and run inference for a model with LoRA adapters

## Overview

LoRA (Low-Rank Adaptation) enables efficient fine-tuning of large language models by training only a small set of additional parameters while keeping the original model weights frozen. This approach delivers several key advantages:

* **Reduced training costs**: Trains fewer parameters than full fine-tuning, using less GPU memory
* **Faster deployment**: Produces compact adapter files that can be quickly shared and deployed

Together AI handles the entire LoRA workflow: fine-tune your model and start running inference immediately.

> **Important**: Adapters trained before December 17, 2024, require migration to work with the current serverless infrastructure. As a temporary workaround, you can download and re-upload these adapters following the instructions in our [adapter upload guide](/docs/adapter-upload).

## Quick start

This guide demonstrates how to fine-tune a model using LoRA and deploy it for serverless inference. For comprehensive fine-tuning options and best practices, refer to the [Fine-Tuning Guide](/docs/fine-tuning-quickstart).

### Prerequisites

* Together AI API key
* Training data in the JSONL format
* [Compatible base model](/docs/adapter-upload#supported-base-models) selection

### Step 1: Upload Training Data

First, upload your training dataset to Together AI:

<CodeGroup>
  ```curl CLI theme={null}
  together files upload "your-datafile.jsonl"
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  files_response = client.files.upload(file="your-datafile.jsonl")

  print(files_response.model_dump())
  ```
</CodeGroup>

### Step 2: Create Fine-tuning Job

Launch a LoRA fine-tuning job using the uploaded file ID:

<CodeGroup>
  ```curl CLI theme={null}
  together fine-tuning create \
    --training-file "file-629e58b4-ff73-438c-b2cc-f69542b27980" \
    --model "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference" \
    --lora
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

  fine_tuning_response = client.fine_tuning.create(
      training_file=files_response.id,
      model="meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
      lora=True,
  )

  print(fine_tuning_response.model_dump())
  ```
</CodeGroup>

> **Note**: If you plan to use a validation set, make sure to set the `--validation-file` and `--n-evals` (the number of evaluations over the entire job) parameters. `--n-evals` needs to be set as a number above 0 in order for your validation set to be used.

Once you submit the fine-tuning job you should be able to see the model `output_name` and `job_id` in the response:

<CodeGroup>
  ```json Json theme={null}
  {
    "id": "ft-44129430-ac08-4136-9774-aed81e0164a4",
    "training_file": "file-629e58b4-ff73-438c-b2cc-f69542b27980",
    "validation_file": "",
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    "output_name": "zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
    ...
  }
  ```
</CodeGroup>

### Step 3: Getting the output model

Once you submit the fine-tuning job you should be able to see the model `output_name` and `job_id` in the response:

<CodeGroup>
  ```json Json theme={null}
  {
    "id": "ft-44129430-ac08-4136-9774-aed81e0164a4",
    "training_file": "file-629e58b4-ff73-438c-b2cc-f69542b27980",
    "validation_file": "",
    "model": "meta-llama/Meta-Llama-3.1-8B-Instruct-Reference",
    "output_name": "zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
    ...
  }
  ```
</CodeGroup>

You can also see the status of the job and get the model name if you navigate to your fine-tuned model in the 'Model' or 'Jobs' tab in the Together dashboard.

<Frame>
    <img src="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7e332c714e184d6d4d9554b761a6e350" alt="" data-og-width="1920" width="1920" data-og-height="1080" height="1080" data-path="images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=280&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=cc3d85962dac161d2842617ce37f0b45 280w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=560&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=2081ba31e7cb4fa4d9cacb96d4a08976 560w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=840&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=db9915d04970709baaa0ee97c53d3235 840w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=1100&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=a051712d1d8408ba70701d81dc41aef3 1100w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=1650&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=6677dee05d46a3641aa28021bb3ddcf5 1650w, https://mintcdn.com/togetherai-52386018/msWWavplJrEZR36N/images/docs/a9c3fb15e77e1df27b72195dc80dea4d0748fcf5f958a15d5884bdb982d3d9b9-image.png?w=2500&fit=max&auto=format&n=msWWavplJrEZR36N&q=85&s=7a83d855bf5a9d4dd8f4fc26497cdb19 2500w" />
</Frame>

### Step 4: Running LoRA inference

Once the fine-tuning job is completed, your model is immediately available for inference.

<CodeGroup>
  ```curl cURL theme={null}
  MODEL_NAME_FOR_INFERENCE="zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a"

  curl -X POST https://api.together.xyz/v1/chat/completions \
    -H "Authorization: Bearer $TOGETHER_API_KEY" \
    -H "Content-Type: application/json" \
    --data @- <<EOF
  {
    "model": "$MODEL_NAME_FOR_INFERENCE",
    "messages": [
      { "role": "user", "content": "debate the pros and cons of AI" }
    ],
    "max_tokens": 128
  }
  EOF
  ```

  ```python Python theme={null}
  import os
  from together import Together

  client = Together(api_key=TOGETHERAI_API_KEY)

  user_prompt = "debate the pros and cons of AI"

  response = client.chat.completions.create(
      model=fine_tuning_response.output_name,
      messages=[
          {
              "role": "user",
              "content": user_prompt,
          }
      ],
      max_tokens=512,
      temperature=0.7,
  )

  print(response.choices[0].message.content)
  ```

  ```typescript TypeScript theme={null}
  import Together from 'together-ai';
  const together = new Together();

  const stream = await together.chat.completions.create({
    model: 'zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a',
    messages: [
      { role: 'user', content: '"ebate the pros and cons of AI' },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    // use process.stdout.write instead of console.log to avoid newlines
    process.stdout.write(chunk.choices[0]?.delta?.content || '');
  }
  ```
</CodeGroup>

Expected Response:

<CodeGroup>
  ```json JSON theme={null}
  {
    "id": "8f2cb236c80ea20e-YYZ",
    "object": "text.completion",
    "created": 1734331375,
    "model": "zainhas/Meta-Llama-3.1-8B-Instruct-Reference-my-demo-finetune-4224205a",
    "prompt": [],
    "choices": [
      {
        "text": "Here's a debate on the pros and cons of AI:\n\n**Moderator:** Welcome to today's debate on the pros and cons of AI. We have two debaters, Alex and Ben, who will present their arguments on the topic. Alex will argue in favor of AI, while Ben will argue against it. Let's begin with opening statements.\n\n**Alex (In Favor of AI):** Thank you, Moderator. AI has revolutionized the way we live and work. It has improved efficiency, productivity, and accuracy in various industries, such as healthcare, finance, and transportation. AI-powered systems can analyze vast amounts of data, identify",
        "finish_reason": "length",
        "seed": 5626645655383684000,
        "logprobs": null,
        "index": 0
      }
    ],
    "usage": {
      "prompt_tokens": 18,
      "completion_tokens": 128,
      "total_tokens": 146,
      "cache_hit_rate": 0
    }
  }
  ```
</CodeGroup>

## Performance Characteristics

### Latency Expectations

* **Cold start:** Initial requests may experience 5-10 seconds of latency
* **Warm requests:** Subsequent queries typically respond under 1 second
* **Optimization tip:** Send a warmup query after deployment to minimize cold starts for production traffic

## Best Practices

1. **Data Preparation**: Ensure your training data follows the correct JSONL format for your chosen model
2. **Validation Sets**: Always include validation data to monitor training quality
3. **Model Naming**: Use descriptive names for easy identification in production
4. **Warmup Queries**: Run test queries immediately after deployment to optimize response times
5. **Monitoring**: Track inference metrics through the Together dashboard

## Frequently Asked Questions

### Which base models support LoRA fine-tuning?

Together AI supports LoRA fine-tuning on a curated selection of high-performance base models. See the [complete list](/docs/adapter-upload#supported-base-models) for current options.

### What are typical inference latencies?

After an initial cold start period (5-10 seconds for the first request), subsequent requests typically achieve sub-second response times. Latency remains consistently low for warm models.

### Can I use streaming responses?

Yes, streaming is fully supported. Add `"stream": true` to your request parameters to receive incremental responses.

### How do I migrate pre-December 2024 adapters?

Download your existing adapter files and re-upload them using our [adapter upload workflow](/docs/adapter-upload). We're working on automated migration for legacy adapters.

### What's the difference between LoRA and full fine-tuning?

LoRA trains only a small set of additional parameters (typically 0.1-1% of model size), resulting in faster training, lower costs, and smaller output files, while full fine-tuning updates all model parameters for maximum customization at higher computational cost.

## Next Steps

* Explore [advanced fine-tuning parameters](/docs/fine-tuning-quickstart) for optimizing model performance
* Learn about [uploading custom adapters](/docs/adapter-upload) trained outside Together AI


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt