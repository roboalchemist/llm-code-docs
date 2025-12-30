# Source: https://apple.github.io/coremltools/source/coremltools.converters.mil.mil.ops.defs.html

# MIL Ops[](#mil-ops "Link to this heading")

Operators supported by the Model Intermediate Language (MIL):

[]

## activation (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.activation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[clamped_relu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#clamped_relu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.clamped_relu "Link to this definition")

:   If [`x`]` `[`>=`]` `[`0`] return elementwise [`min(beta,`]` `[`x)`], otherwise return [`min(beta,`]` `[`alpha`]` `[`*`]` `[`x)`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

        **beta: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same type and shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[elu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#elu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.elu "Link to this definition")

:   If [`x`]` `[`>`]` `[`0`] return elementwise [`x`], otherwise return [`alpha`]` `[`*`]` `[`(e^x`]` `[`-`]` `[`1)`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[gelu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#gelu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.gelu "Link to this definition")

:   Return the elementwise Gaussian error linear unit activation function for [`x`].

    You can use [`EXACT`], [`TANH_APPROXIMATION`], or [`SIGMOID_APPROXIMATION`] values based on the following formulas:

    - [`EXACT`]:

    ::: 
    \\\[f(x) = 0.5x\\left ( 1+\\rm\\left ( \\frac} \\right ) \\right )\\\]
    :::

    - [`TANH_APPROXIMATION`]:

    ::: 
    \\\[f(x) = 0.5x\\left ( 1+\\rm\\left ( \\sqrt\\left ( x + 0.044715x\^3 \\right ) \\right ) \\right )\\\]
    :::

    - [`SIGMOID_APPROXIMATION`]:

    ::: 
    \\\[f(x) = x\*\\rm(1.702x)\\\]
    :::

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **mode: const str (Optional)**

        :   - Use [`'EXACT'`], [`'TANH_APPROXIMATION'`], or [`'SIGMOID_APPROXIMATION'`] for [`str`].

            - Default is [`'EXACT'`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[leaky_relu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#leaky_relu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.leaky_relu "Link to this definition")

:   If [`x`]` `[`>=`]` `[`0`] apply [`x`] elementwise, otherwise apply [`alpha`]` `[`*`]` `[`x`] elementwise.

    Parameters[:]

    :   

        **x: \<\*?, T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[linear_activation]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#linear_activation)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.linear_activation "Link to this definition")

:   Apply elementwise [`x`]` `[`*`]` `[`alpha`]` `[`+`]` `[`beta`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

        **beta: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[prelu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#prelu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.prelu "Link to this definition")

:   Where [`i`]` `[`=`]` `[`1`]` `[`...`]` `[`C`], if [`x_i`]` `[`>`]` `[`0`], return [`x_i`] , otherwise return [`alpha_i`]` `[`*`]` `[`x_i`].

    Parameters[:]

    :   

        **x: tensor\<\[B, C, 1..3\], T\> (Required)**

        :   - [`x`] must have rank 4, rank 3, or rank 5; that is, a shape of [`(B,C,H)`], [`(B,C,H,W)`], or [`(B,C,D,H,W)`].

        **alpha: const tensor\<\[C\], T\>, (Required)**

        :   - The length of [`alpha`] must match the second dimension of [`x`] (channel dimension).

    Attributes[:]

    :   

        **T: fp32, fp16**

        :   

    Returns[:]

    :   

        tensor\<\[B, C, 1..3\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[relu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#relu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.relu "Link to this definition")

:   Return elementwise-applied rectified linear activation: [`max(x,`]` `[`0)`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[relu6]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#relu6)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.relu6 "Link to this definition")

:   Return elementwise-applied rectified linear activation: [`min(max(x,`]` `[`0),`]` `[`6)`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[scaled_tanh]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#scaled_tanh)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.scaled_tanh "Link to this definition")

:   Return [`alpha`]` `[`*`]` `[`tanh(beta`]` `[`*`]` `[`x)`] elementwise.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input range is [`(-inf,`]` `[`inf)`].

        **alpha: const T (Required)**

        :   

        **beta: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[sigmoid]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#sigmoid)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.sigmoid "Link to this definition")

:   Return [`sigmoid(x)`] elementwise.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[sigmoid_hard]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#sigmoid_hard)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.sigmoid_hard "Link to this definition")

:   Return [`min(`]` `[`max(`]` `[`alpha`]` `[`*`]` `[`x`]` `[`+`]` `[`beta,`]` `[`0`]` `[`),`]` `[`1`]` `[`)`] elementwise.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

        **beta: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[silu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#silu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.silu "Link to this definition")

:   Sigmoid Linear Unit, elementwise apply the SiLU or Swish operation [`x`]` `[`*`]` `[`sigmoid(x)`].

    Parameters[:]

    :   

        **x: tensor\<\*, T\>**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*, T\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[softplus]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#softplus)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.softplus "Link to this definition")

:   Return [`log(`]` `[`1`]` `[`+`]` `[`e^x`]` `[`)`] elementwise.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[softplus_parametric]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#softplus_parametric)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.softplus_parametric "Link to this definition")

:   Return [`alpha_i`]` `[`*`]` `[`log(`]` `[`1`]` `[`+`]` `[`e^(`]` `[`beta_i`]` `[`*`]` `[`x_i`]` `[`)`]` `[`)`], where [`i`]` `[`=`]` `[`1`]` `[`...`]` `[`C`].

    Parameters[:]

    :   

        **x: tensor\<\[b, C, n, m\], T\> (Required)**

        :   

        **alpha: const tensor\<\[C\], T\> (Required)**

        :   

        **beta: const tensor\<\[C\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[b, C, n, m\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[softmax]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#softmax)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.softmax "Link to this definition")

:   Return [`exp(x)`]` `[`/`]` `[`tf.reduce_sum(tf.exp(x),`]` `[`axis)`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **axis: const i32 (Optional)**

        :   - Default is [`-1`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[softsign]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#softsign)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.softsign "Link to this definition")

:   Return [`x`]` `[`/`]` `[`(`]` `[`1`]` `[`+`]` `[`|x|`]` `[`)`] applied elementwise.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.activation.]][[thresholded_relu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html#thresholded_relu)[](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.thresholded_relu "Link to this definition")

:   Return [`x`] if [`x`]` `[`>=`]` `[`alpha`], otherwise return [`0`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*, T\>

        :   - A tensor of the same shape and type as [`x`].

[]

## activation (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.activation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[clamped_relu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#clamped_relu)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.clamped_relu "Link to this definition")

:   If [`x`]` `[`>=`]` `[`0`] return elementwise [`min(beta,`]` `[`x)`], otherwise return [`min(beta,`]` `[`alpha`]` `[`*`]` `[`x)`].

    The major difference between this version and the iOS 15 [[`clamped_relu`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.clamped_relu "coremltools.converters.mil.mil.ops.defs.iOS15.activation.clamped_relu") is that the [`alpha`] and [`beta`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const U (Required)**

        :   

        **beta: const U (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same type and shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[elu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#elu)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.elu "Link to this definition")

:   If [`x`]` `[`>`]` `[`0`] return elementwise [`x`], otherwise return [`alpha`]` `[`*`]` `[`(e^x`]` `[`-`]` `[`1)`].

    The major difference between this version and the iOS 15 [[`elu`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.elu "coremltools.converters.mil.mil.ops.defs.iOS15.activation.elu") is that the [`alpha`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const U (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[leaky_relu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#leaky_relu)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.leaky_relu "Link to this definition")

:   If [`x`]` `[`>=`]` `[`0`] apply [`x`] elementwise, otherwise apply [`alpha`]` `[`*`]` `[`x`] elementwise.

    The major difference between this version and the iOS 15 [[`leaky_relu`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.leaky_relu "coremltools.converters.mil.mil.ops.defs.iOS15.activation.leaky_relu") is that the [`alpha`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: \<\*?, T\> (Required)**

        :   

        **alpha: const U (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[linear_activation]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#linear_activation)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.linear_activation "Link to this definition")

:   Apply elementwise [`x`]` `[`*`]` `[`alpha`]` `[`+`]` `[`beta`].

    The major difference between this version and the iOS 15 [[`linear_activation`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.linear_activation "coremltools.converters.mil.mil.ops.defs.iOS15.activation.linear_activation") is that the [`alpha`] and [`beta`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const U (Required)**

        :   

        **beta: const U (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[prelu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#prelu)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.prelu "Link to this definition")

:   Where [`i`]` `[`=`]` `[`1`]` `[`...`]` `[`C`], if [`x_i`]` `[`>`]` `[`0`], return [`x_i`] , otherwise return [`alpha_i`]` `[`*`]` `[`x_i`].

    The major difference between this version and the iOS 15 [[`prelu`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.prelu "coremltools.converters.mil.mil.ops.defs.iOS15.activation.prelu") is that the [`alpha`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\[B, C, 1..3\], T\> (Required)**

        :   - [`x`] must have rank 4, rank 3, or rank 5; that is, a shape of [`(B,C,H)`], [`(B,C,H,W)`], or [`(B,C,D,H,W)`].

        **alpha: const tensor\<\[C\], U\>, (Required)**

        :   - The length of [`alpha`] must match the second dimension of [`x`] (channel dimension).

    Attributes[:]

    :   

        **T: fp32, fp16**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[B, C, 1..3\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[scaled_tanh]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#scaled_tanh)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.scaled_tanh "Link to this definition")

:   Return [`alpha`]` `[`*`]` `[`tanh(beta`]` `[`*`]` `[`x)`] elementwise.

    The major difference between this version and the iOS 15 [[`scaled_tanh`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.scaled_tanh "coremltools.converters.mil.mil.ops.defs.iOS15.activation.scaled_tanh") is that the [`alpha`] and [`beta`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input range is [`(-inf,`]` `[`inf)`].

        **alpha: const U (Required)**

        :   

        **beta: const U (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[sigmoid_hard]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#sigmoid_hard)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.sigmoid_hard "Link to this definition")

:   Return [`min(`]` `[`max(`]` `[`alpha`]` `[`*`]` `[`x`]` `[`+`]` `[`beta,`]` `[`0`]` `[`),`]` `[`1`]` `[`)`] elementwise.

    The major difference between this version and the iOS 15 [[`sigmoid_hard`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.sigmoid_hard "coremltools.converters.mil.mil.ops.defs.iOS15.activation.sigmoid_hard") is that the [`alpha`] and [`beta`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const U (Required)**

        :   

        **beta: const U (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor of the same shape and type as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[softplus_parametric]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#softplus_parametric)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.softplus_parametric "Link to this definition")

:   Return [`alpha_i`]` `[`*`]` `[`log(`]` `[`1`]` `[`+`]` `[`e^(`]` `[`beta_i`]` `[`*`]` `[`x_i`]` `[`)`]` `[`)`], where [`i`]` `[`=`]` `[`1`]` `[`...`]` `[`C`].

    Parameters[:]

    :   

        **x: tensor\<\[b, C, n, m\], T\> (Required)**

        :   

        **alpha: const tensor\<\[C\], U\> (Required)**

        :   

        **beta: const tensor\<\[C\], U\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[b, C, n, m\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.activation.]][[thresholded_relu]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html#thresholded_relu)[](#coremltools.converters.mil.mil.ops.defs.iOS17.activation.thresholded_relu "Link to this definition")

:   Return [`x`] if [`x`]` `[`>=`]` `[`alpha`], otherwise return [`0`].

    The major difference between this version and the iOS 15 [[`thresholded_relu`]](#coremltools.converters.mil.mil.ops.defs.iOS15.activation.thresholded_relu "coremltools.converters.mil.mil.ops.defs.iOS15.activation.thresholded_relu") is that the [`alpha`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   

        **alpha: const U (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*, T\>

        :   - A tensor of the same shape and type as [`x`].

[]

## classify[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.classify "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.classify.]][[classify]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/classify.html#classify)[](#coremltools.converters.mil.mil.ops.defs.iOS15.classify.classify "Link to this definition")

:   The presence of this op indicates that the model is of type classifier. The op constructs the model output accordingly; that is, the predicted class label and the output probability dictionary. The parameters of this op are set based on the attributes set for the [coremltools.ClassifierConfig](https://apple.github.io/coremltools/source/coremltools.converters.mil.input_types.html#classifierconfig) class by the user. The outputs of this op cannot be used by another op.

    Parameters[:]

    :   

        **probabilities: tensor\<\[\* , ProbT\]\> (Required)**

        :   A tensor in the graph, which is used to compute the classifier output(s). This is the tensor whose values are mapped to the class labels and used for constructing the predicted class label and the output dictionary of class names and values.

        **classes: list\<\*, ClassT\> (Required)**

        :   List of classes.

    Attributes[:]

    :   

        **ProbT: fp32**

        :   

        **ClassT: i64, str**

        :   

    Returns[:]

    :   

        \<classT\>

        :   

        Dict\[classT, probT\]

        :   

[]

## constexpr_ops (iOS 16+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.]][[constexpr_affine_dequantize]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/constexpr_ops.html#constexpr_affine_dequantize)[](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_affine_dequantize "Link to this definition")

:   A compile-time operation that returns a constant output value upon dequantizing its constant inputs.

    This operation is used to represent constant 8-bit quantized data with affine/linear quantization. The quantized data is stored in the parameter [`quantized_data`]. The other parameters -- [`scale`], [`zero_point`], and [`axis`] -- describe how unquantized values can be extracted from it, using the equation for affine/linear quantization:

    :::: 
    ::: highlight
        unquantized_data = scale * (quantized_data - zero_point)
    :::
    ::::

    Although all of the parameters of this op are constants, this op is not constant folded to a single const op at the time of model serialization. The unquantized output will be decompressed later, based on the implementation detail (either at model load time or runtime).

    Parameters[:]

    :   

        **quantized_data: const tensor\<SrcT, \[1..\]\> (Required)**

        :   

        **zero_point: const tensor\<ZeroPointT, \[0..1\]\> (Required)**

        :   - [`zero_point`] can be either a scalar or a vector.

            - [`zero_point`] follows similar broadcasting rules and size constraints as [`scale`].

        **scale: const tensor\<DstT, \[0..1\]\> (Required)**

        :   - [`scale`] can be either a scalar or a vector.

            - 

              If [`scale`] is a vector, for implementation it is broadcast to the following shape:

              :   - The rank of [`scale`] becomes the same as the rank of [`quantized_data`].

                  - The constraint: [`size(scale-vector)`]` `[`==`]` `[`quantized_data.shape[axis]`].

                  - For [`i`]` `[`==`]` `[`axis`], [`scale.shape[i]`]` `[`==`]` `[`quantized_data.shape[i]`].

                  - For [`i`]` `[`!=`]` `[`axis`], [`scale.shape`]` `[`==`]` `[`1`]. For example, assume [`quantized_data.shape`]` `[`=`]` `[`(2,`]` `[`3,`]` `[`4,`]` `[`5)`] and [`axis`]` `[`=`]` `[`1`]. If [`scale`] is a vector, then [`scale.size`] needs to be equal to [`quantized_data.shape[axis]`]` `[`i.e`]` `[`=`]` `[`3`], which would be broadcast to [`(1,`]` `[`3,`]` `[`1,`]` `[`1)`].

        **axis: const tensor\<int32, \[\]\> (Required)**

        :   

    Attributes[:]

    :   

        **SrcT: uint8, int8**

        :   

        **ZeroPointT: uint8, int8, fp32**

        :   

        **DstT: fp16, fp32**

        :   

    Returns[:]

    :   

        const tensor\<DstT, \[1..\]\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.]][[constexpr_cast]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/constexpr_ops.html#constexpr_cast)[](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_cast "Link to this definition")

:   A compile-time operation that returns a constant output value upon casting its constant input.

    :::: 
    ::: highlight
        Expression: output = constexpr_cast(source_val, output_dtype="fp32")
    :::
    ::::

    Parameters[:]

    :   

        **source_val: const tensor\<SrcT, \[...\]\> (Required)**

        :   

        **output_dtype: const tensor\<string, \[\]\> (Required)**

        :   

    Attributes[:]

    :   

        **SrcT: fp16**

        :   

        **DstT: fp32**

        :   

    Returns[:]

    :   

        const tensor\<DstT, \[...\]\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.]][[constexpr_lut_to_dense]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/constexpr_ops.html#constexpr_lut_to_dense)[](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_lut_to_dense "Link to this definition")

:   A compile-time operation that returns a constant output value upon decompressing a look-up table (LUT) to a dense tensor.

    This operation is used to store constant weights in a LUT format (also known as palettized weights). A LUT is a mapping from index to values. Weights are quantized and stored as indices (or keys) into the LUT. Before computation, these keys are mapped to corresponding values in the LUT.

    Parameters[:]

    :   

        **indices: const tensor\<uint8, \[M\]\> (Required)**

        :   

        **lut: const tensor\<T, \[NUM_PALETTES\]\> (Required)**

        :   

        **shape: const tensor\<uint32, \[K\]\> (Required)**

        :   

    Attributes[:]

    :   

        **T: uint8, int8, fp16, fp32**

        :   

    Returns[:]

    :   

        const tensor\<T, \[...\]\>

        :   

    Notes

    - Any data is packed and read in a row-major order.

    - [`NUM_PALETTES`] can be one of [`]` `[`4,`]` `[`16,`]` `[`64`]` `[`or`]` `[`256}`].

    - [`n_bits`]` `[`=`]` `[`log2(NUM_PALETTES)`] can thus be one of [`]` `[`2,`]` `[`4,`]` `[`6,`]` `[`8}`].

    - Indices are packed in bytes of size [`M`], where [`M`]` `[`=`]` `[`ceil(n_bits`]` `[`*`]` `[`product(shape)`]` `[`/`]` `[`8)`].

    The bit fields are packed one byte at a time, starting with the least significant bit (LSB) and moving upward to the most significant bit (MSB). It follows, naturally, that if an index is split across two bytes, the LSBs of that index is filled over the MSBs of current byte, and the remaining bits of the same index are filled in the LSBs of the next byte.

    For example:

    :::: 
    ::: highlight
        if n_bits = 2, shape = (5,) => M = 2 bytes

                    MSB             LSB
                     |               |
        indices =  | 01   10   11   00 | xx   xx   xx   11 |      <== packed elements
                   | i3 | i2 | i1 | i0 | -- | -- | -- | i4 |      <== tagged element ids
                   |      byte 0       |       byte 1      |      <== tagged bytes
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.]][[constexpr_sparse_to_dense]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/constexpr_ops.html#constexpr_sparse_to_dense)[](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_sparse_to_dense "Link to this definition")

:   A compile-time operation that returns a constant output value upon de-sparsification of its constant inputs.

    This operation represents unstructured sparsity and uses bit mask binary representation. If a bit is set, then the corresponding element in the output tensor is non-zero and the value is read from the [`nonzero_data`] attribute. Likewise, if the bit is not set, then the corresponding element in the output tensor is zero.

    Parameters[:]

    :   

        **nonzero_data: const tensor\<T, \[D\]\> (Required)**

        :   

        **mask: const tensor\<uint8, \[M\]\> (Required)**

        :   

        **shape: const tensor\<uint32, \[K\]\> (Required)**

        :   

    Attributes[:]

    :   

        **T: uint8, int8, fp16, fp32**

        :   

    Returns[:]

    :   

        const tensor\<T, \[...\]\>

        :   

    Notes

    - Any data is packed and read in a row-major order.

    - [`mask`] contains [`M`] bytes, where [`M`]` `[`=`]` `[`ceil(`]` `[`product(shape)`]` `[`/`]` `[`8)`]. That is, each bit field corresponds to one element in the output tensor.

    - [`D`]` `[`==`] the total number of set bits in [`mask`].

    The bit fields are packed one byte at a time, starting with the least significant bit and moving up to the most significant bit.

    For example:

    :::: 
    ::: highlight
        shape = (5,) => M = 1 bytes

                   MSB                  LSB
                    |                    |
        mask    =  |x  x  x  0  1  1  0  0 |      <== packed elements
                   |--|--|--|i4|i3|i2|i1|i0|      <== tagged element ids
                   |      byte 0           |      <== tagged bytes
    :::
    ::::

[]

## constexpr_ops (iOS 18+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS18.compression "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.compression.]][[constexpr_blockwise_shift_scale]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/compression.html#constexpr_blockwise_shift_scale)[](#coremltools.converters.mil.mil.ops.defs.iOS18.compression.constexpr_blockwise_shift_scale "Link to this definition")

:   A compile-time operation that returns a constant output value upon dequantizing its constant inputs.

    It's similar to iOS 16 [[`constexpr_affine_dequantize`]](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_affine_dequantize "coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_affine_dequantize"), but supports block-wise quantization for int4 and int8.

    Although all parameters of this op are constants, this op is not constant-folded to a single const op at the time of model serialization. The unquantized output will be decompressed later, based on the implementation detail (either at model load time or runtime).

    Generic expression: output = scale \* (data - offset)

    Algorithm:

    :   

        Assuming Rank 3 scenario:

        :   output_data\[i, j, k\] = scale\[i0, j0, k0\] \* (data\[i, j, k\] - offset\[i0, j0, k0\]) where

            > ::: 
            > i0 = floor(i/block_size\[0\]), j0 = floor(j/block_size\[1\]), k0 = floor(k/block_size\[2\])
            > :::

        The block size is implied by block_size\[m\] = data.shape\[m\] / scale.shape\[m\]

    Constraints: - All tensors: scale, data, offset and output have same rank. - Inputs: scale and offset (if provided) have same shape. - Output shape is same as the shape of input argument: data. - Number of scales along each dimension should be a factor of corresponding dimension size of

    > ::: 
    > data. That is, block_size\[i\] should be an integer where block_size\[i\] = data.shape\[i\] / scale.shape\[i\]
    > :::

    Parameters[:]

    :   

        **data: const tensor\<SrcT, \[1..\]\> (Required)**

        :   

        **scale: const tensor\<DstT, \[1..\]\> (Required)**

        :   

        **offset: const tensor\<OffsetT, \[1..\]\> (Optional)**

        :   - If provided, must have the same shape as the [`scale`].

            - If dtype is not fp16 or fp32, it must be the same as SrcT.

    Attributes[:]

    :   

        **SrcT: int4, uint4, int8, uint8, fp16, fp32**

        :   

        **DstT: fp16, fp32**

        :   

        **OffsetT: int4, uint4, int8, uint8, fp16, fp32**

        :   

    Returns[:]

    :   

        const tensor\<DstT, \[1..\]\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.compression.]][[constexpr_lut_to_dense]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/compression.html#constexpr_lut_to_dense)[](#coremltools.converters.mil.mil.ops.defs.iOS18.compression.constexpr_lut_to_dense "Link to this definition")

:   A compile-time operation that returns a constant output value upon dequantizing its constant inputs.

    This operator is used to store constant weights in lookup tables format (aka palettized weights). It's similar to iOS 16 [[`constexpr_lut_to_dense`]](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_lut_to_dense "coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_lut_to_dense"), but supports block-wise / vector palettization.

    LUT's rank is K + 2, where K is the rank of indices. Each dimension of LUT's first K dimensions should be divisible by each corresponding dimension of the decompressed tensor. e.g., when indices_shape = \[2, 3, 4\], lut_shape\[:3\] = \[1, 1, 2\], it means that there are two lookup tables over the last axis. And each of them have their own LUT values. See Case 1 below for details.

    VECTOR_SIZE is added to support vector palettization. - When VECTOR_SIZE is 1, it is scalar palettization. - When VECTOR_SIZE is larger than 1, it retrieves a vector instead of a single value from the

    > ::: 
    > lookup table, and fill the result continuously.
    > :::

    The vector_axis is used to define which axis the vectored elements in the lookup table be filled across the output tensor. vector_axis is only optional if VECTOR_SIZE is 1. As a result:

    > ::: 
    > output_shape\[i\] = indices_shape\[i\] , i != vector_axis output_shape\[i\] = indices_shape\[i\] \* VECTOR_SIZE, i == vector_axis
    > :::

    See Case 2 below for details.

    Examples

    Case 1: per-group scalar palettization:

    :   e.g.: - indices = tensor\<uint2, \[6, 2\]\>\>(\[2, 3, 3, 0, 1, 0, 3, 0, 2, 1, 0, 3\]) - lut = tensor\<fp16, \[2, 1, 4, 1\]\>(\[1.0, 5.0, 9.0, 13.0, 2.0, 10.0, 18.0, 26.0\])

        It is effectively a 2-group 2-bit scalar palettization. The output shape would be \[6, 2\], which is the same as the indices shape. The output tensor values are: \[\[lut0\[2\]-\>9.0, lut0\[3\]-\>13.0\],

        > ::: 
        > \[lut0\[3\]-\>13.0, lut0\[0\]-\>1.0\], \[lut0\[1\]-\>5.0, lut0\[0\]-\>1.0\], \[lut1\[3\]-\>26.0, lut1\[0\]-\>2.0\], \[lut1\[2\]-\>18.0, lut1\[1\]-\>10.0\], \[lut1\[0\]-\>2.0, lut1\[3\]-\>26.0\]\]
        > :::

        where lut0 is the first lookup table (lut\[0, :, :, :\]) and lut1 is the second lookup table.

    Case 2: per-tensor vector palettization:

    :   e.g.: - indices = tensor\<uint1, \[2, 2, 2\]\>\>. The indices values are:

        > ::: 
        >
        > \[
        >
        > :   
        >
        >     \[
        >
        >     :   \[0, 0\], \[1, 0\]
        >
        >     \], \[
        >
        >     > ::: 
        >     > \[1, 1\], \[0, 0\]
        >     > :::
        >
        >     \]
        >
        > \]
        > :::

        - 

          lut = tensor\<int8, \[1, 1, 1, 2, 3\]\>(\[a0, a1, a2,

          :   > ::: 
              > b0, b1, b2\])
              > :::

              which means the two centroids are \[a1, a2, a3\] and \[b1, b2, b3\].

    Case 2.1: vector_axis = 1

    :   It is effectively a 1-bit vector palettization. The output shape would be \[2, 2\*3, 2\], where each index in the indices would be effectively replaced with the 3 elements in the vector over the 1st dimension to construct the output tensor. The output values are: \[

        > ::: 
        >
        > \[
        >
        > :   \[a0, a0\], \[a1, a1\], \[a2, a2\], \[b0, a0\], \[b1, a1\], \[b2, a2\],
        >
        > \], \[
        >
        > > ::: 
        > > \[b0, b0\], \[b1, b1\], \[b2, b2\], \[a0, a0\], \[a1, a1\], \[a2, a2\],
        > > :::
        >
        > \]
        > :::

        \]

    Case 2.2: vector_axis = 2

    :   The output shape would be \[2, 2, 2\*3\], where each index in the indices would be effectively replaced with the 3 elements in the vector over the last dimension to construct the output tensor. The output values are: \[

        > ::: 
        >
        > \[
        >
        > :   \[a0, a1, a2, a0, a1, a2\], \[b0, b1, b2, a0, a1, a2\],
        >
        > \], \[
        >
        > > ::: 
        > > \[b0, b1, b2, b0, b1, b2\], \[a0, a1, a2, a0, a1, a2\],
        > > :::
        >
        > \]
        > :::

        \]

    Parameters[:]

    :   

        **indices: const tensor\<IndicesT, \[1..\]\> (Required)**

        :   

        **lut: const tensor\<T, \[1.., NUM_PALETTES, VECTOR_SIZE\]\> (Required)**

        :   - NUM_PALETTES needs to be 2\^nbits where nbits is indicated by IndicesT.

        **vector_axis: const tensor\<int32, \[\]\> (Optional)**

        :   - vector_axis can be optional if VECTOR_SIZE is 1.

    Attributes[:]

    :   

        **IndicesT: uint1, uint2, uint3, uint4, uint6, uint8**

        :   

        **T: uint8, int8, fp16, fp32**

        :   

    Returns[:]

    :   

        const tensor\<T, \[1..\]\>

        :   - output_shape = indices_shape \* \[1..1, VECTOR_SIZE, 1..1\] (all 1 but VECTOR_SIZE at vector_axis dimension).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.compression.]][[constexpr_sparse_to_dense]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/compression.html#constexpr_sparse_to_dense)[](#coremltools.converters.mil.mil.ops.defs.iOS18.compression.constexpr_sparse_to_dense "Link to this definition")

:   A compile-time operation that returns a constant output value upon de-sparsification of its constant inputs.

    The differences from iOS16 [[`constexpr_sparse_to_dense`]](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_sparse_to_dense "coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_sparse_to_dense") are: - In iOS16, the mask parameter is 'const tensor\<uint8, \[M\]\>', which is a flat tensor with length

    > ::: 
    > M, so it requires a parameter shape to determine the output shape. In iOS18, we use uint1 (0 or 1) to represent bitmask, which packs the bitmask data and costs the same memory as the uint8 mask in iOS16, but can explicitly tell the tensor shape. We use uint1 instead of bool because bool in MIL uses uint8 as the storage dtype, which costs 8x memory compared to uint1.
    > :::

    - Support more dtypes (int4 and uint4) for the input/output data.

    Parameters[:]

    :   

        **nonzero_data: const tensor\<T, \[D\]\> (Required)**

        :   

        **mask: const tensor\<uint1, \[1..\]\> (Required)**

        :   

    Attributes[:]

    :   

        **T: int4, uint4, int8, uint8, fp16, fp32**

        :   

    Returns[:]

    :   

        const tensor\<T, \[1..\]\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.compression.]][[constexpr_lut_to_sparse]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/compression.html#constexpr_lut_to_sparse)[](#coremltools.converters.mil.mil.ops.defs.iOS18.compression.constexpr_lut_to_sparse "Link to this definition")

:   A compile-time operation that returns a constant output value upon de-palettizing its constant inputs.

    This op is a sparse-to-sparse op to support constexpr_lut_to_dense on sparse data, where the de-palettization is only applied on the nonzero data. Usually it would be followed by a constexpr_sparse_to_dense op to get the dense tensor. So, parameters of this op are similar to constexpr_sparse_to_dense and constexpr_lut_to_dense. For detailed descriptions about its parameters, please refer to iOS 18 [`constexpr_sparse_to_dense`] and [`constexpr_lut_to_dense`].

    This op has two outputs:

    :   1.  the mask of the de-palettized nonzero_data.

        2.  the de-palettized nonzero_data.

    Parameters[:]

    :   

        **indices_mask: const tensor\<uint1, \[1..\]\> (Required)**

        :   

        **indices_nonzero_data: const tensor\<IndicesT, \[D\]\> (Required)**

        :   

        **lut: const tensor\<T, \[1.., NUM_PALETTES, VECTOR_SIZE\]\> (Required)**

        :   - NUM_PALETTES needs to be 2\^nbits where nbits is indicated by IndicesT.

        **vector_axis: const tensor\<int32, \[\]\> (Optional)**

        :   - vector_axis can be optional if VECTOR_SIZE is 1.

    Attributes[:]

    :   

        **IndicesT: uint1, uint2, uint3, uint4, uint6, uint8**

        :   

        **T: uint8, int8, fp16, fp32**

        :   

    Returns[:]

    :   

        const tensor\<uint1, \[1..\]\>

        :   - the mask of the de-palettized nonzero_data. For scalar palettization, it's the same as the input indices_mask. For vector palettization, it's expanded of the indices_mask over axis=vector_axis.

        const tensor\<T, \[VD\]\>

        :   - the de-palettized nonzero_data. For scalar palettization, VD=D (same size as indices_nonzero_data). For vector palettization, VD=VECTOR_SIZE \* D (each entry is expanded by a vector).

    Examples

    Assume we have the following inputs:

    :   

        indices_mask\<uint1, \[4, 6\]\> = \[\[1, 1, 0, 0, 0, 0\],

        :   \[1, 1, 0, 0, 0, 1\], \[0, 1, 1, 0, 1, 0\], \[0, 0, 0, 1, 0, 0\]\]

        indices_nonzero_data\<uint1, \[9\]\> = \[0, 1, 1, 0, 1, 1, 0, 0, 1\]

        Notice that: - The uint1 in indices_mask and indices_nonzero_data has different meanings. For

        > ::: 
        > indices_mask the dtype is always uint1 to represent bit mask. For indices_nonzero_data the uint1 means the LUT only has two entries, so only 1 bit is needed to represent indices.
        > :::

        - The 0 in indices_mask and indices_nonzero_data has different meanings. For indices_mask the 0 means empty entry in sparse representation. For indices_nonzero_data the 0 means index 0 in LUT.

    With the given indices_mask and indices_nonzero_data, an example for "Scalar Palettization":

    :   lut\<fp16, \[1, 1, 2, 1\]\> = \[2.0, 3.0\] (indices-to-values mapping is )

        The sparse indices in the dense layout would look like: 0 1 . . . . 1 0 . . . 1 . 1 0 . 0 . . . . 1 . . (here "." means spare elements in sparse representation)

        When we apply per-tensor de-palettization with this sparse indices, the indices_nonzero_data is used to read the values from the LUT as in the dense layout. The output sparse tensor in the dense layout would be: 2.0 3.0 . . . . 3.0 2.0 . . . 3.0

        > ::: 
        > . 3.0 2.0 . 2.0 . . . . 3.0 . .
        > :::

        The first output would be the same as the indices_mask. The second output would be \[2.0, 3.0, 3.0, 2.0, 3.0, 3.0, 2.0, 2.0, 3.0\]

    With the given indices_mask and indices_nonzero_data, an example for "Vector Palettization":

    :   lut\<fp16, \[1, 1, 2, 2\] = \[\[2.0, 2.0\], \[3.0, 3.0\]\] vector_axis = 0

        The first output would be the expanded mask of the indices_mask over axis=0, which is: output\<uint1, \[8, 6\]\> = \[

        > ::: 
        > \[1, 1, 0, 0, 0, 0\], \[1, 1, 0, 0, 0, 0\], \[1, 1, 0, 0, 0, 1\], \[1, 1, 0, 0, 0, 1\], \[0, 1, 1, 0, 1, 0\], \[0, 1, 1, 0, 1, 0\], \[0, 0, 0, 1, 0, 0\], \[0, 0, 0, 1, 0, 0\],
        > :::

        \] The second output in the dense layout would be: 2.0 3.0 . . . . 2.0 3.0 . . . . 3.0 2.0 . . . 3.0 3.0 2.0 . . . 3.0

        > ::: 
        > . 3.0 2.0 . 2.0 . . 3.0 2.0 2.0 . . . . 3.0 . . . . . 3.0 . .
        > :::

        It is created by fetching the vector entry from the lut for every bit 1 in the data_mask, and filling the vector over axis=0.

    Those two outputs of this op could be passed as inputs to a following sparse_to_dense op in order to recover the dense weights.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.compression.]][[constexpr_sparse_blockwise_shift_scale]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/compression.html#constexpr_sparse_blockwise_shift_scale)[](#coremltools.converters.mil.mil.ops.defs.iOS18.compression.constexpr_sparse_blockwise_shift_scale "Link to this definition")

:   A compile-time operation that returns a constant output value upon de-quantize (shift-scale) its constant inputs. This op is a sparse-to-sparse op to support constexpr_blockwise_shift_scale on sparse data, where the de-quantization is only applied on the nonzero data. Usually it would be followed by a constexpr_sparse_to_dense op to get the dense tensor. So, parameters of this op are similar to constexpr_sparse_to_dense and constexpr_blockwise_shift_scale. For detailed descriptions about its parameters, please refer to iOS 18 [`constexpr_sparse_to_dense`] and [`constexpr_blockwise_shift_scale`].

    This op has two outputs:

    :   1.  the mask of the de-quantized nonzero_data.

        2.  the de-quantized nonzero_data.

    Parameters[:]

    :   - **data_mask** (*const tensor\<uint1, \[1..\]\> (Required)*)

        - **nonzero_data** (*const tensor\<SrcT, \[D\]\> (Required)*)

        - **scale** (*const tensor\<DstT, \[1..\]\> (Required)*)

        - **offset** (*const tensor\<OffsetT, \[1..\]\> (Optional)*) --

          - If provided, must have the same shape as the [`scale`].

    Returns[:]

    :   

        const tensor\<uint1, \[1..\]\>

        :   - the mask of the shift-scaled nonzero_data.

        const tensor\<DstT, \[D\]\>

        :   - the shift-scaled nonzero_data.

        Attributes

        :   

        > ::: 
        > :::

        SrcT: int4, uint4, int8, uint8, fp16, fp32

        :   

        DstT: fp16, fp32

        :   

        OffsetT: int4, uint4, int8, uint8, fp16, fp32

        :   

        Examples

        :   

        > ::: 
        > :::

        For example:

        :   data_mask = \[\[1, 1, 0, 0\], \[1, 1, 1, 0\], \[0, 0, 1, 1\], \[1, 1, 0, 0\]\] nonzero_data = \[10, 11, 3, 4, 5, 6, 7, 8, 9\] The sparse tensor in the dense layout would look like:

            > ::: 
            >
            > 10 11 . .
            >
            > :   3 4 5 . . . 6 7 8 9 . .
            > :::

            When we apply per-channel de-quantization on this sparse tensor, where: scale = \[\[0.1, 0.2, 0.3, 0.4\]\] offset = \[\[1, 2, 3, 4\]\] The input nonzero_data would be dequantized per-column as in the dense layout, and the output sparse tensor in the dense layout would be:

            > ::: 
            > (10-1)\*0.1 (11-2)\*0.2 . . (10-1)\*0.1 (11-2)\*0.2 . .
            >
            > > ::: 
            > >
            > > (3-1)\*0.1 (4-2)\*0.2 (5-3)\*0.3 .
            > >
            > > :   . . (6-3)\*0.3 (7-4)\*0.4
            > >
            > > (8-1)\*0.1 (9-2)\*0.2 . .
            > > :::
            > :::

            The first output would be the same as the data_mask, The second output would be \[0.9, 1.8, 0.2, 0.4, 0.6, 0.9, 1.2, 0.7, 1.4\]. The two outputs could be passed as inputs to the following sparse_to_dense op in order to get the dense weights.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.compression.]][[constexpr_cast]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/compression.html#constexpr_cast)[](#coremltools.converters.mil.mil.ops.defs.iOS18.compression.constexpr_cast "Link to this definition")

:   A compile-time operation that returns a constant output value upon casting its constant input.

    The only difference between this version and the iOS 16 [[`constexpr_cast`]](#coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_cast "coremltools.converters.mil.mil.ops.defs.iOS16.constexpr_ops.constexpr_cast") is the parameters are treated as inputs, instead of attributes in the MIL backend framework.

[]

## control_flow[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.control_flow "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[cond]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#cond)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.cond "Link to this definition")

:   Perform a conditional execution. The return types must be identical between the true and false branches.

    Parameters[:]

    :   

        **pred: tensor\<\[\], bool\> (Required)**

        :   - 0-D tensor (scalar) predicate to switch between true and false branches.

        **\_true_fn: function (Required)**

        :   - A Python function that executes if [`pred`] evaluates to [`True`].

            - It must take zero input (i.e, no input), and return one or more values whose type becomes the operation's return type.

        **\_false_fn: function (Required)**

        :   - A Python function that executes if [`pred`] evaluates to [`False`].

            - It must take zero input (i.e. no input), and have return types that match those of the [`if`] branch.

        **\_existing_blocks: list\[Block\] (Optional)**

        :   - Python list of [`Block`].

            - For internal use only. When converting a milproto, we already got existing blocks, and the [`build_nested_blocks`] function can use them directly.

            - When [`_existing_blocks`] is set, [`_true_fn`] and [`_false_fn`] must be dummy functions which returns [`None`].

    Returns[:]

    :   

        tuple

        :   - Python tuple of [`Variables`] from one of the branches.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[Const]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#Const)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.Const "Link to this definition")

:   A base class that returns constant values.

    Parameters[:]

    :   

        **val: const\<\*,T\> (Required)**

        :   

        **mode: immediate_value, file_value (Optional)**

        :   - Determines how the constant value is stored in the internal MIL format.

            - For large constants such as convolution weights, use [`file_value`].

            - For smaller-size constants such as values of a stride, use [`immediate_value`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, str, bool**

        :   

    Returns[:]

    :   

        const\<\*,T\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[select]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#select)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.select "Link to this definition")

:   Return the elements selected from either [`a`] or [`b`] depending on the [`cond`].

    You must provide [`a`], [`b`] and [`cond`]. The shape of [`cond`], [`a`], and [`b`] must be broadcastable.

    Parameters[:]

    :   

        **cond: tensor\<\[\*D1\], B\> (Required)**

        :   - Tensor. When [`True`], select element from [`x`], otherwise, [`y`].

        **a: tensor\<\[\*D2\], T\> (Optional)**

        :   - Values selected at indices where [`cond`] is [`True`].

            - Default is [`None`].

        **b: tensor\<\[\*D3\], T\> (Optional)**

        :   - Values selected at indices where [`cond`] is [`False`].

            - Default is [`None`].

    Attributes[:]

    :   

        **B: bool**

        :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\[\*D_out\], T\> or tensor\<\[n, len(D1)\], int32\>

        :   - If [`a,`]` `[`b`] are both provided, the return shape is based on broadcast rules from [`cond,`]` `[`a,`]` `[`b`].

            - If [`a,`]` `[`b`] are [`None`], the return shape is 2-D, where the first dimension [`n`] is the number of matching indices in [`cond`], and [`len(D1)`] is the rank of [`cond`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[while_loop]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#while_loop)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.while_loop "Link to this definition")

:   Perform the body repeatedly while the condition [`cond`] is true.

    Parameters[:]

    :   

        **\_cond: function (Required)**

        :   - A Python function that takes [`loop_vars`] as positional arguments.

            - The function must return a [`bool`] [`Var`].

        **\_body: function (Required)**

        :   - A Python function that takes [`loop_vars`] as positional arguments.

            - The function must return the same number of output vars as [`loop_vars`] with the same types.

        **loop_vars: tuple (Required)**

        :   - Python tuple of [`Variables`].

        **\_existing_blocks: list\[Block\] (Optional)**

        :   - Python list of [`Block`].

            - For internal use only. When converting a milproto, we already got existing blocks, and the [`build_nested_blocks`] function can use them directly.

            - When [`_existing_blocks`] is set, [`_cond`] and [`_body`] must be dummy functions which returns [`None`].

    Returns[:]

    :   

        tuple

        :   - Python tuple (same type as [`loop_vars`]).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[make_list]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#make_list)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.make_list "Link to this definition")

:   Create a list of tensor elements. The elements should have the same shape. The list is similar to an auto-resizing array.

    Parameters[:]

    :   

        **init_length: \<i32\> (Optional, Default=1)**

        :   - Initial length for the list.

            - If [`dynamic_length`] is [`False`], [`init_length`] is the fixed length of the list throughout runtime.

        **dynamic_length: \<bool\> (Optional, Default is True)**

        :   

        **elem_shape: Tuple\[const\<T\>\] (Required)**

        :   - 1-D vector denoting the shape of elements.

            - If [`T`]` `[`=`]` `[`int32`], the element shape is known at compile time.

            - [`T`]` `[`=`]` `[`string`] denotes the symbolic shape, in which the shape is determined at runtime.

            - If not provided, the resulting [`List`] won't have the elementary shape info, which may cause backend errors. Remedy this with SSA passes.

        **dtype: const (Optional, Default is fp32)**

        :   - Possible values: [`]` `[`"fp16",`]` `[`"fp32",`]` `[`"int32"}`]

            - Element tensor's [`dtype`].

    Attributes[:]

    :   

        **T: i32, string**

        :   

    Returns[:]

    :   

        List\[\*\]

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[list_length]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#list_length)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.list_length "Link to this definition")

:   Return the length of [`ls`].

    Parameters[:]

    :   

        **ls: List\[\*\] (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        \<i32\>

        :   - Length of [`ls`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[list_write]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#list_write)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.list_write "Link to this definition")

:   Write a value into index [`index`] of [`ls`].

    Parameters[:]

    :   

        **ls: List (Required)**

        :   

        **index: \<i32\> (Required)**

        :   - Size of the list.

        **value: \<\*,T\> (Optional)**

        :   - Element value to write, which must match the element shape of [`ls`].

            - Default is [`None`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        List\[\*\]

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[list_read]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#list_read)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.list_read "Link to this definition")

:   Read the value at location [`index`] of [`ls`].

    Parameters[:]

    :   

        **ls: List\[\*\] (Required)**

        :   

        **index: \<i32\> (Required)**

        :   - Size of the list.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        \<\*,T\>

        :   - The element's value.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[list_gather]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#list_gather)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.list_gather "Link to this definition")

:   Return selected values in [`ls`] as a packed [`Tensor`].

    Parameters[:]

    :   

        **ls: List\[\*\] (Required)**

        :   

        **indices: \<K, i32\> (Required)**

        :   - Gather from indices, whose element must be in [`[0,`]` `[`ls.length)`] at runtime.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        \<\*K, T\>

        :   - Selected tensors packed into a [`len(ls.elem_shape)+1`] rank tensor.

            - [`K[0]`]` `[`==`]` `[`len(indices)`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.]][[list_scatter]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html#list_scatter)[](#coremltools.converters.mil.mil.ops.defs.iOS15.control_flow.list_scatter "Link to this definition")

:   Scatter [`values`] to [`ls`] at locations [`indices`].

    Parameters[:]

    :   

        **ls: List\[\*\] (Required)**

        :   

        **indices: tensor\<num_updates, i32\> (Required)**

        :   - Indices of [`ls`] to scatter to.

            - Elements of [`indices`] must be in [`[0,`]` `[`ls.length)`] at runtime.

            - If indices are greater than or equal to the list length, the list is dynamically resized.

        **value: \<\*,T\> (Optional)**

        :   - Element value to write, which must match the element shape of [`ls`].

            - Default is [`None`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        List\[\*\]

        :   - Updated list.

[]

## conv (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.conv "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.conv.]][[conv]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/conv.html#conv)[](#coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv "Link to this definition")

:   Perform convolution over input. Supports 1-D, 2-D, and 3-D convolution.

    Parameters[:]

    :   

        **x: tensor\<\[n, C_in, \*d_in\], T\> (Required)**

        :   - [`d_in`] are (possibly runtime-determined) spatial dimensions. For example, [`d_in`]` `[`=`]` `[`[224,`]` `[`224]`] for 2D convolution.

            - [`1`]` `[`<=`]` `[`len(d_in)`]` `[`<=`]` `[`3`].

            - [`C_in`] is the number of input channels or depth dimensions.

            - [`n`] is the batch dimension.

        **weight: tensor\<\[C_out, C_in/groups, \*K\], T\> (Required)**

        :   - Filter weights.

            - [`C_in`] is the number of input channels.

            - [`C_in`] must be divisible by [`groups`].

            - [`K`] are kernel sizes. For example, [`K`]` `[`=`]` `[`[KH,`]` `[`KW]`] for 2-D convolution.

            - When [`dilations`] is not all [`1`], [`weight`] has to be [`const`] at compile time

        **strides: const tensor\<\[S\], i32\> (Optional)**

        :   - Default to one vector of length equal to the number of spatial dimensions.

            - Strides along each of the spatial dimensions.

            - [`S`]` `[`==`]` `[`len(d_in)`].

        **pad_type: const str (Required)**

        :   Must be one of the following:

            > ::: 
            > - [`valid`]: No padding. This is equivalent to custom pad with [`pad[2*i]`]` `[`==`]` `[`pad[2*i+1]`]` `[`==`]` `[`0,`]` `[`for`]` `[`i=0,...,len(d_in)-1`].
            >
            > - [`custom`]: Specify custom padding in the parameter [`pad`].
            >
            > - [`same`]: Input is padded such that out spatial shapes are [`d_out[i]`]` `[`=`]` `[`ceil(d_in[i]`]` `[`/`]` `[`strides[i])`].
            >
            > - [`same_lower`]: Similar to [`same`] but the padding will place extra rows/cols on the top/left if the padding amount is odd.
            > :::

            Specifically, for [`i`]` `[`=`]` `[`0,..,,len(d_in)-1`], the equivalent paddings are calculated as follows:

            > ::: 
            > - [`dilated_kernel`]` `[`=`]` `[`(K[i]`]` `[`-`]` `[`1)`]` `[`*`]` `[`dilate[i]`]` `[`+`]` `[`1`]
            >
            > - If [`dilated_kernel`] is odd, [`padding[2*i]`]` `[`=`]` `[`padding[2*i+1]`]` `[`=`]` `[`floor(dilated_kernel`]` `[`/`]` `[`2)`]
            >
            > - Otherwise: [`padding[2*i]`]` `[`=`]` `[`ceil((dilated_kernel`]` `[`-`]` `[`1)`]` `[`/`]` `[`2)`], [`padding[2*i+1]`]` `[`=`]` `[`floor((dilated_kernel`]` `[`-`]` `[`1)`]` `[`/`]` `[`2)`]
            > :::

        **pad: const tensor\<\[P\], i32\> (Optional. Default to all zeros)**

        :   - [`len(P)`]` `[`=`]` `[`2`]` `[`*`]` `[`len(d_in)`]

            - [`pad`] should be specified if and only if [`pad_type`]` `[`==`]` `[`custom`], otherwise errors occur.

            - [`pad`] represents the number of elements to pad before and after each dimension. Specifically, [`pad[0],`]` `[`pad[1]`] are the pad size before / after spatial dimension 0, [`pad[2],`]` `[`pad[3]`] are the pad size before / after spatial dimension 1, etc.

        **dilations: const tensor\<\[S\], i32\> (Optional. Default to all 1s)**

        :   - Dilation value along each spatial dimension in [`d_in`]. See [visualization](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md).

            - [`S`]` `[`==`]` `[`len(d_in)`].

        **groups: const tensor\<\[\], i32\> (Optional, default to 1)**

        :   - Input and output channels are split by [`groups`].

            - [`C_in`] must be divisible by [`groups`].

            - Maximum value for group is [`C_in`], in which case it is a depthwise convolution.

            For examples (assuming [`C_in`]` `[`=`]` `[`16,`]` `[`C_out`]` `[`=`]` `[`32`]):

            > ::: 
            > - [`groups`]` `[`==`]` `[`1`], [`weight`] has shape [`[32,`]` `[`16,`]` `[`KH,`]` `[`KW]`]: All input channels are convolved with the [`weight`] kernel to produce all output channels.
            >
            > - [`groups`]` `[`==`]` `[`2`], [`weight`] has shape [`[32,`]` `[`8,`]` `[`KH,`]` `[`KW]`]: Input channels 0\~7 are convolved with half of the [`weight`] kernel to produce output channels 0\~15. Similarly, input channels 8\~15 are convolved with the other half of [`weight`] to product output channels 16\~31.
            >
            > - [`groups`]` `[`==`]` `[`C_in`], [`weight`] has shape [`[32,`]` `[`1,`]` `[`KH,`]` `[`KW]`]: Each input channel is convolved with its own set of filters and each produce [`C_out`]` `[`/`]` `[`C_in`]` `[`=`]` `[`2`] channels. This is equivalent to depthwise convolution.
            > :::

        **bias: const tensor\<\[C_out\],T\> (Optional, default to all 0)**

        :   - Bias along output channels.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C_out, \*d_out\], T\>

        :   - Output activation has the same rank and spatial dimension as the input. That is, [`len(d_out)`]` `[`==`]` `[`len(d_in)`].

            - For [`i=0,..,len(d_in)-1,`]` `[`d_out[i]`]` `[`=`]` `[`floor`]` `[`[(D_in[i]`]` `[`+`]` `[`pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`-`]` `[`(K[i]-1)*dilations[i]`]` `[`-`]` `[`1)`]` `[`/`]` `[`strides[i]`]` `[`]`]` `[`+`]` `[`1`].

    ::: 
    See also

    [[`conv_transpose`]](#coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv_transpose "coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv_transpose")

    :   
    :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.conv.]][[conv_transpose]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/conv.html#conv_transpose)[](#coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv_transpose "Link to this definition")

:   Perform transposed convolution (also known as deconvolution and fractionally stride convolution) over input. [`conv_transpose`] can also be used to compute the gradient of conv. Supports 1-D, 2-D, and 3-D convolution.

    Parameters[:]

    :   

        **x: tensor\<\[n,C_in,\*D_in\],T\> (Required)**

        :   - Input data.

            - [`D_in`] are spatial dimensions.

            - [`1`]` `[`<=`]` `[`len(D_in)`]` `[`<=`]` `[`3`].

            - [`C_in`] is the number of input channels.

        **weight: const tensor\<\[C_in,C_out/groups,\*D_in\], T\> (Required)**

        :   - Filter weights. [`C_in,`]` `[`C_out`] are the number of input and output channels respectively.

            - [`D_in`] are spatial dimensions. [`1`]` `[`<=`]` `[`len(D_in)`]` `[`<=`]` `[`2`].

        **bias: const tensor\<\[C_out\],T\> (Optional, default to all 0)**

        :   - Bias added along output channels.

        **pad: const tensor\<\[P\],i32\> (Optional, default to all 0s)**

        :   - Number of elements to pad before and after each dimension.

            - [`P`]` `[`==`]` `[`2`]` `[`*`]` `[`len(D_in)`].

            - [`pad[2*i],`]` `[`pad[2*i+1]`] are pad sizes before and after dimension [`i`], where [`0`]` `[`<=`]` `[`i`]` `[`<`]` `[`len(D_in)`].

        **output_shape: const tensor\<\[P\],i32\> (Optional, default None)**

        :   - Expected output shape. The first two dimensions must be [`[n,`]` `[`C_out]`].

            - The output shape of [`conv_transpose`] is underdetermined in general, because [`conv`] can map multiple input shapes to a single output shape. For example, for [`same`] padding mode, [`conv_out`]` `[`=`]` `[`ceil(conv_in/stride)`]. Hence we need [`output_shape`] when this occurs.

        **pad_type: const tensor\<\[P\],i32\> (Optional, default valid)**

        :   - One of [`same`], [`valid`], or [`custom`].

        **strides: const tensor\<\[S\],i32\> (Optional. Default to all 1s)**

        :   - Stride along each of the spatial dimensions.

            - [`S`]` `[`==`]` `[`len(D_in)`].

        **dilations: const tensor\<\[S\],i32\> (Optional. Default to all 1s)**

        :   - Dilation value along each spatial dimension in [`d_in`]. See [`conv`].

            - [`S`]` `[`==`]` `[`len(D_in)`].

        **groups: const tensor\<\[\], i32\> (Optional. Default to 1)**

        :   - Input and output channels are separated into [`groups`].

            - [`C_in`] and [`C_out`] must be divisible by the number of groups. See [`conv`] for examples.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n,C_out,\*D_out\],T\>

        :   - If [`output_shape`] is not [`None`]:

              > ::: 
              > [`Dout`]` `[`=`]` `[`output_shape`]
              > :::

            - If [`pad_type`]` `[`==`]` `[`"custom"`]:

              > ::: 
              > [`Dout[i]`]` `[`=`]` `[`(D_in[i]-1)*stride[i]`]` `[`+`]` `[`(K[i]-1)`]` `[`*`]` `[`dilation[i]`]` `[`+`]` `[`1`]` `[`-`]` `[`pad[2*i]`]` `[`-`]` `[`pad[2*i-1]`]
              > :::

            - If [`pad_type`]` `[`==`]` `[`"valid"`]:

              > ::: 
              > [`Dout[i]`]` `[`=`]` `[`(D_in[i]-1)*stride[i]`]` `[`+`]` `[`(K[i]-1)`]` `[`*`]` `[`dilation[i]`]` `[`+`]` `[`1`]
              > :::

            - If [`pad_type`]` `[`==`]` `[`"same"`]:

              > ::: 
              > [`Dout[i]`]` `[`=`]` `[`D_in[i]`]` `[`*`]` `[`stride[i]`]
              > :::

    ::: 
    See also

    [[`conv`]](#coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv "coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv")

    :   
    :::

[]

## conv (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.conv "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.conv.]][[conv]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/conv.html#conv)[](#coremltools.converters.mil.mil.ops.defs.iOS17.conv.conv "Link to this definition")

:   Perform convolution over input. Supports 1-D, 2-D, and 3-D convolution.

    The difference between this version and the iOS 15 [[`conv`]](#coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv "coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv") is that the [`weight`] and [`bias`] may have a different dtype than the input/output.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.conv.]][[conv_transpose]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/conv.html#conv_transpose)[](#coremltools.converters.mil.mil.ops.defs.iOS17.conv.conv_transpose "Link to this definition")

:   Perform transposed convolution (also known as deconvolution and fractionally stride convolution) over input. [`conv_transpose`] can also be used to compute the gradient of conv. Supports 1-D, 2-D, and 3-D convolution.

    The differences between this version and the iOS 15 [[`conv_transpose`]](#coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv_transpose "coremltools.converters.mil.mil.ops.defs.iOS15.conv.conv_transpose") are: - [`weight`] and [`bias`] may have a different dtype than the input/output. - [`weight`] doesn't have to be const.

[]

## coreml_update_state[](#module-coremltools.converters.mil.mil.ops.defs.coreml_dialect.ops "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.coreml_dialect.ops.]][[coreml_update_state]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/coreml_dialect/ops.html#coreml_update_state)[](#coremltools.converters.mil.mil.ops.defs.coreml_dialect.ops.coreml_update_state "Link to this definition")

:   Copy the content of a variable into a state and return the copy of the variable. The type of the variable must match the type that is wrapped inside the state. This is a coreml dialect op to simplify the program. When loading into MIL, the following transformation is done:

    :::: 
    ::: highlight
        %x = coreml_update_state(state=%state, value=%value)

        -->

        write_state(state=%state, value=%value)
        %x = read_state(input=%state)
    :::
    ::::

    Parameters[:]

    :   

        **state: state\<ST\> (Required)**

        :   

        **value: ST (Required)**

        :   

    Attributes[:]

    :   

        **ST: tensor**

        :   

    Returns[:]

    :   

        ST

        :   

[]

## elementwise_binary[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[add]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#add)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.add "Link to this definition")

:   Return [`x`]` `[`+`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: \<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[equal]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#equal)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.equal "Link to this definition")

:   Return the truth value of [`x`]` `[`==`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) ([`1`] for true, [`0`] for false in numeric domain).

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: \<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        \<\*, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[floor_div]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#floor_div)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.floor_div "Link to this definition")

:   Return [`x`]` `[`/`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html), rounded towards negative infinity.

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*, T\>

        :   - A tensor of the same type and shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[greater]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#greater)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.greater "Link to this definition")

:   Return the truth value of [`x`]` `[`>`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) ([`1`] for true, [`0`] for false in numeric domain).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[greater_equal]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#greater_equal)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.greater_equal "Link to this definition")

:   Return the truth value of [`x`]` `[`>=`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) ([`1`] for true, [`0`] for false in numeric domain).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[less]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#less)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.less "Link to this definition")

:   Return the truth value of [`x`]` `[`<`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) ([`1`] for true, [`0`] for false in numeric domain).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[less_equal]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#less_equal)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.less_equal "Link to this definition")

:   Return the truth value of [`x`]` `[`<=`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) ([`1`] for true, [`0`] for false in numeric domain).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[logical_and]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#logical_and)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.logical_and "Link to this definition")

:   Return the truth value of [`x`]` `[`AND`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[logical_or]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#logical_or)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.logical_or "Link to this definition")

:   Return the truth value of [`x`]` `[`OR`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[logical_xor]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#logical_xor)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.logical_xor "Link to this definition")

:   Return the truth value of [`x`]` `[`XOR`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, bool\>

        :   - A boolean tensor with the same shape as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[maximum]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#maximum)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.maximum "Link to this definition")

:   Return [`x`]` `[`>`]` `[`y`]` `[`?`]` `[`x`]` `[`:`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor with the broadcasted shape from inputs, and type is derived from inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[minimum]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#minimum)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.minimum "Link to this definition")

:   Return [`x`]` `[`>`]` `[`y`]` `[`?`]` `[`y`]` `[`:`]` `[`x`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor with the broadcasted shape from inputs, and type is derived from inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[mod]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#mod)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.mod "Link to this definition")

:   Return [`x`]` `[`%`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor with the broadcasted shape from inputs, and type is derived from inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[mul]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#mul)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.mul "Link to this definition")

:   Return [`x`]` `[`*`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor with the broadcasted shape from inputs, and type is derived from inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[not_equal]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#not_equal)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.not_equal "Link to this definition")

:   Return the truth value of [`x`]` `[`!=`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html) ([`1`] for true, [`0`] for false in numeric domain).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, bool\>

        :   - A boolean tensor with the broadcasted shape from inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[real_div]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#real_div)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.real_div "Link to this definition")

:   Return [`x`]` `[`/`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor with the broadcasted shape from inputs, and type is derived from inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[pow]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#pow)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.pow "Link to this definition")

:   Return [`x`]` `[`^`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor with the broadcasted shape from inputs, and type is derived from inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.]][[sub]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html#sub)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_binary.sub "Link to this definition")

:   Return [`x`]` `[`-`]` `[`y`] element-wise with [broadcasting](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

    Parameters[:]

    :   

        **x: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`y`] in broadcast.

        **y: tensor\<\*, T\> (Required)**

        :   - Shape must be compatible with [`x`] in broadcast.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor with the broadcasted shape from inputs, and type is derived from inputs.

[]

## elementwise_unary (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[abs]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#abs)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.abs "Link to this definition")

:   Return the absolute values of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[acos]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#acos)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.acos "Link to this definition")

:   Return the inverse cosine values of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[asin]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#asin)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.asin "Link to this definition")

:   Return the inverse sine of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[atan]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#atan)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.atan "Link to this definition")

:   Return the inverse tangent of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[atanh]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#atanh)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.atanh "Link to this definition")

:   Return the inverse hyperbolic tangent values of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[cast]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#cast)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.cast "Link to this definition")

:   Cast the input [`x`] to the new type [`dtype`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **dtype: const str (Required)**

        :   - Can be one of the following types: [`int32`], [`fp16`], [`fp32`], [`bool`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32, bool.**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], dtype\>

        :   - A tensor of the same shape as [`x`], with type [`dtype`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[ceil]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#ceil)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.ceil "Link to this definition")

:   Return the ceil values of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[clip]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#clip)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.clip "Link to this definition")

:   Clip the values in the input [`x`] to [`[alpha,`]` `[`beta]`], element-wise. Any values less than [`alpha`] are set to [`alpha`], and any values greater than [`beta`] are set to [`beta`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

        **beta: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[cos]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#cos)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.cos "Link to this definition")

:   Return cosine of [`x`] element-wise. Input domain is [`(-inf,`]` `[`inf)`] and output range is [`[-1,1]`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[cosh]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#cosh)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.cosh "Link to this definition")

:   Return hyperbolic cosine of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[erf]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#erf)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.erf "Link to this definition")

:   Return the gauss error function of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[exp]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#exp)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.exp "Link to this definition")

:   Return e\^x, element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[exp2]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#exp2)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.exp2 "Link to this definition")

:   Return 2\^x, element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[floor]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#floor)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.floor "Link to this definition")

:   Return the floor of the input [`x`], element-wise, the same as rounding towards negative infinity.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[inverse]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#inverse)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.inverse "Link to this definition")

:   Return the reciprocal value of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **epsilon: const T (Optional, default=1e-4)**

        :   - This is a small constant that is added to the input, before taking its inverse, for stability.

            - [`y`]` `[`=`]` `[`1`]` `[`/`]` `[`(x`]` `[`+`]` `[`epsilon)`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[log]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#log)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.log "Link to this definition")

:   Return the natural logarithm value of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **epsilon: const T (Optional, default=1e-45)**

        :   - This is a small constant that is added to the input, before taking log.

            - [`y`]` `[`=`]` `[`log(x`]` `[`+`]` `[`epsilon)`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[logical_not]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#logical_not)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.logical_not "Link to this definition")

:   Return the value of NOT the input [`x`], element-wise. ([`1`] for true, [`0`] for false in numeric domain.) A numeric value [`t`] is evaluated to true [`iff`]` `[`t`]` `[`!=`]` `[`0`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], bool\> (Required)**

        :   

    Attributes[:]

    :   

        **T: bool**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], bool\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[round]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#round)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.round "Link to this definition")

:   Return the round value of the input [`x`] to nearest integer, element-wise. [`0.5`] is rounded to [`0`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[rsqrt]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#rsqrt)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.rsqrt "Link to this definition")

:   Return the reciprocal value of the square root of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **epsilon: const T (Optional, default=1e-12)**

        :   - This is a small constant that is added to the input, before applying the [`rsqrt`] function, for stability.

            - [`y`]` `[`=`]` `[`1`]` `[`/`]` `[`sqrt(x`]` `[`+`]` `[`epsilon)`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[sign]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#sign)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.sign "Link to this definition")

:   Return the sign value of the input [`x`], element-wise.

    All elements in the output will be either [`-1`] or [`1`], or zero if the input [`x`] is zero.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[sin]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#sin)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.sin "Link to this definition")

:   Return the sine value of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[sinh]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#sinh)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.sinh "Link to this definition")

:   Return the hyperbolic sine value of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[sqrt]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#sqrt)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.sqrt "Link to this definition")

:   Returns the square root value of the input [`x`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[square]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#square)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.square "Link to this definition")

:   Return [`x^2`], element-wise.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[tan]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#tan)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.tan "Link to this definition")

:   Return the tangent value of the input [`x`], element-wise. Both input and output ranges are [`(-inf,`]` `[`inf)`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[tanh]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#tanh)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.tanh "Link to this definition")

:   Return the hyperbolic tangent value of the input [`x`], element-wise. Both input and output ranges are [`(-inf,`]` `[`inf)`] while output range is [`[-1,`]`  `[`1]`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.]][[threshold]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html#threshold)[](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.threshold "Link to this definition")

:   Set a lower bound [`alpha`] to the values in the input [`x`], element-wise. Any values less than [`alpha`] are set to [`alpha`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

[]

## elementwise_unary (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.]][[cast]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/elementwise_unary.html#cast)[](#coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.cast "Link to this definition")

:   Cast the input [`x`] to the new type [`dtype`]. The only difference between this version and the iOS 15 [[`cast`]](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.cast "coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.cast") is that it supports int8, uint8, int16, and uint16.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **dtype: const str (Required)**

        :   - Can be one of the following types: [`int8`], [`uint8`], [`int16`], [`uint16`], [`int32`], [`fp16`], [`fp32`], or [`bool`].

    Attributes[:]

    :   

        **T: i8, ui8, i16, ui16, i32, fp16, fp32, bool.**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], dtype\>

        :   - A tensor of the same shape as [`x`], with type [`dtype`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.]][[clip]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/elementwise_unary.html#clip)[](#coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.clip "Link to this definition")

:   Clip the values in the input [`x`] to [`[alpha,`]` `[`beta]`], element-wise. Any values less than [`alpha`] are set to [`alpha`], and any values greater than [`beta`] are set to [`beta`].

    The major difference between this version and the iOS 15 [[`clip`]](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.clip "coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.clip") is that it uses strict validation to ensure that [`alpha`]` `[`<`]` `[`beta`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **alpha: const T (Required)**

        :   

        **beta: const T (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.]][[inverse]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/elementwise_unary.html#inverse)[](#coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.inverse "Link to this definition")

:   Return the reciprocal value of the input [`x`], element-wise. The only difference between this version and the iOS 15 [[`inverse`]](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.inverse "coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.inverse") is [`epsilon`] may have different dtypes than the inputs/outputs.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **epsilon: const U (Optional, default=1e-4)**

        :   - This is a small constant that is added to the input, before taking its inverse, for stability.

            - [`y`]` `[`=`]` `[`1`]` `[`/`]` `[`(x`]` `[`+`]` `[`epsilon)`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.]][[log]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/elementwise_unary.html#log)[](#coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.log "Link to this definition")

:   Return the natural logarithm value of the input [`x`], element-wise. The only difference between this version and the iOS 15 [[`log`]](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.log "coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.log") is [`epsilon`] may have different dtypes than the inputs/outputs.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **epsilon: const U (Optional, default=1e-45)**

        :   - This is a small constant that is added to the input, before taking log.

            - [`y`]` `[`=`]` `[`log(x`]` `[`+`]` `[`epsilon)`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.]][[rsqrt]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/elementwise_unary.html#rsqrt)[](#coremltools.converters.mil.mil.ops.defs.iOS17.elementwise_unary.rsqrt "Link to this definition")

:   Return the reciprocal value of the square root of the input [`x`], element-wise. The only difference between this version and the iOS 15 [[`rsqrt`]](#coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.rsqrt "coremltools.converters.mil.mil.ops.defs.iOS15.elementwise_unary.rsqrt") is [`epsilon`] may have different dtypes than the inputs/outputs.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   

        **epsilon: const U (Optional, default=1e-12)**

        :   - This is a small constant that is added to the input, before applying the [`rsqrt`] function, for stability.

            - [`y`]` `[`=`]` `[`1`]` `[`/`]` `[`sqrt(x`]` `[`+`]` `[`epsilon)`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d\], T\>

        :   - A tensor of the same shape as [`x`].

[]

## image_resizing (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[affine]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#affine)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.affine "Link to this definition")

:   Apply a linear affine transform to the input 2D image tensor. The value at the [`(x,`]` `[`y)`] (i.e., [`(w,`]` `[`h)`]) coordinate of the output is computed by first computing the coordinates [`x’`] and [`y’`] with the following equation, and then computing the value at the coordinate [`(x’,y’)`] in the input image using either bilinear or nearest neighbor interpolation. If the [`(x’,`]` `[`y’)`] point falls outside the input image, then padding information is used to compute the value:

    :::: 
    ::: highlight
        x’ = a0 * x + a1 * y + a2
        y’ = b0 * x + b1 * y + b2
    :::
    ::::

    Parameters[:]

    :   

        **x: tensor\<\[B, C, H1, W1\], T\>**

        :   - Must be rank [`4`].

        **transform_matrix: tensor\<\[D, 6\], T\>**

        :   - Must be rank [`2`].

            - 

              [`D`] can be either [`B`] or 1.

              :   - If [`D`]` `[`==`]` `[`B`], there is a separate transform matrix for each batch.

                  - If [`D`]` `[`==`]` `[`1`], the same matrix is used for all input batches.

                  - For each batch: [`[a0,`]` `[`a1,`]` `[`a2,`]` `[`b0,`]` `[`b1,`]` `[`b2]`].

        **output_height: const\<i32\>**

        :   - Target output height

        **output_width: const\<i32\>**

        :   - Target output width

        **sampling_mode: const\<str\>**

        :   - Allowed values: [`"bilinear"`]

        **padding_mode: const\<str\>**

        :   - Allowed values: [`"constant"`].

            - Note that the following example is 1D case for brevity. The op supports only 2D image input.

            - 

              If [`padding_mode`]` `[`==`]` `[`"constant"`]:

              :   - The input image is assumed to be padded with the padding_value.

                  - For example, [`|1,`]` `[`2,`]` `[`3|`]` `[`->`]` `[`|0,`]` `[`0,`]` `[`0,`]` `[`1,`]` `[`2,`]` `[`3,`]` `[`0,`]` `[`0,`]` `[`0|`].

        **padding_value: const\<T\>**

        :   - Currently non-zero values are not supported.

            - To be used only when [`padding_mode`]` `[`==`]` `[`"constant"`], ignored in other cases.

        **coordinates_mode: const\<str\>**

        :   - Allowed values: [`"normalized_minus_one_to_one"`].

            - If [`coordinates_mode`]` `[`==`]` `[`"normalized_minus_one_to_one"`], in-image values are [`[-1,`]` `[`1]`].

            - 

              For example, if [`coordinates_mode`]` `[`==`]` `[`"normalized_minus_one_to_one"`], the in-range values are [`[-1,`]` `[`1]`]. That is:

              :   - [`(-1,`]` `[`-1)`], i.e. [`(w=-1,`]` `[`h=-1)`], corresponds to the top-left pixel.

                  - [`(1,`]` `[`-1)`], i.e. [`(w=1,`]` `[`h=-1)`], corresponds to the top-right pixel.

                  - [`(-1,`]` `[`1)`], i.e. [`(w=-1,`]` `[`h=1)`], corresponds to the bottom-left pixel.

                  - [`(1,`]` `[`1)`], i.e. [`(w=1,`]` `[`h=1)`], corresponds to the bottom-right pixel.

        **align_corners: const\<bool\>**

        :   - Currently [`align_corners=False`] is not supported.

            - To be used only when [`coordinates_mode`]` `[`!=`]` `[`unnormalized`], ignored otherwise.

            - If [`align_corners`]` `[`==`]` `[`True`], the extrema coordinates correspond to the center of the first and last corner pixels.

            - If [`align_corners`]` `[`==`]` `[`False`], the extrema coordinates correspond to the edge of the first and last corner pixels.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[B, C, output_height, output_width\], T\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[crop]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#crop)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.crop "Link to this definition")

:   Crop the spatial dimensions (last two dimensions) of the input by the specified amounts.

    Parameters[:]

    :   

        **x: tensor\<\[\*D, H1, W1\],T\> (Required)**

        :   - Must be at least rank [`3`].

        **crop_height: const\<2, i32\> (Required)**

        :   - Amount to be cropped from the top and bottom of the height dimension ([`axis=-2`]).

        **crop_width: const\<2, i32\> (Required)**

        :   - Amount to be cropped from the left and right sides of the width dimension ([`axis=-1`]).

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D, H2, W2\],T\>

        :   - Tensor with same type as the input.

            - [`H2`] = [`H1`]` `[`-`]` `[`crop_height[0]`]` `[`-`]` `[`crop_height[1]`].

            - [`W2`] = [`W1`]` `[`-`]` `[`crop_width[0]`]` `[`-`]` `[`crop_width[1]`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[crop_resize]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#crop_resize)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.crop_resize "Link to this definition")

:   Resize the spatial dimensions (last two dimensions) of the first input according to the bounding boxes specified in the second input, using bilinear interpolation.

    Parameters[:]

    :   

        **x: tensor\<\[B, C, H, W\],T\> (Required)**

        :   - The input, from which patches (regions of interest) are extracted and resized using bilinear interpolation.

            - Rank [`4`].

        **roi: tensor\<\[N,1,4,1,1\], T\> or tensor\<\[N,1,5,1,1\], T\> (Required)**

        :   - Regions of interest, or coordinates of the boxes. The above input represents coordinates of [`N`] boxes.

            - The convention to express coordinates depends on the value of the input [`box_coordinate_mode`].

            - Rank [`5`].

            - If [`tensor<[N,1,4,1,1],`]` `[`T>`]: Resized images are computed for all [`B`] input images.

            - If [`tensor<[N,1,5,1,1],`]` `[`T>`]: The first element from [`axis=-3`] to be resized is an index. It must be within range [`[0,`]` `[`B)`].

        **target_height: const\<i32\> (Optional, Default=1)**

        :   - Target height for resizing each patch.

        **target_width: const\<i32\> (Optional, Default=1)**

        :   - Target width for resizing each patch.

        **normalized_coordinates**[const\<bool\> (Optional, default=False)]

        :   - If [`True`], the bounding box coordinates must be in the interval [`[0,`]` `[`1]`]. Scaling is based on the input spatial dimensions: [`(H_in`]` `[`-`]` `[`1)`] for height and [`(W_in`]` `[`-`]` `[`1)`] for width.

            - If [`False`], the bounding box coordinates must be in the interval [`[0,`]` `[`H_in`]` `[`-`]` `[`1]`] for height dimensions and [`[0,`]` `[`W_in`]` `[`-`]` `[`1]`] for width dimensions.

        **spatial_scale**[const\<fp32\> (Optional, default=1.0)]

        :   - Additional spatial scale that multiplies the bounding box coordinates. You would use this to implement the RoI Align layer, which typically uses unnormalized RoI coordinates along with a spatial scale that is less than or equal to 1.

        **box_coordinate_mode: const\<str\> (Optional, default="CORNERS_HEIGHT_FIRST")**

        :   - Specifies the convention for specifying the four bounding box coordinates for an image of size [`(Height,`]` `[`Width)`]. The [`(0,0)`] coordinate corresponds to the top-left corner of the image.

            - This parameter can take one of four values:

              [`"CORNERS_HEIGHT_FIRST"`]: [`[h_start,`]` `[`w_start,`]` `[`h_end,`]` `[`w_end]`]

              [`"CORNERS_WIDTH_FIRST"`]: [`[w_start,`]` `[`h_start,`]` `[`w_end,`]` `[`h_end]`]

              [`"CENTER_SIZE_HEIGHT_FIRST"`]: [`[h_center,`]` `[`w_center,`]` `[`box_height,`]` `[`box_width]`]

              [`"CENTER_SIZE_WIDTH_FIRST"`]: [`[w_center,`]` `[`h_center,`]` `[`box_width,`]` `[`box_height]`]

        **sampling_mode**[const\<str\> (Optional, default="DEFAULT")]

        :   - This parameter can take [`"STRICT_ALIGN_CORNERS"`], [`"ALIGN_CORNERS"`], [`"DEFAULT"`], [`"OFFSET_CORNERS"`] or [`UNALIGN_CORNERS`] as values.

            - This same convention is used by the [`resize_bilinear`] op (see that op for details).

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[N, B, C, target_height, target_width\],T\> or tensor\<\[N, 1, C, target_height, target_width\],T\>

        :   - Tensor with same type as the input.

            - If [`roi`]` `[`:`]` `[`tensor<[N,1,4,1,1],`]` `[`T>`], the output is [`tensor<[N,`]` `[`B,`]` `[`C,`]` `[`target_height,`]` `[`target_width],T>`]. Total crops = [`N*B`]; that is, [`N`] crops for each input in the batch.

            - If [`roi`]` `[`:`]` `[`tensor<[N,1,5,1,1],`]` `[`T>`], the output is [`tensor<[N,`]` `[`1,`]` `[`C,`]` `[`target_height,`]` `[`target_width],T>`]. Total crops = [`N`]; that is, 1 crop for given input image index in the batch.

    ::: 
    See also

    [[`resize_bilinear`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear")

    :   
    :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[resample]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#resample)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resample "Link to this definition")

:   Resample the input image tensor [`x`] at the [`coordinates`]. Resampling is required if the coordinates do not correspond to exact pixels in the input image. The [`sampling_mode`] determines the algorithm used for resampling and computing the values.

    Parameters[:]

    :   

        **x: tensor\<\[B, C, H1, W1\], T\>**

        :   - Must be rank [`4`].

        **coordinates: tensor\<\[B, H2, W2, 2\], U\>**

        :   - Must be rank [`4`].

            - Coordinates are provided in the order [`(x,`]` `[`y)`] (i.e. [`(w,`]` `[`h)`]).

            - The value of each output location [`output[b,`]` `[`c,`]` `[`h,`]` `[`w]`] is calculated by sampling from the input image [`x[b,`]` `[`c,`]` `[`:,`]` `[`:]`].

            - The pixel at the [`(x,`]` `[`y)`] location corresponds to the length-2 vector: [`coordinates[b,`]` `[`h,`]` `[`w,`]` `[`:]`].

            - Coordinate (normalized or unnormalized) should be specified according to [`coordinates_mode`].

        **sampling_mode: const\<str\>**

        :   - Allowed values: [`"bilinear"`] , [`"nearest"`]

        **padding_mode: const\<str\>**

        :   - Allowed values: [`"constant"`], [`"border"`], [`"reflection"`], [`"symmetric"`]

            - Note that the following example is 1D case for brevity. The op supports only 2D image input.

            - 

              If [`padding_mode`]` `[`==`]` `[`"constant"`]:

              :   - The input image is assumed to be padded with the [`padding_value`].

                  - For example: [`|1,`]` `[`2,`]` `[`3|`]` `[`->`]` `[`|0,`]` `[`0,`]` `[`0,`]` `[`1,`]` `[`2,`]` `[`3,`]` `[`0,`]` `[`0,`]` `[`0|`]

            - 

              if [`padding_mode`]` `[`==`]` `[`"border"`]:

              :   - The input image is assumed to be padded with the values replicated from the values at the edge. This is also referred to as the "clamped" or "replication" mode, since the padded values are clamped to the border values.

                  - For example: [`|1,`]` `[`2,`]` `[`3|`]` `[`->`]` `[`|1,`]` `[`1,`]` `[`1,`]` `[`1,`]` `[`2,`]` `[`3,`]` `[`3,`]` `[`3,`]` `[`3|`]

            - 

              If [`padding_mode`]` `[`==`]` `[`"reflection"`]:

              :   - The border values are reflected, *not* including the values at the edge/border.

                  - For example: [`|1,`]` `[`2,`]` `[`3|`]` `[`->`]` `[`|2,`]` `[`3,`]` `[`2,`]` `[`1,`]` `[`2,`]` `[`3,`]` `[`2,`]` `[`1,`]` `[`2|`]

            - 

              If [`padding_mode`]` `[`==`]` `[`"symmetric"`]:

              :   - Values are reflected, including the border/edge values.

                  - For example: [`|1,`]` `[`2,`]` `[`3|`]` `[`->`]` `[`|3,`]` `[`2,`]` `[`1`]` `[`,`]` `[`1,`]` `[`2,`]` `[`3,`]` `[`3,`]` `[`2,`]` `[`1|`]

        **padding_value: const\<T\>**

        :   - To be used only when [`padding_mode`]` `[`==`]` `[`"constant"`], ignored in other cases.

        **coordinates_mode: const\<str\>**

        :   - Allowed values: [`"unnormalized"`], [`"normalized_minus_one_to_one"`], [`"normalized_zero_to_one"`]

            - If [`coordinates_mode`]` `[`==`]` `[`"unnormalized"`], the coordinates input values are interpreted to be in range [`[0,`]` `[`W`]` `[`-`]` `[`1]`]` `[`/`]` `[`[0,`]` `[`H`]` `[`-`]` `[`1]`], which corresponds to the in-image point.

            - If [`coordinates_mode`]` `[`==`]` `[`"normalized_minus_one_to_one"`], the in-image values are [`[-1,`]` `[`1]`].

            - If [`coordinates_mode`]` `[`==`]` `[`"normalized_zero_to_one"`], in-image values are [`[0,`]` `[`1]`].

            - 

              For example, if [`coordinates_mode`]` `[`==`]` `[`"normalized_minus_one_to_one"`], the in range values are \[-1, 1\]. That is:

              :   - [`(-1,`]` `[`-1)`], i.e. [`(w=-1,`]` `[`h=-1)`], corresponds to the top-left pixel.

                  - [`(1,`]` `[`-1)`], i.e. [`(w=1,`]` `[`h=-1)`], corresponds to the top-right pixel.

                  - [`(-1,`]` `[`1)`], i.e. [`(w=-1,`]` `[`h=1)`], corresponds to the bottom-left pixel.

                  - [`(1,`]` `[`1)`], i.e. [`(w=1,`]` `[`h=1)`], corresponds to the bottom-right pixel.

        **align_corners: const\<bool\>**

        :   - If [`align_corners`]` `[`==`]` `[`True`], the extrema coordinates correspond to the center of the first and last corner pixels.

            - If [`align_corners`]` `[`==`]` `[`False`], the extrema coordinates correspond to the edge of the first and last corner pixels.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp32, int32**

        :   

    Returns[:]

    :   

        tensor\<\[B, C, H2, W2\], T\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[resize_bilinear]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#resize_bilinear)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear "Link to this definition")

:   Resize the spatial (last two) dimensions to the specified target size using bilinear interpolation. Although this op is similar to [`upsample_bilinear`], [`resize_bilinear`] works with a target size rather than with scale factors.

    Parameters[:]

    :   

        **x: tensor\<\[\*D, H1, W1\],T\> (Required)**

        :   - Must be at least rank [`3`].

        **target_size_height: const\<int32\> (Optional, default=1)**

        :   - Target spatial size for the height dimension ([`axis=-2`]).

        **target_size_width: const\<int32\> (Optional, default=1)**

        :   - Target spatial size for the width dimension ([`axis=-1`]).

        **sampling_mode: const\<str\> (Optional, default="DEFAULT")**

        :   - This parameter can take [`"STRICT_ALIGN_CORNERS”`], [`"ALIGN_CORNERS"`], [`"DEFAULT"`], [`"OFFSET_CORNERS"`] or [`UNALIGN_CORNERS`] as values. For details, see the Notes section.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D, H2, W2\],T\>

        :   - Tensor with same type as the input.

            - [`H2`] = [`target_size_height`].

            - [`W2`] = [`target_size_width`].

    Notes

    To understand the [`sampling_mode`] parameter, consider the 1-D case. You need to sample a grid of pixels whose values are computed using linear interpolation. This parameter controls how the grid is sampled. If the input grid is [`[0,`]` `[`Xin-1]`] (corresponding to an input size of [`Xin`]), and if the output size is [`Xout`], then the grid points are sampled in the following manner:

    :::: 
    ::: highlight
        # "STRICT_ALIGN_CORNERS":
        spacing = (Xin - 1) / (Xout - 1)
        grid_point[i] = min(Xin-1, max(0, i*spacing)), for i=0,1,...,Xout-1

        # "ALIGN_CORNERS": Same as "STRICT_ALIGN_CORNERS" unless Xout=1,
        # in which case:
        grid_point[0] = (Xin-1) / 2, if Xout==1

        # "DEFAULT":
        spacing = (Xin - Xin/Xout) / (Xout - 1)
        grid_point[i] = min(Xin-1, max(0, i*spacing)), for i=0,1,...,Xout-1

        # "OFFSET_CORNERS":
        delta = max(1, Xin - 1) / Xout
        spacing = ((Xout - 1) * delta) / (Xout - 1)
        grid_point[i] = min(Xin-1, max(0, 0.5*delta + i*spacing)), for
        ...   i=0,1,...,Xout-1

        # "UNALIGN_CORNERS":
        spacing = Xin / Xout
        grid_point[i] = min(Xin - 1, max(0, i*spacing + 0.5*spacing - 0.5)), for i=0,1,...,Xout-1
    :::
    ::::

    For example:

    :::: 
    ::: highlight
        Xin = 2
        input_interval = [0,1]
    :::
    ::::

    Grid points:

    :::: 
    ::: highlight
        [0., 0.1, 0.5, 0.9, 1.] (Xout = 5, UNALIGN_CORNERS)
        [0., 0.25, 0.5, 0.75, 1.] (Xout = 5, "STRICT_ALIGN_CORNERS" / "ALIGN_CORNERS")
        [0., 0.4, 0.8, 1., 1.] (Xout = 5, "DEFAULT")
        [0.1, 0.3, 0.5, 0.7, 0.9] (Xout = 5, "OFFSET_CORNERS")

        [0., 0., 0.33, 0.67, 1., 1.] (Xout = 6, UNALIGN_CORNERS)
        [0., 0.2, 0.4, 0.6, 0.8, 1.] (Xout = 6, "STRICT_ALIGN_CORNERS" / "ALIGN_CORNERS")
        [0., 0.33, 0.67, 1., 1., 1.] (Xout = 6, "DEFAULT")
        [0.08, 0.25, 0.42, 0.58, 0.75, 0.92] (Xout = 6, "OFFSET_CORNERS")
    :::
    ::::

    Note the following similarities:

    > ::: 
    > - [`"DEFAULT"`] is same as [`tf.raw_ops.ResizeBilinear(align_corners=False,`]` `[`half_pixel_centers=False)`].
    >
    > - [`"STRICT_ALIGN_CORNERS"`] is same as [`tf.raw_ops.ResizeBilinear(align_corners=True,`]` `[`half_pixel_centers=False)`].
    > :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[resize_nearest_neighbor]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#resize_nearest_neighbor)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_nearest_neighbor "Link to this definition")

:   Resize the spatial (last two) dimensions to the specified target size using nearest neighbor interpolation. Although this op is similar to [`upsample_nearest_neighbor`], [`resize_nearest_neighbor`] works with a target size rather than with scale factors.

    Parameters[:]

    :   

        **x: tensor\<\[\*D, H1, W1\], T\> (Required)**

        :   - Must be at least rank [`3`].

        **target_size_height: const\<int32\> (Required)**

        :   - Target spatial size for the height dimension ([`axis=-2`]).

        **target_size_width: const\<int32\> (Required)**

        :   - Target spatial size for the width dimension ([`axis=-1`]).

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D, H2, W2\], T\>

        :   - Tensor with same type as the input.

            - [`H2`] = [`target_size_height`].

            - [`W2`] = [`target_size_width`].

    ::: 
    See also

    [[`resize_bilinear`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear")

    :   
    :::

    Notes

    See [`resize_bilinear`] for examples.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[upsample_bilinear]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#upsample_bilinear)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.upsample_bilinear "Link to this definition")

:   Upsample the spatial dimensions (last two dimensions) of the input by scale factors using bilinear interpolation. The upsample_bilinear operation in MIL corresponds to the [`recompute_scale_factor=True`] mode in the pyorch bilinear interpolation op. That is, the scale factor is recomputed by the output size. Note that when the [`scale_factor_height`] and [`scale_factor_width`] are floating point, this could result in a different scale factor due to rounding.

    Parameters[:]

    :   

        **x: tensor\<\[\*D, H1, W1\], T\> (Required)**

        :   - Must be at least rank [`3`].

        **scale_factor_height: const\<U\> (Optional, default=1)**

        :   - Scale factor for the height dimension ([`axis=-2`]).

        **scale_factor_width: const\<U\> (Optional, default=1)**

        :   - Scale factor for the width dimension ([`axis=-1`]).

        **align_corners: const\<bool\> (Optional, default=True)**

        :   - This parameter determines how samples are chosen for bilinear interpolation. For details, see the Notes section.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U**[fp32, i32]

        :   

    Returns[:]

    :   

        tensor\<\[\*D, H2, W2\], T\>

        :   - Tensor with same type as the input.

            - [`H2`] = floor([`H1`] \* [`scale_factor_height`]).

            - [`W2`] = floor([`W1`] \* [`scale_factor_width`]).

    Notes

    To understand the [`align_corners`] parameter, consider the 1-D case. You need to sample a grid of pixels whose values are computed using linear interpolation. This parameter controls how the grid is sampled. If the input grid is [`[0,`]` `[`Xin-1]`] (corresponding to an input size of [`Xin`]), and if the output size is [`Xout`], then the grid points are sampled in the following manner:

    :::: 
    ::: highlight
        # If align_corners == True:
        spacing = (Xin - 1) / (Xout - 1)
        grid_point[i] = min(Xin - 1, max(0, i*spacing)), for i=0,1,...,Xout-1

        # If align_corners == False:
        spacing = Xin / Xout
        grid_point[i] = min(Xin - 1, max(0, i*spacing + 0.5*spacing - 0.5)),
        ...   for i=0,1,...,Xout-1
    :::
    ::::

    For example:

    :::: 
    ::: highlight
        Xin = 2
        input_interval = [0,1]
    :::
    ::::

    Grid points:

    :::: 
    ::: highlight
        [0., 0.1, 0.5, 0.9, 1.] (Xout = 5, align_corners=False)
        [0., 0.25, 0.5, 0.75, 1.] (Xout = 5, align_corners=True)
        [0., 0., 0.33, 0.67, 1., 1.] (Xout = 6, align_corners=False)
        [0., 0.2, 0.4, 0.6, 0.8, 1.] (Xout = 6, align_corners=True)
    :::
    ::::

    Note the following similarities:

    - [`align_corners=False`] is the same as [`tf.raw_ops.ResizeBilinear(align_corners=False,`]` `[`half_pixel_centers=True)`].

    - [`align_corners=True`] is the same as [`tf.raw_ops.ResizeBilinear(align_corners=True,`]` `[`half_pixel_centers=False)`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.]][[upsample_nearest_neighbor]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html#upsample_nearest_neighbor)[](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.upsample_nearest_neighbor "Link to this definition")

:   Upsample the spatial dimensions (last two dimensions) of the input by integer scale factors using nearest-neighbor interpolation.

    Parameters[:]

    :   

        **x: tensor\<\[\*D, H1, W1\],T\> (Required)**

        :   - Must be at least rank [`3`].

        **scale_factor_height: const\<i32\> or const\<fp32\> (Optional, default=1)**

        :   - Scale factor for the height dimension ([`axis=-2`]).

            - Can be either an integer or fractional.

        **scale_factor_width: const\<i32\> or const\<fp32\> (Optional, default=1)**

        :   - Scale factor for the width dimension ([`axis=-1`]).

            - Can be either an integer or fractional.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **U: fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D, H2, W2\],T\>

        :   - Tensor with same type as the input.

            - [`H2`] = floor([`H1`] \* [`scale_factor_height`]).

            - [`W2`] = floor([`W1`] \* [`scale_factor_width`]).

[]

## image_resizing (iOS 16+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.]][[crop_resize]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/image_resizing.html#crop_resize)[](#coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.crop_resize "Link to this definition")

:   This version differs from the iOS 15 [[`crop_resize`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.crop_resize "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.crop_resize") by supporting [`pad_value`] as an additional parameter.

    Parameters[:]

    :   

        **pad_value**[const\<T\> (Optional, default=0.0)]

        :   - If the box indexes go beyond the input boundary, the input image is padded with [`pad_value`].

            - Defaults to [`0`].

            - It is the same as [`extrapolation_value`] in [tf.image.crop_and_resize](https://www.tensorflow.org/api_docs/python/tf/image/crop_and_resize).

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.]][[resample]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/image_resizing.html#resample)[](#coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.resample "Link to this definition")

:   This version of [`resample`] supports float 16 coordinates.

    For complete documentation, see the iOS 15 [[`resample`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resample "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resample").

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.]][[upsample_bilinear]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/image_resizing.html#upsample_bilinear)[](#coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.upsample_bilinear "Link to this definition")

:   This version of [`upsample_bilinear`] supports [`half_pixel_centers`]. For complete documentation, see the iOS 15 [[`upsample_bilinear`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.upsample_bilinear "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.upsample_bilinear").

    Parameters[:]

    :   

        **half_pixel_centers: const\<bool\> (Optional)**

        :   - Defaults to [`!align_corners`] if not provided.

[]

## image_resizing (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.image_resizing "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.image_resizing.]][[crop_resize]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/image_resizing.html#crop_resize)[](#coremltools.converters.mil.mil.ops.defs.iOS17.image_resizing.crop_resize "Link to this definition")

:   The major differences between this version and the iOS 16 [[`crop_resize`]](#coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.crop_resize "coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.crop_resize") are as follows:

    - The input [`ROI`] is replaced by [`boxes`] and [`box_indices`].

    - The dtype domain of input [`x`], [`boxes`], and [`box_indices`] are independent.

    - The output no longer has the [`B`] dim. The output is [`[N,`]` `[`C,`]` `[`target_height,`]` `[`target_width]`] rather than the [`[N,`]` `[`B,`]` `[`C,`]` `[`target_height,`]` `[`target_width]`] in iOS 16.

    Parameters[:]

    :   

        **x: tensor\<\[B, C, H, W\], T\> (Required)**

        :   - The input, from which patches (regions of interest) are extracted and resized using bilinear interpolation.

            - Rank [`4`].

        **boxes: tensor\<\[N, 4\], BOX_T\> (Required)**

        :   - Coordinates of [`N`] boxes.

            - The convention to express coordinates depends on the value of [`box_coordinate_mode`].

            - If [`normalized_coordinates`] is True, only fp16 and fp32 dtypes are allowed.

        **box_indices: tensor\<\[N\], BOX_INDEX_T\> (Optional)**

        :   - Default is [`arange(N)`], or [`[0,`]` `[`1,`]` `[`...,`]` `[`N-1]`].

            - If [`box_indices[i]=j`], this means that [`boxes[i]`] will be applied to the [`j`]-th image. Therefore, it is invalid for [`box_indices[i]`] to be greater than [`B`].

        **target_height: const\<i32\> (Optional, Default=1)**

        :   - Target height for resizing each patch.

        **target_width: const\<i32\> (Optional, Default=1)**

        :   - Target width for resizing each patch.

        **normalized_coordinates**[const\<bool\> (Optional, default=False)]

        :   - If [`True`], the bounding box coordinates must be in the interval [`[0,`]` `[`1]`]. Scaling is based on the input spatial dimensions: [`(H_in`]` `[`-`]` `[`1)`] for height and [`(W_in`]` `[`-`]` `[`1)`] for width.

            - If [`False`], the bounding box coordinates must be in the interval [`[0,`]` `[`H_in`]` `[`-`]` `[`1]`] for height dimensions and [`[0,`]` `[`W_in`]` `[`-`]` `[`1]`] for width dimensions.

        **spatial_scale**[const\<fp32\> (Optional, default=1.0)]

        :   - Additional spatial scale that multiplies the bounding box coordinates.

            - You would use this to implement the RoI Align layer, which typically uses unnormalized RoI coordinates along with a spatial scale that is less than or equal to [`1`].

        **box_coordinate_mode: const\<str\> (Optional, default="CORNERS_HEIGHT_FIRST")**

        :   - Specifies the convention for specifying the four bounding box coordinates for an image of size [`(Height,`]` `[`Width)`]. The [`(0,0)`] coordinate corresponds to the top-left corner of the image.

            - This parameter can take one of four values:

              [`"CORNERS_HEIGHT_FIRST"`]: [`[h_start,`]` `[`w_start,`]` `[`h_end,`]` `[`w_end]`]

              [`"CORNERS_WIDTH_FIRST"`]: [`[w_start,`]` `[`h_start,`]` `[`w_end,`]` `[`h_end]`]

              [`"CENTER_SIZE_HEIGHT_FIRST"`]: [`[h_center,`]` `[`w_center,`]` `[`box_height,`]` `[`box_width]`]

              [`"CENTER_SIZE_WIDTH_FIRST"`]: [`[w_center,`]` `[`h_center,`]` `[`box_width,`]` `[`box_height]`]

        **sampling_mode**[const\<str\> (Optional, default="DEFAULT")]

        :   - This parameter can take [`"STRICT_ALIGN_CORNERS"`], [`"ALIGN_CORNERS"`], [`"DEFAULT"`], [`"OFFSET_CORNERS"`] or [`UNALIGN_CORNERS`] as values.

            - This is the same convention used by the [[`resize_bilinear`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear") op.

        **pad_value**[const\<T\> (Optional, default=0.0)]

        :   - If the box indexes go beyond the input boundary, the input image is padded with [`pad_value`].

            - Defaults to [`0`].

            - It is the same as [`extrapolation_value`] in [tf.image.crop_and_resize](https://www.tensorflow.org/api_docs/python/tf/image/crop_and_resize).

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **BOX_T: fp16, fp32, uint16**

        :   

        **BOX_INDEX_T: uint16, int32**

        :   

    Returns[:]

    :   

        tensor\<\[N, C, target_height, target_width\], T\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.image_resizing.]][[resample]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/image_resizing.html#resample)[](#coremltools.converters.mil.mil.ops.defs.iOS17.image_resizing.resample "Link to this definition")

:   Resample the input image tensor [`x`] at the [`coordinates`].

    The major difference between this version and the iOS 16 [[`resample`]](#coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.resample "coremltools.converters.mil.mil.ops.defs.iOS16.image_resizing.resample") is that coordinates supports int8, uint8, int16, uint16.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.image_resizing.]][[resize]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/image_resizing.html#resize)[](#coremltools.converters.mil.mil.ops.defs.iOS17.image_resizing.resize "Link to this definition")

:   Resizes the input tensor [`x`] by choosing the right-most [`resized_dims`] dimensions from the input shape [`shape`], and by choosing the rest from [`x`] 's shape.

    This iOS17 [`resize`] is a superset of iOS 15 [[`resize_bilinear`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear") and [[`resize_nearest_neighbor`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_nearest_neighbor "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_nearest_neighbor"). The main benefit is that this resize op allows a use-case in dynamic tensor shapes where a tensor needs to be resized to a dynamic shape as specified by another tensor.

    To illustrate how output shape is inferred, the following are two examples:

    - Example #1:

      :::: 
      ::: highlight
          x.shape: [1, 2, 3, 4]
          shape: [1, 6, 8]
          resized_dims: 2
          The output's shape will be [1, 2, 6, 8]
      :::
      ::::

    - Example #2:

      :::: 
      ::: highlight
          x.shape: [1, 2, 3, is0]
          shape: [1, 0, 0]
          resized_dims: 2
          The output's shape will be [1, 2, 3, is0]
      :::
      ::::

    Parameters[:]

    :   

        **x: tensor\<\[...\], T\> (Required)**

        :   

        **shape: tensor\<\[K\], U\> (Required)**

        :   - Restriction: [`size(shape)`] \<= [`rank(x)`].

            - If [`shape[i]==0`], the dimension in the output tensor will instead be inferred from the corresponding element of [`x.shape()`]. Note this might not be [`x.shape()[i]`], as [`size(shape)`], [`resized_dims`], and [`size(x)`] may all be different sizes.

        **resized_dims: const tensor\<\[\], uint32\> (Required)**

        :   - Restriction: [`resized_dims`] \<= [`size(shape)`].

        **interpolation_mode: const\<str\> (Optional, default="LINEAR")**

        :   - Available mode: [`LINEAR`], [`NEAREST_NEIGHBOR`].

        **sampling_mode: const\<str\> (Optional, default="DEFAULT")**

        :   - Available mode: [`DEFAULT`], [`STRICT_ALIGN_CORNERS`], [`ALIGN_CORNERS`], [`OFFSET_CORNERS`], [`UNALIGN_CORNERS`].

            - For details about different sampling modes, see iOS 15 [[`resize_bilinear`]](#coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear "coremltools.converters.mil.mil.ops.defs.iOS15.image_resizing.resize_bilinear").

    Attributes[:]

    :   

        **T: fp16, fp32, int32**

        :   

        **U: int32, int16, uint16, uint32**

        :   

    Returns[:]

    :   

        tensor\<\[...\], T\>

        :   

[]

## linear (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.linear "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.linear.]][[einsum]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/linear.html#einsum)[](#coremltools.converters.mil.mil.ops.defs.iOS15.linear.einsum "Link to this definition")

:   Perform tensor multiplication expressed according to the einsum notation. The mode/equation that is currently supported is multiplying matrices that are laid out on dimensions -1 and -3, treating all the other dimensions as batch. Broadcasting is supported along batch dimensions. In particular, the inputs must be of the following shapes:

    - 

      Rank 4 input case:

      :   - Input 1: [`[B,`]` `[`C,`]` `[`H,`]` `[`W1]`].

          - Input 2: [`[B,`]` `[`W1,`]` `[`H,`]` `[`W2]`].

          - Output: [`[B,`]` `[`C,`]` `[`H,`]` `[`W2]`].

          - If, for one of the inputs, the dimensions [`"B"`] or [`"H"`] is 1, they are broadcast to match the other input.

    - 

      Rank 3 input case:

      :   - Input 1: [`[C,`]` `[`H,`]` `[`W1]`].

          - Input 2: [`[W1,`]` `[`H,`]` `[`W2]`].

          - Output: [`[C,`]` `[`H,`]` `[`W2]`].

          - If, for one of the inputs, the dimension [`"H"`] is 1, it is broadcast to match the other input.

    Parameters[:]

    :   

        **values**[Tuple(tensor_1, tensor_2)]

        :   - 

              Where:

              :   - [`tensor_1`]: [`tensor<[*D,`]` `[`C,`]` `[`H,`]` `[`W1],`]` `[`T>`].

                  - Must be of rank 3 or 4.

                  - [`tensor_2`]: [`tensor<[*D,`]` `[`W1,`]` `[`H,`]` `[`W2],`]` `[`T>`].

                  - Must be of rank 3 or 4.

        **equation: const\<str\>**

        :   - 

              Supported equations are:

              :   - [`"nchw,nwhu->nchu"`] and its equivalent equation strings.

                  - [`"chw,whr->chr"`] and its equivalent equation strings.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D, C, H, W2\], T\>

        :   - Same ranks as the inputs.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.linear.]][[linear]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/linear.html#linear)[](#coremltools.converters.mil.mil.ops.defs.iOS15.linear.linear "Link to this definition")

:   Perform [`x`]` `[`*`]` `[`weight.T`]` `[`+`]` `[`bias`] where [`weight`] and [`bias`] are constant at compile time.

    Parameters[:]

    :   

        **x: tensor\<\[\*D, D_in\], T\> (Required)**

        :   - [`1`]` `[`<=`]` `[`rank`]` `[`<=`]` `[`3`].

            - [`0`]` `[`<=`]` `[`rank(*D)`]` `[`<=`]` `[`2`].

        **weight: const tensor\<\[D_out,D_in\], T\> (Required)**

        :   

        **bias: const tensor\<\[D_out\],T\> (Optional)**

        :   - Default to [`0`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D, D_out\], T\>

        :   - Same rank as the input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.linear.]][[matmul]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/linear.html#matmul)[](#coremltools.converters.mil.mil.ops.defs.iOS15.linear.matmul "Link to this definition")

:   Perform N-D batch matrix multiplication with NumPy-style broadcasting based on the following rules:

    Rule 1. If both [`x,`]` `[`y`] are 1-D, return the scalar from the dot product.

    Rule 2. If both [`x,`]` `[`y`] are 2-D or higher, perform a broadcast on the batch dimensions (all dimensions except the last [`2`]).

    For example:

    - [`x.shape`]` `[`==`]` `[`(10,`]` `[`4,`]` `[`3)`]

    - [`y.shape`]` `[`==`]` `[`(5,`]` `[`10,`]` `[`3,`]` `[`2)`]

    - [`matmul(x,`]` `[`y).shape`]` `[`==`]` `[`(5,`]` `[`10,`]` `[`4,`]` `[`2)`]

    Conventional matrix multiplication is a special case where both [`x,`]` `[`y`] are exactly 2-D. For example:

    - [`x.shape`]` `[`==`]` `[`(4,`]` `[`3)`]

    - [`y.shape`]` `[`==`]` `[`(3,`]` `[`2)`]

    - [`matmul(x,`]` `[`y).shape`]` `[`==`]` `[`(4,`]` `[`2)`]

    If [`x`] is 1-D, and [`y`] is N-D where [`N`]` `[`>=`]` `[`2`], [`x`] is first promoted to matrix [`xm`] by prepending a [`1`] to its dimension, and the resulting [`xm`] is broadcast to [`y`] following Rule 2 above. After this, remove the inserted dimension. For example:

    - [`x.shape`]` `[`==`]` `[`(4)`]

    - [`y.shape`]` `[`==`]` `[`(10,`]` `[`4,`]` `[`3)`]

    - [`xm.shape`]` `[`==`]` `[`(1,`]` `[`4)`]

    - [`matmul(xm,`]` `[`y).shape`]` `[`==`]` `[`(10,`]` `[`1,`]` `[`3)`]

    - Removing the inserted dimension results in [`matmul(x,`]` `[`y).shape`]` `[`==`]` `[`(10,`]` `[`3)`].

    - Note: [`xm`] and [`matmul(xm,`]` `[`y)`] are for illustration only.

    If [`x`] is N-D where [`N`]` `[`>=`]` `[`2`], and [`y`] is 1-D, [`y`] is first promoted to matrix [`ym`] by appending a [`1`] to its dimension, and the resulting [`ym`] is broadcast to [`x`] following Rule 2 above. After this, remove the inserted dimension. For example:

    - [`x.shape`]` `[`==`]` `[`(10,`]` `[`3,`]` `[`4)`]

    - [`y.shape`]` `[`==`]` `[`(4,)`]

    - [`ym.shape`]` `[`==`]` `[`(4,`]` `[`1)`]

    - [`matmul(x,`]` `[`ym).shape`]` `[`==`]` `[`(10,`]` `[`3,`]` `[`1)`]

    - Removing the inserted dimension results in [`matmul(x,`]` `[`y).shape`]` `[`==`]` `[`(10,`]` `[`3)`].

    - Note: [`xm`] and [`matmul(xm,`]` `[`y)`] are for illustration only.

    Parameters[:]

    :   

        **x: tensor\<\[\*, K1\], T\> (Required)**

        :   - [`x`] must be 1-D or higher.

        **y: tensor\<\[\*, K2\], T\> (Required)**

        :   - [`y`] must be 1-D or higher.

        **transpose_x: const bool (Optional)**

        :   - Default to [`False`].

            - Use [`True`] to transpose the last two dimensions of [`x`] before multiplication. It has no effect when [`x`] is 1-D.

        **transpose_y: const bool (Optional)**

        :   - Default to [`False`].

            - Use [`True`] to transpose the last two dimensions of [`y`] before multiplication. It has no effect when [`y`] is 1-D.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*, T\>

        :   - Scalar or tensor output.

[]

## linear (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.linear "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.linear.]][[linear]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/linear.html#linear)[](#coremltools.converters.mil.mil.ops.defs.iOS17.linear.linear "Link to this definition")

:   A version of [`linear`] for iOS 17+. The only difference between this version and the iOS 15 [[`linear`]](#coremltools.converters.mil.mil.ops.defs.iOS15.linear.linear "coremltools.converters.mil.mil.ops.defs.iOS15.linear.linear") is that the [`weight`] and [`bias`] may have a different dtype than the input/output.

    Parameters[:]

    :   

        **x: tensor\<\[\*D, D_in\], T\> (Required)**

        :   - [`1`]` `[`<=`]` `[`rank`]` `[`<=`]` `[`3`].

            - [`0`]` `[`<=`]` `[`rank(*D)`]` `[`<=`]` `[`2`].

        **weight: const tensor\<\[D_out, D_in\], U\> (Required)**

        :   

        **bias: const tensor\<\[D_out\], U\> (Optional)**

        :   - Default to [`0`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

        **U: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D, D_out\], T\>

        :   - Same rank as the input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.linear.]][[matmul]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/linear.html#matmul)[](#coremltools.converters.mil.mil.ops.defs.iOS17.linear.matmul "Link to this definition")

:   A version of [`matmul`] for iOS 17+. The only difference between this version and the iOS 15 [[`matmul`]](#coremltools.converters.mil.mil.ops.defs.iOS15.linear.matmul "coremltools.converters.mil.mil.ops.defs.iOS15.linear.matmul") is that the [`x`] and [`y`] can have a different dtypes when one of them is const.

    Parameters[:]

    :   

        **x: tensor\<\[\*, K1\], T\> (Required)**

        :   - [`x`] must be 1-D or higher.

        **y: tensor\<\[\*, K2\], U\> (Required)**

        :   - [`y`] must be 1-D or higher.

        **transpose_x: const bool (Optional)**

        :   - Default to [`False`].

            - Use [`True`] to transpose the last two dimensions of [`x`] before multiplication. It has no effect when [`x`] is 1-D.

        **transpose_y: const bool (Optional)**

        :   - Default to [`False`].

            - Use [`True`] to transpose the last two dimensions of [`y`] before multiplication. It has no effect when [`y`] is 1-D.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

        **U: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*, V\>

        :   - Scalar or tensor output.

            - When [`x`] and [`y`] are both const or both non-const, it should follow ios15 behavior that [`x`], [`y`], and [`output`] all have the same dtype. When one of x and y is const, the output dtype should be the same as the non-const one.

[]

## normalization (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.normalization "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.normalization.]][[batch_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/normalization.html#batch_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.batch_norm "Link to this definition")

:   Normalize input tensor [`x`] by [`mean`] and [`variance`], and optionally apply a scale [`gamma`] and an offset [`beta`]:

    ::: 
    \\\[y_i = \\gamma_i \\dfrac} + beta_i \\;,\\;i=1,\....,C\\\]
    :::

    The [`mean`], [`variance`], [`gamma`], and [`beta`] must be 1-D tensors whose lengths are equal to the second axis (the "depth" or "channel" dimension) of [`x`].

    Parameters[:]

    :   

        **x: tensor\<\[n,C,\*D\], T\> (Required)**

        :   - [`3`]` `[`<=`]` `[`rank`]` `[`<=`]` `[`5`].

            - [`*D`] refers to the spatial dimensions, [`1`]` `[`<=`]` `[`rank(*D)`]` `[`<=`]` `[`3`].

            - [`n`] is the batch dimension.

        **mean: const tensor\<\[C\], T\> (Required)**

        :   

        **variance: const tensor\<\[C\], T\> (Required)**

        :   

        **gamma: const tensor\<\[C\], T\> (Optional)**

        :   - Optional scale applied to normalized tensor.

            - Default is all ones.

        **beta: const tensor\<\[C\], T\> (Optional)**

        :   - Optional offset applied to normalized tensor.

            - Default is all zeros.

        **epsilon: const T (Optional)**

        :   - Default is [`1e-5`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n,C,\*D\], T\>

        :   - Output tensor has the same shape and type as the input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.normalization.]][[instance_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/normalization.html#instance_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.instance_norm "Link to this definition")

:   Apply instance normalization to the n-dimensional input tensor.

    Parameters[:]

    :   

        **x: tensor\<\[n,C,\*D\], T\> (Required)**

        :   - [`3`]` `[`<=`]` `[`rank(x)`]` `[`<=`]` `[`4`].

            - [`*D`] refers to the spatial dimensions, [`1`]` `[`<=`]` `[`rank(*D)`]` `[`<=`]` `[`2`].

            - [`n`] is the batch dimension.

        **gamma: const tensor\<\[C\], T\> (Optional)**

        :   - Optional scale applied to normalized tensor.

            - Default to all ones.

        **beta: const tensor\<\[C\], T\> (Optional)**

        :   - Optional offset applied to normalized tensor.

            - Default to all zeros.

        **epsilon: const f32 (Optional)**

        :   - Default to [`1e-5`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n,C,\*D\], T\>

        :   - Output tensor has the same shape and type as the input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.normalization.]][[l2_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/normalization.html#l2_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.l2_norm "Link to this definition")

:   Apply L2 normalization to the n-dimensional input tensor. That is, divide the input tensor by the square root of the sum of squares of all elements of the input.

    ::: 
    \\\[x_i \\leftarrow \\dfrac + \\epsilon}}\\\]
    :::

    Parameters[:]

    :   

        **x: tensor\<\[\*B, \*D\], T\> (Required)**

        :   - Input tensor, [`rank(x)`]` `[`>=`]` `[`3`].

            - [`*B`] refers to the leading dimensions.

            - [`*D`] refers to the spatial dimensions to be normalized. Must be rank 3: [`rank(*D)`]` `[`==`]` `[`3`].

            - When [`rank(x)`]` `[`==`]` `[`3`], in which [`rank(*B)`]` `[`==`]` `[`0`]` `[`and`]` `[`rank(*D)`]` `[`==`]` `[`3`], the input is divided by the square root of the sum of squares of all elements.

            - For ranks greater than 3, in which [`rank(*B)`]` `[`>=`]` `[`1`]` `[`and`]` `[`rank(*D)`]` `[`==`]` `[`3`], the leading dimensions \*B, starting from [`0`] to [`-4`] (inclusive), are all treated as batch. The L2 normalization are done batch-wise.

        **epsilon: const T (Optional)**

        :   - Small constant to avoid division by [`0`].

            - Optional, defaults to [`1e-6`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*B, \*D\], T\>

        :   - Same type and shape as the input tensor [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.normalization.]][[layer_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/normalization.html#layer_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.layer_norm "Link to this definition")

:   Apply layer normalization to the n-dimensional input tensor:

    ::: 
    \\\[out = gamma \* (input - E\[x\]) / sqrt(Var\[x\] + epsilon) + beta\\\]
    :::

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **axes: const\<\[K\], i32\> (Optional)**

        :   - Dimensions to perform layer normalization.

            - Default is [`None`] (all dimensions).

        **gamma: const tensor\<\*?, T\>, T\> (Optional)**

        :   - if provided, the shape must be be [`x.shape[axes]`]. For instance, if input [`x`] with shape [`(3,4,5,6)`] and [`axes`]` `[`=`]` `[`[2,3]`], gamma must have shape [`(5,6)`].

            - Default is all ones.

        **beta: const tensor\<\*?, T\>, T\> (Optional)**

        :   - Same shape as gamma.

            - Default is all zeros.

        **epsilon: const T (Optional)**

        :   - Small constant to avoid division by [`0`].

            - Default is [`1e-5`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>:

        :   - Tensor with same shape and type as the input tensor [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.normalization.]][[local_response_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/normalization.html#local_response_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.local_response_norm "Link to this definition")

:   Apply local response normalization to the n-dimensional input tensor:

    ::: 
    \\\[x_i \\leftarrow \\dfrac} \\sum_j x_j\^2 \\right )\^\\beta}\\\]
    :::

    Parameters[:]

    :   

        **x: tensor\<\[n,C,\*D\], T\> (Required)**

        :   - Input tensor, [`3`]` `[`<=`]` `[`rank(x)`]` `[`<=`]` `[`4`].

            - [`*D`] refers to the spatial dimensions, [`1`]` `[`<=`]` `[`rank(*D)`]` `[`<=`]` `[`2`].

            - [`n`] is the batch dimension.

        **size: const i32 (Required)**

        :   - Amount of neighboring channels to normalize.

        **alpha: const T (Optional)**

        :   - Scale factor.

            - Default is [`1e-4`].

        **beta: const T (Optional)**

        :   - An exponent.

            - Default is [`0.75`].

        **k: const T (Optional)**

        :   - Additive factor.

            - Default is [`1.0`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n,C,\*D\], T\>

        :   - Same type and shape as the input tensor [`x`].

[]

## normalization (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.normalization "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.normalization.]][[batch_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/normalization.html#batch_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS17.normalization.batch_norm "Link to this definition")

:   Normalize input tensor [`x`] by [`mean`] and [`variance`], and optionally apply a scale [`gamma`] and an offset [`beta`]:

    ::: 
    \\\[y_i = \\gamma_i \\dfrac} + beta_i \\;,\\;i=1,\....,C\\\]
    :::

    The difference between this version and the iOS 15 [[`batch_norm`]](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.batch_norm "coremltools.converters.mil.mil.ops.defs.iOS15.normalization.batch_norm") is that input/output can have different dtypes from other parameters.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.normalization.]][[instance_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/normalization.html#instance_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS17.normalization.instance_norm "Link to this definition")

:   Apply instance normalization to the n-dimensional input tensor.

    The difference between this version and the iOS 15 [[`instance_norm`]](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.instance_norm "coremltools.converters.mil.mil.ops.defs.iOS15.normalization.instance_norm") is that input/output can have different dtypes from other parameters.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.normalization.]][[l2_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/normalization.html#l2_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS17.normalization.l2_norm "Link to this definition")

:   Apply L2 normalization to the n-dimensional input tensor. That is, divide the input tensor by the square root of the sum of squares of all elements of the input.

    ::: 
    \\\[x_i \\leftarrow \\dfrac + \\epsilon}}\\\]
    :::

    The difference between this version and the iOS 15 [[`l2_norm`]](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.l2_norm "coremltools.converters.mil.mil.ops.defs.iOS15.normalization.l2_norm") is that input/output and [`epsilon`] can have different dtypes.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.normalization.]][[layer_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/normalization.html#layer_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS17.normalization.layer_norm "Link to this definition")

:   Apply layer normalization to the n-dimensional input tensor:

    ::: 
    \\\[out = gamma \* (input - E\[x\]) / sqrt(Var\[x\] + epsilon) + beta\\\]
    :::

    The difference between this version and the iOS 15 [[`layer_norm`]](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.layer_norm "coremltools.converters.mil.mil.ops.defs.iOS15.normalization.layer_norm") is that input/output can have different dtypes from other parameters.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.normalization.]][[local_response_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/normalization.html#local_response_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS17.normalization.local_response_norm "Link to this definition")

:   Apply local response normalization to the n-dimensional input tensor:

    ::: 
    \\\[x_i \\leftarrow \\dfrac} \\sum_j x_j\^2 \\right )\^\\beta}\\\]
    :::

    The difference between this version and the iOS 15 [[`local_response_norm`]](#coremltools.converters.mil.mil.ops.defs.iOS15.normalization.local_response_norm "coremltools.converters.mil.mil.ops.defs.iOS15.normalization.local_response_norm") is that input/output can have different dtypes from other parameters.

[]

## pool[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.pool "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.pool.]][[avg_pool]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/pool.html#avg_pool)[](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "Link to this definition")

:   Perform average pooling. Supports 1-D, 2-D, and 3-D pool (1, 2, or 3 spatial dimensions).

    Parameters[:]

    :   

        **x: tensor\<\[n,C_in, \*D_in\], T\> (Required)**

        :   - [`3`]` `[`<=`]` `[`rank`]` `[`<=`]` `[`5`].

            - [`D_in`] are spatial dimensions, [`1`]` `[`<=`]` `[`len(D_in)`]` `[`<=`]` `[`3`].

            - [`C_in`] is the number of input channels or depth dimensions.

            - [`n`] is the batch dimension.

        **kernel_sizes: const tensor\<\[K\], T\> (Required)**

        :   - The size of the window for each spatial dimension [`D_in`] of the input tensor.

            - [`K`]` `[`==`]` `[`len(D_in)`]

        **strides: const tensor\<\[S\],i32\> (Optional, default to all 1s)**

        :   - Stride along each of the spatial dimensions.

            - [`S`]` `[`==`]` `[`len(D_in)`].

        **pad_type: const str (Required)**

        :   Must be one of [`valid`], [`same`], [`custom`] or [`same_lower`].

            - [`valid`]: No padding. This is equivalent to custom pad with [`pad[i]`]` `[`=`]` `[`0,`]` `[`for`]` `[`all`]` `[`i`].

            - [`same`] : This is equivalent to custom pad with [`pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`=`]` `[`kernel_size[i]`].

            - [`custom`]: Specify custom padding in the parameter pad. note that [`same`] padding is equivalent to custom padding with [`pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`=`]` `[`kernel_size[i]`].

            - [`same_lower`]: Similar to [`same`] but the padding will place extra rows/cols on the top/left if the padding amount is odd.

        **pad: const\<\[P\],i32\> (Optional. Default to all 0s)**

        :   - [`pad`] represents the number of elements to pad before and after each dimension: [`pad[2*i],`]` `[`pad[2*i+1]`] are the pad size before and after spatial dimension [`i`].

            - [`P`]` `[`=`]` `[`2`]` `[`*`]` `[`len(D_in)`].

            - [`pad`] should be specified if and only if [`pad_type`]` `[`==`]` `[`custom`]

        **exclude_padding_from_average: const tensor\<\[\], bool\> (Optional, default to False)**

        :   - If [`True`], padded values (0s) are excluded from the denominator count when computing the average over the kernel window.

        **ceil_mode: const\<bool\>**

        :   - Same as PyTorch's [`ceil`] mode.

            - [`ceil`] is used instead of floor in calculating the output size.

            - Optional, defaults to [`False`].

            - Only applicable when [`pad_type`] is [`valid`] or [`custom`].

            - When [`ceil_mode`] is True, padding must be symmetric; that is, if specified, [`pad[2*i]`]` `[`==`]` `[`pad[2*i+1]`] must hold.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C_out, \*D_out\], T\>

        :   - Same rank as [`x`].

            - [`C_out`] is the number of output channels or depth dimensions.

            - 

              When [`ceil_mode`]` `[`=`]` `[`False`]:

              :   - [`D_out[i]`]` `[`=`]` `[`floor[(D_in[i]`]` `[`+`]` `[`pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`-`]` `[`kernel_sizes[i])`]` `[`/`]` `[`strides[i]]`]` `[`+1,`]` `[`for`]` `[`i`]` `[`=`]` `[`0,`]` `[`..,`]` `[`len(D_in)`]` `[`-`]` `[`1`] is mathematically the same as (when all parameters involved are integers):

                    > ::: 
                    > - [`D_out[i]`]` `[`=`]` `[`ceil`]` `[`[(D_in[i]`]` `[`+`]` `[`pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`-`]` `[`kernel_size[i]`]` `[`-`]` `[`1)`]` `[`/`]` `[`stride[i]],`]` `[`for`]` `[`i`]` `[`=`]` `[`0,`]` `[`..,`]` `[`len(D_in)`]` `[`-`]` `[`1`].
                    >
                    > - [`*D_out`] is all ones if [`global_pooling`] is [`true`].
                    > :::

            - 

              When [`ceil_mode`]` `[`=`]` `[`True`]:

              :   - [`D_out[i]`]` `[`=`]` `[`ceil[(D_in[i]`]` `[`+`]` `[`pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`-`]` `[`kernel_sizes[i])`]` `[`/`]` `[`strides[i]]`]` `[`+1,`]` `[`for`]` `[`i`]` `[`=`]` `[`0,`]` `[`..,`]` `[`len(D_in)`]` `[`-`]` `[`1`]

                    > ::: 
                    > - If [`(D_out[i]`]` `[`-`]` `[`1)`]` `[`*`]` `[`strides[i]`]` `[`>=`]` `[`D_in[i]`]` `[`+`]` `[`pad[2*i]`]` `[`and`]` `[`(pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`>`]` `[`0)`] then [`D_out[i]`]` `[`=`]` `[`D_out[i]`]` `[`-`]` `[`1`].
                    > :::

                  - The first equation is same as:

                    > ::: 
                    > - [`D_out[i]`]` `[`=`]` `[`floor[(D_in[i]`]` `[`+`]` `[`pad[2*i]`]` `[`+`]` `[`pad[2*i+1]`]` `[`-`]` `[`kernel_sizes[i]`]` `[`+`]` `[`strides[i]`]` `[`-`]` `[`1)`]` `[`/`]` `[`strides[i]]`]` `[`+1,`]` `[`for`]` `[`i`]` `[`=`]` `[`0,`]` `[`..,`]` `[`len(D_in)`]` `[`-`]` `[`1`]
                    > :::

    ::: 
    See also

    [[`l2_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.l2_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.l2_pool"), [[`max_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.max_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.max_pool")

    :   
    :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.pool.]][[l2_pool]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/pool.html#l2_pool)[](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.l2_pool "Link to this definition")

:   Perform L2 pooling. Supports 1-D and 2-D pool.

    Parameters[:]

    :   

        **x: tensor\<\[n,C_in,\*D_in\], T\> (Required)**

        :   - Only support 1d and 2d pooling.

            - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **kernel_sizes: const tensor\<\[K\], T\> (Required)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **strides: const tensor\<\[S\],i32\> (Optional, default to all 1s)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **pad_type: const str (Required)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **pad: const\<\[P\],i32\> (Optional, default to all 0s)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C_out,\*D_out\], T\>

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

    ::: 
    See also

    [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool"), [[`max_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.max_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.max_pool")

    :   
    :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.pool.]][[max_pool]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/pool.html#max_pool)[](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.max_pool "Link to this definition")

:   Perform max pooling. Supports 1-D, 2-D, and 3-D pool.

    Parameters[:]

    :   

        **x: tensor\<\[n,C_in,\*D_in\], T\> (Required)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **kernel_sizes: const tensor\<\[K\], T\> (Required)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **strides: const tensor\<\[S\],i32\> (Optional, default to all 1s)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **pad_type: const str (Required)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **pad: const\<\[P\],i32\> (Optional, default to all 0s)**

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

        **ceil_mode: const\<bool\>**

        :   - see [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C_out,\*D_out\], T\>

        :   - See [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool").

    ::: 
    See also

    [[`avg_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.avg_pool"), [[`l2_pool`]](#coremltools.converters.mil.mil.ops.defs.iOS15.pool.l2_pool "coremltools.converters.mil.mil.ops.defs.iOS15.pool.l2_pool")

    :   
    :::

[]

## quantization[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.quantization_ops "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.quantization_ops.]][[quantize]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/quantization_ops.html#quantize)[](#coremltools.converters.mil.mil.ops.defs.iOS17.quantization_ops.quantize "Link to this definition")

:   Performs affine/linear quantization on an input tensor.

    The original data comes from the first "input". The other parameters -- [`scale`], [`zero_point`], and [`axis`] -- describe how quantization should occur:

    :::: 
    ::: highlight
        quantized_data = clip(round(input / scale) + zero_point)
    :::
    ::::

    Parameters[:]

    :   

        **input: tensor\<SrcT, \[1..\]\> (Required)**

        :   

        **zero_point: const tensor\<DstT, \[0..1\]\> (Optional)**

        :   - The [`zero_point`] can be either a scalar or a vector. If not provided, it is assumed to be [`0`].

            - The [`zero_point`] follows similar broadcasting rules and size constraints as [`scale`].

        **scale: const tensor\<SrcT, \[0..1\]\> (Required)**

        :   - The [`scale`] can be either a scalar or a vector.

            - 

              If [`scale`] is a vector, for implementation, it is broadcasted to the following shape:

              :   - The rank of [`scale`] becomes the same as the rank of the input.

                  - Constraint: [`size(scale-vector)`]` `[`==`]` `[`input.shape[axis]`].

                  - For [`i`]` `[`==`]` `[`axis`], [`scale.shape[i]`]` `[`==`]` `[`input.shape[i]`].

                  - For [`i`]` `[`!=`]` `[`axis`], [`scale.shape`]` `[`==`]` `[`1`].

                  - 

                    For example:

                    :   - Assume [`input.shape`]` `[`=`]` `[`(2,`]` `[`3,`]` `[`4,`]` `[`5)`] and [`axis`]` `[`=`]` `[`1`].

                        - If [`scale`] is a vector, then [`scale.size`] needs to be equal to [`input.shape[axis]`]; that is, equal to [`3`].

                        - This is broadcasted to [`(1,`]` `[`3,`]` `[`1,`]` `[`1)`].

        **output_dtype: const tensor\<string, \[\]\> (Required)**

        :   - This parameter can take [`"uint8"`], [`"int8"`] as values.

            - The [`output_dtype`] value must match the [`zero_point`] dtype.

        **axis: const tensor\<int32, \[\]\> (Optional)**

        :   

    Attributes[:]

    :   

        **SrcT: fp16, fp32**

        :   

        **DstT: uint8, int8**

        :   

    Returns[:]

    :   

        tensor\<DstT, \[1..\]\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.quantization_ops.]][[dequantize]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/quantization_ops.html#dequantize)[](#coremltools.converters.mil.mil.ops.defs.iOS17.quantization_ops.dequantize "Link to this definition")

:   Performs dequantization on an input tensor with affine/linear quantization.

    The quantized data comes from the first "input". The other parameters -- [`scale`], [`zero_point`], and [`axis`] -- describe how unquantized values can be extracted from it, using the following equation for affine/linear quantization:

    :::: 
    ::: highlight
        unquantized_data = scale * (input - zero_point)
    :::
    ::::

    Parameters[:]

    :   

        **input: tensor\<SrcT, \[1..\]\> (Required)**

        :   

        **zero_point: const tensor\<SrcT, \[0..1\]\> (Optional)**

        :   - The [`zero_point`] can be either a scalar or a vector. If not provided, it is assumed to be [`0`].

            - The [`zero_point`] follows similar broadcasting rules and size constraints as [`scale`].

        **scale: const tensor\<DstT, \[0..1\]\> (Required)**

        :   - The [`scale`] can be either a scalar or a vector.

            - 

              If [`scale`] is a vector, for implementation, it is broadcasted to the following shape:

              :   - The rank of [`scale`] becomes the same as the rank of the input.

                  - Constraint: [`size(scale-vector)`]` `[`==`]` `[`input.shape[axis]`].

                  - For [`i`]` `[`==`]` `[`axis`], [`scale.shape[i]`]` `[`==`]` `[`input.shape[i]`].

                  - For [`i`]` `[`!=`]` `[`axis`], [`scale.shape`]` `[`==`]` `[`1`].

                  - 

                    For example:

                    :   - Assume [`input.shape`]` `[`=`]` `[`(2,`]` `[`3,`]` `[`4,`]` `[`5)`] and [`axis`]` `[`=`]` `[`1`].

                        - If [`scale`] is a vector, then [`scale.size`] needs to be equal to [`input.shape[axis]`]; that is, equal to [`3`].

                        - This is broadcasted to [`(1,`]` `[`3,`]` `[`1,`]` `[`1)`].

        **axis: const tensor\<int32, \[\]\> (Optional)**

        :   

    Attributes[:]

    :   

        **SrcT: uint8, int8**

        :   

        **DstT: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<DstT, \[1..\]\>

        :   

[]

## random[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.random "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.random.]][[random_bernoulli]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/random.html#random_bernoulli)[](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_bernoulli "Link to this definition")

:   Returns a tensor with the specified shape, with random values from a Bernoulli distribution.

    ::: 
    \\\[\\beginf(k) = \\begin1-p &\\text k = 0\\\\ p &\\text k = 1\\end\\end\\\]
    :::

    for [\\(k\\)] in [\\(\\\\)].

    Parameters[:]

    :   

        **shape: \<K, i32\> (Required)**

        :   - Target output tensor shape.

            - [`K`] is the rank of the output tensor. [`shape[k]`]` `[`>`]` `[`0`] for [`k`]` `[`=`]` `[`0,...,`]` `[`K-1`].

        **prob: const\<T\> (Optional)**

        :   - The probability of sampling [`1`]. Defaults to [`0.5`].

        **seed: const\<i32\> (Optional)**

        :   - Seed to create a reproducible sequence of values across multiple invokes.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        \<\\\*, T\>

        :   - A tensor of the given target output shape filled with random values.

    ::: 
    See also

    [[`random_categorical`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_categorical "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_categorical"), [[`random_normal`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_normal "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_normal"), [[`random_uniform`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_uniform "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_uniform")

    :   
    :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.random.]][[random_categorical]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/random.html#random_categorical)[](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_categorical "Link to this definition")

:   Returns random values from a categorical distribution.

    Parameters[:]

    :   

        **x: \<\*D_in, T\>**

        :   - N-dimensional tensor which represents [`logits`] (event log-probabilities) or [`probs`] (event probabilities) depending on [`mode`]. The first [`N`]` `[`-`]` `[`1`] dimensions specifies distributions, and the last dimension represents a vector of probabilities.

        **mode: const\<str\> (Optional)**

        :   One of [`['logits',`]` `[`'probs']`]. Defaults to [`logits`]. When set to [`probs`], an element-wise log layer will be added to calculate logits.

        **size: const\<i32\> (Optional)**

        :   Number of samples to draw. Defaults to [`1`]. When set as [`1`], it's categorical distribution. When set larger than [`1`], it's actually multinomial distribution by drawing with replacement. It means that when a sample index is drawn, it can be drawn again. The categorical distribution is a special case of the multinomial distribution, giving the probabilities of potential outcomes of a single drawing rather than multiple drawings.

        **seed: const\<i32\> (Optional)**

        :   Seed to create a reproducible sequence of values across multiple invokes.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*D_in\[:-1\] + \[size\], T\>

        :   - A tensor of the given target output shape filled with random values.

    ::: 
    See also

    [[`random_bernoulli`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_bernoulli "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_bernoulli"), [[`random_normal`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_normal "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_normal"), [[`random_uniform`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_uniform "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_uniform")

    :   
    :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.random.]][[random_normal]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/random.html#random_normal)[](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_normal "Link to this definition")

:   Returns a tensor with the specified shape, with random values from a normal distribution.

    Parameters[:]

    :   

        **shape: \<K, i32\> (Required)**

        :   - Target output tensor shape.

            - [`K`] is the rank of the output tensor. [`shape[k]`]` `[`>`]` `[`0`] for [`k`]` `[`=`]` `[`0,...,`]` `[`K-1`].

        **mean: const\<T\> (Optional)**

        :   The mean (center) of the normal distribution. Defaults to 0.0.

        **stddev: const\<T\> (Optional)**

        :   The standard deviation (width) of the normal distribution. Defaults to [`1.0`].

        **seed: const\<i32\> (Optional)**

        :   Seed to create a reproducible sequence of values across multiple invokes.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        \<\\\*, T\>

        :   - A tensor of the given target output shape filled with random values.

    ::: 
    See also

    [[`random_categorical`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_categorical "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_categorical"), [[`random_bernoulli`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_bernoulli "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_bernoulli"), [[`random_uniform`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_uniform "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_uniform")

    :   
    :::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.random.]][[random_uniform]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/random.html#random_uniform)[](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_uniform "Link to this definition")

:   Returns a tensor with the specified shape with random values from a uniform distribution. Samples are uniformly distributed over the half-open interval [`[low,`]` `[`high)`] (includes low, but excludes high).

    ::: 
    \\\[p(x) = \\frac\\\]
    :::

    For a real number [\\(x\\)].

    When [`high`]` `[`==`]` `[`low`], values of [`low`] will be returned. If [`high`]` `[`<`]` `[`low`], the results are officially undefined and may eventually raise an error.

    Parameters[:]

    :   

        **shape: \<K, i32\> (Required)**

        :   - Target output tensor shape.

            - [`K`] is the rank of the output tensor. [`shape[k]`]` `[`>`]` `[`0`] for [`k`]` `[`=`]` `[`0,...,`]` `[`K-1`].

        **low: const\<T\> (Optional)**

        :   - Lower boundary of the output interval (inclusive). Defaults to [`0.0`].

        **high: const\<T\> (Optional)**

        :   - Upper boundary of the output interval (exclusive). Defaults to [`1.0`].

        **seed: const\<i32\> (Optional)**

        :   - Seed to create a reproducible sequence of values across multiple invokes.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        \<\\\*, T\>

        :   - A tensor of the given target output shape filled with random values.

    ::: 
    See also

    [[`random_categorical`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_categorical "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_categorical"), [[`random_bernoulli`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_bernoulli "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_bernoulli"), [[`random_normal`]](#coremltools.converters.mil.mil.ops.defs.iOS15.random.random_normal "coremltools.converters.mil.mil.ops.defs.iOS15.random.random_normal")

    :   
    :::

[]

## recurrent (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.recurrent "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.]][[gru]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/recurrent.html#gru)[](#coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.gru "Link to this definition")

:   Gated Recurrent Unit (GRU)

    ::: 
    \\\[r_t = \\rm(W\_ x_t + b\_ + W\_ h\_ + b\_)\\\]
    :::

    ::: 
    \\\[z_t = \\rm(W\_ x_t + b\_ + W\_ h\_ + b\_)\\\]
    :::

    ::: 
    \\\[o_t = \\rm(W\_ x_t + b\_ + r_t \* W\_ h\_ + b\_)\\\]
    :::

    ::: 
    \\\[h_t = (1 − z_t) \* o_t + z_t \* h\_\\\]
    :::

    Where:

    - [\\(W\_\\)] are state input weights for reset, output and update gate, respectively.

    - [\\(b\_\\)] are input biases for reset, output and update gate, respectively.

    - [\\(W\_\\)] are recurrent/hidden weights on hidden state to reset, output, and update gates, respectively.

    - [\\(b\_\\)] are recurrent/hidden biases on hidden state to reset, output, and update gates, respectively.

    - [\\(h_t\\)] is the hidden state at time [`t`].

    - [\\(x_t\\)] is the input at time [`t`].

    - [\\(h\_\\)] is the hidden state of the layer at time [`t-1`] or the initial hidden state at time [`0`].

    - [\\(r_t\\)], [\\(o_t\\)], and [\\(z_t\\)] are the reset, new, and update gates, respectively.

    - [\\(\*\\)] is elementwise product.

    Parameters[:]

    :   

        **x: \<s, b, I, T\> (Required)**

        :   - [`s`] is the sequence length, [`b`] is the batch size, and [`I`] is the input dimension.

        **initial_h: \<b, H, T\> (Required)**

        :   - [`H`] denotes hidden size.

        **weight_ih: const\<3\*H, I, T\> (Required) - Weight matrix**

        :   - [`weigh_ih`]` `[`=`]` `[`[W_`]` `[`|`]` `[`W_`]` `[`|`]` `[`W_]`] where [`[a|b]`] denotes column concatenation and [`[a,`]` `[`b]`] denotes row concatenation. [`W_`], [`W_`], and [`W_`] have shape [`(H,`]` `[`I)`].

        **weight_hh: const\<3\*H, H, T\> (Required) - Weight matrix**

        :   - [`weight_hh`]` `[`=`]`  `[`[W_`]` `[`|`]` `[`W_`]` `[`|`]` `[`W_]`]: [`W_`], [`W_`], and [`W_`] have shape [`(H,`]` `[`H)`].

        **bias: const\<3\*H, T\> (Optional) \[Default all 0s\]**

        :   - [`bias[0]`] are input-hidden and hidden-hidden bias.

            - [`3*H`] are biases for [`[b_`]` `[`|`]` `[`b_`]` `[`|`]` `[`b_]`].

        **direction: const\<str\> (Optional) \[Default=forward\]**

        :   - Either [`forward`] or [`reverse`].

        **output_sequence: const\<bool\> (Optional) \[Default=False\]**

        :   - Outputs every step if [`True`].

        **recurrent_activation: const\<str\> (Optional) \[Default=sigmoid\]**

        :   - Activation applied on update and reset gate.

        **activation: const\<str\> (Optional) \[Default=tanh\]**

        :   - Activation applied on output gate.

    Attributes[:]

    :   

        **T: fp32**

        :   

    Returns[:]

    :   

        \<s, b, H, T\> or \<1, b, H, T\>

        :   - If [`output_sequence`]` `[`==`]` `[`True`] (hidden states from every step): [`<s,`]` `[`b,`]` `[`H,`]` `[`T>`].

            - Else [`<1,`]` `[`b,`]` `[`H,`]` `[`T>`] (hidden states of the final step).

        \<b, H, T\>

        :   - Hidden states of the final step.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.]][[lstm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/recurrent.html#lstm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.lstm "Link to this definition")

:   Long Short-Term Memory (LSTM)

    ::: 
    \\\[i_t = \\rm(W\_ x_t + B\_ + W\_ h\_ + B\_)\\\]
    :::

    ::: 
    \\\[f_t = \\rm(W\_ x_t + B\_ + W\_ h\_ + B\_)\\\]
    :::

    ::: 
    \\\[z_t = \\rm(W\_ x_t + B\_ + W\_ h\_ + B\_)\\\]
    :::

    ::: 
    \\\[o_t = \\rm(W\_ x_t + B\_ + W\_ h\_ + B\_)\\\]
    :::

    ::: 
    \\\[c_t = f_t \* c\_ + i_t \* z_t\\\]
    :::

    ::: 
    \\\[h_t = o_t \* \\rm\\\]
    :::

    Where:

    - [\\(i_t\\)], [\\(f_t\\)], [\\(o_t\\)], and [\\(z_t\\)] are input, forget, output, and cell gates, respectively, at time [`t`].

    - [\\(c_t\\)] is cell state at time [`t`].

    - [\\(h_t\\)] is the hidden state at time [`t`].

    - [\\(W\_\\)], [\\(W\_\\)], [\\(W\_\\)], and [\\(W\_\\)] are input weights for input, forget, output, and cell gate, respectively.

    - [\\(B\_\\)], [\\(B\_\\)], [\\(B\_\\)], and [\\(B\_\\)] are input biases for input, forget, output, and cell gate, respectively.

    - [\\(W\_\\)], [\\(W\_\\)], [\\(W\_\\)], and [\\(W\_\\)] are recurrent weights for input, forget, output, and cell gate, respectively.

    - [\\(B\_\\)], [\\(B\_\\)], [\\(B\_\\)], and [\\(B\_\\)] are recurrent weights for input, forget, output, and cell gate, respectively.

    Parameters[:]

    :   

        **x: \<s, b, I, T\> (Required)**

        :   - [`s`] is the sequence length, [`b`] is the batch size, and [`I`] is the input dimension.

        **initial_h: \<b, DIRECTIONS\*H, T\> (Required)**

        :   - Initial hidden state. [`DIRECTIONS`]` `[`=`]` `[`1`] for uni-directional. [`DIRECTIONS`]` `[`=`]` `[`2`] for bi-directional LSTM.

            - [`H`] denotes hidden size.

            - [`[b,`]` `[`:H]`] and [`[b,`]` `[`H:]`] represents forward and reverse direction values, respectively.

        **initial_c: \<b, DIRECTIONS\*H, T\> (Required)**

        :   - Initial cell state.

            - Format is same as [`initial_h`].

        **weight_ih: const\<4\*H, I, T\> (Required)**

        :   - Input-hidden weight matrix

            - Weight tensor should be in order of [`[input_gate,`]` `[`forget_gate,`]` `[`output_gate,`]` `[`cell_gate]`].

            - If direction=="bidirectional", this is applied in forward direction.

            - If direction=="forward" or "backward" these weights are used.

        **weight_hh: const\<4\*H, H, T\> (Required)**

        :   - Hidden-hidden weight matrix.

            - Weight tensor should be in order of [`[input_gate,`]` `[`forget_gate,`]` `[`output_gate,`]` `[`cell_gate]`].

            - If direction=="bidirectional", this is applied in forward direction.

            - If direction=="forward" or "backward" these weights are used.

        **bias: const\<4\*H, T\> (Optional, default all 0s)**

        :   - bias = input-hidden bias + hidden-hidden bias

            - If direction=="bidirectional", this is applied in forward direction.

            - If direction=="forward" or "backward" this bias are used.

        **peephole: const\<3\*H, T\> (Optional, default all 0s)**

        :   - Weight tensor for peephole.

            - Order is [`[input_gate,`]` `[`forget_gate,`]` `[`output_gate]`].

            - Shape of each peephole vector is [`(H,)`] ([`H`] is hidden size).

            - If direction=="bidirectional", this is applied in forward direction.

            - If direction=="forward" or "backward" these weights are used.

        **weight_ih_back: const\<4\*H, I, T\> (Optional) -**

        :   - Input-hidden weight matrix for backward direction for bidirectinal LSTM.

            - Weight tensor should be in order of [`[input_gate,`]` `[`forget_gate,`]` `[`output_gate,`]` `[`cell_gate]`].

            - Must be provided for bidirectional LSTM.

            - This is only used when direction is "bidirectional".

            - For direction="reverse" use weight_ih instead.

        **weight_hh_back: const\<4\*H, H, T\> (Optional) - Hidden-hidden weight matrix**

        :   - Hidden-hidden weight matrix for backward direction for bidirectinal LSTM.

            - Weight tensor should be in order of [`[input_gate,`]` `[`forget_gate,`]` `[`output_gate,`]` `[`cell_gate]`].

            - Must be provided for bidirectional LSTM.

            - This is only used when direction is "bidirectional".

            - For direction="reverse" use weight_hh instead.

        **bias_back: const\<4\*H, T\> (Optional, default all 0s)**

        :   - bias = input-hidden bias + hidden-hidden bias.

            - Bias of backward direction for bidirectional lstm

            - This is only used when direction is "bidirectional".

            - For direction="reverse" use bias instead.

        **peephole_back: const\<3\*H, T\> (Optional, default all 0s)**

        :   - Weight tensor for peephole in backward direction for bidirectional LSTM.

            - Order is [`[input_gate,`]` `[`forget_gate,`]` `[`output_gate]`].

            - Shape of each peephole vector is [`(H,)`] ([`H`] is hidden size).

            - Peephole of backward direction for bidirectional lstm

            - Bias of backward direction for bidirectional lstm

            - This is only used when direction is "bidirectional".

            - For direction="reverse" use peephole instead.

        **direction: const\<str\> (Optional) \[Default=forward\]**

        :   - One of the following: [`forward`], [`reverse`], or [`bidirectional`].

            - Must match [`DIRECTIONAL`] in initial states and weight parameters.

        **output_sequence: const\<bool\> (Optional) \[Default=False\]**

        :   - Outputs every step if [`True`].

        **recurrent_activation: const\<str\> (Optional) \[Default=sigmoid\]**

        :   - Activation applied on input, forget, and output gates.

            - Supported values: [`hard_sigmoid`], [`linear`], [`relu`], [`scaled_tanh`], [`sigmoid`], [`tanh`]

        **cell_activation: const\<str\> (Optional) \[Default=tanh\]**

        :   - Activation applied on cell gate.

            - Supported values: [`hard_sigmoid`], [`linear`], [`relu`], [`scaled_tanh`], [`sigmoid`], [`tanh`]

        **activation: const\<str\> (Optional) \[Default=tanh\]**

        :   - Activation applied on output gate.

            - Supported values: [`hard_sigmoid`], [`linear`], [`relu`], [`scaled_tanh`], [`sigmoid`], [`tanh`]

        **clip: const\<T\> (optional) \[Default=None\]**

        :   - Cell gate is clipped to [`[-clip,`]` `[`+clip]`].

    Attributes[:]

    :   

        **T: fp32**

        :   

    Returns[:]

    :   

        \<s, b, DIRECTIONS\*H, T\> or \<1, b, DIRECTIONS\*H, T\>

        :   - If [`output_sequence`]` `[`==`]` `[`True`] (hidden states from every step): [`<s,`]` `[`b,`]` `[`DIRECTIONS*H,`]` `[`T>`].

            - Else [`<1,`]` `[`b,`]` `[`DIRECTIONS*H,`]` `[`T>`] (hidden states of the final step).

        \<b, DIRECTIONS\*H, T\>

        :   - Hidden states of the final step.

        \<b, DIRECTIONS\*H, T\>

        :   - Memory state of the final step.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.]][[rnn]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/recurrent.html#rnn)[](#coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.rnn "Link to this definition")

:   Recurrent Neural Network (RNN)

    ::: 
    \\\[h_t = \\rm(W\_ x_t + b\_ + W\_ h\_ + b\_)\\\]
    :::

    Where:

    - [\\(W\_\\)] is the input weight.

    - [\\(W\_\\)] is the hidden/recurrent weight.

    - [\\(h_t\\)] is the hidden state at time [`t`].

    - [\\(x_t\\)] is the input at time [`t`].

    - [\\(h\_\\)] is the hidden state of the layer at time [`t-1`] or the initial hidden state at [`t`]` `[`=`]` `[`0`].

    - [\\(b\_\\)] is the input bias.

    - [\\(b\_\\)] if the hidden/recurrent bias.

    Parameters[:]

    :   

        **x: \<s, b, I, T\> (Required)**

        :   - [`s`] is the sequence length, [`b`] is the batch size, and [`I`] is the input dimension.

        **initial_h: \<b, H, T\> (Required)**

        :   - [`H`] denotes hidden size.

        **weight_ih: const\<H, I, T\> (Required) - Input-hidden weight matrix**

        :   

        **weight_hh: const\<H, H, T\> (Required) - Hidden-hidden weight matrix**

        :   

        **bias: const\<H, T\> (Optional) \[Default all 0s\]**

        :   - bias for input-hidden and hidden-hidden

        **direction: const\<str\> (Optional) \[Default=forward\]**

        :   - Either [`forward`] or [`reverse`].

        **output_sequence: const\<bool\> (Optional) \[Default=False\]**

        :   - Outputs every step if [`True`].

        **activation: const\<str\> (Optional) \[Default=tanh\]**

        :   - Supported activation functions: [`relu`], [`tanh`], [`sigmoid`], [`sigmoid_hard`], [`scaled_tanh`], and [`linear`].

    Attributes[:]

    :   

        **T: fp32**

        :   

    Returns[:]

    :   

        \<s, b, H, T\> or \<1, b, H, T\>

        :   - If [`output_sequence`]` `[`==`]` `[`True`] (hidden states from every step): [`<s,`]` `[`b,`]` `[`H,`]` `[`T>`].

            - Else [`<1,`]` `[`b,`]` `[`H,`]` `[`T>`] (hidden states of the final step).

        \<b, H, T\>

        :   - Hidden states of the final step.

[]

## recurrent (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.recurrent "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.]][[gru]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/recurrent.html#gru)[](#coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.gru "Link to this definition")

:   Gated Recurrent Unit (GRU)

    The only difference between this version and the iOS 15 [[`gru`]](#coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.gru "coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.gru") is adding the support for fp16.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.]][[lstm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/recurrent.html#lstm)[](#coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.lstm "Link to this definition")

:   Long Short-Term Memory (LSTM)

    The only difference between this version and the iOS 15 [[`lstm`]](#coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.lstm "coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.lstm") is adding the support for fp16.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.]][[rnn]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/recurrent.html#rnn)[](#coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.rnn "Link to this definition")

:   Recurrent Neural Network (RNN)

    The only difference between this version and the iOS 15 [[`rnn`]](#coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.rnn "coremltools.converters.mil.mil.ops.defs.iOS15.recurrent.rnn") is adding the support for fp16.

[]

## recurrent (iOS 18+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS18.recurrent "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.recurrent.]][[gru]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/recurrent.html#gru)[](#coremltools.converters.mil.mil.ops.defs.iOS18.recurrent.gru "Link to this definition")

:   Gated Recurrent Unit (GRU)

    Two new parameters have been added to the iOS 17 [[`gru`]](#coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.gru "coremltools.converters.mil.mil.ops.defs.iOS17.recurrent.gru").

    reset_after - this parameter is optional and defaults to False. When True, the reset gate is applied before the elementwise matrix multiplication.

    input_bias - const\<3\*H, T\> (Optional) \[Default all 0s\].

[]

## reduction (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.reduction "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_argmax]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_argmax)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_argmax "Link to this definition")

:   Computes the indices of the maximum value across dimensions of a tensor. In case of ties, the identity of the return value is not guaranteed.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axis: const\<i32\> (Optional)**

        :   - The dimension to reduce. Default is [`-1`].

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] by removing the dimension specified in [`axis`]. If [`True`], retain reduced axis with length [`1`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        \<\*, int32\>

        :   

    References

    See [tf.math.argmax](https://www.tensorflow.org/api_docs/python/tf/math/argmax).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_argmin]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_argmin)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_argmin "Link to this definition")

:   Computes the indices of the minimum value across dimensions of a tensor. In case of ties, the identity of the return value is not guaranteed.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axis: const\<i32\> (Optional)**

        :   - The dimension to reduce. Default is [`-1`].

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] by removing the dimension specified in [`axis`], otherwise retain reduced axis with length [`1`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        \<\*, int32\>

        :   

    References

    See [tf.math.argmin](https://www.tensorflow.org/api_docs/python/tf/math/argmin).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_l1_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_l1_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_l1_norm "Link to this definition")

:   Computes the L1 normalization of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K, i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

    References

    See [reduce_mean](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean?version=stable).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_l2_norm]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_l2_norm)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_l2_norm "Link to this definition")

:   Computes the L2 normalization of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K, i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_log_sum]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_log_sum)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_log_sum "Link to this definition")

:   Computes the natural logarithm of the sum of all the elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K, i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_log_sum_exp]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_log_sum_exp)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_log_sum_exp "Link to this definition")

:   Computes the natural logarithm of the sum of the exponentials of the elements across given dimensions of the input tensor. It is a smooth approximation of the maximum function, more numerically stable than [`log(sum(exp(input)))`]. It avoids overflows caused by taking the [`exp`] of large inputs and underflows caused by taking the [`log`] of small inputs.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K,i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

    References

    See [tf.math.reduce_logsumexp](https://www.tensorflow.org/api_docs/python/tf/math/reduce_logsumexp).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_max]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_max)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_max "Link to this definition")

:   Computes the maximum of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K,i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_mean]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_mean)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_mean "Link to this definition")

:   Computes the mean of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K,i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

    References

    For an example, see [tf.math.reduce_mean](https://www.tensorflow.org/api_docs/python/tf/math/reduce_mean?version=stable).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_min]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_min)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_min "Link to this definition")

:   Computes the minimum of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*,T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K,i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*,T\>

        :   - Scalar or tensor: The reduced tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_prod]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_prod)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_prod "Link to this definition")

:   Computes the product of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K,i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_sum]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_sum)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_sum "Link to this definition")

:   Computes the sum of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K,i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.reduction.]][[reduce_sum_square]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html#reduce_sum_square)[](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_sum_square "Link to this definition")

:   Computes the sum of squares of elements across given dimensions of the input tensor.

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axes: const\<K,i32\> (Optional, default="None", reduce on all axes.)**

        :   - The dimensions to reduce.

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] for each entry in [`axes`], otherwise retain reduced axes with length [`1`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        \<\*, T\>

        :   - Scalar or tensor: The reduced tensor.

[]

## reduction (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.reduction "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.reduction.]][[reduce_argmax]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/reduction.html#reduce_argmax)[](#coremltools.converters.mil.mil.ops.defs.iOS17.reduction.reduce_argmax "Link to this definition")

:   Computes the indices of the maximum value across dimensions of a tensor. In case of ties, the identity of the return value is not guaranteed.

    The differences between this version and the iOS 15 [[`reduce_argmax`]](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_argmax "coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_argmax") are:

    :   - The output supports uint16 dtype.

        - New optional input [`output_dtype`].

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axis: const\<i32\> (Optional)**

        :   - The dimension to reduce. Default is [`-1`].

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] by removing the dimension specified in [`axis`].

            - If [`True`], retain reduced axis with length [`1`].

        **output_dtype: const\<str\> (Optional)**

        :   - Possible values: [`uint16`], [`int32`].

            - If set, then value type inference will output using that dtype.

            - Default is [`int32`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

        **U: int32, uint16**

        :   

    Returns[:]

    :   

        \<\*, U\>

        :   

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.reduction.]][[reduce_argmin]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/reduction.html#reduce_argmin)[](#coremltools.converters.mil.mil.ops.defs.iOS17.reduction.reduce_argmin "Link to this definition")

:   Computes the indices of the minimum value across dimensions of a tensor. In case of ties, the identity of the return value is not guaranteed.

    The differences between this version and the iOS 15 [[`reduce_argmin`]](#coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_argmin "coremltools.converters.mil.mil.ops.defs.iOS15.reduction.reduce_argmin") are:

    :   - The output supports uint16 dtype.

        - New optional input [`output_dtype`].

    Parameters[:]

    :   

        **x: \<\*, T\> (Required)**

        :   - Must be 1-dimensional or higher.

        **axis: const\<i32\> (Optional)**

        :   - The dimension to reduce. Default is [`-1`].

        **keep_dims: const\<bool\> (Optional, default=False)**

        :   - If [`False`], the rank is reduced by [`1`] by removing the dimension specified in [`axis`], otherwise retain reduced axis with length [`1`].

        **output_dtype: const\<str\> (Optional)**

        :   - Possible values: [`uint16`], [`int32`].

            - If set, then value type inference will output using that dtype.

            - Default is [`int32`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

        **U: int32, uint16**

        :   

    Returns[:]

    :   

        \<\*, U\>

        :   

[]

## scatter_gather (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.]][[gather]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/scatter_gather.html#gather)[](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.gather "Link to this definition")

:   Gather slices from input [`x`] along dimension [`axis`] according to [`indices`], similar to [tf.gather](https://www.tensorflow.org/api_docs/python/tf/gather).

    - If [`indices`] is scalar (0-D):

    ::: 
    \\\[output\[p_0, \..., p\_, \~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~\~ p\_, \..., p\_\] =\\\]
    :::

    ::: 
    \\\[x\[p_0, \..., p\_, \~\~\~\~\~\~\~\~\~ indices, \~\~\~\~\~\~\~\~ p\_, \..., p\_\]\\\]
    :::

    Where [`rank(x)`] is the rank of [`x`]. The [`output`] has rank [`rank(x)`]` `[`-`]` `[`1`].

    - If [`indices`] is 1-D tensor:

    ::: 
    \\\[output\[p_0, \..., p\_, \~\~\~\~\~\~\~\~\~\~\~\~\~ i, \~\~\~\~\~\~\~\~\~\~\~\~\~ p\_, \..., p\_\] =\\\]
    :::

    ::: 
    \\\[x\[p_0, \..., p\_, \~\~\~\~\~\~\~\~ indices\[i\], \~\~\~\~\~\~\~\~ p\_, \..., p\_\]\\\]
    :::

    The output has rank [`rank(x)`].

    - In general:

    ::: 
    \\\[output\[p_0, \..., p\_, \~\~\~\~\~\~\~\~ i_0, \..., i\_, \~\~\~\~\~\~\~\~ p\_, \..., p\_\] =\\\]
    :::

    ::: 
    \\\[x\[p_0, \..., p\_, \~\~\~\~\~\~\~ indices\[i_0, \..., i\_\], \~\~\~\~\~\~\~ p\_, \..., p\_\]\\\]
    :::

    Where [`M`]` `[`=`]` `[`rank(indices)`].

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*N, i32\> (Required)**

        :   - Indices values may be negative. More precisely, [`-D[axis]<=`]` `[`v`]` `[`<`]` `[`D[axis]`] for [`v`] in [`indices`].

        **axis: const i32 (Optional. Default=\`\`0\`\`)**

        :   - Negative axis is supported.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*K, T\>

        :   - Where [`K`]` `[`=`]` `[`D[:axis]`]` `[`+`]` `[`N`]` `[`+`]` `[`D[axis+1:]`].

    References

    See [tf.gather](https://www.tensorflow.org/api_docs/python/tf/gather).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.]][[gather_along_axis]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/scatter_gather.html#gather_along_axis)[](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.gather_along_axis "Link to this definition")

:   Take the values along [`axis`] at locations [`indices`].

    ::: 
    \\\[idx = indices\[p_0, \..., p\_, i, p\_, \..., p_D\]\\\]
    :::

    ::: 
    \\\[output\[p_0, \..., p\_, i, p\_, \..., p_D\] = = x\[p_0, \..., p\_, idx, p\_, \..., p_D\]\\\]
    :::

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, i32\> (Required)**

        :   - [`rank(indices)`]` `[`==`]` `[`rank(x)`].

        **axis: const i32 (Optional):**

        :   - Default to [`0`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*D, T\>:

        :   - Output tensor has the same shape as [`indices`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.]][[gather_nd]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/scatter_gather.html#gather_nd)[](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.gather_nd "Link to this definition")

:   Gather slices from [`x`] according to [`indices`], similar to [tf.gather_nd](https://www.tensorflow.org/api_docs/python/tf/gather_nd).

    The [`indices`] is a K-dim tensor, where [`indices[i_0,...,i_]`] defines a slice of [`x`]:

    ::: 
    \\\[output\[i_0, \..., i\_\]= x\[indices\[i_0, \..., i\_\]\]\\\]
    :::

    Where [`K`]` `[`=`]` `[`rank(indices)`] and [`x[indices[i_0,`]` `[`...,`]` `[`i_]]`] has rank [`rank(x)`]` `[`-`]` `[`indices.shape[-1]`].

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, i32\> (Required)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*V, T\>

        :   - [`V`]` `[`=`]` `[`K[:-1]`]` `[`+`]` `[`D[K[-1]:]`], where [`D`]` `[`=`]` `[`x.shape`] and [`K`]` `[`=`]` `[`indices.shape`].

    References

    See [tf.gather_nd](https://www.tensorflow.org/api_docs/python/tf/gather_nd).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.]][[scatter]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/scatter_gather.html#scatter)[](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter "Link to this definition")

:   Scatter [`updates`] to [`data`] at locations [`indices`] at dimension [`axis`] by operation [`mode`].

    Example: [`mode`]` `[`==`]` `[`update`].

    - For [`i`] in [`[0,`]` `[`len(indices)]`]:

    ::: 
    \\\[output\[p_0, \..., p\_, indice\[i\], p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[updates\[p_0, \..., p\_, i, p\_, \..., p_D\]\\\]
    :::

    - For [`j`]` `[`!=`]` `[`i`]:

    ::: 
    \\\[output\[p_0, \..., p\_, j, p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[data\[p_0, \..., p\_, j, p\_, \..., p_D\]\\\]
    :::

    Example: [`mode`]` `[`==`]` `[`add`].

    - For [`i`] in [`[0,`]` `[`len(indices)]`]:

    ::: 
    \\\[output\[p_0, \..., p\_, indice\[i\], p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[updates\[p_0, \..., p\_, i, p\_, \..., p_D\] +\\\]
    :::

    ::: 
    \\\[x\[p_0, \..., p\_, indice\[i\], p\_, \..., p_D\]\\\]
    :::

    - For [`j`]` `[`!=`]` `[`i`]:

    ::: 
    \\\[output\[p_0, \..., p\_, j, p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[data\[p_0, \..., p\_, j, p\_, \..., p_D\]\\\]
    :::

    Parameters[:]

    :   

        **data: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\[C\], i32\> (Required)**

        :   - 1-D tensor.

        **updates: tensor\<\*K, T\> (Required)**

        :   - [`K`]` `[`=`]` `[`data.shape[:axis]`]` `[`+`]` `[`[len(indices)]`]` `[`+`]` `[`data.shape[axis+1:]`].

        **axis: const i32 (Optional)**

        :   - Default to [`0`].

        **mode: const string (Optional)**

        :   - Can be the following modes: [`update`], [`add`], [`sub`], [`mul`], [`div`], [`max`], [`min`].

            - Default value is [`update`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

        **For example:**

        :   data = \[\[1, 2, 3\], \[4, 5, 6\]\] indices = \[1, 0\] updates = \[\[5, 6, 7\], \[8, 9, 10\]\] axis = 0 mode = "add"

        **produces:**

        :   \[\[9, 11, 13\], \[9, 11, 13\]\]

    Returns[:]

    :   

        tensor\<\*D, T\>

        :   - With the same type and shape as input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.]][[scatter_along_axis]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/scatter_gather.html#scatter_along_axis)[](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter_along_axis "Link to this definition")

:   Scatter [`updates`] to [`data`] at locations [`indices`] along [`axis`] dimension using [`mode`] operation.

    Example: [`mode`]` `[`==`]` `[`update`].

    - For [`i`] in [`[0,`]` `[`len(indices)]`]:

    ::: 
    \\\[idx = indices\[p_0, \..., p\_, i, p\_, \..., p_D\]\\\]
    :::

    ::: 
    \\\[output\[p_0, \..., p\_, idx, p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[updates\[p_0, \..., p\_, i, p\_, \..., p_D\]\\\]
    :::

    - For [`j!`]` `[`=`]` `[`i`]:

    ::: 
    \\\[output\[p_0, \..., p\_, j, p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[data\[p_0, \..., p\_, j, p\_, \..., p_D\]\\\]
    :::

    Example: [`mode`]` `[`==`]` `[`add`].

    - For [`i`] in [`[0,`]` `[`len(indices)]`]:

    ::: 
    \\\[idx = indices\[p_0, \..., p\_, i, p\_, \..., p_D\]\\\]
    :::

    ::: 
    \\\[output\[p_0, \..., p\_, idx, p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[updates\[p_0, \..., p\_, i, p\_, \..., p_D\] +\\\]
    :::

    ::: 
    \\\[x\[p_0, \..., p\_, indice\[i\], p\_, \..., p_D\]\\\]
    :::

    - For [`j!`]` `[`=`]` `[`i`]:

    ::: 
    \\\[output\[p_0, \..., p\_, j, p\_, \..., p_D\] =\\\]
    :::

    ::: 
    \\\[data\[p_0, \..., p\_, j, p\_, \..., p_D\]\\\]
    :::

    Parameters[:]

    :   

        **data: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, i32\> (Required)**

        :   - [`rank(indices)`]` `[`==`]` `[`rank(data)`].

        **updates: tensor\<\*K, T\> (Required)**

        :   - Must be the same shape as [`indices`].

        **axis: const i32 (Optional)**

        :   - Default to [`0`].

        **mode: const string (Optional)**

        :   - Default to [`add`].

            - Can be the following modes: [`update`], [`add`], [`sub`], [`mul`], [`div`], [`max`], [`min`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*D, T\>

        :   - With the same type and shape as input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.]][[scatter_nd]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/scatter_gather.html#scatter_nd)[](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter_nd "Link to this definition")

:   Scatter [`updates`] to [`data`] at locations [`indices`].

    The [`indices`] is a K-dim tensor, where [`indices[i_0,...,i_]`] defines a slice of [`data`], [`K`]` `[`=`]` `[`rank(indices)`], and [`data[i_0,`]` `[`...,`]` `[`i_]`] has rank [`rank(data)`]` `[`-`]` `[`indices.shape[-1]`]. Concretely, this means the index is stored in the last dim of [`indices`], e.g. take a [`K`]` `[`==`]` `[`2`] example

    ::: 
    \\\[indices = \[\[0, 1\], \[0, 2\]\]\\\]
    :::

    where [`indices[0]`] / [`[0,`]` `[`1]`] and [`indices[1]`] / [`[0,`]` `[`2]`] are two indices that get applied to [`data`]

    - Example: [`mode`]` `[`==`]` `[`update`]: The [`output`] is set to [`data`] initially, and the op updates [`output`] as follows:

    ::: 
    \\\[output\[indices\[i_0, \..., i\_\]\]= updates\[i_0, \..., i\_\]\\\]
    :::

    - Example: [`mode`]` `[`==`]` `[`add`]. The update rule is:

    ::: 
    \\\[output\[indices\[i_0, \..., i\_\]\] += updates\[i_0, \..., i\_\]\\\]
    :::

    Parameters[:]

    :   

        **data: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*E, i32\> (Required)**

        :   - indices.shape\[-1\] \<= data.rank

        **updates: tensor\<\*F, T\> (Required)**

        :   - Must be the shape as [`indices.shape[:-1]`]` `[`+`]` `[`data.shape[indices.shape[-1]:]`].

        **mode: const string (Optional)**

        :   - Default to [`add`].

            - Can be the following modes: [`update`], [`add`], [`sub`], [`mul`], [`div`], [`max`], [`min`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*D, T\>

        :   - A tensor with the same shape and type as [`data`].

[]

## scatter_gather (iOS 16+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.]][[gather]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/scatter_gather.html#gather)[](#coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.gather "Link to this definition")

:   The iOS16 version. This section documents only the differences between this version and the iOS 15 [[`gather`]](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.gather "coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.gather").

    This version supports [`batch_dims`], similar to [tf.gather](https://www.tensorflow.org/api_docs/python/tf/gather). Input parameter [`indices`] now supports [`int16`] and [`uint16`].

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*N, I\> (Required)**

        :   - Indices values may be negative. More precisely, [`-D[axis]<=`]` `[`v`]` `[`<`]` `[`D[axis]`] for [`v`] in [`indices`].

        **axis: const i32 (Optional. Default=\`\`0\`\`)**

        :   - Negative axis is supported.

        **batch_dims: const i32 (Optional. Default=\`\`0\`\`)**

        :   - The number of batch dimensions.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

        **I: uint16, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*K, T\>

        :   - Where [`K`]` `[`=`]` `[`D[:axis]`]` `[`+`]` `[`N[batch_dims:]`]` `[`+`]` `[`D[axis+1:]`].

    References

    See [tf.gather](https://www.tensorflow.org/api_docs/python/tf/gather).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.]][[gather_nd]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/scatter_gather.html#gather_nd)[](#coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.gather_nd "Link to this definition")

:   The iOS16 version. This section documents only the differences between this version and the iOS 15 [[`gather_nd`]](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.gather_nd "coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.gather_nd").

    This version supports [`batch_dims`]. Input parameter [`indices`] now supports [`int16`] and [`uint16`].

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, I\> (Required)**

        :   

        **batch_dims: const i32 (Optional. Default=\`\`0\`\`)**

        :   - The number of batch dimensions.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

        **I: uint16, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*V, T\>

        :   - [`V`]` `[`=`]` `[`K[:-1]`]` `[`+`]` `[`D[batch_dims`]` `[`+`]` `[`K[-1]:]`], where [`D`]` `[`=`]` `[`x.shape`] and [`K`]` `[`=`]` `[`indices.shape`].

    References

    See [tf.gather_nd](https://www.tensorflow.org/api_docs/python/tf/gather_nd).

[]

## scatter_gather (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.]][[gather]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/scatter_gather.html#gather)[](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.gather "Link to this definition")

:   Gather slices from input [`x`] along dimension [`axis`] according to [`indices`], similar to [tf.gather_nd](https://www.tensorflow.org/api_docs/python/tf/gather_nd).

    This section documents only the differences between this version and the iOS 16 [[`gather`]](#coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.gather "coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.gather"). The major differences are as follows:

    - Input parameter [`x`] adds support for [`int16`], [`uint16`], [`int8`], and [`uint8`].

    - Input parameter [`indices`] adds support for [`int8`] and [`uint8`].

    - Input parameter [`indices`] now supports only positive values -- negative values are considered out-of-bound. If support for negative indices is required, they must be explicitly converted to positive values, using the following:

      :::: 
      ::: highlight
          index = iOS17.select(index >= 0, index, index + max_index)
      :::
      ::::

    - 

      New input parameter called [`validate_indices`] has been added to all gather ops. Its behavior is as follows:

      :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

          - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*N, I\> (Required)**

        :   - Indices values may be negative. More precisely, [`-D[axis]<=`]` `[`v`]` `[`<`]` `[`D[axis]`] for [`v`] in [`indices`].

        **axis: const i32 (Optional. Default=\`\`0\`\`)**

        :   - Negative axis is supported.

        **batch_dims: const i32 (Optional. Default=\`\`0\`\`)**

        :   - The number of batch dimensions.

        **validate_indices: const bool (Optional)**

        :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

            - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

            - Default value is [`False`].

    Attributes[:]

    :   

        **T: fp16, fp32, int32, int16, uint16, int8, uint8**

        :   

        **I: int32, int16, uint16, int8, uint8**

        :   

    Returns[:]

    :   

        tensor\<\*K, T\>

        :   - Where [`K`]` `[`=`]` `[`D[:axis]`]` `[`+`]` `[`N[batch_dims:]`]` `[`+`]` `[`D[axis+1:]`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.]][[gather_along_axis]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/scatter_gather.html#gather_along_axis)[](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.gather_along_axis "Link to this definition")

:   Take the values along [`axis`] at locations [`indices`].

    The major differences from the previous version are illustrated in [[`gather`]](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.gather "coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.gather"). For more information, see the iOS 16 [`gather_along_axis`].

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, I\> (Required)**

        :   - [`rank(indices)`]` `[`==`]` `[`rank(x)`].

        **axis: const i32 (Optional):**

        :   - Default to [`0`].

        **validate_indices: const bool (Optional)**

        :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

            - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

            - Default value is [`False`].

    Attributes[:]

    :   

        **T: fp16, fp32, int32, int16, uint16, int8, uint8**

        :   

        **I: int32, int16, uint16, int8, uint8**

        :   

    Returns[:]

    :   

        tensor\<\*D, T\>:

        :   - Output tensor has the same shape as [`indices`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.]][[gather_nd]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/scatter_gather.html#gather_nd)[](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.gather_nd "Link to this definition")

:   Gather slices from [`x`] according to [`indices`], similar to tf.gather_nd.

    The major differences from the previous version are illustrated in [[`gather`]](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.gather "coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.gather"). For more information, see the iOS 16 [[`gather_nd`]](#coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.gather_nd "coremltools.converters.mil.mil.ops.defs.iOS16.scatter_gather.gather_nd").

    Parameters[:]

    :   

        **x: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, I\> (Required)**

        :   

        **batch_dims: const i32 (Optional. Default=\`\`0\`\`)**

        :   - The number of batch dimensions.

        **validate_indices: const bool (Optional)**

        :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

            - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

            - Default value is [`False`].

    Attributes[:]

    :   

        **T: fp16, fp32, int32, int16, uint16, int8, uint8**

        :   

        **I: int32, int16, uint16, int8, uint8**

        :   

    Returns[:]

    :   

        tensor\<\*V, T\>

        :   - [`V`]` `[`=`]` `[`K[:-1]`]` `[`+`]` `[`D[batch_dims`]` `[`+`]` `[`K[-1]:]`], where [`D`]` `[`=`]` `[`x.shape`] and [`K`]` `[`=`]` `[`indices.shape`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.]][[scatter]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/scatter_gather.html#scatter)[](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.scatter "Link to this definition")

:   Scatter [`updates`] to [`data`] at locations [`indices`] at dimension [`axis`] by the operation [`mode`].

    This section documents only the differences between this version and the iOS 15 [[`scatter`]](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter "coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter"). The major differences are as follows:

    - Input parameter [`indices`] now supports only positive values -- negative values are considered out-of-bound. If support for negative indices is required, they must be explicitly converted to positive values using the following:

      :::: 
      ::: highlight
          index = iOS17.select(index >= 0, index, index + max_index)
      :::
      ::::

    - 

      New input parameter called [`validate_indices`] has been added to all scatter ops. Its behavior is as follows:

      :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

          - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

    Parameters[:]

    :   

        **data: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\[C\], i32\> (Required)**

        :   - 1-D tensor.

        **updates: tensor\<\*K, T\> (Required)**

        :   - [`K`]` `[`=`]` `[`data.shape[:axis]`]` `[`+`]` `[`[len(indices)]`]` `[`+`]` `[`data.shape[axis+1:]`].

        **axis: const i32 (Optional)**

        :   - Default to [`0`].

        **mode: const string (Optional)**

        :   - Can be the following modes: [`add`], [`div`], [`max`], [`min`], [`mul`], [`sub`], [`update`].

            - Default value is [`update`].

        **validate_indices: const bool (Optional)**

        :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

            - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

            - Default value is [`False`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*D, T\>

        :   - With the same type and shape as input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.]][[scatter_along_axis]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/scatter_gather.html#scatter_along_axis)[](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.scatter_along_axis "Link to this definition")

:   Scatter [`updates`] to [`data`] at locations [`indices`] along [`axis`] dimension using the [`mode`] operation.

    The major differences from the previous version are illustrated in [[`scatter`]](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.scatter "coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.scatter"). For more information, see the iOS 15 [[`scatter_along_axis`]](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter_along_axis "coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter_along_axis").

    Parameters[:]

    :   

        **data: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, i32\> (Required)**

        :   - [`rank(indices)`]` `[`==`]` `[`rank(data)`].

        **updates: tensor\<\*K, T\> (Required)**

        :   - Must be the same shape as [`indices`].

        **axis: const i32 (Optional)**

        :   - Default to [`0`].

        **mode: const string (Optional)**

        :   - Default to [`add`].

            - Can be the following modes: [`add`], [`div`], [`max`], [`min`], [`mul`], [`sub`], [`update`].

        **validate_indices: const bool (Optional)**

        :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

            - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

            - Default value is [`False`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*D, T\>

        :   - With the same type and shape as input [`x`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.]][[scatter_nd]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/scatter_gather.html#scatter_nd)[](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.scatter_nd "Link to this definition")

:   Scatter [`updates`] to [`data`] at locations [`indices`].

    The major differences from the previous version are illustrated in [[`scatter`]](#coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.scatter "coremltools.converters.mil.mil.ops.defs.iOS17.scatter_gather.scatter"). For more information, see the iOS 15 [[`scatter_nd`]](#coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter_nd "coremltools.converters.mil.mil.ops.defs.iOS15.scatter_gather.scatter_nd").

    Parameters[:]

    :   

        **data: tensor\<\*D, T\> (Required)**

        :   

        **indices: tensor\<\*K, i32\> (Required)**

        :   

        **updates: tensor\<\*K, T\> (Required)**

        :   - Must be the shape as [`K[:-1]+data.shape[K[-1]:]`].

        **mode: const string (Optional)**

        :   - Default to [`add`].

            - Can be the following modes: [`add`], [`div`], [`max`], [`min`], [`mul`], [`sub`], [`update`].

        **validate_indices: const bool (Optional)**

        :   - If [`True`], it raises a runtime (possibly also a compile-time) exception for out-of-bound values of the [`indices`] parameter.

            - If [`False`], absolutely no checking is performed for out-of-bound values of [`indices`] either at compile or runtime. Behavior for out-of-bound indices is undefined but memory safe.

            - Default value is [`False`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*D, T\>

        :   - A tensor with the same shape and type as [`data`].

[]

## states (iOS 18+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS18.states "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.states.]][[read_state]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/states.html#read_state)[](#coremltools.converters.mil.mil.ops.defs.iOS18.states.read_state "Link to this definition")

:   Read a state, copy its content into a new variable, and return the variable. The type of the output variable depends on the type that is wrapped inside the state, which could be [`types.tensor`].

    Parameters[:]

    :   

        **input: state\<ST\> (Required)**

        :   

    Attributes[:]

    :   

        **ST: tensor**

        :   

    Returns[:]

    :   

        ST

        :   

[]

## tensor_operation (iOS 15+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[argsort]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#argsort)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.argsort "Link to this definition")

:   Returns a tensor containing the indices of the sorted values along a given axis of the input tensor.

    Parameters[:]

    :   

        **x: \<\*?, T\> (Required)**

        :   - Input tensor.

        **\* axis: const\<i32\> (Optional)**

        :   - Defaults to [`-1`] (the last dimension).

            - Axis to perform the operation.

        **\* ascending: const\<bool\> (Optional)**

        :   - Defaults to [`False`], sort in descending order.

            - [`True`] to sort in ascending order.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, int32\>

        :   - Tensor containing the indices of the sorted values

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[band_part]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#band_part)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.band_part "Link to this definition")

:   Returns a tensor setting everything outside a center band to zeros for the innermost matrix. That is, band(m, n) = (lower \< 0 \|\| (m-n) \<= lower) && (upper \< 0 \|\| (n-m) \<= upper) output\[i, j, k, ..., m, n\] = band(m, n) \* input\[i, j, k, ..., m, n\]

    Special cases:

    - [`band_part(x,`]` `[`0,`]` `[`-1)`] returns upper triangular part.

    - [`band_part(x,`]` `[`-1,`]` `[`0)`] returns lower triangular part.

    - [`band_part(x,`]` `[`0,`]` `[`0)`] returns diagonal.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **lower: const\<i32\> (Optional)**

        :   - Number of lower / below sub-diagonals to keep. If negative, keep entire lower triangle.

            - Defaults to [`-1`] (keep the entire lower triangle).

        **upper: const\<i32\> (Optional)**

        :   - Number of upper / above sub-diagonals to keep. If negative, keep entire lower triangle.

            - Defaults to [`-1`] (keep the entire upper triangle).

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type and shape as the input tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[concat]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#concat)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.concat "Link to this definition")

:   Concatenates tensors along a dimension.

    Parameters[:]

    :   

        **values: Tuple\[tensor\<\[d0, d1, ..., d_axis_i, ..., d_n\],T\>\] (Required)**

        :   - The number of dimensions of the input tensors must match, and all dimensions except [`axis`] must be equal.

            - The tensors may be variadic, but the number of tensors must be determined at compile time (i.e. a tuple).

        **axis: const\<int32\> (Required)**

        :   - The dimension along which to concatenate. Must be in the range [`[-rank(values[i]),`]` `[`rank(values[i]))`] for all [`i`].

        **interleave: const\<bool\> (Optional, Default=False)**

        :   - If True, concatenate the inputs by interleaving them.

            - If True, all the inputs to this op must have the exact same shape.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\[d0, d1,...d_axis_out, ..., d_n\],T\>

        :   - Where [`d_axis_out`]` `[`=`]` `[`sum(d_axis_i)`].

    Examples

    :::: 
    ::: highlight
        in1 = [[1, 2], [3, 4], [5, 6]]  # shape (3, 2)
        in2 = [[7, 8], [9, 10], [11, 12]]  # shape (3, 2)
        axis = 0  # output shape is (6, 2)

        if interleave is False:  # default
            # output[0:3, :] = in1
            # output[3:6, :] = in2
            output = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]]

        if interleave is True:
            # output[0::2, :] = in1
            # output[1::2, :] = in2
            output = [[1, 2], [7, 8], [3, 4], [9, 10], [5, 6], [11, 12]]
    :::
    ::::

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[cumsum]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#cumsum)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.cumsum "Link to this definition")

:   Returns the cumulative sum of the input along the given axis.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **axis: const\<i32\> (Optional)**

        :   - Defaults to [`0`].

            - Axis for which the cumulative sum is computed.

        **exclusive: const\<bool\> (Optional)**

        :   - Defaults to [`False`].

            - When set to [`False`], inclusive cumsum is computed, that is the first element of the output is identical to the first element in the input.

            - When set to [`True`], exclusive cumsum is computed, which makes the first element of output to [`0`].

        **reverse: const\<bool\> (Optional)**

        :   - Defaults to [`False`].

            - When set to [`True`], perform cumsum in the reverse order.

    Attributes[:]

    :   

        **T: fp16, fp32, i32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type and shape as the input tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[fill]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#fill)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.fill "Link to this definition")

:   Returns a tensor with a given shape filled with a constant value.

    Parameters[:]

    :   

        **shape: tensor\<\[K\], i32\> (Required)**

        :   - Target output tensor shape.

            - [`K`] is the rank of the output tensor. [`shape[k]`]` `[`>`]` `[`0`] for [`k`]` `[`=`]` `[`0,...,`]` `[`K-1`].

        **value: const\<T\> (Optional)**

        :   - Defaults to [`0.0`].

            - Constant value to fill in.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Tensor with shape determined by the input shape.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[flatten2d]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#flatten2d)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.flatten2d "Link to this definition")

:   Flattens input tensor into 2d tensor by flattening dimensions before and after the provided axis.

    Parameters[:]

    :   

        **x: tensor\<\[\*d\], T\> (Required)**

        :   - Input tensor.

        **axis: const\<i32\> (Optional)**

        :   - Defaults to [`1`].

            - Negative axis is supported.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<d_prior, d_post, T\>

        :   - [`d_prior`] is product of dimensions [`x[:axis]`]

            - [`d_post`] is product of dimensions [`x[axis:]`]

    Examples

    1.  [`input_shape`]` `[`=`]` `[`(3,`]` `[`),`]` `[`axis`]` `[`=`]` `[`-1,`]` `[`output_shape`]` `[`=`]` `[`(1,`]` `[`3)`]

    2.  [`input_shape`]` `[`=`]` `[`(3,`]` `[`),`]` `[`axis`]` `[`=`]` `[`1,`]` `[`output_shape`]` `[`=`]` `[`(3,`]` `[`1)`]

    3.  [`input_shape`]` `[`=`]` `[`(4,`]` `[`3),`]` `[`axis`]` `[`=`]` `[`-1,`]` `[`output_shape`]` `[`=`]` `[`(4,`]` `[`3)`]

    4.  [`input_shape`]` `[`=`]` `[`(2,`]` `[`3,`]` `[`2),`]` `[`axis`]` `[`=`]` `[`-1,`]` `[`output_shape`]` `[`=`]` `[`(6,`]` `[`2)`]

    5.  [`input_shape`]` `[`=`]` `[`(5,`]` `[`5,`]` `[`2),`]` `[`axis`]` `[`=`]` `[`1,`]` `[`output_shape`]` `[`=`]` `[`(5,`]` `[`10)`]

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[identity]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#identity)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.identity "Link to this definition")

:   Returns a tensor with the same shape and contents as input.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type and shape as the input tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[non_maximum_suppression]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#non_maximum_suppression)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.non_maximum_suppression "Link to this definition")

:   Applies non-maximum suppression (NMS) on the input box coordinates according to their intersection-over-union (IoU).

    NMS selects a subset of bounding boxes in descending order of score, and removes boxes that have high intersection-over-union (IOU) overlap with previously-selected boxes.

    Parameters[:]

    :   

        **boxes: tensor\<\[n, B, 4\], T\> (Required)**

        :   - Box coordinates on which to perform NMS. The coordinates are expected in CENTER_SIZE_WIDTH_FIRST format (x, y, width, height) where (x, y) is the center.

        **scores: tensor\<\[n, B, K\], T\> (Required)**

        :   - Scores for each one of the boxes. K is the number of classes.

        **iou_threshold: const\<T\> (Required)**

        :   - The intersection over union ([`IoU`]) threshold over which boxes are suppressed. NMS remove all overlapping boxes with [`IoU`]` `[`>`]` `[`iou_threshold`].

        **score_threshold: const\<T\> (Required)**

        :   - Before IoU suppression is performed, boxes with class scores below this threshold are rejected.

        **max_boxes: const\<i32\> (Required)**

        :   - Maximum number of boxes to select. If the number of surviving boxes are less, output is padded up to this number.

        **per_class_suppression: const\<bool\> (Optional)**

        :   - Defaults to [`False`].

            - If [`True`], suppression is performed independently within boxes of each class.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, max_boxes, 4\], T\>

        :   - Coordinates of selected boxes.

        tensor\<\[n, max_boxes, K\], T\>

        :   - Scores of selected boxes.

        tensor\<\[n, max_boxes\], i32\>

        :   - Indices of selected boxes.

        tensor\<\[n\], i32\>

        :   - Number of boxes selected for each batch.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[non_zero]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#non_zero)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.non_zero "Link to this definition")

:   Returns the indices of the elements in the given tensor that are non-zero.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Tensor, values selected at indices where its values is not equal to [`0`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\[N, R\], int32\>

        :   - 2-dimensional tensor contains indices of elements that are non-zero. Each row is the index for a non-zero value.

            - [`N`] is the number of non-zero elements, [`R`] is the rank of the input.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[one_hot]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#one_hot)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.one_hot "Link to this definition")

:   Returns one-hot vectors whose locations represented in [`indices`] take the [`on_value`], while other locations take the [`off_value`].

    Parameters[:]

    :   

        **indices: tensor\<\[D\], i32\> (Required)**

        :   - Tensor, values indicate the locations for each one-hot vector to take the [`on_value`].

        **one_hot_vector_size: i32 (Required)**

        :   - Indicates the number of returning vectors.

        **axis: const i32 (Optional)**

        :   - Indicates which dimension to append the new axis.

            - If the input indices is rank [`D`], the output tensor will have rank [`D+1`].

            - Defaults to [`-1`] (the last dimension).

        **on_value: const T (Optional)**

        :   - Values for locations where defined in [`indices`].

            - Defaults to [`1`].

        **off_value: const T (Optional)**

        :   - Defaults to [`0`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - A tensor that contains one-hot vectors.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[pad]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#pad)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.pad "Link to this definition")

:   Pads a tensor.

    Parameters[:]

    :   

        **x: tensor\<\[\*D_in\], T\> (Required)**

        :   

        **pad: tensor\<\[2\*N\], i32\> (Required)**

        :   [`N`]` `[`<=`]` `[`D_in`]. Last [`N`] dimensions of [`x`] are padded as follows:

            - 

              For each dimension [`i`] of [`x`] if [`i`]` `[`>=`]` `[`D_in`]` `[`-`]` `[`N`]:

              :   - pad [`pad[2*i]`] elements before [`x[..,i,..]`].

                  - pad [`pad[2*i+1]`] elements after [`x[..,i,..]`].

            - If mode is "reflect" then [`pad[2*i]`] and [`pad[2*i+1]`] can be at most [`D[i]-1`].

            - If mode is "replicate" then [`pad[2*i]`] and [`pad[2*i+1]`] can be at most [`D[i]`].

            - If pad is not a constant, it must be a vector of length [`2`]` `[`*`]` `[`rank(x)`], that is, [`N`]` `[`==`]` `[`D_in`].

        **mode: const\<str\> (Optional)**

        :   - Defaults to [`constant`].

            - Must be one of the following values: [`constant`], [`reflect`], or [`replicate`].

        **constant_val: const\<T\> (Optional)**

        :   - Defaults to [`0`].

            - Constant value to pad. Ignored if [`mode`]` `[`!=`]` `[`constant`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[\*D_out\], T\>

        :   - Tensor with same type as the input.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[range_1d]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#range_1d)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.range_1d "Link to this definition")

:   Returns a numpy-like 1-D range sequence.

    Parameters[:]

    :   

        **start: \<T\> (Required)**

        :   - The start point of the sequence.

        **end: \<T\> (Required)**

        :   - The upper limit of the sequence, exclusive.

        **step: \<T\> (Required)**

        :   - Number that increments [`start`].

    Attributes[:]

    :   

        **T: i32, fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<M, T\>

        :   - A 1-D tensor, where [`M`] is the length of the sequence.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[shape]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#shape)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.shape "Link to this definition")

:   Returns a 1-dimensional tensor with the shape of the input tensor.

    Parameters[:]

    :   

        **x: tensor\<\[\*?\], T\> (Required)**

        :   - Input tensor.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<K, i32\>

        :   - Shape of the input tensor.

            - [`K`]` `[`=`]` `[`x.rank`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[split]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#split)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.split "Link to this definition")

:   Split tensors into a tuple

    Parameters[:]

    :   

        **x: \<\*?, T\> (Required)**

        :   - The tensor to split.

            - The tensors may be variadic, but the number of tensors must be determined at compile time (i.e. a tuple).

        **axis: const\<i32\> (Required)**

        :   - The dimension along which to concatenate. Must be in the range [`[-rank(x),`]` `[`rank(x))`].

        **num_splits: \<i32\> (Optional)**

        :   If specified, divide [`x`] into [`num_splits`] tensors along [`axis`]. Its behavior depends on [`split_sizes`]:

            > ::: 
            > - If [`split_sizes`] is defined, [`num_splits`]` `[`==`]` `[`S`], and the output sizes may be uneven.
            >
            > - If [`split_sizes`] is not defined, [`value.shape[axis]`] must be divisible by [`num_splits`], and the output sizes must be even.
            > :::

            At least one of [`num_splits`] or [`split_sizes`] must be provided. If [`split_sizes`] length [`S`] cannot be determined at compile time, [`num_splits`] must be supplied to determine the number of outputs.

        **split_sizes: const\<S, i32\> (Optional)**

        :   - Sizes to split to. The sum of [`split_sizes`] must equal to [`value.shape[axis]`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        Tuple\[tensor\<\*?, T\>\]

        :   - Where the length of the tuple is the number of splits (determined from [`num_splits`] or [`split_sizes`]).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[stack]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#stack)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.stack "Link to this definition")

:   Concatenates tensors along a dimension.

    Parameters[:]

    :   

        **values: Tuple\[tensor\<\[d0, d1,...d_axis_i, ..., d_n\], T\>\] (Required)**

        :   - All tensors must have identical shape.

        **axis: const\<i32\> (Required)**

        :   - The dimension along which to concatenate. Must be in the range [`[-rank(values[i]),`]` `[`rank(values[i]))`] for all [`i`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tenor\<\[d0, d1,...d_axis_out, ..., d_n\], T\>

        :   - Where [`d_axis_out`]` `[`=`]` `[`sum(d_axis_i)`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[tile]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#tile)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.tile "Link to this definition")

:   Returns a new tensor by replicating input [`x`] multiples times. Dimension [`i`] of [`x`] will be replicated [`reps[i]`] times.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **reps: tensor\<\[rank(x)\], i32\> (Required)**

        :   - A 1-D tensor with length [`rank(x)`], which indicates the number to replicate the input along each dimension.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>:

        :   - An n-D tensor with same type as the input.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.]][[topk]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html#topk)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.topk "Link to this definition")

:   Returns a tensor containing top or bottom [`k`] values and the corresponding indices of the input tensor along a given axis.

    Parameters[:]

    :   

        **x: \<\*?, T\> (Required)**

        :   - Input tensor.

        **k: const\<i32\> (Optional)**

        :   - Defaults to [`1`].

            - Number of values/indices to be computed along each axis.

        **axis: const\<i32\> (Optional)**

        :   - Defaults to [`-1`] (last dimension).

            - Axis to perform the operation.

        **ascending: const\<bool\> (Optional)**

        :   - Defaults to [`False`], sort in descending order.

            - [`True`] to sort in ascending order.

    Attributes[:]

    :   

        **T: fp16, fp32, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Values of top/bottom [`k`] elements.

        tensor\<\*?, int32\>

        :   - Indices of the top/bottom [`k`] elements along axis.

[]

## tensor_operation (iOS 16+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS16.tensor_operation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.tensor_operation.]][[fill_like]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/tensor_operation.html#fill_like)[](#coremltools.converters.mil.mil.ops.defs.iOS16.tensor_operation.fill_like "Link to this definition")

:   Returns a tensor with the same shape as the input tensor filled with a constant value.

    Parameters[:]

    :   

        **ref_tensor: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **value: const\<U\> (Optional)**

        :   - Default is [`0.0`].

            - Constant value to fill in.

    Attributes[:]

    :   

        **T: fp16, fp32, int32, bool**

        :   

        **U: fp16, fp32, int32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Tensor with shape determined by the input tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.tensor_operation.]][[topk]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/tensor_operation.html#topk)[](#coremltools.converters.mil.mil.ops.defs.iOS16.tensor_operation.topk "Link to this definition")

:   A version of [`topk`] for iOS 16+. This section documents the differences. The following are additional parameters for the iOS 16+ version. For the rest of the documentation, see [the iOS 15 version of topk](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.topk).

    Parameters[:]

    :   

        **sort: const\<bool\> (Optional)**

        :   - Defaults to [`True`].

            - If [`True`], [`top-k`] elements are themselves sorted. Otherwise, no particular ordering is guaranteed.

        **return_indices: const\<bool\> (Optional)**

        :   - Defaults to [`True`].

            - If [`True`], returns both values and indices. Otherwise, returns only the [`top-k`] values.

    Attributes[:]

    :   

        **T: fp32, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Values of top/bottom [`k`] elements.

        tensor\<\*?, int32\>

        :   - Only returned when [`return_indices`]` `[`=`]` `[`True`]

            - Indices of the top/bottom [`k`] elements along axis.

[]

## tensor_operation (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.tensor_operation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_operation.]][[non_maximum_suppression]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_operation.html#non_maximum_suppression)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_operation.non_maximum_suppression "Link to this definition")

:   Performs non-maximum suppression (NMS) on the boxes according to their intersection-over-union (IoU).

    NMS iteratively removes lower-scoring boxes which have an IoU greater than [`iou_threshold`] with another (higher-scoring) box.

    The major differences between this version and the iOS 15 [[`non_maximum_suppression`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.non_maximum_suppression "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_operation.non_maximum_suppression") are as follows:

    > ::: 
    > - The input parameter [`score_threshold`] has been removed.
    >
    > - The inputs [`boxes`] and [`scores`] are ordered with number of boxes in the last dimension.
    >
    > - The fourth output containing number of boxes for each batch has been removed.
    > :::

    Parameters[:]

    :   

        **boxes: tensor\<\[n, 4, B\], T\> (Required)**

        :   - Box coordinates on which to perform NMS. The coordinates are expected in [`CENTER_SIZE_WIDTH_FIRST`] format [`(x,`]` `[`y,`]` `[`width,`]` `[`height)`], in which [`(x,`]` `[`y)`] is the center.

        **scores: tensor\<\[n, K, B\], T\> (Required)**

        :   - Scores for each one of the boxes. [`K`] is the number of classes.

        **iou_threshold: const\<T\> (Required)**

        :   - The intersection over union (IoU) threshold over which boxes are suppressed. NMS remove all overlapping boxes with [`IoU`]` `[`>`]` `[`iou_threshold`].

        **max_boxes: const\<i32\> (Required)**

        :   - Maximum number of boxes to select. If the number of surviving boxes are less, the output is padded up to this number.

        **per_class_suppression: const\<bool\> (Optional)**

        :   - Defaults to [`False`].

            - If [`True`], suppression is performed independently within boxes of each class.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, 4, max_boxes\], T\>

        :   - Coordinates of selected boxes.

        tensor\<\[n, K, max_boxes\], T\>

        :   - Scores of selected boxes.

        tensor\<\[n, max_boxes\], i32\>

        :   - Indices of selected boxes.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_operation.]][[topk]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_operation.html#topk)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_operation.topk "Link to this definition")

:   A version of [`topk`] for iOS 17+. The differences between this version and the iOS 16 [[`topk`]](#coremltools.converters.mil.mil.ops.defs.iOS16.tensor_operation.topk "coremltools.converters.mil.mil.ops.defs.iOS16.tensor_operation.topk") are:

    > ::: 
    > - 
    >
    >   New data type support. The newly added data types are:
    >
    >   :   - int8, uint8, int16, unint16 for [`x`] and output.
    >
    >       - int8, int16 for [`k`].
    >
    > - Validation restrictions on the optional [`indices`] output must be either uint16 or int32.
    >
    > - A new input parameter [`output_indices_dtype`] has been added to set the dtype of output [`indices`].
    > :::

    Parameters[:]

    :   

        **x: \<\*?, T\> (Required)**

        :   - Input tensor.

        **k: const\<K\> (Optional)**

        :   - Defaults to [`1`].

            - Number of values/indices to be computed along each axis.

            - Set to [`-1`] to select all elements.

        **axis: const\<i32\> (Optional)**

        :   - Defaults to [`-1`] (last dimension).

            - Axis to perform the operation.

        **ascending: const\<bool\> (Optional)**

        :   - Defaults to [`False`], sort in descending order.

            - [`True`] to sort in ascending order.

        **sort: const\<bool\> (Optional)**

        :   - Defaults to [`True`].

            - If [`True`], [`top-k`] elements are themselves sorted. Otherwise, no particular ordering is guaranteed.

        **return_indices: const\<bool\> (Optional)**

        :   - Defaults to [`True`].

            - If [`True`], returns both values and indices. Otherwise, returns only the [`top-k`] values.

        **output_indices_dtype: const\<str\> (Optional, default="int32")**

        :   - It can only be set when [`return_indices`] is [`True`].

            - This parameter can take [`"int32"`] or [`"uint16"`] as values.

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16**

        :   

        **K: int8, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Values of top/bottom [`k`] elements.

        tensor\<\*?, U\>

        :   - Only returned when [`return_indices`]` `[`=`]` `[`True`]

            - Indices of the top/bottom [`k`] elements along axis.

            - U is int32 or uint16 determined by [`output_indices_dtype`] (int32 by default).

[]

## tensor_transformation (iOS 15)[](#module-coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[batch_to_space]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#batch_to_space)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.batch_to_space "Link to this definition")

:   Rearrange elements in a tensor from batch into spatial dimensions.

    Parameters[:]

    :   

        **x: tensor\<\[n, C, H, W\], T\> (Required)**

        :   - Input tensor must have rank [`4`].

            - The first and the second dimension are batch, channel; respectively.

            - The remaining dimensions [`(H,`]` `[`W)`] are treated as "spatial dimensions".

        **block_shape: const tensor\<\[2\], i32\> (Required)**

        :   - The length of the [`block_shape`] must be [`2`].

            - It defines the shapes of the block in which the spatial dimensions are multiplied.

        **crops: const tensor\<\[2, 2\], i32\> (Required)**

        :   - It must have shape [`(2,`]` `[`2)`].

            - It defines the amount to crop from each spatial dimension.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[new_n, C, new_H, new_W\], T\>

        :   - [`new_n`]` `[`=`]` `[`n`]` `[`/`]` `[`(block_shape[0]`]` `[`*`]` `[`block_shape[1])`]

            - [`new_H`]` `[`=`]` `[`(H`]` `[`*`]` `[`block_shape[0])`]` `[`-`]` `[`paddings[0][0]`]` `[`-`]` `[`padding[0][1]`]

            - [`new_W`]` `[`=`]` `[`(W`]` `[`*`]` `[`block_shape[1])`]` `[`-`]` `[`paddings[1][0]`]` `[`-`]` `[`padding[1][1]`]

            - The output has the same rank as the input.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[depth_to_space]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#depth_to_space)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.depth_to_space "Link to this definition")

:   Rearrange elements in a tensor from depth (channel) into spatial dimensions.

    Parameters[:]

    :   

        **x: tensor\<\[n, C, H, W\], T\> (Required)**

        :   - Input tensor of rank [`4`].

        **block_size: const i32 (Required)**

        :   - The size of the spatial block. Must be greater than [`1`] and divisible by channel dimension [`C`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C / block_size\^2, H x block_size, W x block_size\], T\>

        :   - Where [`b`] is the block size.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[expand_dims]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#expand_dims)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.expand_dims "Link to this definition")

:   Insert a single-dimension in a 1-D or higher tensor at each axis in axes.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Scalar or tensor.

        **axes: const tensor\<\[K\], i32\> Required**

        :   - [`K`] is the number of dimensions expanded.

            - Insert single dimension at dimension index at each axes.

            - Negative value to index from the end. [`-d-1`]` `[`<=`]` `[`axis`]` `[`<=`]` `[`d`] where [`d`] is the rank of [`x`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*(rank(x)+K), T\>

        :   - Same type as the input [`x`] with rank [`rank(x)+K`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[pixel_shuffle]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#pixel_shuffle)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.pixel_shuffle "Link to this definition")

:   Rearrange elements in a tensor from depth (channel) into spatial dimensions. Equivalent to PyTorch's [`PixelShuffle`].

    Parameters[:]

    :   

        **x: tensor\<\[n, C x f\^2, H, W\], T\> (Required)**

        :   - Input tensor of rank [`4`].

        **upscale_factor: const\<i32\>**

        :   - Factor to increase spatial resolution by.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C, H x f, W x f\], T\>

        :   - Where [`f`] is the upscale factor.

    References

    [torch.nn.PixelShuffle](https://pytorch.org/docs/stable/generated/torch.nn.PixelShuffle.html?highlight=pixel%20shuffle#torch.nn.PixelShuffle)

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[reshape]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#reshape)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reshape "Link to this definition")

:   Return a tensor that has the same values as [`x`] with shape [`shape`]. [`shape`] must have the same volume (number of elements) as [`x`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - An n-D tensor or a scalar.

            - If [`x`] is fixed rank (and possibly contains symbolic dimension), shape may contain elements that are not positive integers (see below).

            - If [`x`] is variadic rank, shape can only contain positive integers.

        **shape: tensor\<\[K\], i32\> (Required)**

        :   A 1-D tensor, with elements from the following:

            > ::: 
            > - Positive integers.
            >
            > - Symbols: All but one symbol in shape must be present in [`x.shape`]. The new symbol that is not present in [`x.shape`] represent a dimension such that the total size remains constant. Symbol is illegal if [`x`] is variadic rank.
            >
            > - [`-1`]: [`-1`] introduces a new symbol (see Symbols above). Therefore, [`-1`] is allowed if all symbols in the shape appear in [`x.shape`]. [`-1`] is illegal if [`x`] is variadic rank.
            >
            > - [`0`]: If [`K`]` `[`==`]` `[`rank(x)`] then [`0`] means inheriting from the corresponding dimension in [`x.shape`]. [`0`] is illegal if [`x`] is variadic rank.
            > :::

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Tensor with shape determined by the input shape.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[reverse]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#reverse)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reverse "Link to this definition")

:   Reverse the order of the input tensor [`x`] along specified [`axes`] (dimensions).

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **axes: const\<D, i32\> (Optional)**

        :   - Dimension(s) to reverse. Each axis must be in the range [`[-rank(x),`]` `[`rank(x))`].

            - Defaults to None (reverse on all dimensions).

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type and shape as the input tensor.

    References

    See [tf.reverse](https://www.tensorflow.org/api_docs/python/tf/reverse) and [TORCH](https://pytorch.org/docs/stable/torch.html#torch.flip).

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[reverse_sequence]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#reverse_sequence)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reverse_sequence "Link to this definition")

:   Reverse variable length slices for specified axes / dimensions of the input tensor. This op first slices input tensor along the [`batch_axis`] dimension, then partially reverses the elements along the [`seq_axis`] for the first [`lengths[i]`] elements.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **lengths: tensor\<L, i32\> (Required)**

        :   - 1-dimensional tensor of length [`x.shape[batch_axis]`] specifying the length of the sequence to reverse.

            - Values must be in range [`[0,`]` `[`x.shape[seq_axis]]`].

        **seq_axis: const\<i32\> (Optional)**

        :   - The dimension to reverse.

            - Defaults to [`0`].

        **batch_axis: const\<i32\> (Optional)**

        :   - Dimension for slicing.

            - Defaults to [`0`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type and shape as the input tensor.

    References

    [tf.reverse_sequence](https://www.tensorflow.org/api_docs/python/tf/reverse_sequence)

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[slice_by_index]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#slice_by_index)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_index "Link to this definition")

:   Method for numpy style indexing and slicing. With a tensor [`x`], this method achieves the following:

    [`result`]` `[`=`]` `[`x[begin[0]:`]` `[`end[0]:`]` `[`stride[0],`]` `[`begin[1]:`]` `[`end[1]:`]` `[`stride[1],`]` `[`...]`]

    Note: This method does not support pure indexing. You would need to do a squeeze if indexing is intended.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor

        **begin: tensor\<\[rank(x)\], i32\> (Required)**

        :   - Starting index for the dimension of slicing.

        **end: tensor\<\[rank(x)\], i32\> (Required)**

        :   - Ending index for the dimension of slicing.

        **stride: tensor\<\[rank(x)\], i32\> (Optional)**

        :   - Default is all [`1`].

            - Stride for the dimension of slicing.

        **begin_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`begin_mask[i]==True`], ignores [`begin[i]`], and set [`begin[i]`] to [`0`].

        **end_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`end_mask[i]==True`], ignores [`end[i]`], and set [`end[i]`] to [`x.shape[i]`].

        **squeeze_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`squeeze_mask[i]==true`], ignores [`end[i]`], and do the pure index at [`begin[i]`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Scalar or tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[slice_by_size]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#slice_by_size)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_size "Link to this definition")

:   Slice input tensor starting from the given [`begin`] index and by the amount specified by the [`size`] input, for each dimension.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **begin: tensor\<\[rank(x)\], i32\> (Required)**

        :   - The begin index for slice.

        **size: tensor\<\[rank(x)\], i32\> (Required)**

        :   - The size that is to be sliced. If [`size`] is [`-1`], all the remaining elements starting with "begin" are sliced.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Scalar or tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[sliding_windows]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#sliding_windows)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.sliding_windows "Link to this definition")

:   Return a tensor containing all windows of [`size`], separated by stride along the given [`axis`].

    Parameters[:]

    :   

        **x: tensor\<\[\*d0, d_axis, \*dn\], T\>**

        :   - Input tensor.

        **axis: const\<i32\>**

        :   - Axis to perform the operation.

        **size: const\<i32\>**

        :   - Number of elements in the sliding window.

        **stride: const\<i32\> Optional**

        :   - Default to [`1`].

            - The stride of the input elements in the sliding window.

    Attributes[:]

    :   

        **T: fp16, fp32, int32**

        :   

    Returns[:]

    :   

        tensor\<\[\*d0, d_axis - size // stride + 1, size, \*dn\], T\>

        :   - The output will be a tensor of rank [`N+1`] where [`N`] is the input tensor rank.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[space_to_batch]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#space_to_batch)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.space_to_batch "Link to this definition")

:   Rearrange elements in a tensor from spatial into batch dimensions.

    Parameters[:]

    :   

        **x: tensor\<\[n, C, H, W\], T\> (Required)**

        :   - Input tensor must have rank [`4`].

            - The first and the second dimension are batch, channel; respectively.

            - The remaining dimensions [`(H,`]` `[`W)`] are treated as "spatial dimensions".

        **block_shape: const tensor\<\[2\], i32\> (Required)**

        :   - The length of the [`block_shape`] must be [`2`].

            - It defines the shapes of the block in which the spatial dimensions are divided.

        **paddings: const tensor\<\[2, 2\], i32\> (Required)**

        :   - It must have shape [`(2,`]` `[`2)`].

            - It defines the padding for each spatial dimension.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[new_n, C, new_H, new_W\], T\>

        :   - [`new_n`]` `[`=`]` `[`n`]` `[`*`]` `[`block_shape[0]`]` `[`*`]` `[`block_shape[1]`]

            - [`new_H`]` `[`=`]` `[`(H`]` `[`+`]` `[`paddings[0][0]`]` `[`+`]` `[`padding[0][1])/block_shape[0]`]

            - [`new_W`]` `[`=`]` `[`(W`]` `[`+`]` `[`paddings[1][0]`]` `[`+`]` `[`padding[1][1])/block_shape[1]`]

            - The output has the same rank as the input.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[space_to_depth]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#space_to_depth)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.space_to_depth "Link to this definition")

:   Rearrange elements in a tensor from spatial into depth (channel) dimension.

    Parameters[:]

    :   

        **x: tensor\<\[n, C, H, W\], T\> (Required)**

        :   - Input tensor of rank [`4`].

        **block_size: const\<i32\> (Required)**

        :   - The size of the spatial block. Must be greater than [`1`] and divisible by spatial dimensions [`H,`]` `[`W`].

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C x block_size\^2, H / block_size, W / block_size\], T\>

        :   - Where [`b`] is the block size.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[squeeze]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#squeeze)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.squeeze "Link to this definition")

:   Remove single-dimension dimensions in a 1-D or higher tensor.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Must be at least 1-D.

        **axes: const\<K,i32\> (Optional)**

        :   - Axes to squeeze out.

            - The behaviour of squeezing non-single dimensions follow PyTorch instead of NumPy, where it ignores non-single dimensions instead of erroring out. More specifically, if x has shape (2, 3, 4) and axes is \[0, 1\], the output will be a tensor with shape (2, 3, 4).

            - Default to remove all single-dimensions.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*(rank(x)-K), T\>

        :   - Tensor with same type as input [`x`] and rank [`rank(x)-K`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.]][[transpose]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html#transpose)[](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.transpose "Link to this definition")

:   Permute tensor [`x`] dimensions according to [`perm`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Must be at least 1-D. [`x`] may have a symbolic shape.

        **perm: const\<\[rank(x)\], i32\> (Required)**

        :   - Permutation order. -rank(x) \<= perm\[I\] \< rank(x) for all perm entries.

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Tensor with same rank and type as [`x`].

    References

    [torch.Tensor.permute](https://pytorch.org/docs/stable/tensors.html#torch.Tensor.permute)

[]

## tensor_transformation (iOS 16+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS16.tensor_transformation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.tensor_transformation.]][[pixel_unshuffle]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/tensor_transformation.html#pixel_unshuffle)[](#coremltools.converters.mil.mil.ops.defs.iOS16.tensor_transformation.pixel_unshuffle "Link to this definition")

:   Rearrange elements in a tensor from spatial dimensions into depth (channel). It is basically the inverse operation of [[`pixel_shuffle`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.pixel_shuffle "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.pixel_shuffle"). Equivalent to [PyTorch PixelUnshuffle](https://pytorch.org/docs/stable/generated/torch.nn.PixelUnshuffle.html#pixelunshuffle).

    Parameters[:]

    :   

        **x: tensor\<\[n, C, H / f , W / f\], T\> (Required)**

        :   - Input tensor of rank [`4`].

        **downscale_factor: const\<i32\>**

        :   - Factor to decrease spatial resolution by.

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[n, C \* f\^2, H, W\], T\>

        :   - In which [`f`] is the downscale factor.

    References

    [torch.nn.PixelUnshuffle](https://pytorch.org/docs/stable/generated/torch.nn.PixelUnshuffle.html)

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS16.tensor_transformation.]][[reshape_like]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS16/tensor_transformation.html#reshape_like)[](#coremltools.converters.mil.mil.ops.defs.iOS16.tensor_transformation.reshape_like "Link to this definition")

:   Reshape a tensor to an output shape specified by some or all dimensions of a tuple of reference tensors [`ref_tensors`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - The input tensor to be reshaped.

        **ref_tensors: Tuple\[tensor\<\*?, R\>\] (Required)**

        :   - A tuple of tensors that define the output shape.

        **begins: Tuple\[const\<int32\>\] (Required)**

        :   - A tuple of integers specifying the begin index into the shape vector of the corresponding [`ref_tensor`].

        **ends: Tuple\[const\<int32\>\] (Required)**

        :   - A tuple of integers specifying the end index into the shape vector of the corresponding [`ref_tensor`].

        **end_masks: Tuple\[const\<bool\>\] (Required)**

        :   - If [`True`], select all axes from the begin index until the end of the corresponding [`ref_tensor`], as in [`ref_tensors[i].shape[begins[i]:]`].

    Attributes[:]

    :   

        **T: fp16, fp32, i32, bool**

        :   

        **R: fp16, fp32, i32, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type as input tensor [`x`].

            - Output shape is computed by [`ref_tensors`], [`begins`], [`ends`], and [`end_masks`].

    Notes

    The output shape is computed as follows:

    :::: 
    ::: highlight
        output_shape = []
        num_of_refs = len(begins)
        for i in range(num_of_refs):
            if end_masks[i]:
                output_shape.append(ref_tensor_i.shape[begins[i]:])
            else:
                output_shape.append(ref_tensor_i.shape[begins[i]:ends[i]])
        output_shape = np.concat(output_shape, axis=0)
    :::
    ::::

    The following is an example:

    :::: 
    ::: highlight
        ref_tensors=[tensor[2, 3, 4], tensor[1, 5, 6]]
        begins=[0, 1]
        ends=[2, 0]
        end_masks=[False, True]
    :::
    ::::

    The output shape would be [`(2,`]` `[`3,`]` `[`5,`]` `[`6)`].

[]

## tensor_transformation (iOS 17+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[expand_dims]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#expand_dims)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.expand_dims "Link to this definition")

:   Insert a single-dimension in a 1-D or higher tensor at each axis in axes.

    The major difference between this version and the iOS 15 [[`expand_dims`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.expand_dims "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.expand_dims") is that input [`x`] supports more data types: int8, uint8, int16, uint16.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Scalar or tensor.

        **axes: const tensor\<\[K\], int32\> Required**

        :   - [`K`] is the number of dimensions expanded.

            - Insert single dimension at dimension index at each axes.

            - Negative value to index from the end. [`-d-1`]` `[`<=`]` `[`axis`]` `[`<=`]` `[`d`] where [`d`] is the rank of [`x`].

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

    Returns[:]

    :   

        tensor\<\*(rank(x)+K), T\>

        :   - Same type as the input [`x`] with rank [`rank(x)+K`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[reshape]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#reshape)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.reshape "Link to this definition")

:   Return a tensor that has the same values as [`x`] with shape [`shape`]. [`shape`] must have the same volume (number of elements) as [`x`].

    The major differences between this version and the iOS 15 [[`reshape`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reshape "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reshape") are as follows:

    - When the [`shape`] contains [`0`], the restriction about [`K`]` `[`==`]` `[`rank(x)`] is no longer enforced. Each [`0`] in [`shape`] will match the corresponding dimension in [`x.shape`], counting from the rightmost element. So [`shape[i]`] matches [`input[j]`] if [`length(shape)-i`]` `[`==`]` `[`rank(input)-j`]. If a [`0`] is out of range, assign [`1`] (equivalent to [`expand_dims`] for [`x.shape`]).

      More specifically, when [`x.shape`] is [`[2,`]` `[`50]`] and [`shape`] is [`[1,`]` `[`0,`]` `[`-1,`]` `[`0]`], it will error out in iOS 15 or iOS 16 because [`x`] has rank [`2`] while the [`len`] of [`shape`] is [`4`]. In iOS 17, the result will have [`shape`] [`[1,`]` `[`1,`]` `[`2,`]` `[`50]`], because the rightmost [`0`] will be changed to the rightmost dim of [`x.shape`], which is [`50`]. There is no other [`0`] that has a corresponding dim in [`x.shape`], so it is set as [`1`]. Finally, the [`-1`] is calculated based on knowing dimensions that produce [`2`].

    - Support more data types, including int8, uint8, int16, uint16 for [`x`] and int8, int16 for [`shape`].

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - An [`n-D`] tensor or a scalar.

            - If [`x`] has a fixed rank (and possibly contains symbolic dimension), [`shape`] may contain elements that are not positive integers (see below).

            - If [`x`] has a variadic rank, [`shape`] can only contain positive integers.

        **shape: tensor\<\[K\], U\> (Required)**

        :   A 1-D tensor, with elements from the following:

            > ::: 
            > - Positive integers.
            >
            > - Symbols: All but one symbol in [`shape`] must be present in [`x.shape`]. The new symbol that is not present in [`x.shape`] represents a dimension such that the total size remains constant. Symbol is illegal if [`x`] has a variadic rank.
            >
            > - [`-1`]: [`-1`] introduces a new symbol (see Symbols). Therefore, [`-1`] is allowed if all symbols in the [`shape`] appear in [`x.shape`]. [`-1`] is illegal if [`x`] has a variadic rank.
            >
            > - [`0`]: It will match the corresponding dimension in [`x.shape`]. See the previous description of different behaviors with iOS 17.
            > :::

    Attributes[:]

    :   

        **T: fp16, fp32, int8, uint8, int16, uint16, int32, bool**

        :   

        **U: int8, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Tensor with shape determined by the input shape.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[reshape_like]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#reshape_like)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.reshape_like "Link to this definition")

:   Reshape a tensor to an output shape specified by some or all dimensions of a tuple of reference tensors [`ref_tensors`].

    The major difference between this version and the iOS 15 [[`reshape_like`]](#coremltools.converters.mil.mil.ops.defs.iOS16.tensor_transformation.reshape_like "coremltools.converters.mil.mil.ops.defs.iOS16.tensor_transformation.reshape_like") is that input [`x`] and [`ref_tensors`] supports more data types: int8, uint8, int16, uint16.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - The input tensor to be reshaped.

        **ref_tensors: Tuple\[tensor\<\*?, R\>\] (Required)**

        :   - A tuple of tensors that define the output shape.

        **begins: Tuple\[const\<int32\>\] (Required)**

        :   - A tuple of integers specifying the begin index into the shape vector of the corresponding [`ref_tensor`].

        **ends: Tuple\[const\<int32\>\] (Required)**

        :   - A tuple of integers specifying the end index into the shape vector of the corresponding [`ref_tensor`].

        **end_masks: Tuple\[const\<bool\>\] (Required)**

        :   - If [`True`], select all axes from the begin index until the end of the corresponding [`ref_tensor`], as in [`ref_tensors[i].shape[begins[i]:]`].

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

        **R: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type as input tensor [`x`].

            - Output shape is computed by [`ref_tensors`], [`begins`], [`ends`], and [`end_masks`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[reverse]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#reverse)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.reverse "Link to this definition")

:   Reverse the order of the input tensor [`x`] along specified [`axes`] (dimensions).

    The major difference between this version and the iOS 15 [[`reverse`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reverse "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reverse") is that input [`x`] supports more data types: int8, uint8, int16, uint16.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **axes: const\<D, int32\> (Optional)**

        :   - Dimension(s) to reverse. Each axis must be in the range [`[-rank(x),`]` `[`rank(x))`].

            - Defaults to None (reverse on all dimensions).

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type and shape as the input tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[reverse_sequence]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#reverse_sequence)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.reverse_sequence "Link to this definition")

:   Reverse variable length slices for specified axes / dimensions of the input tensor. This op first slices input tensor along the [`batch_axis`] dimension, then partially reverses the elements along the [`seq_axis`] for the first [`lengths[i]`] elements.

    The major difference between this version and the iOS 15 [[`reverse_sequence`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reverse_sequence "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.reverse_sequence") is that input supports more data types: - [`x`] additionally supports int8, uint8, int16, uint16 - [`lengths`] additionally supports int8, int16

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **lengths: tensor\<L, U\> (Required)**

        :   - 1-dimensional tensor of length [`x.shape[batch_axis]`] specifying the length of the sequence to reverse.

            - Values must be in range [`[0,`]` `[`x.shape[seq_axis]]`].

        **seq_axis: const\<int32\> (Optional)**

        :   - The dimension to reverse.

            - Defaults to [`0`].

        **batch_axis: const\<int32\> (Optional)**

        :   - Dimension for slicing.

            - Defaults to [`0`].

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

        **U: int8, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Same type and shape as the input tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[slice_by_index]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#slice_by_index)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.slice_by_index "Link to this definition")

:   Method for numpy style indexing and slicing. With a tensor [`x`], this method achieves the following:

    [`result`]` `[`=`]` `[`x[begin[0]:`]` `[`end[0]:`]` `[`stride[0],`]` `[`begin[1]:`]` `[`end[1]:`]` `[`stride[1],`]` `[`...]`]

    The differences between this version and the iOS 15 [[`slice_by_index`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_index "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_index") is that additional data types are supported for [`x`], [`begin`], [`end`], and [`stride`]. See Parameters and Attributes sections for details.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor

        **begin: tensor\<\[rank(x)\], U\> (Required)**

        :   - Starting index for the dimension of slicing.

        **end: tensor\<\[rank(x)\], U\> (Required)**

        :   - Ending index for the dimension of slicing.

        **stride: tensor\<\[rank(x)\], U\> (Optional)**

        :   - Default is all [`1`].

            - Stride for the dimension of slicing.

        **begin_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`begin_mask[i]==True`], ignores [`begin[i]`], and set [`begin[i]`] to [`0`].

        **end_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`end_mask[i]==True`], ignores [`end[i]`], and set [`end[i]`] to [`x.shape[i]`].

        **squeeze_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`squeeze_mask[i]==True`], ignores [`end[i]`], and do the pure index at [`begin[i]`].

    Attributes[:]

    :   

        **T: bool, fp16, fp32, int8, int16, int32, uint8, uint16**

        :   

        **U: int8, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Scalar or tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[slice_by_size]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#slice_by_size)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.slice_by_size "Link to this definition")

:   Slice input tensor starting from the given [`begin`] index and by the amount specified by the [`size`] input, for each dimension.

    The differences between this version and the iOS 15 [[`slice_by_size`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_size "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_size") is that additional data types are supported for [`x`], [`begin`], and [`size`]. See Parameters and Attributes sections for details.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **begin: tensor\<\[rank(x)\], U\> Required**

        :   - The begin index for slice.

        **size: tensor\<\[rank(x)\], U\> Required**

        :   - The size that is to be sliced. If [`size`] is [`-1`], all the remaining elements starting with "begin" are sliced.

    Attributes[:]

    :   

        **T: bool, fp16, fp32, int8, int16, int32, uint8, uint16**

        :   

        **U: int8, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Scalar or tensor.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[sliding_windows]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#sliding_windows)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.sliding_windows "Link to this definition")

:   Return a tensor containing all windows of [`size`], separated by stride along the given [`axis`].

    The major difference between this version and the iOS 15 [[`sliding_windows`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.sliding_windows "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.sliding_windows") is that input [`x`] supports more data types: int8, uint8, int16, uint16.

    Parameters[:]

    :   

        **x: tensor\<\[\*d0, d_axis, \*dn\], T\>**

        :   - Input tensor.

        **axis: const\<int32\>**

        :   - Axis to perform the operation.

        **size: const\<int32\>**

        :   - Number of elements in the sliding window.

        **stride: const\<int32\> Optional**

        :   - Default to [`1`].

            - The stride of the input elements in the sliding window.

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

    Returns[:]

    :   

        tensor\<\[\*d0, d_axis - size // stride + 1, size, \*dn\], T\>

        :   - The output will be a tensor of rank [`N+1`] where [`N`] is the input tensor rank.

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[squeeze]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#squeeze)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.squeeze "Link to this definition")

:   Remove single-dimension dimensions in a 1-D or higher tensor.

    The major difference between this version and the iOS 15 [[`squeeze`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.squeeze "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.squeeze") is that input [`x`] supports more data types: int8, uint8, int16, uint16.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Must be at least 1-D.

        **axes: const\<K,int32\> (Optional)**

        :   - Axes to squeeze out.

            - Default to remove all single-dimensions.

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

    Returns[:]

    :   

        tensor\<\*(rank(x)-K), T\>

        :   - Tensor with same type as input [`x`] and rank [`rank(x)-K`].

<!-- -->

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.]][[transpose]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html#transpose)[](#coremltools.converters.mil.mil.ops.defs.iOS17.tensor_transformation.transpose "Link to this definition")

:   Permute tensor [`x`] dimensions according to [`perm`].

    The major difference between this version and the iOS 15 [[`transpose`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.transpose "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.transpose") is that input [`x`] supports more data types: int8, uint8, int16, uint16.

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Must be at least 1-D. [`x`] may have a symbolic shape.

        **perm: const\<\[rank(x)\], i32\> (Required)**

        :   - Permutation order. -rank(x) \<= perm\[I\] \< rank(x) for all perm entries.

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

    Returns[:]

    :   

        tensor\<\*?,T\>

        :   - Tensor with same rank and type as [`x`].

[]

## tensor_transformation (iOS 18+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS18.tensor_transformation "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.tensor_transformation.]][[slice_update]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/tensor_transformation.html#slice_update)[](#coremltools.converters.mil.mil.ops.defs.iOS18.tensor_transformation.slice_update "Link to this definition")

:   Update a custom slice of a source tensor with another tensor of the same shape, as dictated by the slice.

    For example, if you have a tensor [`x`], this method produces the following:

    :::: 
    ::: highlight
        x[begin[0]: end[0]: stride[0], begin[1]: end[1]: stride[1], ...] = value
    :::
    ::::

    The arguments defining the slice ([`begin`], [`end`], [`stride`], [`masks`], and so on) should be treated the same way as iOS15 [[`slice_by_index`]](#coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_index "coremltools.converters.mil.mil.ops.defs.iOS15.tensor_transformation.slice_by_index").

    Parameters[:]

    :   

        **x: tensor\<\*?, T\> (Required)**

        :   - Input tensor.

        **update: tensor\<\*K, T\> (Required)**

        :   - Value tensor to be inserted.

            - The shape of the update tensor must match the slicing result of the input data.

            - rank-0 update is not supported.

        **begin: tensor\<\[rank\<x\>\], U\> (Required)**

        :   - Starting index for the dimension of slicing.

        **end: tensor\<\[rank(x)\], U\> (Required)**

        :   - Ending index for the dimension of slicing.

        **stride: tensor\<\[rank(x)\], U\> (Optional)**

        :   - Default as all [`1`].

            - Stride for the dimension of slicing.

        **begin_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`begin_mask[i]==True`], neglect [`begin[i]`], and set [`begin[i]`] to [`0`].

        **end_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`end_mask[i]==True`], neglect [`end[i]`], and set [`end[i]`] to [`x.shape[i]`].

        **squeeze_mask: tensor\<\[rank(x)\], bool\> (Optional)**

        :   - Default to all [`False`].

            - If [`squeeze_mask[i]==True`], neglect [`end[i]`], and do the pure index at [`begin[i]`].

    Attributes[:]

    :   

        **T: fp16, fp32, int8, int16, int32, uint8, uint16, bool**

        :   

        **U: int8, int16, int32**

        :   

    Returns[:]

    :   

        tensor\<\*?, T\>

        :   - Scalar or tensor.

[]

## transformers (iOS 18+)[](#module-coremltools.converters.mil.mil.ops.defs.iOS18.transformers "Link to this heading")

*[class][ ]*[[coremltools.converters.mil.mil.ops.defs.iOS18.transformers.]][[scaled_dot_product_attention]][(]*[[\*\*]][[kwargs]]*[)][[[\[source\]]]](../_modules/coremltools/converters/mil/mil/ops/defs/iOS18/transformers.html#scaled_dot_product_attention)[](#coremltools.converters.mil.mil.ops.defs.iOS18.transformers.scaled_dot_product_attention "Link to this definition")

:   Source: [PyTorch scaled dot product attention](https://pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html). Computes the scaled dot product attention on query, key, and value tensors, using an optional attention mask if passed. In PyTorch, this is equivalent to:

    :::: 
    ::: highlight
        attn_mask = attn_mask.masked_fill(not attn_mask, -float('inf')) if attn_mask.dtype==torch.bool else attn_mask
        attn_weight = torch.softmax((Q @ K.transpose(-2, -1) / math.sqrt(Q.size(-1))) + attn_mask, dim=-1)
        return attn_weight @ V
    :::
    ::::

    Shape key:

    :   - [`B`] = Batch size

        - [`S`] = Source sequence length

        - [`L`] = Target sequence length

        - [`E`] = Query/Key embedding dimension

        - [`EV`] = Value embedding dimension

    Numerical values can differ due to floating point fusion/accumulation between backends. Note: We currently do not support the [`dropout_p`] and [`is_causal`].

    Mask can either be bool or float matching query, key, or value. For bool, it indicates whether the element should take part in the attention. Floats are added to the attention score. Mask shape must be broadcastable to [`[B,`]` `[`\*?,`]` `[`L,`]` `[`S]`].

    Parameters[:]

    :   

        **query: tensor\<\[B, \*?, L, E\], T\> (Required)**

        :   

        **key: tensor\<\[B, \*?, S, E\], T\> (Required)**

        :   

        **value: tensor\<\[B, \*?, S, EV\], T\> (Required)**

        :   

        **attn_mask: tensor\<\[\*?, S\], M\> (Optional)**

        :   

    Attributes[:]

    :   

        **T: fp16, fp32**

        :   

        **M: bool, fp16, fp32**

        :   

    Returns[:]

    :   

        tensor\<\[B, \*?, L, EV\], T\>

        :