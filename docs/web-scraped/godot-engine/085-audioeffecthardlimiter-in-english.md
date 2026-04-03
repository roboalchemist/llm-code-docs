# AudioEffectHardLimiter in English

# AudioEffectHardLimiter
Inherits:AudioEffect<Resource<RefCounted<Object
Adds a hard limiter audio effect to an Audio bus.

## Description
A limiter is an effect designed to disallow sound from going over a given dB threshold. Hard limiters predict volume peaks, and will smoothly apply gain reduction when a peak crosses the ceiling threshold to prevent clipping and distortion. It preserves the waveform and prevents it from crossing the ceiling threshold. Adding one in the Master bus is recommended as a safety measure to prevent sudden volume peaks from occurring, and to prevent distortion caused by clipping.

## Tutorials
- Audio buses
Audio buses

## Properties

| float | ceiling_db | -0.3 |
|---|---|---|
| float | pre_gain_db | 0.0 |
| float | release | 0.1 |

float
ceiling_db
-0.3
float
pre_gain_db
float
release

## Property Descriptions
floatceiling_db=-0.3🔗
- voidset_ceiling_db(value:float)
voidset_ceiling_db(value:float)
- floatget_ceiling_db()
floatget_ceiling_db()
The waveform's maximum allowed value, in decibels. This value can range from-24.0to0.0.
The default value of-0.3prevents potential inter-sample peaks (ISP) from crossing over 0 dB, which can cause slight distortion on some older hardware.
floatpre_gain_db=0.0🔗
- voidset_pre_gain_db(value:float)
voidset_pre_gain_db(value:float)
- floatget_pre_gain_db()
floatget_pre_gain_db()
Gain to apply before limiting, in decibels.
floatrelease=0.1🔗
- voidset_release(value:float)
voidset_release(value:float)
- floatget_release()
floatget_release()
Time it takes in seconds for the gain reduction to fully release.

## User-contributed notes
Please read theUser-contributed notes policybefore submitting a comment.