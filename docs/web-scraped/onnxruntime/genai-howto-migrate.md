# Source: https://onnxruntime.ai/docs/genai/howto/migrate.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#migrate-onnx-runtime-generate-api-from-052-to-060) Migrate ONNX Runtime generate() API from 0.5.2 to 0.6.0 

Learn how to migrate from ONNX Runtime generate() version 0.5.2 to version 0.6.0.

Version 0.6.0 adds support for "chat mode", also known as *continuation*, *continuous decoding*, and *interactive decoding*. With the introduction of chat mode, a breaking API change was made.

In summary, the new API adds an `AppendTokens` method to the `Generator`, which allows for multi-turn conversations. Previously, input was set in `GeneratorParams` prior to the creation of the `Generator`.

Calling `AppendTokens` outside of the conversation loop can be used to implement system prompt caching.

Note: chat mode and system prompt caching are only supported for batch size 1. Furthermore, they are currently supported on CPU, NVIDIA GPUs with the CUDA EP, and all GPUs with the Web GPU native EP. They are not supported on NPU or GPUs running with the DirecML EP. For question & answer (Q&A) mode, the migrations described below *are* still required.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#python) Python

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#migrate-python-question-and-answer-single-turn-code-to-060) Migrate Python question and answer (single turn) code to 0.6.0 

1.  Replace calls to `params.input_ids = input_tokens` with `generator.append_tokens(input_tokens)` after the generator object has been created.
2.  Remove calls to `generator.compute_logits()`
3.  If the application has a Q&A loop, delete the `generator` between `append_token` call to reset the state of the model.

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-system-prompt-caching-to-python-applications) Add system prompt caching to Python applications

1.  Create and tokenize the system prompt and call `generator.append_tokens(system_tokens)`. This call can be done before the user is asked for their prompt.

    :::: 
    ::: highlight
    ``` highlight
    system_tokens = tokenizer.encode(system_prompt)
    generator.append_tokens(system_tokens)
    ```
    :::
    ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-chat-mode-to-python-applications) Add chat mode to Python applications

1.  Create a loop in your application, and call `generator.append_tokens(prompt)` every time the user provides new input:

    :::: 
    ::: highlight
    ``` highlight
    while True:
        user_input = input("Input: ")
        input_tokens = tokenizer.encode(user_input)
        generator.append_tokens(input_tokens)

        while not generator.is_done():
            generator.generate_next_token()

            new_token = generator.get_next_tokens()[0]
            print(tokenizer_stream.decode(new_token), end='', flush=True)
         except KeyboardInterrupt:
         print()
    ```
    :::
    ::::

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#c) C++

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#migrate-c-question-and-answer-single-turn-code-to-060) Migrate C++ question and answer (single turn) code to 0.6.0 

1.  Replace calls to `params->SetInputSequences(*sequences)` with `generator->AppendTokenSequences(*sequences)`
2.  Remove calls to `generator->ComputeLogits()`

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-system-prompt-caching-to-c-applications) Add system prompt caching to C++ applications

1.  Create and tokenize the system prompt and call `generator->AppendTokenSequences(*sequences)`. This call can be done before the user is asked for their prompt.

    :::: 
    ::: highlight
    ``` highlight
    auto sequences = OgaSequences::Create();
    tokenizer->Encode(system_prompt.c_str(), *sequences);
    generator->AppendTokenSequences(*sequences);
    generator.append_tokens(system_tokens)
    ```
    :::
    ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-chat-mode-to-your-c-application) Add chat mode to your C++ application

1.  Add a chat loop to your application

    :::: 
    ::: highlight
    ``` highlight
    std::cout << "Generating response..." << std::endl;
    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 1024);

    auto generator = OgaGenerator::Create(*model, *params);

    while (true) 
    }
    ```
    :::
    ::::

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#c-1) C#

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#migrate-c-question-and-answer-single-turn-code-to-060-1) Migrate C# question and answer (single turn) code to 0.6.0 

1.  Replace calls to `generatorParams.SetInputSequences(sequences)` with `generator.AppendTokenSequences`(sequences)\`
2.  Remove calls to `generator.ComputeLogits()`

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-system-prompt-caching-to-your-c-application) Add system prompt caching to your C# application

1.  Create and tokenize the system prompt and call `generator->AppendTokenSequences()`. This call can be done before the user is asked for their prompt.

    :::: 
    ::: highlight
    ``` highlight
    var systemPrompt = "..."
    auto sequences = OgaSequences::Create();
    tokenizer->Encode(systemPrompt, *sequences);
    generator->AppendTokenSequences(*sequences);
    ```
    :::
    ::::

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#add-chat-mode-to-your-c-application-1) Add chat mode to your C# application

1.  Add a chat loop to your application

    :::: 
    ::: highlight
    ``` highlight
    using var tokenizerStream = tokenizer.CreateStream();
    using var generator = new Generator(model, generatorParams);
    Console.WriteLine("Prompt:");
    prompt = Console.ReadLine();

    // Example Phi-3 template
    var sequences = tokenizer.Encode($"<|user|><|end|><|assistant|>");

    do
    
       Console.WriteLine();
       watch.Stop();
       var runTimeInSeconds = watch.Elapsed.TotalSeconds;
       var outputSequence = generator.GetSequence(0);
       var totalTokens = outputSequence.Length;
       Console.WriteLine($"Streaming Tokens:  Time:  Tokens per second: ");
       Console.WriteLine("Next prompt:");
       var nextPrompt = Console.ReadLine();
       sequences = tokenizer.Encode($"<|user|><|end|><|assistant|>");
    } while (prompt != null);
    ```
    :::
    ::::

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#java) Java

*Coming soon*