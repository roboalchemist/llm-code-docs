:github_url: hide



# AudioEffectSpectrumAnalyzer

**Inherits:** [AudioEffect<class_AudioEffect>] **<** [Resource<class_Resource>] **<** [RefCounted<class_RefCounted>] **<** [Object<class_Object>]

Audio effect that can be used for real-time audio visualizations.


## Description

This audio effect does not affect sound output, but can be used for real-time audio visualizations.

This resource configures an [AudioEffectSpectrumAnalyzerInstance<class_AudioEffectSpectrumAnalyzerInstance>], which performs the actual analysis at runtime. An instance can be obtained with [AudioServer.get_bus_effect_instance()<class_AudioServer_method_get_bus_effect_instance>].

See also [AudioStreamGenerator<class_AudioStreamGenerator>] for procedurally generating sounds.


## Tutorials

- [Audio Spectrum Visualizer Demo ](https://godotengine.org/asset-library/asset/2762)_


## Properties

> **TABLE**
> :widths: auto
>
> +----------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>`                                | :ref:`buffer_length<class_AudioEffectSpectrumAnalyzer_property_buffer_length>` | ``2.0``  |
> +----------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>` | :ref:`fft_size<class_AudioEffectSpectrumAnalyzer_property_fft_size>`           | ``2``    |
> +----------------------------------------------------------+--------------------------------------------------------------------------------+----------+
> | :ref:`float<class_float>`                                | :ref:`tap_back_pos<class_AudioEffectSpectrumAnalyzer_property_tap_back_pos>`   | ``0.01`` |
> +----------------------------------------------------------+--------------------------------------------------------------------------------+----------+
>

----


## Enumerations



enum **FFTSize**: [🔗<enum_AudioEffectSpectrumAnalyzer_FFTSize>]



[FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **FFT_SIZE_256** = `0`

Use a buffer of 256 samples for the Fast Fourier transform. Lowest latency, but least stable over time.



[FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **FFT_SIZE_512** = `1`

Use a buffer of 512 samples for the Fast Fourier transform. Low latency, but less stable over time.



[FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **FFT_SIZE_1024** = `2`

Use a buffer of 1024 samples for the Fast Fourier transform. This is a compromise between latency and stability over time.



[FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **FFT_SIZE_2048** = `3`

Use a buffer of 2048 samples for the Fast Fourier transform. High latency, but stable over time.



[FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **FFT_SIZE_4096** = `4`

Use a buffer of 4096 samples for the Fast Fourier transform. Highest latency, but most stable over time.



[FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **FFT_SIZE_MAX** = `5`

Represents the size of the [FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] enum.


----


## Property Descriptions



[float<class_float>] **buffer_length** = `2.0` [🔗<class_AudioEffectSpectrumAnalyzer_property_buffer_length>]


- |void| **set_buffer_length**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_buffer_length**\ (\ )

The length of the buffer to keep (in seconds). Higher values keep data around for longer, but require more memory.


----



[FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **fft_size** = `2` [🔗<class_AudioEffectSpectrumAnalyzer_property_fft_size>]


- |void| **set_fft_size**\ (\ value\: [FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>]\ )
- [FFTSize<enum_AudioEffectSpectrumAnalyzer_FFTSize>] **get_fft_size**\ (\ )

The size of the [Fast Fourier transform ](https://en.wikipedia.org/wiki/Fast_Fourier_transform)_ buffer. Higher values smooth out the spectrum analysis over time, but have greater latency. The effects of this higher latency are especially noticeable with sudden amplitude changes.


----



[float<class_float>] **tap_back_pos** = `0.01` [🔗<class_AudioEffectSpectrumAnalyzer_property_tap_back_pos>]


- |void| **set_tap_back_pos**\ (\ value\: [float<class_float>]\ )
- [float<class_float>] **get_tap_back_pos**\ (\ )

> **CONTAINER**
>
	There is currently no description for this property. Please help us by [contributing one ](https://contributing.godotengine.org/en/latest/documentation/class_reference.html)_!

