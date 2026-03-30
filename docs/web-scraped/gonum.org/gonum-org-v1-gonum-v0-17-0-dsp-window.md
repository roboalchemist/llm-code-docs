# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window

Title: window package - gonum.org/v1/gonum/dsp/window - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window

Markdown Content:
Package window provides a set of functions to perform the transformation of sequence by different window functions.

Window functions can be used to control spectral leakage parameters when performing a Fourier transform on a signal of limited length. See [https://en.wikipedia.org/wiki/Window_function](https://en.wikipedia.org/wiki/Window_function) for more details.

#### Spectral leakage parameters [¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#hdr-Spectral_leakage_parameters "Go to Spectral leakage parameters")

Application of window functions to an input will result in changes to the frequency content of the signal in an effect called spectral leakage. See [https://en.wikipedia.org/wiki/Spectral_leakage](https://en.wikipedia.org/wiki/Spectral_leakage).

The characteristic changes associated with each window function may be described using a set of spectral leakage parameters; β, ΔF_0, ΔF_0.5, K and ɣ_max.

The β, attenuation, coefficient of a window is the ratio of the constant component of the spectrum resulting from use of the window compared to that produced using the rectangular window, expressed in a logarithmic scale.

β_w = 20 log10(A_w / A_rect) dB

The ΔF_0 parameter describes the normalized width of the main lobe of the frequency spectrum at zero amplitude.

The ΔF_0.5 parameter describes the normalized width of the main lobe of the frequency spectrum at -3 dB (half maximum amplitude).

The K parameter describes the relative width of the main lobe of the frequency spectrum produced by the window compared with the rectangular window. The rectangular window has the lowest ΔF_0 at a value of 2.

K_w = ΔF_0_w/ΔF_0_rect.

The value of K divides windows into high resolution windows (K≤3) and low resolution windows (K>3).

The ɣ_max parameter is the maximum level of the side lobes of the normalized spectrum, in decibels.

package main

import (
	"fmt"
	"math"
	"math/cmplx"

	"gonum.org/v1/gonum/dsp/fourier"
	"gonum.org/v1/gonum/dsp/window"
)

func main() {
	// The input sequence is a 2.5 period of the Sin function.
	src := make([]float64, 20)
	k := 5 * math.Pi / float64(len(src)-1)
	for i := range src {
		src[i] = math.Sin(k * float64(i))
	}

	// Initialize an FFT and perform the analysis.
	fft := fourier.NewFFT(len(src))
	coeff := fft.Coefficients(nil, src)

	// The result shows that width of the main lobe with center
	// between frequencies 0.1 and 0.15 is small, but that the
	// height of the side lobes is large.
	fmt.Println("Rectangular window (or no window):")
	for i, c := range coeff {
		fmt.Printf("freq=%.4f\tcycles/period, magnitude=%.4f,\tphase=%.4f\n",
			fft.Freq(i), cmplx.Abs(c), cmplx.Phase(c))
	}

	// Initialize an FFT and perform the analysis on a sequence
	// transformed by the Hamming window function.
	fft = fourier.NewFFT(len(src))
	coeff = fft.Coefficients(nil, window.Hamming(src))

	// The result shows that width of the main lobe is wider,
	// but height of the side lobes is lower.
	fmt.Println("Hamming window:")
	// The magnitude of all bins has been decreased by β.
	// Generally in an analysis amplification may be omitted, but to
	// make a comparable data, the result should be amplified by -β
	// of the window function — +5.37 dB for the Hamming window.
	//  -β = 20 log_10(amplifier).
	amplifier := math.Pow(10, 5.37/20.0)
	for i, c := range coeff {
		fmt.Printf("freq=%.4f\tcycles/period, magnitude=%.4f,\tphase=%.4f\n",
			fft.Freq(i), amplifier*cmplx.Abs(c), cmplx.Phase(c))
	}
}
Output:

 Rectangular window (or no window): freq=0.0000 cycles/period, magnitude=2.2798, phase=0.0000 freq=0.0500 cycles/period, magnitude=2.6542, phase=0.1571 freq=0.1000 cycles/period, magnitude=5.3115, phase=0.3142 freq=0.1500 cycles/period, magnitude=7.3247, phase=-2.6704 freq=0.2000 cycles/period, magnitude=1.6163, phase=-2.5133 freq=0.2500 cycles/period, magnitude=0.7681, phase=-2.3562 freq=0.3000 cycles/period, magnitude=0.4385, phase=-2.1991 freq=0.3500 cycles/period, magnitude=0.2640, phase=-2.0420 freq=0.4000 cycles/period, magnitude=0.1530, phase=-1.8850 freq=0.4500 cycles/period, magnitude=0.0707, phase=-1.7279 freq=0.5000 cycles/period, magnitude=0.0000, phase=0.0000 Hamming window: freq=0.0000 cycles/period, magnitude=0.0542, phase=3.1416 freq=0.0500 cycles/period, magnitude=0.8458, phase=-2.9845 freq=0.1000 cycles/period, magnitude=7.1519, phase=0.3142 freq=0.1500 cycles/period, magnitude=8.5907, phase=-2.6704 freq=0.2000 cycles/period, magnitude=2.0804, phase=0.6283 freq=0.2500 cycles/period, magnitude=0.0816, phase=0.7854 freq=0.3000 cycles/period, magnitude=0.0156, phase=-2.1991 freq=0.3500 cycles/period, magnitude=0.0224, phase=-2.0420 freq=0.4000 cycles/period, magnitude=0.0163, phase=-1.8850 freq=0.4500 cycles/period, magnitude=0.0083, phase=-1.7279 freq=0.5000 cycles/period, magnitude=0.0000, phase=0.0000 

*   [func BartlettHann(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#BartlettHann)
*   [func BartlettHannComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#BartlettHannComplex)
*   [func Blackman(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Blackman)
*   [func BlackmanComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#BlackmanComplex)
*   [func BlackmanHarris(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#BlackmanHarris)
*   [func BlackmanHarrisComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#BlackmanHarrisComplex)
*   [func BlackmanNuttall(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#BlackmanNuttall)
*   [func BlackmanNuttallComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#BlackmanNuttallComplex)
*   [func FlatTop(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#FlatTop)
*   [func FlatTopComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#FlatTopComplex)
*   [func Hamming(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Hamming)
*   [func HammingComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#HammingComplex)
*   [func Hann(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Hann)
*   [func HannComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#HannComplex)
*   [func Lanczos(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Lanczos)
*   [func LanczosComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#LanczosComplex)
*   [func Nuttall(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Nuttall)
*   [func NuttallComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#NuttallComplex)
*   [func Rectangular(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Rectangular)
*   [func RectangularComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#RectangularComplex)
*   [func Sine(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Sine)
*   [func SineComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#SineComplex)
*   [func Triangular(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Triangular)
*   [func TriangularComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#TriangularComplex)
*   [type Gaussian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Gaussian)
*       *   [func (g Gaussian) Transform(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Gaussian.Transform)
    *   [func (g Gaussian) TransformComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Gaussian.TransformComplex)

*   [type Tukey](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Tukey)
*       *   [func (t Tukey) Transform(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Tukey.Transform)
    *   [func (t Tukey) TransformComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Tukey.TransformComplex)

*   [type Values](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Values)
*       *   [func NewValues(window func([]float64) []float64, n int) Values](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#NewValues)

*       *   [func (v Values) Transform(seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Values.Transform)
    *   [func (v Values) TransformComplex(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Values.TransformComplex)
    *   [func (v Values) TransformComplexTo(dst, src []complex128)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Values.TransformComplexTo)
    *   [func (v Values) TransformTo(dst, src []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Values.TransformTo)

*   [Package](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#example-package)
*   [Hamming](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#example-Hamming)
*   [Values](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#example-Values)
*   [Values.TransformTo (Gabor)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#example-Values.TransformTo-Gabor)

This section is empty.

This section is empty.

FlatTop modifies seq in place by the Flat Top window and returns the result. See [https://en.wikipedia.org/wiki/Window_function#Flat_top_window](https://en.wikipedia.org/wiki/Window_function#Flat_top_window) and [https://www.recordingblogs.com/wiki/flat-top-window](https://www.recordingblogs.com/wiki/flat-top-window) for details.

The Flat Top window is a low-resolution window.

The sequence weights are

w[k] = 0.21557895 - 0.41663158*cos(2*π*k/(N-1)) +
       0.277263158*cos(4*π*k/(N-1)) - 0.083578947*cos(6*π*k/(N-1)) +
       0.006947368*cos(4*π*k/(N-1)),

for k=0,1,...,N-1 where N is the length of the window.

Spectral leakage parameters: ΔF_0 = 10, ΔF_0.5 = 3.72, K = 5, ɣ_max = -93.0, β = -13.34.

FlatTopComplex modifies seq in place by the Flat Top window and returns the result. See [https://en.wikipedia.org/wiki/Window_function#Flat_top_window](https://en.wikipedia.org/wiki/Window_function#Flat_top_window) and [https://www.recordingblogs.com/wiki/flat-top-window](https://www.recordingblogs.com/wiki/flat-top-window) for details.

The Flat Top window is a low-resolution window.

The sequence weights are

w[k] = 0.21557895 - 0.41663158*cos(2*π*k/(N-1)) +
       0.277263158*cos(4*π*k/(N-1)) - 0.083578947*cos(6*π*k/(N-1)) +
       0.006947368*cos(4*π*k/(N-1)),

for k=0,1,...,N-1 where N is the length of the window.

Spectral leakage parameters: ΔF_0 = 10, ΔF_0.5 = 3.72, K = 5, ɣ_max = -93.0, β = -13.34.

Hamming modifies seq in place by the Hamming window and returns the result. See [https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows](https://en.wikipedia.org/wiki/Window_function#Hann_and_Hamming_windows) and [https://www.recordingblogs.com/wiki/hamming-window](https://www.recordingblogs.com/wiki/hamming-window) for details.

The Hamming window is a high-resolution window. Among K=2 windows it has the highest ɣ_max.

The sequence weights are

w[k] = 25/46 - 21/46 * cos(2*π*k/(N-1)),

for k=0,1,...,N-1 where N is the length of the window.

Spectral leakage parameters: ΔF_0 = 4, ΔF_0.5 = 1.33, K = 2, ɣ_max = -42, β = -5.37.

package main

import (
	"fmt"

	"gonum.org/v1/gonum/dsp/window"
)

func main() {
	src := []float64{1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
		1, 1, 1, 1, 1, 1, 1, 1, 1, 1}

	// Window functions change data in place. So, if input data
	// needs to stay unchanged, it must be copied.
	srcCpy := append([]float64(nil), src...)
	// Apply window function to srcCpy.
	dst := window.Hamming(srcCpy)

	// src is unchanged.
	fmt.Printf("src:    %f\n", src)
	// srcCpy is altered.
	fmt.Printf("srcCpy: %f\n", srcCpy)
	// dst mirrors the srcCpy slice.
	fmt.Printf("dst:    %f\n", dst)

}
Output:

 src: [1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000 1.000000] srcCpy: [0.080000 0.104924 0.176995 0.288404 0.427077 0.577986 0.724780 0.851550 0.944558 0.993726 0.993726 0.944558 0.851550 0.724780 0.577986 0.427077 0.288404 0.176995 0.104924 0.080000] dst: [0.080000 0.104924 0.176995 0.288404 0.427077 0.577986 0.724780 0.851550 0.944558 0.993726 0.993726 0.944558 0.851550 0.724780 0.577986 0.427077 0.288404 0.176995 0.104924 0.080000] 

Rectangular modifies seq in place by the Rectangular window and returns the result. See [https://en.wikipedia.org/wiki/Window_function#Rectangular_window](https://en.wikipedia.org/wiki/Window_function#Rectangular_window) and [https://www.recordingblogs.com/wiki/rectangular-window](https://www.recordingblogs.com/wiki/rectangular-window) for details.

The rectangular window has the lowest width of the main lobe and largest level of the side lobes. The result corresponds to a selection of limited length sequence of values without any modification.

The sequence weights are

w[k] = 1,

for k=0,1,...,N-1 where N is the length of the window.

Spectral leakage parameters: ΔF_0 = 2, ΔF_0.5 = 0.89, K = 1, ɣ_max = -13, β = 0.

RectangularComplex modifies seq in place by the Rectangular window and returns the result. See [https://en.wikipedia.org/wiki/Window_function#Rectangular_window](https://en.wikipedia.org/wiki/Window_function#Rectangular_window) and [https://www.recordingblogs.com/wiki/rectangular-window](https://www.recordingblogs.com/wiki/rectangular-window) for details.

The rectangular window has the lowest width of the main lobe and largest level of the side lobes. The result corresponds to a selection of limited length sequence of values without any modification.

The sequence weights are

w[k] = 1,

for k=0,1,...,N-1 where N is the length of the window.

Spectral leakage parameters: ΔF_0 = 2, ΔF_0.5 = 0.89, K = 1, ɣ_max = -13, β = 0.

type Gaussian struct {
 Sigma [float64](https://pkg.go.dev/builtin#float64)}

Gaussian can modify a sequence using the Gaussian window and return the result. See [https://en.wikipedia.org/wiki/Window_function#Gaussian_window](https://en.wikipedia.org/wiki/Window_function#Gaussian_window) and [https://www.recordingblogs.com/wiki/gaussian-window](https://www.recordingblogs.com/wiki/gaussian-window) for details.

The Gaussian window is an adjustable window.

The sequence weights are

w[k] = exp(-0.5 * ((k-M)/(σ*M))² ), M = (N-1)/2,

for k=0,1,...,N-1 where N is the length of the window.

The properties of the window depend on the value of σ (sigma). It can be used as high or low resolution window, depending of the σ value.

Spectral leakage parameters are summarized in the table:

       |  σ=0.3  |  σ=0.5 |  σ=1.2 |
-------|---------------------------|
ΔF_0   |   8     |   3.4  |   2.2  |
ΔF_0.5 |   1.82  |   1.2  |   0.94 |
K      |   4     |   1.7  |   1.1  |
ɣ_max  | -65     | -31.5  | -15.5  |
β      |  -8.52  |  -4.48 |  -0.96 |

Transform applies the Gaussian transformation to seq in place, using the value of the receiver as the sigma parameter, and returning the result.

TransformComplex applies the Gaussian transformation to seq in place, using the value of the receiver as the sigma parameter, and returning the result.

type Tukey struct {
 Alpha [float64](https://pkg.go.dev/builtin#float64)}

Tukey can modify a sequence using the Tukey window and return the result. See [https://en.wikipedia.org/wiki/Window_function#Tukey_window](https://en.wikipedia.org/wiki/Window_function#Tukey_window) and [https://www.recordingblogs.com/wiki/tukey-window](https://www.recordingblogs.com/wiki/tukey-window) for details.

The Tukey window is an adjustable window.

The sequence weights are

w[k] = 0.5 * (1 + cos(π*(|k - M| - αM)/((1-α) * M))), |k - M| ≥ αM
     = 1, |k - M| < αM

with M = (N - 1)/2 for k=0,1,...,N-1 where N is the length of the window.

Spectral leakage parameters are summarized in the table:

       |  α=0.3 |  α=0.5 |  α=0.7 |
-------|--------------------------|
ΔF_0   |   1.33 |   1.22 |   1.13 |
ΔF_0.5 |   1.28 |   1.16 |   1.04 |
K      |   0.67 |   0.61 |   0.57 |
ɣ_max  | -18.2  | -15.1  | -13.8  |
β      |  -1.41 |  -2.50 |  -3.74 |

Transform applies the Tukey transformation to seq in place, using the value of the receiver as the Alpha parameter, and returning the result.

TransformComplex applies the Tukey transformation to seq in place, using the value of the receiver as the Alpha parameter, and returning the result.

Values is an arbitrary real window function.

package main

import (
	"fmt"

	"gonum.org/v1/gonum/dsp/window"
)

func main() {
	src := []float64{1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
		1, 1, 1, 1, 1, 1, 1, 1, 1, 1}

	// Create a Sine Window lookup table.
	sine := window.NewValues(window.Sine, len(src))

	// Apply the transformation to the src.
	fmt.Printf("dst: %f\n", sine.Transform(src))

}
Output:

 dst: [0.000000 0.164595 0.324699 0.475947 0.614213 0.735724 0.837166 0.915773 0.969400 0.996584 0.996584 0.969400 0.915773 0.837166 0.735724 0.614213 0.475947 0.324699 0.164595 0.000000] 

NewValues returns a Values of length n with weights corresponding to the provided window function.

Transform applies the weights in the receiver to seq in place, returning the result. If v is nil, Transform is a no-op, otherwise the length of v must match the length of seq.

TransformComplex applies the weights in the receiver to seq in place, returning the result. If v is nil, TransformComplex is a no-op, otherwise the length of v must match the length of seq.

TransformComplexTo applies the weights in the receiver to src placing the result in dst. If v is nil, TransformComplexTo is a no-op, otherwise the length of v must match the length of src and dst.

func (v [Values](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/window#Values)) TransformTo(dst, src [][float64](https://pkg.go.dev/builtin#float64))

TransformTo applies the weights in the receiver to src placing the result in dst. If v is nil, TransformTo is a no-op, otherwise the length of v must match the length of src and dst.

package main

import (
	"fmt"

	"gonum.org/v1/gonum/dsp/window"
)

func main() {
	src := []float64{1, 2, 1, 0, -1, -1, -2, -2, -1, -1,
		0, 1, 1, 2, 1, 0, -1, -2, -1, 0}

	// Create a Gaussian Window lookup table for 4 samples.
	gaussian := window.NewValues(window.Gaussian{0.5}.Transform, 4)

	// Prepare a destination.
	dst := make([]float64, 8)

	// Apply the transformation to the src, placing it in dst.
	for i := 0; i < len(src)-len(gaussian); i++ {
		gaussian.TransformTo(dst[0:len(gaussian)], src[i:i+len(gaussian)])

		// To perform the Gabor transform, we would calculate
		// the FFT on dst for each iteration.
		fmt.Printf("FFT(%f)\n", dst)
	}

}
Output:

 FFT([0.135335 1.601475 0.800737 0.000000 0.000000 0.000000 0.000000 0.000000]) FFT([0.270671 0.800737 0.000000 -0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([0.135335 0.000000 -0.800737 -0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([0.000000 -0.800737 -0.800737 -0.270671 0.000000 0.000000 0.000000 0.000000]) FFT([-0.135335 -0.800737 -1.601475 -0.270671 0.000000 0.000000 0.000000 0.000000]) FFT([-0.135335 -1.601475 -1.601475 -0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([-0.270671 -1.601475 -0.800737 -0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([-0.270671 -0.800737 -0.800737 0.000000 0.000000 0.000000 0.000000 0.000000]) FFT([-0.135335 -0.800737 0.000000 0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([-0.135335 0.000000 0.800737 0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([0.000000 0.800737 0.800737 0.270671 0.000000 0.000000 0.000000 0.000000]) FFT([0.135335 0.800737 1.601475 0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([0.135335 1.601475 0.800737 0.000000 0.000000 0.000000 0.000000 0.000000]) FFT([0.270671 0.800737 0.000000 -0.135335 0.000000 0.000000 0.000000 0.000000]) FFT([0.135335 0.000000 -0.800737 -0.270671 0.000000 0.000000 0.000000 0.000000]) FFT([0.000000 -0.800737 -1.601475 -0.135335 0.000000 0.000000 0.000000 0.000000])
