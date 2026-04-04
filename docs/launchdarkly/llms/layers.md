# Source: https://launchdarkly.com/docs/api/layers.md

> ### Available for customers using Experimentation
>
> Layers are available to customers using [Experimentation](https://launchdarkly.com/docs/api/experiments).

There are some cases in which you may not want to include a context in more than one experiment at a time. For example, you may be concerned about collisions between experiments that are testing similar parts of your app, like two different changes to the same section of your app's user interface (UI), or experiments running on both the back end and front end of the same functionality. In this case you can eliminate the interaction effect between experiments using layers.

A layer contains a set of experiments that cannot share traffic with each other. All of the experiments within a layer are mutually exclusive, which means that if a context is included in one experiment, LaunchDarkly will exclude it from any other experiments in the same layer.

To learn more, read [Mutually exclusive experiments](https://launchdarkly.com/docs/home/experimentation/mutually-exclusive).
