# Source: https://apple.github.io/coremltools/source/coremltools.converters.mil.input_types.html

# MIL Input Types[](#mil-input-types "Link to this heading")

Input types supported by the Model Intermediate Language (MIL):

[]

## InputType[](#inputtype "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[InputType]][(]*[[name]][[=]][[None]]*, *[[shape]][[=]][[None]]*, *[[dtype]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#InputType)[](#coremltools.converters.mil.input_types.InputType "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[name]][[=]][[None]]*, *[[shape]][[=]][[None]]*, *[[dtype]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#InputType.__init__)[](#coremltools.converters.mil.input_types.InputType.__init__ "Link to this definition")

    :   The input type for inputs fed into the model.

        Parameters[:]

        :   

            **name: (str)**

            :   The name of the input.

            **shape: list, tuple, Shape object, EnumeratedShapes object, or None**

            :   The shape(s) that are valid for this input. If set to [`None`], the shape will be inferred from the model itself.

## ClassifierConfig[](#classifierconfig "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[ClassifierConfig]][(]*[[class_labels]]*, *[[predicted_feature_name]][[=]][[\'classLabel\']]*, *[[predicted_probabilities_output]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#ClassifierConfig)[](#coremltools.converters.mil.input_types.ClassifierConfig "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[class_labels]]*, *[[predicted_feature_name]][[=]][[\'classLabel\']]*, *[[predicted_probabilities_output]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#ClassifierConfig.__init__)[](#coremltools.converters.mil.input_types.ClassifierConfig.__init__ "Link to this definition")

    :   Configuration for classifier models.

        Parameters[:]

        :   

            **class_labels: str / list of int / list of str**

            :   - If a [`list`] is provided, the [`list`] maps the index of the output of a neural network to labels in a classifier.

                - If a [`str`] is provided, the [`str`] points to a file which maps the index to labels in a classifier.

            **predicted_feature_name: str**

            :   Name of the output feature for the class labels exposed in the Core ML neural network classifier. Default: [`'classLabel'`].

            **predicted_probabilities_output: str**

            :   - If provided, then this is the name of the neural network blob which generates the probabilities for each class label (typically the output of a softmax layer).

                - If not provided, then the last output layer is assumed.

## EnumeratedShapes[](#enumeratedshapes "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[EnumeratedShapes]][(]*[[shapes]]*, *[[default]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#EnumeratedShapes)[](#coremltools.converters.mil.input_types.EnumeratedShapes "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[shapes]]*, *[[default]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#EnumeratedShapes.__init__)[](#coremltools.converters.mil.input_types.EnumeratedShapes.__init__ "Link to this definition")

    :   A shape class for setting multiple valid shapes in InputType.

        Parameters[:]

        :   

            **shapes: list of Shape objects, or Shape-compatible lists**

            :   - The valid shapes of the inputs.

                - If input provided is not a [[`Shape`]](#coremltools.converters.mil.input_types.Shape "coremltools.converters.mil.input_types.Shape") object, but can be converted to a [[`Shape`]](#coremltools.converters.mil.input_types.Shape "coremltools.converters.mil.input_types.Shape"), the [[`Shape`]](#coremltools.converters.mil.input_types.Shape "coremltools.converters.mil.input_types.Shape") object would be stored in [`shapes`] instead.

            **default: tuple of int or None**

            :   - The default shape that is used for initiating the model, and set in the metadata of the model file.

                - If [`None`], then the first element in [`shapes`] is used.

        Examples

        :::: 
        ::: highlight
            sample_shape = ct.EnumeratedShapes(
                shapes=[(2, 4, 64, 64), (2, 4, 48, 48), (2, 4, 32, 32)], default=(2, 4, 64, 64)
            )

            my_core_ml_model = ct.convert(
                my_model,
                inputs=[ct.TensorType(name="sample", shape=sample_shape)],
            )
        :::
        ::::

## ImageType[](#imagetype "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[ImageType]][(]*[[name]][[=]][[None]]*, *[[shape]][[=]][[None]]*, *[[scale]][[=]][[1.0]]*, *[[bias]][[=]][[None]]*, *[[color_layout]][[=]][[ColorLayout.RGB]]*, *[[channel_first]][[=]][[None]]*, *[[grayscale_use_uint8]][[=]][[False]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#ImageType)[](#coremltools.converters.mil.input_types.ImageType "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[name]][[=]][[None]]*, *[[shape]][[=]][[None]]*, *[[scale]][[=]][[1.0]]*, *[[bias]][[=]][[None]]*, *[[color_layout]][[=]][[ColorLayout.RGB]]*, *[[channel_first]][[=]][[None]]*, *[[grayscale_use_uint8]][[=]][[False]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#ImageType.__init__)[](#coremltools.converters.mil.input_types.ImageType.__init__ "Link to this definition")

    :   Configuration class used for image inputs in Core ML.

        Parameters[:]

        :   

            **scale: float or list of floats**

            :   The scaling factor for all values in the image channels.

            **bias: float or list of floats**

            :   - If [`color_layout`] is [`ct.colorlayout.GRAYSCALE`] or [`ct.colorlayout.GRAYSCALE_FLOAT16`], bias would be a [`float`].

                - If [`color_layout`] is [`ct.colorlayout.RGB`] or [`ct.colorlayout.BGR`], bias would be a list of [`float`].

            **color_layout: string or enumeration of type \`\`ct.colorlayout\`\`**

            :   Color layout of the image. Valid values are as follows:

                Enumeration (recommended):

                :   - [`ct.colorlayout.RGB`]

                    - [`ct.colorlayout.BGR`]

                    - [`ct.colorlayout.GRAYSCALE`]

                    - [`ct.colorlayout.GRAYSCALE_FLOAT16`]

                String values (older way to specify):

                :   - [`'G'`]: Grayscale (maps to [`ct.colorlayout.GRAYSCALE`])

                    - [`'RGB'`]: \[Red, Green, Blue\] (maps to [`ct.colorlayout.BGR`])

                    - [`'BGR'`]: \[Blue, Green, Red\] (maps to [`ct.colorlayout.RGB`])

            **channel_first: (bool) or None**

            :   Set to [`True`] if input format is channel first.

                Default format:

                :   - For TensorFlow: channel last ([`channel_first=False`]).

                    - For PyTorch: channel first ([`channel_first=True`]).

            **grayscale_use_uint8: (bool)**

            :   - Only applicable for GRAYSCALE color layout.

                - Defaults to [`False`], in which case fp32 will be used.

                - Using uint8 requires a [`minimum_deployment_target`] of iOS17 or newer.

                - Using uint8 restricts the number of avaliable MIL ops, which can cause conversion to fail.

## RangeDim[](#rangedim "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[RangeDim]][(]*[[lower_bound]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[upper_bound]][[:]][ ][[int]][ ][[=]][ ][[-1]]*, *[[default]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[symbol]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#RangeDim)[](#coremltools.converters.mil.input_types.RangeDim "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[lower_bound]][[:]][ ][[int]][ ][[=]][ ][[1]]*, *[[upper_bound]][[:]][ ][[int]][ ][[=]][ ][[-1]]*, *[[default]][[:]][ ][[int][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[symbol]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#RangeDim.__init__)[](#coremltools.converters.mil.input_types.RangeDim.__init__ "Link to this definition")

    :   A class for providing a range of accepted shapes.

        Parameters[:]

        :   

            **lower_bound:**

            :   The minimum valid value for the shape.

            **upper_bound:**

            :   The maximum valid value for the shape.

                Set to [`-1`] if there is no upper limit (only works if backend is set to "neuralnetwork"). When backend is set to "mlprogram" during conversion, -1 is not allowed. A finite positive upper bound must be provided.

            **default:**

            :   The default value that is used for initiating the model, and set in the input shape field of the model file.

                If set to [`None`], [`lower_bound`] would be used as default.

            **symbol:**

            :   Optional symbol name for the dim. Autogenerate a symbol name if not specified.

## Shape[](#shape "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[Shape]][(]*[[shape]]*, *[[default]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#Shape)[](#coremltools.converters.mil.input_types.Shape "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[shape]]*, *[[default]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#Shape.__init__)[](#coremltools.converters.mil.input_types.Shape.__init__ "Link to this definition")

    :   The basic shape class to be set in [[`InputType`]](#coremltools.converters.mil.input_types.InputType "coremltools.converters.mil.input_types.InputType").

        Parameters[:]

        :   

            **shape: list of (int), symbolic values, RangeDim object**

            :   The valid shape of the input.

            **default: tuple of int or None**

            :   The default shape that is used for initiating the model, and set in the metadata of the model file.

                If [`None`], then [`shape`] is used.

## StateType[](#statetype "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[StateType]][(]*[[wrapped_type]][[:]][ ][[type]]*, *[[name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#StateType)[](#coremltools.converters.mil.input_types.StateType "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[wrapped_type]][[:]][ ][[type]]*, *[[name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#StateType.__init__)[](#coremltools.converters.mil.input_types.StateType.__init__ "Link to this definition")

    :   Specify a model state as a wrapper of a [`TensorType`]. For example, you can use the following code to create a state type input that wraps a fp16 tensor with shape [`(2,`]` `[`3)`]:

        :::: 
        ::: highlight
            ct.StateType(
                wrapped_type=ct.TensorType(
                    shape=(2, 3),
                    dtype=np.float16
                ),
                name="state",
            )
        :::
        ::::

        Parameters[:]

        :   

            **wrapped_type: coremltools.converters.mil.input_types.InputType**

            :   - The type wrapped in the state.

                - Must be [`TensorType`]. Note that the [`name`] and [`default_value`] of the wrapped [`TensorType`] must not be provided.

            **name: str**

            :   The name of the state. It must match the key of [`named_buffers()`] in the source TorchScript model.

## TensorType[](#tensortype "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.input_types.]][[TensorType]][(]*[[name]][[=]][[None]]*, *[[shape]][[=]][[None]]*, *[[dtype]][[=]][[None]]*, *[[default_value]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#TensorType)[](#coremltools.converters.mil.input_types.TensorType "Link to this definition")

:   

    [[\_\_init\_\_]][(]*[[name]][[=]][[None]]*, *[[shape]][[=]][[None]]*, *[[dtype]][[=]][[None]]*, *[[default_value]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/input_types.html#TensorType.__init__)[](#coremltools.converters.mil.input_types.TensorType.__init__ "Link to this definition")

    :   Specify a (dense) tensor input.

        Parameters[:]

        :   

            **name: str**

            :   Input name. Must match an input name in the model (usually the Placeholder name for TensorFlow or the input name for PyTorch).

                The [`name`] is required except for a TensorFlow model in which there is exactly one input Placeholder.

            **shape: The shape of the input**

            :   - List of positive int or [[`RangeDim`]](#coremltools.converters.mil.input_types.RangeDim "coremltools.converters.mil.input_types.RangeDim"), or

                - [[`EnumeratedShapes`]](#coremltools.converters.mil.input_types.EnumeratedShapes "coremltools.converters.mil.input_types.EnumeratedShapes")

                For TensorFlow:

                :   - The [`shape`] is optional. If omitted, the shape is inferred from TensorFlow graph's Placeholder shape.

                For PyTorch:

                :   - The [`shape`] is required.

            **dtype: np.generic or mil.type type**

            :   For example, [`np.int32`] or [`coremltools.converters.mil.mil.types.fp32`]

            **default_value: np.ndarray**

            :   If provided, the input is considered optional. At runtime, if the input is not provided, [`default_value`] is used.

                Limitations:

                :   - If [`default_value`] is [`np.ndarray`], all elements are required to have the same value.

                    - The [`default_value`] may not be specified if [`shape`] is [[`EnumeratedShapes`]](#coremltools.converters.mil.input_types.EnumeratedShapes "coremltools.converters.mil.input_types.EnumeratedShapes").

        Examples

        - [`ct.TensorType(name="input",`]` `[`shape=(1,`]` `[`2,`]` `[`3))`] implies [`dtype`]` `[`==`]` `[`np.float32`]

        - [`ct.TensorType(name="input",`]` `[`shape=(1,`]` `[`2,`]` `[`3),`]` `[`dtype=np.int32)`]

        - [`ct.TensorType(name="input",`]` `[`shape=(1,`]` `[`2,`]` `[`3),`]` `[`dtype=ct.converters.mil.types.fp32)`]