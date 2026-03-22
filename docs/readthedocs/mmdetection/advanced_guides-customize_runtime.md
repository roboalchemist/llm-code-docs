# Customize Runtime Settings

## Customize optimization settings

Optimization related configuration is now all managed by `optim_wrapper` which usually has three fields: `optimizer`, `paramwise_cfg`, `clip_grad`, refer to OptimWrapper [https://mmengine.readthedocs.io/en/latest/tutorials/optim_wrapper.md] for more detail. See the example below, where `Adamw` is used as an `optimizer`, the learning rate of the backbone is reduced by a factor of 10, and gradient clipping is added.

```
optim_wrapper = dict(
    type='OptimWrapper',
    # optimizer
    optimizer=dict(
        type='AdamW',
        lr=0.0001,
        weight_decay=0.05,
        eps=1e-8,
        betas=(0.9, 0.999)),

    # Parameter-level learning rate and weight decay settings
    paramwise_cfg=dict(
        custom_keys={
            'backbone': dict(lr_mult=0.1, decay_mult=1.0),
        },
        norm_decay_mult=0.0),

    # gradient clipping
    clip_grad=dict(max_norm=0.01, norm_type=2))

```