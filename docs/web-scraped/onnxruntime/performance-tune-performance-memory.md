# Source: https://onnxruntime.ai/docs/performance/tune-performance/memory.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#reduce-memory-consumption) Reduce memory consumption

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Shared arena based allocator](#shared-arena-based-allocator)
- [mimalloc allocator usage](#mimalloc-allocator-usage)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#shared-arena-based-allocator) Shared arena based allocator

Memory consumption can be reduced between multiple sessions by configuring the shared arena based allocation. See the `Share allocator(s) between sessions` section in the [C API documentation](/docs/get-started/with-c.html).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#mimalloc-allocator-usage) mimalloc allocator usage

ONNX Runtime supports overriding memory allocations using [mimalloc](https://github.com/microsoft/mimalloc), a fast, general-purpose allocator.

Depending on your model and usage, it can deliver single- or double-digit improvements in performance. The GitHub README page describes various scenarios on how mimalloc can be leveraged for performance tuning.

mimalloc is a submodule in the ONNX Runtime source tree. On Windows, one can employ the `--use_mimalloc` build flag which builds a static version of mimalloc and links it to ONNX Runtime. This redirects ONNX Runtime allocators and all new/delete calls to mimalloc. Currently, there are no special provisions to employ mimalloc on Linux. It is recommended to use the LD_PRELOAD mechanism using pre-built binaries of mimalloc that you can build/obtain separately.