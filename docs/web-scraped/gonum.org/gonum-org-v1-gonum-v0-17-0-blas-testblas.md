# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas

Title: testblas package - gonum.org/v1/gonum/blas/testblas - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas

Markdown Content:
Package testblas provides tests for blas implementations.

*   [Constants](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#pkg-constants)
*   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#pkg-variables)
*   [func DasumTest(t *testing.T, blasser Dasumer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DasumTest)
*   [func DaxpyTest(t *testing.T, d Daxpyer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyTest)
*   [func DcopyTest(t *testing.T, d Dcopier)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DcopyTest)
*   [func DdotTest(t *testing.T, d Ddotter)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DdotTest)
*   [func DgbmvTest(t *testing.T, blasser Dgbmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgbmvTest)
*   [func DgemmBenchmark(b *testing.B, dgemm Dgemmer, m, n, k int, tA, tB blas.Transpose)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemmBenchmark)
*   [func DgemvBenchmark(b *testing.B, impl Dgemver, tA blas.Transpose, m, n, incX, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvBenchmark)
*   [func DgemvTest(t *testing.T, blasser Dgemver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvTest)
*   [func DgerBenchmark(b *testing.B, impl Dgerer, m, n, incX, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgerBenchmark)
*   [func DgerTest(t *testing.T, blasser Dgerer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgerTest)
*   [func Dnrm2Test(t *testing.T, blasser Dnrm2er)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dnrm2Test)
*   [func DrotTest(t *testing.T, d Droter)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotTest)
*   [func DrotgTest(t *testing.T, d Drotger, skipExtreme bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotgTest)
*   [func DrotmTest(t *testing.T, d Drotmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmTest)
*   [func DrotmgTest(t *testing.T, d Drotmger)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmgTest)
*   [func DsbmvTest(t *testing.T, blasser Dsbmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DsbmvTest)
*   [func DscalTest(t *testing.T, blasser Dscaler)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DscalTest)
*   [func DspmvTest(t *testing.T, blasser Dspmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DspmvTest)
*   [func Dspr2Test(t *testing.T, blasser Dspr2er)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dspr2Test)
*   [func DsprTest(t *testing.T, blasser Dsprer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DsprTest)
*   [func DswapTest(t *testing.T, d Dswapper)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DswapTest)
*   [func DsymmTest(t *testing.T, blasser Dsymmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DsymmTest)
*   [func DsymvTest(t *testing.T, blasser Dsymver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DsymvTest)
*   [func Dsyr2Test(t *testing.T, blasser Dsyr2er)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsyr2Test)
*   [func Dsyr2kTest(t *testing.T, blasser Dsyr2ker)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsyr2kTest)
*   [func DsyrTest(t *testing.T, blasser Dsyrer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DsyrTest)
*   [func DsyrkTest(t *testing.T, blasser Dsyker)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DsyrkTest)
*   [func DtbmvTest(t *testing.T, blasser Dtbmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtbmvTest)
*   [func DtbsvTest(t *testing.T, blasser Dtbsver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtbsvTest)
*   [func DtpmvTest(t *testing.T, blasser Dtpmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtpmvTest)
*   [func DtpsvTest(t *testing.T, blasser Dtpsver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtpsvTest)
*   [func DtrmmTest(t *testing.T, blasser Dtrmmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtrmmTest)
*   [func DtrmvBenchmark(b *testing.B, dtrmv Dtrmver, n, lda, incX int, ul blas.Uplo, tA blas.Transpose, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtrmvBenchmark)
*   [func DtrmvTest(t *testing.T, blasser Dtrmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtrmvTest)
*   [func DtrsmTest(t *testing.T, impl Dtrsmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtrsmTest)
*   [func DtrsvTest(t *testing.T, blasser Dtrsver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtrsvTest)
*   [func DtxmvTest(t *testing.T, blasser Dtxmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DtxmvTest)
*   [func DzasumTest(t *testing.T, impl Dzasumer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DzasumTest)
*   [func Dznrm2Test(t *testing.T, impl Dznrm2er)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dznrm2Test)
*   [func IdamaxTest(t *testing.T, blasser Idamaxer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#IdamaxTest)
*   [func IzamaxTest(t *testing.T, impl Izamaxer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#IzamaxTest)
*   [func SgerBenchmark(b *testing.B, blasser Sgerer, m, n, incX, incY int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#SgerBenchmark)
*   [func TestDgemm(t *testing.T, blasser Dgemmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#TestDgemm)
*   [func ZaxpyTest(t *testing.T, impl Zaxpyer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZaxpyTest)
*   [func ZcopyTest(t *testing.T, impl Zcopyer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZcopyTest)
*   [func ZdotcTest(t *testing.T, impl Zdotcer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZdotcTest)
*   [func ZdotuTest(t *testing.T, impl Zdotuer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZdotuTest)
*   [func ZdscalTest(t *testing.T, impl Zdscaler)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZdscalTest)
*   [func ZgbmvTest(t *testing.T, impl Zgbmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZgbmvTest)
*   [func ZgemmTest(t *testing.T, impl Zgemmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZgemmTest)
*   [func ZgemvTest(t *testing.T, impl Zgemver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZgemvTest)
*   [func ZgercTest(t *testing.T, impl Zgercer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZgercTest)
*   [func ZgeruTest(t *testing.T, impl Zgeruer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZgeruTest)
*   [func ZhbmvTest(t *testing.T, impl Zhbmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZhbmvTest)
*   [func ZhemmTest(t *testing.T, impl Zhemmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZhemmTest)
*   [func ZhemvTest(t *testing.T, impl Zhemver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZhemvTest)
*   [func Zher2Test(t *testing.T, impl Zher2er)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zher2Test)
*   [func Zher2kTest(t *testing.T, impl Zher2ker)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zher2kTest)
*   [func ZherTest(t *testing.T, impl Zherer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZherTest)
*   [func ZherkTest(t *testing.T, impl Zherker)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZherkTest)
*   [func ZhpmvTest(t *testing.T, impl Zhpmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZhpmvTest)
*   [func Zhpr2Test(t *testing.T, impl Zhpr2er)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhpr2Test)
*   [func ZhprTest(t *testing.T, impl Zhprer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZhprTest)
*   [func ZscalTest(t *testing.T, impl Zscaler)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZscalTest)
*   [func ZswapTest(t *testing.T, impl Zswaper)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZswapTest)
*   [func ZsymmTest(t *testing.T, impl Zsymmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZsymmTest)
*   [func Zsyr2kTest(t *testing.T, impl Zsyr2ker)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zsyr2kTest)
*   [func ZsyrkTest(t *testing.T, impl Zsyrker)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZsyrkTest)
*   [func ZtbmvTest(t *testing.T, impl Ztbmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtbmvTest)
*   [func ZtbsvTest(t *testing.T, impl Ztbsver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtbsvTest)
*   [func ZtpmvTest(t *testing.T, impl Ztpmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtpmvTest)
*   [func ZtpsvTest(t *testing.T, impl Ztpsver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtpsvTest)
*   [func ZtrmmTest(t *testing.T, impl Ztrmmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtrmmTest)
*   [func ZtrmvTest(t *testing.T, impl Ztrmver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtrmvTest)
*   [func ZtrsmTest(t *testing.T, impl Ztrsmer)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtrsmTest)
*   [func ZtrsvTest(t *testing.T, impl Ztrsver)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#ZtrsvTest)
*   [type DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase)
*   [type DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer)
*   [type Dasumer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dasumer)
*   [type DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase)
*   [type Daxpyer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Daxpyer)
*   [type Dcopier](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dcopier)
*   [type Ddotter](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ddotter)
*   [type Dgbmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dgbmver)
*   [type DgemmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemmCase)
*   [type Dgemmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dgemmer)
*   [type DgemvCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvCase)
*   [type DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase)
*   [type Dgemver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dgemver)
*   [type Dgerer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dgerer)
*   [type Dnrm2er](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dnrm2er)
*   [type DoubleOneVectorCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DoubleOneVectorCase)
*   [type DoubleTwoVectorCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DoubleTwoVectorCase)
*   [type DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase)
*   [type Droter](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Droter)
*   [type DrotgTestStruct](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotgTestStruct)
*   [type Drotger](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Drotger)
*   [type DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase)
*   [type Drotmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Drotmer)
*   [type Drotmger](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Drotmger)
*   [type Dsbmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsbmver)
*   [type Dscaler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dscaler)
*   [type Dspmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dspmver)
*   [type Dspr2er](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dspr2er)
*   [type Dsprer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsprer)
*   [type Dswapper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dswapper)
*   [type Dsyker](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsyker)
*   [type Dsymmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsymmer)
*   [type Dsymver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsymver)
*   [type Dsyr2er](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsyr2er)
*   [type Dsyr2ker](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsyr2ker)
*   [type Dsyrer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dsyrer)
*   [type Dtbmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtbmver)
*   [type Dtbsver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtbsver)
*   [type Dtpmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtpmver)
*   [type Dtpsver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtpsver)
*   [type Dtrmmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtrmmer)
*   [type Dtrmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtrmver)
*   [type Dtrsmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtrsmer)
*   [type Dtrsver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtrsver)
*   [type Dtxmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dtxmver)
*   [type Dzasumer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dzasumer)
*   [type Dznrm2er](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dznrm2er)
*   [type Idamaxer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Idamaxer)
*   [type Izamaxer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Izamaxer)
*   [type Sgerer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Sgerer)
*   [type Zaxpyer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zaxpyer)
*   [type Zcopyer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zcopyer)
*   [type Zdotcer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zdotcer)
*   [type Zdotuer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zdotuer)
*   [type Zdscaler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zdscaler)
*   [type Zgbmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zgbmver)
*   [type Zgemmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zgemmer)
*   [type Zgemver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zgemver)
*   [type Zgercer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zgercer)
*   [type Zgeruer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zgeruer)
*   [type Zhbmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhbmver)
*   [type Zhemmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhemmer)
*   [type Zhemver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhemver)
*   [type Zher2er](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zher2er)
*   [type Zher2ker](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zher2ker)
*   [type Zherer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zherer)
*   [type Zherker](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zherker)
*   [type Zhpmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhpmver)
*   [type Zhpr2er](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhpr2er)
*   [type Zhprer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhprer)
*   [type Zscaler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zscaler)
*   [type Zswaper](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zswaper)
*   [type Zsymmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zsymmer)
*   [type Zsyr2ker](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zsyr2ker)
*   [type Zsyrker](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zsyrker)
*   [type Ztbmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztbmver)
*   [type Ztbsver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztbsver)
*   [type Ztpmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztpmver)
*   [type Ztpsver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztpsver)
*   [type Ztrmmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztrmmer)
*   [type Ztrmver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztrmver)
*   [type Ztrsmer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztrsmer)
*   [type Ztrsver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Ztrsver)

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/blas/testblas/benchsize.go#L7)

const (
 SmallMat = 10  MediumMat = 100  LargeMat = 1000  HugeMat = 10000 )

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/blas/testblas/dgemm.go#L26)

var DgemmCases = [][DgemmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemmCase){ 
	{
		
	},
	{
		
	},
	{
		
	},
	{
		
	},
	{
		
	},
	{
		
	},
	{
		
	},
}

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/blas/testblas/dgemv.go#L35)

var DgemvCases = [][DgemvCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvCase){ 	{
		Name: "M_gt_N_Inc1_NoTrans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
			{1, 1, 2},
			{9, 2, 5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_gt_N_Inc1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
			{1, 1, 2},
			{9, 2, 5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_eq_N_Inc1_NoTrans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_eq_N_Inc1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
		},
		
	},
	{
		Name: "M_lt_N_Inc1_NoTrans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1, 10, 7},
			{9.6, 3.5, 9.1, -2, 9},
			{10, 7, 3, 1, -5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},

			{
				
			},
		},
		
	},
	{
		Name: "M_lt_N_Inc1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1, 10, 7},
			{9.6, 3.5, 9.1, -2, 9},
			{10, 7, 3, 1, -5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
		},
		
	},
	{
		Name: "M_gt_N_Part1_NoTrans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
			{1, 1, 2},
			{9, 2, 5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_gt_N_Part1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
			{1, 1, 2},
			{9, 2, 5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_gt_N_IncNot1_NoTrans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
			{1, 1, 2},
			{9, 2, 5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_gt_N_IncNot1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
			{1, 1, 2},
			{9, 2, 5},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_eq_N_IncNot1_NoTrans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_eq_N_IncNot1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1},
			{9.6, 3.5, 9.1},
			{10, 7, 3},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_lt_N_IncNot1_NoTrans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1, 10, 11},
			{9.6, 3.5, 9.1, -3, -2},
			{10, 7, 3, -7, -4},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_lt_N_IncNot1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1, 10, 11},
			{9.6, 3.5, 9.1, -3, -2},
			{10, 7, 3, -7, -4},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
	{
		Name: "M_eq_N_Lg_IncNot1_Trans",

		A: [][][float64](https://pkg.go.dev/builtin#float64){
			{4.1, 6.2, 8.1, 2.5, 3.3, 7.4, 9.3},
			{9.6, 3.5, 9.1, 1.2, 5.4, 4.8, 8.7},
			{10, 7, 3, 2, 4, 1, 12},
			{9.6, 3.5, 9.1, 1.2, 5.4, 4.8, 8.7},
			{4.1, 6.2, 8.1, 2.5, 3.3, 7.4, 9.3},
			{10, 7, 3, 2, 4, 1, 12},
			{9.6, 3.5, 9.1, 1.2, 5.4, 4.8, 8.7},
		},

		Subcases: [][DgemvSubcase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DgemvSubcase){
			{
				
			},
			{
				
			},
			{
				
			},
			{
				
			},
		},
		
	},
}

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/blas/testblas/level1double.go#L35)

var DoubleOneVectorCases = [][DoubleOneVectorCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DoubleOneVectorCase){ 	{
		Name:   "AllPositive",
		X:      [][float64](https://pkg.go.dev/builtin#float64){6, 5, 4, 2, 6},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  23,
		Dnrm2:  10.81665382639196787935766380241148783875388972153573863813135,
		Idamax: 0,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0},
			},
			{
				Alpha: 1,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){6, 5, 4, 2, 6},
			},
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-12, -10, -8, -4, -12},
			},
		},
	},
	{
		Name:   "LeadingZero",
		X:      [][float64](https://pkg.go.dev/builtin#float64){0, 1},
		Incx:   1,
		N:      2,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  1,
		Dnrm2:  1,
		Idamax: 1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, 0},
			},
			{
				Alpha: 1,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, 1},
			},
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, -2},
			},
		},
	},
	{
		Name:   "MaxInMiddle",
		X:      [][float64](https://pkg.go.dev/builtin#float64){6, 5, 9, 0, 6},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  26,
		Dnrm2:  13.34166406412633371248943627250846646911846482744007727141318,
		Idamax: 2,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-12, -10, -18, 0, -12},
			},
		},
	},
	{
		Name:   "MaxAtEnd",
		X:      [][float64](https://pkg.go.dev/builtin#float64){6, 5, -9, 0, 10},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  30,
		Dnrm2:  15.55634918610404553681857596630667886426639062914642880494347,
		Idamax: 4,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-12, -10, 18, 0, -20},
			},
		},
	},
	{
		Name:   "AllNegative",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, -5, -4, -2, -6},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  23,
		Dnrm2:  10.81665382639196787935766380241148783875388972153573863813135,
		Idamax: 0,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){12, 10, 8, 4, 12},
			},
		},
	},
	{
		Name:   "AllMixed",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  23,
		Dnrm2:  10.81665382639196787935766380241148783875388972153573863813135,
		Idamax: 0,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){12, -10, -8, 4, 12},
			},
		},
	},
	{
		Name:   "ZeroN",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:   1,
		N:      0,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:   "OneN",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:   1,
		N:      1,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  6,
		Dnrm2:  6,
		Idamax: 0,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){12, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:   "PositiveExactInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 10, -2, -5},
		Incx:   2,
		N:      3,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  21,
		Dnrm2:  12.68857754044952038019377274608948979173952662752515253090272,
		Idamax: 1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){12, 5, -20, -2, 10},
			},
		},
	},
	{
		Name:   "PositiveOffInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6, 8, 10, 11},
		Incx:   3,
		N:      3,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  18,
		Dnrm2:  11.83215956619923208513465658312323409683100246158868064575943,
		Idamax: 2,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){12, 5, 4, 4, -6, 8, -20, 11},
			},
		},
	},
	{
		Name:   "PositiveShortInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6, 8, 10, 11},
		Incx:   3,
		N:      2,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  8,
		Dnrm2:  6.324555320336758663997787088865437067439110278650433653715009,
		Idamax: 0,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){12, 5, 4, 4, -6, 8, 10, 11},
			},
		},
	},
	{
		Name:   "NegativeInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:   -1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:   "NegativeExactInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:   -2,
		N:      3,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:   "NegativeOffInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6, 8, 10, 11},
		Incx:   -3,
		N:      2,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6, 8, 10, 11},
			},
		},
	},
	{
		Name:   "NegativeShortInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6, 8, 10, 11},
		Incx:   -3,
		N:      2,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6, 8, 10, 11},
			},
		},
	},
	{
		Name:  "NegativeN",
		X:     [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:  2,
		N:     -5,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:  "ZeroInc",
		X:     [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:  0,
		N:     5,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:  "OutOfBounds",
		X:     [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:  2,
		N:     6,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:   "NegativeOutOfBounds",
		X:      [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
		Incx:   -2,
		N:      6,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-6, 5, 4, -2, -6},
			},
		},
	},
	{
		Name:   "NaN",
		X:      [][float64](https://pkg.go.dev/builtin#float64){[math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), 2.0},
		Incx:   1,
		N:      2,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Dnrm2:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Idamax: 0,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){[math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), -4.0},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, 0},
			},
		},
	},
	{
		Name:   "NaNInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){[math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), 2.0},
		Incx:   2,
		N:      2,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Dnrm2:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Idamax: 0,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){[math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), -4.0},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), 0},
			},
		},
	},
	{
		Name:   "Empty",
		X:      [][float64](https://pkg.go.dev/builtin#float64){},
		Incx:   1,
		N:      0,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
	},
	{
		Name:   "EmptyZeroInc",
		X:      [][float64](https://pkg.go.dev/builtin#float64){},
		Incx:   0,
		N:      0,
		Panic:  [true](https://pkg.go.dev/builtin#true),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
	},
	{
		Name:   "EmptyReverse",
		X:      [][float64](https://pkg.go.dev/builtin#float64){},
		Incx:   -1,
		N:      0,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  0,
		Dnrm2:  0,
		Idamax: -1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
	},
	{
		Name:   "MultiInf",
		X:      [][float64](https://pkg.go.dev/builtin#float64){5, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1), [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(-1), 8, 9},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1),
		Dnrm2:  [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1),
		Idamax: 1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-10, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(-1), [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1), -16, -18},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0},
			},
		},
	},
	{
		Name:   "NaNInf",
		X:      [][float64](https://pkg.go.dev/builtin#float64){5, [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(-1), 8, 9},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Dnrm2:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Idamax: 2,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-10, [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1), -16, -18},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0},
			},
		},
	},
	{
		Name:   "InfNaN",
		X:      [][float64](https://pkg.go.dev/builtin#float64){5, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(1), [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), 8, 9},
		Incx:   1,
		N:      5,
		Panic:  [false](https://pkg.go.dev/builtin#false),
		Dasum:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Dnrm2:  [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(),
		Idamax: 1,
		DscalCases: [][DScalCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DScalCase){
			{
				Alpha: -2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-10, [math](https://pkg.go.dev/math).[Inf](https://pkg.go.dev/math#Inf)(-1), [math](https://pkg.go.dev/math).[NaN](https://pkg.go.dev/math#NaN)(), -16, -18},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0},
			},
		},
	},
}

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/blas/testblas/level1double.go#L552)

var DoubleTwoVectorCases = [][DoubleTwoVectorCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DoubleTwoVectorCase){ 	{
		Name:  "UnitaryInc",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		Incx:  1,
		Incy:  1,
		N:     6,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 1,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){18, 13, -2, 10, 20, 4},
			},
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){28, 28, -8, 13, 34, 11},
			},
			{
				Alpha: -3,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-22, -47, 22, -2, -36, -24},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3},
			},
		},
		DdotAns: 110,
		DswapAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		},
		DcopyAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(0),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(0),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3},
			},
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){12.444023964292095, 12.749380282068351, -3.7473736752571014, 5.677251193294846, 15.224018588957296, 5.076299724034451},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){3.024279678886205, -8.151889500183792, 6.160940718590796, 5.076299724034451, -0.4788089421498931, -5.677251193294846},
			},
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(0.5 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(0.5 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-10, -15, 6, -3, -14, -7},
			},
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)([math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)([math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){-10, -15, 6, -3, -14, -7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-8, 2, -4, -7, -6, 3},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Identity](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Identity),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3},
				Name: "Neg2Flag",
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 13.7, -5.8, 2, 12, 6.6},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, 0.5, 1.4, 3.8, 4.4, -0.8},
				Name: "Neg1Flag",
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[OffDiagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#OffDiagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){1, 0.1, -0.1, 1},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){9.2, 15.2, -6.4, 2.3, 13.4, 7.3},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){9, -0.5, 3.4, 7.3, 7.4, -2.3},
				Name: "ZeroFlag",
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.5, -1, 1, 0.7},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){13, 5.5, 1, 8.5, 13, 0.5},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-4.4, -16.4, 8.8, 1.9, -9.8, -9.1},
				Name: "OneFlag",
			},
		},
	},
	{
		Name:  "UnitaryIncLong",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7, 8, -9, 10},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, 7, -6},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  1,
		Incy:  1,
		N:     6,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 1,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){18, 13, -2, 10, 20, 4, 7, -6},
			},
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){28, 28, -8, 13, 34, 11, 7, -6},
			},
			{
				Alpha: -3,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){-22, -47, 22, -2, -36, -24, 7, -6},
			},
			{
				Alpha: 0,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, 7, -6},
			},
		},
		DdotAns: 110,
		DswapAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, 8, -9, 10},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7, 7, -6},
		},
		DcopyAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7, 8, -9, 10},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7, 7, -6},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(0),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(0),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, 7, -6},
			},
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){12.444023964292095, 12.749380282068351, -3.7473736752571014, 5.677251193294846, 15.224018588957296, 5.076299724034451, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){3.024279678886205, -8.151889500183792, 6.160940718590796, 5.076299724034451, -0.4788089421498931, -5.677251193294846, 7, -6},
			},
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(0.5 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(0.5 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-10, -15, 6, -3, -14, -7, 7, -6},
			},
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)([math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)([math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi)),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){-10, -15, 6, -3, -14, -7, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-8, 2, -4, -7, -6, 3, 7, -6},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Identity](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Identity),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, 7, -6},
				Name: "Neg2Flag",
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 13.7, -5.8, 2, 12, 6.6, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, 0.5, 1.4, 3.8, 4.4, -0.8, 7, -6},
				Name: "Neg1Flag",
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[OffDiagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#OffDiagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){1, 0.1, -0.1, 1},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){9.2, 15.2, -6.4, 2.3, 13.4, 7.3, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){9, -0.5, 3.4, 7.3, 7.4, -2.3, 7, -6},
				Name: "ZeroFlag",
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.5, -1, 1, 0.7},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){13, 5.5, 1, 8.5, 13, 0.5, 8, -9, 10},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-4.4, -16.4, 8.8, 1.9, -9.8, -9.1, 7, -6},
				Name: "OneFlag",
			},
		},
	},
	{
		Name:  "PositiveInc",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  2,
		Incy:  3,
		N:     3,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){28, -2, 4, -5, 6, -3, 24, 10},
			},
		},
		DdotAns: -18,
		DswapAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){8, 15, 7, 3, -4, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, -2, 4, -6, 6, -3, 14, 10},
		},
		DcopyAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, -2, 4, -6, 6, -3, 14, 10},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){12.444023964292095, 15, -2.479518890035003, 3, 10.997835971550302, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){3.024279678886205, -2, 4, 8.879864079700745, 6, -3, -9.541886812516392, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 15, -6.1, 3, 13, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, -2, 4, 2.9, 6, -3, -0.6, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[OffDiagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#OffDiagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){1, 0.1, -0.1, 1},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){9.2, 15, -6.7, 3, 14.4, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){9, -2, 4, 6.4, 6, -3, -2.6, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.5, -1, 1, 0.7},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){13, 15, 4, 3, 3, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-4.4, -2, 4, 10.9, 6, -3, -16.8, 10},
			},
		},
	},
	{
		Name:  "NegativeInc",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  -2,
		Incy:  -3,
		N:     3,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){28, -2, 4, -5, 6, -3, 24, 10},
			},
		},
		DdotAns: -18,
		DswapAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){8, 15, 7, 3, -4, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, -2, 4, -6, 6, -3, 14, 10},
		},
		DcopyAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){10, -2, 4, -6, 6, -3, 14, 10},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){12.444023964292095, 15, -2.479518890035003, 3, 10.997835971550302, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){3.024279678886205, -2, 4, 8.879864079700745, 6, -3, -9.541886812516392, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 15, -6.1, 3, 13, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, -2, 4, 2.9, 6, -3, -0.6, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[OffDiagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#OffDiagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){1, 0.1, -0.1, 1},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){9.2, 15, -6.7, 3, 14.4, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){9, -2, 4, 6.4, 6, -3, -2.6, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.5, -1, 1, 0.7},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){13, 15, 4, 3, 3, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-4.4, -2, 4, 10.9, 6, -3, -16.8, 10},
			},
		},
	},
	{
		Name:  "MixedInc1",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  2,
		Incy:  -3,
		N:     3,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){36, -2, 4, -5, 6, -3, 16, 10},
			},
		},
		DdotAns: 30,
		DswapAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){-4, 15, 7, 3, 8, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){14, -2, 4, -6, 6, -3, 10, 10},
		},
		DcopyAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){14, -2, 4, -6, 6, -3, 10, 10},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){7.372604823403701, 15, -2.479518890035003, 3, 16.069255112438693, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){1.333806631923407, -2, 4, 8.879864079700745, 6, -3, -7.851413765553595, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){9.4, 15, -6.1, 3, 11.8, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5.4, -2, 4, 2.9, 6, -3, -1, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[OffDiagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#OffDiagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){1, 0.1, -0.1, 1},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10.4, 15, -6.7, 3, 13.2, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){9.4, -2, 4, 6.4, 6, -3, -3, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.5, -1, 1, 0.7},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){1, 15, 4, 3, 15, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-8.4, -2, 4, 10.9, 6, -3, -12.8, 10},
			},
		},
	},
	{
		Name:  "MixedInc2",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  -2,
		Incy:  3,
		N:     3,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){36, -2, 4, -5, 6, -3, 16, 10},
			},
		},
		DdotAns: 30,
		DswapAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){-4, 15, 7, 3, 8, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){14, -2, 4, -6, 6, -3, 10, 10},
		},
		DcopyAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){14, -2, 4, -6, 6, -3, 10, 10},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){7.372604823403701, 15, -2.479518890035003, 3, 16.069255112438693, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){1.333806631923407, -2, 4, 8.879864079700745, 6, -3, -7.851413765553595, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){9.4, 15, -6.1, 3, 11.8, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5.4, -2, 4, 2.9, 6, -3, -1, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[OffDiagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#OffDiagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){1, 0.1, -0.1, 1},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10.4, 15, -6.7, 3, 13.2, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){9.4, -2, 4, 6.4, 6, -3, -3, 10},
			},
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diagonal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diagonal),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.5, -1, 1, 0.7},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){1, 15, 4, 3, 15, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){-8.4, -2, 4, 10.9, 6, -3, -12.8, 10},
			},
		},
	},
	{
		Name:  "ZeroN",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  -2,
		Incy:  3,
		N:     0,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
		DswapAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		},
		DcopyAns: [DTwoVecAnswer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DTwoVecAnswer){
			X: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
			Y: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
	},
	{
		Name:  "NegativeN",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  -2,
		Incy:  3,
		N:     -3,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){36, -2, 4, -5, 6, -3, 16, 10},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 13.7, -5.8, 2, 12, 6.6},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, 0.5, 1.4, 3.8, 4.4, -0.8},
			},
		},
	},
	{
		Name:  "ZeroIncX",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  0,
		Incy:  3,
		N:     2,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){36, -2, 4, -5, 6, -3, 16, 10},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 13.7, -5.8, 2, 12, 6.6},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, 0.5, 1.4, 3.8, 4.4, -0.8},
			},
		},
	},
	{
		Name:  "ZeroIncY",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  1,
		Incy:  0,
		N:     2,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){36, -2, 4, -5, 6, -3, 16, 10},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 13.7, -5.8, 2, 12, 6.6},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, 0.5, 1.4, 3.8, 4.4, -0.8},
			},
		},
	},
	{
		Name:  "OutOfBoundsX",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  8,
		Incy:  2,
		N:     2,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){36, -2, 4, -5, 6, -3, 16, 10},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){8.2, 13.7, -5.8, 2, 12, 6.6},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){5, 0.5, 1.4, 3.8, 4.4, -0.8},
			},
		},
	},
	{
		Name:  "OutOfBoundsY",
		X:     [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
		XTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0},
		YTmp:  [][float64](https://pkg.go.dev/builtin#float64){0, 0, 0, 0, 0, 0, 0, 0},
		Incx:  2,
		Incy:  8,
		N:     2,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){36, -2, 4, -5, 6, -3, 16, 10},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){10, 15, -6, 3, 14, 7},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){8, -2, 4, 7, 6, -3, -4, 10},
			},
		},
	},
	{
		Name:  "Empty",
		X:     [][float64](https://pkg.go.dev/builtin#float64){},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){},
		Incx:  1,
		Incy:  1,
		N:     0,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
	},
	{
		Name:  "EmptyZeroIncX",
		X:     [][float64](https://pkg.go.dev/builtin#float64){},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){},
		Incx:  0,
		Incy:  1,
		N:     0,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
	},
	{
		Name:  "EmptyZeroIncY",
		X:     [][float64](https://pkg.go.dev/builtin#float64){},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){},
		Incx:  1,
		Incy:  0,
		N:     0,
		Panic: [true](https://pkg.go.dev/builtin#true),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
	},
	{
		Name:  "EmptyReverse",
		X:     [][float64](https://pkg.go.dev/builtin#float64){},
		Y:     [][float64](https://pkg.go.dev/builtin#float64){},
		Incx:  -1,
		Incy:  -1,
		N:     0,
		Panic: [false](https://pkg.go.dev/builtin#false),
		DaxpyCases: [][DaxpyCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DaxpyCase){
			{
				Alpha: 2,
				Ans:   [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotCases: [][DrotCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotCase){
			{
				C:    [math](https://pkg.go.dev/math).[Cos](https://pkg.go.dev/math#Cos)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				S:    [math](https://pkg.go.dev/math).[Sin](https://pkg.go.dev/math#Sin)(25 * [math](https://pkg.go.dev/math).[Pi](https://pkg.go.dev/math#Pi) / 180),
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
		DrotmCases: [][DrotmCase](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotmCase){
			{
				P: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[DrotmParams](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#DrotmParams){
					Flag: [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Rescaling](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Rescaling),
					H:    [4][float64](https://pkg.go.dev/builtin#float64){0.9, 0.1, -0.1, 0.5},
				},
				XAns: [][float64](https://pkg.go.dev/builtin#float64){},
				YAns: [][float64](https://pkg.go.dev/builtin#float64){},
			},
		},
	},
}

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/blas/testblas/level1double.go#L1517)

var DrotgTests = [][DrotgTestStruct](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#DrotgTestStruct){ 	{
		Name: "ZeroAB",
		C:    1,
	},
	{
		Name: "PosA_ZeroB",
		A:    0.5,
		C:    1,
		R:    0.5,
	},
	{
		Name: "NegA_ZeroB",
		A:    -4.6,
		C:    1,
		R:    -4.6,
	},
	{
		Name: "ZeroA_PosB",
		B:    3,
		S:    1,
		R:    3,
		Z:    1,
	},
	{
		Name: "ZeroA_NegB",
		B:    -0.3,
		S:    1,
		R:    -0.3,
		Z:    1,
	},
	{
		Name: "PosA_PosB_AGTB",
		A:    5,
		B:    0.3,
		C:    0.99820484546577868593549038000,
		S:    0.05989229072794672115612942280,
		R:    5.00899191454727744602429072688,
		Z:    0.05989229072794672115612942280,
	},
	{
		Name: "PosA_PosB_ALTB",
		A:    3,
		B:    4,
		C:    3.0 / 5,
		S:    4.0 / 5,
		R:    5,
		Z:    5.0 / 3.0,
	},

	{
		Name: "PosA_NegB_AGTB",
		A:    2.6,
		B:    -0.9,
		C:    0.94498607344025815971847507095,
		S:    -0.32711056388316628605639521686,
		R:    2.751363298439520872718790879655,
		Z:    -0.3271105638831662860563952168,
	},
	{
		Name: "PosA_NegB_ALTB",
		A:    2.6,
		B:    -2.9,
		C:    -0.6675450157520258540548049558,
		S:    0.7445694406464903756765132200,
		R:    -3.8948684188300893100043812234,
		Z:    1 / -0.6675450157520258540548049558,
	},
	{
		Name: "NegA_PosB_AGTB",
		A:    -11.4,
		B:    10.3,
		C:    0.7419981952497362418487847947,
		S:    -0.6704018781642353764072353847,
		R:    -15.363918770938617534070671122,
		Z:    -0.6704018781642353764072353847,
	},
	{
		Name: "NegA_PosB_ALTB",
		A:    -1.4,
		B:    10.3,
		C:    -0.1346838895922121112404717523,
		S:    0.9908886162855605326977564640,
		R:    10.394710193170370442523552032,
		Z:    1 / -0.1346838895922121112404717523,
	},
	{
		Name: "NegA_NegB_AGTB",
		A:    -11.4,
		B:    10.3,
		C:    0.7419981952497362418487847947,
		S:    -0.6704018781642353764072353847,
		R:    -15.363918770938617534070671122,
		Z:    -0.6704018781642353764072353847,
	},
	{
		Name: "NegA_NegB_ALTB",
		A:    -1.4,
		B:    -10.3,
		C:    0.1346838895922121112404717523,
		S:    0.9908886162855605326977564640,
		R:    -10.394710193170370442523552032,
		Z:    1 / 0.1346838895922121112404717523,
	},
}

func DgerBenchmark(b *[testing](https://pkg.go.dev/testing).[B](https://pkg.go.dev/testing#B), impl [Dgerer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Dgerer), m, n, incX, incY [int](https://pkg.go.dev/builtin#int))

func SgerBenchmark(b *[testing](https://pkg.go.dev/testing).[B](https://pkg.go.dev/testing#B), blasser [Sgerer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Sgerer), m, n, incX, incY [int](https://pkg.go.dev/builtin#int))

type Dgbmver interface {
 Dgbmv(tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, kL, kU [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), y [][float64](https://pkg.go.dev/builtin#float64), incY [int](https://pkg.go.dev/builtin#int)) }

type DgemmCase struct {
	
}

type Dgemmer interface {
 Dgemm(tA, tB [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int)) }

type DgemvSubcase struct {
	
}

type Dgemver interface {
 Dgemv(tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), y [][float64](https://pkg.go.dev/builtin#float64), incY [int](https://pkg.go.dev/builtin#int)) }

type Dsbmver interface {
 Dsbmv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), n, k [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), y [][float64](https://pkg.go.dev/builtin#float64), incY [int](https://pkg.go.dev/builtin#int)) }

type Dsymmer interface {
 Dsymm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int)) }

type Dsyr2ker interface {
 Dsyr2k(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][float64](https://pkg.go.dev/builtin#float64), ldc [int](https://pkg.go.dev/builtin#int)) }

type Dtbsver interface {
 Dtbsv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int))  Dtrsv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), n [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int)) }

type Dtrmmer interface {
 Dtrmm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int)) }

type Dtrsmer interface {
 Dtrsm(s [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), 		alpha [float64](https://pkg.go.dev/builtin#float64), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), b [][float64](https://pkg.go.dev/builtin#float64), ldb [int](https://pkg.go.dev/builtin#int))
}

type Dtxmver interface {
 Dtrmv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), n [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int))  Dtbmv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), n, k [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), lda [int](https://pkg.go.dev/builtin#int), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int))  Dtpmv(ul [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), tA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), d [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), n [int](https://pkg.go.dev/builtin#int), a [][float64](https://pkg.go.dev/builtin#float64), x [][float64](https://pkg.go.dev/builtin#float64), incX [int](https://pkg.go.dev/builtin#int)) }

type Zgbmver interface {
 Zgbmv(trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, kL, kU [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), ab [][complex128](https://pkg.go.dev/builtin#complex128), ldab [int](https://pkg.go.dev/builtin#int), x [][complex128](https://pkg.go.dev/builtin#complex128), incX [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), y [][complex128](https://pkg.go.dev/builtin#complex128), incY [int](https://pkg.go.dev/builtin#int)) 
	[Zgemver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zgemver)
}

type Zgemmer interface {
 Zgemm(tA, tB [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int)) }

type Zgemver interface {
 Zgemv(trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), x [][complex128](https://pkg.go.dev/builtin#complex128), incX [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), y [][complex128](https://pkg.go.dev/builtin#complex128), incY [int](https://pkg.go.dev/builtin#int)) }

type Zhbmver interface {
 Zhbmv(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), ab [][complex128](https://pkg.go.dev/builtin#complex128), ldab [int](https://pkg.go.dev/builtin#int), x [][complex128](https://pkg.go.dev/builtin#complex128), incX [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), y [][complex128](https://pkg.go.dev/builtin#complex128), incY [int](https://pkg.go.dev/builtin#int)) 
	[Zhemver](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas/testblas#Zhemver)
}

type Zhemmer interface {
 Zhemm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int)) }

type Zher2ker interface {
 Zher2k(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [float64](https://pkg.go.dev/builtin#float64), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int)) }

type Zsymmer interface {
 Zsymm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int)) }

type Zsyr2ker interface {
 Zsyr2k(uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), n, k [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int), beta [complex128](https://pkg.go.dev/builtin#complex128), c [][complex128](https://pkg.go.dev/builtin#complex128), ldc [int](https://pkg.go.dev/builtin#int)) }

type Ztrmmer interface {
 Ztrmm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), trans [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), diag [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int)) }

type Ztrsmer interface {
 Ztrsm(side [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Side](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Side), uplo [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Uplo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Uplo), transA [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Transpose](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Transpose), diag [blas](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas).[Diag](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/blas#Diag), m, n [int](https://pkg.go.dev/builtin#int), alpha [complex128](https://pkg.go.dev/builtin#complex128), a [][complex128](https://pkg.go.dev/builtin#complex128), lda [int](https://pkg.go.dev/builtin#int), b [][complex128](https://pkg.go.dev/builtin#complex128), ldb [int](https://pkg.go.dev/builtin#int)) }
