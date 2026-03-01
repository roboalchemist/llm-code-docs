# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3

Title: r3 package - gonum.org/v1/gonum/spatial/r3 - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3

Markdown Content:
Package r3 provides 3D vectors and boxes and operations on them.

Spherically interpolate between two quaternions to obtain a rotation.

Output:

 0.00 {+1.00 -0.00 +1.41} 0.10 {+1.00 -0.33 +1.38} 0.20 {+1.00 -0.64 +1.26} 0.30 {+1.00 -0.92 +1.08} 0.40 {+1.00 -1.14 +0.83} 0.50 {+1.00 -1.31 +0.54} 0.60 {+1.00 -1.40 +0.22} 0.70 {+1.00 -1.41 -0.11} 0.80 {+1.00 -1.34 -0.44} 0.90 {+1.00 -1.21 -0.74} 1.00 {+1.00 -1.00 -1.00} 

*   [func Cos(p, q Vec) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Cos)
*   [func Divergence(p, step Vec, field func(Vec) Vec) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Divergence)
*   [func Dot(p, q Vec) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Dot)
*   [func Norm(p Vec) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Norm)
*   [func Norm2(p Vec) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Norm2)
*   [type Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)
*       *   [func NewBox(x0, y0, z0, x1, y1, z1 float64) Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#NewBox)

*       *   [func (a Box) Add(v Vec) Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Add)
    *   [func (a Box) Canon() Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Canon)
    *   [func (a Box) Center() Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Center)
    *   [func (a Box) Contains(v Vec) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Contains)
    *   [func (a Box) Empty() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Empty)
    *   [func (a Box) Scale(scale Vec) Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Scale)
    *   [func (a Box) Size() Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Size)
    *   [func (a Box) Union(b Box) Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Union)
    *   [func (a Box) Vertices() []Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box.Vertices)

*   [type Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)
*       *   [func Eye() *Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Eye)
    *   [func NewMat(val []float64) *Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#NewMat)
    *   [func Skew(v Vec) (M *Mat)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Skew)deprecated

*       *   [func (m *Mat) Add(a, b mat.Matrix)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Add)
    *   [func (m *Mat) At(i, j int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.At)
    *   [func (m *Mat) CloneFrom(a mat.Matrix)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.CloneFrom)
    *   [func (m *Mat) Det() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Det)
    *   [func (m *Mat) Dims() (r, c int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Dims)
    *   [func (m *Mat) Hessian(p, step Vec, field func(Vec) float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Hessian)
    *   [func (m *Mat) Jacobian(p, step Vec, field func(Vec) Vec)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Jacobian)
    *   [func (m *Mat) Mul(a, b mat.Matrix)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Mul)
    *   [func (m *Mat) MulVec(v Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.MulVec)
    *   [func (m *Mat) MulVecTrans(v Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.MulVecTrans)
    *   [func (m *Mat) Outer(alpha float64, x, y Vec)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Outer)
    *   [func (m *Mat) RawMatrix() blas64.General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.RawMatrix)
    *   [func (m *Mat) Scale(f float64, a mat.Matrix)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Scale)
    *   [func (m *Mat) Set(i, j int, v float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Set)
    *   [func (m *Mat) Skew(v Vec)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Skew)
    *   [func (m *Mat) Sub(a, b mat.Matrix)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.Sub)
    *   [func (m *Mat) T() mat.Matrix](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.T)
    *   [func (m *Mat) VecCol(j int) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.VecCol)
    *   [func (m *Mat) VecRow(i int) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat.VecRow)

*   [type Rotation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Rotation)
*       *   [func NewRotation(alpha float64, axis Vec) Rotation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#NewRotation)

*       *   [func (r Rotation) Mat() *Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Rotation.Mat)
    *   [func (r Rotation) Rotate(p Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Rotation.Rotate)

*   [type Triangle](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Triangle)
*       *   [func (t Triangle) Area() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Triangle.Area)
    *   [func (t Triangle) Centroid() Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Triangle.Centroid)
    *   [func (t Triangle) IsDegenerate(tol float64) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Triangle.IsDegenerate)
    *   [func (t Triangle) Normal() Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Triangle.Normal)

*   [type Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)
*       *   [func Add(p, q Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Add)
    *   [func Cross(p, q Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Cross)
    *   [func Gradient(p, step Vec, field func(Vec) float64) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Gradient)
    *   [func Rotate(p Vec, alpha float64, axis Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Rotate)
    *   [func Scale(f float64, p Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Scale)
    *   [func Sub(p, q Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Sub)
    *   [func Unit(p Vec) Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Unit)

*   [Package (Slerp)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#example-package-Slerp)
*   [Rotation (EulerAngles)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#example-Rotation-EulerAngles)
*   [Triangle (Icosphere)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#example-Triangle-Icosphere)

This section is empty.

This section is empty.

Cos returns the cosine of the opening angle between p and q.

func Divergence(p, step [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec), field func([Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [float64](https://pkg.go.dev/builtin#float64)

Divergence returns the divergence of the vector field at the point p, approximated using finite differences with the given step sizes.

Dot returns the dot product p·q.

Norm returns the Euclidean norm of p

|p| = sqrt(p_x^2 + p_y^2 + p_z^2).

Norm2 returns the Euclidean squared norm of p

|p|^2 = p_x^2 + p_y^2 + p_z^2.

type Box struct {
 Min, Max [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)}

Box is a 3D bounding box. Well formed Boxes Min components are smaller than Max components.

func NewBox(x0, y0, z0, x1, y1, z1 [float64](https://pkg.go.dev/builtin#float64)) [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)

NewBox is shorthand for Box{Min:Vec{x0,y0,z0}, Max:Vec{x1,y1,z1}}. The sides are swapped so that the resulting Box is well formed.

func (a [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) Add(v [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)

Add adds v to the bounding box components. It is the equivalent of translating the Box by v.

Canon returns the canonical version of a. The returned Box has minimum and maximum coordinates swapped if necessary so that it is well-formed.

func (a [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) Center() [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

Center returns the center of the Box.

func (a [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) Contains(v [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [bool](https://pkg.go.dev/builtin#bool)

Contains returns true if v is contained within the bounds of the Box.

func (a [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) Empty() [bool](https://pkg.go.dev/builtin#bool)

Empty returns true if a Box's volume is zero or if a Min component is greater than its Max component.

func (a [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) Scale(scale [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)

Scale returns a new Box scaled by a size vector around its center. The scaling is done element wise which is to say the Box's X dimension is scaled by scale.X. Negative elements of scale are interpreted as zero.

Size returns the size of the Box.

func (a [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) Union(b [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)

Union returns a box enclosing both the receiver and argument Boxes.

func (a [Box](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Box)) Vertices() [][Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

Vertices returns a slice of the 8 vertices corresponding to each of the Box's corners.

Ordering of vertices 0-3 is CCW in the XY plane starting at box minimum. Ordering of vertices 4-7 is CCW in the XY plane starting at box minimum for X and Y values and maximum Z value.

Edges for the box can be constructed with the following indices:

edges := [12][2]int{
 {0, 1}, {1, 2}, {2, 3}, {3, 0},
 {4, 5}, {5, 6}, {6, 7}, {7, 4},
 {0, 4}, {1, 5}, {2, 6}, {3, 7},
}

type Mat struct {
	
}

Mat represents a 3×3 matrix. Useful for rotation matrices and such. The zero value is usable as the 3×3 zero matrix.

Eye returns the 3×3 Identity matrix

NewMat returns a new 3×3 matrix Mat type and populates its elements with values passed as argument in row-major form. If val argument is nil then NewMat returns a matrix filled with zeros.

func Skew(v [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) (M *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat))

Skew returns the 3×3 skew symmetric matrix (right hand system) of v.

                ⎡ 0 -z  y⎤
Skew({x,y,z}) = ⎢ z  0 -x⎥
                ⎣-y  x  0⎦

Deprecated: use Mat.Skew()

Add adds a and b element-wise, placing the result in the receiver. Add will panic if the two matrices do not have the same shape.

At returns the value of a matrix element at row i, column j. At expects indices in the range [0,2]. It will panic if i or j are out of bounds for the matrix.

CloneFrom makes a copy of a into the receiver m. Mat expects a 3×3 input matrix.

Det calculates the determinant of the receiver using the following formula

    ⎡a b c⎤
m = ⎢d e f⎥
    ⎣g h i⎦
det(m) = a(ei − fh) − b(di − fg) + c(dh − eg)

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) Dims() (r, c [int](https://pkg.go.dev/builtin#int))

Dims returns the number of rows and columns of this matrix. This method will always return 3×3 for a Mat.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) Hessian(p, step [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec), field func([Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [float64](https://pkg.go.dev/builtin#float64))

Hessian sets the receiver to the Hessian matrix of the scalar field at the point p, approximated using finite differences with the given step sizes. The field is evaluated at points in the area surrounding p by adding at most 2 components of step to p. Hessian expects the field's second partial derivatives are all continuous for correct results.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) Jacobian(p, step [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec), field func([Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec))

Jacobian sets the receiver to the Jacobian matrix of the vector field at the point p, approximated using finite differences with the given step sizes.

The Jacobian matrix J is the matrix of all first-order partial derivatives of f. If f maps an 3-dimensional vector x to an 3-dimensional vector y = f(x), J is a 3×3 matrix whose elements are given as

J_{i,j} = ∂f_i/∂x_j,

or expanded out

    [ ∂f_1/∂x_1 ∂f_1/∂x_2 ∂f_1/∂x_3 ]
J = [ ∂f_2/∂x_1 ∂f_2/∂x_2 ∂f_2/∂x_3 ]
    [ ∂f_3/∂x_1 ∂f_3/∂x_2 ∂f_3/∂x_3 ]

Jacobian expects the field's first order partial derivatives are all continuous for correct results.

Mul takes the matrix product of a and b, placing the result in the receiver. If the number of columns in a does not equal 3, Mul will panic.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) MulVec(v [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

MulVec returns the matrix-vector product M⋅v.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) MulVecTrans(v [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

MulVecTrans returns the matrix-vector product Mᵀ⋅v.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) Outer(alpha [float64](https://pkg.go.dev/builtin#float64), x, y [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec))

Outer calculates the outer product of the vectors x and y, where x and y are treated as column vectors, and stores the result in the receiver.

m = alpha * x * yᵀ

RawMatrix returns the blas representation of the matrix with the backing data of this matrix. Changes to the returned matrix will be reflected in the receiver.

Scale multiplies the elements of a by f, placing the result in the receiver.

See the mat.Scaler interface for more information.

Set sets the element at row i, column j to the value v.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) Skew(v [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec))

Skew sets the receiver to the 3×3 skew symmetric matrix (right hand system) of v.

                ⎡ 0 -z  y⎤
Skew({x,y,z}) = ⎢ z  0 -x⎥
                ⎣-y  x  0⎦

Sub subtracts the matrix b from a, placing the result in the receiver. Sub will panic if the two matrices do not have the same shape.

T returns the transpose of Mat. Changes in the receiver will be reflected in the returned matrix.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) VecCol(j [int](https://pkg.go.dev/builtin#int)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

VecCol returns the elements in the jth column of the receiver.

func (m *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)) VecRow(i [int](https://pkg.go.dev/builtin#int)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

VecRow returns the elements in the ith row of the receiver.

Rotation describes a rotation in space.

Output:

 rotate around x-axis: {1.00 0.00 0.00} rotate around y-axis: {0.71 0.00 -0.71} rotate around z-axis: {0.71 0.71 0.00} rotate around x+y-axes: {0.71 0.00 -0.71} rotate around x+z-axes: {0.71 0.71 0.00} rotate around y+z-axes: {0.50 0.50 -0.71} rotate around y-axis to singularity: {0.00 0.00 -1.00} rotate around x+y-axes with singularity → gimbal lock: {0.00 0.00 -1.00} rotate around z+y-axes with singularity → gimbal lock: {0.00 0.00 -1.00} rotate around all-axes with singularity → gimbal lock: {0.00 0.00 -1.00} 

NewRotation creates a rotation by alpha, around axis.

func (r [Rotation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Rotation)) Mat() *[Mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Mat)

Mat returns a 3×3 rotation matrix corresponding to the receiver. It may be used to perform rotations on a 3-vector or to apply the rotation to a 3×n matrix of column vectors. If the receiver is not a unit quaternion, the returned matrix will not be a pure rotation.

func (r [Rotation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Rotation)) Rotate(p [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

Rotate returns p rotated according to the parameters used to construct the receiver.

Triangle represents a triangle in 3D space and is composed by 3 vectors corresponding to the position of each of the vertices. Ordering of these vertices decides the "normal" direction. Inverting ordering of two vertices inverts the resulting direction.

Area returns the surface area of the triangle.

func (t [Triangle](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Triangle)) Centroid() [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

Centroid returns the intersection of the three medians of the triangle as a point in space.

IsDegenerate returns true if all of triangle's vertices are within tol distance of its longest side.

func (t [Triangle](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Triangle)) Normal() [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

Normal returns the vector with direction perpendicular to the Triangle's face and magnitude twice that of the Triangle's area. The ordering of the triangle vertices decides the normal's resulting direction. The returned vector is not normalized.

type Vec struct {
 X, Y, Z [float64](https://pkg.go.dev/builtin#float64)}

Vec is a 3D vector.

Add returns the vector sum of p and q.

Cross returns the cross product p×q.

func Gradient(p, step [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec), field func([Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)) [float64](https://pkg.go.dev/builtin#float64)) [Vec](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/spatial/r3#Vec)

Gradient returns the gradient of the scalar field at the point p, approximated using finite differences with the given step sizes.

Rotate returns a new vector, rotated by alpha around the provided axis.

Scale returns the vector p scaled by f.

Sub returns the vector sum of p and -q.

Unit returns the unit vector colinear to p. Unit returns {NaN,NaN,NaN} for the zero vector.
