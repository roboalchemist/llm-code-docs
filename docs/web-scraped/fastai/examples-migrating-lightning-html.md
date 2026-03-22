# Source: https://docs.fast.ai/examples/migrating_lightning.html

Title: Lightning with fastai – fastai

URL Source: https://docs.fast.ai/examples/migrating_lightning.html

Markdown Content:
Lightning with fastai – fastai
===============

[fastai](https://docs.fast.ai/index.html)

*   [](https://github.com/fastai/fastai)

[](https://docs.fast.ai/examples/migrating_lightning.html "Toggle reader mode")

1.   [Tutorials](https://docs.fast.ai/tutorial.html)
2.   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_pytorch.html)
3.   [Lightning with fastai](https://docs.fast.ai/examples/migrating_lightning.html)

[](https://docs.fast.ai/examples/migrating_lightning.html)

*   [Welcome to fastai](https://docs.fast.ai/index.html) 
*   [Quick start](https://docs.fast.ai/quick_start.html) 
*   [Tutorials](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Tutorials](https://docs.fast.ai/tutorial.html) 
    *   [Beginner](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Computer vision intro](https://docs.fast.ai/tutorial.vision.html) 
        *   [Text transfer learning](https://docs.fast.ai/tutorial.text.html) 
        *   [Tabular training](https://docs.fast.ai/tutorial.tabular.html) 
        *   [Collaborative filtering tutorial](https://docs.fast.ai/tutorial.collab.html) 

    *   [Intermediate](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Data block tutorial](https://docs.fast.ai/tutorial.datablock.html) 
        *   [Training Imagenette](https://docs.fast.ai/tutorial.imagenette.html) 
        *   [Mid-tier data API - Pets](https://docs.fast.ai/tutorial.pets.html) 
        *   [Chest X-ray model](https://docs.fast.ai/tutorial.medical_imaging.html) 
        *   [Transformers](https://docs.fast.ai/tutorial.transformers.html) 
        *   [Wikitext data tutorial](https://docs.fast.ai/tutorial.wikitext.html) 
        *   [Notebook distributed training](https://docs.fast.ai/tutorial.distributed.html) 

    *   [Advanced](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Custom transforms](https://docs.fast.ai/tutorial.albumentations.html) 
        *   [Custom new task - siamese](https://docs.fast.ai/tutorial.siamese.html) 
        *   [Image sequences](https://docs.fast.ai/tutorial.image_sequence.html) 

    *   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Pure PyTorch to fastai](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Pytorch to fastai details](https://docs.fast.ai/examples/migrating_pytorch_verbose.html) 
        *   [Ignite with fastai](https://docs.fast.ai/examples/migrating_ignite.html) 
        *   [Lightning with fastai](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Catalyst with fastai](https://docs.fast.ai/examples/migrating_catalyst.html) 

*   [Training](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Learner, Metrics, Callbacks](https://docs.fast.ai/learner.html) 
    *   [Optimizers](https://docs.fast.ai/optimizer.html) 
    *   [Metrics](https://docs.fast.ai/metrics.html) 
    *   [Interpretation of Predictions](https://docs.fast.ai/interpret.html) 
    *   [Distributed training](https://docs.fast.ai/distributed.html) 
    *   [Mixed precision training](https://docs.fast.ai/callback.fp16.html) 
    *   [Channels Last training](https://docs.fast.ai/callback.channelslast.html) 
    *   [Callbacks](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Callbacks](https://docs.fast.ai/callback.core.html) 
        *   [Model hooks](https://docs.fast.ai/callback.hook.html) 
        *   [Progress and logging](https://docs.fast.ai/callback.progress.html) 
        *   [Hyperparam schedule](https://docs.fast.ai/callback.schedule.html) 
        *   [Data Callbacks](https://docs.fast.ai/callback.data.html) 
        *   [MixUp and Friends](https://docs.fast.ai/callback.mixup.html) 
        *   [Predictions callbacks](https://docs.fast.ai/callback.preds.html) 
        *   [Callback for RNN training](https://docs.fast.ai/callback.rnn.html) 
        *   [Tracking callbacks](https://docs.fast.ai/callback.tracker.html) 
        *   [Training callbacks](https://docs.fast.ai/callback.training.html) 

*   [Data](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Data block](https://docs.fast.ai/data.block.html) 
    *   [Data core](https://docs.fast.ai/data.core.html) 
    *   [DataLoaders](https://docs.fast.ai/data.load.html) 
    *   [External data](https://docs.fast.ai/data.external.html) 
    *   [Data transformations](https://docs.fast.ai/data.transforms.html) 

*   [Core](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Torch Core](https://docs.fast.ai/torch_core.html) 
    *   [Layers](https://docs.fast.ai/layers.html) 
    *   [Loss Functions](https://docs.fast.ai/losses.html) 

*   [Vision](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Core vision](https://docs.fast.ai/vision.core.html) 
    *   [Vision data](https://docs.fast.ai/vision.data.html) 
    *   [Vision augmentation](https://docs.fast.ai/vision.augment.html) 
    *   [Vision learner](https://docs.fast.ai/vision.learner.html) 
    *   [Models](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [XResnet](https://docs.fast.ai/vision.models.xresnet.html) 
        *   [Dynamic UNet](https://docs.fast.ai/vision.models.unet.html) 

    *   [GAN](https://docs.fast.ai/vision.gan.html) 
    *   [Vision utils](https://docs.fast.ai/vision.utils.html) 
    *   [Vision widgets](https://docs.fast.ai/vision.widgets.html) 

*   [Text](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Text core](https://docs.fast.ai/text.core.html) 
    *   [Text data](https://docs.fast.ai/text.data.html) 
    *   [Text learner](https://docs.fast.ai/text.learner.html) 
    *   [Models](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Core text modules](https://docs.fast.ai/text.models.core.html) 
        *   [AWD-LSTM](https://docs.fast.ai/text.models.awdlstm.html) 

*   [Tabular](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Tabular core](https://docs.fast.ai/tabular.core.html) 
    *   [Tabular data](https://docs.fast.ai/tabular.data.html) 
    *   [Tabular learner](https://docs.fast.ai/tabular.learner.html) 
    *   [Tabular model](https://docs.fast.ai/tabular.model.html) 
    *   [Collaborative filtering](https://docs.fast.ai/collab.html) 

*   [Medical](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Medical Imaging](https://docs.fast.ai/medical.imaging.html) 
    *   [Medical Text](https://docs.fast.ai/medical.text.html) 

*   [Integrations](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Wandb](https://docs.fast.ai/callback.wandb.html) 
    *   [Captum](https://docs.fast.ai/callback.captum.html) 
    *   [Comet.ml](https://docs.fast.ai/callback.comet.html) 
    *   [Tensorboard](https://docs.fast.ai/callback.tensorboard.html) 
    *   [Hugging Face Hub](https://docs.fast.ai/huggingface.html) 

*   [fastai Development](https://docs.fast.ai/examples/migrating_lightning.html)[](https://docs.fast.ai/examples/migrating_lightning.html) 
    *   [Pull requests made easy](https://docs.fast.ai/dev-setup.html) 
    *   [git Notes](https://docs.fast.ai/dev/git.html) 
    *   [fastai Abbreviation Guide](https://docs.fast.ai/dev/abbr.html) 
    *   [fastai coding style](https://docs.fast.ai/dev/style.html) 
    *   [Working with GPU](https://docs.fast.ai/dev/gpu.html) 
    *   [Notes For Developers](https://docs.fast.ai/dev/develop.html) 

On this page
------------

*   [Using fastai’s training loop](https://docs.fast.ai/examples/migrating_lightning.html#using-fastais-training-loop)
    *   [Taking advantage of fastai Data Blocks](https://docs.fast.ai/examples/migrating_lightning.html#taking-advantage-of-fastai-data-blocks)

*   [Report an issue](https://github.com/fastai/fastai/issues/new)

Other Formats
-------------

*   [CommonMark](https://docs.fast.ai/examples/migrating_lightning.html.md)

1.   [Tutorials](https://docs.fast.ai/tutorial.html)
2.   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_pytorch.html)
3.   [Lightning with fastai](https://docs.fast.ai/examples/migrating_lightning.html)

Lightning with fastai
=====================

 Incrementally adding fastai goodness to your Lightning training 

We’re going to use the MNIST training code from Lightning’s ‘Quick Start’ (as at August 2020), converted to a module.

 Note 

The source script for `migrating_lightning` is in the `examples` subdirectory of this folder if you checked out the `fastai` repo from git, or can be downloaded from [here](https://github.com/fastai/fastai/blob/master/nbs/examples/migrating_lightning.py) if you’re using an online viewer such as Colab.

```
from migrating_lightning import *

from fastai.vision.all import *
```

Using fastai’s training loop
----------------------------

We can use the Lightning module directly:

`model = LitModel()`

To use it in fastai, we first pull the DataLoaders from the module into a [`DataLoaders`](https://docs.fast.ai/data.core.html#dataloaders) object:

`data = DataLoaders(model.train_dataloader(), model.val_dataloader()).cuda()`

We can now create a [`Learner`](https://docs.fast.ai/learner.html#learner) and fit:

```
learn = Learner(data, model, loss_func=F.cross_entropy, opt_func=Adam, metrics=accuracy)
learn.fit_one_cycle(1, 0.001)
```

| epoch | train_loss | valid_loss | accuracy | time |
| --- | --- | --- | --- | --- |
| 0 | 0.367197 | 0.333293 | 0.910800 | 00:11 |

As you can see, migrating from Lightning allowed us to reduce the amount of code, and doesn’t require you to change any of your existing data pipelines, optimizers, loss functions, models, etc. Once you’ve made this change, you can then benefit from fastai’s rich set of callbacks, transforms, visualizations, and so forth.

For instance, in the Lightning example, Tensorboard support was defined a special-case “logger”. In fastai, Tensorboard is just another [`Callback`](https://docs.fast.ai/callback.core.html#callback) that you can add, with the parameter `cbs=Tensorboard`, when you create your [`Learner`](https://docs.fast.ai/learner.html#learner). The callbacks all work together, so you can add an remove any schedulers, loggers, visualizers, and so forth. You don’t have to learn about special types of functionality for each - they are all just plain callbacks.

Note that fastai is very different from Lightning, in that it is much more than just a training loop (although we’re only using the training loop in this example) - it is a complete framework including GPU-accelerated transformations, end-to-end inference, integrated applications for vision, text, tabular, and collaborative filtering, and so forth. You can use any part of the framework on its own, or combine them together, as described in the [fastai paper](https://arxiv.org/abs/2002.04688).

### Taking advantage of fastai Data Blocks

One problem in the Lightning example is that it doesn’t actually use a validation set - it’s just using the training set a second time as a validation set.

You might prefer to use fastai’s Data Block API, which makes it really easy to create, visualize, and test your input data processing. Here’s how you can create input data for MNIST, for instance:

```
mnist = DataBlock(blocks=(ImageBlock(cls=PILImageBW), CategoryBlock), 
                  get_items=get_image_files, 
                  splitter=GrandparentSplitter(),
                  get_y=parent_label)
```

Here, we’re telling [`DataBlock`](https://docs.fast.ai/data.block.html#datablock) that we have a B&W image input, and a category output, our input items are file names of images, the images are labeled based on the name of the parent folder, and they are split by training vs validation based on the grandparent folder name. It’s important to actually look at your data, so fastai also makes it easy to visualize your inputs and outputs, for instance:

```
dls = mnist.dataloaders(untar_data(URLs.MNIST_TINY))
dls.show_batch(max_n=9, figsize=(4,4))
```

![Image 2](https://docs.fast.ai/examples/migrating_lightning_files/figure-html/cell-7-output-1.png)

*   [Report an issue](https://github.com/fastai/fastai/issues/new)
