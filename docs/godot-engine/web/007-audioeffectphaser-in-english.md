# AudioEffectPhaser in English

# AudioEffectPhaser

Inherits:AudioEffect<Resource<RefCounted<Object
Adds a phaser audio effect to an audio bus.
Combines the original signal with a copy that is slightly out of phase with the original.

## Description

Combines phase-shifted signals with the original signal. The movement of the phase-shifted signals is controlled using a low-frequency oscillator.

## Tutorials

- Audio buses
Audio buses

## Properties

| float | depth | 1.0 |
|---|---|---|
| float | feedback | 0.7 |
| float | range_max_hz | 1600.0 |
| float | range_min_hz | 440.0 |
| float | rate_hz | 0.5 |

float
depth
float
feedback
float
range_max_hz
1600.0
float
range_min_hz
440.0
float
rate_hz

## Property Descriptions

floatdepth=1.0🔗

- voidset_depth(value:float)
voidset_depth(value:float)
- floatget_depth()
floatget_depth()
Determines how high the filter frequencies sweep. Low value will primarily affect bass frequencies. High value can sweep high into the treble. Value can range from0.1to4.0.
floatfeedback=0.7🔗
- voidset_feedback(value:float)
voidset_feedback(value:float)
- floatget_feedback()
floatget_feedback()
Output percent of modified sound. Value can range from 0.1 to 0.9.
floatrange_max_hz=1600.0🔗
- voidset_range_max_hz(value:float)
voidset_range_max_hz(value:float)
- floatget_range_max_hz()
floatget_range_max_hz()
Determines the maximum frequency affected by the LFO modulations, in Hz. Value can range from 10 to 10000.
floatrange_min_hz=440.0🔗
- voidset_range_min_hz(value:float)
voidset_range_min_hz(value:float)
- floatget_range_min_hz()
floatget_range_min_hz()
Determines the minimum frequency affected by the LFO modulations, in Hz. Value can range from 10 to 10000.
floatrate_hz=0.5🔗
- voidset_rate_hz(value:float)
voidset_rate_hz(value:float)
- floatget_rate_hz()
floatget_rate_hz()
Adjusts the rate in Hz at which the effect sweeps up and down across the frequency range.

## User-contributed notes

Please read theUser-contributed notes policybefore submitting a comment.
