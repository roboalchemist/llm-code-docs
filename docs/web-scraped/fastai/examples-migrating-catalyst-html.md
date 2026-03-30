# Source: https://docs.fast.ai/examples/migrating_catalyst.html

Title: Catalyst with fastai – fastai

URL Source: https://docs.fast.ai/examples/migrating_catalyst.html

Markdown Content:
Catalyst with fastai – fastai
===============

[fastai](https://docs.fast.ai/index.html)

*   [](https://github.com/fastai/fastai)

[](https://docs.fast.ai/examples/migrating_catalyst.html "Toggle reader mode")

1.   [Tutorials](https://docs.fast.ai/tutorial.html)
2.   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_pytorch.html)
3.   [Catalyst with fastai](https://docs.fast.ai/examples/migrating_catalyst.html)

[](https://docs.fast.ai/examples/migrating_catalyst.html)

*   [Welcome to fastai](https://docs.fast.ai/index.html) 
*   [Quick start](https://docs.fast.ai/quick_start.html) 
*   [Tutorials](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Tutorials](https://docs.fast.ai/tutorial.html) 
    *   [Beginner](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
        *   [Computer vision intro](https://docs.fast.ai/tutorial.vision.html) 
        *   [Text transfer learning](https://docs.fast.ai/tutorial.text.html) 
        *   [Tabular training](https://docs.fast.ai/tutorial.tabular.html) 
        *   [Collaborative filtering tutorial](https://docs.fast.ai/tutorial.collab.html) 

    *   [Intermediate](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
        *   [Data block tutorial](https://docs.fast.ai/tutorial.datablock.html) 
        *   [Training Imagenette](https://docs.fast.ai/tutorial.imagenette.html) 
        *   [Mid-tier data API - Pets](https://docs.fast.ai/tutorial.pets.html) 
        *   [Chest X-ray model](https://docs.fast.ai/tutorial.medical_imaging.html) 
        *   [Transformers](https://docs.fast.ai/tutorial.transformers.html) 
        *   [Wikitext data tutorial](https://docs.fast.ai/tutorial.wikitext.html) 
        *   [Notebook distributed training](https://docs.fast.ai/tutorial.distributed.html) 

    *   [Advanced](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
        *   [Custom transforms](https://docs.fast.ai/tutorial.albumentations.html) 
        *   [Custom new task - siamese](https://docs.fast.ai/tutorial.siamese.html) 
        *   [Image sequences](https://docs.fast.ai/tutorial.image_sequence.html) 

    *   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
        *   [Pure PyTorch to fastai](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Pytorch to fastai details](https://docs.fast.ai/examples/migrating_pytorch_verbose.html) 
        *   [Ignite with fastai](https://docs.fast.ai/examples/migrating_ignite.html) 
        *   [Lightning with fastai](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Catalyst with fastai](https://docs.fast.ai/examples/migrating_catalyst.html) 

*   [Training](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Learner, Metrics, Callbacks](https://docs.fast.ai/learner.html) 
    *   [Optimizers](https://docs.fast.ai/optimizer.html) 
    *   [Metrics](https://docs.fast.ai/metrics.html) 
    *   [Interpretation of Predictions](https://docs.fast.ai/interpret.html) 
    *   [Distributed training](https://docs.fast.ai/distributed.html) 
    *   [Mixed precision training](https://docs.fast.ai/callback.fp16.html) 
    *   [Channels Last training](https://docs.fast.ai/callback.channelslast.html) 
    *   [Callbacks](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
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

*   [Data](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Data block](https://docs.fast.ai/data.block.html) 
    *   [Data core](https://docs.fast.ai/data.core.html) 
    *   [DataLoaders](https://docs.fast.ai/data.load.html) 
    *   [External data](https://docs.fast.ai/data.external.html) 
    *   [Data transformations](https://docs.fast.ai/data.transforms.html) 

*   [Core](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Torch Core](https://docs.fast.ai/torch_core.html) 
    *   [Layers](https://docs.fast.ai/layers.html) 
    *   [Loss Functions](https://docs.fast.ai/losses.html) 

*   [Vision](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Core vision](https://docs.fast.ai/vision.core.html) 
    *   [Vision data](https://docs.fast.ai/vision.data.html) 
    *   [Vision augmentation](https://docs.fast.ai/vision.augment.html) 
    *   [Vision learner](https://docs.fast.ai/vision.learner.html) 
    *   [Models](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
        *   [XResnet](https://docs.fast.ai/vision.models.xresnet.html) 
        *   [Dynamic UNet](https://docs.fast.ai/vision.models.unet.html) 

    *   [GAN](https://docs.fast.ai/vision.gan.html) 
    *   [Vision utils](https://docs.fast.ai/vision.utils.html) 
    *   [Vision widgets](https://docs.fast.ai/vision.widgets.html) 

*   [Text](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Text core](https://docs.fast.ai/text.core.html) 
    *   [Text data](https://docs.fast.ai/text.data.html) 
    *   [Text learner](https://docs.fast.ai/text.learner.html) 
    *   [Models](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
        *   [Core text modules](https://docs.fast.ai/text.models.core.html) 
        *   [AWD-LSTM](https://docs.fast.ai/text.models.awdlstm.html) 

*   [Tabular](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Tabular core](https://docs.fast.ai/tabular.core.html) 
    *   [Tabular data](https://docs.fast.ai/tabular.data.html) 
    *   [Tabular learner](https://docs.fast.ai/tabular.learner.html) 
    *   [Tabular model](https://docs.fast.ai/tabular.model.html) 
    *   [Collaborative filtering](https://docs.fast.ai/collab.html) 

*   [Medical](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Medical Imaging](https://docs.fast.ai/medical.imaging.html) 
    *   [Medical Text](https://docs.fast.ai/medical.text.html) 

*   [Integrations](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Wandb](https://docs.fast.ai/callback.wandb.html) 
    *   [Captum](https://docs.fast.ai/callback.captum.html) 
    *   [Comet.ml](https://docs.fast.ai/callback.comet.html) 
    *   [Tensorboard](https://docs.fast.ai/callback.tensorboard.html) 
    *   [Hugging Face Hub](https://docs.fast.ai/huggingface.html) 

*   [fastai Development](https://docs.fast.ai/examples/migrating_catalyst.html)[](https://docs.fast.ai/examples/migrating_catalyst.html) 
    *   [Pull requests made easy](https://docs.fast.ai/dev-setup.html) 
    *   [git Notes](https://docs.fast.ai/dev/git.html) 
    *   [fastai Abbreviation Guide](https://docs.fast.ai/dev/abbr.html) 
    *   [fastai coding style](https://docs.fast.ai/dev/style.html) 
    *   [Working with GPU](https://docs.fast.ai/dev/gpu.html) 
    *   [Notes For Developers](https://docs.fast.ai/dev/develop.html) 

On this page
------------

*   [Catalyst code](https://docs.fast.ai/examples/migrating_catalyst.html#catalyst-code)
    *   [Using callbacks](https://docs.fast.ai/examples/migrating_catalyst.html#using-callbacks)
    *   [Changing the model](https://docs.fast.ai/examples/migrating_catalyst.html#changing-the-model)

*   [Report an issue](https://github.com/fastai/fastai/issues/new)

Other Formats
-------------

*   [CommonMark](https://docs.fast.ai/examples/migrating_catalyst.html.md)

1.   [Tutorials](https://docs.fast.ai/tutorial.html)
2.   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_pytorch.html)
3.   [Catalyst with fastai](https://docs.fast.ai/examples/migrating_catalyst.html)

Catalyst with fastai
====================

 Incrementally adding fastai goodness to your Catalyst training 

`from fastai.vision.all import *`

Catalyst code
-------------

We’re going to use the MNIST training code from Catalyst’s README (as at August 2020), converted to a module.

 Note 

The source script for `migrating_catalyst` is in the `examples` subdirectory of this folder if you checked out the `fastai` repo from git, or can be downloaded from [here](https://github.com/fastai/fastai/blob/master/nbs/examples/migrating_catalyst.py) if you’re using an online viewer such as Colab.

`from migrating_catalyst import *`

To use it in fastai, we first convert the Catalyst dict into a [`DataLoaders`](https://docs.fast.ai/data.core.html#dataloaders) object:

`data = DataLoaders(loaders['train'], loaders['valid']).cuda()`

### Using callbacks

In the Catalyst code, a training loop is defined manually, which is where the input tensor is flattened. In fastai, there’s no need to define your own training loop - you can insert your own code into any part of the training process by using a callback, which can even modify data, gradients, the loss function, or anything else in the training loop:

```
@before_batch_cb
def cb(self, xb, yb): return (xb[0].view(xb[0].size(0), -1),),yb
```

The Catalyst example also modifies the training loop to add metrics, but you can pass these directly to your [`Learner`](https://docs.fast.ai/learner.html#learner) in fastai:

```
metrics=[accuracy,top_k_accuracy]
learn = Learner(data, model, loss_func=F.cross_entropy, opt_func=Adam,
                metrics=metrics, cbs=cb)
```

You can now fit your model. fastai supports many schedulers. We recommend using 1cycle:

`learn.fit_one_cycle(1, 0.02)`

| epoch | train_loss | valid_loss | accuracy | top_k_accuracy | time |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.230145 | 0.292590 | 0.924700 | 0.995000 | 00:13 |

As you can see, migrating from Catalyst allowed us to replace 17 lines of code (in `CustomRunner`) with just 3 lines, and doesn’t require you to change any of your existing data pipelines, optimizers, loss functions, models, etc. Once you’ve made this change, you can then benefit from fastai’s rich set of callbacks, transforms, visualizations, and so forth.

Note that fastai is very different from Catalyst, in that it is much more than just a training loop (although we’re only using the training loop in this example) - it is a complete framework including GPU-accelerated transformations, end-to-end inference, integrated applications for vision, text, tabular, and collaborative filtering, and so forth. You can use any part of the framework on its own, or combine them together, as described in the [fastai paper](https://arxiv.org/abs/2002.04688).

### Changing the model

Instead of using callbacks, in this case you can also simply change the model. Here we pull the `view()` out of the training loop, and into the model, using fastai’s [`Flatten`](https://docs.fast.ai/layers.html#flatten) layer:

```
model = nn.Sequential(
    Flatten(),
    torch.nn.Linear(28 * 28, 10))
```

We can now create a [`Learner`](https://docs.fast.ai/learner.html#learner) and train without using any callbacks:

```
learn = Learner(data, model, loss_func=F.cross_entropy, opt_func=Adam, metrics=metrics)
learn.fit_one_cycle(1, 0.02)
```

| epoch | train_loss | valid_loss | accuracy | top_k_accuracy | time |
| --- | --- | --- | --- | --- | --- |
| 0 | 0.230051 | 0.292577 | 0.924800 | 0.995100 | 00:11 |

*   [Report an issue](https://github.com/fastai/fastai/issues/new)
