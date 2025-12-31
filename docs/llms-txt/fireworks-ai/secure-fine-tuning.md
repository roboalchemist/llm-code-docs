# Source: https://docs.fireworks.ai/fine-tuning/secure-fine-tuning.md

# Secure Training (BYOB)

> Fine-tune models while keeping sensitive data and components under your control

Fireworks enables secure model fine-tuning while maintaining customer control over sensitive components and data. Use your own cloud storage, keep reward functions proprietary, and ensure training data never persists on our platform beyond active workflows.

## Secure reinforcement fine-tuning (RFT)

Use reinforcement fine-tuning while keeping sensitive components and data under your control. Follow these steps to run secure RFT end to end using your own storage and reward pipeline.

<Steps>
  <Step title="Configure storage (BYOB)">
    Point Fireworks to your storage so you retain governance and apply your own compliance controls.

    * Datasets: [GCS Bucket Integration](#gcs-bucket-integration) (AWS S3 coming soon)
    * Models (optional): [External AWS S3 Bucket Integration](/models/uploading-custom-models#uploading-your-model)

    <Tip>
      Grant least-privilege IAM to only the bucket/path prefixes needed for training. Use server-side encryption and your KMS policies where required.
    </Tip>
  </Step>

  <Step title="Prepare your reward pipeline and rollouts">
    Keep your reward functions, rollout servers, and training metrics under your control. Generate rewards from your environment and write them to examples in your dataset (or export a dataset that contains per-example rewards).

    * Reward functions and reward models remain proprietary and never need to be shared
    * Rollouts and evaluation infrastructure run in your environment
    * Model checkpoints can be registered to your storage registry if desired
  </Step>

  <Step title="Create a dataset that includes rewards">
    Create or point a `Dataset` at your BYOB storage. Ensure each example contains the information required by your reward pipeline (for example, prompts, outputs/trajectories, and numeric rewards).

    <Info>
      You can reuse existing supervised data by attaching reward signals produced by your pipeline, or export a fresh dataset into your bucket for consumption by RFT.
    </Info>
  </Step>

  <Step title="Run reinforcement step from Python">
    Use the Python SDK to run reinforcement steps that read from your BYOB dataset and produce a new checkpoint.

    ```python  theme={null}
    # Assumes you have an authenticated `llm` client and a `dataset` that
    # references your BYOB bucket with per-example rewards.
    import time

    job = llm.reinforcement_step(
        dataset=dataset,                 # Dataset with rewards in your bucket
        output_model="my-improved-model-v1",  # New checkpoint name (must not exist)
        epochs=1,
        learning_rate=1e-5,
        accelerator_count=2,
        accelerator_type="NVIDIA_H100_80GB",
    )

    # Wait for completion
    while not job.is_completed:
        job.raise_if_bad_state()
        time.sleep(1)
        job = job.get()
        if job is None:
            raise RuntimeError("Job was deleted while waiting for completion")

    # The new model is now available at job.output_model
    ```

    See [`LLM.reinforcement_step()`](/tools-sdks/python-client/sdk-reference#reinforcement-step) and [`ReinforcementStep`](/tools-sdks/python-client/sdk-reference#reinforcementstep) for full parameters and return types.

    <Note>
      When continuing from a LoRA checkpoint, training parameters such as `lora_rank`, `learning_rate`, `max_context_length`, `epochs`, and `batch_size` must match the original LoRA training.
    </Note>
  </Step>

  <Step title="Verify outputs and enforce controls">
    * Validate the new checkpoint functions as expected in your environment
    * If exporting models to your storage, apply your registry policies and access reviews
    * Review audit logs and rotate any temporary credentials used for the run
  </Step>
</Steps>

<Warning>
  Do not store long-lived credentials in code. Use short-lived tokens, workload identity, or scoped service accounts when granting Fireworks access to your buckets.
</Warning>

<Check>
  You now have an end-to-end secure RFT workflow with BYOB datasets, proprietary reward pipelines, and isolated training jobs that generate new checkpoints.
</Check>

## GCS Bucket Integration

Use external Google Cloud Storage (GCS) buckets for fine-tuning while keeping your data private. Fireworks creates proxy datasets that reference your external buckets—data is only accessed during fine-tuning within a secure, isolated cluster.

<Info>
  Your data never leaves your GCS bucket except during fine-tuning, ensuring maximum privacy and security.
</Info>

### Required Permissions

You need to grant access to three service accounts:

#### Fireworks Control Plane

* **Account**: `fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com`
* **Required role**: Custom role with `storage.buckets.getIamPolicy` permission

<CodeGroup>
  ```bash Setup command theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:fireworks-control-plane@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=projects/<YOUR_PROJECT>/roles/<YOUR_CUSTOM_ROLE>
  ```
</CodeGroup>

This service account will be used to retrieve the IAM Policy set on the bucket, so that we are able to perform bucket ownership verifications and access verifications during dataset creation.

#### Inference Service Account

* **Account**: `inference@fw-ai-cp-prod.iam.gserviceaccount.com`
* **Required role**: Storage Object Viewer or Storage Object Admin

<CodeGroup>
  ```bash Storage Object Viewer theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:inference@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=roles/storage.objectViewer
  ```

  ```bash Storage Object Admin theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:inference@fw-ai-cp-prod.iam.gserviceaccount.com \
    --role=roles/storage.objectAdmin
  ```
</CodeGroup>

This service account will be used to access the files in the bucket.

#### Your Company's Fireworks Service Account

* **Account**: Your company's Fireworks account registration email
* **Required role**: Storage Object Viewer or Storage Object Admin

<CodeGroup>
  ```bash Storage Object Viewer theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
    --role=roles/storage.objectViewer
  ```

  ```bash Storage Object Admin theme={null}
  gcloud storage buckets add-iam-policy-binding <YOUR_BUCKET> \
    --member=serviceAccount:<YOUR_COMPANY_FW_ACCOUNT_EMAIL> \
    --role=roles/storage.objectAdmin
  ```
</CodeGroup>

This is used to validate that your account actually has access to the bucket that you are trying to reference the dataset from. The email associated with your account (not the email of the user, but the account itself, you can get it with `firectl get account`) must have at least read access to the bucket listed under the bucket access IAM policy.

### Usage Example

<Steps>
  <Step title="Create a Proxy Dataset">
    Create a dataset that references your external GCS bucket:

    ```bash  theme={null}
    firectl create dataset {DATASET_NAME} --external-url gs://bucket-name/object-name
    ```

    <Tip>
      Ensure your gsutil path points directly to the JSONL file. If the file is in a folder, make sure the folder contains only the intended file.
    </Tip>
  </Step>

  <Step title="Start Fine-tuning">
    Use the proxy dataset to create a fine-tuning job:

    ```bash  theme={null}
    firectl create sftj \
      --dataset "accounts/{ACCOUNT}/datasets/{DATASET_NAME}" \
      --base-model "accounts/fireworks/models/{MODEL}" \
      --output-model {TRAINED_MODEL_NAME}
    ```

    <Check>
      For additional options, run: `firectl create sftj -h`
    </Check>
  </Step>
</Steps>

### Key Benefits

<CardGroup cols={3}>
  <Card title="Data Privacy" icon="shield">
    Your data never leaves your GCS bucket except during fine-tuning
  </Card>

  <Card title="Security" icon="lock">
    Access is limited to isolated fine-tuning clusters
  </Card>

  <Card title="Simplicity" icon="circle">
    Reference external data without copying or moving files
  </Card>
</CardGroup>

## Related Resources

<CardGroup cols={2}>
  <Card title="Data Security Overview" href="/guides/security_compliance/data_security" icon="shield-check">
    Learn about our comprehensive security measures
  </Card>

  <Card title="Reinforcement Fine Tuning" href="/fine-tuning/reinforcement-fine-tuning-models" icon="brain">
    Full guide to reinforcement fine-tuning
  </Card>
</CardGroup>
