# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks/blocks/eeg.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# EEG

<Info>
  **Enterprise deployment only**

  All Edge Impulse developers can access this feature for evaluation purposes. However, deployment of this feature to an edge device is only available for enterprise users. If you are an enterprise user, please contact your Solutions Engineer for deployment options.
</Info>

The **EEG** processing block allows you to preprocess electroencephalogram (EEG) data by applying signal conditioning and feature extraction.

Specifically, the EEG processing block can normalize signal levels, filter signals to remove drift, noise, and powerline interference, remove motion artifacts, and extract spectral features.

## Overview

An electroencephalogram (EEG) is a non-invasive method to record electrical activity of the brain as a time-series signal. It allows one to identify different brain waves (gamma, beta, alpha, theta, delta) and is commonly used in applications such as brain-computer interfaces, sleep monitoring, and neurological disorder diagnosis.

The EEG processing block built-in to Edge Impulse provides a comprehensive set of tools to preprocess EEG data, including:

* **Scaling**: Normalize signals to reference microvolt levels.
* **Filtering**: Bandpass and notch filters to remove drift, noise, and powerline interference.
* **Motion Artifact Removal (ATAR)**: Suppress motion artifacts using wavelet packet decomposition and soft-thresholding.
* **Multitaper Power Spectral Density (PSD)**: Robust spectral feature extraction using multitaper windowing and averaging.

## Using the block in a project

To use the EEG processing block, navigate to the *Create impulse* page within your project, then click the `Add a processing block` button, and select the EEG block from the list of blocks in the modal that appears.

After you have saved your impulse, click on the EEG block in the left hand side menu to view and edit the block parameters.

## Block parameters

<Info>
  **Compatible with the DSP Autotuner**

  Picking the right parameters for DSP algorithms can be difficult. It often requires a lot of experience and experimenting. The autotuning function makes this process easier by recommending a set of parameters that is tuned for your dataset.
</Info>

The parameters available for configuring the EEG processing block are defined below.

### Scale axes

The scale axes parameter allows you to scale the input signal to reference microvolt levels by selecting the appropriate scaling factor for your data. For example, if your EEG data is in raw ADC counts, you can select a scaling factor that converts those counts to microvolts based on your hardware specifications. The input value is a float.

### Powerline interference filter

The powerline interference filter parameter adds a notch filter that removes powerline interference at a specified frequency (e.g., 50 Hz or 60 Hz). You can select the appropriate frequency based on your region's powerline frequency. Set to 0 to disable. The input value is an integer.

### High-pass filter

The high-pass filter parameter applies a high-pass filter to remove low-frequency drift from the EEG signal. You can specify the cutoff frequency in Hz. Set to 0 to disable. The input value is a float.

### Low-pass filter

The low-pass filter parameter applies a low-pass filter to remove high-frequency noise from the EEG signal. You can specify the cutoff frequency in Hz. Set to 0 to disable. The input value is a float.

### Sensitivity

The sensitivity parameter controls the aggressiveness of motion artifact removal. Higher sensitivity values will remove more motion artifacts but may also remove some of the underlying EEG signal. Typical values are between 0 and 1. Set to 0 to disable. The input value is a float.

### Epoch length

The epoch length parameter specifies the length of the time window (analysis window) in seconds used for spectral feature extraction. Longer epochs will provide better frequency resolution but may be less responsive to changes in the signal. The input value is a float.

## Block input

The input to the EEG processing block should be a time-series signal containing EEG data. The signal should be sampled at a consistent rate and may contain multiple channels (4 or fewer) corresponding to different electrodes.

## Block output

The output from the EEG processing block is the full band multitaper power spectral density (PSD) of the input EEG signal, which is a representation of the signal's power across different frequency bands.

## Limitations

The EEG processing block is designed for use on edge devices, with limited processing power. As such, although 64 or 128 electrode channels is typical, the block was designed to target 4 or fewer.

Additionally, while the block includes motion artifact removal, it may not be able to fully clean signals with severe motion artifacts or noise contamination.

## Troubleshooting

<Info>
  No common issues have been identified thus far. If you encounter an issue, please reach out on the [forum](https://forum.edgeimpulse.com) or, if you are on the Enterprise plan, through your support channels.
</Info>

## Additional resources

* [Processing blocks](/studio/projects/processing-blocks)
* [Impulse design](/studio/projects/impulse-design)


Built with [Mintlify](https://mintlify.com).