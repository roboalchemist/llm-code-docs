# Fast.AI Documentation

Source: https://github.com/fastai/fastai

This documentation is extracted from the Fast.AI repository. Fast.AI is a deep learning library built on top of PyTorch that aims to simplify training fast and accurate neural networks using modern best practices.

---

## Repository

- **Repository**: https://github.com/fastai/fastai
- **Documentation**: https://docs.fast.ai
- **Website**: https://fast.ai

---

## CHANGELOG

# Release notes

<!-- do not remove -->

## 2.8.7

- Allow any pytorch<3


## 2.8.6

- New fastcore dep


## 2.8.5

### New Features

- PyTorch 2.9 support ([#4116](https://github.com/fastai/fastai/issues/4116))

### Bugs Squashed

- Address deprecation warnings in fp16 Callback ([#4124](https://github.com/fastai/fastai/pull/4124)), thanks to [@FacuRoffet99](https://github.com/FacuRoffet99)
- Make SaveModelCallback fix compatible with TextLearner ([#4121](https://github.com/fastai/fastai/pull/4121)), thanks to [@austinvhuang](https://github.com/austinvhuang)


## 2.8.4

### Bugs Squashed

- set `weights_only=False` for `load_model_text`, fixes LRFinder / `lr_find` ([#4120](https://github.com/fastai/fastai/pull/4120)), thanks to [@austinvhuang](https://github.com/austinvhuang)
- fix: Pass alpha and beta parameters to `rnn_cbs()` in TextLearner constructor ([#4119](https://github.com/fastai/fastai/pull/4119)), thanks to [@austinvhuang](https://github.com/austinvhuang)
- Fixed SaveModelCallback ([#4118](https://github.com/fastai/fastai/pull/4118)), thanks to [@FacuRoffet99](https://github.com/FacuRoffet99)


## 2.8.3

### New Features

- PyTorch 2.8 support ([#4116](https://github.com/fastai/fastai/issues/4116))

### Bugs Squashed

- Update plot lr find ([#4098](https://github.com/fastai/fastai/pull/4098)), thanks to [@Timmecom](https://github.com/Timmecom)


## 2.8.2

### New Features

- update torch version to 2.7 ([#4095](https://github.com/fastai/fastai/pull/4095)), thanks to [@tonyhoo](https://github.com/tonyhoo)


## 2.8.1

### New Features

- Use fasttransform ([#4074](https://github.com/fastai/fastai/pull/4074)), thanks to [@RensDimmendaal](https://github.com/RensDimmendaal)


## 2.7.19

### New Features

- Add support for PyTorch 2.6 ([#4078](https://github.com/fastai/fastai/pull/4078)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)


## 2.7.18

### New Features

- PyTorch 2.5 support


## 2.7.17

### New Features

- add markdown to doc output ([#4044](https://github.com/fastai/fastai/issues/4044))
- Support PyTorch 2.4 ([#4040](https://github.com/fastai/fastai/pull/4040)), thanks to [@tonyhoo](https://github.com/tonyhoo)
- Update Fastcore max version


## 2.7.16

### New Features

- Support PyTorch 2.4 ([#4040](https://github.com/fastai/fastai/pull/4040)), thanks to [@tonyhoo](https://github.com/tonyhoo)
- Support for loss function pickling ([#4034](https://github.com/fastai/fastai/pull/4034)), thanks to [@kevin-vitro](https://github.com/kevin-vitro)


## 2.7.15

### New Features

- Support PyTorch 2.3 ([#4026](https://github.com/fastai/fastai/pull/4026)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Add `log` and `show_epochs` to `log_ploss` ([#3964](https://github.com/fastai/fastai/pull/3964)), thanks to [@turbotimon](https://github.com/turbotimon)


## 2.7.14

### New Features

- PyTorch 2.2 support, thanks to [@warner-benjamin](https://github.com/warner-benjamin)


## 2.7.13

### New Features

- PyTorch 2.1 compatibility ([#3970](https://github.com/fastai/fastai/pull/3970)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Add `MutableMapping` to `torch_core.apply` to Support Moving Transformers Dicts ([#3969](https://github.com/fastai/fastai/pull/3969)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Added Jaccard coefficient metric for multiclass target in segmentation ([#3951](https://github.com/fastai/fastai/pull/3951)), thanks to [@Hazem-Ahmed-Abdelraouf](https://github.com/Hazem-Ahmed-Abdelraouf)
- Support TorchVision's Multi-Weight API ([#3944](https://github.com/fastai/fastai/pull/3944)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix the Deploy to GitHub Pages Action ([#3942](https://github.com/fastai/fastai/pull/3942)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)

### Bugs Squashed

- Fix Pandas Categorical FutureWarning ([#3973](https://github.com/fastai/fastai/pull/3973)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix torch.jit.script on TimmBody ([#3948](https://github.com/fastai/fastai/pull/3948)), thanks to [@johan12345](https://github.com/johan12345)
- Resolve CutMix Deprecation Warning ([#3937](https://github.com/fastai/fastai/pull/3937)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fixed format string ([#3934](https://github.com/fastai/fastai/pull/3934)), thanks to [@bkowshik](https://github.com/bkowshik)
- Fix casting types for mps ([#3912](https://github.com/fastai/fastai/pull/3912)), thanks to [@MSciesiek](https://github.com/MSciesiek)
- Fix AccumMetric name.setter ([#3621](https://github.com/fastai/fastai/pull/3621)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)


## 2.7.12

### New Features

- PyTorch 2.0 compatibility ([#3890](https://github.com/fastai/fastai/pull/3890)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Pytorch 2.0 compiler compatibility ([#3899](https://github.com/fastai/fastai/pull/3899)), thanks to [@ggosline](https://github.com/ggosline)
- Better version support for `TensorBase.new_empty` ([#3887](https://github.com/fastai/fastai/pull/3887)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- TensorBase deepcopy Compatibility ([#3882](https://github.com/fastai/fastai/pull/3882)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)

### Bugs Squashed

- Fix `Learn.predict` Errors Out if Passed a PILImage ([#3884](https://github.com/fastai/fastai/pull/3884)), thanks to [@nglillywhite](https://github.com/nglillywhite)
- Set DataLoaders device if not None and to exists ([#3873](https://github.com/fastai/fastai/pull/3873)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix `default_device` to correctly detect + use mps (Apple Silicon) ([#3858](https://github.com/fastai/fastai/pull/3858)), thanks to [@wolever](https://github.com/wolever)


## 2.7.11

### New Features

- ChannelsLast Callback Improvements, Additional Documentation, & Bug Fix ([#3876](https://github.com/fastai/fastai/pull/3876)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Add support for a batch transforms `to` method ([#3875](https://github.com/fastai/fastai/pull/3875)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Allow Pillow Image to be passed to PILBase.create ([#3872](https://github.com/fastai/fastai/pull/3872)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Compat with latest numpy ([#3871](https://github.com/fastai/fastai/pull/3871)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Move training-only step to separate function in `Learner` ([#3857](https://github.com/fastai/fastai/pull/3857)), thanks to [@kunaltyagi](https://github.com/kunaltyagi)
- TabularPandas data transform reproducibility ([#2826](https://github.com/fastai/fastai/issues/2826))

### Bugs Squashed

- Set DataLoaders device if not None and to exists ([#3873](https://github.com/fastai/fastai/pull/3873)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix `default_device` to correctly detect + use mps (Apple Silicon) ([#3858](https://github.com/fastai/fastai/pull/3858)), thanks to [@wolever](https://github.com/wolever)
- Fix load hanging in distributed processes ([#3839](https://github.com/fastai/fastai/pull/3839)), thanks to [@muellerzr](https://github.com/muellerzr)
- `default_device` logic is repeated twice, related to `mps` / OSX support. ([#3785](https://github.com/fastai/fastai/issues/3785))
- revert auto-enable of mac mps due to pytorch limitations ([#3769](https://github.com/fastai/fastai/issues/3769))
- Fix Classification Interpretation ([#3563](https://github.com/fastai/fastai/pull/3563)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- vision tutorial failed at `learner.fine_tune(1)` ([#3283](https://github.com/fastai/fastai/issues/3283))


## 2.7.10

### New Features

- Add torch save and load kwargs ([#3831](https://github.com/fastai/fastai/pull/3831)), thanks to [@JonathanGrant](https://github.com/JonathanGrant)
  - This lets us do nice things like set pickle_module to cloudpickle
- PyTorch 1.13 Compatibility ([#3828](https://github.com/fastai/fastai/pull/3828)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Recursive copying of attribute dictionaries for TensorImage subclass ([#3822](https://github.com/fastai/fastai/pull/3822)), thanks to [@restlessronin](https://github.com/restlessronin)
- `OptimWrapper` sets same param groups as `Optimizer` ([#3821](https://github.com/fastai/fastai/pull/3821)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
  - This PR harmonizes the default parameter group setting between `OptimWrapper` and `Optimizer` by modifying `OptimWrapper` to match `Optimizer`'s logic.
- Support normalization of 1-channel images in unet ([#3820](https://github.com/fastai/fastai/pull/3820)), thanks to [@marib00](https://github.com/marib00)
- Add `img_cls` param to `ImageDataLoaders` ([#3808](https://github.com/fastai/fastai/pull/3808)), thanks to [@tcapelle](https://github.com/tcapelle)
  - This is particularly useful for passing `PILImageBW` for MNIST.
- Add support for `kwargs` to `tensor()` when arg is an `ndarray` ([#3797](https://github.com/fastai/fastai/pull/3797)), thanks to [@SaadAhmedGit](https://github.com/SaadAhmedGit)
- Add latest TorchVision models on fastai ([#3791](https://github.com/fastai/fastai/pull/3791)), thanks to [@datumbox](https://github.com/datumbox)
- Option to preserve filenames in `download_images` ([#2983](https://github.com/fastai/fastai/pull/2983)), thanks to [@mess-lelouch](https://github.com/mess-lelouch)

### Bugs Squashed

- `get_text_classifier` fails with custom `AWS_LSTM` ([#3817](https://github.com/fastai/fastai/issues/3817))
- revert auto-enable of mac mps due to pytorch limitations ([#3769](https://github.com/fastai/fastai/issues/3769))
- Workaround for performance bug in PyTorch with subclassed tensors ([#3683](https://github.com/fastai/fastai/pull/3683)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)


## 2.7.8

### New Features

- add split value argument to ColSplitter ([#3737](https://github.com/fastai/fastai/pull/3737)), thanks to [@DanteOz](https://github.com/DanteOz)
- deterministic repr for PIL images ([#3762](https://github.com/fastai/fastai/issues/3762))
- option to skip default callbacks in `Learner` ([#3739](https://github.com/fastai/fastai/issues/3739))
- update for nbdev2 ([#3747](https://github.com/fastai/fastai/issues/3747))

### Bugs Squashed

- IntToFloatTensor failing on Mac mps due to missing op ([#3761](https://github.com/fastai/fastai/issues/3761))
- fix for pretrained in vision.learner ([#3746](https://github.com/fastai/fastai/pull/3746)), thanks to [@peterdudfield](https://github.com/peterdudfield)
- fix same file error message when resizing image ([#3743](https://github.com/fastai/fastai/pull/3743)), thanks to [@cvergnes](https://github.com/cvergnes)


## 2.7.6

### New Features

- Initial Mac GPU (mps) support ([#3719](https://github.com/fastai/fastai/issues/3719))


## 2.7.5

### New Features

- auto-normalize timm models ([#3716](https://github.com/fastai/fastai/issues/3716))
- PyTorch 1.12 support


## 2.7.4

### New Features

- Add `DataBlock.weighted_dataloaders` ([#3706](https://github.com/fastai/fastai/issues/3706))


## 2.7.2

### Bugs Squashed

- `PIL.Resampling` only added in v9.1 ([#3699](https://github.com/fastai/fastai/issues/3699))


## 2.7.1

### Bugs Squashed

- Update fastcore minimum version


## 2.7.0

### Breaking changes

- Distributed training now uses Hugging Face Accelerate, rather than fastai's launcher.
  Distributed training is now supported in a notebook -- see [this tutorial](https://docs.fast.ai/tutorial.distributed) for details

### New Features

- `resize_images` creates folder structure at `dest` when `recurse=True` ([#3692](https://github.com/fastai/fastai/issues/3692))
- Integrate nested callable and getcallable ([#3691](https://github.com/fastai/fastai/pull/3691)), thanks to [@muellerzr](https://github.com/muellerzr)
- workaround pytorch subclass performance bug ([#3682](https://github.com/fastai/fastai/issues/3682))
- Torch 1.12.0 compatibility ([#3659](https://github.com/fastai/fastai/pull/3659)), thanks to [@josiahls](https://github.com/josiahls)
- Integrate Accelerate into fastai ([#3646](https://github.com/fastai/fastai/pull/3646)), thanks to [@muellerzr](https://github.com/muellerzr)
- New Callback event, before and after backward ([#3644](https://github.com/fastai/fastai/pull/3644)), thanks to [@muellerzr](https://github.com/muellerzr)
- Let optimizer use built torch opt ([#3642](https://github.com/fastai/fastai/pull/3642)), thanks to [@muellerzr](https://github.com/muellerzr)
- Support PyTorch Dataloaders with `DistributedDL` ([#3637](https://github.com/fastai/fastai/pull/3637)), thanks to [@tmabraham](https://github.com/tmabraham)
- Add `channels_last` cb ([#3634](https://github.com/fastai/fastai/pull/3634)), thanks to [@tcapelle](https://github.com/tcapelle)
- support all timm kwargs ([#3631](https://github.com/fastai/fastai/issues/3631))
- send `self.loss_func` to device if it is an insatnce on nn.Module ([#3395](https://github.com/fastai/fastai/pull/3395)), thanks to [@arampacha](https://github.com/arampacha)
- adds tracking and logging best metrics to wandb cb ([#3372](https://github.com/fastai/fastai/pull/3372)), thanks to [@arampacha](https://github.com/arampacha)

### Bugs Squashed

- Solve hanging `load_model` and let LRFind be ran in a distributed setup ([#3689](https://github.com/fastai/fastai/pull/3689)), thanks to [@muellerzr](https://github.com/muellerzr)
- pytorch subclass functions fail if no positional args ([#3687](https://github.com/fastai/fastai/issues/3687))
- Workaround for performance bug in PyTorch with subclassed tensors ([#3683](https://github.com/fastai/fastai/pull/3683)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix `Tokenizer.get_lengths` ([#3667](https://github.com/fastai/fastai/pull/3667)), thanks to [@karotchykau](https://github.com/karotchykau)
- `load_learner` with `cpu=False` doesn't respect the current cuda device if model exported on another; fixes #3656 ([#3657](https://github.com/fastai/fastai/pull/3657)), thanks to [@ohmeow](https://github.com/ohmeow)
- [Bugfix] Fix smoothloss on distributed ([#3643](https://github.com/fastai/fastai/pull/3643)), thanks to [@muellerzr](https://github.com/muellerzr)
- WandbCallback Error: "Tensors must be CUDA and dense" on distributed training ([#3291](https://github.com/fastai/fastai/issues/3291))
- vision tutorial failed at `learner.fine_tune(1)` ([#3283](https://github.com/fastai/fastai/issues/3283))


## 2.6.3

### Bugs Squashed

- Fix `Learner` pickling problem introduced in v2.6.2


## 2.6.2

### Bugs Squashed

- Race condition: `'Tensor' object has no attribute 'append'` ([#3385](https://github.com/fastai/fastai/issues/3385))


## 2.6.0

### New Features

- add support for Ross Wightman's Pytorch Image Models (timm) library ([#3624](https://github.com/fastai/fastai/issues/3624))
- rename `cnn_learner` to `vision_learner` since we now support models other than CNNs too ([#3625](https://github.com/fastai/fastai/issues/3625))

### Bugs Squashed

- Fix AccumMetric name.setter ([#3621](https://github.com/fastai/fastai/pull/3621)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix Classification Interpretation ([#3563](https://github.com/fastai/fastai/pull/3563)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)


## 2.5.6

### New Features

- support pytorch 1.11 ([#3618](https://github.com/fastai/fastai/issues/3618))
- Add in exceptions and verbose errors ([#3611](https://github.com/fastai/fastai/pull/3611)), thanks to [@muellerzr](https://github.com/muellerzr)

### Bugs Squashed

- Fix name conflicts in `ColReader` ([#3602](https://github.com/fastai/fastai/pull/3602)), thanks to [@hiromis](https://github.com/hiromis)


## 2.5.5

### New Features

- Update fastcore dep

## 2.5.4

### New Features

- Support py3.10 annotations ([#3601](https://github.com/fastai/fastai/issues/3601))

### Bugs Squashed

- Fix pin_memory=True breaking (batch) Transforms ([#3606](https://github.com/fastai/fastai/pull/3606)), thanks to [@johan12345](https://github.com/johan12345)
- Add Python 3.9 to `setup.py` for PyPI ([#3604](https://github.com/fastai/fastai/pull/3604)), thanks to [@nzw0301](https://github.com/nzw0301)
- removes add_vert from get_grid calls ([#3593](https://github.com/fastai/fastai/pull/3593)), thanks to [@kevinbird15](https://github.com/kevinbird15)
- Making `loss_not_reduced` work with DiceLoss ([#3583](https://github.com/fastai/fastai/pull/3583)), thanks to [@hiromis](https://github.com/hiromis)
- Fix bug in URLs.path() in 04_data.external ([#3582](https://github.com/fastai/fastai/pull/3582)), thanks to [@malligaraj](https://github.com/malligaraj)
- Custom name for metrics ([#3573](https://github.com/fastai/fastai/pull/3573)), thanks to [@bdsaglam](https://github.com/bdsaglam)
- Update import for show_install ([#3568](https://github.com/fastai/fastai/pull/3568)), thanks to [@fr1ll](https://github.com/fr1ll)
- Fix Classification Interpretation ([#3563](https://github.com/fastai/fastai/pull/3563)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Updates Interpretation class to be memory efficient ([#3558](https://github.com/fastai/fastai/pull/3558)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Learner.show_results uses passed dataloader via dl_idx or dl arguments ([#3554](https://github.com/fastai/fastai/pull/3554)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix learn.export pickle error with MixedPrecision Callback ([#3544](https://github.com/fastai/fastai/pull/3544)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix concurrent LRFinder instances overwriting each other by using tempfile ([#3528](https://github.com/fastai/fastai/pull/3528)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix _get_shapes to work with dictionaries ([#3520](https://github.com/fastai/fastai/pull/3520)), thanks to [@ohmeow](https://github.com/ohmeow)
- Fix torch version checks, remove clip_grad_norm check ([#3518](https://github.com/fastai/fastai/pull/3518)), thanks to [@warner-benjamin](https://github.com/warner-benjamin)
- Fix nested tensors predictions compatibility with fp16 ([#3516](https://github.com/fastai/fastai/pull/3516)), thanks to [@tcapelle](https://github.com/tcapelle)
- Learning rate passed via OptimWrapper not updated in Learner ([#3337](https://github.com/fastai/fastai/issues/3337))
- Different results after running `lr_find()` at different times ([#3295](https://github.com/fastai/fastai/issues/3295))
- lr_find() may fail if run in parallel from the same directory ([#3240](https://github.com/fastai/fastai/issues/3240))


## 2.5.3

### New Features

- add `at_end` feature to `SaveModelCallback` ([#3296](https://github.com/fastai/fastai/pull/3296)), thanks to [@tmabraham](https://github.com/tmabraham)

### Bugs Squashed

- fix fp16 test ([#3284](https://github.com/fastai/fastai/pull/3284)), thanks to [@tmabraham](https://github.com/tmabraham)


## 2.5.1

- Import `download_url` from fastdownload


## 2.5.0

### Breaking changes

- `config.yml` has been renamed to `config.ini`, and is now in `ConfigParser` format instead of YAML
- THe `_path` suffixes in `config.ini` have been removed

### Bugs Squashed

- Training with `learn.to_fp16(`) fails with PyTorch 1.9 / Cuda 11.4 ([#3438](https://github.com/fastai/fastai/issues/3438))
- pandas 1.3.0 breaks `add_elapsed_times` ([#3431](https://github.com/fastai/fastai/issues/3431))


## 2.4.1

### New Features

- add DiceLoss ([#3386](https://github.com/fastai/fastai/pull/3386)), thanks to [@tcapelle](https://github.com/tcapelle)
- TabularPandas data transform reproducibility ([#2826](https://github.com/fastai/fastai/issues/2826))

### Bugs Squashed

- Latest Pillow v8.3.0 breaks conversion Image to Tensor ([#3416](https://github.com/fastai/fastai/issues/3416))


## 2.4

### Breaking changes

- QRNN module removed, due to incompatibility with PyTorch 1.9, and lack of utilization of QRNN in the deep learning community. QRNN was our only module that wasn't pure Python, so with this change fastai is now a pure Python package.

### New Features

- Support for PyTorch 1.9
- Improved LR Suggestions ([#3377](https://github.com/fastai/fastai/pull/3377)), thanks to [@muellerzr](https://github.com/muellerzr)
- SaveModelCallback every nth epoch ([#3375](https://github.com/fastai/fastai/pull/3375)), thanks to [@KeremTurgutlu](https://github.com/KeremTurgutlu)
- Send self.loss_func to device if it is an instance of nn.Module ([#3395](https://github.com/fastai/fastai/pull/3395)), thanks to [@arampacha](https://github.com/arampacha)
- Batch support for more than one image ([#3339](https://github.com/fastai/fastai/issues/3339))
- Changable tfmdlists for TransformBlock, Datasets, DataBlock ([#3327](https://github.com/fastai/fastai/issues/3327))

### Bugs Squashed

- convert TensorBBox to TensorBase during compare ([#3388](https://github.com/fastai/fastai/pull/3388)), thanks to [@kevinbird15](https://github.com/kevinbird15)
- Check if normalize exists on `_add_norm` ([#3371](https://github.com/fastai/fastai/pull/3371)), thanks to [@renato145](https://github.com/renato145)


## 2.3.1

### New Features

- Add support for pytorch 1.8 ([#3349](https://github.com/fastai/fastai/issues/3349))
- Add support for spacy3 ([#3348](https://github.com/fastai/fastai/issues/3348))
- Add support for Windows. Big thanks to Microsoft for many contributions to get this working
- Timedistributed layer and Image Sequence Tutorial ([#3124](https://github.com/fastai/fastai/pull/3124)), thanks to [@tcapelle](https://github.com/tcapelle)
- Add interactive run logging to AzureMLCallback ([#3341](https://github.com/fastai/fastai/pull/3341)), thanks to [@yijinlee](https://github.com/yijinlee)
- Batch support for more than one image ([#3339](https://github.com/fastai/fastai/issues/3339))
- Have interp use ds_idx, add tests ([#3332](https://github.com/fastai/fastai/pull/3332)), thanks to [@muellerzr](https://github.com/muellerzr)
- Automatically have fastai determine the right device, even with torch DataLoaders ([#3330](https://github.com/fastai/fastai/pull/3330)), thanks to [@muellerzr](https://github.com/muellerzr)
- Add `at_end` feature to `SaveModelCallback` ([#3296](https://github.com/fastai/fastai/pull/3296)), thanks to [@tmabraham](https://github.com/tmabraham)
- Improve inplace params in Tabular's new and allow for new and test_dl to be in place ([#3292](https://github.com/fastai/fastai/pull/3292)), thanks to [@muellerzr](https://github.com/muellerzr)
- Update VSCode & Codespaces dev container ([#3280](https://github.com/fastai/fastai/pull/3280)), thanks to [@bamurtaugh](https://github.com/bamurtaugh)
- Add max_scale param to RandomResizedCrop(GPU) ([#3252](https://github.com/fastai/fastai/pull/3252)), thanks to [@kai-tub](https://github.com/kai-tub)
- Increase testing granularity for speedup ([#3242](https://github.com/fastai/fastai/pull/3242)), thanks to [@ddobrinskiy](https://github.com/ddobrinskiy)

### Bugs Squashed

- Make TTA turn shuffle and drop_last off when using ds_idx ([#3347](https://github.com/fastai/fastai/pull/3347)), thanks to [@muellerzr](https://github.com/muellerzr)
- Add order to TrackerCallback derived classes ([#3346](https://github.com/fastai/fastai/pull/3346)), thanks to [@muellerzr](https://github.com/muellerzr)
- Prevent schedule from crashing close to the end of training ([#3335](https://github.com/fastai/fastai/pull/3335)), thanks to [@Lewington-pitsos](https://github.com/Lewington-pitsos)
- Fix ability to use raw pytorch DataLoaders ([#3328](https://github.com/fastai/fastai/pull/3328)), thanks to [@hamelsmu](https://github.com/hamelsmu)
- Fix PixelShuffle_icnr weight ([#3322](https://github.com/fastai/fastai/pull/3322)), thanks to [@pratX](https://github.com/pratX)
- Creation of new DataLoader in Learner.get_preds has wrong keyword ([#3316](https://github.com/fastai/fastai/pull/3316)), thanks to [@tcapelle](https://github.com/tcapelle)
- Correct layers order in tabular learner ([#3314](https://github.com/fastai/fastai/pull/3314)), thanks to [@gradientsky](https://github.com/gradientsky)
- Fix vmin parameter default ([#3305](https://github.com/fastai/fastai/pull/3305)), thanks to [@tcapelle](https://github.com/tcapelle)
- Ensure call to `one_batch` places data on the right device ([#3298](https://github.com/fastai/fastai/pull/3298)), thanks to [@tcapelle](https://github.com/tcapelle)
- Fix Cutmix Augmentation ([#3259](https://github.com/fastai/fastai/pull/3259)), thanks to [@MrRobot2211](https://github.com/MrRobot2211)
- Fix custom tokenizers for DataLoaders ([#3256](https://github.com/fastai/fastai/pull/3256)), thanks to [@iskode](https://github.com/iskode)
- fix error setting  'tok_tfm' parameter in TextDataloaders.from_folder
- Fix lighting augmentation ([#3255](https://github.com/fastai/fastai/pull/3255)), thanks to [@kai-tub](https://github.com/kai-tub)
- Fix CUDA variable serialization ([#3253](https://github.com/fastai/fastai/pull/3253)), thanks to [@mszhanyi](https://github.com/mszhanyi)
- change batch tfms to have the correct dimensionality ([#3251](https://github.com/fastai/fastai/pull/3251)), thanks to [@trdvangraft](https://github.com/trdvangraft)
- Ensure add_datepart adds elapsed as numeric column ([#3230](https://github.com/fastai/fastai/pull/3230)), thanks to [@aberres](https://github.com/aberres)


## 2.3.0
### Breaking Changes

- fix optimwrapper to work with `param_groups` ([#3241](https://github.com/fastai/fastai/pull/3241)), thanks to [@tmabraham](https://github.com/tmabraham)
  - OptimWrapper now has a different constructor signature, which makes it easier to wrap PyTorch optimizers

### New Features

- Support discriminative learning with OptimWrapper ([#2829](https://github.com/fastai/fastai/issues/2829))

### Bugs Squashed

- Updated to support adding transforms to multiple dataloaders ([#3268](https://github.com/fastai/fastai/pull/3268)), thanks to [@marii-moe](https://github.com/marii-moe)
  - This fixes an issue in 2.2.7 which resulted in incorrect validation metrics when using Normalization


## 2.2.7

### Bugs Squashed

- Regression fix: Ensure `add_datepart` adds elapsed as numeric column ([#3230](https://github.com/fastai/fastai/pull/3230)), thanks to [@aberres](https://github.com/aberres)


## 2.2.6

### Bugs Squashed

- 2.2.5 was not released correctly - it was actually 2.2.3

## 2.2.5

### New Features

- Enhancement: Let TextDataLoaders take in a custom `tok_text_col` ([#3208](https://github.com/fastai/fastai/pull/3208)), thanks to [@muellerzr](https://github.com/muellerzr)
- Changed dataloaders arguments to have consistent overrides ([#3178](https://github.com/fastai/fastai/pull/3178)), thanks to [@marii-moe](https://github.com/marii-moe)
- Better support for iterable datasets ([#3173](https://github.com/fastai/fastai/pull/3173)), thanks to [@jcaw](https://github.com/jcaw)

### Bugs Squashed

- BrokenProcessPool in `download_images()` on Windows ([#3196](https://github.com/fastai/fastai/issues/3196))
- error on predict() or using interp with resnet and MixUp ([#3180](https://github.com/fastai/fastai/issues/3180))
- Fix 'cat' attribute with pandas dataframe: `AttributeError: Can only use .cat accessor with a 'category' dtype` ([#3165](https://github.com/fastai/fastai/pull/3165)), thanks to [@dreamflasher](https://github.com/dreamflasher)
- `cont_cat_split` does not support pandas types ([#3156](https://github.com/fastai/fastai/issues/3156))
- `DataBlock.dataloaders` does not support the advertised "shuffle" argument ([#3133](https://github.com/fastai/fastai/issues/3133))


## 2.2.3

### New Features

- Calculate correct `nf` in `create_head` based on `concat_pool` ([#3115](https://github.com/fastai/fastai/pull/3115)), thanks to [@muellerzr](https://github.com/muellerzr)

### Bugs Squashed

- wandb integration failing with latest wandb library ([#3066](https://github.com/fastai/fastai/issues/3066))
- `Learner.load` and `LRFinder` not functioning properly for the optimizer states ([#2892](https://github.com/fastai/fastai/issues/2892))


## 2.2.2

### Bugs Squashed

- tensorboard and wandb can not access `smooth_loss` ([#3131](https://github.com/fastai/fastai/issues/3131))


## 2.2.0
### Breaking Changes

- Promote `NativeMixedPrecision` to default `MixedPrecision` (and similar for `Learner.to_fp16`); old `MixedPrecision` is now called `NonNativeMixedPrecision` ([#3127](https://github.com/fastai/fastai/issues/3127))
  - Use the new `GradientClip` callback instead of the `clip` parameter to use gradient clipping
- Adding a `Callback` which has the same name as an attribute no longer raises an exception ([#3109](https://github.com/fastai/fastai/issues/3109))
- RNN training now requires `RNNCallback`, but does not require `RNNRegularizer`; `out` and `raw_out` have moved to `RNNRegularizer` ([#3108](https://github.com/fastai/fastai/issues/3108))
  - Call `rnn_cbs` to get all callbacks needed for RNN training, optionally with regularization
- replace callback `run_after` with `order`; do not run `after` cbs on exception ([#3101](https://github.com/fastai/fastai/issues/3101))

### New Features

- Add `GradientClip` callback ([#3107](https://github.com/fastai/fastai/issues/3107))
- Make `Flatten` cast to `TensorBase` to simplify type compatibility ([#3106](https://github.com/fastai/fastai/issues/3106))
- make flattened metrics compatible with all tensor subclasses ([#3105](https://github.com/fastai/fastai/issues/3105))
- New class method `TensorBase.register_func` to register types for `__torch_function__` ([#3097](https://github.com/fastai/fastai/issues/3097))
- new `dynamic` flag for controlling dynamic loss scaling in `NativeMixedPrecision` ([#3096](https://github.com/fastai/fastai/issues/3096))
- remove need to call `to_native_fp32` before `predict`; set `skipped` in NativeMixedPrecision after NaN from dynamic loss scaling ([#3095](https://github.com/fastai/fastai/issues/3095))
- make native fp16 extensible with callbacks ([#3094](https://github.com/fastai/fastai/issues/3094))
- Calculate correct `nf` in `create_head` based on `concat_pool` ([#3115](https://github.com/fastai/fastai/pull/3115)) thanks to [@muellerzr](https://github.com/muellerzr)


## 2.1.10

### New Features

- Small DICOM segmentation dataset ([#3034](https://github.com/fastai/fastai/pull/3034)), thanks to [@moritzschwyzer](https://github.com/moritzschwyzer)

### Bugs Squashed

- `NoneType object has no attribute append` in fastbook chapter 6 BIWI example ([#3091](https://github.com/fastai/fastai/issues/3091))


## 2.1.9

### New Features

- Refactor MixUp and CutMix into MixHandler ([#3037](https://github.com/fastai/fastai/pull/3037)), thanks to [@muellerzr](https://github.com/muellerzr)
  - Refactors into a general MixHandler class, with MixUp and CutMix simply implementing a `before_batch` to perform the data augmentation. See `fastai.callback.mixup`

### Bugs Squashed

- Gradient Accumulation + Mixed Precision shows artificially high training loss ([#3048](https://github.com/fastai/fastai/issues/3048))


## 2.1.8

### New Features

### Bugs Squashed

- Update for fastcore `negate_func`->`not_`
- LR too high for gradient accumulation ([#3040](https://github.com/fastai/fastai/pull/3040)), thanks to [@marii-moe](https://github.com/marii-moe)
- Torchscript transforms incompatibility with nn.Sequential ([#2920](https://github.com/fastai/fastai/issues/2920))


## 2.1.7

### New Features

- Pytorch 1.7 subclassing support ([#2769](https://github.com/fastai/fastai/issues/2769))

### Bugs Squashed

- unsupported operand type(s) for +=: 'TensorCategory' and 'TensorText' when using AWD_LSTM for text classification ([#3027](https://github.com/fastai/fastai/issues/3027))
- UserWarning when using SaveModelCallback() on after_epoch ([#3025](https://github.com/fastai/fastai/issues/3025))
- Segmentation error: no implementation found for 'torch.nn.functional.cross_entropy' on types that implement torch_function ([#3022](https://github.com/fastai/fastai/issues/3022))
- `TextDataLoaders.from_df()` returns `TypeError: 'float' object is not iterable` ([#2978](https://github.com/fastai/fastai/issues/2978))
- Internal assert error in awd_qrnn ([#2967](https://github.com/fastai/fastai/issues/2967))


## 2.1.6

### New Features

- Option to preserve filenames in `download_images` ([#2983](https://github.com/fastai/fastai/pull/2983)), thanks to [@mess-lelouch](https://github.com/mess-lelouch)
- Deprecate `config` in `create_cnn` and instead pass kwargs directly ([#2966](https://github.com/fastai/fastai/pull/2966)), thanks to [@borisdayma](https://github.com/borisdayma)

### Bugs Squashed

- Progress and Recorder callbacks serialize their data, resulting in large Learner export file sizes ([#2981](https://github.com/fastai/fastai/issues/2981))
- `TextDataLoaders.from_df()` returns `TypeError: 'float' object is not iterable` ([#2978](https://github.com/fastai/fastai/issues/2978))
- "only one element tensors can be converted to Python scalars" exception in Siamese Tutorial ([#2973](https://github.com/fastai/fastai/issues/2973))
- Learn.load and LRFinder not functioning properly for the optimizer states ([#2892](https://github.com/fastai/fastai/issues/2892))


## 2.1.5

### Breaking Changes

- remove `log_args` ([#2954](https://github.com/fastai/fastai/issues/2954))

### New Features

- Improve performance of `RandomSplitter` (h/t @muellerzr) ([#2957](https://github.com/fastai/fastai/issues/2957))

### Bugs Squashed

- Exporting TabularLearner via learn.export() leads to huge file size ([#2945](https://github.com/fastai/fastai/issues/2945))
- `TensorPoint` object has no attribute `img_size` ([#2950](https://github.com/fastai/fastai/issues/2950))


## 2.1.4

### Breaking Changes

- moved `has_children` from `nn.Module` to free function ([#2931](https://github.com/fastai/fastai/issues/2931))

### New Features

- Support persistent workers ([#2768](https://github.com/fastai/fastai/issues/2768))

### Bugs Squashed

- `unet_learner` segmentation fails ([#2939](https://github.com/fastai/fastai/issues/2939))
- In "Transfer learning in text" tutorial, the "dls.show_batch()" show wrong outputs ([#2910](https://github.com/fastai/fastai/issues/2910))
- `Learn.load` and `LRFinder` not functioning properly for the optimizer states ([#2892](https://github.com/fastai/fastai/issues/2892))
- Documentation for `Show_Images` broken ([#2876](https://github.com/fastai/fastai/issues/2876))
- URL link for documentation for `torch_core` library from the `doc()` method gives incorrect url ([#2872](https://github.com/fastai/fastai/issues/2872))


## 2.1.3

### Bugs Squashed

- Work around broken PyTorch subclassing of some `new_*` methods ([#2769](https://github.com/fastai/fastai/issues/2769))


## 2.1.0

### New Features

- PyTorch 1.7 compatibility ([#2917](https://github.com/fastai/fastai/issues/2917))

PyTorch 1.7 includes support for tensor subclassing, so we have replaced much of our custom subclassing code with PyTorch's. We have seen a few bugs in PyTorch's subclassing feature, however, so please file an issue if you see any code failing now which was working before.

There is one breaking change in this version of fastai, which is that custom metadata is now stored directly in tensors as standard python attributes, instead of in the special `_meta` attribute. Only advanced customization of fastai OO tensors would have used this functionality, so if you do not know what this all means, then it means you did not use it.


## 2.0.19

This version was released *after* `2.1.0`, and adds fastcore 1.3 compatibility, whilst maintaining PyTorch 1.6 compatibility. It has no new features or bug fixes.


## 2.0.18

### Forthcoming breaking changes

The next version of fastai will be 2.1. It will require PyTorch 1.7, which has significant foundational changes. It should not require any code changes except for people doing sophisticated tensor subclassing work, but nonetheless we recommend testing carefully. Therefore, we recommend pinning your fastai version to `<2.1` if you are not able to fully test your fastai code when the new version comes out.

### Dependencies

- pin pytorch (`<1.7`) and torchvision (`<0.8`) requirements ([#2915](https://github.com/fastai/fastai/issues/2915))
- Add version pin for fastcore
- Remove version pin for sentencepiece


## 2.0.16

### New Features

- added support for tb projector word embeddings ([#2853](https://github.com/fastai/fastai/pull/2853)), thanks to [@floleuerer](https://github.com/floleuerer)
- Added ability to have variable length draw ([#2845](https://github.com/fastai/fastai/pull/2845)), thanks to [@marii-moe](https://github.com/marii-moe)
- add pip upgrade cell to all notebooks, to ensure colab has current fastai version ([#2843](https://github.com/fastai/fastai/issues/2843))

### Bugs Squashed

- fix TabularDataLoaders inference of cont_names to keep y_names separate ([#2859](https://github.com/fastai/fastai/pull/2859)), thanks to [@sutt](https://github.com/sutt)


## 2.0.15

### Breaking Changes

- loss functions were moved to `loss.py` ([#2843](https://github.com/fastai/fastai/pull/2810))


## 2.0.14

### New Features

- new callback event: `after_create` ([#2842](https://github.com/fastai/fastai/issues/2842))
  - This event runs after a `Learner` is constructed. It's useful for initial setup which isn't needed for every `fit`, but just once for each `Learner` (such as setting initial defaults).

- Modified XResNet to support Conv1d / Conv3d ([#2744](https://github.com/fastai/fastai/pull/2744)), thanks to [@floleuerer](https://github.com/floleuerer)
  - Supports different input dimensions, kernel sizes and stride (added parameters ndim, ks, stride). Tested with fastai_audio and fastai time series with promising results.

### Bugs Squashed

- `img_size` attribute for `TensorPoint` is not updated properly ([#2799](https://github.com/fastai/fastai/pull/2799)), thanks to [@IRailean](https://github.com/IRailean)

## 2.0.13

### Bugs Squashed

- Undo breaking num_workers fix ([#2804](https://github.com/fastai/fastai/pull/2804))
  - Some users found the recent addition of `num_workers` to inference
    functions was causing problems, particularly on Windows. This PR
    reverts that change, until we find a more reliable way to handle
    `num_workers` for inference.
- learn.tta() fails on a learner imported with load_learner() ([#2764](https://github.com/fastai/fastai/issues/2764))
- learn.summary() crashes out on 2nd transfer learning ([#2735](https://github.com/fastai/fastai/issues/2735))

## 2.0.12

### Bugs Squashed

- Undo breaking `num_workers` fix ([#2804](https://github.com/fastai/fastai/pull/2804))

## 2.0.11

### Bugs Squashed

- Fix `cont_cat_split` for multi-label classification ([#2759](https://github.com/fastai/fastai/issues/2759))
- fastbook error: "index 3 is out of bounds for dimension 0 with size 3" ([#2792](https://github.com/fastai/fastai/issues/2792))

## 2.0.10

### New Features

- update for fastcore 1.0.5 ([#2775](https://github.com/fastai/fastai/issues/2775))

## 2.0.6

### New Features

- "Remove pandas min version requirement" ([#2765](https://github.com/fastai/fastai/issues/2765))
- Modify XResNet to support Conv1d / Conv3d ([#2744](https://github.com/fastai/fastai/issues/2744))
  - Also support different input dimensions, kernel sizes and stride (added parameters ndim, ks, stride).
- Add support for multidimensional arrays for RNNDropout ([#2737](https://github.com/fastai/fastai/issues/2737))
- MCDropoutCallback to enable Monte Carlo Dropout in fastai. ([#2733](https://github.com/fastai/fastai/issues/2733))
  - A new callback to enable Monte Carlo Dropout in fastai in the `get_preds` method.
    Monte Carlo Dropout is simply enabling dropout during inference.
    Calling get_preds multiple times and stacking them yield of a distribution of predictions that you can use to evaluate your prediction uncertainty.
- adjustable workers in `get_preds` ([#2721](https://github.com/fastai/fastai/issues/2721))

## Version 2.0.0

- Initial release of v2


---

## CONTRIBUTING

# How to contribute to fastai

First, thanks a lot for wanting to help! Make sure you have read the [doc on code style](
https://docs.fast.ai/dev/style.html) first. (Note that we don't follow PEP8, but instead follow a coding style designed specifically for numerical and interactive programming.) For help running and building the code, see the [developers guide](https://docs.fast.ai/dev/develop.html).

## Note for new contributors from Jeremy

It can be tempting to jump into a new project by questioning the stylistic decisions that have been made, such as naming, formatting, and so forth. This can be especially so for python programmers contributing to this project, which is unusual in following a number of conventions that are common in other programming communities, but not in Python. However, please don’t do this, for (amongst others) the following reasons:

- Contributing to [Parkinson’s law of triviality](https://www.wikiwand.com/en/Law_of_triviality) has negative consequences for a project. Let’s focus on deep learning!
- It’s exhausting to repeat the same discussion over and over again, especially when it’s been well documented already. When you have a question about the project, please check the pages in the docs website linked here.
- You’re likely to get a warmer welcome from the community if you start out by contributing something that’s been requested on the forum, since you’ll be solving someone’s current problem.
- If you start out by just telling us your point of view, rather than studying the background behind the decisions that have been made, you’re unlikely to be contributing anything new or useful.
- I’ve been writing code for nearly 40 years now, across dozens of languages, and other folks involved have quite a bit of experience too - the approaches used are based on significant experience and research. Whilst there’s always room for improvement, it’s much more likely you’ll be making a positive contribution if you spend a few weeks studying and working within the current framework before suggesting wholesale changes.

## How to get started

Here are some ways that you can learn a lot about the library, whilst also contributing to the community:

- Pick a class, function, or method and write tests for it. For instance, here are the tests for [fastai.core](https://github.com/fastai/fastai1/blob/master/tests/test_core.py). Adding tests for anything without good test coverage is a great way to really understand that part of the library deeply, and have in-depth conversations with the dev team about the reasoning behind decisions in the code.
- Document something that is currently undocumented. You can find them by looking for the “new methods” section in any doc notebook. Here’s a [search](https://github.com/fastai/fastai/search?q=%22new+methods%22&unscoped_q=%22new+methods%22) that lists them
- Add an example of use to the docs for something that doesn’t currently have an example of use. We’d like everything soon in the docs to include an actual piece of working code demonstrating it. Currently, we’ve largely only provided working examples for stuff higher up the abstraction ladder.

## Did you find a bug?

* Nobody is perfect, especially not us. But first, please double-check the bug doesn't come from something on your side. The [forum](http://forums.fast.ai/) is a tremendous source for help, and we'd advise to use it as a first step. Be sure to include as much code as you can so that other people can easily help you.
* Then, ensure the bug was not already reported by searching on GitHub under [Issues](https://github.com/fastai/fastai/issues).
* If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/fastai/fastai/issues/new). Be sure to include a title and clear description, as much relevant information as possible, and a code sample or an executable test case demonstrating the expected behavior that is not occurring.
* Be sure to add the complete error messages as well as the result of the line `import fastai.test_utils; fastai.test_utils.show_install(1)`.

#### Did you write a patch that fixes a bug?

* Open a new GitHub pull request with the patch.
* Ensure that your PR includes tests that fail without your patch, and pass with it.
* Ensure the PR description clearly describes the problem and solution. Include the relevant issue number if applicable.
* Before submitting, please be sure you abide by our [coding style](https://docs.fast.ai/dev/style.html) and [the guide on abbreviations](https://docs.fast.ai/dev/abbr.html) and clean-up your code accordingly.

## Do you intend to add a new feature or change an existing one?

* You can suggest your change on the [fastai forum](http://forums.fast.ai/) to see if others are interested or want to help. [This topic](http://forums.fast.ai/t/fastai-v1-adding-features/23041/8) lists the features that will be added to fastai in the foreseeable future. Be sure to read it too!
* Before implementing a non-trivial new feature, first create a notebook version of your new feature, like those in [dev_nb](https://github.com/fastai/fastai_docs/tree/master/dev_nb). It should show step-by-step what your code is doing, and why, with the result of each step. Try to simplify the code as much as possible. When you're happy with it, let us know on the forum (include a link to gist with your notebook.)
* Once your approach has been discussed and confirmed on the forum, you are welcome to push a PR, including a complete description of the new feature and an example of how it's used. Be sure to document your code and read the [doc on code style](https://docs.fast.ai/dev/style.html) and [the one on abbreviations](https://docs.fast.ai/dev/abbr.html).
* Ensure that your PR includes tests that exercise not only your feature, but also any other code that might be impacted. Currently we have poor test coverage of existing features, so often you'll need to add tests of existing code. Your help here is much appreciated!

## How to submit notebook PRs?

Please run [`nbdev_install_hooks`](https://nbdev.fast.ai/api/clean.html#nbdev_install_hooks) in your terminal after cloning the repository. This sets up git hooks, which clean up the notebooks to remove the extraneous stuff stored in the notebooks (e.g. which cells you ran) which causes unnecessary merge conflicts.

If you made a change to the notebooks in one of the exported cells, you can export it to the library with [`nbdev_export`](https://nbdev.fast.ai/api/doclinks.html#nbdev_export).
If you made a change to the library, you can export it back to the notebooks with [`nbdev_update`](https://nbdev.fast.ai/api/sync.html#nbdev_update).

Furthermore, you can run tests in parallel by launching [`nbdev_test`](https://nbdev.fast.ai/api/test.html#nbdev_test).

If you'd like to learn the nbdev commands available and more about the project, please visit [`the docs`](https://nbdev.fast.ai/getting_started.html#how-to-use-nbdev).


## PR submission guidelines

* Keep each PR focused. While it's more convenient, do not combine several unrelated fixes together. Create as many branches as needing to keep each PR focused.

* Do not mix style changes/fixes with "functional" changes. It's very difficult to review such PRs and it most likely get rejected.

* Do not add/remove vertical whitespace. Preserve the original style of the file you edit as much as you can.

* Do not turn an already submitted PR into your development playground. If after you submitted PR, you discovered that more work is needed - close the PR, do the required work and then submit a new PR. Otherwise each of your commits requires attention from maintainers of the project.

* If, however, you submitted a PR and received a request for changes, you should proceed with commits inside that PR, so that the maintainer can see the incremental fixes and won't need to review the whole PR again. In the exception case where you realize it'll take many many commits to complete the requests, then it's probably best to close the PR, do the work and then submit it again. Use common sense where you'd choose one way over another.


### Code PRs

* If your PR is a bug fix, please also include a test that demonstrates the problem, or modifies an existing test that wasn't catching that problem already. Of course, it's not a requirement, so proceed anyway if you can't figure out how to write a test, but do try. Without having a test your fix could be lost down the road. By supplying a test, you're ensuring that your projects won't break in the future.

* Same applies for PRs that implement new features - without having a test case validating this new feature, it'd be very easy for that new feature to break in the future. A test case ensures that the feature will not break.


## Do you have questions about the source code?

* Please ask it on the [fastai forum](http://forums.fast.ai/) (after searching someone didn't ask the same one before with a quick search). We'd rather have the maximum of discussions there so that the largest number can benefit from it.

## Do you want to contribute to the documentation?

* Docs are automatically created from the notebooks in the `/nbs` directory.
* To switch the `docs` submodule to ssh, `cd docs && git remote set-url origin git@github.com:fastai/fastai-docs.git`

---

## README

# Welcome to fastai


<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

[![CI](https://github.com/fastai/fastai/actions/workflows/main.yml/badge.svg)](https://github.com/fastai/fastai/actions/workflows/main.yml)
[![PyPI](https://img.shields.io/pypi/v/fastai?color=blue&label=pypi%20version.png)](https://pypi.org/project/fastai/#description)
[![Conda (channel
only)](https://img.shields.io/conda/vn/fastai/fastai?color=seagreen&label=conda%20version.png)](https://anaconda.org/fastai/fastai)

## Installing

You can use fastai without any installation by using [Google
Colab](https://colab.research.google.com/). In fact, every page of this
documentation is also available as an interactive notebook - click “Open
in colab” at the top of any page to open it (be sure to change the Colab
runtime to “GPU” to have it run fast!) See the fast.ai documentation on
[Using Colab](https://course19.fast.ai/start_colab.html) for more
information.

You can install fastai on your own machines with: `pip install fastai`.

To ensure that you have the best available version of PyTorch on your
machine, recommend
[installing](https://pytorch.org/get-started/locally/) that first.

If you plan to develop fastai yourself, or want to be on the cutting
edge, you can use an editable install (if you do this, you should also
use an editable install of
[fastcore](https://github.com/fastai/fastcore) to go with it.) First
install PyTorch, and then:

    git clone https://github.com/fastai/fastai
    pip install -e "fastai[dev]"

## Learning fastai

The best way to get started with fastai (and deep learning) is to read
[the
book](https://www.amazon.com/Deep-Learning-Coders-fastai-PyTorch/dp/1492045527),
and complete [the free course](https://course.fast.ai).

To see what’s possible with fastai, take a look at the [Quick
Start](https://docs.fast.ai/quick_start.html), which shows how to use
around 5 lines of code to build an image classifier, an image
segmentation model, a text sentiment model, a recommendation system, and
a tabular model. For each of the applications, the code is much the
same.

Read through the [Tutorials](https://docs.fast.ai/tutorial.html) to
learn how to train your own models on your own datasets. Use the
navigation sidebar to look through the fastai documentation. Every
class, function, and method is documented here.

To learn about the design and motivation of the library, read the [peer
reviewed paper](https://www.mdpi.com/2078-2489/11/2/108/htm).

## About fastai

fastai is a deep learning library which provides practitioners with
high-level components that can quickly and easily provide
state-of-the-art results in standard deep learning domains, and provides
researchers with low-level components that can be mixed and matched to
build new approaches. It aims to do both things without substantial
compromises in ease of use, flexibility, or performance. This is
possible thanks to a carefully layered architecture, which expresses
common underlying patterns of many deep learning and data processing
techniques in terms of decoupled abstractions. These abstractions can be
expressed concisely and clearly by leveraging the dynamism of the
underlying Python language and the flexibility of the PyTorch library.
fastai includes:

- A new type dispatch system for Python along with a semantic type
  hierarchy for tensors
- A GPU-optimized computer vision library which can be extended in pure
  Python
- An optimizer which refactors out the common functionality of modern
  optimizers into two basic pieces, allowing optimization algorithms to
  be implemented in 4–5 lines of code
- A novel 2-way callback system that can access any part of the data,
  model, or optimizer and change it at any point during training
- A new data block API
- And much more…

fastai is organized around two main design goals: to be approachable and
rapidly productive, while also being deeply hackable and configurable.
It is built on top of a hierarchy of lower-level APIs which provide
composable building blocks. This way, a user wanting to rewrite part of
the high-level API or add particular behavior to suit their needs does
not have to learn how to use the lowest level.

<img alt="Layered API" src="images/layered.png" width="345">

## Migrating from other libraries

It’s very easy to migrate from plain PyTorch, Ignite, or any other
PyTorch-based library, or even to use fastai in conjunction with other
libraries. Generally, you’ll be able to use all your existing data
processing code, but will be able to reduce the amount of code you
require for training, and more easily take advantage of modern best
practices. Here are migration guides from some popular libraries to help
you on your way:

- [Plain PyTorch](https://docs.fast.ai/examples/migrating_pytorch.html)
- [Ignite](https://docs.fast.ai/examples/migrating_ignite.html)
- [Lightning](https://docs.fast.ai/examples/migrating_lightning.html)
- [Catalyst](https://docs.fast.ai/examples/migrating_catalyst.html)

## Windows Support

Due to python multiprocessing issues on Jupyter and Windows,
`num_workers` of `Dataloader` is reset to 0 automatically to avoid
Jupyter hanging. This makes tasks such as computer vision in Jupyter on
Windows many times slower than on Linux. This limitation doesn’t exist
if you use fastai from a script.

See [this
example](https://github.com/fastai/fastai/blob/master/nbs/examples/dataloader_spawn.py)
to fully leverage the fastai API on Windows.

We recommend using Windows Subsystem for Linux (WSL) instead – if you do
that, you can use the regular Linux installation approach, and you won’t
have any issues with `num_workers`.

## Tests

To run the tests in parallel, launch:

`nbdev_test`

For all the tests to pass, you’ll need to install the dependencies
specified as part of dev_requirements in settings.ini

`pip install -e .[dev]`

Tests are written using `nbdev`, for example see the documentation for
`test_eq`.

## Contributing

After you clone this repository, make sure you have run
`nbdev_install_hooks` in your terminal. This install Jupyter and git
hooks to automatically clean, trust, and fix merge conflicts in
notebooks.

After making changes in the repo, you should run `nbdev_prepare` and
make additional and necessary changes in order to pass all the tests.

## Docker Containers

For those interested in official docker containers for this project,
they can be found
[here](https://github.com/fastai/docker-containers#fastai).

---

