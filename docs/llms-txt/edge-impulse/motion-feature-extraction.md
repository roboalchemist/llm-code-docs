# Source: https://docs.edgeimpulse.com/knowledge/concepts/data-engineering/motion-feature-extraction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Motion feature extraction

Motion feature extraction is a key component in many applications, including activity recognition, gesture control, and vibration analysis. In this concept article, we'll explore the basics of motion feature extraction, its importance, and how to implement it using Edge Impulse, specifically for Edge AI use cases. At Edge Impulse, when speaking about feature extraction techniques, we also use the terms DSP (Digital Signal Processing) or pre-processing.

## What is motion feature extraction?

Motion feature extraction involves transforming raw motion sensor data (such as accelerometer or gyroscope readings) into a set of meaningful features that can be used for further processing or analysis. These features capture essential characteristics of the motion signal, such as its frequency content, amplitude, and temporal dynamics.

## Why is motion feature extraction important?

Raw motion data is often too complex and voluminous to be directly used for machine learning tasks. Feature extraction simplifies the motion signal, making it easier to analyze and interpret. This process helps in reducing the dimensionality of the data while retaining the most informative aspects, improving the performance of machine learning models, especially in Edge AI applications where computational resources are limited.

## Motion features extraction with Edge Impulse

Edge Impulse offers a powerful **[Spectral Features](/studio/projects/processing-blocks/blocks/spectral-analysis)** block to extract key motion features, simplifying the development process for Edge AI applications. This block supports two main types of analysis:

* **Fast Fourier Transform (FFT)**: Transforms the time-domain signal into the frequency domain, providing information about the signal's frequency content. It is best suited for analyzing repetitive patterns in a signal.
* **Wavelet Transform**: Decomposes the signal into components at various scales, capturing both frequency and temporal information. It works better for complex signals that have transients or irregular waveforms.

<Tabs>
  <Tab title="FFT">
    <Frame caption="FFT">
      <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-spectral-parameters.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=e9f206b35eeca853e01e18894363d3cb" width="1556" height="1000" data-path=".assets/images/studio-spectral-parameters.png" />
    </Frame>
  </Tab>

  <Tab title="Wavelet">
    <Frame caption="Wavelet">
      <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-spectral-features-wavelets-2.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=1059b4488164e5188b22cade357b9bfe" width="1600" height="973" data-path=".assets/images/studio-spectral-features-wavelets-2.png" />
    </Frame>
  </Tab>
</Tabs>

Note that you can also import your own feature extraction block so you can use it directly in Edge Impulse Studio. See [Custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks).


Built with [Mintlify](https://mintlify.com).