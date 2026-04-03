# AudioEffectSpectrumAnalyzerInstance

# AudioEffectSpectrumAnalyzerInstance

Inherits:AudioEffectInstance<RefCounted<Object
Queryable instance of anAudioEffectSpectrumAnalyzer.

## Description

The runtime part of anAudioEffectSpectrumAnalyzer, which can be used to query the magnitude of a frequency range on its host bus.
An instance of this class can be obtained withAudioServer.get_bus_effect_instance().

## Tutorials

- Audio Spectrum Visualizer Demo
Audio Spectrum Visualizer Demo

## Methods

| Vector2 | get_magnitude_for_frequency_range(from_hz:float, to_hz:float, mode:MagnitudeMode= 1)const |

Vector2
get_magnitude_for_frequency_range(from_hz:float, to_hz:float, mode:MagnitudeMode= 1)const

## Enumerations

enumMagnitudeMode:🔗
MagnitudeModeMAGNITUDE_AVERAGE=0
Use the average value across the frequency range as magnitude.
MagnitudeModeMAGNITUDE_MAX=1
Use the maximum value of the frequency range as magnitude.

## Method Descriptions

Vector2get_magnitude_for_frequency_range(from_hz:float, to_hz:float, mode:MagnitudeMode= 1)const🔗
Returns the magnitude of the frequencies fromfrom_hztoto_hzin linear energy as a Vector2. Thexcomponent of the return value represents the left stereo channel, andyrepresents the right channel.
modedetermines how the frequency range will be processed.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
