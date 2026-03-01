# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv

Title: distmv package - gonum.org/v1/gonum/stat/distmv - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv

Markdown Content:
Package distmv provides multivariate random distribution types.

*   [func NormalLogProb(x, mu []float64, chol *mat.Cholesky) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NormalLogProb)
*   [func NormalRand(dst, mean []float64, chol *mat.Cholesky, src rand.Source) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NormalRand)
*   [func NormalRandCov(dst, mean []float64, cov mat.Symmetric, src rand.Source) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NormalRandCov)
*   [type Bhattacharyya](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Bhattacharyya)
*       *   [func (Bhattacharyya) DistNormal(l, r *Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Bhattacharyya.DistNormal)
    *   [func (Bhattacharyya) DistUniform(l, r *Uniform) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Bhattacharyya.DistUniform)

*   [type CrossEntropy](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#CrossEntropy)
*       *   [func (CrossEntropy) DistNormal(l, r *Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#CrossEntropy.DistNormal)

*   [type Dirichlet](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet)
*       *   [func NewDirichlet(alpha []float64, src rand.Source) *Dirichlet](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewDirichlet)

*       *   [func (d *Dirichlet) CovarianceMatrix(dst *mat.SymDense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet.CovarianceMatrix)
    *   [func (d *Dirichlet) Dim() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet.Dim)
    *   [func (d *Dirichlet) LogProb(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet.LogProb)
    *   [func (d *Dirichlet) Mean(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet.Mean)
    *   [func (d *Dirichlet) Prob(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet.Prob)
    *   [func (d *Dirichlet) Rand(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet.Rand)

*   [type EigenSym](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#EigenSym)
*   [type Hellinger](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Hellinger)
*       *   [func (Hellinger) DistNormal(l, r *Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Hellinger.DistNormal)

*   [type KullbackLeibler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#KullbackLeibler)
*       *   [func (KullbackLeibler) DistDirichlet(l, r *Dirichlet) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#KullbackLeibler.DistDirichlet)
    *   [func (KullbackLeibler) DistNormal(l, r *Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#KullbackLeibler.DistNormal)
    *   [func (KullbackLeibler) DistUniform(l, r *Uniform) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#KullbackLeibler.DistUniform)

*   [type LogProber](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#LogProber)
*   [type Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal)
*       *   [func NewNormal(mu []float64, sigma mat.Symmetric, src rand.Source) (*Normal, bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewNormal)
    *   [func NewNormalChol(mu []float64, chol *mat.Cholesky, src rand.Source) *Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewNormalChol)
    *   [func NewNormalPrecision(mu []float64, prec *mat.SymDense, src rand.Source) (norm *Normal, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewNormalPrecision)

*       *   [func (n *Normal) ConditionNormal(observed []int, values []float64, src rand.Source) (*Normal, bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.ConditionNormal)
    *   [func (n *Normal) CovarianceMatrix(dst *mat.SymDense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.CovarianceMatrix)
    *   [func (n *Normal) Dim() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.Dim)
    *   [func (n *Normal) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.Entropy)
    *   [func (n *Normal) LogProb(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.LogProb)
    *   [func (n *Normal) MarginalNormal(vars []int, src rand.Source) (*Normal, bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.MarginalNormal)
    *   [func (n *Normal) MarginalNormalSingle(i int, src rand.Source) distuv.Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.MarginalNormalSingle)
    *   [func (n *Normal) Mean(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.Mean)
    *   [func (n *Normal) Prob(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.Prob)
    *   [func (n *Normal) Quantile(dst, p []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.Quantile)
    *   [func (n *Normal) Rand(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.Rand)
    *   [func (n *Normal) ScoreInput(dst, x []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.ScoreInput)
    *   [func (n *Normal) SetMean(mu []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.SetMean)
    *   [func (n *Normal) TransformNormal(dst, x []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.TransformNormal)

*   [type PositivePartEigenSym](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym)
*       *   [func NewPositivePartEigenSym(ed *mat.EigenSym) *PositivePartEigenSym](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewPositivePartEigenSym)

*       *   [func (ed *PositivePartEigenSym) At(i, j int) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym.At)
    *   [func (ed *PositivePartEigenSym) Dims() (r, c int)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym.Dims)
    *   [func (ed *PositivePartEigenSym) RawQ() mat.Matrix](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym.RawQ)
    *   [func (ed *PositivePartEigenSym) RawValues() []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym.RawValues)
    *   [func (ed *PositivePartEigenSym) SymmetricDim() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym.SymmetricDim)
    *   [func (ed *PositivePartEigenSym) T() mat.Matrix](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym.T)

*   [type Quantiler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Quantiler)
*   [type RandLogProber](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#RandLogProber)
*   [type Rander](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Rander)
*   [type Renyi](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Renyi)
*       *   [func (renyi Renyi) DistNormal(l, r *Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Renyi.DistNormal)

*   [type StudentsT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT)
*       *   [func NewStudentsT(mu []float64, sigma mat.Symmetric, nu float64, src rand.Source) (dist *StudentsT, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewStudentsT)

*       *   [func (s *StudentsT) ConditionStudentsT(observed []int, values []float64, src rand.Source) (dist *StudentsT, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.ConditionStudentsT)
    *   [func (st *StudentsT) CovarianceMatrix(dst *mat.SymDense)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.CovarianceMatrix)
    *   [func (s *StudentsT) Dim() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.Dim)
    *   [func (s *StudentsT) LogProb(y []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.LogProb)
    *   [func (s *StudentsT) MarginalStudentsT(vars []int, src rand.Source) (dist *StudentsT, ok bool)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.MarginalStudentsT)
    *   [func (s *StudentsT) MarginalStudentsTSingle(i int, src rand.Source) distuv.StudentsT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.MarginalStudentsTSingle)
    *   [func (s *StudentsT) Mean(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.Mean)
    *   [func (s *StudentsT) Nu() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.Nu)
    *   [func (s *StudentsT) Prob(y []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.Prob)
    *   [func (s *StudentsT) Rand(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.Rand)

*   [type Uniform](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform)
*       *   [func NewUniform(bnds []r1.Interval, src rand.Source) *Uniform](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewUniform)
    *   [func NewUnitUniform(dim int, src rand.Source) *Uniform](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NewUnitUniform)

*       *   [func (u *Uniform) Bounds(bounds []r1.Interval) []r1.Interval](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Bounds)
    *   [func (u *Uniform) CDF(dst, x []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.CDF)
    *   [func (u *Uniform) Dim() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Dim)
    *   [func (u *Uniform) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Entropy)
    *   [func (u *Uniform) LogProb(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.LogProb)
    *   [func (u *Uniform) Mean(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Mean)
    *   [func (u *Uniform) Prob(x []float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Prob)
    *   [func (u *Uniform) Quantile(dst, p []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Quantile)
    *   [func (u *Uniform) Rand(dst []float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Rand)

*   [type Wasserstein](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Wasserstein)
*       *   [func (Wasserstein) DistNormal(l, r *Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Wasserstein.DistNormal)

This section is empty.

This section is empty.

NormalLogProb computes the log probability of the location x for a Normal distribution the given mean and Cholesky decomposition of the covariance matrix. NormalLogProb panics if len(x) is not equal to len(mu), or if len(mu) != chol.Size().

This function saves time and memory if the Cholesky decomposition is already available. Otherwise, the NewNormal function should be used.

#### func [NormalRand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/normal.go#L314)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NormalRand "Go to NormalRand")

NormalRand generates a random sample from a multivariate normal distribution given by the mean and the Cholesky factorization of the covariance matrix.

If dst is not nil, the sample will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

This function saves time and memory if the Cholesky factorization is already available. Otherwise, the NewNormal function should be used.

#### func [NormalRandCov](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/normal.go#L409)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#NormalRandCov "Go to NormalRandCov")added in v0.15.0

NormalRandCov generates a random sample from a multivariate normal distribution given by the mean and the covariance matrix.

If dst is not nil, the sample will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

cov should be *mat.Cholesky, *mat.PivotedCholesky or EigenSym, otherwise NormalRandCov will be very inefficient because a pivoted Cholesky factorization of cov will be computed for every sample.

If cov is an EigenSym, all eigenvalues returned by RawValues must be non-negative, otherwise NormalRandCov will panic.

type Bhattacharyya struct{}

Bhattacharyya is a type for computing the Bhattacharyya distance between probability distributions.

The Bhattacharyya distance is defined as

D_B = -ln(BC(l,r))
BC = \int_-∞^∞ (p(x)q(x))^(1/2) dx

Where BC is known as the Bhattacharyya coefficient. The Bhattacharyya distance is related to the Hellinger distance by

H(l,r) = sqrt(1-BC(l,r))

For more information, see

https://en.wikipedia.org/wiki/Bhattacharyya_distance

DistNormal computes the Bhattacharyya distance between normal distributions l and r. The dimensions of the input distributions must match or DistNormal will panic.

For Normal distributions, the Bhattacharyya distance is

Σ = (Σ_l + Σ_r)/2
D_B = (1/8)*(μ_l - μ_r)ᵀ*Σ^-1*(μ_l - μ_r) + (1/2)*ln(det(Σ)/(det(Σ_l)*det(Σ_r))^(1/2))

DistUniform computes the Bhattacharyya distance between uniform distributions l and r. The dimensions of the input distributions must match or DistUniform will panic.

type CrossEntropy struct{}

CrossEntropy is a type for computing the cross-entropy between probability distributions.

The cross-entropy is defined as

*   \int_x l(x) log(r(x)) dx = KL(l || r) + H(l)

where KL is the Kullback-Leibler divergence and H is the entropy. For more information, see

https://en.wikipedia.org/wiki/Cross_entropy

DistNormal returns the cross-entropy between normal distributions l and r. The dimensions of the input distributions must match or DistNormal will panic.

type Dirichlet struct {
	
}

Dirichlet implements the Dirichlet probability distribution.

The Dirichlet distribution is a continuous probability distribution that generates elements over the probability simplex, i.e. ||x||_1 = 1. The Dirichlet distribution is the conjugate prior to the categorical distribution and the multivariate version of the beta distribution. The probability of a point x is

1/Beta(α) \prod_i x_i^(α_i - 1)

where Beta(α) is the multivariate Beta function (see the mathext package).

For more information see [https://en.wikipedia.org/wiki/Dirichlet_distribution](https://en.wikipedia.org/wiki/Dirichlet_distribution)

NewDirichlet creates a new dirichlet distribution with the given parameters alpha. NewDirichlet will panic if len(alpha) == 0, or if any alpha is <= 0.

CovarianceMatrix calculates the covariance matrix of the distribution, storing the result in dst. Upon return, the value at element {i, j} of the covariance matrix is equal to the covariance of the i^th and j^th variables.

covariance(i, j) = E[(x_i - E[x_i])(x_j - E[x_j])]

If the dst matrix is empty it will be resized to the correct dimensions, otherwise dst must match the dimension of the receiver or CovarianceMatrix will panic.

func (d *[Dirichlet](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet)) Dim() [int](https://pkg.go.dev/builtin#int)

Dim returns the dimension of the distribution.

LogProb computes the log of the pdf of the point x.

It does not check that ||x||_1 = 1.

Mean returns the mean of the probability distribution.

If dst is not nil, the mean will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

Prob computes the value of the probability density function at x.

#### func (*Dirichlet) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/dirichlet.go#L141)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Dirichlet.Rand "Go to Dirichlet.Rand")

Rand generates a random number according to the distribution.

If dst is not nil, the sample will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

EigenSym is an eigendecomposition of a symmetric matrix.

type Hellinger struct{}

Hellinger is a type for computing the Hellinger distance between probability distributions.

The Hellinger distance is defined as

H^2(l,r) = 1/2 * int_x (\sqrt(l(x)) - \sqrt(r(x)))^2 dx

and is bounded between 0 and 1. Note the above formula defines the squared Hellinger distance, while this returns the Hellinger distance itself. The Hellinger distance is related to the Bhattacharyya distance by

H^2 = 1 - exp(-D_B)

For more information, see

https://en.wikipedia.org/wiki/Hellinger_distance

DistNormal returns the Hellinger distance between normal distributions l and r. The dimensions of the input distributions must match or DistNormal will panic.

See the documentation of Bhattacharyya.DistNormal for the formula for Normal distributions.

type KullbackLeibler struct{}

KullbackLeibler is a type for computing the Kullback-Leibler divergence from l to r.

The Kullback-Leibler divergence is defined as

D_KL(l || r ) = \int_x p(x) log(p(x)/q(x)) dx

Note that the Kullback-Leibler divergence is not symmetric with respect to the order of the input arguments.

DistDirichlet returns the Kullback-Leibler divergence between Dirichlet distributions l and r. The dimensions of the input distributions must match or DistDirichlet will panic.

For two Dirichlet distributions, the KL divergence is computed as

D_KL(l || r) = log Γ(α_0_l) - \sum_i log Γ(α_i_l) - log Γ(α_0_r) + \sum_i log Γ(α_i_r)
               + \sum_i (α_i_l - α_i_r)(ψ(α_i_l)- ψ(α_0_l))

Where Γ is the gamma function, ψ is the digamma function, and α_0 is the sum of the Dirichlet parameters.

DistNormal returns the KullbackLeibler divergence between normal distributions l and r. The dimensions of the input distributions must match or DistNormal will panic.

For two normal distributions, the KL divergence is computed as

D_KL(l || r) = 0.5*[ln(|Σ_r|) - ln(|Σ_l|) + (μ_l - μ_r)ᵀ*Σ_r^-1*(μ_l - μ_r) + tr(Σ_r^-1*Σ_l)-d]

DistUniform returns the KullbackLeibler divergence between uniform distributions l and r. The dimensions of the input distributions must match or DistUniform will panic.

LogProber computes the log of the probability of the point x.

type Normal struct {
	
}

Normal is a multivariate normal distribution (also known as the multivariate Gaussian distribution). Its pdf in k dimensions is given by

(2 π)^(-k/2) |Σ|^(-1/2) exp(-1/2 (x-μ)'Σ^-1(x-μ))

where μ is the mean vector and Σ the covariance matrix. Σ must be symmetric and positive definite. Use NewNormal to construct.

NewNormal creates a new Normal with the given mean and covariance matrix. NewNormal panics if len(mu) == 0, or if len(mu) != sigma.N. If the covariance matrix is not positive-definite, the returned boolean is false.

NewNormalChol creates a new Normal distribution with the given mean and covariance matrix represented by its Cholesky decomposition. NewNormalChol panics if len(mu) is not equal to chol.Size().

NewNormalPrecision creates a new Normal distribution with the given mean and precision matrix (inverse of the covariance matrix). NewNormalPrecision panics if len(mu) is not equal to prec.SymmetricDim(). If the precision matrix is not positive-definite, NewNormalPrecision returns nil for norm and false for ok.

ConditionNormal returns the Normal distribution that is the receiver conditioned on the input evidence. The returned multivariate normal has dimension n - len(observed), where n is the dimension of the original receiver. The updated mean and covariance are

mu = mu_un + sigma_{ob,un}ᵀ * sigma_{ob,ob}^-1 (v - mu_ob)
sigma = sigma_{un,un} - sigma_{ob,un}ᵀ * sigma_{ob,ob}^-1 * sigma_{ob,un}

where mu_un and mu_ob are the original means of the unobserved and observed variables respectively, sigma_{un,un} is the unobserved subset of the covariance matrix, sigma_{ob,ob} is the observed subset of the covariance matrix, and sigma_{un,ob} are the cross terms. The elements of x_2 have been observed with values v. The dimension order is preserved during conditioning, so if the value of dimension 1 is observed, the returned normal represents dimensions {0, 2, ...} of the original Normal distribution.

ConditionNormal returns {nil, false} if there is a failure during the update. Mathematically this is impossible, but can occur with finite precision arithmetic.

CovarianceMatrix stores the covariance matrix of the distribution in dst. Upon return, the value at element {i, j} of the covariance matrix is equal to the covariance of the i^th and j^th variables.

covariance(i, j) = E[(x_i - E[x_i])(x_j - E[x_j])]

If the dst matrix is empty it will be resized to the correct dimensions, otherwise dst must match the dimension of the receiver or CovarianceMatrix will panic.

func (n *[Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal)) Dim() [int](https://pkg.go.dev/builtin#int)

Dim returns the dimension of the distribution.

Entropy returns the differential entropy of the distribution.

LogProb computes the log of the pdf of the point x.

MarginalNormal returns the marginal distribution of the given input variables. That is, MarginalNormal returns

p(x_i) = \int_{x_o} p(x_i | x_o) p(x_o) dx_o

where x_i are the dimensions in the input, and x_o are the remaining dimensions. See [https://en.wikipedia.org/wiki/Marginal_distribution](https://en.wikipedia.org/wiki/Marginal_distribution) for more information.

The input src is passed to the call to NewNormal.

MarginalNormalSingle returns the marginal of the given input variable. That is, MarginalNormal returns

p(x_i) = \int_{x_¬i} p(x_i | x_¬i) p(x_¬i) dx_¬i

where i is the input index. See [https://en.wikipedia.org/wiki/Marginal_distribution](https://en.wikipedia.org/wiki/Marginal_distribution) for more information.

The input src is passed to the constructed distuv.Normal.

Mean returns the mean of the probability distribution.

If dst is not nil, the mean will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the value of the multi-dimensional inverse cumulative distribution function at p.

If dst is not nil, the quantile will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution. Quantile will also panic if the length of p is not equal to the dimension of the distribution.

All of the values of p must be between 0 and 1, inclusive, or Quantile will panic.

#### func (*Normal) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/normal.go#L301)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Normal.Rand "Go to Normal.Rand")

Rand generates a random sample according to the distribution.

If dst is not nil, the sample will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

ScoreInput returns the gradient of the log-probability with respect to the input x. That is, ScoreInput computes

∇_x log(p(x))

If dst is not nil, the score will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

SetMean changes the mean of the normal distribution. SetMean panics if len(mu) does not equal the dimension of the normal distribution.

TransformNormal transforms x generated from a standard multivariate normal into a vector that has been generated under the normal distribution of the receiver.

If dst is not nil, the result will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution. TransformNormal will also panic if the length of x is not equal to the dimension of the receiver.

type PositivePartEigenSym struct {
	
}

PositivePartEigenSym is an EigenSym that sets any negative eigenvalues from the given eigendecomposition to zero but otherwise returns the values unchanged.

This is useful for filtering eigenvalues of positive semi-definite matrices that are almost zero but negative due to rounding errors.

NewPositivePartEigenSym returns a new PositivePartEigenSym, wrapping the given eigendecomposition.

At returns the value from the wrapped eigendecomposition.

func (ed *[PositivePartEigenSym](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym)) Dims() (r, c [int](https://pkg.go.dev/builtin#int))

Dims returns the dimensions from the wrapped eigendecomposition.

RawQ returns the orthogonal matrix Q from the wrapped eigendecomposition. The returned matrix must not be modified.

RawValues returns the eigenvalues from the wrapped eigendecomposition in ascending order with any negative value replaced by zero. The returned slice must not be modified.

func (ed *[PositivePartEigenSym](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#PositivePartEigenSym)) SymmetricDim() [int](https://pkg.go.dev/builtin#int)

SymmetricDim returns the value from the wrapped eigendecomposition.

T returns the transpose from the wrapped eigendecomposition.

Quantiler returns the multi-dimensional inverse cumulative distribution function. len(x) must equal len(p), and if x is non-nil, len(x) must also equal len(p). If x is nil, a new slice will be allocated and returned, otherwise the quantile will be stored in-place into x. All of the values of p must be between 0 and 1, or Quantile will panic.

#### type [RandLogProber](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/interfaces.go#L32)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#RandLogProber "Go to RandLogProber")

type RandLogProber interface {
	[Rander](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Rander)
	[LogProber](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#LogProber)
}

RandLogProber is both a Rander and a LogProber.

#### type [Rander](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/interfaces.go#L27)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Rander "Go to Rander")

Rander generates a random number according to the distribution.

If the input is non-nil, len(x) must equal len(p) and the dimension of the distribution, otherwise Quantile will panic.

If the input is nil, a new slice will be allocated and returned.

type Renyi struct {
 Alpha [float64](https://pkg.go.dev/builtin#float64)}

Renyi is a type for computing the Rényi divergence of order α from l to r.

The Rényi divergence with α > 0, α ≠ 1 is defined as

D_α(l || r) = 1/(α-1) log(\int_-∞^∞ l(x)^α r(x)^(1-α)dx)

The Rényi divergence has special forms for α = 0 and α = 1. This type does not implement α = ∞. For α = 0,

D_0(l || r) = -log \int_-∞^∞ r(x)1{p(x)>0} dx

that is, the negative log probability under r(x) that l(x) > 0. When α = 1, the Rényi divergence is equal to the Kullback-Leibler divergence. The Rényi divergence is also equal to half the Bhattacharyya distance when α = 0.5.

The parameter α must be in 0 ≤ α < ∞ or the distance functions will panic.

DistNormal returns the Rényi divergence between normal distributions l and r. The dimensions of the input distributions must match or DistNormal will panic.

For two normal distributions, the Rényi divergence is computed as

Σ_α = (1-α) Σ_l + αΣ_r
D_α(l||r) = α/2 * (μ_l - μ_r)'*Σ_α^-1*(μ_l - μ_r) + 1/(2(α-1))*ln(|Σ_λ|/(|Σ_l|^(1-α)*|Σ_r|^α))

For a more nicely formatted version of the formula, see Eq. 15 of

Kolchinsky, Artemy, and Brendan D. Tracey. "Estimating Mixture Entropy
with Pairwise Distances." arXiv preprint arXiv:1706.02419 (2017).

Note that the this formula is for Chernoff divergence, which differs from Rényi divergence by a factor of 1-α. Also be aware that most sources in the literature report this formula incorrectly.

type StudentsT struct {
	
}

StudentsT is a multivariate Student's T distribution. It is a distribution over ℝ^n with the probability density

p(y) = (Γ((ν+n)/2) / Γ(ν/2)) * (νπ)^(-n/2) * |Ʃ|^(-1/2) *
           (1 + 1/ν * (y-μ)ᵀ * Ʃ^-1 * (y-μ))^(-(ν+n)/2)

where ν is a scalar greater than 2, μ is a vector in ℝ^n, and Ʃ is an n×n symmetric positive definite matrix.

In this distribution, ν sets the spread of the distribution, similar to the degrees of freedom in a univariate Student's T distribution. As ν → ∞, the distribution approaches a multi-variate normal distribution. μ is the mean of the distribution, and the covariance is ν/(ν-2)*Ʃ.

See [https://en.wikipedia.org/wiki/Student%27s_t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution) and [http://users.isy.liu.se/en/rt/roth/student.pdf](http://users.isy.liu.se/en/rt/roth/student.pdf) for more information.

NewStudentsT creates a new StudentsT with the given nu, mu, and sigma parameters.

NewStudentsT panics if len(mu) == 0, or if len(mu) != sigma.SymmetricDim(). If the covariance matrix is not positive-definite, nil is returned and ok is false.

ConditionStudentsT returns the Student's T distribution that is the receiver conditioned on the input evidence, and the success of the operation. The returned Student's T has dimension n - len(observed), where n is the dimension of the original receiver. The dimension order is preserved during conditioning, so if the value of dimension 1 is observed, the returned normal represents dimensions {0, 2, ...} of the original Student's T distribution.

ok indicates whether there was a failure during the update. If ok is false the operation failed and dist is not usable. Mathematically this is impossible, but can occur with finite precision arithmetic.

CovarianceMatrix calculates the covariance matrix of the distribution, storing the result in dst. Upon return, the value at element {i, j} of the covariance matrix is equal to the covariance of the i^th and j^th variables.

covariance(i, j) = E[(x_i - E[x_i])(x_j - E[x_j])]

If the dst matrix is empty it will be resized to the correct dimensions, otherwise dst must match the dimension of the receiver or CovarianceMatrix will panic.

func (s *[StudentsT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT)) Dim() [int](https://pkg.go.dev/builtin#int)

Dim returns the dimension of the distribution.

LogProb computes the log of the pdf of the point x.

MarginalStudentsT returns the marginal distribution of the given input variables, and the success of the operation. That is, MarginalStudentsT returns

p(x_i) = \int_{x_o} p(x_i | x_o) p(x_o) dx_o

where x_i are the dimensions in the input, and x_o are the remaining dimensions. See [https://en.wikipedia.org/wiki/Marginal_distribution](https://en.wikipedia.org/wiki/Marginal_distribution) for more information.

The input src is passed to the created StudentsT.

ok indicates whether there was a failure during the marginalization. If ok is false the operation failed and dist is not usable. Mathematically this is impossible, but can occur with finite precision arithmetic.

MarginalStudentsTSingle returns the marginal distribution of the given input variable. That is, MarginalStudentsTSingle returns

p(x_i) = \int_{x_o} p(x_i | x_o) p(x_o) dx_o

where i is the input index, and x_o are the remaining dimensions. See [https://en.wikipedia.org/wiki/Marginal_distribution](https://en.wikipedia.org/wiki/Marginal_distribution) for more information.

The input src is passed to the call to NewStudentsT.

Mean returns the mean of the probability distribution.

If dst is not nil, the mean will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

Nu returns the degrees of freedom parameter of the distribution.

Prob computes the value of the probability density function at x.

#### func (*StudentsT) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/studentst.go#L339)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#StudentsT.Rand "Go to StudentsT.Rand")

Rand generates a random sample according to the distribution.

If dst is not nil, the sample will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

type Uniform struct {
	
}

Uniform represents a multivariate uniform distribution.

NewUniform creates a new uniform distribution with the given bounds.

NewUnitUniform creates a new Uniform distribution over the dim-dimensional unit hypercube. That is, a uniform distribution where each dimension has Min = 0 and Max = 1.

Bounds returns the bounds on the variables of the distribution.

If dst is not nil, the bounds will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

CDF returns the value of the multidimensional cumulative distribution function of the probability distribution at the point x.

If dst is not nil, the value will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution. CDF will also panic if the length of x is not equal to the dimension of the distribution.

func (u *[Uniform](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform)) Dim() [int](https://pkg.go.dev/builtin#int)

Dim returns the dimension of the distribution.

Entropy returns the differential entropy of the distribution.

LogProb computes the log of the pdf of the point x.

Mean returns the mean of the probability distribution.

If dst is not nil, the mean will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the value of the multi-dimensional inverse cumulative distribution function at p.

If dst is not nil, the quantile will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution. Quantile will also panic if the length of p is not equal to the dimension of the distribution.

All of the values of p must be between 0 and 1, inclusive, or Quantile will panic.

#### func (*Uniform) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distmv/uniform.go#L163)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distmv#Uniform.Rand "Go to Uniform.Rand")

Rand generates a random sample according to the distribution.

If dst is not nil, the sample will be stored in-place into dst and returned, otherwise a new slice will be allocated first. If dst is not nil, it must have length equal to the dimension of the distribution.

type Wasserstein struct{}

Wasserstein is a type for computing the Wasserstein distance between two probability distributions.

The Wasserstein distance is defined as

W(l,r) := inf 𝔼(||X-Y||_2^2)^1/2

For more information, see

https://en.wikipedia.org/wiki/Wasserstein_metric

DistNormal returns the Wasserstein distance between normal distributions l and r. The dimensions of the input distributions must match or DistNormal will panic.

The Wasserstein distance for Normal distributions is

d^2 = ||m_l - m_r||_2^2 + Tr(Σ_l + Σ_r - 2(Σ_l^(1/2)*Σ_r*Σ_l^(1/2))^(1/2))

For more information, see

http://djalil.chafai.net/blog/2010/04/30/wasserstein-distance-between-two-gaussians/
