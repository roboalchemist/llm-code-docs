# Source: https://onnxruntime.ai/docs/genai/tutorials/snapdragon.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-slms-on-snapdragon-devices-with-npus) Run SLMs on Snapdragon devices with NPUs

Learn how to run SLMs on Snapdragon devices with ONNX Runtime.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#models) Models

Models supported currently are:

- Phi-3.5 mini instruct
- Llama 3.2 3B

Devices with Snapdragon NPUs requires models in a specific size and format.

Instructions to generate models in this format can be found in [Build models for snapdragon](/docs/genai/howto/build-models-for-snapdragon.html)

Once you have built or downloaded the model, place the model assets in a known location. These assets consist of:

- genai_config.json
- tokenizer.json
- tokenizer_config.json
- special_tokens_map.json
- quantizer.onnx
- dequantizer.onnx
- position-processor.onnx
- a set of transformer model binaries
  - Qualcomm context binaries (\*.bin)
  - Context binary meta data (\*.json)
  - ONNX wrapper models (\*.onnx)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python-application) Python application

If your device has Python installed, you can run a simple question and answering script to query the model.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-the-runtime) Install the runtime

``` highlight
pip install onnxruntime-genai
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#download-the-script) Download the script

``` highlight
curl https://raw.githubusercontent.com/microsoft/onnxruntime-genai/refs/heads/main/examples/python/model-qa.py -o model-qa.py
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-the-script) Run the script

This script assumes that the model assets are in a folder called models\\Phi-3.5-mini-instruct

``` highlight
python .\model-qa.py -e cpu -g -v --system_prompt "You are a helpful assistant. Be brief and concise." --chat_template "<|user|>\n <|end|>\n<|assistant|>" -m ..\..\models\Phi-3.5-mini-instruct
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#a-look-inside-the-python-script) A look inside the Python script

The complete Python script is published here: https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/model-qa.py. The script utilizes the API in the following standard way:

1.  Load the model

    :::: 
    ::: highlight
    ``` highlight
    model = og.Model(config)
    ```
    :::
    ::::

    This loads the model into memory.

2.  Create pre processors and tokenize system prompt

    :::: 
    ::: highlight
    ``` highlight
     tokenizer = og.Tokenizer(model)
     tokenizer_stream = tokenizer.create_stream()

     # Optional
     system_tokens = tokenizer.encode(system_prompt)
    ```
    :::
    ::::

    This creates a tokenizer and a tokenizer stream which allows tokens to be returned to the user as they are generated.

3.  Interactive input loop

    :::: 
    ::: highlight
    ``` highlight
    while True:
        # Read prompt
        # Run the generation, streaming the output tokens
    ```
    :::
    ::::

4.  Generative loop

    :::: 
    ::: highlight
    ``` highlight
    # 1. Pre-process the prompt into tokens
    input_tokens = tokenizer.encode(prompt)

    # 2. Create parameters and generator (KV cache etc) and process the prompt
    params = og.GeneratorParams(model)
    params.set_search_options(**search_options)
    generator = og.Generator(model, params)
    generator.append_tokens(system_tokens + input_tokens)

    # 3. Loop until all output tokens are generated, printing
    # out the decoded token
    while not generator.is_done():
        generator.generate_next_token()

        new_token = generator.get_next_tokens()[0]
        print(tokenizer_stream.decode(new_token), end="", flush=True)

     print()
        
     # Delete the generator to free the captured graph before creating another one
     del generator
    ```
    :::
    ::::

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#c-application) C++ Application

To run the models on snadragon NPU within a C++ application, use the code from here: https://github.com/microsoft/onnxruntime-genai/tree/main/examples/c.

Building and running this application requires a Windows PC with a Snapdragon NPU, as well as:

- cmake
- Visual Studio 2022

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#clone-the-repo) Clone the repo

``` highlight
   git clone https://github.com/microsoft/onnxruntime-genai
   cd examples\c
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnxruntime) Install onnxruntime

Currently requires the nightly build of onnxruntime, as there are up to the minute changes to QNN support for language models.

Download the nightly version of the ONNX Runtime QNN binaries from [here](https://aiinfra.visualstudio.com/PublicPackages/_artifacts/feed/ORT-Nightly/NuGet/Microsoft.ML.OnnxRuntime.QNN/overview/1.22.0-dev-20250225-0548-e46c0d8)

``` highlight
   mkdir onnxruntime-win-arm64-qnn
   move Microsoft.ML.OnnxRuntime.QNN.1.22.0-dev-20250225-0548-e46c0d8.nupkg onnxruntime-win-arm64-qnn
   cd onnxruntime-win-arm64-qnn
   tar xvzf Microsoft.ML.OnnxRuntime.QNN.1.22.0-dev-20250225-0548-e46c0d8.nupkg
   copy runtimes\win-arm64\native\* ..\..\..\lib
   cd ..
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-onnxruntime-genai) Install onnxruntime-genai

``` highlight
   curl https://github.com/microsoft/onnxruntime-genai/releases/download/v0.6.0/onnxruntime-genai-0.6.0-win-arm64.zip -o onnxruntime-genai-win-arm64.zip
   tar xvf onnxruntime-genai-win-arm64.zip
   cd onnxruntime-genai-0.6.0-win-arm64
   copy include\* ..\include
   copy lib\* ..\lib
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-the-sample) Build the sample

``` highlight
   cmake -A arm64 -S . -B build -DPHI3-QA=ON
   cd build
   cmake --build . --config Release
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-the-sample) Run the sample

``` highlight
   cd Release
   .\phi3_qa.exe <path_to_model>
```

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#a-look-inside-the-c-sample) A look inside the C++ sample

The C++ application is published here: https://github.com/microsoft/onnxruntime-genai/blob/main/examples/c/src/phi3_qa.cpp. The script utilizes the API in the following standard way:

1.  Load the model

    :::: 
    ::: highlight
    ``` highlight
    auto model = OgaModel::Create(*config);
    ```
    :::
    ::::

    This loads the model into memory.

2.  Create pre processors

    :::: 
    ::: highlight
    ``` highlight
    auto tokenizer = OgaTokenizer::Create(*model);
    auto tokenizer_stream = OgaTokenizerStream::Create(*tokenizer);
    ```
    :::
    ::::

    This creates a tokenizer and a tokenizer stream which allows tokens to be returned to the user as they are generated.

3.  Interactive input loop

    :::: 
    ::: highlight
    ``` highlight
    while True:
        # Read prompt
        # Run the generation, streaming the output tokens
    ```
    :::
    ::::

4.  Generative loop

    :::: 
    ::: highlight
    ``` highlight
    # 1. Pre-process the prompt into tokens
    auto sequences = OgaSequences::Create();
    tokenizer->Encode(prompt.c_str(), *sequences);
       
    # 2. Create parameters and generator (KV cache etc) and process the prompt
    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 1024);
    auto generator = OgaGenerator::Create(*model, *params);
    generator->AppendTokenSequences(*sequences);

    # 3. Loop until all output tokens are generated, printing
    # out the decoded token
    while (!generator->IsDone()) 

      const auto num_tokens = generator->GetSequenceCount(0);
      const auto new_token = generator->GetSequenceData(0)[num_tokens - 1];
      std::cout << tokenizer_stream->Decode(new_token) << std::flush;
    }
    ```
    :::
    ::::