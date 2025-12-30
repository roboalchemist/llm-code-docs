# Source: https://ml-explore.github.io/mlx/build/html/cpp/ops.html

[]

[[ ]](https://github.com/ml-explore/mlx "Source repository")

- [[ ] [.rst]](../_sources/cpp/ops.rst "Download source file")
- [ ] [.pdf]

[ ]

[]

# Operations

## Contents

- [[`arange()`]](#_CPPv46arangeddd5Dtype14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangeddd14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangedd5Dtype14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangedd14StreamOrDevice)
- [[`arange()`]](#_CPPv46aranged5Dtype14StreamOrDevice)
- [[`arange()`]](#_CPPv46aranged14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangeiii14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangeii14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangei14StreamOrDevice)
- [[`linspace()`]](#_CPPv48linspaceddi5Dtype14StreamOrDevice)
- [[`astype()`]](#_CPPv46astype5array5Dtype14StreamOrDevice)
- [[`as_strided()`]](#_CPPv410as_strided5array5Shape7Strides6size_t14StreamOrDevice)
- [[`copy()`]](#_CPPv44copy5array14StreamOrDevice)
- [[`full()`]](#_CPPv44full5Shape5array5Dtype14StreamOrDevice)
- [[`full()`]](#_CPPv44full5Shape5array14StreamOrDevice)
- [[`full()`]](#_CPPv4I0E4full5array5Shape1T5Dtype14StreamOrDevice)
- [[`full()`]](#_CPPv4I0E4full5array5Shape1T14StreamOrDevice)
- [[`full_like()`]](#_CPPv49full_likeRK5array5array5Dtype14StreamOrDevice)
- [[`full_like()`]](#_CPPv49full_likeRK5array5array14StreamOrDevice)
- [[`full_like()`]](#_CPPv4I0E9full_like5arrayRK5array1T5Dtype14StreamOrDevice)
- [[`full_like()`]](#_CPPv4I0E9full_like5arrayRK5array1T14StreamOrDevice)
- [[`zeros()`]](#_CPPv45zerosRK5Shape5Dtype14StreamOrDevice)
- [[`zeros()`]](#_CPPv45zerosRK5Shape14StreamOrDevice)
- [[`zeros_like()`]](#_CPPv410zeros_likeRK5array14StreamOrDevice)
- [[`ones()`]](#_CPPv44onesRK5Shape5Dtype14StreamOrDevice)
- [[`ones()`]](#_CPPv44onesRK5Shape14StreamOrDevice)
- [[`ones_like()`]](#_CPPv49ones_likeRK5array14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyeiii5Dtype14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyei5Dtype14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyeii14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyeiii14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyei14StreamOrDevice)
- [[`identity()`]](#_CPPv48identityi5Dtype14StreamOrDevice)
- [[`identity()`]](#_CPPv48identityi14StreamOrDevice)
- [[`tri()`]](#_CPPv43triiii5Dtype14StreamOrDevice)
- [[`tri()`]](#_CPPv43trii5Dtype14StreamOrDevice)
- [[`tril()`]](#_CPPv44tril5arrayi14StreamOrDevice)
- [[`triu()`]](#_CPPv44triu5arrayi14StreamOrDevice)
- [[`reshape()`]](#_CPPv47reshapeRK5array5Shape14StreamOrDevice)
- [[`unflatten()`]](#_CPPv49unflattenRK5arrayi5Shape14StreamOrDevice)
- [[`flatten()`]](#_CPPv47flattenRK5arrayii14StreamOrDevice)
- [[`flatten()`]](#_CPPv47flattenRK5array14StreamOrDevice)
- [[`hadamard_transform()`]](#_CPPv418hadamard_transformRK5arrayNSt8optionalIfEE14StreamOrDevice)
- [[`squeeze()`]](#_CPPv47squeezeRK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`squeeze()`]](#_CPPv47squeezeRK5arrayi14StreamOrDevice)
- [[`squeeze()`]](#_CPPv47squeezeRK5array14StreamOrDevice)
- [[`expand_dims()`]](#_CPPv411expand_dimsRK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`expand_dims()`]](#_CPPv411expand_dimsRK5arrayi14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5array5Shape5Shape5Shape14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5arrayNSt16initializer_listIiEE5Shape5Shape14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5array5Shape5Shape14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5arrayRK5arrayNSt6vectorIiEE5Shape14StreamOrDevice)
- [[`slice_update()`]](#_CPPv412slice_updateRK5arrayRK5array5Shape5Shape5Shape14StreamOrDevice)
- [[`slice_update()`]](#_CPPv412slice_updateRK5arrayRK5array5Shape5Shape14StreamOrDevice)
- [[`slice_update()`]](#_CPPv412slice_updateRK5arrayRK5arrayRK5arrayNSt6vectorIiEE14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayii14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayi14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayRK5Shapei14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayRK5Shape14StreamOrDevice)
- [[`meshgrid()`]](#_CPPv48meshgridRKNSt6vectorI5arrayEEbRKNSt6stringE14StreamOrDevice)
- [[`clip()`]](#_CPPv44clipRK5arrayRKNSt8optionalI5arrayEERKNSt8optionalI5arrayEE14StreamOrDevice)
- [[`concatenate()`]](#_CPPv411concatenateNSt6vectorI5arrayEEi14StreamOrDevice)
- [[`concatenate()`]](#_CPPv411concatenateNSt6vectorI5arrayEE14StreamOrDevice)
- [[`stack()`]](#_CPPv45stackRKNSt6vectorI5arrayEEi14StreamOrDevice)
- [[`stack()`]](#_CPPv45stackRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`repeat()`]](#_CPPv46repeatRK5arrayii14StreamOrDevice)
- [[`repeat()`]](#_CPPv46repeatRK5arrayi14StreamOrDevice)
- [[`tile()`]](#_CPPv44tileRK5arrayNSt6vectorIiEE14StreamOrDevice)
- [[`transpose()`]](#_CPPv49transposeRK5arrayNSt6vectorIiEE14StreamOrDevice)
- [[`transpose()`]](#_CPPv49transposeRK5arrayNSt16initializer_listIiEE14StreamOrDevice)
- [[`swapaxes()`]](#_CPPv48swapaxesRK5arrayii14StreamOrDevice)
- [[`moveaxis()`]](#_CPPv48moveaxisRK5arrayii14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayRKNSt6vectorIiEERK5ShapeRK5ShapeRK5arrayRKNSt6stringE14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayRKNSt6vectorINSt4pairIiiEEEERK5arrayRKNSt6stringE14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayRKNSt4pairIiiEERK5arrayRKNSt6stringE14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayiRK5arrayRKNSt6stringE14StreamOrDevice)
- [[`transpose()`]](#_CPPv49transposeRK5array14StreamOrDevice)
- [[`broadcast_to()`]](#_CPPv412broadcast_toRK5arrayRK5Shape14StreamOrDevice)
- [[`broadcast_arrays()`]](#_CPPv416broadcast_arraysRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`equal()`]](#_CPPv45equalRK5arrayRK5array14StreamOrDevice)
- [[`operator==()`]](#_CPPv4eqRK5arrayRK5array)
- [[`operator==()`]](#_CPPv4I0Eeq5array1TRK5array)
- [[`operator==()`]](#_CPPv4I0Eeq5arrayRK5array1T)
- [[`not_equal()`]](#_CPPv49not_equalRK5arrayRK5array14StreamOrDevice)
- [[`operator!=()`]](#_CPPv4neRK5arrayRK5array)
- [[`operator!=()`]](#_CPPv4I0Ene5array1TRK5array)
- [[`operator!=()`]](#_CPPv4I0Ene5arrayRK5array1T)
- [[`greater()`]](#_CPPv47greaterRK5arrayRK5array14StreamOrDevice)
- [[`operator>()`]](#_CPPv4gtRK5arrayRK5array)
- [[`operator>()`]](#_CPPv4I0Egt5array1TRK5array)
- [[`operator>()`]](#_CPPv4I0Egt5arrayRK5array1T)
- [[`greater_equal()`]](#_CPPv413greater_equalRK5arrayRK5array14StreamOrDevice)
- [[`operator>=()`]](#_CPPv4geRK5arrayRK5array)
- [[`operator>=()`]](#_CPPv4I0Ege5array1TRK5array)
- [[`operator>=()`]](#_CPPv4I0Ege5arrayRK5array1T)
- [[`less()`]](#_CPPv44lessRK5arrayRK5array14StreamOrDevice)
- [[`operator<()`]](#_CPPv4ltRK5arrayRK5array)
- [[`operator<()`]](#_CPPv4I0Elt5array1TRK5array)
- [[`operator<()`]](#_CPPv4I0Elt5arrayRK5array1T)
- [[`less_equal()`]](#_CPPv410less_equalRK5arrayRK5array14StreamOrDevice)
- [[`operator<=()`]](#_CPPv4leRK5arrayRK5array)
- [[`operator<=()`]](#_CPPv4I0Ele5array1TRK5array)
- [[`operator<=()`]](#_CPPv4I0Ele5arrayRK5array1T)
- [[`array_equal()`]](#_CPPv411array_equalRK5arrayRK5arrayb14StreamOrDevice)
- [[`array_equal()`]](#_CPPv411array_equalRK5arrayRK5array14StreamOrDevice)
- [[`isnan()`]](#_CPPv45isnanRK5array14StreamOrDevice)
- [[`isinf()`]](#_CPPv45isinfRK5array14StreamOrDevice)
- [[`isfinite()`]](#_CPPv48isfiniteRK5array14StreamOrDevice)
- [[`isposinf()`]](#_CPPv48isposinfRK5array14StreamOrDevice)
- [[`isneginf()`]](#_CPPv48isneginfRK5array14StreamOrDevice)
- [[`where()`]](#_CPPv45whereRK5arrayRK5arrayRK5array14StreamOrDevice)
- [[`nan_to_num()`]](#_CPPv410nan_to_numRK5arrayfKNSt8optionalIfEEKNSt8optionalIfEE14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5arrayb14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5array14StreamOrDevice)
- [[`allclose()`]](#_CPPv48allcloseRK5arrayRK5arrayddb14StreamOrDevice)
- [[`isclose()`]](#_CPPv47iscloseRK5arrayRK5arrayddb14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5arrayib14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5arrayb14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5array14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5arrayib14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5arrayb14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5array14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5arrayib14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5arrayb14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5array14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5arrayib14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5arrayb14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5array14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5arrayib14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5arraybi14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5array14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5arrayibi14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5arraybi14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5array14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5arrayibi14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5arrayb14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5array14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5arrayib14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5arrayb14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5array14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5arrayib14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5arrayb14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5array14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5arrayib14StreamOrDevice)
- [[`argmin()`]](#_CPPv46argminRK5arrayb14StreamOrDevice)
- [[`argmin()`]](#_CPPv46argminRK5array14StreamOrDevice)
- [[`argmin()`]](#_CPPv46argminRK5arrayib14StreamOrDevice)
- [[`argmax()`]](#_CPPv46argmaxRK5arrayb14StreamOrDevice)
- [[`argmax()`]](#_CPPv46argmaxRK5array14StreamOrDevice)
- [[`argmax()`]](#_CPPv46argmaxRK5arrayib14StreamOrDevice)
- [[`sort()`]](#_CPPv44sortRK5array14StreamOrDevice)
- [[`sort()`]](#_CPPv44sortRK5arrayi14StreamOrDevice)
- [[`argsort()`]](#_CPPv47argsortRK5array14StreamOrDevice)
- [[`argsort()`]](#_CPPv47argsortRK5arrayi14StreamOrDevice)
- [[`partition()`]](#_CPPv49partitionRK5arrayi14StreamOrDevice)
- [[`partition()`]](#_CPPv49partitionRK5arrayii14StreamOrDevice)
- [[`argpartition()`]](#_CPPv412argpartitionRK5arrayi14StreamOrDevice)
- [[`argpartition()`]](#_CPPv412argpartitionRK5arrayii14StreamOrDevice)
- [[`topk()`]](#_CPPv44topkRK5arrayi14StreamOrDevice)
- [[`topk()`]](#_CPPv44topkRK5arrayii14StreamOrDevice)
- [[`logcumsumexp()`]](#_CPPv412logcumsumexpRK5arraybb14StreamOrDevice)
- [[`logcumsumexp()`]](#_CPPv412logcumsumexpRK5arrayibb14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5arrayb14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5array14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5arrayib14StreamOrDevice)
- [[`abs()`]](#_CPPv43absRK5array14StreamOrDevice)
- [[`negative()`]](#_CPPv48negativeRK5array14StreamOrDevice)
- [[`operator-()`]](#_CPPv4miRK5array)
- [[`sign()`]](#_CPPv44signRK5array14StreamOrDevice)
- [[`logical_not()`]](#_CPPv411logical_notRK5array14StreamOrDevice)
- [[`logical_and()`]](#_CPPv411logical_andRK5arrayRK5array14StreamOrDevice)
- [[`operator&&()`]](#_CPPv4aaRK5arrayRK5array)
- [[`logical_or()`]](#_CPPv410logical_orRK5arrayRK5array14StreamOrDevice)
- [[`operator||()`]](#_CPPv4ooRK5arrayRK5array)
- [[`reciprocal()`]](#_CPPv410reciprocalRK5array14StreamOrDevice)
- [[`add()`]](#_CPPv43addRK5arrayRK5array14StreamOrDevice)
- [[`operator+()`]](#_CPPv4plRK5arrayRK5array)
- [[`operator+()`]](#_CPPv4I0Epl5array1TRK5array)
- [[`operator+()`]](#_CPPv4I0Epl5arrayRK5array1T)
- [[`subtract()`]](#_CPPv48subtractRK5arrayRK5array14StreamOrDevice)
- [[`operator-()`]](#_CPPv4miRK5arrayRK5array)
- [[`operator-()`]](#_CPPv4I0Emi5array1TRK5array)
- [[`operator-()`]](#_CPPv4I0Emi5arrayRK5array1T)
- [[`multiply()`]](#_CPPv48multiplyRK5arrayRK5array14StreamOrDevice)
- [[`operator*()`]](#_CPPv4mlRK5arrayRK5array)
- [[`operator*()`]](#_CPPv4I0Eml5array1TRK5array)
- [[`operator*()`]](#_CPPv4I0Eml5arrayRK5array1T)
- [[`divide()`]](#_CPPv46divideRK5arrayRK5array14StreamOrDevice)
- [[`operator/()`]](#_CPPv4dvRK5arrayRK5array)
- [[`operator/()`]](#_CPPv4dvdRK5array)
- [[`operator/()`]](#_CPPv4dvRK5arrayd)
- [[`divmod()`]](#_CPPv46divmodRK5arrayRK5array14StreamOrDevice)
- [[`floor_divide()`]](#_CPPv412floor_divideRK5arrayRK5array14StreamOrDevice)
- [[`remainder()`]](#_CPPv49remainderRK5arrayRK5array14StreamOrDevice)
- [[`operator%()`]](#_CPPv4rmRK5arrayRK5array)
- [[`operator%()`]](#_CPPv4I0Erm5array1TRK5array)
- [[`operator%()`]](#_CPPv4I0Erm5arrayRK5array1T)
- [[`maximum()`]](#_CPPv47maximumRK5arrayRK5array14StreamOrDevice)
- [[`minimum()`]](#_CPPv47minimumRK5arrayRK5array14StreamOrDevice)
- [[`floor()`]](#_CPPv45floorRK5array14StreamOrDevice)
- [[`ceil()`]](#_CPPv44ceilRK5array14StreamOrDevice)
- [[`square()`]](#_CPPv46squareRK5array14StreamOrDevice)
- [[`exp()`]](#_CPPv43expRK5array14StreamOrDevice)
- [[`sin()`]](#_CPPv43sinRK5array14StreamOrDevice)
- [[`cos()`]](#_CPPv43cosRK5array14StreamOrDevice)
- [[`tan()`]](#_CPPv43tanRK5array14StreamOrDevice)
- [[`arcsin()`]](#_CPPv46arcsinRK5array14StreamOrDevice)
- [[`arccos()`]](#_CPPv46arccosRK5array14StreamOrDevice)
- [[`arctan()`]](#_CPPv46arctanRK5array14StreamOrDevice)
- [[`arctan2()`]](#_CPPv47arctan2RK5arrayRK5array14StreamOrDevice)
- [[`sinh()`]](#_CPPv44sinhRK5array14StreamOrDevice)
- [[`cosh()`]](#_CPPv44coshRK5array14StreamOrDevice)
- [[`tanh()`]](#_CPPv44tanhRK5array14StreamOrDevice)
- [[`arcsinh()`]](#_CPPv47arcsinhRK5array14StreamOrDevice)
- [[`arccosh()`]](#_CPPv47arccoshRK5array14StreamOrDevice)
- [[`arctanh()`]](#_CPPv47arctanhRK5array14StreamOrDevice)
- [[`degrees()`]](#_CPPv47degreesRK5array14StreamOrDevice)
- [[`radians()`]](#_CPPv47radiansRK5array14StreamOrDevice)
- [[`log()`]](#_CPPv43logRK5array14StreamOrDevice)
- [[`log2()`]](#_CPPv44log2RK5array14StreamOrDevice)
- [[`log10()`]](#_CPPv45log10RK5array14StreamOrDevice)
- [[`log1p()`]](#_CPPv45log1pRK5array14StreamOrDevice)
- [[`logaddexp()`]](#_CPPv49logaddexpRK5arrayRK5array14StreamOrDevice)
- [[`sigmoid()`]](#_CPPv47sigmoidRK5array14StreamOrDevice)
- [[`erf()`]](#_CPPv43erfRK5array14StreamOrDevice)
- [[`erfinv()`]](#_CPPv46erfinvRK5array14StreamOrDevice)
- [[`expm1()`]](#_CPPv45expm1RK5array14StreamOrDevice)
- [[`stop_gradient()`]](#_CPPv413stop_gradientRK5array14StreamOrDevice)
- [[`round()`]](#_CPPv45roundRK5arrayi14StreamOrDevice)
- [[`round()`]](#_CPPv45roundRK5array14StreamOrDevice)
- [[`matmul()`]](#_CPPv46matmulRK5arrayRK5array14StreamOrDevice)
- [[`gather()`]](#_CPPv46gatherRK5arrayRKNSt6vectorI5arrayEERKNSt6vectorIiEERK5Shape14StreamOrDevice)
- [[`gather()`]](#_CPPv46gatherRK5arrayRK5arrayiRK5Shape14StreamOrDevice)
- [[`kron()`]](#_CPPv44kronRK5arrayRK5array14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayRK5arrayi14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayii14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayRK5array14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayi14StreamOrDevice)
- [[`take_along_axis()`]](#_CPPv415take_along_axisRK5arrayRK5arrayi14StreamOrDevice)
- [[`put_along_axis()`]](#_CPPv414put_along_axisRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_add_axis()`]](#_CPPv416scatter_add_axisRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter()`]](#_CPPv47scatterRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter()`]](#_CPPv47scatterRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_add()`]](#_CPPv411scatter_addRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_add()`]](#_CPPv411scatter_addRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_prod()`]](#_CPPv412scatter_prodRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_prod()`]](#_CPPv412scatter_prodRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_max()`]](#_CPPv411scatter_maxRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_max()`]](#_CPPv411scatter_maxRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_min()`]](#_CPPv411scatter_minRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_min()`]](#_CPPv411scatter_minRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`masked_scatter()`]](#_CPPv414masked_scatterRK5arrayRK5arrayRK5array14StreamOrDevice)
- [[`sqrt()`]](#_CPPv44sqrtRK5array14StreamOrDevice)
- [[`rsqrt()`]](#_CPPv45rsqrtRK5array14StreamOrDevice)
- [[`softmax()`]](#_CPPv47softmaxRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`softmax()`]](#_CPPv47softmaxRK5arrayb14StreamOrDevice)
- [[`softmax()`]](#_CPPv47softmaxRK5arrayib14StreamOrDevice)
- [[`power()`]](#_CPPv45powerRK5arrayRK5array14StreamOrDevice)
- [[`cumsum()`]](#_CPPv46cumsumRK5arraybb14StreamOrDevice)
- [[`cumsum()`]](#_CPPv46cumsumRK5arrayibb14StreamOrDevice)
- [[`cumprod()`]](#_CPPv47cumprodRK5arraybb14StreamOrDevice)
- [[`cumprod()`]](#_CPPv47cumprodRK5arrayibb14StreamOrDevice)
- [[`cummax()`]](#_CPPv46cummaxRK5arraybb14StreamOrDevice)
- [[`cummax()`]](#_CPPv46cummaxRK5arrayibb14StreamOrDevice)
- [[`cummin()`]](#_CPPv46cumminRK5arraybb14StreamOrDevice)
- [[`cummin()`]](#_CPPv46cumminRK5arrayibb14StreamOrDevice)
- [[`conv_general()`]](#_CPPv412conv_general5array5arrayNSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEEib14StreamOrDevice)
- [[`conv_general()`]](#_CPPv412conv_generalRK5arrayRK5arrayNSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEEib14StreamOrDevice)
- [[`conv1d()`]](#_CPPv46conv1dRK5arrayRK5arrayiiii14StreamOrDevice)
- [[`conv2d()`]](#_CPPv46conv2dRK5arrayRK5arrayRKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEEi14StreamOrDevice)
- [[`conv3d()`]](#_CPPv46conv3dRK5arrayRK5arrayRKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEEi14StreamOrDevice)
- [[`conv_transpose1d()`]](#_CPPv416conv_transpose1dRK5arrayRK5arrayiiiii14StreamOrDevice)
- [[`conv_transpose2d()`]](#_CPPv416conv_transpose2dRK5arrayRK5arrayRKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEEi14StreamOrDevice)
- [[`conv_transpose3d()`]](#_CPPv416conv_transpose3dRK5arrayRK5arrayRKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEEi14StreamOrDevice)
- [[`quantized_matmul()`]](#_CPPv416quantized_matmul5array5array5arrayNSt8optionalI5arrayEEbNSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice)
- [[`quantize()`]](#_CPPv48quantizeRK5arrayNSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice)
- [[`dequantize()`]](#_CPPv410dequantizeRK5arrayRK5arrayRKNSt8optionalI5arrayEENSt8optionalIiEENSt8optionalIiEERKNSt6stringENSt8optionalI5DtypeEE14StreamOrDevice)
- [[`qqmm()`]](#_CPPv44qqmm5array5arrayNSt8optionalI5arrayEENSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice)
- [[`from_fp8()`]](#_CPPv48from_fp85array5Dtype14StreamOrDevice)
- [[`to_fp8()`]](#_CPPv46to_fp85array14StreamOrDevice)
- [[`gather_qmm()`]](#_CPPv410gather_qmmRK5arrayRK5arrayRK5arrayRKNSt8optionalI5arrayEENSt8optionalI5arrayEENSt8optionalI5arrayEEbNSt8optionalIiEENSt8optionalIiEERKNSt6stringEb14StreamOrDevice)
- [[`tensordot()`]](#_CPPv49tensordotRK5arrayRK5arrayKi14StreamOrDevice)
- [[`tensordot()`]](#_CPPv49tensordotRK5arrayRK5arrayRKNSt6vectorIiEERKNSt6vectorIiEE14StreamOrDevice)
- [[`outer()`]](#_CPPv45outerRK5arrayRK5array14StreamOrDevice)
- [[`inner()`]](#_CPPv45innerRK5arrayRK5array14StreamOrDevice)
- [[`addmm()`]](#_CPPv45addmm5array5array5arrayRKfRKf14StreamOrDevice)
- [[`block_masked_mm()`]](#_CPPv415block_masked_mm5array5arrayiNSt8optionalI5arrayEENSt8optionalI5arrayEENSt8optionalI5arrayEE14StreamOrDevice)
- [[`gather_mm()`]](#_CPPv49gather_mm5array5arrayNSt8optionalI5arrayEENSt8optionalI5arrayEEb14StreamOrDevice)
- [[`segmented_mm()`]](#_CPPv412segmented_mm5array5array5array14StreamOrDevice)
- [[`diagonal()`]](#_CPPv48diagonalRK5arrayiii14StreamOrDevice)
- [[`diag()`]](#_CPPv44diagRK5arrayi14StreamOrDevice)
- [[`trace()`]](#_CPPv45traceRK5arrayiii5Dtype14StreamOrDevice)
- [[`trace()`]](#_CPPv45traceRK5arrayiii14StreamOrDevice)
- [[`trace()`]](#_CPPv45traceRK5array14StreamOrDevice)
- [[`depends()`]](#_CPPv47dependsRKNSt6vectorI5arrayEERKNSt6vectorI5arrayEE)
- [[`atleast_1d()`]](#_CPPv410atleast_1dRK5array14StreamOrDevice)
- [[`atleast_1d()`]](#_CPPv410atleast_1dRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`atleast_2d()`]](#_CPPv410atleast_2dRK5array14StreamOrDevice)
- [[`atleast_2d()`]](#_CPPv410atleast_2dRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`atleast_3d()`]](#_CPPv410atleast_3dRK5array14StreamOrDevice)
- [[`atleast_3d()`]](#_CPPv410atleast_3dRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`number_of_elements()`]](#_CPPv418number_of_elementsRK5arrayNSt6vectorIiEEb5Dtype14StreamOrDevice)
- [[`conjugate()`]](#_CPPv49conjugateRK5array14StreamOrDevice)
- [[`bitwise_and()`]](#_CPPv411bitwise_andRK5arrayRK5array14StreamOrDevice)
- [[`operator&()`]](#_CPPv4anRK5arrayRK5array)
- [[`bitwise_or()`]](#_CPPv410bitwise_orRK5arrayRK5array14StreamOrDevice)
- [[`operator|()`]](#_CPPv4orRK5arrayRK5array)
- [[`bitwise_xor()`]](#_CPPv411bitwise_xorRK5arrayRK5array14StreamOrDevice)
- [[`operator^()`]](#_CPPv4eoRK5arrayRK5array)
- [[`left_shift()`]](#_CPPv410left_shiftRK5arrayRK5array14StreamOrDevice)
- [[`operator<<()`]](#_CPPv4lsRK5arrayRK5array)
- [[`right_shift()`]](#_CPPv411right_shiftRK5arrayRK5array14StreamOrDevice)
- [[`operator>>()`]](#_CPPv4rsRK5arrayRK5array)
- [[`bitwise_invert()`]](#_CPPv414bitwise_invertRK5array14StreamOrDevice)
- [[`operator~()`]](#_CPPv4coRK5array)
- [[`view()`]](#_CPPv44viewRK5arrayRK5Dtype14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayi14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayRK5Shape14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayii14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayiRKNSt6vectorIiEE14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayRK5Shapei14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayRK5ShapeRKNSt6vectorIiEE14StreamOrDevice)
- [[`real()`]](#_CPPv44realRK5array14StreamOrDevice)
- [[`imag()`]](#_CPPv44imagRK5array14StreamOrDevice)
- [[`contiguous()`]](#_CPPv410contiguousRK5arrayb14StreamOrDevice)

[]

# Operations[\#](#operations "Link to this heading")

[][][][][[array]][ ][[[arange]]][(][[double]][ ][[start]], [[double]][ ][[stop]], [[double]][ ][[step]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arangeddd5Dtype14StreamOrDevice "Link to this definition")\

:   A 1D array of numbers starting at [`start`] (optional), stopping at stop, stepping by [`step`] (optional).

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[double]][ ][[start]], [[double]][ ][[stop]], [[double]][ ][[step]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arangeddd14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[double]][ ][[start]], [[double]][ ][[stop]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arangedd5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[double]][ ][[start]], [[double]][ ][[stop]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arangedd14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[double]][ ][[stop]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46aranged5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[double]][ ][[stop]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46aranged14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[int]][ ][[start]], [[int]][ ][[stop]], [[int]][ ][[step]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arangeiii14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[int]][ ][[start]], [[int]][ ][[stop]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arangeii14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[arange]]][(][[int]][ ][[stop]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arangei14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[linspace]]][(][[double]][ ][[start]], [[double]][ ][[stop]], [[int]][ ][[num]][ ][[=]][ ][[50]], [[Dtype]][ ][[dtype]][ ][[=]][ ][[float32]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48linspaceddi5Dtype14StreamOrDevice "Link to this definition")\

:   A 1D array of [`num`] evenly spaced numbers in the range [`[start,`]` `[`stop]`]

<!-- -->

[][][][][[array]][ ][[[astype]]][(][[array]][ ][[a]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46astype5array5Dtype14StreamOrDevice "Link to this definition")\

:   Convert an array to the given data type.

<!-- -->

[][][][][[array]][ ][[[as_strided]]][(][[array]][ ][[a]], [[Shape]][ ][[shape]], [[Strides]][ ][[strides]], [[size_t]][ ][[offset]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410as_strided5array5Shape7Strides6size_t14StreamOrDevice "Link to this definition")\

:   Create a view of an array with the given shape and strides.

<!-- -->

[][][][][[array]][ ][[[copy]]][(][[array]][ ][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44copy5array14StreamOrDevice "Link to this definition")\

:   Copy another array.

<!-- -->

[][][][][[array]][ ][[[full]]][(][[Shape]][ ][[shape]], [[array]][ ][[vals]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44full5Shape5array5Dtype14StreamOrDevice "Link to this definition")\

:   Fill an array of the given shape with the given value(s).

<!-- -->

[][][][][[array]][ ][[[full]]][(][[Shape]][ ][[shape]], [[array]][ ][[vals]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44full5Shape5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[full]]][(][[Shape]][ ][[shape]], [[[T]]](#_CPPv4I0E4full5array5Shape1T5Dtype14StreamOrDevice "full::T")[ ][[val]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4I0E4full5array5Shape1T5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[full]]][(][[Shape]][ ][[shape]], [[[T]]](#_CPPv4I0E4full5array5Shape1T14StreamOrDevice "full::T")[ ][[val]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4I0E4full5array5Shape1T14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[full_like]]][(][[const]][ ][[array]][ ][[&]][[a]], [[array]][ ][[vals]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49full_likeRK5array5array5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[full_like]]][(][[const]][ ][[array]][ ][[&]][[a]], [[array]][ ][[vals]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49full_likeRK5array5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[full_like]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0E9full_like5arrayRK5array1T5Dtype14StreamOrDevice "full_like::T")[ ][[val]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4I0E9full_like5arrayRK5array1T5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[full_like]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0E9full_like5arrayRK5array1T14StreamOrDevice "full_like::T")[ ][[val]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4I0E9full_like5arrayRK5array1T14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[zeros]]][(][[const]][ ][[Shape]][ ][[&]][[shape]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45zerosRK5Shape5Dtype14StreamOrDevice "Link to this definition")\

:   Fill an array of the given shape with zeros.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[zeros]]][(][[const]][ ][[Shape]][ ][[&]][[shape]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45zerosRK5Shape14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[zeros_like]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410zeros_likeRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[ones]]][(][[const]][ ][[Shape]][ ][[&]][[shape]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44onesRK5Shape5Dtype14StreamOrDevice "Link to this definition")\

:   Fill an array of the given shape with ones.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[ones]]][(][[const]][ ][[Shape]][ ][[&]][[shape]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44onesRK5Shape14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[ones_like]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49ones_likeRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[eye]]][(][[int]][ ][[n]], [[int]][ ][[m]], [[int]][ ][[k]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43eyeiii5Dtype14StreamOrDevice "Link to this definition")\

:   Fill an array of the given shape (n,m) with ones in the specified diagonal k, and zeros everywhere else.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[eye]]][(][[int]][ ][[n]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43eyei5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[eye]]][(][[int]][ ][[n]], [[int]][ ][[m]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43eyeii14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[eye]]][(][[int]][ ][[n]], [[int]][ ][[m]], [[int]][ ][[k]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43eyeiii14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[eye]]][(][[int]][ ][[n]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43eyei14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[identity]]][(][[int]][ ][[n]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48identityi5Dtype14StreamOrDevice "Link to this definition")\

:   Create a square matrix of shape (n,n) of zeros, and ones in the major diagonal.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[identity]]][(][[int]][ ][[n]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48identityi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[tri]]][(][[int]][ ][[n]], [[int]][ ][[m]], [[int]][ ][[k]], [[Dtype]][ ][[type]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43triiii5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[tri]]][(][[int]][ ][[n]], [[Dtype]][ ][[type]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43trii5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[tril]]][(][[array]][ ][[x]], [[int]][ ][[k]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44tril5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[triu]]][(][[array]][ ][[x]], [[int]][ ][[k]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44triu5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[reshape]]][(][[const]][ ][[array]][ ][[&]][[a]], [[Shape]][ ][[shape]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47reshapeRK5array5Shape14StreamOrDevice "Link to this definition")\

:   Reshape an array to the given shape.

<!-- -->

[][][][][[array]][ ][[[unflatten]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[Shape]][ ][[shape]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49unflattenRK5arrayi5Shape14StreamOrDevice "Link to this definition")\

:   Unflatten the axis to the given shape.

<!-- -->

[][][][][[array]][ ][[[flatten]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[start_axis]], [[int]][ ][[end_axis]][ ][[=]][ ][[-]][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47flattenRK5arrayii14StreamOrDevice "Link to this definition")\

:   Flatten the dimensions in the range [`[start_axis,`]` `[`end_axis]`] .

<!-- -->

[][][][][[array]][ ][[[flatten]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47flattenRK5array14StreamOrDevice "Link to this definition")\

:   Flatten the array to 1D.

<!-- -->

[][][][][[array]][ ][[[hadamard_transform]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[float]][[\>]][ ][[scale]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv418hadamard_transformRK5arrayNSt8optionalIfEE14StreamOrDevice "Link to this definition")\

:   Multiply the array by the Hadamard matrix of corresponding size.

<!-- -->

[][][][][[array]][ ][[[squeeze]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47squeezeRK5arrayRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Remove singleton dimensions at the given axes.

<!-- -->

[][][][][[array]][ ][[[squeeze]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47squeezeRK5arrayi14StreamOrDevice "Link to this definition")\

:   Remove singleton dimensions at the given axis.

<!-- -->

[][][][][[array]][ ][[[squeeze]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47squeezeRK5array14StreamOrDevice "Link to this definition")\

:   Remove all singleton dimensions.

<!-- -->

[][][][][[array]][ ][[[expand_dims]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411expand_dimsRK5arrayRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Add a singleton dimension at the given axes.

<!-- -->

[][][][][[array]][ ][[[expand_dims]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411expand_dimsRK5arrayi14StreamOrDevice "Link to this definition")\

:   Add a singleton dimension at the given axis.

<!-- -->

[][][][][[array]][ ][[[slice]]][(][[const]][ ][[array]][ ][[&]][[a]], [[Shape]][ ][[start]], [[Shape]][ ][[stop]], [[Shape]][ ][[strides]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45sliceRK5array5Shape5Shape5Shape14StreamOrDevice "Link to this definition")\

:   Slice an array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[slice]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[initializer_list]][[\<]][[int]][[\>]][ ][[start]], [[Shape]][ ][[stop]], [[Shape]][ ][[strides]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45sliceRK5arrayNSt16initializer_listIiEE5Shape5Shape14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[slice]]][(][[const]][ ][[array]][ ][[&]][[a]], [[Shape]][ ][[start]], [[Shape]][ ][[stop]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45sliceRK5array5Shape5Shape14StreamOrDevice "Link to this definition")\

:   Slice an array with a stride of 1 in each dimension.

<!-- -->

[][][][][[array]][ ][[[slice]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[start]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[axes]], [[Shape]][ ][[slice_size]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45sliceRK5arrayRK5arrayNSt6vectorIiEE5Shape14StreamOrDevice "Link to this definition")\

:   Slice an array with dynamic starting indices.

<!-- -->

[][][][][[array]][ ][[[slice_update]]][(][[const]][ ][[array]][ ][[&]][[src]], [[const]][ ][[array]][ ][[&]][[update]], [[Shape]][ ][[start]], [[Shape]][ ][[stop]], [[Shape]][ ][[strides]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412slice_updateRK5arrayRK5array5Shape5Shape5Shape14StreamOrDevice "Link to this definition")\

:   Update a slice from the source array.

<!-- -->

[][][][][[array]][ ][[[slice_update]]][(][[const]][ ][[array]][ ][[&]][[src]], [[const]][ ][[array]][ ][[&]][[update]], [[Shape]][ ][[start]], [[Shape]][ ][[stop]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412slice_updateRK5arrayRK5array5Shape5Shape14StreamOrDevice "Link to this definition")\

:   Update a slice from the source array with stride 1 in each dimension.

<!-- -->

[][][][][[array]][ ][[[slice_update]]][(][[const]][ ][[array]][ ][[&]][[src]], [[const]][ ][[array]][ ][[&]][[update]], [[const]][ ][[array]][ ][[&]][[start]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412slice_updateRK5arrayRK5arrayRK5arrayNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Update a slice from the source array with dynamic starting indices.

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[split]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[num_splits]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45splitRK5arrayii14StreamOrDevice "Link to this definition")\

:   Split an array into sub-arrays along a given axis.

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[split]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[num_splits]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45splitRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[split]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[Shape]][ ][[&]][[indices]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45splitRK5arrayRK5Shapei14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[split]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[Shape]][ ][[&]][[indices]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45splitRK5arrayRK5Shape14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[meshgrid]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[arrays]], [[bool]][ ][[sparse]][ ][[=]][ ][[false]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[indexing]][ ][[=]][ ][[\"xy\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48meshgridRKNSt6vectorI5arrayEEbRKNSt6stringE14StreamOrDevice "Link to this definition")\

:   A vector of coordinate arrays from coordinate vectors.

<!-- -->

[][][][][[array]][ ][[[clip]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[&]][[a_min]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[&]][[a_max]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44clipRK5arrayRKNSt8optionalI5arrayEERKNSt8optionalI5arrayEE14StreamOrDevice "Link to this definition")\

:   Clip (limit) the values in an array.

<!-- -->

[][][][][[array]][ ][[[concatenate]]][(][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[arrays]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411concatenateNSt6vectorI5arrayEEi14StreamOrDevice "Link to this definition")\

:   Concatenate arrays along a given axis.

<!-- -->

[][][][][[array]][ ][[[concatenate]]][(][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[arrays]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411concatenateNSt6vectorI5arrayEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[stack]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[arrays]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45stackRKNSt6vectorI5arrayEEi14StreamOrDevice "Link to this definition")\

:   Stack arrays along a new axis.

<!-- -->

[][][][][[array]][ ][[[stack]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[arrays]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45stackRKNSt6vectorI5arrayEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[repeat]]][(][[const]][ ][[array]][ ][[&]][[arr]], [[int]][ ][[repeats]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46repeatRK5arrayii14StreamOrDevice "Link to this definition")\

:   Repeat an array along an axis.

<!-- -->

[][][][][[array]][ ][[[repeat]]][(][[const]][ ][[array]][ ][[&]][[arr]], [[int]][ ][[repeats]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46repeatRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[tile]]][(][[const]][ ][[array]][ ][[&]][[arr]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[reps]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44tileRK5arrayNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[transpose]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49transposeRK5arrayNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Permutes the dimensions according to the given axes.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[transpose]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[initializer_list]][[\<]][[int]][[\>]][ ][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49transposeRK5arrayNSt16initializer_listIiEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[swapaxes]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis1]], [[int]][ ][[axis2]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48swapaxesRK5arrayii14StreamOrDevice "Link to this definition")\

:   Swap two axes of an array.

<!-- -->

[][][][][[array]][ ][[[moveaxis]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[source]], [[int]][ ][[destination]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48moveaxisRK5arrayii14StreamOrDevice "Link to this definition")\

:   Move an axis of an array.

<!-- -->

[][][][][[array]][ ][[[pad]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[const]][ ][[Shape]][ ][[&]][[low_pad_size]], [[const]][ ][[Shape]][ ][[&]][[high_pad_size]], [[const]][ ][[array]][ ][[&]][[pad_value]][ ][[=]][ ][[array]][[(]][[0]][[)]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"constant\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43padRK5arrayRKNSt6vectorIiEERK5ShapeRK5ShapeRK5arrayRKNSt6stringE14StreamOrDevice "Link to this definition")\

:   Pad an array with a constant value.

<!-- -->

[][][][][[array]][ ][[[pad]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][[\>]][ ][[&]][[pad_width]], [[const]][ ][[array]][ ][[&]][[pad_value]][ ][[=]][ ][[array]][[(]][[0]][[)]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"constant\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43padRK5arrayRKNSt6vectorINSt4pairIiiEEEERK5arrayRKNSt6stringE14StreamOrDevice "Link to this definition")\

:   Pad an array with a constant value along all axes.

<!-- -->

[][][][][[array]][ ][[[pad]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[pad_width]], [[const]][ ][[array]][ ][[&]][[pad_value]][ ][[=]][ ][[array]][[(]][[0]][[)]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"constant\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43padRK5arrayRKNSt4pairIiiEERK5arrayRKNSt6stringE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[pad]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[pad_width]], [[const]][ ][[array]][ ][[&]][[pad_value]][ ][[=]][ ][[array]][[(]][[0]][[)]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"constant\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43padRK5arrayiRK5arrayRKNSt6stringE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[transpose]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49transposeRK5array14StreamOrDevice "Link to this definition")\

:   Permutes the dimensions in reverse order.

<!-- -->

[][][][][[array]][ ][[[broadcast_to]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[Shape]][ ][[&]][[shape]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412broadcast_toRK5arrayRK5Shape14StreamOrDevice "Link to this definition")\

:   Broadcast an array to a given shape.

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[broadcast_arrays]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[inputs]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv416broadcast_arraysRKNSt6vectorI5arrayEE14StreamOrDevice "Link to this definition")\

:   Broadcast a vector of arrays against one another.

<!-- -->

[][][][][[array]][ ][[[equal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45equalRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Returns the bool array with (a == b) element-wise.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[operator]][[==]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4eqRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[==]]][(][[[T]]](#_CPPv4I0Eeq5array1TRK5array "operator==::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Eeq5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[==]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Eeq5arrayRK5array1T "operator==::T")[ ][[b]][)][\#](#_CPPv4I0Eeq5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[not_equal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49not_equalRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Returns the bool array with (a != b) element-wise.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[operator]][[!=]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4neRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[!=]]][(][[[T]]](#_CPPv4I0Ene5array1TRK5array "operator!=::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Ene5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[!=]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Ene5arrayRK5array1T "operator!=::T")[ ][[b]][)][\#](#_CPPv4I0Ene5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[greater]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47greaterRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Returns bool array with (a \> b) element-wise.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[operator]][[\>]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4gtRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\>]]][(][[[T]]](#_CPPv4I0Egt5array1TRK5array "operator>::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Egt5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\>]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Egt5arrayRK5array1T "operator>::T")[ ][[b]][)][\#](#_CPPv4I0Egt5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[greater_equal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv413greater_equalRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Returns bool array with (a \>= b) element-wise.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[operator]][[\>=]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4geRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\>=]]][(][[[T]]](#_CPPv4I0Ege5array1TRK5array "operator>=::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Ege5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\>=]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Ege5arrayRK5array1T "operator>=::T")[ ][[b]][)][\#](#_CPPv4I0Ege5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[less]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44lessRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Returns bool array with (a \< b) element-wise.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[operator]][[\<]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4ltRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\<]]][(][[[T]]](#_CPPv4I0Elt5array1TRK5array "operator<::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Elt5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\<]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Elt5arrayRK5array1T "operator<::T")[ ][[b]][)][\#](#_CPPv4I0Elt5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[less_equal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410less_equalRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Returns bool array with (a \<= b) element-wise.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[operator]][[\<=]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4leRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\<=]]][(][[[T]]](#_CPPv4I0Ele5array1TRK5array "operator<=::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Ele5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\<=]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Ele5arrayRK5array1T "operator<=::T")[ ][[b]][)][\#](#_CPPv4I0Ele5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[array_equal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[bool]][ ][[equal_nan]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411array_equalRK5arrayRK5arrayb14StreamOrDevice "Link to this definition")\

:   True if two arrays have the same shape and elements.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[array_equal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411array_equalRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[isnan]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45isnanRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[isinf]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45isinfRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[isfinite]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48isfiniteRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[isposinf]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48isposinfRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[isneginf]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48isneginfRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[where]]][(][[const]][ ][[array]][ ][[&]][[condition]], [[const]][ ][[array]][ ][[&]][[x]], [[const]][ ][[array]][ ][[&]][[y]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45whereRK5arrayRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Select from x or y depending on condition.

<!-- -->

[][][][][[array]][ ][[[nan_to_num]]][(][[const]][ ][[array]][ ][[&]][[a]], [[float]][ ][[nan]][ ][[=]][ ][[0.0f]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[float]][[\>]][ ][[posinf]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[float]][[\>]][ ][[neginf]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410nan_to_numRK5arrayfKNSt8optionalIfEEKNSt8optionalIfEE14StreamOrDevice "Link to this definition")\

:   Replace NaN and infinities with finite numbers.

<!-- -->

[][][][][[array]][ ][[[all]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43allRK5arrayb14StreamOrDevice "Link to this definition")\

:   True if all elements in the array are true (or non-zero).

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[all]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43allRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[allclose]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[double]][ ][[rtol]][ ][[=]][ ][[1e-5]], [[double]][ ][[atol]][ ][[=]][ ][[1e-8]], [[bool]][ ][[equal_nan]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48allcloseRK5arrayRK5arrayddb14StreamOrDevice "Link to this definition")\

:   True if the two arrays are equal within the specified tolerance.

<!-- -->

[][][][][[array]][ ][[[isclose]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[double]][ ][[rtol]][ ][[=]][ ][[1e-5]], [[double]][ ][[atol]][ ][[=]][ ][[1e-8]], [[bool]][ ][[equal_nan]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47iscloseRK5arrayRK5arrayddb14StreamOrDevice "Link to this definition")\

:   Returns a boolean array where two arrays are element-wise equal within the specified tolerance.

<!-- -->

[][][][][[array]][ ][[[all]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43allRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   Reduces the input along the given axes.

    An output value is true if all the corresponding inputs are true.

<!-- -->

[][][][][[array]][ ][[[all]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43allRK5arrayib14StreamOrDevice "Link to this definition")\

:   Reduces the input along the given axis.

    An output value is true if all the corresponding inputs are true.

<!-- -->

[][][][][[array]][ ][[[any]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43anyRK5arrayb14StreamOrDevice "Link to this definition")\

:   True if any elements in the array are true (or non-zero).

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[any]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43anyRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[any]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43anyRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   Reduces the input along the given axes.

    An output value is true if any of the corresponding inputs are true.

<!-- -->

[][][][][[array]][ ][[[any]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43anyRK5arrayib14StreamOrDevice "Link to this definition")\

:   Reduces the input along the given axis.

    An output value is true if any of the corresponding inputs are true.

<!-- -->

[][][][][[array]][ ][[[sum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43sumRK5arrayb14StreamOrDevice "Link to this definition")\

:   Sums the elements of an array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[sum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43sumRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[sum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43sumRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   Sums the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[sum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43sumRK5arrayib14StreamOrDevice "Link to this definition")\

:   Sums the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[mean]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44meanRK5arrayb14StreamOrDevice "Link to this definition")\

:   Computes the mean of the elements of an array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[mean]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44meanRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[mean]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44meanRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   Computes the mean of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[mean]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44meanRK5arrayib14StreamOrDevice "Link to this definition")\

:   Computes the mean of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[median]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46medianRK5arrayb14StreamOrDevice "Link to this definition")\

:   Computes the median of the elements of an array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[median]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46medianRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[median]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46medianRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   Computes the median of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[median]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46medianRK5arrayib14StreamOrDevice "Link to this definition")\

:   Computes the median of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[var]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[int]][ ][[ddof]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43varRK5arraybi14StreamOrDevice "Link to this definition")\

:   Computes the variance of the elements of an array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[var]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43varRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[var]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[int]][ ][[ddof]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43varRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice "Link to this definition")\

:   Computes the variance of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[var]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[int]][ ][[ddof]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43varRK5arrayibi14StreamOrDevice "Link to this definition")\

:   Computes the variance of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[std]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[int]][ ][[ddof]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4StRK5arraybi14StreamOrDevice "Link to this definition")\

:   Computes the standard deviation of the elements of an array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[std]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4StRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[std]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[int]][ ][[ddof]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4StRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice "Link to this definition")\

:   Computes the standard deviation of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[std]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[int]][ ][[ddof]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv4StRK5arrayibi14StreamOrDevice "Link to this definition")\

:   Computes the standard deviation of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[prod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44prodRK5arrayb14StreamOrDevice "Link to this definition")\

:   The product of all elements of the array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[prod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44prodRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[prod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44prodRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   The product of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[prod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44prodRK5arrayib14StreamOrDevice "Link to this definition")\

:   The product of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[max]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43maxRK5arrayb14StreamOrDevice "Link to this definition")\

:   The maximum of all elements of the array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[max]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43maxRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[max]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43maxRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   The maximum of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[max]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43maxRK5arrayib14StreamOrDevice "Link to this definition")\

:   The maximum of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[min]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43minRK5arrayb14StreamOrDevice "Link to this definition")\

:   The minimum of all elements of the array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[min]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43minRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[min]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43minRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   The minimum of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[min]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43minRK5arrayib14StreamOrDevice "Link to this definition")\

:   The minimum of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[argmin]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46argminRK5arrayb14StreamOrDevice "Link to this definition")\

:   Returns the index of the minimum value in the array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[argmin]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46argminRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[argmin]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46argminRK5arrayib14StreamOrDevice "Link to this definition")\

:   Returns the indices of the minimum values along a given axis.

<!-- -->

[][][][][[array]][ ][[[argmax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46argmaxRK5arrayb14StreamOrDevice "Link to this definition")\

:   Returns the index of the maximum value in the array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[argmax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46argmaxRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[argmax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46argmaxRK5arrayib14StreamOrDevice "Link to this definition")\

:   Returns the indices of the maximum values along a given axis.

<!-- -->

[][][][][[array]][ ][[[sort]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44sortRK5array14StreamOrDevice "Link to this definition")\

:   Returns a sorted copy of the flattened array.

<!-- -->

[][][][][[array]][ ][[[sort]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44sortRK5arrayi14StreamOrDevice "Link to this definition")\

:   Returns a sorted copy of the array along a given axis.

<!-- -->

[][][][][[array]][ ][[[argsort]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47argsortRK5array14StreamOrDevice "Link to this definition")\

:   Returns indices that sort the flattened array.

<!-- -->

[][][][][[array]][ ][[[argsort]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47argsortRK5arrayi14StreamOrDevice "Link to this definition")\

:   Returns indices that sort the array along a given axis.

<!-- -->

[][][][][[array]][ ][[[partition]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[kth]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49partitionRK5arrayi14StreamOrDevice "Link to this definition")\

:   Returns a partitioned copy of the flattened array such that the smaller kth elements are first.

<!-- -->

[][][][][[array]][ ][[[partition]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[kth]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49partitionRK5arrayii14StreamOrDevice "Link to this definition")\

:   Returns a partitioned copy of the array along a given axis such that the smaller kth elements are first.

<!-- -->

[][][][][[array]][ ][[[argpartition]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[kth]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412argpartitionRK5arrayi14StreamOrDevice "Link to this definition")\

:   Returns indices that partition the flattened array such that the smaller kth elements are first.

<!-- -->

[][][][][[array]][ ][[[argpartition]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[kth]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412argpartitionRK5arrayii14StreamOrDevice "Link to this definition")\

:   Returns indices that partition the array along a given axis such that the smaller kth elements are first.

<!-- -->

[][][][][[array]][ ][[[topk]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[k]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44topkRK5arrayi14StreamOrDevice "Link to this definition")\

:   Returns topk elements of the flattened array.

<!-- -->

[][][][][[array]][ ][[[topk]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[k]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44topkRK5arrayii14StreamOrDevice "Link to this definition")\

:   Returns topk elements of the array along a given axis.

<!-- -->

[][][][][[array]][ ][[[logcumsumexp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412logcumsumexpRK5arraybb14StreamOrDevice "Link to this definition")\

:   Cumulative logsumexp of an array.

<!-- -->

[][][][][[array]][ ][[[logcumsumexp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412logcumsumexpRK5arrayibb14StreamOrDevice "Link to this definition")\

:   Cumulative logsumexp of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[logsumexp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[keepdims]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49logsumexpRK5arrayb14StreamOrDevice "Link to this definition")\

:   The logsumexp of all elements of the array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[logsumexp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49logsumexpRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[logsumexp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49logsumexpRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   The logsumexp of the elements of an array along the given axes.

<!-- -->

[][][][][[array]][ ][[[logsumexp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[keepdims]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49logsumexpRK5arrayib14StreamOrDevice "Link to this definition")\

:   The logsumexp of the elements of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[abs]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43absRK5array14StreamOrDevice "Link to this definition")\

:   Absolute value of elements in an array.

<!-- -->

[][][][][[array]][ ][[[negative]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48negativeRK5array14StreamOrDevice "Link to this definition")\

:   Negate an array.

<!-- -->

[][][][][[array]][ ][[[operator]][[-]]][(][[const]][ ][[array]][ ][[&]][[a]][)][\#](#_CPPv4miRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[sign]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44signRK5array14StreamOrDevice "Link to this definition")\

:   The sign of the elements in an array.

<!-- -->

[][][][][[array]][ ][[[logical_not]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411logical_notRK5array14StreamOrDevice "Link to this definition")\

:   Logical not of an array.

<!-- -->

[][][][][[array]][ ][[[logical_and]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411logical_andRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Logical and of two arrays.

<!-- -->

[][][][][[array]][ ][[[operator]][[&&]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4aaRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[logical_or]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410logical_orRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Logical or of two arrays.

<!-- -->

[][][][][[array]][ ][[[operator]][[\|\|]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4ooRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[reciprocal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410reciprocalRK5array14StreamOrDevice "Link to this definition")\

:   The reciprocal (1/x) of the elements in an array.

<!-- -->

[][][][][[array]][ ][[[add]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43addRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Add two arrays.

<!-- -->

[][][][][[array]][ ][[[operator]][[+]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4plRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[+]]][(][[[T]]](#_CPPv4I0Epl5array1TRK5array "operator+::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Epl5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[+]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Epl5arrayRK5array1T "operator+::T")[ ][[b]][)][\#](#_CPPv4I0Epl5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[subtract]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48subtractRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Subtract two arrays.

<!-- -->

[][][][][[array]][ ][[[operator]][[-]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4miRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[-]]][(][[[T]]](#_CPPv4I0Emi5array1TRK5array "operator-::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Emi5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[-]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Emi5arrayRK5array1T "operator-::T")[ ][[b]][)][\#](#_CPPv4I0Emi5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[multiply]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48multiplyRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Multiply two arrays.

<!-- -->

[][][][][[array]][ ][[[operator]][[\*]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4mlRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\*]]][(][[[T]]](#_CPPv4I0Eml5array1TRK5array "operator*::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Eml5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[\*]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Eml5arrayRK5array1T "operator*::T")[ ][[b]][)][\#](#_CPPv4I0Eml5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[divide]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46divideRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Divide two arrays.

<!-- -->

[][][][][[array]][ ][[[operator]][[/]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4dvRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[operator]][[/]]][(][[double]][ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4dvdRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[operator]][[/]]][(][[const]][ ][[array]][ ][[&]][[a]], [[double]][ ][[b]][)][\#](#_CPPv4dvRK5arrayd "Link to this definition")\

:   

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[divmod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46divmodRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Compute the element-wise quotient and remainder.

<!-- -->

[][][][][[array]][ ][[[floor_divide]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412floor_divideRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Compute integer division.

    Equivalent to doing floor(a / x).

<!-- -->

[][][][][[array]][ ][[[remainder]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49remainderRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Compute the element-wise remainder of division.

<!-- -->

[][][][][[array]][ ][[[operator]][[%]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4rmRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[%]]][(][[[T]]](#_CPPv4I0Erm5array1TRK5array "operator%::T")[ ][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4I0Erm5array1TRK5array "Link to this definition")\

:   

<!-- -->

[][][[template]][[\<]][[typename]][ ][[[T]]][[\>]]\
[][[array]][ ][[[operator]][[%]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[T]]](#_CPPv4I0Erm5arrayRK5array1T "operator%::T")[ ][[b]][)][\#](#_CPPv4I0Erm5arrayRK5array1T "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[maximum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47maximumRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Element-wise maximum between two arrays.

<!-- -->

[][][][][[array]][ ][[[minimum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47minimumRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Element-wise minimum between two arrays.

<!-- -->

[][][][][[array]][ ][[[floor]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45floorRK5array14StreamOrDevice "Link to this definition")\

:   Floor the element of an array.

<!-- -->

[][][][][[array]][ ][[[ceil]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44ceilRK5array14StreamOrDevice "Link to this definition")\

:   Ceil the element of an array.

<!-- -->

[][][][][[array]][ ][[[square]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46squareRK5array14StreamOrDevice "Link to this definition")\

:   Square the elements of an array.

<!-- -->

[][][][][[array]][ ][[[exp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43expRK5array14StreamOrDevice "Link to this definition")\

:   Exponential of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[sin]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43sinRK5array14StreamOrDevice "Link to this definition")\

:   Sine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[cos]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43cosRK5array14StreamOrDevice "Link to this definition")\

:   Cosine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[tan]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43tanRK5array14StreamOrDevice "Link to this definition")\

:   Tangent of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[arcsin]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arcsinRK5array14StreamOrDevice "Link to this definition")\

:   Arc Sine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[arccos]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arccosRK5array14StreamOrDevice "Link to this definition")\

:   Arc Cosine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[arctan]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46arctanRK5array14StreamOrDevice "Link to this definition")\

:   Arc Tangent of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[arctan2]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47arctan2RK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Inverse tangent of the ratio of two arrays.

<!-- -->

[][][][][[array]][ ][[[sinh]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44sinhRK5array14StreamOrDevice "Link to this definition")\

:   Hyperbolic Sine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[cosh]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44coshRK5array14StreamOrDevice "Link to this definition")\

:   Hyperbolic Cosine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[tanh]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44tanhRK5array14StreamOrDevice "Link to this definition")\

:   Hyperbolic Tangent of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[arcsinh]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47arcsinhRK5array14StreamOrDevice "Link to this definition")\

:   Inverse Hyperbolic Sine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[arccosh]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47arccoshRK5array14StreamOrDevice "Link to this definition")\

:   Inverse Hyperbolic Cosine of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[arctanh]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47arctanhRK5array14StreamOrDevice "Link to this definition")\

:   Inverse Hyperbolic Tangent of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[degrees]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47degreesRK5array14StreamOrDevice "Link to this definition")\

:   Convert the elements of an array from Radians to Degrees.

<!-- -->

[][][][][[array]][ ][[[radians]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47radiansRK5array14StreamOrDevice "Link to this definition")\

:   Convert the elements of an array from Degrees to Radians.

<!-- -->

[][][][][[array]][ ][[[log]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43logRK5array14StreamOrDevice "Link to this definition")\

:   Natural logarithm of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[log2]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44log2RK5array14StreamOrDevice "Link to this definition")\

:   Log base 2 of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[log10]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45log10RK5array14StreamOrDevice "Link to this definition")\

:   Log base 10 of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[log1p]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45log1pRK5array14StreamOrDevice "Link to this definition")\

:   Natural logarithm of one plus elements in the array: [`log(1`]` `[`+`]` `[`a)`].

<!-- -->

[][][][][[array]][ ][[[logaddexp]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49logaddexpRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Log-add-exp of one elements in the array: [`log(exp(a)`]` `[`+`]` `[`exp(b))`].

<!-- -->

[][][][][[array]][ ][[[sigmoid]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47sigmoidRK5array14StreamOrDevice "Link to this definition")\

:   Element-wise logistic sigmoid of the array: [`1`]` `[`/`]` `[`(1`]` `[`+`]` `[`exp(-x)`].

<!-- -->

[][][][][[array]][ ][[[erf]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv43erfRK5array14StreamOrDevice "Link to this definition")\

:   Computes the error function of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[erfinv]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46erfinvRK5array14StreamOrDevice "Link to this definition")\

:   Computes the inverse error function of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[expm1]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45expm1RK5array14StreamOrDevice "Link to this definition")\

:   Computes the expm1 function of the elements of an array.

<!-- -->

[][][][][[array]][ ][[[stop_gradient]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv413stop_gradientRK5array14StreamOrDevice "Link to this definition")\

:   Stop the flow of gradients.

<!-- -->

[][][][][[array]][ ][[[round]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[decimals]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45roundRK5arrayi14StreamOrDevice "Link to this definition")\

:   Round a floating point number.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[round]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45roundRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[matmul]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46matmulRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Matrix-matrix multiplication.

<!-- -->

[][][][][[array]][ ][[[gather]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[indices]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[const]][ ][[Shape]][ ][[&]][[slice_sizes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46gatherRK5arrayRKNSt6vectorI5arrayEERKNSt6vectorIiEERK5Shape14StreamOrDevice "Link to this definition")\

:   Gather array entries given indices and slices.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[gather]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[int]][ ][[axis]], [[const]][ ][[Shape]][ ][[&]][[slice_sizes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46gatherRK5arrayRK5arrayiRK5Shape14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[kron]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44kronRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Compute the Kronecker product of two arrays.

<!-- -->

[][][][][[array]][ ][[[take]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44takeRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   Take array slices at the given indices of the specified axis.

<!-- -->

[][][][][[array]][ ][[[take]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[index]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44takeRK5arrayii14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[take]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44takeRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Take array entries at the given indices treating the array as flattened.

<!-- -->

[][][][][[array]][ ][[[take]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[index]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44takeRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[take_along_axis]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv415take_along_axisRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   Take array entries given indices along the axis.

<!-- -->

[][][][][[array]][ ][[[put_along_axis]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[values]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv414put_along_axisRK5arrayRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   Put the values into the array at the given indices along the axis.

<!-- -->

[][][][][[array]][ ][[[scatter_add_axis]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[values]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv416scatter_add_axisRK5arrayRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   Add the values into the array at the given indices along the axis.

<!-- -->

[][][][][[array]][ ][[[scatter]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47scatterRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Scatter updates to the given indices.

    The parameters [`indices`] and [`axes`] determine the locations of [`a`] that are updated with the values in [`updates`]. Assuming 1-d [`indices`] for simplicity, [`indices[i]`] are the indices on axis [`axes[i]`] to which the values in [`updates`] will be applied. Note each array in [`indices`] is assigned to a corresponding axis and hence [`indices.size()`]` `[`==`]` `[`axes.size()`]. If an index/axis pair is not provided then indices along that axis are assumed to be zero.

    Note the rank of [`updates`] must be equal to the sum of the rank of the broadcasted [`indices`] and the rank of [`a`]. In other words, assuming the arrays in [`indices`] have the same shape, [`updates.ndim()`]` `[`==`]` `[`indices[0].ndim()`]` `[`+`]` `[`a.ndim()`]. The leading dimensions of [`updates`] correspond to the indices, and the remaining [`a.ndim()`] dimensions are the values that will be applied to the given location in [`a`].

    For example:

    :::: 
    ::: highlight
        auto in = zeros(, float32);
        auto indices = array();
        auto updates = reshape(arange(1, 3, float32), );
        std::vector<int> axes;

        auto out = scatter(in, , updates, axes);
    :::
    ::::

    will produce:

    :::: 
    ::: highlight
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [1, 2, 0, 0],
               [0, 0, 0, 0]], dtype=float32)
    :::
    ::::

    This scatters the two-element row vector [`[1,`]` `[`2]`] starting at the [`(2,`]` `[`0)`] position of [`a`].

    Adding another element to [`indices`] will scatter into another location of [`a`]. We also have to add an another update for the new index:

    :::: 
    ::: highlight
        auto in = zeros(, float32);
        auto indices = array();
        auto updates = reshape(arange(1, 5, float32), );
        std::vector<int> axes;

        auto out = scatter(in, , updates, axes):
    :::
    ::::

    will produce:

    :::: 
    ::: highlight
        array([[3, 4, 0, 0],
               [0, 0, 0, 0],
               [1, 2, 0, 0],
               [0, 0, 0, 0]], dtype=float32)
    :::
    ::::

    To control the scatter location on an additional axis, add another index array to [`indices`] and another axis to [`axes`]:

    :::: 
    ::: highlight
        auto in = zeros(, float32);
        auto indices = std::vector), array()};
        auto updates = reshape(arange(1, 5, float32), );
        std::vector<int> axes;

        auto out = scatter(in, indices, updates, axes);
    :::
    ::::

    will produce:

    :::: 
    ::: highlight
        array([[0, 0, 3, 4],
              [0, 0, 0, 0],
              [0, 1, 2, 0],
              [0, 0, 0, 0]], dtype=float32)
    :::
    ::::

    Items in indices are broadcasted together. This means:

    :::: 
    ::: highlight
        auto indices = std::vector), array()};
    :::
    ::::

    is equivalent to:

    :::: 
    ::: highlight
        auto indices = std::vector), array()};
    :::
    ::::

    Note, [`scatter`] does not perform bounds checking on the indices and updates. Out-of-bounds accesses on [`a`] are undefined and typically result in unintended or invalid memory writes.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[scatter]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47scatterRK5arrayRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[scatter_add]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411scatter_addRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Scatter and add updates to given indices.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[scatter_add]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411scatter_addRK5arrayRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[scatter_prod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412scatter_prodRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Scatter and prod updates to given indices.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[scatter_prod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412scatter_prodRK5arrayRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[scatter_max]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411scatter_maxRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Scatter and max updates to given linear indices.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[scatter_max]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411scatter_maxRK5arrayRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[scatter_min]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411scatter_minRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   Scatter and min updates to given linear indices.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[scatter_min]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[indices]], [[const]][ ][[array]][ ][[&]][[updates]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411scatter_minRK5arrayRK5arrayRK5arrayi14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[masked_scatter]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[mask]], [[const]][ ][[array]][ ][[&]][[src]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv414masked_scatterRK5arrayRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[sqrt]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44sqrtRK5array14StreamOrDevice "Link to this definition")\

:   Square root the elements of an array.

<!-- -->

[][][][][[array]][ ][[[rsqrt]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45rsqrtRK5array14StreamOrDevice "Link to this definition")\

:   Square root and reciprocal the elements of an array.

<!-- -->

[][][][][[array]][ ][[[softmax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[bool]][ ][[precise]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47softmaxRK5arrayRKNSt6vectorIiEEb14StreamOrDevice "Link to this definition")\

:   Softmax of an array.

<!-- -->

[][][][][[array]][ ][[[softmax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[precise]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47softmaxRK5arrayb14StreamOrDevice "Link to this definition")\

:   Softmax of an array.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[softmax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[precise]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47softmaxRK5arrayib14StreamOrDevice "Link to this definition")\

:   Softmax of an array.

<!-- -->

[][][][][[array]][ ][[[power]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45powerRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Raise elements of a to the power of b element-wise.

<!-- -->

[][][][][[array]][ ][[[cumsum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46cumsumRK5arraybb14StreamOrDevice "Link to this definition")\

:   Cumulative sum of an array.

<!-- -->

[][][][][[array]][ ][[[cumsum]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46cumsumRK5arrayibb14StreamOrDevice "Link to this definition")\

:   Cumulative sum of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[cumprod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47cumprodRK5arraybb14StreamOrDevice "Link to this definition")\

:   Cumulative product of an array.

<!-- -->

[][][][][[array]][ ][[[cumprod]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv47cumprodRK5arrayibb14StreamOrDevice "Link to this definition")\

:   Cumulative product of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[cummax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46cummaxRK5arraybb14StreamOrDevice "Link to this definition")\

:   Cumulative max of an array.

<!-- -->

[][][][][[array]][ ][[[cummax]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46cummaxRK5arrayibb14StreamOrDevice "Link to this definition")\

:   Cumulative max of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[cummin]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46cumminRK5arraybb14StreamOrDevice "Link to this definition")\

:   Cumulative min of an array.

<!-- -->

[][][][][[array]][ ][[[cummin]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[axis]], [[bool]][ ][[reverse]][ ][[=]][ ][[false]], [[bool]][ ][[inclusive]][ ][[=]][ ][[true]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46cumminRK5arrayibb14StreamOrDevice "Link to this definition")\

:   Cumulative min of an array along the given axis.

<!-- -->

[][][][][[array]][ ][[[conv_general]]][(][[array]][ ][[input]], [[array]][ ][[weight]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[stride]][ ][[=]][ ][[][[}]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[padding_lo]][ ][[=]][ ][[][[}]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[padding_hi]][ ][[=]][ ][[][[}]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[kernel_dilation]][ ][[=]][ ][[][[}]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[input_dilation]][ ][[=]][ ][[][[}]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[bool]][ ][[flip]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412conv_general5array5arrayNSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEEib14StreamOrDevice "Link to this definition")\

:   General convolution with a filter.

<!-- -->

[][][][][[inline]][ ][[array]][ ][[[conv_general]]][(][[const]][ ][[array]][ ][[&]][[input]], [[const]][ ][[array]][ ][[&]][[weight]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[stride]][ ][[=]][ ][[][[}]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[padding]][ ][[=]][ ][[][[}]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[kernel_dilation]][ ][[=]][ ][[][[}]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[input_dilation]][ ][[=]][ ][[][[}]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[bool]][ ][[flip]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412conv_generalRK5arrayRK5arrayNSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEEib14StreamOrDevice "Link to this definition")\

:   General convolution with a filter.

<!-- -->

[][][][][[array]][ ][[[conv1d]]][(][[const]][ ][[array]][ ][[&]][[input]], [[const]][ ][[array]][ ][[&]][[weight]], [[int]][ ][[stride]][ ][[=]][ ][[1]], [[int]][ ][[padding]][ ][[=]][ ][[0]], [[int]][ ][[dilation]][ ][[=]][ ][[1]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46conv1dRK5arrayRK5arrayiiii14StreamOrDevice "Link to this definition")\

:   1D convolution with a filter

<!-- -->

[][][][][[array]][ ][[[conv2d]]][(][[const]][ ][[array]][ ][[&]][[input]], [[const]][ ][[array]][ ][[&]][[weight]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[stride]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[padding]][ ][[=]][ ][[][[0]][[,]][ ][[0]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[dilation]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[}]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46conv2dRK5arrayRK5arrayRKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEEi14StreamOrDevice "Link to this definition")\

:   2D convolution with a filter

<!-- -->

[][][][][[array]][ ][[[conv3d]]][(][[const]][ ][[array]][ ][[&]][[input]], [[const]][ ][[array]][ ][[&]][[weight]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[tuple]][[\<]][[int]][[,]][ ][[int]][[,]][ ][[int]][[\>]][ ][[&]][[stride]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[,]][ ][[1]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[tuple]][[\<]][[int]][[,]][ ][[int]][[,]][ ][[int]][[\>]][ ][[&]][[padding]][ ][[=]][ ][[][[0]][[,]][ ][[0]][[,]][ ][[0]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[tuple]][[\<]][[int]][[,]][ ][[int]][[,]][ ][[int]][[\>]][ ][[&]][[dilation]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[,]][ ][[1]][[}]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46conv3dRK5arrayRK5arrayRKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEEi14StreamOrDevice "Link to this definition")\

:   3D convolution with a filter

<!-- -->

[][][][][[array]][ ][[[conv_transpose1d]]][(][[const]][ ][[array]][ ][[&]][[input]], [[const]][ ][[array]][ ][[&]][[weight]], [[int]][ ][[stride]][ ][[=]][ ][[1]], [[int]][ ][[padding]][ ][[=]][ ][[0]], [[int]][ ][[dilation]][ ][[=]][ ][[1]], [[int]][ ][[output_padding]][ ][[=]][ ][[0]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv416conv_transpose1dRK5arrayRK5arrayiiiii14StreamOrDevice "Link to this definition")\

:   1D transposed convolution with a filter

<!-- -->

[][][][][[array]][ ][[[conv_transpose2d]]][(][[const]][ ][[array]][ ][[&]][[input]], [[const]][ ][[array]][ ][[&]][[weight]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[stride]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[padding]][ ][[=]][ ][[][[0]][[,]][ ][[0]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[dilation]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[pair]][[\<]][[int]][[,]][ ][[int]][[\>]][ ][[&]][[output_padding]][ ][[=]][ ][[][[0]][[,]][ ][[0]][[}]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv416conv_transpose2dRK5arrayRK5arrayRKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEEi14StreamOrDevice "Link to this definition")\

:   2D transposed convolution with a filter

<!-- -->

[][][][][[array]][ ][[[conv_transpose3d]]][(][[const]][ ][[array]][ ][[&]][[input]], [[const]][ ][[array]][ ][[&]][[weight]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[tuple]][[\<]][[int]][[,]][ ][[int]][[,]][ ][[int]][[\>]][ ][[&]][[stride]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[,]][ ][[1]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[tuple]][[\<]][[int]][[,]][ ][[int]][[,]][ ][[int]][[\>]][ ][[&]][[padding]][ ][[=]][ ][[][[0]][[,]][ ][[0]][[,]][ ][[0]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[tuple]][[\<]][[int]][[,]][ ][[int]][[,]][ ][[int]][[\>]][ ][[&]][[dilation]][ ][[=]][ ][[][[1]][[,]][ ][[1]][[,]][ ][[1]][[}]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[tuple]][[\<]][[int]][[,]][ ][[int]][[,]][ ][[int]][[\>]][ ][[&]][[output_padding]][ ][[=]][ ][[][[0]][[,]][ ][[0]][[,]][ ][[0]][[}]], [[int]][ ][[groups]][ ][[=]][ ][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv416conv_transpose3dRK5arrayRK5arrayRKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEEi14StreamOrDevice "Link to this definition")\

:   3D transposed convolution with a filter

<!-- -->

[][][][][[array]][ ][[[quantized_matmul]]][(][[array]][ ][[x]], [[array]][ ][[w]], [[array]][ ][[scales]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[biases]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[bool]][ ][[transpose]][ ][[=]][ ][[true]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[group_size]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[bits]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"affine\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv416quantized_matmul5array5array5arrayNSt8optionalI5arrayEEbNSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice "Link to this definition")\

:   Quantized matmul multiplies x with a quantized matrix w.

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[quantize]]][(][[const]][ ][[array]][ ][[&]][[w]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[group_size]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[bits]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"affine\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48quantizeRK5arrayNSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice "Link to this definition")\

:   Quantize a matrix along its last axis.

<!-- -->

[][][][][[array]][ ][[[dequantize]]][(][[const]][ ][[array]][ ][[&]][[w]], [[const]][ ][[array]][ ][[&]][[scales]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[&]][[biases]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[group_size]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[bits]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"affine\"]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[Dtype]][[\>]][ ][[dtype]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410dequantizeRK5arrayRK5arrayRKNSt8optionalI5arrayEENSt8optionalIiEENSt8optionalIiEERKNSt6stringENSt8optionalI5DtypeEE14StreamOrDevice "Link to this definition")\

:   Dequantize a matrix produced by [[quantize()]](#group__ops_1gaf6a56ec149f9c8bd694c9bf9c9659660)

<!-- -->

[][][][][[array]][ ][[[qqmm]]][(][[array]][ ][[x]], [[array]][ ][[w]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[w_scales]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[group_size]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[bits]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"nvfp4\"]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44qqmm5array5arrayNSt8optionalI5arrayEENSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[from_fp8]]][(][[array]][ ][[x]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48from_fp85array5Dtype14StreamOrDevice "Link to this definition")\

:   Convert an E4M3 float8 to the given floating point dtype.

<!-- -->

[][][][][[array]][ ][[[to_fp8]]][(][[array]][ ][[x]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv46to_fp85array14StreamOrDevice "Link to this definition")\

:   Convert a floating point matrix to E4M3 float8.

<!-- -->

[][][][][[array]][ ][[[gather_qmm]]][(][[const]][ ][[array]][ ][[&]][[x]], [[const]][ ][[array]][ ][[&]][[w]], [[const]][ ][[array]][ ][[&]][[scales]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[&]][[biases]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[lhs_indices]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[rhs_indices]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[bool]][ ][[transpose]][ ][[=]][ ][[true]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[group_size]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[int]][[\>]][ ][[bits]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[string]][ ][[&]][[mode]][ ][[=]][ ][[\"affine\"]], [[bool]][ ][[sorted_indices]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410gather_qmmRK5arrayRK5arrayRK5arrayRKNSt8optionalI5arrayEENSt8optionalI5arrayEENSt8optionalI5arrayEEbNSt8optionalIiEENSt8optionalIiEERKNSt6stringEb14StreamOrDevice "Link to this definition")\

:   Compute matrix products with matrix-level gather.

<!-- -->

[][][][][[array]][ ][[[tensordot]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[const]][ ][[int]][ ][[axis]][ ][[=]][ ][[2]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49tensordotRK5arrayRK5arrayKi14StreamOrDevice "Link to this definition")\

:   Returns a contraction of a and b over multiple dimensions.

<!-- -->

[][][][][[array]][ ][[[tensordot]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes_a]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes_b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49tensordotRK5arrayRK5arrayRKNSt6vectorIiEERKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[outer]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45outerRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Compute the outer product of two vectors.

<!-- -->

[][][][][[array]][ ][[[inner]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45innerRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Compute the inner product of two vectors.

<!-- -->

[][][][][[array]][ ][[[addmm]]][(][[array]][ ][[c]], [[array]][ ][[a]], [[array]][ ][[b]], [[const]][ ][[float]][ ][[&]][[alpha]][ ][[=]][ ][[1.f]], [[const]][ ][[float]][ ][[&]][[beta]][ ][[=]][ ][[1.f]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45addmm5array5array5arrayRKfRKf14StreamOrDevice "Link to this definition")\

:   Compute D = beta \* C + alpha \* (A @ B)

<!-- -->

[][][][][[array]][ ][[[block_masked_mm]]][(][[array]][ ][[a]], [[array]][ ][[b]], [[int]][ ][[block_size]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[mask_out]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[mask_lhs]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[mask_rhs]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv415block_masked_mm5array5arrayiNSt8optionalI5arrayEENSt8optionalI5arrayEENSt8optionalI5arrayEE14StreamOrDevice "Link to this definition")\

:   Compute matrix product with block masking.

<!-- -->

[][][][][[array]][ ][[[gather_mm]]][(][[array]][ ][[a]], [[array]][ ][[b]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[lhs_indices]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[optional]][[\<]][[array]][[\>]][ ][[rhs_indices]][ ][[=]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[nullopt]], [[bool]][ ][[sorted_indices]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49gather_mm5array5arrayNSt8optionalI5arrayEENSt8optionalI5arrayEEb14StreamOrDevice "Link to this definition")\

:   Compute matrix product with matrix-level gather.

<!-- -->

[][][][][[array]][ ][[[segmented_mm]]][(][[array]][ ][[a]], [[array]][ ][[b]], [[array]][ ][[segments]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv412segmented_mm5array5array5array14StreamOrDevice "Link to this definition")\

:   Compute a matrix product but segment the inner dimension and write the result separately for each segment.

<!-- -->

[][][][][[array]][ ][[[diagonal]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[offset]][ ][[=]][ ][[0]], [[int]][ ][[axis1]][ ][[=]][ ][[0]], [[int]][ ][[axis2]][ ][[=]][ ][[1]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv48diagonalRK5arrayiii14StreamOrDevice "Link to this definition")\

:   Extract a diagonal or construct a diagonal array.

<!-- -->

[][][][][[array]][ ][[[diag]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[k]][ ][[=]][ ][[0]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44diagRK5arrayi14StreamOrDevice "Link to this definition")\

:   Extract diagonal from a 2d array or create a diagonal matrix.

<!-- -->

[][][][][[array]][ ][[[trace]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[offset]], [[int]][ ][[axis1]], [[int]][ ][[axis2]], [[Dtype]][ ][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45traceRK5arrayiii5Dtype14StreamOrDevice "Link to this definition")\

:   Return the sum along a specified diagonal in the given array.

<!-- -->

[][][][][[array]][ ][[[trace]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[offset]], [[int]][ ][[axis1]], [[int]][ ][[axis2]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45traceRK5arrayiii14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[trace]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv45traceRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[depends]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[inputs]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[dependencies]][)][\#](#_CPPv47dependsRKNSt6vectorI5arrayEERKNSt6vectorI5arrayEE "Link to this definition")\

:   Implements the identity function but allows injecting dependencies to other arrays.

    This ensures that these other arrays will have been computed when the outputs of this function are computed.

<!-- -->

[][][][][[array]][ ][[[atleast_1d]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410atleast_1dRK5array14StreamOrDevice "Link to this definition")\

:   convert an array to an atleast ndim array

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[atleast_1d]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410atleast_1dRKNSt6vectorI5arrayEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[atleast_2d]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410atleast_2dRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[atleast_2d]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410atleast_2dRKNSt6vectorI5arrayEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[atleast_3d]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410atleast_3dRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[[atleast_3d]]][(][[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[array]][[\>]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410atleast_3dRKNSt6vectorI5arrayEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[number_of_elements]]][(][[const]][ ][[array]][ ][[&]][[a]], [[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[axes]], [[bool]][ ][[inverted]], [[Dtype]][ ][[dtype]][ ][[=]][ ][[int32]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv418number_of_elementsRK5arrayNSt6vectorIiEEb5Dtype14StreamOrDevice "Link to this definition")\

:   Extract the number of elements along some axes as a scalar array.

    Used to allow shape dependent shapeless compilation (pun intended).

<!-- -->

[][][][][[array]][ ][[[conjugate]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv49conjugateRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[bitwise_and]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411bitwise_andRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Bitwise and.

<!-- -->

[][][][][[array]][ ][[[operator]][[&]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4anRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[bitwise_or]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410bitwise_orRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Bitwise inclusive or.

<!-- -->

[][][][][[array]][ ][[[operator]][[\|]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4orRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[bitwise_xor]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411bitwise_xorRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Bitwise exclusive or.

<!-- -->

[][][][][[array]][ ][[[operator]][[\^]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4eoRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[left_shift]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410left_shiftRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Shift bits to the left.

<!-- -->

[][][][][[array]][ ][[[operator]][[\<\<]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4lsRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[right_shift]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv411right_shiftRK5arrayRK5array14StreamOrDevice "Link to this definition")\

:   Shift bits to the right.

<!-- -->

[][][][][[array]][ ][[[operator]][[\>\>]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[array]][ ][[&]][[b]][)][\#](#_CPPv4rsRK5arrayRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[bitwise_invert]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv414bitwise_invertRK5array14StreamOrDevice "Link to this definition")\

:   Invert the bits.

<!-- -->

[][][][][[array]][ ][[[operator]][[\~]]][(][[const]][ ][[array]][ ][[&]][[a]][)][\#](#_CPPv4coRK5array "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[view]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[Dtype]][ ][[&]][[dtype]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44viewRK5arrayRK5Dtype14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[roll]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[shift]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44rollRK5arrayi14StreamOrDevice "Link to this definition")\

:   Roll elements along an axis and introduce them on the other side.

<!-- -->

[][][][][[array]][ ][[[roll]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[Shape]][ ][[&]][[shift]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44rollRK5arrayRK5Shape14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[roll]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[shift]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44rollRK5arrayii14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[roll]]][(][[const]][ ][[array]][ ][[&]][[a]], [[int]][ ][[shift]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44rollRK5arrayiRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[roll]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[Shape]][ ][[&]][[shift]], [[int]][ ][[axis]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44rollRK5arrayRK5Shapei14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[roll]]][(][[const]][ ][[array]][ ][[&]][[a]], [[const]][ ][[Shape]][ ][[&]][[shift]], [[const]][ ][[[std]]](#_CPPv4StRK5arraybi14StreamOrDevice "std")[[::]][[vector]][[\<]][[int]][[\>]][ ][[&]][[axes]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44rollRK5arrayRK5ShapeRKNSt6vectorIiEE14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[real]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44realRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[imag]]][(][[const]][ ][[array]][ ][[&]][[a]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv44imagRK5array14StreamOrDevice "Link to this definition")\

:   

<!-- -->

[][][][][[array]][ ][[[contiguous]]][(][[const]][ ][[array]][ ][[&]][[a]], [[bool]][ ][[allow_col_major]][ ][[=]][ ][[false]], [[StreamOrDevice]][ ][[s]][ ][[=]][ ][[][[}]][)][\#](#_CPPv410contiguousRK5arrayb14StreamOrDevice "Link to this definition")\

:   

[](../python/_autosummary/mlx.utils.tree_reduce.html "previous page")

previous

mlx.utils.tree_reduce

[](../dev/extensions.html "next page")

next

Custom Extensions in MLX

Contents

- [[`arange()`]](#_CPPv46arangeddd5Dtype14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangeddd14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangedd5Dtype14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangedd14StreamOrDevice)
- [[`arange()`]](#_CPPv46aranged5Dtype14StreamOrDevice)
- [[`arange()`]](#_CPPv46aranged14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangeiii14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangeii14StreamOrDevice)
- [[`arange()`]](#_CPPv46arangei14StreamOrDevice)
- [[`linspace()`]](#_CPPv48linspaceddi5Dtype14StreamOrDevice)
- [[`astype()`]](#_CPPv46astype5array5Dtype14StreamOrDevice)
- [[`as_strided()`]](#_CPPv410as_strided5array5Shape7Strides6size_t14StreamOrDevice)
- [[`copy()`]](#_CPPv44copy5array14StreamOrDevice)
- [[`full()`]](#_CPPv44full5Shape5array5Dtype14StreamOrDevice)
- [[`full()`]](#_CPPv44full5Shape5array14StreamOrDevice)
- [[`full()`]](#_CPPv4I0E4full5array5Shape1T5Dtype14StreamOrDevice)
- [[`full()`]](#_CPPv4I0E4full5array5Shape1T14StreamOrDevice)
- [[`full_like()`]](#_CPPv49full_likeRK5array5array5Dtype14StreamOrDevice)
- [[`full_like()`]](#_CPPv49full_likeRK5array5array14StreamOrDevice)
- [[`full_like()`]](#_CPPv4I0E9full_like5arrayRK5array1T5Dtype14StreamOrDevice)
- [[`full_like()`]](#_CPPv4I0E9full_like5arrayRK5array1T14StreamOrDevice)
- [[`zeros()`]](#_CPPv45zerosRK5Shape5Dtype14StreamOrDevice)
- [[`zeros()`]](#_CPPv45zerosRK5Shape14StreamOrDevice)
- [[`zeros_like()`]](#_CPPv410zeros_likeRK5array14StreamOrDevice)
- [[`ones()`]](#_CPPv44onesRK5Shape5Dtype14StreamOrDevice)
- [[`ones()`]](#_CPPv44onesRK5Shape14StreamOrDevice)
- [[`ones_like()`]](#_CPPv49ones_likeRK5array14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyeiii5Dtype14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyei5Dtype14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyeii14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyeiii14StreamOrDevice)
- [[`eye()`]](#_CPPv43eyei14StreamOrDevice)
- [[`identity()`]](#_CPPv48identityi5Dtype14StreamOrDevice)
- [[`identity()`]](#_CPPv48identityi14StreamOrDevice)
- [[`tri()`]](#_CPPv43triiii5Dtype14StreamOrDevice)
- [[`tri()`]](#_CPPv43trii5Dtype14StreamOrDevice)
- [[`tril()`]](#_CPPv44tril5arrayi14StreamOrDevice)
- [[`triu()`]](#_CPPv44triu5arrayi14StreamOrDevice)
- [[`reshape()`]](#_CPPv47reshapeRK5array5Shape14StreamOrDevice)
- [[`unflatten()`]](#_CPPv49unflattenRK5arrayi5Shape14StreamOrDevice)
- [[`flatten()`]](#_CPPv47flattenRK5arrayii14StreamOrDevice)
- [[`flatten()`]](#_CPPv47flattenRK5array14StreamOrDevice)
- [[`hadamard_transform()`]](#_CPPv418hadamard_transformRK5arrayNSt8optionalIfEE14StreamOrDevice)
- [[`squeeze()`]](#_CPPv47squeezeRK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`squeeze()`]](#_CPPv47squeezeRK5arrayi14StreamOrDevice)
- [[`squeeze()`]](#_CPPv47squeezeRK5array14StreamOrDevice)
- [[`expand_dims()`]](#_CPPv411expand_dimsRK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`expand_dims()`]](#_CPPv411expand_dimsRK5arrayi14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5array5Shape5Shape5Shape14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5arrayNSt16initializer_listIiEE5Shape5Shape14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5array5Shape5Shape14StreamOrDevice)
- [[`slice()`]](#_CPPv45sliceRK5arrayRK5arrayNSt6vectorIiEE5Shape14StreamOrDevice)
- [[`slice_update()`]](#_CPPv412slice_updateRK5arrayRK5array5Shape5Shape5Shape14StreamOrDevice)
- [[`slice_update()`]](#_CPPv412slice_updateRK5arrayRK5array5Shape5Shape14StreamOrDevice)
- [[`slice_update()`]](#_CPPv412slice_updateRK5arrayRK5arrayRK5arrayNSt6vectorIiEE14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayii14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayi14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayRK5Shapei14StreamOrDevice)
- [[`split()`]](#_CPPv45splitRK5arrayRK5Shape14StreamOrDevice)
- [[`meshgrid()`]](#_CPPv48meshgridRKNSt6vectorI5arrayEEbRKNSt6stringE14StreamOrDevice)
- [[`clip()`]](#_CPPv44clipRK5arrayRKNSt8optionalI5arrayEERKNSt8optionalI5arrayEE14StreamOrDevice)
- [[`concatenate()`]](#_CPPv411concatenateNSt6vectorI5arrayEEi14StreamOrDevice)
- [[`concatenate()`]](#_CPPv411concatenateNSt6vectorI5arrayEE14StreamOrDevice)
- [[`stack()`]](#_CPPv45stackRKNSt6vectorI5arrayEEi14StreamOrDevice)
- [[`stack()`]](#_CPPv45stackRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`repeat()`]](#_CPPv46repeatRK5arrayii14StreamOrDevice)
- [[`repeat()`]](#_CPPv46repeatRK5arrayi14StreamOrDevice)
- [[`tile()`]](#_CPPv44tileRK5arrayNSt6vectorIiEE14StreamOrDevice)
- [[`transpose()`]](#_CPPv49transposeRK5arrayNSt6vectorIiEE14StreamOrDevice)
- [[`transpose()`]](#_CPPv49transposeRK5arrayNSt16initializer_listIiEE14StreamOrDevice)
- [[`swapaxes()`]](#_CPPv48swapaxesRK5arrayii14StreamOrDevice)
- [[`moveaxis()`]](#_CPPv48moveaxisRK5arrayii14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayRKNSt6vectorIiEERK5ShapeRK5ShapeRK5arrayRKNSt6stringE14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayRKNSt6vectorINSt4pairIiiEEEERK5arrayRKNSt6stringE14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayRKNSt4pairIiiEERK5arrayRKNSt6stringE14StreamOrDevice)
- [[`pad()`]](#_CPPv43padRK5arrayiRK5arrayRKNSt6stringE14StreamOrDevice)
- [[`transpose()`]](#_CPPv49transposeRK5array14StreamOrDevice)
- [[`broadcast_to()`]](#_CPPv412broadcast_toRK5arrayRK5Shape14StreamOrDevice)
- [[`broadcast_arrays()`]](#_CPPv416broadcast_arraysRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`equal()`]](#_CPPv45equalRK5arrayRK5array14StreamOrDevice)
- [[`operator==()`]](#_CPPv4eqRK5arrayRK5array)
- [[`operator==()`]](#_CPPv4I0Eeq5array1TRK5array)
- [[`operator==()`]](#_CPPv4I0Eeq5arrayRK5array1T)
- [[`not_equal()`]](#_CPPv49not_equalRK5arrayRK5array14StreamOrDevice)
- [[`operator!=()`]](#_CPPv4neRK5arrayRK5array)
- [[`operator!=()`]](#_CPPv4I0Ene5array1TRK5array)
- [[`operator!=()`]](#_CPPv4I0Ene5arrayRK5array1T)
- [[`greater()`]](#_CPPv47greaterRK5arrayRK5array14StreamOrDevice)
- [[`operator>()`]](#_CPPv4gtRK5arrayRK5array)
- [[`operator>()`]](#_CPPv4I0Egt5array1TRK5array)
- [[`operator>()`]](#_CPPv4I0Egt5arrayRK5array1T)
- [[`greater_equal()`]](#_CPPv413greater_equalRK5arrayRK5array14StreamOrDevice)
- [[`operator>=()`]](#_CPPv4geRK5arrayRK5array)
- [[`operator>=()`]](#_CPPv4I0Ege5array1TRK5array)
- [[`operator>=()`]](#_CPPv4I0Ege5arrayRK5array1T)
- [[`less()`]](#_CPPv44lessRK5arrayRK5array14StreamOrDevice)
- [[`operator<()`]](#_CPPv4ltRK5arrayRK5array)
- [[`operator<()`]](#_CPPv4I0Elt5array1TRK5array)
- [[`operator<()`]](#_CPPv4I0Elt5arrayRK5array1T)
- [[`less_equal()`]](#_CPPv410less_equalRK5arrayRK5array14StreamOrDevice)
- [[`operator<=()`]](#_CPPv4leRK5arrayRK5array)
- [[`operator<=()`]](#_CPPv4I0Ele5array1TRK5array)
- [[`operator<=()`]](#_CPPv4I0Ele5arrayRK5array1T)
- [[`array_equal()`]](#_CPPv411array_equalRK5arrayRK5arrayb14StreamOrDevice)
- [[`array_equal()`]](#_CPPv411array_equalRK5arrayRK5array14StreamOrDevice)
- [[`isnan()`]](#_CPPv45isnanRK5array14StreamOrDevice)
- [[`isinf()`]](#_CPPv45isinfRK5array14StreamOrDevice)
- [[`isfinite()`]](#_CPPv48isfiniteRK5array14StreamOrDevice)
- [[`isposinf()`]](#_CPPv48isposinfRK5array14StreamOrDevice)
- [[`isneginf()`]](#_CPPv48isneginfRK5array14StreamOrDevice)
- [[`where()`]](#_CPPv45whereRK5arrayRK5arrayRK5array14StreamOrDevice)
- [[`nan_to_num()`]](#_CPPv410nan_to_numRK5arrayfKNSt8optionalIfEEKNSt8optionalIfEE14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5arrayb14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5array14StreamOrDevice)
- [[`allclose()`]](#_CPPv48allcloseRK5arrayRK5arrayddb14StreamOrDevice)
- [[`isclose()`]](#_CPPv47iscloseRK5arrayRK5arrayddb14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`all()`]](#_CPPv43allRK5arrayib14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5arrayb14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5array14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`any()`]](#_CPPv43anyRK5arrayib14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5arrayb14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5array14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`sum()`]](#_CPPv43sumRK5arrayib14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5arrayb14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5array14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`mean()`]](#_CPPv44meanRK5arrayib14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5arrayb14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5array14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`median()`]](#_CPPv46medianRK5arrayib14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5arraybi14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5array14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice)
- [[`var()`]](#_CPPv43varRK5arrayibi14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5arraybi14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5array14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5arrayRKNSt6vectorIiEEbi14StreamOrDevice)
- [[`std()`]](#_CPPv4StRK5arrayibi14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5arrayb14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5array14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`prod()`]](#_CPPv44prodRK5arrayib14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5arrayb14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5array14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`max()`]](#_CPPv43maxRK5arrayib14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5arrayb14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5array14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`min()`]](#_CPPv43minRK5arrayib14StreamOrDevice)
- [[`argmin()`]](#_CPPv46argminRK5arrayb14StreamOrDevice)
- [[`argmin()`]](#_CPPv46argminRK5array14StreamOrDevice)
- [[`argmin()`]](#_CPPv46argminRK5arrayib14StreamOrDevice)
- [[`argmax()`]](#_CPPv46argmaxRK5arrayb14StreamOrDevice)
- [[`argmax()`]](#_CPPv46argmaxRK5array14StreamOrDevice)
- [[`argmax()`]](#_CPPv46argmaxRK5arrayib14StreamOrDevice)
- [[`sort()`]](#_CPPv44sortRK5array14StreamOrDevice)
- [[`sort()`]](#_CPPv44sortRK5arrayi14StreamOrDevice)
- [[`argsort()`]](#_CPPv47argsortRK5array14StreamOrDevice)
- [[`argsort()`]](#_CPPv47argsortRK5arrayi14StreamOrDevice)
- [[`partition()`]](#_CPPv49partitionRK5arrayi14StreamOrDevice)
- [[`partition()`]](#_CPPv49partitionRK5arrayii14StreamOrDevice)
- [[`argpartition()`]](#_CPPv412argpartitionRK5arrayi14StreamOrDevice)
- [[`argpartition()`]](#_CPPv412argpartitionRK5arrayii14StreamOrDevice)
- [[`topk()`]](#_CPPv44topkRK5arrayi14StreamOrDevice)
- [[`topk()`]](#_CPPv44topkRK5arrayii14StreamOrDevice)
- [[`logcumsumexp()`]](#_CPPv412logcumsumexpRK5arraybb14StreamOrDevice)
- [[`logcumsumexp()`]](#_CPPv412logcumsumexpRK5arrayibb14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5arrayb14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5array14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`logsumexp()`]](#_CPPv49logsumexpRK5arrayib14StreamOrDevice)
- [[`abs()`]](#_CPPv43absRK5array14StreamOrDevice)
- [[`negative()`]](#_CPPv48negativeRK5array14StreamOrDevice)
- [[`operator-()`]](#_CPPv4miRK5array)
- [[`sign()`]](#_CPPv44signRK5array14StreamOrDevice)
- [[`logical_not()`]](#_CPPv411logical_notRK5array14StreamOrDevice)
- [[`logical_and()`]](#_CPPv411logical_andRK5arrayRK5array14StreamOrDevice)
- [[`operator&&()`]](#_CPPv4aaRK5arrayRK5array)
- [[`logical_or()`]](#_CPPv410logical_orRK5arrayRK5array14StreamOrDevice)
- [[`operator||()`]](#_CPPv4ooRK5arrayRK5array)
- [[`reciprocal()`]](#_CPPv410reciprocalRK5array14StreamOrDevice)
- [[`add()`]](#_CPPv43addRK5arrayRK5array14StreamOrDevice)
- [[`operator+()`]](#_CPPv4plRK5arrayRK5array)
- [[`operator+()`]](#_CPPv4I0Epl5array1TRK5array)
- [[`operator+()`]](#_CPPv4I0Epl5arrayRK5array1T)
- [[`subtract()`]](#_CPPv48subtractRK5arrayRK5array14StreamOrDevice)
- [[`operator-()`]](#_CPPv4miRK5arrayRK5array)
- [[`operator-()`]](#_CPPv4I0Emi5array1TRK5array)
- [[`operator-()`]](#_CPPv4I0Emi5arrayRK5array1T)
- [[`multiply()`]](#_CPPv48multiplyRK5arrayRK5array14StreamOrDevice)
- [[`operator*()`]](#_CPPv4mlRK5arrayRK5array)
- [[`operator*()`]](#_CPPv4I0Eml5array1TRK5array)
- [[`operator*()`]](#_CPPv4I0Eml5arrayRK5array1T)
- [[`divide()`]](#_CPPv46divideRK5arrayRK5array14StreamOrDevice)
- [[`operator/()`]](#_CPPv4dvRK5arrayRK5array)
- [[`operator/()`]](#_CPPv4dvdRK5array)
- [[`operator/()`]](#_CPPv4dvRK5arrayd)
- [[`divmod()`]](#_CPPv46divmodRK5arrayRK5array14StreamOrDevice)
- [[`floor_divide()`]](#_CPPv412floor_divideRK5arrayRK5array14StreamOrDevice)
- [[`remainder()`]](#_CPPv49remainderRK5arrayRK5array14StreamOrDevice)
- [[`operator%()`]](#_CPPv4rmRK5arrayRK5array)
- [[`operator%()`]](#_CPPv4I0Erm5array1TRK5array)
- [[`operator%()`]](#_CPPv4I0Erm5arrayRK5array1T)
- [[`maximum()`]](#_CPPv47maximumRK5arrayRK5array14StreamOrDevice)
- [[`minimum()`]](#_CPPv47minimumRK5arrayRK5array14StreamOrDevice)
- [[`floor()`]](#_CPPv45floorRK5array14StreamOrDevice)
- [[`ceil()`]](#_CPPv44ceilRK5array14StreamOrDevice)
- [[`square()`]](#_CPPv46squareRK5array14StreamOrDevice)
- [[`exp()`]](#_CPPv43expRK5array14StreamOrDevice)
- [[`sin()`]](#_CPPv43sinRK5array14StreamOrDevice)
- [[`cos()`]](#_CPPv43cosRK5array14StreamOrDevice)
- [[`tan()`]](#_CPPv43tanRK5array14StreamOrDevice)
- [[`arcsin()`]](#_CPPv46arcsinRK5array14StreamOrDevice)
- [[`arccos()`]](#_CPPv46arccosRK5array14StreamOrDevice)
- [[`arctan()`]](#_CPPv46arctanRK5array14StreamOrDevice)
- [[`arctan2()`]](#_CPPv47arctan2RK5arrayRK5array14StreamOrDevice)
- [[`sinh()`]](#_CPPv44sinhRK5array14StreamOrDevice)
- [[`cosh()`]](#_CPPv44coshRK5array14StreamOrDevice)
- [[`tanh()`]](#_CPPv44tanhRK5array14StreamOrDevice)
- [[`arcsinh()`]](#_CPPv47arcsinhRK5array14StreamOrDevice)
- [[`arccosh()`]](#_CPPv47arccoshRK5array14StreamOrDevice)
- [[`arctanh()`]](#_CPPv47arctanhRK5array14StreamOrDevice)
- [[`degrees()`]](#_CPPv47degreesRK5array14StreamOrDevice)
- [[`radians()`]](#_CPPv47radiansRK5array14StreamOrDevice)
- [[`log()`]](#_CPPv43logRK5array14StreamOrDevice)
- [[`log2()`]](#_CPPv44log2RK5array14StreamOrDevice)
- [[`log10()`]](#_CPPv45log10RK5array14StreamOrDevice)
- [[`log1p()`]](#_CPPv45log1pRK5array14StreamOrDevice)
- [[`logaddexp()`]](#_CPPv49logaddexpRK5arrayRK5array14StreamOrDevice)
- [[`sigmoid()`]](#_CPPv47sigmoidRK5array14StreamOrDevice)
- [[`erf()`]](#_CPPv43erfRK5array14StreamOrDevice)
- [[`erfinv()`]](#_CPPv46erfinvRK5array14StreamOrDevice)
- [[`expm1()`]](#_CPPv45expm1RK5array14StreamOrDevice)
- [[`stop_gradient()`]](#_CPPv413stop_gradientRK5array14StreamOrDevice)
- [[`round()`]](#_CPPv45roundRK5arrayi14StreamOrDevice)
- [[`round()`]](#_CPPv45roundRK5array14StreamOrDevice)
- [[`matmul()`]](#_CPPv46matmulRK5arrayRK5array14StreamOrDevice)
- [[`gather()`]](#_CPPv46gatherRK5arrayRKNSt6vectorI5arrayEERKNSt6vectorIiEERK5Shape14StreamOrDevice)
- [[`gather()`]](#_CPPv46gatherRK5arrayRK5arrayiRK5Shape14StreamOrDevice)
- [[`kron()`]](#_CPPv44kronRK5arrayRK5array14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayRK5arrayi14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayii14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayRK5array14StreamOrDevice)
- [[`take()`]](#_CPPv44takeRK5arrayi14StreamOrDevice)
- [[`take_along_axis()`]](#_CPPv415take_along_axisRK5arrayRK5arrayi14StreamOrDevice)
- [[`put_along_axis()`]](#_CPPv414put_along_axisRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_add_axis()`]](#_CPPv416scatter_add_axisRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter()`]](#_CPPv47scatterRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter()`]](#_CPPv47scatterRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_add()`]](#_CPPv411scatter_addRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_add()`]](#_CPPv411scatter_addRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_prod()`]](#_CPPv412scatter_prodRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_prod()`]](#_CPPv412scatter_prodRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_max()`]](#_CPPv411scatter_maxRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_max()`]](#_CPPv411scatter_maxRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`scatter_min()`]](#_CPPv411scatter_minRK5arrayRKNSt6vectorI5arrayEERK5arrayRKNSt6vectorIiEE14StreamOrDevice)
- [[`scatter_min()`]](#_CPPv411scatter_minRK5arrayRK5arrayRK5arrayi14StreamOrDevice)
- [[`masked_scatter()`]](#_CPPv414masked_scatterRK5arrayRK5arrayRK5array14StreamOrDevice)
- [[`sqrt()`]](#_CPPv44sqrtRK5array14StreamOrDevice)
- [[`rsqrt()`]](#_CPPv45rsqrtRK5array14StreamOrDevice)
- [[`softmax()`]](#_CPPv47softmaxRK5arrayRKNSt6vectorIiEEb14StreamOrDevice)
- [[`softmax()`]](#_CPPv47softmaxRK5arrayb14StreamOrDevice)
- [[`softmax()`]](#_CPPv47softmaxRK5arrayib14StreamOrDevice)
- [[`power()`]](#_CPPv45powerRK5arrayRK5array14StreamOrDevice)
- [[`cumsum()`]](#_CPPv46cumsumRK5arraybb14StreamOrDevice)
- [[`cumsum()`]](#_CPPv46cumsumRK5arrayibb14StreamOrDevice)
- [[`cumprod()`]](#_CPPv47cumprodRK5arraybb14StreamOrDevice)
- [[`cumprod()`]](#_CPPv47cumprodRK5arrayibb14StreamOrDevice)
- [[`cummax()`]](#_CPPv46cummaxRK5arraybb14StreamOrDevice)
- [[`cummax()`]](#_CPPv46cummaxRK5arrayibb14StreamOrDevice)
- [[`cummin()`]](#_CPPv46cumminRK5arraybb14StreamOrDevice)
- [[`cummin()`]](#_CPPv46cumminRK5arrayibb14StreamOrDevice)
- [[`conv_general()`]](#_CPPv412conv_general5array5arrayNSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEEib14StreamOrDevice)
- [[`conv_general()`]](#_CPPv412conv_generalRK5arrayRK5arrayNSt6vectorIiEENSt6vectorIiEENSt6vectorIiEENSt6vectorIiEEib14StreamOrDevice)
- [[`conv1d()`]](#_CPPv46conv1dRK5arrayRK5arrayiiii14StreamOrDevice)
- [[`conv2d()`]](#_CPPv46conv2dRK5arrayRK5arrayRKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEEi14StreamOrDevice)
- [[`conv3d()`]](#_CPPv46conv3dRK5arrayRK5arrayRKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEEi14StreamOrDevice)
- [[`conv_transpose1d()`]](#_CPPv416conv_transpose1dRK5arrayRK5arrayiiiii14StreamOrDevice)
- [[`conv_transpose2d()`]](#_CPPv416conv_transpose2dRK5arrayRK5arrayRKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEERKNSt4pairIiiEEi14StreamOrDevice)
- [[`conv_transpose3d()`]](#_CPPv416conv_transpose3dRK5arrayRK5arrayRKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEERKNSt5tupleIiiiEEi14StreamOrDevice)
- [[`quantized_matmul()`]](#_CPPv416quantized_matmul5array5array5arrayNSt8optionalI5arrayEEbNSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice)
- [[`quantize()`]](#_CPPv48quantizeRK5arrayNSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice)
- [[`dequantize()`]](#_CPPv410dequantizeRK5arrayRK5arrayRKNSt8optionalI5arrayEENSt8optionalIiEENSt8optionalIiEERKNSt6stringENSt8optionalI5DtypeEE14StreamOrDevice)
- [[`qqmm()`]](#_CPPv44qqmm5array5arrayNSt8optionalI5arrayEENSt8optionalIiEENSt8optionalIiEERKNSt6stringE14StreamOrDevice)
- [[`from_fp8()`]](#_CPPv48from_fp85array5Dtype14StreamOrDevice)
- [[`to_fp8()`]](#_CPPv46to_fp85array14StreamOrDevice)
- [[`gather_qmm()`]](#_CPPv410gather_qmmRK5arrayRK5arrayRK5arrayRKNSt8optionalI5arrayEENSt8optionalI5arrayEENSt8optionalI5arrayEEbNSt8optionalIiEENSt8optionalIiEERKNSt6stringEb14StreamOrDevice)
- [[`tensordot()`]](#_CPPv49tensordotRK5arrayRK5arrayKi14StreamOrDevice)
- [[`tensordot()`]](#_CPPv49tensordotRK5arrayRK5arrayRKNSt6vectorIiEERKNSt6vectorIiEE14StreamOrDevice)
- [[`outer()`]](#_CPPv45outerRK5arrayRK5array14StreamOrDevice)
- [[`inner()`]](#_CPPv45innerRK5arrayRK5array14StreamOrDevice)
- [[`addmm()`]](#_CPPv45addmm5array5array5arrayRKfRKf14StreamOrDevice)
- [[`block_masked_mm()`]](#_CPPv415block_masked_mm5array5arrayiNSt8optionalI5arrayEENSt8optionalI5arrayEENSt8optionalI5arrayEE14StreamOrDevice)
- [[`gather_mm()`]](#_CPPv49gather_mm5array5arrayNSt8optionalI5arrayEENSt8optionalI5arrayEEb14StreamOrDevice)
- [[`segmented_mm()`]](#_CPPv412segmented_mm5array5array5array14StreamOrDevice)
- [[`diagonal()`]](#_CPPv48diagonalRK5arrayiii14StreamOrDevice)
- [[`diag()`]](#_CPPv44diagRK5arrayi14StreamOrDevice)
- [[`trace()`]](#_CPPv45traceRK5arrayiii5Dtype14StreamOrDevice)
- [[`trace()`]](#_CPPv45traceRK5arrayiii14StreamOrDevice)
- [[`trace()`]](#_CPPv45traceRK5array14StreamOrDevice)
- [[`depends()`]](#_CPPv47dependsRKNSt6vectorI5arrayEERKNSt6vectorI5arrayEE)
- [[`atleast_1d()`]](#_CPPv410atleast_1dRK5array14StreamOrDevice)
- [[`atleast_1d()`]](#_CPPv410atleast_1dRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`atleast_2d()`]](#_CPPv410atleast_2dRK5array14StreamOrDevice)
- [[`atleast_2d()`]](#_CPPv410atleast_2dRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`atleast_3d()`]](#_CPPv410atleast_3dRK5array14StreamOrDevice)
- [[`atleast_3d()`]](#_CPPv410atleast_3dRKNSt6vectorI5arrayEE14StreamOrDevice)
- [[`number_of_elements()`]](#_CPPv418number_of_elementsRK5arrayNSt6vectorIiEEb5Dtype14StreamOrDevice)
- [[`conjugate()`]](#_CPPv49conjugateRK5array14StreamOrDevice)
- [[`bitwise_and()`]](#_CPPv411bitwise_andRK5arrayRK5array14StreamOrDevice)
- [[`operator&()`]](#_CPPv4anRK5arrayRK5array)
- [[`bitwise_or()`]](#_CPPv410bitwise_orRK5arrayRK5array14StreamOrDevice)
- [[`operator|()`]](#_CPPv4orRK5arrayRK5array)
- [[`bitwise_xor()`]](#_CPPv411bitwise_xorRK5arrayRK5array14StreamOrDevice)
- [[`operator^()`]](#_CPPv4eoRK5arrayRK5array)
- [[`left_shift()`]](#_CPPv410left_shiftRK5arrayRK5array14StreamOrDevice)
- [[`operator<<()`]](#_CPPv4lsRK5arrayRK5array)
- [[`right_shift()`]](#_CPPv411right_shiftRK5arrayRK5array14StreamOrDevice)
- [[`operator>>()`]](#_CPPv4rsRK5arrayRK5array)
- [[`bitwise_invert()`]](#_CPPv414bitwise_invertRK5array14StreamOrDevice)
- [[`operator~()`]](#_CPPv4coRK5array)
- [[`view()`]](#_CPPv44viewRK5arrayRK5Dtype14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayi14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayRK5Shape14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayii14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayiRKNSt6vectorIiEE14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayRK5Shapei14StreamOrDevice)
- [[`roll()`]](#_CPPv44rollRK5arrayRK5ShapeRKNSt6vectorIiEE14StreamOrDevice)
- [[`real()`]](#_CPPv44realRK5array14StreamOrDevice)
- [[`imag()`]](#_CPPv44imagRK5array14StreamOrDevice)
- [[`contiguous()`]](#_CPPv410contiguousRK5arrayb14StreamOrDevice)

By MLX Contributors

© Copyright 2023, Apple.\