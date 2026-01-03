# dasp_window Documentation
# Source: https://docs.rs/dasp_window/latest/dasp_window/

# Crate dasp_window Copy item path

[Source](../src/dasp_window/lib.rs.html#1-40)

Expand description

Module for windowing over a batch of Frames. Includes default Hanning and
Rectangle window types.

#### §Optional Features

  * The **hanning** feature (or **window-hanning** feature if using `dasp`) provides the [**Hanning**](./struct.Hanning.html) window function implementation.
  * The **rectangle** feature (or **window-rectangle** feature if using `dasp`) provides the [**Rectangle**](./struct.Rectangle.html) window function implementation.

#### §no_std

If working in a `no_std` context, you can disable the default **std** feature
with `--no-default-features`.

To enable all of the above features in a `no_std` context, enable the **all-
no-std** feature.

## Structs§

[Hanning](struct.Hanning.html "struct dasp_window::Hanning")

    A type of window function, also known as the “raised cosine window”.
[Rectangle](struct.Rectangle.html "struct dasp_window::Rectangle")

    The simplest window type, equivalent to replacing all but _N_ values of data sequence by zeroes, making it appear as though the waveform suddenly turns on and off.

## Traits§

[Window](trait.Window.html "trait dasp_window::Window")

    An abstraction supporting different types of `Window` functions.

