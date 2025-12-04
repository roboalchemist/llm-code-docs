# Source: https://onnxruntime.ai/docs/get-started/with-csharp.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#get-started-with-ort-for-c) Get started with ORT for C# 

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Install the Nuget Packages with the .NET CLI](#install-the-nuget-packages-with-the-net-cli)
- [Import the libraries](#import-the-libraries)
- [Create method for inference](#create-method-for-inference)
- [Reuse input/output tensor buffers](#reuse-inputoutput-tensor-buffers)
  - [Chaining: Feed model A's output(s) as input(s) to model B](#chaining-feed-model-as-outputs-as-inputs-to-model-b)
  - [Multiple inference runs with fixed sized input(s) and output(s)](#multiple-inference-runs-with-fixed-sized-inputs-and-outputs)
- [Running on GPU (Optional)](#running-on-gpu-optional)
- [Supported Versions](#supported-versions)
- [Builds](#builds)
- [API Reference](#api-reference)
- [Samples](#samples)
- [Learn More](#learn-more)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-the-nuget-packages-with-the-net-cli) Install the Nuget Packages with the .NET CLI 

``` highlight
dotnet add package Microsoft.ML.OnnxRuntime --version 1.16.0
dotnet add package System.Numerics.Tensors --version 0.1.0
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#import-the-libraries) Import the libraries

``` highlight
using Microsoft.ML.OnnxRuntime;
using System.Numerics.Tensors;
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#create-method-for-inference) Create method for inference

This is an [Azure Function](https://azure.microsoft.com/services/functions/) example that uses ORT with C# for inference on an NLP model created with SciKit Learn.

``` highlight
 public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "get", "post", Route = null)] HttpRequest req,
            ILogger log, ExecutionContext context)
        );
            inputOrtValue.StringTensorSetElementAt(review, 0);

            // Create input data for session. Request all outputs in this case.
            var inputs = new Dictionary<string, OrtValue>
            
            };

            using var runOptions = new RunOptions();

            // We are getting a sequence of maps as output. We are interested in the first element (map) of the sequence.
            // That result is a Sequence of Maps, and we only need the first map from there.
            using var outputs = session.Run(runOptions, inputs, session.OutputNames);
            Debug.Assert(outputs.Count > 0, "Expecting some output");

            // We want the last output, which is the sequence of maps
            var lastOutput = outputs[outputs.Count - 1];

            // Optional code to check the output type
            

            var elementsNum = lastOutput.GetValueCount();
            Debug.Assert(elementsNum > 0, "Expecting a non empty sequence");

            // Get the first map in sequence
            using var firstMap = lastOutput.GetValue(0, OrtAllocator.DefaultInstance);

            // Optional code just checking
            

            var inferenceResult = new Dictionary<string, float>();
            // Let use the visitor to read map keys and values
            // Here keys and values are represented with the same number of corresponding entries
            // string -> float
            firstMap.ProcessMap((keys, values) => 
            }, OrtAllocator.DefaultInstance);

            // Return the inference result as json.
            return new JsonResult(inferenceResult);

        }
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#reuse-inputoutput-tensor-buffers) Reuse input/output tensor buffers

In some scenarios, you may want to reuse input/output tensors. This often happens when you want to chain 2 models (ie. feed one's output as input to another), or want to accelerate inference speed during multiple inference runs.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#chaining-feed-model-as-outputs-as-inputs-to-model-b) Chaining: Feed model A's output(s) as input(s) to model B

``` highlight
using Microsoft.ML.OnnxRuntime.Tensors;
using Microsoft.ML.OnnxRuntime;

namespace Samples
;
            long[] inputShape = ;

            using var inputOrtValue = OrtValue.CreateTensorValueFromMemory(inputData, inputShape);

            // Create input data for session. Request all outputs in this case.
            var inputs1 = new Dictionary<string, OrtValue>
            
            };

            using var runOptions = new RunOptions();

            // session1 inference
            using (var outputs1 = session1.Run(runOptions, inputs1, session1.OutputNames))
            
                };

                // session2 inference
                using (var results = session2.Run(runOptions, inputs2, session2.OutputNames))
                
            }
        }
    }
}
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#multiple-inference-runs-with-fixed-sized-inputs-and-outputs) Multiple inference runs with fixed sized input(s) and output(s)

If the model have fixed sized inputs and outputs of numeric tensors, use the preferable **OrtValue** and its API to accelerate the inference speed and minimize data transfer. **OrtValue** class makes it possible to reuse the underlying buffer for the input and output tensors. It pins the managed buffers and makes use of them for inference. It also provides direct access to the native buffers for outputs. You can also preallocate `OrtValue` for outputs or create it on top of the existing buffers. This avoids some overhead which may be beneficial for smaller models where the time is noticeable in the overall running time.

Keep in mind that **OrtValue** class, like many other classes in Onnruntime C# API is **IDisposable**. It needs to be properly disposed to either unpin the managed buffers or release the native buffers to avoid memory leaks.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#running-on-gpu-optional) Running on GPU (Optional)

If using the GPU package, simply use the appropriate SessionOptions when creating an InferenceSession.

``` highlight
int gpuDeviceId = 0; // The GPU device ID to execute on
using var gpuSessionOptoins = SessionOptions.MakeSessionOptionWithCudaProvider(gpuDeviceId);
using var session = new InferenceSession("model.onnx", gpuSessionOptoins);
```

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-c-api) ONNX Runtime C# API 

The ONNX runtime provides a C# .NET binding for running inference on ONNX models in any of the .NET standard platforms.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#supported-versions) Supported Versions

.NET standard 1.1

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#builds) Builds

  Artifact                                                                                                Description                                Supported Platforms
  ------------------------------------------------------------------------------------------------------- ------------------------------------------ ----------------------------------------------------------------------------------------------------------------------------------------
  [Microsoft.ML.OnnxRuntime](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime)                     CPU (Release)                              Windows, Linux, Mac, X64, X86 (Windows-only), ARM64 (Windows-only)...more details: [compatibility](/docs/reference/compatibility.html)
  [Microsoft.ML.OnnxRuntime.Gpu](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.gpu)             GPU - CUDA (Release)                       Windows, Linux, Mac, X64...more details: [compatibility](/docs/reference/compatibility.html)
  [Microsoft.ML.OnnxRuntime.DirectML](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime.directml)   GPU - DirectML (Release)                   Windows 10 1709+
  [onnxruntime](https://aiinfra.visualstudio.com/PublicPackages/_packaging?_a=feed&feed=ORT-Nightly)      CPU, GPU (Dev), CPU (On-Device Training)   Same as Release versions
  [Microsoft.ML.OnnxRuntime.Training](https://www.nuget.org/packages/Microsoft.ML.OnnxRuntime)            CPU On-Device Training (Release)           Windows, Linux, Mac, X64, X86 (Windows-only), ARM64 (Windows-only)...more details: [compatibility](/docs/reference/compatibility.html)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#api-reference) API Reference

[C# API Reference](../api/csharp/api)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#samples) Samples

See [Tutorials: Basics - C#](../tutorials/api-basics)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#learn-more) Learn More

- [C# Tutorials](../tutorials/)
- [C# API Reference](../api/csharp/api)