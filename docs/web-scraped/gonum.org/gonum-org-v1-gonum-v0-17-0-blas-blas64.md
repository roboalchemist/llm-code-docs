# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64

Title: blas64 package - gonum.org/v1/gonum/blas/blas64 - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64

Markdown Content:
Package blas64 provides a simple interface to the float64 BLAS API.

*   [func Asum(x Vector) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Asum)
*   [func Axpy(alpha float64, x, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Axpy)
*   [func Copy(x, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Copy)
*   [func Dot(x, y Vector) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Dot)
*   [func Gbmv(t blas.Transpose, alpha float64, a Band, x Vector, beta float64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Gbmv)
*   [func Gemm(tA, tB blas.Transpose, alpha float64, a, b General, beta float64, c General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Gemm)
*   [func Gemv(t blas.Transpose, alpha float64, a General, x Vector, beta float64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Gemv)
*   [func Ger(alpha float64, x, y Vector, a General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Ger)
*   [func Iamax(x Vector) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Iamax)
*   [func Implementation() blas.Float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Implementation)
*   [func Nrm2(x Vector) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Nrm2)
*   [func Rot(x, y Vector, c, s float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Rot)
*   [func Rotg(a, b float64) (c, s, r, z float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Rotg)
*   [func Rotm(x, y Vector, p blas.DrotmParams)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Rotm)
*   [func Rotmg(d1, d2, b1, b2 float64) (p blas.DrotmParams, rd1, rd2, rb1 float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Rotmg)
*   [func Sbmv(alpha float64, a SymmetricBand, x Vector, beta float64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Sbmv)
*   [func Scal(alpha float64, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Scal)
*   [func Spmv(alpha float64, a SymmetricPacked, x Vector, beta float64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Spmv)
*   [func Spr(alpha float64, x Vector, a SymmetricPacked)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Spr)
*   [func Spr2(alpha float64, x, y Vector, a SymmetricPacked)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Spr2)
*   [func Swap(x, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Swap)
*   [func Symm(s blas.Side, alpha float64, a Symmetric, b General, beta float64, c General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Symm)
*   [func Symv(alpha float64, a Symmetric, x Vector, beta float64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Symv)
*   [func Syr(alpha float64, x Vector, a Symmetric)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Syr)
*   [func Syr2(alpha float64, x, y Vector, a Symmetric)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Syr2)
*   [func Syr2k(t blas.Transpose, alpha float64, a, b General, beta float64, c Symmetric)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Syr2k)
*   [func Syrk(t blas.Transpose, alpha float64, a General, beta float64, c Symmetric)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Syrk)
*   [func Tbmv(t blas.Transpose, a TriangularBand, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Tbmv)
*   [func Tbsv(t blas.Transpose, a TriangularBand, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Tbsv)
*   [func Tpmv(t blas.Transpose, a TriangularPacked, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Tpmv)
*   [func Tpsv(t blas.Transpose, a TriangularPacked, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Tpsv)
*   [func Trmm(s blas.Side, tA blas.Transpose, alpha float64, a Triangular, b General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Trmm)
*   [func Trmv(t blas.Transpose, a Triangular, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Trmv)
*   [func Trsm(s blas.Side, tA blas.Transpose, alpha float64, a Triangular, b General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Trsm)
*   [func Trsv(t blas.Transpose, a Triangular, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Trsv)
*   [func Use(b blas.Float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Use)
*   [type Band](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Band)
*       *   [func (t Band) From(a BandCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Band.From)

*   [type BandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#BandCols)
*       *   [func (t BandCols) From(a Band)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#BandCols.From)

*   [type General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#General)
*       *   [func (t General) From(a GeneralCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#General.From)

*   [type GeneralCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#GeneralCols)
*       *   [func (t GeneralCols) From(a General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#GeneralCols.From)

*   [type Symmetric](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Symmetric)
*       *   [func (t Symmetric) From(a SymmetricCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Symmetric.From)

*   [type SymmetricBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBand)
*       *   [func (t SymmetricBand) From(a SymmetricBandCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBand.From)

*   [type SymmetricBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBandCols)
*       *   [func (t SymmetricBandCols) From(a SymmetricBand)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBandCols.From)

*   [type SymmetricCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricCols)
*       *   [func (t SymmetricCols) From(a Symmetric)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricCols.From)

*   [type SymmetricPacked](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricPacked)
*   [type Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Triangular)
*       *   [func (t Triangular) From(a TriangularCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Triangular.From)

*   [type TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBand)
*       *   [func (t TriangularBand) From(a TriangularBandCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBand.From)

*   [type TriangularBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBandCols)
*       *   [func (t TriangularBandCols) From(a TriangularBand)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBandCols.From)

*   [type TriangularCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularCols)
*       *   [func (t TriangularCols) From(a Triangular)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularCols.From)

*   [type TriangularPacked](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularPacked)
*   [type Vector](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Vector)

This section is empty.

This section is empty.

Asum computes the sum of the absolute values of the elements of x:

\sum_i |x[i]|.

Asum will panic if the vector increment is negative.

Axpy adds x scaled by alpha to y:

y[i] += alpha*x[i] for all i.

Axpy will panic if the lengths of x and y do not match.

Copy copies the elements of x into the elements of y:

y[i] = x[i] for all i.

Copy will panic if the lengths of x and y do not match.

Dot computes the dot product of the two vectors:

\sum_i x[i]*y[i].

Dot will panic if the lengths of x and y do not match.

Gbmv computes

y = alpha * A * x + beta * y   if t == blas.NoTrans,
y = alpha * Aᵀ * x + beta * y  if t == blas.Trans or blas.ConjTrans,

where A is an m×n band matrix, x and y are vectors, and alpha and beta are scalars.

Gemm computes

C = alpha * A * B + beta * C,

where A, B, and C are dense matrices, and alpha and beta are scalars. tA and tB specify whether A or B are transposed.

Gemv computes

y = alpha * A * x + beta * y   if t == blas.NoTrans,
y = alpha * Aᵀ * x + beta * y  if t == blas.Trans or blas.ConjTrans,

where A is an m×n dense matrix, x and y are vectors, and alpha and beta are scalars.

Ger performs a rank-1 update

A += alpha * x * yᵀ,

where A is an m×n dense matrix, x and y are vectors, and alpha is a scalar.

Iamax returns the index of an element of x with the largest absolute value. If there are multiple such indices the earliest is returned. Iamax returns -1 if n == 0.

Iamax will panic if the vector increment is negative.

Implementation returns the current BLAS float64 implementation.

Implementation allows direct calls to the current BLAS float64 implementation giving finer control of parameters.

Nrm2 computes the Euclidean norm of the vector x:

sqrt(\sum_i x[i]*x[i]).

Nrm2 will panic if the vector increment is negative.

Rot applies a plane transformation to n points represented by the vectors x and y:

x[i] =  c*x[i] + s*y[i],
y[i] = -s*x[i] + c*y[i], for all i.

Rotg computes the parameters of a Givens plane rotation so that

⎡ c s⎤   ⎡a⎤   ⎡r⎤
⎣-s c⎦ * ⎣b⎦ = ⎣0⎦

where a and b are the Cartesian coordinates of a given point. c, s, and r are defined as

r = ±Sqrt(a^2 + b^2),
c = a/r, the cosine of the rotation angle,
s = a/r, the sine of the rotation angle,

and z is defined such that

if |a| > |b|,        z = s,
otherwise if c != 0, z = 1/c,
otherwise            z = 1.

Rotm applies the modified Givens rotation to n points represented by the vectors x and y.

Sbmv performs

y = alpha * A * x + beta * y,

where A is an n×n symmetric band matrix, x and y are vectors, and alpha and beta are scalars.

Scal scales the vector x by alpha:

x[i] *= alpha for all i.

Scal will panic if the vector increment is negative.

Spmv performs

y = alpha * A * x + beta * y,

where A is an n×n symmetric matrix in packed format, x and y are vectors, and alpha and beta are scalars.

Spr performs the rank-1 update

A += alpha * x * xᵀ,

where A is an n×n symmetric matrix in packed format, x is a vector, and alpha is a scalar.

Spr2 performs a rank-2 update

A += alpha * x * yᵀ + alpha * y * xᵀ,

where A is an n×n symmetric matrix in packed format, x and y are vectors, and alpha is a scalar.

Swap exchanges the elements of the two vectors:

x[i], y[i] = y[i], x[i] for all i.

Swap will panic if the lengths of x and y do not match.

Symm performs

C = alpha * A * B + beta * C  if s == blas.Left,
C = alpha * B * A + beta * C  if s == blas.Right,

where A is an n×n or m×m symmetric matrix, B and C are m×n matrices, and alpha is a scalar.

Symv computes

y = alpha * A * x + beta * y,

where A is an n×n symmetric matrix, x and y are vectors, and alpha and beta are scalars.

Syr performs a rank-1 update

A += alpha * x * xᵀ,

where A is an n×n symmetric matrix, x is a vector, and alpha is a scalar.

Syr2 performs a rank-2 update

A += alpha * x * yᵀ + alpha * y * xᵀ,

where A is a symmetric n×n matrix, x and y are vectors, and alpha is a scalar.

Syr2k performs a symmetric rank-2k update

C = alpha * A * Bᵀ + alpha * B * Aᵀ + beta * C  if t == blas.NoTrans,
C = alpha * Aᵀ * B + alpha * Bᵀ * A + beta * C  if t == blas.Trans or blas.ConjTrans,

where C is an n×n symmetric matrix, A and B are n×k matrices if t == NoTrans and k×n matrices otherwise, and alpha and beta are scalars.

Syrk performs a symmetric rank-k update

C = alpha * A * Aᵀ + beta * C  if t == blas.NoTrans,
C = alpha * Aᵀ * A + beta * C  if t == blas.Trans or blas.ConjTrans,

where C is an n×n symmetric matrix, A is an n×k matrix if t == blas.NoTrans and a k×n matrix otherwise, and alpha and beta are scalars.

Tbmv computes

x = A * x   if t == blas.NoTrans,
x = Aᵀ * x  if t == blas.Trans or blas.ConjTrans,

where A is an n×n triangular band matrix, and x is a vector.

Tbsv solves

A * x = b   if t == blas.NoTrans,
Aᵀ * x = b  if t == blas.Trans or blas.ConjTrans,

where A is an n×n triangular band matrix, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Tpmv computes

x = A * x   if t == blas.NoTrans,
x = Aᵀ * x  if t == blas.Trans or blas.ConjTrans,

where A is an n×n triangular matrix in packed format, and x is a vector.

Tpsv solves

A * x = b   if t == blas.NoTrans,
Aᵀ * x = b  if t == blas.Trans or blas.ConjTrans,

where A is an n×n triangular matrix in packed format, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Trmm performs

B = alpha * A * B   if tA == blas.NoTrans and s == blas.Left,
B = alpha * Aᵀ * B  if tA == blas.Trans or blas.ConjTrans, and s == blas.Left,
B = alpha * B * A   if tA == blas.NoTrans and s == blas.Right,
B = alpha * B * Aᵀ  if tA == blas.Trans or blas.ConjTrans, and s == blas.Right,

where A is an n×n or m×m triangular matrix, B is an m×n matrix, and alpha is a scalar.

Trmv computes

x = A * x   if t == blas.NoTrans,
x = Aᵀ * x  if t == blas.Trans or blas.ConjTrans,

where A is an n×n triangular matrix, and x is a vector.

Trsm solves

A * X = alpha * B   if tA == blas.NoTrans and s == blas.Left,
Aᵀ * X = alpha * B  if tA == blas.Trans or blas.ConjTrans, and s == blas.Left,
X * A = alpha * B   if tA == blas.NoTrans and s == blas.Right,
X * Aᵀ = alpha * B  if tA == blas.Trans or blas.ConjTrans, and s == blas.Right,

where A is an n×n or m×m triangular matrix, X and B are m×n matrices, and alpha is a scalar.

At entry to the function, X contains the values of B, and the result is stored in-place into X.

No check is made that A is invertible.

Trsv solves

A * x = b   if t == blas.NoTrans,
Aᵀ * x = b  if t == blas.Trans or blas.ConjTrans,

where A is an n×n triangular matrix, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Use sets the BLAS float64 implementation to be used by subsequent BLAS calls. The default implementation is gonum.org/v1/gonum/blas/gonum.Implementation.

#### type [Band](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/blas64.go#L44)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Band "Go to Band")

Band represents a band matrix using the band storage scheme.

#### func (Band) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv.go#L152)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Band.From "Go to Band.From")

func (t [Band](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Band)) From(a [BandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#BandCols))

From fills the receiver with elements from a. The receiver must have the same dimensions and bandwidth as a and have adequate backing data storage.

#### type [BandCols](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv.go#L124)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#BandCols "Go to BandCols")

BandCols represents a matrix using the band column-major storage scheme.

#### func (BandCols) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv.go#L129)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#BandCols.From "Go to BandCols.From")

func (t [BandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#BandCols)) From(a [Band](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Band))

From fills the receiver with elements from a. The receiver must have the same dimensions and bandwidth as a and have adequate backing data storage.

General represents a matrix using the conventional storage scheme.

func (t [General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#General)) From(a [GeneralCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#GeneralCols))

From fills the receiver with elements from a. The receiver must have the same dimensions as a and have adequate backing data storage.

GeneralCols represents a matrix using the conventional column-major storage scheme.

func (t [GeneralCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#GeneralCols)) From(a [General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#General))

From fills the receiver with elements from a. The receiver must have the same dimensions as a and have adequate backing data storage.

Symmetric represents a symmetric matrix using the conventional storage scheme.

func (t [Symmetric](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Symmetric)) From(a [SymmetricCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricCols))

From fills the receiver with elements from a. The receiver must have the same dimensions and uplo as a and have adequate backing data storage.

#### type [SymmetricBand](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/blas64.go#L86)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBand "Go to SymmetricBand")

SymmetricBand represents a symmetric matrix using the band storage scheme.

#### func (SymmetricBand) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv_symmetric.go#L116)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBand.From "Go to SymmetricBand.From")

func (t [SymmetricBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBand)) From(a [SymmetricBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBandCols))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

#### type [SymmetricBandCols](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv_symmetric.go#L69)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBandCols "Go to SymmetricBandCols")

type SymmetricBandCols [SymmetricBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBand)

SymmetricBandCols represents a symmetric matrix using the band column-major storage scheme.

#### func (SymmetricBandCols) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv_symmetric.go#L74)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBandCols.From "Go to SymmetricBandCols.From")

func (t [SymmetricBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBandCols)) From(a [SymmetricBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricBand))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

type SymmetricCols [Symmetric](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Symmetric)

SymmetricCols represents a matrix using the conventional column-major storage scheme.

func (t [SymmetricCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#SymmetricCols)) From(a [Symmetric](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Symmetric))

From fills the receiver with elements from a. The receiver must have the same dimensions and uplo as a and have adequate backing data storage.

SymmetricPacked represents a symmetric matrix using the packed storage scheme.

Triangular represents a triangular matrix using the conventional storage scheme.

func (t [Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Triangular)) From(a [TriangularCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularCols))

From fills the receiver with elements from a. The receiver must have the same dimensions, uplo and diag as a and have adequate backing data storage.

#### type [TriangularBand](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/blas64.go#L61)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBand "Go to TriangularBand")

TriangularBand represents a triangular matrix using the band storage scheme.

#### func (TriangularBand) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv.go#L223)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBand.From "Go to TriangularBand.From")

func (t [TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBand)) From(a [TriangularBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBandCols))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

#### type [TriangularBandCols](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv.go#L173)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBandCols "Go to TriangularBandCols")

type TriangularBandCols [TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBand)

TriangularBandCols represents a triangular matrix using the band column-major storage scheme.

#### func (TriangularBandCols) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/blas64/conv.go#L178)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBandCols.From "Go to TriangularBandCols.From")

func (t [TriangularBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBandCols)) From(a [TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularBand))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

type TriangularCols [Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Triangular)

TriangularCols represents a matrix using the conventional column-major storage scheme.

func (t [TriangularCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#TriangularCols)) From(a [Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#Triangular))

From fills the receiver with elements from a. The receiver must have the same dimensions, uplo and diag as a and have adequate backing data storage.

TriangularPacked represents a triangular matrix using the packed storage scheme.

Vector represents a vector with an associated element increment.
