rapier3d

# Module utils

Source

## Modules§

serdeHelpers around serialization.

## Constants§

DIM_MINUS_ONEDimension minus one (1 for 2D, 2 for 3D).

## Traits§

AngularInertiaOpsTrait for angular inertia operations.ComponentMulExtension trait for element-wise vector operationsCopySignTrait to copy the sign of each component of one scalar/vector/matrix to another.CrossProductTrait for computing generalized cross products.CrossProductMatrixTrait for computing cross product matrices.DotProductTrait for computing generalized dot products.IndexMut2Methods for simultaneously indexing a container with two distinct indices.MatrixColumnExtension trait for matrix column access (like nalgebra’s `.column()`)OrthonormalBasisTrait to compute the orthonormal basis of a vector.PoseOpsTrait for pose types (isometry) providing access to rotation and translation.RotationOpsTrait implemented by quaternions.ScalarTypeTrait for types that can be used as scalars in the generic code supporting both
the scalar and AoSoA SIMD pattern.SimdLengthTrait for computing generalized lengths.SimdRealCopyThe trait for real numbers used by Rapier.SimdSelectTrait for conditional selection between two values.

## Functions§

mat_to_naConvert glam Matrix to nalgebra `Matrix3<Real>` (3D matrix)smallest_abs_diff_between_anglesCalculate the difference with smallest absolute value between the two given angles.smallest_abs_diff_between_sin_anglesCalculate the difference with smallest absolute value between the two given values.try_normalize_and_get_lengthTry to normalize a vector and return both the normalized vector and the original length.vect_to_naConvert glam Vector to nalgebra `SimdVector<Real>`
