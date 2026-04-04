# dasp_ring_buffer Documentation
# Source: https://docs.rs/dasp_ring_buffer/latest/dasp_ring_buffer/

# Crate dasp_ring_bufferCopy item path

[Source](../src/dasp_ring_buffer/lib.rs.html#1-893)

Expand description

Items related to the implementation of ring buffers.

The primary items of interest in this module include:

  * The [Slice](./trait.Slice.html) and [SliceMut](./trait.SliceMut.html) traits - implemented for types that may be used as the underlying buffer in `Fixed` and `Bounded` ring buffers.
  * The [Fixed](./struct.Fixed.html) ring buffer type.
  * The [Bounded](./struct.Bounded.html) ring buffer type.

## Structs§

[Bounded](struct.Bounded.html "struct dasp_ring_buffer::Bounded")

    A ring buffer with an upper bound on its length.
[DrainBounded](struct.DrainBounded.html "struct
dasp_ring_buffer::DrainBounded")

    An iterator that drains the ring buffer by `pop`ping each element one at a time.
[Fixed](struct.Fixed.html "struct dasp_ring_buffer::Fixed")

    A ring buffer with a fixed length.

## Traits§

[FixedSizeArray](trait.FixedSizeArray.html "trait
dasp_ring_buffer::FixedSizeArray")

    Types that may be used as a constant-length buffer underlying a `Bounded` ring buffer.
[Slice](trait.Slice.html "trait dasp_ring_buffer::Slice")

    Types that may be used as a data slice for `Fixed` and `Bounded` ring buffers.
[SliceMut](trait.SliceMut.html "trait dasp_ring_buffer::SliceMut")

    Types that may be used as a data slice for mutable `Fixed` and `Bounded` ring buffers.

