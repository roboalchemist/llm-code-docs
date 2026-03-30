# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual

Title: hyperdual package - gonum.org/v1/gonum/num/hyperdual - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual

Markdown Content:
Package hyperdual provides the hyperdual numeric type and functions. Hyperdual numbers are an extension of the real numbers in the form a+bϵ₁+bϵ₂+dϵ₁ϵ₂ where ϵ₁^2=0 and ϵ₂^2=0, but ϵ₁≠0, ϵ₂≠0 and ϵ₁ϵ₂≠0.

See [https://doi.org/10.2514/6.2011-886](https://doi.org/10.2514/6.2011-886) and [http://adl.stanford.edu/hyperdual/](http://adl.stanford.edu/hyperdual/) for details of their properties and uses.

*   [type Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)
*       *   [func Abs(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Abs)
    *   [func Acos(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Acos)
    *   [func Acosh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Acosh)
    *   [func Add(x, y Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Add)
    *   [func Asin(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Asin)
    *   [func Asinh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Asinh)
    *   [func Atan(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Atan)
    *   [func Atanh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Atanh)
    *   [func Cos(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Cos)
    *   [func Cosh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Cosh)
    *   [func Exp(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Exp)
    *   [func Inv(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Inv)
    *   [func Log(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Log)
    *   [func Mul(x, y Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Mul)
    *   [func Pow(d, p Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Pow)
    *   [func PowReal(d Number, p float64) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#PowReal)
    *   [func Scale(f float64, d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Scale)
    *   [func Sin(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Sin)
    *   [func Sinh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Sinh)
    *   [func Sqrt(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Sqrt)
    *   [func Sub(x, y Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Sub)
    *   [func Tan(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Tan)
    *   [func Tanh(d Number) Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Tanh)

*       *   [func (d Number) Format(fs fmt.State, c rune)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number.Format)

*   [Number (Fike)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#example-Number-Fike)

This section is empty.

This section is empty.

This section is empty.

type Number struct {
 Real, E1mag, E2mag, E1E2mag [float64](https://pkg.go.dev/builtin#float64)}

Number is a float64 precision hyperdual number.

Output:

 v=(4.4978+4.0534ϵ₁+4.0534ϵ₂+9.4631ϵ₁ϵ₂) fn(1.5)=4.4978 fn′(1.5)=4.0534 fn′′(1.5)=9.4631 

func Abs(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Abs returns the absolute value of d.

func Acos(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Acos returns the inverse cosine of d.

Special cases are:

Acos(-1) = (Pi-Infϵ₁-Infϵ₂+Infϵ₁ϵ₂)
Acos(1) = (0-Infϵ₁-Infϵ₂-Infϵ₁ϵ₂)
Acos(x) = NaN if x < -1 or x > 1

func Acosh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Acosh returns the inverse hyperbolic cosine of d.

Special cases are:

Acosh(+Inf) = +Inf
Acosh(1) = (0+Infϵ₁+Infϵ₂-Infϵ₁ϵ₂)
Acosh(x) = NaN if x < 1
Acosh(NaN) = NaN

func Add(x, y [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Add returns the sum of x and y.

func Asin(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Asin returns the inverse sine of d.

Special cases are:

Asin(±0) = (±0+Nϵ₁+Nϵ₂±0ϵ₁ϵ₂)
Asin(±1) = (±Inf+Infϵ₁+Infϵ₂±Infϵ₁ϵ₂)
Asin(x) = NaN if x < -1 or x > 1

func Asinh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Asinh returns the inverse hyperbolic sine of d.

Special cases are:

Asinh(±0) = (±0+Nϵ₁+Nϵ₂∓0ϵ₁ϵ₂)
Asinh(±Inf) = ±Inf
Asinh(NaN) = NaN

func Atan(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Atan returns the inverse tangent of d.

Special cases are:

Atan(±0) = (±0+Nϵ₁+Nϵ₂∓0ϵ₁ϵ₂)
Atan(±Inf) = (±Pi/2+0ϵ₁+0ϵ₂∓0ϵ₁ϵ₂)

func Atanh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Atanh returns the inverse hyperbolic tangent of d.

Special cases are:

Atanh(1) = +Inf
Atanh(±0) = (±0+Nϵ₁+Nϵ₂±0ϵ₁ϵ₂)
Atanh(-1) = -Inf
Atanh(x) = NaN if x < -1 or x > 1
Atanh(NaN) = NaN

func Cos(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Cos returns the cosine of d.

Special cases are:

Cos(±Inf) = NaN
Cos(NaN) = NaN

func Cosh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Cosh returns the hyperbolic cosine of d.

Special cases are:

Cosh(±0) = 1
Cosh(±Inf) = +Inf
Cosh(NaN) = NaN

func Exp(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Exp returns e**q, the base-e exponential of d.

Special cases are:

Exp(+Inf) = +Inf
Exp(NaN) = NaN

Very large values overflow to 0 or +Inf. Very small values underflow to 1.

func Inv(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Inv returns the hyperdual inverse of d.

Special cases are:

Inv(±Inf) = ±0-0ϵ₁-0ϵ₂±0ϵ₁ϵ₂
Inv(±0) = ±Inf-Infϵ₁-Infϵ₂±Infϵ₁ϵ₂

func Log(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Log returns the natural logarithm of d.

Special cases are:

Log(+Inf) = (+Inf+0ϵ₁+0ϵ₂-0ϵ₁ϵ₂)
Log(0) = (-Inf±Infϵ₁±Infϵ₂-Infϵ₁ϵ₂)
Log(x < 0) = NaN
Log(NaN) = NaN

func Mul(x, y [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Mul returns the hyperdual product of x and y.

func Pow(d, p [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Pow returns x**p, the base-x exponential of p.

PowReal returns x**p, the base-x exponential of p.

Special cases are (in order):

PowReal(NaN+xϵ₁+yϵ₂, ±0) = 1+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂ for any x and y
PowReal(x, ±0) = 1 for any x
PowReal(1+xϵ₁+yϵ₂, z) = 1+xzϵ₁+yzϵ₂+2xyzϵ₁ϵ₂ for any z
PowReal(NaN+xϵ₁+yϵ₂, 1) = NaN+xϵ₁+yϵ₂+NaNϵ₁ϵ₂ for any x
PowReal(x, 1) = x for any x
PowReal(NaN+xϵ₁+xϵ₂, y) = NaN+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂
PowReal(x, NaN) = NaN+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂
PowReal(±0, y) = ±Inf for y an odd integer < 0
PowReal(±0, -Inf) = +Inf
PowReal(±0, +Inf) = +0
PowReal(±0, y) = +Inf for finite y < 0 and not an odd integer
PowReal(±0, y) = ±0 for y an odd integer > 0
PowReal(±0, y) = +0 for finite y > 0 and not an odd integer
PowReal(-1, ±Inf) = 1
PowReal(x+0ϵ₁+0ϵ₂, +Inf) = +Inf+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂ for |x| > 1
PowReal(x+xϵ₁+yϵ₂, +Inf) = +Inf+Infϵ₁+Infϵ₂+NaNϵ₁ϵ₂ for |x| > 1
PowReal(x, -Inf) = +0+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂ for |x| > 1
PowReal(x+yϵ₁+zϵ₂, +Inf) = +0+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂ for |x| < 1
PowReal(x+0ϵ₁+0ϵ₂, -Inf) = +Inf+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂ for |x| < 1
PowReal(x, -Inf) = +Inf-Infϵ₁-Infϵ₂+NaNϵ₁ϵ₂ for |x| < 1
PowReal(+Inf, y) = +Inf for y > 0
PowReal(+Inf, y) = +0 for y < 0
PowReal(-Inf, y) = Pow(-0, -y)
PowReal(x, y) = NaN+NaNϵ₁+NaNϵ₂+NaNϵ₁ϵ₂ for finite x < 0 and finite non-integer y

Scale returns d scaled by f.

func Sin(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Sin returns the sine of d.

Special cases are:

Sin(±0) = (±0+Nϵ₁+Nϵ₂∓0ϵ₁ϵ₂)
Sin(±Inf) = NaN
Sin(NaN) = NaN

func Sinh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Sinh returns the hyperbolic sine of d.

Special cases are:

Sinh(±0) = (±0+Nϵ₁+Nϵ₂±0ϵ₁ϵ₂)
Sinh(±Inf) = ±Inf
Sinh(NaN) = NaN

func Sqrt(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Sqrt returns the square root of d.

Special cases are:

Sqrt(+Inf) = +Inf
Sqrt(±0) = (±0+Infϵ₁+Infϵ₂-Infϵ₁ϵ₂)
Sqrt(x < 0) = NaN
Sqrt(NaN) = NaN

func Sub(x, y [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Sub returns the difference of x and y, x-y.

func Tan(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Tan returns the tangent of d.

Special cases are:

Tan(±0) = (±0+Nϵ₁+Nϵ₂±0ϵ₁ϵ₂)
Tan(±Inf) = NaN
Tan(NaN) = NaN

func Tanh(d [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)) [Number](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/num/hyperdual#Number)

Tanh returns the hyperbolic tangent of d.

Special cases are:

Tanh(±0) = (±0+Nϵ₁+Nϵ₂∓0ϵ₁ϵ₂)
Tanh(±Inf) = (±1+0ϵ₁+0ϵ₂∓0ϵ₁ϵ₂)
Tanh(NaN) = NaN

Format implements fmt.Formatter.
