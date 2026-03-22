# Weight initialization

During training, a proper initialization strategy is beneficial to speeding up the training or obtaining a higher performance. MMCV [https://github.com/open-mmlab/mmcv/blob/master/mmcv/cnn/utils/weight_init.py] provide some commonly used methods for initializing modules like `nn.Conv2d`. Model initialization in MMdetection mainly uses `init_cfg`. Users can initialize models with following two steps:

- 

Define `init_cfg` for a model or its components in `model_cfg`,  but `init_cfg` of children components have higher priority and will override `init_cfg` of parents modules.

- 

Build model as usual, but call `model.init_weights()` method explicitly, and model parameters will be initialized as configuration.

The high-level workflow of initialization in MMdetection is :

model_cfg(init_cfg) -> build_from_cfg -> model -> init_weight() -> initialize(self, self.init_cfg) -> children’s init_weight()

## Description

It is dict or list[dict], and contains the following keys and values:

- 

`type` (str), containing the initializer name in `INTIALIZERS`, and followed by arguments of the initializer.

- 

`layer` (str or list[str]), containing the names of basic layers in Pytorch or MMCV with learnable parameters that will be initialized, e.g. `'Conv2d'`,`'DeformConv2d'`.

- 

`override` (dict or list[dict]),  containing the sub-modules that not inherit from BaseModule and whose initialization configuration is different from other layers’ which are in `'layer'` key. Initializer defined in `type` will work for all layers defined in `layer`, so if sub-modules are not derived Classes of `BaseModule` but can be initialized as same ways of layers in `layer`, it does not need to use `override`. `override` contains:

  - 

`type` followed by arguments of initializer;

  - 

`name` to indicate sub-module which will be initialized.