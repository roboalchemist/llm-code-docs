# Source: https://docs.fireworks.ai/fine-tuning/quickstart-svg-agent.md

# Remote Agent Quickstart

> Train an SVG drawing agent running in a remote environment

<Note>
  **Following the [RFT Overview](/fine-tuning/reinforcement-fine-tuning-models)?** This is the **Remote Agent Training** path—for training agents that run in your production infrastructure.
</Note>

In this quickstart, you'll train an agent to generate SVG drawings. Your agent runs in a remote server (Vercel), which means rollouts happen remotely while Fireworks handles the training. This approach lets you train agents that already live in your production environment.

Here's a quick walkthrough:

<Frame>
  <iframe src="https://www.loom.com/embed/24ba433601de45ba8b63d9fb34c31fd5" width="100%" height="420" frameBorder="0" allow="autoplay; fullscreen" allowFullScreen />
</Frame>

## What You'll Learn

* **Apply RFT to production agents** — Train models that work with remote servers and existing infrastructure
* **Remote rollout processing** — Connect your production environment to Fireworks RFT using Eval Protocol
* **Monitor and debug training** — Track progress, inspect rollouts, and debug issues with live logs

## 1. Installation

1. **Clone the quickstart repo**: [https://github.com/eval-protocol/quickstart](https://github.com/eval-protocol/quickstart)

```bash  theme={null}
git clone git@github.com:eval-protocol/quickstart.git
cd quickstart
```

2. **Install Eval Protocol**:

```bash  theme={null}
pip install "eval-protocol[svgbench]"
```

3. **Environment Setup**:

The `env.example` file is located in the `evaluator/` directory. Make a copy of it in the same directory, name it `.env`, and fill in your API keys:

```bash  theme={null}
cp evaluator/env.example evaluator/.env
```

Then edit `evaluator/.env` with your API keys:

```
FIREWORKS_API_KEY=your-fireworks-key-here
OPENAI_API_KEY=your-openai-key-here
```

The create process below automatically reads and uploads these secrets to Fireworks.

## 2. Test your evaluator locally

Test your evaluator locally before launching training, to verify everything works with your rollout processor.

**Terminal 1** - Start the local UI server to view results:

```bash  theme={null}
ep logs
```

**Terminal 2** - Kick off the test:

```bash  theme={null}
cd evaluator
ep local-test
```

This command discovers and runs your `@evaluation_test` with pytest. In this case, it builds an image and runs the test in Docker, because a `Dockerfile` is present.

The test automatically uses our Vercel remote server:

```
rollout_processor=RemoteRolloutProcessor(
    remote_base_url="https://vercel-svg-server-ts.vercel.app",
)
```

If you want to use a local development Vercel server instead, see [Local Development Server](#local-development-server).

**Note:**

* If your evaluation setup has custom system dependencies (e.g., Chromium), add a `Dockerfile`. When you run `ep local-test`, it will build an image and run `pytest` inside Docker.
* If you don't need Docker, `ep local-test` will run `pytest` on your host machine by default.
* You can ignore the `Dockerfile` and force host execution with: `ep local-test --ignore-docker`.

### Expected Test Output

Navigate to [http://localhost:8000](http://localhost:8000) to see the Eval Protocol UI.

```
INFO:eval_protocol.pytest.remote_rollout_processor:Found status log for rollout democratic-way-12: Rollout democratic-way-12 completed
INFO:eval_protocol.pytest.remote_rollout_processor:Found Fireworks log for rollout democratic-way-12 with status code 100.0
INFO:eval_protocol.adapters.fireworks_tracing:Successfully converted 1 traces to evaluation rows | 3/8 [00:19<00:22, 4.52s/rollout]
...
Runs (Parallel): 100%|████████████████████████████████████████████| 1/1 [00:31<00:00, 31.07s/run]
PASSED
```

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e77097c700e374bdf7e7cafbe867eacb" alt="Eval Protocol Logs Interface" data-og-width="1273" width="1273" data-og-height="716" height="716" data-path="images/ep_logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=d9929ea24b65066e9b49db7a1cc01735 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e65c345b1cc114b86cc482c0b049595f 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=a9ff29184be84502944bef0fec9e3c78 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=fc6db5a4b499f5039bf5625f8293e2c2 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=3346acbf2a9428562371dc2f5500c58e 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/ep_logs.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=d38c0c8c66935f754ff97757dd1b90e1 2500w" />

If you're interested in understanding how Remote Rollout Processing works and how it communicates with the remote server, see [How Remote Rollout Processing Works](#how-remote-rollout-processing-works).

## 3. Start training with a single command

To kickoff training, simply do:

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b \
  --epochs 8 \
  --chunk-size 10
```

This command:

1. Uploads secrets — reads your `.env` and uploads API keys as Fireworks secrets
2. Uploads evaluator — packages and uploads your evaluation code
3. Waits for build — polls evaluator status until ACTIVE (timeout: 10 minutes)
4. Creates dataset — uploads your `svgbench_dataset.jsonl`
5. Launches RFT job — starts reinforcement fine-tuning with your evaluator

### Configuration & Troubleshooting

**Training Parameters**: We use Eval Protocol's default values for training parameters (batch size, epochs, learning rate, LoRA rank, accelerator count, etc.). For a complete list of available RFT flags you can customize, see [Fireworks RFT Command Documentation](https://docs.fireworks.ai/tools-sdks/firectl/commands/create-reinforcement-fine-tuning-job).

**Changing Evaluators**: If you've made changes to your evaluator code and want to upload a new version:

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/qwen3-0p6b \
  --epochs 8 \
  --chunk-size 10 \
  --force
```

**Evaluator Upload Timing Out**: If your evaluator takes longer than 10 minutes to build, you'll see:

```
⏰ Timeout after 10.0m - evaluator is not yet ACTIVE

❌ Evaluator is not ready within the timeout period.
📊 Please check the evaluator status at: https://app.fireworks.ai/dashboard/evaluators/test-svgagent-test-svg-generation-evaluation
   Wait for it to become ACTIVE, then run 'eval-protocol create rft' again.
```

In this case, monitor the evaluator upload at the link, and run the command again when ACTIVE.

## 4. Monitor Training Progress

After successful job creation, you'll see:

```
✅ Created Reinforcement Fine-tuning Job
   name: accounts/pyroworks/reinforcementFineTuningJobs/sdnld4yn

📊 Dashboard Links:
   Evaluator: https://app.fireworks.ai/dashboard/evaluators/test-svgagent-test-svg-generation-evaluation
   Dataset:   https://app.fireworks.ai/dashboard/datasets/svgbench-dataset
   RFT Job:   https://app.fireworks.ai/dashboard/fine-tuning/reinforcement/sdnld4yn
```

Click on the **RFT Job** link to view real-time training progress, epoch counts, and rollout data.

### Training Results

After successful training, you should see performance improvements reflected in the training metrics:

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=049359a9ff673f1ebbe79870bebc646e" alt="SVG Agent Training Progress" data-og-width="1145" width="1145" data-og-height="727" height="727" data-path="images/graph.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c134ea53f61e553faed64f894fbd0968 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=33b9a24999f60e61c13de78a55e3825a 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=029ff347c5522122c86cdc6e5f98036b 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e8920443c785f7a525342f33a80183fd 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=5d4544e02181f10132840bb4c748d38f 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/graph.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=b064462ba16e5906472fe66a7c4b5b98 2500w" />

### SVG Quality Improvement

You can inspect individual rollouts to see the dramatic improvement in SVG generation quality. Below is a comparison between the first epoch and the final 8th epoch:

**Before (1st Epoch):**
<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=7160c0606439b6a7c5bc851d207975f7" alt="SVG Generation - Before Training" data-og-width="1606" width="1606" data-og-height="1136" height="1136" data-path="images/before.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c3dc3ebfa621ef702648f84c4ebe2657 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=48d46aad8b93acc9e9eb40c42137d6b7 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=94f322bcf6fd77d3709ae6cebd4e9f5f 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=03476db9954ce10c5179f934f235d60c 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=328e7e71e39095a6c868bb1cc40f4c19 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/before.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=5088edd903f4c0d3c71c18e6ff70c74b 2500w" />

**After (8th Epoch):**
<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=4d99b24ddb6cd458f35f2b4b00fd8646" alt="SVG Generation - After Training" data-og-width="2030" width="2030" data-og-height="1134" height="1134" data-path="images/after.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=1679375e0cf298aee49b0d0b666ca55e 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=f8ec41ee5416fdecf791041e61fe197d 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=622917132d20de1c72529156353d4cbe 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c6d98d80618948496ec32998486c4564 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=29b3e697b5b9667255a04a6ede7e6c06 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/after.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=02b71ab52b92f08ef90eade45d365361 2500w" />

The reinforcement fine tuning process significantly improves the model's ability to generate accurate, detailed SVG graphics that better match the input descriptions.

## Debugging Tips

When your training is running, you have several powerful tools to debug and monitor your rollouts:

### Rollout Overview

Clicking on any **Epoch** or **Step** in the training dashboard, then clicking the **table icon** to the right, will show you a comprehensive table of all rollouts. It's a good high-level overview to see if any rollouts failed and for what reason.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=4e6dda85703f77bcce58b83a391e0f2d" alt="Rollout Overview Table" data-og-width="981" width="981" data-og-height="824" height="824" data-path="images/rollouts.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=0a39037d8e3818f7ffe5dd311c210b74 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=2bbe1b8c9b5ade0376fa8363fe8d5ec2 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=54cf4174612678513d44af4afb7a4387 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=ec2e71a16032151cbb3f0c647f16a94f 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=f9cd11af326b4329adf16993bb1a970e 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollouts.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=94ab07e54df7e21f8f2b9cf216c3d961 2500w" />

### Individual Rollout Details

If you click on a specific row in the rollout table, you can see exactly what the prompt was and how the model responded. You can even copy and paste out the SVG code generated and render it yourself to see what the model did. This is how we got the results above in the before and after comparison.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=0f1384d546a1d5f5f2e85cef97242265" alt="Individual Rollout Details" data-og-width="1497" width="1497" data-og-height="958" height="958" data-path="images/rollout_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=c38dbe0ea185fc439889ec216b4d7d89 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=20831b5ff6710155343ec26a519c69cd 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=6de20cd4112cc11966b92792eb9d38f6 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=e7fc0f01da318743bd0d0d47539ef9c9 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=082a3a517842f905b4b002ec6898c22d 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/rollout_details.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=237f8903eefb31bb1f66937cf2979769 2500w" />

### Live Log Streaming

Clicking on **View Logs** takes you to a page of logs being streamed in. Here, you can see precisely what errors are happening to the rollouts. This is useful to debug and fix any issues with your rollouts.

<img src="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=66aed2a6eac9532a37f0106c0f5a526a" alt="Live Log Streaming" data-og-width="1399" width="1399" data-og-height="958" height="958" data-path="images/logs.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=280&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=9b5d411a6c5810f975952bda32990a74 280w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=560&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=3b1067074975220120cf884e2fe4e04e 560w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=840&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=990e0d1a4815818d085cfe6e8319185c 840w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=1100&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=a6f64807089b7221495cbac2e8eeea5a 1100w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=1650&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=658c42b53a98ce57d8746106ec2b7b03 1650w, https://mintcdn.com/fireworksai/53mdbJUS0jgliYBV/images/logs.png?w=2500&fit=max&auto=format&n=53mdbJUS0jgliYBV&q=85&s=b726b75b643b3837231aa5e4c3cf795c 2500w" />

## Next steps

<CardGroup cols={3}>
  <Card title="Customize training" icon="terminal" href="/fine-tuning/cli-reference">
    Learn all CLI options to customize your training parameters
  </Card>

  <Card title="Try a single-turn example" icon="laptop-code" href="/fine-tuning/quickstart-math">
    Train models with  Python evaluators for simpler tasks
  </Card>

  <Card title="Learn RFT concepts" icon="brain" href="/fine-tuning/reinforcement-fine-tuning-models">
    Understand how reinforcement fine-tuning works
  </Card>
</CardGroup>

## Additional resources

* [Discord Server](https://discord.gg/mMqQxvFD9A) - Come talk to us in the #eval-protocol channel!
* [Eval Protocol Documentation](https://evalprotocol.io/introduction)
* [Remote Rollout Processor Tutorial](https://evalprotocol.io/tutorial/remote-rollout-processor)
* [SVGBench Dataset](https://github.com/johnbean393/SVGBench) - The original benchmark this project is based on

## Appendix

### How Remote Rollout Processing Works

Eval Protocol enables **reinforcement learning that meets you where you are**. Instead of forcing you to rewrite your agent in a specific framework, you can implement a lightweight remote server wherever your codebase and infrastructure already live.

Your remote server is only responsible for:

* **Executing rollouts** - Run your agent logic (in this case, SVG generation from text prompts)
* **Logging to tracing** - Send structured logs to `tracing.fireworks.ai` for evaluation (see the below linked docs for more information)

In this example, we showcase a **Vercel TypeScript server** that executes single-turn SVG code generation.

> **📖 Learn More**: For a complete deep-dive into Remote Rollout Processing, see the [Remote Rollout Processor Tutorial](https://evalprotocol.io/tutorial/remote-rollout-processor).

### Local Development Server

```bash  theme={null}
cd vercel_svg_server_ts
vercel dev
```

Then swap out the `remote_base_url` to point to the local server you just started:

```
rollout_processor=RemoteRolloutProcessor(
    remote_base_url="http://localhost:3000",
)
```

And in a third terminal, run the evaluation:

```bash  theme={null}
ep local-test
```

> See [Vercel CLI documentation](https://vercel.com/docs/cli/dev) for more information on local development.
