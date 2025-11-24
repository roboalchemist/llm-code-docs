# Source: https://docs.fireworks.ai/fine-tuning/cli-reference.md

# Training Guide: CLI

> Launch RFT jobs using the eval-protocol CLI

The Eval Protocol CLI provides the fastest, most reproducible way to launch RFT jobs. This page covers everything you need to know about using `eval-protocol create rft`.

<Note>
  Before launching, review [Training Prerequisites & Validation](/fine-tuning/training-prerequisites) for requirements, validation checks, and common errors.
</Note>

<Tip>
  Already familiar with [firectl](/fine-tuning/cli-reference#using-firectl-cli-alternative)? Use it as an alternative to eval-protocol.
</Tip>

## Installation and setup

The following guide will help you:

* Upload your evaluator to Fireworks. If you don't have one yet, see [Concepts > Evaluators](/fine-tuning/evaluators)
* Upload your dataset to Fireworks
* Create and launch the RFT job

<Steps>
  <Step title="Install Eval Protocol CLI">
    ```bash  theme={null}
    pip install eval-protocol
    ```

    Verify installation:

    ```bash  theme={null}
    eval-protocol --version
    ```
  </Step>

  <Step title="Set up authentication">
    Configure your Fireworks API key:

    ```bash  theme={null}
    export FIREWORKS_API_KEY="fw_your_api_key_here"
    ```

    Or create a `.env` file:

    ```bash  theme={null}
    FIREWORKS_API_KEY=fw_your_api_key_here
    ```
  </Step>

  <Step title="Test your evaluator locally">
    Before training, verify your evaluator works. This command discovers and runs your `@evaluation_test` with pytest. If a Dockerfile is present, it builds an image and runs the test in Docker; otherwise it runs on your host.

    ```bash  theme={null}
    cd evaluator_directory
    ep local-test
    ```
  </Step>

  <Step title="Create the RFT job">
    From the directory where your evaluator and dataset (dataset.jsonl) are located,

    ```bash  theme={null}
    eval-protocol create rft \
      --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
      --output-model my-model-name 
    ```

    The CLI will:

    * Upload evaluator code (if changed)
    * Upload dataset (if changed)
    * Create the RFT job
    * Display dashboard links for monitoring

    Expected output:

    ```
    Created Reinforcement Fine-tuning Job
       name: accounts/your-account/reinforcementFineTuningJobs/abc123

    Dashboard Links:
       Evaluator: https://app.fireworks.ai/dashboard/evaluators/your-evaluator
       Dataset:   https://app.fireworks.ai/dashboard/datasets/your-dataset
       RFT Job:   https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/abc123
    ```
  </Step>

  <Step title="Monitor training">
    Click the RFT Job link to watch training progress in real-time. See [Monitor Training](/fine-tuning/monitor-training) for details.
  </Step>
</Steps>

## Common CLI options

Customize your RFT job with these flags:

**Model and output**:

```bash  theme={null}
--base-model accounts/fireworks/models/llama-v3p1-8b-instruct  # Base model to fine-tune
--output-model my-custom-name                                   # Name for fine-tuned model
```

**Training parameters**:

```bash  theme={null}
--epochs 2                    # Number of training epochs (default: 1)
--learning-rate 5e-5          # Learning rate (default: 1e-4)
--lora-rank 16                # LoRA rank (default: 8)
--batch-size 65536            # Batch size in tokens (default: 32768)
```

**Rollout (sampling) parameters**:

```bash  theme={null}
--inference-temperature 0.8   # Sampling temperature (default: 0.7)
--inference-n 8               # Number of rollouts per prompt (default: 4)
--inference-max-tokens 4096   # Max tokens per response (default: 2048)
--inference-top-p 0.95        # Top-p sampling (default: 1.0)
--inference-top-k 50          # Top-k sampling (default: 40)
```

**Remote environments**:

```bash  theme={null}
--remote-server-url https://your-evaluator.example.com  # For remote rollout processing
```

**Force re-upload**:

```bash  theme={null}
--force                       # Re-upload evaluator even if unchanged
```

See all options:

```bash  theme={null}
eval-protocol create rft --help
```

## Advanced options

<AccordionGroup>
  <Accordion title="Weights & Biases integration">
    Track training metrics in W\&B for deeper analysis:

    ```bash  theme={null}
    eval-protocol create rft \
      --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
      --wandb-project my-rft-experiments \
      --wandb-entity my-org
    ```

    Set `WANDB_API_KEY` in your environment first.
  </Accordion>

  <Accordion title="Custom checkpoint frequency">
    Save intermediate checkpoints during training:

    ```bash  theme={null}
    firectl create rftj \
      --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
      --checkpoint-frequency 500  # Save every 500 steps
      ...
    ```

    Available in `firectl` only.
  </Accordion>

  <Accordion title="Multi-GPU acceleration">
    Speed up training with multiple GPUs:

    ```bash  theme={null}
    firectl create rftj \
      --base-model accounts/fireworks/models/llama-v3p1-70b-instruct \
      --accelerator-count 4  # Use 4 GPUs
      ...
    ```

    Recommended for large models (70B+).
  </Accordion>

  <Accordion title="Custom timeout">
    For evaluators that need more time:

    ```bash  theme={null}
    firectl create rftj \
      --rollout-timeout 300  # 5 minutes per rollout
      ...
    ```

    Default is 60 seconds. Increase for complex evaluations.
  </Accordion>
</AccordionGroup>

## Examples

**Fast experimentation** (small model, 1 epoch):

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b \
  --output-model quick-test
```

**High-quality training** (more rollouts, higher temperature):

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model high-quality-model \
  --inference-n 8 \
  --inference-temperature 1.0
```

**Remote environment** (for multi-turn agents):

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --remote-server-url https://your-agent.example.com \
  --output-model remote-agent
```

**Multiple epochs with custom learning rate**:

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --epochs 3 \
  --learning-rate 5e-5 \
  --output-model multi-epoch-model
```

## Using `firectl` CLI (Alternative)

For users already familiar with Fireworks `firectl`, you can create RFT jobs directly:

```bash  theme={null}
firectl create rftj \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --dataset accounts/your-account/datasets/my-dataset \
  --evaluator accounts/your-account/evaluators/my-evaluator \
  --output-model my-finetuned-model
```

**Differences from `eval-protocol`**:

* Requires fully qualified resource names (accounts/...)
* Must manually upload evaluators and datasets first
* More verbose but offers finer control
* Same underlying API as `eval-protocol`

See [firectl documentation](/tools-sdks/firectl/commands/create-reinforcement-fine-tuning-job) for all options.

## Next steps

<CardGroup cols={3}>
  <Card title="Prerequisites & Validation" icon="list-check" href="/fine-tuning/training-prerequisites">
    Review requirements, validation, and common errors
  </Card>

  <Card title="Monitor training" icon="chart-line" href="/fine-tuning/monitor-training">
    Track job progress, inspect rollouts, and debug issues
  </Card>

  <Card title="Parameter tuning" icon="sliders" href="/fine-tuning/parameter-tuning">
    Learn how to adjust parameters for better results
  </Card>
</CardGroup>
