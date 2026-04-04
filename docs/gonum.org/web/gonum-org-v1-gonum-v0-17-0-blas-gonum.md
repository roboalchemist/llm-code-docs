# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum

Title: gonum package - gonum.org/v1/gonum/blas/gonum - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum

Markdown Content:
Package gonum is a Go implementation of the BLAS API. This implementation panics when the input arguments are invalid as per the standard, for example if a vector increment is zero. Note that the treatment of NaN values is not specified, and differs among the BLAS implementations. gonum.org/v1/gonum/blas/blas64 provides helpful wrapper functions to the BLAS interface. The rest of this text describes the layout of the data for the input types.

Note that in the function documentation, x[i] refers to the i^th element of the vector, which will be different from the i^th element of the slice if incX != 1.

See [http://www.netlib.org/lapack/explore-html/d4/de1/_l_i_c_e_n_s_e_source.html](http://www.netlib.org/lapack/explore-html/d4/de1/_l_i_c_e_n_s_e_source.html) for more license information.

Vector arguments are effectively strided slices. They have two input arguments, a number of elements, n, and an increment, incX. The increment specifies the distance between elements of the vector. The actual Go slice may be longer than necessary. The increment may be positive or negative, except in functions with only a single vector argument where the increment may only be positive. If the increment is negative, s[0] is the last element in the slice. Note that this is not the same as counting backward from the end of the slice, as len(s) may be longer than necessary. So, for example, if n = 5 and incX = 3, the elements of s are

[0 * * 1 * * 2 * * 3 * * 4 * * * ...]

where ∗ elements are never accessed. If incX = -3, the same elements are accessed, just in reverse order (4, 3, 2, 1, 0).

Dense matrices are specified by a number of rows, a number of columns, and a stride. The stride specifies the number of entries in the slice between the first element of successive rows. The stride must be at least as large as the number of columns but may be longer.

[a00 ... a0n a0* ... a1stride-1 a21 ... amn am* ... amstride-1]

Thus, dense[i*ld + j] refers to the {i, j}th element of the matrix.

Symmetric and triangular matrices (non-packed) are stored identically to Dense, except that only elements in one triangle of the matrix are accessed.

Packed symmetric and packed triangular matrices are laid out with the entries condensed such that all of the unreferenced elements are removed. So, the upper triangular matrix

[
  1  2  3
  0  4  5
  0  0  6
]

and the lower-triangular matrix

[
  1  0  0
  2  3  0
  4  5  6
]

will both be compacted as [1 2 3 4 5 6]. The (i, j) element of the original dense matrix can be found at element i*n - (i-1)*i/2 + j for upper triangular, and at element i * (i+1) /2 + j for lower triangular.

Banded matrices are laid out in a compact format, constructed by removing the zeros in the rows and aligning the diagonals. For example, the matrix

[
  1  2  3  0  0  0
  4  5  6  7  0  0
  0  8  9 10 11  0
  0  0 12 13 14 15
  0  0  0 16 17 18
  0  0  0  0 19 20
]

implicitly becomes (∗ entries are never accessed)

[
   *  1  2  3
   4  5  6  7
   8  9 10 11
  12 13 14 15
  16 17 18  *
  19 20  *  *
]

which is given to the BLAS routine as [∗ 1 2 3 4 ...].

See [http://www.crest.iu.edu/research/mtl/reference/html/banded.html](http://www.crest.iu.edu/research/mtl/reference/html/banded.html) for more information

*   [type Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)
*       *   [func (Implementation) Caxpy(n int, alpha complex64, x []complex64, incX int, y []complex64, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Caxpy)
    *   [func (Implementation) Ccopy(n int, x []complex64, incX int, y []complex64, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ccopy)
    *   [func (Implementation) Cdotc(n int, x []complex64, incX int, y []complex64, incY int) complex64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cdotc)
    *   [func (Implementation) Cdotu(n int, x []complex64, incX int, y []complex64, incY int) complex64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cdotu)
    *   [func (Implementation) Cgbmv(trans blas.Transpose, m, n, kL, kU int, alpha complex64, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cgbmv)
    *   [func (Implementation) Cgemm(tA, tB blas.Transpose, m, n, k int, alpha complex64, a []complex64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cgemm)
    *   [func (Implementation) Cgemv(trans blas.Transpose, m, n int, alpha complex64, a []complex64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cgemv)
    *   [func (Implementation) Cgerc(m, n int, alpha complex64, x []complex64, incX int, y []complex64, incY int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cgerc)
    *   [func (Implementation) Cgeru(m, n int, alpha complex64, x []complex64, incX int, y []complex64, incY int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cgeru)
    *   [func (Implementation) Chbmv(uplo blas.Uplo, n, k int, alpha complex64, a []complex64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Chbmv)
    *   [func (Implementation) Chemm(side blas.Side, uplo blas.Uplo, m, n int, alpha complex64, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Chemm)
    *   [func (Implementation) Chemv(uplo blas.Uplo, n int, alpha complex64, a []complex64, lda int, x []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Chemv)
    *   [func (Implementation) Cher(uplo blas.Uplo, n int, alpha float32, x []complex64, incX int, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cher)
    *   [func (Implementation) Cher2(uplo blas.Uplo, n int, alpha complex64, x []complex64, incX int, y []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cher2)
    *   [func (Implementation) Cher2k(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha complex64, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cher2k)
    *   [func (Implementation) Cherk(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha float32, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cherk)
    *   [func (Implementation) Chpmv(uplo blas.Uplo, n int, alpha complex64, ap []complex64, x []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Chpmv)
    *   [func (Implementation) Chpr(uplo blas.Uplo, n int, alpha float32, x []complex64, incX int, ap []complex64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Chpr)
    *   [func (Implementation) Chpr2(uplo blas.Uplo, n int, alpha complex64, x []complex64, incX int, y []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Chpr2)
    *   [func (Implementation) Cscal(n int, alpha complex64, x []complex64, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cscal)
    *   [func (Implementation) Csscal(n int, alpha float32, x []complex64, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Csscal)
    *   [func (Implementation) Cswap(n int, x []complex64, incX int, y []complex64, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Cswap)
    *   [func (Implementation) Csymm(side blas.Side, uplo blas.Uplo, m, n int, alpha complex64, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Csymm)
    *   [func (Implementation) Csyr2k(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha complex64, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Csyr2k)
    *   [func (Implementation) Csyrk(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha complex64, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Csyrk)
    *   [func (Implementation) Ctbmv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n, k int, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctbmv)
    *   [func (Implementation) Ctbsv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n, k int, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctbsv)
    *   [func (Implementation) Ctpmv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, ap []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctpmv)
    *   [func (Implementation) Ctpsv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, ap []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctpsv)
    *   [func (Implementation) Ctrmm(side blas.Side, uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, m, n int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctrmm)
    *   [func (Implementation) Ctrmv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctrmv)
    *   [func (Implementation) Ctrsm(side blas.Side, uplo blas.Uplo, transA blas.Transpose, diag blas.Diag, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctrsm)
    *   [func (Implementation) Ctrsv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, a []complex64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ctrsv)
    *   [func (Implementation) Dasum(n int, x []float64, incX int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dasum)
    *   [func (Implementation) Daxpy(n int, alpha float64, x []float64, incX int, y []float64, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Daxpy)
    *   [func (Implementation) Dcopy(n int, x []float64, incX int, y []float64, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dcopy)
    *   [func (Implementation) Ddot(n int, x []float64, incX int, y []float64, incY int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ddot)
    *   [func (Implementation) Dgbmv(tA blas.Transpose, m, n, kL, kU int, alpha float64, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dgbmv)
    *   [func (Implementation) Dgemm(tA, tB blas.Transpose, m, n, k int, alpha float64, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dgemm)
    *   [func (Implementation) Dgemv(tA blas.Transpose, m, n int, alpha float64, a []float64, lda int, x []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dgemv)
    *   [func (Implementation) Dger(m, n int, alpha float64, x []float64, incX int, y []float64, incY int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dger)
    *   [func (Implementation) Dnrm2(n int, x []float64, incX int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dnrm2)
    *   [func (Implementation) Drot(n int, x []float64, incX int, y []float64, incY int, c float64, s float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Drot)
    *   [func (Implementation) Drotg(a, b float64) (c, s, r, z float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Drotg)
    *   [func (Implementation) Drotm(n int, x []float64, incX int, y []float64, incY int, p blas.DrotmParams)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Drotm)
    *   [func (Implementation) Drotmg(d1, d2, x1, y1 float64) (p blas.DrotmParams, rd1, rd2, rx1 float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Drotmg)
    *   [func (Implementation) Dsbmv(ul blas.Uplo, n, k int, alpha float64, a []float64, lda int, x []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsbmv)
    *   [func (Implementation) Dscal(n int, alpha float64, x []float64, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dscal)
    *   [func (Implementation) Dsdot(n int, x []float32, incX int, y []float32, incY int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsdot)
    *   [func (Implementation) Dspmv(ul blas.Uplo, n int, alpha float64, ap []float64, x []float64, incX int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dspmv)
    *   [func (Implementation) Dspr(ul blas.Uplo, n int, alpha float64, x []float64, incX int, ap []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dspr)
    *   [func (Implementation) Dspr2(ul blas.Uplo, n int, alpha float64, x []float64, incX int, y []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dspr2)
    *   [func (Implementation) Dswap(n int, x []float64, incX int, y []float64, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dswap)
    *   [func (Implementation) Dsymm(s blas.Side, ul blas.Uplo, m, n int, alpha float64, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsymm)
    *   [func (Implementation) Dsymv(ul blas.Uplo, n int, alpha float64, a []float64, lda int, x []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsymv)
    *   [func (Implementation) Dsyr(ul blas.Uplo, n int, alpha float64, x []float64, incX int, a []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsyr)
    *   [func (Implementation) Dsyr2(ul blas.Uplo, n int, alpha float64, x []float64, incX int, y []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsyr2)
    *   [func (Implementation) Dsyr2k(ul blas.Uplo, tA blas.Transpose, n, k int, alpha float64, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsyr2k)
    *   [func (Implementation) Dsyrk(ul blas.Uplo, tA blas.Transpose, n, k int, alpha float64, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dsyrk)
    *   [func (Implementation) Dtbmv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n, k int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtbmv)
    *   [func (Implementation) Dtbsv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n, k int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtbsv)
    *   [func (Implementation) Dtpmv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, ap []float64, x []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtpmv)
    *   [func (Implementation) Dtpsv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, ap []float64, x []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtpsv)
    *   [func (Implementation) Dtrmm(s blas.Side, ul blas.Uplo, tA blas.Transpose, d blas.Diag, m, n int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtrmm)
    *   [func (Implementation) Dtrmv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtrmv)
    *   [func (Implementation) Dtrsm(s blas.Side, ul blas.Uplo, tA blas.Transpose, d blas.Diag, m, n int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtrsm)
    *   [func (Implementation) Dtrsv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dtrsv)
    *   [func (Implementation) Dzasum(n int, x []complex128, incX int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dzasum)
    *   [func (Implementation) Dznrm2(n int, x []complex128, incX int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Dznrm2)
    *   [func (Implementation) Icamax(n int, x []complex64, incX int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Icamax)
    *   [func (Implementation) Idamax(n int, x []float64, incX int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Idamax)
    *   [func (Implementation) Isamax(n int, x []float32, incX int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Isamax)
    *   [func (Implementation) Izamax(n int, x []complex128, incX int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Izamax)
    *   [func (Implementation) Sasum(n int, x []float32, incX int) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sasum)
    *   [func (Implementation) Saxpy(n int, alpha float32, x []float32, incX int, y []float32, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Saxpy)
    *   [func (Implementation) Scasum(n int, x []complex64, incX int) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Scasum)
    *   [func (Implementation) Scnrm2(n int, x []complex64, incX int) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Scnrm2)
    *   [func (Implementation) Scopy(n int, x []float32, incX int, y []float32, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Scopy)
    *   [func (Implementation) Sdot(n int, x []float32, incX int, y []float32, incY int) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sdot)
    *   [func (Implementation) Sdsdot(n int, alpha float32, x []float32, incX int, y []float32, incY int) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sdsdot)
    *   [func (Implementation) Sgbmv(tA blas.Transpose, m, n, kL, kU int, alpha float32, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sgbmv)
    *   [func (Implementation) Sgemm(tA, tB blas.Transpose, m, n, k int, alpha float32, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sgemm)
    *   [func (Implementation) Sgemv(tA blas.Transpose, m, n int, alpha float32, a []float32, lda int, x []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sgemv)
    *   [func (Implementation) Sger(m, n int, alpha float32, x []float32, incX int, y []float32, incY int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sger)
    *   [func (Implementation) Snrm2(n int, x []float32, incX int) float32](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Snrm2)
    *   [func (Implementation) Srot(n int, x []float32, incX int, y []float32, incY int, c float32, s float32)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Srot)
    *   [func (Implementation) Srotg(a, b float32) (c, s, r, z float32)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Srotg)
    *   [func (Implementation) Srotm(n int, x []float32, incX int, y []float32, incY int, p blas.SrotmParams)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Srotm)
    *   [func (Implementation) Srotmg(d1, d2, x1, y1 float32) (p blas.SrotmParams, rd1, rd2, rx1 float32)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Srotmg)
    *   [func (Implementation) Ssbmv(ul blas.Uplo, n, k int, alpha float32, a []float32, lda int, x []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ssbmv)
    *   [func (Implementation) Sscal(n int, alpha float32, x []float32, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sscal)
    *   [func (Implementation) Sspmv(ul blas.Uplo, n int, alpha float32, ap []float32, x []float32, incX int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sspmv)
    *   [func (Implementation) Sspr(ul blas.Uplo, n int, alpha float32, x []float32, incX int, ap []float32)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sspr)
    *   [func (Implementation) Sspr2(ul blas.Uplo, n int, alpha float32, x []float32, incX int, y []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sspr2)
    *   [func (Implementation) Sswap(n int, x []float32, incX int, y []float32, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Sswap)
    *   [func (Implementation) Ssymm(s blas.Side, ul blas.Uplo, m, n int, alpha float32, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ssymm)
    *   [func (Implementation) Ssymv(ul blas.Uplo, n int, alpha float32, a []float32, lda int, x []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ssymv)
    *   [func (Implementation) Ssyr(ul blas.Uplo, n int, alpha float32, x []float32, incX int, a []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ssyr)
    *   [func (Implementation) Ssyr2(ul blas.Uplo, n int, alpha float32, x []float32, incX int, y []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ssyr2)
    *   [func (Implementation) Ssyr2k(ul blas.Uplo, tA blas.Transpose, n, k int, alpha float32, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ssyr2k)
    *   [func (Implementation) Ssyrk(ul blas.Uplo, tA blas.Transpose, n, k int, alpha float32, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ssyrk)
    *   [func (Implementation) Stbmv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n, k int, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Stbmv)
    *   [func (Implementation) Stbsv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n, k int, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Stbsv)
    *   [func (Implementation) Stpmv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, ap []float32, x []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Stpmv)
    *   [func (Implementation) Stpsv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, ap []float32, x []float32, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Stpsv)
    *   [func (Implementation) Strmm(s blas.Side, ul blas.Uplo, tA blas.Transpose, d blas.Diag, m, n int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Strmm)
    *   [func (Implementation) Strmv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Strmv)
    *   [func (Implementation) Strsm(s blas.Side, ul blas.Uplo, tA blas.Transpose, d blas.Diag, m, n int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Strsm)
    *   [func (Implementation) Strsv(ul blas.Uplo, tA blas.Transpose, d blas.Diag, n int, a []float32, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Strsv)
    *   [func (Implementation) Zaxpy(n int, alpha complex128, x []complex128, incX int, y []complex128, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zaxpy)
    *   [func (Implementation) Zcopy(n int, x []complex128, incX int, y []complex128, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zcopy)
    *   [func (Implementation) Zdotc(n int, x []complex128, incX int, y []complex128, incY int) complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zdotc)
    *   [func (Implementation) Zdotu(n int, x []complex128, incX int, y []complex128, incY int) complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zdotu)
    *   [func (Implementation) Zdscal(n int, alpha float64, x []complex128, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zdscal)
    *   [func (Implementation) Zgbmv(trans blas.Transpose, m, n, kL, kU int, alpha complex128, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zgbmv)
    *   [func (Implementation) Zgemm(tA, tB blas.Transpose, m, n, k int, alpha complex128, a []complex128, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zgemm)
    *   [func (Implementation) Zgemv(trans blas.Transpose, m, n int, alpha complex128, a []complex128, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zgemv)
    *   [func (Implementation) Zgerc(m, n int, alpha complex128, x []complex128, incX int, y []complex128, incY int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zgerc)
    *   [func (Implementation) Zgeru(m, n int, alpha complex128, x []complex128, incX int, y []complex128, incY int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zgeru)
    *   [func (Implementation) Zhbmv(uplo blas.Uplo, n, k int, alpha complex128, a []complex128, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zhbmv)
    *   [func (Implementation) Zhemm(side blas.Side, uplo blas.Uplo, m, n int, alpha complex128, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zhemm)
    *   [func (Implementation) Zhemv(uplo blas.Uplo, n int, alpha complex128, a []complex128, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zhemv)
    *   [func (Implementation) Zher(uplo blas.Uplo, n int, alpha float64, x []complex128, incX int, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zher)
    *   [func (Implementation) Zher2(uplo blas.Uplo, n int, alpha complex128, x []complex128, incX int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zher2)
    *   [func (Implementation) Zher2k(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zher2k)
    *   [func (Implementation) Zherk(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha float64, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zherk)
    *   [func (Implementation) Zhpmv(uplo blas.Uplo, n int, alpha complex128, ap []complex128, x []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zhpmv)
    *   [func (Implementation) Zhpr(uplo blas.Uplo, n int, alpha float64, x []complex128, incX int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zhpr)
    *   [func (Implementation) Zhpr2(uplo blas.Uplo, n int, alpha complex128, x []complex128, incX int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zhpr2)
    *   [func (Implementation) Zscal(n int, alpha complex128, x []complex128, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zscal)
    *   [func (Implementation) Zswap(n int, x []complex128, incX int, y []complex128, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zswap)
    *   [func (Implementation) Zsymm(side blas.Side, uplo blas.Uplo, m, n int, alpha complex128, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zsymm)
    *   [func (Implementation) Zsyr2k(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zsyr2k)
    *   [func (Implementation) Zsyrk(uplo blas.Uplo, trans blas.Transpose, n, k int, alpha complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Zsyrk)
    *   [func (Implementation) Ztbmv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n, k int, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztbmv)
    *   [func (Implementation) Ztbsv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n, k int, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztbsv)
    *   [func (Implementation) Ztpmv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, ap []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztpmv)
    *   [func (Implementation) Ztpsv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, ap []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztpsv)
    *   [func (Implementation) Ztrmm(side blas.Side, uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, m, n int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztrmm)
    *   [func (Implementation) Ztrmv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztrmv)
    *   [func (Implementation) Ztrsm(side blas.Side, uplo blas.Uplo, transA blas.Transpose, diag blas.Diag, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztrsm)
    *   [func (Implementation) Ztrsv(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n int, a []complex128, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation.Ztrsv)

This section is empty.

This section is empty.

This section is empty.

type Implementation struct{}

Caxpy adds alpha times x to y:

y[i] += alpha * x[i] for all i

Complex64 implementations are autogenerated and not directly tested.

Ccopy copies the vector x to vector y.

Complex64 implementations are autogenerated and not directly tested.

Cdotc computes the dot product

xᴴ · y

of two complex vectors x and y.

Complex64 implementations are autogenerated and not directly tested.

Cdotu computes the dot product

xᵀ · y

of two complex vectors x and y.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Cgbmv(trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, kL, kU [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), x [][complex64](https://pkg.go.dev/builtin#complex64), incX [int](https://pkg.go.dev/builtin#int), beta [complex64](https://pkg.go.dev/builtin#complex64), y [][complex64](https://pkg.go.dev/builtin#complex64), incY [int](https://pkg.go.dev/builtin#int))

Cgbmv performs one of the matrix-vector operations

y = alpha * A * x + beta * y   if trans = blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if trans = blas.Trans
y = alpha * Aᴴ * x + beta * y  if trans = blas.ConjTrans

where alpha and beta are scalars, x and y are vectors, and A is an m×n band matrix with kL sub-diagonals and kU super-diagonals.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Cgemm(tA, tB [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), b [][complex64](https://pkg.go.dev/builtin#complex64), ldb [int](https://pkg.go.dev/builtin#int), beta [complex64](https://pkg.go.dev/builtin#complex64), c [][complex64](https://pkg.go.dev/builtin#complex64), ldc [int](https://pkg.go.dev/builtin#int))

Cgemm performs one of the matrix-matrix operations

C = alpha * op(A) * op(B) + beta * C

where op(X) is one of

op(X) = X  or  op(X) = Xᵀ  or  op(X) = Xᴴ,

alpha and beta are scalars, and A, B and C are matrices, with op(A) an m×k matrix, op(B) a k×n matrix and C an m×n matrix.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Cgemv(trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), x [][complex64](https://pkg.go.dev/builtin#complex64), incX [int](https://pkg.go.dev/builtin#int), beta [complex64](https://pkg.go.dev/builtin#complex64), y [][complex64](https://pkg.go.dev/builtin#complex64), incY [int](https://pkg.go.dev/builtin#int))

Cgemv performs one of the matrix-vector operations

y = alpha * A * x + beta * y   if trans = blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if trans = blas.Trans
y = alpha * Aᴴ * x + beta * y  if trans = blas.ConjTrans

where alpha and beta are scalars, x and y are vectors, and A is an m×n dense matrix.

Complex64 implementations are autogenerated and not directly tested.

Cgerc performs the rank-one operation

A += alpha * x * yᴴ

where A is an m×n dense matrix, alpha is a scalar, x is an m element vector, and y is an n element vector.

Complex64 implementations are autogenerated and not directly tested.

Cgeru performs the rank-one operation

A += alpha * x * yᵀ

where A is an m×n dense matrix, alpha is a scalar, x is an m element vector, and y is an n element vector.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Chbmv(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), x [][complex64](https://pkg.go.dev/builtin#complex64), incX [int](https://pkg.go.dev/builtin#int), beta [complex64](https://pkg.go.dev/builtin#complex64), y [][complex64](https://pkg.go.dev/builtin#complex64), incY [int](https://pkg.go.dev/builtin#int))

Chbmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where alpha and beta are scalars, x and y are vectors, and A is an n×n Hermitian band matrix with k super-diagonals. The imaginary parts of the diagonal elements of A are ignored and assumed to be zero.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Chemm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), b [][complex64](https://pkg.go.dev/builtin#complex64), ldb [int](https://pkg.go.dev/builtin#int), beta [complex64](https://pkg.go.dev/builtin#complex64), c [][complex64](https://pkg.go.dev/builtin#complex64), ldc [int](https://pkg.go.dev/builtin#int))

Chemm performs one of the matrix-matrix operations

C = alpha*A*B + beta*C  if side == blas.Left
C = alpha*B*A + beta*C  if side == blas.Right

where alpha and beta are scalars, A is an m×m or n×n hermitian matrix and B and C are m×n matrices. The imaginary parts of the diagonal elements of A are assumed to be zero.

Complex64 implementations are autogenerated and not directly tested.

Chemv performs the matrix-vector operation

y = alpha * A * x + beta * y

where alpha and beta are scalars, x and y are vectors, and A is an n×n Hermitian matrix. The imaginary parts of the diagonal elements of A are ignored and assumed to be zero.

Complex64 implementations are autogenerated and not directly tested.

Cher performs the Hermitian rank-one operation

A += alpha * x * xᴴ

where A is an n×n Hermitian matrix, alpha is a real scalar, and x is an n element vector. On entry, the imaginary parts of the diagonal elements of A are ignored and assumed to be zero, on return they will be set to zero.

Complex64 implementations are autogenerated and not directly tested.

Cher2 performs the Hermitian rank-two operation

A += alpha * x * yᴴ + conj(alpha) * y * xᴴ

where alpha is a scalar, x and y are n element vectors and A is an n×n Hermitian matrix. On entry, the imaginary parts of the diagonal elements are ignored and assumed to be zero. On return they will be set to zero.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Cher2k(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), b [][complex64](https://pkg.go.dev/builtin#complex64), ldb [int](https://pkg.go.dev/builtin#int), beta [float32](https://pkg.go.dev/builtin#float32), c [][complex64](https://pkg.go.dev/builtin#complex64), ldc [int](https://pkg.go.dev/builtin#int))

Cher2k performs one of the hermitian rank-2k operations

C = alpha*A*Bᴴ + conj(alpha)*B*Aᴴ + beta*C  if trans == blas.NoTrans
C = alpha*Aᴴ*B + conj(alpha)*Bᴴ*A + beta*C  if trans == blas.ConjTrans

where alpha and beta are scalars with beta real, C is an n×n hermitian matrix and A and B are n×k matrices in the first case and k×n matrices in the second case.

The imaginary parts of the diagonal elements of C are assumed to be zero, and on return they will be set to zero.

Complex64 implementations are autogenerated and not directly tested.

Cherk performs one of the hermitian rank-k operations

C = alpha*A*Aᴴ + beta*C  if trans == blas.NoTrans
C = alpha*Aᴴ*A + beta*C  if trans == blas.ConjTrans

where alpha and beta are real scalars, C is an n×n hermitian matrix and A is an n×k matrix in the first case and a k×n matrix in the second case.

The imaginary parts of the diagonal elements of C are assumed to be zero, and on return they will be set to zero.

Complex64 implementations are autogenerated and not directly tested.

Chpmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where alpha and beta are scalars, x and y are vectors, and A is an n×n Hermitian matrix in packed form. The imaginary parts of the diagonal elements of A are ignored and assumed to be zero.

Complex64 implementations are autogenerated and not directly tested.

Chpr performs the Hermitian rank-1 operation

A += alpha * x * xᴴ

where alpha is a real scalar, x is a vector, and A is an n×n hermitian matrix in packed form. On entry, the imaginary parts of the diagonal elements are assumed to be zero, and on return they are set to zero.

Complex64 implementations are autogenerated and not directly tested.

Chpr2 performs the Hermitian rank-2 operation

A += alpha * x * yᴴ + conj(alpha) * y * xᴴ

where alpha is a complex scalar, x and y are n element vectors, and A is an n×n Hermitian matrix, supplied in packed form. On entry, the imaginary parts of the diagonal elements are assumed to be zero, and on return they are set to zero.

Complex64 implementations are autogenerated and not directly tested.

Cscal scales the vector x by a complex scalar alpha. Cscal has no effect if incX < 0.

Complex64 implementations are autogenerated and not directly tested.

Csscal scales the vector x by a real scalar alpha. Csscal has no effect if incX < 0.

Complex64 implementations are autogenerated and not directly tested.

Cswap exchanges the elements of two complex vectors x and y.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Csymm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), b [][complex64](https://pkg.go.dev/builtin#complex64), ldb [int](https://pkg.go.dev/builtin#int), beta [complex64](https://pkg.go.dev/builtin#complex64), c [][complex64](https://pkg.go.dev/builtin#complex64), ldc [int](https://pkg.go.dev/builtin#int))

Csymm performs one of the matrix-matrix operations

C = alpha*A*B + beta*C  if side == blas.Left
C = alpha*B*A + beta*C  if side == blas.Right

where alpha and beta are scalars, A is an m×m or n×n symmetric matrix and B and C are m×n matrices.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Csyr2k(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), b [][complex64](https://pkg.go.dev/builtin#complex64), ldb [int](https://pkg.go.dev/builtin#int), beta [complex64](https://pkg.go.dev/builtin#complex64), c [][complex64](https://pkg.go.dev/builtin#complex64), ldc [int](https://pkg.go.dev/builtin#int))

Csyr2k performs one of the symmetric rank-2k operations

C = alpha*A*Bᵀ + alpha*B*Aᵀ + beta*C  if trans == blas.NoTrans
C = alpha*Aᵀ*B + alpha*Bᵀ*A + beta*C  if trans == blas.Trans

where alpha and beta are scalars, C is an n×n symmetric matrix and A and B are n×k matrices in the first case and k×n matrices in the second case.

Complex64 implementations are autogenerated and not directly tested.

Csyrk performs one of the symmetric rank-k operations

C = alpha*A*Aᵀ + beta*C  if trans == blas.NoTrans
C = alpha*Aᵀ*A + beta*C  if trans == blas.Trans

where alpha and beta are scalars, C is an n×n symmetric matrix and A is an n×k matrix in the first case and a k×n matrix in the second case.

Complex64 implementations are autogenerated and not directly tested.

Ctbmv performs one of the matrix-vector operations

x = A * x   if trans = blas.NoTrans
x = Aᵀ * x  if trans = blas.Trans
x = Aᴴ * x  if trans = blas.ConjTrans

where x is an n element vector and A is an n×n triangular band matrix, with (k+1) diagonals.

Complex64 implementations are autogenerated and not directly tested.

Ctbsv solves one of the systems of equations

A * x = b   if trans == blas.NoTrans
Aᵀ * x = b  if trans == blas.Trans
Aᴴ * x = b  if trans == blas.ConjTrans

where b and x are n element vectors and A is an n×n triangular band matrix with (k+1) diagonals.

On entry, x contains the values of b, and the solution is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Complex64 implementations are autogenerated and not directly tested.

Ctpmv performs one of the matrix-vector operations

x = A * x   if trans = blas.NoTrans
x = Aᵀ * x  if trans = blas.Trans
x = Aᴴ * x  if trans = blas.ConjTrans

where x is an n element vector and A is an n×n triangular matrix, supplied in packed form.

Complex64 implementations are autogenerated and not directly tested.

Ctpsv solves one of the systems of equations

A * x = b   if trans == blas.NoTrans
Aᵀ * x = b  if trans == blas.Trans
Aᴴ * x = b  if trans == blas.ConjTrans

where b and x are n element vectors and A is an n×n triangular matrix in packed form.

On entry, x contains the values of b, and the solution is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Ctrmm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), diag [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), b [][complex64](https://pkg.go.dev/builtin#complex64), ldb [int](https://pkg.go.dev/builtin#int))

Ctrmm performs one of the matrix-matrix operations

B = alpha * op(A) * B  if side == blas.Left,
B = alpha * B * op(A)  if side == blas.Right,

where alpha is a scalar, B is an m×n matrix, A is a unit, or non-unit, upper or lower triangular matrix and op(A) is one of

op(A) = A   if trans == blas.NoTrans,
op(A) = Aᵀ  if trans == blas.Trans,
op(A) = Aᴴ  if trans == blas.ConjTrans.

Complex64 implementations are autogenerated and not directly tested.

Ctrmv performs one of the matrix-vector operations

x = A * x   if trans = blas.NoTrans
x = Aᵀ * x  if trans = blas.Trans
x = Aᴴ * x  if trans = blas.ConjTrans

where x is a vector, and A is an n×n triangular matrix.

Complex64 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Ctrsm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), transA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), diag [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex64](https://pkg.go.dev/builtin#complex64), a [][complex64](https://pkg.go.dev/builtin#complex64), lda [int](https://pkg.go.dev/builtin#int), b [][complex64](https://pkg.go.dev/builtin#complex64), ldb [int](https://pkg.go.dev/builtin#int))

Ctrsm solves one of the matrix equations

op(A) * X = alpha * B  if side == blas.Left,
X * op(A) = alpha * B  if side == blas.Right,

where alpha is a scalar, X and B are m×n matrices, A is a unit or non-unit, upper or lower triangular matrix and op(A) is one of

op(A) = A   if transA == blas.NoTrans,
op(A) = Aᵀ  if transA == blas.Trans,
op(A) = Aᴴ  if transA == blas.ConjTrans.

On return the matrix X is overwritten on B.

Complex64 implementations are autogenerated and not directly tested.

Ctrsv solves one of the systems of equations

A * x = b   if trans == blas.NoTrans
Aᵀ * x = b  if trans == blas.Trans
Aᴴ * x = b  if trans == blas.ConjTrans

where b and x are n element vectors and A is an n×n triangular matrix.

On entry, x contains the values of b, and the solution is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Complex64 implementations are autogenerated and not directly tested.

Dasum computes the sum of the absolute values of the elements of x.

\sum_i |x[i]|

Dasum returns 0 if incX is negative.

Daxpy adds alpha times x to y

y[i] += alpha * x[i] for all i

Dcopy copies the elements of x into the elements of y.

y[i] = x[i] for all i

Ddot computes the dot product of the two vectors

\sum_i x[i]*y[i]

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dgbmv(tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, kL, kU [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), y [][float64](https://pkg.go.dev/builtin#float64), incY [int](https://pkg.go.dev/builtin#int))

Dgbmv performs one of the matrix-vector operations

y = alpha * A * x + beta * y   if tA == blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if tA == blas.Trans or blas.ConjTrans

where A is an m×n band matrix with kL sub-diagonals and kU super-diagonals, x and y are vectors, and alpha and beta are scalars.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dgemm(tA, tB [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int))

Dgemm performs one of the matrix-matrix operations

C = alpha * A * B + beta * C
C = alpha * Aᵀ * B + beta * C
C = alpha * A * Bᵀ + beta * C
C = alpha * Aᵀ * Bᵀ + beta * C

where A is an m×k or k×m dense matrix, B is an n×k or k×n dense matrix, C is an m×n matrix, and alpha and beta are scalars. tA and tB specify whether A or B are transposed.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dgemv(tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), y [][float64](https://pkg.go.dev/builtin#float64), incY [int](https://pkg.go.dev/builtin#int))

Dgemv computes

y = alpha * A * x + beta * y   if tA = blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if tA = blas.Trans or blas.ConjTrans

where A is an m×n dense matrix, x and y are vectors, and alpha and beta are scalars.

Dger performs the rank-one operation

A += alpha * x * yᵀ

where A is an m×n dense matrix, x and y are vectors, and alpha is a scalar.

Dnrm2 computes the Euclidean norm of a vector,

sqrt(\sum_i x[i] * x[i]).

This function returns 0 if incX is negative.

Drot applies a plane transformation.

x[i] = c * x[i] + s * y[i]
y[i] = c * y[i] - s * x[i]

Drotg computes a plane rotation

⎡  c s ⎤ ⎡ a ⎤ = ⎡ r ⎤
⎣ -s c ⎦ ⎣ b ⎦   ⎣ 0 ⎦

satisfying c^2 + s^2 = 1.

The computation uses the formulas

sigma = sgn(a)    if |a| >  |b|
      = sgn(b)    if |b| >= |a|
r = sigma*sqrt(a^2 + b^2)
c = 1; s = 0      if r = 0
c = a/r; s = b/r  if r != 0
c >= 0            if |a| > |b|

The subroutine also computes

z = s    if |a| > |b|,
  = 1/c  if |b| >= |a| and c != 0
  = 1    if c = 0

This allows c and s to be reconstructed from z as follows:

If z = 1, set c = 0, s = 1.
If |z| < 1, set c = sqrt(1 - z^2) and s = z.
If |z| > 1, set c = 1/z and s = sqrt(1 - c^2).

NOTE: There is a discrepancy between the reference implementation and the BLAS technical manual regarding the sign for r when a or b are zero. Drotg agrees with the definition in the manual and other common BLAS implementations.

Drotm applies the modified Givens rotation to the 2×n matrix.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dsbmv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), n, k [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), y [][float64](https://pkg.go.dev/builtin#float64), incY [int](https://pkg.go.dev/builtin#int))

Dsbmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where A is an n×n symmetric band matrix with k super-diagonals, x and y are vectors, and alpha and beta are scalars.

Dscal scales x by alpha.

x[i] *= alpha

Dscal has no effect if incX < 0.

Dsdot computes the dot product of the two vectors

\sum_i x[i]*y[i]

Float32 implementations are autogenerated and not directly tested.

Dspmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where A is an n×n symmetric matrix in packed format, x and y are vectors, and alpha and beta are scalars.

Dspr performs the symmetric rank-one operation

A += alpha * x * xᵀ

where A is an n×n symmetric matrix in packed format, x is a vector, and alpha is a scalar.

Dspr2 performs the symmetric rank-2 update

A += alpha * x * yᵀ + alpha * y * xᵀ

where A is an n×n symmetric matrix in packed format, x and y are vectors, and alpha is a scalar.

Dswap exchanges the elements of two vectors.

x[i], y[i] = y[i], x[i] for all i

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dsymm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int))

Dsymm performs one of the matrix-matrix operations

C = alpha * A * B + beta * C  if side == blas.Left
C = alpha * B * A + beta * C  if side == blas.Right

where A is an n×n or m×m symmetric matrix, B and C are m×n matrices, and alpha is a scalar.

Dsymv performs the matrix-vector operation

y = alpha * A * x + beta * y

where A is an n×n symmetric matrix, x and y are vectors, and alpha and beta are scalars.

Dsyr performs the symmetric rank-one update

A += alpha * x * xᵀ

where A is an n×n symmetric matrix, and x is a vector.

Dsyr2 performs the symmetric rank-two update

A += alpha * x * yᵀ + alpha * y * xᵀ

where A is an n×n symmetric matrix, x and y are vectors, and alpha is a scalar.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dsyr2k(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int))

Dsyr2k performs one of the symmetric rank 2k operations

C = alpha * A * Bᵀ + alpha * B * Aᵀ + beta * C  if tA == blas.NoTrans
C = alpha * Aᵀ * B + alpha * Bᵀ * A + beta * C  if tA == blas.Trans or tA == blas.ConjTrans

where A and B are n×k or k×n matrices, C is an n×n symmetric matrix, and alpha and beta are scalars.

Dsyrk performs one of the symmetric rank-k operations

C = alpha * A * Aᵀ + beta * C  if tA == blas.NoTrans
C = alpha * Aᵀ * A + beta * C  if tA == blas.Trans or tA == blas.ConjTrans

where A is an n×k or k×n matrix, C is an n×n symmetric matrix, and alpha and beta are scalars.

Dtbmv performs one of the matrix-vector operations

x = A * x   if tA == blas.NoTrans
x = Aᵀ * x  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular band matrix with k+1 diagonals, and x is a vector.

Dtbsv solves one of the systems of equations

A * x = b   if tA == blas.NoTrans
Aᵀ * x = b  if tA == blas.Trans or tA == blas.ConjTrans

where A is an n×n triangular band matrix with k+1 diagonals, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Dtpmv performs one of the matrix-vector operations

x = A * x   if tA == blas.NoTrans
x = Aᵀ * x  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix in packed format, and x is a vector.

Dtpsv solves one of the systems of equations

A * x = b   if tA == blas.NoTrans
Aᵀ * x = b  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix in packed format, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dtrmm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int))

Dtrmm performs one of the matrix-matrix operations

B = alpha * A * B   if tA == blas.NoTrans and side == blas.Left
B = alpha * Aᵀ * B  if tA == blas.Trans or blas.ConjTrans, and side == blas.Left
B = alpha * B * A   if tA == blas.NoTrans and side == blas.Right
B = alpha * B * Aᵀ  if tA == blas.Trans or blas.ConjTrans, and side == blas.Right

where A is an n×n or m×m triangular matrix, B is an m×n matrix, and alpha is a scalar.

Dtrmv performs one of the matrix-vector operations

x = A * x   if tA == blas.NoTrans
x = Aᵀ * x  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix, and x is a vector.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Dtrsm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int))

Dtrsm solves one of the matrix equations

A * X = alpha * B   if tA == blas.NoTrans and side == blas.Left
Aᵀ * X = alpha * B  if tA == blas.Trans or blas.ConjTrans, and side == blas.Left
X * A = alpha * B   if tA == blas.NoTrans and side == blas.Right
X * Aᵀ = alpha * B  if tA == blas.Trans or blas.ConjTrans, and side == blas.Right

where A is an n×n or m×m triangular matrix, X and B are m×n matrices, and alpha is a scalar.

At entry to the function, X contains the values of B, and the result is stored in-place into X.

No check is made that A is invertible.

Dtrsv solves one of the systems of equations

A * x = b   if tA == blas.NoTrans
Aᵀ * x = b  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Dzasum returns the sum of the absolute values of the elements of x

\sum_i |Re(x[i])| + |Im(x[i])|

Dzasum returns 0 if incX is negative.

Dznrm2 computes the Euclidean norm of the complex vector x,

‖x‖_2 = sqrt(\sum_i x[i] * conj(x[i])).

This function returns 0 if incX is negative.

Icamax returns the index of the first element of x having largest |Re(·)|+|Im(·)|. Icamax returns -1 if n is 0 or incX is negative.

Complex64 implementations are autogenerated and not directly tested.

Idamax returns the index of an element of x with the largest absolute value. If there are multiple such indices the earliest is returned. Idamax returns -1 if n == 0.

Isamax returns the index of an element of x with the largest absolute value. If there are multiple such indices the earliest is returned. Isamax returns -1 if n == 0.

Float32 implementations are autogenerated and not directly tested.

Izamax returns the index of the first element of x having largest |Re(·)|+|Im(·)|. Izamax returns -1 if n is 0 or incX is negative.

Sasum computes the sum of the absolute values of the elements of x.

\sum_i |x[i]|

Sasum returns 0 if incX is negative.

Float32 implementations are autogenerated and not directly tested.

Saxpy adds alpha times x to y

y[i] += alpha * x[i] for all i

Float32 implementations are autogenerated and not directly tested.

Scasum returns the sum of the absolute values of the elements of x

\sum_i |Re(x[i])| + |Im(x[i])|

Scasum returns 0 if incX is negative.

Complex64 implementations are autogenerated and not directly tested.

Scnrm2 computes the Euclidean norm of the complex vector x,

‖x‖_2 = sqrt(\sum_i x[i] * conj(x[i])).

This function returns 0 if incX is negative.

Complex64 implementations are autogenerated and not directly tested.

Scopy copies the elements of x into the elements of y.

y[i] = x[i] for all i

Float32 implementations are autogenerated and not directly tested.

Sdot computes the dot product of the two vectors

\sum_i x[i]*y[i]

Float32 implementations are autogenerated and not directly tested.

Sdsdot computes the dot product of the two vectors plus a constant

alpha + \sum_i x[i]*y[i]

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Sgbmv(tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, kL, kU [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), x [][float32](https://pkg.go.dev/builtin#float32), incX [int](https://pkg.go.dev/builtin#int), beta [float32](https://pkg.go.dev/builtin#float32), y [][float32](https://pkg.go.dev/builtin#float32), incY [int](https://pkg.go.dev/builtin#int))

Sgbmv performs one of the matrix-vector operations

y = alpha * A * x + beta * y   if tA == blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if tA == blas.Trans or blas.ConjTrans

where A is an m×n band matrix with kL sub-diagonals and kU super-diagonals, x and y are vectors, and alpha and beta are scalars.

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Sgemm(tA, tB [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), b [][float32](https://pkg.go.dev/builtin#float32), ldb [int](https://pkg.go.dev/builtin#int), beta [float32](https://pkg.go.dev/builtin#float32), c [][float32](https://pkg.go.dev/builtin#float32), ldc [int](https://pkg.go.dev/builtin#int))

Sgemm performs one of the matrix-matrix operations

C = alpha * A * B + beta * C
C = alpha * Aᵀ * B + beta * C
C = alpha * A * Bᵀ + beta * C
C = alpha * Aᵀ * Bᵀ + beta * C

where A is an m×k or k×m dense matrix, B is an n×k or k×n dense matrix, C is an m×n matrix, and alpha and beta are scalars. tA and tB specify whether A or B are transposed.

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Sgemv(tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), x [][float32](https://pkg.go.dev/builtin#float32), incX [int](https://pkg.go.dev/builtin#int), beta [float32](https://pkg.go.dev/builtin#float32), y [][float32](https://pkg.go.dev/builtin#float32), incY [int](https://pkg.go.dev/builtin#int))

Sgemv computes

y = alpha * A * x + beta * y   if tA = blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if tA = blas.Trans or blas.ConjTrans

where A is an m×n dense matrix, x and y are vectors, and alpha and beta are scalars.

Float32 implementations are autogenerated and not directly tested.

Sger performs the rank-one operation

A += alpha * x * yᵀ

where A is an m×n dense matrix, x and y are vectors, and alpha is a scalar.

Float32 implementations are autogenerated and not directly tested.

Snrm2 computes the Euclidean norm of a vector,

sqrt(\sum_i x[i] * x[i]).

This function returns 0 if incX is negative.

Float32 implementations are autogenerated and not directly tested.

Srot applies a plane transformation.

x[i] = c * x[i] + s * y[i]
y[i] = c * y[i] - s * x[i]

Float32 implementations are autogenerated and not directly tested.

Srotg computes a plane rotation

⎡  c s ⎤ ⎡ a ⎤ = ⎡ r ⎤
⎣ -s c ⎦ ⎣ b ⎦   ⎣ 0 ⎦

satisfying c^2 + s^2 = 1.

The computation uses the formulas

sigma = sgn(a)    if |a| >  |b|
      = sgn(b)    if |b| >= |a|
r = sigma*sqrt(a^2 + b^2)
c = 1; s = 0      if r = 0
c = a/r; s = b/r  if r != 0
c >= 0            if |a| > |b|

The subroutine also computes

z = s    if |a| > |b|,
  = 1/c  if |b| >= |a| and c != 0
  = 1    if c = 0

This allows c and s to be reconstructed from z as follows:

If z = 1, set c = 0, s = 1.
If |z| < 1, set c = sqrt(1 - z^2) and s = z.
If |z| > 1, set c = 1/z and s = sqrt(1 - c^2).

NOTE: There is a discrepancy between the reference implementation and the BLAS technical manual regarding the sign for r when a or b are zero. Drotg agrees with the definition in the manual and other common BLAS implementations.

Float32 implementations are autogenerated and not directly tested.

Srotm applies the modified Givens rotation to the 2×n matrix.

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Ssbmv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), n, k [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), x [][float32](https://pkg.go.dev/builtin#float32), incX [int](https://pkg.go.dev/builtin#int), beta [float32](https://pkg.go.dev/builtin#float32), y [][float32](https://pkg.go.dev/builtin#float32), incY [int](https://pkg.go.dev/builtin#int))

Ssbmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where A is an n×n symmetric band matrix with k super-diagonals, x and y are vectors, and alpha and beta are scalars.

Float32 implementations are autogenerated and not directly tested.

Sscal scales x by alpha.

x[i] *= alpha

Sscal has no effect if incX < 0.

Float32 implementations are autogenerated and not directly tested.

Sspmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where A is an n×n symmetric matrix in packed format, x and y are vectors, and alpha and beta are scalars.

Float32 implementations are autogenerated and not directly tested.

Sspr performs the symmetric rank-one operation

A += alpha * x * xᵀ

where A is an n×n symmetric matrix in packed format, x is a vector, and alpha is a scalar.

Float32 implementations are autogenerated and not directly tested.

Sspr2 performs the symmetric rank-2 update

A += alpha * x * yᵀ + alpha * y * xᵀ

where A is an n×n symmetric matrix in packed format, x and y are vectors, and alpha is a scalar.

Float32 implementations are autogenerated and not directly tested.

Sswap exchanges the elements of two vectors.

x[i], y[i] = y[i], x[i] for all i

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Ssymm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), b [][float32](https://pkg.go.dev/builtin#float32), ldb [int](https://pkg.go.dev/builtin#int), beta [float32](https://pkg.go.dev/builtin#float32), c [][float32](https://pkg.go.dev/builtin#float32), ldc [int](https://pkg.go.dev/builtin#int))

Ssymm performs one of the matrix-matrix operations

C = alpha * A * B + beta * C  if side == blas.Left
C = alpha * B * A + beta * C  if side == blas.Right

where A is an n×n or m×m symmetric matrix, B and C are m×n matrices, and alpha is a scalar.

Float32 implementations are autogenerated and not directly tested.

Ssymv performs the matrix-vector operation

y = alpha * A * x + beta * y

where A is an n×n symmetric matrix, x and y are vectors, and alpha and beta are scalars.

Float32 implementations are autogenerated and not directly tested.

Ssyr performs the symmetric rank-one update

A += alpha * x * xᵀ

where A is an n×n symmetric matrix, and x is a vector.

Float32 implementations are autogenerated and not directly tested.

Ssyr2 performs the symmetric rank-two update

A += alpha * x * yᵀ + alpha * y * xᵀ

where A is an n×n symmetric matrix, x and y are vectors, and alpha is a scalar.

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Ssyr2k(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), b [][float32](https://pkg.go.dev/builtin#float32), ldb [int](https://pkg.go.dev/builtin#int), beta [float32](https://pkg.go.dev/builtin#float32), c [][float32](https://pkg.go.dev/builtin#float32), ldc [int](https://pkg.go.dev/builtin#int))

Ssyr2k performs one of the symmetric rank 2k operations

C = alpha * A * Bᵀ + alpha * B * Aᵀ + beta * C  if tA == blas.NoTrans
C = alpha * Aᵀ * B + alpha * Bᵀ * A + beta * C  if tA == blas.Trans or tA == blas.ConjTrans

where A and B are n×k or k×n matrices, C is an n×n symmetric matrix, and alpha and beta are scalars.

Float32 implementations are autogenerated and not directly tested.

Ssyrk performs one of the symmetric rank-k operations

C = alpha * A * Aᵀ + beta * C  if tA == blas.NoTrans
C = alpha * Aᵀ * A + beta * C  if tA == blas.Trans or tA == blas.ConjTrans

where A is an n×k or k×n matrix, C is an n×n symmetric matrix, and alpha and beta are scalars.

Float32 implementations are autogenerated and not directly tested.

Stbmv performs one of the matrix-vector operations

x = A * x   if tA == blas.NoTrans
x = Aᵀ * x  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular band matrix with k+1 diagonals, and x is a vector.

Float32 implementations are autogenerated and not directly tested.

Stbsv solves one of the systems of equations

A * x = b   if tA == blas.NoTrans
Aᵀ * x = b  if tA == blas.Trans or tA == blas.ConjTrans

where A is an n×n triangular band matrix with k+1 diagonals, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Float32 implementations are autogenerated and not directly tested.

Stpmv performs one of the matrix-vector operations

x = A * x   if tA == blas.NoTrans
x = Aᵀ * x  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix in packed format, and x is a vector.

Float32 implementations are autogenerated and not directly tested.

Stpsv solves one of the systems of equations

A * x = b   if tA == blas.NoTrans
Aᵀ * x = b  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix in packed format, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Strmm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), b [][float32](https://pkg.go.dev/builtin#float32), ldb [int](https://pkg.go.dev/builtin#int))

Strmm performs one of the matrix-matrix operations

B = alpha * A * B   if tA == blas.NoTrans and side == blas.Left
B = alpha * Aᵀ * B  if tA == blas.Trans or blas.ConjTrans, and side == blas.Left
B = alpha * B * A   if tA == blas.NoTrans and side == blas.Right
B = alpha * B * Aᵀ  if tA == blas.Trans or blas.ConjTrans, and side == blas.Right

where A is an n×n or m×m triangular matrix, B is an m×n matrix, and alpha is a scalar.

Float32 implementations are autogenerated and not directly tested.

Strmv performs one of the matrix-vector operations

x = A * x   if tA == blas.NoTrans
x = Aᵀ * x  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix, and x is a vector.

Float32 implementations are autogenerated and not directly tested.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Strsm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [float32](https://pkg.go.dev/builtin#float32), a [][float32](https://pkg.go.dev/builtin#float32), lda [int](https://pkg.go.dev/builtin#int), b [][float32](https://pkg.go.dev/builtin#float32), ldb [int](https://pkg.go.dev/builtin#int))

Strsm solves one of the matrix equations

A * X = alpha * B   if tA == blas.NoTrans and side == blas.Left
Aᵀ * X = alpha * B  if tA == blas.Trans or blas.ConjTrans, and side == blas.Left
X * A = alpha * B   if tA == blas.NoTrans and side == blas.Right
X * Aᵀ = alpha * B  if tA == blas.Trans or blas.ConjTrans, and side == blas.Right

where A is an n×n or m×m triangular matrix, X and B are m×n matrices, and alpha is a scalar.

At entry to the function, X contains the values of B, and the result is stored in-place into X.

No check is made that A is invertible.

Float32 implementations are autogenerated and not directly tested.

Strsv solves one of the systems of equations

A * x = b   if tA == blas.NoTrans
Aᵀ * x = b  if tA == blas.Trans or blas.ConjTrans

where A is an n×n triangular matrix, and x and b are vectors.

At entry to the function, x contains the values of b, and the result is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Float32 implementations are autogenerated and not directly tested.

Zaxpy adds alpha times x to y:

y[i] += alpha * x[i] for all i

Zcopy copies the vector x to vector y.

Zdotc computes the dot product

xᴴ · y

of two complex vectors x and y.

Zdotu computes the dot product

xᵀ · y

of two complex vectors x and y.

Zdscal scales the vector x by a real scalar alpha. Zdscal has no effect if incX < 0.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zgbmv(trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, kL, kU [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), x [][complex128](https://pkg.go.dev/builtin#complex128), incX [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), y [][complex128](https://pkg.go.dev/builtin#complex128), incY [int](https://pkg.go.dev/builtin#int))

Zgbmv performs one of the matrix-vector operations

y = alpha * A * x + beta * y   if trans = blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if trans = blas.Trans
y = alpha * Aᴴ * x + beta * y  if trans = blas.ConjTrans

where alpha and beta are scalars, x and y are vectors, and A is an m×n band matrix with kL sub-diagonals and kU super-diagonals.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zgemm(tA, tB [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int))

Zgemm performs one of the matrix-matrix operations

C = alpha * op(A) * op(B) + beta * C

where op(X) is one of

op(X) = X  or  op(X) = Xᵀ  or  op(X) = Xᴴ,

alpha and beta are scalars, and A, B and C are matrices, with op(A) an m×k matrix, op(B) a k×n matrix and C an m×n matrix.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zgemv(trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), x [][complex128](https://pkg.go.dev/builtin#complex128), incX [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), y [][complex128](https://pkg.go.dev/builtin#complex128), incY [int](https://pkg.go.dev/builtin#int))

Zgemv performs one of the matrix-vector operations

y = alpha * A * x + beta * y   if trans = blas.NoTrans
y = alpha * Aᵀ * x + beta * y  if trans = blas.Trans
y = alpha * Aᴴ * x + beta * y  if trans = blas.ConjTrans

where alpha and beta are scalars, x and y are vectors, and A is an m×n dense matrix.

Zgerc performs the rank-one operation

A += alpha * x * yᴴ

where A is an m×n dense matrix, alpha is a scalar, x is an m element vector, and y is an n element vector.

Zgeru performs the rank-one operation

A += alpha * x * yᵀ

where A is an m×n dense matrix, alpha is a scalar, x is an m element vector, and y is an n element vector.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zhbmv(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), x [][complex128](https://pkg.go.dev/builtin#complex128), incX [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), y [][complex128](https://pkg.go.dev/builtin#complex128), incY [int](https://pkg.go.dev/builtin#int))

Zhbmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where alpha and beta are scalars, x and y are vectors, and A is an n×n Hermitian band matrix with k super-diagonals. The imaginary parts of the diagonal elements of A are ignored and assumed to be zero.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zhemm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int))

Zhemm performs one of the matrix-matrix operations

C = alpha*A*B + beta*C  if side == blas.Left
C = alpha*B*A + beta*C  if side == blas.Right

where alpha and beta are scalars, A is an m×m or n×n hermitian matrix and B and C are m×n matrices. The imaginary parts of the diagonal elements of A are assumed to be zero.

Zhemv performs the matrix-vector operation

y = alpha * A * x + beta * y

where alpha and beta are scalars, x and y are vectors, and A is an n×n Hermitian matrix. The imaginary parts of the diagonal elements of A are ignored and assumed to be zero.

Zher performs the Hermitian rank-one operation

A += alpha * x * xᴴ

where A is an n×n Hermitian matrix, alpha is a real scalar, and x is an n element vector. On entry, the imaginary parts of the diagonal elements of A are ignored and assumed to be zero, on return they will be set to zero.

Zher2 performs the Hermitian rank-two operation

A += alpha * x * yᴴ + conj(alpha) * y * xᴴ

where alpha is a scalar, x and y are n element vectors and A is an n×n Hermitian matrix. On entry, the imaginary parts of the diagonal elements are ignored and assumed to be zero. On return they will be set to zero.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zher2k(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int))

Zher2k performs one of the hermitian rank-2k operations

C = alpha*A*Bᴴ + conj(alpha)*B*Aᴴ + beta*C  if trans == blas.NoTrans
C = alpha*Aᴴ*B + conj(alpha)*Bᴴ*A + beta*C  if trans == blas.ConjTrans

where alpha and beta are scalars with beta real, C is an n×n hermitian matrix and A and B are n×k matrices in the first case and k×n matrices in the second case.

The imaginary parts of the diagonal elements of C are assumed to be zero, and on return they will be set to zero.

Zherk performs one of the hermitian rank-k operations

C = alpha*A*Aᴴ + beta*C  if trans == blas.NoTrans
C = alpha*Aᴴ*A + beta*C  if trans == blas.ConjTrans

where alpha and beta are real scalars, C is an n×n hermitian matrix and A is an n×k matrix in the first case and a k×n matrix in the second case.

The imaginary parts of the diagonal elements of C are assumed to be zero, and on return they will be set to zero.

Zhpmv performs the matrix-vector operation

y = alpha * A * x + beta * y

where alpha and beta are scalars, x and y are vectors, and A is an n×n Hermitian matrix in packed form. The imaginary parts of the diagonal elements of A are ignored and assumed to be zero.

Zhpr performs the Hermitian rank-1 operation

A += alpha * x * xᴴ

where alpha is a real scalar, x is a vector, and A is an n×n hermitian matrix in packed form. On entry, the imaginary parts of the diagonal elements are assumed to be zero, and on return they are set to zero.

Zhpr2 performs the Hermitian rank-2 operation

A += alpha * x * yᴴ + conj(alpha) * y * xᴴ

where alpha is a complex scalar, x and y are n element vectors, and A is an n×n Hermitian matrix, supplied in packed form. On entry, the imaginary parts of the diagonal elements are assumed to be zero, and on return they are set to zero.

Zscal scales the vector x by a complex scalar alpha. Zscal has no effect if incX < 0.

Zswap exchanges the elements of two complex vectors x and y.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zsymm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int))

Zsymm performs one of the matrix-matrix operations

C = alpha*A*B + beta*C  if side == blas.Left
C = alpha*B*A + beta*C  if side == blas.Right

where alpha and beta are scalars, A is an m×m or n×n symmetric matrix and B and C are m×n matrices.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Zsyr2k(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int))

Zsyr2k performs one of the symmetric rank-2k operations

C = alpha*A*Bᵀ + alpha*B*Aᵀ + beta*C  if trans == blas.NoTrans
C = alpha*Aᵀ*B + alpha*Bᵀ*A + beta*C  if trans == blas.Trans

where alpha and beta are scalars, C is an n×n symmetric matrix and A and B are n×k matrices in the first case and k×n matrices in the second case.

Zsyrk performs one of the symmetric rank-k operations

C = alpha*A*Aᵀ + beta*C  if trans == blas.NoTrans
C = alpha*Aᵀ*A + beta*C  if trans == blas.Trans

where alpha and beta are scalars, C is an n×n symmetric matrix and A is an n×k matrix in the first case and a k×n matrix in the second case.

Ztbmv performs one of the matrix-vector operations

x = A * x   if trans = blas.NoTrans
x = Aᵀ * x  if trans = blas.Trans
x = Aᴴ * x  if trans = blas.ConjTrans

where x is an n element vector and A is an n×n triangular band matrix, with (k+1) diagonals.

Ztbsv solves one of the systems of equations

A * x = b   if trans == blas.NoTrans
Aᵀ * x = b  if trans == blas.Trans
Aᴴ * x = b  if trans == blas.ConjTrans

where b and x are n element vectors and A is an n×n triangular band matrix with (k+1) diagonals.

On entry, x contains the values of b, and the solution is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

Ztpmv performs one of the matrix-vector operations

x = A * x   if trans = blas.NoTrans
x = Aᵀ * x  if trans = blas.Trans
x = Aᴴ * x  if trans = blas.ConjTrans

where x is an n element vector and A is an n×n triangular matrix, supplied in packed form.

Ztpsv solves one of the systems of equations

A * x = b   if trans == blas.NoTrans
Aᵀ * x = b  if trans == blas.Trans
Aᴴ * x = b  if trans == blas.ConjTrans

where b and x are n element vectors and A is an n×n triangular matrix in packed form.

On entry, x contains the values of b, and the solution is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Ztrmm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), diag [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int))

Ztrmm performs one of the matrix-matrix operations

B = alpha * op(A) * B  if side == blas.Left,
B = alpha * B * op(A)  if side == blas.Right,

where alpha is a scalar, B is an m×n matrix, A is a unit, or non-unit, upper or lower triangular matrix and op(A) is one of

op(A) = A   if trans == blas.NoTrans,
op(A) = Aᵀ  if trans == blas.Trans,
op(A) = Aᴴ  if trans == blas.ConjTrans.

Ztrmv performs one of the matrix-vector operations

x = A * x   if trans = blas.NoTrans
x = Aᵀ * x  if trans = blas.Trans
x = Aᴴ * x  if trans = blas.ConjTrans

where x is a vector, and A is an n×n triangular matrix.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/gonum#Implementation)) Ztrsm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), transA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), diag [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int))

Ztrsm solves one of the matrix equations

op(A) * X = alpha * B  if side == blas.Left,
X * op(A) = alpha * B  if side == blas.Right,

where alpha is a scalar, X and B are m×n matrices, A is a unit or non-unit, upper or lower triangular matrix and op(A) is one of

op(A) = A   if transA == blas.NoTrans,
op(A) = Aᵀ  if transA == blas.Trans,
op(A) = Aᴴ  if transA == blas.ConjTrans.

On return the matrix X is overwritten on B.

Ztrsv solves one of the systems of equations

A * x = b   if trans == blas.NoTrans
Aᵀ * x = b  if trans == blas.Trans
Aᴴ * x = b  if trans == blas.ConjTrans

where b and x are n element vectors and A is an n×n triangular matrix.

On entry, x contains the values of b, and the solution is stored in-place into x.

No test for singularity or near-singularity is included in this routine. Such tests must be performed before calling this routine.
