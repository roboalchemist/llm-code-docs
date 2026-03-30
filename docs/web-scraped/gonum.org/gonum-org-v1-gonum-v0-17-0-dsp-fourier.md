# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier

Title: fourier package - gonum.org/v1/gonum/dsp/fourier - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier

Markdown Content:
Package fourier provides functions to perform Discrete Fourier Transforms.

package main

import (
	"fmt"
	"math/cmplx"

	"gonum.org/v1/gonum/dsp/fourier"
	"gonum.org/v1/gonum/floats/scalar"
	"gonum.org/v1/gonum/mat"
)

func main() {
	// Image is a set of diagonal lines.
	image := mat.NewDense(11, 11, []float64{
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
		1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
		1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
		1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
	})

	// Make appropriately sized complex FFT.
	// Rows and columns are the same, so the same
	// CmplxFFT can be used for both axes.
	r, c := image.Dims()
	cfft := fourier.NewCmplxFFT(r)

	// Perform the first axis transform.
	rows := make([]complex128, r*c)
	for i := 0; i < r; i++ {
		row := rows[c*i : c*(i+1)]
		for j, v := range image.RawRowView(i) {
			row[j] = complex(v, 0)
		}
		cfft.Coefficients(row, row)
	}

	// Perform the second axis transform, storing
	// the result in freqs.
	freqs := mat.NewDense(c, c, nil)
	column := make([]complex128, r)
	for j := 0; j < c; j++ {
		for i := 0; i < r; i++ {
			column[i] = rows[i*c+j]
		}
		cfft.Coefficients(column, column)
		for i, v := range column {
			// Center the frequencies.
			freqs.Set(cfft.UnshiftIdx(i), cfft.UnshiftIdx(j), scalar.Round(cmplx.Abs(v), 1))
		}
	}

	fmt.Printf("%v\n", mat.Formatted(freqs))

}
Output:

 ⎡ 1.6 6.8 3.8 1.7 1.2 1.1 1.1 1.4 2.6 3.9 1.1⎤ ⎢ 6.8 27.5 14.1 5.9 4 3.2 3 3 3.9 3.2 3.9⎥ ⎢ 3.8 14.1 6.8 2.8 1.8 1.4 1.2 1.1 1.4 3.9 2.6⎥ ⎢ 1.7 5.9 2.8 1.1 0.7 0.5 0.5 0.5 1.1 3 1.4⎥ ⎢ 1.2 4 1.8 0.7 0.5 0.4 0.4 0.5 1.2 3 1.1⎥ ⎢ 1.1 3.2 1.4 0.5 0.4 40 0.4 0.5 1.4 3.2 1.1⎥ ⎢ 1.1 3 1.2 0.5 0.4 0.4 0.5 0.7 1.8 4 1.2⎥ ⎢ 1.4 3 1.1 0.5 0.5 0.5 0.7 1.1 2.8 5.9 1.7⎥ ⎢ 2.6 3.9 1.4 1.1 1.2 1.4 1.8 2.8 6.8 14.1 3.8⎥ ⎢ 3.9 3.2 3.9 3 3 3.2 4 5.9 14.1 27.5 6.8⎥ ⎣ 1.1 3.9 2.6 1.4 1.1 1.1 1.2 1.7 3.8 6.8 1.6⎦ 

package main

import (
	"fmt"
	"math/cmplx"

	"gonum.org/v1/gonum/dsp/fourier"
	"gonum.org/v1/gonum/floats/scalar"
	"gonum.org/v1/gonum/mat"
)

func main() {
	// This example shows how to perform a 2D fourier transform
	// on an image. The transform identifies the lines present
	// in the image.

	// Image is a set of diagonal lines.
	image := mat.NewDense(11, 11, []float64{
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
		1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
		1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
		1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0,
		0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
		0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1,
	})

	// Make appropriately sized real and complex FFT types.
	r, c := image.Dims()
	fft := fourier.NewFFT(c)
	cfft := fourier.NewCmplxFFT(r)

	// Only c/2+1 coefficients will be returned for
	// the real FFT.
	c = c/2 + 1

	// Perform the first axis transform.
	rows := make([]complex128, r*c)
	for i := 0; i < r; i++ {
		fft.Coefficients(rows[c*i:c*(i+1)], image.RawRowView(i))
	}

	// Perform the second axis transform, storing
	// the result in freqs.
	freqs := mat.NewDense(c, c, nil)
	column := make([]complex128, r)
	for j := 0; j < c; j++ {
		for i := 0; i < r; i++ {
			column[i] = rows[i*c+j]
		}
		cfft.Coefficients(column, column)
		for i, v := range column[:c] {
			freqs.Set(i, j, scalar.Round(cmplx.Abs(v), 1))
		}
	}

	fmt.Printf("%v\n", mat.Formatted(freqs))

}
Output:

 ⎡ 40 0.4 0.5 1.4 3.2 1.1⎤ ⎢ 0.4 0.5 0.7 1.8 4 1.2⎥ ⎢ 0.5 0.7 1.1 2.8 5.9 1.7⎥ ⎢ 1.4 1.8 2.8 6.8 14.1 3.8⎥ ⎢ 3.2 4 5.9 14.1 27.5 6.8⎥ ⎣ 1.1 1.2 1.7 3.8 6.8 1.6⎦ 

*   [func CoefficientsRadix2(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CoefficientsRadix2)
*   [func CoefficientsRadix4(seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CoefficientsRadix4)
*   [func PadRadix2(x []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#PadRadix2)
*   [func PadRadix4(x []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#PadRadix4)
*   [func SequenceRadix2(coeff []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#SequenceRadix2)
*   [func SequenceRadix4(coeff []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#SequenceRadix4)
*   [func TrimRadix2(x []complex128) (even, remains []complex128)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#TrimRadix2)
*   [func TrimRadix4(x []complex128) (even, remains []complex128)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#TrimRadix4)
*   [type CmplxFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT)
*       *   [func NewCmplxFFT(n int) *CmplxFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#NewCmplxFFT)

*       *   [func (t *CmplxFFT) Coefficients(dst, seq []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT.Coefficients)
    *   [func (t *CmplxFFT) Freq(i int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT.Freq)
    *   [func (t *CmplxFFT) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT.Len)
    *   [func (t *CmplxFFT) Reset(n int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT.Reset)
    *   [func (t *CmplxFFT) Sequence(dst, coeff []complex128) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT.Sequence)
    *   [func (t *CmplxFFT) ShiftIdx(i int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT.ShiftIdx)
    *   [func (t *CmplxFFT) UnshiftIdx(i int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT.UnshiftIdx)

*   [type DCT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DCT)
*       *   [func NewDCT(n int) *DCT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#NewDCT)

*       *   [func (t *DCT) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DCT.Len)
    *   [func (t *DCT) Reset(n int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DCT.Reset)
    *   [func (t *DCT) Transform(dst, src []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DCT.Transform)

*   [type DST](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DST)
*       *   [func NewDST(n int) *DST](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#NewDST)

*       *   [func (t *DST) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DST.Len)
    *   [func (t *DST) Reset(n int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DST.Reset)
    *   [func (t *DST) Transform(dst, src []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DST.Transform)

*   [type FFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#FFT)
*       *   [func NewFFT(n int) *FFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#NewFFT)

*       *   [func (t *FFT) Coefficients(dst []complex128, seq []float64) []complex128](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#FFT.Coefficients)
    *   [func (t *FFT) Freq(i int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#FFT.Freq)
    *   [func (t *FFT) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#FFT.Len)
    *   [func (t *FFT) Reset(n int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#FFT.Reset)
    *   [func (t *FFT) Sequence(dst []float64, coeff []complex128) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#FFT.Sequence)

*   [type QuarterWaveFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT)
*       *   [func NewQuarterWaveFFT(n int) *QuarterWaveFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#NewQuarterWaveFFT)

*       *   [func (t *QuarterWaveFFT) CosCoefficients(dst, seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT.CosCoefficients)
    *   [func (t *QuarterWaveFFT) CosSequence(dst, coeff []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT.CosSequence)
    *   [func (t *QuarterWaveFFT) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT.Len)
    *   [func (t *QuarterWaveFFT) Reset(n int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT.Reset)
    *   [func (t *QuarterWaveFFT) SinCoefficients(dst, seq []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT.SinCoefficients)
    *   [func (t *QuarterWaveFFT) SinSequence(dst, coeff []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT.SinSequence)

*   [Package (CmplxFFT2)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#example-package-CmplxFFT2)
*   [Package (FFT2)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#example-package-FFT2)
*   [CmplxFFT.Coefficients](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#example-CmplxFFT.Coefficients)
*   [FFT.Coefficients](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#example-FFT.Coefficients)
*   [FFT.Coefficients (Tone)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#example-FFT.Coefficients-Tone)

This section is empty.

This section is empty.

CoefficientsRadix2 computes the Fourier coefficients of the input sequence, converting the time series in seq into the frequency spectrum, in place and returning it. This transform is unnormalized; a call to CoefficientsRadix2 followed by a call of SequenceRadix2 will multiply the input sequence by the length of the sequence.

CoefficientsRadix2 does not allocate, requiring that FFT twiddle factors be calculated lazily. For performance reasons, this is done by successive multiplication, so numerical accuracies can accumulate for large inputs. If accuracy is needed, the FFT or CmplxFFT types should be used.

If the length of seq is not an integer power of 2, CoefficientsRadix2 will panic.

CoefficientsRadix4 computes the Fourier coefficients of the input sequence, converting the time series in seq into the frequency spectrum, in place and returning it. This transform is unnormalized; a call to CoefficientsRadix4 followed by a call of SequenceRadix4 will multiply the input sequence by the length of the sequence.

CoefficientsRadix4 does not allocate, requiring that FFT twiddle factors be calculated lazily. For performance reasons, this is done by successive multiplication, so numerical accuracies can accumulate for large inputs. If accuracy is needed, the FFT or CmplxFFT types should be used.

If the length of seq is not an integer power of 4, CoefficientsRadix4 will panic.

PadRadix2 returns the values in x in a slice that is an integer power of 2 long. If x already has an integer power of 2 length it is returned unaltered.

PadRadix4 returns the values in x in a slice that is an integer power of 4 long. If x already has an integer power of 4 length it is returned unaltered.

SequenceRadix2 computes the real periodic sequence from the Fourier coefficients, converting the frequency spectrum in coeff into a time series, in place and returning it. This transform is unnormalized; a call to CoefficientsRadix2 followed by a call of SequenceRadix2 will multiply the input sequence by the length of the sequence.

SequenceRadix2 does not allocate, requiring that FFT twiddle factors be calculated lazily. For performance reasons, this is done by successive multiplication, so numerical accuracies can accumulate for large inputs. If accuracy is needed, the FFT or CmplxFFT types should be used.

If the length of coeff is not an integer power of 2, SequenceRadix2 will panic.

SequenceRadix4 computes the real periodic sequence from the Fourier coefficients, converting the frequency spectrum in coeff into a time series, in place and returning it. This transform is unnormalized; a call to CoefficientsRadix4 followed by a call of SequenceRadix4 will multiply the input sequence by the length of the sequence.

SequenceRadix4 does not allocate, requiring that FFT twiddle factors be calculated lazily. For performance reasons, this is done by successive multiplication, so numerical accuracies can accumulate for large inputs. If accuracy is needed, the FFT or CmplxFFT types should be used.

If the length of coeff is not an integer power of 4, SequenceRadix4 will panic.

TrimRadix2 returns the largest slice of x that is has an integer power of 2 length, and a slice holding the remaining elements.

TrimRadix4 returns the largest slice of x that is has an integer power of 4 length, and a slice holding the remaining elements.

type CmplxFFT struct {
	
}

CmplxFFT implements Fast Fourier Transform and its inverse for complex sequences.

func NewCmplxFFT(n [int](https://pkg.go.dev/builtin#int)) *[CmplxFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT)

NewCmplxFFT returns an CmplxFFT initialized for work on sequences of length n.

Coefficients computes the Fourier coefficients of a complex input sequence, converting the time series in seq into the frequency spectrum, placing the result in dst and returning it. This transform is unnormalized; a call to Coefficients followed by a call of Sequence will multiply the input sequence by the length of the sequence.

If the length of seq is not t.Len(), Coefficients will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal the length of seq, Coefficients will panic. It is safe to use the same slice for dst and seq.

package main

import (
	"fmt"
	"math/cmplx"

	"gonum.org/v1/gonum/dsp/fourier"
)

func main() {
	// Samples is a set of samples over a given period.
	samples := []complex128{1, 0, 2, 0, 4, 0, 2, 0}
	period := float64(len(samples))

	// Initialize a complex FFT and perform the analysis.
	fft := fourier.NewCmplxFFT(len(samples))
	coeff := fft.Coefficients(nil, samples)

	for i := range coeff {
		// Center the spectrum.
		i = fft.ShiftIdx(i)

		fmt.Printf("freq=%v cycles/period, magnitude=%v, phase=%.4g\n",
			fft.Freq(i)*period, cmplx.Abs(coeff[i]), cmplx.Phase(coeff[i]))
	}

}
Output:

 freq=-4 cycles/period, magnitude=9, phase=0 freq=-3 cycles/period, magnitude=3, phase=3.142 freq=-2 cycles/period, magnitude=1, phase=0 freq=-1 cycles/period, magnitude=3, phase=3.142 freq=0 cycles/period, magnitude=9, phase=0 freq=1 cycles/period, magnitude=3, phase=3.142 freq=2 cycles/period, magnitude=1, phase=0 freq=3 cycles/period, magnitude=3, phase=3.142 

Freq returns the relative frequency center for coefficient i. Freq will panic if i is negative or greater than or equal to t.Len().

func (t *[CmplxFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the length of the acceptable input.

func (t *[CmplxFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#CmplxFFT)) Reset(n [int](https://pkg.go.dev/builtin#int))

Reset reinitializes the FFT for work on sequences of length n.

Sequence computes the complex periodic sequence from the Fourier coefficients, converting the frequency spectrum in coeff into a time series, placing the result in dst and returning it. This transform is unnormalized; a call to Coefficients followed by a call of Sequence will multiply the input sequence by the length of the sequence.

If the length of coeff is not t.Len(), Sequence will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal the length of coeff, Sequence will panic. It is safe to use the same slice for dst and coeff.

ShiftIdx returns a shifted index into a slice of coefficients returned by the CmplxFFT so that indexing into the coefficients places the zero frequency component at the center of the spectrum. ShiftIdx will panic if i is negative or greater than or equal to t.Len().

UnshiftIdx returns inverse of ShiftIdx. UnshiftIdx will panic if i is negative or greater than or equal to t.Len().

type DCT struct {
	
}

DCT implements Discrete Cosine Transform for real sequences.

NewDCT returns a DCT initialized for work on sequences of length n. NewDCT will panic is n is not greater than 1.

Len returns the length of the acceptable input.

func (t *[DCT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DCT)) Reset(n [int](https://pkg.go.dev/builtin#int))

Reset reinitializes the DCT for work on sequences of length n. Reset will panic is n is not greater than 1.

Transform computes the Discrete Fourier Cosine Transform of the input data, src, placing the result in dst and returning it. This transform is unnormalized; a call to Transform followed by another call to Transform will multiply the input sequence by 2*(n-1), where n is the length of the sequence.

If the length of src is not t.Len(), Transform will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal t.Len(), FFT will panic. It is safe to use the same slice for dst and src.

type DST struct {
	
}

DST implements Discrete Sine Transform for real sequences.

NewDST returns a DST initialized for work on sequences of length n.

Len returns the length of the acceptable input.

func (t *[DST](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#DST)) Reset(n [int](https://pkg.go.dev/builtin#int))

Reset reinitializes the DCT for work on sequences of length n.

Transform computes the Discrete Fourier Sine Transform of the input data, src, placing the result in dst and returning it. This transform is unnormalized; a call to Transform followed by another call to Transform will multiply the input sequence by 2*(n-1), where n is the length of the sequence.

If the length of src is not t.Len(), Transform will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal t.Len(), FFT will panic. It is safe to use the same slice for dst and src.

type FFT struct {
	
}

FFT implements Fast Fourier Transform and its inverse for real sequences.

NewFFT returns an FFT initialized for work on sequences of length n.

Coefficients computes the Fourier coefficients of the input sequence, converting the time series in seq into the frequency spectrum, placing the result in dst and returning it. This transform is unnormalized; a call to Coefficients followed by a call of Sequence will multiply the input sequence by the length of the sequence.

If the length of seq is not t.Len(), Coefficients will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal t.Len()/2+1, Coefficients will panic.

package main

import (
	"fmt"
	"math/cmplx"

	"gonum.org/v1/gonum/dsp/fourier"
)

func main() {
	// Samples is a set of samples over a given period.
	samples := []float64{1, 0, 2, 0, 4, 0, 2, 0}
	period := float64(len(samples))

	// Initialize an FFT and perform the analysis.
	fft := fourier.NewFFT(len(samples))
	coeff := fft.Coefficients(nil, samples)

	for i, c := range coeff {
		fmt.Printf("freq=%v cycles/period, magnitude=%v, phase=%.4g\n",
			fft.Freq(i)*period, cmplx.Abs(c), cmplx.Phase(c))
	}

}
Output:

 freq=0 cycles/period, magnitude=9, phase=0 freq=1 cycles/period, magnitude=3, phase=3.142 freq=2 cycles/period, magnitude=1, phase=-0 freq=3 cycles/period, magnitude=3, phase=3.142 freq=4 cycles/period, magnitude=9, phase=0 

package main

import (
	"fmt"
	"math"
	"math/cmplx"

	"gonum.org/v1/gonum/dsp/fourier"
)

func main() {
	// Tone is a set of samples over a second of a pure Middle C.
	const (
		mC      = 261.625565 // Hz
		samples = 44100
	)
	tone := make([]float64, samples)
	for i := range tone {
		tone[i] = math.Sin(mC * 2 * math.Pi * float64(i) / samples)
	}

	// Initialize an FFT and perform the analysis.
	fft := fourier.NewFFT(samples)
	coeff := fft.Coefficients(nil, tone)

	var maxFreq, magnitude, mean float64
	for i, c := range coeff {
		m := cmplx.Abs(c)
		mean += m
		if m > magnitude {
			magnitude = m
			maxFreq = fft.Freq(i) * samples
		}
	}
	fmt.Printf("freq=%v Hz, magnitude=%.0f, mean=%.4f\n", maxFreq, magnitude, mean/samples)

}
Output:

 freq=262 Hz, magnitude=17296, mean=2.7835 

Freq returns the relative frequency center for coefficient i. Freq will panic if i is negative or greater than or equal to t.Len().

Len returns the length of the acceptable input.

func (t *[FFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#FFT)) Reset(n [int](https://pkg.go.dev/builtin#int))

Reset reinitializes the FFT for work on sequences of length n.

Sequence computes the real periodic sequence from the Fourier coefficients, converting the frequency spectrum in coeff into a time series, placing the result in dst and returning it. This transform is unnormalized; a call to Coefficients followed by a call of Sequence will multiply the input sequence by the length of the sequence.

If the length of coeff is not t.Len()/2+1, Sequence will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal the length of coeff, Sequence will panic.

type QuarterWaveFFT struct {
	
}

QuarterWaveFFT implements Fast Fourier Transform for quarter wave data.

func NewQuarterWaveFFT(n [int](https://pkg.go.dev/builtin#int)) *[QuarterWaveFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT)

NewQuarterWaveFFT returns a QuarterWaveFFT initialized for work on sequences of length n.

CosCoefficients computes the Fast Fourier Transform of quarter wave data for the input sequence, seq, placing the cosine series coefficients in dst and returning it. This transform is unnormalized; a call to CosCoefficients followed by a call to CosSequence will multiply the input sequence by 4*n, where n is the length of the sequence.

If the length of seq is not t.Len(), CosCoefficients will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal t.Len(), CosCoefficients will panic. It is safe to use the same slice for dst and seq.

CosSequence computes the Inverse Fast Fourier Transform of quarter wave data for the input cosine series coefficients, coeff, placing the sequence data in dst and returning it. This transform is unnormalized; a call to CosSequence followed by a call to CosCoefficients will multiply the input sequence by 4*n, where n is the length of the sequence.

If the length of seq is not t.Len(), CosSequence will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal t.Len(), CosSequence will panic. It is safe to use the same slice for dst and seq.

Len returns the length of the acceptable input.

func (t *[QuarterWaveFFT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/dsp/fourier#QuarterWaveFFT)) Reset(n [int](https://pkg.go.dev/builtin#int))

Reset reinitializes the QuarterWaveFFT for work on sequences of length n.

SinCoefficients computes the Fast Fourier Transform of quarter wave data for the input sequence, seq, placing the sine series coefficients in dst and returning it. This transform is unnormalized; a call to SinCoefficients followed by a call to SinSequence will multiply the input sequence by 4*n, where n is the length of the sequence.

If the length of seq is not t.Len(), SinCoefficients will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal t.Len(), SinCoefficients will panic. It is safe to use the same slice for dst and seq.

SinSequence computes the Inverse Fast Fourier Transform of quarter wave data for the input sine series coefficients, coeff, placing the sequence data in dst and returning it. This transform is unnormalized; a call to SinSequence followed by a call to SinCoefficients will multiply the input sequence by 4*n, where n is the length of the sequence.

If the length of seq is not t.Len(), SinSequence will panic. If dst is nil, a new slice is allocated and returned. If dst is not nil and the length of dst does not equal t.Len(), SinSequence will panic. It is safe to use the same slice for dst and seq.
