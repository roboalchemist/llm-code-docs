# Source: https://docs.fireworks.ai/fine-tuning/rft-parameters-reference.md

# Parameters Reference

> Quick lookup for all RFT training and rollout parameters

Quick reference for all reinforcement fine-tuning parameters. Most experiments converge with the defaults below. Change them only when you have a clear hypothesis.

<Tip>
  For guidance on **when to change** these parameters, see the [Parameter Tuning guide](/fine-tuning/parameter-tuning).
</Tip>

## Training parameters

| Flag                   | Default         | Suggested range             | When to change                                                                                                        |
| ---------------------- | --------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `--epochs`             | **1**           | 1 – 10 (whole numbers only) | Add 1-2 more passes if the reward still climbs steadily near the end of training. Too many epochs risks over-fitting. |
| `--learning-rate`      | **1 e-4**       | 1 e-5 – 5 e-4               | Decrease when the reward spikes then collapses; increase when the curve plateaus too early.                           |
| `--lora-rank`          | **8**           | 4 – 32 (powers of 2)        | Higher ranks may potentially improve training quality, but often require more data/iterations to train                |
| `--max-context-length` | **8192 tokens** | Up to model limit           | Raise only when your prompts truncate; remember longer sequences consume quadratic compute.                           |

### Example usage

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model my-rft-model \
  --epochs 3 \
  --learning-rate 1e-4 \
  --lora-rank 16 \
  --max-context-length 16384
```

## Rollout (sampling) parameters

During each training step, the model generates multiple responses with stochastic decoding. These parameters control that generation process.

| Field           | CLI flag                 | Default   | Recommended range      | Why it matters                                                                                            |
| --------------- | ------------------------ | --------- | ---------------------- | --------------------------------------------------------------------------------------------------------- |
| Maximum tokens  | `--max-tokens`           | **2 048** | 16 – 16 384            | Longer responses improve reward on summarisation / story tasks but add cost.                              |
| Temperature     | `--temperature`          | **0.7**   | 0.1 – 2.0 ( > 0 only ) | Values below 0.1 converge towards greedy decoding and kill exploration; 0.5–1.0 is a sweet spot for RLHF. |
| Top-p           | `--top-p`                | **1.0**   | 0 – 1                  | Lower to 0.2–0.5 to clamp long-tail tokens when the reward penalises hallucinations.                      |
| Top-k           | `--top-k`                | **40**    | 0 – 100 (0 = off)      | Combine with `temperature` for more creative exploration; keep ≤50 for latency.                           |
| *n* (choices)   | `--n`                    | **4**     | 2 – 8                  | Policy-Optimization needs multiple candidates to compute a meaningful KL term; ≥2 is mandatory.           |
| Extra body JSON | `--inference-extra-body` | *empty*   | valid JSON             | Pass extra OpenAI-style params (e.g., `stop`, `logit_bias`). Invalid JSON is rejected.                    |

### Example usage

```bash  theme={null}
eval-protocol create rft \
  --base-model accounts/fireworks/models/llama-v3p1-8b-instruct \
  --output-model my-model \
  --max-tokens 1024 \
  --temperature 0.8 \
  --top-p 0.9 \
  --top-k 40 \
  --n 6 \
  --inference-extra-body '{"stop":["\n\n"]}'
```

## Quick reference by goal

| Goal                   | Parameters to adjust                           |
| ---------------------- | ---------------------------------------------- |
| **Faster convergence** | ↑ `epochs`, tune `learning-rate` \< 2× default |
| **Safer / less toxic** | ↓ `temperature`, `top_p`, `top_k`              |
| **More creative**      | `temperature` ≈ 1 – 1.2, `top_p` 0.9           |
| **Cheaper roll-outs**  | ↓ `n`, `max_tokens`, batch size                |
| **Higher capacity**    | ↑ `lora-rank`                                  |

## Important constraints

### Temperature must be > 0

Greedy sampling (temperature 0) is deterministic and cannot produce multiple different rollouts, which is a requirement for RFT. It also can lead to mode-dropping and repetitive text.

### At least 2 rollouts required

Policy optimization needs multiple candidates per prompt to compute a meaningful KL divergence term. Setting `--inference-n 1` will fail.

### Range enforcement

The UI and CLI enforce the ranges shown above. Out-of-bound values throw an *Invalid rollout parameters* error immediately, saving wasted GPU hours.

## Next steps

<CardGroup cols={2}>
  <Card title="Parameter tuning guide" icon="sliders" href="/fine-tuning/parameter-tuning">
    Learn strategies for when and how to adjust parameters
  </Card>

  <Card title="Launch training" icon="rocket" href="/fine-tuning/cli-reference">
    Launch your RFT job
  </Card>

  <Card title="GSM8K Quickstart" icon="graduation-cap" href="/fine-tuning/quickstart-math">
    Hands-on tutorial for RFT training
  </Card>

  <Card title="RFT Overview" icon="book-open" href="/fine-tuning/reinforcement-fine-tuning-models">
    Learn about the RFT training process
  </Card>
</CardGroup>
