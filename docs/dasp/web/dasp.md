# dasp Documentation
# Source: https://docs.rs/dasp/latest/dasp/

# Crate daspCopy item path

[Source](../src/dasp/lib.rs.html#1-116)

Expand description

**dasp** (formerly known as _**sample**_) is a suite of crates providing the
fundamentals for working with pulse-code modulation **digital audio signal
processing**. In other words, **dasp** provides a suite of low-level, high-
performance tools including types, traits and functions for working with
digital audio signals.

Each of the **dasp** crates are re-exported under their respective
[modules](file:///home/mindtree/programming/rust/dasp/target/doc/dasp/index.html#modules).

### §Highlights

The following are some of the more interesting items within the dasp
collection:

  * Use the [**Sample** trait](./trait.Sample.html) to remain generic across bit-depth.
  * Use the [**Frame** trait](./frame/trait.Frame.html) to remain generic over channel layout.
  * Use the [**Signal** trait](./signal/trait.Signal.html) for working with **Iterators** that yield **Frames**.
  * See the [**signal** module](./signal/index.html) for a collection of interesting signal constructors (e.g. `sine`, `noise`, `from_iter`, etc).
  * Use the [**slice** module](./slice/index.html) for working with slices of **Samples** and **Frames**.
  * See the [**sample::types** module](./sample/types/index.html) for provided custom sample types.
  * See the [**Converter** type](./signal/interpolate/struct.Converter.html) for sample rate conversion and scaling.
  * See the [**ring_buffer** module](./ring_buffer/index.html) for fast FIFO queue options.

### §Optional Features

By default, only the **sample** and **frame** modules and their respective
traits are included within this crate. You may pick and choose between the
following features for additional functionality.

  * The **all** feature enables all of the following features.
  * The **std** feature enables the std library. This is enabled by default.
  * The **all-no-std** feature enables all of the following features (without std).

The following features map to each of the sub-crates and their respective
features.

  * The **envelope** feature enables the `dasp_envelope` crate via the [envelope](./envelope/index.html) module. 
    * The **envelope-peak** feature enables peak envelope detection.
    * The **envelope-rms** feature enables RMS envelope detection.
  * The **interpolate** feature enables the `dasp_interpolate` crate via the [interpolate](./interpolate/index.html) module. 
    * The **interpolate-floor** feature enables a floor interpolation implementation.
    * The **interpolate-linear** feature enables a linear interpolation implementation.
    * The **interpolate-sinc** feature enables a sinc interpolation implementation.
  * The **peak** feature enables the `dasp_peak` crate via the [peak](./peak/index.html) module.
  * The **ring_buffer** feature enables the `dasp_ring_buffer` crate via the [ring_buffer](./peak/index.html) module.
  * The **rms** feature enables the `dasp_rms` crate via the [rms](./rms/index.html) module.
  * The **signal** feature enables the `dasp_signal` crate via the [signal](./signal/index.html) module. 
    * The **signal-boxed** feature enables an implementation of **Signal** for `Box<dyn Signal>`.
    * The **signal-bus** feature enables the [**SignalBus**](./signal/bus/trait.SignalBus.html) trait.
    * The **signal-envelope** feature enables the [**SignalEnvelope**](./signal/envelope/trait.SignalEnvelope.html) trait.
    * The **signal-rms** feature enables the [**SignalRms**](./signal/rms/trait.SignalRms.html) trait.
    * The **signal-window** feature enables the [**signal::window**](./signal/window/index.html) module.
    * The **signal-window-hanning** enables the [**signal::window::hanning**](./signal/window/fn.hanning.html) window constructor.
    * The **signal-window-rectangle** enables the [**signal::window::rectangle**](./signal/window/fn.rectangle.html) window constructor.
  * The **slice** feature enables the `dasp_slice` crate via the [slice](./slice/index.html) module. 
    * The **slice-boxed** feature enables boxed slice conversion traits and functions.
  * The **window** feature enables the `dasp_window` crate via the [window](./window/index.html) module. 
    * The **window-hanning** feature enables the [**Hanning**](./window/struct.Hanning.html) window implementation.
    * The **window-rectangle** feature enables the [**Rectangle**](./window/struct.Rectangle.html) window implementation.

You can also enable all of the above features with the `--all-features` flag.

#### §no_std

If working in a `no_std` context, you can disable the default **std** feature
with `--no-default-features`.

To enable all of the above features in a `no_std` context, enable the **all-
no-std** feature.

## Modules§

[envelope](envelope/index.html "mod dasp::envelope")

    An abstraction supporting different kinds of envelope detection.
[frame](frame/index.html "mod dasp::frame")

    Use the [**Frame**](./trait.Frame.html) trait to remain generic over the number of channels at a single discrete moment in time.
[interpolate](interpolate/index.html "mod dasp::interpolate")

    An abstraction for sample/frame rate interpolation.
[peak](peak/index.html "mod dasp::peak")

    Peak envelope detection over a signal.
[ring_buffer](ring_buffer/index.html "mod dasp::ring_buffer")

    Items related to the implementation of ring buffers.
[rms](rms/index.html "mod dasp::rms")

    Root mean square calculation over a signal.
[sample](sample/index.html "mod dasp::sample")

    Use the [**Sample**](./trait.Sample.html) trait to remain generic over sample types, easily access sample type conversions, apply basic audio operations and more.
[signal](signal/index.html "mod dasp::signal")

    Use the [**Signal**](./trait.Signal.html) trait to abstract over infinite-iterator-like types that yield **Frame** s. The **Signal** trait provides methods for adding, scaling, offsetting, multiplying, clipping, generating frame iterators and more.
[slice](slice/index.html "mod dasp::slice")

    For working with slices of PCM audio data.
[window](window/index.html "mod dasp::window")

    Module for windowing over a batch of Frames. Includes default Hanning and Rectangle window types.

## Traits§

[Frame](trait.Frame.html "trait dasp::Frame")

    Represents one sample from each channel at a single discrete instance in time within a PCM signal.
[Sample](trait.Sample.html "trait dasp::Sample")

    A trait for working generically across different **Sample** format types.
[Signal](trait.Signal.html "trait dasp::Signal")

    Types that yield `Frame`s of a one-or-more-channel PCM signal.

