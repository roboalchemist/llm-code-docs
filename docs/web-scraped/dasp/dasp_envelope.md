# dasp_envelope Documentation
# Source: https://docs.rs/dasp_envelope/latest/dasp_envelope/

# Crate dasp_envelopeCopy item path

[Source](../src/dasp_envelope/lib.rs.html#1-30)

Expand description

An abstraction supporting different kinds of envelope detection.

  * The [**Detect**](./trait.Detect.html) trait provides an abstraction for generalising over types of envelope detection.
  * The [**Detector**](./struct.Detector.html) type allows for applying a **Detect** implementation in order to detect the envelope of a signal.

See the `dasp_signal` crate (or `dasp::signal` module) **SignalWindow** trait
for a convenient way to detect envelopes over arbitrary signals.

#### §Optional Features

  * The **peak** feature (or **envelope-peak** feature if using `dasp`) provides a peak envelope detection implementation.
  * The **rms** feature (or **envelope-rms** feature if using `dasp`) provides an RMS envelope detection implementation.

#### §no_std

If working in a `no_std` context, you can disable the default **std** feature
with `--no-default-features`.

To enable all of the above features in a `no_std` context, enable the **all-
no-std** feature.

## Re-exports§

`pub use self::detect::[Detect](detect/trait.Detect.html "trait
dasp_envelope::detect::Detect");`

`pub use self::detect::[Detector](detect/struct.Detector.html "struct
dasp_envelope::detect::Detector");`

## Modules§

[detect](detect/index.html "mod dasp_envelope::detect")

