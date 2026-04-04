# Source: https://docs.fireworks.ai/fine-tuning/deploying-loras.md

# Deploying Fine Tuned Models

> Deploy one or multiple LoRA models fine tuned on Fireworks

After fine-tuning your model on Fireworks, deploy it to make it available for inference.

<Note>
  You can also upload and deploy LoRA models fine-tuned outside of Fireworks. See [importing fine-tuned models](/models/uploading-custom-models#importing-fine-tuned-models) for details.
</Note>

## Single-LoRA deployment

Deploy your LoRA fine-tuned model with a single command that delivers performance matching the base model. This streamlined approach, called live merge, eliminates the previous two-step process and provides better performance compared to multi-LoRA deployments.

### Quick deployment

Deploy your LoRA fine-tuned model with one simple command:

```bash  theme={null}
firectl create deployment "accounts/fireworks/models/<MODEL_ID of lora model>"
```

<Check>
  Your deployment will be ready to use once it completes, with performance that matches the base model.
</Check>

### Deployment with the Build SDK

You can also deploy your LoRA fine-tuned model using the Build SDK:

```python  theme={null}
from fireworks import LLM

# Deploy a fine-tuned model with on-demand deployment (live merge)
fine_tuned_llm = LLM(
    model="accounts/your-account/models/your-fine-tuned-model-id",
    deployment_type="on-demand",
    id="my-fine-tuned-deployment"  # Simple string identifier
)

# Apply the deployment to ensure it's ready
fine_tuned_llm.apply()

# Use the deployed model
response = fine_tuned_llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello!"}]
)

# Track deployment in web dashboard
print(f"Track at: {fine_tuned_llm.deployment_url}")
```

<Note>
  The `id` parameter can be any simple string - it does not need to follow the format `"accounts/account_id/deployments/model_id"`.
</Note>

## Multi-LoRA deployment

If you have multiple fine-tuned versions of the same base model (e.g., you've fine-tuned the same model for different use cases, applications, or prototyping), you can share a single base model deployment across these LoRA models to achieve higher utilization.

<Warning>
  Multi-LoRA deployment comes with performance tradeoffs. We recommend using it only if you need to serve multiple fine-tunes of the same base model and are willing to trade performance for higher deployment utilization.
</Warning>

### Deploy with CLI

<Steps>
  <Step title="Create base model deployment">
    Deploy the base model with addons enabled:

    ```bash  theme={null}
    firectl create deployment "accounts/fireworks/models/<MODEL_ID of base model>" --enable-addons
    ```
  </Step>

  <Step title="Load LoRA addons">
    Once the deployment is ready, load your LoRA models onto the deployment:

    ```bash  theme={null}
    firectl load-lora <FINE_TUNED_MODEL_ID> --deployment <DEPLOYMENT_ID>
    ```

    You can load multiple LoRA models onto the same deployment by repeating this command with different model IDs.
  </Step>
</Steps>

### Deploy with the Build SDK

You can also use multi-LoRA deployment with the Build SDK:

```python  theme={null}
from fireworks import LLM

# Create a base model deployment with addons enabled
base_model = LLM(
    model="accounts/fireworks/models/base-model-id",
    deployment_type="on-demand",
    id="shared-base-deployment",  # Simple string identifier
    enable_addons=True
)
base_model.apply()

# Deploy multiple fine-tuned models using the same base deployment
fine_tuned_model_1 = LLM(
    model="accounts/your-account/models/fine-tuned-model-1",
    deployment_type="on-demand-lora",
    base_id=base_model.deployment_id
)

fine_tuned_model_2 = LLM(
    model="accounts/your-account/models/fine-tuned-model-2", 
    deployment_type="on-demand-lora",
    base_id=base_model.deployment_id
)

# Apply deployments
fine_tuned_model_1.apply()
fine_tuned_model_2.apply()

# Use the deployed models
response_1 = fine_tuned_model_1.chat.completions.create(
    messages=[{"role": "user", "content": "Hello from model 1!"}]
)

response_2 = fine_tuned_model_2.chat.completions.create(
    messages=[{"role": "user", "content": "Hello from model 2!"}]
)
```

<Note>
  When using `deployment_type="on-demand-lora"`, you need to provide the `base_id` parameter that references the deployment ID of your base model deployment.
</Note>

### When to use multi-LoRA deployment

Use multi-LoRA deployment when you:

* Need to serve multiple fine-tuned models based on the same base model
* Want to maximize deployment utilization
* Can accept some performance tradeoff compared to single-LoRA deployment
* Are managing multiple variants or experiments of the same model

## Serverless deployment

For quick experimentation and prototyping, you can deploy your fine-tuned model to shared serverless infrastructure without managing GPUs.

<Note>
  Not all base models support serverless addons. Check the [list of models that support serverless with LoRA](https://app.fireworks.ai/models?filter=LLM\&serverlessWithLoRA=true) to confirm your base model is supported.
</Note>

### Deploy to serverless

Load your fine-tuned model into a serverless deployment:

```bash  theme={null}
firectl load-lora <FINE_TUNED_MODEL_ID>
```

### Key considerations

* **No hosting costs**: Deploying to serverless is free—you only pay per-token usage costs
* **Rate limits**: Same rate limits apply as serverless base models
* **Performance**: Lower performance than on-demand deployments and the base model
* **Automatic unloading**: Unused addons may be automatically unloaded after a week
* **Limit**: Deploy up to 100 fine-tuned models to serverless

<Tip>
  For production workloads requiring consistent performance, use [on-demand deployments](#single-lora-deployment) instead.
</Tip>

## Next steps

<CardGroup cols={2}>
  <Card title="On-Demand Deployments" href="/guides/ondemand-deployments" icon="rocket">
    Learn about deployment configuration and optimization
  </Card>

  <Card title="Import Fine-Tuned Models" href="/models/uploading-custom-models#importing-fine-tuned-models" icon="upload">
    Upload LoRA models fine-tuned outside of Fireworks
  </Card>
</CardGroup>
