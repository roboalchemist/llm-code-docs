# Source: https://docs.edgeimpulse.com/studio/projects/eon-tuner.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# EON Tuner

The EON Tuner is a powerful engineering tool that helps you find and select the best performing impulses for your application, given your hardware target resource constraints. This saves you the time and effort of manually creating experiments and allows you to explore a parameter search space more efficiently.

On top of being hardware aware by taking into account the RAM, flash, and inference time for your selected device, one aspect of the EON Tuner that sets it apart from other tuners is that it includes parameter selection for your input and processing blocks in addition to model hyperparameters for your learning block; it is not simply another model hyperparameter tuner. This allows you to optimize your feature extraction in conjunction with your model, ensuring the two are closely paired.

<iframe src="https://www.youtube.com/embed/RrwpEwcXjhg" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<br />

<iframe src="https://www.youtube.com/embed/Gbl-ZnF8Ax0" title="YouTube video player" className="w-full aspect-video rounded-xl" frameborder="0" allowFullScreen />

<Info>
  The videos above show a previous version of the EON Tuner. The Studio user interface and the EON Tuner configuration, operation, and results have since been updated. However, the videos provide relevant background information and are still worth watching, even though you will come across differences in your projects today.
</Info>

## Overview

The EON Tuner explores a user defined parameter search space to perform end-to-end impulse optimizations, from the input block, to the processing block, learning block, and even additional configurations such as data augmentation, to help you find the ideal trade-off between options for these block, their associated parameters, and your target hardware resources constraints.

The exploration of a specific search space is called an EON Tuner run. Each run consists of a number of trials, with each trial being a variation of the input, processing, and learning block options and their parameter values that had been specified in the search space. After the creation of several trials, the training and testing of each one is then scheduled and executed, with several trials being completed in parallel.

<Frame caption="EON Tuner run progress">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-progress-bar.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=e3386b1fd4ec962fe81a2c0714f7b5a5" width="1538" height="1000" data-path=".assets/images/eon-tuner-progress-bar.png" />
</Frame>

During operation, the top level progress bar shows trials that have been completed (solid bar), trials that are in progress (striped bar), and trials that are pending (no fill bar).

### Search algorithm

There are several approaches to exploring a parameter search space. For example, the most common methods include: manual search, random search, grid search, and Bayesian optimization.

The EON Tuner has been updated to use Bayesian optimization (previously random search). Compared to the other techniques listed, Bayesian optimization is a more efficient and effective option. It is a "smarter" algorithm that learns from prior results by building a probabilistic model based on these results, the possible parameter values, and your objectives to determine what area of the search space to explore next. This leads to improved results in a shorter amount of time using fewer compute resources.

## Getting started

<Frame caption="EON Tuner tab">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-tab.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=d46dfb1cf4d948dbeb8b4ef5ea088a6d" width="1538" height="1000" data-path=".assets/images/eon-tuner-tab.png" />
</Frame>

To get started, first ensure there is data in your project. Then navigate to the EON Tuner, which can be found under experiments in your project. If you have not previously [configured the target](/studio/projects/dashboard/target-device) for your project, now is a great time to do so because the EON Tuner will use this information. You are now ready to configure a tuner run.

## Configuring a new run

<Frame caption="">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-new-run.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=e8e4259ed290832e132370f03a285a49" width="1538" height="1000" data-path=".assets/images/eon-tuner-new-run.png" />
</Frame>

<br />

<Frame caption="Configuring an EON Tuner run">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-configuration.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=b04af642cb59fdf0dabf19dc67a6ad12" width="1538" height="1000" data-path=".assets/images/eon-tuner-configuration.png" />
</Frame>

To configure a new run, click the `New run` button. This will launch a modal window where you can adjust the settings for the run. In this modal, you will be able to set the name, select the compute time limit, specify the run objectives, and define the parameter search space for your run.

You are able to prioritize one or more run objectives that are most relevant to your application. The objectives you set are taken into account in the Bayesian optimization algorithm. Note that an objective that is higher on the list will be weighted more heavily (given a greater importance) than the the objectives that come below it.

### Search space

For information on configuring the search space, please see the [EON Tuner search space documentation](/studio/projects/eon-tuner/search-space).

## Reviewing run results

<Frame caption="Reviewing EON Tuner results">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-results.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=86fbc36a9387fc6570a60df318f03086" width="1538" height="1000" data-path=".assets/images/eon-tuner-results.png" />
</Frame>

While the EON Tuner is running, results for trials will be shown as they become available. The run is completed when all created trials have finished or the compute time limit has been reached.

Trial summaries are shown in a visual manner that includes both the configuration and results. The trial configuration and further details about the training job can also be viewed in the trial logs. To show the logs, click the three dots for the trial and select `Show logs`. This will launch a trial logs modal window.

Trial results can be filtered based on the trial status, the processing block used, or the machine learning model used. The results can also be sorted by several metrics. Lastly, you are able to view the results for either the validation or test datasets.

These filtering, sorting, and view options are available to the right of the trial results.

## Extending a run

<Frame caption="Extending an EON Tuner run">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-extend-search.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=2b4f641cc63087b01d98882f1d56cb3a" width="1538" height="1000" data-path=".assets/images/eon-tuner-extend-search.png" />
</Frame>

If you would like to perform more trials for the given parameter search space, or if a trial did not complete because you reached your defined compute limit, you can extend a run. To do so, click the `Extend search` button located above the the trial results.

<Frame caption="Extending an EON Tuner run not recommended">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-extend-search-not-recommended.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=4b2f6df7dd70f71d6e6113204d827aa0" width="1538" height="1000" data-path=".assets/images/eon-tuner-extend-search-not-recommended.png" />
</Frame>

There may come a time where an optimal configuration has been reached and running more trials would provide diminishing returns if you continue to extend the search. At this point, you will receive a warning that extending the search is not recommended, as the new combinations of parameters may not lead to better results. However, you can continue to extend if you'd like.

## Adding a trial to your experiments

<Frame caption="Adding a trial to your experiments list">
  <img src="https://mintcdn.com/edgeimpulse/uHWro5V1wRm9iJRo/.assets/images/eon-tuner-add-trial.png?fit=max&auto=format&n=uHWro5V1wRm9iJRo&q=85&s=15239024ffc03ad15522144fc1779a9c" width="1538" height="1000" data-path=".assets/images/eon-tuner-add-trial.png" />
</Frame>

If you would like to add a trial to your list of experiments as an impulse, you can do so by clicking the `+ Add` button for the trial.

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional resources

* [Impulse design and experiments](/studio/projects/impulse-design)
* [EON Tuner search space](/studio/projects/eon-tuner/search-space)


Built with [Mintlify](https://mintlify.com).