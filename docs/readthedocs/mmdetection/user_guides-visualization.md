# Visualization

Before reading this tutorial, it is recommended to read MMEngine’s Visualization [https://github.com/open-mmlab/mmengine/blob/main/docs/en/advanced_tutorials/visualization.md] documentation to get a first glimpse of the `Visualizer` definition and usage.

In brief, the `Visualizer` is implemented in MMEngine to meet the daily visualization needs, and contains three main functions:

- 

Implement common drawing APIs, such as `draw_bboxes` which implements bounding box drawing functions, `draw_lines` implements the line drawing function.

- 

Support writing visualization results, learning rate curves, loss function curves, and verification accuracy curves to various backends, including local disks and common deep learning training logging tools such as TensorBoard [https://www.tensorflow.org/tensorboard] and Wandb [https://wandb.ai/site].

- 

Support calling anywhere in the code to visualize or record intermediate states of the model during training or testing, such as feature maps and validation results.

Based on MMEngine’s Visualizer, MMDet comes with a variety of pre-built visualization tools that can be used by the user by simply modifying the following configuration files.

- 

The `tools/analysis_tools/browse_dataset.py` script provides a dataset visualization function that draws images and corresponding annotations after Data Transforms, as described in `browse_dataset.py`.

- 

MMEngine implements `LoggerHook`, which uses `Visualizer` to write the learning rate, loss and evaluation results to the backend set by `Visualizer`. Therefore, by modifying the `Visualizer` backend in the configuration file, for example to ` TensorBoardVISBackend` or `WandbVISBackend`, you can implement logging to common training logging tools such as `TensorBoard` or `WandB`, thus making it easy for users to use these visualization tools to analyze and monitor the training process.

- 

The `VisualizerHook` is implemented in MMDet, which uses the `Visualizer` to visualize or store the prediction results of the validation or prediction phase into the backend set by the `Visualizer`, so by modifying the `Visualizer` backend in the configuration file, for example, to ` TensorBoardVISBackend` or `WandbVISBackend`, you can implement storing the predicted images to `TensorBoard` or `Wandb`.

## Configuration

Thanks to the use of the registration mechanism, in MMDet we can set the behavior of the `Visualizer` by modifying the configuration file. Usually, we define the default configuration for the visualizer in `configs/_base_/default_runtime.py`, see configuration tutorial for details.

```
vis_backends = [dict(type='LocalVisBackend')]
visualizer = dict(
    type='DetLocalVisualizer',
    vis_backends=vis_backends,
    name='visualizer')

```