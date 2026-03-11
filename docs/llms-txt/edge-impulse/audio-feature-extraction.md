# Source: https://docs.edgeimpulse.com/knowledge/concepts/data-engineering/audio-feature-extraction.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio feature extraction

Audio feature extraction is a crucial step in many audio-based applications, including speech recognition, music analysis, and environmental sound classification. In this concept article, we'll explore the basics of audio feature extraction, its importance, and how to implement it using Edge Impulse, particularly for Edge AI use cases. At Edge Impulse, when speaking about feature extraction techniques, we also use the terms DSP (Digital Signal Processing) or pre-processing.

## What is audio feature extraction?

Audio feature extraction involves transforming raw audio signals into a set of meaningful features that can be used for further processing or analysis, including training Edge AI models. These features capture essential characteristics of the audio signal, such as its frequency content, amplitude, and temporal dynamics.

## Why is audio feature extraction important?

Raw audio data is often too complex and voluminous to be directly used for machine learning tasks. Feature extraction simplifies the audio signal, making it easier to analyze and interpret. This process helps in reducing the dimensionality of the data while retaining the most informative aspects, improving the performance of machine learning models, especially in Edge AI applications where computational resources are limited.

## Audio features extraction techniques with Edge Impulse

Edge Impulse offers several pre-processing blocks to extract key audio features, simplifying the development process for Edge AI applications:

1. **Spectrogram**: A visual representation of the spectrum of frequencies in a signal as it varies with time. It helps in understanding how the energy of the signal is distributed across different frequencies. See the [Spectrogram pre-processing block](/studio/projects/processing-blocks/blocks/spectrogram) in Edge Impulse.
2. **Mel-Frequency Cepstral Coefficients (MFCC)**: Represent the short-term power spectrum of a sound, widely used in speech and audio processing due to their effectiveness in capturing the phonetically relevant characteristics of the audio signal. See the [MFCC block](/studio/projects/processing-blocks/blocks/audio-mfcc) in Edge Impulse.
3. **Mel-filterbank Energy (MFE)**: Similar to MFCCs but focuses on the energy in different frequency bands, providing a simpler yet powerful representation of the audio signal. See the [MFE block](/studio/projects/processing-blocks/blocks/audio-mfe) in Edge Impulse.

<Tabs>
  <Tab title="Spectrogram">
    <Frame caption="Spectrogram parameters overview">
      <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-spectrogram-parameters.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=396c09a7d29798494148436a892257fa" width="1600" height="793" data-path=".assets/images/studio-spectrogram-parameters.png" />
    </Frame>
  </Tab>

  <Tab title="MFCC">
    <Frame caption="MFCC parameters overview">
      <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-mfcc-parameters.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=48ae65c0475a97485a83e00a15aacdaf" width="1600" height="990" data-path=".assets/images/studio-mfcc-parameters.png" />
    </Frame>
  </Tab>

  <Tab title="MFE">
    <Frame caption="MFE parameters overview">
      <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-mfe-parameters.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=8a86bc0dcb73343ddf0b74a6e15f88e2" width="1600" height="919" data-path=".assets/images/studio-mfe-parameters.png" />
    </Frame>
  </Tab>
</Tabs>

Note that you can also import your own feature extraction block so you can use it directly in Edge Impulse Studio. See [Custom processing blocks](/studio/organizations/custom-blocks/custom-processing-blocks).

## Other resources

Tutorials:

* Keyword Spotting: [Keyword spotting](/tutorials/end-to-end/keyword-spotting)
* Continuous Audio Classification: [Sound recognition](/tutorials/end-to-end/sound-recognition)

Blog posts:

* [Even Better Audio Classification with Our New DSP Blocks](https://www.edgeimpulse.com/blog/even-better-audio-classification-with-our-new-dsp-blocks/)
* [How Hyfe Is Transforming Coughs into Actionable Data with Edge Impulse](https://www.edgeimpulse.com/blog/how-hyfe-is-transforming-coughs-into-actionable-data-with-edge-impulse/)


Built with [Mintlify](https://mintlify.com).