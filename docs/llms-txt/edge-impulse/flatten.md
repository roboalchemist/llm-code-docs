# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks/blocks/flatten.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Flatten

**The Flatten** block performs statistical analysis on the signal. It is useful for slow-moving averages like temperature data, in combination with other blocks.

GitHub repository containing all DSP block code: [edgeimpulse/processing-blocks](https://github.com/edgeimpulse/processing-blocks).

## Flatten parameters

**Normalize features**

To enable data normalization, you can use the **Normalize features** option in the processing blocks **generate features** tab. This will learn the mean and standard deviation of each output column during the feature generation step, and apply a normalization step during training and inference.

<Frame caption="Normalize features">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/normalization/enable.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=0e4b4773a3ea8f53500ba59e7b84b902" width="1494" height="1000" data-path=".assets/images/normalization/enable.png" />
</Frame>

When enabled, the block learns the mean and standard deviation of every output column during **Generate features**, then applies a normalization step at training and inference. Recommended when raw numeric ranges differ by more than \~10×. see [Why normalize?](/studio/projects/processing-blocks#why-normalize) for more details.

**Scaling**

* Scale axes: Multiplies axes by this number

**Method**

* Average: Calculates the average value for the window
* Minimum: Calculates the minimum value in the window
* Maximum: Calculates the maximum value in the window
* Root-mean square: Calculates the RMS value of the window
* Standard deviation: Calculates the standard deviation of the window
* Skewness: Calculates the skewness of the window
* Kurtosis: Calculates the kurtosis of the window
* Moving Average Number of Windows: Calculates the moving average by maintaining a rolling average of the last N windows.  Note, there is no zero padding, the block will accumulate averages up to N windows. (Ex. for the first window in a sample, the moving average will equal the average).  The moving average resets for each sample during training, and during inference, when run\_classifier\_init() is called.  Note if you enable this, you probably don't want overlapping windows for training.

## How does the flatten block work?

<Frame caption="Flatten concept">
  <img src="https://mintcdn.com/edgeimpulse/pJSWdGs0WnFDtO8T/.assets/images/ei-concept-animations/dsp_block_flatten.gif?s=e012ed9a05ccefb2c48d01c11b94a1b9" width="1200" height="720" data-path=".assets/images/ei-concept-animations/dsp_block_flatten.gif" />
</Frame>

The **Flatten** block first rescales axes of the signal if value is different than 1. Then statistical analysis is performed on each window, computing between 1 and 8 features for each axis, depending on the number of selected methods.


Built with [Mintlify](https://mintlify.com).