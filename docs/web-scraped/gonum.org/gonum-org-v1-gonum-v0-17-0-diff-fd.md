# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd

Title: fd package - gonum.org/v1/gonum/diff/fd - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd

Markdown Content:
Package fd provides functions to approximate derivatives using finite differences.

*   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#pkg-variables)
*   [func CrossLaplacian(f func(x, y []float64) float64, x, y []float64, settings *Settings) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#CrossLaplacian)
*   [func Derivative(f func(float64) float64, x float64, settings *Settings) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Derivative)
*   [func Gradient(dst []float64, f func([]float64) float64, x []float64, settings *Settings) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Gradient)
*   [func Hessian(dst *mat.SymDense, f func(x []float64) float64, x []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Hessian)
*   [func Jacobian(dst *mat.Dense, f func(y, x []float64), x []float64, ...)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Jacobian)
*   [func Laplacian(f func(x []float64) float64, x []float64, settings *Settings) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Laplacian)
*   [type Formula](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Formula)
*   [type JacobianSettings](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#JacobianSettings)
*   [type Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point)
*   [type Settings](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Settings)

*   [Derivative](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#example-Derivative)
*   [Jacobian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#example-Jacobian)

This section is empty.

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/diff/fd/diff.go#L70)

var Backward = [Formula](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Formula){ 	Stencil:    [][Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point){{Loc: -1, Coeff: -1}, {Loc: 0, Coeff: 1}},
	Derivative: 1,
	Step:       2e-8,
}

Backward represents a first-order accurate backward approximation to the first derivative.

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/diff/fd/diff.go#L78)

var Backward2nd = [Formula](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Formula){ 	Stencil:    [][Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point){{Loc: 0, Coeff: 1}, {Loc: -1, Coeff: -2}, {Loc: -2, Coeff: 1}},
	Derivative: 2,
	Step:       1e-4,
}

Backward2nd represents a first-order accurate forward approximation to the second derivative.

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/diff/fd/diff.go#L86)

var Central = [Formula](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Formula){ 	Stencil:    [][Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point){{Loc: -1, Coeff: -0.5}, {Loc: 1, Coeff: 0.5}},
	Derivative: 1,
	Step:       6e-6,
}

Central represents a second-order accurate centered approximation to the first derivative.

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/diff/fd/diff.go#L94)

var Central2nd = [Formula](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Formula){ 	Stencil:    [][Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point){{Loc: -1, Coeff: 1}, {Loc: 0, Coeff: -2}, {Loc: 1, Coeff: 1}},
	Derivative: 2,
	Step:       1e-4,
}

Central2nd represents a second-order accurate centered approximation to the second derivative.

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/diff/fd/diff.go#L54)

var Forward = [Formula](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Formula){ 	Stencil:    [][Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point){{Loc: 0, Coeff: -1}, {Loc: 1, Coeff: 1}},
	Derivative: 1,
	Step:       2e-8,
}

Forward represents a first-order accurate forward approximation to the first derivative.

[View Source](https://github.com/gonum/gonum/blob/v0.17.0/diff/fd/diff.go#L62)

var Forward2nd = [Formula](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Formula){ 	Stencil:    [][Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point){{Loc: 0, Coeff: 1}, {Loc: 1, Coeff: -2}, {Loc: 2, Coeff: 1}},
	Derivative: 2,
	Step:       1e-4,
}

Forward2nd represents a first-order accurate forward approximation to the second derivative.

CrossLaplacian computes a Laplacian-like quantity for a function of two vectors at the locations x and y. It computes

∇_y · ∇_x f(x,y) = \sum_i ∂^2 f(x,y)/∂x_i ∂y_i

The two input vector lengths must be the same.

Finite difference formula and other options are specified by settings. If settings is nil, CrossLaplacian will be estimated using the Forward formula and a default step size.

CrossLaplacian panics if the two input vectors are not the same length, or if the derivative order of the formula is not 1.

Derivative estimates the derivative of the function f at the given location. The finite difference formula, the step size, and other options are specified by settings. If settings is nil, the first derivative will be estimated using the Forward formula and a default step size.

package main

import (
	"fmt"
	"math"

	"gonum.org/v1/gonum/diff/fd"
)

func main() {
	f := func(x float64) float64 {
		return math.Sin(x)
	}
	// Compute the first derivative of f at 0 using the default settings.
	fmt.Println("f′(0) ≈", fd.Derivative(f, 0, nil))
	// Compute the first derivative of f at 0 using the forward approximation
	// with a custom step size.
	df := fd.Derivative(f, 0, &fd.Settings{
		Formula: fd.Forward,
		Step:    1e-3,
	})
	fmt.Println("f′(0) ≈", df)

	f = func(x float64) float64 {
		return math.Pow(math.Cos(x), 3)
	}
	// Compute the second derivative of f at 0 using
	// the centered approximation, concurrent evaluation,
	// and a known function value at x.
	df = fd.Derivative(f, 0, &fd.Settings{
		Formula:     fd.Central2nd,
		Concurrent:  true,
		OriginKnown: true,
		OriginValue: f(0),
	})
	fmt.Println("f′′(0) ≈", df)

}
Output:

f′(0) ≈ 1 f′(0) ≈ 0.9999998333333416 f′′(0) ≈ -2.999999981767587 

Gradient estimates the gradient of the multivariate function f at the location x. If dst is not nil, the result will be stored in-place into dst and returned, otherwise a new slice will be allocated first. Finite difference formula and other options are specified by settings. If settings is nil, the gradient will be estimated using the Forward formula and a default step size.

Gradient panics if the length of dst and x is not equal, or if the derivative order of the formula is not 1.

Hessian approximates the Hessian matrix of the multivariate function f at the location x. That is

H_{i,j} = ∂^2 f(x)/∂x_i ∂x_j

The resulting H will be stored in dst. Finite difference formula and other options are specified by settings. If settings is nil, the Hessian will be estimated using the Forward formula and a default step size.

If the dst matrix is empty it will be resized to the correct dimensions, otherwise the dimensions of dst must match the length of x or Hessian will panic. Hessian will panic if the derivative order of the formula is not 1.

Jacobian approximates the Jacobian matrix of a vector-valued function f at the location x and stores the result in-place into dst.

Finite difference formula and other options are specified by settings. If settings is nil, the Jacobian will be estimated using the Forward formula and a default step size.

The Jacobian matrix J is the matrix of all first-order partial derivatives of f. If f maps an n-dimensional vector x to an m-dimensional vector y = f(x), J is an m×n matrix whose elements are given as

J_{i,j} = ∂f_i/∂x_j,

or expanded out

    [ ∂f_1/∂x_1 ... ∂f_1/∂x_n ]
    [     .  .          .     ]
J = [     .      .      .     ]
    [     .          .  .     ]
    [ ∂f_m/∂x_1 ... ∂f_m/∂x_n ]

dst must be non-nil, the number of its columns must equal the length of x, and the derivative order of the formula must be 1, otherwise Jacobian will panic.

package main

import (
	"fmt"
	"math"

	"gonum.org/v1/gonum/diff/fd"
	"gonum.org/v1/gonum/mat"
)

func main() {
	f := func(dst, x []float64) {
		dst[0] = x[0] + 1
		dst[1] = 5 * x[2]
		dst[2] = 4*x[1]*x[1] - 2*x[2]
		dst[3] = x[2] * math.Sin(x[0])
	}
	jac := mat.NewDense(4, 3, nil)
	fd.Jacobian(jac, f, []float64{1, 2, 3}, &fd.JacobianSettings{
		Formula:    fd.Central,
		Concurrent: true,
	})
	fmt.Printf("J ≈ %.6v\n", mat.Formatted(jac, mat.Prefix("    ")))

}
Output:

J ≈ ⎡ 1 0 0⎤ ⎢ 0 0 5⎥ ⎢ 0 16 -2⎥ ⎣ 1.62091 0 0.841471⎦ 

Laplacian computes the Laplacian of the multivariate function f at the location x. That is, Laplacian returns

∆ f(x) = ∇ · ∇ f(x) = \sum_i ∂^2 f(x)/∂x_i^2

The finite difference formula and other options are specified by settings. The order of the difference formula must be 2 or Laplacian will panic.

type Formula struct {
	
	
 Stencil [][Point](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/diff/fd#Point) Derivative [int](https://pkg.go.dev/builtin#int)  Step [float64](https://pkg.go.dev/builtin#float64) }

Formula represents a finite difference formula on a regularly spaced grid that approximates the derivative of order k of a function f at x as

d^k f(x) ≈ (1 / Step^k) * \sum_i Coeff_i * f(x + Step * Loc_i).

Step must be positive, or the finite difference formula will panic.

A Point is a stencil location in a finite difference formula.

Settings is the settings structure for computing finite differences.
