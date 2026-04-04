# Source: https://docs.ragas.io/en/stable/references/optimizers/index.md

# Optimizers API Reference

Ragas provides optimizers to improve metric prompts through automated optimization. This page documents the available optimizer classes and their configuration.

## Overview

Optimizers use annotated datasets with ground truth scores to refine metric prompts, improving accuracy through:

- **Instruction optimization**: Finding better prompt wording
- **Demonstration optimization**: Selecting effective few-shot examples
- **Search strategies**: Exploring the prompt space efficiently

## Core Classes

## Optimizer

```python
Optimizer(metric: Optional[MetricWithLLM] = None, llm: Optional[BaseRagasLLM] = None)
```

Bases: `ABC`

Abstract base class for all optimizers.

### optimize

```python
optimize(dataset: SingleMetricAnnotation, loss: Loss, config: Dict[Any, Any], run_config: Optional[RunConfig] = None, batch_size: Optional[int] = None, callbacks: Optional[Callbacks] = None, with_debugging_logs=False, raise_exceptions: bool = True) -> Dict[str, str]
```

Optimizes the prompts for the given metric.

Parameters:

| Name         | Type                | Description                 | Default    |
| ------------ | ------------------- | --------------------------- | ---------- |
| `metric`     | `MetricWithLLM`     | The metric to optimize.     | *required* |
| `train_data` | `Any`               | The training data.          | *required* |
| `config`     | `InstructionConfig` | The training configuration. | *required* |

Returns:

| Type             | Description                            |
| ---------------- | -------------------------------------- |
| `Dict[str, str]` | The optimized prompts for given chain. |

Source code in `src/ragas/optimizers/base.py`

```python
@abstractmethod
def optimize(
    self,
    dataset: SingleMetricAnnotation,
    loss: Loss,
    config: t.Dict[t.Any, t.Any],
    run_config: t.Optional[RunConfig] = None,
    batch_size: t.Optional[int] = None,
    callbacks: t.Optional[Callbacks] = None,
    with_debugging_logs=False,
    raise_exceptions: bool = True,
) -> t.Dict[str, str]:
    """
    Optimizes the prompts for the given metric.

    Parameters
    ----------
    metric : MetricWithLLM
        The metric to optimize.
    train_data : Any
        The training data.
    config : InstructionConfig
        The training configuration.

    Returns
    -------
    Dict[str, str]
        The optimized prompts for given chain.
    """
    raise NotImplementedError("The method `optimize` must be implemented.")
```

## GeneticOptimizer

```python
GeneticOptimizer(metric: Optional[MetricWithLLM] = None, llm: Optional[BaseRagasLLM] = None)
```

Bases: `Optimizer`

A genetic algorithm optimizer that balances exploration and exploitation.

## DSPyOptimizer

```python
DSPyOptimizer(metric: Optional[MetricWithLLM] = None, llm: Optional[BaseRagasLLM] = None, num_candidates: int = 10, max_bootstrapped_demos: int = 5, max_labeled_demos: int = 5, init_temperature: float = 1.0, auto: Optional[Literal['light', 'medium', 'heavy']] = 'light', num_threads: Optional[int] = None, max_errors: Optional[int] = None, seed: int = 9, verbose: bool = False, track_stats: bool = True, log_dir: Optional[str] = None, metric_threshold: Optional[float] = None, cache: Optional[CacheInterface] = None)
```

Bases: `Optimizer`

Advanced prompt optimizer using DSPy's MIPROv2.

MIPROv2 performs sophisticated prompt optimization by combining:

- Instruction optimization (prompt engineering)
- Demonstration optimization (few-shot examples)
- Combined search over both spaces

Requires: pip install dspy-ai or uv add ragas[dspy]

Parameters:

| Name                     | Type             | Description                                                                                              | Default   |
| ------------------------ | ---------------- | -------------------------------------------------------------------------------------------------------- | --------- |
| `num_candidates`         | `int`            | Number of prompt variants to try during optimization.                                                    | `10`      |
| `max_bootstrapped_demos` | `int`            | Maximum number of auto-generated examples to use.                                                        | `5`       |
| `max_labeled_demos`      | `int`            | Maximum number of human-annotated examples to use.                                                       | `5`       |
| `init_temperature`       | `float`          | Exploration temperature for optimization.                                                                | `1.0`     |
| `auto`                   | `str`            | Automatic configuration level: 'light', 'medium', or 'heavy'. Controls the depth of optimization search. | `'light'` |
| `num_threads`            | `int`            | Number of parallel threads for optimization.                                                             | `None`    |
| `max_errors`             | `int`            | Maximum errors tolerated during optimization before stopping.                                            | `None`    |
| `seed`                   | `int`            | Random seed for reproducibility.                                                                         | `9`       |
| `verbose`                | `bool`           | Enable verbose logging during optimization.                                                              | `False`   |
| `track_stats`            | `bool`           | Track and report optimization statistics.                                                                | `True`    |
| `log_dir`                | `str`            | Directory for saving optimization logs and progress.                                                     | `None`    |
| `metric_threshold`       | `float`          | Minimum acceptable metric value to achieve.                                                              | `None`    |
| `cache`                  | `CacheInterface` | Cache backend for storing optimization results.                                                          | `None`    |

### optimize

```python
optimize(dataset: SingleMetricAnnotation, loss: Loss, config: Dict[Any, Any], run_config: Optional[RunConfig] = None, batch_size: Optional[int] = None, callbacks: Optional[Callbacks] = None, with_debugging_logs: bool = False, raise_exceptions: bool = True) -> Dict[str, str]
```

Optimize metric prompts using DSPy MIPROv2.

Steps:

1. Convert Ragas PydanticPrompt to DSPy Signature
1. Create DSPy Module with signature
1. Convert dataset to DSPy Examples
1. Run MIPROv2 optimization
1. Extract optimized prompts
1. Convert back to Ragas format

Parameters:

| Name                  | Type                     | Description                                      | Default    |
| --------------------- | ------------------------ | ------------------------------------------------ | ---------- |
| `dataset`             | `SingleMetricAnnotation` | Annotated dataset with ground truth scores.      | *required* |
| `loss`                | `Loss`                   | Loss function to optimize.                       | *required* |
| `config`              | `Dict[Any, Any]`         | Additional configuration parameters.             | *required* |
| `run_config`          | `RunConfig`              | Runtime configuration.                           | `None`     |
| `batch_size`          | `int`                    | Batch size for evaluation.                       | `None`     |
| `callbacks`           | `Callbacks`              | Langchain callbacks for tracking.                | `None`     |
| `with_debugging_logs` | `bool`                   | Enable debug logging.                            | `False`    |
| `raise_exceptions`    | `bool`                   | Whether to raise exceptions during optimization. | `True`     |

Returns:

| Type             | Description                             |
| ---------------- | --------------------------------------- |
| `Dict[str, str]` | Optimized prompts for each prompt name. |

Source code in `src/ragas/optimizers/dspy_optimizer.py`

```python
def optimize(
    self,
    dataset: SingleMetricAnnotation,
    loss: Loss,
    config: t.Dict[t.Any, t.Any],
    run_config: t.Optional[RunConfig] = None,
    batch_size: t.Optional[int] = None,
    callbacks: t.Optional[Callbacks] = None,
    with_debugging_logs: bool = False,
    raise_exceptions: bool = True,
) -> t.Dict[str, str]:
    """
    Optimize metric prompts using DSPy MIPROv2.

    Steps:

    1. Convert Ragas PydanticPrompt to DSPy Signature
    2. Create DSPy Module with signature
    3. Convert dataset to DSPy Examples
    4. Run MIPROv2 optimization
    5. Extract optimized prompts
    6. Convert back to Ragas format

    Parameters
    ----------
    dataset : SingleMetricAnnotation
        Annotated dataset with ground truth scores.
    loss : Loss
        Loss function to optimize.
    config : Dict[Any, Any]
        Additional configuration parameters.
    run_config : RunConfig, optional
        Runtime configuration.
    batch_size : int, optional
        Batch size for evaluation.
    callbacks : Callbacks, optional
        Langchain callbacks for tracking.
    with_debugging_logs : bool
        Enable debug logging.
    raise_exceptions : bool
        Whether to raise exceptions during optimization.

    Returns
    -------
    Dict[str, str]
        Optimized prompts for each prompt name.
    """
    if self.metric is None:
        raise ValueError("No metric provided for optimization.")

    if self.llm is None:
        raise ValueError("No llm provided for optimization.")

    if self._dspy is None:
        raise RuntimeError("DSPy module not loaded.")

    if self.cache is not None:
        cache_key = self._generate_cache_key(dataset, loss, config)
        if self.cache.has_key(cache_key):
            logger.info(
                f"Cache hit for DSPy optimization of metric: {self.metric.name}"
            )
            return self.cache.get(cache_key)

    logger.info(f"Starting DSPy optimization for metric: {self.metric.name}")

    from ragas.optimizers.dspy_adapter import (
        create_dspy_metric,
        pydantic_prompt_to_dspy_signature,
        ragas_dataset_to_dspy_examples,
        setup_dspy_llm,
    )

    setup_dspy_llm(self._dspy, self.llm)

    prompts = self.metric.get_prompts()
    optimized_prompts = {}

    for prompt_name, prompt in prompts.items():
        logger.info(f"Optimizing prompt: {prompt_name}")

        signature = pydantic_prompt_to_dspy_signature(prompt)
        module = self._dspy.Predict(signature)
        examples = ragas_dataset_to_dspy_examples(dataset, prompt_name)

        teleprompter = self._dspy.MIPROv2(
            num_candidates=self.num_candidates,
            max_bootstrapped_demos=self.max_bootstrapped_demos,
            max_labeled_demos=self.max_labeled_demos,
            init_temperature=self.init_temperature,
            auto=self.auto,
            num_threads=self.num_threads,
            max_errors=self.max_errors,
            seed=self.seed,
            verbose=self.verbose,
            track_stats=self.track_stats,
            log_dir=self.log_dir,
            metric_threshold=self.metric_threshold,
        )

        metric_fn = create_dspy_metric(loss, dataset.name)

        optimized = teleprompter.compile(
            module,
            trainset=examples,
            metric=metric_fn,
        )

        optimized_instruction = self._extract_instruction(optimized)
        optimized_prompts[prompt_name] = optimized_instruction

        logger.info(
            f"Optimized prompt for {prompt_name}: {optimized_instruction[:100]}..."
        )

    if self.cache is not None:
        cache_key = self._generate_cache_key(dataset, loss, config)
        self.cache.set(cache_key, optimized_prompts)
        logger.info("Cached optimization results")

    return optimized_prompts
```

## GeneticOptimizer

Simple evolutionary optimizer for prompt instructions.

### Parameters

| Parameter         | Type    | Default | Description                    |
| ----------------- | ------- | ------- | ------------------------------ |
| `max_steps`       | `int`   | 50      | Maximum evolution steps        |
| `population_size` | `int`   | 10      | Population size per generation |
| `mutation_rate`   | `float` | 0.2     | Probability of mutation        |

### Usage

```python
from ragas.optimizers import GeneticOptimizer
from ragas.config import InstructionConfig

optimizer = GeneticOptimizer(
    max_steps=50,
    population_size=10,
)

config = InstructionConfig(llm=llm, optimizer=optimizer)
metric.optimize_prompts(dataset, config)
```

### How it Works

1. Generates population of prompt variations
1. Evaluates each on annotated dataset
1. Selects best performers
1. Creates next generation via crossover and mutation
1. Repeats for max_steps iterations

**Pros**: Simple, works with limited data **Cons**: Slower convergence, instruction-only

## DSPyOptimizer

Advanced optimizer using DSPy's [MIPROv2](https://dspy.ai/api/optimizers/MIPROv2/) algorithm.

### Parameters

| Parameter                | Type    | Default | Description                       |
| ------------------------ | ------- | ------- | --------------------------------- |
| `num_candidates`         | `int`   | 10      | Number of prompt variants to try  |
| `max_bootstrapped_demos` | `int`   | 5       | Max auto-generated examples       |
| `max_labeled_demos`      | `int`   | 5       | Max human-annotated examples      |
| `init_temperature`       | `float` | 1.0     | Exploration temperature (0.0-2.0) |

### Usage

```python
from ragas.optimizers import DSPyOptimizer
from ragas.config import InstructionConfig

optimizer = DSPyOptimizer(
    num_candidates=10,
    max_bootstrapped_demos=5,
    max_labeled_demos=5,
)

config = InstructionConfig(llm=llm, optimizer=optimizer)
metric.optimize_prompts(dataset, config)
```

### How it Works

1. Generates candidate prompt instructions
1. Bootstraps few-shot demonstrations from data
1. Selects best human-annotated examples
1. Evaluates all combinations on dataset
1. Returns best-performing configuration

Learn more about DSPy concepts:

- [Signatures](https://dspy.ai/learn/programming/signatures/) - DSPy's approach to defining input/output specifications
- [Optimizers](https://dspy.ai/learn/optimization/optimizers/) - Algorithms for improving prompts and LM weights
- [Modules](https://dspy.ai/learn/programming/modules/) - Building blocks for LLM programs

**Pros**: Better results, combines instructions + demos **Cons**: Requires DSPy installation, more LLM calls

### Installation

[DSPy](https://dspy.ai/) is an optional dependency:

```bash
# Using uv (recommended)
uv add "ragas[dspy]"

# Using pip
pip install "ragas[dspy]"
```

### Cost Estimation

Approximate LLM calls per optimization:

```text
Total calls ≈ num_candidates × 30 + max_bootstrapped_demos × 7
```

Examples:

- Default config (10, 5, 5): ~335 calls
- Budget config (5, 2, 3): ~164 calls
- Aggressive config (20, 10, 10): ~670 calls

## Optimizer Base Class

Bases: `ABC`

Abstract base class for all optimizers.

## optimize

```python
optimize(dataset: SingleMetricAnnotation, loss: Loss, config: Dict[Any, Any], run_config: Optional[RunConfig] = None, batch_size: Optional[int] = None, callbacks: Optional[Callbacks] = None, with_debugging_logs=False, raise_exceptions: bool = True) -> Dict[str, str]
```

Optimizes the prompts for the given metric.

Parameters:

| Name         | Type                | Description                 | Default    |
| ------------ | ------------------- | --------------------------- | ---------- |
| `metric`     | `MetricWithLLM`     | The metric to optimize.     | *required* |
| `train_data` | `Any`               | The training data.          | *required* |
| `config`     | `InstructionConfig` | The training configuration. | *required* |

Returns:

| Type             | Description                            |
| ---------------- | -------------------------------------- |
| `Dict[str, str]` | The optimized prompts for given chain. |

## Configuration

Both optimizers are used with `InstructionConfig`:

```python
from ragas.config import InstructionConfig

config = InstructionConfig(
    llm=llm,                      # LLM for optimization
    optimizer=optimizer_instance, # Optimizer to use
)

# Use with metric
metric.optimize_prompts(dataset, config)
```

## Dataset Format

Optimizers require annotated datasets with ground truth scores:

```python
from ragas.dataset_schema import (
    PromptAnnotation,
    SampleAnnotation,
    SingleMetricAnnotation
)

# Create annotated sample
prompt_annotation = PromptAnnotation(
    prompt_input={"user_input": "...", "response": "..."},
    prompt_output={"score": 0.9},
    edited_output=None,  # Optional: corrected output
)

sample = SampleAnnotation(
    metric_input={"user_input": "...", "response": "..."},
    metric_output=0.9,  # Ground truth score
    prompts={"metric_prompt": prompt_annotation},
    is_accepted=True,  # Include in optimization
)

# Create dataset
dataset = SingleMetricAnnotation(
    name="metric_name",
    samples=[sample, ...]  # 20-50+ samples recommended
)
```

## Loss Functions

Optimizers use loss functions to evaluate prompt quality:

```python
from ragas.losses import MSELoss, HuberLoss

# Mean Squared Error (default)
loss = MSELoss()

# Huber Loss (robust to outliers)
loss = HuberLoss(delta=1.0)

# Use with config
config = InstructionConfig(llm=llm, optimizer=optimizer, loss=loss)
```

## Comparison

| Feature              | GeneticOptimizer   | DSPyOptimizer          |
| -------------------- | ------------------ | ---------------------- |
| Installation         | Built-in           | Requires `ragas[dspy]` |
| Optimization Target  | Instructions only  | Instructions + Demos   |
| Min Dataset Size     | 10+ samples        | 20+ samples            |
| Typical LLM Calls    | 100-500            | 200-700                |
| Accuracy Improvement | +5-8%              | +8-12%                 |
| Best For             | Quick optimization | Production metrics     |

## See Also

- [DSPy Optimizer Guide](https://docs.ragas.io/en/stable/references/howtos/customizations/optimizers/dspy-optimizer.md) - Detailed usage
- [Metric Customization](https://docs.ragas.io/en/stable/references/howtos/customizations/metrics/custom-metrics.md) - Creating metrics
- [Prompt API Reference](https://docs.ragas.io/en/stable/references/prompt/index.md) - Understanding prompts

## Additional Resources

**DSPy Documentation:**

- [DSPy Official Documentation](https://dspy.ai/) - Complete guide to DSPy
- [MIPROv2 API Reference](https://dspy.ai/api/optimizers/MIPROv2/) - Detailed MIPROv2 documentation
- [DSPy Optimizers Overview](https://dspy.ai/learn/optimization/optimizers/) - Guide to all DSPy optimizers
- [DSPy GitHub Repository](https://github.com/stanfordnlp/dspy) - Source code and examples

**Research Papers:**

- [Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs](https://arxiv.org/abs/2406.11695) - MIPROv2 paper
