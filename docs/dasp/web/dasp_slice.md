# dasp_slice Documentation
# Source: https://docs.rs/dasp_slice/latest/dasp_slice/

# Crate dasp_sliceCopy item path

[Source](../src/dasp_slice/lib.rs.html#1-361)

Expand description

For working with slices of PCM audio data.

Items related to conversion between slices of frames and slices of samples,
particularly useful for working with interleaved data.

#### §Optional Features

  * The **boxed** feature (or **slice-boxed** feature if using `dasp`) provides a suite of boxed slice conversion traits and functions under the [**boxed**](./boxed/index.html) module.

#### §no_std

If working in a `no_std` context, you can disable the default **std** feature
with `--no-default-features`.

## Re-exports§

`pub use boxed::[from_boxed_frame_slice](boxed/fn.from_boxed_frame_slice.html
"fn dasp_slice::boxed::from_boxed_frame_slice");`

`pub use
boxed::[from_boxed_sample_slice](boxed/fn.from_boxed_sample_slice.html "fn
dasp_slice::boxed::from_boxed_sample_slice");`

`pub use boxed::[to_boxed_frame_slice](boxed/fn.to_boxed_frame_slice.html "fn
dasp_slice::boxed::to_boxed_frame_slice");`

`pub use boxed::[to_boxed_sample_slice](boxed/fn.to_boxed_sample_slice.html
"fn dasp_slice::boxed::to_boxed_sample_slice");`

`pub use boxed::[DuplexBoxedFrameSlice](boxed/trait.DuplexBoxedFrameSlice.html
"trait dasp_slice::boxed::DuplexBoxedFrameSlice");`

`pub use
boxed::[DuplexBoxedSampleSlice](boxed/trait.DuplexBoxedSampleSlice.html "trait
dasp_slice::boxed::DuplexBoxedSampleSlice");`

`pub use boxed::[DuplexBoxedSlice](boxed/trait.DuplexBoxedSlice.html "trait
dasp_slice::boxed::DuplexBoxedSlice");`

`pub use boxed::[FromBoxedFrameSlice](boxed/trait.FromBoxedFrameSlice.html
"trait dasp_slice::boxed::FromBoxedFrameSlice");`

`pub use boxed::[FromBoxedSampleSlice](boxed/trait.FromBoxedSampleSlice.html
"trait dasp_slice::boxed::FromBoxedSampleSlice");`

`pub use boxed::[ToBoxedFrameSlice](boxed/trait.ToBoxedFrameSlice.html "trait
dasp_slice::boxed::ToBoxedFrameSlice");`

`pub use boxed::[ToBoxedSampleSlice](boxed/trait.ToBoxedSampleSlice.html
"trait dasp_slice::boxed::ToBoxedSampleSlice");`

## Modules§

[boxed](boxed/index.html "mod dasp_slice::boxed")

    Items related to boxed-slice conversions.

## Traits§

[DuplexFrameSlice](trait.DuplexFrameSlice.html "trait
dasp_slice::DuplexFrameSlice")

    For converting to and from a slice of `Frame`s.
[DuplexFrameSliceMut](trait.DuplexFrameSliceMut.html "trait
dasp_slice::DuplexFrameSliceMut")

    For converting to and from a mutable slice of `Frame`s.
[DuplexSampleSlice](trait.DuplexSampleSlice.html "trait
dasp_slice::DuplexSampleSlice")

    For converting to and from a slice of `Sample`s.
[DuplexSampleSliceMut](trait.DuplexSampleSliceMut.html "trait
dasp_slice::DuplexSampleSliceMut")

    For converting to and from a mutable slice of `Sample`s.
[DuplexSlice](trait.DuplexSlice.html "trait dasp_slice::DuplexSlice")

    For converting to and from a slice of `Sample`s of type `S` and a slice of `Frame`s of type `F`.
[DuplexSliceMut](trait.DuplexSliceMut.html "trait dasp_slice::DuplexSliceMut")

    For converting to and from a mutable slice of `Sample`s of type `S` and a slice of `Frame`s of type `F`.
[FromFrameSlice](trait.FromFrameSlice.html "trait dasp_slice::FromFrameSlice")

    For converting from a slice of `Frame`s to a slice of `Sample`s.
[FromFrameSliceMut](trait.FromFrameSliceMut.html "trait
dasp_slice::FromFrameSliceMut")

    For converting from a slice of `Frame`s to a slice of `Sample`s.
[FromSampleSlice](trait.FromSampleSlice.html "trait
dasp_slice::FromSampleSlice")

    For converting from a slice of `Sample`s to a slice of `Frame`s.
[FromSampleSliceMut](trait.FromSampleSliceMut.html "trait
dasp_slice::FromSampleSliceMut")

    For converting from a mutable slice of `Sample`s to a mutable slice of `Frame`s.
[ToFrameSlice](trait.ToFrameSlice.html "trait dasp_slice::ToFrameSlice")

    For converting from a slice of `Sample`s to a slice of `Frame`s.
[ToFrameSliceMut](trait.ToFrameSliceMut.html "trait
dasp_slice::ToFrameSliceMut")

    For converting from a mutable slice of `Sample`s to a mutable slice of `Frame`s.
[ToSampleSlice](trait.ToSampleSlice.html "trait dasp_slice::ToSampleSlice")

    For converting from a slice of `Frame`s to a slice of `Sample`s.
[ToSampleSliceMut](trait.ToSampleSliceMut.html "trait
dasp_slice::ToSampleSliceMut")

    For converting from a mutable slice of `Frame`s to a mutable slice of `Sample`s.

## Functions§

[add_in_place](fn.add_in_place.html "fn dasp_slice::add_in_place")

    Adds every sample in slice `b` to every sample in slice `a` respectively.
[add_in_place_with_amp_per_channel](fn.add_in_place_with_amp_per_channel.html
"fn dasp_slice::add_in_place_with_amp_per_channel")

    Scale the amplitude of each frame in `b` by `amp_per_channel` before summing it onto `a`.
[equilibrium](fn.equilibrium.html "fn dasp_slice::equilibrium")

    Sets the slice of frames at the associated `Sample`’s equilibrium value.
[from_frame_slice](fn.from_frame_slice.html "fn dasp_slice::from_frame_slice")

    Converts the given slice of `Frame`s into some slice `T`.
[from_frame_slice_mut](fn.from_frame_slice_mut.html "fn
dasp_slice::from_frame_slice_mut")

    Converts the given slice of mutable `Frame`s into some mutable slice `T`.
[from_sample_slice](fn.from_sample_slice.html "fn
dasp_slice::from_sample_slice")

    Converts the given slice of `Sample`s into some slice `T`.
[from_sample_slice_mut](fn.from_sample_slice_mut.html "fn
dasp_slice::from_sample_slice_mut")

    Converts the given mutable slice of `Sample`s into some mutable slice `T`.
[map_in_place](fn.map_in_place.html "fn dasp_slice::map_in_place")

    Mutate every element in the slice with the given function.
[to_frame_slice](fn.to_frame_slice.html "fn dasp_slice::to_frame_slice")

    Converts the given slice into a slice of `Frame`s.
[to_frame_slice_mut](fn.to_frame_slice_mut.html "fn
dasp_slice::to_frame_slice_mut")

    Converts the given mutable slice into a mutable slice of `Frame`s.
[to_sample_slice](fn.to_sample_slice.html "fn dasp_slice::to_sample_slice")

    Converts the given slice into a slice of `Sample`s.
[to_sample_slice_mut](fn.to_sample_slice_mut.html "fn
dasp_slice::to_sample_slice_mut")

    Converts the given mutable slice of `Frame`s into a mutable slice of `Sample`s.
[write](fn.write.html "fn dasp_slice::write")

    Writes every sample in slice `b` to slice `a`.
[zip_map_in_place](fn.zip_map_in_place.html "fn dasp_slice::zip_map_in_place")

    Mutate every frame in slice `a` while reading from each frame in slice `b` in lock-step using the given function.

