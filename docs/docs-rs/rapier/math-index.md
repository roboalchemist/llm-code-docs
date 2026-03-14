rapier3d

# Module math

Source

## Re-exports§

`pub use parry::glamx;``pub use f32 as Real;``pub use i32 as Int;`

## Structs§

Mat2A 2x2 column major matrix.Mat3A 3x3 column major matrix.Pose2A 2D pose (rotation + translation), representing a rigid body transformation (f32 precision).Pose3A 3D pose (rotation + translation), representing a rigid body transformation (f32 precision).Rot2A 2D rotation represented as a unit complex number (f32 precision).SimdBoolAn SIMD boolean structure associated to `wide::f32x4` that implements all the relevant traits from `simba`.SimdRealA wrapper type of `wide::f32x4` that implements all the relevant traits from `num` and `simba`.SymmetricEigen2The eigen decomposition of a symmetric 2x2 matrix (f32 precision).SymmetricEigen3The eigen decomposition of a symmetric 3x3 matrix (f32 precision).Vec2A 2-dimensional vector.Vec3A 3-dimensional vector.Vec4A 4-dimensional vector.Vec3AA 3-dimensional vector.

## Constants§

ANG_DIMThe maximum number of rotational degrees of freedom of a rigid-body.DEFAULT_EPSILONThe default tolerance used for geometric operations.DIMThe dimension of the space.MAX_MANIFOLD_POINTSMax number of pairs of contact points from the same
contact manifold that can be solved as part of a
single contact constraint.SIMD_LAST_INDEXSIMD_WIDTH - 1SIMD_WIDTHThe number of lanes of a SIMD number.SPATIAL_DIMThe maximum number of possible rotations and translations of a rigid body.TWO_DIMThe dimension of the space multiplied by two.

## Traits§

ComplexFieldTrait shared by all complex fields and its subfields (like real numbers).MatExtExtension trait for square matrix types.RealFieldTrait shared by all reals.VectorExtExtension trait for glam vector types to provide additional functionality.

## Functions§

ivect_to_vectConverts an integer vector to a floating-point vector.orthonormal_subspace_basisComputes an orthonormal basis for the subspace orthogonal to the given vectors.
Calls the callback `f` with each basis vector.rotation_from_angleCreates a rotation from an angular vector.vect_to_ivectConverts a floating-point vector to an integer vector.

## Type Aliases§

AngDimThe angular dimension type constant (U3 for 3D).AngVectorThe angular vector type.AngularInertiaThe angular inertia of a rigid body.CrossMatrixA matrix that represent the cross product with a given vector.DMatrixDynamic matrix type for multibody/solver codeDVectorDynamic vector type for multibody/solver codeDimThe dimension type constant (U3 for 3D).IVectorThe integer vector type.JacobianThe type of a constraint Jacobian in twist coordinates.JacobianViewThe type of a slice of the constraint Jacobian in twist coordinates.JacobianViewMutThe type of a mutable slice of the constraint Jacobian in twist coordinates.MatrixThe matrix type.Matrix2A 2x2 matrix type for use in any dimension context.Matrix3A 3x3 matrix type for use in any dimension context.OrientationThe orientation type.PoseThe transformation matrix type (pose = rotation + translation).PrincipalAngularInertiaThe principal angular inertia of a rigid body.Rot3A 3D rotation represented as a unit quaternion (f32 precision).RotationThe rotation type.SdpMatrixA 3D symmetric-definite-positive matrix.SimdAngVectorGeneric angular vector type (nalgebra) for SoA SIMD codeSimdAngularInertiaGeneric angular inertia type for SoA SIMD code (scalar in 2D, SdpMatrix3 in 3D)SimdMatrixGeneric 2D/3D square matrix for SoA SIMD codeSimdPointGeneric point type (nalgebra) for SoA SIMD codeSimdPoseGeneric isometry type (nalgebra) for SoA SIMD codeSimdRotationGeneric rotation type (nalgebra) for SoA SIMD codeSimdVectorGeneric vector type (nalgebra) for SoA SIMD codeSpatialVectorA vector with a dimension equal to the maximum number of degrees of freedom of a rigid body.SymmetricEigenThe result of eigendecomposition of a symmetric matrix.TangentImpulseThe type of impulse applied for friction constraints.VectorThe vector type.Vector2A 2D vector type for use in any dimension context.Vector3A 3D vector type for use in any dimension context.
