# Source: https://onnxruntime.ai/docs/tutorials/csharp/resnet50_csharp.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#image-recognition-with-resnet50v2-in-c) Image recognition with ResNet50v2 in C# 

The sample walks through how to run a pretrained ResNet50 v2 ONNX model using the Onnx Runtime C# API.

The source code for this sample is available [here](https://github.com/microsoft/onnxruntime/tree/main/csharp/sample/Microsoft.ML.OnnxRuntime.ResNet50v2Sample).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#contents) Contents 

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Read paths](#read-paths)
  - [Read image](#read-image)
  - [Resize image](#resize-image)
  - [Preprocess image](#preprocess-image)
  - [Setup inputs](#setup-inputs)
  - [Run inference](#run-inference)
  - [Postprocess output](#postprocess-output)
  - [Extract top 10](#extract-top-10)
  - [Print results](#print-results)
- [Running the program](#running-the-program)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#prerequisites) Prerequisites

To run this sample, you'll need the following things:

1.  Install [.NET Core 3.1](https://dotnet.microsoft.com/download/dotnet-core/3.1) or higher for you OS (Mac, Windows or Linux).
2.  Download the [ResNet50 v2](https://github.com/onnx/models/blob/main/validated/vision/classification/resnet/model/resnet50-v2-7.onnx) ONNX model to your local system.
3.  Download [this picture of a dog](/images/dog.jpeg) to test the model. You can also use any image you like.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#getting-started) Getting Started

Now we have everything set up, we can start adding code to run the model on the image. We'll do this in the main method of the program for simplicity.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#read-paths) Read paths

Firstly, let's read the path to the model and path to the image we want to test in through program arguments:

``` highlight
string modelFilePath = args[0];
string imageFilePath = args[1];
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#read-image) Read image

Next, we will read the image in using the cross-platform image library [ImageSharp](https://www.nuget.org/packages/SixLabors.ImageSharp):

``` highlight
using Image<Rgb24> image = Image.Load<Rgb24>(imageFilePath, out IImageFormat format);
```

Note, we're specifically reading the `Rgb24` type so we can efficiently preprocess the image in a later step.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#resize-image) Resize image

Next, we will resize the image to the appropriate size that the model is expecting; 224 pixels by 224 pixels:

``` highlight
using Stream imageStream = new MemoryStream();
image.Mutate(x =>
);
});
image.Save(imageStream, format);
```

Note, we're doing a centered crop resize to preserve aspect ratio.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#preprocess-image) Preprocess image

Next, we will preprocess the image according to the [requirements of the model](https://github.com/onnx/models/tree/main/validated/vision/classification/resnet#preprocessing):

``` highlight
// We use DenseTensor for multi-dimensional access to populate the image data
var mean = new[] ;
var stddev = new[] ;
DenseTensor<float> processedImage = new(new[] );
image.ProcessPixelRows(accessor =>

    }
});
```

Here, we're creating a Tensor of the required size `(batch-size, channels, height, width)`, accessing the pixel values, preprocessing them and finally assigning them to the tensor at the appropriate indicies.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setup-inputs) Setup inputs

Next, we will create the inputs to the model:

``` highlight
// Pin tensor buffer and create a OrtValue with native tensor that makes use of
// DenseTensor buffer directly. This avoids extra data copy within OnnxRuntime.
// It will be unpinned on ortValue disposal
using var inputOrtValue = OrtValue.CreateTensorValueFromMemory(OrtMemoryInfo.DefaultInstance,
    processedImage.Buffer, new long[] );

var inputs = new Dictionary<string, OrtValue>

}
```

To check the input node names for an ONNX model, you can use [Netron](https://github.com/lutzroeder/netron) to visualise the model and see input/output names. In this case, this model has `data` as the input node name.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-inference) Run inference

Next, we will create an inference session and run the input through it:

``` highlight
using var session = new InferenceSession(modelFilePath);
using var runOptions = new RunOptions();
using IDisposableReadOnlyCollection<OrtValue> results = session.Run(runOptions, inputs, session.OutputNames);
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#postprocess-output) Postprocess output

Next, we will need to postprocess the output to get the softmax vector, as this is not handled by the model itself:

``` highlight
// We copy results to array only to apply algorithms, otherwise data can be accessed directly
// from the native buffer via ReadOnlySpan<T> or Span<T>
var output = results[0].GetTensorDataAsSpan<float>().ToArray();
float sum = output.Sum(x => (float)Math.Exp(x));
IEnumerable<float> softmax = output.Select(x => (float)Math.Exp(x) / sum);
```

Other models may apply a Softmax node before the output, in which case you won't need this step. Again, you can use Netron to see the model outputs.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#extract-top-10) Extract top 10

Next, we will extract the top 10 class predictions:

``` highlight
IEnumerable<Prediction> top10 = softmax.Select((x, i) => new Prediction )
                                       .OrderByDescending(x => x.Confidence)
                                       .Take(10);
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#print-results) Print results

Next, we will print the top 10 results to the console:

``` highlight
Console.WriteLine("Top 10 predictions for ResNet50 v2...");
Console.WriteLine("--------------------------------------------------------------");
foreach (var t in top10)
, Confidence: ");
}
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#running-the-program) Running the program

Now the program is created, we can run it will the following command:

``` highlight
dotnet run [path-to-model] [path-to-image]
```

e.g.

``` highlight
dotnet run ~/Downloads/resnet50-v2-7.onnx ~/Downloads/dog.jpeg
```

Running this on the following image:

![](/images/dog.jpeg)

We get the following output:

``` highlight
Top 10 predictions for ResNet50 v2...
--------------------------------------------------------------
Label: Golden Retriever, Confidence: 0.9212826
Label: Kuvasz, Confidence: 0.026514154
Label: Clumber Spaniel, Confidence: 0.012455719
Label: Labrador Retriever, Confidence: 0.004103844
Label: Saluki, Confidence: 0.0033182495
Label: Flat-Coated Retriever, Confidence: 0.0032045357
Label: English Setter, Confidence: 0.002513516
Label: Brittany, Confidence: 0.0023459378
Label: Cocker Spaniels, Confidence: 0.0019343802
Label: Sussex Spaniel, Confidence: 0.0019247672
```