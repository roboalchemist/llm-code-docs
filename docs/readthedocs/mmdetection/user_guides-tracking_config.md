# Learn about Configs

We use python files as our config system. You can find all the provided configs under $MMDetection/configs.

We incorporate modular and inheritance design into our config system,
which is convenient to conduct various experiments.
If you wish to inspect the config file,
you may run `python tools/misc/print_config.py /PATH/TO/CONFIG` to see the complete config.

## A brief description of a complete config

A complete config usually contains the following primary fields:

- 

`model`: the basic config of model, which may contain `data_preprocessor`, modules (e.g., `detector`, `motion`),`train_cfg`, `test_cfg`, etc.

- 

`train_dataloader`: the config of training dataloader, which usually contains `batch_size`, `num_workers`, `sampler`, `dataset`, etc.

- 

`val_dataloader`: the config of validation dataloader, which is similar with `train_dataloader`.

- 

`test_dataloader`: the config of testing dataloader, which is similar with `train_dataloader`.

- 

`val_evaluator`: the config of validation evaluator. For example,`type='MOTChallengeMetrics'` for MOT task on the MOTChallenge benchmarks.

- 

`test_evaluator`: the config of testing evaluator, which is similar with `val_evaluator`.

- 

`train_cfg`: the config of training loop. For example, `type='EpochBasedTrainLoop'`.

- 

`val_cfg`: the config of validation loop. For example, `type='VideoValLoop'`.

- 

`test_cfg`: the config of testing loop. For example, `type='VideoTestLoop'`.

- 

`default_hooks`: the config of default hooks, which may include hooks for timer, logger, param_scheduler, checkpoint, sampler_seed, visualization, etc.

- 

`vis_backends`: the config of visualization backends, which uses `type='LocalVisBackend'` as default.

- 

`visualizer`: the config of visualizer.  `type='TrackLocalVisualizer'` for MOT tasks.

- 

`param_scheduler`: the config of parameter scheduler, which usually sets the learning rate scheduler.

- 

`optim_wrapper`: the config of optimizer wrapper, which contains optimization-related information, for example optimizer, gradient clipping, etc.

- 

`load_from`: load models as a pre-trained model from a given path.

- 

`resume`: If `True`, resume checkpoints from `load_from`, and the training will be resumed from the epoch when the checkpoint is saved.