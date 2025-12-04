# Source: https://onnxruntime.ai/docs/genai/tutorials/phi2-python.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#language-generation-in-python-with-phi-2) Language generation in Python with Phi-2

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setup-and-installation) Setup and installation

Install the ONNX Runtime generate() API Python package using the [installation instructions](/docs/genai/howto/install.html).

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#build-phi-2-onnx-model) Build phi-2 ONNX model

The onnxruntime-genai package contains a model builder that generates the phi-2 ONNX model using the weights and config on Huggingface. The tools also allows you to download the weights from Hugging Face, load locally stored weights, or convert from GGUF format. For more details, see [how to build models](/docs/genai/howto/build-model.html)

If using the `-m` option shown here, you will need to login into Hugging Face.

``` highlight
pip install huggingface-hub
huggingface-cli login
```

You can build the model in different precisions. This command uses int4 as it produces the smallest model and can run on a CPU.

``` highlight
python -m onnxruntime_genai.models.builder -m microsoft/phi-2 -e cpu -p int4 -o ./example-models/phi2-int4-cpu
```

You can replace the name of the output folder specified with the `-o` option with a folder of your choice.

After you run the script, you will see a series of files generated in this folder. They include the HuggingFace configs for your reference, as well as the following generated files used by ONNX Runtime generate() API.

- `model.onnx`: the phi-2 ONNX model
- `model.onnx.data`: the phi-2 ONNX model weights
- `genai_config.json`: the configuration used by ONNX Runtime generate() API

You can view and change the values in the `genai_config.json` file. The model section should not be updated unless you have brought your own model and it has different parameters.

The search parameters can be changed. For example, you might want to generate with a different temperature value. These values can also be set via the `set_search_options` method shown below.

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-the-model-with-a-sample-prompt) Run the model with a sample prompt

Run the model with the following Python script. You can change the prompt and other parameters as needed.

``` highlight
import onnxruntime_genai as og

prompt = '''def print_prime(n):
    """
    Print all primes between 1 and n
    """'''

model=og.Model(f'example-models/phi2-int4-cpu')

tokenizer = og.Tokenizer(model)

tokens = tokenizer.encode(prompt)

params=og.GeneratorParams(model)
params.set_search_options()
params.input_ids = tokens

output_tokens=model.generate(params)[0]

text = tokenizer.decode(output_tokens)

print(text)
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#run-batches-of-prompts) Run batches of prompts

You can also run batches of prompts through the model.

``` highlight
prompts = [
    "This is a test.",
    "Rats are awesome pets!",
    "The quick brown fox jumps over the lazy dog.",
    ]

inputs = tokenizer.encode_batch(prompts)

params=og.GeneratorParams(model)
params.input_ids = tokens

outputs = model.generate(params)[0]

text = tokenizer.decode(output_tokens)
```

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#stream-the-output-of-the-tokenizer) Stream the output of the tokenizer

If you are developing an application that requires tokens to be output to the user interface one at a time, you can use the streaming tokenizer.

``` highlight
generator=og.Generator(model, params)
tokenizer_stream=tokenizer.create_stream()

print(prompt, end='', flush=True)

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token_top_p(0.7, 0.6)
    print(tokenizer_stream.decode(generator.get_next_tokens()[0]), end='', flush=True)
```