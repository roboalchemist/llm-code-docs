# Source: https://docs.edgeimpulse.com/studio/projects/processing-blocks/blocks/audio-mfcc.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Audio MFCC

The **Audio MFCC** blocks extracts coefficients from an audio signal. Similarly to the [Audio MFE block](/studio/projects/processing-blocks/blocks/audio-mfe), it uses a non-linear scale called Mel-scale. It is the reference block for speech recognition and can also perform well on some non-human voice use cases.

GitHub repository containing all DSP block code: [edgeimpulse/processing-blocks](https://github.com/edgeimpulse/processing-blocks).

<Frame caption="MFCC parameters overview">
  <img src="https://mintcdn.com/edgeimpulse/sFtdfPhSpbLZ2-cz/.assets/images/studio-mfcc-parameters.png?fit=max&auto=format&n=sFtdfPhSpbLZ2-cz&q=85&s=48ae65c0475a97485a83e00a15aacdaf" width="1600" height="990" data-path=".assets/images/studio-mfcc-parameters.png" />
</Frame>

### Feature output format

The "Processed features" array has the following format:

* Column major, from low cepstrum to high.
* Number of rows will be equal to the parameter "Number of coefficients" (or number of cepstra)
* Each column represents a single frame

### Audio MFCC parameters

<Info>
  #### Compatible with the DSP Autotuner

  Picking the right parameters for DSP algorithms can be difficult. It often requires a lot of experience and experimenting. The autotuning function makes this process easier by looking at the entire dataset and recommending a set of parameters that is tuned for your dataset.
</Info>

**Mel Frequency Cepstral Coefficients**

* Number of coefficients: Number of cepstral coefficients to keep after applying Discrete Cosine Transform
* Frame length: The length of each frame in seconds
* Frame stride: The step between successive frame in seconds
* Filter number: The number of triangular filters applied to the spectrogram
* FFT length: The FFT size
* Low frequency: Lowest band edge of Mel-scale filterbanks
* High frequency: Highest band edge of Mel-scale filterbanks
* Window size: The size of sliding window for local cepstral mean normalization. Windows size must be odd.

**Pre-emphasis**

* Coefficient: The pre-emphasizing coefficient to apply to the input signal (0 equals to no filtering)
* Note: Shift has been removed and set to 1 for all future projects. Older & existing projects can still change this value or use an existing value.

### How does the MFCC block work?

The features' extractions adds one extra step to the [MFE block](/studio/projects/processing-blocks/blocks/audio-mfe) resulting in a compressed representation of the filterbanks. A Discrete Cosine Transform is applied on each filterbank to extract cepstral coefficients. 13 coefficients are usually retained, the rest are discarded as they represent fast changes not useful for speech recognition.


Built with [Mintlify](https://mintlify.com).