# dasp_interpolate Documentation
# Source: https://docs.rs/dasp_interpolate/latest/dasp_interpolate/

# Crate dasp_interpolateCopy item path

[Source](../src/dasp_interpolate/lib.rs.html#1-51)

Expand description

An abstraction for sample/frame rate interpolation.

The [**Interpolator**](./trait.Interpolator.html) trait provides an
abstraction over different types of rate interpolation.

See the `dasp_signal` crate (or `dasp::signal` module) **Converter** type for
a convenient way to interpolate the rate of arbitrary signals.

#### §Optional Features

  * The **floor** feature (or **interpolate-floor** feature if using `dasp`) provides a floor interpolator implementation.
  * The **linear** feature (or **interpolate-linear** feature if using `dasp`) provides a linear interpolator implementation.
  * The **sinc** feature (or **interpolate-sinc** feature if using `dasp`) provides a sinc interpolator implementation.

#### §no_std

If working in a `no_std` context, you can disable the default **std** feature
with `--no-default-features`.

To enable all of the above features in a `no_std` context, enable the **all-
no-std** feature.

## Modules§

[floor](floor/index.html "mod dasp_interpolate::floor")

    A floor interpolator implementation.
[linear](linear/index.html "mod dasp_interpolate::linear")

    A linear interpolator implementation.
[sinc](sinc/index.html "mod dasp_interpolate::sinc")

    A sinc interpolator implementation.

## Traits§

[Interpolator](trait.Interpolator.html "trait dasp_interpolate::Interpolator")

    Types that can interpolate between two values.

