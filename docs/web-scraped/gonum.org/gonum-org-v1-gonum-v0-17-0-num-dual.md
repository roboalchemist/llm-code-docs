# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual

Title: dual package - gonum.org/v1/gonum/num/dual - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual

Markdown Content:
Package dual provides the dual numeric type and functions. Dual numbers are an extension of the real numbers in the form a+bϵ where ϵ^2=0, but ϵ≠0.

See [https://en.wikipedia.org/wiki/Dual_number](https://en.wikipedia.org/wiki/Dual_number) for details of their properties and uses.

*   [type Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)
*       *   [func Abs(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Abs)
    *   [func Acos(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Acos)
    *   [func Acosh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Acosh)
    *   [func Add(x, y Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Add)
    *   [func Asin(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Asin)
    *   [func Asinh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Asinh)
    *   [func Atan(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Atan)
    *   [func Atanh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Atanh)
    *   [func Cos(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Cos)
    *   [func Cosh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Cosh)
    *   [func Exp(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Exp)
    *   [func Inv(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Inv)
    *   [func Log(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Log)
    *   [func Mul(x, y Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Mul)
    *   [func Pow(d, p Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Pow)
    *   [func PowReal(d Number, p float64) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#PowReal)
    *   [func Scale(f float64, d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Scale)
    *   [func Sin(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Sin)
    *   [func Sinh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Sinh)
    *   [func Sqrt(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Sqrt)
    *   [func Sub(x, y Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Sub)
    *   [func Tan(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Tan)
    *   [func Tanh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Tanh)

*       *   [func (d Number) Format(fs fmt.State, c rune)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number.Format)

*   [Number (Fike)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#example-Number-Fike)

This section is empty.

This section is empty.

This section is empty.

type Number struct {
 Real, Emag [float64](https://pkg.go.dev/builtin#float64)}

Number is a float64 precision dual number.

Output:

 v=(4.4978+4.0534ϵ) fn(1.5)=4.4978 fn'(1.5)=4.0534 

func Abs(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Abs returns the absolute value of d.

func Acos(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Acos returns the inverse cosine of d.

Special cases are:

Acos(-1) = (Pi-Infϵ)
Acos(1) = (0-Infϵ)
Acos(x) = NaN if x < -1 or x > 1

func Acosh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Acosh returns the inverse hyperbolic cosine of d.

Special cases are:

Acosh(+Inf) = +Inf
Acosh(1) = (0+Infϵ)
Acosh(x) = NaN if x < 1
Acosh(NaN) = NaN

func Add(x, y [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Add returns the sum of x and y.

func Asin(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Asin returns the inverse sine of d.

Special cases are:

Asin(±0) = (±0+Nϵ)
Asin(±1) = (±Inf+Infϵ)
Asin(x) = NaN if x < -1 or x > 1

func Asinh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Asinh returns the inverse hyperbolic sine of d.

Special cases are:

Asinh(±0) = (±0+Nϵ)
Asinh(±Inf) = ±Inf
Asinh(NaN) = NaN

func Atan(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Atan returns the inverse tangent of d.

Special cases are:

Atan(±0) = (±0+Nϵ)
Atan(±Inf) = (±Pi/2+0ϵ)

func Atanh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Atanh returns the inverse hyperbolic tangent of d.

Special cases are:

Atanh(1) = +Inf
Atanh(±0) = (±0+Nϵ)
Atanh(-1) = -Inf
Atanh(x) = NaN if x < -1 or x > 1
Atanh(NaN) = NaN

func Cos(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Cos returns the cosine of d.

Special cases are:

Cos(±Inf) = NaN
Cos(NaN) = NaN

func Cosh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Cosh returns the hyperbolic cosine of d.

Special cases are:

Cosh(±0) = 1
Cosh(±Inf) = +Inf
Cosh(NaN) = NaN

func Exp(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Exp returns e**q, the base-e exponential of d.

Special cases are:

Exp(+Inf) = +Inf
Exp(NaN) = NaN

Very large values overflow to 0 or +Inf. Very small values underflow to 1.

func Inv(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Inv returns the dual inverse of d.

Special cases are:

Inv(±Inf) = ±0-0ϵ
Inv(±0) = ±Inf-Infϵ

func Log(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Log returns the natural logarithm of d.

Special cases are:

Log(+Inf) = (+Inf+0ϵ)
Log(0) = (-Inf±Infϵ)
Log(x < 0) = NaN
Log(NaN) = NaN

func Mul(x, y [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Mul returns the dual product of x and y.

func Pow(d, p [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Pow returns d**r, the base-d exponential of r.

PowReal returns x**p, the base-x exponential of p.

Special cases are (in order):

PowReal(NaN+xϵ, ±0) = 1+NaNϵ for any x
PowReal(x, ±0) = 1 for any x
PowReal(1+xϵ, y) = 1+xyϵ for any y
PowReal(x, 1) = x for any x
PowReal(NaN+xϵ, y) = NaN+NaNϵ
PowReal(x, NaN) = NaN+NaNϵ
PowReal(±0, y) = ±Inf for y an odd integer < 0
PowReal(±0, -Inf) = +Inf
PowReal(±0, +Inf) = +0
PowReal(±0, y) = +Inf for finite y < 0 and not an odd integer
PowReal(±0, y) = ±0 for y an odd integer > 0
PowReal(±0, y) = +0 for finite y > 0 and not an odd integer
PowReal(-1, ±Inf) = 1
PowReal(x+0ϵ, +Inf) = +Inf+NaNϵ for |x| > 1
PowReal(x+yϵ, +Inf) = +Inf for |x| > 1
PowReal(x, -Inf) = +0+NaNϵ for |x| > 1
PowReal(x, +Inf) = +0+NaNϵ for |x| < 1
PowReal(x+0ϵ, -Inf) = +Inf+NaNϵ for |x| < 1
PowReal(x, -Inf) = +Inf-Infϵ for |x| < 1
PowReal(+Inf, y) = +Inf for y > 0
PowReal(+Inf, y) = +0 for y < 0
PowReal(-Inf, y) = Pow(-0, -y)
PowReal(x, y) = NaN+NaNϵ for finite x < 0 and finite non-integer y

Scale returns d scaled by f.

func Sin(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Sin returns the sine of d.

Special cases are:

Sin(±0) = (±0+Nϵ)
Sin(±Inf) = NaN
Sin(NaN) = NaN

func Sinh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Sinh returns the hyperbolic sine of d.

Special cases are:

Sinh(±0) = (±0+Nϵ)
Sinh(±Inf) = ±Inf
Sinh(NaN) = NaN

func Sqrt(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Sqrt returns the square root of d.

Special cases are:

Sqrt(+Inf) = +Inf
Sqrt(±0) = (±0+Infϵ)
Sqrt(x < 0) = NaN
Sqrt(NaN) = NaN

func Sub(x, y [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Sub returns the difference of x and y, x-y.

func Tan(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Tan returns the tangent of d.

Special cases are:

Tan(±0) = (±0+Nϵ)
Tan(±Inf) = NaN
Tan(NaN) = NaN

func Tanh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/dual#Number)

Tanh returns the hyperbolic tangent of d.

Special cases are:

Tanh(±0) = (±0+Nϵ)
Tanh(±Inf) = (±1+0ϵ)
Tanh(NaN) = NaN

Format implements fmt.Formatter.
