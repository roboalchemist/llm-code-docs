# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks/blocks/audio-syntiant.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio Syntiant

The **Audio Syntiant** processing block extracts time and frequency features from a signal. It is similar to the [Audio MFE](/studio/projects/processing-blocks/blocks/audio-mfe) but performs additional processing specific to the Syntiant NDP101/120 chip. **This block can be used only with Syntiant targets.**

<Frame caption="Syntiant spectrogram of the sentence \'Hello, World\'">
  <img src="https://mintcdn.com/edgeimpulse/BnOEP1CPlKpl2ntM/.assets/images/cbd5ae2-screenshot_2021-12-02_at_101236.png?fit=max&auto=format&n=BnOEP1CPlKpl2ntM&q=85&s=45225af5219377fefbe3a976cfc23288" width="1022" height="546" data-path=".assets/images/cbd5ae2-screenshot_2021-12-02_at_101236.png" />
</Frame>

## Audio Syntiant parameters

**Log Mel-filterbank energy features**

* Frame length: The length of each frame in seconds
* Frame stride: The step between successive frame in seconds
* Filter number (fixed): The number of triangular filters applied to the spectrogram
* FFT length (fixed): The FFT size
* Low frequency (fixed): Lowest band edge of Mel-scale filterbanks
* High frequency (fixed): Highest band edge of Mel-scale filterbanks

**Preemphasis**

* Coefficient: Pre-emphasis coefficient

**Chip**

* Features extractor: Syntiant method to generate features, choose accordingly to your chip

## How does the Syntiant block work?

The features' extractions is a proprietary algorithm from Syntiant. However parameters are very close to the [Audio MFE](/studio/projects/processing-blocks/blocks/audio-mfe). *Pre-emphasis coefficient* is applied first to amplify higher frequencies. The signal is then divided in overlapping frames, defined by the *Frame length* and *Frame stride* to extract speech features.

<Info>
  #### Sampling frequency

  The Audio Syntiant block only supports a 16 kHz frequency. You can adjust the sampling frequency in the "Create Impulse" section.
</Info>


Built with [Mintlify](https://mintlify.com).