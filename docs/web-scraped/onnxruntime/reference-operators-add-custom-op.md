# Source: https://onnxruntime.ai/docs/reference/operators/add-custom-op.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#custom-operators) Custom operators 

ONNX Runtime provides options to run custom operators that are not official ONNX operators. Note that custom operators differ from [contrib ops](/docs/reference/operators/ContribOperators.html), which are selected unofficial ONNX operators that are built in directly to ORT.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Define and register a custom operator](#define-and-register-a-custom-operator)
- [Legacy way for custom op development and registration](#legacy-way-for-custom-op-development-and-registration)
- [Create a library of custom operators](#create-a-library-of-custom-operators)
- [Calling a native operator from custom operator](#calling-a-native-operator-from-custom-operator)
- [Custom ops for CUDA and ROCM](#custom-ops-for-cuda-and-rocm)
- [One op, varied types](#one-op-varied-types)
- [Wrapping an external inference runtime in a custom operator](#wrapping-an-external-inference-runtime-in-a-custom-operator)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#define-and-register-a-custom-operator) Define and register a custom operator

Since onnxruntime 1.16, custom op could simply be implemented as a function:

``` highlight
void KernelOne(const Ort::Custom::Tensor<float>& X,
               const Ort::Custom::Tensor<float>& Y,
               Ort::Custom::Tensor<float>& Z) 
}

int main() ;
  // please make sure that custom_op_one has the same lifetime as the consuming session
  std::unique_ptr<OrtLiteCustomOp> custom_op_one;
  v1_domain.Add(custom_op_one.get());
  Ort::SessionOptions session_options;
  session_options.Add(v1_domain);
  // create a session with the session_options ...
}
```

For custom ops that bear attributes, structs are also supported：

``` highlight
struct Merge 
  // a "Compute" member function is required to be present
  void Compute(const Ort::Custom::Tensor<std::string_view>& strings_in,
               std::string_view string_in,
               Ort::Custom::Tensor<std::string>* strings_out) 
    string_pool.emplace_back(string_in.data(), string_in.size());
    if (reverse_) 
      std::reverse(string_pool.begin(), string_pool.end());
    }
    strings_out->SetStringOutput(string_pool, );
  }
  bool reverse_ = false;
};

int main() ;
  // please make sure that mrg_op_ptr has the same lifetime as the consuming session
  std::unique_ptr<Ort::Custom::OrtLiteCustomOp> mrg_op_ptr;
  v2_domain.Add(mrg_op_ptr.get());
  Ort::SessionOptions session_options;
  session_options.Add(v2_domain);
  // create a session with the session_options ...
}
```

A "Compute" member function is required for the struct to run as a custom op.

For both cases:

- Inputs need to be declared as const references.
- Outputs need to be declared as non-const references.
- [Ort::Custom::Tensor::Shape()](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/include/onnxruntime/core/session/onnxruntime_lite_custom_op.h#L67) returns input shape.
- [Ort::Custom::Tensor::Data()](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/include/onnxruntime/core/session/onnxruntime_lite_custom_op.h#L80) returns raw input data.
- [Ort::Custom::Tensor::NumberOfElement()](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/include/onnxruntime/core/session/onnxruntime_lite_custom_op.h#L73) returns number of elements in the input.
- [Ort::Custom::Tensor::Allocate(...)](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/include/onnxruntime/core/session/onnxruntime_lite_custom_op.h#L83) allocates an output and returns raw data address.
- Supported template arguments are: int8_t, int16_t, int32_t, int64_t, float, double.
- Support [std::string_view](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/include/onnxruntime/core/session/onnxruntime_lite_custom_op.h#L188) as input and [std::string](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/include/onnxruntime/core/session/onnxruntime_lite_custom_op.h#L117) as output, please find usage [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/shared_lib/test_inference.cc#L3129).
- For custom op functions running on CPUExecutionProvider, [span](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/include/onnxruntime/core/session/onnxruntime_lite_custom_op.h#L40) and scalar as inputs are supported, please find usage [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/testdata/custom_op_library/cpu/cpu_ops.cc#L43).
- For custom op functions that expect kernel context, please see an example [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/testdata/custom_op_library/cpu/cpu_ops.cc#L43).
- When using unique_ptr to host a created custom op, please be sure to keep it alive along with the consuming session.

More examples could be found [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/testdata/custom_op_library/cpu/cpu_ops.cc) and [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/shared_lib/test_inference.cc#L3123).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#legacy-way-for-custom-op-development-and-registration) Legacy way for custom op development and registration

The legacy way for developing custom op is still supported, please refer to examples [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/shared_lib/custom_op_utils.h).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-a-library-of-custom-operators) Create a library of custom operators

Custom operators can be defined in a separate shared library (e.g., a .dll on Windows or a .so on Linux). A custom operator library must export and implement a `RegisterCustomOps` function. The `RegisterCustomOps` function adds a `Ort::CustomOpDomain` containing the library's custom operators to the provided session options. Please refer to a project [here](https://github.com/microsoft/onnxruntime/tree/rel-1.16.0/onnxruntime/test/testdata/custom_op_library) and related cmake commands [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/cmake/onnxruntime_unittests.cmake#L1482).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#calling-a-native-operator-from-custom-operator) Calling a native operator from custom operator

To simplify implementation of custom operators, native onnxruntime operators can directly be invoked. For example, some custom ops might have to do GEMM or TopK in between other computations. This may also be useful for preprocessing and postprocessing on a node, such as Conv, for state management purpose. To achieve this, the Conv node can be wrapped up by a custom operator such as CustomConv, within which the input and output could be cached and processed.

This feature is supported from ONNX Runtime 1.12.0+. See: [API](https://github.com/microsoft/onnxruntime/blob/ced7c2deac958391414d2bbf951f86e2fc904b05/include/onnxruntime/core/session/onnxruntime_cxx_api.h#L1156) and [examples](https://github.com/microsoft/onnxruntime/blob/ced7c2deac958391414d2bbf951f86e2fc904b05/onnxruntime/test/shared_lib/custom_op_utils.cc#L210).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#custom-ops-for-cuda-and-rocm) Custom ops for CUDA and ROCM

Since onnxruntime 1.16, customer op for CUDA and ROCM devices are supported. Device related resources could be directly accessed from within the op via a device related context. Take CUDA for example:

``` highlight
void KernelOne(const Ort::Custom::CudaContext& cuda_ctx,
               const Ort::Custom::Tensor<float>& X,
               const Ort::Custom::Tensor<float>& Y,
               Ort::Custom::Tensor<float>& Z) 
```

Full example could be found [here](https://github.com/microsoft/onnxruntime/tree/rel-1.17.0/onnxruntime/test/testdata/custom_op_library/cuda). To further facilitate development, a wide variety of cuda ep resources and configurations are exposed via CudaContext, please refer to the [header](https://github.com/microsoft/onnxruntime/blob/rel-1.17.0/include/onnxruntime/core/providers/cuda/cuda_resource.h#L8) for detail.

For ROCM, it is like:

``` highlight
void KernelOne(const Ort::Custom::RocmContext& rocm_ctx,
               const Ort::Custom::Tensor<float>& X,
               const Ort::Custom::Tensor<float>& Y,
               Ort::Custom::Tensor<float>& Z) 
```

Details could be found [here](https://github.com/microsoft/onnxruntime/tree/rel-1.16.0/onnxruntime/test/testdata/custom_op_library/rocm).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#one-op-varied-types) One op, varied types

Since onnxruntime 1.16, a custom op is allowed to support varied data types:

``` highlight
template <typename T>
void MulTop(const Ort::Custom::Span<T>& in, Ort::Custom::Tensor<T>& out) )[0] = in[0] * in[1];
}

int main() ;
  std::unique_ptr<OrtLiteCustomOp> c_MulTopOpInt32;
  // create a domain adding both c_MulTopOpFloat and c_MulTopOpInt32
}
```

Code could be found [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/testdata/custom_op_library/cpu/cpu_ops.cc#L39). A unit test case could found [here](https://github.com/microsoft/onnxruntime/blob/rel-1.16.0/onnxruntime/test/shared_lib/test_inference.cc#L3272).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#wrapping-an-external-inference-runtime-in-a-custom-operator) Wrapping an external inference runtime in a custom operator

A custom operator can wrap an entire model that is then inferenced with an external API or runtime. This can facilitate the integration of external inference engines or APIs with ONNX Runtime.

As an example, consider the following ONNX model with a custom operator named "OpenVINO_Wrapper". The "OpenVINO_Wrapper" node encapsulates an entire MNIST model in OpenVINO's native model format (XML and BIN data). The model data is serialized into the node's attributes and later retrieved by the custom operator's kernel to build an in-memory representation of the model and run inference with OpenVINO C++ APIs.

![ONNX model of a custom operator wrapping an OpenVINO MNIST model](../../../images/custom_op_wrapper.png)

The following code snippet shows how the custom operator is defined.

``` highlight
// Note - below code utilizes legacy custom op interfaces
struct CustomOpOpenVINO : Ort::CustomOpBase<CustomOpOpenVINO, KernelOpenVINO> 

  constexpr const char* GetExecutionProviderType() const noexcept 

  // IMPORTANT: In order to wrap a generic runtime-specific model, the custom operator
  // must have a single non-homogeneous variadic input and output.

  constexpr size_t GetInputTypeCount() const noexcept 

  constexpr size_t GetOutputTypeCount() const noexcept 

  constexpr ONNXTensorElementDataType GetInputType(size_t /* index */) const noexcept 

  constexpr ONNXTensorElementDataType GetOutputType(size_t /* index */) const noexcept 

  constexpr OrtCustomOpInputOutputCharacteristic GetInputCharacteristic(size_t /* index */) const noexcept 

  constexpr OrtCustomOpInputOutputCharacteristic GetOutputCharacteristic(size_t /* index */) const noexcept 

  constexpr bool GetVariadicInputHomogeneity() const noexcept 

  constexpr bool GetVariadicOutputHomogeneity() const noexcept 

  // The "device_type" is configurable at the session level.
  std::vector<std::string> GetSessionConfigKeys() const ; }

 private:
  std::unordered_map<std::string, std::string> session_configs_;
};
```

Note that the custom operator is defined to have a single variadic/heterogenous input and a single variadic/heterogeneous output. This is necessary to enable wrapping OpenVINO models with varying input and output types and shapes (not just an MNIST model). For more information on input and output characteristics, refer to the [OrtCustomOp struct documentation](https://onnxruntime.ai/docs/api/c/struct_ort_custom_op.html).

Additionally, the custom operator declares "device_type" as a session configuration that can be set by the application. The following code snippet shows how to register and configure a custom operator library containing the aforementioned custom operator.

``` highlight
Ort::Env env;
Ort::SessionOptions session_options;
Ort::CustomOpConfigs custom_op_configs;

// Create local session config entries for the custom op.
custom_op_configs.AddConfig("OpenVINO_Wrapper", "device_type", "CPU");

// Register custom op library and pass in the custom op configs (optional).
session_options.RegisterCustomOpsLibrary("MyOpenVINOWrapper_Lib.so", custom_op_configs);

Ort::Session session(env, ORT_TSTR("custom_op_mnist_ov_wrapper.onnx"), session_options);
```

Refer to the [complete OpenVINO custom operator wrapper example](https://github.com/microsoft/onnxruntime/tree/main/onnxruntime/test/testdata/custom_op_openvino_wrapper_library) for more details. To create an ONNX model that wraps an external model or weights, refer to the [create_custom_op_wrapper.py tool](https://github.com/microsoft/onnxruntime/blob/main/onnxruntime/python/tools/custom_op_wrapper/create_custom_op_wrapper.py).