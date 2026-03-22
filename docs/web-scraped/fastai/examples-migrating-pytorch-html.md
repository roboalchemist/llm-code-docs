# Source: https://docs.fast.ai/examples/migrating_pytorch.html

Title: Pure PyTorch to fastai – fastai

URL Source: https://docs.fast.ai/examples/migrating_pytorch.html

Markdown Content:
Pure PyTorch to fastai – fastai
===============

[fastai](https://docs.fast.ai/index.html)

*   [](https://github.com/fastai/fastai)

[](https://docs.fast.ai/examples/migrating_pytorch.html "Toggle reader mode")

1.   [Tutorials](https://docs.fast.ai/tutorial.html)
2.   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_pytorch.html)
3.   [Pure PyTorch to fastai](https://docs.fast.ai/examples/migrating_pytorch.html)

[](https://docs.fast.ai/examples/migrating_pytorch.html)

*   [Welcome to fastai](https://docs.fast.ai/index.html) 
*   [Quick start](https://docs.fast.ai/quick_start.html) 
*   [Tutorials](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Tutorials](https://docs.fast.ai/tutorial.html) 
    *   [Beginner](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Computer vision intro](https://docs.fast.ai/tutorial.vision.html) 
        *   [Text transfer learning](https://docs.fast.ai/tutorial.text.html) 
        *   [Tabular training](https://docs.fast.ai/tutorial.tabular.html) 
        *   [Collaborative filtering tutorial](https://docs.fast.ai/tutorial.collab.html) 

    *   [Intermediate](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Data block tutorial](https://docs.fast.ai/tutorial.datablock.html) 
        *   [Training Imagenette](https://docs.fast.ai/tutorial.imagenette.html) 
        *   [Mid-tier data API - Pets](https://docs.fast.ai/tutorial.pets.html) 
        *   [Chest X-ray model](https://docs.fast.ai/tutorial.medical_imaging.html) 
        *   [Transformers](https://docs.fast.ai/tutorial.transformers.html) 
        *   [Wikitext data tutorial](https://docs.fast.ai/tutorial.wikitext.html) 
        *   [Notebook distributed training](https://docs.fast.ai/tutorial.distributed.html) 

    *   [Advanced](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Custom transforms](https://docs.fast.ai/tutorial.albumentations.html) 
        *   [Custom new task - siamese](https://docs.fast.ai/tutorial.siamese.html) 
        *   [Image sequences](https://docs.fast.ai/tutorial.image_sequence.html) 

    *   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Pure PyTorch to fastai](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Pytorch to fastai details](https://docs.fast.ai/examples/migrating_pytorch_verbose.html) 
        *   [Ignite with fastai](https://docs.fast.ai/examples/migrating_ignite.html) 
        *   [Lightning with fastai](https://docs.fast.ai/examples/migrating_lightning.html) 
        *   [Catalyst with fastai](https://docs.fast.ai/examples/migrating_catalyst.html) 

*   [Training](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Learner, Metrics, Callbacks](https://docs.fast.ai/learner.html) 
    *   [Optimizers](https://docs.fast.ai/optimizer.html) 
    *   [Metrics](https://docs.fast.ai/metrics.html) 
    *   [Interpretation of Predictions](https://docs.fast.ai/interpret.html) 
    *   [Distributed training](https://docs.fast.ai/distributed.html) 
    *   [Mixed precision training](https://docs.fast.ai/callback.fp16.html) 
    *   [Channels Last training](https://docs.fast.ai/callback.channelslast.html) 
    *   [Callbacks](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
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

*   [Data](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Data block](https://docs.fast.ai/data.block.html) 
    *   [Data core](https://docs.fast.ai/data.core.html) 
    *   [DataLoaders](https://docs.fast.ai/data.load.html) 
    *   [External data](https://docs.fast.ai/data.external.html) 
    *   [Data transformations](https://docs.fast.ai/data.transforms.html) 

*   [Core](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Torch Core](https://docs.fast.ai/torch_core.html) 
    *   [Layers](https://docs.fast.ai/layers.html) 
    *   [Loss Functions](https://docs.fast.ai/losses.html) 

*   [Vision](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Core vision](https://docs.fast.ai/vision.core.html) 
    *   [Vision data](https://docs.fast.ai/vision.data.html) 
    *   [Vision augmentation](https://docs.fast.ai/vision.augment.html) 
    *   [Vision learner](https://docs.fast.ai/vision.learner.html) 
    *   [Models](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [XResnet](https://docs.fast.ai/vision.models.xresnet.html) 
        *   [Dynamic UNet](https://docs.fast.ai/vision.models.unet.html) 

    *   [GAN](https://docs.fast.ai/vision.gan.html) 
    *   [Vision utils](https://docs.fast.ai/vision.utils.html) 
    *   [Vision widgets](https://docs.fast.ai/vision.widgets.html) 

*   [Text](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Text core](https://docs.fast.ai/text.core.html) 
    *   [Text data](https://docs.fast.ai/text.data.html) 
    *   [Text learner](https://docs.fast.ai/text.learner.html) 
    *   [Models](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
        *   [Core text modules](https://docs.fast.ai/text.models.core.html) 
        *   [AWD-LSTM](https://docs.fast.ai/text.models.awdlstm.html) 

*   [Tabular](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Tabular core](https://docs.fast.ai/tabular.core.html) 
    *   [Tabular data](https://docs.fast.ai/tabular.data.html) 
    *   [Tabular learner](https://docs.fast.ai/tabular.learner.html) 
    *   [Tabular model](https://docs.fast.ai/tabular.model.html) 
    *   [Collaborative filtering](https://docs.fast.ai/collab.html) 

*   [Medical](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Medical Imaging](https://docs.fast.ai/medical.imaging.html) 
    *   [Medical Text](https://docs.fast.ai/medical.text.html) 

*   [Integrations](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Wandb](https://docs.fast.ai/callback.wandb.html) 
    *   [Captum](https://docs.fast.ai/callback.captum.html) 
    *   [Comet.ml](https://docs.fast.ai/callback.comet.html) 
    *   [Tensorboard](https://docs.fast.ai/callback.tensorboard.html) 
    *   [Hugging Face Hub](https://docs.fast.ai/huggingface.html) 

*   [fastai Development](https://docs.fast.ai/examples/migrating_pytorch.html)[](https://docs.fast.ai/examples/migrating_pytorch.html) 
    *   [Pull requests made easy](https://docs.fast.ai/dev-setup.html) 
    *   [git Notes](https://docs.fast.ai/dev/git.html) 
    *   [fastai Abbreviation Guide](https://docs.fast.ai/dev/abbr.html) 
    *   [fastai coding style](https://docs.fast.ai/dev/style.html) 
    *   [Working with GPU](https://docs.fast.ai/dev/gpu.html) 
    *   [Notes For Developers](https://docs.fast.ai/dev/develop.html) 

Other Formats
-------------

*   [CommonMark](https://docs.fast.ai/examples/migrating_pytorch.html.md)

1.   [Tutorials](https://docs.fast.ai/tutorial.html)
2.   [Migrating from Other Libs](https://docs.fast.ai/examples/migrating_pytorch.html)
3.   [Pure PyTorch to fastai](https://docs.fast.ai/examples/migrating_pytorch.html)

Pure PyTorch to fastai
======================

 Incrementally adding fastai goodness to your PyTorch models 

`from fastai.vision.all import *`

We’re going to use the MNIST training code from the official PyTorch examples, slightly reformatted for space, updated from AdaDelta to AdamW, and converted from a script to a module. There’s a lot of code, so we’ve put it into migrating_pytorch.py!

 Note 

The source script for `migrating_pytorch` is in the `examples` subdirectory of this folder if you checked out the `fastai` repo from git, or can be downloaded from [here](https://github.com/fastai/fastai/blob/master/nbs/examples/migrating_pytorch.py) if you’re using an online viewer such as Colab.

`from migrating_pytorch import *`

We can entirely replace the custom training loop with fastai’s. That means you can get rid of `train()`, `test()`, and the epoch loop in the original code, and replace it all with just this:

```
data = DataLoaders(train_loader, test_loader)
learn = Learner(data, Net(), loss_func=F.nll_loss, opt_func=Adam, metrics=accuracy)
```

Data is automatically moved to the GPU or CPU depending on what’s available, without the need of extra Callbacks or overhead.

fastai supports many schedulers. We recommend fitting with one cycle training:

`learn.fit_one_cycle(epochs, lr)`

| epoch | train_loss | valid_loss | accuracy | time |
| --- | --- | --- | --- | --- |
| 0 | 0.130664 | 0.049394 | 0.984200 | 01:16 |

As you can see, migrating from pure PyTorch allows you to remove a lot of code, and doesn’t require you to change any of your existing data pipelines, optimizers, loss functions, models, etc.

Once you’ve made this change, you can then benefit from fastai’s rich set of callbacks, transforms, visualizations, and so forth.

Note that fastai is much more than just a training loop (although we’re only using the training loop in this example) - it is a complete framework including GPU-accelerated transformations, end-to-end inference, integrated applications for vision, text, tabular, and collaborative filtering, and so forth. You can use any part of the framework on its own, or combine them together, as described in the [fastai paper](https://arxiv.org/abs/2002.04688).

*   [Report an issue](https://github.com/fastai/fastai/issues/new)
