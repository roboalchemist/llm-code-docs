# Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md

Title: NeMo Models — NVIDIA NeMo Framework User Guide

URL Source: https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html

Published Time: Thu, 30 Oct 2025 07:07:32 GMT

Markdown Content:
NeMo Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#nemo-models "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

Basics[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#basics "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

NeMo models contain everything needed to train and reproduce conversational AI models:

*   neural network architectures

*   datasets/data loaders

*   data preprocessing/postprocessing

*   data augmentors

*   optimizers and schedulers

*   tokenizers

*   language models

NeMo uses [Hydra](https://hydra.cc/) for configuring both NeMo models and the PyTorch Lightning Trainer.

Note

Every NeMo model has an example configuration file and training script that can be found [here](https://github.com/NVIDIA/NeMo/tree/stable/examples).

The end result of using NeMo, [Pytorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning), and Hydra is that NeMo models all have the same look and feel and are also fully compatible with the PyTorch ecosystem.

Pretrained[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#pretrained "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------

NeMo comes with many pretrained models for each of our collections: ASR, NLP, and TTS. Every pretrained NeMo model can be downloaded and used with the `from_pretrained()` method.

As an example, we can instantiate QuartzNet with the following:

import nemo.collections.asr as nemo_asr

model = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="QuartzNet15x5Base-En")

To see all available pretrained models for a specific NeMo model, use the `list_available_models()` method:

nemo_asr.models.EncDecCTCModel.list_available_models()

For detailed information on the available pretrained models, refer to the collections documentation:

*   [Automatic Speech Recognition (ASR)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md)

*   Natural Language Processing (NLP)

*   [Text-to-Speech Synthesis (TTS)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/intro.html.md)

Training[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#training "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------

NeMo leverages [PyTorch Lightning](https://www.pytorchlightning.ai/) for model training. PyTorch Lightning lets NeMo decouple the conversational AI code from the PyTorch training code. This means that NeMo users can focus on their domain (ASR, NLP, TTS) and build complex AI applications without having to rewrite boilerplate code for PyTorch training.

When using PyTorch Lightning, NeMo users can automatically train with:

*   multi-GPU/multi-node

*   mixed precision

*   model checkpointing

*   logging

*   early stopping

*   and more

The two main aspects of the Lightning API are the [LightningModule](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#) and the [Trainer](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html).

### PyTorch Lightning `LightningModule`[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#pytorch-lightning-lightningmodule "Link to this heading")

Every NeMo model is a `LightningModule` which is an `nn.module`. This means that NeMo models are compatible with the PyTorch ecosystem and can be plugged into existing PyTorch workflows.

Creating a NeMo model is similar to any other PyTorch workflow. We start by initializing our model architecture, then define the forward pass:

class TextClassificationModel(NLPModel, Exportable):
    ...
    def  __init__ (self, cfg: DictConfig, trainer: Trainer = None):
 """Initializes the BERTTextClassifier model."""
        ...
        super(). __init__ (cfg=cfg, trainer=trainer)

        # instantiate a BERT based encoder
        self.bert_model = get_lm_model(
            config_file=cfg.language_model.config_file,
            config_dict=cfg.language_model.config,
            vocab_file=cfg.tokenizer.vocab_file,
            trainer=trainer,
            cfg=cfg,
        )

        # instantiate the FFN for classification
        self.classifier = SequenceClassifier(
            hidden_size=self.bert_model.config.hidden_size,
            num_classes=cfg.dataset.num_classes,
            num_layers=cfg.classifier_head.num_output_layers,
            activation='relu',
            log_softmax=False,
            dropout=cfg.classifier_head.fc_dropout,
            use_transformer_init=True,
            idx_conditioned_on=0,
        )

def forward(self, input_ids, token_type_ids, attention_mask):
 """
 No special modification required for Lightning, define it as you normally would
 in the `nn.Module` in vanilla PyTorch.
 """
    hidden_states = self.bert_model(
        input_ids=input_ids, token_type_ids=token_type_ids, attention_mask=attention_mask
    )
    logits = self.classifier(hidden_states=hidden_states)
    return logits

The `LightningModule` organizes PyTorch code so that across all NeMo models we have a similar look and feel. For example, the training logic can be found in `training_step`:

def training_step(self, batch, batch_idx):
 """
 Lightning calls this inside the training loop with the data from the training dataloader
 passed in as `batch`.
 """
    # forward pass
    input_ids, input_type_ids, input_mask, labels = batch
    logits = self.forward(input_ids=input_ids, token_type_ids=input_type_ids, attention_mask=input_mask)

    train_loss = self.loss(logits=logits, labels=labels)

    lr = self._optimizer.param_groups[0]['lr']

    self.log('train_loss', train_loss)
    self.log('lr', lr, prog_bar=True)

    return {
        'loss': train_loss,
        'lr': lr,
    }

While validation logic can be found in `validation_step`:

def validation_step(self, batch, batch_idx):
 """
 Lightning calls this inside the validation loop with the data from the validation dataloader
 passed in as `batch`.
 """
    if self.testing:
        prefix = 'test'
    else:
        prefix = 'val'

    input_ids, input_type_ids, input_mask, labels = batch
    logits = self.forward(input_ids=input_ids, token_type_ids=input_type_ids, attention_mask=input_mask)

    val_loss = self.loss(logits=logits, labels=labels)

    preds = torch.argmax(logits, axis=-1)

    tp, fn, fp, _ = self.classification_report(preds, labels)

    return {'val_loss': val_loss, 'tp': tp, 'fn': fn, 'fp': fp}

PyTorch Lightning then handles all of the boilerplate code needed for training. Virtually any aspect of training can be customized via PyTorch Lightning [hooks](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#hooks), [Plugins](https://pytorch-lightning.readthedocs.io/en/stable/extensions/plugins.html), [callbacks](https://pytorch-lightning.readthedocs.io/en/stable/extensions/callbacks.html), or by overriding [methods](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#methods).

For more domain-specific information, see:

*   [Automatic Speech Recognition (ASR)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md)

*   Natural Language Processing (NLP)

*   [Text-to-Speech Synthesis (TTS)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/intro.html.md)

### PyTorch Lightning Trainer[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#pytorch-lightning-trainer "Link to this heading")

Since every NeMo model is a `LightningModule`, we can automatically take advantage of the PyTorch Lightning `Trainer`. Every NeMo [example](https://github.com/NVIDIA/NeMo/tree/v1.0.2/examples) training script uses the `Trainer` object to fit the model.

First, instantiate the model and trainer, then call `.fit`:

# We first instantiate the trainer based on the model configuration.
# See the model configuration documentation for details.
trainer = pl.Trainer(**cfg.trainer)

# Then pass the model configuration and trainer object into the NeMo model
model = TextClassificationModel(cfg.model, trainer=trainer)

# Now we can train with by calling .fit
trainer.fit(model)

# Or we can run the test loop on test data by calling
trainer.test(model=model)

All [trainer flags](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html#trainer-flags) can be set from from the NeMo configuration.

Configuration[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------

Hydra is an open-source Python framework that simplifies configuration for complex applications that must bring together many different software libraries. Conversational AI model training is a great example of such an application. To train a conversational AI model, we must be able to configure:

*   neural network architectures

*   training and optimization algorithms

*   data pre/post processing

*   data augmentation

*   experiment logging/visualization

*   model checkpointing

For an introduction to using Hydra, refer to the [Hydra Tutorials](https://hydra.cc/docs/tutorials/intro).

With Hydra, we can configure everything needed for NeMo with three interfaces:

*   Command Line (CLI)

*   Configuration Files (YAML)

*   Dataclasses (Python)

### YAML[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#yaml "Link to this heading")

NeMo provides YAML configuration files for all of our [example](https://github.com/NVIDIA/NeMo/tree/v1.0.2/examples) training scripts. YAML files make it easy to experiment with different model and training configurations.

Every NeMo example YAML has the same underlying configuration structure:

*   trainer

*   exp_manager

*   model

The model configuration always contains `train_ds`, `validation_ds`, `test_ds`, and `optim`. Model architectures, however, can vary across domains. Refer to the documentation of specific collections (LLM, ASR etc.) for detailed information on model architecture configuration.

A NeMo configuration file should look similar to the following:

# PyTorch Lightning Trainer configuration
# any argument of the Trainer object can be set here
trainer:
 devices: 1 # number of gpus per node
 accelerator: gpu
 num_nodes: 1 # number of nodes
 max_epochs: 10 # how many training epochs to run
 val_check_interval: 1.0 # run validation after every epoch

# Experiment logging configuration
exp_manager:
 exp_dir: /path/to/my/nemo/experiments
 name: name_of_my_experiment
 create_tensorboard_logger: True
 create_wandb_logger: True

# Model configuration
# model network architecture, train/val/test datasets, data augmentation, and optimization
model:
 train_ds:
 manifest_filepath: /path/to/my/train/manifest.json
 batch_size: 256
 shuffle: True
 validation_ds:
 manifest_filepath: /path/to/my/validation/manifest.json
 batch_size: 32
 shuffle: False
 test_ds:
 manifest_filepath: /path/to/my/test/manifest.json
 batch_size: 32
 shuffle: False
 optim:
 name: novograd
 lr: .01
 betas: [0.8, 0.5]
 weight_decay: 0.001
 # network architecture can vary greatly depending on the domain
 encoder:
 ...
 decoder:
 ...

### CLI[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#cli "Link to this heading")

With NeMo and Hydra, every aspect of model training can be modified from the command-line. This is extremely helpful for running lots of experiments on compute clusters or for quickly testing parameters during development.

All NeMo [examples](https://github.com/NVIDIA/NeMo/tree/stable/examples) come with instructions on how to run the training/inference script from the command-line (e.g. see [here](https://github.com/NVIDIA/NeMo/blob/stable/examples/asr/asr_ctc/speech_to_text_ctc.py) for an example).

With Hydra, arguments are set using the `=` operator:

python examples/asr/asr_ctc/speech_to_text_ctc.py \
 model.train_ds.manifest_filepath=/path/to/my/train/manifest.json \
 model.validation_ds.manifest_filepath=/path/to/my/validation/manifest.json \
 trainer.devices=2 \
 trainer.accelerator='gpu' \
 trainer.max_epochs=50

We can use the `+` operator to add arguments from the CLI:

python examples/asr/asr_ctc/speech_to_text_ctc.py \
 model.train_ds.manifest_filepath=/path/to/my/train/manifest.json \
 model.validation_ds.manifest_filepath=/path/to/my/validation/manifest.json \
 trainer.devices=2 \
 trainer.accelerator='gpu' \
 trainer.max_epochs=50 \
 +trainer.fast_dev_run=true

We can use the `~` operator to remove configurations:

python examples/asr/asr_ctc/speech_to_text_ctc.py \
 model.train_ds.manifest_filepath=/path/to/my/train/manifest.json \
 model.validation_ds.manifest_filepath=/path/to/my/validation/manifest.json \
 ~model.test_ds \
 trainer.devices=2 \
 trainer.accelerator='gpu' \
 trainer.max_epochs=50 \
 +trainer.fast_dev_run=true

We can specify configuration files using the `--config-path` and `--config-name` flags:

python examples/asr/asr_ctc/speech_to_text_ctc.py \
 --config-path=conf/quartznet \
 --config-name=quartznet_15x5 \
 model.train_ds.manifest_filepath=/path/to/my/train/manifest.json \
 model.validation_ds.manifest_filepath=/path/to/my/validation/manifest.json \
 ~model.test_ds \
 trainer.devices=2 \
 trainer.accelerator='gpu' \
 trainer.max_epochs=50 \
 +trainer.fast_dev_run=true

### Dataclasses[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#dataclasses "Link to this heading")

Dataclasses allow NeMo to ship model configurations as part of the NeMo library and also enables pure Python configuration of NeMo models. With Hydra, dataclasses can be used to create [structured configs](https://hydra.cc/docs/tutorials/structured_config/intro) for the conversational AI application.

As an example, refer to the code block below for an _Attenion is All You Need_ machine translation model. The model configuration can be instantiated and modified like any Python [Dataclass](https://docs.python.org/3/library/dataclasses.html).

from nemo.collections.nlp.models.machine_translation.mt_enc_dec_config import AAYNBaseConfig

cfg = AAYNBaseConfig()

# modify the number of layers in the encoder
cfg.encoder.num_layers = 8

# modify the training batch size
cfg.train_ds.tokens_in_batch = 8192

Note

Configuration with Hydra always has the following precedence CLI > YAML > Dataclass.

Optimization[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#optimization "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

Optimizers and learning rate schedules are configurable across all NeMo models and have their own namespace. Here is a sample YAML configuration for a Novograd optimizer with a Cosine Annealing learning rate schedule.

optim:
 name: novograd
 lr: 0.01

 # optimizer arguments
 betas: [0.8, 0.25]
 weight_decay: 0.001

 # scheduler setup
 sched:
 name: CosineAnnealing

 # Optional arguments
 max_steps: -1 # computed at runtime or explicitly set here
 monitor: val_loss
 reduce_on_plateau: false

 # scheduler config override
 warmup_steps: 1000
 warmup_ratio: null
 min_lr: 1e-9:

Note

[NeMo Examples](https://github.com/NVIDIA/NeMo/tree/stable/examples) has optimizer and scheduler configurations for every NeMo model.

Optimizers can be configured from the CLI as well:

python examples/asr/asr_ctc/speech_to_text_ctc.py \
 --config-path=conf/quartznet \
 --config-name=quartznet_15x5 \
 ...
 # train with the adam optimizer
 model.optim=adam \
 # change the learning rate
 model.optim.lr=.0004 \
 # modify betas
 model.optim.betas=[.8, .5]

### Optimizers[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#optimizers "Link to this heading")

`name` corresponds to the lowercase name of the optimizer. To view a list of available optimizers, run:

from nemo.core.optim.optimizers import AVAILABLE_OPTIMIZERS

for name, opt in AVAILABLE_OPTIMIZERS.items():
    print(f'name: {name}, opt: {opt}')

name: sgd opt: <class 'torch.optim.sgd.SGD'>
name: adam opt: <class 'torch.optim.adam.Adam'>
name: adamw opt: <class 'torch.optim.adamw.AdamW'>
name: adadelta opt: <class 'torch.optim.adadelta.Adadelta'>
name: adamax opt: <class 'torch.optim.adamax.Adamax'>
name: adagrad opt: <class 'torch.optim.adagrad.Adagrad'>
name: rmsprop opt: <class 'torch.optim.rmsprop.RMSprop'>
name: rprop opt: <class 'torch.optim.rprop.Rprop'>
name: novograd opt: <class 'nemo.core.optim.novograd.Novograd'>

### Optimizer Params[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#optimizer-params "Link to this heading")

Optimizer params can vary between optimizers but the `lr` param is required for all optimizers. To see the available params for an optimizer, we can look at its corresponding dataclass.

from nemo.core.config.optimizers import NovogradParams

print(NovogradParams())

NovogradParams(lr='???', betas=(0.95, 0.98), eps=1e-08, weight_decay=0, grad_averaging=False, amsgrad=False, luc=False, luc_trust=0.001, luc_eps=1e-08)

`'???'` indicates that the lr argument is required.

### Register Optimizer[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#register-optimizer "Link to this heading")

To register a new optimizer to be used with NeMo, run:

nemo.core.optim.optimizers.register_optimizer(_name:str_,_optimizer:torch.optim.optimizer.Optimizer_,_optimizer\_params:OptimizerParams_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#nemo.core.optim.optimizers.register_optimizer "Link to this definition")
Checks if the optimizer name exists in the registry, and if it doesnt, adds it.

This allows custom optimizers to be added and called by name during instantiation.

Parameters:
*   **name** – Name of the optimizer. Will be used as key to retrieve the optimizer.

*   **optimizer** – Optimizer class

*   **optimizer_params** – The parameters as a dataclass of the optimizer

### Learning Rate Schedulers[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#learning-rate-schedulers "Link to this heading")

Learning rate schedulers can be optionally configured under the `optim.sched` namespace.

`name` corresponds to the name of the learning rate schedule. To view a list of available schedulers, run:

from nemo.core.optim.lr_scheduler import AVAILABLE_SCHEDULERS

for name, opt in AVAILABLE_SCHEDULERS.items():
    print(f'name: {name}, schedule: {opt}')

name: WarmupPolicy, schedule: <class 'nemo.core.optim.lr_scheduler.WarmupPolicy'>
name: WarmupHoldPolicy, schedule: <class 'nemo.core.optim.lr_scheduler.WarmupHoldPolicy'>
name: SquareAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.SquareAnnealing'>
name: CosineAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.CosineAnnealing'>
name: NoamAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.NoamAnnealing'>
name: WarmupAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.WarmupAnnealing'>
name: InverseSquareRootAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.InverseSquareRootAnnealing'>
name: SquareRootAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.SquareRootAnnealing'>
name: PolynomialDecayAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.PolynomialDecayAnnealing'>
name: PolynomialHoldDecayAnnealing, schedule: <class 'nemo.core.optim.lr_scheduler.PolynomialHoldDecayAnnealing'>
name: StepLR, schedule: <class 'torch.optim.lr_scheduler.StepLR'>
name: ExponentialLR, schedule: <class 'torch.optim.lr_scheduler.ExponentialLR'>
name: ReduceLROnPlateau, schedule: <class 'torch.optim.lr_scheduler.ReduceLROnPlateau'>
name: CyclicLR, schedule: <class 'torch.optim.lr_scheduler.CyclicLR'>

### Scheduler Params[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#scheduler-params "Link to this heading")

To see the available params for a scheduler, we can look at its corresponding dataclass:

from nemo.core.config.schedulers import CosineAnnealingParams

print(CosineAnnealingParams())

CosineAnnealingParams(last_epoch=-1, warmup_steps=None, warmup_ratio=None, min_lr=0.0)

### Register scheduler[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#register-scheduler "Link to this heading")

To register a new scheduler to be used with NeMo, run:

nemo.core.optim.lr_scheduler.register_scheduler(_name:str_,_scheduler:torch.optim.lr\_scheduler.\_LRScheduler_,_scheduler\_params:SchedulerParams_,)[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#nemo.core.optim.lr_scheduler.register_scheduler "Link to this definition")
Checks if the scheduler name exists in the registry, and if it doesnt, adds it.

This allows custom schedulers to be added and called by name during instantiation.

Parameters:
*   **name** – Name of the optimizer. Will be used as key to retrieve the optimizer.

*   **scheduler** – Scheduler class (inherits from _LRScheduler)

*   **scheduler_params** – The parameters as a dataclass of the scheduler

Save and Restore[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#save-and-restore "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------

NeMo models all come with `.save_to` and `.restore_from` methods.

### Save[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#save "Link to this heading")

To save a NeMo model, run:

model.save_to('/path/to/model.nemo')

Everything needed to use the trained model is packaged and saved in the `.nemo` file. For example, in the NLP domain, `.nemo` files include the necessary tokenizer models and/or vocabulary files, etc.

Note

A `.nemo` file is simply an archive like any other `.tar` file.

### Restore[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#restore "Link to this heading")

To restore a NeMo model, run:

# Here, you should usually use the class of the model, or simply use ModelPT.restore_from() for simplicity.
model.restore_from('/path/to/model.nemo')

When using the PyTorch Lightning Trainer, a PyTorch Lightning checkpoint is created. These are mainly used within NeMo to auto-resume training. Since NeMo models are `LightningModules`, the PyTorch Lightning method `load_from_checkpoint` is available. Note that `load_from_checkpoint` won’t necessarily work out-of-the-box for all models as some models require more artifacts than just the checkpoint to be restored. For these models, the user will have to override `load_from_checkpoint` if they want to use it.

It’s highly recommended to use `restore_from` to load NeMo models.

### Restore with Modified Config[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#restore-with-modified-config "Link to this heading")

Sometimes, there may be a need to modify the model (or it’s sub-components) prior to restoring a model. A common case is when the model’s internal config must be updated due to various reasons (such as deprecation, newer versioning, support a new feature). As long as the model has the same parameters as compared to the original config, the parameters can once again be restored safely.

In NeMo, as part of the .nemo file, the model’s internal config will be preserved. This config is used during restoration, and as shown below we can update this config prior to restoring the model.

# When restoring a model, you should generally use the class of the model
# Obtain the config (as an OmegaConf object)
config = model_class.restore_from('/path/to/model.nemo', return_config=True)
# OR
config = model_class.from_pretrained('name_of_the_model', return_config=True)

# Modify the config as needed
config.x.y = z

# Restore the model from the updated config
model = model_class.restore_from('/path/to/model.nemo', override_config_path=config)
# OR
model = model_class.from_pretrained('name_of_the_model', override_config_path=config)

Register Artifacts[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#register-artifacts "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

Restoring conversational AI models can be complicated because it requires more than just the checkpoint weights; additional information is also needed to use the model. NeMo models can save additional artifacts in the .nemo file by calling `.register_artifact`. When restoring NeMo models using `.restore_from` or `.from_pretrained`, any artifacts that were registered will be available automatically.

As an example, consider an NLP model that requires a trained tokenizer model. The tokenizer model file can be automatically added to the .nemo file with the following:

self.encoder_tokenizer = get_nmt_tokenizer(
    ...
    tokenizer_model=self.register_artifact(config_path='encoder_tokenizer.tokenizer_model',
                                           src='/path/to/tokenizer.model',
                                           verify_src_exists=True),
)

By default, `.register_artifact` will always return a path. If the model is being restored from a .nemo file, then that path will be to the artifact in the .nemo file. Otherwise, `.register_artifact` will return the local path specified by the user.

`config_path` is the artifact key. It usually corresponds to a model configuration but does not have to. The model config that is packaged with the .nemo file will be updated according to the `config_path` key. In the above example, the model config will have

encoder_tokenizer:
 ...
 tokenizer_model: nemo:4978b28103264263a03439aaa6560e5e_tokenizer.model

`src` is the path to the artifact and the base-name of the path will be used when packaging the artifact in the .nemo file. Each artifact will have a hash prepended to the basename of `src` in the .nemo file. This is to prevent collisions with basenames base-names that are identical (say when there are two or more tokenizers, both called tokenizer.model). The resulting .nemo file will then have the following file:

4978b28103264263a03439aaa6560e5e_tokenizer.model

If `verify_src_exists` is set to `False`, then the artifact is optional. This means that `.register_artifact` will return `None` if the `src` cannot be found.

Push to Hugging Face Hub[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#push-to-hugging-face-hub "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------

NeMo models can be pushed to the [Hugging Face Hub](https://huggingface.co/) with the [`push_to_hf_hub()`](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO.push_to_hf_hub "nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO.push_to_hf_hub") method. This method performs the same actions as `save_to()` and then uploads the model to the HuggingFace Hub. It offers an additional `pack_nemo_file` argument that allows the user to upload the entire NeMo file or just the `.nemo` file. This is useful for large language models that have a massive number of parameters, and a single NeMo file could exceed the max upload size of Hugging Face Hub.

### Upload a model to the Hub[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#upload-a-model-to-the-hub "Link to this heading")

token = "<HF TOKEN>" or None
pack_nemo_file = True  # False will upload multiple files that comprise the NeMo file onto HF Hub; Generally useful for LLMs

model.push_to_hf_hub(
   repo_id=repo_id, pack_nemo_file=pack_nemo_file, token=token,
)

### Use a Custom Model Card Template for the Hub[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#use-a-custom-model-card-template-for-the-hub "Link to this heading")

# Override the default model card
template = """ <Your own custom template>
# {model_name}
"""
kwargs = {"model_name": "ABC", "repo_id": "nvidia/ABC_XYZ"}
model_card = model.generate_model_card(template=template, template_kwargs=kwargs, type="hf")

model.push_to_hf_hub(
    repo_id=repo_id, token=token, model_card=model_card
)

# Write your own model card class
class MyModelCard:
  def  __init__ (self, model_name):
    self.model_name = model_name

  def  __repr__ (self):
    template = """This is the {model_name} model""".format(model_name=self.model_name)
    return template

model.push_to_hf_hub(
    repo_id=repo_id, token=token, model_card=MyModelCard("ABC")
)

Nested NeMo Models[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#nested-nemo-models "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------

In some cases, it may be helpful to use NeMo models inside other NeMo models. For example, we can incorporate language models into ASR models to use in a decoding process to improve accuracy or use hybrid ASR-TTS models to generate audio from the text on the fly to train or fine-tune the ASR model.

There are three ways to instantiate child models inside parent models:

*   use subconfig directly

*   use the `.nemo` checkpoint path to load the child model

*   use a pretrained NeMo model

To register a child model, use the `register_nemo_submodule` method of the parent model. This method will add the child model to a specified model attribute. During serialization, it will correctly handle child artifacts and store the child model’s configuration in the parent model’s `config_field`.

from nemo.core.classes import ModelPT

class ChildModel(ModelPT):
    ...  # implement necessary methods

class ParentModel(ModelPT):
    def  __init__ (self, cfg, trainer=None):
        super(). __init__ (cfg=cfg, trainer=trainer)

        # optionally annotate type for IDE autocompletion and type checking
        self.child_model: Optional[ChildModel]
        if cfg.get("child_model") is not None:
            # load directly from config
            # either if config provided initially, or automatically
            # after model restoration
            self.register_nemo_submodule(
                name="child_model",
                config_field="child_model",
                model=ChildModel(self.cfg.child_model, trainer=trainer),
            )
        elif cfg.get('child_model_path') is not None:
            # load from .nemo model checkpoint
            # while saving, config will be automatically assigned/updated
            # in cfg.child_model
            self.register_nemo_submodule(
                name="child_model",
                config_field="child_model",
                model=ChildModel.restore_from(self.cfg.child_model_path, trainer=trainer),
            )
        elif cfg.get('child_model_name') is not None:
            # load from pretrained model
            # while saving, config will be automatically assigned/updated
            # in cfg.child_model
            self.register_nemo_submodule(
                name="child_model",
                config_field="child_model",
                model=ChildModel.from_pretrained(self.cfg.child_model_name, trainer=trainer),
            )
        else:
            self.child_model = None

Profiling[#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#profiling "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

NeMo offers users two options for profiling: Nsys and CUDA memory profiling. These two options allow users to debug performance issues as well as memory issues such as memory leaks.

To enable Nsys profiling, add the following options to the model config:

nsys_profile: False
 start_step: 10 # Global batch to start profiling
 end_step: 10 # Global batch to end profiling
 ranks: [0] # Global rank IDs to profile
 gen_shape: False # Generate model and kernel details including input shapes

Finally, run the model training script with:

nsys profile -s none -o <profile filepath> -t cuda,nvtx --force-overwrite true --capture-range=cudaProfilerApi --capture-range-end=stop python ./examples/...

See more options at [nsight user guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html.md#cli-profiling).

To enable CUDA memory profiling, add the following options to the model config:

memory_profile:
 enabled: True
 start_step: 10 # Global batch to start profiling
 end_step: 10 # Global batch to end profiling
 rank: 0 # Global rank ID to profile
 output_path: None # Path to store the profile output file

Then invoke your NeMo script without any changes in the invocation command.

Links/Buttons:
- [#](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/core.html.md#profiling)
- [Hydra](https://hydra.cc/)
- [here](https://github.com/NVIDIA/NeMo/blob/stable/examples/asr/asr_ctc/speech_to_text_ctc.py)
- [Pytorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning)
- [Automatic Speech Recognition (ASR)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/asr/intro.html.md)
- [Text-to-Speech Synthesis (TTS)](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/tts/intro.html.md)
- [PyTorch Lightning](https://www.pytorchlightning.ai/)
- [LightningModule](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#)
- [Trainer](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html)
- [hooks](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#hooks)
- [Plugins](https://pytorch-lightning.readthedocs.io/en/stable/extensions/plugins.html)
- [callbacks](https://pytorch-lightning.readthedocs.io/en/stable/extensions/callbacks.html)
- [methods](https://pytorch-lightning.readthedocs.io/en/stable/common/lightning_module.html#methods)
- [example](https://github.com/NVIDIA/NeMo/tree/v1.0.2/examples)
- [trainer flags](https://pytorch-lightning.readthedocs.io/en/stable/common/trainer.html#trainer-flags)
- [Hydra Tutorials](https://hydra.cc/docs/tutorials/intro)
- [structured configs](https://hydra.cc/docs/tutorials/structured_config/intro)
- [Dataclass](https://docs.python.org/3/library/dataclasses.html)
- [Hugging Face Hub](https://huggingface.co/)
- [push_to_hf_hub()](https://docs.nvidia.com/nemo-framework/user-guide/latest/nemotoolkit/core/api.html.md#nemo.core.classes.mixins.hf_io_mixin.HuggingFaceFileIO.push_to_hf_hub)
- [nsight user guide](https://docs.nvidia.com/nsight-systems/UserGuide/index.html.md#cli-profiling)
