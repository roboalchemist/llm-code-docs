# Source: https://apple.github.io/coremltools/source/coremltools.converters.mil.mil.passes.defs.html

# MIL Graph Passes[](#mil-graph-passes "Link to this heading")

Graph Passes supported by the Model Intermediate Language (MIL):

[]

## cleanup[](#module-coremltools.converters.mil.mil.passes.defs.cleanup "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[const_deduplication]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/const_deduplication.html#const_deduplication)[](#coremltools.converters.mil.mil.passes.defs.cleanup.const_deduplication "Link to this definition")

:   Remove duplicated large constants (tensor with 100+ elements)

    For example

    :::: 
    ::: highlight
        Input graph (where weight and bias are large constants):
            weight_q = const(weight)
            weight_k = const(weight)
            bias_q = const(bias)
            bias_k = const(bias)
            q_embedding = linear(x=q, weight=weight_q, bias=bias_q)
            k_embedding = linear(x=k, weight=weight_k, bias=bias_k)

        Output graph:
            weight_q = const(weight)
            bias_q = const(bias)
            q_embedding = linear(x=q, weight=weight_q, bias=bias_q)
            k_embedding = linear(x=k, weight=weight_q, bias=bias_q)
    :::
    ::::

    Concretely, this graph pass consists of two stages:

    1.  Deduplication of [`const`] op:

        We consider a [`const`] as duplicated if there exists such a previous [`const`] that has same dtype and value

    2.  Deduplication of [`constexpr_*`] op:

        We consider a [`constexpr_*`] as duplicated if there exists such a previous [`constexpr_*`] that has the same [`op_type`] and input attributes.

    Support options:

    - [`const_threshold`]: Skip deduplicating [`const`] ops that have smaller number of elements than a threshold. Defaults to [`100`]. i.e. the constants with [`size`]` `[`<`]` `[`100`] will not be deduplicated.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[const_elimination]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/const_elimination.html#const_elimination)[](#coremltools.converters.mil.mil.passes.defs.cleanup.const_elimination "Link to this definition")

:   Replace non-[`const`] ops that have [`const`] Var. Outputs are replaced with the [`const`] op. Example:

    :::: 
    ::: highlight
        Given:
            %2, %3 = non_const_op(...)  # %2 is const, %3 isn't const
            %4 = other_op(%2, %3)

        Result:
            _, %3 = non_const_op(...)  # _ is the ignored output
            %2_const = const()         # %2_const name is for illustration only
            %4 = other_op(%2_const, %3)
    :::
    ::::

    Support options:

    - [`skip_const_by_size`]: Skip folding [`const`] ops that have larger number of elements than a threshold.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[dead_code_elimination]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/dead_code_elimination.html#dead_code_elimination)[](#coremltools.converters.mil.mil.passes.defs.cleanup.dead_code_elimination "Link to this definition")

:   Eliminate unused ops in program. Ops whose outputs do not contribute to final outputs will be deleted.

    :::: 
    ::: highlight
        # Before dead_code_elimination pass.
        main(%x: (2, 4, fp32))  -> (%linear_0)
        }

        # After dead_code_elimination pass.
        main(%x: (2, 4, fp32))  -> (%linear_0)
        }
    :::
    ::::

    In the example above, [`%matmul_0`] is an op that is not used in the computation. This op and its input ops ([`%tx_0`] and [`%ty_0`]) are eliminated in this pass.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[dedup_op_and_var_names]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/dedup_op_and_var_names.html#dedup_op_and_var_names)[](#coremltools.converters.mil.mil.passes.defs.cleanup.dedup_op_and_var_names "Link to this definition")

:   For each function, this pass renames ops and variables with the same name as any preceding ops/variables across all scopes in the given function, where the precedence is implementation-specific. Note that an op name and variable names are tracked separately, so an op may have the same name as a variable.

    The pass preserves input and output name. Raises ValueError if we cannot dedup without changing the input/output var names.

    :::: 
    ::: highlight
        def prog(x):
            x = mb.cast(x=x, dtype="fp16", name="castop")
            x = mb.cast(x=x, dtype="fp32", name="castop")
            x = mb.square(x=x, name="square_last")
            return x

        # Before dedup pass, the op names are ["castop", "castop", "square_last"].
        # After dedup pass, the op names are ["castop", "castop_1", "square_last"].
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[expand_dynamic_linear]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/expand_dynamic_linear.html#expand_dynamic_linear)[](#coremltools.converters.mil.mil.passes.defs.cleanup.expand_dynamic_linear "Link to this definition")

:   Translate to [`linear`] when the operand is a descendant of const, since such an operand may be folded into const or fused into constexpr later by graph passes. In op translation, we prefer [`linear`] whenever possible because it requires const or constexpr [`weight`] and [`bias`].

    If such const folding or constexpr fusion did not happen, this pass would clean up the too-ambitious [`linear`] ops by replacing them with [`matmul`] ops.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[fuse_reduce_mean]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/fuse_reduce_mean.html#fuse_reduce_mean)[](#coremltools.converters.mil.mil.passes.defs.cleanup.fuse_reduce_mean "Link to this definition")

:   Detect the [`reduce_sum`] ---\> [`mul/real_div`] pattern than can be mapped to [`reduce_mean`]. That is, the operation [`reduce_sum/count`]` `[`==`]` `[`reduce_mean`].

    Input graph

    :::: 
    ::: highlight
                                    const (scalar)
                                        |
        input ----> reduce_sum ----> mul/real_div -----------> output
    :::
    ::::

    Output graph

    :::: 
    ::: highlight
        input --------> reduce_mean ---------> output
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[loop_invariant_elimination]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/loop_invariant_elimination.html#loop_invariant_elimination)[](#coremltools.converters.mil.mil.passes.defs.cleanup.loop_invariant_elimination "Link to this definition")

:   When a block does not modify a block input var, eliminate that block input var and use the corresponding var in the outer scope. Example:

    :::: 
    ::: highlight
        # Before loop_invariant_elimination pass.
        # Notice that ``%b.x`` is constant through while loop iterates.
        main(%a: (1, 2, fp32),
             %b: (1, 2, fp32))  -> (%cond_var)
              loop_body(%a.x, %b.x)  -> (%add_0, %b.x)
          } -> (%loop:0, %loop:1)
        }

        # After loop_invariant_elimination pass.
        main(%a: (1, 2, fp32),
             %b: (1, 2, fp32))  -> (%cond_var)
              loop_body(%a.x)  -> (%add_0)
          } -> (%loop:0, %loop:1)
        }
    :::
    ::::

    where we eliminate loop invariant [`%b.x`] from [`while_loop`], which returns 1 instead of 2 outputs. We also preserve the return var names with identity.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[noop_elimination]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/noop_elimination.html#noop_elimination)[](#coremltools.converters.mil.mil.passes.defs.cleanup.noop_elimination "Link to this definition")

:   Remove ops that have no effect.

    :::: 
    ::: highlight
        Given:
            %1 (1, 96, 128, 64, fp32) = ...
            %2 (1, 96, 128, 64, fp32) = reshape(%1)
            ...
            %3 (1, 96, 128, 64, fp32) = add(%2, constant)
            ...

        Result:
            %1 (1, 96, 128, 64, fp32) = ...
            %3 (1, 96, 128, 64, fp32) = add(%1, constant)
        ...
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[remove_redundant_ops]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/remove_redundant_ops.html#remove_redundant_ops)[](#coremltools.converters.mil.mil.passes.defs.cleanup.remove_redundant_ops "Link to this definition")

:   If there are multiple ops with "identical" inputs, then they are redundant and all but one of them can be removed. This pass checks and removes such ops.

    Since all inputs to ops in MIL are named, two ops with same [`op_types`] can be compared by comparing their correspondingly named inputs. Inputs are treated as identical if one of the following is true:

    - The input is a constant var, in which case its value should have the same dtype and numerical value.

    - The input is a non constant var, in which case it should be the same var object.

    This pass iterates over the ops, takes its first output var, and then builds a candidate op list from the child ops of this var. This candidate ops list contains ops of the same [`op_type`], arranged in topological order. From each of these candidate ops in the list, the second, third, and subsequent ops are pairwise compared with the first op, and if identical to it, they are removed. For example:

    :::: 
    ::: highlight
        Input:
            %0 = op0(...)
            %1 = op1(...)
            %2 = const(val=4.5)
            %3 = const(val=4.5)
            %4 = op2(%1, %0, %2)
            %5 = op3(%1, %0, %3)

        Output:
            %0 = op0(...)
            %1 = op1(...)
            %2 = const(val=4.5)
            %3 = const(val=4.5) # this will get removed later by dead code elimination pass
            %4 = op2(%1, %0, %2)
    :::
    ::::

    In the example above, [`op3`] is removed and all uses of [`%5`] is replaced by [`%4`]. For more examples, see "TestRemoveRedundantOpsPass".

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[remove_symbolic_reshape]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/remove_symbolic_reshape.html#remove_symbolic_reshape)[](#coremltools.converters.mil.mil.passes.defs.cleanup.remove_symbolic_reshape "Link to this definition")

:   Convert symbolic shape in [`reshape`] to integers.

    Note: This does not perform any optimization, but simply replaces symbols with positive integers if solved from volumetric constraint, or -1. Therefore, this pass fails if more than one symbol needs to be resolved to -1.

    :::: 
    ::: highlight
        # Before remove_symbolic_reshape pass.
        main(%x: (s0, 4, fp32))  -> (%reshape_0)
        }

        # After remove_symbolic_reshape pass.
        main(%x: (s0, 4, fp32))  -> (%reshape_0)
        }
    :::
    ::::

    TODO ([rdar://59165842](rdar://59165842)): Use expand_dims, squeeze etc to use 0 instead of dynamic reshape with -1.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.cleanup.]][[topological_reorder]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/cleanup/topological_reorder.html#topological_reorder)[](#coremltools.converters.mil.mil.passes.defs.cleanup.topological_reorder "Link to this definition")

:   Topologically re-orders the list of operations in a program by places each operation closer to its first use, or at the end if it's not consumed by any other operation.

    Currently, This pass re-orders only Transpose and Cast operations.

    :::: 
    ::: highlight
        # Example: input program
        main(x: (2, 4, fp32))  -> x2, x4, x7, x8

        # After moving `cast` ops becomes
        main(x: (2, 4, fp32))  -> x2, x4, x7, x8

        # After moving `transpose` ops becomes
        main(x: (2, 4, fp32))  -> x2, x4, x7, x8
    :::
    ::::

[]

## optimize_activation[](#module-coremltools.converters.mil.mil.passes.defs.optimize_activation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_activation.]][[fuse_gelu_exact]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_activation.html#fuse_gelu_exact)[](#coremltools.converters.mil.mil.passes.defs.optimize_activation.fuse_gelu_exact "Link to this definition")

:   Identify the pattern that corresponds to the exact version of [`gelu`], and replace it with a single [`gelu`] layer with [`mode=EXACT`]. The pattern is [`y`]` `[`=`]` `[`0.5`]` `[`*`]` `[`x`]` `[`*`]` `[`(1`]` `[`+`]` `[`erf`]` `[`(x`]` `[`/`]` `[`srqt`]` `[`(2))`], which can be represented by one of the following:

    :::: 
    ::: highlight
        (1)
            [...] ----> div (1.414) ---> erf ---> add (1) -----> mul (0.5) ---> mul ---> [...]
              |                                                                  ^
              |                                                                  |
              |-------------------------------------------------------------------

        (2)
            [...] ----> div (1.414) ---> erf ---> add (1) -----> mul ---> mul (0.5) ---> [...]
              |                                                   ^
              |                                                   |
              |----------------------------------------------------

        (3)
            [...] ----> div (1.414) ---> erf ---> add (1) -----> mul ------> [...]
              |                                                   ^
              |                                                   |
              |---------------> mul(0.5) --------------------------

        All of them are converted to:
            [...] ----> gelu (mode=EXACT) ---> [...]
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_activation.]][[fuse_gelu_tanh_approximation]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_activation.html#fuse_gelu_tanh_approximation)[](#coremltools.converters.mil.mil.passes.defs.optimize_activation.fuse_gelu_tanh_approximation "Link to this definition")

:   Identify the pattern that corresponds to the [`tanh`] approximate version of [`gelu`], and replace it with a single [`gelu`] layer with [`mode=TANH_APPROXIMATION`].

    The implementation of this pass uses the generic graph pattern matching and transform algorithm implemented in [`coremltools.converters.mil.experimental.passes.generic_pass_infrastructure`] and documented in [`coremltools/converters/mil/experimental/passes/readme.md`].

    Graph for [`get_gelu_pattern1()`]

    [`y`]` `[`=`]` `[`x`]` `[`*`]` `[`(0.5`]` `[`*`]` `[`(tanh(((.0447)x^3`]` `[`+`]` `[`x`]` `[`)`]` `[`*`]` `[`sqrt(2/pi))`]` `[`+`]` `[`1))`]

    :::: 
    ::: highlight
        [...] -----> pow (3) ----> mul (.044715) ---> add -----> mul (sqrt(2/pi)) ---> tanh ----> add (1) ----> mul (0.5) -----> mul ---> [...]
          |                                            ^                                                                          ^
          |                                            |                                                                          |
          |------------------------------------------------------------------------------------------------------------------------
    :::
    ::::

    Graph for [`get_gelu_pattern2()`]

    [`y`]` `[`=`]` `[`(0.5`]` `[`*`]` `[`x)`]` `[`*`]` `[`(tanh(((.0447)x^3`]` `[`+`]` `[`x`]` `[`)`]` `[`*`]` `[`sqrt(2/pi))`]` `[`+`]` `[`1)`]

    :::: 
    ::: highlight
                       --------------------------------------------------------------------------------------------------------
                       ^                                                                                                      |
                       |                                                                                                      V
        [...] -----> mul(0.5)    pow (3) ----> mul (.044715) ---> add -----> mul (sqrt(2/pi)) ---> tanh ----> add (1) -----> mul ---> [...]
          |                        ^                               ^
          |                        |                               |
          |---------------------------------------------------------
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_activation.]][[fuse_leaky_relu]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_activation.html#fuse_leaky_relu)[](#coremltools.converters.mil.mil.passes.defs.optimize_activation.fuse_leaky_relu "Link to this definition")

:   Detect the [`mul`] ---\> [`max`] pattern than can be mapped to [`leaky_relu`].

    In code form - Input

    :::: 
    ::: highlight
        %2 = const(value = alpha) # where 0 <= alpha <= 1
        %3 = mul(%1, %2) # alpha * x
        %4 = max(%3, %1) # max(alpha * x, x)
    :::
    ::::

    In code form - Output

    :::: 
    ::: highlight
        %4 = leaky_relu(x=%1, alpha=%2)
    :::
    ::::

    In graphical form - Input graph

    :::: 
    ::: highlight
                 const (val = alpha)
                     |
        input ----> mul ---------------> maximum -----------> output
          |                                 |
          |----------------------------------
    :::
    ::::

    In graphical form - Output graph

    :::: 
    ::: highlight
        input --------> leaky_relu ---------> output
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_activation.]][[fuse_prelu]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_activation.html#fuse_prelu)[](#coremltools.converters.mil.mil.passes.defs.optimize_activation.fuse_prelu "Link to this definition")

:   Detect the following patterns that can be mapped to a [`prelu`] op. Essentially, the [`prelu`] op can be broken down into the following ops:

    [`y`]` `[`=`]` `[`a`]` `[`*`]` `[`relu(-1`]` `[`*`]` `[`x)`]` `[`+`]` `[`relu(x)`]

    Pattern 1

    :::: 
    ::: highlight
                       | ------------> relu --------------------|
                       |                                        V
        x (BCHW) ------|                                       add -----> y (BCHW)
                       |                                        ^
                       --------> mul -------> relu -----> mul---|
                                  ^                        ^
                                  |                        |
                             Const(val=-1)            Const(name=a, shape=(C,1,1) or (1,C,1,1))
    :::
    ::::

    This will be mapped to:

    :::: 
    ::: highlight
        x (BCHW) ------> prelu(alpha=a, shape=(C,)) ---------> y (BCHW)
    :::
    ::::

    Pattern 2

    :::: 
    ::: highlight
                                        | ------------> relu --------------------|
                                        |                                        V
        x (BCHW) -->transpose(BHWC)---->|                                       add -----> y (BHWC)
                                        |                                        ^
                                        --------> mul -------> relu -----> mul---|
                                                   ^                        ^
                                                   |                        |
                                          Const(val=-1)    Const(shape=(C,) or (1,C) or (1,1,C) or (1,1,1,C))
    :::
    ::::

    This will be mapped to:

    :::: 
    ::: highlight
        x (BCHW) ------> prelu ---------> transpose ------> y (BHWC)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_activation.]][[prelu_to_lrelu]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_activation.html#prelu_to_lrelu)[](#coremltools.converters.mil.mil.passes.defs.optimize_activation.prelu_to_lrelu "Link to this definition")

:   If [`prelu`] has the same leakage factor across all channels, it will be converted to [`leaky_relu`].

[]

## optimize_conv[](#module-coremltools.converters.mil.mil.passes.defs.optimize_conv "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_conv.]][[add_conv_transpose_output_shape]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_conv.html#add_conv_transpose_output_shape)[](#coremltools.converters.mil.mil.passes.defs.optimize_conv.add_conv_transpose_output_shape "Link to this definition")

:   The [`conv_transpose`] input [`output_shape`] is an optional input. Since we can infer the output shape from [`type_inference`], we add [`output_shape`] input whenever it is known to be constant at compile time. For example:

    :::: 
    ::: highlight
        Given:
          %1: (1, 5, 39, fp32) = conv_transpose(...) # no output_shape input.

        Result:
          %2: (3, i32) = const(val=[1,5,39])
          %3: (1, 5, 39, fp32) = conv_transpose(..., output_shape=%2)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_conv.]][[compose_conv1d]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_conv.html#compose_conv1d)[](#coremltools.converters.mil.mil.passes.defs.optimize_conv.compose_conv1d "Link to this definition")

:   In [TensorFlow](https://github.com/tensorflow/tensorflow/blob/r1.15/tensorflow/python/ops/nn_ops.py#L1657), [`tf.keras.layers.Conv1D`] is a composite op:

    :::: 
    ::: highlight
        expand a dummy dim -> Conv2D -> squeeze the dummy dim
    :::
    ::::

    In [PyTorch](https://github.com/pytorch/pytorch/blob/release/1.13/aten/src/ATen/native/Convolution.cpp#L1087), this is also true for some backends ([`mkldnn`] and [`xpu`]).

    This decomposition wrecks the coremltools [`conv1d`] graph passes, so we should recompose the fragments back to MIL [`conv`], which natively supports [`conv1d`]:

    :::: 
    ::: highlight
        Pattern 1:
            Given:
                %2 = expand_dims(%1, axes=-2) or expand_dims(%1, axes=2), %1.rank = 3
                %3 = conv(%2)
                %4 = squeeze(%3, axes=-2) or squeeze(%3, axes=2)
                ...

            Result:
                %4 = conv(%1)
                ...

        Pattern 2 (TensorFlow channel_last):
            Given:
                %2 = expand_dims(%1, axes=-3) or expand_dims(%1, axes=1), %1.rank = 3
                %3 = transpose(%2, perm=(0, 3, 1, 2))
                %4 = conv(%3)
                %5 = transpose(%4, perm=(0, 2, 3, 1))
                %6 = squeeze(%5, axes=-3) or squeeze(%5, axes=1)
                ...

            Result:
                %3 = transpose(%1, perm=(0, 2, 1))
                %4 = conv(%3)
                %6 = transpose(%4, perm=(0, 2, 1))
                ...
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_conv.]][[fuse_conv_batchnorm]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_conv.html#fuse_conv_batchnorm)[](#coremltools.converters.mil.mil.passes.defs.optimize_conv.fuse_conv_batchnorm "Link to this definition")

:   Fuse the following [`batch_norm`] layer into [`conv`] and [`conv_transpose`]. That is, convert [`conv`]` `[`+`]` `[`batch_norm`] to [`conv`], by modifying the weight and bias in the [`conv`] layer.

    :::: 
    ::: highlight
        Given:
            %2 = conv(%1)
            ...
            %3 = batch_norm(%2)
            ...

        Result:
            %3 = conv(%1)
            ...
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_conv.]][[fuse_conv_bias]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_conv.html#fuse_conv_bias)[](#coremltools.converters.mil.mil.passes.defs.optimize_conv.fuse_conv_bias "Link to this definition")

:   Fold [`add`]/[`sub`] into [`bias`] of [`conv`] and [`conv_transpose`]. That is, convert [`conv`]` `[`+`]` `[`add/sub`] to [`conv`], when [`add`]/[`sub`] is adding a constant.

    Two patterns are supported:

    :::: 
    ::: highlight
        Pattern 1:
        Given:
            %2 = conv(%1)
            ...
            %3 = add(%2, constant) # where constant has shape (1,C,1)/(C,1) for 1d conv, (1,C,1,1)/(C,1,1) for 2d conv etc
            ...

        Result:
            %3 = conv(%1)
            ...

        Pattern 2:
        Given:
            %2 = conv(%1)
            %3 = transpose(%2)
            ...
            %4 = add(%3, constant) # where constant has a broacasable shape
            ...

        Result:
            %2 = conv(%1)
            %4 = transpose(%2)
            ...
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_conv.]][[fuse_conv_scale]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_conv.html#fuse_conv_scale)[](#coremltools.converters.mil.mil.passes.defs.optimize_conv.fuse_conv_scale "Link to this definition")

:   Fold [`mul`]/[`div`] into [`conv`]/[`conv_transpose`] by updating the weight/bias of the convolution layers.

    The scale [`const`] can be a single number (scalar) or a vector with a broadcastable shape. For example, if the output of the [`conv`]/[`deconv`] layer is [`(B,`]` `[`Cout,`]` `[`H,`]` `[`W)`], [`const`] of shape [`(Cout,`]` `[`1,`]` `[`1)`] and [`(1,`]` `[`Cout,`]` `[`1,`]` `[`1)`] are allowed.

    :::: 
    ::: highlight
        Given:
            %2 = conv(%1)
            ...
            %3 = mul(%2, constant) # where constant is the scale constant
            ...

        Result:
            %3 = conv(%1)
            ...
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_conv.]][[fuse_pad_conv]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_conv.html#fuse_pad_conv)[](#coremltools.converters.mil.mil.passes.defs.optimize_conv.fuse_pad_conv "Link to this definition")

:   When we observe [`pad`]` `[`->`]` `[`transpose`]` `[`->`]` `[`conv`], we move the [`pad`] to be next to [`conv`]. This allows us to meld [`pad`]` `[`+`]` `[`conv`] if possible.

    :::: 
    ::: highlight
        Given:
            %1 = pad(%0, ...)
            %2 = transpose(%1, ...)
            %3 = conv(%2, ...)
            ...

        Result:
            %1.a = transpose(%0, ...)
            $2.a = pad(%1.a, ...)
            %3 = conv(%2.a)
            ...
    :::
    ::::

[]

## optimize_elementwise_binary[](#module-coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.]][[divide_to_multiply]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_elementwise_binary.html#divide_to_multiply)[](#coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.divide_to_multiply "Link to this definition")

:   Convert divide into multiply if the divisor is [`const`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.]][[select_optimization]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_elementwise_binary.html#select_optimization)[](#coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.select_optimization "Link to this definition")

:   For [`select(cond,`]` `[`a,`]` `[`b)`], there are 2 cases where we can replace it with a single simpler op

    1.  If [`cond`] is a const scalar (or a const tensor but all elements are the same, which is equivalent to a scalar), then we replace [`select(cond,`]` `[`a,`]` `[`b)`] with simply [`a`] or [`b`]

        :::: 
        ::: highlight
            Input graph:

                const(scalar cond) -|
                                    |
                a ------------------|-> select -> output
                                    |
                b ------------------|

            Output graph:

                if cond:
                    a -> output
                else:
                    b -> output
        :::
        ::::

    2.  If [`cond`] is a more complicated const, and [`a`] is an inf const, then we replace [`a`] with [`select(cond,`]` `[`a,`]` `[`0)`], then return [`a`]` `[`+`]` `[`b`]

        > ::::::: 
        > :::: 
        > ::: highlight
        >     Input graph:
        >
        >         const(cond) -|
        >                      |
        >         const(±inf) -|-> select -> output
        >                      |
        >         b -----------|
        >
        >     Output graph:
        >
        >         select(cond, ±inf, 0) -|
        >                                |-> add -> output
        >         b ---------------------|
        > :::
        > ::::
        >
        > Note that [`select(cond,`]` `[`±inf,`]` `[`0))`] will further get eliminated by [`const_elimination`], so in the end the op in graph is simply [`add`]
        >
        > This replacement is based on floating-point arithmetic
        >
        > :::: 
        > ::: highlight
        >     inf + b = inf
        >     -inf + b = -inf
        >     0 + b = b
        > :::
        > ::::
        >
        > PS: if [`a`] is not inf const but [`b`] is, then we would swap [`a`] and [`b`]
        > :::::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.]][[fuse_elementwise_to_batchnorm]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_elementwise_binary.html#fuse_elementwise_to_batchnorm)[](#coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.fuse_elementwise_to_batchnorm "Link to this definition")

:   Fold [`mul`] + [`add`] into a [`batchnorm`] if the [`const`] feeding into the [`mul`]/[`add`] is of shape [`(1,C,1,1)`] or [`(C,1,1)`] and input to [`mul`] is of rank 4.

    :::: 
    ::: highlight
        Given:
                 [Const]   [Const]
                    |         |
                    V         V
        [...] --> [Mul] --> [Add] --> [...]

        That is,

            %2 = op1(%1)
            %3 = mul(%2, constant)
            %4 = add(%3, constant)
            %5 = op2(%4)
            ...

        Result:

        [...] --> [BatchNorm] --> [...]

        That is,
            %2 = op1(%1)
            %4 = batchnorm(%2)
            %5 = op2(%4)
            ...
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.]][[rank0_expand_dims_swap]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_elementwise_binary.html#rank0_expand_dims_swap)[](#coremltools.converters.mil.mil.passes.defs.optimize_elementwise_binary.rank0_expand_dims_swap "Link to this definition")

:   Identify the pattern of a [`rank-0`] binary elementwise operation followed by an [`expand_dims`] op. In the MIL backend, the output of the [`elementwise`] op becomes rank 1. Hence, an [`expand_dims`] op should be added after both of the [`rank-0`] tensors, and the final [`expand_dims`] should be removed. If the output var of the binary elementwise op is consumed by more than one op, a [`squeeze`] op is inserted.

    Input

    :::: 
    ::: highlight
        [...](rank-0) --> sub --> expand_dims (axes=[0]) --> [...]
                           ^   |
                           |   |--> op2
                           |   |
                           |   |--> op3
                           |
                     [scalar const]
    :::
    ::::

    Output

    :::: 
    ::: highlight
        [...](rank-0) --> expand_dims (axes=[0]) --> sub --> [...]
                                                      ^   |
                                                      |   |--> squeeze ---> op2
                                                      |                |
                                                      |                |--> op3
                                                      |
                                                expand_dims (axes=[0])
                                                      ^
                                                      |
                                                      |
                                                [scalar const]
    :::
    ::::

[]

## optimize_linear[](#module-coremltools.converters.mil.mil.passes.defs.optimize_linear "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_linear.]][[fuse_linear_bias]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_linear.html#fuse_linear_bias)[](#coremltools.converters.mil.mil.passes.defs.optimize_linear.fuse_linear_bias "Link to this definition")

:   Convert [`linear`]` `[`+`]` `[`add/sub`] to a single [`linear`] by updating the weight and bias of the [`linear`] layer.

    :::: 
    ::: highlight
        Example 1:
            Original:
                %4 = linear(x=%1, weight=%2, bias=%3) # %2 is a rank-2 const tensor (weight)
                                                      # %3 is a rank-1 const tensor (bias)
                ...
                %6 = add(x=%4, y=%5) # %5 is a const tensor with same shape as %3

            Result:
                %8 = linear(x=%1, weight=%2, bias=%7) # where %7 is a new const tensor with value
                                                      # %7 = %3 + %6

        Example 2:
            Original:
                %4 = linear(x=%1, weight=%2, bias=%3) # %2 is a rank-2 const tensor (weight)
                                                      # %3 is a rank-1 const tensor (bias)
                ...
                %6 = sub(x=%5, y=%4) # %5 is a const tensor with a broacasable shape with %3.
                                       i.e. if %3 has shape (Dout), %5 could be (1, Dout).

            Result:
                %9 = linear(x=%1, weight=%7, bias=%8) # where %7 is a new const tensor with value %7 = -%2
                                                      # %8 = %5 - %3
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_linear.]][[fuse_matmul_weight_bias]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_linear.html#fuse_matmul_weight_bias)[](#coremltools.converters.mil.mil.passes.defs.optimize_linear.fuse_matmul_weight_bias "Link to this definition")

:   Convert [`matmul`]` `[`+`]` `[`add/sub`] to [`linear`] whenever possible.

    :::: 
    ::: highlight
        Given:
            %3 = matmul(x=%1, y=%2)  # %1 or %2 is const and rank 2 (weight)
            ...
            %5 = add(x=%3, y=%4) # %4 is const. add(x=%4, y=%3) is equivalent
                                 # sub is similar.

        Result:
            # assuming %2 above is const and rank 2
            %5 = linear(x=%1, weight=%2, bias=%4)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_linear.]][[fuse_transpose_matmul]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_linear.html#fuse_transpose_matmul)[](#coremltools.converters.mil.mil.passes.defs.optimize_linear.fuse_transpose_matmul "Link to this definition")

:   Fuse [`transpose`]` `[`+`]` `[`matmul`] to [`matmul`] if possible, since [`matmul`] has args [`transpose_x`] and [`transpose_y`] to transpose last 2 dims

    :::: 
    ::: highlight
        Positive example:
            Input graph:
                transpose(x=x, perm=(1, 0)) -|
                                             |-> matmul(x=transposed_x, y=transposed_y)
                transpose(x=y, perm=(1, 0)) -|

            Output graph:
                matmul(x=x, y=y, transpose_x=True, transpose_y=True)

        Negative example:
            Input graph:
                transpose(x=x, perm=(1, 0, 2)) -|
                                                |-> matmul(x=transposed_x, y=transposed_y)
                transpose(x=y, perm=(1, 0, 2)) -|

            Output graph:
                Same to input graph, nothing changes
    :::
    ::::

[]

## optimize_normalization[](#module-coremltools.converters.mil.mil.passes.defs.optimize_normalization "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_normalization.]][[fuse_layernorm_or_instancenorm]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_normalization.html#fuse_layernorm_or_instancenorm)[](#coremltools.converters.mil.mil.passes.defs.optimize_normalization.fuse_layernorm_or_instancenorm "Link to this definition")

:   A graph optimization pass on PyMIL to detect and fuse several variants of [`layer_norm`] or [`instance_norm`]. Pattern 1 corresponds to either [`layer_norm`] or [`instance_norm`]. Patterns 2-4 are [`instance_norm`]. Pattern 5 is [`layer_norm`]. You can find these patterns in the methods for this class in the source code. To quickly view the source code, click the **\[source\]** button at the end of the class definition.

[]

## optimize_quantization[](#module-coremltools.converters.mil.mil.passes.defs.optimize_quantization "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_quantization.]][[merge_affine_dequantize_with_consecutive_ops]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_quantization.html#merge_affine_dequantize_with_consecutive_ops)[](#coremltools.converters.mil.mil.passes.defs.optimize_quantization.merge_affine_dequantize_with_consecutive_ops "Link to this definition")

:   This graph pass does const folding to a chain of supported ops starts with a [`constexpr_affine_dequantize`] op. More types of op are supported when quantization is tensor-wise, and only a subset is supported for channel-wise. For example

    :::: 
    ::: highlight
        Input graph:
            data -> constexpr_affine_dequantize -> transpose -> expand_dims -> out

        Output graph:
            new_data -> constexpr_affine_dequantize -> out
    :::
    ::::

    where [`new_data`] is computed by [`data`]` `[`->`]` `[`transpose`]` `[`->`]` `[`expand_dims`].

    Note that, the graph pass only supports const folding of a single linked list pattern. For example, the following pattern will not be changed

    :::: 
    ::: highlight
              |-> constexpr_affine_dequantize -> transpose -> out
        data -|
              |-> constexpr_affine_dequantize -> reshape -> out_2
    :::
    ::::

    since the quantized data is used by multiple [`constexpr`]

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_quantization.]][[int_op_canonicalization]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_quantization.html#int_op_canonicalization)[](#coremltools.converters.mil.mil.passes.defs.optimize_quantization.int_op_canonicalization "Link to this definition")

:   For general quantized operators, in Core ML, we represent them as [`dequantize`]` `[`->`]` `[`the`]` `[`floating-point`]` `[`version`]` `[`of`]` `[`this`]` `[`operator`]` `[`->`]` `[`quantize`], because mathematically it is the floating-point tensor rather than its quantized integer representation that gets operated upon.

    For some quantized operators that do not involve floating-point arithmetic, however, it is unnecessary to prepend [`dequantize`] and append [`quantize`]. Examples are:

    - reshape

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_quantization.]][[nullify_redundant_quantization_zero_point]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_quantization.html#nullify_redundant_quantization_zero_point)[](#coremltools.converters.mil.mil.passes.defs.optimize_quantization.nullify_redundant_quantization_zero_point "Link to this definition")

:   In Core ML quantization, the performance is better when [`zero`]` `[`point`]` `[`=`]` `[`0`], so we try to make [`zero`]` `[`point`]` `[`=`]` `[`0`] if possible:

    - 

      [`zero`]` `[`point`]` `[`=`]` `[`-128`]

      :   - this must be an int8 quantization

          - equivalent to uint8 quantization with 0 zero point

    - 

      [`zero`]` `[`point`]` `[`=`]` `[`128`]

      :   - this must be an uint8 quantization

          - equivalent to int8 quantization with 0 zero point

    Since [`zero`]` `[`point`]` `[`=`]` `[`0`] is equivalent to [`zero`]` `[`point`]` `[`=`]` `[`None`] in Core ML semantics, we further canonicalize to [`zero`]` `[`point`]` `[`=`]` `[`None`] to:

    - make further graph passes easier

    - avoid serializing trivial 0

    The [`zero`]` `[`point`]` `[`=`]` `[`0`] case can be canonicalized trivially

    :::: 
    ::: highlight
        Input op:

            quantize/dequantize(zero_point=0)

        Output op:

            quantize/dequantize(zero_point=None)
    :::
    ::::

    To guarantee the conservation of output regardless the zero-point shift in [`zero`]` `[`point`]` `[`=`]` `[`±128`] cases, we would only transform:

    - const dequantize, where we fuse the zero-point shift into the const

    :::: 
    ::: highlight
        Input op:

            dequantize(input=const, zero_point=±128)

        Output op:

            dequantize(input=const∓128, zero_point=None)
    :::
    ::::

    - [`quantize`]` `[`->`]` `[`dequantize`], where we nullify both simultaneously

    :::: 
    ::: highlight
        Input graph:

            input -> quantize(zero_point=±128) -> dequantize(zero_point=±128) -> output

        Output graph:

            input -> quantize(zero_point=None) -> dequantize(zero_point=None) -> output
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_quantization.]][[dequantize_quantize_pair_elimination]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_quantization.html#dequantize_quantize_pair_elimination)[](#coremltools.converters.mil.mil.passes.defs.optimize_quantization.dequantize_quantize_pair_elimination "Link to this definition")

:   When a [`dequantize`] is followed by an identical [`quantize`] (same scale, zero point, axis), they cancel out and can be eliminated

    :::: 
    ::: highlight
        Input graph:
            input -> dequantize -> quantize -> output

        Output graph:
            input -> output
    :::
    ::::

    When the pattern has branches (dequantize has multiple children), we cannot eliminate the whole pair, but can still shorten the path. More specifically:

    :::: 
    ::: highlight
        Input graph:
            op1 -> dequantize -> quantize -> op2
                         |
                         |-> some_other_op

        Output graph:
            op1 -> dequantize -> some_other_op
             |
             |-> op2
    :::
    ::::

    PS: On the other hand, the reversed pattern, i.e., [`quantize`]` `[`->`]` `[`dequantize`], is not redundant, since that is the pattern which naturally occurs when a quantized op is converted. In current activation quantization conversion, a quantized op becomes

    :::: 
    ::: highlight
        dequantize -> regular op -> quantize
    :::
    ::::

    so if we have a sequence of quantized ops, we will get

    :::: 
    ::: highlight
        dequantize -> regular op1 -> quantize -> dequantize -> regular op2 -> quantize
    :::
    ::::

    The [`quantize`]` `[`->`]` `[`dequantize`] pair in the middle is not redundant, even if they have identical scales and zero points and axes, since removing them will lead to loss of information about the quantization parameters of the output var of op1

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_quantization.]][[distributive_quantized_binary_op_scale_normalization]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_quantization.html#distributive_quantized_binary_op_scale_normalization)[](#coremltools.converters.mil.mil.passes.defs.optimize_quantization.distributive_quantized_binary_op_scale_normalization "Link to this definition")

:   In the backend, for better performance, quantized op can have 1 input scale fused within the quantized op kernel. For binary ops, there are 2 inputs, but only 1 can get fused. For example, for quantized [`add`]

    :::: 
    ::: highlight
        MIL graph (consists of MIL ops):

            dequantize(x, s_x, zp_x) -|
            x_fp = (x - zp_x) * s_x   |
                                      |->  add(x_fp, y_fp)   -> quantize(z_fp, s_z, zp_z)
            dequantize(y, s_y, zp_y) -|   z_fp = x_fp + y_fp      z = z_fp / s_z + zp_z
            y_fp = (y - zp_y) * s_y

        Backend graph (consists of backend instructions, usually including + - * / and fused *+):

            x_shift = x - zp_x -------------------------|
                                                        |-> z_fp = s_x * x_shift + y_fp -> z = z_fp / s_z + zp_z
            y_shift = y - zp_y -> y_fp = s_y * y_shift -|
    :::
    ::::

    Where [`x`] and [`y`] are the inputs, [`z`] is the output, [`s`] and [`zp`] are the corresponding scale and zero point.

    The reason why fusing one scale leads to better performance is, instead of 2 instructions [`x_fp`]` `[`=`]` `[`s_x`]` `[`*`]` `[`x_shift`] and [`z_fp`]` `[`=`]` `[`x_fp`]` `[`+`]` `[`y_fp`], a single [`z_fp`]` `[`=`]` `[`x_shift`]` `[`*`]` `[`s_x`]` `[`+`]` `[`y_fp`] instruction achieves the same result.

    In this pass, we normalize [`s_y`] to 1, so the [`y_fp`]` `[`=`]` `[`s_y`]` `[`*`]` `[`y_shift`] instruction can get skipped as well, leading to even better performance. This pass only applies to distributive binary ops such as [`add`] and [`sub`]

    Appendix: Mathematical and Computer-Scientific Details

    Mathematically, for a binary operator [`.op.`]

    :::: 
    ::: highlight
        z_fp = (x - zp_x) * s_x .op. (y - zp_y) * s_y
             = s_y * [(x - zp_x) * s_x/s_y .op. (y - zp_y) * 1]
    :::
    ::::

    The corresponding pseudo code is

    :::: 
    ::: highlight
        # before
        z_fp = (x - zp_x) * s_x .op. (y - zp_y) * s_y
        z = z_fp / s - zp_z

        # after
        z_fp_modified = (x - zp_x) * s_x/s_y .op. (y - zp_y) * 1.0
        z = z_fp_modified / (s_z/s_y) - zp_z
    :::
    ::::

    Concretely, as a MIL graph pass

    :::: 
    ::: highlight
        Input graph:
            dequantize(scale=s_x) -|
                                   |-> op -> quantize(scale=s_z)
            dequantize(scale=s_y) -|

        Output graph:
            dequantize(scale=s_x/s_y) -|
                                       |-> op -> quantize(scale=s_z/s_y)
            dequantize(scale=1.0)     -|
    :::
    ::::

    PS: we only support scalar [`s_y`] for now. If [`s_y`] is not scalar but [`s_x`] is, we would swap [`x`] and [`y`]. Support for both-vector case is to be explored, due to the broadcasting complication.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_quantization.]][[dequantize_to_constexpr]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_quantization.html#dequantize_to_constexpr)[](#coremltools.converters.mil.mil.passes.defs.optimize_quantization.dequantize_to_constexpr "Link to this definition")

:   [`dequantize`] op with constant input is equivalent to [`constexpr_affine_dequantize`]. This is one of the canonicalization pass that transforms all such [`dequantize`] ops to respective [`constexpr_affine_dequantize`] ops.

    :::: 
    ::: highlight
        Input graph:

            dequantize(input=const) -> downstream op

        Output graph:

            constexpr_affine_dequantize -> downstream op
    :::
    ::::

    This pass is being performed because constant tensors being propagated through [`dequantize`] op would be serialized in bloated/decompressed fashion, whereas with [`constexpr_affine_dequantize`], constant weights/tensors remain compressed at serialization.

[]

## optimize_repeat_ops[](#module-coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.]][[cast_optimization]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_repeat_ops.html#cast_optimization)[](#coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.cast_optimization "Link to this definition")

:   This optimization pass performs the following:

    - Removes redundant [`cast`] op; that is, [`cast`] where source and destination tensors have same dtypes.

    - Fuses two consecutive cast ops if applicable, repeatedly.

    This is a non-algebraic translation which assumes that the upcasting doesn't change the user's intent.

    1.  Example for redundant [`cast`] op removal: .. code-block:

        :::: 
        ::: highlight
            Input graph:
            input(fp16) -> cast(dtype="fp16") -> relu -> out

            Output graph:
            input -> relu -> out
        :::
        ::::

        The input and output tensors for the [`cast`] op are both with type of [`fp16`]. Hence, it can be removed.

    2.  Example for two [`cast`] ops fusion: .. code-block:

        :::: 
        ::: highlight
            Input graph:
            input(int8) -> cast(dtype="fp16") -> cast(dtype="fp32") -> out

            Output graph:
            input(int8) -> cast(dtype="fp32") -> out
        :::
        ::::

        The data range and resolution of the above graph are limited by the int8 input, so the fusion is allowed.

    3.  Negative example for two [`cast`] ops fusion: .. code-block:

        :::: 
        ::: highlight
            Input graph:
            input(fp32) -> cast(dtype="bool") -> cast(dtype="fp16") -> out

            Output graph:
            Same as input graph.
        :::
        ::::

        The above two [`cast`] ops cannot be merged, since after the first cast, the resolution of the numerical output is downcasted to binary ([`0,`]` `[`1`]). If we fuse them, the output would be in the range and resolution of [`fp16`] instead.

    4.  Another Negative example for two [`cast`] ops fusion: .. code-block:

        :::: 
        ::: highlight
            Input graph:
            input(int32) -> cast(dtype="int8") -> cast(dtype="uint8") -> out

            Output graph:
            Same as input graph.
        :::
        ::::

        The above two [`cast`] ops cannot be merged, since in the original graph, by going through two casts, the output numerical range is capped to [`[0,`]` `[`127]`]. However, if two [`cast`] ops are reduced to 1 [`cast(dtype="uint8")`], the output numerical would in the range of [`[0,`]` `[`255]`]. The fusion would cause numerical issue for the numbers between [`[128,`]` `[`255]`], which is prohibited.

    In general, two [`cast`] ops can be merged if the output data range and resolution is not affected.

    For more examples, please see the unittests that start with prefix [`TestCastOptimization`] in [`test_passes.py`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.]][[merge_consecutive_paddings]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_repeat_ops.html#merge_consecutive_paddings)[](#coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.merge_consecutive_paddings "Link to this definition")

:   Identify two consecutive [`pad`] layers which could be merged into a single [`pad`] layer.

    This is possible only if one of the following conditions is satisfied:

    - The paddings are "constant" and have the same [`constant_val`].

    - The paddings act along different axes.

    :::: 
    ::: highlight
        Input graph:
        input(1, 2, 6, 8) ------> pad([1, 1], mode='reflect) -----> pad([1, 1, 0, 0], mode='reflect') ---> out(1, 2, 8, 10)

        Output graph:
        input(1, 2, 6, 8) ------> pad([1, 1, 1, 1], mode='reflect) ---> out(1, 2, 8, 10)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.]][[merge_consecutive_relus]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_repeat_ops.html#merge_consecutive_relus)[](#coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.merge_consecutive_relus "Link to this definition")

:   Identify consecutive [`relu`] layers which could be merged into a single [`relu`] layer.

    :::: 
    ::: highlight
        Input graph:
        input ------> relu -----> 1 or more relu layers ---> out

        Output graph:
        input ------> relu ---> out
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.]][[merge_consecutive_reshapes]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_repeat_ops.html#merge_consecutive_reshapes)[](#coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.merge_consecutive_reshapes "Link to this definition")

:   Identify consecutive [`reshape`] ops which could be merged into a single [`reshape`].

    :::: 
    ::: highlight
        Input graph:
        input -> reshape -> 1 or more reshapes -> output

        Output graph:
        input -> reshape -> output
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.]][[merge_consecutive_transposes]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_repeat_ops.html#merge_consecutive_transposes)[](#coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.merge_consecutive_transposes "Link to this definition")

:   Identify consecutive 'transpose' layers which could be merged into a single 'transpose' layer.

    :::: 
    ::: highlight
        Input graph:
        input ------> transpose -----> 1 or more transpose layers ---> out

        Output graph:
        input ------> transpose ---> out
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.]][[reduce_transposes]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_repeat_ops.html#reduce_transposes)[](#coremltools.converters.mil.mil.passes.defs.optimize_repeat_ops.reduce_transposes "Link to this definition")

:   Reduce transposes when it is applicable. For example:

    :::: 
    ::: highlight
        # Example 1
            Input graph:
            input -----> transpose(axis=[1,0]) -----> transpose(axis=[1,0]) ---> out

            Output graph:
            input -----> identity -----> out

        # Example 2
            Input graph:
            input---->transpose(axis=[0,3,1,2])---->relu---->transpose(axis=[0,2,3,1])--->out

            Output graph:
            input----->relu----->out

        # Example 3
            Input graph:
            input(shape=10,2,3,5)--->transpose(axis=[0,2,3,1])----->relu---->pool----->out1
                                                               |
                                                               |
                                                               --->relu----->log---->transpose(axis=[0,3,1,2])---->out2

            Output graph:
            input(shape=10,2,3,5)----->relu---->transpose(axis=[0,2,3,1])---->pool----->out1
                                   |
                                   |
                                   --->relu----->log---->out2
    :::
    ::::

    Please see [`TransposeOptimizationPass`] for more details.

    Notes

    This pass is divided into 3 phases:

    1st phase: Information gathering.

    - Plug in Identity ops for all output nodes. This allows us to treat all ops uniformly during traversal.

    - Block is traversed in the topological order, starting from the ops connected to the inputs.

    - During the traversal, a value is associated with every var in the block. This value can be either of type [`_HypotheticalValue`] or [`_LazyTransposeHypotheticalValue`]. The main purpose of type [`_HypotheticalValue`] is to indicate that it is not of type [`_LazyTransposeHypotheticalValue`].

    - [`_LazyTransposeHypotheticalValue`] represents either one or multiple transpose ops with the same perm value. This information is stored in this class. It also wraps a [`_HypotheticalValue`] that was the last hypothetical value which was generated prior to the origin of [`_LazyTransposeHypotheticalValue`].

    - Each op decides which type of hypothetical value to associate with its output vars, based on its op type, attributes, and the types of the hypothetical values of its input vars.

    - Ops are classified into 4 categories: unary like, axis update, transpose, and materialize (for all the rest).

    - 

      Transpose ops are the ops from which a [`_LazyTransposeHypotheticalValue`] originate.

      :   - If the input to it is a [`_HypotheticalValue`], its output will be a [`_LazyTransposeHypotheticalValue`], indicating that this [`transpose`] op is available to get cancelled downstream.

          - 

            If the input to it is a [`_LazyTransposeHypotheticalValue`], then it is checked whether this op cancels it or not.

            :   - If the op cancels it, a [`_HypotheticalValue`] value is generated at the output and the information about this [`transpose`] cancellation is recorded in the dictionary [`transpose_op_to_cancel_ops`].

                - If the op does not cancel, the current [`transpose`] op is categrorized as a materialize op. Therefore, the information in dictionary [`transpose_op_to_materialize_ops`] is updated accordingly. The output of the op is now mapped to a [`_HypotheticalValue`].

    - Unary like ops: These simply transfer their input hypothetical value type to the output.

    - Axis update ops: If a [`transpose`] can pass through them, they are treated like a unary op and the dictionary [`transpose_op_to_axis_update_ops`] is updated. If the op cannot be updated in any manner to allow a [`transpose`] to pass through, this op is then categorized as a materialize op and handled accordingly.

    - Materialize ops: All [`_LazyTransposeHypotheticalValue`] input vars, if present, materialize here. Output of this op is always of type [`_HypotheticalValue`]. If the input is a [`_LazyTransposeHypotheticalValue`], update the dictionary [`transpose_op_to_materialize_ops`].

    - To treat an op like a unary op, add its type to [`_UNARY_LIKE_OP_TYPES`]. In future changes we want to make this process automatic by detecting an op as a unary like by its "traits".

    - To treat an op like axis update op, add a class specific to the op implementing the class [`TransformAxisUpdateOps`]. For examples, see classes [`_TransformConcat`], [`_TransformPad`], and so on. The dictionary [`AXIS_UPDATE_OPS`] is automatically filled in by the decorator [`_TransposeOptimization.register_axis_update_op`].

    2nd phase: Determining which [`transpose`] ops to remove from the graph.

    All [`transpose`] ops that have a corresponding compliment op in dict [`transpose_op_to_cancel_ops`] is a candidate. However, you need to ensure the following:

    - If a [`transpose`] op is removed, then all of its [`cancel`] ops in [`transpose_op_to_cancel_ops`] must also be removed, to ensure correctness of the graph. The same is true in the reverse direction as well; that is, for every [`cancel`] op that is removed, all its parent [`transpose`] ops upstream must also be removed.

    - [`transpose`] ops should be removed only if the number of [`cancel`] ops is greater than the number of [`transpose`] ops that would get freshly introduced to the block as a result of materialization ops. Currently in the algorithm, each materialization op/output var (dicts [`transpose_op_to_materialize_ops`]/[`old_output_vars`]) results in one more [`transpose`] op, although this can be further optimized in the future.

    To resolve this, we recognize that nodes consisting of sets [`(a)`] and [`(b)`] form a bipartitle graph, where, [`(a)`]` `[`==`] starting [`transpose`] ops (originators of [`_LazyTransposeHypotheticalValue`]) and [`(b)`]` `[`==`] set of [`transpose`] [`cancel`] ops and [`materialize`] ops.

    - In this bipartite graph, we find all the connected components for each connected component. Either the entire set of [`transpose`] ops in it are removed/materialized, or none of them are touched.

    - Thus for each set, a determination is made based on counting the number of [`cancel`] ops and [`materialize`] ops.

    - Based on this determination, the final set of [`transpose`] ops to be removed is updated.

    3rd phase: Transforming the graph.

    - [`transpose`] starting ops and the [`cancel`] ops are removed.

    - Axis update ops, affected by these [`transpose`] ops, are updated.

    - Transposes are materialized; that is, added just before the [`materialize`] ops, which are linked to the starting [`transpose`] ops. The starting [`transpose`] op can be materialized (inserted) multiple times, before each of the [`materialize`] ops downstream.

    - Block outputs are handled in a similar fashion as the materialize ops.

    - Type inference on all ops is invoked after all the transformations.

    - All Identity ops that are plugged into the graph to treat outputs as materialized are removed.

    Debugging

    If the [`debug`] flag is set to [`True`], the block before and after the transformation is plotted, with transpose nodes highlighted.

[]

## optimize_state[](#module-coremltools.converters.mil.mil.passes.defs.optimize_state "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_state.]][[canonicalize_inplace_pattern]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_state.html#canonicalize_inplace_pattern)[](#coremltools.converters.mil.mil.passes.defs.optimize_state.canonicalize_inplace_pattern "Link to this definition")

:   As a functional-graph framework, Core ML represents in-place operation as

    :::: 
    ::: highlight
        read_state -> functional operation -> write_state
    :::
    ::::

    Due to the non-uniqueness of topological order, in the list representation of ops, [`write_state`] can be anywhere after the functional op. We prefer the canonical order, i.e. have [`write_state`] immediately follow the functional op

    In practice

    1\. In PyMIL, we do not use [`write_state`] op. Instead, we use [`coreml_update_state`], which is the composition of [`write_state`]` `[`->`]` `[`read_state`]

    2.  The [`read_state`] op does not matter in the pattern match and transform

    So we will match

    :::: 
    ::: highlight
        functional operation -> coreml_update_state
    :::
    ::::

    then reorder the [`coreml_update_state`]. For example

    :::: 
    ::: highlight
        Given:

            mul = mul(state, x)
            add = add(mul, y)
            update = coreml_update_state(state, mul)

        Return:

            mul = mul(state, x)
            update = coreml_update_state(state, mul)
            add = add(mul, y)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_state.]][[prefer_state_in_downstream]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_state.html#prefer_state_in_downstream)[](#coremltools.converters.mil.mil.passes.defs.optimize_state.prefer_state_in_downstream "Link to this definition")

:   As a functional-graph framework, Core ML represents in-place operation as

    :::: 
    ::: highlight
        read_state -> functional operation -> write_state
    :::
    ::::

    When the output of the in-place operation is used downstream, there are 2 possible patterns, one reuses state memory

    :::: 
    ::: highlight
        read_state -> functional operation -> write_state -> read_state -> ...
    :::
    ::::

    the other wastes memory for keeping functional output

    :::: 
    ::: highlight
                                            |-> write_state
        read_state -> functional operation -|
                                            |-> ...
    :::
    ::::

    We prefer the reuse-state one

    In practice

    1\. In PyMIL, we do not use [`write_state`] op. Instead, we use [`coreml_update_state`], which is the composition of [`write_state`]` `[`->`]` `[`read_state`]

    2\. With canonical inplace pattern (guaranteed by graph pass [`canonicalize_inplace_pattern`]), simply replace the usage of functional output with [`coreml_update_state`] output is enough

    For example

    :::: 
    ::: highlight
        Given:

            mul = mul(state, x)
            update = coreml_update_state(state, mul)
            add = add(mul, y)

        Return:

            mul = mul(state, x)
            update = coreml_update_state(state, mul)
            add = add(update, y)
    :::
    ::::

[]

## optimize_tensor_operation[](#module-coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.]][[concat_to_pixel_shuffle]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_tensor_operation.html#concat_to_pixel_shuffle)[](#coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.concat_to_pixel_shuffle "Link to this definition")

:   Identify nested, interleaved [`concat`] ops which can be replaced by a single [`concat`] and a pixel shuffle layer.

    This pattern occurs with the faster up-convolution from the FCRN model (Laina et al., 2016).

    :::: 
    ::: highlight
        # Before the concat_to_pixel_shuffle pass.
        input(N, C, H, W) -------------------
                                            |
                                            v
        input(N, C, H, W) -----> concat(axis=2, interleave=True) -----> concat(axis=3, interleave=True) ----> output
                                                                                    ^
                                                                                    |
        input(N, C, H, W) -----> concat(axis=2, interleave=True) --------------------
                    |                       ^
                    |                       |
        input(N, C, H, W) -------------------

        # After the concat_to_pixel_shuffle pass.
        input(N, C, H, W) ---------------
                                        |
                                        v
        input(N, C, H, W) -----> concat(axis=1, interleave=True) -----> pixel_shuffle(upscale_factor=2) ----> output
                                        ^
                                        |
        input(N, C, H, W) --------------|
                                        |
                                        |
        input(N, C, H, W) ---------------
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.]][[detect_concat_interleave]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_tensor_operation.html#detect_concat_interleave)[](#coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.detect_concat_interleave "Link to this definition")

:   Detect the pattern [`concat-->reshape--->transpose--->reshape`], where [`concat`] is along the channel axis [`(axis=-3)`], and map this pattern to the [`concat`] with [`interleave`] op.

    This pattern occurs, for example, in the [`shufflenet`] model in [`torchvision`].

    :::: 
    ::: highlight
        Given:
            %3 = concat(%1.a, %1.b, ..., axis=-3, interleave=False) #shape = (B, n*C, H, W)
            %4 = reshape(%3) #shape = (B, n, C, H, W)
            %5 = transpose(%4, perm=[0, 2, 1, 3, 4]) # shape = (B, C, n, H, W)
            %6 = reshape(%5) # shape = (B, C*n, H, W)

        Result:
            %6 = concat(%1.a, %1.b, ..., axis=-3, interleave=True)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.]][[expand_high_rank_reshape_and_transpose]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_tensor_operation.html#expand_high_rank_reshape_and_transpose)[](#coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.expand_high_rank_reshape_and_transpose "Link to this definition")

:   Detect the pattern [`reshape_1-->transpose-->reshape_2`], where [`reshape_1`] has an output tensor with [`rank`]` `[`>=`]` `[`6`], and [`reshape_2`] produces a tensor with [`rank`]` `[`<=`]` `[`5`].

    In general, we can expand this pattern into a sequence of rank 4 [`reshape`] and [`transpose`] ops, which is supported by the Core ML runtime.

    :::: 
    ::: highlight
        Given:
            %1 = reshape(%x, shape=(d1, d2, d3, d4, ..., dn))
            %2 = transpose(%1, perm=(p1, p2, ..., pn))
            %3 = reshape(%2, shape=(o1, o2, o3, o4, o5))

        Result:
            %t1 = reshape(%x, shape=(y11, y12, y13, y14))
            %h1 = transpose(%t1, perm=[0, 2, 1, 3])
            %t2 = reshape(%h1, shape=(y21, y22, y23, 214))
            %h2 = transpose(%t2, perm=[0, 2, 1, 3])
            ....
            %hn = transpose(%tn, perm=[0, 2, 1, 3])
            %3 = reshape(%hn, shape=(o1, o2, o3, o4, o5))
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.]][[fuse_onehot_matmul_to_gather]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_tensor_operation.html#fuse_onehot_matmul_to_gather)[](#coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.fuse_onehot_matmul_to_gather "Link to this definition")

:   Detect if [`onehot`]` `[`(axis=-1,`]` `[`on_value=1,`]` `[`off_value=0)`] is followed by a [`matmul`] op (no bias). If so, they can be replaced by a [`gather`] op.

    :::: 
    ::: highlight
        Input:
            %2 = one_hot(%1, on_value=1, off_value=0, axis=-1)
            %3 = const() # rank 2
            %4  = matmul(%2, %3)

        Output:
            %4 = gather(%3, %2, axis=0)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.]][[replace_stack_reshape]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_tensor_operation.html#replace_stack_reshape)[](#coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.replace_stack_reshape "Link to this definition")

:   A stack followed by a reshape layer can be replaced by a [`concat`] if the reshape simply removes the new axis and doubles the size of one of the axes next to it.

    If the new axis is reshaped to the "right" (that is, the axis just after it is doubled), then we can use a [`concat`]. If it is reshaped to the "left" (the axis just before it is doubled), then the [`concat`] needs to set the [`interleaved`] flag.

    Examples:

    :::: 
    ::: highlight
        Given:
            %1 = tensor(1, 5, 3, 4)
            %2 = tensor(1, 5, 3, 4)
            %3 = stack((%1,%2), axis=2) # shape = (1, 5, 2, 3, 4)
            %4 = reshape(%3, shape=[1, 10, 3, 4])

        Result:
            %1 = tensor(1, 5, 3, 4)
            %2 = tensor(1, 5, 3, 4)
            %4 = concat((%1,%2), axis=1, interleave=True) # shape = (1, 10, 3, 4)

        Given:
            %1 = tensor(1, 5, 3, 4)
            %2 = tensor(1, 5, 3, 4)
            %3 = stack((%1, %2), axis=1) # shape = (1, 2, 5, 3, 4)
            %4 = reshape(%3, shape=[1, 10, 3, 4])

        Result:
            %1 = tensor(1, 5, 3, 4)
            %2 = tensor(1, 5, 3, 4)
            %4 = concat((%1, %2), axis = 1) # shape = (1, 10, 3, 4)
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.]][[use_reflection_padding]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/optimize_tensor_operation.html#use_reflection_padding)[](#coremltools.converters.mil.mil.passes.defs.optimize_tensor_operation.use_reflection_padding "Link to this definition")

:   Identify a reflection padding layer composed out of slices and concats.

    :::: 
    ::: highlight
        Input graph:

                ------------------------------------------------------------------------------------- |
                |                                                                                     v
        input(1, 2, 6, 8) ------> slice_by_index(begin=[0, 0, 0, 1], end=[0, 0, 0, 2]) -----> concat(axis=3) ---> out(1, 2, 6, 10)
                |                                                                                     ^
                ----------------> slice_by_index(begin=[0, 0, 0, -2], end=[0, 0, 0, -1]) -------------|

        Output graph:

        input(1, 2, 6, 8) -----0> pad(mode=reflect, size=[0, 0, 1, 1]) -----> out(1, 2, 6, 10)
    :::
    ::::

[]

## preprocess[](#module-coremltools.converters.mil.mil.passes.defs.preprocess "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.preprocess.]][[image_input_preprocess]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/preprocess.html#image_input_preprocess)[](#coremltools.converters.mil.mil.passes.defs.preprocess.image_input_preprocess "Link to this definition")

:   Plug in to [`transpose`] image input in NHWC format to NCHW format.

    Follow these steps:

    1.  Check whether there are any inputs that the users specify as ImageType.

    2.  Check the channel's dimension for all inputs that are ImageType.

        > ::: 
        > 1.  [`channel_first`]` `[`==`]` `[`True`] We do not modify this input, since [`channel_first`] is the intended behaviour for feeding images for optimal performance.
        >
        > 2.  [`channel_first`]` `[`==`]` `[`False`] We convert the input into a "channel_first" input, and plug in a [`transpose`] for the input to maintain the remaining graph's dimensionality.
        > :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.preprocess.]][[sanitize_input_output_names]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/preprocess.html#sanitize_input_output_names)[](#coremltools.converters.mil.mil.passes.defs.preprocess.sanitize_input_output_names "Link to this definition")

:   Sanitize the names of model input and output vars to make sure that they are of the format as described in the NameSanitizer class; that is, of the format [`[a-zA-Z_][a-zA-Z0-9_]*`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.preprocess.]][[update_output_dtypes]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/preprocess.html#update_output_dtypes)[](#coremltools.converters.mil.mil.passes.defs.preprocess.update_output_dtypes "Link to this definition")

:   Update the dtypes of output vars of each function block to match the dtypes provided in [`function.output_types`]. The output types for the main function is populated by the [`outputs`] argument provided by the user in the [`coremltools.convert()`] API. This graph pass assumes that the list of outputs in [`function.output_types`] (if not [`None`]), are in the same order as the output vars.

[]

## quantization[](#module-coremltools.converters.mil.mil.passes.defs.quantization "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.quantization.]][[add_fp16_cast]][(]*[[op_selector]][[=]][[None]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/quantization.html#add_fp16_cast)[](#coremltools.converters.mil.mil.passes.defs.quantization.add_fp16_cast "Link to this definition")

:   For each input of dtype float32, inject a [`cast`] op to change it to float16 dtype.

    For each output of dtype float16, inject a [`cast`] op to change it back to float32.

    This pass is the registered interface for FP16ComputePrecision, which makes it consistent with other passes' interfaces.

    Support options:

    - [`skip_ops_by_type`]: Skip op types specified by comma-separated string; for example, [`"mul,const"`].

[]

## symbol_transform[](#module-coremltools.converters.mil.mil.passes.defs.symbol_transform "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.symbol_transform.]][[materialize_symbolic_shape_program]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/symbol_transform.html#materialize_symbolic_shape_program)[](#coremltools.converters.mil.mil.passes.defs.symbol_transform.materialize_symbolic_shape_program "Link to this definition")

:   If we realize that only a few fixed shapes are used in a symbolic-shape model, we may prefer materialization into a fixed-shape (multifunction) model, which has the potential to be further optimized

    Supported options:

    - 

      [`function_name_to_materialization_map`]: Dict\[str, Dict\[str, Tuple\[int\]\]\]

      :   A dictionary specifying the name of new functions to be created, and for each new function what is the new fixed shapes for inputs. If a new function has the same name as an old function, then the old function will be overridden

    - 

      [`source_function_name`]: str

      :   The name of the source symbolic-shape function to be materialized, default = main

    Example:

    Suppose we have a symbolic shape model with 2 symbols [`is0`] and [`is1`]

    :::: 
    ::: highlight
        symbolic_shape_mlmodel: ct.models.MLModel
        symbolic_shape_prog = symbolic_shape_mlmodel._mil_program
    :::
    ::::

    We may invoke this graph pass to materialize some fixed shapes (e.g. [`is0`]` `[`=`]` `[`2,`]` `[`is1`]` `[`=`]` `[`5`] and [`is0`]` `[`=`]` `[`4,`]` `[`is1`]` `[`=`]` `[`7`]), then run every other optimization passes

    :::: 
    ::: highlight
        pass_pipeline: PassPipeline = ct.PassPipeline.DEFAULT
        pass_pipeline.insert_pass(0, "common::materialize_symbolic_shape_program")
        pass_pipeline.set_options(
            "common::materialize_symbolic_shape_program",
            ,
                    "materialization_4_7": ,
                }
            },
        )
        PassPipelineManager.apply_pipeline(symbolic_shape_prog, pass_pipeline)
    :::
    ::::

    We will arrive at

    :::: 
    ::: highlight
        main[CoreML8](%x: (is0, is1, 1024, fp16)(Tensor))  -> (%y)
        }

        materialization_2_5[CoreML8](%x: (2, 5, 1024, fp16)(Tensor))  -> (%y)
        }

        materialization_4_7[CoreML8](%x: (4, 7, 1024, fp16)(Tensor))  -> (%y)
        }
    :::
    ::::

[]

## transformer[](#module-coremltools.converters.mil.mil.passes.defs.transformer "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.passes.defs.transformer.]][[scaled_dot_product_attention_sliced_q]][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/passes/defs/transformer.html#scaled_dot_product_attention_sliced_q)[](#coremltools.converters.mil.mil.passes.defs.transformer.scaled_dot_product_attention_sliced_q "Link to this definition")

:   Replace the ios18.scaled_dot_product_attention operation with a memory efficient implementation of attention calculation based on slicing Q. The benefits are clearly visible for higher Q sequence lengths, though.

    Graph pass options:

    :   - min_seq_length: int Only operations working with Q of sequence length greater or equal to this value will be transformed.

        - seq_length_divider: int Defines the size of the chunks of Q being processed in SDPA (chunk_size = seq_length / seq_length_divider)