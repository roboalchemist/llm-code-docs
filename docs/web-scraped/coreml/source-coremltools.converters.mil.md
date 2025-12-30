# Source: https://apple.github.io/coremltools/source/coremltools.converters.mil.html

[]

# MIL Builder[](#module-coremltools.converters.mil.mil "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.]][[Builder]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/builder.html#Builder)[](#coremltools.converters.mil.mil.Builder "Link to this definition")

:   This class is a singleton builder to construct a MIL program. For more information, see [Create a MIL program](https://coremltools.readme.io/docs/model-intermediate-language#create-a-mil-program).

    Importing [`.ops`] triggers the installation of all MIL ops into the Builder. For details on each op, see [MIL ops](https://apple.github.io/coremltools/source/coremltools.converters.mil.mil.ops.defs.html).

    Examples

    :::: 
    ::: highlight
        >>> from coremltools.converters.mil.mil import Builder as mb
        >>> from coremltools.converters.mil.mil import Program, Function
    :::
    ::::

    :::: 
    ::: highlight
        >>> prog = Program()
        >>> func_inputs = 
        >>> with Function(func_inputs) as ssa_fun:
        >>>   x, y = ssa_fun.inputs['x'], ssa_fun.inputs['y']
        >>>   res_var = mb.add(x=x, y=y) # created within ssa_fun block
        >>>   ssa_fun.set_outputs([res_var])
        >>> prog.add_function("main", ssa_fun)
    :::
    ::::

    :::: 
    ::: highlight
        >>> # Importing ops triggers installation of all ops into Builder.
        >>> from .ops import defs as _ops
    :::
    ::::

    *[static][ ]*[[program]][(]*[[input_specs]][[:]][ ][[List][[\[]][Placeholder][[\]]][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[opset_version]][[:]][ ][[AvailableTarget][ ][[\|]][ ][None]][ ][[=]][ ][[None]]*, *[[function_name]][[:]][ ][[str][ ][[\|]][ ][None]][ ][[=]][ ][[\'main\']]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/builder.html#Builder.program)[](#coremltools.converters.mil.mil.Builder.program "Link to this definition")

    :   The [`mb.program`] decorator creates a MIL program with a single function with name [`function_name`].

        Parameters[:]

        :   

            **input_specs: List\[TensorSpec\]**

            :   Describes the function inputs

            **opset_version: AvailableTarget enum**

            :   Describes the opset version of the program

            **function_name: str**

            :   Name of the function

        Examples

        :::: 
        ::: highlight
            >>> import coremltools as ct
            >>> from coremltools.converters.mil.mil import Builder as mb
            >>>
            >>> @mb.program(input_specs=[mb.TensorSpec(shape=(1,2))], opset_version=ct.target.iOS16)
            >>> def prog(a):
            >>>     return mb.add(x=a, y=2)
        :::
        ::::