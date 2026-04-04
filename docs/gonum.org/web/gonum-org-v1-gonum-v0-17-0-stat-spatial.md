# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial

Title: spatial package - gonum.org/v1/gonum/stat/spatial - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial

Markdown Content:
Package spatial provides spatial statistical functions.

*   [func GetisOrdGStar(i int, data, weights []float64, locality mat.Matrix) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial#GetisOrdGStar)
*   [func GlobalMoransI(data, weights []float64, locality mat.Matrix) (i, v, z float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial#GlobalMoransI)

*   [GetisOrdGStar](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial#example-GetisOrdGStar)
*   [GetisOrdGStar (Banded)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial#example-GetisOrdGStar-Banded)
*   [GlobalMoransI (Areal)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial#example-GlobalMoransI-Areal)
*   [GlobalMoransI (Banded)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial#example-GlobalMoransI-Banded)
*   [GlobalMoransI (Linear)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/spatial#example-GlobalMoransI-Linear)

This section is empty.

This section is empty.

GetisOrdGStar returns the Local Getis-Ord G*i statistic for element of the weighted data using the provided locality matrix. The returned value is a z-score.

G^*_i = num_i / den_i

num_i = \sum_j (w_{ij} x_j) - \bar X \sum_j w_{ij}
den_i = S \sqrt(((n \sum_j w_{ij}^2 - (\sum_j w_{ij})^2))/(n - 1))
\bar X = (\sum_j x_j) / n
S = \sqrt((\sum_j x_j^2)/n - (\bar X)^2)

GetisOrdGStar will panic if locality is not a square matrix with dimensions the same as the length of data or if i is not a valid index into data.

See doi.org/10.1111%2Fj.1538-4632.1995.tb00912.x.

Weighted Getis-Ord G*i is not currently implemented and GetisOrdGStar will panic if weights is not nil.

package main

import (
	"fmt"

	"gonum.org/v1/gonum/mat"
	"gonum.org/v1/gonum/stat/spatial"
)

func main() {
	data := []float64{0, 0, 0, 1, 1, 1, 0, 1, 0, 0}

	// The locality here describes spatial neighbor
	// relationships including self.
	locality := mat.NewDense(10, 10, []float64{
		1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
		1, 1, 1, 0, 0, 0, 0, 0, 0, 0,
		0, 1, 1, 1, 0, 0, 0, 0, 0, 0,
		0, 0, 1, 1, 1, 0, 0, 0, 0, 0,
		0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
		0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
		0, 0, 0, 0, 0, 1, 1, 1, 0, 0,
		0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
		0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
		0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
	})

	for i, v := range data {
		fmt.Printf("v=%v G*i=% .4v\n", v, spatial.GetisOrdGStar(i, data, nil, locality))
	}

}
Output:

 v=0 G*i=-1.225 v=0 G*i=-1.604 v=0 G*i=-0.2673 v=1 G*i= 1.069 v=1 G*i= 2.405 v=1 G*i= 1.069 v=0 G*i= 1.069 v=1 G*i=-0.2673 v=0 G*i=-0.2673 v=0 G*i=-1.225 

package main

import (
	"fmt"

	"gonum.org/v1/gonum/mat"
	"gonum.org/v1/gonum/stat/spatial"
)

func main() {
	data := []float64{0, 0, 0, 1, 1, 1, 0, 1, 0, 0}

	// The locality here describes spatial neighbor
	// relationships including self.
	// This example uses the band matrix representation
	// to improve time and space efficiency.
	locality := mat.NewBandDense(10, 10, 1, 1, []float64{
		0, 1, 1,
		1, 1, 1,
		1, 1, 1,
		1, 1, 1,
		1, 1, 1,
		1, 1, 1,
		1, 1, 1,
		1, 1, 1,
		1, 1, 1,
		1, 1, 0,
	})

	for i, v := range data {
		fmt.Printf("v=%v G*i=% .4v\n", v, spatial.GetisOrdGStar(i, data, nil, locality))
	}

}
Output:

 v=0 G*i=-1.225 v=0 G*i=-1.604 v=0 G*i=-0.2673 v=1 G*i= 1.069 v=1 G*i= 2.405 v=1 G*i= 1.069 v=0 G*i= 1.069 v=1 G*i=-0.2673 v=0 G*i=-0.2673 v=0 G*i=-1.225 

GlobalMoransI performs Global Moran's I calculation of spatial autocorrelation for the given data using the provided locality matrix. GlobalMoransI returns Moran's I, Var(I) and the z-score associated with those values. GlobalMoransI will panic if locality is not a square matrix with dimensions the same as the length of data.

See [https://doi.org/10.1111%2Fj.1538-4632.2007.00708.x](https://doi.org/10.1111%2Fj.1538-4632.2007.00708.x).

Weighted Global Moran's I is not currently implemented and GlobalMoransI will panic if weights is not nil.

package main

import (
	"fmt"
	"math"

	"gonum.org/v1/gonum/floats"
	"gonum.org/v1/gonum/mat"
	"gonum.org/v1/gonum/stat/spatial"
)

// Euclid is a mat.Matrix whose elements reflects the Euclidean
// distance between a series of unit-separated points strided
// to be arranged in an x by y grid.
type Euclid struct{ x, y int }

func (e Euclid) Dims() (r, c int) { return e.x * e.y, e.x * e.y }
func (e Euclid) At(i, j int) float64 {
	d := e.x * e.y
	if i < 0 || d <= i || j < 0 || d <= j {
		panic("bounds error")
	}
	if i == j {
		return 0
	}
	x := float64(j%e.x - i%e.x)
	y := float64(j/e.x - i/e.x)
	return 1 / math.Hypot(x, y)
}
func (e Euclid) T() mat.Matrix { return mat.Transpose{Matrix: e} }

func main() {
	locality := Euclid{10, 10}

	data1 := []float64{
		1, 0, 0, 1, 0, 0, 1, 0, 0, 0,
		0, 1, 1, 0, 0, 1, 0, 0, 0, 0,
		1, 0, 0, 1, 0, 0, 0, 0, 1, 0,
		0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
		1, 0, 0, 0, 0, 0, 0, 1, 0, 0,
		0, 0, 0, 0, 1, 0, 0, 0, 0, 0,
		0, 0, 1, 0, 0, 0, 1, 0, 1, 0,
		1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
		1, 0, 0, 0, 0, 0, 0, 0, 1, 0,
	}
	i1, _, z1 := spatial.GlobalMoransI(data1, nil, locality)

	data2 := []float64{
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
		0, 0, 0, 1, 1, 0, 0, 0, 0, 0,
		0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
		0, 0, 1, 1, 1, 1, 0, 0, 0, 0,
		0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
		0, 0, 0, 0, 1, 0, 0, 0, 1, 0,
		0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
		0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
		0, 0, 0, 0, 0, 0, 0, 1, 1, 1,
	}
	i2, _, z2 := spatial.GlobalMoransI(data2, nil, locality)

	fmt.Printf("%v scattered points Moran's I=%.4v z-score=%.4v\n", floats.Sum(data1), i1, z1)
	fmt.Printf("%v clustered points Moran's I=%.4v z-score=%.4v\n", floats.Sum(data2), i2, z2)

}
Output:

 24 scattered points Moran's I=-0.02999 z-score=-1.913 24 clustered points Moran's I=0.09922 z-score=10.52 

package main

import (
	"fmt"

	"gonum.org/v1/gonum/mat"
	"gonum.org/v1/gonum/stat/spatial"
)

func main() {
	data := []float64{0, 0, 0, 1, 1, 1, 0, 1, 0, 0}

	// The locality here describes spatial neighbor
	// relationships.
	// This example uses the band matrix representation
	// to improve time and space efficiency.
	locality := mat.NewBandDense(10, 10, 1, 1, []float64{
		0, 0, 1,
		1, 0, 1,
		1, 0, 1,
		1, 0, 1,
		1, 0, 1,
		1, 0, 1,
		1, 0, 1,
		1, 0, 1,
		1, 0, 1,
		1, 0, 0,
	})

	i, _, z := spatial.GlobalMoransI(data, nil, locality)

	fmt.Printf("Moran's I=%.4v z-score=%.4v\n", i, z)

}
Output:

 Moran's I=0.1111 z-score=0.6335 

package main

import (
	"fmt"

	"gonum.org/v1/gonum/mat"
	"gonum.org/v1/gonum/stat/spatial"
)

func main() {
	data := []float64{0, 0, 0, 1, 1, 1, 0, 1, 0, 0}

	// The locality here describes spatial neighbor
	// relationships.
	locality := mat.NewDense(10, 10, []float64{
		0, 1, 0, 0, 0, 0, 0, 0, 0, 0,
		1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
		0, 1, 0, 1, 0, 0, 0, 0, 0, 0,
		0, 0, 1, 0, 1, 0, 0, 0, 0, 0,
		0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
		0, 0, 0, 0, 1, 0, 1, 0, 0, 0,
		0, 0, 0, 0, 0, 1, 0, 1, 0, 0,
		0, 0, 0, 0, 0, 0, 1, 0, 1, 0,
		0, 0, 0, 0, 0, 0, 0, 1, 0, 1,
		0, 0, 0, 0, 0, 0, 0, 0, 1, 0,
	})

	i, _, z := spatial.GlobalMoransI(data, nil, locality)

	fmt.Printf("Moran's I=%.4v z-score=%.4v\n", i, z)

}
Output:

 Moran's I=0.1111 z-score=0.6335 

This section is empty.
