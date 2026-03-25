# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Processing blocks

Extracting meaningful features from your data is crucial to building small and reliable machine learning models, and in Edge Impulse this is done through processing blocks. We ship a number of processing blocks for common sensor data (such as vibration and audio):

* [Audio MFE](/studio/projects/processing-blocks/blocks/audio-mfe)
* [Audio MFCC](/studio/projects/processing-blocks/blocks/audio-mfcc)
* [Audio Syntiant](/studio/projects/processing-blocks/blocks/audio-syntiant)
* [EEG](/studio/projects/processing-blocks/blocks/eeg)
* [Flatten](/studio/projects/processing-blocks/blocks/flatten)
* [HR/HRV features](/studio/projects/processing-blocks/blocks/hr-hrv)
* [Image](/studio/projects/processing-blocks/blocks/image)
* [IMU Syntiant](/studio/projects/processing-blocks/blocks/imu-syntiant)
* [Raw Data](/studio/projects/processing-blocks/blocks/raw-data)
* [Spectral features](/studio/projects/processing-blocks/blocks/spectral-analysis)
* [Spectrogram](/studio/projects/processing-blocks/blocks/spectrogram)

The source code of these blocks are available in the [Edge Impulse processing blocks GitHub repository](https://github.com/edgeimpulse/processing-blocks).

## Custom processing blocks

If you have a very specific sensor, want to apply custom filters, or are implementing the latest research in digital signal processing, follow our tutorial on [Building custom processing blocks](/tutorials/topics/feature-extraction/build-custom-processing-blocks).

## Feature importance

In most of our DSP blocks, you have the option to calculate the **feature importance**. Edge Impulse Studio will then output a Feature Importance list that will help you determine which axes generated from your DSP block are most significant to analyze when you want to train a model.

<Warning>
  #### Feature importance

  For feature importance to work, you must have at least two labeled classes in your training dataset
</Warning>

<Frame caption="Features importance">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-features-importance-gmm.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=a2b507c5f53c3d92706d38dc92aa499a" width="877" height="1000" data-path=".assets/images/studio-features-importance-gmm.png" />
</Frame>

This process of generating features and determining the most important features of your data will further reduce the amount of signal analysis needed on the device with new and unseen data.

To calculate the feature importance, a [RandomForestClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html) is trained on the data and the `feature_importances_` are extracted from the trained classifier.

## Data normalization

In some cases, you may want to normalize your data before training a model. This is especially useful when your data has different scales or units, as it can help improve the performance of your model.

**Normalize features**

<Frame caption="Normalize features">
  <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/normalization/enable.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=0e4b4773a3ea8f53500ba59e7b84b902" width="1494" height="1000" data-path=".assets/images/normalization/enable.png" />
</Frame>

To enable data normalization, you can use the **Normalize features** option in the processing blocks generate features tab. This will learn the mean and standard deviation of each output column during the feature generation step, and apply a normalization step during training and inference.

### Why normalize?

Machine-learning algorithms assume every input dimension has a comparable numeric range.
Large differences (e.g., temperature ∈ \[–10, 40] vs. vibration RMS ∈ \[0, 2 000]) make the optimiser search in a distorted space, slowing training and sometimes letting one feature dominate the loss.

Many Edge Impulse DSP blocks already emit values with bounded ranges (e.g., image pixels are auto-normalised to 0–1 ), but generic numeric or multi-sensor pipelines typically are not. With the **Normalize features** option we can ensure that all features are on a similar scale, which can lead to better model performance.

<Tabs>
  <Tab title="Before normalization 94.6%">
    <Frame caption="Training run without scaling">
      <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/normalization/before.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=3b50ee6220d46fa91da14c45ff728eb5" width="1588" height="1000" data-path=".assets/images/normalization/before.png" />
    </Frame>
  </Tab>

  <Tab title="After normalization 99.1%">
    <Frame caption="Training run with scaling">
      <img src="https://mintcdn.com/edgeimpulse/JEriF3YpqtMjSUxH/.assets/images/normalization/after.png?fit=max&auto=format&n=JEriF3YpqtMjSUxH&q=85&s=76abdd6413a7b8fe367d10111736c792" width="1588" height="1000" data-path=".assets/images/normalization/after.png" />
    </Frame>
  </Tab>
</Tabs>

As shown in the example above, normalizing the data can significantly improve the model's performance, leading to higher accuracy and lower loss.

See the Scikit-learn documentation on [StandardScaler docs](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html) for more information on how normalization works.


Built with [Mintlify](https://mintlify.com).