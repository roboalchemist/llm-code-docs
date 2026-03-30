# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64

Title: lapack64 package - gonum.org/v1/gonum/lapack/lapack64 - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64

Markdown Content:
Package lapack64 provides a set of convenient wrapper functions for LAPACK calls, as specified in the netlib standard (www.netlib.org).

The native Go routines are used by default, and the Use function can be used to set an alternative implementation.

If the type of matrix (General, Symmetric, etc.) is known and fixed, it is used in the wrapper signature. In many cases, however, the type of the matrix changes during the call to the routine, for example the matrix is symmetric on entry and is triangular on exit. In these cases the correct types should be checked in the documentation.

The full set of Lapack functions is very large, and it is not clear that a full implementation is desirable, let alone feasible. Please open up an issue if there is a specific function you need and/or are willing to implement.

*   [func Gecon(norm lapack.MatrixNorm, a blas64.General, anorm float64, work []float64, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Gecon)
*   [func Geev(jobvl lapack.LeftEVJob, jobvr lapack.RightEVJob, a blas64.General, ...) (first int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Geev)
*   [func Gelqf(a blas64.General, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Gelqf)
*   [func Gels(trans blas.Transpose, a blas64.General, b blas64.General, work []float64, ...) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Gels)
*   [func Geqp3(a blas64.General, jpvt []int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Geqp3)
*   [func Geqrf(a blas64.General, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Geqrf)
*   [func Gesvd(jobU, jobVT lapack.SVDJob, a, u, vt blas64.General, s, work []float64, ...) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Gesvd)
*   [func Getrf(a blas64.General, ipiv []int) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Getrf)
*   [func Getri(a blas64.General, ipiv []int, work []float64, lwork int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Getri)
*   [func Getrs(trans blas.Transpose, a blas64.General, b blas64.General, ipiv []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Getrs)
*   [func Ggsvd3(jobU, jobV, jobQ lapack.GSVDJob, a, b blas64.General, alpha, beta []float64, ...) (k, l int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Ggsvd3)
*   [func Gtsv(trans blas.Transpose, a Tridiagonal, b blas64.General) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Gtsv)
*   [func Lagtm(trans blas.Transpose, alpha float64, a Tridiagonal, b blas64.General, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lagtm)
*   [func Langb(norm lapack.MatrixNorm, a blas64.Band) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Langb)
*   [func Lange(norm lapack.MatrixNorm, a blas64.General, work []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lange)
*   [func Langt(norm lapack.MatrixNorm, a Tridiagonal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Langt)
*   [func Lansb(norm lapack.MatrixNorm, a blas64.SymmetricBand, work []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lansb)
*   [func Lansy(norm lapack.MatrixNorm, a blas64.Symmetric, work []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lansy)
*   [func Lantb(norm lapack.MatrixNorm, a blas64.TriangularBand, work []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lantb)
*   [func Lantr(norm lapack.MatrixNorm, a blas64.Triangular, work []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lantr)
*   [func Lapmr(forward bool, x blas64.General, k []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lapmr)
*   [func Lapmt(forward bool, x blas64.General, k []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Lapmt)
*   [func Orglq(a blas64.General, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Orglq)
*   [func Orgqr(a blas64.General, tau []float64, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Orgqr)
*   [func Ormlq(side blas.Side, trans blas.Transpose, a blas64.General, tau []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Ormlq)
*   [func Ormqr(side blas.Side, trans blas.Transpose, a blas64.General, tau []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Ormqr)
*   [func Pbcon(a blas64.SymmetricBand, anorm float64, work []float64, iwork []int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Pbcon)
*   [func Pbtrf(a blas64.SymmetricBand) (t blas64.TriangularBand, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Pbtrf)
*   [func Pbtrs(t blas64.TriangularBand, b blas64.General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Pbtrs)
*   [func Pocon(a blas64.Symmetric, anorm float64, work []float64, iwork []int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Pocon)
*   [func Potrf(a blas64.Symmetric) (t blas64.Triangular, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Potrf)
*   [func Potri(t blas64.Triangular) (a blas64.Symmetric, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Potri)
*   [func Potrs(t blas64.Triangular, b blas64.General)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Potrs)
*   [func Pstrf(a blas64.Symmetric, piv []int, tol float64, work []float64) (t blas64.Triangular, rank int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Pstrf)
*   [func Syev(jobz lapack.EVJob, a blas64.Symmetric, w, work []float64, lwork int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Syev)
*   [func Tbtrs(trans blas.Transpose, a blas64.TriangularBand, b blas64.General) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Tbtrs)
*   [func Trcon(norm lapack.MatrixNorm, a blas64.Triangular, work []float64, iwork []int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Trcon)
*   [func Trtri(a blas64.Triangular) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Trtri)
*   [func Trtrs(trans blas.Transpose, a blas64.Triangular, b blas64.General) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Trtrs)
*   [func Use(l lapack.Float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Use)
*   [type Tridiagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/lapack64#Tridiagonal)

This section is empty.

This section is empty.

Gecon estimates the reciprocal of the condition number of the n×n matrix A given the LU decomposition of the matrix. The condition number computed may be based on the 1-norm or the ∞-norm.

a contains the result of the LU decomposition of A as computed by Getrf.

anorm is the corresponding 1-norm or ∞-norm of the original matrix A.

work is a temporary data slice of length at least 4*n and Gecon will panic otherwise.

iwork is a temporary data slice of length at least n and Gecon will panic otherwise.

Geev computes the eigenvalues and, optionally, the left and/or right eigenvectors for an n×n real nonsymmetric matrix A.

The right eigenvector v_j of A corresponding to an eigenvalue λ_j is defined by

A v_j = λ_j v_j,

and the left eigenvector u_j corresponding to an eigenvalue λ_j is defined by

u_jᴴ A = λ_j u_jᴴ,

where u_jᴴ is the conjugate transpose of u_j.

On return, A will be overwritten and the left and right eigenvectors will be stored, respectively, in the columns of the n×n matrices VL and VR in the same order as their eigenvalues. If the j-th eigenvalue is real, then

u_j = VL[:,j],
v_j = VR[:,j],

and if it is not real, then j and j+1 form a complex conjugate pair and the eigenvectors can be recovered as

u_j     = VL[:,j] + i*VL[:,j+1],
u_{j+1} = VL[:,j] - i*VL[:,j+1],
v_j     = VR[:,j] + i*VR[:,j+1],
v_{j+1} = VR[:,j] - i*VR[:,j+1],

where i is the imaginary unit. The computed eigenvectors are normalized to have Euclidean norm equal to 1 and largest component real.

Left eigenvectors will be computed only if jobvl == lapack.LeftEVCompute, otherwise jobvl must be lapack.LeftEVNone. Right eigenvectors will be computed only if jobvr == lapack.RightEVCompute, otherwise jobvr must be lapack.RightEVNone. For other values of jobvl and jobvr Geev will panic.

On return, wr and wi will contain the real and imaginary parts, respectively, of the computed eigenvalues. Complex conjugate pairs of eigenvalues appear consecutively with the eigenvalue having the positive imaginary part first. wr and wi must have length n, and Geev will panic otherwise.

work must have length at least lwork and lwork must be at least max(1,4*n) if the left or right eigenvectors are computed, and at least max(1,3*n) if no eigenvectors are computed. For good performance, lwork must generally be larger. On return, optimal value of lwork will be stored in work[0].

If lwork == -1, instead of performing Geev, the function only calculates the optimal value of lwork and stores it into work[0].

On return, first will be the index of the first valid eigenvalue. If first == 0, all eigenvalues and eigenvectors have been computed. If first is positive, Geev failed to compute all the eigenvalues, no eigenvectors have been computed and wr[first:] and wi[first:] contain those eigenvalues which have converged.

Gelqf computes the LQ factorization of the m×n matrix A using a blocked algorithm. A is modified to contain the information to construct L and Q. The lower triangle of a contains the matrix L. The elements above the diagonal and the slice tau represent the matrix Q. tau is modified to contain the reflector scales. tau must have length at least min(m,n), and this function will panic otherwise.

See Geqrf for a description of the elementary reflectors and orthonormal matrix Q. Q is constructed as a product of these elementary reflectors, Q = H_{k-1} * ... * H_1 * H_0.

Work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= m and this function will panic otherwise. Gelqf is a blocked LQ factorization, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Gelqf, the optimal work length will be stored into work[0].

Gels finds a minimum-norm solution based on the matrices A and B using the QR or LQ factorization. Gels returns false if the matrix A is singular, and true if this solution was successfully found.

The minimization problem solved depends on the input parameters.

1.   If m >= n and trans == blas.NoTrans, Gels finds X such that || A*X - B||_2 is minimized.
2.   If m < n and trans == blas.NoTrans, Gels finds the minimum norm solution of A * X = B.
3.   If m >= n and trans == blas.Trans, Gels finds the minimum norm solution of Aᵀ * X = B.
4.   If m < n and trans == blas.Trans, Gels finds X such that || A*X - B||_2 is minimized.

Note that the least-squares solutions (cases 1 and 3) perform the minimization per column of B. This is not the same as finding the minimum-norm matrix.

The matrix A is a general matrix of size m×n and is modified during this call. The input matrix B is of size max(m,n)×nrhs, and serves two purposes. On entry, the elements of b specify the input matrix B. B has size m×nrhs if trans == blas.NoTrans, and n×nrhs if trans == blas.Trans. On exit, the leading submatrix of b contains the solution vectors X. If trans == blas.NoTrans, this submatrix is of size n×nrhs, and of size m×nrhs otherwise.

Work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= max(m,n) + max(m,n,nrhs), and this function will panic otherwise. A longer work will enable blocked algorithms to be called. In the special case that lwork == -1, work[0] will be set to the optimal working length.

Geqp3 computes a QR factorization with column pivoting of the m×n matrix A:

A*P = Q*R

where P is a permutation matrix, Q is an orthogonal matrix and R is a min(m,n)×n upper trapezoidal matrix.

On return, the upper triangle of A contains the matrix R. The elements below the diagonal together with tau represent the matrix Q as a product of elementary reflectors

Q = H_0 * H_1 * ... * H_{k-1}, where k = min(m,n).

Each H_i has the form

H_i = I - tau * v * vᵀ

where tau is a scalar and v is a vector with v[0:i] = 0 and v[i] = 1; v[i+1:m] is stored on exit in A[i+1:m,i], and tau in tau[i].

jpvt specifies a column pivot to be applied to A. On entry, if jpvt[j] is at least zero, the jth column of A is permuted to the front of A*P (a leading column), if jpvt[j] is -1 the jth column of A is a free column. If jpvt[j] < -1, Geqp3 will panic. On return, jpvt holds the permutation that was applied; the jth column of A*P was the jpvt[j] column of A. jpvt must have length n or Geqp3 will panic.

tau holds the scalar factors of the elementary reflectors. It must have length min(m,n), otherwise Geqp3 will panic.

work must have length at least max(1,lwork), and lwork must be at least 3*n+1, otherwise Geqp3 will panic. For optimal performance lwork must be at least 2*n+(n+1)*nb, where nb is the optimal blocksize. On return, work[0] will contain the optimal value of lwork.

If lwork == -1, instead of performing Geqp3, only the optimal value of lwork will be stored in work[0].

Geqrf computes the QR factorization of the m×n matrix A using a blocked algorithm. A is modified to contain the information to construct Q and R. The upper triangle of a contains the matrix R. The lower triangular elements (not including the diagonal) contain the elementary reflectors. tau is modified to contain the reflector scales. tau must have length min(m,n), and this function will panic otherwise.

The ith elementary reflector can be explicitly constructed by first extracting the

v[j] = 0           j < i
v[j] = 1           j == i
v[j] = a[j*lda+i]  j > i

and computing H_i = I - tau[i] * v * vᵀ.

The orthonormal matrix Q can be constructed from a product of these elementary reflectors, Q = H_0 * H_1 * ... * H_{k-1}, where k = min(m,n).

Work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= m and this function will panic otherwise. Geqrf is a blocked QR factorization, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Geqrf, the optimal work length will be stored into work[0].

Gesvd computes the singular value decomposition of the input matrix A.

The singular value decomposition is

A = U * Sigma * Vᵀ

where Sigma is an m×n diagonal matrix containing the singular values of A, U is an m×m orthogonal matrix and V is an n×n orthogonal matrix. The first min(m,n) columns of U and V are the left and right singular vectors of A respectively.

jobU and jobVT are options for computing the singular vectors. The behavior is as follows

jobU == lapack.SVDAll       All m columns of U are returned in u
jobU == lapack.SVDStore     The first min(m,n) columns are returned in u
jobU == lapack.SVDOverwrite The first min(m,n) columns of U are written into a
jobU == lapack.SVDNone      The columns of U are not computed.

The behavior is the same for jobVT and the rows of Vᵀ. At most one of jobU and jobVT can equal lapack.SVDOverwrite, and Gesvd will panic otherwise.

On entry, a contains the data for the m×n matrix A. During the call to Gesvd the data is overwritten. On exit, A contains the appropriate singular vectors if either job is lapack.SVDOverwrite.

s is a slice of length at least min(m,n) and on exit contains the singular values in decreasing order.

u contains the left singular vectors on exit, stored columnwise. If jobU == lapack.SVDAll, u is of size m×m. If jobU == lapack.SVDStore u is of size m×min(m,n). If jobU == lapack.SVDOverwrite or lapack.SVDNone, u is not used.

vt contains the left singular vectors on exit, stored rowwise. If jobV == lapack.SVDAll, vt is of size n×m. If jobVT == lapack.SVDStore vt is of size min(m,n)×n. If jobVT == lapack.SVDOverwrite or lapack.SVDNone, vt is not used.

work is a slice for storing temporary memory, and lwork is the usable size of the slice. lwork must be at least max(5*min(m,n), 3*min(m,n)+max(m,n)). If lwork == -1, instead of performing Gesvd, the optimal work length will be stored into work[0]. Gesvd will panic if the working memory has insufficient storage.

Gesvd returns whether the decomposition successfully completed.

Getrf computes the LU decomposition of an m×n matrix A using partial pivoting with row interchanges.

The LU decomposition is a factorization of A into

A = P * L * U

where P is a permutation matrix, L is a lower triangular with unit diagonal elements (lower trapezoidal if m > n), and U is upper triangular (upper trapezoidal if m < n).

On entry, a contains the matrix A. On return, L and U are stored in place into a, and P is represented by ipiv.

ipiv contains a sequence of row swaps. It indicates that row i of the matrix was interchanged with ipiv[i]. ipiv must have length min(m,n), and Getrf will panic otherwise. ipiv is zero-indexed.

Getrf returns whether the matrix A is nonsingular. The LU decomposition will be computed regardless of the singularity of A, but the result should not be used to solve a system of equation.

Getri computes the inverse of the matrix A using the LU factorization computed by Getrf. On entry, a contains the PLU decomposition of A as computed by Getrf and on exit contains the reciprocal of the original matrix.

Getri will not perform the inversion if the matrix is singular, and returns a boolean indicating whether the inversion was successful.

Work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= n and this function will panic otherwise. Getri is a blocked inversion, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Getri, the optimal work length will be stored into work[0].

Getrs solves a system of equations using an LU factorization. The system of equations solved is

A * X = B   if trans == blas.Trans
Aᵀ * X = B  if trans == blas.NoTrans

A is a general n×n matrix with stride lda. B is a general matrix of size n×nrhs.

On entry b contains the elements of the matrix B. On exit, b contains the elements of X, the solution to the system of equations.

a and ipiv contain the LU factorization of A and the permutation indices as computed by Getrf. ipiv is zero-indexed.

func Ggsvd3(jobU, jobV, jobQ [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[GSVDJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#GSVDJob), a, b [blas64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64).[General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#General), alpha, beta [][float64](https://pkg.go.dev/builtin#float64), u, v, q [blas64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64).[General](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/blas64#General), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int), iwork [][int](https://pkg.go.dev/builtin#int)) (k, l [int](https://pkg.go.dev/builtin#int), ok [bool](https://pkg.go.dev/builtin#bool))

Ggsvd3 computes the generalized singular value decomposition (GSVD) of an m×n matrix A and p×n matrix B:

Uᵀ*A*Q = D1*[ 0 R ]

Vᵀ*B*Q = D2*[ 0 R ]

where U, V and Q are orthogonal matrices.

Ggsvd3 returns k and l, the dimensions of the sub-blocks. k+l is the effective numerical rank of the (m+p)×n matrix [ Aᵀ Bᵀ ]ᵀ. R is a (k+l)×(k+l) nonsingular upper triangular matrix, D1 and D2 are m×(k+l) and p×(k+l) diagonal matrices and of the following structures, respectively:

If m-k-l >= 0,

                  k  l
     D1 =     k [ I  0 ]
              l [ 0  C ]
          m-k-l [ 0  0 ]

                k  l
     D2 = l   [ 0  S ]
          p-l [ 0  0 ]

             n-k-l  k    l
[ 0 R ] = k [  0   R11  R12 ] k
          l [  0    0   R22 ] l

where

C = diag( alpha_k, ... , alpha_{k+l} ),
S = diag( beta_k,  ... , beta_{k+l} ),
C^2 + S^2 = I.

R is stored in

A[0:k+l, n-k-l:n]

on exit.

If m-k-l < 0,

               k m-k k+l-m
    D1 =   k [ I  0    0  ]
         m-k [ 0  C    0  ]

                 k m-k k+l-m
    D2 =   m-k [ 0  S    0  ]
         k+l-m [ 0  0    I  ]
           p-l [ 0  0    0  ]

               n-k-l  k   m-k  k+l-m
[ 0 R ] =    k [ 0    R11  R12  R13 ]
           m-k [ 0     0   R22  R23 ]
         k+l-m [ 0     0    0   R33 ]

where

C = diag( alpha_k, ... , alpha_m ),
S = diag( beta_k,  ... , beta_m ),
C^2 + S^2 = I.

R = [ R11 R12 R13 ] is stored in A[1:m, n-k-l+1:n]
    [  0  R22 R23 ]

and R33 is stored in

B[m-k:l, n+m-k-l:n] on exit.

Ggsvd3 computes C, S, R, and optionally the orthogonal transformation matrices U, V and Q.

jobU, jobV and jobQ are options for computing the orthogonal matrices. The behavior is as follows

jobU == lapack.GSVDU        Compute orthogonal matrix U
jobU == lapack.GSVDNone     Do not compute orthogonal matrix.

The behavior is the same for jobV and jobQ with the exception that instead of lapack.GSVDU these accept lapack.GSVDV and lapack.GSVDQ respectively. The matrices U, V and Q must be m×m, p×p and n×n respectively unless the relevant job parameter is lapack.GSVDNone.

alpha and beta must have length n or Ggsvd3 will panic. On exit, alpha and beta contain the generalized singular value pairs of A and B

alpha[0:k] = 1,
beta[0:k]  = 0,

if m-k-l >= 0,

alpha[k:k+l] = diag(C),
beta[k:k+l]  = diag(S),

if m-k-l < 0,

alpha[k:m]= C, alpha[m:k+l]= 0
beta[k:m] = S, beta[m:k+l] = 1.

if k+l < n,

alpha[k+l:n] = 0 and
beta[k+l:n]  = 0.

On exit, iwork contains the permutation required to sort alpha descending.

iwork must have length n, work must have length at least max(1, lwork), and lwork must be -1 or greater than n, otherwise Ggsvd3 will panic. If lwork is -1, work[0] holds the optimal lwork on return, but Ggsvd3 does not perform the GSVD.

Gtsv solves one of the equations

A * X = B   if trans == blas.NoTrans
Aᵀ * X = B  if trans == blas.Trans or blas.ConjTrans

where A is an n×n tridiagonal matrix. It uses Gaussian elimination with partial pivoting.

On entry, a contains the matrix A, on return it will be overwritten.

On entry, b contains the n×nrhs right-hand side matrix B. On return, it will be overwritten. If ok is true, it will be overwritten by the solution matrix X.

Gtsv returns whether the solution X has been successfully computed.

Dgtsv is not part of the lapack.Float64 interface and so calls to Gtsv are always executed by the Gonum implementation.

Lagtm performs one of the matrix-matrix operations

C = alpha * A * B + beta * C   if trans == blas.NoTrans
C = alpha * Aᵀ * B + beta * C  if trans == blas.Trans or blas.ConjTrans

where A is an m×m tridiagonal matrix represented by its diagonals dl, d, du, B and C are m×n dense matrices, and alpha and beta are scalars.

Dlagtm is not part of the lapack.Float64 interface and so calls to Lagtm are always executed by the Gonum implementation.

Langb returns the given norm of a general m×n band matrix with kl sub-diagonals and ku super-diagonals.

Dlangb is not part of the lapack.Float64 interface and so calls to Langb are always executed by the Gonum implementation.

Lange computes the matrix norm of the general m×n matrix A. The input norm specifies the norm computed.

lapack.MaxAbs: the maximum absolute value of an element.
lapack.MaxColumnSum: the maximum column sum of the absolute values of the entries.
lapack.MaxRowSum: the maximum row sum of the absolute values of the entries.
lapack.Frobenius: the square root of the sum of the squares of the entries.

If norm == lapack.MaxColumnSum, work must be of length n, and this function will panic otherwise. There are no restrictions on work for the other matrix norms.

Langt computes the specified norm of an n×n tridiagonal matrix.

Dlangt is not part of the lapack.Float64 interface and so calls to Langt are always executed by the Gonum implementation.

Lansb computes the specified norm of an n×n symmetric band matrix. If norm == lapack.MaxColumnSum or norm == lapack.MaxRowSum, work must have length at least n and this function will panic otherwise. There are no restrictions on work for the other matrix norms.

Dlansb is not part of the lapack.Float64 interface and so calls to Lansb are always executed by the Gonum implementation.

Lansy computes the specified norm of an n×n symmetric matrix. If norm == lapack.MaxColumnSum or norm == lapack.MaxRowSum, work must have length at least n and this function will panic otherwise. There are no restrictions on work for the other matrix norms.

Lantb computes the specified norm of an n×n triangular band matrix A. If norm == lapack.MaxColumnSum work must have length at least n and this function will panic otherwise. There are no restrictions on work for the other matrix norms.

Lantr computes the specified norm of an m×n trapezoidal matrix A. If norm == lapack.MaxColumnSum work must have length at least n and this function will panic otherwise. There are no restrictions on work for the other matrix norms.

Lapmr rearranges the rows of the m×n matrix X as specified by the permutation k[0],k[1],...,k[m-1] of the integers 0,...,m-1.

If forward is true, a forward permutation is applied:

X[k[i],0:n] is moved to X[i,0:n] for i=0,1,...,m-1.

If forward is false, a backward permutation is applied:

X[i,0:n] is moved to X[k[i],0:n] for i=0,1,...,m-1.

k must have length m, otherwise Lapmr will panic. k is zero-indexed.

Lapmt rearranges the columns of the m×n matrix X as specified by the permutation k[0],k[1],...,k[n-1] of the integers 0,...,n-1.

If forward is true, a forward permutation is applied:

X[0:m,k[j]] is moved to X[0:m,j] for j=0,1,...,n-1.

If forward is false, a backward permutation is applied:

X[0:m,j] is moved to X[0:m,k[j]] for j=0,1,...,n-1.

k must have length n, otherwise Lapmt will panic. k is zero-indexed.

Orglq generates an m×n matrix Q with orthonormal rows defined as the first m rows of a product of k elementary reflectors of order n

Q = H_{k-1} * ... * H_0

as returned by Dgelqf.

k is determined by the length of tau.

On entry, tau and the first k rows of A must contain the scalar factors and the vectors, respectively, which define the elementary reflectors H_i, i=0,...,k-1, as returned by Dgelqf. On return, A contains the matrix Q.

work must have length at least lwork and lwork must be at least max(1,m). On return, optimal value of lwork will be stored in work[0]. It must also hold that 0 <= k <= m <= n, otherwise Orglq will panic.

If lwork == -1, instead of performing Orglq, the function only calculates the optimal value of lwork and stores it into work[0].

Orgqr generates an m×n matrix Q with orthonormal columns defined by the product of elementary reflectors

Q = H_0 * H_1 * ... * H_{k-1}

as computed by Geqrf.

k is determined by the length of tau.

The length of work must be at least n and it also must be that 0 <= k <= n and 0 <= n <= m.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= n, and the amount of blocking is limited by the usable length. If lwork == -1, instead of computing Orgqr the optimal work length is stored into work[0].

Orgqr will panic if the conditions on input values are not met.

Ormlq multiplies the matrix C by the othogonal matrix Q defined by A and tau. A and tau are as returned from Gelqf.

C = Q * C   if side == blas.Left and trans == blas.NoTrans
C = Qᵀ * C  if side == blas.Left and trans == blas.Trans
C = C * Q   if side == blas.Right and trans == blas.NoTrans
C = C * Qᵀ  if side == blas.Right and trans == blas.Trans

If side == blas.Left, A is a matrix of side k×m, and if side == blas.Right A is of size k×n. This uses a blocked algorithm.

Work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= m if side == blas.Left and lwork >= n if side == blas.Right, and this function will panic otherwise. Ormlq uses a block algorithm, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Ormlq, the optimal work length will be stored into work[0].

Tau contains the Householder scales and must have length at least k, and this function will panic otherwise.

Ormqr multiplies an m×n matrix C by an orthogonal matrix Q as

C = Q * C   if side == blas.Left  and trans == blas.NoTrans,
C = Qᵀ * C  if side == blas.Left  and trans == blas.Trans,
C = C * Q   if side == blas.Right and trans == blas.NoTrans,
C = C * Qᵀ  if side == blas.Right and trans == blas.Trans,

where Q is defined as the product of k elementary reflectors

Q = H_0 * H_1 * ... * H_{k-1}.

k is determined by the length of tau.

If side == blas.Left, A is an m×k matrix and 0 <= k <= m. If side == blas.Right, A is an n×k matrix and 0 <= k <= n. The ith column of A contains the vector which defines the elementary reflector H_i and tau[i] contains its scalar factor. Geqrf returns A and tau in the required form.

work must have length at least max(1,lwork), and lwork must be at least n if side == blas.Left and at least m if side == blas.Right, otherwise Ormqr will panic.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= m if side == blas.Left and lwork >= n if side == blas.Right, and this function will panic otherwise. Larger values of lwork will generally give better performance. On return, work[0] will contain the optimal value of lwork.

If lwork is -1, instead of performing Ormqr, the optimal workspace size will be stored into work[0].

Pbcon returns an estimate of the reciprocal of the condition number (in the 1-norm) of an n×n symmetric positive definite band matrix using the Cholesky factorization

A = Uᵀ*U  if uplo == blas.Upper
A = L*Lᵀ  if uplo == blas.Lower

computed by Pbtrf. The estimate is obtained for norm(inv(A)), and the reciprocal of the condition number is computed as

rcond = 1 / (anorm * norm(inv(A))).

The length of work must be at least 3*n and the length of iwork must be at least n.

Pbtrf computes the Cholesky factorization of an n×n symmetric positive definite band matrix

A = Uᵀ * U  if a.Uplo == blas.Upper
A = L * Lᵀ  if a.Uplo == blas.Lower

where U and L are upper, respectively lower, triangular band matrices.

The triangular matrix U or L is returned in t, and the underlying data between a and t is shared. The returned bool indicates whether A is positive definite and the factorization could be finished.

Pbtrs solves a system of linear equations A*X = B with an n×n symmetric positive definite band matrix A using the Cholesky factorization

A = Uᵀ * U  if t.Uplo == blas.Upper
A = L * Lᵀ  if t.Uplo == blas.Lower

t contains the corresponding triangular factor as returned by Pbtrf.

On entry, b contains the right hand side matrix B. On return, it is overwritten with the solution matrix X.

Pocon estimates the reciprocal of the condition number of a positive-definite matrix A given the Cholesky decomposition of A. The condition number computed is based on the 1-norm and the ∞-norm.

anorm is the 1-norm and the ∞-norm of the original matrix A.

work is a temporary data slice of length at least 3*n and Pocon will panic otherwise.

iwork is a temporary data slice of length at least n and Pocon will panic otherwise.

Potrf computes the Cholesky factorization of a. The factorization has the form

A = Uᵀ * U  if a.Uplo == blas.Upper, or
A = L * Lᵀ  if a.Uplo == blas.Lower,

where U is an upper triangular matrix and L is lower triangular. The triangular matrix is returned in t, and the underlying data between a and t is shared. The returned bool indicates whether a is positive definite and the factorization could be finished.

Potri computes the inverse of a real symmetric positive definite matrix A using its Cholesky factorization.

On entry, t contains the triangular factor U or L from the Cholesky factorization A = Uᵀ*U or A = L*Lᵀ, as computed by Potrf.

On return, the upper or lower triangle of the (symmetric) inverse of A is stored in t, overwriting the input factor U or L, and also returned in a. The underlying data between a and t is shared.

The returned bool indicates whether the inverse was computed successfully.

Potrs solves a system of n linear equations A*X = B where A is an n×n symmetric positive definite matrix and B is an n×nrhs matrix, using the Cholesky factorization A = Uᵀ*U or A = L*Lᵀ. t contains the corresponding triangular factor as returned by Potrf. On entry, B contains the right-hand side matrix B, on return it contains the solution matrix X.

Pstrf computes the Cholesky factorization with complete pivoting of an n×n symmetric positive semidefinite matrix A.

The factorization has the form

Pᵀ * A * P = Uᵀ * U ,  if a.Uplo = blas.Upper,
Pᵀ * A * P = L  * Lᵀ,  if a.Uplo = blas.Lower,

where U is an upper triangular matrix, L is lower triangular, and P is a permutation matrix.

tol is a user-defined tolerance. The algorithm terminates if the pivot is less than or equal to tol. If tol is negative, then n*eps*max(A[k,k]) will be used instead.

The triangular factor U or L from the Cholesky factorization is returned in t and the underlying data between a and t is shared. P is stored on return in vector piv such that P[piv[k],k] = 1.

Pstrf returns the computed rank of A and whether the factorization can be used to solve a system. Pstrf does not attempt to check that A is positive semi-definite, so if ok is false, the matrix A is either rank deficient or is not positive semidefinite.

The length of piv must be n and the length of work must be at least 2*n, otherwise Pstrf will panic.

Syev computes all eigenvalues and, optionally, the eigenvectors of a real symmetric matrix A.

w contains the eigenvalues in ascending order upon return. w must have length at least n, and Syev will panic otherwise.

On entry, a contains the elements of the symmetric matrix A in the triangular portion specified by uplo. If jobz == lapack.EVCompute, a contains the orthonormal eigenvectors of A on exit, otherwise jobz must be lapack.EVNone and on exit the specified triangular region is overwritten.

Work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= 3*n-1, and Syev will panic otherwise. The amount of blocking is limited by the usable length. If lwork == -1, instead of computing Syev the optimal work length is stored into work[0].

Tbtrs solves a triangular system of the form

A * X = B   if trans == blas.NoTrans
Aᵀ * X = B  if trans == blas.Trans or blas.ConjTrans

where A is an n×n triangular band matrix, and B is an n×nrhs matrix.

Tbtrs returns whether A is non-singular. If A is singular, no solutions X are computed.

Trcon estimates the reciprocal of the condition number of a triangular matrix A. The condition number computed may be based on the 1-norm or the ∞-norm.

work is a temporary data slice of length at least 3*n and Trcon will panic otherwise.

iwork is a temporary data slice of length at least n and Trcon will panic otherwise.

Trtri computes the inverse of a triangular matrix, storing the result in place into a.

Trtri will not perform the inversion if the matrix is singular, and returns a boolean indicating whether the inversion was successful.

Trtrs solves a triangular system of the form A * X = B or Aᵀ * X = B. Trtrs returns whether the solve completed successfully. If A is singular, no solve is performed.

Use sets the LAPACK float64 implementation to be used by subsequent BLAS calls. The default implementation is native.Implementation.

Tridiagonal represents a tridiagonal matrix using its three diagonals.
