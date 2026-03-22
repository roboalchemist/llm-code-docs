# OVERVIEW

This chapter introduces you to the framework of MMDetection, and provides links to detailed tutorials about MMDetection.

## What is MMDetection

MMDetection is an object detection toolbox that contains a rich set of object detection, instance segmentation, and panoptic segmentation methods as well as related components and modules, and below is its whole framework:

MMDetection consists of 7 main parts, apis, structures, datasets, models, engine, evaluation and visualization.

- 

**apis** provides high-level APIs for model inference.

- 

**structures** provides data structures like bbox, mask, and DetDataSample.

- 

**datasets** supports various dataset for object detection, instance segmentation, and panoptic segmentation.

  - 

**transforms** contains a lot of useful data augmentation transforms.

  - 

**samplers** defines different data loader sampling strategy.

- 

**models** is the most vital part for detectors and contains different components of a detector.

  - 

**detectors** defines all of the detection model classes.

  - 

**data_preprocessors** is for preprocessing the input data of the model.

  - 

**backbones** contains various backbone networks.

  - 

**necks** contains various neck components.

  - 

**dense_heads** contains various detection heads that perform dense predictions.

  - 

**roi_heads** contains various detection heads that predict from RoIs.

  - 

**seg_heads** contains various segmentation heads.

  - 

**losses** contains various loss functions.

  - 

**task_modules** provides modules for detection tasks. E.g. assigners, samplers, box coders, and prior generators.

  - 

**layers** provides some basic neural network layers.

- 

**engine** is a part for runtime components.

  - 

**runner** provides extensions for MMEngine’s runner [https://mmengine.readthedocs.io/en/latest/tutorials/runner.html].

  - 

**schedulers** provides schedulers for adjusting optimization hyperparameters.

  - 

**optimizers** provides optimizers and optimizer wrappers.

  - 

**hooks** provides various hooks of the runner.

- 

**evaluation** provides different metrics for evaluating model performance.

- 

**visualization** is for visualizing detection results.