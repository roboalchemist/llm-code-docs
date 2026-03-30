# Source: https://docs.edgeimpulse.com/studio/organizations/transformation-blocks/blocks/time-series-data-augmentation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Time-series data augmentation

<Info>
  **Only available on the Enterprise plan**

  This feature is only available on the Enterprise plan. Review our [plans and pricing](https://edgeimpulse.com/pricing) or sign up for our free [expert-led trial](https://edgeimpulse.com/expert-led-trial) today.
</Info>

<Info>
  **Available as a synthetic data block**

  The time-series data augmentation block is also available as a synthetic data block. The parameters and usage are the same across both block types. For more information, see the [synthetic data](/studio/projects/data-acquisition/synthetic-data) documentation.
</Info>

In many machine learning applications, especially those involving time-series data, obtaining a large, diverse, and high-quality labeled dataset is one of the biggest hurdles. To address this, data augmentation, the process of generating new data from existing samples, has become a key strategy. However, traditional augmentation methods like adding noise, scaling, or using generative models often fail to preserve the underlying structure of time-series data.

The **Time-series data augmentation** block in Edge Impulse offers a sophisticated approach to augmenting time-series data by decomposing signals into their fundamental components, applying targeted transformations, and then recombining them to create new, structurally valid samples. This method not only enhances the diversity of the dataset but also maintains the integrity of the original signal characteristics, making it particularly effective for training robust machine learning models.

## Overview

Time-series data is often composed of three main components:

* **Trend:** Long-term progression (e.g., voltage drift in sensors)
* **Seasonality:** Repeating patterns (e.g., machine rotation cycles)
* **Residual:** Irregular short-term fluctuations (e.g., noise)

The method used in the time-series data augmentation block decomposes a time-series signal into these components, applies transformations to each component individually, and then reconstructs a new series. This ensures the augmented data retains the structural integrity of the original series.

<Frame caption="Time-series signal components">
  <img src="https://mintcdn.com/edgeimpulse/j2yv7MfG4vGZlq__/.assets/images/time-series-signal-components.png?fit=max&auto=format&n=j2yv7MfG4vGZlq__&q=85&s=119679a653c40cfe23ac438deca473db" width="1248" height="500" data-path=".assets/images/time-series-signal-components.png" />
</Frame>

The augmentation process can be thought of involving two layers: transforming components from the same series and mixing components from different series.

In the first layer, a single series is decomposed using techniques like Seasonal-Trend Decomposition using Loess (STL) or wavelet decomposition. Transformations are then applied such as:

* Amplitude scaling (e.g., increase trend magnitude)
* Time scaling (e.g., compress or stretch the seasonal cycle)
* Synchronized slicing (reorder cycles of the seasonal component with smooth transitions)

The transformed components are then recombined to synthesize a new series.

If there are multiple series from similar sources (e.g., different machines of the same origin), the augmentation can be further expanded by mixing components across series as the second layer. For example:

* Use the *trend* from Series A
* Combine it with the *seasonality* from Series B
* Add the *residual* from Series C

This creates a new series that is structurally valid but more diverse than any individual source.

## Using the block in an organization

To use the time-series data augmentation block, navigate to your [organization](/studio/organizations/dashboard) and go to the [data transformation](/studio/organizations/data-transformation) view, then select the **Create job** tab. From there, you can select the time-series data augmentation block from the transformation block dropdown menu.

<Frame caption="Selecting the time-series data augmentation block">
  <img src="https://mintcdn.com/edgeimpulse/rD87_C8D2Xqmph53/.assets/images/transformation-job-time-series-data-augmentation-block.png?fit=max&auto=format&n=rD87_C8D2Xqmph53&q=85&s=984e7b83466fbcf4af272538bc16d365" width="1538" height="1000" data-path=".assets/images/transformation-job-time-series-data-augmentation-block.png" />
</Frame>

## Block parameters

After selecting the time-series data augmentation block for a data transformation job, the block specific parameters will be shown. Each parameter is described below.

### Number of samples

The number of samples parameter specifies the number of additional data samples, per existing sample in your dataset, to generate from your original data. For example, if you have 100 samples in your dataset and you set this parameter to 4, 400 additional samples will be generated. The value must be a positive integer.

### Signal type

The signal type parameter allows you to specify whether the input time-series signal is periodic or not. If you are unsure, you can also select the `unknown` option. The option selected for this parameter aids the underlying algorithm in choosing the signal decomposition strategy.

### Divergence

Instead of manually tuning multiple augmentation parameters, you can adjust a single divergence parameter. Behind the scenes, this parameter controls amplitude and time scaling, whether to apply slicing or remixing, and the degree of transformation per component.

Higher divergence values lead to more pronounced changes, while lower values yield subtler variations. The divergence parameter accepts values between `0.0` and `1.0`.

### Remix

The remix parameter is a boolean that allows you to specify whether to mix components across different series when generating augmented data. This is only applicable if your dataset contains multiple series from similar sources (e.g., different machines of the same origin). If set to `true`, the augmentation process will randomly select components from different series to combine and create new samples, increasing the diversity of the generated data. If set to `false`, the augmentation will only transform components within the same series.

### Signal column prefix

The signal column prefix parameter allows you to specify a prefix for the time-series signals that you wish to augment. This is useful when your dataset samples contain multiple different types of time-series data.

For example, if your dataset samples contain both accelerometer and gyroscope data in the format `accel_x, accel_y, accel_z, gyro_x, gyro_y, gyro_z`, you can specify `accel` as the signal column prefix to augment the accelerometer data. At this time, it is only possible to specify a single prefix.

### Upsample factor

<Info>
  **Parameter is conditionally shown**

  The upsample factor parameter is conditionally shown based on the selection for the signal type parameter. It will be shown if the signal type is set to `periodic`.
</Info>

The decomposition strategy for periodic signals expects an integer number of data points per period. However, rarely is this true of real-world signals. The upsample factor parameter allows you to specify a value by which to upsample the input time-series signal before applying the augmentation, to reduce inaccuracies and improve performance. The output signal is then downsampled by the same factor after augmentation. The upsample factor must be a positive integer.

For example, if the period of your signal only contains 2.5 data points, you can set the upsample factor to `2`, which will make the period contain 5 data points. An upsample factor of `1` means no upsampling is applied.

If your signal contains multiple periods, apply an upsample factor for the dominant period. You may need to experiment with different upsample factors to find the best setting for your specific use case.

### Period range

<Info>
  **Parameter is conditionally shown**

  The period range parameter is conditionally shown based on the selection for the signal type parameter. It will be shown if the signal type is set to `periodic`.
</Info>

The period range parameter allows you to specify the expected range of data points per period for the input time-series signal. This information helps the underlying algorithm to accurately identify and decompose the seasonal component of the signal. The range is specified as two positive integers separated by a comma, representing the minimum and maximum expected.

## Best practices

<Steps>
  <Step title="Use high-quality input data">
    Use clean, representative examples; poor data leads to poor results. "Garbage in, garbage out" still applies.
  </Step>

  <Step title="Use consistent, single-label samples">
    This decomposition approach performs optimally when samples have uniform characteristics, with each labeled with a single class.
  </Step>

  <Step title="Start small and iterate">
    Begin with a small number of outputs and low divergence setting, and gradually explore the impact of tuning parameters.
  </Step>

  <Step title="Reach out for help">
    Whether you're debugging or scaling up, don't hesitate to reach out. We're always ready to assist.
  </Step>
</Steps>

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional resources

* [Data transformation](/studio/organizations/data-transformation)
* [Transformation blocks](/studio/organizations/transformation-blocks)
* [Custom transformation blocks](/studio/organizations/custom-blocks/custom-transformation-blocks)


Built with [Mintlify](https://mintlify.com).