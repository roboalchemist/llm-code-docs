# Source: https://onnxruntime.ai/docs/api/python/api_summary.html

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHN0eWxlPSJkaXNwbGF5OiBub25lOyI+CiAgPHN5bWJvbCBpZD0ic3ZnLXRvYyIgdmlld2JveD0iMCAwIDI0IDI0Ij4KICAgIDx0aXRsZT5Db250ZW50czwvdGl0bGU+CiAgICA8c3ZnIHN0cm9rZT0iY3VycmVudENvbG9yIiBmaWxsPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMCIgdmlld2JveD0iMCAwIDEwMjQgMTAyNCI+CiAgICAgIDxwYXRoIGQ9Ik00MDggNDQyaDQ4MGM0LjQgMCA4LTMuNiA4LTh2LTU2YzAtNC40LTMuNi04LTgtOEg0MDhjLTQuNCAwLTggMy42LTggOHY1NmMwIDQuNCAzLjYgOCA4IDh6bS04IDIwNGMwIDQuNCAzLjYgOCA4IDhoNDgwYzQuNCAwIDgtMy42IDgtOHYtNTZjMC00LjQtMy42LTgtOC04SDQwOGMtNC40IDAtOCAzLjYtOCA4djU2em01MDQtNDg2SDEyMGMtNC40IDAtOCAzLjYtOCA4djU2YzAgNC40IDMuNiA4IDggOGg3ODRjNC40IDAgOC0zLjYgOC04di01NmMwLTQuNC0zLjYtOC04LTh6bTAgNjMySDEyMGMtNC40IDAtOCAzLjYtOCA4djU2YzAgNC40IDMuNiA4IDggOGg3ODRjNC40IDAgOC0zLjYgOC04di01NmMwLTQuNC0zLjYtOC04LTh6TTExNS40IDUxOC45TDI3MS43IDY0MmM1LjggNC42IDE0LjQuNSAxNC40LTYuOVYzODguOWMwLTcuNC04LjUtMTEuNS0xNC40LTYuOUwxMTUuNCA1MDUuMWE4Ljc0IDguNzQgMCAwIDAgMCAxMy44eiIgLz4KICAgIDwvc3ZnPg==)

Menu

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0iZmVhdGhlci1tZW51Ij4KICAgICAgPGxpbmUgeDE9IjMiIHkxPSIxMiIgeDI9IjIxIiB5Mj0iMTIiPjwvbGluZT4KICAgICAgPGxpbmUgeDE9IjMiIHkxPSI2IiB4Mj0iMjEiIHkyPSI2Ij48L2xpbmU+CiAgICAgIDxsaW5lIHgxPSIzIiB5MT0iMTgiIHgyPSIyMSIgeTI9IjE4Ij48L2xpbmU+CiAgICA8L3N2Zz4=)

Expand

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMiIgc3Ryb2tlLWxpbmVjYXA9InJvdW5kIiBzdHJva2UtbGluZWpvaW49InJvdW5kIiBjbGFzcz0iZmVhdGhlci1jaGV2cm9uLXJpZ2h0Ij4KICAgICAgPHBvbHlsaW5lIHBvaW50cz0iOSAxOCAxNSAxMiA5IDYiPjwvcG9seWxpbmU+CiAgICA8L3N2Zz4=)

Light mode

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJmZWF0aGVyLXN1biI+CiAgICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjUiPjwvY2lyY2xlPgogICAgICA8bGluZSB4MT0iMTIiIHkxPSIxIiB4Mj0iMTIiIHkyPSIzIj48L2xpbmU+CiAgICAgIDxsaW5lIHgxPSIxMiIgeTE9IjIxIiB4Mj0iMTIiIHkyPSIyMyI+PC9saW5lPgogICAgICA8bGluZSB4MT0iNC4yMiIgeTE9IjQuMjIiIHgyPSI1LjY0IiB5Mj0iNS42NCI+PC9saW5lPgogICAgICA8bGluZSB4MT0iMTguMzYiIHkxPSIxOC4zNiIgeDI9IjE5Ljc4IiB5Mj0iMTkuNzgiPjwvbGluZT4KICAgICAgPGxpbmUgeDE9IjEiIHkxPSIxMiIgeDI9IjMiIHkyPSIxMiI+PC9saW5lPgogICAgICA8bGluZSB4MT0iMjEiIHkxPSIxMiIgeDI9IjIzIiB5Mj0iMTIiPjwvbGluZT4KICAgICAgPGxpbmUgeDE9IjQuMjIiIHkxPSIxOS43OCIgeDI9IjUuNjQiIHkyPSIxOC4zNiI+PC9saW5lPgogICAgICA8bGluZSB4MT0iMTguMzYiIHkxPSI1LjY0IiB4Mj0iMTkuNzgiIHkyPSI0LjIyIj48L2xpbmU+CiAgICA8L3N2Zz4=)

Dark mode

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJpY29uLXRhYmxlci1tb29uIj4KICAgICAgPHBhdGggc3Ryb2tlPSJub25lIiBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgICA8cGF0aCBkPSJNMTIgM2MuMTMyIDAgLjI2MyAwIC4zOTMgMGE3LjUgNy41IDAgMCAwIDcuOTIgMTIuNDQ2YTkgOSAwIDEgMSAtOC4zMTMgLTEyLjQ1NHoiIC8+CiAgICA8L3N2Zz4=)

Auto light/dark mode

![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSJjdXJyZW50Q29sb3IiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJpY29uLXRhYmxlci1zaGFkb3ciPgogICAgICA8cGF0aCBzdHJva2U9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiIGZpbGw9Im5vbmUiIC8+CiAgICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjkiPjwvY2lyY2xlPgogICAgICA8cGF0aCBkPSJNMTMgMTJoNSIgLz4KICAgICAgPHBhdGggZD0iTTEzIDE1aDQiIC8+CiAgICAgIDxwYXRoIGQ9Ik0xMyAxOGgxIiAvPgogICAgICA8cGF0aCBkPSJNMTMgOWg0IiAvPgogICAgICA8cGF0aCBkPSJNMTMgNmgxIiAvPgogICAgPC9zdmc+)

Hide navigation sidebar

Hide table of contents sidebar

Toggle site navigation sidebar

*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctbWVudSIgLz48L3N2Zz4=)*

[](index.html)

Python API documentation

Toggle Light / Dark / Auto color theme

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWF1dG8iPjx1c2UgaHJlZj0iI3N2Zy1zdW4taGFsZiIgLz48L3N2Zz4=) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWRhcmsiPjx1c2UgaHJlZj0iI3N2Zy1tb29uIiAvPjwvc3ZnPg==) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWxpZ2h0Ij48dXNlIGhyZWY9IiNzdmctc3VuIiAvPjwvc3ZnPg==)

Toggle table of contents sidebar

*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctdG9jIiAvPjwvc3ZnPg==)*

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+CiAgICAgICAgICAgIDxwYXRoIGQ9Ik0xMyAyMGgtMlY4bC01LjUgNS41LTEuNDItMS40MkwxMiA0LjE2bDcuOTIgNy45Mi0xLjQyIDEuNDJMMTMgOHYxMnoiIC8+CiAgICAgICAgICA8L3N2Zz4=) Back to top](#)

Toggle Light / Dark / Auto color theme

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWF1dG8iPjx1c2UgaHJlZj0iI3N2Zy1zdW4taGFsZiIgLz48L3N2Zz4=) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWRhcmsiPjx1c2UgaHJlZj0iI3N2Zy1tb29uIiAvPjwvc3ZnPg==) ![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0idGhlbWUtaWNvbi13aGVuLWxpZ2h0Ij48dXNlIGhyZWY9IiNzdmctc3VuIiAvPjwvc3ZnPg==)

Toggle table of contents sidebar

*![](data:image/svg+xml;base64,PHN2Zz48dXNlIGhyZWY9IiNzdmctdG9jIiAvPjwvc3ZnPg==)*

# API[\#](#api "Permalink to this heading")

## API Overview[\#](#api-overview "Permalink to this heading")

*ONNX Runtime* loads and runs inference on a model in ONNX graph format, or ORT format (for memory and disk constrained environments).

The data consumed and produced by the model can be specified and accessed in the way that best matches your scenario.

### Load and run a model[\#](#load-and-run-a-model "Permalink to this heading")

InferenceSession is the main class of ONNX Runtime. It is used to load and run an ONNX model, as well as specify environment and application configuration options.

    session = onnxruntime.InferenceSession('model.onnx')

    outputs = session.run([output names], inputs)

ONNX and ORT format models consist of a graph of computations, modeled as operators, and implemented as optimized operator kernels for different hardware targets. ONNX Runtime orchestrates the execution of operator kernels via execution providers. An execution provider contains the set of kernels for a specific execution target (CPU, GPU, IoT etc). Execution provides are configured using the providers parameter. Kernels from different execution providers are chosen in the priority order given in the list of providers. In the example below if there is a kernel in the CUDA execution provider ONNX Runtime executes that on GPU. If not the kernel is executed on CPU.

    session = onnxruntime.InferenceSession(
            model, providers=['CUDAExecutionProvider', 'CPUExecutionProvider']
    )

The list of available execution providers can be found here: [Execution Providers](https://onnxruntime.ai/docs/execution-providers).

Since ONNX Runtime 1.10, you must explicitly specify the execution provider for your target. Running on CPU is the only time the API allows no explicit setting of the provider parameter. In the examples that follow, the CUDAExecutionProvider and CPUExecutionProvider are used, assuming the application is running on NVIDIA GPUs. Replace these with the execution provider specific to your environment.

You can supply other session configurations via the session options parameter. For example, to enable profiling on the session:

    options = onnxruntime.SessionOptions()
    options.enable_profiling=True
    session = onnxruntime.InferenceSession(
            'model.onnx',
            sess_options=options,
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    )

### Data inputs and outputs[\#](#data-inputs-and-outputs "Permalink to this heading")

The ONNX Runtime Inference Session consumes and produces data using its OrtValue class.

#### Data on CPU[\#](#data-on-cpu "Permalink to this heading")

On CPU (the default), OrtValues can be mapped to and from native Python data structures: numpy arrays, dictionaries and lists of numpy arrays.

    # X is numpy array on cpu
    ortvalue = onnxruntime.OrtValue.ortvalue_from_numpy(X)
    ortvalue.device_name()  # 'cpu'
    ortvalue.shape()        # shape of the numpy array X
    ortvalue.data_type()    # 'tensor(float)'
    ortvalue.is_tensor()    # 'True'
    np.array_equal(ortvalue.numpy(), X)  # 'True'

    # ortvalue can be provided as part of the input feed to a model
    session = onnxruntime.InferenceSession(
            'model.onnx',
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    )
    results = session.run(["Y"], )

By default, *ONNX Runtime* always places input(s) and output(s) on CPU. Having the data on CPU may not optimal if the input or output is consumed and produced on a device other than CPU because it introduces data copy between CPU and the device.

#### Data on device[\#](#data-on-device "Permalink to this heading")

*ONNX Runtime* supports a custom data structure that supports all ONNX data formats that allows users to place the data backing these on a device, for example, on a CUDA supported device. In ONNX Runtime, this called IOBinding.

To use the IOBinding feature, replace InferenceSession.run() with InferenceSession.run_with_iobinding().

A graph is executed on a device other than CPU, for instance CUDA. Users can use IOBinding to copy the data onto the GPU.

    # X is numpy array on cpu
    session = onnxruntime.InferenceSession(
            'model.onnx',
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    )
    io_binding = session.io_binding()
    # OnnxRuntime will copy the data over to the CUDA device if 'input' is consumed by nodes on the CUDA device
    io_binding.bind_cpu_input('input', X)
    io_binding.bind_output('output')
    session.run_with_iobinding(io_binding)
    Y = io_binding.copy_outputs_to_cpu()[0]

The input data is on a device, users directly use the input. The output data is on CPU.

    # X is numpy array on cpu
    X_ortvalue = onnxruntime.OrtValue.ortvalue_from_numpy(X, 'cuda', 0)
    session = onnxruntime.InferenceSession(
            'model.onnx',
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    )
    io_binding = session.io_binding()
    io_binding.bind_input(name='input', device_type=X_ortvalue.device_name(), device_id=0, element_type=np.float32, shape=X_ortvalue.shape(), buffer_ptr=X_ortvalue.data_ptr())
    io_binding.bind_output('output')
    session.run_with_iobinding(io_binding)
    Y = io_binding.copy_outputs_to_cpu()[0]

The input data and output data are both on a device, users directly use the input and also place output on the device.

    #X is numpy array on cpu
    X_ortvalue = onnxruntime.OrtValue.ortvalue_from_numpy(X, 'cuda', 0)
    Y_ortvalue = onnxruntime.OrtValue.ortvalue_from_shape_and_type([3, 2], np.float32, 'cuda', 0)  # Change the shape to the actual shape of the output being bound
    session = onnxruntime.InferenceSession(
            'model.onnx',
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    )
    io_binding = session.io_binding()
    io_binding.bind_input(
            name='input',
            device_type=X_ortvalue.device_name(),
            device_id=0,
            element_type=np.float32,
            shape=X_ortvalue.shape(),
            buffer_ptr=X_ortvalue.data_ptr()
    )
    io_binding.bind_output(
            name='output',
            device_type=Y_ortvalue.device_name(),
            device_id=0,
            element_type=np.float32,
            shape=Y_ortvalue.shape(),
            buffer_ptr=Y_ortvalue.data_ptr()
    )
    session.run_with_iobinding(io_binding)

Users can request *ONNX Runtime* to allocate an output on a device. This is particularly useful for dynamic shaped outputs. Users can use the *get_outputs()* API to get access to the *OrtValue* (s) corresponding to the allocated output(s). Users can thus consume the *ONNX Runtime* allocated memory for the output as an *OrtValue*.

    #X is numpy array on cpu
    X_ortvalue = onnxruntime.OrtValue.ortvalue_from_numpy(X, 'cuda', 0)
    session = onnxruntime.InferenceSession(
            'model.onnx',
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    )
    io_binding = session.io_binding()
    io_binding.bind_input(
            name='input',
            device_type=X_ortvalue.device_name(),
            device_id=0,
            element_type=np.float32,
            shape=X_ortvalue.shape(),
            buffer_ptr=X_ortvalue.data_ptr()
    )
    #Request ONNX Runtime to bind and allocate memory on CUDA for 'output'
    io_binding.bind_output('output', 'cuda')
    session.run_with_iobinding(io_binding)
    # The following call returns an OrtValue which has data allocated by ONNX Runtime on CUDA
    ort_output = io_binding.get_outputs()[0]

In addition, *ONNX Runtime* supports directly working with *OrtValue* (s) while inferencing a model if provided as part of the input feed.

Users can bind *OrtValue* (s) directly.

    #X is numpy array on cpu
    #X is numpy array on cpu
    X_ortvalue = onnxruntime.OrtValue.ortvalue_from_numpy(X, 'cuda', 0)
    Y_ortvalue = onnxruntime.OrtValue.ortvalue_from_shape_and_type([3, 2], np.float32, 'cuda', 0)  # Change the shape to the actual shape of the output being bound
    session = onnxruntime.InferenceSession(
            'model.onnx',
            providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
    )
    io_binding = session.io_binding()
    io_binding.bind_ortvalue_input('input', X_ortvalue)
    io_binding.bind_ortvalue_output('output', Y_ortvalue)
    session.run_with_iobinding(io_binding)

You can also bind inputs and outputs directly to a PyTorch tensor.

    # X is a PyTorch tensor on device
    session = onnxruntime.InferenceSession('model.onnx', providers=['CUDAExecutionProvider', 'CPUExecutionProvider']))
    binding = session.io_binding()

    X_tensor = X.contiguous()

    binding.bind_input(
        name='X',
        device_type='cuda',
        device_id=0,
        element_type=np.float32,
        shape=tuple(x_tensor.shape),
        buffer_ptr=x_tensor.data_ptr(),
        )

    ## Allocate the PyTorch tensor for the model output
    Y_shape = ... # You need to specify the output PyTorch tensor shape
    Y_tensor = torch.empty(Y_shape, dtype=torch.float32, device='cuda:0').contiguous()
    binding.bind_output(
        name='Y',
        device_type='cuda',
        device_id=0,
        element_type=np.float32,
        shape=tuple(Y_tensor.shape),
        buffer_ptr=Y_tensor.data_ptr(),
    )

    session.run_with_iobinding(binding)

You can also see code examples of this API in in the [ONNX Runtime inferences examples](https://github.com/microsoft/onnxruntime-inference-examples/blob/main/python/api/onnxruntime-python-api.py).

Some onnx data type (like TensorProto.BFLOAT16, TensorProto.FLOAT8E4M3FN and TensorProto.FLOAT8E5M2) are not supported by Numpy. You can directly bind input or output with Torch tensor of corresponding data type (like torch.bfloat16, torch.float8_e4m3fn and torch.float8_e5m2) in GPU memory.

    x = torch.ones([3], dtype=torch.float8_e5m2, device='cuda:0')
    y = torch.empty([3], dtype=torch.bfloat16, device='cuda:0')

    binding = session.io_binding()
    binding.bind_input(
        name='X',
        device_type='cuda',
        device_id=0,
        element_type=TensorProto.FLOAT8E5M2,
        shape=tuple(x.shape),
        buffer_ptr=x.data_ptr(),
        )
    binding.bind_output(
        name='Y',
        device_type='cuda',
        device_id=0,
        element_type=TensorProto.BFLOAT16,
        shape=tuple(y.shape),
        buffer_ptr=y.data_ptr(),
        )
        session.run_with_iobinding(binding)

## API Details[\#](#api-details "Permalink to this heading")

### InferenceSession[\#](#inferencesession "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[InferenceSession]][(]*[[path_or_bytes]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[bytes]](https://docs.python.org/3/library/stdtypes.html#bytes "(in Python v3.14)")[ ][[\|]][ ][[os.PathLike]](https://docs.python.org/3/library/os.html#os.PathLike "(in Python v3.14)")]*, *[[sess_options]][[:]][ ][[[onnxruntime.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.SessionOptions")[ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[providers]][[:]][ ][[Sequence][[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[ ][[\|]][ ][[tuple]](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][Any][[,]][ ][Any][[\]]][[\]]][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[provider_options]][[:]][ ][[Sequence][[\[]][[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][Any][[,]][ ][Any][[\]]][[\]]][ ][[\|]][ ][[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")][ ][[=]][ ][[None]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#InferenceSession)[\#](#onnxruntime.InferenceSession "Permalink to this definition")

:   This is the main class used to run a model.

    Parameters[:]

    :   - **path_or_bytes** -- Filename or serialized ONNX or ORT format model in a byte string.

        - **sess_options** -- Session options.

        - **providers** -- Optional sequence of providers in order of decreasing precedence. Values can either be provider names or tuples of (provider name, options dict). If not provided, then all available providers are used with the default precedence.

        - **provider_options** -- Optional sequence of options dicts corresponding to the providers listed in 'providers'.

    The model type will be inferred unless explicitly set in the SessionOptions. To explicitly set:

    :::: 
    ::: highlight
        so = onnxruntime.SessionOptions()
        # so.add_session_config_entry('session.load_model_format', 'ONNX') or
        so.add_session_config_entry('session.load_model_format', 'ORT')
    :::
    ::::

    A file extension of '.ort' will be inferred as an ORT format model. All other filenames are assumed to be ONNX format models.

    'providers' can contain either names or names and options. When any options are given in 'providers', 'provider_options' should not be used.

    The list of providers is ordered by precedence. For example \['CUDAExecutionProvider', 'CPUExecutionProvider'\] means execute a node using CUDAExecutionProvider if capable, otherwise execute using CPUExecutionProvider.

    [[disable_fallback]][(][)][\#](#onnxruntime.InferenceSession.disable_fallback "Permalink to this definition")

    :   Disable session.run() fallback mechanism.

    [[enable_fallback]][(][)][\#](#onnxruntime.InferenceSession.enable_fallback "Permalink to this definition")

    :   Enable session.Run() fallback mechanism. If session.Run() fails due to an internal Execution Provider failure, reset the Execution Providers enabled for this session. If GPU is enabled, fall back to CUDAExecutionProvider. otherwise fall back to CPUExecutionProvider.

    [[end_profiling]][(][)][\#](#onnxruntime.InferenceSession.end_profiling "Permalink to this definition")

    :   End profiling and return results in a file.

        The results are stored in a filename if the option [[`onnxruntime.SessionOptions.enable_profiling()`]](#onnxruntime.SessionOptions.enable_profiling "onnxruntime.SessionOptions.enable_profiling").

    [[get_inputs]][(][)][\#](#onnxruntime.InferenceSession.get_inputs "Permalink to this definition")

    :   Return the inputs metadata as a list of [[`onnxruntime.NodeArg`]](#onnxruntime.NodeArg "onnxruntime.NodeArg").

    [[get_modelmeta]][(][)][\#](#onnxruntime.InferenceSession.get_modelmeta "Permalink to this definition")

    :   Return the metadata. See [[`onnxruntime.ModelMetadata`]](#onnxruntime.ModelMetadata "onnxruntime.ModelMetadata").

    [[get_outputs]][(][)][\#](#onnxruntime.InferenceSession.get_outputs "Permalink to this definition")

    :   Return the outputs metadata as a list of [[`onnxruntime.NodeArg`]](#onnxruntime.NodeArg "onnxruntime.NodeArg").

    [[get_overridable_initializers]][(][)][\#](#onnxruntime.InferenceSession.get_overridable_initializers "Permalink to this definition")

    :   Return the inputs (including initializers) metadata as a list of [[`onnxruntime.NodeArg`]](#onnxruntime.NodeArg "onnxruntime.NodeArg").

    [[get_profiling_start_time_ns]][(][)][\#](#onnxruntime.InferenceSession.get_profiling_start_time_ns "Permalink to this definition")

    :   Return the nanoseconds of profiling's start time Comparable to time.monotonic_ns() after Python 3.3 On some platforms, this timer may not be as precise as nanoseconds For instance, on Windows and MacOS, the precision will be \~100ns

    [[get_provider_options]][(][)][\#](#onnxruntime.InferenceSession.get_provider_options "Permalink to this definition")

    :   Return registered execution providers' configurations.

    [[get_providers]][(][)][\#](#onnxruntime.InferenceSession.get_providers "Permalink to this definition")

    :   Return list of registered execution providers.

    [[get_session_options]][(][)][\#](#onnxruntime.InferenceSession.get_session_options "Permalink to this definition")

    :   Return the session options. See [[`onnxruntime.SessionOptions`]](#onnxruntime.SessionOptions "onnxruntime.SessionOptions").

    [[io_binding]][(][)][\#](#onnxruntime.InferenceSession.io_binding "Permalink to this definition")

    :   Return an onnxruntime.IOBinding object\`.

    [[run]][(]*[[output_names]]*, *[[input_feed]]*, *[[run_options]][[=]][[None]]*[)][\#](#onnxruntime.InferenceSession.run "Permalink to this definition")

    :   Compute the predictions.

        Parameters[:]

        :   - **output_names** -- name of the outputs

            - **input_feed** -- dictionary [`]` `[`input_name:`]` `[`input_value`]` `[`}`]

            - **run_options** -- See [[`onnxruntime.RunOptions`]](#onnxruntime.RunOptions "onnxruntime.RunOptions").

        Returns[:]

        :   list of results, every result is either a numpy array, a sparse tensor, a list or a dictionary.

        :::: 
        ::: highlight
            sess.run([output_name], )
        :::
        ::::

    [[run_async]][(]*[[output_names]]*, *[[input_feed]]*, *[[callback]]*, *[[user_data]]*, *[[run_options]][[=]][[None]]*[)][\#](#onnxruntime.InferenceSession.run_async "Permalink to this definition")

    :   Compute the predictions asynchronously in a separate cxx thread from ort intra-op threadpool.

        Parameters[:]

        :   - **output_names** -- name of the outputs

            - **input_feed** -- dictionary [`]` `[`input_name:`]` `[`input_value`]` `[`}`]

            - **callback** -- python function that accept array of results, and a status string on error. The callback will be invoked by a cxx thread from ort intra-op threadpool.

            - **run_options** -- See [[`onnxruntime.RunOptions`]](#onnxruntime.RunOptions "onnxruntime.RunOptions").

        ::

        :   

            class MyData:

            :   

                def \_\_init\_\_(self):

                :   \# ...

                def save_results(self, results):

                :   \# ...

            def callback(results: np.ndarray, user_data: MyData, err: str) -\> None:

            :   

                if err:

                :   print (err)

                else:

                :   \# save results to user_data

            sess.run_async(\[output_name\], , callback)

    [[run_with_iobinding]][(]*[[iobinding]]*, *[[run_options]][[=]][[None]]*[)][\#](#onnxruntime.InferenceSession.run_with_iobinding "Permalink to this definition")

    :   Compute the predictions.

        Parameters[:]

        :   - **iobinding** -- the iobinding object that has graph inputs/outputs bind.

            - **run_options** -- See [[`onnxruntime.RunOptions`]](#onnxruntime.RunOptions "onnxruntime.RunOptions").

    [[run_with_ort_values]][(]*[[output_names]]*, *[[input_dict_ort_values]]*, *[[run_options]][[=]][[None]]*[)][\#](#onnxruntime.InferenceSession.run_with_ort_values "Permalink to this definition")

    :   Compute the predictions.

        Parameters[:]

        :   - **output_names** -- name of the outputs

            - **input_dict_ort_values** -- dictionary [`]` `[`input_name:`]` `[`input_ort_value`]` `[`}`] See [`OrtValue`] class how to create OrtValue from numpy array or SparseTensor

            - **run_options** -- See [[`onnxruntime.RunOptions`]](#onnxruntime.RunOptions "onnxruntime.RunOptions").

        Returns[:]

        :   an array of OrtValue

        :::: 
        ::: highlight
            sess.run([output_name], )
        :::
        ::::

    [[run_with_ortvaluevector]][(]*[[run_options]]*, *[[feed_names]]*, *[[feeds]]*, *[[fetch_names]]*, *[[fetches]]*, *[[fetch_devices]]*[)][\#](#onnxruntime.InferenceSession.run_with_ortvaluevector "Permalink to this definition")

    :   Compute the predictions similar to other run\_\*() methods but with minimal C++/Python conversion overhead.

        Parameters[:]

        :   - **run_options** -- See [[`onnxruntime.RunOptions`]](#onnxruntime.RunOptions "onnxruntime.RunOptions").

            - **feed_names** -- list of input names.

            - **feeds** -- list of input OrtValue.

            - **fetch_names** -- list of output names.

            - **fetches** -- list of output OrtValue.

            - **fetch_devices** -- list of output devices.

    [[set_providers]][(]*[[providers]][[=]][[None]]*, *[[provider_options]][[=]][[None]]*[)][\#](#onnxruntime.InferenceSession.set_providers "Permalink to this definition")

    :   Register the input list of execution providers. The underlying session is re-created.

        Parameters[:]

        :   - **providers** -- Optional sequence of providers in order of decreasing precedence. Values can either be provider names or tuples of (provider name, options dict). If not provided, then all available providers are used with the default precedence.

            - **provider_options** -- Optional sequence of options dicts corresponding to the providers listed in 'providers'.

        'providers' can contain either names or names and options. When any options are given in 'providers', 'provider_options' should not be used.

        The list of providers is ordered by precedence. For example \['CUDAExecutionProvider', 'CPUExecutionProvider'\] means execute a node using CUDAExecutionProvider if capable, otherwise execute using CPUExecutionProvider.

### Options[\#](#options "Permalink to this heading")

#### RunOptions[\#](#runoptions "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[RunOptions]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.RunOptions]](#onnxruntime.RunOptions "onnxruntime.capi.onnxruntime_pybind11_state.RunOptions")]*[)][\#](#onnxruntime.RunOptions "Permalink to this definition")

:   Configuration information for a single Run.

    [[add_run_config_entry]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.RunOptions]](#onnxruntime.RunOptions "onnxruntime.capi.onnxruntime_pybind11_state.RunOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.RunOptions.add_run_config_entry "Permalink to this definition")

    :   Set a single run configuration entry as a pair of strings.

    [[get_run_config_entry]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.RunOptions]](#onnxruntime.RunOptions "onnxruntime.capi.onnxruntime_pybind11_state.RunOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][\#](#onnxruntime.RunOptions.get_run_config_entry "Permalink to this definition")

    :   Get a single run configuration value using the given configuration key.

    *[property][ ]*[[log_severity_level]][\#](#onnxruntime.RunOptions.log_severity_level "Permalink to this definition")

    :   Info, 2:Warning. 3:Error, 4:Fatal. Default is 2.

        Type[:]

        :   Log severity level for a particular Run() invocation. 0

        Type[:]

        :   Verbose, 1

    *[property][ ]*[[log_verbosity_level]][\#](#onnxruntime.RunOptions.log_verbosity_level "Permalink to this definition")

    :   VLOG level if DEBUG build and run_log_severity_level is 0. Applies to a particular Run() invocation. Default is 0.

    *[property][ ]*[[logid]][\#](#onnxruntime.RunOptions.logid "Permalink to this definition")

    :   To identify logs generated by a particular Run() invocation.

    *[property][ ]*[[only_execute_path_to_fetches]][\#](#onnxruntime.RunOptions.only_execute_path_to_fetches "Permalink to this definition")

    :   Only execute the nodes needed by fetch list

    *[property][ ]*[[terminate]][\#](#onnxruntime.RunOptions.terminate "Permalink to this definition")

    :   Set to True to terminate any currently executing calls that are using this RunOptions instance. The individual calls will exit gracefully and return an error status.

    *[property][ ]*[[training_mode]][\#](#onnxruntime.RunOptions.training_mode "Permalink to this definition")

    :   Choose to run in training or inferencing mode

#### SessionOptions[\#](#sessionoptions "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[SessionOptions]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*[)][\#](#onnxruntime.SessionOptions "Permalink to this definition")

:   Configuration information for a session.

    [[add_external_initializers]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*, *[[arg0]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionOptions.add_external_initializers "Permalink to this definition")

    :   

    [[add_free_dimension_override_by_denotation]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionOptions.add_free_dimension_override_by_denotation "Permalink to this definition")

    :   Specify the dimension size for each denotation associated with an input's free dimension.

    [[add_free_dimension_override_by_name]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionOptions.add_free_dimension_override_by_name "Permalink to this definition")

    :   Specify values of named dimensions within model inputs.

    [[add_initializer]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[object]](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionOptions.add_initializer "Permalink to this definition")

    :   

    [[add_session_config_entry]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionOptions.add_session_config_entry "Permalink to this definition")

    :   Set a single session configuration entry as a pair of strings.

    *[property][ ]*[[enable_cpu_mem_arena]][\#](#onnxruntime.SessionOptions.enable_cpu_mem_arena "Permalink to this definition")

    :   Enables the memory arena on CPU. Arena may pre-allocate memory for future usage. Set this option to false if you don't want it. Default is True.

    *[property][ ]*[[enable_mem_pattern]][\#](#onnxruntime.SessionOptions.enable_mem_pattern "Permalink to this definition")

    :   Enable the memory pattern optimization. Default is true.

    *[property][ ]*[[enable_mem_reuse]][\#](#onnxruntime.SessionOptions.enable_mem_reuse "Permalink to this definition")

    :   Enable the memory reuse optimization. Default is true.

    *[property][ ]*[[enable_profiling]][\#](#onnxruntime.SessionOptions.enable_profiling "Permalink to this definition")

    :   Enable profiling for this session. Default is false.

    *[property][ ]*[[execution_mode]][\#](#onnxruntime.SessionOptions.execution_mode "Permalink to this definition")

    :   Sets the execution mode. Default is sequential.

    *[property][ ]*[[execution_order]][\#](#onnxruntime.SessionOptions.execution_order "Permalink to this definition")

    :   Sets the execution order. Default is basic topological order.

    [[get_session_config_entry]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][\#](#onnxruntime.SessionOptions.get_session_config_entry "Permalink to this definition")

    :   Get a single session configuration value using the given configuration key.

    *[property][ ]*[[graph_optimization_level]][\#](#onnxruntime.SessionOptions.graph_optimization_level "Permalink to this definition")

    :   Graph optimization level for this session.

    *[property][ ]*[[inter_op_num_threads]][\#](#onnxruntime.SessionOptions.inter_op_num_threads "Permalink to this definition")

    :   Sets the number of threads used to parallelize the execution of the graph (across nodes). Default is 0 to let onnxruntime choose.

    *[property][ ]*[[intra_op_num_threads]][\#](#onnxruntime.SessionOptions.intra_op_num_threads "Permalink to this definition")

    :   Sets the number of threads used to parallelize the execution within nodes. Default is 0 to let onnxruntime choose.

    *[property][ ]*[[log_severity_level]][\#](#onnxruntime.SessionOptions.log_severity_level "Permalink to this definition")

    :   Log severity level. Applies to session load, initialization, etc. 0:Verbose, 1:Info, 2:Warning. 3:Error, 4:Fatal. Default is 2.

    *[property][ ]*[[log_verbosity_level]][\#](#onnxruntime.SessionOptions.log_verbosity_level "Permalink to this definition")

    :   VLOG level if DEBUG build and session_log_severity_level is 0. Applies to session load, initialization, etc. Default is 0.

    *[property][ ]*[[logid]][\#](#onnxruntime.SessionOptions.logid "Permalink to this definition")

    :   Logger id to use for session output.

    *[property][ ]*[[optimized_model_filepath]][\#](#onnxruntime.SessionOptions.optimized_model_filepath "Permalink to this definition")

    :   File path to serialize optimized model to. Optimized model is not serialized unless optimized_model_filepath is set. Serialized model format will default to ONNX unless: - add_session_config_entry is used to set 'session.save_model_format' to 'ORT', or - there is no 'session.save_model_format' config entry and optimized_model_filepath ends in '.ort' (case insensitive)

    *[property][ ]*[[profile_file_prefix]][\#](#onnxruntime.SessionOptions.profile_file_prefix "Permalink to this definition")

    :   The prefix of the profile file. The current time will be appended to the file name.

    [[register_custom_ops_library]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions]](#onnxruntime.SessionOptions "onnxruntime.capi.onnxruntime_pybind11_state.SessionOptions")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionOptions.register_custom_ops_library "Permalink to this definition")

    :   Specify the path to the shared library containing the custom op kernels required to run a model.

    *[property][ ]*[[use_deterministic_compute]][\#](#onnxruntime.SessionOptions.use_deterministic_compute "Permalink to this definition")

    :   Whether to use deterministic compute. Default is false.

<!-- -->

*[class][ ]*[[onnxruntime.]][[ExecutionMode]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.ExecutionMode]](#onnxruntime.ExecutionMode "onnxruntime.capi.onnxruntime_pybind11_state.ExecutionMode")]*, *[[value]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)][\#](#onnxruntime.ExecutionMode "Permalink to this definition")

:   Members:

    ORT_SEQUENTIAL

    ORT_PARALLEL

    *[property][ ]*[[name]][\#](#onnxruntime.ExecutionMode.name "Permalink to this definition")

    :   

<!-- -->

*[class][ ]*[[onnxruntime.]][[ExecutionOrder]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.ExecutionOrder]](#onnxruntime.ExecutionOrder "onnxruntime.capi.onnxruntime_pybind11_state.ExecutionOrder")]*, *[[value]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)][\#](#onnxruntime.ExecutionOrder "Permalink to this definition")

:   Members:

    DEFAULT

    PRIORITY_BASED

    MEMORY_EFFICIENT

    *[property][ ]*[[name]][\#](#onnxruntime.ExecutionOrder.name "Permalink to this definition")

    :   

<!-- -->

*[class][ ]*[[onnxruntime.]][[GraphOptimizationLevel]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.GraphOptimizationLevel]](#onnxruntime.GraphOptimizationLevel "onnxruntime.capi.onnxruntime_pybind11_state.GraphOptimizationLevel")]*, *[[value]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)][\#](#onnxruntime.GraphOptimizationLevel "Permalink to this definition")

:   Members:

    ORT_DISABLE_ALL

    ORT_ENABLE_BASIC

    ORT_ENABLE_EXTENDED

    ORT_ENABLE_ALL

    *[property][ ]*[[name]][\#](#onnxruntime.GraphOptimizationLevel.name "Permalink to this definition")

    :   

<!-- -->

*[class][ ]*[[onnxruntime.]][[OrtAllocatorType]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.OrtAllocatorType]](#onnxruntime.OrtAllocatorType "onnxruntime.capi.onnxruntime_pybind11_state.OrtAllocatorType")]*, *[[value]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)][\#](#onnxruntime.OrtAllocatorType "Permalink to this definition")

:   Members:

    INVALID

    ORT_DEVICE_ALLOCATOR

    ORT_ARENA_ALLOCATOR

    *[property][ ]*[[name]][\#](#onnxruntime.OrtAllocatorType.name "Permalink to this definition")

    :   

<!-- -->

*[class][ ]*[[onnxruntime.]][[OrtArenaCfg]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][\#](#onnxruntime.OrtArenaCfg "Permalink to this definition")

:   Overloaded function.

    1.  \_\_init\_\_(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtArenaCfg, arg0: int, arg1: int, arg2: int, arg3: int) -\> None

    2.  \_\_init\_\_(self: onnxruntime.capi.onnxruntime_pybind11_state.OrtArenaCfg, arg0: dict) -\> None

<!-- -->

*[class][ ]*[[onnxruntime.]][[OrtMemoryInfo]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.OrtMemoryInfo]](#onnxruntime.OrtMemoryInfo "onnxruntime.capi.onnxruntime_pybind11_state.OrtMemoryInfo")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.OrtAllocatorType]](#onnxruntime.OrtAllocatorType "onnxruntime.capi.onnxruntime_pybind11_state.OrtAllocatorType")]*, *[[arg2]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *[[arg3]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.OrtMemType]](#onnxruntime.OrtMemType "onnxruntime.capi.onnxruntime_pybind11_state.OrtMemType")]*[)][\#](#onnxruntime.OrtMemoryInfo "Permalink to this definition")

:   

<!-- -->

*[class][ ]*[[onnxruntime.]][[OrtMemType]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.OrtMemType]](#onnxruntime.OrtMemType "onnxruntime.capi.onnxruntime_pybind11_state.OrtMemType")]*, *[[value]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)][\#](#onnxruntime.OrtMemType "Permalink to this definition")

:   Members:

    CPU_INPUT

    CPU_OUTPUT

    CPU

    DEFAULT

    *[property][ ]*[[name]][\#](#onnxruntime.OrtMemType.name "Permalink to this definition")

    :   

### Functions[\#](#functions "Permalink to this heading")

#### Allocators[\#](#allocators "Permalink to this heading")

[[onnxruntime.]][[create_and_register_allocator]][(]*[[arg0]][[:]][ ][[[OrtMemoryInfo]](#onnxruntime.OrtMemoryInfo "onnxruntime.OrtMemoryInfo")]*, *[[arg1]][[:]][ ][[[OrtArenaCfg]](#onnxruntime.OrtArenaCfg "onnxruntime.OrtArenaCfg")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.create_and_register_allocator "Permalink to this definition")

:   

<!-- -->

[[onnxruntime.]][[create_and_register_allocator_v2]][(]*[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[[OrtMemoryInfo]](#onnxruntime.OrtMemoryInfo "onnxruntime.OrtMemoryInfo")]*, *[[arg2]][[:]][ ][[[dict]](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[,]][ ][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]*, *[[arg3]][[:]][ ][[[OrtArenaCfg]](#onnxruntime.OrtArenaCfg "onnxruntime.OrtArenaCfg")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.create_and_register_allocator_v2 "Permalink to this definition")

:   

#### Telemetry events[\#](#telemetry-events "Permalink to this heading")

[[onnxruntime.]][[disable_telemetry_events]][(][)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.disable_telemetry_events "Permalink to this definition")

:   Disables platform-specific telemetry collection.

<!-- -->

[[onnxruntime.]][[enable_telemetry_events]][(][)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.enable_telemetry_events "Permalink to this definition")

:   Enables platform-specific telemetry collection where applicable.

#### Providers[\#](#providers "Permalink to this heading")

[[onnxruntime.]][[get_all_providers]][(][)] [[→] [[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][\#](#onnxruntime.get_all_providers "Permalink to this definition")

:   Return list of Execution Providers that this version of Onnxruntime can support. The order of elements represents the default priority order of Execution Providers from highest to lowest.

<!-- -->

[[onnxruntime.]][[get_available_providers]][(][)] [[→] [[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[\[]][[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")[[\]]]]][\#](#onnxruntime.get_available_providers "Permalink to this definition")

:   Return list of available Execution Providers in this installed version of Onnxruntime. The order of elements represents the default priority order of Execution Providers from highest to lowest.

#### Build, Version[\#](#build-version "Permalink to this heading")

[[onnxruntime.]][[get_build_info]][(][)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][\#](#onnxruntime.get_build_info "Permalink to this definition")

:   

<!-- -->

[[onnxruntime.]][[get_version_string]][(][)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][\#](#onnxruntime.get_version_string "Permalink to this definition")

:   

<!-- -->

[[onnxruntime.]][[has_collective_ops]][(][)] [[→] [[[bool]](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")]][\#](#onnxruntime.has_collective_ops "Permalink to this definition")

:   

#### Device[\#](#device "Permalink to this heading")

[[onnxruntime.]][[get_device]][(][)] [[→] [[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]][\#](#onnxruntime.get_device "Permalink to this definition")

:   Return the device used to compute the prediction (CPU, MKL, ...)

#### Logging[\#](#logging "Permalink to this heading")

[[onnxruntime.]][[set_default_logger_severity]][(]*[[arg0]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.set_default_logger_severity "Permalink to this definition")

:   Sets the default logging severity. 0:Verbose, 1:Info, 2:Warning, 3:Error, 4:Fatal

<!-- -->

[[onnxruntime.]][[set_default_logger_verbosity]][(]*[[arg0]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.set_default_logger_verbosity "Permalink to this definition")

:   Sets the default logging verbosity level. To activate the verbose log, you need to set the default logging severity to 0:Verbose level.

#### Random[\#](#random "Permalink to this heading")

[[onnxruntime.]][[set_seed]][(]*[[arg0]][[:]][ ][[[int]](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.set_seed "Permalink to this definition")

:   Sets the seed used for random number generation in Onnxruntime.

### Data[\#](#data "Permalink to this heading")

#### OrtValue[\#](#ortvalue "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[OrtValue]][(]*[[ortvalue]]*, *[[numpy_obj]][[=]][[None]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue)[\#](#onnxruntime.OrtValue "Permalink to this definition")

:   A data structure that supports all ONNX data formats (tensors and non-tensors) that allows users to place the data backing these on a device, for example, on a CUDA supported device. This class provides APIs to construct and deal with OrtValues.

    [[as_sparse_tensor]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.as_sparse_tensor)[\#](#onnxruntime.OrtValue.as_sparse_tensor "Permalink to this definition")

    :   The function will return SparseTensor contained in this OrtValue

    [[data_ptr]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.data_ptr)[\#](#onnxruntime.OrtValue.data_ptr "Permalink to this definition")

    :   Returns the address of the first element in the OrtValue's data buffer

    [[data_type]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.data_type)[\#](#onnxruntime.OrtValue.data_type "Permalink to this definition")

    :   Returns the data type of the data in the OrtValue

    [[device_name]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.device_name)[\#](#onnxruntime.OrtValue.device_name "Permalink to this definition")

    :   Returns the name of the device where the OrtValue's data buffer resides e.g. cpu, cuda, cann

    [[element_type]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.element_type)[\#](#onnxruntime.OrtValue.element_type "Permalink to this definition")

    :   Returns the proto type of the data in the OrtValue if the OrtValue is a tensor.

    [[has_value]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.has_value)[\#](#onnxruntime.OrtValue.has_value "Permalink to this definition")

    :   Returns True if the OrtValue corresponding to an optional type contains data, else returns False

    [[is_sparse_tensor]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.is_sparse_tensor)[\#](#onnxruntime.OrtValue.is_sparse_tensor "Permalink to this definition")

    :   Returns True if the OrtValue contains a SparseTensor, else returns False

    [[is_tensor]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.is_tensor)[\#](#onnxruntime.OrtValue.is_tensor "Permalink to this definition")

    :   Returns True if the OrtValue contains a Tensor, else returns False

    [[is_tensor_sequence]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.is_tensor_sequence)[\#](#onnxruntime.OrtValue.is_tensor_sequence "Permalink to this definition")

    :   Returns True if the OrtValue contains a Tensor Sequence, else returns False

    [[numpy]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.numpy)[\#](#onnxruntime.OrtValue.numpy "Permalink to this definition")

    :   Returns a Numpy object from the OrtValue. Valid only for OrtValues holding Tensors. Throws for OrtValues holding non-Tensors. Use accessors to gain a reference to non-Tensor objects such as SparseTensor

    *[static][ ]*[[ort_value_from_sparse_tensor]][(]*[[sparse_tensor]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.ort_value_from_sparse_tensor)[\#](#onnxruntime.OrtValue.ort_value_from_sparse_tensor "Permalink to this definition")

    :   The function will construct an OrtValue instance from a valid SparseTensor The new instance of OrtValue will assume the ownership of sparse_tensor

    *[static][ ]*[[ortvalue_from_numpy]][(]*[[numpy_obj]]*, *[[device_type]][[=]][[\'cpu\']]*, *[[device_id]][[=]][[0]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.ortvalue_from_numpy)[\#](#onnxruntime.OrtValue.ortvalue_from_numpy "Permalink to this definition")

    :   Factory method to construct an OrtValue (which holds a Tensor) from a given Numpy object A copy of the data in the Numpy object is held by the OrtValue only if the device is NOT cpu

        Parameters[:]

        :   - **numpy_obj** -- The Numpy object to construct the OrtValue from

            - **device_type** -- e.g. cpu, cuda, cann, cpu by default

            - **device_id** -- device id, e.g. 0

    *[static][ ]*[[ortvalue_from_shape_and_type]][(]*[[shape]][[=]][[None]]*, *[[element_type]][[=]][[None]]*, *[[device_type]][[=]][[\'cpu\']]*, *[[device_id]][[=]][[0]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.ortvalue_from_shape_and_type)[\#](#onnxruntime.OrtValue.ortvalue_from_shape_and_type "Permalink to this definition")

    :   Factory method to construct an OrtValue (which holds a Tensor) from given shape and element_type

        Parameters[:]

        :   - **shape** -- List of integers indicating the shape of the OrtValue

            - **element_type** -- The data type of the elements in the OrtValue (numpy type)

            - **device_type** -- e.g. cpu, cuda, cann, cpu by default

            - **device_id** -- device id, e.g. 0

    [[shape]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.shape)[\#](#onnxruntime.OrtValue.shape "Permalink to this definition")

    :   Returns the shape of the data in the OrtValue

    [[update_inplace]][(]*[[np_arr]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtValue.update_inplace)[\#](#onnxruntime.OrtValue.update_inplace "Permalink to this definition")

    :   Update the OrtValue in place with a new Numpy array. The numpy contents are copied over to the device memory backing the OrtValue. It can be used to update the input valuess for an InferenceSession with CUDA graph enabled or other scenarios where the OrtValue needs to be updated while the memory address can not be changed.

#### SparseTensor[\#](#sparsetensor "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[SparseTensor]][(]*[[sparse_tensor]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor)[\#](#onnxruntime.SparseTensor "Permalink to this definition")

:   A data structure that project the C++ SparseTensor object The class provides API to work with the object. Depending on the format, the class will hold more than one buffer depending on the format

    Internal constructor

    [[as_blocksparse_view]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.as_blocksparse_view)[\#](#onnxruntime.SparseTensor.as_blocksparse_view "Permalink to this definition")

    :   The method will return coo representation of the sparse tensor which will enable querying BlockSparse indices. If the instance did not contain BlockSparse format, it would throw. You can query coo indices as:

        :::: 
        ::: highlight
            block_sparse_indices = sparse_tensor.as_blocksparse_view().indices()
        :::
        ::::

        which will return a numpy array that is backed by the native memory

    [[as_coo_view]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.as_coo_view)[\#](#onnxruntime.SparseTensor.as_coo_view "Permalink to this definition")

    :   The method will return coo representation of the sparse tensor which will enable querying COO indices. If the instance did not contain COO format, it would throw. You can query coo indices as:

        :::: 
        ::: highlight
            coo_indices = sparse_tensor.as_coo_view().indices()
        :::
        ::::

        which will return a numpy array that is backed by the native memory.

    [[as_csrc_view]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.as_csrc_view)[\#](#onnxruntime.SparseTensor.as_csrc_view "Permalink to this definition")

    :   The method will return CSR(C) representation of the sparse tensor which will enable querying CRS(C) indices. If the instance dit not contain CSR(C) format, it would throw. You can query indices as:

        :::: 
        ::: highlight
            inner_ndices = sparse_tensor.as_csrc_view().inner()
            outer_ndices = sparse_tensor.as_csrc_view().outer()
        :::
        ::::

        returning numpy arrays backed by the native memory.

    [[data_type]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.data_type)[\#](#onnxruntime.SparseTensor.data_type "Permalink to this definition")

    :   Returns a string data type of the data in the OrtValue

    [[dense_shape]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.dense_shape)[\#](#onnxruntime.SparseTensor.dense_shape "Permalink to this definition")

    :   Returns a numpy array(int64) containing a dense shape of a sparse tensor

    [[device_name]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.device_name)[\#](#onnxruntime.SparseTensor.device_name "Permalink to this definition")

    :   Returns the name of the device where the SparseTensor data buffers reside e.g. cpu, cuda

    [[format]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.format)[\#](#onnxruntime.SparseTensor.format "Permalink to this definition")

    :   Returns a OrtSparseFormat enumeration

    *[static][ ]*[[sparse_coo_from_numpy]][(]*[[dense_shape]]*, *[[values]]*, *[[coo_indices]]*, *[[ort_device]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.sparse_coo_from_numpy)[\#](#onnxruntime.SparseTensor.sparse_coo_from_numpy "Permalink to this definition")

    :   Factory method to construct a SparseTensor in COO format from given arguments

        Parameters[:]

        :   - **dense_shape** -- 1-D numpy array(int64) or a python list that contains a dense_shape of the sparse tensor must be on cpu memory

            - **values** -- a homogeneous, contiguous 1-D numpy array that contains non-zero elements of the tensor of a type.

            - **coo_indices** -- contiguous numpy array(int64) that contains COO indices for the tensor. coo_indices may have a 1-D shape when it contains a linear index of non-zero values and its length must be equal to that of the values. It can also be of 2-D shape, in which has it contains pairs of coordinates for each of the nnz values and its length must be exactly twice of the values length.

            - **ort_device** --

              - describes the backing memory owned by the supplied nummpy arrays. Only CPU memory is

              suppored for non-numeric data types.

        For primitive types, the method will map values and coo_indices arrays into native memory and will use them as backing storage. It will increment the reference count for numpy arrays and it will decrement it on GC. The buffers may reside in any storage either CPU or GPU. For strings and objects, it will create a copy of the arrays in CPU memory as ORT does not support those on other devices and their memory can not be mapped.

    *[static][ ]*[[sparse_csr_from_numpy]][(]*[[dense_shape]]*, *[[values]]*, *[[inner_indices]]*, *[[outer_indices]]*, *[[ort_device]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.sparse_csr_from_numpy)[\#](#onnxruntime.SparseTensor.sparse_csr_from_numpy "Permalink to this definition")

    :   Factory method to construct a SparseTensor in CSR format from given arguments

        Parameters[:]

        :   - **dense_shape** -- 1-D numpy array(int64) or a python list that contains a dense_shape of the sparse tensor (rows, cols) must be on cpu memory

            - **values** -- a contiguous, homogeneous 1-D numpy array that contains non-zero elements of the tensor of a type.

            - **inner_indices** -- contiguous 1-D numpy array(int64) that contains CSR inner indices for the tensor. Its length must be equal to that of the values.

            - **outer_indices** -- contiguous 1-D numpy array(int64) that contains CSR outer indices for the tensor. Its length must be equal to the number of rows + 1.

            - **ort_device** --

              - describes the backing memory owned by the supplied nummpy arrays. Only CPU memory is

              suppored for non-numeric data types.

        For primitive types, the method will map values and indices arrays into native memory and will use them as backing storage. It will increment the reference count and it will decrement then count when it is GCed. The buffers may reside in any storage either CPU or GPU. For strings and objects, it will create a copy of the arrays in CPU memory as ORT does not support those on other devices and their memory can not be mapped.

    [[to_cuda]][(]*[[ort_device]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.to_cuda)[\#](#onnxruntime.SparseTensor.to_cuda "Permalink to this definition")

    :   Returns a copy of this instance on the specified cuda device

        Parameters[:]

        :   **ort_device** -- with name 'cuda' and valid gpu device id

        The method will throw if:

        - this instance contains strings

        - this instance is already on GPU. Cross GPU copy is not supported

        - CUDA is not present in this build

        - if the specified device is not valid

    [[values]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#SparseTensor.values)[\#](#onnxruntime.SparseTensor.values "Permalink to this definition")

    :   The method returns a numpy array that is backed by the native memory if the data type is numeric. Otherwise, the returned numpy array that contains copies of the strings.

### Devices[\#](#devices "Permalink to this heading")

#### IOBinding[\#](#iobinding "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[IOBinding]][(]*[[session]][[:]][ ][[Session]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding)[\#](#onnxruntime.IOBinding "Permalink to this definition")

:   This class provides API to bind input/output to a specified device, e.g. GPU.

    [[bind_cpu_input]][(]*[[name]]*, *[[arr_on_cpu]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding.bind_cpu_input)[\#](#onnxruntime.IOBinding.bind_cpu_input "Permalink to this definition")

    :   bind an input to array on CPU :param name: input name :param arr_on_cpu: input values as a python array on CPU

    [[bind_input]][(]*[[name]]*, *[[device_type]]*, *[[device_id]]*, *[[element_type]]*, *[[shape]]*, *[[buffer_ptr]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding.bind_input)[\#](#onnxruntime.IOBinding.bind_input "Permalink to this definition")

    :   

        Parameters[:]

        :   - **name** -- input name

            - **device_type** -- e.g. cpu, cuda, cann

            - **device_id** -- device id, e.g. 0

            - **element_type** -- input element type

            - **shape** -- input shape

            - **buffer_ptr** -- memory pointer to input data

    [[bind_ortvalue_input]][(]*[[name]]*, *[[ortvalue]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding.bind_ortvalue_input)[\#](#onnxruntime.IOBinding.bind_ortvalue_input "Permalink to this definition")

    :   

        Parameters[:]

        :   - **name** -- input name

            - **ortvalue** -- OrtValue instance to bind

    [[bind_ortvalue_output]][(]*[[name]]*, *[[ortvalue]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding.bind_ortvalue_output)[\#](#onnxruntime.IOBinding.bind_ortvalue_output "Permalink to this definition")

    :   

        Parameters[:]

        :   - **name** -- output name

            - **ortvalue** -- OrtValue instance to bind

    [[bind_output]][(]*[[name]]*, *[[device_type]][[=]][[\'cpu\']]*, *[[device_id]][[=]][[0]]*, *[[element_type]][[=]][[None]]*, *[[shape]][[=]][[None]]*, *[[buffer_ptr]][[=]][[None]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding.bind_output)[\#](#onnxruntime.IOBinding.bind_output "Permalink to this definition")

    :   

        Parameters[:]

        :   - **name** -- output name

            - **device_type** -- e.g. cpu, cuda, cann, cpu by default

            - **device_id** -- device id, e.g. 0

            - **element_type** -- output element type

            - **shape** -- output shape

            - **buffer_ptr** -- memory pointer to output data

    [[copy_outputs_to_cpu]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding.copy_outputs_to_cpu)[\#](#onnxruntime.IOBinding.copy_outputs_to_cpu "Permalink to this definition")

    :   Copy output contents to CPU.

    [[get_outputs]][(][)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#IOBinding.get_outputs)[\#](#onnxruntime.IOBinding.get_outputs "Permalink to this definition")

    :   Returns the output OrtValues from the Run() that preceded the call. The data buffer of the obtained OrtValues may not reside on CPU memory

<!-- -->

*[class][ ]*[[onnxruntime.]][[SessionIOBinding]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*, *[[arg0]][[:]][ ][[onnxruntime.capi.onnxruntime_pybind11_state.InferenceSession]]*[)][\#](#onnxruntime.SessionIOBinding "Permalink to this definition")

:   

    [[bind_input]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][\#](#onnxruntime.SessionIOBinding.bind_input "Permalink to this definition")

    :   Overloaded function.

        1.  bind_input(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: object) -\> None

        2.  bind_input(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice, arg2: object, arg3: list\[int\], arg4: int) -\> None

    [[bind_ortvalue_input]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[onnxruntime.capi.onnxruntime_pybind11_state.OrtValue]]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionIOBinding.bind_ortvalue_input "Permalink to this definition")

    :   

    [[bind_ortvalue_output]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*, *[[arg0]][[:]][ ][[[str]](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *[[arg1]][[:]][ ][[onnxruntime.capi.onnxruntime_pybind11_state.OrtValue]]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionIOBinding.bind_ortvalue_output "Permalink to this definition")

    :   

    [[bind_output]][(]*[[\*]][[args]]*, *[[\*\*]][[kwargs]]*[)][\#](#onnxruntime.SessionIOBinding.bind_output "Permalink to this definition")

    :   Overloaded function.

        1.  bind_output(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice, arg2: object, arg3: list\[int\], arg4: int) -\> None

        2.  bind_output(self: onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding, arg0: str, arg1: onnxruntime.capi.onnxruntime_pybind11_state.OrtDevice) -\> None

    [[clear_binding_inputs]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionIOBinding.clear_binding_inputs "Permalink to this definition")

    :   

    [[clear_binding_outputs]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionIOBinding.clear_binding_outputs "Permalink to this definition")

    :   

    [[copy_outputs_to_cpu]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*[)] [[→] [[[list]](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")]][\#](#onnxruntime.SessionIOBinding.copy_outputs_to_cpu "Permalink to this definition")

    :   

    [[get_outputs]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*[)] [[→] [[onnxruntime.capi.onnxruntime_pybind11_state.OrtValueVector]]][\#](#onnxruntime.SessionIOBinding.get_outputs "Permalink to this definition")

    :   

    [[synchronize_inputs]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionIOBinding.synchronize_inputs "Permalink to this definition")

    :   

    [[synchronize_outputs]][(]*[[self]][[:]][ ][[[onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding]](#onnxruntime.SessionIOBinding "onnxruntime.capi.onnxruntime_pybind11_state.SessionIOBinding")]*[)] [[→] [[[None]](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]][\#](#onnxruntime.SessionIOBinding.synchronize_outputs "Permalink to this definition")

    :   

#### OrtDevice[\#](#ortdevice "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[OrtDevice]][(]*[[c_ort_device]]*[)][[[\[source\]]]](modules/onnxruntime/capi/onnxruntime_inference_collection.html#OrtDevice)[\#](#onnxruntime.OrtDevice "Permalink to this definition")

:   A data structure that exposes the underlying C++ OrtDevice

    Internal constructor

### Internal classes[\#](#internal-classes "Permalink to this heading")

These classes cannot be instantiated by users but they are returned by methods or functions of this library.

#### ModelMetadata[\#](#modelmetadata "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[ModelMetadata]][\#](#onnxruntime.ModelMetadata "Permalink to this definition")

:   Pre-defined and custom metadata about the model. It is usually used to identify the model used to run the prediction and facilitate the comparison.

    *[property][ ]*[[custom_metadata_map]][\#](#onnxruntime.ModelMetadata.custom_metadata_map "Permalink to this definition")

    :   additional metadata

    *[property][ ]*[[description]][\#](#onnxruntime.ModelMetadata.description "Permalink to this definition")

    :   description of the model

    *[property][ ]*[[domain]][\#](#onnxruntime.ModelMetadata.domain "Permalink to this definition")

    :   ONNX domain

    *[property][ ]*[[graph_description]][\#](#onnxruntime.ModelMetadata.graph_description "Permalink to this definition")

    :   description of the graph hosted in the model

    *[property][ ]*[[graph_name]][\#](#onnxruntime.ModelMetadata.graph_name "Permalink to this definition")

    :   graph name

    *[property][ ]*[[producer_name]][\#](#onnxruntime.ModelMetadata.producer_name "Permalink to this definition")

    :   producer name

    *[property][ ]*[[version]][\#](#onnxruntime.ModelMetadata.version "Permalink to this definition")

    :   version of the model

#### NodeArg[\#](#nodearg "Permalink to this heading")

*[class][ ]*[[onnxruntime.]][[NodeArg]][\#](#onnxruntime.NodeArg "Permalink to this definition")

:   Node argument definition, for both input and output, including arg name, arg type (contains both type and shape).

    *[property][ ]*[[name]][\#](#onnxruntime.NodeArg.name "Permalink to this definition")

    :   node name

    *[property][ ]*[[shape]][\#](#onnxruntime.NodeArg.shape "Permalink to this definition")

    :   node shape (assuming the node holds a tensor)

    *[property][ ]*[[type]][\#](#onnxruntime.NodeArg.type "Permalink to this definition")

    :   node type

## Backend[\#](#backend "Permalink to this heading")

In addition to the regular API which is optimized for performance and usability, *ONNX Runtime* also implements the [ONNX backend API](https://github.com/onnx/onnx/blob/main/docs/ImplementingAnOnnxBackend.md) for verification of *ONNX* specification conformance. The following functions are supported:

[[onnxruntime.backend.]][[is_compatible]][(]*[[model]]*, *[[device]][[=]][[None]]*, *[[\*\*]][[kwargs]]*[)][\#](#onnxruntime.backend.is_compatible "Permalink to this definition")

:   Return whether the model is compatible with the backend.

    Parameters[:]

    :   - **model** -- unused

        - **device** -- None to use the default device or a string (ex: 'CPU')

    Returns[:]

    :   boolean

<!-- -->

[[onnxruntime.backend.]][[prepare]][(]*[[model]]*, *[[device]][[=]][[None]]*, *[[\*\*]][[kwargs]]*[)][\#](#onnxruntime.backend.prepare "Permalink to this definition")

:   Load the model and creates a [[`onnxruntime.InferenceSession`]](#onnxruntime.InferenceSession "onnxruntime.InferenceSession") ready to be used as a backend.

    Parameters[:]

    :   - **model** -- ModelProto (returned by onnx.load), string for a filename or bytes for a serialized model

        - **device** -- requested device for the computation, None means the default one which depends on the compilation settings

        - **kwargs** -- see [[`onnxruntime.SessionOptions`]](#onnxruntime.SessionOptions "onnxruntime.SessionOptions")

    Returns[:]

    :   [[`onnxruntime.InferenceSession`]](#onnxruntime.InferenceSession "onnxruntime.InferenceSession")

<!-- -->

[[onnxruntime.backend.]][[run]][(]*[[model]]*, *[[inputs]]*, *[[device]][[=]][[None]]*, *[[\*\*]][[kwargs]]*[)][\#](#onnxruntime.backend.run "Permalink to this definition")

:   Compute the prediction.

    Parameters[:]

    :   - **model** -- [[`onnxruntime.InferenceSession`]](#onnxruntime.InferenceSession "onnxruntime.InferenceSession") returned by function *prepare*

        - **inputs** -- inputs

        - **device** -- requested device for the computation, None means the default one which depends on the compilation settings

        - **kwargs** -- see [[`onnxruntime.RunOptions`]](#onnxruntime.RunOptions "onnxruntime.RunOptions")

    Returns[:]

    :   predictions

<!-- -->

[[onnxruntime.backend.]][[supports_device]][(]*[[device]]*[)][\#](#onnxruntime.backend.supports_device "Permalink to this definition")

:   Check whether the backend is compiled with particular device support. In particular it's used in the testing suite.

[](ortmodule/overview.html)

Next

Overview

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZnVyby1yZWxhdGVkLWljb24iPjx1c2UgaHJlZj0iI3N2Zy1hcnJvdy1yaWdodCIgLz48L3N2Zz4=) [![](data:image/svg+xml;base64,PHN2ZyBjbGFzcz0iZnVyby1yZWxhdGVkLWljb24iPjx1c2UgaHJlZj0iI3N2Zy1hcnJvdy1yaWdodCIgLz48L3N2Zz4=)](tutorial.html)

Previous

Tutorial

Copyright © 2018-2024, Microsoft

Made with [Sphinx](https://www.sphinx-doc.org/) and [\@pradyunsg](https://pradyunsg.me)\'s [Furo](https://github.com/pradyunsg/furo)