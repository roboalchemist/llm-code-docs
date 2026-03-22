# Source: https://huggingface.co/docs/timm/v1.0.25/reference/schedulers.md

# Learning Rate Schedulers

This page contains the API reference documentation for learning rate schedulers included in `timm`.

## Schedulers

### Factory functions[[timm.scheduler.create_scheduler]]

#### timm.scheduler.create_scheduler[[timm.scheduler.create_scheduler]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/scheduler_factory.py#L51)

#### timm.scheduler.create_scheduler_v2[[timm.scheduler.create_scheduler_v2]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/scheduler_factory.py#L63)

### Scheduler Classes[[timm.scheduler.CosineLRScheduler]]

#### timm.scheduler.CosineLRScheduler[[timm.scheduler.CosineLRScheduler]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/cosine_lr.py#L19)

Cosine decay with restarts.
This is described in the paper https://arxiv.org/abs/1608.03983.

Inspiration from
https://github.com/allenai/allennlp/blob/master/allennlp/training/learning_rate_schedulers/cosine.py

k-decay option based on `k-decay: A New Method For Learning Rate Schedule` - https://arxiv.org/abs/2004.05909

#### timm.scheduler.MultiStepLRScheduler[[timm.scheduler.MultiStepLRScheduler]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/multistep_lr.py#L10)

#### timm.scheduler.PlateauLRScheduler[[timm.scheduler.PlateauLRScheduler]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/plateau_lr.py#L13)

Decay the LR by a factor every time the validation loss plateaus.

#### timm.scheduler.PolyLRScheduler[[timm.scheduler.PolyLRScheduler]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/poly_lr.py#L19)

Polynomial LR Scheduler w/ warmup, noise, and k-decay

k-decay option based on `k-decay: A New Method For Learning Rate Schedule` - https://arxiv.org/abs/2004.05909

#### timm.scheduler.StepLRScheduler[[timm.scheduler.StepLRScheduler]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/step_lr.py#L15)

#### timm.scheduler.TanhLRScheduler[[timm.scheduler.TanhLRScheduler]]

[Source](https://github.com/huggingface/pytorch-image-models/blob/v1.0.25/timm/scheduler/tanh_lr.py#L19)

Hyberbolic-Tangent decay with restarts.
This is described in the paper https://arxiv.org/abs/1806.01593

