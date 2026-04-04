# dasp_peak Documentation
# Source: https://docs.rs/dasp_peak/latest/dasp_peak/

# Crate dasp_peakCopy item path

[Source](../src/dasp_peak/lib.rs.html#1-100)

Expand description

Peak envelope detection over a signal.

## Structs§

[FullWave](struct.FullWave.html "struct dasp_peak::FullWave")

    A signal rectifier that produces the absolute amplitude from samples.
[NegativeHalfWave](struct.NegativeHalfWave.html "struct
dasp_peak::NegativeHalfWave")

    A signal rectifier that produces only the negative samples.
[PositiveHalfWave](struct.PositiveHalfWave.html "struct
dasp_peak::PositiveHalfWave")

    A signal rectifier that produces only the positive samples.

## Traits§

[Rectifier](trait.Rectifier.html "trait dasp_peak::Rectifier")

    Types that may be used to rectify a signal of frames `F` for a `Peak` detector.

## Functions§

[full_wave](fn.full_wave.html "fn dasp_peak::full_wave")

    A signal rectifier that produces the absolute amplitude from samples.
[negative_half_wave](fn.negative_half_wave.html "fn
dasp_peak::negative_half_wave")

    A signal rectifier that produces only the negative samples.
[positive_half_wave](fn.positive_half_wave.html "fn
dasp_peak::positive_half_wave")

    A signal rectifier that produces only the positive samples.

