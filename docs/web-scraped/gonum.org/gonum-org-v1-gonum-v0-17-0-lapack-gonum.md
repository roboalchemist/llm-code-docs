# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum

Title: gonum package - gonum.org/v1/gonum/lapack/gonum - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum

Markdown Content:
Package gonum is a pure-go implementation of the LAPACK API. The LAPACK API defines a set of algorithms for advanced matrix operations.

The function definitions and implementations follow that of the netlib reference implementation. See [http://www.netlib.org/lapack/explore-html/](http://www.netlib.org/lapack/explore-html/) for more information, and [http://www.netlib.org/lapack/explore-html/d4/de1/_l_i_c_e_n_s_e_source.html](http://www.netlib.org/lapack/explore-html/d4/de1/_l_i_c_e_n_s_e_source.html) for more license information.

Slice function arguments frequently represent vectors and matrices. The data layout is identical to that found in [https://pkg.go.dev/gonum.org/v1/gonum/blas/gonum](https://pkg.go.dev/gonum.org/v1/gonum/blas/gonum).

Most LAPACK functions are built on top the routines defined in the BLAS API, and as such the computation time for many LAPACK functions is dominated by BLAS calls. Here, BLAS is accessed through the blas64 package ([https://pkg.go.dev/gonum.org/v1/gonum/blas/blas64](https://pkg.go.dev/gonum.org/v1/gonum/blas/blas64)). In particular, this implies that an external BLAS library will be used if it is registered in blas64.

The full LAPACK capability has not been implemented at present. The full API is very large, containing approximately 200 functions for double precision alone. Future additions will be focused on supporting the Gonum matrix package ([https://pkg.go.dev/gonum.org/v1/gonum/mat](https://pkg.go.dev/gonum.org/v1/gonum/mat)), though pull requests with implementations and tests for LAPACK function are encouraged.

*   [type Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)
*       *   [func (impl Implementation) Dbdsqr(uplo blas.Uplo, n, ncvt, nru, ncc int, d, e, vt []float64, ldvt int, ...) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dbdsqr)
    *   [func (impl Implementation) Dgebak(job lapack.BalanceJob, side lapack.EVSide, n, ilo, ihi int, scale []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgebak)
    *   [func (impl Implementation) Dgebal(job lapack.BalanceJob, n int, a []float64, lda int, scale []float64) (ilo, ihi int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgebal)
    *   [func (impl Implementation) Dgebd2(m, n int, a []float64, lda int, d, e, tauQ, tauP, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgebd2)
    *   [func (impl Implementation) Dgebrd(m, n int, a []float64, lda int, d, e, tauQ, tauP, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgebrd)
    *   [func (impl Implementation) Dgecon(norm lapack.MatrixNorm, n int, a []float64, lda int, anorm float64, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgecon)
    *   [func (impl Implementation) Dgeev(jobvl lapack.LeftEVJob, jobvr lapack.RightEVJob, n int, a []float64, lda int, ...) (first int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgeev)
    *   [func (impl Implementation) Dgehd2(n, ilo, ihi int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgehd2)
    *   [func (impl Implementation) Dgehrd(n, ilo, ihi int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgehrd)
    *   [func (impl Implementation) Dgelq2(m, n int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgelq2)
    *   [func (impl Implementation) Dgelqf(m, n int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgelqf)
    *   [func (impl Implementation) Dgels(trans blas.Transpose, m, n, nrhs int, a []float64, lda int, b []float64, ...) bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgels)
    *   [func (impl Implementation) Dgeql2(m, n int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgeql2)
    *   [func (impl Implementation) Dgeqp3(m, n int, a []float64, lda int, jpvt []int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgeqp3)
    *   [func (impl Implementation) Dgeqr2(m, n int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgeqr2)
    *   [func (impl Implementation) Dgeqrf(m, n int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgeqrf)
    *   [func (impl Implementation) Dgerq2(m, n int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgerq2)
    *   [func (impl Implementation) Dgerqf(m, n int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgerqf)
    *   [func (impl Implementation) Dgesc2(n int, a []float64, lda int, rhs []float64, ipiv, jpiv []int) (scale float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgesc2)
    *   [func (impl Implementation) Dgesv(n, nrhs int, a []float64, lda int, ipiv []int, b []float64, ldb int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgesv)
    *   [func (impl Implementation) Dgesvd(jobU, jobVT lapack.SVDJob, m, n int, a []float64, lda int, s, u []float64, ...) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgesvd)
    *   [func (impl Implementation) Dgetc2(n int, a []float64, lda int, ipiv, jpiv []int) (k int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgetc2)
    *   [func (Implementation) Dgetf2(m, n int, a []float64, lda int, ipiv []int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgetf2)
    *   [func (impl Implementation) Dgetrf(m, n int, a []float64, lda int, ipiv []int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgetrf)
    *   [func (impl Implementation) Dgetri(n int, a []float64, lda int, ipiv []int, work []float64, lwork int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgetri)
    *   [func (impl Implementation) Dgetrs(trans blas.Transpose, n, nrhs int, a []float64, lda int, ipiv []int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgetrs)
    *   [func (impl Implementation) Dgghrd(compq, compz lapack.OrthoComp, n, ilo, ihi int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgghrd)
    *   [func (impl Implementation) Dggsvd3(jobU, jobV, jobQ lapack.GSVDJob, m, n, p int, a []float64, lda int, ...) (k, l int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dggsvd3)
    *   [func (impl Implementation) Dggsvp3(jobU, jobV, jobQ lapack.GSVDJob, m, p, n int, a []float64, lda int, ...) (k, l int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dggsvp3)
    *   [func (impl Implementation) Dgtsv(n, nrhs int, dl, d, du []float64, b []float64, ldb int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dgtsv)
    *   [func (impl Implementation) Dhseqr(job lapack.SchurJob, compz lapack.SchurComp, n, ilo, ihi int, h []float64, ...) (unconverged int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dhseqr)
    *   [func (impl Implementation) Dlabrd(m, n, nb int, a []float64, lda int, d, e, tauQ, tauP, x []float64, ldx int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlabrd)
    *   [func (impl Implementation) Dlacn2(n int, v, x []float64, isgn []int, est float64, kase int, isave *[3]int) (float64, int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlacn2)
    *   [func (impl Implementation) Dlacpy(uplo blas.Uplo, m, n int, a []float64, lda int, b []float64, ldb int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlacpy)
    *   [func (impl Implementation) Dlae2(a, b, c float64) (rt1, rt2 float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlae2)
    *   [func (impl Implementation) Dlaev2(a, b, c float64) (rt1, rt2, cs1, sn1 float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaev2)
    *   [func (impl Implementation) Dlaexc(wantq bool, n int, t []float64, ldt int, q []float64, ldq int, j1, n1, n2 int, ...) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaexc)
    *   [func (Implementation) Dlag2(a []float64, lda int, b []float64, ldb int) (scale1, scale2, wr1, wr2, wi float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlag2)
    *   [func (impl Implementation) Dlags2(upper bool, a1, a2, a3, b1, b2, b3 float64) (csu, snu, csv, snv, csq, snq float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlags2)
    *   [func (impl Implementation) Dlagtm(trans blas.Transpose, m, n int, alpha float64, dl, d, du []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlagtm)
    *   [func (impl Implementation) Dlahqr(wantt, wantz bool, n, ilo, ihi int, h []float64, ldh int, wr, wi []float64, ...) (unconverged int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlahqr)
    *   [func (impl Implementation) Dlahr2(n, k, nb int, a []float64, lda int, tau, t []float64, ldt int, y []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlahr2)
    *   [func (impl Implementation) Dlaln2(trans bool, na, nw int, smin, ca float64, a []float64, lda int, d1, d2 float64, ...) (scale, xnorm float64, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaln2)
    *   [func (impl Implementation) Dlangb(norm lapack.MatrixNorm, m, n, kl, ku int, ab []float64, ldab int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlangb)
    *   [func (impl Implementation) Dlange(norm lapack.MatrixNorm, m, n int, a []float64, lda int, work []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlange)
    *   [func (impl Implementation) Dlangt(norm lapack.MatrixNorm, n int, dl, d, du []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlangt)
    *   [func (impl Implementation) Dlanhs(norm lapack.MatrixNorm, n int, a []float64, lda int, work []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlanhs)
    *   [func (impl Implementation) Dlansb(norm lapack.MatrixNorm, uplo blas.Uplo, n, kd int, ab []float64, ldab int, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlansb)
    *   [func (impl Implementation) Dlanst(norm lapack.MatrixNorm, n int, d, e []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlanst)
    *   [func (impl Implementation) Dlansy(norm lapack.MatrixNorm, uplo blas.Uplo, n int, a []float64, lda int, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlansy)
    *   [func (impl Implementation) Dlantb(norm lapack.MatrixNorm, uplo blas.Uplo, diag blas.Diag, n, k int, a []float64, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlantb)
    *   [func (impl Implementation) Dlantr(norm lapack.MatrixNorm, uplo blas.Uplo, diag blas.Diag, m, n int, a []float64, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlantr)
    *   [func (impl Implementation) Dlanv2(a, b, c, d float64) (aa, bb, cc, dd float64, rt1r, rt1i, rt2r, rt2i float64, cs, sn float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlanv2)
    *   [func (impl Implementation) Dlapll(n int, x []float64, incX int, y []float64, incY int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlapll)
    *   [func (impl Implementation) Dlapmr(forward bool, m, n int, x []float64, ldx int, k []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlapmr)
    *   [func (impl Implementation) Dlapmt(forward bool, m, n int, x []float64, ldx int, k []int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlapmt)
    *   [func (Implementation) Dlapy2(x, y float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlapy2)
    *   [func (impl Implementation) Dlaqp2(m, n, offset int, a []float64, lda int, jpvt []int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaqp2)
    *   [func (impl Implementation) Dlaqps(m, n, offset, nb int, a []float64, lda int, jpvt []int, ...) (kb int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaqps)
    *   [func (impl Implementation) Dlaqr1(n int, h []float64, ldh int, sr1, si1, sr2, si2 float64, v []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaqr1)
    *   [func (impl Implementation) Dlaqr04(wantt, wantz bool, n, ilo, ihi int, h []float64, ldh int, wr, wi []float64, ...) (unconverged int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaqr04)
    *   [func (impl Implementation) Dlaqr5(wantt, wantz bool, kacc22 int, n, ktop, kbot, nshfts int, sr, si []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaqr5)
    *   [func (impl Implementation) Dlaqr23(wantt, wantz bool, n, ktop, kbot, nw int, h []float64, ldh int, iloz, ihiz int, ...) (ns, nd int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaqr23)
    *   [func (impl Implementation) Dlarf(side blas.Side, m, n int, v []float64, incv int, tau float64, c []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlarf)
    *   [func (Implementation) Dlarfb(side blas.Side, trans blas.Transpose, direct lapack.Direct, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlarfb)
    *   [func (impl Implementation) Dlarfg(n int, alpha float64, x []float64, incX int) (beta, tau float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlarfg)
    *   [func (Implementation) Dlarft(direct lapack.Direct, store lapack.StoreV, n, k int, v []float64, ldv int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlarft)
    *   [func (impl Implementation) Dlarfx(side blas.Side, m, n int, v []float64, tau float64, c []float64, ldc int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlarfx)
    *   [func (impl Implementation) Dlartg(f, g float64) (cs, sn, r float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlartg)
    *   [func (impl Implementation) Dlas2(f, g, h float64) (ssmin, ssmax float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlas2)
    *   [func (impl Implementation) Dlascl(kind lapack.MatrixType, kl, ku int, cfrom, cto float64, m, n int, a []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlascl)
    *   [func (impl Implementation) Dlaset(uplo blas.Uplo, m, n int, alpha, beta float64, a []float64, lda int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaset)
    *   [func (impl Implementation) Dlasq1(n int, d, e, work []float64) (info int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasq1)
    *   [func (impl Implementation) Dlasq2(n int, z []float64) (info int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasq2)
    *   [func (impl Implementation) Dlasq3(i0, n0 int, z []float64, pp int, dmin, sigma, desig, qmax float64, ...) (i0Out, n0Out, ppOut int, dminOut, sigmaOut, desigOut, qmaxOut float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasq3)
    *   [func (impl Implementation) Dlasq4(i0, n0 int, z []float64, pp int, n0in int, ...) (tauOut float64, ttypeOut int, gOut float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasq4)
    *   [func (impl Implementation) Dlasq5(i0, n0 int, z []float64, pp int, tau, sigma float64) (i0Out, n0Out, ppOut int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasq5)
    *   [func (impl Implementation) Dlasq6(i0, n0 int, z []float64, pp int) (dmin, dmin1, dmin2, dn, dnm1, dnm2 float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasq6)
    *   [func (impl Implementation) Dlasr(side blas.Side, pivot lapack.Pivot, direct lapack.Direct, m, n int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasr)
    *   [func (impl Implementation) Dlasrt(s lapack.Sort, n int, d []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasrt)
    *   [func (impl Implementation) Dlassq(n int, x []float64, incx int, scale float64, sumsq float64) (scl, smsq float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlassq)
    *   [func (impl Implementation) Dlasv2(f, g, h float64) (ssmin, ssmax, snr, csr, snl, csl float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasv2)
    *   [func (impl Implementation) Dlaswp(n int, a []float64, lda int, k1, k2 int, ipiv []int, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlaswp)
    *   [func (impl Implementation) Dlasy2(tranl, tranr bool, isgn, n1, n2 int, tl []float64, ldtl int, tr []float64, ...) (scale, xnorm float64, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlasy2)
    *   [func (Implementation) Dlatbs(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, normin bool, n, kd int, ...) (scale float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlatbs)
    *   [func (impl Implementation) Dlatdf(job lapack.MaximizeNormXJob, n int, z []float64, ldz int, rhs []float64, ...) (scale, sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlatdf)
    *   [func (impl Implementation) Dlatrd(uplo blas.Uplo, n, nb int, a []float64, lda int, e, tau, w []float64, ldw int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlatrd)
    *   [func (impl Implementation) Dlatrs(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, normin bool, n int, ...) (scale float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlatrs)
    *   [func (impl Implementation) Dlauu2(uplo blas.Uplo, n int, a []float64, lda int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlauu2)
    *   [func (impl Implementation) Dlauum(uplo blas.Uplo, n int, a []float64, lda int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dlauum)
    *   [func (impl Implementation) Dorg2l(m, n, k int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorg2l)
    *   [func (impl Implementation) Dorg2r(m, n, k int, a []float64, lda int, tau []float64, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorg2r)
    *   [func (impl Implementation) Dorgbr(vect lapack.GenOrtho, m, n, k int, a []float64, lda int, tau, work []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorgbr)
    *   [func (impl Implementation) Dorghr(n, ilo, ihi int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorghr)
    *   [func (impl Implementation) Dorgl2(m, n, k int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorgl2)
    *   [func (impl Implementation) Dorglq(m, n, k int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorglq)
    *   [func (impl Implementation) Dorgql(m, n, k int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorgql)
    *   [func (impl Implementation) Dorgqr(m, n, k int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorgqr)
    *   [func (impl Implementation) Dorgr2(m, n, k int, a []float64, lda int, tau, work []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorgr2)
    *   [func (impl Implementation) Dorgtr(uplo blas.Uplo, n int, a []float64, lda int, tau, work []float64, lwork int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorgtr)
    *   [func (impl Implementation) Dorm2r(side blas.Side, trans blas.Transpose, m, n, k int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorm2r)
    *   [func (impl Implementation) Dormbr(vect lapack.ApplyOrtho, side blas.Side, trans blas.Transpose, m, n, k int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dormbr)
    *   [func (impl Implementation) Dormhr(side blas.Side, trans blas.Transpose, m, n, ilo, ihi int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dormhr)
    *   [func (impl Implementation) Dorml2(side blas.Side, trans blas.Transpose, m, n, k int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dorml2)
    *   [func (impl Implementation) Dormlq(side blas.Side, trans blas.Transpose, m, n, k int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dormlq)
    *   [func (impl Implementation) Dormqr(side blas.Side, trans blas.Transpose, m, n, k int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dormqr)
    *   [func (impl Implementation) Dormr2(side blas.Side, trans blas.Transpose, m, n, k int, a []float64, lda int, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dormr2)
    *   [func (impl Implementation) Dpbcon(uplo blas.Uplo, n, kd int, ab []float64, ldab int, anorm float64, ...) (rcond float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpbcon)
    *   [func (Implementation) Dpbtf2(uplo blas.Uplo, n, kd int, ab []float64, ldab int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpbtf2)
    *   [func (impl Implementation) Dpbtrf(uplo blas.Uplo, n, kd int, ab []float64, ldab int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpbtrf)
    *   [func (Implementation) Dpbtrs(uplo blas.Uplo, n, kd, nrhs int, ab []float64, ldab int, b []float64, ldb int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpbtrs)
    *   [func (impl Implementation) Dpocon(uplo blas.Uplo, n int, a []float64, lda int, anorm float64, work []float64, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpocon)
    *   [func (Implementation) Dpotf2(ul blas.Uplo, n int, a []float64, lda int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpotf2)
    *   [func (impl Implementation) Dpotrf(ul blas.Uplo, n int, a []float64, lda int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpotrf)
    *   [func (impl Implementation) Dpotri(uplo blas.Uplo, n int, a []float64, lda int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpotri)
    *   [func (Implementation) Dpotrs(uplo blas.Uplo, n, nrhs int, a []float64, lda int, b []float64, ldb int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpotrs)
    *   [func (Implementation) Dpstf2(uplo blas.Uplo, n int, a []float64, lda int, piv []int, tol float64, ...) (rank int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpstf2)
    *   [func (impl Implementation) Dpstrf(uplo blas.Uplo, n int, a []float64, lda int, piv []int, tol float64, ...) (rank int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpstrf)
    *   [func (impl Implementation) Dptcon(n int, d, e []float64, anorm float64, work []float64) (rcond float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dptcon)
    *   [func (impl Implementation) Dptsv(n, nrhs int, d, e []float64, b []float64, ldb int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dptsv)
    *   [func (impl Implementation) Dpttrf(n int, d, e []float64) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpttrf)
    *   [func (impl Implementation) Dpttrs(n, nrhs int, d, e []float64, b []float64, ldb int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dpttrs)
    *   [func (impl Implementation) Drscl(n int, a float64, x []float64, incX int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Drscl)
    *   [func (impl Implementation) Dsteqr(compz lapack.EVComp, n int, d, e, z []float64, ldz int, work []float64) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dsteqr)
    *   [func (impl Implementation) Dsterf(n int, d, e []float64) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dsterf)
    *   [func (impl Implementation) Dsyev(jobz lapack.EVJob, uplo blas.Uplo, n int, a []float64, lda int, ...) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dsyev)
    *   [func (impl Implementation) Dsytd2(uplo blas.Uplo, n int, a []float64, lda int, d, e, tau []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dsytd2)
    *   [func (impl Implementation) Dsytrd(uplo blas.Uplo, n int, a []float64, lda int, d, e, tau, work []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dsytrd)
    *   [func (impl Implementation) Dtbtrs(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n, kd, nrhs int, ...) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtbtrs)
    *   [func (impl Implementation) Dtgsja(jobU, jobV, jobQ lapack.GSVDJob, m, p, n, k, l int, a []float64, lda int, ...) (cycles int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtgsja)
    *   [func (impl Implementation) Dtrcon(norm lapack.MatrixNorm, uplo blas.Uplo, diag blas.Diag, n int, a []float64, ...) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtrcon)
    *   [func (impl Implementation) Dtrevc3(side lapack.EVSide, howmny lapack.EVHowMany, selected []bool, n int, ...) (m int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtrevc3)
    *   [func (impl Implementation) Dtrexc(compq lapack.UpdateSchurComp, n int, t []float64, ldt int, q []float64, ...) (ifstOut, ilstOut int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtrexc)
    *   [func (impl Implementation) Dtrti2(uplo blas.Uplo, diag blas.Diag, n int, a []float64, lda int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtrti2)
    *   [func (impl Implementation) Dtrtri(uplo blas.Uplo, diag blas.Diag, n int, a []float64, lda int) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtrtri)
    *   [func (impl Implementation) Dtrtrs(uplo blas.Uplo, trans blas.Transpose, diag blas.Diag, n, nrhs int, a []float64, ...) (ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Dtrtrs)
    *   [func (Implementation) Iladlc(m, n int, a []float64, lda int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Iladlc)
    *   [func (Implementation) Iladlr(m, n int, a []float64, lda int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Iladlr)
    *   [func (impl Implementation) Ilaenv(ispec int, name string, opts string, n1, n2, n3, n4 int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Ilaenv)
    *   [func (Implementation) Iparmq(ispec int, name, opts string, n, ilo, ihi, lwork int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation.Iparmq)

This section is empty.

This section is empty.

This section is empty.

type Implementation struct{}

Implementation is the native Go implementation of LAPACK routines. It is built on top of calls to the return of blas64.Implementation(), so while this code is in pure Go, the underlying BLAS implementation may not be.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dbdsqr(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), n, ncvt, nru, ncc [int](https://pkg.go.dev/builtin#int), d, e, vt [][float64](https://pkg.go.dev/builtin#float64), ldvt [int](https://pkg.go.dev/builtin#int), u [][float64](https://pkg.go.dev/builtin#float64), ldu [int](https://pkg.go.dev/builtin#int), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64)) (ok [bool](https://pkg.go.dev/builtin#bool))

Dbdsqr performs a singular value decomposition of a real n×n bidiagonal matrix.

The SVD of the bidiagonal matrix B is

B = Q * S * Pᵀ

where S is a diagonal matrix of singular values, Q is an orthogonal matrix of left singular vectors, and P is an orthogonal matrix of right singular vectors.

Q and P are only computed if requested. If left singular vectors are requested, this routine returns U * Q instead of Q, and if right singular vectors are requested Pᵀ * VT is returned instead of Pᵀ.

Frequently Dbdsqr is used in conjunction with Dgebrd which reduces a general matrix A into bidiagonal form. In this case, the SVD of A is

A = (U * Q) * S * (Pᵀ * VT)

This routine may also compute Qᵀ * C.

d and e contain the elements of the bidiagonal matrix b. d must have length at least n, and e must have length at least n-1. Dbdsqr will panic if there is insufficient length. On exit, D contains the singular values of B in decreasing order.

VT is a matrix of size n×ncvt whose elements are stored in vt. The elements of vt are modified to contain Pᵀ * VT on exit. VT is not used if ncvt == 0.

U is a matrix of size nru×n whose elements are stored in u. The elements of u are modified to contain U * Q on exit. U is not used if nru == 0.

C is a matrix of size n×ncc whose elements are stored in c. The elements of c are modified to contain Qᵀ * C on exit. C is not used if ncc == 0.

work contains temporary storage and must have length at least 4*(n-1). Dbdsqr will panic if there is insufficient working memory.

Dbdsqr returns whether the decomposition was successful.

Dbdsqr is an internal routine. It is exported for testing purposes.

Dgebak updates an n×m matrix V as

V = P D V       if side == lapack.EVRight,
V = P D^{-1} V  if side == lapack.EVLeft,

where P and D are n×n permutation and scaling matrices, respectively, implicitly represented by job, scale, ilo and ihi as returned by Dgebal.

Typically, columns of the matrix V contain the right or left (determined by side) eigenvectors of the balanced matrix output by Dgebal, and Dgebak forms the eigenvectors of the original matrix.

Dgebak is an internal routine. It is exported for testing purposes.

Dgebal balances an n×n matrix A. Balancing consists of two stages, permuting and scaling. Both steps are optional and depend on the value of job.

Permuting consists of applying a permutation matrix P such that the matrix that results from Pᵀ*A*P takes the upper block triangular form

         [ T1  X  Y  ]
Pᵀ A P = [  0  B  Z  ],
         [  0  0  T2 ]

where T1 and T2 are upper triangular matrices and B contains at least one nonzero off-diagonal element in each row and column. The indices ilo and ihi mark the starting and ending columns of the submatrix B. The eigenvalues of A isolated in the first 0 to ilo-1 and last ihi+1 to n-1 elements on the diagonal can be read off without any roundoff error.

Scaling consists of applying a diagonal similarity transformation D such that D^{-1}*B*D has the 1-norm of each row and its corresponding column nearly equal. The output matrix is

[ T1     X*D          Y    ]
[  0  inv(D)*B*D  inv(D)*Z ].
[  0      0           T2   ]

Scaling may reduce the 1-norm of the matrix, and improve the accuracy of the computed eigenvalues and/or eigenvectors.

job specifies the operations that will be performed on A. If job is lapack.BalanceNone, Dgebal sets scale[i] = 1 for all i and returns ilo=0, ihi=n-1. If job is lapack.Permute, only permuting will be done. If job is lapack.Scale, only scaling will be done. If job is lapack.PermuteScale, both permuting and scaling will be done.

On return, if job is lapack.Permute or lapack.PermuteScale, it will hold that

A[i,j] == 0,   for i > j and j ∈ {0, ..., ilo-1, ihi+1, ..., n-1}.

If job is lapack.BalanceNone or lapack.Scale, or if n == 0, it will hold that

ilo == 0 and ihi == n-1.

On return, scale will contain information about the permutations and scaling factors applied to A. If π(j) denotes the index of the column interchanged with column j, and D[j,j] denotes the scaling factor applied to column j, then

scale[j] == π(j),     for j ∈ {0, ..., ilo-1, ihi+1, ..., n-1},
         == D[j,j],   for j ∈ {ilo, ..., ihi}.

scale must have length equal to n, otherwise Dgebal will panic.

Dgebal is an internal routine. It is exported for testing purposes.

Dgebd2 reduces an m×n matrix A to upper or lower bidiagonal form by an orthogonal transformation.

Qᵀ * A * P = B

if m >= n, B is upper diagonal, otherwise B is lower bidiagonal. d is the diagonal, len = min(m,n) e is the off-diagonal len = min(m,n)-1

Dgebd2 is an internal routine. It is exported for testing purposes.

Dgebrd reduces a general m×n matrix A to upper or lower bidiagonal form B by an orthogonal transformation:

Qᵀ * A * P = B.

The diagonal elements of B are stored in d and the off-diagonal elements are stored in e. These are additionally stored along the diagonal of A and the off-diagonal of A. If m >= n B is an upper-bidiagonal matrix, and if m < n B is a lower-bidiagonal matrix.

The remaining elements of A store the data needed to construct Q and P. The matrices Q and P are products of elementary reflectors

if m >= n, Q = H_0 * H_1 * ... * H_{n-1},
           P = G_0 * G_1 * ... * G_{n-2},
if m < n,  Q = H_0 * H_1 * ... * H_{m-2},
           P = G_0 * G_1 * ... * G_{m-1},

where

H_i = I - tauQ[i] * v_i * v_iᵀ,
G_i = I - tauP[i] * u_i * u_iᵀ.

As an example, on exit the entries of A when m = 6, and n = 5

[ d   e  u1  u1  u1]
[v1   d   e  u2  u2]
[v1  v2   d   e  u3]
[v1  v2  v3   d   e]
[v1  v2  v3  v4   d]
[v1  v2  v3  v4  v5]

and when m = 5, n = 6

[ d  u1  u1  u1  u1  u1]
[ e   d  u2  u2  u2  u2]
[v1   e   d  u3  u3  u3]
[v1  v2   e   d  u4  u4]
[v1  v2  v3   e   d  u5]

d, tauQ, and tauP must all have length at least min(m,n), and e must have length min(m,n) - 1, unless lwork is -1 when there is no check except for work which must have a length of at least one.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= max(1,m,n) or be -1 and this function will panic otherwise. Dgebrd is blocked decomposition, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Dgebrd, the optimal work length will be stored into work[0].

Dgebrd is an internal routine. It is exported for testing purposes.

Dgecon estimates and returns the reciprocal of the condition number of the n×n matrix A, in either the 1-norm or the ∞-norm, using the LU factorization computed by Dgetrf.

An estimate is obtained for norm(A⁻¹), and the reciprocal of the condition number rcond is computed as

rcond 1 / ( norm(A) * norm(A⁻¹) ).

If n is zero, rcond is always 1.

anorm is the 1-norm or the ∞-norm of the original matrix A. anorm must be non-negative, otherwise Dgecon will panic. If anorm is 0 or infinity, Dgecon returns 0. If anorm is NaN, Dgecon returns NaN.

work must have length at least 4*n and iwork must have length at least n, otherwise Dgecon will panic.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dgeev(jobvl [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[LeftEVJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#LeftEVJob), jobvr [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[RightEVJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#RightEVJob), n [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), wr, wi [][float64](https://pkg.go.dev/builtin#float64), vl [][float64](https://pkg.go.dev/builtin#float64), ldvl [int](https://pkg.go.dev/builtin#int), vr [][float64](https://pkg.go.dev/builtin#float64), ldvr [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int)) (first [int](https://pkg.go.dev/builtin#int))

Dgeev computes the eigenvalues and, optionally, the left and/or right eigenvectors for an n×n real nonsymmetric matrix A.

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

Left eigenvectors will be computed only if jobvl == lapack.LeftEVCompute, otherwise jobvl must be lapack.LeftEVNone. Right eigenvectors will be computed only if jobvr == lapack.RightEVCompute, otherwise jobvr must be lapack.RightEVNone. For other values of jobvl and jobvr Dgeev will panic.

wr and wi contain the real and imaginary parts, respectively, of the computed eigenvalues. Complex conjugate pairs of eigenvalues appear consecutively with the eigenvalue having the positive imaginary part first. wr and wi must have length n, and Dgeev will panic otherwise.

work must have length at least lwork and lwork must be at least max(1,4*n) if the left or right eigenvectors are computed, and at least max(1,3*n) if no eigenvectors are computed. For good performance, lwork must generally be larger. On return, optimal value of lwork will be stored in work[0].

If lwork == -1, instead of performing Dgeev, the function only calculates the optimal value of lwork and stores it into work[0].

On return, first is the index of the first valid eigenvalue. If first == 0, all eigenvalues and eigenvectors have been computed. If first is positive, Dgeev failed to compute all the eigenvalues, no eigenvectors have been computed and wr[first:] and wi[first:] contain those eigenvalues which have converged.

Dgehd2 reduces a block of a general n×n matrix A to upper Hessenberg form H by an orthogonal similarity transformation Qᵀ * A * Q = H.

The matrix Q is represented as a product of (ihi-ilo) elementary reflectors

Q = H_{ilo} H_{ilo+1} ... H_{ihi-1}.

Each H_i has the form

H_i = I - tau[i] * v * vᵀ

where v is a real vector with v[0:i+1] = 0, v[i+1] = 1 and v[ihi+1:n] = 0. v[i+2:ihi+1] is stored on exit in A[i+2:ihi+1,i].

On entry, a contains the n×n general matrix to be reduced. On return, the upper triangle and the first subdiagonal of A are overwritten with the upper Hessenberg matrix H, and the elements below the first subdiagonal, with the slice tau, represent the orthogonal matrix Q as a product of elementary reflectors.

The contents of A are illustrated by the following example, with n = 7, ilo = 1 and ihi = 5. On entry,

[ a   a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[                         a ]

on return,

[ a   a   h   h   h   h   a ]
[     a   h   h   h   h   a ]
[     h   h   h   h   h   h ]
[     v1  h   h   h   h   h ]
[     v1  v2  h   h   h   h ]
[     v1  v2  v3  h   h   h ]
[                         a ]

where a denotes an element of the original matrix A, h denotes a modified element of the upper Hessenberg matrix H, and vi denotes an element of the vector defining H_i.

ilo and ihi determine the block of A that will be reduced to upper Hessenberg form. It must hold that 0 <= ilo <= ihi <= max(0, n-1), otherwise Dgehd2 will panic.

On return, tau will contain the scalar factors of the elementary reflectors. It must have length equal to n-1, otherwise Dgehd2 will panic.

work must have length at least n, otherwise Dgehd2 will panic.

Dgehd2 is an internal routine. It is exported for testing purposes.

Dgehrd reduces a block of a real n×n general matrix A to upper Hessenberg form H by an orthogonal similarity transformation Qᵀ * A * Q = H.

The matrix Q is represented as a product of (ihi-ilo) elementary reflectors

Q = H_{ilo} H_{ilo+1} ... H_{ihi-1}.

Each H_i has the form

H_i = I - tau[i] * v * vᵀ

where v is a real vector with v[0:i+1] = 0, v[i+1] = 1 and v[ihi+1:n] = 0. v[i+2:ihi+1] is stored on exit in A[i+2:ihi+1,i].

On entry, a contains the n×n general matrix to be reduced. On return, the upper triangle and the first subdiagonal of A will be overwritten with the upper Hessenberg matrix H, and the elements below the first subdiagonal, with the slice tau, represent the orthogonal matrix Q as a product of elementary reflectors.

The contents of a are illustrated by the following example, with n = 7, ilo = 1 and ihi = 5. On entry,

[ a   a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[     a   a   a   a   a   a ]
[                         a ]

on return,

[ a   a   h   h   h   h   a ]
[     a   h   h   h   h   a ]
[     h   h   h   h   h   h ]
[     v1  h   h   h   h   h ]
[     v1  v2  h   h   h   h ]
[     v1  v2  v3  h   h   h ]
[                         a ]

where a denotes an element of the original matrix A, h denotes a modified element of the upper Hessenberg matrix H, and vi denotes an element of the vector defining H_i.

ilo and ihi determine the block of A that will be reduced to upper Hessenberg form. It must hold that 0 <= ilo <= ihi < n if n > 0, and ilo == 0 and ihi == -1 if n == 0, otherwise Dgehrd will panic.

On return, tau will contain the scalar factors of the elementary reflectors. Elements tau[:ilo] and tau[ihi:] will be set to zero. tau must have length equal to n-1 if n > 0, otherwise Dgehrd will panic.

work must have length at least lwork and lwork must be at least max(1,n), otherwise Dgehrd will panic. On return, work[0] contains the optimal value of lwork.

If lwork == -1, instead of performing Dgehrd, only the optimal value of lwork will be stored in work[0].

Dgehrd is an internal routine. It is exported for testing purposes.

Dgelq2 computes the LQ factorization of the m×n matrix A.

In an LQ factorization, L is a lower triangular m×n matrix, and Q is an n×n orthonormal matrix.

a is modified to contain the information to construct L and Q. The lower triangle of a contains the matrix L. The upper triangular elements (not including the diagonal) contain the elementary reflectors. tau is modified to contain the reflector scales. tau must have length of at least k = min(m,n) and this function will panic otherwise.

See Dgeqr2 for a description of the elementary reflectors and orthonormal matrix Q. Q is constructed as a product of these elementary reflectors, Q = H_{k-1} * ... * H_1 * H_0.

work is temporary storage of length at least m and this function will panic otherwise.

Dgelq2 is an internal routine. It is exported for testing purposes.

Dgelqf computes the LQ factorization of the m×n matrix A using a blocked algorithm. See the documentation for Dgelq2 for a description of the parameters at entry and exit.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= m, and this function will panic otherwise. Dgelqf is a blocked LQ factorization, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Dgelqf, the optimal work length will be stored into work[0].

tau must have length at least min(m,n), and this function will panic otherwise.

Dgels finds a minimum-norm solution based on the matrices A and B using the QR or LQ factorization. Dgels returns false if the matrix A is singular, and true if this solution was successfully found.

The minimization problem solved depends on the input parameters.

1.   If m >= n and trans == blas.NoTrans, Dgels finds X such that || A*X - B||_2 is minimized.
2.   If m < n and trans == blas.NoTrans, Dgels finds the minimum norm solution of A * X = B.
3.   If m >= n and trans == blas.Trans, Dgels finds the minimum norm solution of Aᵀ * X = B.
4.   If m < n and trans == blas.Trans, Dgels finds X such that || A*X - B||_2 is minimized.

Note that the least-squares solutions (cases 1 and 3) perform the minimization per column of B. This is not the same as finding the minimum-norm matrix.

The matrix A is a general matrix of size m×n and is modified during this call. The input matrix B is of size max(m,n)×nrhs, and serves two purposes. On entry, the elements of b specify the input matrix B. B has size m×nrhs if trans == blas.NoTrans, and n×nrhs if trans == blas.Trans. On exit, the leading submatrix of b contains the solution vectors X. If trans == blas.NoTrans, this submatrix is of size n×nrhs, and of size m×nrhs otherwise.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= max(m,n) + max(m,n,nrhs), and this function will panic otherwise. A longer work will enable blocked algorithms to be called. In the special case that lwork == -1, work[0] will be set to the optimal working length.

Dgeql2 computes the QL factorization of the m×n matrix A. That is, Dgeql2 computes Q and L such that

A = Q * L

where Q is an m×m orthonormal matrix and L is a lower trapezoidal matrix.

Q is represented as a product of elementary reflectors,

Q = H_{k-1} * ... * H_1 * H_0

where k = min(m,n) and each H_i has the form

H_i = I - tau[i] * v_i * v_iᵀ

Vector v_i has v[m-k+i+1:m] = 0, v[m-k+i] = 1, and v[:m-k+i+1] is stored on exit in A[0:m-k+i-1, n-k+i].

tau must have length at least min(m,n), and Dgeql2 will panic otherwise.

work is temporary memory storage and must have length at least n.

Dgeql2 is an internal routine. It is exported for testing purposes.

Dgeqp3 computes a QR factorization with column pivoting of the m×n matrix A:

A*P = Q*R

where P is a permutation matrix, Q is an orthogonal matrix and R is a min(m,n)×n upper trapezoidal matrix.

On return, the upper triangle of A contains the matrix R. The elements below the diagonal together with tau represent the matrix Q as a product of elementary reflectors

Q = H_0 * H_1 * ... * H_{k-1}, where k = min(m,n).

Each H_i has the form

H_i = I - tau * v * vᵀ

where tau is a scalar and v is a vector with v[0:i] = 0 and v[i] = 1; v[i+1:m] is stored on exit in A[i+1:m,i], and tau in tau[i].

jpvt specifies a column pivot to be applied to A. On entry, if jpvt[j] is at least zero, the jth column of A is permuted to the front of A*P (a leading column), if jpvt[j] is -1 the jth column of A is a free column. If jpvt[j] < -1, Dgeqp3 will panic. On return, jpvt holds the permutation that was applied; the jth column of A*P was the jpvt[j] column of A. jpvt must have length n or Dgeqp3 will panic.

tau holds the scalar factors of the elementary reflectors. It must have length min(m,n), otherwise Dgeqp3 will panic.

work must have length at least max(1,lwork), and lwork must be at least 3*n+1, otherwise Dgeqp3 will panic. For optimal performance lwork must be at least 2*n+(n+1)*nb, where nb is the optimal blocksize. On return, work[0] will contain the optimal value of lwork.

If lwork == -1, instead of performing Dgeqp3, only the optimal value of lwork will be stored in work[0].

Dgeqp3 is an internal routine. It is exported for testing purposes.

Dgeqr2 computes a QR factorization of the m×n matrix A.

In a QR factorization, Q is an m×m orthonormal matrix, and R is an upper triangular m×n matrix.

A is modified to contain the information to construct Q and R. The upper triangle of a contains the matrix R. The lower triangular elements (not including the diagonal) contain the elementary reflectors. tau is modified to contain the reflector scales. tau must have length min(m,n), and this function will panic otherwise.

The ith elementary reflector can be explicitly constructed by first extracting the

v[j] = 0           j < i
v[j] = 1           j == i
v[j] = a[j*lda+i]  j > i

and computing H_i = I - tau[i] * v * vᵀ.

The orthonormal matrix Q can be constructed from a product of these elementary reflectors, Q = H_0 * H_1 * ... * H_{k-1}, where k = min(m,n).

work is temporary storage of length at least n and this function will panic otherwise.

Dgeqr2 is an internal routine. It is exported for testing purposes.

Dgeqrf computes the QR factorization of the m×n matrix A using a blocked algorithm. See the documentation for Dgeqr2 for a description of the parameters at entry and exit.

work is temporary storage, and lwork specifies the usable memory length. The length of work must be at least max(1, lwork) and lwork must be -1 or at least n, otherwise this function will panic. Dgeqrf is a blocked QR factorization, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Dgeqrf, the optimal work length will be stored into work[0].

tau must have length min(m,n), and this function will panic otherwise.

Dgerq2 computes an RQ factorization of the m×n matrix A,

A = R * Q.

On exit, if m <= n, the upper triangle of the subarray A[0:m, n-m:n] contains the m×m upper triangular matrix R. If m >= n, the elements on and above the (m-n)-th subdiagonal contain the m×n upper trapezoidal matrix R. The remaining elements, with tau, represent the orthogonal matrix Q as a product of min(m,n) elementary reflectors.

The matrix Q is represented as a product of elementary reflectors

Q = H_0 H_1 . . . H_{min(m,n)-1}.

Each H(i) has the form

H_i = I - tau_i * v * vᵀ

where v is a vector with v[0:n-k+i-1] stored in A[m-k+i, 0:n-k+i-1], v[n-k+i:n] = 0 and v[n-k+i] = 1.

tau must have length min(m,n) and work must have length m, otherwise Dgerq2 will panic.

Dgerq2 is an internal routine. It is exported for testing purposes.

Dgerqf computes an RQ factorization of the m×n matrix A,

A = R * Q.

On exit, if m <= n, the upper triangle of the subarray A[0:m, n-m:n] contains the m×m upper triangular matrix R. If m >= n, the elements on and above the (m-n)-th subdiagonal contain the m×n upper trapezoidal matrix R. The remaining elements, with tau, represent the orthogonal matrix Q as a product of min(m,n) elementary reflectors.

The matrix Q is represented as a product of elementary reflectors

Q = H_0 H_1 . . . H_{min(m,n)-1}.

Each H(i) has the form

H_i = I - tau_i * v * vᵀ

where v is a vector with v[0:n-k+i-1] stored in A[m-k+i, 0:n-k+i-1], v[n-k+i:n] = 0 and v[n-k+i] = 1.

tau must have length min(m,n), work must have length max(1, lwork), and lwork must be -1 or at least max(1, m), otherwise Dgerqf will panic. On exit, work[0] will contain the optimal length for work.

Dgerqf is an internal routine. It is exported for testing purposes.

Dgesc2 solves a system of linear equations

A * x = scale * b

with a general n×n matrix A represented by the LU factorization with complete pivoting

A = P * L * U * Q

as computed by Dgetc2.

On entry, rhs contains the right hand side vector b. On return, it is overwritten with the solution vector x.

Dgesc2 returns a scale factor

0 <= scale <= 1

chosen to prevent overflow in the solution.

Dgesc2 is an internal routine. It is exported for testing purposes.

Dgesv computes the solution to a real system of linear equations

A * X = B

where A is an n×n matrix and X and B are n×nrhs matrices.

The LU decomposition with partial pivoting and row interchanges is used to factor A as

A = P * L * U

where P is a permutation matrix, L is unit lower triangular, and U is upper triangular. On return, the factors L and U are stored in a; the unit diagonal elements of L are not stored. The row pivot indices that define the permutation matrix P are stored in ipiv.

The factored form of A is then used to solve the system of equations A * X = B. On entry, b contains the right hand side matrix B. On return, if ok is true, b contains the solution matrix X.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dgesvd(jobU, jobVT [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[SVDJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#SVDJob), m, n [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), s, u [][float64](https://pkg.go.dev/builtin#float64), ldu [int](https://pkg.go.dev/builtin#int), vt [][float64](https://pkg.go.dev/builtin#float64), ldvt [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int)) (ok [bool](https://pkg.go.dev/builtin#bool))

Dgesvd computes the singular value decomposition of the input matrix A.

The singular value decomposition is

A = U * Sigma * Vᵀ

where Sigma is an m×n diagonal matrix containing the singular values of A, U is an m×m orthogonal matrix and V is an n×n orthogonal matrix. The first min(m,n) columns of U and V are the left and right singular vectors of A respectively.

jobU and jobVT are options for computing the singular vectors. The behavior is as follows

jobU == lapack.SVDAll       All m columns of U are returned in u
jobU == lapack.SVDStore     The first min(m,n) columns are returned in u
jobU == lapack.SVDOverwrite The first min(m,n) columns of U are written into a
jobU == lapack.SVDNone      The columns of U are not computed.

The behavior is the same for jobVT and the rows of Vᵀ. At most one of jobU and jobVT can equal lapack.SVDOverwrite, and Dgesvd will panic otherwise.

On entry, a contains the data for the m×n matrix A. During the call to Dgesvd the data is overwritten. On exit, A contains the appropriate singular vectors if either job is lapack.SVDOverwrite.

s is a slice of length at least min(m,n) and on exit contains the singular values in decreasing order.

u contains the left singular vectors on exit, stored column-wise. If jobU == lapack.SVDAll, u is of size m×m. If jobU == lapack.SVDStore u is of size m×min(m,n). If jobU == lapack.SVDOverwrite or lapack.SVDNone, u is not used.

vt contains the left singular vectors on exit, stored row-wise. If jobV == lapack.SVDAll, vt is of size n×n. If jobVT == lapack.SVDStore vt is of size min(m,n)×n. If jobVT == lapack.SVDOverwrite or lapack.SVDNone, vt is not used.

work is a slice for storing temporary memory, and lwork is the usable size of the slice. lwork must be at least max(5*min(m,n), 3*min(m,n)+max(m,n)). If lwork == -1, instead of performing Dgesvd, the optimal work length will be stored into work[0]. Dgesvd will panic if the working memory has insufficient storage.

Dgesvd returns whether the decomposition successfully completed.

Dgetc2 computes an LU factorization with complete pivoting of the n×n matrix A. The factorization has the form

A = P * L * U * Q,

where P and Q are permutation matrices, L is lower triangular with unit diagonal elements and U is upper triangular.

On entry, a contains the matrix A to be factored. On return, a is overwritten with the factors L and U. The unit diagonal elements of L are not stored.

On return, ipiv and jpiv contain the pivot indices: row i has been interchanged with row ipiv[i] and column j has been interchanged with column jpiv[j]. ipiv and jpiv must have length n, otherwise Dgetc2 will panic.

If k is non-negative, then U[k,k] is likely to produce overflow when solving for x in A*x=b and U has been perturbed to avoid the overflow.

Dgetc2 is an internal routine. It is exported for testing purposes.

Dgetf2 computes the LU decomposition of an m×n matrix A using partial pivoting with row interchanges.

The LU decomposition is a factorization of A into

A = P * L * U

where P is a permutation matrix, L is a lower triangular with unit diagonal elements (lower trapezoidal if m > n), and U is upper triangular (upper trapezoidal if m < n).

On entry, a contains the matrix A. On return, L and U are stored in place into a, and P is represented by ipiv.

ipiv contains a sequence of row interchanges. It indicates that row i of the matrix was interchanged with ipiv[i]. ipiv must have length min(m,n), and Dgetf2 will panic otherwise. ipiv is zero-indexed.

Dgetf2 returns whether the matrix A is nonsingular. The LU decomposition will be computed regardless of the singularity of A, but the result should not be used to solve a system of equation.

Dgetf2 is an internal routine. It is exported for testing purposes.

Dgetrf computes the LU decomposition of an m×n matrix A using partial pivoting with row interchanges.

The LU decomposition is a factorization of A into

A = P * L * U

where P is a permutation matrix, L is a lower triangular with unit diagonal elements (lower trapezoidal if m > n), and U is upper triangular (upper trapezoidal if m < n).

On entry, a contains the matrix A. On return, L and U are stored in place into a, and P is represented by ipiv.

ipiv contains a sequence of row interchanges. It indicates that row i of the matrix was interchanged with ipiv[i]. ipiv must have length min(m,n), and Dgetrf will panic otherwise. ipiv is zero-indexed.

Dgetrf returns whether the matrix A is nonsingular. The LU decomposition will be computed regardless of the singularity of A, but the result should not be used to solve a system of equation.

Dgetri computes the inverse of the matrix A using the LU factorization computed by Dgetrf. On entry, a contains the PLU decomposition of A as computed by Dgetrf and on exit contains the reciprocal of the original matrix.

Dgetri will not perform the inversion if the matrix is singular, and returns a boolean indicating whether the inversion was successful.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= n and this function will panic otherwise. Dgetri is a blocked inversion, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Dgetri, the optimal work length will be stored into work[0].

Dgetrs solves a system of equations using an LU factorization. The system of equations solved is

A * X = B  if trans == blas.Trans
Aᵀ * X = B if trans == blas.NoTrans

A is a general n×n matrix with stride lda. B is a general matrix of size n×nrhs.

On entry b contains the elements of the matrix B. On exit, b contains the elements of X, the solution to the system of equations.

a and ipiv contain the LU factorization of A and the permutation indices as computed by Dgetrf. ipiv is zero-indexed.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dgghrd(compq, compz [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[OrthoComp](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#OrthoComp), n, ilo, ihi [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), q [][float64](https://pkg.go.dev/builtin#float64), ldq [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), ldz [int](https://pkg.go.dev/builtin#int))

Dgghrd reduces a pair of real matrices (A,B) to generalized upper Hessenberg form using orthogonal transformations, where A is a general matrix and B is upper triangular.

This subroutine simultaneously reduces A to a Hessenberg matrix H

Qᵀ*A*Z = H,

and transforms B to another upper triangular matrix T

Qᵀ*B*Z = T.

The orthogonal matrices Q and Z are determined as products of Givens rotations. They may either be formed explicitly (lapack.OrthoExplicit), or they may be postmultiplied into input matrices Q1 and Z1 (lapack.OrthoPostmul), so that

Q1 * A * Z1ᵀ = (Q1*Q) * H * (Z1*Z)ᵀ,
Q1 * B * Z1ᵀ = (Q1*Q) * T * (Z1*Z)ᵀ.

ilo and ihi determine the block of A that will be reduced. It must hold that

*   0 <= ilo <= ihi < n if n > 0,
*   ilo == 0 and ihi == -1 if n == 0,

otherwise Dgghrd will panic.

Dgghrd is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dggsvd3(jobU, jobV, jobQ [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[GSVDJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#GSVDJob), m, n, p [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), alpha, beta, u [][float64](https://pkg.go.dev/builtin#float64), ldu [int](https://pkg.go.dev/builtin#int), v [][float64](https://pkg.go.dev/builtin#float64), ldv [int](https://pkg.go.dev/builtin#int), q [][float64](https://pkg.go.dev/builtin#float64), ldq [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int), iwork [][int](https://pkg.go.dev/builtin#int)) (k, l [int](https://pkg.go.dev/builtin#int), ok [bool](https://pkg.go.dev/builtin#bool))

Dggsvd3 computes the generalized singular value decomposition (GSVD) of an m×n matrix A and p×n matrix B:

Uᵀ*A*Q = D1*[ 0 R ]

Vᵀ*B*Q = D2*[ 0 R ]

where U, V and Q are orthogonal matrices.

Dggsvd3 returns k and l, the dimensions of the sub-blocks. k+l is the effective numerical rank of the (m+p)×n matrix [ Aᵀ Bᵀ ]ᵀ. R is a (k+l)×(k+l) nonsingular upper triangular matrix, D1 and D2 are m×(k+l) and p×(k+l) diagonal matrices and of the following structures, respectively:

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

Dggsvd3 computes C, S, R, and optionally the orthogonal transformation matrices U, V and Q.

jobU, jobV and jobQ are options for computing the orthogonal matrices. The behavior is as follows

jobU == lapack.GSVDU        Compute orthogonal matrix U
jobU == lapack.GSVDNone     Do not compute orthogonal matrix.

The behavior is the same for jobV and jobQ with the exception that instead of lapack.GSVDU these accept lapack.GSVDV and lapack.GSVDQ respectively. The matrices U, V and Q must be m×m, p×p and n×n respectively unless the relevant job parameter is lapack.GSVDNone.

alpha and beta must have length n or Dggsvd3 will panic. On exit, alpha and beta contain the generalized singular value pairs of A and B

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

iwork must have length n, work must have length at least max(1, lwork), and lwork must be -1 or greater than n, otherwise Dggsvd3 will panic. If lwork is -1, work[0] holds the optimal lwork on return, but Dggsvd3 does not perform the GSVD.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dggsvp3(jobU, jobV, jobQ [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[GSVDJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#GSVDJob), m, p, n [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), tola, tolb [float64](https://pkg.go.dev/builtin#float64), u [][float64](https://pkg.go.dev/builtin#float64), ldu [int](https://pkg.go.dev/builtin#int), v [][float64](https://pkg.go.dev/builtin#float64), ldv [int](https://pkg.go.dev/builtin#int), q [][float64](https://pkg.go.dev/builtin#float64), ldq [int](https://pkg.go.dev/builtin#int), iwork [][int](https://pkg.go.dev/builtin#int), tau, work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int)) (k, l [int](https://pkg.go.dev/builtin#int))

Dggsvp3 computes orthogonal matrices U, V and Q such that

                n-k-l  k    l
Uᵀ*A*Q =     k [ 0    A12  A13 ] if m-k-l >= 0;
             l [ 0     0   A23 ]
         m-k-l [ 0     0    0  ]

                n-k-l  k    l
Uᵀ*A*Q =     k [ 0    A12  A13 ] if m-k-l < 0;
           m-k [ 0     0   A23 ]

                n-k-l  k    l
Vᵀ*B*Q =     l [ 0     0   B13 ]
           p-l [ 0     0    0  ]

where the k×k matrix A12 and l×l matrix B13 are non-singular upper triangular. A23 is l×l upper triangular if m-k-l >= 0, otherwise A23 is (m-k)×l upper trapezoidal.

Dggsvp3 returns k and l, the dimensions of the sub-blocks. k+l is the effective numerical rank of the (m+p)×n matrix [ Aᵀ Bᵀ ]ᵀ.

jobU, jobV and jobQ are options for computing the orthogonal matrices. The behavior is as follows

jobU == lapack.GSVDU        Compute orthogonal matrix U
jobU == lapack.GSVDNone     Do not compute orthogonal matrix.

The behavior is the same for jobV and jobQ with the exception that instead of lapack.GSVDU these accept lapack.GSVDV and lapack.GSVDQ respectively. The matrices U, V and Q must be m×m, p×p and n×n respectively unless the relevant job parameter is lapack.GSVDNone.

tola and tolb are the convergence criteria for the Jacobi-Kogbetliantz iteration procedure. Generally, they are the same as used in the preprocessing step, for example,

tola = max(m, n)*norm(A)*eps,
tolb = max(p, n)*norm(B)*eps.

Where eps is the machine epsilon.

iwork must have length n, work must have length at least max(1, lwork), and lwork must be -1 or greater than zero, otherwise Dggsvp3 will panic.

Dggsvp3 is an internal routine. It is exported for testing purposes.

Dgtsv solves the equation

A * X = B

where A is an n×n tridiagonal matrix. It uses Gaussian elimination with partial pivoting. The equation Aᵀ * X = B may be solved by swapping the arguments for du and dl.

On entry, dl, d and du contain the sub-diagonal, the diagonal and the super-diagonal, respectively, of A. On return, the first n-2 elements of dl, the first n-1 elements of du and the first n elements of d may be overwritten.

On entry, b contains the n×nrhs right-hand side matrix B. On return, b will be overwritten. If ok is true, it will be overwritten by the solution matrix X.

Dgtsv returns whether the solution X has been successfully computed.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dhseqr(job [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[SchurJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#SchurJob), compz [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[SchurComp](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#SchurComp), n, ilo, ihi [int](https://pkg.go.dev/builtin#int), h [][float64](https://pkg.go.dev/builtin#float64), ldh [int](https://pkg.go.dev/builtin#int), wr, wi [][float64](https://pkg.go.dev/builtin#float64), z [][float64](https://pkg.go.dev/builtin#float64), ldz [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int)) (unconverged [int](https://pkg.go.dev/builtin#int))

Dhseqr computes the eigenvalues of an n×n Hessenberg matrix H and, optionally, the matrices T and Z from the Schur decomposition

H = Z T Zᵀ,

where T is an n×n upper quasi-triangular matrix (the Schur form), and Z is the n×n orthogonal matrix of Schur vectors.

Optionally Z may be postmultiplied into an input orthogonal matrix Q so that this routine can give the Schur factorization of a matrix A which has been reduced to the Hessenberg form H by the orthogonal matrix Q:

A = Q H Qᵀ = (QZ) T (QZ)ᵀ.

If job == lapack.EigenvaluesOnly, only the eigenvalues will be computed. If job == lapack.EigenvaluesAndSchur, the eigenvalues and the Schur form T will be computed. For other values of job Dhseqr will panic.

If compz == lapack.SchurNone, no Schur vectors will be computed and Z will not be referenced. If compz == lapack.SchurHess, on return Z will contain the matrix of Schur vectors of H. If compz == lapack.SchurOrig, on entry z is assumed to contain the orthogonal matrix Q that is the identity except for the submatrix Q[ilo:ihi+1,ilo:ihi+1]. On return z will be updated to the product Q*Z.

ilo and ihi determine the block of H on which Dhseqr operates. It is assumed that H is already upper triangular in rows and columns [0:ilo] and [ihi+1:n], although it will be only checked that the block is isolated, that is,

ilo == 0   or H[ilo,ilo-1] == 0,
ihi == n-1 or H[ihi+1,ihi] == 0,

and Dhseqr will panic otherwise. ilo and ihi are typically set by a previous call to Dgebal, otherwise they should be set to 0 and n-1, respectively. It must hold that

0 <= ilo <= ihi < n     if n > 0,
ilo == 0 and ihi == -1  if n == 0.

wr and wi must have length n.

work must have length at least lwork and lwork must be at least max(1,n) otherwise Dhseqr will panic. The minimum lwork delivers very good and sometimes optimal performance, although lwork as large as 11*n may be required. On return, work[0] will contain the optimal value of lwork.

If lwork is -1, instead of performing Dhseqr, the function only estimates the optimal workspace size and stores it into work[0]. Neither h nor z are accessed.

unconverged indicates whether Dhseqr computed all the eigenvalues.

If unconverged == 0, all the eigenvalues have been computed and their real and imaginary parts will be stored on return in wr and wi, respectively. If two eigenvalues are computed as a complex conjugate pair, they are stored in consecutive elements of wr and wi, say the i-th and (i+1)th, with wi[i] > 0 and wi[i+1] < 0.

If unconverged == 0 and job == lapack.EigenvaluesAndSchur, on return H will contain the upper quasi-triangular matrix T from the Schur decomposition (the Schur form). 2×2 diagonal blocks (corresponding to complex conjugate pairs of eigenvalues) will be returned in standard form, with

H[i,i] == H[i+1,i+1],

and

H[i+1,i]*H[i,i+1] < 0.

The eigenvalues will be stored in wr and wi in the same order as on the diagonal of the Schur form returned in H, with

wr[i] = H[i,i],

and, if H[i:i+2,i:i+2] is a 2×2 diagonal block,

wi[i]   = sqrt(-H[i+1,i]*H[i,i+1]),
wi[i+1] = -wi[i].

If unconverged == 0 and job == lapack.EigenvaluesOnly, the contents of h on return is unspecified.

If unconverged > 0, some eigenvalues have not converged, and the blocks [0:ilo] and [unconverged:n] of wr and wi will contain those eigenvalues which have been successfully computed. Failures are rare.

If unconverged > 0 and job == lapack.EigenvaluesOnly, on return the remaining unconverged eigenvalues are the eigenvalues of the upper Hessenberg matrix H[ilo:unconverged,ilo:unconverged].

If unconverged > 0 and job == lapack.EigenvaluesAndSchur, then on return

(initial H) U = U (final H),   (*)

where U is an orthogonal matrix. The final H is upper Hessenberg and H[unconverged:ihi+1,unconverged:ihi+1] is upper quasi-triangular.

If unconverged > 0 and compz == lapack.SchurOrig, then on return

(final Z) = (initial Z) U,

where U is the orthogonal matrix in (*) regardless of the value of job.

If unconverged > 0 and compz == lapack.SchurHess, then on return

(final Z) = U,

where U is the orthogonal matrix in (*) regardless of the value of job.

References:

[1] R. Byers. LAPACK 3.1 xHSEQR: Tuning and Implementation Notes on the
    Small Bulge Multi-Shift QR Algorithm with Aggressive Early Deflation.
    LAPACK Working Note 187 (2007)
    URL: http://www.netlib.org/lapack/lawnspdf/lawn187.pdf
[2] K. Braman, R. Byers, R. Mathias. The Multishift QR Algorithm. Part I:
    Maintaining Well-Focused Shifts and Level 3 Performance. SIAM J. Matrix
    Anal. Appl. 23(4) (2002), pp. 929—947
    URL: http://dx.doi.org/10.1137/S0895479801384573
[3] K. Braman, R. Byers, R. Mathias. The Multishift QR Algorithm. Part II:
    Aggressive Early Deflation. SIAM J. Matrix Anal. Appl. 23(4) (2002), pp. 948—973
    URL: http://dx.doi.org/10.1137/S0895479801384585

Dhseqr is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlabrd(m, n, nb [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), d, e, tauQ, tauP, x [][float64](https://pkg.go.dev/builtin#float64), ldx [int](https://pkg.go.dev/builtin#int), y [][float64](https://pkg.go.dev/builtin#float64), ldy [int](https://pkg.go.dev/builtin#int))

Dlabrd reduces the first NB rows and columns of a real general m×n matrix A to upper or lower bidiagonal form by an orthogonal transformation

Q**T * A * P

If m >= n, A is reduced to upper bidiagonal form and upon exit the elements on and below the diagonal in the first nb columns represent the elementary reflectors, and the elements above the diagonal in the first nb rows represent the matrix P. If m < n, A is reduced to lower bidiagonal form and the elements P is instead stored above the diagonal.

The reduction to bidiagonal form is stored in d and e, where d are the diagonal elements, and e are the off-diagonal elements.

The matrices Q and P are products of elementary reflectors

Q = H_0 * H_1 * ... * H_{nb-1}
P = G_0 * G_1 * ... * G_{nb-1}

where

H_i = I - tauQ[i] * v_i * v_iᵀ
G_i = I - tauP[i] * u_i * u_iᵀ

As an example, on exit the entries of A when m = 6, n = 5, and nb = 2

[ 1   1  u1  u1  u1]
[v1   1   1  u2  u2]
[v1  v2   a   a   a]
[v1  v2   a   a   a]
[v1  v2   a   a   a]
[v1  v2   a   a   a]

and when m = 5, n = 6, and nb = 2

[ 1  u1  u1  u1  u1  u1]
[ 1   1  u2  u2  u2  u2]
[v1   1   a   a   a   a]
[v1  v2   a   a   a   a]
[v1  v2   a   a   a   a]

Dlabrd also returns the matrices X and Y which are used with U and V to apply the transformation to the unreduced part of the matrix

A := A - V*Yᵀ - X*Uᵀ

and returns the matrices X and Y which are needed to apply the transformation to the unreduced part of A.

X is an m×nb matrix, Y is an n×nb matrix. d, e, taup, and tauq must all have length at least nb. Dlabrd will panic if these size constraints are violated.

Dlabrd is an internal routine. It is exported for testing purposes.

Dlacn2 estimates the 1-norm of an n×n matrix A using sequential updates with matrix-vector products provided externally.

Dlacn2 is called sequentially and it returns the value of est and kase to be used on the next call. On the initial call, kase must be 0. In between calls, x must be overwritten by

A * X    if kase was returned as 1,
Aᵀ * X   if kase was returned as 2,

and all other parameters must not be changed. On the final return, kase is returned as 0, v contains A*W where W is a vector, and est = norm(V)/norm(W) is a lower bound for 1-norm of A.

v, x, and isgn must all have length n and n must be at least 1, otherwise Dlacn2 will panic. isave is used for temporary storage.

Dlacn2 is an internal routine. It is exported for testing purposes.

Dlacpy copies the elements of A specified by uplo into B. Uplo can specify a triangular portion with blas.Upper or blas.Lower, or can specify all of the elements with blas.All.

Dlacpy is an internal routine. It is exported for testing purposes.

Dlae2 computes the eigenvalues of a 2×2 symmetric matrix

[a b]
[b c]

and returns the eigenvalue with the larger absolute value as rt1 and the smaller as rt2.

Dlae2 is an internal routine. It is exported for testing purposes.

Dlaev2 computes the Eigen decomposition of a symmetric 2×2 matrix. The matrix is given by

[a b]
[b c]

Dlaev2 returns rt1 and rt2, the eigenvalues of the matrix where |RT1| > |RT2|, and [cs1, sn1] which is the unit right eigenvalue for RT1.

[ cs1 sn1] [a b] [cs1 -sn1] = [rt1   0]
[-sn1 cs1] [b c] [sn1  cs1]   [  0 rt2]

Dlaev2 is an internal routine. It is exported for testing purposes.

Dlaexc swaps two adjacent diagonal blocks of order 1 or 2 in an n×n upper quasi-triangular matrix T by an orthogonal similarity transformation.

T must be in Schur canonical form, that is, block upper triangular with 1×1 and 2×2 diagonal blocks; each 2×2 diagonal block has its diagonal elements equal and its off-diagonal elements of opposite sign. On return, T will contain the updated matrix again in Schur canonical form.

If wantq is true, the transformation is accumulated in the n×n matrix Q, otherwise Q is not referenced.

j1 is the index of the first row of the first block. n1 and n2 are the order of the first and second block, respectively.

work must have length at least n, otherwise Dlaexc will panic.

If ok is false, the transformed matrix T would be too far from Schur form. The blocks are not swapped, and T and Q are not modified.

If n1 and n2 are both equal to 1, Dlaexc will always return true.

Dlaexc is an internal routine. It is exported for testing purposes.

Dlag2 computes the eigenvalues of a 2×2 generalized eigenvalue problem

A - w*B

where B is an upper triangular matrix.

Dlag2 uses scaling as necessary to avoid over-/underflow. Scaling results in a modified eigenvalue problem

s*A - w*B

where s is a non-negative scaling factor chosen so that w, w*B, and s*A do not overflow and, if possible, do not underflow, either.

scale1 and scale2 are used to avoid over-/underflow in the eigenvalue equation which defines the first and second eigenvalue respectively. Note that scale1 and scale2 may be zero or less than the underflow threshold if the corresponding exact eigenvalue is sufficiently large.

If the eigenvalues are real, then:

*   wi is zero,
*   the eigenvalues are wr1/scale1 and wr2/scale2.

If the eigenvalues are complex, then:

*   wi is non-negative,
*   the eigenvalues are (wr1 ± wi*i)/scale1,
*   wr1 = wr2,
*   scale1 = scale2.

Dlag2 assumes that the one-norm of A and B is less than 1/dlamchS. Entries of A less than sqrt(dlamchS)*norm(A) are subject to being treated as zero. The diagonals of B should be at least sqrt(dlamchS) times the largest element of B (in absolute value); if a diagonal is smaller than that, then ±sqrt(dlamchS) will be used instead of that diagonal.

Dlag2 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlags2(upper [bool](https://pkg.go.dev/builtin#bool), a1, a2, a3, b1, b2, b3 [float64](https://pkg.go.dev/builtin#float64)) (csu, snu, csv, snv, csq, snq [float64](https://pkg.go.dev/builtin#float64))

Dlags2 computes 2-by-2 orthogonal matrices U, V and Q with the triangles of A and B specified by upper.

If upper is true

Uᵀ*A*Q = Uᵀ*[ a1 a2 ]*Q = [ x  0 ]
            [ 0  a3 ]     [ x  x ]

and

Vᵀ*B*Q = Vᵀ*[ b1 b2 ]*Q = [ x  0 ]
            [ 0  b3 ]     [ x  x ]

otherwise

Uᵀ*A*Q = Uᵀ*[ a1 0  ]*Q = [ x  x ]
            [ a2 a3 ]     [ 0  x ]

and

Vᵀ*B*Q = Vᵀ*[ b1 0  ]*Q = [ x  x ]
            [ b2 b3 ]     [ 0  x ].

The rows of the transformed A and B are parallel, where

U = [  csu  snu ], V = [  csv snv ], Q = [  csq   snq ]
    [ -snu  csu ]      [ -snv csv ]      [ -snq   csq ]

Dlags2 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlagtm(trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), dl, d, du [][float64](https://pkg.go.dev/builtin#float64), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int))

Dlagtm performs one of the matrix-matrix operations

C = alpha * A * B + beta * C   if trans == blas.NoTrans
C = alpha * Aᵀ * B + beta * C  if trans == blas.Trans or blas.ConjTrans

where A is an m×m tridiagonal matrix represented by its diagonals dl, d, du, B and C are m×n dense matrices, and alpha and beta are scalars.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlahqr(wantt, wantz [bool](https://pkg.go.dev/builtin#bool), n, ilo, ihi [int](https://pkg.go.dev/builtin#int), h [][float64](https://pkg.go.dev/builtin#float64), ldh [int](https://pkg.go.dev/builtin#int), wr, wi [][float64](https://pkg.go.dev/builtin#float64), iloz, ihiz [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), ldz [int](https://pkg.go.dev/builtin#int)) (unconverged [int](https://pkg.go.dev/builtin#int))

Dlahqr computes the eigenvalues and Schur factorization of a block of an n×n upper Hessenberg matrix H, using the double-shift/single-shift QR algorithm.

h and ldh represent the matrix H. Dlahqr works primarily with the Hessenberg submatrix H[ilo:ihi+1,ilo:ihi+1], but applies transformations to all of H if wantt is true. It is assumed that H[ihi+1:n,ihi+1:n] is already upper quasi-triangular, although this is not checked.

It must hold that

0 <= ilo <= max(0,ihi), and ihi < n,

and that

H[ilo,ilo-1] == 0,  if ilo > 0,

otherwise Dlahqr will panic.

If unconverged is zero on return, wr[ilo:ihi+1] and wi[ilo:ihi+1] will contain respectively the real and imaginary parts of the computed eigenvalues ilo to ihi. If two eigenvalues are computed as a complex conjugate pair, they are stored in consecutive elements of wr and wi, say the i-th and (i+1)th, with wi[i] > 0 and wi[i+1] < 0. If wantt is true, the eigenvalues are stored in the same order as on the diagonal of the Schur form returned in H, with wr[i] = H[i,i], and, if H[i:i+2,i:i+2] is a 2×2 diagonal block, wi[i] = sqrt(abs(H[i+1,i]*H[i,i+1])) and wi[i+1] = -wi[i].

wr and wi must have length ihi+1.

z and ldz represent an n×n matrix Z. If wantz is true, the transformations will be applied to the submatrix Z[iloz:ihiz+1,ilo:ihi+1] and it must hold that

0 <= iloz <= ilo, and ihi <= ihiz < n.

If wantz is false, z is not referenced.

unconverged indicates whether Dlahqr computed all the eigenvalues ilo to ihi in a total of 30 iterations per eigenvalue.

If unconverged is zero, all the eigenvalues ilo to ihi have been computed and will be stored on return in wr[ilo:ihi+1] and wi[ilo:ihi+1].

If unconverged is zero and wantt is true, H[ilo:ihi+1,ilo:ihi+1] will be overwritten on return by upper quasi-triangular full Schur form with any 2×2 diagonal blocks in standard form.

If unconverged is zero and if wantt is false, the contents of h on return is unspecified.

If unconverged is positive, some eigenvalues have not converged, and wr[unconverged:ihi+1] and wi[unconverged:ihi+1] contain those eigenvalues which have been successfully computed.

If unconverged is positive and wantt is true, then on return

(initial H)*U = U*(final H),   (*)

where U is an orthogonal matrix. The final H is upper Hessenberg and H[unconverged:ihi+1,unconverged:ihi+1] is upper quasi-triangular.

If unconverged is positive and wantt is false, on return the remaining unconverged eigenvalues are the eigenvalues of the upper Hessenberg matrix H[ilo:unconverged,ilo:unconverged].

If unconverged is positive and wantz is true, then on return

(final Z) = (initial Z)*U,

where U is the orthogonal matrix in (*) regardless of the value of wantt.

Dlahqr is an internal routine. It is exported for testing purposes.

Dlahr2 reduces the first nb columns of a real general n×(n-k+1) matrix A so that elements below the k-th subdiagonal are zero. The reduction is performed by an orthogonal similarity transformation Qᵀ * A * Q. Dlahr2 returns the matrices V and T which determine Q as a block reflector I - V*T*Vᵀ, and also the matrix Y = A * V * T.

The matrix Q is represented as a product of nb elementary reflectors

Q = H_0 * H_1 * ... * H_{nb-1}.

Each H_i has the form

H_i = I - tau[i] * v * vᵀ,

where v is a real vector with v[0:i+k-1] = 0 and v[i+k-1] = 1. v[i+k:n] is stored on exit in A[i+k+1:n,i].

The elements of the vectors v together form the (n-k+1)×nb matrix V which is needed, with T and Y, to apply the transformation to the unreduced part of the matrix, using an update of the form

A = (I - V*T*Vᵀ) * (A - Y*Vᵀ).

On entry, a contains the n×(n-k+1) general matrix A. On return, the elements on and above the k-th subdiagonal in the first nb columns are overwritten with the corresponding elements of the reduced matrix; the elements below the k-th subdiagonal, with the slice tau, represent the matrix Q as a product of elementary reflectors. The other columns of A are unchanged.

The contents of A on exit are illustrated by the following example with n = 7, k = 3 and nb = 2:

[ a   a   a   a   a ]
[ a   a   a   a   a ]
[ a   a   a   a   a ]
[ h   h   a   a   a ]
[ v0  h   a   a   a ]
[ v0  v1  a   a   a ]
[ v0  v1  a   a   a ]

where a denotes an element of the original matrix A, h denotes a modified element of the upper Hessenberg matrix H, and vi denotes an element of the vector defining H_i.

k is the offset for the reduction. Elements below the k-th subdiagonal in the first nb columns are reduced to zero.

nb is the number of columns to be reduced.

On entry, a represents the n×(n-k+1) matrix A. On return, the elements on and above the k-th subdiagonal in the first nb columns are overwritten with the corresponding elements of the reduced matrix. The elements below the k-th subdiagonal, with the slice tau, represent the matrix Q as a product of elementary reflectors. The other columns of A are unchanged.

tau will contain the scalar factors of the elementary reflectors. It must have length at least nb.

t and ldt represent the nb×nb upper triangular matrix T, and y and ldy represent the n×nb matrix Y.

Dlahr2 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlaln2(trans [bool](https://pkg.go.dev/builtin#bool), na, nw [int](https://pkg.go.dev/builtin#int), smin, ca [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), d1, d2 [float64](https://pkg.go.dev/builtin#float64), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), wr, wi [float64](https://pkg.go.dev/builtin#float64), x [][float64](https://pkg.go.dev/builtin#float64), ldx [int](https://pkg.go.dev/builtin#int)) (scale, xnorm [float64](https://pkg.go.dev/builtin#float64), ok [bool](https://pkg.go.dev/builtin#bool))

Dlaln2 solves a linear equation or a system of 2 linear equations of the form

(ca A   - w D) X = scale B  if trans == false,
(ca Aᵀ - w D) X = scale B   if trans == true,

where A is a na×na real matrix, ca is a real scalar, D is a na×na diagonal real matrix, w is a scalar, real if nw == 1, complex if nw == 2, and X and B are na×1 matrices, real if w is real, complex if w is complex.

If w is complex, X and B are represented as na×2 matrices, the first column of each being the real part and the second being the imaginary part.

na and nw must be 1 or 2, otherwise Dlaln2 will panic.

d1 and d2 are the diagonal elements of D. d2 is not used if na == 1.

wr and wi represent the real and imaginary part, respectively, of the scalar w. wi is not used if nw == 1.

smin is the desired lower bound on the singular values of A. This should be a safe distance away from underflow or overflow, say, between (underflow/machine precision) and (overflow*machine precision).

If both singular values of (ca A - w D) are less than smin, smin*identity will be used instead of (ca A - w D). If only one singular value is less than smin, one element of (ca A - w D) will be perturbed enough to make the smallest singular value roughly smin. If both singular values are at least smin, (ca A - w D) will not be perturbed. In any case, the perturbation will be at most some small multiple of max(smin, ulp*norm(ca A - w D)). The singular values are computed by infinity-norm approximations, and thus will only be correct to a factor of 2 or so.

All input quantities are assumed to be smaller than overflow by a reasonable factor.

scale is a scaling factor less than or equal to 1 which is chosen so that X can be computed without overflow. X is further scaled if necessary to assure that norm(ca A - w D)*norm(X) is less than overflow.

xnorm contains the infinity-norm of X when X is regarded as a na×nw real matrix.

ok will be false if (ca A - w D) had to be perturbed to make its smallest singular value greater than smin, otherwise ok will be true.

Dlaln2 is an internal routine. It is exported for testing purposes.

Dlangb returns the given norm of an m×n band matrix with kl sub-diagonals and ku super-diagonals.

Dlange returns the value of the specified norm of a general m×n matrix A:

lapack.MaxAbs:       the maximum absolute value of any element.
lapack.MaxColumnSum: the maximum column sum of the absolute values of the elements (1-norm).
lapack.MaxRowSum:    the maximum row sum of the absolute values of the elements (infinity-norm).
lapack.Frobenius:    the square root of the sum of the squares of the elements (Frobenius norm).

If norm == lapack.MaxColumnSum, work must be of length n, and this function will panic otherwise. There are no restrictions on work for the other matrix norms.

Dlangt returns the value of the given norm of an n×n tridiagonal matrix represented by the three diagonals.

d must have length at least n and dl and du must have length at least n-1.

Dlanhs returns the value of the one norm, or the Frobenius norm, or the infinity norm, or the element of largest absolute value of a Hessenberg matrix A.

If norm is lapack.MaxColumnSum, work must have length at least n.

Dlansb returns the given norm of an n×n symmetric band matrix with kd super-diagonals.

When norm is lapack.MaxColumnSum or lapack.MaxRowSum, the length of work must be at least n.

Dlanst computes the specified norm of a symmetric tridiagonal matrix A. The diagonal elements of A are stored in d and the off-diagonal elements are stored in e.

Dlansy returns the value of the specified norm of an n×n symmetric matrix. If norm == lapack.MaxColumnSum or norm == lapack.MaxRowSum, work must have length at least n, otherwise work is unused.

Dlantb returns the value of the given norm of an n×n triangular band matrix A with k+1 diagonals.

When norm is lapack.MaxColumnSum, the length of work must be at least n.

Dlantr computes the specified norm of an m×n trapezoidal matrix A. If norm == lapack.MaxColumnSum work must have length at least n, otherwise work is unused.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlanv2(a, b, c, d [float64](https://pkg.go.dev/builtin#float64)) (aa, bb, cc, dd [float64](https://pkg.go.dev/builtin#float64), rt1r, rt1i, rt2r, rt2i [float64](https://pkg.go.dev/builtin#float64), cs, sn [float64](https://pkg.go.dev/builtin#float64))

Dlanv2 computes the Schur factorization of a real 2×2 matrix:

[ a b ] = [ cs -sn ] * [ aa bb ] * [ cs sn ]
[ c d ]   [ sn  cs ]   [ cc dd ] * [-sn cs ]

If cc is zero, aa and dd are real eigenvalues of the matrix. Otherwise it holds that aa = dd and bb*cc < 0, and aa ± sqrt(bb*cc) are complex conjugate eigenvalues. The real and imaginary parts of the eigenvalues are returned in (rt1r,rt1i) and (rt2r,rt2i).

Dlapll returns the smallest singular value of the n×2 matrix A = [ x y ]. The function first computes the QR factorization of A = Q*R, and then computes the SVD of the 2-by-2 upper triangular matrix r.

The contents of x and y are overwritten during the call.

Dlapll is an internal routine. It is exported for testing purposes.

Dlapmr rearranges the rows of the m×n matrix X as specified by the permutation k[0],k[1],...,k[m-1] of the integers 0,...,m-1.

If forward is true, a forward permutation is applied:

X[k[i],0:n] is moved to X[i,0:n] for i=0,1,...,m-1.

If forward is false, a backward permutation is applied:

X[i,0:n] is moved to X[k[i],0:n] for i=0,1,...,m-1.

k must have length m, otherwise Dlapmr will panic.

Dlapmt rearranges the columns of the m×n matrix X as specified by the permutation k_0, k_1, ..., k_n-1 of the integers 0, ..., n-1.

If forward is true a forward permutation is performed:

X[0:m, k[j]] is moved to X[0:m, j] for j = 0, 1, ..., n-1.

otherwise a backward permutation is performed:

X[0:m, j] is moved to X[0:m, k[j]] for j = 0, 1, ..., n-1.

k must have length n, otherwise Dlapmt will panic. k is zero-indexed.

Dlapy2 is the LAPACK version of math.Hypot.

Dlapy2 is an internal routine. It is exported for testing purposes.

Dlaqp2 computes a QR factorization with column pivoting of the block A[offset:m, 0:n] of the m×n matrix A. The block A[0:offset, 0:n] is accordingly pivoted, but not factorized.

On exit, the upper triangle of block A[offset:m, 0:n] is the triangular factor obtained. The elements in block A[offset:m, 0:n] below the diagonal, together with tau, represent the orthogonal matrix Q as a product of elementary reflectors.

offset is number of rows of the matrix A that must be pivoted but not factorized. offset must not be negative otherwise Dlaqp2 will panic.

On exit, jpvt holds the permutation that was applied; the jth column of A*P was the jpvt[j] column of A. jpvt must have length n, otherwise Dlaqp2 will panic.

On exit tau holds the scalar factors of the elementary reflectors. It must have length at least min(m-offset, n) otherwise Dlaqp2 will panic.

vn1 and vn2 hold the partial and complete column norms respectively. They must have length n, otherwise Dlaqp2 will panic.

work must have length n, otherwise Dlaqp2 will panic.

Dlaqp2 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlaqps(m, n, offset, nb [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), jpvt [][int](https://pkg.go.dev/builtin#int), tau, vn1, vn2, auxv, f [][float64](https://pkg.go.dev/builtin#float64), ldf [int](https://pkg.go.dev/builtin#int)) (kb [int](https://pkg.go.dev/builtin#int))

Dlaqps computes a step of QR factorization with column pivoting of an m×n matrix A by using Blas-3. It tries to factorize nb columns from A starting from the row offset, and updates all of the matrix with Dgemm.

In some cases, due to catastrophic cancellations, it cannot factorize nb columns. Hence, the actual number of factorized columns is returned in kb.

Dlaqps computes a QR factorization with column pivoting of the block A[offset:m, 0:nb] of the m×n matrix A. The block A[0:offset, 0:n] is accordingly pivoted, but not factorized.

On exit, the upper triangle of block A[offset:m, 0:kb] is the triangular factor obtained. The elements in block A[offset:m, 0:n] below the diagonal, together with tau, represent the orthogonal matrix Q as a product of elementary reflectors.

offset is number of rows of the matrix A that must be pivoted but not factorized. offset must not be negative otherwise Dlaqps will panic.

On exit, jpvt holds the permutation that was applied; the jth column of A*P was the jpvt[j] column of A. jpvt must have length n, otherwise Dlapqs will panic.

On exit tau holds the scalar factors of the elementary reflectors. It must have length nb, otherwise Dlapqs will panic.

vn1 and vn2 hold the partial and complete column norms respectively. They must have length n, otherwise Dlapqs will panic.

auxv must have length nb, otherwise Dlaqps will panic.

f and ldf represent an n×nb matrix F that is overwritten during the call.

Dlaqps is an internal routine. It is exported for testing purposes.

Dlaqr1 sets v to a scalar multiple of the first column of the product

(H - (sr1 + i*si1)*I)*(H - (sr2 + i*si2)*I)

where H is a 2×2 or 3×3 matrix, I is the identity matrix of the same size, and i is the imaginary unit. Scaling is done to avoid overflows and most underflows.

n is the order of H and must be either 2 or 3. It must hold that either sr1 = sr2 and si1 = -si2, or si1 = si2 = 0. The length of v must be equal to n. If any of these conditions is not met, Dlaqr1 will panic.

Dlaqr1 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlaqr04(wantt, wantz [bool](https://pkg.go.dev/builtin#bool), n, ilo, ihi [int](https://pkg.go.dev/builtin#int), h [][float64](https://pkg.go.dev/builtin#float64), ldh [int](https://pkg.go.dev/builtin#int), wr, wi [][float64](https://pkg.go.dev/builtin#float64), iloz, ihiz [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), ldz [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int), recur [int](https://pkg.go.dev/builtin#int)) (unconverged [int](https://pkg.go.dev/builtin#int))

Dlaqr04 computes the eigenvalues of a block of an n×n upper Hessenberg matrix H, and optionally the matrices T and Z from the Schur decomposition

H = Z T Zᵀ

where T is an upper quasi-triangular matrix (the Schur form), and Z is the orthogonal matrix of Schur vectors.

wantt indicates whether the full Schur form T is required. If wantt is false, then only enough of H will be updated to preserve the eigenvalues.

wantz indicates whether the n×n matrix of Schur vectors Z is required. If it is true, the orthogonal similarity transformation will be accumulated into Z[iloz:ihiz+1,ilo:ihi+1], otherwise Z will not be referenced.

ilo and ihi determine the block of H on which Dlaqr04 operates. It must hold that

0 <= ilo <= ihi < n     if n > 0,
ilo == 0 and ihi == -1  if n == 0,

and the block must be isolated, that is,

ilo == 0   or H[ilo,ilo-1] == 0,
ihi == n-1 or H[ihi+1,ihi] == 0,

otherwise Dlaqr04 will panic.

wr and wi must have length ihi+1.

iloz and ihiz specify the rows of Z to which transformations will be applied if wantz is true. It must hold that

0 <= iloz <= ilo,  and  ihi <= ihiz < n,

otherwise Dlaqr04 will panic.

work must have length at least lwork and lwork must be

lwork >= 1  if n <= 11,
lwork >= n  if n > 11,

otherwise Dlaqr04 will panic. lwork as large as 6*n may be required for optimal performance. On return, work[0] will contain the optimal value of lwork.

If lwork is -1, instead of performing Dlaqr04, the function only estimates the optimal workspace size and stores it into work[0]. Neither h nor z are accessed.

recur is the non-negative recursion depth. For recur > 0, Dlaqr04 behaves as DLAQR0, for recur == 0 it behaves as DLAQR4.

unconverged indicates whether Dlaqr04 computed all the eigenvalues of H[ilo:ihi+1,ilo:ihi+1].

If unconverged is zero and wantt is true, H will contain on return the upper quasi-triangular matrix T from the Schur decomposition. 2×2 diagonal blocks (corresponding to complex conjugate pairs of eigenvalues) will be returned in standard form, with H[i,i] == H[i+1,i+1] and H[i+1,i]*H[i,i+1] < 0.

If unconverged is zero and if wantt is false, the contents of h on return is unspecified.

If unconverged is zero, all the eigenvalues have been computed and their real and imaginary parts will be stored on return in wr[ilo:ihi+1] and wi[ilo:ihi+1], respectively. If two eigenvalues are computed as a complex conjugate pair, they are stored in consecutive elements of wr and wi, say the i-th and (i+1)th, with wi[i] > 0 and wi[i+1] < 0. If wantt is true, then the eigenvalues are stored in the same order as on the diagonal of the Schur form returned in H, with wr[i] = H[i,i] and, if H[i:i+2,i:i+2] is a 2×2 diagonal block, wi[i] = sqrt(-H[i+1,i]*H[i,i+1]) and wi[i+1] = -wi[i].

If unconverged is positive, some eigenvalues have not converged, and wr[unconverged:ihi+1] and wi[unconverged:ihi+1] will contain those eigenvalues which have been successfully computed. Failures are rare.

If unconverged is positive and wantt is true, then on return

(initial H)*U = U*(final H),   (*)

where U is an orthogonal matrix. The final H is upper Hessenberg and H[unconverged:ihi+1,unconverged:ihi+1] is upper quasi-triangular.

If unconverged is positive and wantt is false, on return the remaining unconverged eigenvalues are the eigenvalues of the upper Hessenberg matrix H[ilo:unconverged,ilo:unconverged].

If unconverged is positive and wantz is true, then on return

(final Z) = (initial Z)*U,

where U is the orthogonal matrix in (*) regardless of the value of wantt.

References:

[1] K. Braman, R. Byers, R. Mathias. The Multishift QR Algorithm. Part I:
    Maintaining Well-Focused Shifts and Level 3 Performance. SIAM J. Matrix
    Anal. Appl. 23(4) (2002), pp. 929—947
    URL: http://dx.doi.org/10.1137/S0895479801384573
[2] K. Braman, R. Byers, R. Mathias. The Multishift QR Algorithm. Part II:
    Aggressive Early Deflation. SIAM J. Matrix Anal. Appl. 23(4) (2002), pp. 948—973
    URL: http://dx.doi.org/10.1137/S0895479801384585

Dlaqr04 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlaqr5(wantt, wantz [bool](https://pkg.go.dev/builtin#bool), kacc22 [int](https://pkg.go.dev/builtin#int), n, ktop, kbot, nshfts [int](https://pkg.go.dev/builtin#int), sr, si [][float64](https://pkg.go.dev/builtin#float64), h [][float64](https://pkg.go.dev/builtin#float64), ldh [int](https://pkg.go.dev/builtin#int), iloz, ihiz [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), ldz [int](https://pkg.go.dev/builtin#int), v [][float64](https://pkg.go.dev/builtin#float64), ldv [int](https://pkg.go.dev/builtin#int), u [][float64](https://pkg.go.dev/builtin#float64), ldu [int](https://pkg.go.dev/builtin#int), nv [int](https://pkg.go.dev/builtin#int), wv [][float64](https://pkg.go.dev/builtin#float64), ldwv [int](https://pkg.go.dev/builtin#int), nh [int](https://pkg.go.dev/builtin#int), wh [][float64](https://pkg.go.dev/builtin#float64), ldwh [int](https://pkg.go.dev/builtin#int))

Dlaqr5 performs a single small-bulge multi-shift QR sweep on an isolated block of a Hessenberg matrix.

wantt and wantz determine whether the quasi-triangular Schur factor and the orthogonal Schur factor, respectively, will be computed.

kacc22 specifies the computation mode of far-from-diagonal orthogonal updates. Permitted values are:

0: Dlaqr5 will not accumulate reflections and will not use matrix-matrix
   multiply to update far-from-diagonal matrix entries.
1: Dlaqr5 will accumulate reflections and use matrix-matrix multiply to
   update far-from-diagonal matrix entries.
2: Same as kacc22=1. This option used to enable exploiting the 2×2 structure
   during matrix multiplications, but this is no longer supported.

For other values of kacc2 Dlaqr5 will panic.

n is the order of the Hessenberg matrix H.

ktop and kbot are indices of the first and last row and column of an isolated diagonal block upon which the QR sweep will be applied. It must hold that

ktop == 0,   or 0 < ktop <= n-1 and H[ktop, ktop-1] == 0, and
kbot == n-1, or 0 <= kbot < n-1 and H[kbot+1, kbot] == 0,

otherwise Dlaqr5 will panic.

nshfts is the number of simultaneous shifts. It must be positive and even, otherwise Dlaqr5 will panic.

sr and si contain the real and imaginary parts, respectively, of the shifts of origin that define the multi-shift QR sweep. On return both slices may be reordered by Dlaqr5. Their length must be equal to nshfts, otherwise Dlaqr5 will panic.

h and ldh represent the Hessenberg matrix H of size n×n. On return multi-shift QR sweep with shifts sr+i*si has been applied to the isolated diagonal block in rows and columns ktop through kbot, inclusive.

iloz and ihiz specify the rows of Z to which transformations will be applied if wantz is true. It must hold that 0 <= iloz <= ihiz < n, otherwise Dlaqr5 will panic.

z and ldz represent the matrix Z of size n×n. If wantz is true, the QR sweep orthogonal similarity transformation is accumulated into z[iloz:ihiz,iloz:ihiz] from the right, otherwise z not referenced.

v and ldv represent an auxiliary matrix V of size (nshfts/2)×3. Note that V is transposed with respect to the reference netlib implementation.

u and ldu represent an auxiliary matrix of size (2*nshfts)×(2*nshfts).

wh and ldwh represent an auxiliary matrix of size (2*nshfts-1)×nh.

wv and ldwv represent an auxiliary matrix of size nv×(2*nshfts-1).

Dlaqr5 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlaqr23(wantt, wantz [bool](https://pkg.go.dev/builtin#bool), n, ktop, kbot, nw [int](https://pkg.go.dev/builtin#int), h [][float64](https://pkg.go.dev/builtin#float64), ldh [int](https://pkg.go.dev/builtin#int), iloz, ihiz [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), ldz [int](https://pkg.go.dev/builtin#int), sr, si [][float64](https://pkg.go.dev/builtin#float64), v [][float64](https://pkg.go.dev/builtin#float64), ldv [int](https://pkg.go.dev/builtin#int), nh [int](https://pkg.go.dev/builtin#int), t [][float64](https://pkg.go.dev/builtin#float64), ldt [int](https://pkg.go.dev/builtin#int), nv [int](https://pkg.go.dev/builtin#int), wv [][float64](https://pkg.go.dev/builtin#float64), ldwv [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int), recur [int](https://pkg.go.dev/builtin#int)) (ns, nd [int](https://pkg.go.dev/builtin#int))

Dlaqr23 performs the orthogonal similarity transformation of an n×n upper Hessenberg matrix to detect and deflate fully converged eigenvalues from a trailing principal submatrix using aggressive early deflation [1].

On return, H will be overwritten by a new Hessenberg matrix that is a perturbation of an orthogonal similarity transformation of H. It is hoped that on output H will have many zero subdiagonal entries.

If wantt is true, the matrix H will be fully updated so that the quasi-triangular Schur factor can be computed. If wantt is false, then only enough of H will be updated to preserve the eigenvalues.

If wantz is true, the orthogonal similarity transformation will be accumulated into Z[iloz:ihiz+1,ktop:kbot+1], otherwise Z is not referenced.

ktop and kbot determine a block [ktop:kbot+1,ktop:kbot+1] along the diagonal of H. It must hold that

0 <= ilo <= ihi < n     if n > 0,
ilo == 0 and ihi == -1  if n == 0,

and the block must be isolated, that is, it must hold that

ktop == 0   or H[ktop,ktop-1] == 0,
kbot == n-1 or H[kbot+1,kbot] == 0,

otherwise Dlaqr23 will panic.

nw is the deflation window size. It must hold that

0 <= nw <= kbot-ktop+1,

otherwise Dlaqr23 will panic.

iloz and ihiz specify the rows of the n×n matrix Z to which transformations will be applied if wantz is true. It must hold that

0 <= iloz <= ktop,  and  kbot <= ihiz < n,

otherwise Dlaqr23 will panic.

sr and si must have length kbot+1, otherwise Dlaqr23 will panic.

v and ldv represent an nw×nw work matrix. t and ldt represent an nw×nh work matrix, and nh must be at least nw. wv and ldwv represent an nv×nw work matrix.

work must have length at least lwork and lwork must be at least max(1,2*nw), otherwise Dlaqr23 will panic. Larger values of lwork may result in greater efficiency. On return, work[0] will contain the optimal value of lwork.

If lwork is -1, instead of performing Dlaqr23, the function only estimates the optimal workspace size and stores it into work[0]. Neither h nor z are accessed.

recur is the non-negative recursion depth. For recur > 0, Dlaqr23 behaves as DLAQR3, for recur == 0 it behaves as DLAQR2.

On return, ns and nd will contain respectively the number of unconverged (i.e., approximate) eigenvalues and converged eigenvalues that are stored in sr and si.

On return, the real and imaginary parts of approximate eigenvalues that may be used for shifts will be stored respectively in sr[kbot-nd-ns+1:kbot-nd+1] and si[kbot-nd-ns+1:kbot-nd+1].

On return, the real and imaginary parts of converged eigenvalues will be stored respectively in sr[kbot-nd+1:kbot+1] and si[kbot-nd+1:kbot+1].

References:

[1] K. Braman, R. Byers, R. Mathias. The Multishift QR Algorithm. Part II:
    Aggressive Early Deflation. SIAM J. Matrix Anal. Appl 23(4) (2002), pp. 948—973
    URL: http://dx.doi.org/10.1137/S0895479801384585

Dlarf applies an elementary reflector H to an m×n matrix C:

C = H * C  if side == blas.Left
C = C * H  if side == blas.Right

H is represented in the form

H = I - tau * v * vᵀ

where tau is a scalar and v is a vector.

work must have length at least m if side == blas.Left and at least n if side == blas.Right.

Dlarf is an internal routine. It is exported for testing purposes.

func ([Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlarfb(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), direct [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[Direct](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#Direct), store [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[StoreV](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#StoreV), m, n, k [int](https://pkg.go.dev/builtin#int), v [][float64](https://pkg.go.dev/builtin#float64), ldv [int](https://pkg.go.dev/builtin#int), t [][float64](https://pkg.go.dev/builtin#float64), ldt [int](https://pkg.go.dev/builtin#int), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), ldwork [int](https://pkg.go.dev/builtin#int))

Dlarfb applies a block reflector to a matrix.

In the call to Dlarfb, the mxn c is multiplied by the implicitly defined matrix h as follows:

c = h * c   if side == Left and trans == NoTrans
c = c * h   if side == Right and trans == NoTrans
c = hᵀ * c  if side == Left and trans == Trans
c = c * hᵀ  if side == Right and trans == Trans

h is a product of elementary reflectors. direct sets the direction of multiplication

h = h_1 * h_2 * ... * h_k    if direct == Forward
h = h_k * h_k-1 * ... * h_1  if direct == Backward

The combination of direct and store defines the orientation of the elementary reflectors. In all cases the ones on the diagonal are implicitly represented.

If direct == lapack.Forward and store == lapack.ColumnWise

V = [ 1        ]
    [v1   1    ]
    [v1  v2   1]
    [v1  v2  v3]
    [v1  v2  v3]

If direct == lapack.Forward and store == lapack.RowWise

V = [ 1  v1  v1  v1  v1]
    [     1  v2  v2  v2]
    [         1  v3  v3]

If direct == lapack.Backward and store == lapack.ColumnWise

V = [v1  v2  v3]
    [v1  v2  v3]
    [ 1  v2  v3]
    [     1  v3]
    [         1]

If direct == lapack.Backward and store == lapack.RowWise

V = [v1  v1   1        ]
    [v2  v2  v2   1    ]
    [v3  v3  v3  v3   1]

An elementary reflector can be explicitly constructed by extracting the corresponding elements of v, placing a 1 where the diagonal would be, and placing zeros in the remaining elements.

t is a k×k matrix containing the block reflector, and this function will panic if t is not of sufficient size. See Dlarft for more information.

work is a temporary storage matrix with stride ldwork. work must be of size at least n×k side == Left and m×k if side == Right, and this function will panic if this size is not met.

Dlarfb is an internal routine. It is exported for testing purposes.

Dlarfg generates an elementary reflector for a Householder matrix. It creates a real elementary reflector of order n such that

H * (alpha) = (beta)
    (    x)   (   0)
Hᵀ * H = I

H is represented in the form

H = 1 - tau * (1; v) * (1 vᵀ)

where tau is a real scalar.

On entry, x contains the vector x, on exit it contains v.

Dlarfg is an internal routine. It is exported for testing purposes.

Dlarft forms the triangular factor T of a block reflector H, storing the answer in t.

H = I - V * T * Vᵀ  if store == lapack.ColumnWise
H = I - Vᵀ * T * V  if store == lapack.RowWise

H is defined by a product of the elementary reflectors where

H = H_0 * H_1 * ... * H_{k-1}  if direct == lapack.Forward
H = H_{k-1} * ... * H_1 * H_0  if direct == lapack.Backward

t is a k×k triangular matrix. t is upper triangular if direct = lapack.Forward and lower triangular otherwise. This function will panic if t is not of sufficient size.

store describes the storage of the elementary reflectors in v. See Dlarfb for a description of layout.

tau contains the scalar factors of the elementary reflectors H_i.

Dlarft is an internal routine. It is exported for testing purposes.

Dlarfx applies an elementary reflector H to a real m×n matrix C, from either the left or the right, with loop unrolling when the reflector has order less than 11.

H is represented in the form

H = I - tau * v * vᵀ,

where tau is a real scalar and v is a real vector. If tau = 0, then H is taken to be the identity matrix.

v must have length equal to m if side == blas.Left, and equal to n if side == blas.Right, otherwise Dlarfx will panic.

c and ldc represent the m×n matrix C. On return, C is overwritten by the matrix H * C if side == blas.Left, or C * H if side == blas.Right.

work must have length at least n if side == blas.Left, and at least m if side == blas.Right, otherwise Dlarfx will panic. work is not referenced if H has order < 11.

Dlarfx is an internal routine. It is exported for testing purposes.

Dlartg generates a plane rotation so that

[ cs sn] * [f] = [r]
[-sn cs]   [g] = [0]

where cs*cs + sn*sn = 1.

This is a more accurate version of BLAS Drotg that uses scaling to avoid overflow or underflow, with the other differences that

*   cs >= 0
*   if g = 0, then cs = 1 and sn = 0
*   if f = 0 and g != 0, then cs = 0 and sn = sign(1,g)

Dlartg is an internal routine. It is exported for testing purposes.

Dlas2 computes the singular values of the 2×2 matrix defined by

[F G]
[0 H]

The smaller and larger singular values are returned in that order.

Dlas2 is an internal routine. It is exported for testing purposes.

Dlascl multiplies an m×n matrix by the scalar cto/cfrom.

cfrom must not be zero, and cto and cfrom must not be NaN, otherwise Dlascl will panic.

Dlascl is an internal routine. It is exported for testing purposes.

Dlaset sets the off-diagonal elements of A to alpha, and the diagonal elements to beta. If uplo == blas.Upper, only the elements in the upper triangular part are set. If uplo == blas.Lower, only the elements in the lower triangular part are set. If uplo is otherwise, all of the elements of A are set.

Dlaset is an internal routine. It is exported for testing purposes.

Dlasq1 computes the singular values of an n×n bidiagonal matrix with diagonal d and off-diagonal e. On exit, d contains the singular values in decreasing order, and e is overwritten. d must have length at least n, e must have length at least n-1, and the input work must have length at least 4*n. Dlasq1 will panic if these conditions are not met.

Dlasq1 is an internal routine. It is exported for testing purposes.

Dlasq2 computes all the eigenvalues of the symmetric positive definite tridiagonal matrix associated with the qd array Z. Eigevalues are computed to high relative accuracy avoiding denormalization, underflow and overflow.

To see the relation of Z to the tridiagonal matrix, let L be a unit lower bidiagonal matrix with sub-diagonals Z(2,4,6,,..) and let U be an upper bidiagonal matrix with 1's above and diagonal Z(1,3,5,,..). The tridiagonal is L*U or, if you prefer, the symmetric tridiagonal to which it is similar.

info returns a status error. The return codes mean as follows:

0: The algorithm completed successfully.
1: A split was marked by a positive value in e.
2: Current block of Z not diagonalized after 100*n iterations (in inner
   while loop). On exit Z holds a qd array with the same eigenvalues as
   the given Z.
3: Termination criterion of outer while loop not met (program created more
   than N unreduced blocks).

z must have length at least 4*n, and must not contain any negative elements. Dlasq2 will panic otherwise.

Dlasq2 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlasq3(i0, n0 [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), pp [int](https://pkg.go.dev/builtin#int), dmin, sigma, desig, qmax [float64](https://pkg.go.dev/builtin#float64), nFail, iter, nDiv [int](https://pkg.go.dev/builtin#int), ttype [int](https://pkg.go.dev/builtin#int), dmin1, dmin2, dn, dn1, dn2, g, tau [float64](https://pkg.go.dev/builtin#float64)) (
	i0Out, n0Out, ppOut [int](https://pkg.go.dev/builtin#int), dminOut, sigmaOut, desigOut, qmaxOut [float64](https://pkg.go.dev/builtin#float64), nFailOut, iterOut, nDivOut, ttypeOut [int](https://pkg.go.dev/builtin#int), dmin1Out, dmin2Out, dnOut, dn1Out, dn2Out, gOut, tauOut [float64](https://pkg.go.dev/builtin#float64))

Dlasq3 checks for deflation, computes a shift (tau) and calls dqds. In case of failure it changes shifts, and tries again until output is positive.

Dlasq3 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlasq4(i0, n0 [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), pp [int](https://pkg.go.dev/builtin#int), n0in [int](https://pkg.go.dev/builtin#int), dmin, dmin1, dmin2, dn, dn1, dn2, tau [float64](https://pkg.go.dev/builtin#float64), ttype [int](https://pkg.go.dev/builtin#int), g [float64](https://pkg.go.dev/builtin#float64)) (tauOut [float64](https://pkg.go.dev/builtin#float64), ttypeOut [int](https://pkg.go.dev/builtin#int), gOut [float64](https://pkg.go.dev/builtin#float64))

Dlasq4 computes an approximation to the smallest eigenvalue using values of d from the previous transform. i0, n0, and n0in are zero-indexed.

Dlasq4 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlasq5(i0, n0 [int](https://pkg.go.dev/builtin#int), z [][float64](https://pkg.go.dev/builtin#float64), pp [int](https://pkg.go.dev/builtin#int), tau, sigma [float64](https://pkg.go.dev/builtin#float64)) (i0Out, n0Out, ppOut [int](https://pkg.go.dev/builtin#int), tauOut, sigmaOut, dmin, dmin1, dmin2, dn, dnm1, dnm2 [float64](https://pkg.go.dev/builtin#float64))

Dlasq5 computes one dqds transform in ping-pong form. i0 and n0 are zero-indexed.

Dlasq5 is an internal routine. It is exported for testing purposes.

Dlasq6 computes one dqd transform in ping-pong form with protection against overflow and underflow. z has length at least 4*(n0+1) and holds the qd array. i0 is the zero-based first index. n0 is the zero-based last index.

Dlasq6 is an internal routine. It is exported for testing purposes.

Dlasr applies a sequence of plane rotations to the m×n matrix A. This series of plane rotations is implicitly represented by a matrix P. P is multiplied by a depending on the value of side -- A = P * A if side == lapack.Left, A = A * Pᵀ if side == lapack.Right.

The exact value of P depends on the value of pivot, but in all cases P is implicitly represented by a series of 2×2 rotation matrices. The entries of rotation matrix k are defined by s[k] and c[k]

R(k) = [ c[k] s[k]]
       [-s[k] s[k]]

If direct == lapack.Forward, the rotation matrices are applied as P = P(z-1) * ... * P(2) * P(1), while if direct == lapack.Backward they are applied as P = P(1) * P(2) * ... * P(n).

pivot defines the mapping of the elements in R(k) to P(k). If pivot == lapack.Variable, the rotation is performed for the (k, k+1) plane.

P(k) = [1                    ]
       [    ...              ]
       [     1               ]
       [       c[k] s[k]     ]
       [      -s[k] c[k]     ]
       [                 1   ]
       [                ...  ]
       [                    1]

if pivot == lapack.Top, the rotation is performed for the (1, k+1) plane,

P(k) = [c[k]        s[k]     ]
       [    1                ]
       [     ...             ]
       [         1           ]
       [-s[k]       c[k]     ]
       [                 1   ]
       [                ...  ]
       [                    1]

and if pivot == lapack.Bottom, the rotation is performed for the (k, z) plane.

P(k) = [1                    ]
       [  ...                ]
       [      1              ]
       [        c[k]     s[k]]
       [           1         ]
       [            ...      ]
       [              1      ]
       [       -s[k]     c[k]]

s and c have length m - 1 if side == blas.Left, and n - 1 if side == blas.Right.

Dlasr is an internal routine. It is exported for testing purposes.

Dlasrt sorts the numbers in the input slice d. If s == lapack.SortIncreasing, the elements are sorted in increasing order. If s == lapack.SortDecreasing, the elements are sorted in decreasing order. For other values of s Dlasrt will panic.

Dlasrt is an internal routine. It is exported for testing purposes.

Dlassq updates a sum of squares represented in scaled form. Dlassq returns the values scl and smsq such that

scl^2*smsq = X[0]^2 + ... + X[n-1]^2 + scale^2*sumsq

The value of sumsq is assumed to be non-negative.

Dlassq is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlasv2(f, g, h [float64](https://pkg.go.dev/builtin#float64)) (ssmin, ssmax, snr, csr, snl, csl [float64](https://pkg.go.dev/builtin#float64))

Dlasv2 computes the singular value decomposition of a 2×2 matrix.

[ csl snl] [f g] [csr -snr] = [ssmax     0]
[-snl csl] [0 h] [snr  csr] = [    0 ssmin]

ssmax is the larger absolute singular value, and ssmin is the smaller absolute singular value. [cls, snl] and [csr, snr] are the left and right singular vectors.

Dlasv2 is an internal routine. It is exported for testing purposes.

Dlaswp swaps the rows k1 to k2 of a rectangular matrix A according to the indices in ipiv so that row k is swapped with ipiv[k].

n is the number of columns of A and incX is the increment for ipiv. If incX is 1, the swaps are applied from k1 to k2. If incX is -1, the swaps are applied in reverse order from k2 to k1. For other values of incX Dlaswp will panic. ipiv must have length k2+1, otherwise Dlaswp will panic.

The indices k1, k2, and the elements of ipiv are zero-based.

Dlaswp is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dlasy2(tranl, tranr [bool](https://pkg.go.dev/builtin#bool), isgn, n1, n2 [int](https://pkg.go.dev/builtin#int), tl [][float64](https://pkg.go.dev/builtin#float64), ldtl [int](https://pkg.go.dev/builtin#int), tr [][float64](https://pkg.go.dev/builtin#float64), ldtr [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), ldx [int](https://pkg.go.dev/builtin#int)) (scale, xnorm [float64](https://pkg.go.dev/builtin#float64), ok [bool](https://pkg.go.dev/builtin#bool))

Dlasy2 solves the Sylvester matrix equation where the matrices are of order 1 or 2. It computes the unknown n1×n2 matrix X so that

TL*X   + sgn*X*TR  = scale*B  if tranl == false and tranr == false,
TLᵀ*X + sgn*X*TR   = scale*B  if tranl == true  and tranr == false,
TL*X   + sgn*X*TRᵀ = scale*B  if tranl == false and tranr == true,
TLᵀ*X + sgn*X*TRᵀ  = scale*B  if tranl == true  and tranr == true,

where TL is n1×n1, TR is n2×n2, B is n1×n2, and 1 <= n1,n2 <= 2.

isgn must be 1 or -1, and n1 and n2 must be 0, 1, or 2, but these conditions are not checked.

Dlasy2 returns three values, a scale factor that is chosen less than or equal to 1 to prevent the solution overflowing, the infinity norm of the solution, and an indicator of success. If ok is false, TL and TR have eigenvalues that are too close, so TL or TR is perturbed to get a non-singular equation.

Dlasy2 is an internal routine. It is exported for testing purposes.

Dlatbs solves a triangular banded system of equations

A * x = s*b    if trans == blas.NoTrans
Aᵀ * x = s*b  if trans == blas.Trans or blas.ConjTrans

where A is an upper or lower triangular band matrix, x and b are n-element vectors, and s is a scaling factor chosen so that the components of x will be less than the overflow threshold.

On entry, x contains the right-hand side b of the triangular system. On return, x is overwritten by the solution vector x.

normin specifies whether the cnorm parameter contains the column norms of A on entry. If it is true, cnorm[j] contains the norm of the off-diagonal part of the j-th column of A. If it is false, the norms will be computed and stored in cnorm.

Dlatbs returns the scaling factor s for the triangular system. If the matrix A is singular (A[j,j]==0 for some j), then scale is set to 0 and a non-trivial solution to A*x = 0 is returned.

Dlatbs is an internal routine. It is exported for testing purposes.

Dlatdf computes a contribution to the reciprocal Dif-estimate by solving

Z * x = h - f

and choosing the vector h such that the norm of x is as large as possible.

The n×n matrix Z is represented by its LU factorization as computed by Dgetc2 and has the form

Z = P * L * U * Q

where P and Q are permutation matrices, L is lower triangular with unit diagonal elements and U is upper triangular.

job specifies the heuristic method for computing the contribution.

If job is lapack.LocalLookAhead, all entries of h are chosen as either +1 or -1.

If job is lapack.NormalizedNullVector, an approximate null-vector e of Z is computed using Dgecon and normalized. h is chosen as ±e with the sign giving the greater value of 2-norm(x). This strategy is about 5 times as expensive as LocalLookAhead.

On entry, rhs holds the contribution f from earlier solved sub-systems. On return, rhs holds the solution x.

ipiv and jpiv contain the pivot indices as returned by Dgetc2: row i of the matrix has been interchanged with row ipiv[i] and column j of the matrix has been interchanged with column jpiv[j].

n must be at most 8, ipiv and jpiv must have length n, and rhs must have length at least n, otherwise Dlatdf will panic.

rdsum and rdscal represent the sum of squares of computed contributions to the Dif-estimate from earlier solved sub-systems. rdscal is the scaling factor used to prevent overflow in rdsum. Dlatdf returns this sum of squares updated with the contributions from the current sub-system.

Dlatdf is an internal routine. It is exported for testing purposes.

Dlatrd reduces nb rows and columns of a real n×n symmetric matrix A to symmetric tridiagonal form. It computes the orthonormal similarity transformation

Qᵀ * A * Q

and returns the matrices V and W to apply to the unreduced part of A. If uplo == blas.Upper, the upper triangle is supplied and the last nb rows are reduced. If uplo == blas.Lower, the lower triangle is supplied and the first nb rows are reduced.

a contains the symmetric matrix on entry with active triangular half specified by uplo. On exit, the nb columns have been reduced to tridiagonal form. The diagonal contains the diagonal of the reduced matrix, the off-diagonal is set to 1, and the remaining elements contain the data to construct Q.

If uplo == blas.Upper, with n = 5 and nb = 2 on exit a is

[ a   a   a  v4  v5]
[     a   a  v4  v5]
[         a   1  v5]
[             d   1]
[                 d]

If uplo == blas.Lower, with n = 5 and nb = 2, on exit a is

[ d                ]
[ 1   d            ]
[v1   1   a        ]
[v1  v2   a   a    ]
[v1  v2   a   a   a]

e contains the superdiagonal elements of the reduced matrix. If uplo == blas.Upper, e[n-nb:n-1] contains the last nb columns of the reduced matrix, while if uplo == blas.Lower, e[:nb] contains the first nb columns of the reduced matrix. e must have length at least n-1, and Dlatrd will panic otherwise.

tau contains the scalar factors of the elementary reflectors needed to construct Q. The reflectors are stored in tau[n-nb:n-1] if uplo == blas.Upper, and in tau[:nb] if uplo == blas.Lower. tau must have length n-1, and Dlatrd will panic otherwise.

w is an n×nb matrix. On exit it contains the data to update the unreduced part of A.

The matrix Q is represented as a product of elementary reflectors. Each reflector H has the form

I - tau * v * vᵀ

If uplo == blas.Upper,

Q = H_{n-1} * H_{n-2} * ... * H_{n-nb}

where v[:i-1] is stored in A[:i-1,i], v[i-1] = 1, and v[i:n] = 0.

If uplo == blas.Lower,

Q = H_0 * H_1 * ... * H_{nb-1}

where v[:i+1] = 0, v[i+1] = 1, and v[i+2:n] is stored in A[i+2:n,i].

The vectors v form the n×nb matrix V which is used with W to apply a symmetric rank-2 update to the unreduced part of A

A = A - V * Wᵀ - W * Vᵀ

Dlatrd is an internal routine. It is exported for testing purposes.

Dlatrs solves a triangular system of equations scaled to prevent overflow. It solves

A * x = scale * b if trans == blas.NoTrans
Aᵀ * x = scale * b if trans == blas.Trans

where the scale s is set for numeric stability.

A is an n×n triangular matrix. On entry, the slice x contains the values of b, and on exit it contains the solution vector x.

If normin == true, cnorm is an input and cnorm[j] contains the norm of the off-diagonal part of the j^th column of A. If trans == blas.NoTrans, cnorm[j] must be greater than or equal to the infinity norm, and greater than or equal to the one-norm otherwise. If normin == false, then cnorm is treated as an output, and is set to contain the 1-norm of the off-diagonal part of the j^th column of A.

Dlatrs is an internal routine. It is exported for testing purposes.

Dlauu2 computes the product

U * Uᵀ  if uplo is blas.Upper
Lᵀ * L  if uplo is blas.Lower

where U or L is stored in the upper or lower triangular part of A. Only the upper or lower triangle of the result is stored, overwriting the corresponding factor in A.

Dlauum computes the product

U * Uᵀ  if uplo is blas.Upper
Lᵀ * L  if uplo is blas.Lower

where U or L is stored in the upper or lower triangular part of A. Only the upper or lower triangle of the result is stored, overwriting the corresponding factor in A.

Dorg2l generates an m×n matrix Q with orthonormal columns which is defined as the last n columns of a product of k elementary reflectors of order m.

Q = H_{k-1} * ... * H_1 * H_0

See Dgelqf for more information. It must be that m >= n >= k.

tau contains the scalar reflectors computed by Dgeqlf. tau must have length at least k, and Dorg2l will panic otherwise.

work contains temporary memory, and must have length at least n. Dorg2l will panic otherwise.

Dorg2l is an internal routine. It is exported for testing purposes.

Dorg2r generates an m×n matrix Q with orthonormal columns defined by the product of elementary reflectors as computed by Dgeqrf.

Q = H_0 * H_1 * ... * H_{k-1}

len(tau) = k, 0 <= k <= n, 0 <= n <= m, len(work) >= n. Dorg2r will panic if these conditions are not met.

Dorg2r is an internal routine. It is exported for testing purposes.

Dorgbr generates one of the matrices Q or Pᵀ computed by Dgebrd computed from the decomposition Dgebrd. See Dgebd2 for the description of Q and Pᵀ.

If vect == lapack.GenerateQ, then a is assumed to have been an m×k matrix and Q is of order m. If m >= k, then Dorgbr returns the first n columns of Q where m >= n >= k. If m < k, then Dorgbr returns Q as an m×m matrix.

If vect == lapack.GeneratePT, then A is assumed to have been a k×n matrix, and Pᵀ is of order n. If k < n, then Dorgbr returns the first m rows of Pᵀ, where n >= m >= k. If k >= n, then Dorgbr returns Pᵀ as an n×n matrix.

Dorgbr is an internal routine. It is exported for testing purposes.

Dorghr generates an n×n orthogonal matrix Q which is defined as the product of ihi-ilo elementary reflectors:

Q = H_{ilo} H_{ilo+1} ... H_{ihi-1}.

a and lda represent an n×n matrix that contains the elementary reflectors, as returned by Dgehrd. On return, a is overwritten by the n×n orthogonal matrix Q. Q will be equal to the identity matrix except in the submatrix Q[ilo+1:ihi+1,ilo+1:ihi+1].

ilo and ihi must have the same values as in the previous call of Dgehrd. It must hold that

0 <= ilo <= ihi < n  if n > 0,
ilo = 0, ihi = -1    if n == 0.

tau contains the scalar factors of the elementary reflectors, as returned by Dgehrd. tau must have length n-1.

work must have length at least max(1,lwork) and lwork must be at least ihi-ilo. For optimum performance lwork must be at least (ihi-ilo)*nb where nb is the optimal blocksize. On return, work[0] will contain the optimal value of lwork.

If lwork == -1, instead of performing Dorghr, only the optimal value of lwork will be stored into work[0].

If any requirement on input sizes is not met, Dorghr will panic.

Dorghr is an internal routine. It is exported for testing purposes.

Dorgl2 generates an m×n matrix Q with orthonormal rows defined as the first m rows of a product of k elementary reflectors of order n

Q = H_{k-1} * ... * H_0

as returned by Dgelqf.

On entry, tau and the first k rows of A must contain the scalar factors and the vectors, respectively, which define the elementary reflectors H_i, i=0,...,k-1, as returned by Dgelqf. On return, A contains the matrix Q.

tau must have length at least k, work must have length at least m, and it must hold that 0 <= k <= m <= n, otherwise Dorgl2 will panic.

Dorgl2 is an internal routine. It is exported for testing purposes.

Dorglq generates an m×n matrix Q with orthonormal rows defined as the first m rows of a product of k elementary reflectors of order n

Q = H_{k-1} * ... * H_0

as returned by Dgelqf.

On entry, tau and the first k rows of A must contain the scalar factors and the vectors, respectively, which define the elementary reflectors H_i, i=0,...,k-1, as returned by Dgelqf. On return, A contains the matrix Q.

tau must have length at least k, work must have length at least lwork and lwork must be at least max(1,m). On return, optimal value of lwork will be stored in work[0]. It must also hold that 0 <= k <= m <= n, otherwise Dorglq will panic.

If lwork == -1, instead of performing Dorglq, the function only calculates the optimal value of lwork and stores it into work[0].

Dorgql generates the m×n matrix Q with orthonormal columns defined as the last n columns of a product of k elementary reflectors of order m

Q = H_{k-1} * ... * H_1 * H_0.

It must hold that

0 <= k <= n <= m,

and Dorgql will panic otherwise.

On entry, the (n-k+i)-th column of A must contain the vector which defines the elementary reflector H_i, for i=0,...,k-1, and tau[i] must contain its scalar factor. On return, a contains the m×n matrix Q.

tau must have length at least k, and Dorgql will panic otherwise.

work must have length at least max(1,lwork), and lwork must be at least max(1,n), otherwise Dorgql will panic. For optimum performance lwork must be a sufficiently large multiple of n.

If lwork == -1, instead of computing Dorgql the optimal work length is stored into work[0].

Dorgql is an internal routine. It is exported for testing purposes.

Dorgqr generates an m×n matrix Q with orthonormal columns defined by the product of elementary reflectors

Q = H_0 * H_1 * ... * H_{k-1}

as computed by Dgeqrf. Dorgqr is the blocked version of Dorg2r that makes greater use of level-3 BLAS routines.

The length of tau must be k, and the length of work must be at least n. It also must be that 0 <= k <= n and 0 <= n <= m.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= n, and the amount of blocking is limited by the usable length. If lwork == -1, instead of computing Dorgqr the optimal work length is stored into work[0].

Dorgqr will panic if the conditions on input values are not met.

Dorgqr is an internal routine. It is exported for testing purposes.

Dorgr2 generates an m×n real matrix Q with orthonormal rows, which is defined as the last m rows of a product of k elementary reflectors of order n

Q = H_0 * H_1 * ... * H_{k-1}

as returned by Dgerqf.

On entry, the (m-k+i)-th row of A must contain the vector which defines the elementary reflector H_i, for i = 0,1,...,k, as returned by Dgerqf. On return, A will contain the m×n matrix Q.

The i-th element of tau must contain the scalar factor of the elementary reflector H_i, as returned by Dgerqf.

It must hold that

n >= m >= k >= 0,

the length of tau must be k and the length of work must be m, otherwise Dorgr2 will panic.

Dorgr2 is an internal routine. It is exported for testing purposes.

Dorgtr generates a real orthogonal matrix Q which is defined as the product of n-1 elementary reflectors of order n as returned by Dsytrd.

The construction of Q depends on the value of uplo:

Q = H_{n-1} * ... * H_1 * H_0  if uplo == blas.Upper
Q = H_0 * H_1 * ... * H_{n-1}  if uplo == blas.Lower

where H_i is constructed from the elementary reflectors as computed by Dsytrd. See the documentation for Dsytrd for more information.

tau must have length at least n-1, and Dorgtr will panic otherwise.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= max(1,n-1), and Dorgtr will panic otherwise. The amount of blocking is limited by the usable length. If lwork == -1, instead of computing Dorgtr the optimal work length is stored into work[0].

Dorgtr is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dorm2r(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), tau, c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64))

Dorm2r multiplies a general matrix C by an orthogonal matrix from a QR factorization determined by Dgeqrf.

C = Q * C   if side == blas.Left and trans == blas.NoTrans
C = Qᵀ * C  if side == blas.Left and trans == blas.Trans
C = C * Q   if side == blas.Right and trans == blas.NoTrans
C = C * Qᵀ  if side == blas.Right and trans == blas.Trans

If side == blas.Left, a is a matrix of size m×k, and if side == blas.Right a is of size n×k.

tau contains the Householder factors and must have length k and this function will panic otherwise.

work is temporary storage of length at least n if side == blas.Left and at least m if side == blas.Right and this function will panic otherwise.

Dorm2r is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dormbr(vect [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[ApplyOrtho](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#ApplyOrtho), side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), tau, c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int))

Dormbr applies a multiplicative update to the matrix C based on a decomposition computed by Dgebrd.

Dormbr overwrites the m×n matrix C with

Q * C   if vect == lapack.ApplyQ, side == blas.Left, and trans == blas.NoTrans
C * Q   if vect == lapack.ApplyQ, side == blas.Right, and trans == blas.NoTrans
Qᵀ * C  if vect == lapack.ApplyQ, side == blas.Left, and trans == blas.Trans
C * Qᵀ  if vect == lapack.ApplyQ, side == blas.Right, and trans == blas.Trans

P * C   if vect == lapack.ApplyP, side == blas.Left, and trans == blas.NoTrans
C * P   if vect == lapack.ApplyP, side == blas.Right, and trans == blas.NoTrans
Pᵀ * C  if vect == lapack.ApplyP, side == blas.Left, and trans == blas.Trans
C * Pᵀ  if vect == lapack.ApplyP, side == blas.Right, and trans == blas.Trans

where P and Q are the orthogonal matrices determined by Dgebrd when reducing a matrix A to bidiagonal form: A = Q * B * Pᵀ. See Dgebrd for the definitions of Q and P.

If vect == lapack.ApplyQ, A is assumed to have been an nq×k matrix, while if vect == lapack.ApplyP, A is assumed to have been a k×nq matrix. nq = m if side == blas.Left, while nq = n if side == blas.Right.

tau must have length min(nq,k), and Dormbr will panic otherwise. tau contains the elementary reflectors to construct Q or P depending on the value of vect.

work must have length at least max(1,lwork), and lwork must be either -1 or at least max(1,n) if side == blas.Left, and at least max(1,m) if side == blas.Right. For optimum performance lwork should be at least n*nb if side == blas.Left, and at least m*nb if side == blas.Right, where nb is the optimal block size. On return, work[0] will contain the optimal value of lwork.

If lwork == -1, the function only calculates the optimal value of lwork and returns it in work[0].

Dormbr is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dormhr(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, ilo, ihi [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), tau, c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int))

Dormhr multiplies an m×n general matrix C with an nq×nq orthogonal matrix Q

Q * C   if side == blas.Left  and trans == blas.NoTrans,
Qᵀ * C  if side == blas.Left  and trans == blas.Trans,
C * Q   if side == blas.Right and trans == blas.NoTrans,
C * Qᵀ  if side == blas.Right and trans == blas.Trans,

where nq == m if side == blas.Left and nq == n if side == blas.Right.

Q is defined implicitly as the product of ihi-ilo elementary reflectors, as returned by Dgehrd:

Q = H_{ilo} H_{ilo+1} ... H_{ihi-1}.

Q is equal to the identity matrix except in the submatrix Q[ilo+1:ihi+1,ilo+1:ihi+1].

ilo and ihi must have the same values as in the previous call of Dgehrd. It must hold that

0 <= ilo <= ihi < m   if m > 0 and side == blas.Left,
ilo = 0 and ihi = -1  if m = 0 and side == blas.Left,
0 <= ilo <= ihi < n   if n > 0 and side == blas.Right,
ilo = 0 and ihi = -1  if n = 0 and side == blas.Right.

a and lda represent an m×m matrix if side == blas.Left and an n×n matrix if side == blas.Right. The matrix contains vectors which define the elementary reflectors, as returned by Dgehrd.

tau contains the scalar factors of the elementary reflectors, as returned by Dgehrd. tau must have length m-1 if side == blas.Left and n-1 if side == blas.Right.

c and ldc represent the m×n matrix C. On return, c is overwritten by the product with Q.

work must have length at least max(1,lwork), and lwork must be at least max(1,n), if side == blas.Left, and max(1,m), if side == blas.Right. For optimum performance lwork should be at least n*nb if side == blas.Left and m*nb if side == blas.Right, where nb is the optimal block size. On return, work[0] will contain the optimal value of lwork.

If lwork == -1, instead of performing Dormhr, only the optimal value of lwork will be stored in work[0].

If any requirement on input sizes is not met, Dormhr will panic.

Dormhr is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dorml2(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), tau, c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64))

Dorml2 multiplies a general matrix C by an orthogonal matrix from an LQ factorization determined by Dgelqf.

C = Q * C   if side == blas.Left and trans == blas.NoTrans
C = Qᵀ * C  if side == blas.Left and trans == blas.Trans
C = C * Q   if side == blas.Right and trans == blas.NoTrans
C = C * Qᵀ  if side == blas.Right and trans == blas.Trans

If side == blas.Left, a is a matrix of side k×m, and if side == blas.Right a is of size k×n.

tau contains the Householder factors and is of length at least k and this function will panic otherwise.

work is temporary storage of length at least n if side == blas.Left and at least m if side == blas.Right and this function will panic otherwise.

Dorml2 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dormlq(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), tau, c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int))

Dormlq multiplies the matrix C by the orthogonal matrix Q defined by the slices a and tau. A and tau are as returned from Dgelqf.

C = Q * C   if side == blas.Left and trans == blas.NoTrans
C = Qᵀ * C  if side == blas.Left and trans == blas.Trans
C = C * Q   if side == blas.Right and trans == blas.NoTrans
C = C * Qᵀ  if side == blas.Right and trans == blas.Trans

If side == blas.Left, A is a matrix of side k×m, and if side == blas.Right A is of size k×n. This uses a blocked algorithm.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= m if side == blas.Left and lwork >= n if side == blas.Right, and this function will panic otherwise. Dormlq uses a block algorithm, but the block size is limited by the temporary space available. If lwork == -1, instead of performing Dormlq, the optimal work length will be stored into work[0].

tau contains the Householder scales and must have length at least k, and this function will panic otherwise.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dormqr(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), tau, c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int))

Dormqr multiplies an m×n matrix C by an orthogonal matrix Q as

C = Q * C   if side == blas.Left  and trans == blas.NoTrans,
C = Qᵀ * C  if side == blas.Left  and trans == blas.Trans,
C = C * Q   if side == blas.Right and trans == blas.NoTrans,
C = C * Qᵀ  if side == blas.Right and trans == blas.Trans,

where Q is defined as the product of k elementary reflectors

Q = H_0 * H_1 * ... * H_{k-1}.

If side == blas.Left, A is an m×k matrix and 0 <= k <= m. If side == blas.Right, A is an n×k matrix and 0 <= k <= n. The ith column of A contains the vector which defines the elementary reflector H_i and tau[i] contains its scalar factor. tau must have length k and Dormqr will panic otherwise. Dgeqrf returns A and tau in the required form.

work must have length at least max(1,lwork), and lwork must be at least n if side == blas.Left and at least m if side == blas.Right, otherwise Dormqr will panic.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= m if side == blas.Left and lwork >= n if side == blas.Right, and this function will panic otherwise. Larger values of lwork will generally give better performance. On return, work[0] will contain the optimal value of lwork.

If lwork is -1, instead of performing Dormqr, the optimal workspace size will be stored into work[0].

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dormr2(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), tau, c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64))

Dormr2 multiplies a general matrix C by an orthogonal matrix from a RQ factorization determined by Dgerqf.

C = Q * C   if side == blas.Left and trans == blas.NoTrans
C = Qᵀ * C  if side == blas.Left and trans == blas.Trans
C = C * Q   if side == blas.Right and trans == blas.NoTrans
C = C * Qᵀ  if side == blas.Right and trans == blas.Trans

If side == blas.Left, a is a matrix of size k×m, and if side == blas.Right a is of size k×n.

tau contains the Householder factors and is of length at least k and this function will panic otherwise.

work is temporary storage of length at least n if side == blas.Left and at least m if side == blas.Right and this function will panic otherwise.

Dormr2 is an internal routine. It is exported for testing purposes.

Dpbcon returns an estimate of the reciprocal of the condition number (in the 1-norm) of an n×n symmetric positive definite band matrix using the Cholesky factorization

A = Uᵀ*U  if uplo == blas.Upper
A = L*Lᵀ  if uplo == blas.Lower

computed by Dpbtrf. The estimate is obtained for norm(inv(A)), and the reciprocal of the condition number is computed as

rcond = 1 / (anorm * norm(inv(A))).

The length of work must be at least 3*n and the length of iwork must be at least n.

Dpbtf2 computes the Cholesky factorization of a symmetric positive banded matrix ab. The matrix ab is n×n with kd diagonal bands. The Cholesky factorization computed is

A = Uᵀ * U  if ul == blas.Upper
A = L * Lᵀ  if ul == blas.Lower

ul also specifies the storage of ab. If ul == blas.Upper, then ab is stored as an upper-triangular banded matrix with kd super-diagonals, and if ul == blas.Lower, ab is stored as a lower-triangular banded matrix with kd sub-diagonals. On exit, the banded matrix U or L is stored in-place into ab depending on the value of ul. Dpbtf2 returns whether the factorization was successfully completed.

The band storage scheme is illustrated below when n = 6, and kd = 2. The resulting Cholesky decomposition is stored in the same elements as the input band matrix (a11 becomes u11 or l11, etc.).

ul = blas.Upper
a11 a12 a13
a22 a23 a24
a33 a34 a35
a44 a45 a46
a55 a56  *
a66  *   *

ul = blas.Lower
 *   *  a11
 *  a21 a22
a31 a32 a33
a42 a43 a44
a53 a54 a55
a64 a65 a66

Dpbtf2 is the unblocked version of the algorithm, see Dpbtrf for the blocked version.

Dpbtf2 is an internal routine, exported for testing purposes.

Dpbtrf computes the Cholesky factorization of an n×n symmetric positive definite band matrix

A = Uᵀ * U  if uplo == blas.Upper
A = L * Lᵀ  if uplo == blas.Lower

where U is an upper triangular band matrix and L is lower triangular. kd is the number of super- or sub-diagonals of A.

The band storage scheme is illustrated below when n = 6 and kd = 2. Elements marked * are not used by the function.

uplo == blas.Upper
On entry:         On return:
 a00  a01  a02     u00  u01  u02
 a11  a12  a13     u11  u12  u13
 a22  a23  a24     u22  u23  u24
 a33  a34  a35     u33  u34  u35
 a44  a45   *      u44  u45   *
 a55   *    *      u55   *    *

uplo == blas.Lower
On entry:         On return:
  *    *   a00       *    *   l00
  *   a10  a11       *   l10  l11
 a20  a21  a22      l20  l21  l22
 a31  a32  a33      l31  l32  l33
 a42  a43  a44      l42  l43  l44
 a53  a54  a55      l53  l54  l55

Dpbtrs solves a system of linear equations A*X = B with an n×n symmetric positive definite band matrix A using the Cholesky factorization

A = Uᵀ * U  if uplo == blas.Upper
A = L * Lᵀ  if uplo == blas.Lower

computed by Dpbtrf. kd is the number of super- or sub-diagonals of A. See the documentation for Dpbtrf for a description of the band storage format of A.

On entry, b contains the n×nrhs right hand side matrix B. On return, it is overwritten with the solution matrix X.

Dpocon estimates the reciprocal of the condition number of a positive-definite matrix A given the Cholesky decomposition of A. The condition number computed is based on the 1-norm and the ∞-norm.

anorm is the 1-norm and the ∞-norm of the original matrix A.

work is a temporary data slice of length at least 3*n and Dpocon will panic otherwise.

iwork is a temporary data slice of length at least n and Dpocon will panic otherwise.

Dpotf2 computes the Cholesky decomposition of the symmetric positive definite matrix a. If ul == blas.Upper, then a is stored as an upper-triangular matrix, and a = Uᵀ U is stored in place into a. If ul == blas.Lower, then a = L Lᵀ is computed and stored in-place into a. If a is not positive definite, false is returned. This is the unblocked version of the algorithm.

Dpotf2 is an internal routine. It is exported for testing purposes.

Dpotrf computes the Cholesky decomposition of the symmetric positive definite matrix a. If ul == blas.Upper, then a is stored as an upper-triangular matrix, and a = Uᵀ U is stored in place into a. If ul == blas.Lower, then a = L Lᵀ is computed and stored in-place into a. If a is not positive definite, false is returned. This is the blocked version of the algorithm.

Dpotri computes the inverse of a real symmetric positive definite matrix A using its Cholesky factorization.

On entry, a contains the triangular factor U or L from the Cholesky factorization A = Uᵀ*U or A = L*Lᵀ, as computed by Dpotrf. On return, a contains the upper or lower triangle of the (symmetric) inverse of A, overwriting the input factor U or L.

Dpotrs solves a system of n linear equations A*X = B where A is an n×n symmetric positive definite matrix and B is an n×nrhs matrix. The matrix A is represented by its Cholesky factorization

A = Uᵀ*U  if uplo == blas.Upper
A = L*Lᵀ  if uplo == blas.Lower

as computed by Dpotrf. On entry, B contains the right-hand side matrix B, on return it contains the solution matrix X.

Dpstf2 computes the Cholesky factorization with complete pivoting of an n×n symmetric positive semidefinite matrix A.

The factorization has the form

Pᵀ * A * P = Uᵀ * U ,  if uplo = blas.Upper,
Pᵀ * A * P = L  * Lᵀ,  if uplo = blas.Lower,

where U is an upper triangular matrix, L is lower triangular, and P is a permutation matrix.

tol is a user-defined tolerance. The algorithm terminates if the pivot is less than or equal to tol. If tol is negative, then n*eps*max(A[k,k]) will be used instead.

On return, A contains the factor U or L from the Cholesky factorization and piv contains P stored such that P[piv[k],k] = 1.

Dpstf2 returns the computed rank of A and whether the factorization can be used to solve a system. Dpstf2 does not attempt to check that A is positive semi-definite, so if ok is false, the matrix A is either rank deficient or is not positive semidefinite.

The length of piv must be n and the length of work must be at least 2*n, otherwise Dpstf2 will panic.

Dpstf2 is an internal routine. It is exported for testing purposes.

Dpstrf computes the Cholesky factorization with complete pivoting of an n×n symmetric positive semidefinite matrix A.

The factorization has the form

Pᵀ * A * P = Uᵀ * U ,  if uplo = blas.Upper,
Pᵀ * A * P = L  * Lᵀ,  if uplo = blas.Lower,

where U is an upper triangular matrix, L is lower triangular, and P is a permutation matrix.

tol is a user-defined tolerance. The algorithm terminates if the pivot is less than or equal to tol. If tol is negative, then n*eps*max(A[k,k]) will be used instead.

On return, A contains the factor U or L from the Cholesky factorization and piv contains P stored such that P[piv[k],k] = 1.

Dpstrf returns the computed rank of A and whether the factorization can be used to solve a system. Dpstrf does not attempt to check that A is positive semi-definite, so if ok is false, the matrix A is either rank deficient or is not positive semidefinite.

The length of piv must be n and the length of work must be at least 2*n, otherwise Dpstrf will panic.

Dpstrf is an internal routine. It is exported for testing purposes.

Dptcon computes and returns the reciprocal of the condition number (in the 1-norm) of a symmetric positive definite tridiagonal matrix A using the factorization A = L*D*Lᵀ or A = Uᵀ*D*U computed by Dpttrf.

The reciprocal of the condition number is computed as

rcond = 1 / (anorm * ‖A⁻¹‖)

and ‖A⁻¹‖ is computed by a direct method.

d and e contain, respectively, the n diagonal elements of the diagonal matrix D and the (n-1) off-diagonal elements of the unit bidiagonal factor U or L from the factorization of A, as computed by Dpttrf.

anorm is the 1-norm of the original matrix A.

work must have length n, otherwise Dptcon will panic.

Dptsv computes the solution to system of linear equations

A * X = B

where A is an n×n symmetric positive definite tridiagonal matrix, and X and B are n×nrhs matrices. A is factored as A = L*D*Lᵀ, and the factored form of A is then used to solve the system of equations.

On entry, d contains the n diagonal elements of A and e contains the (n-1) subdiagonal elements of A. On return, d contains the n diagonal elements of the diagonal matrix D from the factorization A = L*D*Lᵀ and e contains the (n-1) subdiagonal elements of the unit bidiagonal factor L.

Dptsv returns whether the solution X has been successfully computed.

Dpttrf computes the L*D*Lᵀ factorization of an n×n symmetric positive definite tridiagonal matrix A and returns whether the factorization was successful.

On entry, d and e contain the n diagonal and (n-1) subdiagonal elements, respectively, of A.

On return, d contains the n diagonal elements of the diagonal matrix D and e contains the (n-1) subdiagonal elements of the unit bidiagonal matrix L.

Dpttrs solves a tridiagonal system of the form

A * X = B

using the L*D*Lᵀ factorization of A computed by Dpttrf. D is a diagonal matrix specified in d, L is a unit bidiagonal matrix whose subdiagonal is specified in e, and X and B are n×nrhs matrices.

Drscl multiplies the vector x by 1/a being careful to avoid overflow or underflow where possible.

Drscl is an internal routine. It is exported for testing purposes.

Dsteqr computes the eigenvalues and optionally the eigenvectors of a symmetric tridiagonal matrix using the implicit QL or QR method. The eigenvectors of a full or band symmetric matrix can also be found if Dsytrd, Dsptrd, or Dsbtrd have been used to reduce this matrix to tridiagonal form.

d, on entry, contains the diagonal elements of the tridiagonal matrix. On exit, d contains the eigenvalues in ascending order. d must have length n and Dsteqr will panic otherwise.

e, on entry, contains the off-diagonal elements of the tridiagonal matrix on entry, and is overwritten during the call to Dsteqr. e must have length n-1 and Dsteqr will panic otherwise.

z, on entry, contains the n×n orthogonal matrix used in the reduction to tridiagonal form if compz == lapack.EVOrig. On exit, if compz == lapack.EVOrig, z contains the orthonormal eigenvectors of the original symmetric matrix, and if compz == lapack.EVTridiag, z contains the orthonormal eigenvectors of the symmetric tridiagonal matrix. z is not used if compz == lapack.EVCompNone.

work must have length at least max(1, 2*n-2) if the eigenvectors are computed, and Dsteqr will panic otherwise.

Dsteqr is an internal routine. It is exported for testing purposes.

Dsterf computes all eigenvalues of a symmetric tridiagonal matrix using the Pal-Walker-Kahan variant of the QL or QR algorithm.

d contains the diagonal elements of the tridiagonal matrix on entry, and contains the eigenvalues in ascending order on exit. d must have length at least n, or Dsterf will panic.

e contains the off-diagonal elements of the tridiagonal matrix on entry, and is overwritten during the call to Dsterf. e must have length of at least n-1 or Dsterf will panic.

Dsterf is an internal routine. It is exported for testing purposes.

Dsyev computes all eigenvalues and, optionally, the eigenvectors of a real symmetric matrix A.

w contains the eigenvalues in ascending order upon return. w must have length at least n, and Dsyev will panic otherwise.

On entry, a contains the elements of the symmetric matrix A in the triangular portion specified by uplo. If jobz == lapack.EVCompute, a contains the orthonormal eigenvectors of A on exit, otherwise jobz must be lapack.EVNone and on exit the specified triangular region is overwritten.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= 3*n-1, and Dsyev will panic otherwise. The amount of blocking is limited by the usable length. If lwork == -1, instead of computing Dsyev the optimal work length is stored into work[0].

Dsytd2 reduces a symmetric n×n matrix A to symmetric tridiagonal form T by an orthogonal similarity transformation

Qᵀ * A * Q = T

On entry, the matrix is contained in the specified triangle of a. On exit, if uplo == blas.Upper, the diagonal and first super-diagonal of a are overwritten with the elements of T. The elements above the first super-diagonal are overwritten with the elementary reflectors that are used with the elements written to tau in order to construct Q. If uplo == blas.Lower, the elements are written in the lower triangular region.

d must have length at least n. e and tau must have length at least n-1. Dsytd2 will panic if these sizes are not met.

Q is represented as a product of elementary reflectors. If uplo == blas.Upper

Q = H_{n-2} * ... * H_1 * H_0

and if uplo == blas.Lower

Q = H_0 * H_1 * ... * H_{n-2}

where

H_i = I - tau * v * vᵀ

where tau is stored in tau[i], and v is stored in a.

If uplo == blas.Upper, v[0:i-1] is stored in A[0:i-1,i+1], v[i] = 1, and v[i+1:] = 0. The elements of a are

[ d   e  v2  v3  v4]
[     d   e  v3  v4]
[         d   e  v4]
[             d   e]
[                 d]

If uplo == blas.Lower, v[0:i+1] = 0, v[i+1] = 1, and v[i+2:] is stored in A[i+2:n,i]. The elements of a are

[ d                ]
[ e   d            ]
[v1   e   d        ]
[v1  v2   e   d    ]
[v1  v2  v3   e   d]

Dsytd2 is an internal routine. It is exported for testing purposes.

Dsytrd reduces a symmetric n×n matrix A to symmetric tridiagonal form by an orthogonal similarity transformation

Qᵀ * A * Q = T

where Q is an orthonormal matrix and T is symmetric and tridiagonal.

On entry, a contains the elements of the input matrix in the triangle specified by uplo. On exit, the diagonal and sub/super-diagonal are overwritten by the corresponding elements of the tridiagonal matrix T. The remaining elements in the triangle, along with the array tau, contain the data to construct Q as the product of elementary reflectors.

If uplo == blas.Upper, Q is constructed with

Q = H_{n-2} * ... * H_1 * H_0

where

H_i = I - tau_i * v * vᵀ

v is constructed as v[i+1:n] = 0, v[i] = 1, v[0:i-1] is stored in A[0:i-1, i+1]. The elements of A are

[ d   e  v1  v2  v3]
[     d   e  v2  v3]
[         d   e  v3]
[             d   e]
[                 e]

If uplo == blas.Lower, Q is constructed with

Q = H_0 * H_1 * ... * H_{n-2}

where

H_i = I - tau_i * v * vᵀ

v is constructed as v[0:i+1] = 0, v[i+1] = 1, v[i+2:n] is stored in A[i+2:n, i]. The elements of A are

[ d                ]
[ e   d            ]
[v0   e   d        ]
[v0  v1   e   d    ]
[v0  v1  v2   e   d]

d must have length n, and e and tau must have length n-1. Dsytrd will panic if these conditions are not met.

work is temporary storage, and lwork specifies the usable memory length. At minimum, lwork >= 1, and Dsytrd will panic otherwise. The amount of blocking is limited by the usable length. If lwork == -1, instead of computing Dsytrd the optimal work length is stored into work[0].

Dsytrd is an internal routine. It is exported for testing purposes.

Dtbtrs solves a triangular system of the form

A * X = B   if trans == blas.NoTrans
Aᵀ * X = B  if trans == blas.Trans or blas.ConjTrans

where A is an n×n triangular band matrix with kd super- or subdiagonals, and B is an n×nrhs matrix.

Dtbtrs returns whether A is non-singular. If A is singular, no solution X is computed.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dtgsja(jobU, jobV, jobQ [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[GSVDJob](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#GSVDJob), m, p, n, k, l [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), tola, tolb [float64](https://pkg.go.dev/builtin#float64), alpha, beta, u [][float64](https://pkg.go.dev/builtin#float64), ldu [int](https://pkg.go.dev/builtin#int), v [][float64](https://pkg.go.dev/builtin#float64), ldv [int](https://pkg.go.dev/builtin#int), q [][float64](https://pkg.go.dev/builtin#float64), ldq [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64)) (cycles [int](https://pkg.go.dev/builtin#int), ok [bool](https://pkg.go.dev/builtin#bool))

Dtgsja computes the generalized singular value decomposition (GSVD) of two real upper triangular or trapezoidal matrices A and B.

A and B have the following forms, which may be obtained by the preprocessing subroutine Dggsvp from a general m×n matrix A and p×n matrix B:

          n-k-l  k    l
A =    k [  0   A12  A13 ] if m-k-l >= 0;
       l [  0    0   A23 ]
   m-k-l [  0    0    0  ]

          n-k-l  k    l
A =    k [  0   A12  A13 ] if m-k-l < 0;
     m-k [  0    0   A23 ]

          n-k-l  k    l
B =    l [  0    0   B13 ]
     p-l [  0    0    0  ]

where the k×k matrix A12 and l×l matrix B13 are non-singular upper triangular. A23 is l×l upper triangular if m-k-l >= 0, otherwise A23 is (m-k)×l upper trapezoidal.

On exit,

Uᵀ*A*Q = D1*[ 0 R ], Vᵀ*B*Q = D2*[ 0 R ],

where U, V and Q are orthogonal matrices. R is a non-singular upper triangular matrix, and D1 and D2 are diagonal matrices, which are of the following structures:

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

R = [ R11 R12 R13 ] is stored in A[0:m, n-k-l:n]
    [  0  R22 R23 ]

and R33 is stored in

B[m-k:l, n+m-k-l:n] on exit.

The computation of the orthogonal transformation matrices U, V or Q is optional. These matrices may either be formed explicitly, or they may be post-multiplied into input matrices U1, V1, or Q1.

Dtgsja essentially uses a variant of Kogbetliantz algorithm to reduce min(l,m-k)×l triangular or trapezoidal matrix A23 and l×l matrix B13 to the form:

U1ᵀ*A13*Q1 = C1*R1; V1ᵀ*B13*Q1 = S1*R1,

where U1, V1 and Q1 are orthogonal matrices. C1 and S1 are diagonal matrices satisfying

C1^2 + S1^2 = I,

and R1 is an l×l non-singular upper triangular matrix.

jobU, jobV and jobQ are options for computing the orthogonal matrices. The behavior is as follows

jobU == lapack.GSVDU        Compute orthogonal matrix U
jobU == lapack.GSVDUnit     Use unit-initialized matrix
jobU == lapack.GSVDNone     Do not compute orthogonal matrix.

The behavior is the same for jobV and jobQ with the exception that instead of lapack.GSVDU these accept lapack.GSVDV and lapack.GSVDQ respectively. The matrices U, V and Q must be m×m, p×p and n×n respectively unless the relevant job parameter is lapack.GSVDNone.

k and l specify the sub-blocks in the input matrices A and B:

A23 = A[k:min(k+l,m), n-l:n) and B13 = B[0:l, n-l:n]

of A and B, whose GSVD is going to be computed by Dtgsja.

tola and tolb are the convergence criteria for the Jacobi-Kogbetliantz iteration procedure. Generally, they are the same as used in the preprocessing step, for example,

tola = max(m, n)*norm(A)*eps,
tolb = max(p, n)*norm(B)*eps,

where eps is the machine epsilon.

work must have length at least 2*n, otherwise Dtgsja will panic.

alpha and beta must have length n or Dtgsja will panic. On exit, alpha and beta contain the generalized singular value pairs of A and B

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

On exit, A[n-k:n, 0:min(k+l,m)] contains the triangular matrix R or part of R and if necessary, B[m-k:l, n+m-k-l:n] contains a part of R.

Dtgsja returns whether the routine converged and the number of iteration cycles that were run.

Dtgsja is an internal routine. It is exported for testing purposes.

Dtrcon estimates the reciprocal of the condition number of a triangular matrix A. The condition number computed may be based on the 1-norm or the ∞-norm.

work is a temporary data slice of length at least 3*n and Dtrcon will panic otherwise.

iwork is a temporary data slice of length at least n and Dtrcon will panic otherwise.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dtrevc3(side [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[EVSide](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#EVSide), howmny [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[EVHowMany](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#EVHowMany), selected [][bool](https://pkg.go.dev/builtin#bool), n [int](https://pkg.go.dev/builtin#int), t [][float64](https://pkg.go.dev/builtin#float64), ldt [int](https://pkg.go.dev/builtin#int), vl [][float64](https://pkg.go.dev/builtin#float64), ldvl [int](https://pkg.go.dev/builtin#int), vr [][float64](https://pkg.go.dev/builtin#float64), ldvr [int](https://pkg.go.dev/builtin#int), mm [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64), lwork [int](https://pkg.go.dev/builtin#int)) (m [int](https://pkg.go.dev/builtin#int))

Dtrevc3 computes some or all of the right and/or left eigenvectors of an n×n upper quasi-triangular matrix T in Schur canonical form. Matrices of this type are produced by the Schur factorization of a real general matrix A

A = Q T Qᵀ,

as computed by Dhseqr.

The right eigenvector x of T corresponding to an eigenvalue λ is defined by

T x = λ x,

and the left eigenvector y is defined by

yᵀ T = λ yᵀ.

The eigenvalues are read directly from the diagonal blocks of T.

This routine returns the matrices X and/or Y of right and left eigenvectors of T, or the products Q*X and/or Q*Y, where Q is an input matrix. If Q is the orthogonal factor that reduces a matrix A to Schur form T, then Q*X and Q*Y are the matrices of right and left eigenvectors of A.

If side == lapack.EVRight, only right eigenvectors will be computed. If side == lapack.EVLeft, only left eigenvectors will be computed. If side == lapack.EVBoth, both right and left eigenvectors will be computed. For other values of side, Dtrevc3 will panic.

If howmny == lapack.EVAll, all right and/or left eigenvectors will be computed. If howmny == lapack.EVAllMulQ, all right and/or left eigenvectors will be computed and multiplied from left by the matrices in VR and/or VL. If howmny == lapack.EVSelected, right and/or left eigenvectors will be computed as indicated by selected. For other values of howmny, Dtrevc3 will panic.

selected specifies which eigenvectors will be computed. It must have length n if howmny == lapack.EVSelected, and it is not referenced otherwise. If w_j is a real eigenvalue, the corresponding real eigenvector will be computed if selected[j] is true. If w_j and w_{j+1} are the real and imaginary parts of a complex eigenvalue, the corresponding complex eigenvector is computed if either selected[j] or selected[j+1] is true, and on return selected[j] will be set to true and selected[j+1] will be set to false.

VL and VR are n×mm matrices. If howmny is lapack.EVAll or lapack.AllEVMulQ, mm must be at least n. If howmny is lapack.EVSelected, mm must be large enough to store the selected eigenvectors. Each selected real eigenvector occupies one column and each selected complex eigenvector occupies two columns. If mm is not sufficiently large, Dtrevc3 will panic.

On entry, if howmny is lapack.EVAllMulQ, it is assumed that VL (if side is lapack.EVLeft or lapack.EVBoth) contains an n×n matrix QL, and that VR (if side is lapack.EVRight or lapack.EVBoth) contains an n×n matrix QR. QL and QR are typically the orthogonal matrix Q of Schur vectors returned by Dhseqr.

On return, if side is lapack.EVLeft or lapack.EVBoth, VL will contain:

if howmny == lapack.EVAll,      the matrix Y of left eigenvectors of T,
if howmny == lapack.EVAllMulQ,  the matrix Q*Y,
if howmny == lapack.EVSelected, the left eigenvectors of T specified by
                                selected, stored consecutively in the
                                columns of VL, in the same order as their
                                eigenvalues.

VL is not referenced if side == lapack.EVRight.

On return, if side is lapack.EVRight or lapack.EVBoth, VR will contain:

if howmny == lapack.EVAll,      the matrix X of right eigenvectors of T,
if howmny == lapack.EVAllMulQ,  the matrix Q*X,
if howmny == lapack.EVSelected, the left eigenvectors of T specified by
                                selected, stored consecutively in the
                                columns of VR, in the same order as their
                                eigenvalues.

VR is not referenced if side == lapack.EVLeft.

Complex eigenvectors corresponding to a complex eigenvalue are stored in VL and VR in two consecutive columns, the first holding the real part, and the second the imaginary part.

Each eigenvector will be normalized so that the element of largest magnitude has magnitude 1. Here the magnitude of a complex number (x,y) is taken to be |x| + |y|.

work must have length at least lwork and lwork must be at least max(1,3*n), otherwise Dtrevc3 will panic. For optimum performance, lwork should be at least n+2*n*nb, where nb is the optimal blocksize.

If lwork == -1, instead of performing Dtrevc3, the function only estimates the optimal workspace size based on n and stores it into work[0].

Dtrevc3 returns the number of columns in VL and/or VR actually used to store the eigenvectors.

Dtrevc3 is an internal routine. It is exported for testing purposes.

func (impl [Implementation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack/gonum#Implementation)) Dtrexc(compq [lapack](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack).[UpdateSchurComp](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/lapack#UpdateSchurComp), n [int](https://pkg.go.dev/builtin#int), t [][float64](https://pkg.go.dev/builtin#float64), ldt [int](https://pkg.go.dev/builtin#int), q [][float64](https://pkg.go.dev/builtin#float64), ldq [int](https://pkg.go.dev/builtin#int), ifst, ilst [int](https://pkg.go.dev/builtin#int), work [][float64](https://pkg.go.dev/builtin#float64)) (ifstOut, ilstOut [int](https://pkg.go.dev/builtin#int), ok [bool](https://pkg.go.dev/builtin#bool))

Dtrexc reorders the real Schur factorization of a n×n real matrix

A = Q*T*Qᵀ

so that the diagonal block of T with row index ifst is moved to row ilst.

On entry, T must be in Schur canonical form, that is, block upper triangular with 1×1 and 2×2 diagonal blocks; each 2×2 diagonal block has its diagonal elements equal and its off-diagonal elements of opposite sign.

On return, T will be reordered by an orthogonal similarity transformation Z as Zᵀ*T*Z, and will be again in Schur canonical form.

If compq is lapack.UpdateSchur, on return the matrix Q of Schur vectors will be updated by post-multiplying it with Z. If compq is lapack.UpdateSchurNone, the matrix Q is not referenced and will not be updated. For other values of compq Dtrexc will panic.

ifst and ilst specify the reordering of the diagonal blocks of T. The block with row index ifst is moved to row ilst, by a sequence of transpositions between adjacent blocks.

If ifst points to the second row of a 2×2 block, ifstOut will point to the first row, otherwise it will be equal to ifst.

ilstOut will point to the first row of the block in its final position. If ok is true, ilstOut may differ from ilst by +1 or -1.

It must hold that

0 <= ifst < n, and  0 <= ilst < n,

otherwise Dtrexc will panic.

If ok is false, two adjacent blocks were too close to swap because the problem is very ill-conditioned. T may have been partially reordered, and ilstOut will point to the first row of the block at the position to which it has been moved.

work must have length at least n, otherwise Dtrexc will panic.

Dtrexc is an internal routine. It is exported for testing purposes.

Dtrti2 computes the inverse of a triangular matrix, storing the result in place into a. This is the BLAS level 2 version of the algorithm.

Dtrti2 is an internal routine. It is exported for testing purposes.

Dtrtri computes the inverse of a triangular matrix, storing the result in place into a. This is the BLAS level 3 version of the algorithm which builds upon Dtrti2 to operate on matrix blocks instead of only individual columns.

Dtrtri will not perform the inversion if the matrix is singular, and returns a boolean indicating whether the inversion was successful.

Dtrtrs solves a triangular system of the form A * X = B or Aᵀ * X = B. Dtrtrs returns whether the solve completed successfully. If A is singular, no solve is performed.

Iladlc scans a matrix for its last non-zero column. Returns -1 if the matrix is all zeros.

Iladlc is an internal routine. It is exported for testing purposes.

Iladlr scans a matrix for its last non-zero row. Returns -1 if the matrix is all zeros.

Iladlr is an internal routine. It is exported for testing purposes.

Ilaenv returns algorithm tuning parameters for the algorithm given by the input string. ispec specifies the parameter to return:

1: The optimal block size for a blocked algorithm.
2: The minimum block size for a blocked algorithm.
3: The block size of unprocessed data at which a blocked algorithm should
   crossover to an unblocked version.
4: The number of shifts.
5: The minimum column dimension for blocking to be used.
6: The crossover point for SVD (to use QR factorization or not).
7: The number of processors.
8: The crossover point for multi-shift in QR and QZ methods for non-symmetric eigenvalue problems.
9: Maximum size of the subproblems in divide-and-conquer algorithms.
10: ieee infinity and NaN arithmetic can be trusted not to trap.
11: ieee infinity arithmetic can be trusted not to trap.
12...16: parameters for Dhseqr and related functions. See Iparmq for more
         information.

Ilaenv is an internal routine. It is exported for testing purposes.

Iparmq returns problem and machine dependent parameters useful for Dhseqr and related subroutines for eigenvalue problems.

ispec specifies the parameter to return:

12: Crossover point between Dlahqr and Dlaqr0. Will be at least 11.
13: Deflation window size.
14: Nibble crossover point. Determines when to skip a multi-shift QR sweep.
15: Number of simultaneous shifts in a multishift QR iteration.
16: Select structured matrix multiply.

For other values of ispec Iparmq will panic.

name is the name of the calling function. name must be in uppercase but this is not checked.

opts is not used and exists for future use.

n is the order of the Hessenberg matrix H.

ilo and ihi specify the block [ilo:ihi+1,ilo:ihi+1] that is being processed.

lwork is the amount of workspace available.

Except for ispec input parameters are not checked.

Iparmq is an internal routine. It is exported for testing purposes.
