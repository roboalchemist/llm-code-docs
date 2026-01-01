# dasp_signal Documentation
# Source: https://docs.rs/dasp_signal/latest/dasp_signal/

# Crate dasp_signalCopy item path

[Source](../src/dasp_signal/lib.rs.html#1-2505)

Expand description

Use the [**Signal**](./trait.Signal.html) trait to abstract over infinite-
iterator-like types that yield **Frame** s. The **Signal** trait provides
methods for adding, scaling, offsetting, multiplying, clipping, generating
frame iterators and more.

You may also find a series of **Signal** source functions, including:

  * [equilibrium](./fn.equilibrium.html) for generating “silent” frames.
  * [phase](./fn.phase.html) for a stepping phase, useful for oscillators.
  * [sine](./fn.sine.html) for generating a sine waveform.
  * [saw](./fn.saw.html) for generating a sawtooth waveform.
  * [square](./fn.square.html) for generating a square waveform.
  * [noise](./fn.noise.html) for generating a noise waveform.
  * [noise_simplex](./fn.noise_simplex.html) for generating a 1D simplex noise waveform.
  * [gen](./fn.gen.html) for generating frames of type F from some `Fn() -> F`.
  * [gen_mut](./fn.gen_mut.html) for generating frames of type F from some `FnMut() -> F`.
  * [from_iter](./fn.from_iter.html) for converting an iterator yielding frames to a signal.
  * [from_interleaved_samples_iter](./fn.from_interleaved_samples_iter.html) for converting an iterator yielding interleaved samples to a signal.

Working with **Signal** s allows for easy, readable creation of rich and
complex DSP graphs with a simple and familiar API.

#### §Optional Features

  * The **boxed** feature (or **signal-boxed** feature if using `dasp`) provides a **Signal** implementation for `Box<dyn Signal>`.
  * The **bus** feature (or **signal-bus** feature if using `dasp`) provides the [**SignalBus**](./bus/trait.SignalBus.html) trait.
  * The **envelope** feature (or **signal-envelope** feature if using `dasp`) provides the [**SignalEnvelope**](./envelope/trait.SignalEnvelope.html) trait.
  * The **rms** feature (or **signal-rms** feature if using `dasp`) provides the [**SignalRms**](./rms/trait.SignalRms.html) trait.
  * The **window** feature (or **signal-window** feature if using `dasp`) provides the [**window**](./window/index.html) module.

#### §no_std

If working in a `no_std` context, you can disable the default **std** feature
with `--no-default-features`.

To enable all of the above features in a `no_std` context, enable the **all-
no-std** feature.

## Modules§

[bus](bus/index.html "mod dasp_signal::bus")

    An extension to the **Signal** trait that enables multiple signal outputs.
[envelope](envelope/index.html "mod dasp_signal::envelope")

    An extension to the **Signal** trait that enables envelope detection.
[interpolate](interpolate/index.html "mod dasp_signal::interpolate")

    The [**Converter**](./struct.Converter.html) type for interpolating the rate of a signal.
[rms](rms/index.html "mod dasp_signal::rms")

    An extension to the **Signal** trait that monitors the RMS of a signal.
[window](window/index.html "mod dasp_signal::window")

    Items to ease the application of windowing functions to signals.

## Structs§

[AddAmp](struct.AddAmp.html "struct dasp_signal::AddAmp")

    An iterator that yields the sum of the frames yielded by both `other` and `self` in lock-step.
[BranchRcA](struct.BranchRcA.html "struct dasp_signal::BranchRcA")

    One of the two `Branch` signals returned by `Fork::by_rc`.
[BranchRcB](struct.BranchRcB.html "struct dasp_signal::BranchRcB")

    One of the two `Branch` signals returned by `Fork::by_rc`.
[BranchRefA](struct.BranchRefA.html "struct dasp_signal::BranchRefA")

    One of the two `Branch` signals returned by `Fork::by_ref`.
[BranchRefB](struct.BranchRefB.html "struct dasp_signal::BranchRefB")

    One of the two `Branch` signals returned by `Fork::by_ref`.
[Buffered](struct.Buffered.html "struct dasp_signal::Buffered")

    Buffers the signal using the given ring buffer.
[BufferedFrames](struct.BufferedFrames.html "struct
dasp_signal::BufferedFrames")

    An iterator that pops elements from the inner bounded ring buffer and yields them.
[ClipAmp](struct.ClipAmp.html "struct dasp_signal::ClipAmp")

    Clips samples in each frame yielded by `signal` to the given threshhold amplitude.
[ConstHz](struct.ConstHz.html "struct dasp_signal::ConstHz")

    A constant phase step size.
[Delay](struct.Delay.html "struct dasp_signal::Delay")

    Delays the `signal` by the given number of frames.
[Equilibrium](struct.Equilibrium.html "struct dasp_signal::Equilibrium")

    An iterator that endlessly yields `Frame`s of type `F` at equilibrium.
[Fork](struct.Fork.html "struct dasp_signal::Fork")

    Represents a forked `Signal` that has not yet been split into its two branches.
[FromInterleavedSamplesIterator](struct.FromInterleavedSamplesIterator.html
"struct dasp_signal::FromInterleavedSamplesIterator")

    An iterator that converts an iterator of `Sample`s to an iterator of `Frame`s.
[FromIterator](struct.FromIterator.html "struct dasp_signal::FromIterator")

    A type that wraps an Iterator and provides a `Signal` implementation for it.
[Gen](struct.Gen.html "struct dasp_signal::Gen")

    A signal that generates frames using the given function.
[GenMut](struct.GenMut.html "struct dasp_signal::GenMut")

    A signal that generates frames using the given function which may mutate some state.
[Hz](struct.Hz.html "struct dasp_signal::Hz")

    An iterator that yields the step size for a phase.
[Inspect](struct.Inspect.html "struct dasp_signal::Inspect")

    A signal that calls its enclosing function and returns the original value. The signal may mutate state.
[IntoInterleavedSamples](struct.IntoInterleavedSamples.html "struct
dasp_signal::IntoInterleavedSamples")

    Converts a `Signal` to a type that yields the individual interleaved samples.
[IntoInterleavedSamplesIterator](struct.IntoInterleavedSamplesIterator.html
"struct dasp_signal::IntoInterleavedSamplesIterator")

    Converts the `IntoInterleavedSamples` into an `Iterator` that always returns `Some`.
[Map](struct.Map.html "struct dasp_signal::Map")

    A signal that maps from one signal to another
[MulAmp](struct.MulAmp.html "struct dasp_signal::MulAmp")

    An iterator that yields the product of the frames yielded by both `other` and `self` in lock-step.
[MulHz](struct.MulHz.html "struct dasp_signal::MulHz")

    Multiplies the rate at which frames of `self` are yielded by the given `signal`.
[Noise](struct.Noise.html "struct dasp_signal::Noise")

    A noise signal generator.
[NoiseSimplex](struct.NoiseSimplex.html "struct dasp_signal::NoiseSimplex")

    A 1D simplex-noise generator.
[OffsetAmp](struct.OffsetAmp.html "struct dasp_signal::OffsetAmp")

    Provides an iterator that offsets the amplitude of every channel in each frame of the signal by some sample value and yields the resulting frames.
[OffsetAmpPerChannel](struct.OffsetAmpPerChannel.html "struct
dasp_signal::OffsetAmpPerChannel")

    An `Iterator` that scales the amplitude of every `Frame` in `self` by the respective amplitudes in each channel of the given `amp` `Frame`.
[Phase](struct.Phase.html "struct dasp_signal::Phase")

    An iterator that yields a phase, useful for waveforms like Sine or Saw.
[Rate](struct.Rate.html "struct dasp_signal::Rate")

    The rate at which phrase a **Signal** is sampled.
[Saw](struct.Saw.html "struct dasp_signal::Saw")

    A saw wave signal generator.
[ScaleAmp](struct.ScaleAmp.html "struct dasp_signal::ScaleAmp")

    An `Iterator` that scales the amplitude of the sample of each channel in every `Frame` yielded by `self` by the given amplitude.
[ScaleAmpPerChannel](struct.ScaleAmpPerChannel.html "struct
dasp_signal::ScaleAmpPerChannel")

    An `Iterator` that scales the amplitude of every `Frame` in `self` by the respective amplitudes in each channel of the given `amp` `Frame`.
[Sine](struct.Sine.html "struct dasp_signal::Sine")

    A sine wave signal generator.
[Square](struct.Square.html "struct dasp_signal::Square")

    A square wave signal generator.
[Take](struct.Take.html "struct dasp_signal::Take")

    An iterator that yields `n` number of `Frame`s from the inner `signal`.
[UntilExhausted](struct.UntilExhausted.html "struct
dasp_signal::UntilExhausted")

    Yields frames from the signal until the `signal.is_exhausted()` returns `true`.
[ZipMap](struct.ZipMap.html "struct dasp_signal::ZipMap")

    A signal that iterates two signals in parallel and combines them with a function.

## Traits§

[Signal](trait.Signal.html "trait dasp_signal::Signal")

    Types that yield `Frame`s of a one-or-more-channel PCM signal.
[Step](trait.Step.html "trait dasp_signal::Step")

    Types that may be used to give a phase step size based on some `hz / sample rate`.

## Functions§

[equilibrium](fn.equilibrium.html "fn dasp_signal::equilibrium")

    Provides an iterator that endlessly yields `Frame`s of type `F` at equilibrium.
[from_interleaved_samples_iter](fn.from_interleaved_samples_iter.html "fn
dasp_signal::from_interleaved_samples_iter")

    Create a new `Signal` from the given `Frame`-yielding `Iterator`.
[from_iter](fn.from_iter.html "fn dasp_signal::from_iter")

    Create a new `Signal` from the given `Frame`-yielding `Iterator`.
[gen](fn.gen.html "fn dasp_signal::gen")

    A signal that generates frames using the given function.
[gen_mut](fn.gen_mut.html "fn dasp_signal::gen_mut")

    A signal that generates frames using the given function which may mutate some state.
[lift](fn.lift.html "fn dasp_signal::lift")

    Consumes the given `Iterator`, converts it to a `Signal`, applies the given function to the `Signal` and returns an `Iterator` that will become exhausted when the consumed `Iterator` does.
[noise](fn.noise.html "fn dasp_signal::noise")

    Produces a `Signal` that yields random values between -1.0..1.0.
[noise_simplex](fn.noise_simplex.html "fn dasp_signal::noise_simplex")

    Produces a 1-dimensional simplex noise `Signal`.
[phase](fn.phase.html "fn dasp_signal::phase")

    Creates a `Phase` that continuously steps forward by the given `step` size yielder.
[rate](fn.rate.html "fn dasp_signal::rate")

    Creates a frame `Rate` (aka sample rate) representing the rate at which a signal may be sampled.
[saw](fn.saw.html "fn dasp_signal::saw")

    Produces a `Signal` that yields a saw wave oscillating at the given hz.
[sine](fn.sine.html "fn dasp_signal::sine")

    Produces a `Signal` that yields a sine wave oscillating at the given hz.
[square](fn.square.html "fn dasp_signal::square")

    Produces a `Signal` that yields a square wave oscillating at the given hz.

