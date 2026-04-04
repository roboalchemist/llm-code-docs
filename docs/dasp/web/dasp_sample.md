# dasp_sample Documentation
# Source: https://docs.rs/dasp_sample/latest/dasp_sample/

# Crate dasp_sampleCopy item path

[Source](../src/dasp_sample/lib.rs.html#1-324)

Expand description

Use the [**Sample**](./trait.Sample.html) trait to remain generic over sample
types, easily access sample type conversions, apply basic audio operations and
more.

The **Sample** trait is the core abstraction throughout dasp on which most
other abstractions are based.

## Re-exports§

`pub use conv::[Duplex](conv/trait.Duplex.html "trait
dasp_sample::conv::Duplex");`

`pub use conv::[FromSample](conv/trait.FromSample.html "trait
dasp_sample::conv::FromSample");`

`pub use conv::[ToSample](conv/trait.ToSample.html "trait
dasp_sample::conv::ToSample");`

`pub use types::[I24](types/i24/struct.I24.html "struct
dasp_sample::types::i24::I24");`

`pub use types::[I48](types/i48/struct.I48.html "struct
dasp_sample::types::i48::I48");`

`pub use types::[U24](types/u24/struct.U24.html "struct
dasp_sample::types::u24::U24");`

`pub use types::[U48](types/u48/struct.U48.html "struct
dasp_sample::types::u48::U48");`

## Modules§

[conv](conv/index.html "mod dasp_sample::conv")

    Pure functions and traits for converting between i8, i16, I24, i32, I48, i64, u8, u16, U24, u32, U48, u64, f32 and f64.
[types](types/index.html "mod dasp_sample::types")

    A collection of custom, non-std **Sample** types.

## Traits§

[FloatSample](trait.FloatSample.html "trait dasp_sample::FloatSample")

    Sample format types represented as floating point numbers.
[Sample](trait.Sample.html "trait dasp_sample::Sample")

    A trait for working generically across different **Sample** format types.
[SignedSample](trait.SignedSample.html "trait dasp_sample::SignedSample")

    Integral and floating-point **Sample** format types whose equilibrium is at 0.

