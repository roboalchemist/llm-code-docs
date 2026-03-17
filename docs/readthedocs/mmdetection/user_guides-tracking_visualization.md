# Learn about Visualization

## Local Visualization

This section will present how to visualize the detection/tracking results with local visualizer.

If you want to draw prediction results, you can turn this feature on by setting `draw=True` in `TrackVisualizationHook` as follows.

```
default_hooks = dict(visualization=dict(type='TrackVisualizationHook', draw=True))

```