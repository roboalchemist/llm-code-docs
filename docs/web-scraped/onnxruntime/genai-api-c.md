# Source: https://onnxruntime.ai/docs/genai/api/c.html

# [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#onnx-runtime-generate-c-api) ONNX Runtime generate() C API

*Note: this API is in preview and is subject to change.*

- [Overview](#overview)
- [Model API](#model-api)
  - [OgaCreateModel](#ogacreatemodel)
  - [OgaDestroyModel](#ogadestroymodel)
  - [OgaCreateModelWithRuntimeSettings](#ogacreatemodelwithruntimesettings)
  - [OgaCreateModelFromConfig](#ogacreatemodelfromconfig)
  - [OgaModelGetType](#ogamodelgettype)
  - [OgaModelGetDeviceType](#ogamodelgetdevicetype)
- [Config API](#config-api)
  - [OgaCreateConfig](#ogacreateconfig)
  - [OgaConfigClearProviders](#ogaconfigclearproviders)
  - [OgaConfigAppendProvider](#ogaconfigappendprovider)
  - [OgaConfigSetProviderOption](#ogaconfigsetprovideroption)
  - [OgaConfigOverlay](#ogaconfigoverlay)
  - [OgaDestroyConfig](#ogadestroyconfig)
- [Runtime Settings API](#runtime-settings-api)
  - [OgaCreateRuntimeSettings](#ogacreateruntimesettings)
  - [OgaRuntimeSettingsSetHandle](#ogaruntimesettingssethandle)
  - [OgaDestroyRuntimeSettings](#ogadestroyruntimesettings)
- [Tokenizer API](#tokenizer-api)
  - [OgaCreateTokenizer](#ogacreatetokenizer)
  - [OgaDestroyTokenizer](#ogadestroytokenizer)
  - [OgaTokenizerEncode](#ogatokenizerencode)
  - [OgaTokenizerEncodeBatch](#ogatokenizerencodebatch)
  - [OgaTokenizerToTokenId](#ogatokenizertotokenid)
  - [OgaTokenizerDecode](#ogatokenizerdecode)
  - [OgaTokenizerApplyChatTemplate](#ogatokenizerapplychattemplate)
  - [OgaTokenizerDecodeBatch](#ogatokenizerdecodebatch)
  - [OgaCreateTokenizerStream](#ogacreatetokenizerstream)
  - [OgaDestroyTokenizerStream](#ogadestroytokenizerstream)
  - [OgaTokenizerStreamDecode](#ogatokenizerstreamdecode)
- [Sequences API](#sequences-api)
  - [OgaCreateSequences](#ogacreatesequences)
  - [OgaDestroySequences](#ogadestroysequences)
  - [OgaSequencesCount](#ogasequencescount)
  - [OgaSequencesGetSequenceCount](#ogasequencesgetsequencecount)
  - [OgaSequencesGetSequenceData](#ogasequencesgetsequencedata)
- [Generator Params API](#generator-params-api)
  - [OgaCreateGeneratorParams](#ogacreategeneratorparams)
  - [OgaDestroyGeneratorParams](#ogadestroygeneratorparams)
  - [OgaGeneratorParamsSetSearchNumber](#ogageneratorparamssetsearchnumber)
  - [OgaGeneratorParamsSetSearchBool](#ogageneratorparamssetsearchbool)
  - [OgaGeneratorParamsTryGraphCaptureWithMaxBatchSize](#ogageneratorparamstrygraphcapturewithmaxbatchsize)
  - [OgaGeneratorParamsSetInputIDs](#ogageneratorparamssetinputids)
  - [OgaGeneratorParamsSetInputSequences](#ogageneratorparamssetinputsequences)
  - [OgaGeneratorParamsSetModelInput](#ogageneratorparamssetmodelinput)
  - [OgaGeneratorParamsSetInputs](#ogageneratorparamssetinputs)
  - [OgaGeneratorParamsSetGuidance](#ogageneratorparamssetguidance)
- [Generator API](#generator-api)
  - [OgaCreateGenerator](#ogacreategenerator)
  - [OgaDestroyGenerator](#ogadestroygenerator)
  - [OgaGenerator_IsDone](#ogagenerator_isdone)
  - [OgaGenerator_AppendTokenSequences](#ogagenerator_appendtokensequences)
  - [OgaGenerator_AppendTokens](#ogagenerator_appendtokens)
  - [OgaGenerator_IsSessionTerminated](#ogagenerator_issessionterminated)
  - [OgaGenerator_GenerateNextToken](#ogagenerator_generatenexttoken)
  - [OgaGenerator_RewindTo](#ogagenerator_rewindto)
  - [OgaGenerator_SetRuntimeOption](#ogagenerator_setruntimeoption)
  - [OgaGenerator_GetSequenceCount](#ogagenerator_getsequencecount)
  - [OgaGenerator_GetSequenceData](#ogagenerator_getsequencedata)
  - [OgaGenerator_GetOutput](#ogagenerator_getoutput)
  - [OgaGenerator_GetLogits](#ogagenerator_getlogits)
  - [OgaGenerator_SetLogits](#ogagenerator_setlogits)
  - [OgaSetActiveAdapter](#ogasetactiveadapter)
- [Adapter API](#adapter-api)
  - [OgaCreateAdapters](#ogacreateadapters)
  - [OgaLoadAdapter](#ogaloadadapter)
  - [OgaUnloadAdapter](#ogaunloadadapter)
- [Tensor API](#tensor-api)
  - [OgaCreateTensorFromBuffer](#ogacreatetensorfrombuffer)
  - [OgaTensorGetType](#ogatensorgettype)
  - [OgaTensorGetShapeRank](#ogatensorgetshaperank)
  - [OgaTensorGetShape](#ogatensorgetshape)
  - [OgaTensorGetData](#ogatensorgetdata)
  - [OgaDestroyTensor](#ogadestroytensor)
- [Images and Audios API](#images-and-audios-api)
  - [OgaLoadImages](#ogaloadimages)
  - [OgaLoadImagesFromBuffers](#ogaloadimagesfrombuffers)
  - [OgaDestroyImages](#ogadestroyimages)
  - [OgaLoadAudios](#ogaloadaudios)
  - [OgaLoadAudiosFromBuffers](#ogaloadaudiosfrombuffers)
  - [OgaDestroyAudios](#ogadestroyaudios)
- [Named Tensors API](#named-tensors-api)
  - [OgaCreateNamedTensors](#ogacreatenamedtensors)
  - [OgaNamedTensorsGet](#oganamedtensorsget)
  - [OgaNamedTensorsSet](#oganamedtensorsset)
  - [OgaNamedTensorsDelete](#oganamedtensorsdelete)
  - [OgaNamedTensorsCount](#oganamedtensorscount)
  - [OgaNamedTensorsGetNames](#oganamedtensorsgetnames)
  - [OgaDestroyNamedTensors](#ogadestroynamedtensors)
- [Utility Functions](#utility-functions)
  - [OgaSetLogBool](#ogasetlogbool)
  - [OgaSetLogString](#ogasetlogstring)
  - [OgaSetCurrentGpuDeviceId](#ogasetcurrentgpudeviceid)
  - [OgaGetCurrentGpuDeviceId](#ogagetcurrentgpudeviceid)
  - [OgaResultGetError](#ogaresultgeterror)
  - [OgaDestroyResult](#ogadestroyresult)
  - [OgaDestroyString](#ogadestroystring)
  - [OgaDestroyBuffer](#ogadestroybuffer)
  - [OgaBufferGetType](#ogabuffergettype)
  - [OgaBufferGetDimCount](#ogabuffergetdimcount)
  - [OgaBufferGetDims](#ogabuffergetdims)
  - [OgaBufferGetData](#ogabuffergetdata)

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#overview) Overview

This document describes the C API for ONNX Runtime GenAI.\
Below are the main functions and types, with code snippets and descriptions for each.

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#model-api) Model API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatemodel) OgaCreateModel

Creates a model from the given directory. The directory should contain a file called `genai_config.json`, which corresponds to the [configuration specification](/docs/genai/reference/config.html).

``` highlight
OgaModel* model = NULL;
OgaResult* result = OgaCreateModel("path/to/model_dir", &model);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroymodel) OgaDestroyModel

Destroys the given model.

``` highlight
OgaDestroyModel(model);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatemodelwithruntimesettings) OgaCreateModelWithRuntimeSettings

Creates a model with runtime settings.

``` highlight
OgaRuntimeSettings* settings = NULL;
OgaCreateRuntimeSettings(&settings);
// ... configure settings ...
OgaModel* model = NULL;
OgaResult* result = OgaCreateModelWithRuntimeSettings("path/to/model_dir", settings, &model);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatemodelfromconfig) OgaCreateModelFromConfig

Creates a model from a config object.

``` highlight
OgaConfig* config = NULL;
OgaCreateConfig("path/to/model_dir", &config);
OgaModel* model = NULL;
OgaResult* result = OgaCreateModelFromConfig(config, &model);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogamodelgettype) OgaModelGetType

Gets the type of the model.

``` highlight
const char* type = NULL;
OgaModelGetType(model, &type);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogamodelgetdevicetype) OgaModelGetDeviceType

Gets the device type used by the model.

``` highlight
const char* device_type = NULL;
OgaModelGetDeviceType(model, &device_type);
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#config-api) Config API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreateconfig) OgaCreateConfig

Creates a configuration object from a config path.

``` highlight
OgaConfig* config = NULL;
OgaResult* result = OgaCreateConfig("path/to/model_dir", &config);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaconfigclearproviders) OgaConfigClearProviders

Clears all providers from the configuration.

``` highlight
OgaConfigClearProviders(config);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaconfigappendprovider) OgaConfigAppendProvider

Appends a provider to the configuration.

``` highlight
OgaConfigAppendProvider(config, "CUDAExecutionProvider");
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaconfigsetprovideroption) OgaConfigSetProviderOption

Sets a provider option in the configuration.

``` highlight
OgaConfigSetProviderOption(config, "CUDAExecutionProvider", "device_id", "0");
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaconfigoverlay) OgaConfigOverlay

Overlays a JSON string onto the configuration.

``` highlight
OgaConfigOverlay(config, "");
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroyconfig) OgaDestroyConfig

Destroys the configuration object.

``` highlight
OgaDestroyConfig(config);
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#runtime-settings-api) Runtime Settings API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreateruntimesettings) OgaCreateRuntimeSettings

Creates a runtime settings object.

``` highlight
OgaRuntimeSettings* settings = NULL;
OgaCreateRuntimeSettings(&settings);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaruntimesettingssethandle) OgaRuntimeSettingsSetHandle

Sets a named handle in the runtime settings.

``` highlight
OgaRuntimeSettingsSetHandle(settings, "custom_handle", handle_ptr);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroyruntimesettings) OgaDestroyRuntimeSettings

Destroys the runtime settings object.

``` highlight
OgaDestroyRuntimeSettings(settings);
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tokenizer-api) Tokenizer API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatetokenizer) OgaCreateTokenizer

Creates a tokenizer for the given model.

``` highlight
OgaTokenizer* tokenizer = NULL;
OgaResult* result = OgaCreateTokenizer(model, &tokenizer);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroytokenizer) OgaDestroyTokenizer

Destroys the tokenizer.

``` highlight
OgaDestroyTokenizer(tokenizer);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatokenizerencode) OgaTokenizerEncode

Encodes a single string and adds the encoded sequence of tokens to the OgaSequences.

``` highlight
OgaSequences* sequences = NULL;
OgaCreateSequences(&sequences);
OgaTokenizerEncode(tokenizer, "Hello world", sequences);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatokenizerencodebatch) OgaTokenizerEncodeBatch

Encodes a batch of strings.

``` highlight
const char* texts[] = ;
OgaTensor* tensor = NULL;
OgaTokenizerEncodeBatch(tokenizer, texts, 2, &tensor);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatokenizertotokenid) OgaTokenizerToTokenId

Converts a string to its corresponding token ID.

``` highlight
int32_t token_id = 0;
OgaTokenizerToTokenId(tokenizer, "Hello", &token_id);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatokenizerdecode) OgaTokenizerDecode

Decodes a sequence of tokens into a string.

``` highlight
const char* out_string = NULL;
OgaTokenizerDecode(tokenizer, tokens, token_count, &out_string);
// Use out_string, then:
OgaDestroyString(out_string);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatokenizerapplychattemplate) OgaTokenizerApplyChatTemplate

Applies a chat template to messages and tools.

``` highlight
const char* result = NULL;
OgaTokenizerApplyChatTemplate(tokenizer, "template", "messages", "tools", true, &result);
OgaDestroyString(result);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatokenizerdecodebatch) OgaTokenizerDecodeBatch

Decodes a batch of token sequences.

``` highlight
OgaStringArray* out_strings = NULL;
OgaTokenizerDecodeBatch(tokenizer, tensor, &out_strings);
// Use out_strings, then:
OgaDestroyStringArray(out_strings);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatetokenizerstream) OgaCreateTokenizerStream

Creates a tokenizer stream for incremental decoding.

``` highlight
OgaTokenizerStream* stream = NULL;
OgaCreateTokenizerStream(tokenizer, &stream);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroytokenizerstream) OgaDestroyTokenizerStream

Destroys the tokenizer stream.

``` highlight
OgaDestroyTokenizerStream(stream);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatokenizerstreamdecode) OgaTokenizerStreamDecode

Decodes a single token in the stream.

``` highlight
const char* chunk = NULL;
OgaTokenizerStreamDecode(stream, token, &chunk);
// chunk is valid until next call or stream is destroyed
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#sequences-api) Sequences API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatesequences) OgaCreateSequences

Creates an empty OgaSequences object.

``` highlight
OgaSequences* sequences = NULL;
OgaCreateSequences(&sequences);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroysequences) OgaDestroySequences

Destroys the given OgaSequences.

``` highlight
OgaDestroySequences(sequences);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogasequencescount) OgaSequencesCount

Returns the number of sequences.

``` highlight
size_t count = OgaSequencesCount(sequences);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogasequencesgetsequencecount) OgaSequencesGetSequenceCount

Returns the number of tokens in the sequence at the given index.

``` highlight
size_t token_count = OgaSequencesGetSequenceCount(sequences, 0);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogasequencesgetsequencedata) OgaSequencesGetSequenceData

Returns a pointer to the token data for the sequence at the given index.

``` highlight
const int32_t* data = OgaSequencesGetSequenceData(sequences, 0);
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generator-params-api) Generator Params API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreategeneratorparams) OgaCreateGeneratorParams

Creates generator parameters for the given model.

``` highlight
OgaGeneratorParams* params = NULL;
OgaCreateGeneratorParams(model, &params);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroygeneratorparams) OgaDestroyGeneratorParams

Destroys the given generator params.

``` highlight
OgaDestroyGeneratorParams(params);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamssetsearchnumber) OgaGeneratorParamsSetSearchNumber

Sets a numeric search option.

``` highlight
OgaGeneratorParamsSetSearchNumber(params, "max_length", 128);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamssetsearchbool) OgaGeneratorParamsSetSearchBool

Sets a boolean search option.

``` highlight
OgaGeneratorParamsSetSearchBool(params, "do_sample", true);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamstrygraphcapturewithmaxbatchsize) OgaGeneratorParamsTryGraphCaptureWithMaxBatchSize

Attempts to enable graph capture mode with a maximum batch size.

``` highlight
OgaGeneratorParamsTryGraphCaptureWithMaxBatchSize(params, 8);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamssetinputids) OgaGeneratorParamsSetInputIDs

Sets the input ids for the generator params.

``` highlight
OgaGeneratorParamsSetInputIDs(params, input_ids, input_ids_count, sequence_length, batch_size);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamssetinputsequences) OgaGeneratorParamsSetInputSequences

Sets the input id sequences for the generator params.

``` highlight
OgaGeneratorParamsSetInputSequences(params, sequences);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamssetmodelinput) OgaGeneratorParamsSetModelInput

Sets an additional model input.

``` highlight
OgaGeneratorParamsSetModelInput(params, "input_name", tensor);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamssetinputs) OgaGeneratorParamsSetInputs

Sets named tensors as inputs.

``` highlight
OgaGeneratorParamsSetInputs(params, named_tensors);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogageneratorparamssetguidance) OgaGeneratorParamsSetGuidance

Sets guidance data.

``` highlight
OgaGeneratorParamsSetGuidance(params, "type", "data");
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#generator-api) Generator API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreategenerator) OgaCreateGenerator

Creates a generator from the given model and generator params.

``` highlight
OgaGenerator* generator = NULL;
OgaCreateGenerator(model, params, &generator);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroygenerator) OgaDestroyGenerator

Destroys the given generator.

``` highlight
OgaDestroyGenerator(generator);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_isdone) OgaGenerator_IsDone

Checks if generation is complete.

``` highlight
bool done = OgaGenerator_IsDone(generator);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_appendtokensequences) OgaGenerator_AppendTokenSequences

Appends token sequences to the generator.

``` highlight
OgaGenerator_AppendTokenSequences(generator, sequences);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_appendtokens) OgaGenerator_AppendTokens

Appends tokens to the generator.

``` highlight
OgaGenerator_AppendTokens(generator, input_ids, input_ids_count);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_issessionterminated) OgaGenerator_IsSessionTerminated

Checks if the session is terminated.

``` highlight
bool terminated = OgaGenerator_IsSessionTerminated(generator);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_generatenexttoken) OgaGenerator_GenerateNextToken

Generates the next token.

``` highlight
OgaGenerator_GenerateNextToken(generator);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_rewindto) OgaGenerator_RewindTo

Rewinds the sequence to a new length.

``` highlight
OgaGenerator_RewindTo(generator, new_length);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_setruntimeoption) OgaGenerator_SetRuntimeOption

Sets a runtime option.

``` highlight
OgaGenerator_SetRuntimeOption(generator, "terminate_session", "1");
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_getsequencecount) OgaGenerator_GetSequenceCount

Returns the number of tokens in the sequence at the given index.

``` highlight
size_t count = OgaGenerator_GetSequenceCount(generator, 0);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_getsequencedata) OgaGenerator_GetSequenceData

Returns a pointer to the sequence data at the given index.

``` highlight
const int32_t* data = OgaGenerator_GetSequenceData(generator, 0);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_getoutput) OgaGenerator_GetOutput

Gets a named output tensor.

``` highlight
OgaTensor* tensor = NULL;
OgaGenerator_GetOutput(generator, "output_name", &tensor);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_getlogits) OgaGenerator_GetLogits

Gets the logits tensor.

``` highlight
OgaTensor* logits = NULL;
OgaGenerator_GetLogits(generator, &logits);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagenerator_setlogits) OgaGenerator_SetLogits

Sets the logits tensor.

``` highlight
OgaGenerator_SetLogits(generator, tensor);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogasetactiveadapter) OgaSetActiveAdapter

Sets the active adapter for the generator.

``` highlight
OgaSetActiveAdapter(generator, adapters, "adapter_name");
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#adapter-api) Adapter API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreateadapters) OgaCreateAdapters

Creates the object that manages the adapters.

``` highlight
OgaAdapters* adapters = NULL;
OgaCreateAdapters(model, &adapters);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaloadadapter) OgaLoadAdapter

Loads the model adapter from the given adapter file path and adapter name.

``` highlight
OgaLoadAdapter(adapters, "adapter_file_path", "adapter_name");
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaunloadadapter) OgaUnloadAdapter

Unloads the adapter with the given identifier.

``` highlight
OgaUnloadAdapter(adapters, "adapter_name");
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#tensor-api) Tensor API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatetensorfrombuffer) OgaCreateTensorFromBuffer

Creates a tensor from a buffer.

``` highlight
OgaTensor* tensor = NULL;
OgaCreateTensorFromBuffer(data, shape_dims, shape_dims_count, element_type, &tensor);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatensorgettype) OgaTensorGetType

Returns the element type of the tensor.

``` highlight
OgaElementType type;
OgaTensorGetType(tensor, &type);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatensorgetshaperank) OgaTensorGetShapeRank

Returns the rank (number of dimensions) of the tensor.

``` highlight
size_t rank;
OgaTensorGetShapeRank(tensor, &rank);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatensorgetshape) OgaTensorGetShape

Returns the shape of the tensor.

``` highlight
int64_t shape[rank];
OgaTensorGetShape(tensor, shape, rank);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogatensorgetdata) OgaTensorGetData

Returns a pointer to the tensor data.

``` highlight
void* data = NULL;
OgaTensorGetData(tensor, &data);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroytensor) OgaDestroyTensor

Destroys the tensor.

``` highlight
OgaDestroyTensor(tensor);
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#images-and-audios-api) Images and Audios API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaloadimages) OgaLoadImages

Loads images from file paths.

``` highlight
OgaStringArray* image_paths = NULL;
OgaCreateStringArrayFromStrings(paths, count, &image_paths);
OgaImages* images = NULL;
OgaLoadImages(image_paths, &images);
OgaDestroyStringArray(image_paths);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaloadimagesfrombuffers) OgaLoadImagesFromBuffers

Loads images from memory buffers.

``` highlight
OgaImages* images = NULL;
OgaLoadImagesFromBuffers(image_data, image_sizes, count, &images);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroyimages) OgaDestroyImages

Destroys the images object.

``` highlight
OgaDestroyImages(images);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaloadaudios) OgaLoadAudios

Loads audios from file paths.

``` highlight
OgaStringArray* audio_paths = NULL;
OgaCreateStringArrayFromStrings(paths, count, &audio_paths);
OgaAudios* audios = NULL;
OgaLoadAudios(audio_paths, &audios);
OgaDestroyStringArray(audio_paths);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaloadaudiosfrombuffers) OgaLoadAudiosFromBuffers

Loads audios from memory buffers.

``` highlight
OgaAudios* audios = NULL;
OgaLoadAudiosFromBuffers(audio_data, audio_sizes, count, &audios);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroyaudios) OgaDestroyAudios

Destroys the audios object.

``` highlight
OgaDestroyAudios(audios);
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#named-tensors-api) Named Tensors API

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogacreatenamedtensors) OgaCreateNamedTensors

Creates a named tensors object.

``` highlight
OgaNamedTensors* named_tensors = NULL;
OgaCreateNamedTensors(&named_tensors);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#oganamedtensorsget) OgaNamedTensorsGet

Gets a tensor by name.

``` highlight
OgaTensor* tensor = NULL;
OgaNamedTensorsGet(named_tensors, "input_name", &tensor);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#oganamedtensorsset) OgaNamedTensorsSet

Sets a tensor by name.

``` highlight
OgaNamedTensorsSet(named_tensors, "input_name", tensor);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#oganamedtensorsdelete) OgaNamedTensorsDelete

Deletes a tensor by name.

``` highlight
OgaNamedTensorsDelete(named_tensors, "input_name");
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#oganamedtensorscount) OgaNamedTensorsCount

Returns the number of named tensors.

``` highlight
size_t count = 0;
OgaNamedTensorsCount(named_tensors, &count);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#oganamedtensorsgetnames) OgaNamedTensorsGetNames

Gets the names of all tensors.

``` highlight
OgaStringArray* names = NULL;
OgaNamedTensorsGetNames(named_tensors, &names);
OgaDestroyStringArray(names);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroynamedtensors) OgaDestroyNamedTensors

Destroys the named tensors object.

``` highlight
OgaDestroyNamedTensors(named_tensors);
```

------------------------------------------------------------------------

## [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#utility-functions) Utility Functions

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogasetlogbool) OgaSetLogBool

Sets a boolean logging option.

``` highlight
OgaSetLogBool("option_name", true);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogasetlogstring) OgaSetLogString

Sets a string logging option.

``` highlight
OgaSetLogString("option_name", "value");
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogasetcurrentgpudeviceid) OgaSetCurrentGpuDeviceId

Sets the current GPU device ID.

``` highlight
OgaSetCurrentGpuDeviceId(0);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogagetcurrentgpudeviceid) OgaGetCurrentGpuDeviceId

Gets the current GPU device ID.

``` highlight
int device_id = 0;
OgaGetCurrentGpuDeviceId(&device_id);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogaresultgeterror) OgaResultGetError

Gets the error message from an OgaResult.

``` highlight
const char* error = OgaResultGetError(result);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroyresult) OgaDestroyResult

Destroys an OgaResult.

``` highlight
OgaDestroyResult(result);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroystring) OgaDestroyString

Destroys a string returned by the API.

``` highlight
OgaDestroyString(str);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogadestroybuffer) OgaDestroyBuffer

Destroys a buffer.

``` highlight
OgaDestroyBuffer(buffer);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogabuffergettype) OgaBufferGetType

Gets the type of the buffer.

``` highlight
OgaDataType type = OgaBufferGetType(buffer);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogabuffergetdimcount) OgaBufferGetDimCount

Gets the number of dimensions of a buffer.

``` highlight
size_t dim_count = OgaBufferGetDimCount(buffer);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogabuffergetdims) OgaBufferGetDims

Gets the dimensions of a buffer.

``` highlight
size_t dims[dim_count];
OgaBufferGetDims(buffer, dims, dim_count);
```

------------------------------------------------------------------------

### [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiIGFyaWEtaGlkZGVuPSJ0cnVlIj48dXNlIHhsaW5rOmhyZWY9IiNzdmctbGluayIgLz48L3N2Zz4=)](#ogabuffergetdata) OgaBufferGetData

Gets the data from a buffer.

``` highlight
const void* data = OgaBufferGetData(buffer);
```

------------------------------------------------------------------------