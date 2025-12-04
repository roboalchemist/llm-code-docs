# Source: https://onnxruntime.ai/docs/genai/api/java.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-generate-java-api) ONNX Runtime generate() Java API

*Note: this API is in preview and is subject to change.*

- [Overview](#overview)
- [Install and import](#install-and-import)
- [Model class](#model-class)
  - [Constructor](#constructor)
  - [createGeneratorParams](#creategeneratorparams)
  - [createTokenizer](#createtokenizer)
  - [generate](#generate)
- [Config class](#config-class)
  - [Constructor](#constructor-1)
  - [clearProviders](#clearproviders)
  - [appendProvider](#appendprovider)
  - [setProviderOption](#setprovideroption)
  - [overlay](#overlay)
- [Tokenizer class](#tokenizer-class)
  - [Constructor](#constructor-2)
  - [encode](#encode)
  - [encodeBatch](#encodebatch)
  - [decode](#decode)
  - [decodeBatch](#decodebatch)
  - [createStream](#createstream)
- [TokenizerStream class](#tokenizerstream-class)
  - [decode](#decode-1)
- [GeneratorParams class](#generatorparams-class)
  - [Constructor](#constructor-3)
  - [setSearchOption (double)](#setsearchoption-double)
  - [setSearchOption (boolean)](#setsearchoption-boolean)
  - [setInput (Sequences)](#setinput-sequences)
  - [setInput (int\[\])](#setinput-int)
- [Generator class](#generator-class)
  - [Constructor](#constructor-4)
  - [isDone](#isdone)
  - [computeLogits](#computelogits)
  - [generateNextToken](#generatenexttoken)
  - [getSequence](#getsequence)
  - [getLastTokenInSequence](#getlasttokeninsequence)
- [Sequences class](#sequences-class)
  - [numSequences](#numsequences)
  - [getSequence](#getsequence-1)
- [Tensor class](#tensor-class)
  - [Constructor](#constructor-5)
- [Result class](#result-class)
  - [isSuccess](#issuccess)
  - [getError](#geterror)
- [Utils class](#utils-class)
  - [setLogBool](#setlogbool)
  - [setLogString](#setlogstring)
  - [setCurrentGpuDeviceId](#setcurrentgpudeviceid)
  - [getCurrentGpuDeviceId](#getcurrentgpudeviceid)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#overview) Overview

This document describes the Java API for ONNX Runtime GenAI.\
Below are the main classes and methods, with code snippets and descriptions for each.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#install-and-import) Install and import

The Java API is delivered by the `ai.onnxruntime.genai` Java package. Package publication is pending. To build the package from source, see the [build from source guide](/docs/genai/howto/build-from-source.html).

``` highlight
import ai.onnxruntime.genai.*;
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#model-class) Model class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#constructor) Constructor

Initializes a new model from the given model path.

``` highlight
public Model(String modelPath) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#creategeneratorparams) createGeneratorParams

Creates a GeneratorParams instance for executing the model.

``` highlight
public GeneratorParams createGeneratorParams() throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#createtokenizer) createTokenizer

Creates a Tokenizer instance for this model.

``` highlight
public Tokenizer createTokenizer() throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generate) generate

Generates output sequences using the provided generator parameters.

``` highlight
public Sequences generate(GeneratorParams generatorParams) throws GenAIException
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#config-class) Config class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#constructor-1) Constructor

Initializes a new configuration object from a config path.

``` highlight
public Config(String configPath) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#clearproviders) clearProviders

Clears all providers from the configuration.

``` highlight
public void clearProviders() throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#appendprovider) appendProvider

Appends a provider to the configuration.

``` highlight
public void appendProvider(String provider) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setprovideroption) setProviderOption

Sets a provider option in the configuration.

``` highlight
public void setProviderOption(String provider, String name, String value) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#overlay) overlay

Overlays a JSON string onto the configuration.

``` highlight
public void overlay(String json) throws GenAIException
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tokenizer-class) Tokenizer class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#constructor-2) Constructor

Initializes a tokenizer for the given model.

``` highlight
public Tokenizer(Model model) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#encode) encode

Encodes a string into a sequence of token ids.

``` highlight
public Sequences encode(String string) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#encodebatch) encodeBatch

Encodes an array of strings into a sequence of token ids for each input.

``` highlight
public Sequences encodeBatch(String[] strings) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#decode) decode

Decodes a sequence of token ids into text.

``` highlight
public String decode(int[] sequence) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#decodebatch) decodeBatch

Decodes a batch of sequences of token ids into text.

``` highlight
public String[] decodeBatch(Sequences sequences) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#createstream) createStream

Creates a TokenizerStream object for streaming tokenization.

``` highlight
public TokenizerStream createStream() throws GenAIException
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tokenizerstream-class) TokenizerStream class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#decode-1) decode

Decodes a single token in the stream and returns the generated string chunk.

``` highlight
public String decode(int token) throws GenAIException
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generatorparams-class) GeneratorParams class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#constructor-3) Constructor

Initializes generator parameters for the given model.

``` highlight
public GeneratorParams(Model model) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setsearchoption-double) setSearchOption (double)

Sets a numeric search option.

``` highlight
public void setSearchOption(String optionName, double value) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setsearchoption-boolean) setSearchOption (boolean)

Sets a boolean search option.

``` highlight
public void setSearchOption(String optionName, boolean value) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setinput-sequences) setInput (Sequences)

Sets the prompt(s) for model execution using sequences.

``` highlight
public void setInput(Sequences sequences) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setinput-int) setInput (int\[\])

Sets the prompt(s) token ids for model execution.

``` highlight
public void setInput(int[] tokenIds, int sequenceLength, int batchSize) throws GenAIException
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generator-class) Generator class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#constructor-4) Constructor

Constructs a Generator object with the given model and generator parameters.

``` highlight
public Generator(Model model, GeneratorParams generatorParams) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#isdone) isDone

Checks if the generation process is done.

``` highlight
public boolean isDone()
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#computelogits) computeLogits

Computes the logits for the next token in the sequence.

``` highlight
public void computeLogits() throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generatenexttoken) generateNextToken

Generates the next token in the sequence.

``` highlight
public void generateNextToken() throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#getsequence) getSequence

Retrieves a sequence of token ids for the specified sequence index.

``` highlight
public int[] getSequence(long sequenceIndex) throws GenAIException
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#getlasttokeninsequence) getLastTokenInSequence

Retrieves the last token in the sequence for the specified sequence index.

``` highlight
public int getLastTokenInSequence(long sequenceIndex) throws GenAIException
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#sequences-class) Sequences class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#numsequences) numSequences

Gets the number of sequences in the collection.

``` highlight
public long numSequences()
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#getsequence-1) getSequence

Gets the sequence at the specified index.

``` highlight
public int[] getSequence(long sequenceIndex)
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tensor-class) Tensor class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#constructor-5) Constructor

Constructs a Tensor with the given data, shape, and element type.

``` highlight
public Tensor(ByteBuffer data, long[] shape, ElementType elementType) throws GenAIException
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#result-class) Result class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#issuccess) isSuccess

Indicates if the operation was successful.

``` highlight
public boolean isSuccess()
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#geterror) getError

Gets the error message from a failed operation.

``` highlight
public String getError()
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#utils-class) Utils class

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setlogbool) setLogBool

Sets a boolean logging option.

``` highlight
public static void setLogBool(String name, boolean value)
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setlogstring) setLogString

Sets a string logging option.

``` highlight
public static void setLogString(String name, String value)
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#setcurrentgpudeviceid) setCurrentGpuDeviceId

Sets the current GPU device ID.

``` highlight
public static void setCurrentGpuDeviceId(int deviceId)
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#getcurrentgpudeviceid) getCurrentGpuDeviceId

Gets the current GPU device ID.

``` highlight
public static int getCurrentGpuDeviceId()
```

------------------------------------------------------------------------