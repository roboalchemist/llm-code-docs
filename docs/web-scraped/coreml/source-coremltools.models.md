# Source: https://apple.github.io/coremltools/source/coremltools.models.html

# Model APIs[](#model-apis "Link to this heading")

[]

## MLModel[](#module-coremltools.models.model "Link to this heading")

*[class][ ]*[[coremltools.models.model.]][[MLModel]][(]*[[model]]*, *[[is_temp_package]][[=]][[False]]*, *[[mil_program]][[=]][[None]]*, *[[skip_model_load]][[=]][[False]]*, *[[compute_units]][[=]][[ComputeUnit.ALL]]*, *[[weights_dir]][[=]][[None]]*, *[[function_name]][[=]][[None]]*, *[[optimization_hints]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel)[](#coremltools.models.model.MLModel "Link to this definition")

:   This class defines the minimal interface to a Core ML object in Python.

    At a high level, the protobuf specification consists of:

    - Model description: Encodes names and type information of the inputs and outputs to the model.

    - Model parameters: The set of parameters required to represent a specific instance of the model.

    - Metadata: Information about the origin, license, and author of the model.

    With this class, you can inspect a Core ML model, modify metadata, and make predictions for the purposes of testing (on select platforms).

    ::: 
    See also

    [[`predict`]](#coremltools.models.model.MLModel.predict "coremltools.models.model.MLModel.predict")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        # Load the model
        model = MLModel("HousePricer.mlmodel")

        # Set the model metadata
        model.author = "Author"
        model.license = "BSD"
        model.short_description = "Predicts the price of a house in the Seattle area."

        # Get the interface to the model
        model.input_description
        model.output_description

        # Set feature descriptions manually
        model.input_description["bedroom"] = "Number of bedrooms"
        model.input_description["bathrooms"] = "Number of bathrooms"
        model.input_description["size"] = "Size (in square feet)"

        # Set
        model.output_description["price"] = "Price of the house"

        # Make predictions
        predictions = model.predict()

        # Get the spec of the model
        spec = model.get_spec()

        # Save the model
        model.save("HousePricer.mlpackage")

        # Load the model from the spec object
        spec = model.get_spec()
        # modify spec (e.g. rename inputs/outputs etc)
        model = MLModel(spec)
        # if model type is mlprogram, i.e. spec.WhichOneof('Type') == "mlProgram", then:
        model = MLModel(spec, weights_dir=model.weights_dir)

        # Load a non-default function from a multifunction .mlpackage
        model = MLModel("MultifunctionModel.mlpackage", function_name="deep_features")
    :::
    ::::

    [[\_\_init\_\_]][(]*[[model]]*, *[[is_temp_package]][[=]][[False]]*, *[[mil_program]][[=]][[None]]*, *[[skip_model_load]][[=]][[False]]*, *[[compute_units]][[=]][[ComputeUnit.ALL]]*, *[[weights_dir]][[=]][[None]]*, *[[function_name]][[=]][[None]]*, *[[optimization_hints]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[None]]][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel.__init__)[](#coremltools.models.model.MLModel.__init__ "Link to this definition")

    :   Construct an MLModel from an [`.mlmodel`].

        Parameters[:]

        :   

            **model: str or Model_pb2**

            :   For an ML program ([`mlprogram`]), the model can be a path string ([`.mlpackage`]) or [`Model_pb2`]. If it is a path string, it must point to a directory containing bundle artifacts (such as [`weights.bin`]). If it is of type [`Model_pb2`] (spec), then you must also provide [`weights_dir`] if the model has weights, because both the proto spec and the weights are required to initialize and load the model. The proto spec for an [`mlprogram`], unlike a neural network ([`neuralnetwork`]), does not contain the weights; they are stored separately. If the model does not have weights, you can provide an empty [`weights_dir`].

                For non- [`mlprogram`] model types, the model can be a path string ([`.mlmodel`]) or type [`Model_pb2`], such as a spec object.

            **is_temp_package: bool**

            :   Set to [`True`] if the input model package dir is temporary and can be deleted upon interpreter termination.

            **mil_program: coremltools.converters.mil.Program**

            :   Set to the MIL program object, if available. It is available whenever an MLModel object is constructed using the unified converter API [coremltools.convert()](https://apple.github.io/coremltools/source/coremltools.converters.convert.html).

            **skip_model_load: bool**

            :   Set to [`True`] to prevent Core ML Tools from calling into the Core ML framework to compile and load the model. In that case, the returned model object cannot be used to make a prediction. This flag may be used to load a newer model type on an older Mac, to inspect or load/save the spec.

                Example: Loading an ML program model type on a macOS 11, since an ML program can be compiled and loaded only from macOS12+.

                Defaults to [`False`].

            **compute_units: coremltools.ComputeUnit**

            :   The set of processing units the model can use to make predictions.

                An enum with four possible values:

                :   - [`coremltools.ComputeUnit.ALL`]: Use all compute units available, including the neural engine.

                    - [`coremltools.ComputeUnit.CPU_ONLY`]: Limit the model to only use the CPU.

                    - [`coremltools.ComputeUnit.CPU_AND_GPU`]: Use both the CPU and GPU, but not the neural engine.

                    - [`coremltools.ComputeUnit.CPU_AND_NE`]: Use both the CPU and neural engine, but not the GPU. Available only for macOS \>= 13.0.

            **weights_dir: str**

            :   Path to the weight directory, required when loading an MLModel of type [`mlprogram`], from a spec object, such as when the argument [`model`] is of type [`Model_pb2`].

            **function_name**[str]

            :   The name of the function from [`model`] to load. If not provided, [`function_name`] will be set to the [`defaultFunctionName`] in the proto.

            **optimization_hints**[dict or None]

            :   

                Keys are the names of the optimization hint: 'allowLowPrecisionAccumulationOnGPU', 'reshapeFrequency'

                :   or 'specializationStrategy'.

                - 'allowLowPrecisionAccumulationOnGPU' value must have [`bool`] type.

                - 'reshapeFrequency' value must have [`coremltools.ReshapeFrequency`] type.

                - 'specializationStrategy' must have\`\`coremltools.SpecializationStrategy\`\` type.

        Notes

        Internally this maintains the following:

        - [`_MLModelProxy`]: A pybind wrapper around CoreML::Python::Model (see [coremltools/coremlpython/CoreMLPython.mm](https://github.com/apple/coremltools/blob/main/coremlpython/CoreMLPython.mm))

        - [`package_path`] (mlprogram only): Directory containing all artifacts ([`.mlmodel`], weights, and so on).

        - [`weights_dir`] (mlprogram only): Directory containing weights inside the package_path.

        Examples

        :::: 
        ::: highlight
            loaded_model = MLModel("my_model.mlmodel")
            loaded_model = MLModel("my_model.mlpackage")
        :::
        ::::

    *[classmethod][ ]*[[get_available_compute_devices]][(][)] [[→] [[List][[\[]][[MLComputeDevice]](#coremltools.models.compute_device.MLComputeDevice "coremltools.models.compute_device.MLComputeDevice")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel.get_available_compute_devices)[](#coremltools.models.model.MLModel.get_available_compute_devices "Link to this definition")

    :   The list of available compute devices for CoreML.

        Use the method to get the list of compute devices that MLModel's predict method can use.

        Some compute devices on the hardware are exclusive to the domain ML frameworks such as Vision and SoundAnalysis and not available to Core ML framework. See also [`MLComputeDevice.get_all_compute_devices()`].

        Returns[:]

        :   

            The list of compute devices MLModel's predict method can use.

            :   

        Examples

        :::: 
        ::: highlight
            compute_devices = coremltools.MLModel.get_available_compute_devices()
        :::
        ::::

    [[get_compiled_model_path]][(][)][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel.get_compiled_model_path)[](#coremltools.models.model.MLModel.get_compiled_model_path "Link to this definition")

    :   Returns the path for the underlying compiled ML Model.

        **Important**: This path is available only for the lifetime of this Python object. If you want the compiled model to persist, you need to make a copy.

    [[get_spec]][(][)][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel.get_spec)[](#coremltools.models.model.MLModel.get_spec "Link to this definition")

    :   Get a deep copy of the protobuf specification of the model.

        Returns[:]

        :   

            model: Model_pb2

            :   Protobuf specification of the model.

        Examples

        :::: 
        ::: highlight
            spec = model.get_spec()
        :::
        ::::

    *[property][ ]*[[last_predict_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.model.MLModel.last_predict_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the last predict operation in nanoseconds. This method returns the time taken for the most recent prediction made by the model, measured in nanoseconds.

        Returns[:]

        :   

            Optional\[int\]:

            :   The duration of the last prediction operation in nanoseconds. Returns None if no prediction has been made yet.

        Notes

        Calculates the time elapsed during the model predict call, specifically measuring the execution time of [`[MLModel`]` `[`predictionFromFeatures:error:]`] or [`[MLModel`]` `[`predictionFromBatch:error:]`] method of the Core ML framework.

    *[property][ ]*[[load_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.model.MLModel.load_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the model loading process in nanoseconds.

        Returns[:]

        :   

            Optional\[int\]:

            :   The duration of the model loading process in nanoseconds. Returns None if duration is not available.

        Notes

        Calculates the time elapsed during the model loading process, specifically measuring the execution time of [`[MLModel`]` `[`loadContentsOfURL:configuration:error:]`] method of the Core ML framework.

    [[make_state]][(][)] [[→] [[MLState]]][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel.make_state)[](#coremltools.models.model.MLModel.make_state "Link to this definition")

    :   Returns a new state object, which can be passed to the [`predict`] method.

        Returns[:]

        :   - **state** (*MLState*) -- Holds state for an MLModel.

            - *State functionality is only supported on macOS 15+.*

        ::: 
        See also

        [[`predict`]](#coremltools.models.model.MLModel.predict "coremltools.models.model.MLModel.predict")

        :   
        :::

        Examples

        :::: 
        ::: highlight
            state = model.make_state()
            predictions = model.predict(x, state)
        :::
        ::::

    [[predict]][(]*[[data]]*, *[[state]][[:]][ ][[MLState][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel.predict)[](#coremltools.models.model.MLModel.predict "Link to this definition")

    :   Return predictions for the model.

        Parameters[:]

        :   

            **data: dict\[str, value\] or list\[dict\[str, value\]\]**

            :   Dictionary of data to use for predictions, where the keys are the names of the input features. For batch predictons, use a list of such dictionaries.

                The following dictionary values types are acceptable: list, array, numpy.ndarray, tensorflow.Tensor and torch.Tensor.

            **state**[MLState]

            :   Optional state object as returned by [`make_state()`].

        Returns[:]

        :   

            dict\[str, value\]

            :   Predictions as a dictionary where each key is the output feature name.

            list\[dict\[str, value\]\]

            :   For batch prediction, returns a list of the above dictionaries.

        Examples

        :::: 
        ::: highlight
            data = 
            predictions = model.predict(data)

            data = [
                ,
                ,
            ]
            batch_predictions = model.predict(data)
        :::
        ::::

    [[save]][(]*[[save_path]][[:]][ ][[str]]*[)][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModel.save)[](#coremltools.models.model.MLModel.save "Link to this definition")

    :   Save the model to an [`.mlmodel`] format. For an MIL program, the [`save_path`] is a package directory containing the [`mlmodel`] and weights.

        Parameters[:]

        :   

            **save_path: Target file path / bundle directory for the model.**

            :   

        Examples

        :::: 
        ::: highlight
            model.save("my_model_file.mlmodel")
            loaded_model = MLModel("my_model_file.mlmodel")
        :::
        ::::

<!-- -->

*[class][ ]*[[coremltools.models.model.]][[MLModelAsset]][(]*[[proxy]]*[)][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModelAsset)[](#coremltools.models.model.MLModelAsset "Link to this definition")

:   A class representing a compiled model asset.

    It supports two initialization methods: - From a compiled model directory: The directory should have a '.mlmodelc' extension. - From memory: Allows direct initialization using in-memory model data.

    *[classmethod][ ]*[[from_memory]][(]*[[spec_data]][[:]][ ][[bytes]]*, *[[blob_mapping]][[:]][ ][[Dict][[\[]][str][[,]][ ][bytes][[\]]]][ ][[=]][ ][[]]*[)] [[→] [[[MLModelAsset]](#coremltools.models.model.MLModelAsset "coremltools.models.model.MLModelAsset")]][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModelAsset.from_memory)[](#coremltools.models.model.MLModelAsset.from_memory "Link to this definition")

    :   Create an MLModelAsset instance from in-memory data.

        Parameters[:]

        :   

            **spec_data**[bytes]

            :   The specification data of the model.

            **blob_mapping**[Dict\[str, bytes\])]

            :   A dictionary with blob path as the key and blob data as the value.

        Returns[:]

        :   

            MLModelAsset

            :   An instance of MLModelAsset created from the provided memory data.

    *[classmethod][ ]*[[from_path]][(]*[[compiled_model_path]][[:]][ ][[str]]*[)] [[→] [[[MLModelAsset]](#coremltools.models.model.MLModelAsset "coremltools.models.model.MLModelAsset")]][[[\[source\]]]](../_modules/coremltools/models/model.html#MLModelAsset.from_path)[](#coremltools.models.model.MLModelAsset.from_path "Link to this definition")

    :   Create an MLModelAsset instance from a compiled model path.

        Parameters[:]

        :   

            **compiled_model_path**[str]

            :   The file path to the compiled model.

        Returns[:]

        :   

            MLModelAsset

            :   An instance of MLModelAsset created from the specified path.

## Compiled MLModel[](#compiled-mlmodel "Link to this heading")

*[class][ ]*[[coremltools.models.]][[CompiledMLModel]][(]*[[path]][[:]][ ][[str]]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[asset]][[:]][ ][[[MLModelAsset]](#coremltools.models.model.MLModelAsset "coremltools.models.model.MLModelAsset")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/_compiled_model.html#CompiledMLModel)[](#coremltools.models.CompiledMLModel "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[path]][[:]][ ][[str]]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[asset]][[:]][ ][[[MLModelAsset]](#coremltools.models.model.MLModelAsset "coremltools.models.model.MLModelAsset")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/_compiled_model.html#CompiledMLModel.__init__)[](#coremltools.models.CompiledMLModel.__init__ "Link to this definition")

    :   Loads a compiled Core ML model.

        Parameters[:]

        :   

            **path**[str]

            :   The path to a compiled model directory, ending in [`.mlmodelc`].

            **compute_units**[coremltools.ComputeUnit]

            :   

                An enum with the following possible values:

                :   - [`coremltools.ComputeUnit.ALL`]: Use all compute units available, including the neural engine.

                    - [`coremltools.ComputeUnit.CPU_ONLY`]: Limit the model to only use the CPU.

                    - [`coremltools.ComputeUnit.CPU_AND_GPU`]: Use both the CPU and GPU, but not the neural engine.

                    - [`coremltools.ComputeUnit.CPU_AND_NE`]: Use both the CPU and neural engine, but not the GPU. Available only for macOS \>= 13.0.

            **optimization_hints**[dict or None]

            :   

                Keys are the names of the optimization hint: 'allowLowPrecisionAccumulationOnGPU', 'reshapeFrequency'

                :   or 'specializationStrategy'.

                - 'allowLowPrecisionAccumulationOnGPU' value must have [`bool`] type.

                - 'reshapeFrequency' value must have [`coremltools.ReshapeFrequency`] type.

                - 'specializationStrategy' must have\`\`coremltools.SpecializationStrategy\`\` type.

            **asset**[MLModelAsset or None]

            :   The model asset.

        ::: 
        See also

        [[`predict`]](#coremltools.models.CompiledMLModel.predict "coremltools.models.CompiledMLModel.predict")

        :   
        :::

        Examples

        :::: 
        ::: highlight
            my_compiled_model = ct.models.CompiledMLModel("my_model_path.mlmodelc")
            y = my_compiled_model.predict()
        :::
        ::::

    *[classmethod][ ]*[[from_asset]][(]*[[asset]][[:]][ ][[[MLModelAsset]](#coremltools.models.model.MLModelAsset "coremltools.models.model.MLModelAsset")]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[dict][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[Type][[\[]][[CompiledMLModel]](#coremltools.models.CompiledMLModel "coremltools.models._compiled_model.CompiledMLModel")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/_compiled_model.html#CompiledMLModel.from_asset)[](#coremltools.models.CompiledMLModel.from_asset "Link to this definition")

    :   Creates a CompiledModel instance from an asset.

        Parameters[:]

        :   

            **asset: MLModelAsset**

            :   The model asset to create the compiled model from.

            **compute_units**[coremltools.ComputeUnit]

            :   

                An enum with the following possible values:

                :   - [`coremltools.ComputeUnit.ALL`]: Use all compute units available, including the neural engine.

                    - [`coremltools.ComputeUnit.CPU_ONLY`]: Limit the model to only use the CPU.

                    - [`coremltools.ComputeUnit.CPU_AND_GPU`]: Use both the CPU and GPU, but not the neural engine.

                    - [`coremltools.ComputeUnit.CPU_AND_NE`]: Use both the CPU and neural engine, but not the GPU. Available only for macOS \>= 13.0.

            **optimization_hints**[dict or None]

            :   Keys are the names of the optimization hint, either 'reshapeFrequency' or 'specializationStrategy'. Values are enumeration values of type [`coremltools.ReshapeFrequency`] or [`coremltools.SpecializationStrategy`].

        Returns[:]

        :   

            CompiledMLModel

            :   An instance of [`CompiledMLModel`] loaded from the provided asset.

        Examples

        :::: 
        ::: highlight
            my_model_asset = MLModelAsset.from_memory(spec_data)
            my_compiled_model = CompiledMLModel.from_asset(my_model_asset)
            y = my_compiled_model.predict()
        :::
        ::::

    [[make_state]][(][)] [[→] [[MLState]]][[[\[source\]]]](../_modules/coremltools/models/_compiled_model.html#CompiledMLModel.make_state)[](#coremltools.models.CompiledMLModel.make_state "Link to this definition")

    :   Returns a new state object, which can be passed to the [`predict`] method.

        ::: 
        See also

        [[`predict`]](#coremltools.models.CompiledMLModel.predict "coremltools.models.CompiledMLModel.predict")

        :   
        :::

        Examples

        :::: 
        ::: highlight
            state = model.make_state()
            predictions = model.predict(x, state)
        :::
        ::::

    [[predict]][(]*[[data]]*, *[[state]][[:]][ ][[MLState][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/_compiled_model.html#CompiledMLModel.predict)[](#coremltools.models.CompiledMLModel.predict "Link to this definition")

    :   Return predictions for the model.

        Parameters[:]

        :   

            **data: dict\[str, value\] or list\[dict\[str, value\]\]**

            :   Dictionary of data to use for predictions, where the keys are the names of the input features. For batch predictons, use a list of such dictionaries.

            **state**[MLState]

            :   Optional state object as returned by [`make_state()`].

        Returns[:]

        :   

            dict\[str, value\]

            :   Predictions as a dictionary where each key is the output feature name.

            list\[dict\[str, value\]\]

            :   For batch prediction, returns a list of the above dictionaries.

        Examples

        :::: 
        ::: highlight
            data = 
            predictions = model.predict(data)

            data = [
                ,
                ,
            ]
            batch_predictions = model.predict(data)
        :::
        ::::

## compression_utils[](#compression-utils "Link to this heading")

- [[`affine_quantize_weights()`]](coremltools.models.ml_program.html)
- [[`palettize_weights()`]](coremltools.models.ml_program.html#coremltools.models.ml_program.compression_utils.palettize_weights)
- [[`sparsify_weights()`]](coremltools.models.ml_program.html#coremltools.models.ml_program.compression_utils.sparsify_weights)

[]

## array_feature_extractor[](#module-coremltools.models.array_feature_extractor "Link to this heading")

[[coremltools.models.array_feature_extractor.]][[create_array_feature_extractor]][(]*[[input_features]]*, *[[output_name]]*, *[[extract_indices]]*, *[[output_type]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/array_feature_extractor.html#create_array_feature_extractor)[](#coremltools.models.array_feature_extractor.create_array_feature_extractor "Link to this definition")

:   Creates a feature extractor from an input array [`(feature,`]` `[`return)`].

    Parameters[:]

    :   

        **input_features:**

        :   A list of one [`(name,`]` `[`array)`] tuple.

        **extract_indices:**

        :   Either an integer or a list. If it's an integer, the output type is by default a double (but may also be an integer). If a list, the output type is an array.

[]

## extract_submodel[](#module-coremltools.converters.mil.debugging_utils "Link to this heading")

[[coremltools.converters.mil.debugging_utils.]][[extract_submodel]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[outputs]][[:]][ ][[List][[\[]][str][[\]]]]*, *[[inputs]][[:]][ ][[List][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[function_name]][[:]][ ][[str]][ ][[=]][ ][[\'main\']]*[)] [[→] [[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]][[[\[source\]]]](../_modules/coremltools/converters/mil/debugging_utils.html#extract_submodel)[](#coremltools.converters.mil.debugging_utils.extract_submodel "Link to this definition")

:   This utility function lets you extract a submodel from a Core ML model.

    For a neural network model, the function extracts only in-memory Core ML models. You should always call this function for a model directly from [[`convert`]](coremltools.converters.convert.html#coremltools.converters._converters_entry.convert "coremltools.converters._converters_entry.convert"). It is not allowed to load the model from disk and then call this API.

    For an ML program model, both cases (in-memory and from disk) are supported.

    Parameters[:]

    :   

        **model: MLModel**

        :   The Core ML model from which the submodel is extracted.

        **outputs: list\[str\]**

        :   A list of names of Vars, which are the outputs of the extracted submodel.

        **inputs: list\[str\] (Optional)**

        :   A list of names of Vars, which are the inputs of the extracted submodel. If not provided, the inputs from the original model are used.

        **function_name: str (Optional)**

        :   Name of the function where the subgraph is extracted. Default is [`main`].

    Examples

    Neural network:

    :::: 
    ::: highlight
        >>> from coremltools.converters.mil.debugging_utils import extract_submodel
        >>> mlmodel = ct.convert(model, convert_to="neuralnetwork")
        >>> outputs = ["output_0", "output_1"]
        >>> submodel = extract_submodel(mlmodel, outputs)
    :::
    ::::

    ML program:

    :::: 
    ::: highlight
        >>> from coremltools.converters.mil.debugging_utils import extract_submodel
        >>> mlmodel = ct.convert(model, convert_to="mlprogram")
        >>> outputs = ["output_0", "output_1"]
        >>>
        >>> # Directly extract model in memory
        >>> submodel = extract_submodel(mlmodel, outputs)
        >>>
        >>> # Extract model loaded from disk
        >>> mlmodel.save("model.mlpackage")
        >>> mlmodel = coremltools.model.models.MLModel("model.mlpackage")
        >>> submodel = extract_submodel(mlmodel, outputs)
    :::
    ::::

[]

## feature_vectorizer[](#module-coremltools.models.feature_vectorizer "Link to this heading")

[[coremltools.models.feature_vectorizer.]][[create_feature_vectorizer]][(]*[[input_features]]*, *[[output_feature_name]]*, *[[known_size_map]][[=]][[]]*[)][[[\[source\]]]](../_modules/coremltools/models/feature_vectorizer.html#create_feature_vectorizer)[](#coremltools.models.feature_vectorizer.create_feature_vectorizer "Link to this definition")

:   Create a feature vectorizer from input features. This returns a 2-tuple [`(spec,`]` `[`num_dimension)`] for a feature vectorizer that puts everything into a single array with a length equal to the total size of all the input features.

    Parameters[:]

    :   

        **input_features: \[list of 2-tuples\]**

        :   Name(s) of the input features, given as a list of [`('name',`]` `[`datatype)`] tuples. The datatypes entry is one of the data types defined in the [`datatypes`] module. Allowed [`datatypes`] are [`datatype.Int64`], [`datatype.Double`], [`datatypes.Dictionary`], and [`datatype.Array`].

            If the feature is a dictionary type, then the dictionary must have integer keys, and the number of dimensions to expand it into must be provided by [`known_size_map`].

            Feature indices in the final array are counted sequentially from the from 0 through the total number of features.

        **output_feature_name: str**

        :   The name of the output feature. The type is an Array List of the output features of the network.

        **known_size_map:**

        :   A dictionary mapping the feature name to the expanded size in the final array. This is most useful for specifying the size of sparse vectors given as dictionaries of index to value.

[]

## nearest_neighbors[](#module-coremltools.models.nearest_neighbors.builder "Link to this heading")

*[class][ ]*[[coremltools.models.nearest_neighbors.builder.]][[KNearestNeighborsClassifierBuilder]][(]*[[input_name]]*, *[[output_name]]*, *[[number_of_dimensions]]*, *[[default_class_label]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/models/nearest_neighbors/builder.html#KNearestNeighborsClassifierBuilder)[](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder "Link to this definition")

:   Construct a CoreML KNearestNeighborsClassifier specification.

    Please see the Core ML Nearest Neighbors protobuf message for more information on KNearestNeighborsClassifier parameters.

    Examples

    :::: 
    ::: highlight
        from coremltools.models.nearest_neighbors import KNearestNeighborsClassifierBuilder
        from coremltools.models.utils import save_spec

        # Create a KNearestNeighborsClassifier model that takes 4-dimensional input data and outputs a string label.
        >>> builder = KNearestNeighborsClassifierBuilder(input_name='input',
        ...                                              output_name='output',
        ...                                              number_of_dimensions=4,
        ...                                              default_class_label='default_label')

        # save the spec by the builder
        >>> save_spec(builder.spec, 'knnclassifier.mlmodel')
    :::
    ::::

    [[\_\_init\_\_]][(]*[[input_name]]*, *[[output_name]]*, *[[number_of_dimensions]]*, *[[default_class_label]]*, *[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/models/nearest_neighbors/builder.html#KNearestNeighborsClassifierBuilder.__init__)[](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.__init__ "Link to this definition")

    :   Create a KNearestNeighborsClassifierBuilder object.

        Parameters[:]

        :   

            **input_name**

            :   Name of the model input.

            **output_name**

            :   Name of the output.

            **number_of_dimensions**

            :   Number of dimensions of the input data.

            **default_class_label**

            :   The default class label to use for predictions. Must be either an int64 or a string.

            **number_of_neighbors**

            :   Number of neighbors to use for predictions. Default = 5 with allowed values between 1-1000.

            **weighting_scheme**

            :   Weight function used in prediction. One of [`'uniform'`] (default) or [`'inverse_distance'`].

            **index_type**

            :   Algorithm to compute nearest neighbors. One of [`'linear'`] (default), or [`'kd_tree'`].

            **leaf_size**

            :   Leaf size for the kd-tree. Ignored if index type is [`'linear'`]. Default = 30.

    [[add_samples]][(]*[[data_points]]*, *[[labels]]*[)][[[\[source\]]]](../_modules/coremltools/models/nearest_neighbors/builder.html#KNearestNeighborsClassifierBuilder.add_samples)[](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.add_samples "Link to this definition")

    :   Add some samples to the KNearestNeighborsClassifier model.

        Parameters[:]

        :   

            **data_points**

            :   List of input data points.

            **labels**

            :   List of corresponding labels.

        Returns[:]

        :   

            None

            :   

    *[property][ ]*[[author]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.author "Link to this definition")

    :   Get the author for the KNearestNeighborsClassifier model.

        Returns[:]

        :   

            The author

            :   

    *[property][ ]*[[description]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.description "Link to this definition")

    :   Get the description for the KNearestNeighborsClassifier model.

        Returns[:]

        :   

            The description.

            :   

    *[property][ ]*[[index_type]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.index_type "Link to this definition")

    :   Get the index type for the KNearestNeighborsClassifier model.

        Returns[:]

        :   

            The index type.

            :   

    *[property][ ]*[[is_updatable]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.is_updatable "Link to this definition")

    :   Check if the KNearestNeighborsClassifier is updatable.

        Returns[:]

        :   

            Is updatable.

            :   

    *[property][ ]*[[leaf_size]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.leaf_size "Link to this definition")

    :   Get the leaf size for the KNearestNeighborsClassifier.

        Returns[:]

        :   

            The leaf size.

            :   

    *[property][ ]*[[license]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.license "Link to this definition")

    :   Get the license for the KNearestNeighborsClassifier model.

        Returns[:]

        :   

            The license.

            :   

    *[property][ ]*[[number_of_dimensions]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.number_of_dimensions "Link to this definition")

    :   Get the number of dimensions of the input data for the KNearestNeighborsClassifier model.

        Returns[:]

        :   

            Number of dimensions.

            :   

    *[property][ ]*[[number_of_neighbors]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.number_of_neighbors "Link to this definition")

    :   Get the number of neighbors value for the KNearestNeighborsClassifier model.

        Returns[:]

        :   

            The number of neighbors default value.

            :   

    [[number_of_neighbors_allowed_range]][(][)][[[\[source\]]]](../_modules/coremltools/models/nearest_neighbors/builder.html#KNearestNeighborsClassifierBuilder.number_of_neighbors_allowed_range)[](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.number_of_neighbors_allowed_range "Link to this definition")

    :   Get the range of allowed values for the numberOfNeighbors parameter.

        Returns[:]

        :   

            Tuple of ([`min_value`], [`max_value`]) or [`None`] if the range hasn't been set.

            :   

    [[number_of_neighbors_allowed_set]][(][)][[[\[source\]]]](../_modules/coremltools/models/nearest_neighbors/builder.html#KNearestNeighborsClassifierBuilder.number_of_neighbors_allowed_set)[](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.number_of_neighbors_allowed_set "Link to this definition")

    :   Get the set of allowed values for the numberOfNeighbors parameter.

        Returns[:]

        :   

            Set of allowed values or [`None`] if the set of allowed values hasn't been

            :   

            populated.

            :   

    [[set_index_type]][(]*[[index_type]]*, *[[leaf_size]][[=]][[30]]*[)][[[\[source\]]]](../_modules/coremltools/models/nearest_neighbors/builder.html#KNearestNeighborsClassifierBuilder.set_index_type)[](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.set_index_type "Link to this definition")

    :   Set the index type for the KNearestNeighborsClassifier model.

        Parameters[:]

        :   

            **index_type**

            :   One of \[ [`'linear'`], [`'kd_tree'`] \].

            **leaf_size**

            :   For kd_tree indexes, the leaf size to use (default = 30).

        Returns[:]

        :   

            None

            :   

    [[set_number_of_neighbors_with_bounds]][(]*[[number_of_neighbors]]*, *[[allowed_range]][[=]][[None]]*, *[[allowed_set]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/nearest_neighbors/builder.html#KNearestNeighborsClassifierBuilder.set_number_of_neighbors_with_bounds)[](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.set_number_of_neighbors_with_bounds "Link to this definition")

    :   Set the numberOfNeighbors parameter for the KNearestNeighborsClassifier model.

        Parameters[:]

        :   

            **allowed_range**

            :   Tuple of ([`min_value`], [`max_value`]) defining the range of allowed values.

            **allowed_values**

            :   Set of allowed values for the number of neighbors.

        Returns[:]

        :   

            None

            :   

    *[property][ ]*[[weighting_scheme]][](#coremltools.models.nearest_neighbors.builder.KNearestNeighborsClassifierBuilder.weighting_scheme "Link to this definition")

    :   Get the weighting scheme for the KNearestNeighborsClassifier model.

        Returns[:]

        :   

            The weighting scheme.

            :   

## neural_network[](#neural-network "Link to this heading")

- [neural_network.builder](coremltools.models.neural_network.html)
- [neural_network.flexible_shape_utils](coremltools.models.neural_network.html#module-coremltools.models.neural_network.flexible_shape_utils)
- [neural_network.quantization_utils](coremltools.models.neural_network.html#module-coremltools.models.neural_network.quantization_utils)
- [neural_network.update_optimizer_utils](coremltools.models.neural_network.html#module-coremltools.models.neural_network.update_optimizer_utils)

[]

## pipeline[](#module-coremltools.models.pipeline "Link to this heading")

Pipeline utils for this package.

*[class][ ]*[[coremltools.models.pipeline.]][[Pipeline]][(]*[[input_features]]*, *[[output_features]]*, *[[training_features]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#Pipeline)[](#coremltools.models.pipeline.Pipeline "Link to this definition")

:   A pipeline model that exposes a sequence of models as a single model, It requires a set of inputs, a sequence of other models and a set of outputs.

    This class is the base class for [[`PipelineClassifier`]](#coremltools.models.pipeline.PipelineClassifier "coremltools.models.pipeline.PipelineClassifier") and [[`PipelineRegressor`]](#coremltools.models.pipeline.PipelineRegressor "coremltools.models.pipeline.PipelineRegressor"), which contain a sequence ending in a classifier or regressor and themselves behave like a classifier or regressor. This class may be used directly for a sequence of feature transformer objects.

    [[\_\_init\_\_]][(]*[[input_features]]*, *[[output_features]]*, *[[training_features]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#Pipeline.__init__)[](#coremltools.models.pipeline.Pipeline.__init__ "Link to this definition")

    :   Create a pipeline of models to be executed sequentially.

        Parameters[:]

        :   

            **input_features: \[list of 2-tuples\]**

            :   Name(s) of the input features, given as a list of ('name', datatype) tuples. The datatypes entry can be any of the data types defined in the [`models.datatypes`] module.

            **output_features: \[list of features\]**

            :   Name(s) of the output features, given as a list of ('name',datatype) tuples. The datatypes entry can be any of the data types defined in the [`models.datatypes`] module. All features must be either defined in the inputs or be produced by one of the contained models.

    [[add_model]][(]*[[spec]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#Pipeline.add_model)[](#coremltools.models.pipeline.Pipeline.add_model "Link to this definition")

    :   Add a protobuf spec or [`models.MLModel`] instance to the pipeline.

        All input features of this model must either match the input_features of the pipeline, or match the outputs of a previous model.

        Parameters[:]

        :   

            **spec: \[MLModel, Model_pb2\]**

            :   A protobuf spec or MLModel instance containing a model.

    [[set_training_input]][(]*[[training_input]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#Pipeline.set_training_input)[](#coremltools.models.pipeline.Pipeline.set_training_input "Link to this definition")

    :   Set the training inputs of the network spec.

        Parameters[:]

        :   

            **training_input: \[tuple\]**

            :   List of training input names and type of the network.

<!-- -->

*[class][ ]*[[coremltools.models.pipeline.]][[PipelineClassifier]][(]*[[input_features]]*, *[[class_labels]]*, *[[output_features]][[=]][[None]]*, *[[training_features]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineClassifier)[](#coremltools.models.pipeline.PipelineClassifier "Link to this definition")

:   A pipeline model that exposes a sequence of models as a single model, It requires a set of inputs, a sequence of other models and a set of outputs. In this case the pipeline itself behaves as a classification model by designating a discrete categorical output feature as its 'predicted feature'.

    [[\_\_init\_\_]][(]*[[input_features]]*, *[[class_labels]]*, *[[output_features]][[=]][[None]]*, *[[training_features]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineClassifier.__init__)[](#coremltools.models.pipeline.PipelineClassifier.__init__ "Link to this definition")

    :   Create a set of pipeline models given a set of model specs. The last model in this list must be a classifier model.

        Parameters[:]

        :   

            **input_features: \[list of 2-tuples\]**

            :   Name(s) of the input features, given as a list of ('name', datatype) tuples. The datatypes entry can be any of the data types defined in the [`models.datatypes`] module.

            **class_labels: \[list\]**

            :   A list of string or integer class labels to use in making predictions. This list must match the class labels in the model outputting the categorical predictedFeatureName

            **output_features: \[list\]**

            :   A string or a list of two strings specifying the names of the two output features, the first being a class label corresponding to the class with the highest predicted score, and the second being a dictionary mapping each class to its score. If output_features is a string, it specifies the predicted class label and the class scores is set to the default value of "classProbability."

    [[add_model]][(]*[[spec]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineClassifier.add_model)[](#coremltools.models.pipeline.PipelineClassifier.add_model "Link to this definition")

    :   Add a protobuf spec or [`models.MLModel`] instance to the pipeline.

        All input features of this model must either match the input_features of the pipeline, or match the outputs of a previous model.

        Parameters[:]

        :   

            **spec: \[MLModel, Model_pb2\]**

            :   A protobuf spec or MLModel instance containing a model.

    [[set_training_input]][(]*[[training_input]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineClassifier.set_training_input)[](#coremltools.models.pipeline.PipelineClassifier.set_training_input "Link to this definition")

    :   Set the training inputs of the network spec.

        Parameters[:]

        :   

            **training_input: \[tuple\]**

            :   List of training input names and type of the network.

<!-- -->

*[class][ ]*[[coremltools.models.pipeline.]][[PipelineRegressor]][(]*[[input_features]]*, *[[output_features]]*, *[[training_features]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineRegressor)[](#coremltools.models.pipeline.PipelineRegressor "Link to this definition")

:   A pipeline model that exposes a sequence of models as a single model, It requires a set of inputs, a sequence of other models and a set of outputs. In this case the pipeline itself behaves as a regression model by designating a real valued output feature as its 'predicted feature'.

    [[\_\_init\_\_]][(]*[[input_features]]*, *[[output_features]]*, *[[training_features]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineRegressor.__init__)[](#coremltools.models.pipeline.PipelineRegressor.__init__ "Link to this definition")

    :   Create a set of pipeline models given a set of model specs. The final output model must be a regression model.

        Parameters[:]

        :   

            **input_features: \[list of 2-tuples\]**

            :   Name(s) of the input features, given as a list of ('name', datatype) tuples. The datatypes entry can be any of the data types defined in the [`models.datatypes`] module.

            **output_features: \[list of features\]**

            :   Name(s) of the output features, given as a list of ('name',datatype) tuples. The datatypes entry can be any of the data types defined in the [`models.datatypes`] module. All features must be either defined in the inputs or be produced by one of the contained models.

    [[add_model]][(]*[[spec]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineRegressor.add_model)[](#coremltools.models.pipeline.PipelineRegressor.add_model "Link to this definition")

    :   Add a protobuf spec or [`models.MLModel`] instance to the pipeline.

        All input features of this model must either match the input_features of the pipeline, or match the outputs of a previous model.

        Parameters[:]

        :   

            **spec: \[MLModel, Model_pb2\]**

            :   A protobuf spec or MLModel instance containing a model.

    [[set_training_input]][(]*[[training_input]]*[)][[[\[source\]]]](../_modules/coremltools/models/pipeline.html#PipelineRegressor.set_training_input)[](#coremltools.models.pipeline.PipelineRegressor.set_training_input "Link to this definition")

    :   Set the training inputs of the network spec.

        Parameters[:]

        :   

            **training_input: \[tuple\]**

            :   List of training input names and type of the network.

[]

## tree_ensemble[](#module-coremltools.models.tree_ensemble "Link to this heading")

Tree ensemble builder class to construct CoreML models.

*[class][ ]*[[coremltools.models.tree_ensemble.]][[TreeEnsembleBase]][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleBase)[](#coremltools.models.tree_ensemble.TreeEnsembleBase "Link to this definition")

:   Base class for the tree ensemble builder class. This should be instantiated either through the [[`TreeEnsembleRegressor`]](#coremltools.models.tree_ensemble.TreeEnsembleRegressor "coremltools.models.tree_ensemble.TreeEnsembleRegressor") or [[`TreeEnsembleClassifier`]](#coremltools.models.tree_ensemble.TreeEnsembleClassifier "coremltools.models.tree_ensemble.TreeEnsembleClassifier") classes.

    [[\_\_init\_\_]][(][)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleBase.__init__)[](#coremltools.models.tree_ensemble.TreeEnsembleBase.__init__ "Link to this definition")

    :   High level Python API to build a tree ensemble model for Core ML.

    [[add_branch_node]][(]*[[tree_id]]*, *[[node_id]]*, *[[feature_index]]*, *[[feature_value]]*, *[[branch_mode]]*, *[[true_child_id]]*, *[[false_child_id]]*, *[[relative_hit_rate]][[=]][[None]]*, *[[missing_value_tracks_true_child]][[=]][[False]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleBase.add_branch_node)[](#coremltools.models.tree_ensemble.TreeEnsembleBase.add_branch_node "Link to this definition")

    :   Add a branch node to the tree ensemble.

        Parameters[:]

        :   

            **tree_id: int**

            :   ID of the tree to add the node to.

            **node_id: int**

            :   ID of the node within the tree.

            **feature_index: int**

            :   Index of the feature in the input being split on.

            **feature_value: double or int**

            :   The value used in the feature comparison determining the traversal direction from this node.

            **branch_mode: str**

            :   Branch mode of the node, specifying the condition under which the node referenced by [`true_child_id`] is called next.

                Must be one of the following:

                > ::: 
                > - [`"BranchOnValueLessThanEqual"`]. Traverse to node [`true_child_id`] if [`input[feature_index]`]` `[`<=`]` `[`feature_value`], and [`false_child_id`] otherwise.
                >
                > - [`"BranchOnValueLessThan"`]. Traverse to node [`true_child_id`] if [`input[feature_index]`]` `[`<`]` `[`feature_value`], and [`false_child_id`] otherwise.
                >
                > - [`"BranchOnValueGreaterThanEqual"`]. Traverse to node [`true_child_id`] if [`input[feature_index]`]` `[`>=`]` `[`feature_value`], and [`false_child_id`] otherwise.
                >
                > - [`"BranchOnValueGreaterThan"`]. Traverse to node [`true_child_id`] if [`input[feature_index]`]` `[`>`]` `[`feature_value`], and [`false_child_id`] otherwise.
                >
                > - [`"BranchOnValueEqual"`]. Traverse to node [`true_child_id`] if [`input[feature_index]`]` `[`==`]` `[`feature_value`], and [`false_child_id`] otherwise.
                >
                > - [`"BranchOnValueNotEqual"`]. Traverse to node [`true_child_id`] if [`input[feature_index]`]` `[`!=`]` `[`feature_value`], and [`false_child_id`] otherwise.
                > :::

            **true_child_id: int**

            :   ID of the child under the true condition of the split. An error will be raised at model validation if this does not match the [`node_id`] of a node instantiated by [`add_branch_node`] or [`add_leaf_node`] within this [`tree_id`].

            **false_child_id: int**

            :   ID of the child under the false condition of the split. An error will be raised at model validation if this does not match the [`node_id`] of a node instantiated by [`add_branch_node`] or [`add_leaf_node`] within this [`tree_id`].

            **relative_hit_rate: float \[optional\]**

            :   When the model is converted compiled by CoreML, this gives hints to Core ML about which node is more likely to be hit on evaluation, allowing for additional optimizations. The values can be on any scale, with the values between child nodes being compared relative to each other.

            **missing_value_tracks_true_child: bool \[optional\]**

            :   If the training data contains NaN values or missing values, then this flag determines which direction a NaN value traverses.

    [[add_leaf_node]][(]*[[tree_id]]*, *[[node_id]]*, *[[values]]*, *[[relative_hit_rate]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleBase.add_leaf_node)[](#coremltools.models.tree_ensemble.TreeEnsembleBase.add_leaf_node "Link to this definition")

    :   Add a leaf node to the tree ensemble.

        Parameters[:]

        :   

            **tree_id: int**

            :   ID of the tree to add the node to.

            **node_id: int**

            :   ID of the node within the tree.

            **values: \[float \| int \| list \| dict\]**

            :   Value(s) at the leaf node to add to the prediction when this node is activated. If the prediction dimension of the tree is 1, then the value is specified as a float or integer value.

                For multidimensional predictions, the values can be a list of numbers with length matching the dimension of the predictions or a dictionary mapping index to value added to that dimension.

                Note that the dimension of any tree must match the dimension given when [[`set_default_prediction_value()`]](#coremltools.models.tree_ensemble.TreeEnsembleBase.set_default_prediction_value "coremltools.models.tree_ensemble.TreeEnsembleBase.set_default_prediction_value") is called.

    [[set_default_prediction_value]][(]*[[values]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleBase.set_default_prediction_value)[](#coremltools.models.tree_ensemble.TreeEnsembleBase.set_default_prediction_value "Link to this definition")

    :   Set the default prediction value(s).

        The values given here form the base prediction value that the values at activated leaves are added to. If values is a scalar, then the output of the tree must also be 1 dimensional; otherwise, values must be a list with length matching the dimension of values in the tree.

        Parameters[:]

        :   

            **values: \[int \| double \| list\[double\]\]**

            :   Default values for predictions.

    [[set_post_evaluation_transform]][(]*[[value]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleBase.set_post_evaluation_transform)[](#coremltools.models.tree_ensemble.TreeEnsembleBase.set_post_evaluation_transform "Link to this definition")

    :   Set the post processing transform applied after the prediction value from the tree ensemble.

        Parameters[:]

        :   

            **value: str**

            :   A value denoting the transform applied. Possible values are:

                - [`"NoTransform"`] (default). Do not apply a transform.

                - [`"Classification_SoftMax"`].

                  Apply a softmax function to the outcome to produce normalized, non-negative scores that sum to 1. The transformation applied to dimension i is equivalent to:

                  > :::: 
                  > ::: 
                  > \\\[\\frac}}\\\]
                  > :::
                  > ::::

                  Note: This is the output transformation applied by the XGBoost package with multiclass classification.

                - [`"Regression_Logistic"`].

                  Applies a logistic transform the predicted value, specifically:

                  > :::: 
                  > ::: 
                  > \\\[(1 + e\^)\^\\\]
                  > :::
                  > ::::

                  This is the transformation used in binary classification.

<!-- -->

*[class][ ]*[[coremltools.models.tree_ensemble.]][[TreeEnsembleClassifier]][(]*[[features]]*, *[[class_labels]]*, *[[output_features]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleClassifier)[](#coremltools.models.tree_ensemble.TreeEnsembleClassifier "Link to this definition")

:   Tree Ensemble builder class to construct a Tree Ensemble classification model.

    The TreeEnsembleClassifier class constructs a Tree Ensemble model incrementally using methods to add branch and leaf nodes specifying the behavior of the model.

    Examples

    In the following example, the code saves the model to disk, which is a recommended practice but not required.

    :::: 
    ::: highlight
        >>> input_features = [("a", datatypes.Array(3)), ("b", datatypes.Double())]

        >>> tm = TreeEnsembleClassifier(features = input_features, class_labels = [0, 1],
                                        output_features = "predicted_class")

        >>> # Split on a[2] <= 3
        >>> tm.add_branch_node(0, 0, 2, 3, "BranchOnValueLessThanEqual", 1, 2)

        >>> # Add leaf to the true branch of node 0 that subtracts 1.
        >>> tm.add_leaf_node(0, 1, -1)

        >>> # Add split on b == 0 to the false branch of node 0.
        >>> tm.add_branch_node(0, 2, 3, 0, "BranchOnValueEqual", 3, 4)

        >>> # Add leaf to the true branch of node 2 that adds 1 to the result.
        >>> tm.add_leaf_node(0, 3, 1)

        >>> # Add leaf to the false branch of node 2 that subtracts 1 from the result.
        >>> tm.add_leaf_node(0, 4, -1)

        >>> # Put in a softmax transform to translate these into probabilities.
        >>> tm.set_post_evaluation_transform("Classification_SoftMax")

        >>> tm.set_default_prediction_value([0, 0])

        >>> # save the model to a .mlmodel file
        >>> model_path = './tree.mlmodel'
        >>> coremltools.models.utils.save_spec(tm.spec, model_path)

        >>> # load the .mlmodel
        >>> mlmodel = coremltools.models.MLModel(model_path)

        >>> # make predictions
        >>> test_input = 
        >>> predictions = mlmodel.predict(test_input)
    :::
    ::::

    [[\_\_init\_\_]][(]*[[features]]*, *[[class_labels]]*, *[[output_features]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleClassifier.__init__)[](#coremltools.models.tree_ensemble.TreeEnsembleClassifier.__init__ "Link to this definition")

    :   Create a tree ensemble classifier model.

        Parameters[:]

        :   

            **features: \[list of features\]**

            :   Name(s) of the input features, given as a list of [`('name',`]` `[`datatype)`] tuples. The features are one of [`models.datatypes.Int64`], [`datatypes.Double`], or [`models.datatypes.Array`]. Feature indices in the nodes are counted sequentially from 0 through the features.

            **class_labels: \[list\]**

            :   A list of string or integer class labels to use in making predictions. The length of this must match the dimension of the tree model.

            **output_features: \[list\]**

            :   A string or a list of two strings specifying the names of the two output features, the first being a class label corresponding to the class with the highest predicted score, and the second being a dictionary mapping each class to its score. If [`output_features`] is a string, it specifies the predicted class label and the class scores is set to the default value of [`"classProbability"`].

<!-- -->

*[class][ ]*[[coremltools.models.tree_ensemble.]][[TreeEnsembleRegressor]][(]*[[features]]*, *[[target]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleRegressor)[](#coremltools.models.tree_ensemble.TreeEnsembleRegressor "Link to this definition")

:   Tree Ensemble builder class to construct a Tree Ensemble regression model.

    The TreeEnsembleRegressor class constructs a Tree Ensemble model incrementally using methods to add branch and leaf nodes specifying the behavior of the model.

    Examples

    In the following example, the code saves the model to disk, which is a recommended practice but not required.

    :::: 
    ::: highlight
        >>> # Required inputs
        >>> import coremltools
        >>> from coremltools.models import datatypes
        >>> from coremltools.models.tree_ensemble import TreeEnsembleRegressor
        >>> import numpy as np

        >>> # Define input features
        >>> input_features = [("a", datatypes.Array(3)), ("b", (datatypes.Double()))]

        >>> # Define output_features
        >>> output_features = [("predicted_values", datatypes.Double())]

        >>> tm = TreeEnsembleRegressor(features = input_features, target = output_features)

        >>> # Split on a[2] <= 3
        >>> tm.add_branch_node(0, 0, 2, 3, "BranchOnValueLessThanEqual", 1, 2)

        >>> # Add leaf to the true branch of node 0 that subtracts 1.
        >>> tm.add_leaf_node(0, 1, -1)

        >>> # Add split on b == 0 to the false branch of node 0, which is index 3
        >>> tm.add_branch_node(0, 2, 3, 0, "BranchOnValueEqual", 3, 4)

        >>> # Add leaf to the true branch of node 2 that adds 1 to the result.
        >>> tm.add_leaf_node(0, 3, 1)

        >>> # Add leaf to the false branch of node 2 that subtracts 1 from the result.
        >>> tm.add_leaf_node(0, 4, -1)

        >>> tm.set_default_prediction_value([0, 0])

        >>> # save the model to a .mlmodel file
        >>> model_path = './tree.mlmodel'
        >>> coremltools.models.utils.save_spec(tm.spec, model_path)

        >>> # load the .mlmodel
        >>> mlmodel = coremltools.models.MLModel(model_path)

        >>> # make predictions
        >>> test_input = 
        >>> predictions = mlmodel.predict(test_input)
    :::
    ::::

    [[\_\_init\_\_]][(]*[[features]]*, *[[target]]*[)][[[\[source\]]]](../_modules/coremltools/models/tree_ensemble.html#TreeEnsembleRegressor.__init__)[](#coremltools.models.tree_ensemble.TreeEnsembleRegressor.__init__ "Link to this definition")

    :   Create a Tree Ensemble regression model that takes one or more input features and maps them to an output feature.

        Parameters[:]

        :   

            **features: \[list of features\]**

            :   Name(s) of the input features, given as a list of [`('name',`]` `[`datatype)`] tuples. The features are one of [`models.datatypes.Int64`], [`datatypes.Double`], or [`models.datatypes.Array`]. Feature indices in the nodes are counted sequentially from 0 through the features.

            **target: (default = None)**

            :   Name of the target feature predicted.

[]

## utils[](#module-coremltools.models.utils "Link to this heading")

Utilities for the entire package.

*[class][ ]*[[coremltools.models.utils.]][[MultiFunctionDescriptor]][(]*[[model_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#MultiFunctionDescriptor)[](#coremltools.models.utils.MultiFunctionDescriptor "Link to this definition")

:   This data class defines how to construct a multifunction model from different model sources. Use the [`add_function`] method to specify the path to the source [`mlpackage`], along with the source and target function names.

    After setting the [`default_function_name`] to the [`MultiFunctionDescriptor`] instance, you can export a multifunction model using the [`save_multifunction`] method.

    ::: 
    See also

    [[`save_multifunction`]](#coremltools.models.utils.save_multifunction "coremltools.models.utils.save_multifunction")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        from coremltools.utils import MultiFunctionDescriptor, save_multifunction

        # Initialize a MultiFunctionDescriptor instance with functions in an existing mlpackage.
        # desc will contain all functions in "my_model.mlpackage"
        desc = MultiFunctionDescriptor("my_model.mlpackage")

        # Construct a MultiFunctionDescriptor instance from scratch.
        # The below code inserts the "main" function from "my_model.mlpackage" as "main_1",
        # and inserts the "main" function from "my_model_2.mlpackage" as "main_2".
        desc = MultiFunctionDescriptor()
        desc.add_function(
            model_path="my_model.mlpackage",
            source_function_name="main",
            target_function_name="main_1",
        )
        desc.add_function(
            model_path="my_model_2.mlpackage",
            source_function_name="main",
            target_function_name="main_2",
        )

        # Each MultiFunctionDescriptor instance must have a default function name
        # so it can be saved as a multifunction mlpackage on disk.
        desc.default_function_name = "main_1"
        save_multifunction(desc, "my_multifunction_model.mlpackage")
    :::
    ::::

    [[\_\_init\_\_]][(]*[[model_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#MultiFunctionDescriptor.__init__)[](#coremltools.models.utils.MultiFunctionDescriptor.__init__ "Link to this definition")

    :   If [`model_path`] is passed to the constructor, it must be a [`str`] pointing to an existing [`mlpackage`] on disk. The [[`MultiFunctionDescriptor`]](#coremltools.models.utils.MultiFunctionDescriptor "coremltools.models.utils.MultiFunctionDescriptor") instance will be initiated with the functions in [`model_path`].

    [[add_function]][(]*[[model_path]][[:]][ ][[str]]*, *[[src_function_name]][[:]][ ][[str]]*, *[[target_function_name]][[:]][ ][[str]]*[)] [[→] [[None]]][[[\[source\]]]](../_modules/coremltools/models/utils.html#MultiFunctionDescriptor.add_function)[](#coremltools.models.utils.MultiFunctionDescriptor.add_function "Link to this definition")

    :   Insert a [`src_function_name`] function from [`model_path`] as the [`target_function_name`] function in the multifunction descriptor.

    [[add_model]][(]*[[model_path]][[:]][ ][[str]]*[)] [[→] [[None]]][[[\[source\]]]](../_modules/coremltools/models/utils.html#MultiFunctionDescriptor.add_model)[](#coremltools.models.utils.MultiFunctionDescriptor.add_model "Link to this definition")

    :   Insert all functions from the model in [`model_path`] into the multifunction descriptor. The function names will remain the same as in the original model.

    [[remove_function]][(]*[[function_name]][[:]][ ][[str]]*[)] [[→] [[None]]][[[\[source\]]]](../_modules/coremltools/models/utils.html#MultiFunctionDescriptor.remove_function)[](#coremltools.models.utils.MultiFunctionDescriptor.remove_function "Link to this definition")

    :   Remove a function [`function_name`] from the multifunction descriptor.

<!-- -->

[[coremltools.models.utils.]][[bisect_model]][(]*[[model]][[:]][ ][[str][ ][[\|]][ ][[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[output_dir]][[:]][ ][[str]]*, *[[merge_chunks_to_pipeline]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[False]]*, *[[check_output_correctness]][[:]][ ][[bool][ ][[\|]][ ][None]][ ][[=]][ ][[True]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#bisect_model)[](#coremltools.models.utils.bisect_model "Link to this definition")

:   Utility function to split a mlpackage model into two mlpackages of approximately same file size.

    Parameters[:]

    :   

        **model: str or MLModel**

        :   Path to the mlpackage file, or a Core ML model, to be split into two mlpackages of approximately same file size.

        **output_dir: str**

        :   Path to output directory where the two model chunks / pipeline model would be saved.

            If the model is /.mlpackage, the chunk models are going to be saved as: 1. first chunk model: /\_chunk1.mlpackage 2. second chunk model: /\_chunk2.mlpackage 3. chunked pipeline model: /\_chunked_pipeline.mlpackage

            If the model is type of MLModel, the chunk models are saved as: 1. first chunk model: /chunk1.mlpackage 2. second chunk model: /chunk2.mlpackage 3. chunked pipeline model: /chunked_pipeline.mlpackage

        **merge_chunks_to_pipeline: bool**

        :   If True, model chunks are managed inside a single pipeline model for easier asset maintenance.

        **check_output_correctness: bool**

        :   - If True, compares the outputs of original Core ML model with that of pipelined CoreML model chunks and reports PSNR in dB.

            - Enabling this feature uses more memory. Disable it if your machine runs out of memory.

    Examples

    :::: 
    ::: highlight
        import coremltools as ct

        model_path = "my_model.mlpackage"
        output_dir = "./output/"

        # The following code will produce two smaller models:
        # `./output/my_model_chunk1.mlpackage` and `./output/my_model_chunk2.mlpackage`
        # It also compares the output numerical of the original Core ML model with the chunked models.
        ct.models.utils.bisect_model(
            model_path,
            output_dir,
        )

        # The following code will produce a single pipeline model `./output/my_model_chunked_pipeline.mlpackage`
        ct.models.utils.bisect_model(
            model_path,
            output_dir,
            merge_chunks_to_pipeline=True,
        )

        # You can also pass the MLModel object directly
        mlmodel = ct.models.MLModel(model_path)
        ct.models.utils.bisect_model(
            mlmodel,
            output_dir,
            merge_chunks_to_pipeline=True,
        )
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[change_input_output_tensor_type]][(]*[[ml_model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[from_type]][[:]][ ][[ArrayFeatureType]]*, *[[to_type]][[:]][ ][[ArrayFeatureType]]*, *[[function_names]][[:]][ ][[List][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[input_names]][[:]][ ][[List][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[output_names]][[:]][ ][[List][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]][[[\[source\]]]](../_modules/coremltools/models/utils.html#change_input_output_tensor_type)[](#coremltools.models.utils.change_input_output_tensor_type "Link to this definition")

:   Change the tensor data types of Core ML model inputs / outputs. Supported types are FLOAT16, FLOAT32.

    Parameters[:]

    :   

        **ml_model: MLModel**

        :   A Core ML model that needs to change its input/output type. Note: - the original model is not modified, the model with updated types is returned as a new instance. - only an mlProgram is supported (not pipelines, not neural networks).

        **from_type:**

        :   The type that should be changed from.

        **to_type:**

        :   The type that will be used instead of all the from_type type.

        **function_names:**

        :   Optional list of function names where the input/output needs to be changed. If not specified, only the "main" function will be updated.

        **input_names:**

        :   Optional list of input names that should be updated (by default none of the inputs will be updated).

        **output_names:**

        :   Optional list of output names that should be updated (by default all the outputs that match the from_type type will be updated).

    Examples

    :::: 
    ::: highlight
        from coremltools.models.model import MLModel
        from coremltools.utils import change_input_output_tensor_type
        from coremltools.proto.FeatureTypes_pb2 import ArrayFeatureType

        model = MLModel("my_model.mlpackage")
        updated_model = change_input_output_tensor_type(
            ml_model=model,
            from_type=ArrayFeatureType.FLOAT32,
            to_type=ArrayFeatureType.FLOAT16,
        )
        updated_model.save("my_updated_model.mlpackage")
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[compile_model]][(]*[[model]][[:]][ ][[Model][ ][[\|]][ ][str]]*, *[[destination_path]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[str]]][[[\[source\]]]](../_modules/coremltools/models/utils.html#compile_model)[](#coremltools.models.utils.compile_model "Link to this definition")

:   Compiles a Core ML model.

    Parameters[:]

    :   

        **model: Model_pb2 \| str**

        :   Either a Core ML model specification (protobuf object) or a path to a saved model (.mlmodel or .mlpackage) file.

        **destination_path: str**

        :   Path where the compiled model will be saved.

    Returns[:]

    :   

        **str**[Path to compiled model directory]

        :   If the [`destination_path`] is specified, that is the value that will be returned.

    ::: 
    See also

    [[`coremltools.models.CompiledMLModel`]](#coremltools.models.CompiledMLModel "coremltools.models.CompiledMLModel")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        from coremltools.models import CompiledMLModel
        from coremltools.models.utils import compile_model
        from coremltools.proto import Model_pb2

        spec = Model_pb2.Model()
        spec.specificationVersion = 1

        input_ = spec.description.input.add()
        input_.name = "x"
        input_.type.doubleType.MergeFromString(b"")

        output_ = spec.description.output.add()
        output_.name = "y"
        output_.type.doubleType.MergeFromString(b"")
        spec.description.predictedFeatureName = "y"

        lr = spec.glmRegressor
        lr.offset.append(0.1)
        weights = lr.weights.add()
        weights.value.append(2.0)

        compiled_model_path = compile_model(spec)
        model = CompiledMLModel(compiled_model_path)
        y = model.predict()
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[convert_double_to_float_multiarray_type]][(]*[[spec]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#convert_double_to_float_multiarray_type)[](#coremltools.models.utils.convert_double_to_float_multiarray_type "Link to this definition")

:   Convert all double multiarrays feature descriptions (input, output, training input) to float multiarrays.

    Parameters[:]

    :   

        **spec: Model_pb**

        :   The specification containing the multiarrays types to convert.

    Examples

    :::: 
    ::: highlight
        # In-place convert multiarray type of spec
        spec = mlmodel.get_spec()
        coremltools.utils.convert_double_to_float_multiarray_type(spec)
        model = coremltools.models.MLModel(spec)
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[evaluate_classifier]][(]*[[model]]*, *[[data]]*, *[[target]][[=]][[\'target\']]*, *[[verbose]][[=]][[False]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#evaluate_classifier)[](#coremltools.models.utils.evaluate_classifier "Link to this definition")

:   Evaluate a Core ML classifier model and compare against predictions from the original framework (for testing correctness of conversion). Use this evaluation for models that don't deal with probabilities.

    Parameters[:]

    :   

        **filename: list of str or list of MLModel**

        :   File to load the model from, or a loaded version of the MLModel.

        **data: list of str or list of Dataframe**

        :   Test data on which to evaluate the models (dataframe, or path to a CSV file).

        **target: str**

        :   Column to interpret as the target column.

        **verbose: bool**

        :   Set to true for more verbose output.

    ::: 
    See also

    [[`evaluate_regressor`]](#coremltools.models.utils.evaluate_regressor "coremltools.models.utils.evaluate_regressor"), [[`evaluate_classifier_with_probabilities`]](#coremltools.models.utils.evaluate_classifier_with_probabilities "coremltools.models.utils.evaluate_classifier_with_probabilities")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        metrics = coremltools.utils.evaluate_classifier(
            spec, "data_and_predictions.csv", "target"
        )
        print(metrics)
        
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[evaluate_classifier_with_probabilities]][(]*[[model]]*, *[[data]]*, *[[probabilities]][[=]][[\'probabilities\']]*, *[[verbose]][[=]][[False]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#evaluate_classifier_with_probabilities)[](#coremltools.models.utils.evaluate_classifier_with_probabilities "Link to this definition")

:   Evaluate a classifier specification for testing.

    Parameters[:]

    :   

        **filename: \[str \| Model\]**

        :   File to load the model from, or a loaded version of the MLModel.

        **data: \[str \| Dataframe\]**

        :   Test data on which to evaluate the models (dataframe, or path to a CSV file).

        **probabilities: str**

        :   Column to interpret as the probabilities column.

        **verbose: bool**

        :   Verbosity levels of the predictions.

<!-- -->

[[coremltools.models.utils.]][[evaluate_regressor]][(]*[[model]]*, *[[data]]*, *[[target]][[=]][[\'target\']]*, *[[verbose]][[=]][[False]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#evaluate_regressor)[](#coremltools.models.utils.evaluate_regressor "Link to this definition")

:   Evaluate a Core ML regression model and compare against predictions from the original framework (for testing correctness of conversion).

    Parameters[:]

    :   

        **model: MLModel or str**

        :   A loaded MLModel or a path to a saved MLModel.

        **data: Dataframe**

        :   Test data on which to evaluate the models.

        **target: str**

        :   Name of the column in the dataframe to be compared against the prediction.

        **verbose: bool**

        :   Set to true for a more verbose output.

    ::: 
    See also

    [[`evaluate_classifier`]](#coremltools.models.utils.evaluate_classifier "coremltools.models.utils.evaluate_classifier")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        metrics = coremltools.utils.evaluate_regressor(
            spec, "data_and_predictions.csv", "target"
        )
        print(metrics)
        
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[evaluate_transformer]][(]*[[model]]*, *[[input_data]]*, *[[reference_output]]*, *[[verbose]][[=]][[False]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#evaluate_transformer)[](#coremltools.models.utils.evaluate_transformer "Link to this definition")

:   Evaluate a transformer specification for testing.

    Parameters[:]

    :   

        **model: list of str or list of MLModel**

        :   File to load the Model from, or a loaded version of the MLModel.

        **input_data: list of dict**

        :   Test data on which to evaluate the models.

        **reference_output: list of dict**

        :   Expected results for the model.

        **verbose: bool**

        :   Verbosity levels of the predictions.

    ::: 
    See also

    [[`evaluate_regressor`]](#coremltools.models.utils.evaluate_regressor "coremltools.models.utils.evaluate_regressor"), [[`evaluate_classifier`]](#coremltools.models.utils.evaluate_classifier "coremltools.models.utils.evaluate_classifier")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        input_data = [, ]
        expected_output = [, ]
        metrics = coremltools.utils.evaluate_transformer(
            scaler_spec, input_data, expected_output
        )
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[load_spec]][(]*[[model_path]][[:]][ ][[str]]*[)] [[→] [[\_proto.Model_pb2]]][[[\[source\]]]](../_modules/coremltools/models/utils.html#load_spec)[](#coremltools.models.utils.load_spec "Link to this definition")

:   Load a protobuf model specification from file ([`mlmodel`]) or directory ([`mlpackage`]).

    Parameters[:]

    :   

        **model_path: Path to the model from which the protobuf spec is loaded.**

        :   

    Returns[:]

    :   

        model_spec: Model_pb

        :   Protobuf representation of the model.

    ::: 
    See also

    [[`save_spec`]](#coremltools.models.utils.save_spec "coremltools.models.utils.save_spec")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        spec = coremltools.utils.load_spec("HousePricer.mlmodel")
        spec = coremltools.utils.load_spec("HousePricer.mlpackage")
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[make_pipeline]][(]*[[\*]][[models]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[compute_units]][[:]][ ][[None][ ][[\|]][ ][ComputeUnit]][ ][[=]][ ][[None]]*[)] [[→] [[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]][[[\[source\]]]](../_modules/coremltools/models/utils.html#make_pipeline)[](#coremltools.models.utils.make_pipeline "Link to this definition")

:   Makes a pipeline with the given models.

    Parameters[:]

    :   

        **\*models**

        :   Two or more instances of [`ct.models.MLModel`].

        **compute_units**

        :   The set of processing units that all models in the pipeline can use to make predictions. Can be [`None`] or [`coremltools.ComputeUnit`].

            - If [`None`], the [`compute_unit`] will be inferred from the [`compute_unit`] values of the models. If all models do not have the same [`compute_unit`] values, this parameter must be specified.

            - 

              [`coremltools.ComputeUnit`] is an enum with four possible values:

              :   - [`coremltools.ComputeUnit.ALL`]: Use all compute units available, including the neural engine.

                  - [`coremltools.ComputeUnit.CPU_ONLY`]: Limit the model to only use the CPU.

                  - [`coremltools.ComputeUnit.CPU_AND_GPU`]: Use both the CPU and GPU, but not the neural engine.

                  - [`coremltools.ComputeUnit.CPU_AND_NE`]: Use both the CPU and neural engine, but not the GPU. Available only for macOS \>= 13.0.

    Returns[:]

    :   

        ct.models.MLModel

        :   

    Examples

    :::: 
    ::: highlight
        my_model1 = ct.models.MLModel("/tmp/m1.mlpackage")
        my_model2 = ct.models.MLModel("/tmp/m2.mlmodel")

        my_pipeline_model = ct.utils.make_pipeline(my_model1, my_model2)

        y = my_pipeline_model.predict()

        my_pipeline_model.save("/tmp/my_pipeline.mlpackage")
        new_my_pipeline = ct.model.MLModel("/tmp/my_pipeline.mlpackage")
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[materialize_dynamic_shape_mlmodel]][(]*[[dynamic_shape_mlmodel]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[function_name_to_materialization_map]][[:]][ ][[Dict][[\[]][str][[,]][ ][Dict][[\[]][str][[,]][ ][Tuple][[\[]][int][[\]]][[\]]][[\]]]]*, *[[destination_path]][[:]][ ][[str]]*, *[[source_function_name]][[:]][ ][[str]][ ][[=]][ ][[\'main\']]*[)] [[→] [[None]]][[[\[source\]]]](../_modules/coremltools/models/utils.html#materialize_dynamic_shape_mlmodel)[](#coremltools.models.utils.materialize_dynamic_shape_mlmodel "Link to this definition")

:   Given a dynamic-shape mlmodel, materialize symbols to create fixed-shape functions, then save as an .mlpackage to destination path. To save memory, the pymil program of input dynamic-shape mlmodel is re-used. Constant deduplication across functions is performed to allow weight sharing.

    Parameters[:]

    :   

        **dynamic_shape_mlmodel**[ct.models.MLModel]

        :   A dynamic-shape mlmodel to be materialized

        **function_name_to_materialization_map: Dict\[str, Dict\[str, Tuple\[int\]\]\]**

        :   A dictionary specifying the name of new functions to be created, and for each new function what is the new fixed shapes for inputs. If a new function has the same name as an old function, then the old function will be overridden

        **destination_path**[str]

        :   The saved .mlpackage model path

        **source_function_name: str**

        :   The name of the source symbolic-shape function to be materialized, default = main

    ::: 
    See also

    [`coremltools.converters.mil.mil.passes.defs.experiment.materialize_symbolic_shape_program`]

    :   
    :::

    Examples

    :::: 
    ::: highlight
        from coremltools.utils import materialize_dynamic_shape_mlmodel

        # A dynamic-shape mlmodel you have converted
        dynamic_shape_mlmodel: ct.models.MLModel

        # As an example, let us assume the inputs are
        # 1. ``input_ids (1, query_length)``
        # 2. ``mask (query_length, context_length)``
        function_name_to_materialization_map = ,
                "materialization_4_5": ,
            }
        }

        materialize_dynamic_shape_mlmodel(
            dynamic_shape_mlmodel,
            function_name_to_materialization_map,
            "materialized_model.mlpackage",
        )
    :::
    ::::

    To make prediction from the materialized mlmodel, load the desired materialized function

    :::: 
    ::: highlight
        materialization_2_3 = ct.models.MLModel(
            "materialized_model.mlpackage", function_name="materialization_2_3"
        )
        materialization_4_5 = ct.models.MLModel(
            "materialized_model.mlpackage", function_name="materialization_4_5"
        )
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[randomize_weights]][(]*[[mlmodel]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#randomize_weights)[](#coremltools.models.utils.randomize_weights "Link to this definition")

:   Utility function to randomize weights

    Parameters[:]

    :   

        **mlmodel: MLModel**

        :   Model which will be randomized.

    Returns[:]

    :   

        model: MLModel

        :   The MLModel with randomized weights.

    Examples

    :::: 
    ::: highlight
        import coremltools as ct

        model = ct.models.MLModel("my_model.mlpackage")
        randomized_mlmodel = ct.models.utils.randomize_weights(mlmodel)
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[rename_feature]][(]*[[spec]]*, *[[current_name]]*, *[[new_name]]*, *[[rename_inputs]][[=]][[True]]*, *[[rename_outputs]][[=]][[True]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#rename_feature)[](#coremltools.models.utils.rename_feature "Link to this definition")

:   Rename a feature in the specification.

    Parameters[:]

    :   

        **spec: Model_pb**

        :   The specification containing the feature to rename.

        **current_name: str**

        :   Current name of the feature. If this feature doesn't exist, the rename is a no-op.

        **new_name: str**

        :   New name of the feature.

        **rename_inputs: bool**

        :   Search for [`current_name`] only in the input features (that is, ignore output features).

        **rename_outputs: bool**

        :   Search for [`current_name`] only in the output features (that is, ignore input features).

    Examples

    :::: 
    ::: highlight
        # In-place rename of spec
        model = MLModel("model.mlmodel")
        spec = model.get_spec()
        coremltools.utils.rename_feature(spec, "old_feature", "new_feature_name")
        # re-initialize model
        model = MLModel(spec)
        model.save("model.mlmodel")

        # Rename a spec when the model is an mlprogram, in that case, weights are stored outside of the spec
        model = coremltools.convert(torch_model, convert_to="mlprogram")
        spec = model.get_spec()
        # print info about inputs and outputs
        print(spec.description)
        coremltools.utils.rename_feature(spec, "old_feature", "new_feature_name")
        # re-initialize model
        model = MLModel(spec, weights_dir=model.weights_dir)
        model.save("model.mlpackage")
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[save_multifunction]][(]*[[desc]][[:]][ ][[[MultiFunctionDescriptor]](#coremltools.models.utils.MultiFunctionDescriptor "coremltools.models.utils.MultiFunctionDescriptor")]*, *[[destination_path]][[:]][ ][[str]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#save_multifunction)[](#coremltools.models.utils.save_multifunction "Link to this definition")

:   Save a [[`MultiFunctionDescriptor`]](#coremltools.models.utils.MultiFunctionDescriptor "coremltools.models.utils.MultiFunctionDescriptor") instance into a multifunction [`mlpackage`]. This function also performs constant deduplication across functions to allow for weight sharing.

    Parameters[:]

    :   

        **desc: MultiFunctionDescriptor**

        :   Multifunction descriptor to save on the disk.

        **destination_path: str**

        :   The path where the new [`mlpackage`] will be saved.

    ::: 
    See also

    [[`MultiFunctionDescriptor`]](#coremltools.models.utils.MultiFunctionDescriptor "coremltools.models.utils.MultiFunctionDescriptor")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        from coremltools.utils import MultiFunctionDescriptor, save_multifunction

        desc = MultiFunctionDescriptor("my_model_1.mlpackage")
        desc.add_function("my_model_2.mlpackage", "main", "main_2")
        desc.default_function_name = "main_2"

        save_multifunction(desc, "multifunction_model.mlpackage")
    :::
    ::::

<!-- -->

[[coremltools.models.utils.]][[save_spec]][(]*[[spec]]*, *[[filename]]*, *[[auto_set_specification_version]][[=]][[False]]*, *[[weights_dir]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/utils.html#save_spec)[](#coremltools.models.utils.save_spec "Link to this definition")

:   Save a protobuf model specification to file.

    Parameters[:]

    :   

        **spec: Model_pb**

        :   Protobuf representation of the model.

        **filename: str**

        :   File path where the spec is saved.

        **auto_set_specification_version: bool**

        :   If [`True`], will always try to set specification version automatically.

        **weights_dir: str**

        :   Path to the directory containing the weights.bin file. This is required when the spec has model type [`mlprogram`]. If the [`mlprogram`] does not contain any weights, this path can be an empty directory.

    ::: 
    See also

    [[`load_spec`]](#coremltools.models.utils.load_spec "coremltools.models.utils.load_spec")

    :   
    :::

    Examples

    :::: 
    ::: highlight
        coremltools.utils.save_spec(spec, "HousePricer.mlmodel")
        coremltools.utils.save_spec(spec, "HousePricer.mlpackage")
        coremltools.utils.save_spec(
            spec, "mlprogram_model.mlpackage", weights_dir="/path/to/weights/directory"
        )
    :::
    ::::

[]

## compute_plan[](#module-coremltools.models.compute_plan "Link to this heading")

*[class][ ]*[[coremltools.models.compute_plan.]][[MLComputePlan]][(]*[[proxy]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLComputePlan)[](#coremltools.models.compute_plan.MLComputePlan "Link to this definition")

:   Represents the plan for executing a model.

    The application can use the plan to estimate the necessary cost and resources of the model before running the predictions.

    [[get_compute_device_usage_for_mlprogram_operation]][(]*[[operation]][[:]][ ][[[MLModelStructureProgramOperation]](#coremltools.models.compute_plan.MLModelStructureProgramOperation "coremltools.models.compute_plan.MLModelStructureProgramOperation")]*[)] [[→] [[[MLComputePlanDeviceUsage]](#coremltools.models.compute_plan.MLComputePlanDeviceUsage "coremltools.models.compute_plan.MLComputePlanDeviceUsage")[ ][[\|]][ ][None]]][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLComputePlan.get_compute_device_usage_for_mlprogram_operation)[](#coremltools.models.compute_plan.MLComputePlan.get_compute_device_usage_for_mlprogram_operation "Link to this definition")

    :   Returns the estimated cost of executing an ML Program operation.

        Parameters[:]

        :   

            **operation**[MLModelStructureProgramOperation]

            :   An ML Program operation.

        Returns[:]

        :   

            Optional\[MLComputePlanDeviceUsage\]

            :   The anticipated compute devices that would be used for executing the operation or [`None`] if the usage couldn't be determined.

    [[get_compute_device_usage_for_neuralnetwork_layer]][(]*[[layer]][[:]][ ][[[MLModelStructureNeuralNetworkLayer]](#coremltools.models.compute_plan.MLModelStructureNeuralNetworkLayer "coremltools.models.compute_plan.MLModelStructureNeuralNetworkLayer")]*[)] [[→] [[[MLComputePlanDeviceUsage]](#coremltools.models.compute_plan.MLComputePlanDeviceUsage "coremltools.models.compute_plan.MLComputePlanDeviceUsage")[ ][[\|]][ ][None]]][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLComputePlan.get_compute_device_usage_for_neuralnetwork_layer)[](#coremltools.models.compute_plan.MLComputePlan.get_compute_device_usage_for_neuralnetwork_layer "Link to this definition")

    :   Returns the estimated cost of executing a NeuralNetwork layer.

        Parameters[:]

        :   

            **operation**[MLModelStructureProgramOperation]

            :   A NeuralNetwork layer.

        Returns[:]

        :   

            Optional\[MLComputePlanDeviceUsage\]

            :   The anticipated compute devices that would be used for executing the layer or [`None`] if the usage couldn't be determined.

    [[get_estimated_cost_for_mlprogram_operation]][(]*[[operation]][[:]][ ][[[MLModelStructureProgramOperation]](#coremltools.models.compute_plan.MLModelStructureProgramOperation "coremltools.models.compute_plan.MLModelStructureProgramOperation")]*[)] [[→] [[[MLComputePlanCost]](#coremltools.models.compute_plan.MLComputePlanCost "coremltools.models.compute_plan.MLComputePlanCost")[ ][[\|]][ ][None]]][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLComputePlan.get_estimated_cost_for_mlprogram_operation)[](#coremltools.models.compute_plan.MLComputePlan.get_estimated_cost_for_mlprogram_operation "Link to this definition")

    :   Returns the estimated cost of executing an ML Program operation.

        Parameters[:]

        :   

            **operation**[MLModelStructureProgramOperation]

            :   An ML Program operation.

        Returns[:]

        :   

            Optional\[MLComputePlanCost\]

            :   The estimated cost of executing the operation.

    *[classmethod][ ]*[[load_from_path]][(]*[[path]][[:]][ ][[str]]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*[)] [[→] [[[MLComputePlan]](#coremltools.models.compute_plan.MLComputePlan "coremltools.models.compute_plan.MLComputePlan")]][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLComputePlan.load_from_path)[](#coremltools.models.compute_plan.MLComputePlan.load_from_path "Link to this definition")

    :   Loads the compute plan of a compiled model.

        The path must be the location of the [`mlmodelc`] directory.

        Parameters[:]

        :   

            **compiled_model_path**[str]

            :   The path to the compiled model.

        Returns[:]

        :   

            The plan for executing the model.

            :   

        Examples

        :::: 
        ::: highlight
            compute_plan = coremltools.models.compute_plan.MLComputePlan.load_from_path(
                model.get_compiled_path()
            )

            if compute_plan.model_structure.program is None:
                raise ValueError("Unexpected model type.")

            program = compute_plan.model_structure.program
            mainFunction = program["main"]
            for operation in mainFunction.block.operations:
                # Get the compute device usage for the operation.
                compute_device_usage = (
                    compute_plan.get_compute_device_usage_for_mlprogram_operation(operation)
                )
                # Get the estimated cost of executing the operation.
                estimated_cost = compute_plan.get_estimated_cost_for_mlprogram_operation(operation)
        :::
        ::::

    *[async][ ]*[[load_from_path_on_device]][(]*[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[[MLComputePlan]](#coremltools.models.compute_plan.MLComputePlan "coremltools.models.compute_plan.MLComputePlan")]][](#coremltools.models.compute_plan.MLComputePlan.load_from_path_on_device "Link to this definition")

    :   Loads the compute plan of a compiled model on a remote or local device.

        The path must be the location of the [`mlmodelc`] directory.

        Parameters[:]

        :   

            **path**[str]

            :   The path to the compiled model.

        Returns[:]

        :   

            The plan for executing the model.

            :   

        Examples

        :::: 
        ::: highlight
            # Retrieve a development device.
            devices = Device.get_connected_development_devices(device_type=DeviceType.IPHONE)
            device = devices[0]
            # Prepare device for model debugging.
            device = await device.prepare_for_model_debugging()
            compute_plan = await coremltools.models.ml_program.experimental.compute_plan_utils.load_compute_plan_from_path_on_device(
                path=model.get_compiled_path(),
                device=device,
            )

            if compute_plan.model_structure.program is None:
                raise ValueError("Unexpected model type.")

            program = compute_plan.model_structure.program
            mainFunction = program.functions["main"]
            for operation in mainFunction.block.operations:
                # Get the compute device usage for the operation.
                compute_device_usage = (
                    compute_plan.get_compute_device_usage_for_mlprogram_operation(operation)
                )
                # Get the estimated cost of executing the operation.
                estimated_cost = compute_plan.get_estimated_cost_for_mlprogram_operation(operation)
        :::
        ::::

    *[property][ ]*[[model_structure]]*[[:]][ ][[MLModelStructure]](#coremltools.models.compute_plan.MLModelStructure "coremltools.models.compute_plan.MLModelStructure")*[](#coremltools.models.compute_plan.MLComputePlan.model_structure "Link to this definition")

    :   Returns the model structure.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLComputePlanCost]][(]*[[weight]][[:]][ ][[float]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLComputePlanCost)[](#coremltools.models.compute_plan.MLComputePlanCost "Link to this definition")

:   Represents the estimated cost of executing a layer/operation.

    Attributes[:]

    :   

        **weight**[float]

        :   The estimated workload of executing the operation over the total model execution. The value is between \[0.0, 1.0\].

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLComputePlanDeviceUsage]][(]*[[preferred_compute_device]][[:]][ ][[[MLComputeDevice]](#coremltools.models.compute_device.MLComputeDevice "coremltools.models.compute_device.MLComputeDevice")]*, *[[supported_compute_devices]][[:]][ ][[List][[\[]][[MLComputeDevice]](#coremltools.models.compute_device.MLComputeDevice "coremltools.models.compute_device.MLComputeDevice")[[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLComputePlanDeviceUsage)[](#coremltools.models.compute_plan.MLComputePlanDeviceUsage "Link to this definition")

:   Represents the anticipated compute devices that would be used for executing a layer/operation.

    Attributes[:]

    :   

        **preferred_compute_device**[MLComputeDevice]

        :   The compute device that the framework prefers to execute the layer/operation.

        **supported_compute_devices**[List\[MLComputeDevice\]]

        :   The compute device that the framework prefers to execute the layer/operation.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructure]][(]*[[neuralnetwork]][[:]][ ][[[MLModelStructureNeuralNetwork]](#coremltools.models.compute_plan.MLModelStructureNeuralNetwork "coremltools.models.compute_plan.MLModelStructureNeuralNetwork")[ ][[\|]][ ][None]]*, *[[program]][[:]][ ][[[MLModelStructureProgram]](#coremltools.models.compute_plan.MLModelStructureProgram "coremltools.models.compute_plan.MLModelStructureProgram")[ ][[\|]][ ][None]]*, *[[pipeline]][[:]][ ][[[MLModelStructurePipeline]](#coremltools.models.compute_plan.MLModelStructurePipeline "coremltools.models.compute_plan.MLModelStructurePipeline")[ ][[\|]][ ][None]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructure)[](#coremltools.models.compute_plan.MLModelStructure "Link to this definition")

:   Represents the structure of a model.

    Attributes[:]

    :   

        **neuralnetwork**[Optional\[MLModelStructureNeuralNetwork\]]

        :   The structure of a NeuralNetwork model, if the model is a NeuralNetwork; otherwise None.

        **program**[Optional\[MLModelStructureProgram\]]

        :   The structure of an ML Program model, if the model is an ML Program; otherwise, None.

        **pipeline**[Optional\[MLModelStructurePipeline\]]

        :   The structure of a Pipeline model. if the model is a Pipeline; otherwise None.

    *[classmethod][ ]*[[load_from_path]][(]*[[compiled_model_path]][[:]][ ][[str]]*[)] [[→] [[[MLModelStructure]](#coremltools.models.compute_plan.MLModelStructure "coremltools.models.compute_plan.MLModelStructure")]][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructure.load_from_path)[](#coremltools.models.compute_plan.MLModelStructure.load_from_path "Link to this definition")

    :   Loads the structure of a compiled model.

        The path must be the location of the [`mlmodelc`] directory.

        Parameters[:]

        :   

            **compiled_model_path (str): The path to the compiled model.**

            :   

        Returns[:]

        :   

            MLModelStructure

            :   An instance of MLModelStructure.

        Examples

        :::: 
        ::: highlight
            model_structure = coremltools.models.compute_plan.MLModelStructure.load_from_path(
                model.get_compiled_path()
            )

            if model_structure.neuralNetwork is not None:
                # Examine Neural network model.
                pass
            elif model_structure.program is not None:
                # Examine ML Program model.
                pass
            elif model_structure.pipeline is not None:
                # Examine Pipeline model.
                pass
            else:
                # The model type is something else.
                pass
        :::
        ::::

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureNeuralNetwork]][(]*[[layers]][[:]][ ][[List][[\[]][[MLModelStructureNeuralNetworkLayer]](#coremltools.models.compute_plan.MLModelStructureNeuralNetworkLayer "coremltools.models.compute_plan.MLModelStructureNeuralNetworkLayer")[[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureNeuralNetwork)[](#coremltools.models.compute_plan.MLModelStructureNeuralNetwork "Link to this definition")

:   Represents the structure of a neural network model.

    Attributes[:]

    :   

        **layers**[List\[MLModelStructureNeuralNetworkLayer\]]

        :   The list of layers in the neural network.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureNeuralNetworkLayer]][(]*[[name]][[:]][ ][[str]]*, *[[type]][[:]][ ][[str]]*, *[[input_names]][[:]][ ][[List][[\[]][str][[\]]]]*, *[[output_names]][[:]][ ][[List][[\[]][str][[\]]]]*, *[[\_\_proxy\_\_]][[:]][ ][[Any]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureNeuralNetworkLayer)[](#coremltools.models.compute_plan.MLModelStructureNeuralNetworkLayer "Link to this definition")

:   Represents a layer in a neural network model structure.

    Attributes[:]

    :   

        **name**[str]

        :   The name of the neural network layer.

        **type**[str]

        :   The type of the layer (e.g., 'Dense', 'Convolutional', etc.).

        **input_names**[List\[str\]]

        :   A list of names representing the inputs to this layer.

        **output_names**[List\[str\]]

        :   A list of names representing the outputs from this layer.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructurePipeline]][(]*[[sub_models]][[:]][ ][[Tuple][[\[]][str][[,]][ ][[MLModelStructure]](#coremltools.models.compute_plan.MLModelStructure "coremltools.models.compute_plan.MLModelStructure")[[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructurePipeline)[](#coremltools.models.compute_plan.MLModelStructurePipeline "Link to this definition")

:   Represents the structure of a pipeline model.

    Attributes[:]

    :   

        **sub_models**[Tuple\[str, MLModelStructure\]]

        :   The list of sub-models in the pipeline.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgram]][(]*[[functions]][[:]][ ][[Dict][[\[]][str][[,]][ ][[MLModelStructureProgramFunction]](#coremltools.models.compute_plan.MLModelStructureProgramFunction "coremltools.models.compute_plan.MLModelStructureProgramFunction")[[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgram)[](#coremltools.models.compute_plan.MLModelStructureProgram "Link to this definition")

:   Represents the structure of an ML Program model.

    Attributes[:]

    :   

        **functions**[Dict\[str, MLModelStructureProgramFunction\]]

        :   The functions in the program.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramArgument]][(]*[[bindings]][[:]][ ][[List][[\[]][[MLModelStructureProgramBinding]](#coremltools.models.compute_plan.MLModelStructureProgramBinding "coremltools.models.compute_plan.MLModelStructureProgramBinding")[[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramArgument)[](#coremltools.models.compute_plan.MLModelStructureProgramArgument "Link to this definition")

:   Represents an argument in an ML Program.

    Attributes[:]

    :   

        **bindings**[List\[MLModelStructureProgramBinding\]]

        :   The list of bindings.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramBinding]][(]*[[name]][[:]][ ][[str][ ][[\|]][ ][None]]*, *[[value]][[:]][ ][[[MLModelStructureProgramValue]](#coremltools.models.compute_plan.MLModelStructureProgramValue "coremltools.models.compute_plan.MLModelStructureProgramValue")[ ][[\|]][ ][None]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramBinding)[](#coremltools.models.compute_plan.MLModelStructureProgramBinding "Link to this definition")

:   Represents a binding between a name and a program value in an ML Program. This is either a previously defined name of a variable or a constant value in the Program.

    Attributes[:]

    :   

        **name**[Optional\[str\]]

        :   The name of the variable, it can be None.

        **value**[Optional\[MLModelStructureProgramValue\]]

        :   The constant value, it can be None.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramBlock]][(]*[[inputs]][[:]][ ][[List][[\[]][[MLModelStructureProgramNamedValueType]](#coremltools.models.compute_plan.MLModelStructureProgramNamedValueType "coremltools.models.compute_plan.MLModelStructureProgramNamedValueType")[[\]]]]*, *[[operations]][[:]][ ][[List][[\[]][[MLModelStructureProgramOperation]](#coremltools.models.compute_plan.MLModelStructureProgramOperation "coremltools.models.compute_plan.MLModelStructureProgramOperation")[[\]]]]*, *[[output_names]][[:]][ ][[List][[\[]][str][[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramBlock)[](#coremltools.models.compute_plan.MLModelStructureProgramBlock "Link to this definition")

:   Represents a block in an ML Program.

    Attributes[:]

    :   

        **inputs**[List\[MLModelStructureProgramNamedValueType\]]

        :   The named inputs to the block.

        **operator_name**[str]

        :   The name of the operator, e.g., "conv", "pool", "softmax", etc.

        **outputs**[List\[MLModelStructureProgramNamedValueType\]]

        :   The outputs of the Operation.

        **blocks: List\[MLModelStructureProgramBlock\]**

        :   The list of nested blocks for loops and conditionals, e.g., a conditional block will have two entries here.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramFunction]][(]*[[inputs]][[:]][ ][[List][[\[]][[MLModelStructureProgramNamedValueType]](#coremltools.models.compute_plan.MLModelStructureProgramNamedValueType "coremltools.models.compute_plan.MLModelStructureProgramNamedValueType")[[\]]]]*, *[[block]][[:]][ ][[[MLModelStructureProgramBlock]](#coremltools.models.compute_plan.MLModelStructureProgramBlock "coremltools.models.compute_plan.MLModelStructureProgramBlock")]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramFunction)[](#coremltools.models.compute_plan.MLModelStructureProgramFunction "Link to this definition")

:   Represents a function in an ML Program.

    Attributes[:]

    :   

        **inputs**[List\[MLModelStructureProgramNamedValueType\]]

        :   The named inputs to the function.

        **block**[MLModelStructureProgramBlock]

        :   The active block in the function.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramNamedValueType]][(]*[[name]][[:]][ ][[str]]*, *[[type]][[:]][ ][[[MLModelStructureProgramValueType]](#coremltools.models.compute_plan.MLModelStructureProgramValueType "coremltools.models.compute_plan.MLModelStructureProgramValueType")]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramNamedValueType)[](#coremltools.models.compute_plan.MLModelStructureProgramNamedValueType "Link to this definition")

:   Represents a parameter's name and type in an ML Program.

    Attributes[:]

    :   

        **name**[str]

        :   The name of the parameter.

        **type**[MLModelStructureProgramValueType]

        :   The type of the parameter.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramOperation]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][[MLModelStructureProgramArgument]](#coremltools.models.compute_plan.MLModelStructureProgramArgument "coremltools.models.compute_plan.MLModelStructureProgramArgument")[[\]]]]*, *[[operator_name]][[:]][ ][[str]]*, *[[outputs]][[:]][ ][[List][[\[]][[MLModelStructureProgramNamedValueType]](#coremltools.models.compute_plan.MLModelStructureProgramNamedValueType "coremltools.models.compute_plan.MLModelStructureProgramNamedValueType")[[\]]]]*, *[[blocks]][[:]][ ][[List][[\[]][[MLModelStructureProgramBlock]](#coremltools.models.compute_plan.MLModelStructureProgramBlock "coremltools.models.compute_plan.MLModelStructureProgramBlock")[[\]]]]*, *[[\_\_proxy\_\_]][[:]][ ][[Any]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramOperation)[](#coremltools.models.compute_plan.MLModelStructureProgramOperation "Link to this definition")

:   Represents an operation in an ML Program.

    Attributes[:]

    :   

        **inputs**[Dict\[str, MLModelStructureProgramArgument\]]

        :   The arguments to the Operation.

        **operator_name**[str]

        :   The name of the operator, e.g., "conv", "pool", "softmax", etc.

        **outputs**[List\[MLModelStructureProgramNamedValueType\]]

        :   The outputs of the Operation.

        **blocks**[List\[MLModelStructureProgramBlock\]]

        :   The list of nested blocks for loops and conditionals, e.g., a conditional block will have two entries here.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramValue]][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramValue)[](#coremltools.models.compute_plan.MLModelStructureProgramValue "Link to this definition")

:   Represents the value of a constant in an ML Program.

<!-- -->

*[class][ ]*[[coremltools.models.compute_plan.]][[MLModelStructureProgramValueType]][[[\[source\]]]](../_modules/coremltools/models/compute_plan.html#MLModelStructureProgramValueType)[](#coremltools.models.compute_plan.MLModelStructureProgramValueType "Link to this definition")

:   Represents the type of a value or a variable in an ML Program.

[]

## compute_device[](#module-coremltools.models.compute_device "Link to this heading")

*[class][ ]*[[coremltools.models.compute_device.]][[MLCPUComputeDevice]][(]*[[proxy]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_device.html#MLCPUComputeDevice)[](#coremltools.models.compute_device.MLCPUComputeDevice "Link to this definition")

:   Represents a CPU compute device.

<!-- -->

*[class][ ]*[[coremltools.models.compute_device.]][[MLComputeDevice]][[[\[source\]]]](../_modules/coremltools/models/compute_device.html#MLComputeDevice)[](#coremltools.models.compute_device.MLComputeDevice "Link to this definition")

:   Represents a compute device.

    The represented device is capable of running machine learning computations and other tasks like analysis and processing of images, sound, etc.

    *[classmethod][ ]*[[get_all_compute_devices]][(][)] [[→] [[List][[\[]][[MLComputeDevice]](#coremltools.models.compute_device.MLComputeDevice "coremltools.models.compute_device.MLComputeDevice")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/compute_device.html#MLComputeDevice.get_all_compute_devices)[](#coremltools.models.compute_device.MLComputeDevice.get_all_compute_devices "Link to this definition")

    :   Returns the list of all of the compute devices that are accessible.

        Returns[:]

        :   

            List\[MLComputeDevice\]

            :   The accessible compute devices.

        Examples

        :::: 
        ::: highlight
            compute_devices = (
                coremltools.models.compute_device.MLComputeDevice.get_all_compute_devices()
            )
        :::
        ::::

<!-- -->

*[class][ ]*[[coremltools.models.compute_device.]][[MLGPUComputeDevice]][(]*[[proxy]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_device.html#MLGPUComputeDevice)[](#coremltools.models.compute_device.MLGPUComputeDevice "Link to this definition")

:   Represents a GPU compute device.

<!-- -->

*[class][ ]*[[coremltools.models.compute_device.]][[MLNeuralEngineComputeDevice]][(]*[[proxy]]*[)][[[\[source\]]]](../_modules/coremltools/models/compute_device.html#MLNeuralEngineComputeDevice)[](#coremltools.models.compute_device.MLNeuralEngineComputeDevice "Link to this definition")

:   Represents a Neural Engine compute device.

    *[property][ ]*[[total_core_count]]*[[:]][ ][int]*[](#coremltools.models.compute_device.MLNeuralEngineComputeDevice.total_core_count "Link to this definition")

    :   Get the total number of cores in the Neural Engine.

        Returns[:]

        :   

            int

            :   The total number of cores in the Neural Engine.

        Examples

        :::: 
        ::: highlight
            compute_devices = (
                coremltools.models.compute_device.MLComputeDevice.get_all_compute_devices()
            )
            compute_devices = filter(
                lambda compute_device: isinstance(
                    compute_device, coremltools.models.compute_device.MLNeuralEngineComputeDevice
                ),
                compute_devices,
            )
            neural_engine_compute_device = next(compute_devices, None)
            neural_engine_core_count = (
                neural_engine_compute_device.total_core_count
                if neural_engine_compute_device is not None
                else 0
            )
        :::
        ::::

## experimental[](#experimental "Link to this heading")

### torch[](#torch "Link to this heading")

[]

#### debugging_utils[](#module-coremltools.models.ml_program.experimental.torch.debugging_utils "Link to this heading")

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[FrameInfo]][(]*[[filename]][[:]][ ][[str]]*, *[[lineno]][[:]][ ][[int]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#FrameInfo)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.FrameInfo "Link to this definition")

:   

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[TorchExportMLModelComparator]][(]*[[model]][[:]][ ][[ExportedProgram]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[target_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[converter_kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchExportMLModelComparator)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchExportMLModelComparator "Link to this definition")

:   Compares intermediate outputs between a PyTorch ExportedProgram and its converted Core ML model.

    This class facilitates the comparison of intermediate outputs from a PyTorch model and its corresponding Core ML conversion. It helps identify specific PyTorch operations that may produce divergent results in the converted model.

    [[\_\_init\_\_]][(]*[[model]][[:]][ ][[ExportedProgram]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[target_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[converter_kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchExportMLModelComparator.__init__)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchExportMLModelComparator.__init__ "Link to this definition")

    :   Initialize the TorchExportMLModelComparator.

        Parameters[:]

        :   

            **model**[torch.export.ExportedProgram]

            :   The ExportedProgram to be compared.

            **num_predict_intermediate_outputs**[int]

            :   The number of intermediate outputs to retrieve in each [`MLModel`] prediction call. Defaults to 20.

            **target_device**[Optional\[Device\]]

            :   The target device on which to run the Core ML model. If None, the current default device will be used.

            **\*\*converter_kwargs**[Any]

            :   Additional keyword arguments to be passed to the Core ML converter. These can include options like 'minimum_deployment_target', 'compute_units', etc., allowing for fine-tuning of the conversion process.

    *[async][ ]*[[find_failing_ops]][(]*[[inputs]][[:]][ ][[Tuple][[\[]][tensor][[\]]]]*, *[[compare_outputs]][[:]][ ][[Callable][[\[]][[\[]][Operation][[,]][ ][array][[,]][ ][array][[\]]][[,]][ ][bool][[\]]]]*, *[[output_nodes]][[:]][ ][[List][[\[]][Node][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[Iterable][[\[]][Node][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchExportMLModelComparator.find_failing_ops)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchExportMLModelComparator.find_failing_ops "Link to this definition")

    :   Identifies operations that produce different outputs in the reference and target models.

        This method compares the outputs of the source and target models for specified operations, identifying those that fail the comparison criteria.

        Parameters[:]

        :   

            **inputs: Tuple\[torch.tensor\]**

            :   Input data for the model.

            **compare_outputs**[Callable\[\[proto.MIL_pb2.Operation, np.array, np.array\], bool\])]

            :   A function to compare outputs of an operation between the two models.

            **outputs: Optional\[List\[torch.fx.Node\]\]**

            :   Specific outputs to compare. If None, all model outputs are compared. Defaults to None.

        Returns[:]

        :   

            List\[proto.MIL_pb2.Operation\]

            :   A list of operations that failed the comparison.

        Notes

        - The method uses a breadth-first search strategy to traverse the operation graph.

        - An operation is considered a failure source if it fails comparison while its direct inputs do not.

        Examples

        :::: 
        ::: highlight
            class Model(torch.nn.Module):
                def forward(self, x, y):
                    return x + y

            model = Model()
            input1 = torch.full((1, 10), 1, dtype=torch.float)
            input2 = torch.full((1, 10), 2, dtype=torch.float)
            inputs = (input1, input2)
            exported_program = torch.export.export(model, inputs)

            comparator = (
                coremltools.models.ml_program.experimental.torch.TorchExportMLModelComparator(
                    model=exported_program,
                    inputs=[
                        coremltools.TensorType(name="x", shape=inputs[0].shape, dtype=np.float16),
                        coremltools.TensorType(name="y", shape=inputs[1].shape, dtype=np.float16),
                    ],
                    minimum_deployment_target=coremltools.target.iOS16,
                    compute_units=coremltools.ComputeUnit.ALL,
                )
            )

            def compare_outputs(op, reference_output, target_output):
                return np.allclose(reference_output, target_output, atol=0.01)

            ops = await comparator.find_failing_ops(inputs=inputs, compare_outputs=compare_outputs)
        :::
        ::::

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[TorchNodeToMILOperationMapping]][(]*[[node_to_operations_map]][[:]][ ][[Dict][[\[]][[TorchScriptNodeInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo")[ ][[\|]][ ][Node][[,]][ ][List][[\[]][Operation][[\]]][[\]]]]*, *[[operation_output_name_to_node_map]][[:]][ ][[Dict][[\[]][str][[,]][ ][[TorchScriptNodeInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo")[ ][[\|]][ ][Node][[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchNodeToMILOperationMapping)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchNodeToMILOperationMapping "Link to this definition")

:   A class that represents the mapping between PyTorch nodes and MIL operations.

    [[get_source_nodes_for_operation]][(]*[[operation]][[:]][ ][[Operation]]*[)] [[→] [[List][[\[]][[TorchScriptNodeInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo")[ ][[\|]][ ][Node][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchNodeToMILOperationMapping.get_source_nodes_for_operation)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchNodeToMILOperationMapping.get_source_nodes_for_operation "Link to this definition")

    :   Retrieves the source node for a given MIL operation.

        Parameters[:]

        :   

            **operation**[proto.MIL_pb2.Operation]

            :   The MIL operation.

        Returns[:]

        :   

            Optional\[TorchNode\]

            :   The corresponding TorchNode if found, None otherwise.

    [[get_source_nodes_for_output_name]][(]*[[output_name]][[:]][ ][[str]]*[)] [[→] [[[TorchScriptNodeInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo")[ ][[\|]][ ][Node][ ][[\|]][ ][None]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchNodeToMILOperationMapping.get_source_nodes_for_output_name)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchNodeToMILOperationMapping.get_source_nodes_for_output_name "Link to this definition")

    :   Retrieves the source node for a given MIL operation's output name.

        Parameters[:]

        :   

            **output_name**[str]

            :   The name of the output.

        Returns[:]

        :   

            Optional\[TorchNode\]

            :   The corresponding TorchNode if found, None otherwise.

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[TorchScriptMLModelComparator]][(]*[[model]][[:]][ ][[Module]]*, *[[example_inputs]][[:]][ ][[Tuple][[\[]][tensor][[\]]]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[target_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[converter_kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptMLModelComparator)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptMLModelComparator "Link to this definition")

:   A class for comparing the the intermediate outputs of a torch model with its converted Core ML model.

    This class provides functionality to compare the intermediate outputs of a torch model and the converted Core ML model, helping to identify the torch modules that produce different results.

    [[\_\_init\_\_]][(]*[[model]][[:]][ ][[Module]]*, *[[example_inputs]][[:]][ ][[Tuple][[\[]][tensor][[\]]]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[target_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[converter_kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptMLModelComparator.__init__)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptMLModelComparator.__init__ "Link to this definition")

    :   Initialize the TorchScriptMLModelComparator.

        This constructor sets up the comparator by preparing both the PyTorch model and its Core ML counterpart for comparison. It traces the PyTorch model, converts it to a Core ML model, and initializes necessary attributes for the comparison process.

    *[async][ ]*[[find_failing_modules]][(]*[[inputs]][[:]][ ][[Tuple][[\[]][tensor][[\]]]]*, *[[compare_outputs]][[:]][ ][[Callable][[\[]][[\[]][Operation][[,]][ ][array][[,]][ ][array][[\]]][[,]][ ][bool][[\]]]]*, *[[source_module_keys]][[:]][ ][[List][[\[]][Tuple][[\[]][str][[,]][ ][int][[\]]][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[List][[\[]][[TorchScriptModuleMappingInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleMappingInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleMappingInfo")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptMLModelComparator.find_failing_modules)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptMLModelComparator.find_failing_modules "Link to this definition")

    :   Asynchronously finds failing operations in the converted model.

        This method compares the outputs of the source PyTorch model with the converted Core ML model to identify operations that produce different results.

        Parameters[:]

        :   

            **inputs**[Tuple\[torch.tensor\]]

            :   Input data for the models.

            **compare_outputs**[CompareOutputs]

            :   Function to compare outputs between models.

            **source_module_keys**[Optional\[List\[TorchScriptModuleInfo.Key\]\]]

            :   Specific module keys to check. Defaults to None (checks all modules).

        Returns[:]

        :   

            List\[TorchModuleMLModelMappingInfo\]

            :   A list of failing modules.

        Examples

        :::: 
        ::: highlight
            class Model(torch.nn.Module):
                def forward(self, x, y):
                    return x + y

            model = Model()
            input1 = torch.full((1, 10), 1, dtype=torch.float)
            input2 = torch.full((1, 10), 2, dtype=torch.float)
            example_inputs = (input1, input2)
            comparator = (
                coremltools.models.ml_program.experimental.torch.TorchScriptMLModelComparator(
                    model=model,
                    example_inputs=example_inputs,
                    inputs=[
                        coremltools.TensorType(name="x", shape=inputs[0].shape, dtype=np.float32),
                        coremltools.TensorType(name="y", shape=inputs[1].shape, dtype=np.float32),
                    ],
                    minimum_deployment_target=coremltools.target.iOS16,
                    compute_units=coremltools.ComputeUnit.ALL,
                )
            )

            def compare_outputs(module, reference_output, target_output):
                return np.allclose(reference_output, target_output, atol=0.01)

            modules = await comparator.find_failing_modules(
                inputs=example_inputs, compare_outputs=compare_outputs
            )
        :::
        ::::

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[TorchScriptModuleAnnotator]][(]*[[name_prefix]][[:]][ ][[str]][ ][[=]][ ][[\'var\']]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptModuleAnnotator)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator "Link to this definition")

:   A class for annotating the module graph.

    This class provides methods to annotate torch modules, track their call sequences, and analyze node dependencies within the graph.

    [[annotate_module]][(]*[[module]][[:]][ ][[ScriptModule]]*, *[[hierarchy]][[:]][ ][[Tuple][[\[]][str][[\]]]]*, *[[name]][[:]][ ][[str]]*, *[[graph]][[:]][ ][[Graph]]*[)] [[→] [[ContextManager]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptModuleAnnotator.annotate_module)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator.annotate_module "Link to this definition")

    :   Creates a context manager for annotating a module.

        Parameters[:]

        :   

            **hierarchy**[Tuple\[str\]]

            :   The hierarchical path of the module.

            **name**[str]

            :   The name of the module.

            **graph**[\_TorchGraph]

            :   The module graph.

        Returns[:]

        :   

            ContextManager

            :   A context manager for module annotation.

    [[enter_module]][(]*[[module]][[:]][ ][[ScriptModule]]*, *[[hierarchy]][[:]][ ][[List][[\[]][str][[\]]]]*, *[[name]][[:]][ ][[str]]*, *[[graph]][[:]][ ][[Graph]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptModuleAnnotator.enter_module)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator.enter_module "Link to this definition")

    :   Enters a module context and annotates its graph.

        Parameters[:]

        :   

            **hierarchy**[List\[str\]]

            :   The hierarchical path of the module.

            **name**[str]

            :   The name of the module.

            **graph**[\_TorchGraph]

            :   The module graph.

    [[exit_module]][(][)] [[→] [[None]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptModuleAnnotator.exit_module)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator.exit_module "Link to this definition")

    :   Exits a module context and finalizes annotations.

    *[property][ ]*[[module_call_stack]]*[[:]][ ][OrderedDict][[\[]][Tuple][[\[]][str][[,]][ ][int][[\]]][[,]][ ][[TorchScriptModuleInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleInfo")[[\]]]*[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator.module_call_stack "Link to this definition")

    :   Returns a copy of the module call stack.

    *[property][ ]*[[node_infos]]*[[:]][ ][OrderedDict][[\[]][str][[,]][ ][[TorchScriptNodeInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo")[[\]]]*[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator.node_infos "Link to this definition")

    :   Returns a copy of the node information dictionary.

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[TorchScriptModuleInfo]][(]*[[name]][[:]][ ][[str]]*, *[[call_sequence]][[:]][ ][[int]]*, *[[hierarchy]][[:]][ ][[Tuple][[\[]][str][[\]]]]*, *[[input_names]][[:]][ ][[Tuple][[\[]][str][[\]]]]*, *[[output_names]][[:]][ ][[Tuple][[\[]][str][[\]]]]*, *[[submodules]][[:]][ ][[Tuple][[\[]][Tuple][[\[]][str][[,]][ ][int][[\]]][[\]]]]*, *[[code]][[:]][ ][[str]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptModuleInfo)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleInfo "Link to this definition")

:   Represents information about a torch module.

    Attributes[:]

    :   

        **name**[str]

        :   

        **The name of the module.**

        :   

        **call_sequence**

        :   

        **The sequence number of this module call.**

        :   

        **hierarchy**[List\[str\]]

        :   

        **The hierarchical path of the module.**

        :   

        **output_names**[List\[str\]]

        :   

        **Names of the module's outputs.**

        :   

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[TorchScriptModuleMappingInfo]][(]*[source:] [\~coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleInfo,] [source_to_target_ops_mapping:] [\~collections.OrderedDict\[slice(\<class] [\'coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo\'\>,] [typing.List\[MIL_pb2.Operation\],] [None)\],] [deps:] [\~typing.Dict\[\~typing.Tuple\[str,] [int\],] [\~typing.Iterable\[\~coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleMappingInfo\]\],] [outputs:] [\~typing.List\[\~MIL_pb2.Operation\],] [submodules:] [\~typing.List\[\~coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleMappingInfo\]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptModuleMappingInfo)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleMappingInfo "Link to this definition")

:   A class that holds mapping information for a TorchScript module and its corresponding operations in the converted Core ML model.

    Attributes[:]

    :   

        **source**[TorchScriptModuleInfo]

        :   An instance representing the source module that is being mapped.

        **source_to_target_mapping**[OrderedDict\[TorchScriptNodeInfo, List\[proto.MIL_pb2.Operation\]\]]

        :   An ordered mapping from nodes in the source TorchScript module to a list of corresponding operations in Core ML. Each key represents a node in the module, while each value is a list of operations that correspond to that node in the target model.

        **deps**[Dict\[TorchScriptModuleInfo.Key, Iterable\[TorchScriptModuleInfo.Key\]\]:]

        :   A dictionary mapping each module to its immediate dependencies.

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[TorchScriptNodeInfo]][(]*[[source_range]][[:]][ ][[str]]*, *[[modules]][[:]][ ][[Tuple][[\[]][Tuple][[\[]][str][[,]][ ][int][[\]]][[\]]]]*, *[[desc]][[:]][ ][[str]]*, *[[kind]][[:]][ ][[str]]*, *[[input_names]][[:]][ ][[Tuple][[\[]][str][[\]]]]*, *[[output_names]][[:]][ ][[Tuple][[\[]][str][[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#TorchScriptNodeInfo)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "Link to this definition")

:   Represents information about a node in a torch graph.

    Attributes[:]

    :   

        **source_range**[str]

        :   

        **The node's source range.**

        :   

        **modules**[Iterable\["TorchScriptModuleInfo.Key"\]]

        :   

        **The modules to which this node belongs.**

        :   

        **input_names**[List\[str\]]

        :   

        **The input names.**

        :   

        **output_names**[List\[str\]]

        :   

        **The output names.**

        :   

<!-- -->

[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[convert_and_retrieve_op_mapping]][(]*[[model]][[:]][ ][[ExportedProgram][ ][[\|]][ ][ScriptModule]]*, *[[\*\*]][[converter_kwargs]]*[)] [[→] [[Tuple][[\[]][[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")[[,]][ ][[TorchNodeToMILOperationMapping]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchNodeToMILOperationMapping "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchNodeToMILOperationMapping")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#convert_and_retrieve_op_mapping)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.convert_and_retrieve_op_mapping "Link to this definition")

:   Converts a TorchScript model to a Core ML model and returns the mapping information mapping between the source TorchScript operations and their corresponding operations in the converted Core ML model.

    Parameters[:]

    :   

        **model**[ScriptModule or ExportedProgram]

        :   The source model.

        **\*\*converter_kwargs:**

        :   Additional keyword arguments to be passed to the Core ML conversion process. These can include options for optimization, input/output specifications, etc.

    Returns[:]

    :   

        Tuple\[MLModel, TorchNodeToMILOperationMapping\]

        :   

            A tuple containing:

            :   - The converted Core ML model.

                - A dictionary-like object mapping each TorchScript node from the original model to a list of corresponding MIL operations in the Core ML model. This mapping helps trace the origin of operations in the converted model back to the source model for debugging and analysis

    Examples

    :::: 
    ::: highlight
        (
            target_model,
            mapping_info,
        ) = coremltools.models.ml_program.experimental.torch.convert_and_retrieve_op_mapping(
            model=traced_model,  # ScriptModule or ExportedProgram
            inputs=[
                coremltools.TensorType(
                    name="x", shape=example_inputs[0].shape, dtype=np.float16
                ),
                coremltools.TensorType(
                    name="y", shape=example_inputs[1].shape, dtype=np.float16
                ),
            ],
            minimum_deployment_target=coremltools.target.iOS16,
            compute_units=coremltools.ComputeUnit.CPU_ONLY,
            skip_model_load=True,
        )
    :::
    ::::

<!-- -->

[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[get_stack_frame_infos]][(]*[[node]][[:]][ ][[[TorchScriptNodeInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo")[ ][[\|]][ ][Node]]*[)] [[→] [[List][[\[]][[FrameInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.FrameInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.FrameInfo")[[\]]][ ][[\|]][ ][None]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#get_stack_frame_infos)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.get_stack_frame_infos "Link to this definition")

:   Extracts frame infos from the node's source range.

    This method parses the stack trace of the node, attempts to extract the filename and line number using a regular expression.

<!-- -->

[[coremltools.models.ml_program.experimental.torch.debugging_utils.]][[inline_and_annotate_module]][(]*[[model]][[:]][ ][[ScriptModule]]*, *[[name_prefix]][[:]][ ][[str]][ ][[=]][ ][[\'var\']]*[)] [[→] [[[TorchScriptModuleAnnotator]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptModuleAnnotator")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/debugging_utils.html#inline_and_annotate_module)[](#coremltools.models.ml_program.experimental.torch.debugging_utils.inline_and_annotate_module "Link to this definition")

:   Inlines and annotates a TorchScript module.

    This function takes a TorchScript module and performs two operations:

    :   1\. Inlining: It inlines the module, which means it replaces calls to submodules with the actual operations performed by those submodules.

        2\. Annotation: It adds annotations to the module, providing additional information about the module's structure and operations.

    Parameters[:]

    :   

        **model**[ScriptModule]

        :   The TorchScript module to be inlined and annotated. This should be an instance of ScriptModule, which is a subclass of torch.nn.Module that has been scripted using torch.jit.script().

    Returns[:]

    :   

        TorchScriptModuleAnnotator

        :   An annotator object that contains the inlined and annotated version of the input module.

[]

#### perf_utils[](#module-coremltools.models.ml_program.experimental.torch.perf_utils "Link to this heading")

*[class][ ]*[[coremltools.models.ml_program.experimental.torch.perf_utils.]][[TorchMLModelBenchmarker]][(]*[[model]][[:]][ ][[ExportedProgram][ ][[\|]][ ][ScriptModule]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[\*\*]][[converter_kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/perf_utils.html#TorchMLModelBenchmarker)[](#coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker "Link to this definition")

:   A specialized benchmarker for PyTorch models.

    This class extends the [`MLModelBenchmarker`] to provide benchmarking capabilities specifically tailored for PyTorch model. It inherits all the functionality of [`MLModelBenchmarker`] and includes methods to provide estimated execution times for torch nodes and submodules.

    *[class][ ]*[[ModuleExecutionInfo]][(]*[[name]][[:]][ ][[str]]*, *[[ops]][[:]][ ][[List][[\[]][ForwardRef][[(]][[\'TorchMLModelBenchmarker.NodeExecutionInfo\']][[)]][[\]]]]*, *[[measurement]][[:]][ ][[ForwardRef][[(]][[\'MLModelBenchmarker.Measurement\']][[)]][ ][[\|]][ ][None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/perf_utils.html#TorchMLModelBenchmarker.ModuleExecutionInfo)[](#coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.ModuleExecutionInfo "Link to this definition")

    :   

    *[class][ ]*[[NodeExecutionInfo]][(]*[[node]][[:]][ ][[[coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo]](#coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo "coremltools.models.ml_program.experimental.torch.debugging_utils.TorchScriptNodeInfo")[ ][[\|]][ ][torch.fx.node.Node]]*, *[[targets]][[:]][ ][[List][[\[]][[coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.OperationExecutionInfo]](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.OperationExecutionInfo "coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.OperationExecutionInfo")[[\]]]]*, *[[measurement]][[:]][ ][[ForwardRef][[(]][[\'MLModelBenchmarker.Measurement\']][[)]][ ][[\|]][ ][None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/perf_utils.html#TorchMLModelBenchmarker.NodeExecutionInfo)[](#coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.NodeExecutionInfo "Link to this definition")

    :   

    *[async][ ]*[[benchmark_module_execution]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[iterations]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[warmup]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[List][[\[]][[ModuleExecutionInfo]](#coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.ModuleExecutionInfo "coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.ModuleExecutionInfo")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/perf_utils.html#TorchMLModelBenchmarker.benchmark_module_execution)[](#coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.benchmark_module_execution "Link to this definition")

    :   Measures the execution time of modules in the PyTorch model.

        This method loads the converted model, runs predictions, and retrieves the execution time of each operation within the model.

        Parameters[:]

        :   

            **inputs**[Optional\[Dict\[str, Any\]\]]

            :   The input data for the model prediction. If None, random input data will be generated.

            **iterations: int**

            :   The number of prediction iterations to run. Defaults to 1.

            **warmup: bool**

            :   Whether to perform a warmup iteration. Defaults to False.

        Returns[:]

        :   

            List\[TorchModuleExecutionInfo\]

            :   A list of [`TorchModuleExecutionInfo`] objects, each containing details about an modules's execution, sorted by execution time in descending order.

        Notes

        - The returned list is sorted by execution time, with the most time-consuming operations first.

        - Execution times are estimated based on the overall prediction time and the converted model's compute plan.

    *[async][ ]*[[benchmark_node_execution]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[iterations]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[warmup]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[List][[\[]][[NodeExecutionInfo]](#coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.NodeExecutionInfo "coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.NodeExecutionInfo")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/torch/perf_utils.html#TorchMLModelBenchmarker.benchmark_node_execution)[](#coremltools.models.ml_program.experimental.torch.perf_utils.TorchMLModelBenchmarker.benchmark_node_execution "Link to this definition")

    :   Measures the execution time of individual nodes in the PyTorch model.

        This method loads the converted model, runs predictions, and retrieves the execution time of each operation within the model.

        Parameters[:]

        :   

            **inputs**[Optional\[Dict\[str, Any\]\]]

            :   The input data for the model prediction. If None, random input data will be generated.

            **iterations: int**

            :   The number of prediction iterations to run. Defaults to 1.

            **warmup: bool**

            :   Whether to perform a warmup iteration. Defaults to False.

        Returns[:]

        :   

            List\[TorchNodeExecutionInfo\]

            :   A list of TorchNodeExecutionInfo objects, each containing details about an node's execution, sorted by execution time in descending order.

        Notes

        - The returned list is sorted by execution time, with the most time-consuming operations first.

        - Execution times are estimated based on the overall prediction time and the converted model's compute plan.

[]

### remote_device[](#module-coremltools.models.ml_program.experimental.remote_device "Link to this heading")

*[class][ ]*[[coremltools.models.ml_program.experimental.remote_device.]][[AppSigningCredentials]][(]*[[development_team]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[\'\']]*, *[[provisioning_profile_uuid]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[bundle_identifier]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#AppSigningCredentials)[](#coremltools.models.ml_program.experimental.remote_device.AppSigningCredentials "Link to this definition")

:   Represents the credentials required for signing an iOS application.

    This class encapsulates the essential information needed for code signing an iOS app, including the development team identifier and optionally the bundle identifier.

    Attributes[:]

    :   

        **development_team**[Optional\[str\]]

        :   The development team identifier associated with the Apple Developer account.

        **provisioning_profile_uuid**[Optional\[str\]]

        :   The UUID of the provisioning profile. This is used to specify which provisioning profile should be applied during the code-signing process.

        **bundle_identifier**[Optional\[str\]]

        :   The bundle identifier for the application. This is an optional parameter that, if provided, should be in the format of a reverse domain name (e.g., "com.example.app"). If None, the bundle identifier from the project's settings will be used.

    Notes

    Either [`provisioning_profile_uuid`] or [`development_team`] must be provided:

    :   - If [`provisioning_profile_uuid`] is provided, then [`bundle_identifier`] must match the one defined in the provisioning profile.

        - If [`development_team`] is provided, Xcode will automatically create and manage a provisioning profile during the build process.

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.remote_device.]][[ComputePlan]][(]*[[infos]][[:]][ ][[Dict][[\[]][[coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath")[[,]][ ][ForwardRef][[(]][[\'ComputePlan.OperationOrLayerInfo\']][[)]][[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#ComputePlan)[](#coremltools.models.ml_program.experimental.remote_device.ComputePlan "Link to this definition")

:   

    *[class][ ]*[[CPUDevice]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#ComputePlan.CPUDevice)[](#coremltools.models.ml_program.experimental.remote_device.ComputePlan.CPUDevice "Link to this definition")

    :   

    *[class][ ]*[[DeviceUsage]][(]*[[preferred]][[:]][ ][[[\'ComputePlan.Device\']]]*, *[[supported]][[:]][ ][[List][[\[]][ForwardRef][[(]][[\'ComputePlan.Device\']][[)]][[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#ComputePlan.DeviceUsage)[](#coremltools.models.ml_program.experimental.remote_device.ComputePlan.DeviceUsage "Link to this definition")

    :   

    *[class][ ]*[[GPUDevice]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#ComputePlan.GPUDevice)[](#coremltools.models.ml_program.experimental.remote_device.ComputePlan.GPUDevice "Link to this definition")

    :   

    *[class][ ]*[[NeuralEngineDevice]][(]*[[total_core_count]][[:]][ ][[int]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#ComputePlan.NeuralEngineDevice)[](#coremltools.models.ml_program.experimental.remote_device.ComputePlan.NeuralEngineDevice "Link to this definition")

    :   

    *[class][ ]*[[OperationOrLayerInfo]][(]*[[device_usage]][[:]][ ][[[\'ComputePlan.DeviceUsage\']]]*, *[[estimated_cost]][[:]][ ][[float][ ][[\|]][ ][None]]*, *[[path]][[:]][ ][[[coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath")]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#ComputePlan.OperationOrLayerInfo)[](#coremltools.models.ml_program.experimental.remote_device.ComputePlan.OperationOrLayerInfo "Link to this definition")

    :   

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.remote_device.]][[Device]][(]*[[name]][[:]][ ][[str]]*, *[[type]][[:]][ ][[[DeviceType]](#coremltools.models.ml_program.experimental.remote_device.DeviceType "coremltools.models.ml_program.experimental.remote_device.DeviceType")]*, *[[identifier]][[:]][ ][[str]]*, *[[udid]][[:]][ ][[str]]*, *[[os_version]][[:]][ ][[str]]*, *[[os_build_number]][[:]][ ][[str]]*, *[[developer_mode_state]][[:]][ ][[str]]*, *[[state]][[:]][ ][[[DeviceState]](#coremltools.models.ml_program.experimental.remote_device.DeviceState "coremltools.models.ml_program.experimental.remote_device.DeviceState")]*, *[[session]][[:]][ ][[Type][[\[]][\_AppSession][[\]]][ ][[\|]][ ][None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#Device)[](#coremltools.models.ml_program.experimental.remote_device.Device "Link to this definition")

:   Represents a device.

    Attributes[:]

    :   

        **name**[str]

        :   The name of the device.

        **type**[DeviceType]

        :   The type of the device.

        **identifier**[str]

        :   A unique identifier for the device.

        **udid**[str]

        :   The device identifier.

        **os_version**[str]

        :   The operating system version of the device.

        **os_build_number**[str]

        :   The build number of the os.

        **developer_mode_state**[str]

        :   The state of developer mode on the device.

    *[static][ ]*[[get_connected_devices]][(]*[[device_type]][[:]][ ][[[DeviceType]](#coremltools.models.ml_program.experimental.remote_device.DeviceType "coremltools.models.ml_program.experimental.remote_device.DeviceType")]*[)] [[→] [[List][[\[]][Type][[\[]][[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[[\]]][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#Device.get_connected_devices)[](#coremltools.models.ml_program.experimental.remote_device.Device.get_connected_devices "Link to this definition")

    :   Retrieve a list of connected devices of a specified type.

        This function uses the DeviceCtl utility to fetch all accessible devices and filters them based on the following criteria: 1. The device is in a connected state 2. The device matches the specified device_type

        Parameters[:]

        :   

            **device_type**[DeviceType]

            :   The type of device to filter for (e.g., iPhone, iPad, Apple TV).

        Returns[:]

        :   

            List\[Device\]

            :   

    *[static][ ]*[[get_devices]][(][)] [[→] [[List][[\[]][Type][[\[]][[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[[\]]][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#Device.get_devices)[](#coremltools.models.ml_program.experimental.remote_device.Device.get_devices "Link to this definition")

    :   Retrieve a list of available devices.

        This method fetches and returns a list of all accessible devices using the DeviceCtl utility.

        Returns[:]

        :   

            List\[Device\]

            :   A list of Device objects representing the available devices.

    *[async][ ]*[[prepare_for_model_debugging]][(]*[[credentials]][[:]][ ][[[AppSigningCredentials]](#coremltools.models.ml_program.experimental.remote_device.AppSigningCredentials "coremltools.models.ml_program.experimental.remote_device.AppSigningCredentials")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[working_directory]][[:]][ ][[Path][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[clean]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[Type][[\[]][[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#Device.prepare_for_model_debugging)[](#coremltools.models.ml_program.experimental.remote_device.Device.prepare_for_model_debugging "Link to this definition")

    :   Prepares the device for model debugging by building and launching the model runner app.

        This method checks if the device is in the correct state for debugging, sets up the working directory, builds the [`modelrunner`] application, and launches it on the device.

        Parameters[:]

        :   

            **credentials**[Optional\[AppSigningCredentials]

            :   The credentials required for signing [`modelrunner`] application.

            **working_directory: Optional\[Path\]**

            :   The directory utilized for storing files required for building and communicating with the [`modelrunner`] application. If None, a temporary director will be created. Defaults to None.

            **clean**[bool]

            :   If True, performs a clean build. Defaults to False.

        Returns[:]

        :   

            Device

            :   A new Device instance with the prepared session.

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.remote_device.]][[DeviceState]][(]*[[value]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#DeviceState)[](#coremltools.models.ml_program.experimental.remote_device.DeviceState "Link to this definition")

:   Enumeration of device states.

    Attributes[:]

    :   

        **CONNECTING**[str]

        :   The device is connecting.

        **CONNECTED**[str]

        :   The device is connected.

        **AVAILABLE**[str]

        :   The device is available for use.

        **UNAVAILABLE**[str]

        :   The device is not available for use.

        **DISCONNECTED :str**

        :   The device is disconnected.

        **UNKNOWN**[str]

        :   Represents an unknown device state.

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.remote_device.]][[DeviceType]][(]*[[value]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/remote_device.html#DeviceType)[](#coremltools.models.ml_program.experimental.remote_device.DeviceType "Link to this definition")

:   Enumeration of device types.

    Attributes[:]

    :   

        **MAC**[str]

        :   Represents a Mac device.

        **IPHONE**[str]

        :   Represents an iPhone device.

        **IPAD**[str]

        :   Represents an iPad device

        **APPLETV**[str]

        :   Represents an Apple TV device.

        **WATCH**[str]

        :   Represents an Apple Watch device.

        **HOMEPOD**[str]

        :   Represents a HomePod device.

        **UNKNOWN**[str]

        :   Represents an unknown device type.

### debugging_utils[](#id1 "Link to this heading")

[]

*[class][ ]*[[coremltools.models.ml_program.experimental.debugging_utils.]][[MLModelComparator]][(]*[[reference_model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[target_model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[reference_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[target_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelComparator)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelComparator "Link to this definition")

:   A class for comparing two MLModel objects and identifying discrepancies in their outputs.

    This class provides functionality to compare the outputs of a reference model and a target model, helping to identify operations that produce different results.

    The ModelComparator is designed to compare models derived from the same source. Using it with reference and target models originating from different sources may lead to unreliable or meaningless results.

    Examples

    :::: 
    ::: highlight
        # Load the reference and target models
        reference_model = coremltools.models.MLModel(
            "model.mlpackage", compute_unit=coremltools.ComputeUnit.CPU_ONLY
        )
        target_model = coremltools.models.MLModel(
            "model.mlpackage", compute_unit=coremltools.ComputeUnit.CPU_AND_GPU
        )
        # Create an instance of MLModelComparator
        comparator = (
            coremltools.models.ml_program.experimental.debugging_utils.MLModelComparator(
                reference_model, target_model
            )
        )
        # Prepare input data
        input_data = 
        # Find failing operations with a PSNR of less than 40.
        failing_ops = await comparator.find_failing_ops(
            inputs=input_data, compare_output=lambda x, y: compute_snr_and_psnr(x, y)[1] >= 40.0
        )
    :::
    ::::

    [[\_\_init\_\_]][(]*[[reference_model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[target_model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[reference_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[target_device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelComparator.__init__)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelComparator.__init__ "Link to this definition")

    :   Initializes the MLModelComparator.

        Parameters[:]

        :   

            **reference_model**[MLModel]

            :   The reference MLModel.

            **target_model**[MLModel]

            :   The target MLModel to compare against the reference.

            **function_name**[Optional\[str\]]

            :   The function name. Defaults to the model's function name.

            **optimization_hints**[Optional\[Dict\[str, Any\]\]]

            :   Keys are the names of the optimization hint, either 'reshapeFrequency' or 'specializationStrategy'. Values are enumeration values of type [`coremltools.ReshapeFrequency`] or [`coremltools.SpecializationStrategy`].

            **num_predict_intermediate_outputs**[int]

            :   The number of intermediate outputs to retrieve in each [`MLModel`] prediction call. Defaults to 20.

            **reference_device: Device**

            :   The device on which the reference model will execute.

            **target_device: Device**

            :   The device on which the target model will execute.

    *[async][ ]*[[find_failing_ops]][(]*[inputs:] [\~typing.Dict\[str,] [\~numpy.array\],] [compare_outputs:] [\~typing.Callable\[\[\~MIL_pb2.Operation,] [\~numpy.array,] [\~numpy.array\],] [bool\],] [output_names:] [\~typing.List\[str\]] [\|] [None] [=] [None,] [skip_op:] [\~typing.Callable\[\[\~MIL_pb2.Operation\],] [bool\]] [=] [\<function] [skip_op_by_type\>]*[)] [[→] [[List][[\[]][Operation][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelComparator.find_failing_ops)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelComparator.find_failing_ops "Link to this definition")

    :   Identifies operations that produce different outputs in the reference and target models.

        This method compares the outputs of the reference and target models for specified operations, identifying those that fail the comparison criteria.

        Parameters[:]

        :   

            **inputs**[Dict\[str, np.array\]]

            :   Input data for the models.

            **compare_outputs**[Callable\[\[proto.MIL_pb2.Operation, np.array, np.array\], bool\])]

            :   A function to compare outputs of an operation between the two models.

            **output_names**[Optional\[List\[str\]\], optional)]

            :   Names of specific outputs to compare. If None, all model outputs are compared. Defaults to None.

            **skip_op: Callable\[\[proto.MIL_pb2.Operation\], bool\]**

            :   A function that determines if an operation should be skipped.

        Returns[:]

        :   

            List\[proto.MIL_pb2.Operation\]

            :   A list of operations that failed the comparison.

        Notes

        - The method uses a breadth-first search strategy to traverse the operation graph.

        - An operation is considered a failure source if it fails comparison while its direct inputs do not.

        Examples

        :::: 
        ::: highlight
            # Load the reference and target models
            reference_model = coremltools.models.MLModel(
                "model.mlpackage", compute_unit=coremltools.ComputeUnit.CPU_ONLY
            )
            target_model = coremltools.models.MLModel(
                "model.mlpackage", compute_unit=coremltools.ComputeUnit.CPU_AND_GPU
            )
            # Create an instance of MLModelComparator
            comparator = (
                coremltools.models.ml_program.experimental.debugging_utils.MLModelComparator(
                    reference_model, target_model
                )
            )
            # Prepare input data
            input_data = 

            # Define a custom comparison function
            def compare_outputs(op, reference_output, target_output):
                return np.allclose(reference_output, target_output, rtol=1e-3, atol=1e-3)

            # Find failing operations
            failing_ops = await comparator.find_failing_ops(
                inputs=input_data, compare_outputs=compare_outputs
            )
        :::
        ::::

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.debugging_utils.]][[MLModelInspector]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[compute_units]][[:]][ ][[ComputeUnit][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelInspector)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector "Link to this definition")

:   A class for inspecting an ML model.

    This class provides functionality to retrieve intermediate outputs of an ML model.

    Examples

    :::: 
    ::: highlight
        inspector = coremltools_internal.models.debugging_utils.MLModelInspector(model)
        input_data = 
        # The intermediate outputs we want to inspect
        output_names = ["conv1_output", "relu1_output", "pool1_output"]
        async for output_name, output_value in inspector.inspect(
            inputs=input_data, output_names=output_names
        ):
            print(f"Name: ")
            print(f"Output: ")
    :::
    ::::

    [[\_\_init\_\_]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[compute_units]][[:]][ ][[ComputeUnit][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelInspector.__init__)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector.__init__ "Link to this definition")

    :   Initializes the MLModelInspector.

        Parameters[:]

        :   

            **model**[MLModel]

            :   The MLModel to inspect.

            **compute_units**[coremltools.ComputeUnit]

            :   The compute units to use. Defaults to the model's compute unit.

            **function_name**[Optional\[str\]]

            :   The function name. Defaults to the model's function name.

            **optimization_hints**[Optional\[Dict\[str, Any\]\]]

            :   Keys are the names of the optimization hint, either 'reshapeFrequency' or 'specializationStrategy'. Values are enumeration values of type [`coremltools.ReshapeFrequency`] or [`coremltools.SpecializationStrategy`].

            **device: Device**

            :   The device on which the model will execute.

    [[clear_cached_models]][(][)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelInspector.clear_cached_models)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector.clear_cached_models "Link to this definition")

    :   Clears the cache of generated models.

    *[async][ ]*[[inspect]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][array][[\]]]]*, *[[output_names]][[:]][ ][[List][[\[]][str][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[ignore_const_ops]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[AsyncIterator][[\[]][Tuple][[\[]][str][[,]][ ][array][ ][[\|]][ ][None][[\]]][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelInspector.inspect)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector.inspect "Link to this definition")

    :   Retrieves intermediate outputs from the model for given inputs.

        Parameters[:]

        :   

            **inputs**[Dict\[str, np.array\]]

            :   Input data for the model.

            **output_names**[List\[str\]]

            :   Names of outputs to retrieve. Defaults to all outputs.

            **num_predict_intermediate_outputs**[Optional\[int\]]

            :   The number of intermediate outputs to retrieve in each [`MLModel`] prediction call. Defaults to None.

            **ignore_const_ops**[bool]

            :   Whether to ignore constant operations. Defaults to True.

        Returns[:]

        :   

            AsyncIterator\[Tuple\[str, Optional\[np.array\]\]\]

            :   An iterator of tuples containing output names and their values.

        Yields[:]

        :   

            Tuple\[str, Optional\[np.array\]\]

            :   A tuple of (output_name, output_value) for each requested output.

        Examples

        :::: 
        ::: highlight
            inspector = coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector(
                model
            )
            input_data = 
            # The intermediate outputs we want to inspect
            output_names = ["conv1_output", "relu1_output", "pool1_output"]
            async for output_name, output_value in inspector.inspect(
                inputs=input_data, output_names=output_names
            ):
                print(f"Name: ")
                print(f"Output: ")
        :::
        ::::

    *[property][ ]*[[output_name_to_op_map]]*[[:]][ ][OrderedDict][[\[]][str][[,]][ ][Operation][[\]]]*[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector.output_name_to_op_map "Link to this definition")

    :   Returns a dictionary mapping output names to their corresponding operations.

        Returns[:]

        :   

            Dict\[str, proto.MIL_pb2.Operation\]

            :   A dictionary of output names to operations.

    *[property][ ]*[[output_names]]*[[:]][ ][List][[\[]][str][[\]]]*[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector.output_names "Link to this definition")

    :   Returns a list of all output names in the model.

        Returns[:]

        :   

            List\[str\]

            :   A list of output names.

    *[async][ ]*[[retrieve_outputs]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][array][[\]]]]*, *[[output_names]][[:]][ ][[List][[\[]][str][[\]]]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[ignore_const_ops]][[:]][ ][[bool]][ ][[=]][ ][[True]]*[)] [[→] [[Dict][[\[]][str][[,]][ ][array][ ][[\|]][ ][None][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelInspector.retrieve_outputs)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector.retrieve_outputs "Link to this definition")

    :   Asynchronously retrieve intermediate outputs for the specified output names and inputs.

        This method inspects the model with given inputs and collects the intermediate outputs for the specified output names.

        Parameters[:]

        :   

            **output_names**[List\[str\]]

            :   Names of intermediate outputs to retrieve.

            **inputs**[Dict\[str, np.ndarray\])]

            :   Input data for the model.

            **num_predict_intermediate_outputs**[Optional\[int\]]

            :   The number of intermediate outputs to retrieve in each [`MLModel`] prediction call. Defaults to None.

            **ignore_const_ops**[bool]

            :   Whether to ignore constant operations. Defaults to True.

        Returns[:]

        :   

            Dict\[str, Optional\[np.array\]\]

            :   A dictionary mapping output names to their corresponding numpy array values. If an output is not available, its value will be None.

        Examples

        :::: 
        ::: highlight
            inspector = coremltools.models.ml_program.experimental.debugging_utils.MLModelInspector(
                model
            )
            input_data = 
            # The intermediate outputs we want to retrieve
            outputs = await inspector.retrieve_outputs(
                inputs=inputs,
                output_names=["conv1_output", "relu1_output", "pool1_output"],
            )

            for output_name, output_value in outputs.items():
                print(f"Name: ")
                print(f"Output: ")
        :::
        ::::

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.debugging_utils.]][[MLModelValidator]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[compute_units]][[:]][ ][[ComputeUnit][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelValidator)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator "Link to this definition")

:   A validator class for diagnosing numerical issues in an ML model.

    This class provides methods to traverse and validate operations within an ML model, specifically focusing on detecting issues such as NaN (Not a Number) or infinite outputs. It uses a graph traversal approach to identify the source of numerical instabilities.

    Examples

    :::: 
    ::: highlight
        validator = coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator(
            model
        )
        failing_ops = validator.find_failing_ops(
            inputs=,
            validate_output=lambda op, out: np.isnan(out).any(),
            output_names=["output1", "output2"],
        )
    :::
    ::::

    [[\_\_init\_\_]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[compute_units]][[:]][ ][[ComputeUnit][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[num_predict_intermediate_outputs]][[:]][ ][[int]][ ][[=]][ ][[20]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelValidator.__init__)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator.__init__ "Link to this definition")

    :   Initializes the MLModelValidator.

        Parameters[:]

        :   

            **model**[MLModel]

            :   The model to be validated.

            **function_name**[Optional\[str\]]

            :   The function name. Defaults to the model's function name.

            **compute_units**[coremltools.ComputeUnit:]

            :   The compute units to use. Defaults to the model's compute unit.

            **optimization_hints**[Optional\[Dict\[str, Any\]\]]

            :   Keys are the names of the optimization hint, either 'reshapeFrequency' or 'specializationStrategy'. Values are enumeration values of type [`coremltools.ReshapeFrequency`] or [`coremltools.SpecializationStrategy`].

            **num_predict_intermediate_outputs**[int]

            :   The number of intermediate outputs to retrieve in each [`MLModel`] prediction call. Defaults to 20.

            **device: Device**

            :   The device on which the model will execute.

    *[async][ ]*[[find_failing_ops]][(]*[inputs:] [\~typing.Dict\[str,] [\~numpy.array\],] [validate_output:] [\~typing.Callable\[\[\~MIL_pb2.Operation,] [\~numpy.array\],] [bool\],] [output_names:] [\~typing.List\[str\]] [\|] [None] [=] [None,] [skip_op:] [\~typing.Callable\[\[\~MIL_pb2.Operation\],] [bool\]] [=] [\<function] [skip_op_by_type\>]*[)] [[→] [[List][[\[]][Operation][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelValidator.find_failing_ops)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator.find_failing_ops "Link to this definition")

    :   Identify operations in the model that fail the specified validation criteria.

        This method traverses the model's operation graph, starting from the specified output operations, and applies the given validation function to each operation's output. It returns a list of operations that are likely the source of failures.

        Parameters[:]

        :   

            **inputs**[Dict\[str, np.array\]]

            :   A dictionary of input tensors for the model. Keys are input names, and values are numpy arrays.

            **validate_output**[Callable\[\[proto.MIL_pb2.Operation, np.array\], bool\]]

            :   A function that takes an operation and its output array, and returns False if the output fails the validation criteria, True otherwise.

            **output_names**[Optional\[List\[str\]\]]

            :   A list of specific output names to start the traversal from. If None, all model outputs are used.

            **skip_op: Callable\[\[proto.MIL_pb2.Operation\], bool\]**

            :   A function that determines if an operation should be skipped.

        Returns[:]

        :   

            List\[proto.MIL_pb2.Operation\]:

            :   A list of operations that are identified as likely sources of failure based on the validation criteria.

        Notes

        - The method uses a breadth-first search strategy to traverse the operation graph.

        - An operation is considered a failure source if it fails validation, but its direct inputs pass.

        Examples

        :::: 
        ::: highlight
            validator = coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator(
                model
            )
            failing_ops = await validator.find_failing_ops(
                inputs=,
                validate_output=lambda op, out: not np.isnan(out).any(),
                output_names=["output1", "output2"],
            )
        :::
        ::::

    *[async][ ]*[[find_failing_ops_with_infinite_output]][(]*[inputs:] [\~typing.Dict\[str,] [\~numpy.array\],] [output_names:] [\~typing.List\[str\]] [\|] [None] [=] [None,] [skip_op:] [\~typing.Callable\[\[\~MIL_pb2.Operation\],] [bool\]] [=] [\<function] [skip_op_by_type\>]*[)] [[→] [[List][[\[]][Operation][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelValidator.find_failing_ops_with_infinite_output)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator.find_failing_ops_with_infinite_output "Link to this definition")

    :   Identify operations in the model that produce infinite outputs.

        This method traverses the model's operation graph and checks for infinite values in the output of each operation. It returns a list of operations that are likely the source of failures. It's useful for debugging numerical instability issues in the model.

        Parameters[:]

        :   

            **inputs**[dict\[str, np.array\]]

            :   A dictionary of input tensors for the model. Keys are input names, and values are numpy arrays.

            **output_names**[Optional\[List\[str\]\]]

            :   A list of specific output names to start the traversal from. If None, all model outputs are used.

            **skip_op: Callable\[\[proto.MIL_pb2.Operation\], bool\]**

            :   A function that determines if an operation should be skipped.

        Returns[:]

        :   

            List\[proto.MIL_pb2.Operation\]

            :   A list of operations that are identified as likely sources of failure.

        Notes

        - The method uses a breadth-first search strategy to traverse the operation graph.

        - An operation is considered a failure source if it outputs infinite values while its direct inputs do not.

        Examples

        :::: 
        ::: highlight
            validator = coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator(
                model
            )
            failing_ops = await validator.find_failing_ops_with_infinite_output(
                inputs=, output_names=["output1", "output2"]
            )
        :::
        ::::

    *[async][ ]*[[find_failing_ops_with_nan_output]][(]*[inputs:] [\~typing.Dict\[str,] [\~numpy.array\],] [output_names:] [\~typing.List\[str\]] [\|] [None] [=] [None,] [skip_op:] [\~typing.Callable\[\[\~MIL_pb2.Operation\],] [bool\]] [=] [\<function] [skip_op_by_type\>]*[)] [[→] [[List][[\[]][Operation][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#MLModelValidator.find_failing_ops_with_nan_output)[](#coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator.find_failing_ops_with_nan_output "Link to this definition")

    :   Identify operations in the model that produce NaN (Not a Number) outputs.

        This method traverses the model's operation graph and checks for NaN values in the output of each operation. It returns a list of operations that are likely the source of failures. It's useful for debugging numerical instability issues in the model.

        Parameters[:]

        :   

            **inputs**[Dict\[str, np.array\]]

            :   A dictionary of input tensors for the model. Keys are input names, and values are numpy arrays.

            **output_names**[Optional\[List\[str\]\]]

            :   A list of specific output names to start the traversal from. If None, all model outputs are used.

            **skip_op: Callable\[\[proto.MIL_pb2.Operation\], bool\]**

            :   A function that determines if an operation should be skipped.

        Returns[:]

        :   

            List\[proto.MIL_pb2.Operation\]

            :   A list of operations that are identified as likely sources of failure.

        Notes

        - The method uses a breadth-first search strategy to traverse the operation graph.

        - An operation is considered a failure source if it outputs NaN while its direct inputs do not.

        Examples

        :::: 
        ::: highlight
            validator = coremltools.models.ml_program.experimental.debugging_utils.MLModelValidator(
                model
            )
            failing_ops = await validator.find_failing_ops_with_nan_output(
                inputs=, output_names=["output1", "output2"]
            )
        :::
        ::::

<!-- -->

[[coremltools.models.ml_program.experimental.debugging_utils.]][[compute_snr_and_psnr]][(]*[[x]][[:]][ ][[array]]*, *[[y]][[:]][ ][[array]]*[)] [[→] [[Tuple][[\[]][float][[,]][ ][float][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#compute_snr_and_psnr)[](#coremltools.models.ml_program.experimental.debugging_utils.compute_snr_and_psnr "Link to this definition")

:   Compute the Signal-to-Noise Ratio (SNR) and Peak Signal-to-Noise Ratio (PSNR) between two signals.

    This function calculates the SNR and PSNR between two input signals, typically used to compare an original signal (y) with a processed or noisy version of that signal (x).

    Parameters[:]

    :   

        **x**[np.array]

        :   The processed or noisy signal.

        **y**[np.array]

        :   The original or reference signal.

    Returns[:]

    :   

        Tuple\[float, float\]

        :   

            A tuple containing two float values:

            :   - snr (float): The Signal-to-Noise Ratio in decibels (dB).

                - psnr (float): The Peak Signal-to-Noise Ratio in decibels (dB).

    Raises[:]

    :   

        AssertionError: If the lengths of x and y are not equal.

        :   

    Examples

    :::: 
    ::: highlight
        original = np.array([1, 2, 3, 4, 5])
        noisy = np.array([1.1, 2.1, 2.9, 4.2, 5.1])
        snr, psnr = compute_snr_and_psnr(noisy, original)
        print(f"SNR:  dB, PSNR:  dB")
    :::
    ::::

<!-- -->

[[coremltools.models.ml_program.experimental.debugging_utils.]][[skip_op_by_type]][(]*[[op]][[:]][ ][[Operation]]*, *[[op_types]][[:]][ ][[Iterable][[\[]][str][[\]]]][ ][[=]][ ][[ [\'compression.constexpr_blockwise_shift_scale\',] [\'concat\',] [\'const\',] [\'constexpr_affine_dequantize\',] [\'constexpr_cast\',] [\'constexpr_lut_to_dense\',] [\'constexpr_lut_to_sparse\',] [\'constexpr_sparse_to_dense\',] [\'expand_dims\',] [\'fill\',] [\'reshape\',] [\'reshape_like\',] [\'shape\',] [\'slice_by_index\',] [\'slice_by_size\',] [\'split\',] [\'squeeze\',] [\'stack\',] [\'transpose\'}]]*[)] [[→] [[bool]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/debugging_utils.html#skip_op_by_type)[](#coremltools.models.ml_program.experimental.debugging_utils.skip_op_by_type "Link to this definition")

:   Determines if an operation should be skipped based on its type.

### perf_utils[](#id2 "Link to this heading")

[]

*[class][ ]*[[coremltools.models.ml_program.experimental.perf_utils.]][[MLModelBenchmarker]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/perf_utils.html#MLModelBenchmarker)[](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker "Link to this definition")

:   A class for benchmarking an MLModel.

    This class provides functionality to measure and analyze the performance of an MLModel, including loading time, prediction time, and individual operation execution times.

    *[class][ ]*[[Measurement]][(]*[[statistics]][[:]][ ][[ForwardRef][[(]][[\'MLModelBenchmarker.Statistics\']][[)]][ ][[\|]][ ][None]]*, *[[samples]][[:]][ ][[List][[\[]][float][[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/perf_utils.html#MLModelBenchmarker.Measurement)[](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.Measurement "Link to this definition")

    :   

    *[class][ ]*[[OperationExecutionInfo]][(]*[[spec]][[:]][ ][[MIL_pb2.Operation]]*, *[[path]][[:]][ ][[[coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath")]*, *[[compute_device_usage]][[:]][ ][[[coremltools.models.compute_plan.MLComputePlanDeviceUsage]](#coremltools.models.compute_plan.MLComputePlanDeviceUsage "coremltools.models.compute_plan.MLComputePlanDeviceUsage")[ ][[\|]][ ][None]]*, *[[measurement]][[:]][ ][[[\'MLModelBenchmarker.Measurement\']]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/perf_utils.html#MLModelBenchmarker.OperationExecutionInfo)[](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.OperationExecutionInfo "Link to this definition")

    :   

    *[class][ ]*[[Statistics]][(]*[[minimum]][[:]][ ][[float]]*, *[[maximum]][[:]][ ][[float]]*, *[[average]][[:]][ ][[float]]*, *[[std_dev]][[:]][ ][[float]]*, *[[median]][[:]][ ][[float]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/perf_utils.html#MLModelBenchmarker.Statistics)[](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.Statistics "Link to this definition")

    :   

    *[async][ ]*[[benchmark_load]][(]*[[iterations]][[:]][ ][[int]][ ][[=]][ ][[1]]*[)] [[→] [[[Measurement]](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.Measurement "coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.Measurement")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/perf_utils.html#MLModelBenchmarker.benchmark_load)[](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.benchmark_load "Link to this definition")

    :   Measures the loading time of the model.

        This method creates and loads the model multiple times, measuring the duration of each load operation. It then unloads the model and performs garbage collection after each iteration to ensure consistent measurements.

        Parameters[:]

        :   

            **iterations: int**

            :   The number of times to load the model. Defaults to 1.

        Returns[:]

        :   

            MLModelBenchmarker.Measurement

            :   A Measurement object containing statistics and samples of the load durations in milliseconds.

    *[async][ ]*[[benchmark_operation_execution]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[iterations]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[warmup]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[List][[\[]][[OperationExecutionInfo]](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.OperationExecutionInfo "coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.OperationExecutionInfo")[[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/perf_utils.html#MLModelBenchmarker.benchmark_operation_execution)[](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.benchmark_operation_execution "Link to this definition")

    :   Measures the execution time of individual operations in the model.

        This method loads the model, runs predictions, and retrieves the execution time of each operation within the model.

        Parameters[:]

        :   

            **inputs**[Optional\[Dict\[str, Any\]\]]

            :   The input data for the model prediction. If None, random input data will be generated.

            **iterations: int**

            :   The number of prediction iterations to run. Defaults to 1.

            **warmup: bool**

            :   Whether to perform a warmup iteration. Defaults to False.

        Returns[:]

        :   

            List\[OperationExecutionInfo\]

            :   A list of OperationExecutionInfo objects, each containing details about an operation's execution, sorted by execution time in descending order.

        Notes

        - The returned list is sorted by execution time, with the most time-consuming operations first.

        - Execution times are estimated based on the overall prediction time and the model's compute plan.

    *[async][ ]*[[benchmark_predict]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[iterations]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[warmup]][[:]][ ][[bool]][ ][[=]][ ][[False]]*[)] [[→] [[[Measurement]](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.Measurement "coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.Measurement")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/perf_utils.html#MLModelBenchmarker.benchmark_predict)[](#coremltools.models.ml_program.experimental.perf_utils.MLModelBenchmarker.benchmark_predict "Link to this definition")

    :   Measures the prediction time of the model.

        This method loads the model, then runs predictions multiple times, measuring the duration of each prediction. It supports an optional warmup iteration.

        Parameters[:]

        :   

            **inputs**[Optional\[Dict\[str, Any\]\]]

            :   The input data for the model prediction. If None, random input data will be generated.

            **iterations: int**

            :   The number of prediction iterations to run. Defaults to 1.

            **warmup: bool**

            :   Whether to perform a warmup iteration. Defaults to False.

        Returns[:]

        :   

            MLModelBenchmarker.Measurement

            :   A Measurement object containing statistics and samples of the prediction durations in milliseconds.

            Raises:

            :   ValueError: If the number of iterations is less than 1.

            Note:

            :   This method is asynchronous and should be awaited when called. The warmup iteration, if enabled, is not included in the returned measurements.

[]

### async_wrapper[](#module-coremltools.models.ml_program.experimental.async_wrapper "Link to this heading")

*[class][ ]*[[coremltools.models.ml_program.experimental.async_wrapper.]][[LocalMLModelAsyncWrapper]][(]*[[spec_or_path]][[:]][ ][[Model][ ][[\|]][ ][str]]*, *[[weights_dir]][[:]][ ][[str]]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#LocalMLModelAsyncWrapper)[](#coremltools.models.ml_program.experimental.async_wrapper.LocalMLModelAsyncWrapper "Link to this definition")

:   

    *[property][ ]*[[last_predict_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.ml_program.experimental.async_wrapper.LocalMLModelAsyncWrapper.last_predict_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the last predict operation in nanoseconds. This method returns the time taken for the most recent prediction made by the model, measured in nanoseconds.

    *[async][ ]*[[load]][(][)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#LocalMLModelAsyncWrapper.load)[](#coremltools.models.ml_program.experimental.async_wrapper.LocalMLModelAsyncWrapper.load "Link to this definition")

    :   Asynchronously loads the [`MLModel`].

    *[property][ ]*[[load_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.ml_program.experimental.async_wrapper.LocalMLModelAsyncWrapper.load_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the model loading process in nanoseconds.

    *[async][ ]*[[predict]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][array][[\]]]]*, *[[state]][[:]][ ][[MLState][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[Dict][[\[]][str][[,]][ ][array][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#LocalMLModelAsyncWrapper.predict)[](#coremltools.models.ml_program.experimental.async_wrapper.LocalMLModelAsyncWrapper.predict "Link to this definition")

    :   Asynchronously performs predictions using the loaded [`MLModel`].

    *[async][ ]*[[retrieve_compute_plan]][(][)] [[→] [[[MLComputePlan]](#coremltools.models.compute_plan.MLComputePlan "coremltools.models.compute_plan.MLComputePlan")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#LocalMLModelAsyncWrapper.retrieve_compute_plan)[](#coremltools.models.ml_program.experimental.async_wrapper.LocalMLModelAsyncWrapper.retrieve_compute_plan "Link to this definition")

    :   Asynchronously retrieves the compute plan for the loaded [`MLModel`].

    *[async][ ]*[[unload]][(][)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#LocalMLModelAsyncWrapper.unload)[](#coremltools.models.ml_program.experimental.async_wrapper.LocalMLModelAsyncWrapper.unload "Link to this definition")

    :   Asynchronously unloads the [`MLModel`].

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.async_wrapper.]][[MLModelAsyncWrapper]][(]*[[spec_or_path]][[:]][ ][[Model][ ][[\|]][ ][str]]*, *[[weights_dir]][[:]][ ][[str]]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#MLModelAsyncWrapper)[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper "Link to this definition")

:   

    *[static][ ]*[[from_spec_or_path]][(]*[[spec_or_path]][[:]][ ][[Model][ ][[\|]][ ][str]]*, *[[weights_dir]][[:]][ ][[str]]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[[MLModelAsyncWrapper]](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper "coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#MLModelAsyncWrapper.from_spec_or_path)[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper.from_spec_or_path "Link to this definition")

    :   Creates an MLModelAsyncWrapper instance from a model specification or model path.

        This static method constructs an [`MLModelAsyncWrapper`] object based on the provided model specification and additional parameters.

        If the device parameter is [`None`], the model is loaded on the local system. Otherwise, it is loaded on the specified device.

        Parameters[:]

        :   

            **spec_or_path**[Union\["proto.Model_pb2.Model", str\]]

            :   Either a protobuf specification of the model ([`proto.Model_pb2.Model`]) or a string representing the file path to the model ([`mlpackage`]).

            **weights_dir: str**

            :   The model weights directory.

            **function_name**[Optional\[str\]]

            :   The function name. Defaults to the model's function name.

            **compute_units**[coremltools.ComputeUnit:]

            :   The compute units to use. Defaults to the model's compute unit.

            **optimization_hints**[Optional\[Dict\[str, Any\]\]]

            :   Keys are the names of the optimization hint, either 'reshapeFrequency' or 'specializationStrategy'. Values are enumeration values of type [`coremltools.ReshapeFrequency`] or [`coremltools.SpecializationStrategy`].

            **device: Device**

            :   The device on which the model will execute.

        Returns[:]

        :   

            MLModelAsyncWrapper

            :   An instance of MLModelAsyncWrapper.

    *[abstract][ ][property][ ]*[[last_predict_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper.last_predict_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the last predict operation in nanoseconds. This method returns the time taken for the most recent prediction made by the model, measured in nanoseconds.

    *[abstract][ ][async][ ]*[[load]][(][)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#MLModelAsyncWrapper.load)[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper.load "Link to this definition")

    :   Asynchronously loads the [`MLModel`].

    *[abstract][ ][property][ ]*[[load_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper.load_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the model loading process in nanoseconds.

    *[abstract][ ][async][ ]*[[predict]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][array][[\]]]]*, *[[state]][[:]][ ][[MLState][ ][[\|]][ ][None]]*[)] [[→] [[Dict][[\[]][str][[,]][ ][array][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#MLModelAsyncWrapper.predict)[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper.predict "Link to this definition")

    :   Asynchronously performs predictions using the loaded [`MLModel`].

    *[abstract][ ][async][ ]*[[retrieve_compute_plan]][(][)] [[→] [[[MLComputePlan]](#coremltools.models.compute_plan.MLComputePlan "coremltools.models.compute_plan.MLComputePlan")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#MLModelAsyncWrapper.retrieve_compute_plan)[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper.retrieve_compute_plan "Link to this definition")

    :   Asynchronously retrieves the compute plan for the loaded [`MLModel`].

    *[abstract][ ][async][ ]*[[unload]][(][)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#MLModelAsyncWrapper.unload)[](#coremltools.models.ml_program.experimental.async_wrapper.MLModelAsyncWrapper.unload "Link to this definition")

    :   Asynchronously unloads the [`MLModel`].

<!-- -->

*[class][ ]*[[coremltools.models.ml_program.experimental.async_wrapper.]][[RemoteMLModelAsyncWrapper]][(]*[[spec_or_path]][[:]][ ][[Model][ ][[\|]][ ][str]]*, *[[weights_dir]][[:]][ ][[str]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[optimization_hints]][[:]][ ][[Dict][[\[]][str][[,]][ ][Any][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#RemoteMLModelAsyncWrapper)[](#coremltools.models.ml_program.experimental.async_wrapper.RemoteMLModelAsyncWrapper "Link to this definition")

:   A concrete implementation of the [`MLModelAsyncWrapper`] for a remote [`MLModel`].

    *[property][ ]*[[last_predict_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.ml_program.experimental.async_wrapper.RemoteMLModelAsyncWrapper.last_predict_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the last predict operation in nanoseconds. This method returns the time taken for the most recent prediction made by the model, measured in nanoseconds.

    *[async][ ]*[[load]][(][)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#RemoteMLModelAsyncWrapper.load)[](#coremltools.models.ml_program.experimental.async_wrapper.RemoteMLModelAsyncWrapper.load "Link to this definition")

    :   Asynchronously loads the [`MLModel`].

    *[property][ ]*[[load_duration_in_nano_seconds]]*[[:]][ ][int][ ][[\|]][ ][None]*[](#coremltools.models.ml_program.experimental.async_wrapper.RemoteMLModelAsyncWrapper.load_duration_in_nano_seconds "Link to this definition")

    :   Retrieves the duration of the model loading process in nanoseconds.

    *[async][ ]*[[predict]][(]*[[inputs]][[:]][ ][[Dict][[\[]][str][[,]][ ][array][[\]]]]*, *[[state]][[:]][ ][[MLState][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[Dict][[\[]][str][[,]][ ][array][[\]]]]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#RemoteMLModelAsyncWrapper.predict)[](#coremltools.models.ml_program.experimental.async_wrapper.RemoteMLModelAsyncWrapper.predict "Link to this definition")

    :   Asynchronously performs predictions using the loaded [`MLModel`].

    *[async][ ]*[[retrieve_compute_plan]][(][)] [[→] [[[MLComputePlan]](#coremltools.models.compute_plan.MLComputePlan "coremltools.models.compute_plan.MLComputePlan")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#RemoteMLModelAsyncWrapper.retrieve_compute_plan)[](#coremltools.models.ml_program.experimental.async_wrapper.RemoteMLModelAsyncWrapper.retrieve_compute_plan "Link to this definition")

    :   Asynchronously retrieves the compute plan for the loaded [`MLModel`].

    *[async][ ]*[[unload]][(][)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/async_wrapper.html#RemoteMLModelAsyncWrapper.unload)[](#coremltools.models.ml_program.experimental.async_wrapper.RemoteMLModelAsyncWrapper.unload "Link to this definition")

    :   Asynchronously unloads the [`MLModel`].

[]

### model_structure_path[](#module-coremltools.models.ml_program.experimental.model_structure_path "Link to this heading")

*[class][ ]*[[coremltools.models.ml_program.experimental.model_structure_path.]][[ModelStructurePath]][(]*[[components]][[:]][ ][[Tuple][[\[]][[Program]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program")[ ][[\|]][ ][[Function]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Function "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Function")[ ][[\|]][ ][[Block]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Block "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Block")[ ][[\|]][ ][[Operation]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Operation "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Operation")[ ][[\|]][ ][[NeuralNetwork]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.NeuralNetwork "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.NeuralNetwork")[ ][[\|]][ ][[Layer]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.NeuralNetwork.Layer "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.NeuralNetwork.Layer")[ ][[\|]][ ][[Pipeline]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Pipeline "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Pipeline")[ ][[\|]][ ][[Model]](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Pipeline.Model "coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Pipeline.Model")[[,]][ ][[\...]][[\]]]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath "Link to this definition")

:   This class represents a hierarchical path within a model structure, allowing for the representation of various components in a program, neural network, or pipeline.

    *[class][ ]*[[NeuralNetwork]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.NeuralNetwork)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.NeuralNetwork "Link to this definition")

    :   Represents a neural network in the model structure.

        *[class][ ]*[[Layer]][(]*[[name]][[:]][ ][[str]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.NeuralNetwork.Layer)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.NeuralNetwork.Layer "Link to this definition")

        :   

    *[class][ ]*[[Pipeline]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.Pipeline)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Pipeline "Link to this definition")

    :   Represents a pipeline in the model structure.

        *[class][ ]*[[Model]][(]*[[name]][[:]][ ][[str]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.Pipeline.Model)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Pipeline.Model "Link to this definition")

        :   

    *[class][ ]*[[Program]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.Program)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program "Link to this definition")

    :   Represents a program in the model structure.

        *[class][ ]*[[Block]][(]*[[index]][[:]][ ][[int]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.Program.Block)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Block "Link to this definition")

        :   

        *[class][ ]*[[Function]][(]*[[name]][[:]][ ][[str]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.Program.Function)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Function "Link to this definition")

        :   

        *[class][ ]*[[Operation]][(]*[[output_name]][[:]][ ][[str]]*[)][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/model_structure_path.html#ModelStructurePath.Program.Operation)[](#coremltools.models.ml_program.experimental.model_structure_path.ModelStructurePath.Program.Operation "Link to this definition")

        :   

[]

### compute_plan_utils[](#module-coremltools.models.ml_program.experimental.compute_plan_utils "Link to this heading")

[[coremltools.models.ml_program.experimental.compute_plan_utils.]][[apply_compute_plan]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[compute_plan]][[:]][ ][[[MLComputePlan]](#coremltools.models.compute_plan.MLComputePlan "coremltools.models.compute_plan.MLComputePlan")]*, *[[backend_assignment_fn]][[:]][ ][[Callable][[\[]][[\[]][Operation][[,]][ ][[MLComputePlanDeviceUsage]](#coremltools.models.compute_plan.MLComputePlanDeviceUsage "coremltools.models.compute_plan.MLComputePlanDeviceUsage")[ ][[\|]][ ][None][[\]]][[,]][ ][List][[\[]][str][[\]]][ ][[\|]][ ][None][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/compute_plan_utils.html#apply_compute_plan)[](#coremltools.models.ml_program.experimental.compute_plan_utils.apply_compute_plan "Link to this definition")

:   This function takes an MLModel and sets the intended backend attribute of each operation in the model as determined by the model's compute plan.

    It updates the 'IntendedBackend' attribute of each operation, ensuring the same dispatch even if the model is modified.

<!-- -->

*[[async]][ ]*[[coremltools.models.ml_program.experimental.compute_plan_utils.]][[load_compute_plan_from_path_on_device]][(]*[[path]][[:]][ ][[str]]*, *[[compute_units]][[:]][ ][[ComputeUnit]][ ][[=]][ ][[ComputeUnit.ALL]]*, *[[device]][[:]][ ][[[Device]](#coremltools.models.ml_program.experimental.remote_device.Device "coremltools.models.ml_program.experimental.remote_device.Device")[ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)] [[→] [[[MLComputePlan]](#coremltools.models.compute_plan.MLComputePlan "coremltools.models.compute_plan.MLComputePlan")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/compute_plan_utils.html#load_compute_plan_from_path_on_device)[](#coremltools.models.ml_program.experimental.compute_plan_utils.load_compute_plan_from_path_on_device "Link to this definition")

:   Loads the compute plan of a compiled model on a remote or local device.

    The path must be the location of the [`mlmodelc`] directory.

    Parameters[:]

    :   

        **path**[str]

        :   The path to the compiled model.

    Returns[:]

    :   

        The plan for executing the model.

        :   

    Examples

    :::: 
    ::: highlight
        # Retrieve a development device.
        devices = Device.get_connected_development_devices(device_type=DeviceType.IPHONE)
        device = devices[0]
        # Prepare device for model debugging.
        device = await device.prepare_for_model_debugging()
        compute_plan = await coremltools.models.ml_program.experimental.compute_plan_utils.load_compute_plan_from_path_on_device(
            path=model.get_compiled_path(),
            device=device,
        )

        if compute_plan.model_structure.program is None:
            raise ValueError("Unexpected model type.")

        program = compute_plan.model_structure.program
        mainFunction = program.functions["main"]
        for operation in mainFunction.block.operations:
            # Get the compute device usage for the operation.
            compute_device_usage = (
                compute_plan.get_compute_device_usage_for_mlprogram_operation(operation)
            )
            # Get the estimated cost of executing the operation.
            estimated_cost = compute_plan.get_estimated_cost_for_mlprogram_operation(operation)
    :::
    ::::

<!-- -->

[[coremltools.models.ml_program.experimental.compute_plan_utils.]][[set_intended_backends]][(]*[[model]][[:]][ ][[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]*, *[[backend_assignment_fn]][[:]][ ][[Callable][[\[]][[\[]][Operation][[\]]][[,]][ ][List][[\[]][str][[\]]][ ][[\|]][ ][None][[\]]]]*[)] [[→] [[[MLModel]](#coremltools.models.model.MLModel "coremltools.models.model.MLModel")]][[[\[source\]]]](../_modules/coremltools/models/ml_program/experimental/compute_plan_utils.html#set_intended_backends)[](#coremltools.models.ml_program.experimental.compute_plan_utils.set_intended_backends "Link to this definition")

:   Assigns intended backends to operations in the given model.

    This function creates a new MLModel with updated backend assignments for each operation. It traverses the entire model structure, applying the provided backend assignment function to determine the intended backends for each operation.

    Parameters[:]

    :   

        **model**[MLModel]

        :   The input model to be processed.

        **backend_assignment_fn**[Callable\[\[proto.MIL_pb2.Operation\], Optional\[List\[str\]\]\]]

        :   A function that takes an operation and returns a list of intended backend names.

    Returns[:]

    :   

        MLModel

        :   A new model instance with updated backend assignments.