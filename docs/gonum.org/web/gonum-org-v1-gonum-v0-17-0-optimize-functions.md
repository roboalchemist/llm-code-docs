# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions

Title: functions package - gonum.org/v1/gonum/optimize/functions - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions

Markdown Content:
Package functions provides objective functions for testing optimization algorithms.

We encourage outside contributions of additional test functions that exhibit properties not already covered in the testing suite or that have significance due to prior use as benchmark cases.

*   [type Ackley](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Ackley)
*       *   [func (Ackley) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Ackley.Func)

*   [type Beale](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Beale)
*       *   [func (Beale) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Beale.Func)
    *   [func (Beale) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Beale.Grad)
    *   [func (Beale) Hess(dst *mat.SymDense, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Beale.Hess)
    *   [func (Beale) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Beale.Minima)

*   [type BiggsEXP2](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP2)
*       *   [func (BiggsEXP2) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP2.Func)
    *   [func (BiggsEXP2) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP2.Grad)
    *   [func (BiggsEXP2) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP2.Minima)

*   [type BiggsEXP3](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP3)
*       *   [func (BiggsEXP3) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP3.Func)
    *   [func (BiggsEXP3) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP3.Grad)
    *   [func (BiggsEXP3) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP3.Minima)

*   [type BiggsEXP4](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP4)
*       *   [func (BiggsEXP4) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP4.Func)
    *   [func (BiggsEXP4) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP4.Grad)
    *   [func (BiggsEXP4) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP4.Minima)

*   [type BiggsEXP5](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP5)
*       *   [func (BiggsEXP5) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP5.Func)
    *   [func (BiggsEXP5) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP5.Grad)
    *   [func (BiggsEXP5) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP5.Minima)

*   [type BiggsEXP6](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP6)
*       *   [func (BiggsEXP6) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP6.Func)
    *   [func (BiggsEXP6) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP6.Grad)
    *   [func (BiggsEXP6) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP6.Minima)

*   [type Box3D](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Box3D)
*       *   [func (Box3D) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Box3D.Func)
    *   [func (Box3D) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Box3D.Grad)
    *   [func (Box3D) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Box3D.Minima)

*   [type BraninHoo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BraninHoo)
*       *   [func (BraninHoo) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BraninHoo.Func)
    *   [func (BraninHoo) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BraninHoo.Minima)

*   [type BrownAndDennis](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis)
*       *   [func (BrownAndDennis) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Func)
    *   [func (BrownAndDennis) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Grad)
    *   [func (BrownAndDennis) Hess(dst *mat.SymDense, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Hess)
    *   [func (BrownAndDennis) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Minima)

*   [type BrownBadlyScaled](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownBadlyScaled)
*       *   [func (BrownBadlyScaled) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownBadlyScaled.Func)
    *   [func (BrownBadlyScaled) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownBadlyScaled.Grad)
    *   [func (BrownBadlyScaled) Hess(dst *mat.SymDense, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownBadlyScaled.Hess)
    *   [func (BrownBadlyScaled) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownBadlyScaled.Minima)

*   [type Bukin6](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Bukin6)
*       *   [func (Bukin6) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Bukin6.Func)

*   [type CamelSix](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#CamelSix)
*       *   [func (c CamelSix) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#CamelSix.Func)

*   [type CamelThree](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#CamelThree)
*       *   [func (c CamelThree) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#CamelThree.Func)

*   [type ConcaveLeft](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ConcaveLeft)
*       *   [func (ConcaveLeft) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ConcaveLeft.Func)
    *   [func (ConcaveLeft) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ConcaveLeft.Grad)

*   [type ConcaveRight](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ConcaveRight)
*       *   [func (ConcaveRight) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ConcaveRight.Func)
    *   [func (ConcaveRight) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ConcaveRight.Grad)

*   [type CrossInTray](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#CrossInTray)
*       *   [func (CrossInTray) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#CrossInTray.Func)

*   [type DixonPrice](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#DixonPrice)
*       *   [func (DixonPrice) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#DixonPrice.Func)

*   [type DropWave](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#DropWave)
*       *   [func (DropWave) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#DropWave.Func)

*   [type Eggholder](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Eggholder)
*       *   [func (Eggholder) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Eggholder.Func)

*   [type ExtendedPowellSingular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedPowellSingular)
*       *   [func (ExtendedPowellSingular) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedPowellSingular.Func)
    *   [func (ExtendedPowellSingular) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedPowellSingular.Grad)
    *   [func (ExtendedPowellSingular) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedPowellSingular.Minima)

*   [type ExtendedRosenbrock](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedRosenbrock)
*       *   [func (ExtendedRosenbrock) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedRosenbrock.Func)
    *   [func (ExtendedRosenbrock) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedRosenbrock.Grad)
    *   [func (ExtendedRosenbrock) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedRosenbrock.Minima)

*   [type Gaussian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Gaussian)
*       *   [func (g Gaussian) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Gaussian.Func)
    *   [func (g Gaussian) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Gaussian.Grad)
    *   [func (Gaussian) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Gaussian.Minima)

*   [type GramacyLee](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GramacyLee)
*       *   [func (GramacyLee) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GramacyLee.Func)

*   [type Griewank](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Griewank)
*       *   [func (Griewank) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Griewank.Func)

*   [type GulfResearchAndDevelopment](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment)
*       *   [func (GulfResearchAndDevelopment) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment.Func)
    *   [func (GulfResearchAndDevelopment) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment.Grad)
    *   [func (GulfResearchAndDevelopment) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment.Minima)

*   [type HelicalValley](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#HelicalValley)
*       *   [func (HelicalValley) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#HelicalValley.Func)
    *   [func (HelicalValley) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#HelicalValley.Grad)
    *   [func (HelicalValley) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#HelicalValley.Minima)

*   [type HolderTable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#HolderTable)
*       *   [func (HolderTable) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#HolderTable.Func)

*   [type Langermann2](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Langermann2)
*       *   [func (Langermann2) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Langermann2.Func)

*   [type Levy](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Levy)
*       *   [func (Levy) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Levy.Func)

*   [type Levy13](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Levy13)
*       *   [func (Levy13) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Levy13.Func)

*   [type Linear](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Linear)
*       *   [func (Linear) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Linear.Func)
    *   [func (Linear) Grad(grad, x []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Linear.Grad)

*   [type MinimalSurface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface)
*       *   [func NewMinimalSurface(nx, ny int) *MinimalSurface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#NewMinimalSurface)

*       *   [func (ms *MinimalSurface) Dims() (nx, ny int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface.Dims)
    *   [func (ms *MinimalSurface) ExactSolution(x, y float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface.ExactSolution)
    *   [func (ms *MinimalSurface) ExactX() []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface.ExactX)
    *   [func (ms *MinimalSurface) Func(x []float64) (area float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface.Func)
    *   [func (ms *MinimalSurface) Grad(grad, x []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface.Grad)
    *   [func (ms *MinimalSurface) InitX() []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface.InitX)
    *   [func (ms *MinimalSurface) Steps() (hx, hy float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface.Steps)

*   [type Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)
*   [type PenaltyI](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyI)
*       *   [func (PenaltyI) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyI.Func)
    *   [func (PenaltyI) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyI.Grad)
    *   [func (PenaltyI) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyI.Minima)

*   [type PenaltyII](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyII)
*       *   [func (PenaltyII) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyII.Func)
    *   [func (PenaltyII) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyII.Grad)
    *   [func (PenaltyII) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyII.Minima)

*   [type Plassmann](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Plassmann)
*       *   [func (f Plassmann) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Plassmann.Func)
    *   [func (f Plassmann) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Plassmann.Grad)

*   [type PowellBadlyScaled](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PowellBadlyScaled)
*       *   [func (PowellBadlyScaled) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PowellBadlyScaled.Func)
    *   [func (PowellBadlyScaled) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PowellBadlyScaled.Grad)
    *   [func (PowellBadlyScaled) Hess(dst *mat.SymDense, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PowellBadlyScaled.Hess)
    *   [func (PowellBadlyScaled) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PowellBadlyScaled.Minima)

*   [type Rastrigin](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Rastrigin)
*       *   [func (Rastrigin) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Rastrigin.Func)

*   [type Schaffer2](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Schaffer2)
*       *   [func (Schaffer2) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Schaffer2.Func)

*   [type Schaffer4](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Schaffer4)
*       *   [func (Schaffer4) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Schaffer4.Func)

*   [type Schwefel](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Schwefel)
*       *   [func (Schwefel) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Schwefel.Func)

*   [type Shubert](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Shubert)
*       *   [func (Shubert) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Shubert.Func)

*   [type Sphere](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Sphere)
*       *   [func (Sphere) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Sphere.Func)
    *   [func (Sphere) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Sphere.Grad)
    *   [func (Sphere) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Sphere.Minima)

*   [type Trigonometric](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Trigonometric)
*       *   [func (Trigonometric) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Trigonometric.Func)
    *   [func (Trigonometric) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Trigonometric.Grad)
    *   [func (Trigonometric) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Trigonometric.Minima)

*   [type VariablyDimensioned](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#VariablyDimensioned)
*       *   [func (VariablyDimensioned) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#VariablyDimensioned.Func)
    *   [func (VariablyDimensioned) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#VariablyDimensioned.Grad)
    *   [func (VariablyDimensioned) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#VariablyDimensioned.Minima)

*   [type Watson](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Watson)
*       *   [func (Watson) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Watson.Func)
    *   [func (Watson) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Watson.Grad)
    *   [func (Watson) Hess(dst *mat.SymDense, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Watson.Hess)
    *   [func (Watson) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Watson.Minima)

*   [type Wood](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Wood)
*       *   [func (Wood) Func(x []float64) (sum float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Wood.Func)
    *   [func (Wood) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Wood.Grad)
    *   [func (Wood) Hess(dst *mat.SymDense, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Wood.Hess)
    *   [func (Wood) Minima() []Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Wood.Minima)

*   [type YanaiOzawaKaneko](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#YanaiOzawaKaneko)
*       *   [func (f YanaiOzawaKaneko) Func(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#YanaiOzawaKaneko.Func)
    *   [func (f YanaiOzawaKaneko) Grad(grad, x []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#YanaiOzawaKaneko.Grad)

This section is empty.

This section is empty.

This section is empty.

type Ackley struct{}

Ackley implements the Ackley function, a function of arbitrary dimension that has many local minima. It has a single global minimum of 0 at 0. Its typical domain is the hypercube of [-32.768, 32.768]^d.

f(x) = -20 * exp(-0.2 sqrt(1/d sum_i x_i^2)) - exp(1/d sum_i cos(2π x_i)) + 20 + exp(1)

where d is the input dimension.

Reference:

https://www.sfu.ca/~ssurjano/ackley.html (obtained June 2017)

type Beale struct{}

Beale implements the Beale's function.

Standard starting points:

Easy: [1, 1]
Hard: [1, 4]

References:

*   Beale, E.: On an Iterative Method for Finding a Local Minimum of a Function of More than One Variable. Technical Report 25, Statistical Techniques Research Group, Princeton University (1958)
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([Beale](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Beale)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type BiggsEXP2 struct{}

BiggsEXP2 implements the Biggs' EXP2 function.

Standard starting point:

[1, 2]

Reference:

Biggs, M.C.: Minimization algorithms making use of non-quadratic properties
of the objective function. IMA J Appl Math 8 (1971), 315-327; doi:10.1093/imamat/8.3.315

func ([BiggsEXP2](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP2)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type BiggsEXP3 struct{}

BiggsEXP3 implements the Biggs' EXP3 function.

Standard starting point:

[1, 2, 1]

Reference:

Biggs, M.C.: Minimization algorithms making use of non-quadratic properties
of the objective function. IMA J Appl Math 8 (1971), 315-327; doi:10.1093/imamat/8.3.315

func ([BiggsEXP3](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP3)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type BiggsEXP4 struct{}

BiggsEXP4 implements the Biggs' EXP4 function.

Standard starting point:

[1, 2, 1, 1]

Reference:

Biggs, M.C.: Minimization algorithms making use of non-quadratic properties
of the objective function. IMA J Appl Math 8 (1971), 315-327; doi:10.1093/imamat/8.3.315

func ([BiggsEXP4](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP4)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type BiggsEXP5 struct{}

BiggsEXP5 implements the Biggs' EXP5 function.

Standard starting point:

[1, 2, 1, 1, 1]

Reference:

Biggs, M.C.: Minimization algorithms making use of non-quadratic properties
of the objective function. IMA J Appl Math 8 (1971), 315-327; doi:10.1093/imamat/8.3.315

func ([BiggsEXP5](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP5)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type BiggsEXP6 struct{}

BiggsEXP6 implements the Biggs' EXP6 function.

Standard starting point:

[1, 2, 1, 1, 1, 1]

References:

*   Biggs, M.C.: Minimization algorithms making use of non-quadratic properties of the objective function. IMA J Appl Math 8 (1971), 315-327; doi:10.1093/imamat/8.3.315
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([BiggsEXP6](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BiggsEXP6)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type Box3D struct{}

Box3D implements the Box' three-dimensional function.

Standard starting point:

[0, 10, 20]

References:

*   Box, M.J.: A comparison of several current optimization methods, and the use of transformations in constrained problems. Comput J 9 (1966), 67-77
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([Box3D](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Box3D)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type BraninHoo struct{}

BraninHoo implements the Branin-Hoo function. BraninHoo is a 2-dimensional test function with three global minima. It is typically evaluated in the domain x_0 ∈ [-5, 10], x_1 ∈ [0, 15].

f(x) = (x_1 - (5.1/(4π^2))*x_0^2 + (5/π)*x_0 - 6)^2 + 10*(1-1/(8π))cos(x_0) + 10

It has a minimum value of 0.397887 at x^* = {(-π, 12.275), (π, 2.275), (9.424778, 2.475)}

Reference:

https://www.sfu.ca/~ssurjano/branin.html (obtained June 2017)

func ([BraninHoo](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BraninHoo)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

#### type [BrownAndDennis](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L614)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis "Go to BrownAndDennis")

type BrownAndDennis struct{}

BrownAndDennis implements the Brown and Dennis function.

Standard starting point:

[25, 5, -5, -1]

References:

*   Brown, K.M., Dennis, J.E.: New computational algorithms for minimizing a sum of squares of nonlinear functions. Research Report Number 71-6, Yale University (1971)
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

#### func (BrownAndDennis) [Func](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L616)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Func "Go to BrownAndDennis.Func")

#### func (BrownAndDennis) [Grad](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L631)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Grad "Go to BrownAndDennis.Grad")

#### func (BrownAndDennis) [Hess](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L654)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Hess "Go to BrownAndDennis.Hess")

#### func (BrownAndDennis) [Minima](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L694)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis.Minima "Go to BrownAndDennis.Minima")

func ([BrownAndDennis](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownAndDennis)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type BrownBadlyScaled struct{}

BrownBadlyScaled implements the Brown's badly scaled function.

Standard starting point:

[1, 1]

References:

*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([BrownBadlyScaled](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#BrownBadlyScaled)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type Bukin6 struct{}

Bukin6 implements Bukin's 6th function. The function is two-dimensional, with the typical domain as x_0 ∈ [-15, -5], x_1 ∈ [-3, 3]. The function has a unique global minimum at [-10, 1], and many local minima.

f(x) = 100 * sqrt(|x_1 - 0.01*x_0^2|) + 0.01*|x_0+10|

Reference:

https://www.sfu.ca/~ssurjano/bukin6.html (obtained June 2017)

type CamelSix struct{}

CamelSix implements the six-hump camel function, a two-dimensional function. with six local minima, two of which are global. The function is given by

f(x) = (4 - 2.1*x_0^2 + x_0^4/3)*x_0^2 + x_0*x_1 + (-4 + 4*x_1^2)*x_1^2

with the global minima at

x^* = (0.0898, -0.7126), (-0.0898, 0.7126)
f(x^*) = -1.0316

The typical domain is x_0 ∈ [-3, 3], x_1 ∈ [-2, 2]. Reference:

https://www.sfu.ca/~ssurjano/camel6.html (obtained December 2017)

type CamelThree struct{}

CamelThree implements the three-hump camel function, a two-dimensional function with three local minima, one of which is global. The function is given by

f(x) = 2*x_0^2 - 1.05*x_0^4 + x_0^6/6 + x_0*x_1 + x_1^2

with the global minimum at

x^* = (0, 0)
f(x^*) = 0

The typical domain is x_i ∈ [-5, 5] for all i. Reference:

https://www.sfu.ca/~ssurjano/camel3.html (obtained December 2017)

type ConcaveLeft struct{}

ConcaveLeft implements an univariate function that is concave to the left of the minimizer which is located at x=399/250=1.596.

References:

More, J.J., and Thuente, D.J.: Line Search Algorithms with Guaranteed Sufficient Decrease.
ACM Transactions on Mathematical Software 20(3) (1994), 286–307, eq. (5.2)

type ConcaveRight struct{}

ConcaveRight implements an univariate function that is concave to the right of the minimizer which is located at x=sqrt(2).

References:

More, J.J., and Thuente, D.J.: Line Search Algorithms with Guaranteed Sufficient Decrease.
ACM Transactions on Mathematical Software 20(3) (1994), 286–307, eq. (5.1)

type CrossInTray struct{}

CrossInTray implements the cross-in-tray function. The cross-in-tray function is a two-dimensional function with many local minima, and four global minima at (±1.3491, ±1.3491). The function is typically evaluated in the square [-10,10]^2.

f(x) = -0.001(|sin(x_0)sin(x_1)exp(|100-sqrt((x_0^2+x_1^2)/π)|)|+1)^0.1

Reference:

https://www.sfu.ca/~ssurjano/crossit.html (obtained June 2017)

type DixonPrice struct{}

DixonPrice implements the DixonPrice function, a function of arbitrary dimension Its typical domain is the hypercube of [-10, 10]^d. The function is given by

f(x) = (x_0-1)^2 + \sum_{i=1}^{d-1} (i+1) * (2*x_i^2-x_{i-1})^2

where d is the input dimension. There is a single global minimum, which has a location and value of

x_i^* = 2^{-(2^{i+1}-2)/(2^{i+1})} for i = 0, ..., d-1.
f(x^*) = 0

Reference:

https://www.sfu.ca/~ssurjano/dixonpr.html (obtained June 2017)

type DropWave struct{}

DropWave implements the drop-wave function, a two-dimensional function with many local minima and one global minimum at 0. The function is typically evaluated in the square [-5.12, 5.12]^2.

f(x) = - (1+cos(12*sqrt(x0^2+x1^2))) / (0.5*(x0^2+x1^2)+2)

Reference:

https://www.sfu.ca/~ssurjano/drop.html (obtained June 2017)

type Eggholder struct{}

Eggholder implements the Eggholder function, a two-dimensional function with many local minima and one global minimum at [512, 404.2319]. The function is typically evaluated in the square [-512, 512]^2.

f(x) = -(x_1+47)*sin(sqrt(|x_1+x_0/2+47|))-x_1*sin(sqrt(|x_0-(x_1+47)|))

Reference:

https://www.sfu.ca/~ssurjano/egg.html (obtained June 2017)

type ExtendedPowellSingular struct{}

ExtendedPowellSingular implements the extended Powell's function. Its Hessian matrix is singular at the minimizer.

Standard starting point:

[3, -1, 0, 3, 3, -1, 0, 3, ..., 3, -1, 0, 3]

References:

*   Spedicato E.: Computational experience with quasi-Newton algorithms for minimization problems of moderately large size. Towards Global Optimization 2 (1978), 209-219
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([ExtendedPowellSingular](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedPowellSingular)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type ExtendedRosenbrock struct{}

ExtendedRosenbrock implements the extended, multidimensional Rosenbrock function.

Standard starting point:

Easy: [-1.2, 1, -1.2, 1, ...]
Hard: any point far from the minimum

References:

*   Rosenbrock, H.H.: An Automatic Method for Finding the Greatest or Least Value of a Function. Computer J 3 (1960), 175-184
*   [http://en.wikipedia.org/wiki/Rosenbrock_function](http://en.wikipedia.org/wiki/Rosenbrock_function)

func ([ExtendedRosenbrock](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#ExtendedRosenbrock)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type Gaussian struct{}

Gaussian implements the Gaussian function. The function has one global minimum and a number of false local minima caused by the finite floating point precision.

Standard starting point:

[0.4, 1, 0]

Reference:

More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization
software. ACM Trans Math Softw 7 (1981), 17-41

func ([Gaussian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Gaussian)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type GramacyLee struct{}

GramacyLee implements the Gramacy-Lee function, a one-dimensional function with many local minima. The function is typically evaluated on the domain [0.5, 2.5].

f(x) = sin(10πx)/(2x) + (x-1)^4

Reference:

https://www.sfu.ca/~ssurjano/grlee12.html (obtained June 2017)

type Griewank struct{}

Griewank implements the Griewank function, a function of arbitrary dimension that has many local minima. It has a single global minimum of 0 at 0. Its typical domain is the hypercube of [-600, 600]^d.

f(x) = \sum_i x_i^2/4000 - \prod_i cos(x_i/sqrt(i)) + 1

where d is the input dimension.

Reference:

https://www.sfu.ca/~ssurjano/griewank.html (obtained June 2017)

#### type [GulfResearchAndDevelopment](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L971)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment "Go to GulfResearchAndDevelopment")

type GulfResearchAndDevelopment struct{}

GulfResearchAndDevelopment implements the Gulf Research and Development function.

Standard starting point:

[5, 2.5, 0.15]

References:

*   Cox, R.A.: Comparison of the performance of seven optimization algorithms on twelve unconstrained minimization problems. Ref. 1335CNO4, Gulf Research and Development Company, Pittsburg (1969)
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

#### func (GulfResearchAndDevelopment) [Func](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L973)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment.Func "Go to GulfResearchAndDevelopment.Func")

#### func (GulfResearchAndDevelopment) [Grad](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L989)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment.Grad "Go to GulfResearchAndDevelopment.Grad")

#### func (GulfResearchAndDevelopment) [Minima](https://github.com/gonum/gonum/blob/v0.17.0/optimize/functions/functions.go#L1016)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment.Minima "Go to GulfResearchAndDevelopment.Minima")

func ([GulfResearchAndDevelopment](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#GulfResearchAndDevelopment)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type HelicalValley struct{}

HelicalValley implements the helical valley function of Fletcher and Powell. Function is not defined at x[0] = 0.

Standard starting point:

[-1, 0, 0]

References:

*   Fletcher, R., Powell, M.J.D.: A rapidly convergent descent method for minimization. Comput J 6 (1963), 163-168
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([HelicalValley](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#HelicalValley)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type HolderTable struct{}

HolderTable implements the Holder table function. The Holder table function is a two-dimensional function with many local minima, and four global minima at (±8.05502, ±9.66459). The function is typically evaluated in the square [-10,10]^2.

f(x) = -|sin(x_0)cos(x1)exp(|1-sqrt(x_0^2+x1^2)/π|)|

Reference:

https://www.sfu.ca/~ssurjano/holder.html (obtained June 2017)

type Langermann2 struct{}

Langermann2 implements the two-dimensional version of the Langermann function. The Langermann function has many local minima. The function is typically evaluated in the square [0,10]^2.

f(x) = \sum_1^5 c_i exp(-(1/π)\sum_{j=1}^2(x_j-A_{ij})^2) * cos(π\sum_{j=1}^2 (x_j - A_{ij})^2)
c = [5]float64{1,2,5,2,3}
A = [5][2]float64{{3,5},{5,2},{2,1},{1,4},{7,9}}

Reference:

https://www.sfu.ca/~ssurjano/langer.html (obtained June 2017)

type Levy struct{}

Levy implements the Levy function, a function of arbitrary dimension that has many local minima. It has a single global minimum of 0 at 1. Its typical domain is the hypercube of [-10, 10]^d.

f(x) = sin^2(π*w_0) + \sum_{i=0}^{d-2}(w_i-1)^2*[1+10sin^2(π*w_i+1)] +
          (w_{d-1}-1)^2*[1+sin^2(2π*w_{d-1})]
 w_i = 1 + (x_i-1)/4

where d is the input dimension.

Reference:

https://www.sfu.ca/~ssurjano/levy.html (obtained June 2017)

type Levy13 struct{}

Levy13 implements the Levy-13 function, a two-dimensional function with many local minima. It has a single global minimum of 0 at 1. Its typical domain is the square [-10, 10]^2.

f(x) = sin^2(3π*x_0) + (x_0-1)^2*[1+sin^2(3π*x_1)] + (x_1-1)^2*[1+sin^2(2π*x_1)]

Reference:

https://www.sfu.ca/~ssurjano/levy13.html (obtained June 2017)

type Linear struct{}

Linear implements a linear function.

type MinimalSurface struct {
	
}

MinimalSurface implements a finite element approximation to a minimal surface problem: determine the surface with minimal area and given boundary values in a unit square centered at the origin.

References:

Averick, M.B., Carter, R.G., Moré, J.J., Xue, G.-L.: The Minpack-2 Test
Problem Collection. Preprint MCS-P153-0692, Argonne National Laboratory (1992)

func NewMinimalSurface(nx, ny [int](https://pkg.go.dev/builtin#int)) *[MinimalSurface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface)

NewMinimalSurface creates a new discrete minimal surface problem and precomputes its boundary values. The problem is discretized on a rectilinear grid with nx×ny nodes which means that the problem dimension is (nx-2)(ny-2).

func (ms *[MinimalSurface](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#MinimalSurface)) Dims() (nx, ny [int](https://pkg.go.dev/builtin#int))

Dims returns the size of the underlying rectilinear grid.

ExactSolution returns the value of the exact solution to the minimal surface problem at (x,y). The exact solution is

F_exact(x,y) = U^2(x,y) - V^2(x,y),

where U and V are the unique solutions to the equations

x =  u + uv^2 - u^3/3,
y = -v - u^2v + v^3/3.

ExactX returns the exact solution to the _continuous_ minimization problem projected on the interior nodes of the grid. Length of the returned slice is (nx-2)(ny-2).

Func returns the area of the surface represented by the vector x.

Grad evaluates the area gradient of the surface represented by the vector.

InitX returns a starting location for the minimization problem. Length of the returned slice is (nx-2)(ny-2).

Steps returns the spatial step sizes of the underlying rectilinear grid.

Minimum represents information about an optimal location of a function.

type PenaltyI struct{}

PenaltyI implements the first penalty function by Gill, Murray and Pitfield.

Standard starting point:

[1, ..., n]

References:

*   Gill, P.E., Murray, W., Pitfield, R.A.: The implementation of two revised quasi-Newton algorithms for unconstrained optimization. Report NAC 11, National Phys Lab (1972), 82-83
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([PenaltyI](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyI)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type PenaltyII struct{}

PenaltyII implements the second penalty function by Gill, Murray and Pitfield.

Standard starting point:

[0.5, ..., 0.5]

References:

*   Gill, P.E., Murray, W., Pitfield, R.A.: The implementation of two revised quasi-Newton algorithms for unconstrained optimization. Report NAC 11, National Phys Lab (1972), 82-83
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([PenaltyII](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PenaltyII)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

Plassmann implements an univariate oscillatory function where the value of L controls the number of oscillations. The value of Beta controls the size of the derivative at zero and the size of the interval where the strong Wolfe conditions can hold. For small values of Beta this function represents a difficult test problem for linesearchers also because the information based on the derivative is unreliable due to the oscillations.

References:

More, J.J., and Thuente, D.J.: Line Search Algorithms with Guaranteed Sufficient Decrease.
ACM Transactions on Mathematical Software 20(3) (1994), 286–307, eq. (5.3)

type PowellBadlyScaled struct{}

PowellBadlyScaled implements the Powell's badly scaled function. The function is very flat near the minimum. A satisfactory solution is one that gives f(x) ≅ 1e-13.

Standard starting point:

[0, 1]

References:

*   Powell, M.J.D.: A Hybrid Method for Nonlinear Equations. Numerical Methods for Nonlinear Algebraic Equations, P. Rabinowitz (ed.), Gordon and Breach (1970)
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([PowellBadlyScaled](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#PowellBadlyScaled)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type Rastrigin struct{}

Rastrigin implements the Rastrigen function, a function of arbitrary dimension that has many local minima. It has a single global minimum of 0 at 0. Its typical domain is the hypercube of [-5.12, 5.12]^d.

f(x) = 10d + \sum_i [x_i^2 - 10cos(2π*x_i)]

where d is the input dimension.

Reference:

https://www.sfu.ca/~ssurjano/rastr.html (obtained June 2017)

type Schaffer2 struct{}

Schaffer2 implements the second Schaffer function, a two-dimensional function with many local minima. It has a single global minimum of 0 at 0. Its typical domain is the square [-100, 100]^2.

f(x) = 0.5 + (sin^2(x_0^2-x_1^2)-0.5) / (1+0.001*(x_0^2+x_1^2))^2

Reference:

https://www.sfu.ca/~ssurjano/schaffer2.html (obtained June 2017)

type Schaffer4 struct{}

Schaffer4 implements the fourth Schaffer function, a two-dimensional function with many local minima. Its typical domain is the square [-100, 100]^2.

f(x) = 0.5 + (cos(sin(|x_0^2-x_1^2|))-0.5) / (1+0.001*(x_0^2+x_1^2))^2

Reference:

https://www.sfu.ca/~ssurjano/schaffer4.html (obtained June 2017)

type Schwefel struct{}

Schwefel implements the Schwefel function, a function of arbitrary dimension that has many local minima. Its typical domain is the hypercube of [-500, 500]^d.

f(x) = 418.9829*d - \sum_i x_i*sin(sqrt(|x_i|))

where d is the input dimension.

Reference:

https://www.sfu.ca/~ssurjano/schwef.html (obtained June 2017)

type Shubert struct{}

Shubert implements the Shubert function, a two-dimensional function with many local minima and many global minima. Its typical domain is the square [-10, 10]^2.

f(x) = (sum_{i=1}^5 i cos((i+1)*x_0+i)) * (\sum_{i=1}^5 i cos((i+1)*x_1+i))

Reference:

https://www.sfu.ca/~ssurjano/shubert.html (obtained June 2017)

type Sphere struct{}

Sphere implements the sphere optimization function. It is continuous, convex, and unimodal. The global minimum is always at f(x)=0 at x=(0,...,0).

Standard starting point:

Any point away from the minimum

References:

*   [https://www.sfu.ca/~ssurjano/spheref.html](https://www.sfu.ca/~ssurjano/spheref.html)

func ([Sphere](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Sphere)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type Trigonometric struct{}

Trigonometric implements the trigonometric function.

Standard starting point:

[1/dim, ..., 1/dim]

References:

*   Spedicato E.: Computational experience with quasi-Newton algorithms for minimization problems of moderately large size. Towards Global Optimization 2 (1978), 209-219
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([Trigonometric](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Trigonometric)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type VariablyDimensioned struct{}

VariablyDimensioned implements a variably dimensioned function.

Standard starting point:

[..., (dim-i)/dim, ...], i=1,...,dim

References:

More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization
software. ACM Trans Math Softw 7 (1981), 17-41

func ([VariablyDimensioned](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#VariablyDimensioned)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type Watson struct{}

Watson implements the Watson's function. Dimension of the problem should be 2 <= dim <= 31. For dim == 9, the problem of minimizing the function is very ill conditioned.

Standard starting point:

[0, ..., 0]

References:

*   Kowalik, J.S., Osborne, M.R.: Methods for Unconstrained Optimization Problems. Elsevier North-Holland, New York, 1968
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([Watson](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Watson)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

type Wood struct{}

Wood implements the Wood's function.

Standard starting point:

[-3, -1, -3, -1]

References:

*   Colville, A.R.: A comparative study of nonlinear programming codes. Report 320-2949, IBM New York Scientific Center (1968)
*   More, J., Garbow, B.S., Hillstrom, K.E.: Testing unconstrained optimization software. ACM Trans Math Softw 7 (1981), 17-41

func ([Wood](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Wood)) Minima() [][Minimum](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/optimize/functions#Minimum)

YanaiOzawaKaneko is an univariate convex function where the values of Beta1 and Beta2 control the curvature around the minimum. Far away from the minimum the function approximates an absolute value function. Near the minimum, the function can either be sharply curved or flat, controlled by the parameter values.

References:

*   More, J.J., and Thuente, D.J.: Line Search Algorithms with Guaranteed Sufficient Decrease. ACM Transactions on Mathematical Software 20(3) (1994), 286–307, eq. (5.4)
*   Yanai, H., Ozawa, M., and Kaneko, S.: Interpolation methods in one dimensional optimization. Computing 27 (1981), 155–163
