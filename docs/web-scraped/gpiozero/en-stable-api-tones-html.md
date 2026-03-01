# Source: https://gpiozero.readthedocs.io/en/stable/api_tones.html

Title: Tones — gpiozero 2.0.1 Documentation

URL Source: https://gpiozero.readthedocs.io/en/stable/api_tones.html

Markdown Content:
22. API - Tones[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#module-gpiozero.tones "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

GPIO Zero includes a [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") class intended for use with the [`TonalBuzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "gpiozero.TonalBuzzer"). This class is in the `tones` module of GPIO Zero and is typically imported as follows:

from gpiozero.tones import Tone

22.1. Tone[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#tone "Link to this heading")
---------------------------------------------------------------------------------------------------

_class_ gpiozero.tones.Tone(_value=None_, _*_, _frequency=None_, _midi=None_, _note=None_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tones.html#Tone)[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "Link to this definition")
Represents a frequency of sound in a variety of musical notations.

[`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") class can be used with the [`TonalBuzzer`](https://gpiozero.readthedocs.io/en/stable/api_output.html#gpiozero.TonalBuzzer "gpiozero.TonalBuzzer") class to easily represent musical tones. The class can be constructed in a variety of ways. For example as a straight frequency in [Hz](https://en.wikipedia.org/wiki/Hertz) (which is the internal storage format), as an integer MIDI note, or as a string representation of a musical note.

All the following constructors are equivalent ways to construct the typical tuning note, [concert A](https://en.wikipedia.org/wiki/Concert_pitch) at 440Hz, which is MIDI note #69:

>>> from gpiozero.tones import Tone
>>> Tone(440.0)
>>> Tone(69)
>>> Tone('A4')

If you do not want the constructor to guess which format you are using (there is some ambiguity between frequencies and MIDI notes at the bottom end of the frequencies, from 128Hz down), you can use one of the explicit constructors, [`from_frequency()`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.from_frequency "gpiozero.tones.Tone.from_frequency"), [`from_midi()`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.from_midi "gpiozero.tones.Tone.from_midi"), or [`from_note()`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.from_note "gpiozero.tones.Tone.from_note"), or you can specify a keyword argument when constructing:

>>> Tone.from_frequency(440)
>>> Tone.from_midi(69)
>>> Tone.from_note('A4')
>>> Tone(frequency=440)
>>> Tone(midi=69)
>>> Tone(note='A4')

Several attributes are provided to permit conversion to any of the supported construction formats: [`frequency`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.frequency "gpiozero.tones.Tone.frequency"), [`midi`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.midi "gpiozero.tones.Tone.midi"), and [`note`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.note "gpiozero.tones.Tone.note"). Methods are provided to step [`up()`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.up "gpiozero.tones.Tone.up") or [`down()`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.down "gpiozero.tones.Tone.down") to adjacent MIDI notes.

Warning

Currently [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") derives from [`float`](https://docs.python.org/3.9/library/functions.html#float "(in Python v3.9)") and can be used as a floating point number in most circumstances (addition, subtraction, etc). This part of the API is not yet considered “stable”; i.e. we may decide to enhance / change this behaviour in future versions.

down(_n=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tones.html#Tone.down)[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.down "Link to this definition")
Return the [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone")_n_ semi-tones below this frequency (_n_ defaults to 1).

_classmethod_ from_frequency(_freq_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tones.html#Tone.from_frequency)[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.from_frequency "Link to this definition")
Construct a [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") from a frequency specified in [Hz](https://en.wikipedia.org/wiki/Hertz) which must be a positive floating-point value in the range 0 < freq <= 20000.

_classmethod_ from_midi(_midi\_note_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tones.html#Tone.from_midi)[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.from_midi "Link to this definition")
Construct a [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") from a MIDI note, which must be an integer in the range 0 to 127. For reference, A4 ([concert A](https://en.wikipedia.org/wiki/Concert_pitch) typically used for tuning) is MIDI note #69.

_classmethod_ from_note(_note_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tones.html#Tone.from_note)[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.from_note "Link to this definition")
Construct a [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone") from a musical note which must consist of a capital letter A through G, followed by an optional semi-tone modifier (“b” for flat, “#” for sharp, or their Unicode equivalents), followed by an octave number (0 through 9).

For example [concert A](https://en.wikipedia.org/wiki/Concert_pitch), the typical tuning note at 440Hz, would be represented as “A4”. One semi-tone above this would be “A#4” or alternatively “Bb4”. Unicode representations of sharp and flat are also accepted.

up(_n=1_)[[source]](https://gpiozero.readthedocs.io/en/stable/_modules/gpiozero/tones.html#Tone.up)[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.up "Link to this definition")
Return the [`Tone`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone "gpiozero.tones.Tone")_n_ semi-tones above this frequency (_n_ defaults to 1).

_property_ frequency[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.frequency "Link to this definition")
Return the frequency of the tone in [Hz](https://en.wikipedia.org/wiki/Hertz).

_property_ midi[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.midi "Link to this definition")
Return the (nearest) MIDI note to the tone’s frequency. This will be an integer number in the range 0 to 127. If the frequency is outside the range represented by MIDI notes (which is approximately 8Hz to 12.5KHz) [`ValueError`](https://docs.python.org/3.9/library/exceptions.html#ValueError "(in Python v3.9)") exception will be raised.

_property_ note[](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.note "Link to this definition")
Return the (nearest) note to the tone’s frequency. This will be a string in the form accepted by [`from_note()`](https://gpiozero.readthedocs.io/en/stable/api_tones.html#gpiozero.tones.Tone.from_note "gpiozero.tones.Tone.from_note"). If the frequency is outside the range represented by this format (“A0” is approximately 27.5Hz, and “G9” is approximately 12.5Khz) a [`ValueError`](https://docs.python.org/3.9/library/exceptions.html#ValueError "(in Python v3.9)") exception will be raised.
