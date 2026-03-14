# Source: https://unsloth.ai/docs/fr/notions-de-base/finetuning-from-last-checkpoint.md

# Source: https://unsloth.ai/docs/de/grundlagen/finetuning-from-last-checkpoint.md

# Source: https://unsloth.ai/docs/jp/ji-ben/finetuning-from-last-checkpoint.md

# Source: https://unsloth.ai/docs/zh/ji-chu-zhi-shi/finetuning-from-last-checkpoint.md

# Source: https://unsloth.ai/docs/basics/finetuning-from-last-checkpoint.md

# Finetuning from Last Checkpoint

You must edit the `Trainer` first to add `save_strategy` and `save_steps`. Below saves a checkpoint every 50 steps to the folder `outputs`.

```python
trainer = SFTTrainer(
    ....
    args = TrainingArguments(
        ....
        output_dir = "outputs",
        save_strategy = "steps",
        save_steps = 50,
    ),
)
```

Then in the trainer do:

```python
trainer_stats = trainer.train(resume_from_checkpoint = True)
```

Which will start from the latest checkpoint and continue training.

### Wandb Integration

```
# Install library
!pip install wandb --upgrade

# Setting up Wandb
!wandb login <token>

import os

os.environ["WANDB_PROJECT"] = "<name>"
os.environ["WANDB_LOG_MODEL"] = "checkpoint"
```

Then in `TrainingArguments()` set

```
report_to = "wandb",
logging_steps = 1, # Change if needed
save_steps = 100 # Change if needed
run_name = "<name>" # (Optional)
```

To train the model, do `trainer.train()`; to resume training, do

```
import wandb
run = wandb.init()
artifact = run.use_artifact('<username>/<Wandb-project-name>/<run-id>', type='model')
artifact_dir = artifact.download()
trainer.train(resume_from_checkpoint=artifact_dir)
```

## :question:How do I do Early Stopping?

If you want to stop or pause the finetuning / training run since the evaluation loss is not decreasing, then you can use early stopping which stops the training process. Use `EarlyStoppingCallback`.

As usual, set up your trainer and your evaluation dataset. The below is used to stop the training run if the `eval_loss` (the evaluation loss) is not decreasing after 3 steps or so.

```python
from trl import SFTConfig, SFTTrainer
trainer = SFTTrainer(
    args = SFTConfig(
        fp16_full_eval = True,
        per_device_eval_batch_size = 2,
        eval_accumulation_steps = 4,
        output_dir = "training_checkpoints", # location of saved checkpoints for early stopping
        save_strategy = "steps",             # save model every N steps
        save_steps = 10,                     # how many steps until we save the model
        save_total_limit = 3,                # keep ony 3 saved checkpoints to save disk space
        eval_strategy = "steps",             # evaluate every N steps
        eval_steps = 10,                     # how many steps until we do evaluation
        load_best_model_at_end = True,       # MUST USE for early stopping
        metric_for_best_model = "eval_loss", # metric we want to early stop on
        greater_is_better = False,           # the lower the eval loss, the better
    ),
    model = model,
    tokenizer = tokenizer,
    train_dataset = new_dataset["train"],
    eval_dataset = new_dataset["test"],
)
```

We then add the callback which can also be customized:

```python
from transformers import EarlyStoppingCallback
early_stopping_callback = EarlyStoppingCallback(
    early_stopping_patience = 3,     # How many steps we will wait if the eval loss doesn't decrease
                                     # For example the loss might increase, but decrease after 3 steps
    early_stopping_threshold = 0.0,  # Can set higher - sets how much loss should decrease by until
                                     # we consider early stopping. For eg 0.01 means if loss was
                                     # 0.02 then 0.01, we consider to early stop the run.
)
trainer.add_callback(early_stopping_callback)
```

Then train the model as usual via `trainer.train() .`
