# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64

Title: cblas64 package - gonum.org/v1/gonum/blas/cblas64 - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64

Markdown Content:
Package cblas64 provides a simple interface to the complex64 BLAS API.

*   [func Asum(x Vector) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Asum)
*   [func Axpy(alpha complex64, x, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Axpy)
*   [func Copy(x, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Copy)
*   [func Dotc(x, y Vector) complex64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Dotc)
*   [func Dotu(x, y Vector) complex64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Dotu)
*   [func Dscal(alpha float32, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Dscal)
*   [func Gbmv(t blas.Transpose, alpha complex64, a Band, x Vector, beta complex64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Gbmv)
*   [func Gemm(tA, tB blas.Transpose, alpha complex64, a, b General, beta complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Gemm)
*   [func Gemv(t blas.Transpose, alpha complex64, a General, x Vector, beta complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Gemv)
*   [func Gerc(alpha complex64, x, y Vector, a General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Gerc)
*   [func Geru(alpha complex64, x, y Vector, a General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Geru)
*   [func Hbmv(alpha complex64, a HermitianBand, x Vector, beta complex64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hbmv)
*   [func Hemm(s blas.Side, alpha complex64, a Hermitian, b General, beta complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hemm)
*   [func Hemv(alpha complex64, a Hermitian, x Vector, beta complex64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hemv)
*   [func Her(alpha float32, x Vector, a Hermitian)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Her)
*   [func Her2(alpha complex64, x, y Vector, a Hermitian)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Her2)
*   [func Her2k(t blas.Transpose, alpha complex64, a, b General, beta float32, c Hermitian)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Her2k)
*   [func Herk(t blas.Transpose, alpha float32, a General, beta float32, c Hermitian)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Herk)
*   [func Hpmv(alpha complex64, a HermitianPacked, x Vector, beta complex64, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hpmv)
*   [func Hpr(alpha float32, x Vector, a HermitianPacked)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hpr)
*   [func Hpr2(alpha complex64, x, y Vector, a HermitianPacked)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hpr2)
*   [func Iamax(x Vector) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Iamax)
*   [func Implementation() blas.Complex64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Implementation)
*   [func Nrm2(x Vector) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Nrm2)
*   [func Scal(alpha complex64, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Scal)
*   [func Swap(x, y Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Swap)
*   [func Symm(s blas.Side, alpha complex64, a Symmetric, b General, beta complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Symm)
*   [func Syr2k(t blas.Transpose, alpha complex64, a, b General, beta complex64, c Symmetric)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Syr2k)
*   [func Syrk(t blas.Transpose, alpha complex64, a General, beta complex64, c Symmetric)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Syrk)
*   [func Tbmv(t blas.Transpose, a TriangularBand, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Tbmv)
*   [func Tbsv(t blas.Transpose, a TriangularBand, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Tbsv)
*   [func Tpmv(t blas.Transpose, a TriangularPacked, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Tpmv)
*   [func Tpsv(t blas.Transpose, a TriangularPacked, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Tpsv)
*   [func Trmm(s blas.Side, tA blas.Transpose, alpha complex64, a Triangular, b General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Trmm)
*   [func Trmv(t blas.Transpose, a Triangular, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Trmv)
*   [func Trsm(s blas.Side, tA blas.Transpose, alpha complex64, a Triangular, b General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Trsm)
*   [func Trsv(t blas.Transpose, a Triangular, x Vector)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Trsv)
*   [func Use(b blas.Complex64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Use)
*   [type Band](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Band)
*       *   [func (t Band) From(a BandCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Band.From)

*   [type BandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#BandCols)
*       *   [func (t BandCols) From(a Band)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#BandCols.From)

*   [type General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#General)
*       *   [func (t General) From(a GeneralCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#General.From)

*   [type GeneralCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#GeneralCols)
*       *   [func (t GeneralCols) From(a General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#GeneralCols.From)

*   [type Hermitian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hermitian)
*       *   [func (t Hermitian) From(a HermitianCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hermitian.From)

*   [type HermitianBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBand)
*       *   [func (t HermitianBand) From(a HermitianBandCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBand.From)

*   [type HermitianBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBandCols)
*       *   [func (t HermitianBandCols) From(a HermitianBand)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBandCols.From)

*   [type HermitianCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianCols)
*       *   [func (t HermitianCols) From(a Hermitian)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianCols.From)

*   [type HermitianPacked](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianPacked)
*   [type Symmetric](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Symmetric)
*   [type SymmetricBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#SymmetricBand)
*   [type SymmetricPacked](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#SymmetricPacked)
*   [type Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Triangular)
*       *   [func (t Triangular) From(a TriangularCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Triangular.From)

*   [type TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBand)
*       *   [func (t TriangularBand) From(a TriangularBandCols)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBand.From)

*   [type TriangularBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBandCols)
*       *   [func (t TriangularBandCols) From(a TriangularBand)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBandCols.From)

*   [type TriangularCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularCols)
*       *   [func (t TriangularCols) From(a Triangular)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularCols.From)

*   [type TriangularPacked](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularPacked)
*   [type Vector](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Vector)

This section is empty.

This section is empty.

Asum computes the sum of magnitudes of the real and imaginary parts of elements of the vector x:

\sum_i (|Re x[i]| + |Im x[i]|).

Asum will panic if the vector increment is negative.

Axpy computes

y = alpha * x + y,

where x and y are vectors, and alpha is a scalar. Axpy will panic if the lengths of x and y do not match.

Copy copies the elements of x into the elements of y:

y[i] = x[i] for all i.

Copy will panic if the lengths of x and y do not match.

Dotc computes the dot product of the two vectors with complex conjugation:

xᴴ * y.

Dotc will panic if the lengths of x and y do not match.

Dotu computes the dot product of the two vectors without complex conjugation:

xᵀ * y

Dotu will panic if the lengths of x and y do not match.

Dscal computes

x = alpha * x,

where x is a vector, and alpha is a real scalar.

Dscal will panic if the vector increment is negative.

Gbmv computes

y = alpha * A * x + beta * y   if t == blas.NoTrans,
y = alpha * Aᵀ * x + beta * y  if t == blas.Trans,
y = alpha * Aᴴ * x + beta * y  if t == blas.ConjTrans,

where A is an m×n band matrix, x and y are vectors, and alpha and beta are scalars.

Gemm computes

C = alpha * A * B + beta * C,

where A, B, and C are dense matrices, and alpha and beta are scalars. tA and tB specify whether A or B are transposed or conjugated.

Gemv computes

y = alpha * A * x + beta * y   if t == blas.NoTrans,
y = alpha * Aᵀ * x + beta * y  if t == blas.Trans,
y = alpha * Aᴴ * x + beta * y  if t == blas.ConjTrans,

where A is an m×n dense matrix, x and y are vectors, and alpha and beta are scalars.

Gerc performs a rank-1 update

A += alpha * x * yᴴ,

where A is an m×n dense matrix, x and y are vectors, and alpha is a scalar.

Geru performs a rank-1 update

A += alpha * x * yᵀ,

where A is an m×n dense matrix, x and y are vectors, and alpha is a scalar.

Hbmv performs

y = alpha * A * x + beta * y,

where A is an n×n Hermitian band matrix, x and y are vectors, and alpha and beta are scalars.

Hemm performs

C = alpha * A * B + beta * C  if s == blas.Left,
C = alpha * B * A + beta * C  if s == blas.Right,

where A is an n×n or m×m Hermitian matrix, B and C are m×n matrices, and alpha and beta are scalars.

Hemv computes

y = alpha * A * x + beta * y,

where A is an n×n Hermitian matrix, x and y are vectors, and alpha and beta are scalars.

Her performs a rank-1 update

A += alpha * x * yᵀ,

where A is an m×n Hermitian matrix, x and y are vectors, and alpha is a scalar.

Her2 performs a rank-2 update

A += alpha * x * yᴴ + conj(alpha) * y * xᴴ,

where A is an n×n Hermitian matrix, x and y are vectors, and alpha is a scalar.

Her2k performs the Hermitian rank-2k update

C = alpha * A * Bᴴ + conj(alpha) * B * Aᴴ + beta * C  if t == blas.NoTrans,
C = alpha * Aᴴ * B + conj(alpha) * Bᴴ * A + beta * C  if t == blas.ConjTrans,

where C is an n×n Hermitian matrix, A and B are n×k matrices if t == NoTrans and k×n matrices otherwise, and alpha and beta are scalars.

Herk performs the Hermitian rank-k update

C = alpha * A * Aᴴ + beta*C  if t == blas.NoTrans,
C = alpha * Aᴴ * A + beta*C  if t == blas.ConjTrans,

where C is an n×n Hermitian matrix, A is an n×k matrix if t == blas.NoTrans and a k×n matrix otherwise, and alpha and beta are scalars.

Hpmv performs

y = alpha * A * x + beta * y,

where A is an n×n Hermitian matrix in packed format, x and y are vectors, and alpha and beta are scalars.

Hpr performs a rank-1 update

A += alpha * x * xᴴ,

where A is an n×n Hermitian matrix in packed format, x is a vector, and alpha is a scalar.

Hpr2 performs a rank-2 update

A += alpha * x * yᴴ + conj(alpha) * y * xᴴ,

where A is an n×n Hermitian matrix in packed format, x and y are vectors, and alpha is a scalar.

Iamax returns the index of an element of x with the largest sum of magnitudes of the real and imaginary parts (|Re x[i]|+|Im x[i]|). If there are multiple such indices, the earliest is returned.

Iamax returns -1 if n == 0.

Iamax will panic if the vector increment is negative.

Implementation returns the current BLAS complex64 implementation.

Implementation allows direct calls to the current the BLAS complex64 implementation giving finer control of parameters.

Nrm2 computes the Euclidean norm of the vector x:

sqrt(\sum_i x[i] * x[i]).

Nrm2 will panic if the vector increment is negative.

Scal computes

x = alpha * x,

where x is a vector, and alpha is a scalar.

Scal will panic if the vector increment is negative.

Swap exchanges the elements of two vectors:

x[i], y[i] = y[i], x[i] for all i.

Swap will panic if the lengths of x and y do not match.

Symm performs

C = alpha * A * B + beta * C  if s == blas.Left,
C = alpha * B * A + beta * C  if s == blas.Right,

where A is an n×n or m×m symmetric matrix, B and C are m×n matrices, and alpha and beta are scalars.

Syr2k performs a symmetric rank-2k update

C = alpha * A * Bᵀ + alpha * B * Aᵀ + beta * C  if t == blas.NoTrans,
C = alpha * Aᵀ * B + alpha * Bᵀ * A + beta * C  if t == blas.Trans,

where C is an n×n symmetric matrix, A and B are n×k matrices if t == blas.NoTrans and k×n otherwise, and alpha and beta are scalars.

Syrk performs a symmetric rank-k update

C = alpha * A * Aᵀ + beta * C  if t == blas.NoTrans,
C = alpha * Aᵀ * A + beta * C  if t == blas.Trans,

where C is an n×n symmetric matrix, A is an n×k matrix if t == blas.NoTrans and a k×n matrix otherwise, and alpha and beta are scalars.

Tbmv computes

x = A * x   if t == blas.NoTrans,
x = Aᵀ * x  if t == blas.Trans,
x = Aᴴ * x  if t == blas.ConjTrans,

where A is an n×n triangular band matrix, and x is a vector.

Tbsv solves

A * x = b   if t == blas.NoTrans,
Aᵀ * x = b  if t == blas.Trans,
Aᴴ * x = b  if t == blas.ConjTrans,

where A is an n×n triangular band matrix, and x is a vector.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Tpmv computes

x = A * x   if t == blas.NoTrans,
x = Aᵀ * x  if t == blas.Trans,
x = Aᴴ * x  if t == blas.ConjTrans,

where A is an n×n triangular matrix in packed format, and x is a vector.

Tpsv solves

A * x = b   if t == blas.NoTrans,
Aᵀ * x = b  if t == blas.Trans,
Aᴴ * x = b  if t == blas.ConjTrans,

where A is an n×n triangular matrix in packed format and x is a vector.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Trmm performs

B = alpha * A * B   if tA == blas.NoTrans and s == blas.Left,
B = alpha * Aᵀ * B  if tA == blas.Trans and s == blas.Left,
B = alpha * Aᴴ * B  if tA == blas.ConjTrans and s == blas.Left,
B = alpha * B * A   if tA == blas.NoTrans and s == blas.Right,
B = alpha * B * Aᵀ  if tA == blas.Trans and s == blas.Right,
B = alpha * B * Aᴴ  if tA == blas.ConjTrans and s == blas.Right,

where A is an n×n or m×m triangular matrix, B is an m×n matrix, and alpha is a scalar.

Trmv computes

x = A * x   if t == blas.NoTrans,
x = Aᵀ * x  if t == blas.Trans,
x = Aᴴ * x  if t == blas.ConjTrans,

where A is an n×n triangular matrix, and x is a vector.

Trsm solves

A * X = alpha * B   if tA == blas.NoTrans and s == blas.Left,
Aᵀ * X = alpha * B  if tA == blas.Trans and s == blas.Left,
Aᴴ * X = alpha * B  if tA == blas.ConjTrans and s == blas.Left,
X * A = alpha * B   if tA == blas.NoTrans and s == blas.Right,
X * Aᵀ = alpha * B  if tA == blas.Trans and s == blas.Right,
X * Aᴴ = alpha * B  if tA == blas.ConjTrans and s == blas.Right,

where A is an n×n or m×m triangular matrix, X and B are m×n matrices, and alpha is a scalar.

At entry to the function, b contains the values of B, and the result is stored in-place into b.

No check is made that A is invertible.

Trsv solves

A * x = b   if t == blas.NoTrans,
Aᵀ * x = b  if t == blas.Trans,
Aᴴ * x = b  if t == blas.ConjTrans,

where A is an n×n triangular matrix and x is a vector.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Use sets the BLAS complex64 implementation to be used by subsequent BLAS calls. The default implementation is gonum.org/v1/gonum/blas/gonum.Implementation.

#### type [Band](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/cblas64.go#L44)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Band "Go to Band")

Band represents a band matrix using the band storage scheme.

#### func (Band) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv.go#L154)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Band.From "Go to Band.From")

func (t [Band](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Band)) From(a [BandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#BandCols))

From fills the receiver with elements from a. The receiver must have the same dimensions and bandwidth as a and have adequate backing data storage.

#### type [BandCols](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv.go#L126)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#BandCols "Go to BandCols")

BandCols represents a matrix using the band column-major storage scheme.

#### func (BandCols) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv.go#L131)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#BandCols.From "Go to BandCols.From")

func (t [BandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#BandCols)) From(a [Band](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Band))

From fills the receiver with elements from a. The receiver must have the same dimensions and bandwidth as a and have adequate backing data storage.

General represents a matrix using the conventional storage scheme.

func (t [General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#General)) From(a [GeneralCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#GeneralCols))

From fills the receiver with elements from a. The receiver must have the same dimensions as a and have adequate backing data storage.

GeneralCols represents a matrix using the conventional column-major storage scheme.

func (t [GeneralCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#GeneralCols)) From(a [General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#General))

From fills the receiver with elements from a. The receiver must have the same dimensions as a and have adequate backing data storage.

Hermitian represents an Hermitian matrix using the conventional storage scheme.

func (t [Hermitian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hermitian)) From(a [HermitianCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianCols))

From fills the receiver with elements from a. The receiver must have the same dimensions and uplo as a and have adequate backing data storage.

#### type [HermitianBand](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/cblas64.go#L104)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBand "Go to HermitianBand")

type HermitianBand [SymmetricBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#SymmetricBand)

HermitianBand represents an Hermitian matrix using the band storage scheme.

#### func (HermitianBand) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv_hermitian.go#L118)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBand.From "Go to HermitianBand.From")

func (t [HermitianBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBand)) From(a [HermitianBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBandCols))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

#### type [HermitianBandCols](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv_hermitian.go#L71)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBandCols "Go to HermitianBandCols")

type HermitianBandCols [HermitianBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBand)

HermitianBandCols represents an Hermitian matrix using the band column-major storage scheme.

#### func (HermitianBandCols) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv_hermitian.go#L76)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBandCols.From "Go to HermitianBandCols.From")

func (t [HermitianBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBandCols)) From(a [HermitianBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianBand))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

type HermitianCols [Hermitian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hermitian)

HermitianCols represents a matrix using the conventional column-major storage scheme.

func (t [HermitianCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#HermitianCols)) From(a [Hermitian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Hermitian))

From fills the receiver with elements from a. The receiver must have the same dimensions and uplo as a and have adequate backing data storage.

type HermitianPacked [SymmetricPacked](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#SymmetricPacked)

HermitianPacked represents an Hermitian matrix using the packed storage scheme.

Symmetric represents a symmetric matrix using the conventional storage scheme.

#### type [SymmetricBand](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/cblas64.go#L86)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#SymmetricBand "Go to SymmetricBand")

SymmetricBand represents a symmetric matrix using the band storage scheme.

SymmetricPacked represents a symmetric matrix using the packed storage scheme.

Triangular represents a triangular matrix using the conventional storage scheme.

func (t [Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Triangular)) From(a [TriangularCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularCols))

From fills the receiver with elements from a. The receiver must have the same dimensions, uplo and diag as a and have adequate backing data storage.

#### type [TriangularBand](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/cblas64.go#L61)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBand "Go to TriangularBand")

TriangularBand represents a triangular matrix using the band storage scheme.

#### func (TriangularBand) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv.go#L225)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBand.From "Go to TriangularBand.From")

func (t [TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBand)) From(a [TriangularBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBandCols))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

#### type [TriangularBandCols](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv.go#L175)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBandCols "Go to TriangularBandCols")

type TriangularBandCols [TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBand)

TriangularBandCols represents a triangular matrix using the band column-major storage scheme.

#### func (TriangularBandCols) [From](https://github.com/gonum/gonum/blob/v0.17.0/blas/cblas64/conv.go#L180)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBandCols.From "Go to TriangularBandCols.From")

func (t [TriangularBandCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBandCols)) From(a [TriangularBand](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularBand))

From fills the receiver with elements from a. The receiver must have the same dimensions, bandwidth and uplo as a and have adequate backing data storage.

type TriangularCols [Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Triangular)

TriangularCols represents a matrix using the conventional column-major storage scheme.

func (t [TriangularCols](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#TriangularCols)) From(a [Triangular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/cblas64#Triangular))

From fills the receiver with elements from a. The receiver must have the same dimensions, uplo and diag as a and have adequate backing data storage.

TriangularPacked represents a triangular matrix using the packed storage scheme.

Vector represents a vector with an associated element increment.
