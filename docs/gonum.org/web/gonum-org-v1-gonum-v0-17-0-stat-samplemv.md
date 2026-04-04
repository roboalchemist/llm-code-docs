# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv

Title: samplemv package - gonum.org/v1/gonum/stat/samplemv - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv

Markdown Content:
Package samplemv implements advanced sampling routines from explicit and implicit probability distributions.

*   [Constants](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#pkg-constants)
*   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#pkg-variables)
*   [type Halton](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Halton)
*       *   [func (h Halton) Sample(batch *mat.Dense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Halton.Sample)

*   [type HaltonKind](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#HaltonKind)
*   [type IID](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#IID)
*       *   [func (iid IID) Sample(batch *mat.Dense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#IID.Sample)

*   [type Importance](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Importance)
*       *   [func (l Importance) SampleWeighted(batch *mat.Dense, weights []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Importance.SampleWeighted)

*   [type LatinHypercube](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#LatinHypercube)
*       *   [func (l LatinHypercube) Sample(batch *mat.Dense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#LatinHypercube.Sample)

*   [type MHProposal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#MHProposal)
*   [type MetropolisHastingser](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#MetropolisHastingser)
*       *   [func (m MetropolisHastingser) Sample(batch *mat.Dense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#MetropolisHastingser.Sample)

*   [type ProposalNormal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#ProposalNormal)
*       *   [func NewProposalNormal(sigma *mat.SymDense, src rand.Source) (*ProposalNormal, bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#NewProposalNormal)

*       *   [func (p *ProposalNormal) ConditionalLogProb(x, y []float64) (prob float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#ProposalNormal.ConditionalLogProb)
    *   [func (p *ProposalNormal) ConditionalRand(x, y []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#ProposalNormal.ConditionalRand)

*   [type Rejection](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Rejection)
*       *   [func (r *Rejection) Err() error](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Rejection.Err)
    *   [func (r *Rejection) Proposed() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Rejection.Proposed)
    *   [func (r *Rejection) Sample(batch *mat.Dense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Rejection.Sample)

*   [type SampleUniformWeighted](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#SampleUniformWeighted)
*       *   [func (w SampleUniformWeighted) SampleWeighted(batch *mat.Dense, weights []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#SampleUniformWeighted.SampleWeighted)

*   [type Sampler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Sampler)
*   [type WeightedSampler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#WeightedSampler)

ErrRejection is returned when the constant in Rejection is not sufficiently high.

This section is empty.

Halton is a type for sampling using the Halton sequence from the given distribution. The specific method for scrambling (or lack thereof) is specified by the HaltonKind. If src is not nil, it will be used to generate the randomness needed to scramble the sequence (if necessary), otherwise the rand package will be used. Halton panics if the HaltonKind is unrecognized or if q is nil.

Halton sequence random number generation is a quasi-Monte Carlo procedure where the samples are generated to be evenly spaced out across the distribution. Note that this means the sample locations are correlated with one another. The distmv.NewUnitUniform function can be used for easy sampling from the unit hypercube.

Sample generates rows(batch) samples using the Halton generation procedure.

HaltonKind specifies the type of algorithm used to generate Halton samples.

IID generates a set of independently and identically distributed samples from the input distribution.

Sample generates a set of identically and independently distributed samples.

Importance is a type for performing importance sampling using the given Target and Proposal distributions.

Importance sampling is a variance reduction technique where samples are generated from a proposal distribution, q(x), instead of the target distribution p(x). This allows relatively unlikely samples in p(x) to be generated more frequently.

The importance sampling weight at x is given by p(x)/q(x). To reduce variance, a good proposal distribution will bound this sampling weight. This implies the support of q(x) should be at least as broad as p(x), and q(x) should be "fatter tailed" than p(x).

SampleWeighted generates rows(batch) samples using the Importance sampling generation procedure.

The length of weights must equal the length of batch, otherwise Importance will panic.

LatinHypercube is a type for sampling using Latin hypercube sampling from the given distribution. If src is not nil, it will be used to generate random numbers, otherwise rand.Float64 will be used.

Latin hypercube sampling divides the cumulative distribution function into equally spaced bins and guarantees that one sample is generated per bin. Within each bin, the location is randomly sampled. The distmv.NewUnitUniform function can be used for easy sampling from the unit hypercube.

Sample generates rows(batch) samples using the LatinHypercube generation procedure.

MHProposal defines a proposal distribution for Metropolis Hastings.

MetropolisHastingser is a type for generating samples using the Metropolis Hastings algorithm ([http://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm](http://en.wikipedia.org/wiki/Metropolis%E2%80%93Hastings_algorithm)), with the given target and proposal distributions, starting at the location specified by Initial. If src != nil, it will be used to generate random numbers, otherwise rand.Float64 will be used.

Metropolis-Hastings is a Markov-chain Monte Carlo algorithm that generates samples according to the distribution specified by target using the Markov chain implicitly defined by the proposal distribution. At each iteration, a proposal point is generated randomly from the current location. This proposal point is accepted with probability

p = min(1, (target(new) * proposal(current|new)) / (target(current) * proposal(new|current)))

If the new location is accepted, it becomes the new current location. If it is rejected, the current location remains. This is the sample stored in batch, ignoring BurnIn and Rate (discussed below).

The samples in Metropolis Hastings are correlated with one another through the Markov chain. As a result, the initial value can have a significant influence on the early samples, and so, typically, the first samples generated by the chain are ignored. This is known as "burn-in", and the number of samples ignored at the beginning is specified by BurnIn. The proper BurnIn value will depend on the mixing time of the Markov chain defined by the target and proposal distributions.

Many choose to have a sampling "rate" where a number of samples are ignored in between each kept sample. This helps decorrelate the samples from one another, but also reduces the number of available samples. This value is specified by Rate. If Rate is 0 it is defaulted to 1 (keep every sample).

The initial value is NOT changed during calls to Sample.

Sample generates rows(batch) samples using the Metropolis Hastings sample generation method. The initial location is NOT updated during the call to Sample.

The number of columns in batch must equal len(m.Initial), otherwise Sample will panic.

type ProposalNormal struct {
	
}

ProposalNormal is a sampling distribution for Metropolis-Hastings. It has a fixed covariance matrix and changes the mean based on the current sampling location.

NewProposalNormal constructs a new ProposalNormal for use as a proposal distribution for Metropolis-Hastings. ProposalNormal is a multivariate normal distribution (implemented by distmv.Normal) where the covariance matrix is fixed and the mean of the distribution changes.

NewProposalNormal returns {nil, false} if the covariance matrix is not positive-definite.

ConditionalLogProb returns the probability of the first argument conditioned on being at the second argument.

p(x|y)

ConditionalLogProb panics if the input slices are not the same length or are not equal to the dimension of the covariance matrix.

#### func (*ProposalNormal) [ConditionalRand](https://github.com/gonum/gonum/blob/v0.17.0/stat/samplemv/metropolishastings.go#L206)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#ProposalNormal.ConditionalRand "Go to ProposalNormal.ConditionalRand")

ConditionalRand generates a new random location conditioned being at the location y. If the first argument is nil, a new slice is allocated and returned. Otherwise, the random location is stored in-place into the first argument, and ConditionalRand will panic if the input slice lengths differ or if they are not equal to the dimension of the covariance matrix.

Rejection is a type for sampling using the rejection sampling algorithm.

Rejection sampling generates points from the target distribution by using the proposal distribution. At each step of the algorithm, the proposed point is accepted with probability

p = target(x) / (proposal(x) * c)

where target(x) is the probability of the point according to the target distribution and proposal(x) is the probability according to the proposal distribution. The constant c must be chosen such that target(x) < proposal(x) * c for all x. The expected number of proposed samples is len(samples) * c.

The number of proposed locations during sampling can be found with a call to Proposed. If there was an error during sampling, all elements of samples are set to NaN and the error can be accessed with the Err method. If src != nil, it will be used to generate random numbers, otherwise rand.Float64 will be used.

Target may return the true (log of) the probability of the location, or it may return a value that is proportional to the probability (logprob + constant). This is useful for cases where the probability distribution is only known up to a normalization constant.

Err returns nil if the most recent call to sample was successful, and returns ErrRejection if it was not.

func (r *[Rejection](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Rejection)) Proposed() [int](https://pkg.go.dev/builtin#int)

Proposed returns the number of samples proposed during the most recent call to Sample.

Sample generates rows(batch) using the Rejection sampling generation procedure. Rejection sampling may fail if the constant is insufficiently high, as described in the type comment for Rejection. If the generation fails, the samples are set to math.NaN(), and a call to Err will return a non-nil value.

type SampleUniformWeighted struct {
[Sampler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/samplemv#Sampler)}

SampleUniformWeighted wraps a Sampler type to create a WeightedSampler where all weights are equal.

SampleWeighted generates rows(batch) samples from the embedded Sampler type and sets all of the weights equal to 1. If rows(batch) and len(weights) of weights are not equal, SampleWeighted will panic.

type Sampler interface {
 Sample(batch *[mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/mat).[Dense](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/mat#Dense)) }

Sampler generates a batch of samples according to the rule specified by the implementing type. The number of samples generated is equal to rows(batch), and the samples are stored in-place into the input.

type WeightedSampler interface {
 SampleWeighted(batch *[mat](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/mat).[Dense](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/mat#Dense), weights [][float64](https://pkg.go.dev/builtin#float64)) }

WeightedSampler generates a batch of samples and their relative weights according to the rule specified by the implementing type. The number of samples generated is equal to rows(batch), and the samples and weights are stored in-place into the inputs. The length of weights must equal rows(batch), otherwise SampleWeighted will panic.
