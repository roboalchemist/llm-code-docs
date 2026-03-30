# Retrieve a job
curl https://api.mistral.ai/v1/fine_tuning/jobs/<jobid> \
--header "Authorization: Bearer $MISTRAL_API_KEY" \
--header 'Content-Type: application/json'
```
  </TabItem>
</Tabs>

<details>
<summary><b>Example output when we run 100 steps:</b></summary>

```
{
    "id": "2813b7e6-c511-43ac-a16a-1a54a5b884b2",
    "hyperparameters": {
        "training_steps": 100,
        "learning_rate": 0.0001
    },
    "fine_tuned_model": "ft:open-mistral-7b:57d37e6c:20240531:2813b7e6",
    "model": "open-mistral-7b",
    "status": "SUCCESS",
    "job_type": "FT",
    "created_at": 1717172592,
    "modified_at": 1717173491,
    "training_files": [
        "66f96d02-8b51-4c76-a5ac-a78e28b2584f"
    ],
    "validation_files": [
        "84482011-dfe9-4245-9103-d28b6aef30d4"
    ],
    "object": "job",
    "integrations": [],
    "events": [
        {
            "name": "status-updated",
            "data": {
                "status": "SUCCESS"
            },
            "created_at": 1717173491
        },
        {
            "name": "status-updated",
            "data": {
                "status": "RUNNING"
            },
            "created_at": 1717172594
        },
        {
            "name": "status-updated",
            "data": {
                "status": "QUEUED"
            },
            "created_at": 1717172592
        }
    ],
    "checkpoints": [
        {
            "metrics": {
                "train_loss": 0.816135,
                "valid_loss": 0.819697,
                "valid_mean_token_accuracy": 1.765035
            },
            "step_number": 100,
            "created_at": 1717173470
        },
        {
            "metrics": {
                "train_loss": 0.84643,
                "valid_loss": 0.819768,
                "valid_mean_token_accuracy": 1.765122
            },
            "step_number": 90,
            "created_at": 1717173388
        },
        {
            "metrics": {
                "train_loss": 0.816602,
                "valid_loss": 0.820234,
                "valid_mean_token_accuracy": 1.765692
            },
            "step_number": 80,
            "created_at": 1717173303
        },
        {
            "metrics": {
                "train_loss": 0.775537,
                "valid_loss": 0.821105,
                "valid_mean_token_accuracy": 1.766759
            },
            "step_number": 70,
            "created_at": 1717173217
        },
        {
            "metrics": {
                "train_loss": 0.840297,
                "valid_loss": 0.822249,
                "valid_mean_token_accuracy": 1.76816
            },
            "step_number": 60,
            "created_at": 1717173131
        },
        {
            "metrics": {
                "train_loss": 0.823884,
                "valid_loss": 0.824598,
                "valid_mean_token_accuracy": 1.771041
            },
            "step_number": 50,
            "created_at": 1717173045
        },
        {
            "metrics": {
                "train_loss": 0.786473,
                "valid_loss": 0.827982,
                "valid_mean_token_accuracy": 1.775201
            },
            "step_number": 40,
            "created_at": 1717172960
        },
        {
            "metrics": {
                "train_loss": 0.8704,
                "valid_loss": 0.835169,
                "valid_mean_token_accuracy": 1.784066
            },
            "step_number": 30,
            "created_at": 1717172874
        },
        {
            "metrics": {
                "train_loss": 0.880803,
                "valid_loss": 0.852521,
                "valid_mean_token_accuracy": 1.805653
            },
            "step_number": 20,
            "created_at": 1717172788
        },
        {
            "metrics": {
                "train_loss": 0.803578,
                "valid_loss": 0.914257,
                "valid_mean_token_accuracy": 1.884598
            },
            "step_number": 10,
            "created_at": 1717172702
        }
    ]
}
```
</details>

### Use a fine-tuned model 
When a fine-tuned job is finished, you will be able to see the fine-tuned model name via `retrieved_jobs.fine_tuned_model`. Then you can use our `chat` endpoint to chat with the fine-tuned model: 


<Tabs>
  <TabItem value="python" label="python" default>

```python
chat_response = client.chat.complete(
    model = retrieved_jobs.fine_tuned_model,
    messages = [{"role":'user', "content":'What is the best French cheese?'}]
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const chatResponse = await client.chat({
  model: retrievedJob.fine_tuned_model,
  messages: [{role: 'user', content: 'What is the best French cheese?'}],
});
```
  </TabItem>
  
  <TabItem value="curl" label="curl">

```bash
curl "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "ft:open-mistral-7b:daf5e488:20240430:c1bed559",
    "messages": [{"role": "user", "content": "Who is the most renowned French painter?"}]
  }'

```
  </TabItem>

</Tabs>

### Integration with Weights and Biases
We can also offer support for integration with Weights & Biases (W&B) to monitor and track various metrics and statistics associated with our fine-tuning jobs. To enable integration with W&B, you will need to create an account with W&B and add your W&B information in the “integrations” section in the job creation request: 

```python
client.fine_tuning.jobs.create(
    model="open-mistral-7b", 
    training_files=[{"file_id": ultrachat_chunk_train.id, "weight": 1}],
    validation_files=[ultrachat_chunk_eval.id],
    hyperparameters={"training_steps": 10, "learning_rate": 0.0001},
    integrations=[
        {
            "project": "<value>",
            "api_key": "<value>",
        }
    ]
)
```

Here are the screenshots of the W&B dashboard showing the information of our fine-tuning job. 

<img src="/img/guides/ft2.png" alt="drawing" width="100%"/>

## End-to-end example with open-source `mistral-finetune`
We have also open sourced fine-tuning codebase mistral-finetune allowing you to fine-tune Mistral’s open-weights models (Mistral 7B, Mixtral 8x7B, Mixtral 8x22B). 

To see an end-to-end example of how to install mistral-finetune, prepare and validate your dataset, define your training configuration, fine-tune using Mistral-LoRA, and run inference, please refer to the README file provided in the Mistral-finetune repo: https://github.com/mistralai/mistral-finetune/tree/main or follow this example: 


<a target="_blank" href="https://colab.research.google.com/github/mistralai/mistral-finetune/blob/main/tutorials/mistral_finetune_7b.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>


[get data from hugging face]
Source: https://docs.mistral.ai/docs/guides/finetuning_sections/_04_faq

## FAQ

### How to validate data format? 

- Mistral API: We currently validate each file when you upload the dataset. 

- `mistral-finetune`: You can run the [data validation script](https://github.com/mistralai/mistral-finetune/blob/main/utils/validate_data.py) to validate the data and run the [reformat data script](https://github.com/mistralai/mistral-finetune/blob/main/utils/reformat_data.py) to reformat the data to the right format: 

    ```bash
    # download the reformat script
    wget https://raw.githubusercontent.com/mistralai/mistral-finetune/main/utils/reformat_data.py
    # download the validation script
    wget https://raw.githubusercontent.com/mistralai/mistral-finetune/main/utils/validate_data.py
    # reformat data
    python reformat_data.py data.jsonl
    # validate data
    python validate_data.py data.jsonl
    ```

    However, it's important to note that these scripts might not detect all problematic cases. Therefore, you may need to manually validate and correct any unique edge cases in your data.

### What's the size limit of the training data? 

While the size limit for an individual training data file is 512MB, there's no limitation on the number of files you can upload. You can upload multiple files and reference them when creating the job.

### What's the size limit of the validation data? 

The size limit for the validation data is 1MB. As a rule of thumb: 

`validation_set_max_size = min(1MB, 5% of training data)`

### What happens if I try to create a job that already exists?

At job creation, you will receive a `409 Conflict` error in case a similar job is already running / validated / queued. This mechanism helps avoid inadvertently creating duplicate jobs, saving resources and preventing redundancy.

### What if I upload an already existing file?

If a file is uploaded and matches an existing file in both content and name, the pre-existing file is returned instead of creating a new one.

### How many epochs are in the training process? 

A general rule of thumb is: Num epochs = max_steps / file_of_training_jsonls_in_MB. For instance, if your training file is 100MB and you set max_steps=1000, the training process will roughly perform 10 epochs.

### Where can I find information on cost/ ETA / number of tokens / number of passes over each files?

Mistral API: When you create a fine-tuning job, you should automatically see these info with the default `auto_start=False` argument.

Note that the `dry_run=True` argument will be removed in September.

`mistral-finetune`: You can use the following script to find out: https://github.com/mistralai/mistral-finetune/blob/main/utils/validate_data.py. This script accepts a .yaml training file as input and returns the number of tokens the model is being trained on.

### How to estimate cost of a fine-tuning job?
For Mistral API, you can use the `auto_start=False` argument as mentioned in the previous question. 

### What is the recommended learning rate? 

For LoRA fine-tuning, we recommend 1e-4 (default) or 1e-5. 

Note that the learning rate we define is the peak learning rate, instead of a flat learning rate. The learning rate follows a linear warmup and cosine decay schedule. During the warmup phase, the learning rate is linearly increased from a small initial value to a larger value over a certain number of training steps. After the warmup phase, the learning rate is decayed using a cosine function.

### Is the fine-tuning API compatible with OpenAI data format?

Yes, we support OpenAI format.

### What if my file size is larger than 500MB and I get the error message `413 Request Entity Too Large`? 

You can split your data file into chunks. Here is an example:

<details>
```py

from datasets import load_dataset