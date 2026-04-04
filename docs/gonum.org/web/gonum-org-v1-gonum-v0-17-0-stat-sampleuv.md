# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv

Title: sampleuv package - gonum.org/v1/gonum/stat/sampleuv - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv

Markdown Content:
Package sampleuv implements advanced sampling routines from explicit and implicit probability distributions.

Each sampling routine is implemented as a stateless function with a complementary wrapper type. The wrapper types allow the sampling routines to implement interfaces.

*   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#pkg-variables)
*   [func WithoutReplacement(idxs []int, n int, src rand.Source)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#WithoutReplacement)
*   [type IIDer](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#IIDer)
*       *   [func (iid IIDer) Sample(batch []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#IIDer.Sample)

*   [type Importance](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Importance)
*       *   [func (l Importance) SampleWeighted(batch, weights []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Importance.SampleWeighted)

*   [type LatinHypercube](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#LatinHypercube)
*       *   [func (l LatinHypercube) Sample(batch []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#LatinHypercube.Sample)

*   [type MHProposal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#MHProposal)
*   [type MetropolisHastings](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#MetropolisHastings)
*       *   [func (m MetropolisHastings) Sample(batch []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#MetropolisHastings.Sample)

*   [type Rejection](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Rejection)
*       *   [func (r *Rejection) Err() error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Rejection.Err)
    *   [func (r *Rejection) Proposed() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Rejection.Proposed)
    *   [func (r *Rejection) Sample(batch []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Rejection.Sample)

*   [type SampleUniformWeighted](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#SampleUniformWeighted)
*       *   [func (w SampleUniformWeighted) SampleWeighted(batch, weights []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#SampleUniformWeighted.SampleWeighted)

*   [type Sampler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Sampler)
*   [type Weighted](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Weighted)
*       *   [func NewWeighted(w []float64, src rand.Source) Weighted](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#NewWeighted)

*       *   [func (s Weighted) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Weighted.Len)
    *   [func (s Weighted) Reweight(idx int, w float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Weighted.Reweight)
    *   [func (s Weighted) ReweightAll(w []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Weighted.ReweightAll)
    *   [func (s Weighted) Take() (idx int, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Weighted.Take)

*   [type WeightedSampler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#WeightedSampler)

*   [MetropolisHastings (Burnin)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#example-MetropolisHastings-Burnin)
*   [MetropolisHastings (SamplingRate)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#example-MetropolisHastings-SamplingRate)

This section is empty.

ErrRejection is returned when the constant in Rejection is not sufficiently high.

WithoutReplacement samples len(idxs) integers from [0, n) without replacement. That is, upon return the elements of idxs will be unique integers. If source is non-nil it will be used to generate random numbers, otherwise the default source from the math/rand package will be used.

WithoutReplacement will panic if len(idxs) > n.

IIDer generates a set of independently and identically distributed samples from the input distribution.

Sample generates a set of identically and independently distributed samples.

Importance is a type for performing importance sampling using the given Target and Proposal distributions.

Importance sampling is a variance reduction technique where samples are generated from a proposal distribution, q(x), instead of the target distribution p(x). This allows relatively unlikely samples in p(x) to be generated more frequently.

The importance sampling weight at x is given by p(x)/q(x). To reduce variance, a good proposal distribution will bound this sampling weight. This implies the support of q(x) should be at least as broad as p(x), and q(x) should be "fatter tailed" than p(x).

func (l [Importance](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Importance)) SampleWeighted(batch, weights [][float64](https://pkg.go.dev/builtin#float64))

SampleWeighted generates len(batch) samples using the Importance sampling generation procedure.

The length of weights must equal the length of batch, otherwise Importance will panic.

LatinHypercube is a type for sampling using Latin hypercube sampling from the given distribution. If src is not nil, it will be used to generate random numbers, otherwise rand.Float64 will be used.

Latin hypercube sampling divides the cumulative distribution function into equally spaced bins and guarantees that one sample is generated per bin. Within each bin, the location is randomly sampled. The distuv.UnitUniform variable can be used for easy sampling from the unit hypercube.

Sample generates len(batch) samples using the LatinHypercube generation procedure.

MHProposal defines a proposal distribution for Metropolis Hastings.

MetropolisHastings is a type for generating samples using the Metropolis Hastings algorithm ([http://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm](http://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm)), with the given target and proposal distributions, starting at the location specified by Initial. If src != nil, it will be used to generate random numbers, otherwise rand.Float64 will be used.

Metropolis-Hastings is a Markov-chain Monte Carlo algorithm that generates samples according to the distribution specified by target using the Markov chain implicitly defined by the proposal distribution. At each iteration, a proposal point is generated randomly from the current location. This proposal point is accepted with probability

p = min(1, (target(new) * proposal(current|new)) / (target(current) * proposal(new|current)))

If the new location is accepted, it becomes the new current location. If it is rejected, the current location remains. This is the sample stored in batch, ignoring BurnIn and Rate (discussed below).

The samples in Metropolis Hastings are correlated with one another through the Markov chain. As a result, the initial value can have a significant influence on the early samples, and so, typically, the first samples generated by the chain are ignored. This is known as "burn-in", and the number of samples ignored at the beginning is specified by BurnIn. The proper BurnIn value will depend on the mixing time of the Markov chain defined by the target and proposal distributions.

Many choose to have a sampling "rate" where a number of samples are ignored in between each kept sample. This helps decorrelate the samples from one another, but also reduces the number of available samples. This value is specified by Rate. If Rate is 0 it is defaulted to 1 (keep every sample).

The initial value is NOT changed during calls to Sample.

Sample generates len(batch) samples using the Metropolis Hastings sample generation method. The initial location is NOT updated during the call to Sample.

Rejection is a type for sampling using the rejection sampling algorithm.

Rejection sampling generates points from the target distribution by using the proposal distribution. At each step of the algorithm, the proposed point is accepted with probability

p = target(x) / (proposal(x) * c)

where target(x) is the probability of the point according to the target distribution and proposal(x) is the probability according to the proposal distribution. The constant c must be chosen such that target(x) < proposal(x) * c for all x. The expected number of proposed samples is len(samples) * c.

The number of proposed locations during sampling can be found with a call to Proposed. If there was an error during sampling, all elements of samples are set to NaN and the error can be accessed with the Err method. If src != nil, it will be used to generate random numbers, otherwise rand.Float64 will be used.

Target may return the true (log of) the probability of the location, or it may return a value that is proportional to the probability (logprob + constant). This is useful for cases where the probability distribution is only known up to a normalization constant.

Err returns nil if the most recent call to sample was successful, and returns ErrRejection if it was not.

func (r *[Rejection](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Rejection)) Proposed() [int](https://pkg.go.dev/builtin#int)

Proposed returns the number of samples proposed during the most recent call to Sample.

Sample generates len(batch) using the Rejection sampling generation procedure. Rejection sampling may fail if the constant is insufficiently high, as described in the type comment for Rejection. If the generation fails, the samples are set to math.NaN(), and a call to Err will return a non-nil value.

type SampleUniformWeighted struct {
[Sampler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Sampler)}

SampleUniformWeighted wraps a Sampler type to create a WeightedSampler where all weights are equal.

func (w [SampleUniformWeighted](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#SampleUniformWeighted)) SampleWeighted(batch, weights [][float64](https://pkg.go.dev/builtin#float64))

SampleWeighted generates len(batch) samples from the embedded Sampler type and sets all of the weights equal to 1. If len(batch) and len(weights) are not equal, SampleWeighted will panic.

type Sampler interface {
 Sample(batch [][float64](https://pkg.go.dev/builtin#float64)) }

Sampler generates a batch of samples according to the rule specified by the implementing type. The number of samples generated is equal to len(batch), and the samples are stored in-place into the input.

type Weighted struct {
	
}

Weighted provides sampling without replacement from a collection of items with non-uniform probability.

NewWeighted returns a Weighted for the weights w. If src is nil, rand.Rand is used as the random number generator.

Note that sampling from weights with a high variance or overall low absolute value sum may result in problems with numerical stability.

func (s [Weighted](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/sampleuv#Weighted)) Len() [int](https://pkg.go.dev/builtin#int)

Len returns the number of items held by the Weighted, including items already taken.

Reweight sets the weight of item idx to w.

ReweightAll sets the weight of all items in the Weighted. ReweightAll panics if len(w) != s.Len.

Take returns an index from the Weighted with probability proportional to the weight of the item. The weight of the item is then set to zero. Take returns false if there are no items remaining.

type WeightedSampler interface {
 SampleWeighted(batch, weights [][float64](https://pkg.go.dev/builtin#float64)) }

WeightedSampler generates a batch of samples and their relative weights according to the rule specified by the implementing type. The number of samples generated is equal to len(batch), and the samples and weights are stored in-place into the inputs. The length of weights must equal len(batch), otherwise SampleWeighted will panic.
