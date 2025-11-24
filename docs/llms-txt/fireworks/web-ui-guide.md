# Source: https://docs.fireworks.ai/fine-tuning/web-ui-guide.md

# Training Guide: UI

> Launch RFT jobs using the Fireworks dashboard

The Fireworks RFT UI provides a visual interface for creating RFT jobs, with guided parameter selection. Results for all jobs can also be found in the UI.

## When to use Web UI

<Tip>
  Start with the UI to learn the options, then switch to [CLI](/fine-tuning/cli-reference) for faster iteration and automation. Remember, your results will always live in the UI.
</Tip>

| Feature                 | CLI (eval-protocol)           | Web UI                        |
| ----------------------- | ----------------------------- | ----------------------------- |
| **Best for**            | Experienced users, automation | First-time users, exploration |
| **Parameter discovery** | Need to know flag names       | Guided with tooltips          |
| **Speed**               | Fast - single command         | Slower - multiple steps       |
| **Automation**          | Easy to script and reproduce  | Manual process                |
| **Batch operations**    | Easy to launch multiple jobs  | One at a time                 |
| **Reproducibility**     | Excellent - save commands     | Manual tracking needed        |

## Launch training via Web UI

<Steps>
  <Step title="Navigate to Fine-Tuning">
    1. Go to [Fireworks Dashboard](https://app.fireworks.ai)
    2. Click **Fine-Tuning** in the left sidebar
    3. Click **Fine-tune a Model**

    <Frame>
      <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=4c2ad94681a8327cb870c5f92c1cf5d7" alt="Fine-tuning dashboard showing list of jobs" data-og-width="2966" width="2966" data-og-height="2052" height="2052" data-path="images/fine-tuning/fine-tuning.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=67e542c9ea90128f6cd1b53ff8c92aed 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=deef7708b9713cce4afd4cf7744df559 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=f99d019df0142144114475ce9e7c7729 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=bca80f9c479e23ed45e8c51374ac71bb 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5835f9d2a269326985b00cb9b15f12e6 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/fine-tuning.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=040f237a22bd3109c36acaad9c15907f 2500w" />
    </Frame>
  </Step>

  <Step title="Select Reinforcement Fine-Tuning">
    1. Choose **Reinforcement** as the tuning method
    2. Select your base model from the dropdown

    The UI shows only models that support fine-tuning. Popular choices appear at the top.

    <Tip>
      Not sure which model to choose? Start with `llama-v3p1-8b-instruct` for a good balance of quality and speed.
    </Tip>
  </Step>

  <Step title="Configure Dataset">
    1. **Upload new dataset** or **select existing** from your account
    2. Preview dataset entries to verify format
    3. The UI validates your JSONL format automatically

    <Frame>
      <img src="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=33255bb2d9afefc697230a6f4e723577" alt="Dataset selection interface" data-og-width="2972" width="2972" data-og-height="2060" height="2060" data-path="images/fine-tuning/dataset.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=280&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=e1f7631eedf19be2ffe910e931734378 280w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=560&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=5148e67713f7a207c47a73da1fa56658 560w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=840&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=dde9343748034e1d13ae4fbc1ad4aecf 840w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1100&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=a4a99ce824157064f5cbbdfdf0953c0d 1100w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=1650&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=699fd69866de9383a06dc08a5139cb69 1650w, https://mintcdn.com/fireworksai/sTHhFfY93wc80BaS/images/fine-tuning/dataset.png?w=2500&fit=max&auto=format&n=sTHhFfY93wc80BaS&q=85&s=b55ed77bc807c1ebf00223fff2997342 2500w" />
    </Frame>

    Each dataset row should have `messages` array:

    ```json  theme={null}
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is 25 * 4?"}
      ]
    }
    ```
  </Step>

  <Step title="Select Evaluator">
    1. Choose from your uploaded evaluators
    2. Preview evaluator code and test results
    3. View recent evaluation metrics

    If you haven't uploaded an evaluator yet, you'll need to do that first via CLI:

    ```bash  theme={null}
    pytest my-evaluator-name.py -vs
    ```

    <Note>
      For remote evaluators, you'll enter your server URL in the environment configuration section.
    </Note>
  </Step>

  <Step title="Set Training Parameters">
    Configure how the model learns:

    **Core parameters**:

    * **Output model name**: Custom name for your fine-tuned model
    * **Epochs**: Number of passes through the dataset (start with 1)
    * **Learning rate**: How fast the model updates (use default 1e-4)
    * **LoRA rank**: Model capacity (8-16 for most tasks)
    * **Batch size**: Training throughput (use default 32k tokens)

    The UI shows helpful tooltips for each parameter. See [Parameter Tuning](/fine-tuning/parameter-tuning) for detailed guidance.
  </Step>

  <Step title="Configure Rollout Parameters">
    Control how the model generates responses during training:

    * **Temperature**: Sampling randomness (0.7 for balanced exploration)
    * **Top-p**: Probability mass cutoff (0.9-1.0)
    * **Top-k**: Token candidate limit (40 is standard)
    * **Number of rollouts (n)**: Responses per prompt (4-8 recommended)
    * **Max tokens**: Maximum response length (2048 default)

    Higher temperature and more rollouts increase exploration but also cost.
  </Step>

  <Step title="Review and Launch">
    1. Review all settings in the summary panel
    2. See estimated training time and cost
    3. Click **Start Fine-Tuning** to launch

    The dashboard will redirect you to the job monitoring page where you can track progress in real-time.
  </Step>
</Steps>

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
