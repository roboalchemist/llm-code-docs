# Source: https://docs.fireworks.ai/fine-tuning/monitor-training.md

# Monitor Training

> Track RFT job progress and diagnose issues in real-time

Once your RFT job is running, the Fireworks dashboard provides comprehensive monitoring tools to track progress, inspect individual rollouts, and debug issues as they arise.

## Accessing the monitoring dashboard

After creating your RFT job, you'll receive a dashboard link in the CLI output:

```
Dashboard Links:
   RFT Job: https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/abc123
```

Click this link or navigate manually:

1. Go to [Fireworks Dashboard](https://app.fireworks.ai)
2. Click **Fine-Tuning** in the sidebar
3. Select your job from the list

## Understanding the overview

The main dashboard shows your job's current state and key metrics.

### Job status

<AccordionGroup>
  <Accordion title="PENDING">
    Your job is queued waiting for GPU resources. Queue time depends on current demand and your account priority.

    **Action**: None needed. Job will start automatically when resources become available.
  </Accordion>

  <Accordion title="VALIDATING">
    Fireworks is validating your dataset to ensure it meets format requirements and quality standards.

    **Duration**: Typically 1-2 minutes

    **Action**: None needed. If validation fails, you'll receive specific error messages about issues in your dataset.
  </Accordion>

  <Accordion title="RUNNING">
    Training is actively in progress. Rollouts are being generated, evaluated, and the model is learning.

    **Action**: Monitor metrics and rollout quality. This is when you'll watch reward curves improve.
  </Accordion>

  <Accordion title="COMPLETED">
    Training finished successfully. Your fine-tuned model is ready for deployment.

    **Action**: Review final metrics, then [deploy your model](/fine-tuning/deploying-loras).
  </Accordion>

  <Accordion title="FAILED">
    Training encountered an unrecoverable error and stopped.

    **Action**: Check error logs and troubleshooting section below. Common causes include evaluator errors, resource limits, or dataset issues.
  </Accordion>

  <Accordion title="CANCELLED">
    You or another user manually stopped the job.

    **Action**: Review partial results if needed. Create a new job to continue training.
  </Accordion>

  <Accordion title="EARLY_STOPPED">
    Training stopped automatically because the full epoch showed no improvement. All rollouts received the same scores, indicating no training progress.

    **Action**: This typically indicates an issue with your evaluator or training setup. Check that:

    * Your evaluator is returning varied scores (not all 0s or all 1s)
    * The reward function can distinguish between good and bad outputs
    * The model is actually generating different responses

    Review the troubleshooting section below for common causes.
  </Accordion>
</AccordionGroup>

### Key metrics at a glance

The overview panel displays:

* **Elapsed time**: How long the job has been running
* **Progress**: Current epoch and step counts
* **Reward**: Latest mean reward from rollouts
* **Model**: Base model and output model names

## Training metrics

### Reward curves

The most important metric in RFT is the reward curve, which shows how well your model is performing over time.

**What to look for**:

* **Upward trend** - Model is learning and improving
* **Plateauing** - Model may have converged; consider stopping or adjusting parameters
* **Decline** - Potential issue with evaluator or training instability
* **Spikes** - Could indicate noisy rewards or outliers in evaluation

<Frame>
  <img src="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rft-curve.png?fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=30a9835239d9811bd99f8641e6c90c9a" alt="Reward curve showing upward trend over training epochs" data-og-width="995" width="995" data-og-height="640" height="640" data-path="images/fine-tuning/rft-curve.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rft-curve.png?w=280&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=fbab65cb28b1db31b5654619c9c819c4 280w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rft-curve.png?w=560&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=02b7fdee7646eab5ce3cbf04b450211a 560w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rft-curve.png?w=840&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=6ea697df83c36145d78f002624de411b 840w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rft-curve.png?w=1100&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=6935a782b99aa116e98edde28da2e5b1 1100w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rft-curve.png?w=1650&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=7952d0f69d7ce54cd2a89620f3c95fb5 1650w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rft-curve.png?w=2500&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=78aaa06c5e2defea39e696ed817261ac 2500w" />
</Frame>

<Tip>
  Healthy training shows steady reward improvement. Don't worry about minor fluctuations—focus on the overall trend.
</Tip>

### Training loss

Loss measures how well the model is fitting the training data:

* **Decreasing loss** - Normal learning behavior
* **Increasing loss** - Learning rate may be too high
* **Flat loss** - Model may not be learning; check evaluator rewards

### Evaluation metrics

If you provided an evaluation dataset, you'll see validation metrics:

* **Eval reward**: Model performance on held-out data
* **Generalization gap**: Difference between training and eval rewards

<Note>
  Large gaps between training and eval rewards suggest overfitting. Consider reducing epochs or adding more diverse training data.
</Note>

## Inspecting rollouts

Understanding individual rollouts helps you verify your evaluator is working correctly and identify quality issues.

### Rollout overview table

Click any **Epoch** in the training timeline, then click the **table icon** to view all rollouts for that step.

<Frame>
  <img src="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollouts.png?fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=ce21765cb4aea1ddf692022ef46b2103" alt="Table showing rollout IDs, prompts, responses, and rewards" data-og-width="970" width="970" data-og-height="738" height="738" data-path="images/fine-tuning/rollouts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollouts.png?w=280&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=03d4817a065f954817539a6d72dcb27e 280w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollouts.png?w=560&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=881653d7d6900f773ebb15bdccb2cfd2 560w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollouts.png?w=840&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=7d0a95d99eb4917dce29e83980278965 840w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollouts.png?w=1100&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=fe1736ae21cdd89f95b53b5db479c923 1100w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollouts.png?w=1650&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=8f9bf1f0210a0c4b1d86ed21b843fd63 1650w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollouts.png?w=2500&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=9818f2f4873ecb2b84712137e83ddba5 2500w" />
</Frame>

The table shows:

* **Row ID**: Unique identifier for each dataset row used in this rollout
* **Prompt**: The input prompt sent to the model
* **Messages**: The model's generated response messages
* **Valid**: Whether the rollout completed successfully without errors
* **Reason**: Explanation if the rollout failed or was marked invalid
* **Score**: Reward score assigned by your evaluator (0.0 to 1.0)

**What to check**:

* Most rollouts succeeding (status: complete)
* Reward distribution makes sense (high for good outputs, low for bad)
* Many failures indicate evaluator issues
* All rewards identical may indicate evaluator is broken

### Individual rollout details

Click any row in the rollout table to see full details:

<Frame>
  <img src="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollout_details.png?fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=ddd3e5b90495925b71b869d9814a0437" alt="Detailed view of a single rollout showing full prompt, response, and evaluation" data-og-width="958" width="958" data-og-height="1134" height="1134" data-path="images/fine-tuning/rollout_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollout_details.png?w=280&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=56d02fc5120b13c55203609cf130d74a 280w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollout_details.png?w=560&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=40fbc95ea50ad570bf0b7d06b66e4956 560w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollout_details.png?w=840&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=7affad09e726a4c46c5b7c2aa255e26c 840w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollout_details.png?w=1100&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=4eb63a6539b5a4caf7305f191c092b6e 1100w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollout_details.png?w=1650&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=72c0f95c60aabed999bf2586102e8085 1650w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/rollout_details.png?w=2500&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=d9b764f09c51d63fe9207475c239d891 2500w" />
</Frame>

You'll see:

1. **Full prompt**: Exact messages sent to the model
2. **Model response**: Complete generated output
3. **Evaluation result**: Reward score and reasoning (if provided)
4. **Metadata**: Token counts, timing, temperature settings
5. **Tool calls**: For agentic rollouts with function calling

<Tip>
  Copy and paste model outputs to test them manually. For example, if you're training a code generator, try running the generated code yourself to verify your evaluator is scoring correctly.
</Tip>

### Quality spot checks

Regularly inspect rollouts at different stages of training:

**Early training (first epoch)**:

* Verify evaluator is working correctly
* Check that high-reward rollouts are actually good
* Ensure low-reward rollouts are actually bad

**Mid-training**:

* Confirm model quality is improving
* Look for new strategies or behaviors emerging
* Check that evaluator isn't being gamed

**Late training**:

* Verify final model quality meets your standards
* Check for signs of overfitting (memorizing training data)
* Ensure diversity in responses (not all identical)

## Live logs

Real-time logs show what's happening inside your training job.

### Accessing logs

Click the **Logs icon** next to the table icon to view real-time logs for your training job.

<Frame>
  <img src="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/logs.png?fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=3a7932de5139fc3262084fc67ee94dd7" alt="Live log streaming showing rollout processing and evaluation" data-og-width="1227" width="1227" data-og-height="606" height="606" data-path="images/fine-tuning/logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/logs.png?w=280&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=3c4da82b89545ca421565884207ef74c 280w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/logs.png?w=560&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=8ccfa4fbaf154bcfb48b2d4ce4d7a41c 560w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/logs.png?w=840&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=a2b8fe1865347b37bbaaaeeafbf5593f 840w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/logs.png?w=1100&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=6e02bc57070a8506d29a595b68b90015 1100w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/logs.png?w=1650&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=b4a17c66e8c74abbb6695f19b0c627a2 1650w, https://mintcdn.com/fireworksai/Q8d9TB4Mz8qoqdNf/images/fine-tuning/logs.png?w=2500&fit=max&auto=format&n=Q8d9TB4Mz8qoqdNf&q=85&s=0b26b25f8b43c9962a1c2ee45855fb80 2500w" />
</Frame>

### Using logs for debugging

When things go wrong, logs are your first stop:

1. **Filter by error level**: Focus on `[ERROR]` and `[WARNING]` messages
2. **Search for rollout IDs**: Track specific rollouts through their lifecycle
3. **Look for patterns**: Repeated errors indicate systematic issues
4. **Check timestamps**: Correlate errors with metric changes

## Common issues and solutions

<AccordionGroup>
  <Accordion title="Training stuck at low reward">
    **Symptoms**: Reward curve flat or very low throughout training

    **Possible causes**:

    * Evaluator always returning 0 or very low scores
    * Model outputs not matching expected format
    * Task too difficult for base model

    **Solutions**:

    1. Inspect rollouts to verify evaluator is working:
       * Check that some rollouts get high rewards
       * Verify reward logic makes sense
    2. Test evaluator locally on known good/bad outputs
    3. Simplify the task or provide more examples
    4. Try a stronger base model
  </Accordion>

  <Accordion title="Reward suddenly drops">
    **Symptoms**: Reward increases then crashes and stays low

    **Possible causes**:

    * Learning rate too high causing training instability
    * Model found an exploit in the evaluator (reward hacking)
    * Catastrophic forgetting

    **Solutions**:

    1. Stop training and use the last good checkpoint
    2. Restart with lower learning rate (e.g., `--learning-rate 5e-5`)
    3. Review recent rollouts for reward hacking behavior
    4. Improve evaluator to be more robust
  </Accordion>

  <Accordion title="Many rollout failures">
    **Symptoms**: Rollout table shows lots of errors or timeouts

    **Possible causes**:

    * Evaluator code errors
    * Timeout too short for evaluation
    * External API failures (for remote evaluators)
    * Resource exhaustion

    **Solutions**:

    1. Check error logs for specific error messages
    2. Test evaluator locally to reproduce errors
    3. Increase `--rollout-timeout` if evaluations need more time
    4. Add better error handling in evaluator code
    5. For remote evaluators: check server health and logs
  </Accordion>

  <Accordion title="Training loss increases">
    **Symptoms**: Loss goes up instead of down

    **Possible causes**:

    * Learning rate too high
    * Conflicting reward signals
    * Numerical instability

    **Solutions**:

    1. Reduce learning rate by 2-5x
    2. Check that rewards are consistent (same prompt gets similar rewards)
    3. Verify rewards are in valid range \[0, 1]
    4. Consider reducing batch size
  </Accordion>

  <Accordion title="All rollouts identical">
    **Symptoms**: Model generates the same response for every prompt

    **Possible causes**:

    * Temperature too low (near 0)
    * Model found one high-reward response and overfit to it
    * Evaluator only rewards one specific output

    **Solutions**:

    1. Increase `--temperature` to 0.8-1.0
    2. Make evaluator more flexible to accept diverse good answers
    3. Use more diverse prompts in training data
    4. Reduce epochs to prevent overfitting
  </Accordion>

  <Accordion title="Remote evaluator timeouts">
    **Symptoms**: Many rollouts timing out with remote environment

    **Possible causes**:

    * Remote server slow or overloaded
    * Network latency issues
    * Evaluator not logging completion correctly

    **Solutions**:

    1. Check remote server logs for errors
    2. Verify server is logging `Status.rollout_finished()`
    3. Increase `--rollout-timeout` to allow more time
    4. Scale remote server to handle concurrent requests
    5. Optimize evaluator code for performance
  </Accordion>
</AccordionGroup>

## Performance optimization

### Speeding up training

If training is slower than expected:

<AccordionGroup>
  <Accordion title="Optimize evaluator speed">
    **Slow evaluators directly increase training time**:

    * Profile your evaluator code to find bottlenecks
    * Cache expensive computations
    * Use batch processing for API calls
    * Add timeouts to prevent hanging

    **For remote evaluators**:

    * Add more worker instances to handle concurrent rollouts
    * Use faster machines (more CPU, memory)
    * Optimize network connectivity to Fireworks

    Target: Evaluations should complete in 1-5 seconds per rollout.
  </Accordion>

  <Accordion title="Adjust rollout parameters">
    **Reduce compute while maintaining quality**:

    * Decrease `--n` (e.g., from 8 to 4 rollouts per prompt)
    * Reduce `--max-tokens` if responses don't need to be long
    * Lower temperature slightly to speed up sampling

    Caution: Too few rollouts (n \< 4) may hurt training quality.
  </Accordion>
</AccordionGroup>

### Cost optimization

Reduce costs without sacrificing too much quality:

1. **Start small**: Experiment with `qwen3-0p6b` before scaling to larger models
2. **Reduce rollouts**: Use `--n 4` instead of 8
3. **Shorter responses**: Lower `--max-tokens` to minimum needed
4. **Fewer epochs**: Start with 1 epoch, only add more if needed
5. **Efficient evaluators**: Minimize API calls and computation

## Stopping and resuming jobs

### Stopping a running job

If you need to stop training:

1. Click **Cancel Job** in the dashboard
2. Or via CLI:
   ```bash  theme={null}
   firectl delete rftj <job-id>
   ```

The model state at the last checkpoint is saved and can be deployed.

<Warning>
  Cancelled jobs cannot be resumed. If you want to continue training, create a new job starting from the last checkpoint.
</Warning>

### Using checkpoints

Checkpoints are automatically saved during training. To continue from a checkpoint:

```bash  theme={null}
eval-protocol create rft \
  --warm-start-from accounts/your-account/models/previous-checkpoint \
  --output-model continued-training
```

This is useful for:

* Extending training after early stopping
* Trying different hyperparameters on a trained model
* Building on previous successful training runs

## Comparing multiple jobs

Running multiple experiments? Compare them side-by-side:

1. Navigate to **Fine-Tuning** dashboard
2. Select multiple jobs using checkboxes
3. Click **Compare**

This shows:

* Reward curves overlaid on same graph
* Parameter differences highlighted
* Final metrics comparison
* Training time and cost comparison

<Tip>
  Use consistent naming for experiments (e.g., `math-lr-1e4`, `math-lr-5e5`) to make comparisons easier.
</Tip>

## Exporting metrics

For deeper analysis or paper writing:

### Via dashboard

1. Click **Export** button in job view
2. Choose format: CSV, JSON
3. Select metrics to export (rewards, loss, rollout data)

### Via API

```python  theme={null}
import requests

response = requests.get(
    f"https://api.fireworks.ai/v1/accounts/{account}/reinforcementFineTuningJobs/{job_id}/metrics",
    headers={"Authorization": f"Bearer {api_key}"}
)

metrics = response.json()
```

### Weights & Biases integration

If you enabled W\&B when creating the job:

```bash  theme={null}
eval-protocol create rft \
  --wandb-project my-experiments \
  --wandb-entity my-org \
  ...
```

All metrics automatically sync to W\&B for advanced analysis, comparison, and sharing.

## Best practices

<AccordionGroup>
  <Accordion title="Monitor early, monitor often">
    Check your job within the first 15-30 minutes of training:

    * Verify evaluator is working correctly
    * Confirm rewards are in expected range
    * Catch configuration errors early

    Don't wait until training completes to discover issues.
  </Accordion>

  <Accordion title="Spot check rollouts regularly">
    Every few epochs, inspect 5-10 random rollouts:

    * Manually verify high-reward outputs are actually good
    * Check low-reward outputs are actually bad
    * Look for unexpected model behaviors

    This catches evaluator bugs and reward hacking.
  </Accordion>

  <Accordion title="Save successful configurations">
    When you find good hyperparameters, save the command:

    ```bash  theme={null}
    # Save to file for reproducibility
    echo "eval-protocol create rft --base-model ... --learning-rate 5e-5 ..." > best_config.sh
    ```

    Makes it easy to reproduce results or share with team.
  </Accordion>

  <Accordion title="Use meaningful names">
    Name jobs descriptively:

    * Good: `math-solver-llama8b-temp08-n8`
    * Bad: `test1`, `try2`, `final-final`

    Future you will thank you when comparing experiments.
  </Accordion>

  <Accordion title="Document experiments">
    Keep notes on what worked and what didn't:

    * Hypothesis for each experiment
    * Parameters changed
    * Results and insights
    * Next steps

    Build institutional knowledge for your team.
  </Accordion>
</AccordionGroup>

## Next steps

<CardGroup cols={2}>
  <Card title="Deploy your model" icon="rocket" href="/fine-tuning/deploying-loras">
    Once training completes, deploy your fine-tuned model for inference
  </Card>

  <Card title="Parameter tuning" icon="sliders" href="/fine-tuning/parameter-tuning">
    Learn how to adjust parameters for better results
  </Card>

  <Card title="Evaluator best practices" icon="lightbulb" href="/fine-tuning/evaluators">
    Improve your reward functions based on training insights
  </Card>

  <Card title="Launch another job" icon="play" href="/fine-tuning/cli-reference">
    Start a new experiment using the CLI
  </Card>
</CardGroup>
