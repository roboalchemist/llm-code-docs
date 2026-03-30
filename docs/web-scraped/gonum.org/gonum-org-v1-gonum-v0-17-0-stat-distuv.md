# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv

Title: distuv package - gonum.org/v1/gonum/stat/distuv - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv

Markdown Content:
Package distuv provides univariate random distribution types.

*   [Variables](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#pkg-variables)
*   [type AlphaStable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable)
*       *   [func (a AlphaStable) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.ExKurtosis)
    *   [func (a AlphaStable) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.Mean)
    *   [func (a AlphaStable) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.Median)
    *   [func (a AlphaStable) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.Mode)
    *   [func (a AlphaStable) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.NumParameters)
    *   [func (a AlphaStable) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.Rand)
    *   [func (a AlphaStable) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.Skewness)
    *   [func (a AlphaStable) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.StdDev)
    *   [func (a AlphaStable) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.Variance)

*   [type Bernoulli](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli)
*       *   [func (b Bernoulli) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.CDF)
    *   [func (b Bernoulli) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Entropy)
    *   [func (b Bernoulli) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.ExKurtosis)
    *   [func (b Bernoulli) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.LogProb)
    *   [func (b Bernoulli) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Mean)
    *   [func (b Bernoulli) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Median)
    *   [func (Bernoulli) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.NumParameters)
    *   [func (b Bernoulli) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Prob)
    *   [func (b Bernoulli) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Quantile)
    *   [func (b Bernoulli) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Rand)
    *   [func (b Bernoulli) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Skewness)
    *   [func (b Bernoulli) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.StdDev)
    *   [func (b Bernoulli) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Survival)
    *   [func (b Bernoulli) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Variance)

*   [type Beta](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta)
*       *   [func (b Beta) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.CDF)
    *   [func (b Beta) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Entropy)
    *   [func (b Beta) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.ExKurtosis)
    *   [func (b Beta) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.LogProb)
    *   [func (b Beta) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Mean)
    *   [func (b Beta) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Mode)
    *   [func (b Beta) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.NumParameters)
    *   [func (b Beta) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Prob)
    *   [func (b Beta) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Quantile)
    *   [func (b Beta) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Rand)
    *   [func (b Beta) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.StdDev)
    *   [func (b Beta) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Survival)
    *   [func (b Beta) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Variance)

*   [type Bhattacharyya](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bhattacharyya)
*       *   [func (Bhattacharyya) DistBeta(l, r Beta) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bhattacharyya.DistBeta)
    *   [func (Bhattacharyya) DistNormal(l, r Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bhattacharyya.DistNormal)

*   [type Binomial](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial)
*       *   [func (b Binomial) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.CDF)
    *   [func (b Binomial) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.ExKurtosis)
    *   [func (b Binomial) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.LogProb)
    *   [func (b Binomial) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.Mean)
    *   [func (Binomial) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.NumParameters)
    *   [func (b Binomial) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.Prob)
    *   [func (b Binomial) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.Rand)
    *   [func (b Binomial) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.Skewness)
    *   [func (b Binomial) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.StdDev)
    *   [func (b Binomial) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.Survival)
    *   [func (b Binomial) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.Variance)

*   [type Categorical](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical)
*       *   [func NewCategorical(w []float64, src rand.Source) Categorical](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NewCategorical)

*       *   [func (c Categorical) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.CDF)
    *   [func (c Categorical) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.Entropy)
    *   [func (c Categorical) Len() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.Len)
    *   [func (c Categorical) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.LogProb)
    *   [func (c Categorical) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.Mean)
    *   [func (c Categorical) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.Prob)
    *   [func (c Categorical) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.Rand)
    *   [func (c Categorical) Reweight(idx int, w float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.Reweight)
    *   [func (c Categorical) ReweightAll(w []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.ReweightAll)

*   [type Chi](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi)
*       *   [func (c Chi) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.CDF)
    *   [func (c Chi) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Entropy)
    *   [func (c Chi) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.ExKurtosis)
    *   [func (c Chi) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.LogProb)
    *   [func (c Chi) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Mean)
    *   [func (c Chi) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Median)
    *   [func (c Chi) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Mode)
    *   [func (c Chi) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.NumParameters)
    *   [func (c Chi) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Prob)
    *   [func (c Chi) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Quantile)
    *   [func (c Chi) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Rand)
    *   [func (c Chi) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Skewness)
    *   [func (c Chi) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.StdDev)
    *   [func (c Chi) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Survival)
    *   [func (c Chi) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Variance)

*   [type ChiSquared](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared)
*       *   [func (c ChiSquared) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.CDF)
    *   [func (c ChiSquared) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.ExKurtosis)
    *   [func (c ChiSquared) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.LogProb)
    *   [func (c ChiSquared) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Mean)
    *   [func (c ChiSquared) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Mode)
    *   [func (c ChiSquared) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.NumParameters)
    *   [func (c ChiSquared) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Prob)
    *   [func (c ChiSquared) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Quantile)
    *   [func (c ChiSquared) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Rand)
    *   [func (c ChiSquared) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.StdDev)
    *   [func (c ChiSquared) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Survival)
    *   [func (c ChiSquared) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Variance)

*   [type Exponential](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential)
*       *   [func (e Exponential) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.CDF)
    *   [func (e *Exponential) ConjugateUpdate(suffStat []float64, nSamples float64, priorStrength []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.ConjugateUpdate)
    *   [func (e Exponential) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Entropy)
    *   [func (Exponential) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.ExKurtosis)
    *   [func (e *Exponential) Fit(samples, weights []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Fit)
    *   [func (e Exponential) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.LogProb)
    *   [func (e Exponential) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Mean)
    *   [func (e Exponential) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Median)
    *   [func (Exponential) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Mode)
    *   [func (Exponential) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.NumParameters)
    *   [func (Exponential) NumSuffStat() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.NumSuffStat)
    *   [func (e Exponential) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Prob)
    *   [func (e Exponential) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Quantile)
    *   [func (e Exponential) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Rand)
    *   [func (e Exponential) Score(deriv []float64, x float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Score)
    *   [func (e Exponential) ScoreInput(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.ScoreInput)
    *   [func (Exponential) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Skewness)
    *   [func (e Exponential) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.StdDev)
    *   [func (Exponential) SuffStat(suffStat, samples, weights []float64) (nSamples float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.SuffStat)
    *   [func (e Exponential) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Survival)
    *   [func (e Exponential) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Variance)

*   [type F](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F)
*       *   [func (f F) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.CDF)
    *   [func (f F) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.ExKurtosis)
    *   [func (f F) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.LogProb)
    *   [func (f F) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Mean)
    *   [func (f F) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Mode)
    *   [func (f F) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.NumParameters)
    *   [func (f F) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Prob)
    *   [func (f F) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Quantile)
    *   [func (f F) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Rand)
    *   [func (f F) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Skewness)
    *   [func (f F) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.StdDev)
    *   [func (f F) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Survival)
    *   [func (f F) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Variance)

*   [type Gamma](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma)
*       *   [func (g Gamma) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.CDF)
    *   [func (g Gamma) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.ExKurtosis)
    *   [func (g Gamma) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.LogProb)
    *   [func (g Gamma) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Mean)
    *   [func (g Gamma) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Mode)
    *   [func (Gamma) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.NumParameters)
    *   [func (g Gamma) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Prob)
    *   [func (g Gamma) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Quantile)
    *   [func (g Gamma) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Rand)
    *   [func (g Gamma) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.StdDev)
    *   [func (g Gamma) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Survival)
    *   [func (g Gamma) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Variance)

*   [type GumbelRight](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight)
*       *   [func (g GumbelRight) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.CDF)
    *   [func (g GumbelRight) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Entropy)
    *   [func (g GumbelRight) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.ExKurtosis)
    *   [func (g GumbelRight) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.LogProb)
    *   [func (g GumbelRight) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Mean)
    *   [func (g GumbelRight) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Median)
    *   [func (g GumbelRight) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Mode)
    *   [func (GumbelRight) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.NumParameters)
    *   [func (g GumbelRight) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Prob)
    *   [func (g GumbelRight) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Quantile)
    *   [func (g GumbelRight) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Rand)
    *   [func (GumbelRight) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Skewness)
    *   [func (g GumbelRight) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.StdDev)
    *   [func (g GumbelRight) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Survival)
    *   [func (g GumbelRight) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Variance)

*   [type Hellinger](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Hellinger)
*       *   [func (Hellinger) DistBeta(l, r Beta) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Hellinger.DistBeta)
    *   [func (Hellinger) DistNormal(l, r Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Hellinger.DistNormal)

*   [type InverseGamma](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma)
*       *   [func (g InverseGamma) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.CDF)
    *   [func (g InverseGamma) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.ExKurtosis)
    *   [func (g InverseGamma) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.LogProb)
    *   [func (g InverseGamma) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Mean)
    *   [func (g InverseGamma) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Mode)
    *   [func (InverseGamma) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.NumParameters)
    *   [func (g InverseGamma) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Prob)
    *   [func (g InverseGamma) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Quantile)
    *   [func (g InverseGamma) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Rand)
    *   [func (g InverseGamma) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.StdDev)
    *   [func (g InverseGamma) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Survival)
    *   [func (g InverseGamma) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Variance)

*   [type KullbackLeibler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#KullbackLeibler)
*       *   [func (KullbackLeibler) DistBeta(l, r Beta) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#KullbackLeibler.DistBeta)
    *   [func (KullbackLeibler) DistNormal(l, r Normal) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#KullbackLeibler.DistNormal)

*   [type Laplace](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace)
*       *   [func (l Laplace) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.CDF)
    *   [func (l Laplace) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Entropy)
    *   [func (l Laplace) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.ExKurtosis)
    *   [func (l *Laplace) Fit(samples, weights []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Fit)
    *   [func (l Laplace) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.LogProb)
    *   [func (l Laplace) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Mean)
    *   [func (l Laplace) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Median)
    *   [func (l Laplace) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Mode)
    *   [func (l Laplace) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.NumParameters)
    *   [func (l Laplace) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Prob)
    *   [func (l Laplace) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Quantile)
    *   [func (l Laplace) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Rand)
    *   [func (l Laplace) Score(deriv []float64, x float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Score)
    *   [func (l Laplace) ScoreInput(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.ScoreInput)
    *   [func (Laplace) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Skewness)
    *   [func (l Laplace) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.StdDev)
    *   [func (l Laplace) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Survival)
    *   [func (l Laplace) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Variance)

*   [type LogNormal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal)
*       *   [func (l LogNormal) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.CDF)
    *   [func (l LogNormal) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Entropy)
    *   [func (l LogNormal) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.ExKurtosis)
    *   [func (l LogNormal) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.LogProb)
    *   [func (l LogNormal) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Mean)
    *   [func (l LogNormal) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Median)
    *   [func (l LogNormal) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Mode)
    *   [func (LogNormal) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.NumParameters)
    *   [func (l LogNormal) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Prob)
    *   [func (l LogNormal) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Quantile)
    *   [func (l LogNormal) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Rand)
    *   [func (l LogNormal) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Skewness)
    *   [func (l LogNormal) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.StdDev)
    *   [func (l LogNormal) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Survival)
    *   [func (l LogNormal) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Variance)

*   [type LogProber](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogProber)
*   [type Logistic](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic)
*       *   [func (l Logistic) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.CDF)
    *   [func (l Logistic) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.ExKurtosis)
    *   [func (l Logistic) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.LogProb)
    *   [func (l Logistic) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Mean)
    *   [func (l Logistic) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Median)
    *   [func (l Logistic) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Mode)
    *   [func (l Logistic) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.NumParameters)
    *   [func (l Logistic) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Prob)
    *   [func (l Logistic) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Quantile)
    *   [func (l Logistic) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Skewness)
    *   [func (l Logistic) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.StdDev)
    *   [func (l Logistic) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Survival)
    *   [func (l Logistic) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic.Variance)

*   [type NoncentralT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT)
*       *   [func (n NoncentralT) CDF(t float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.CDF)
    *   [func (n NoncentralT) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.LogProb)
    *   [func (n NoncentralT) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.Mean)
    *   [func (n NoncentralT) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.Prob)
    *   [func (n NoncentralT) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.Quantile)
    *   [func (n NoncentralT) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.Rand)
    *   [func (n NoncentralT) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.Variance)

*   [type Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal)
*       *   [func (n Normal) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.CDF)
    *   [func (n *Normal) ConjugateUpdate(suffStat []float64, nSamples float64, priorStrength []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.ConjugateUpdate)
    *   [func (n Normal) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Entropy)
    *   [func (Normal) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.ExKurtosis)
    *   [func (n *Normal) Fit(samples, weights []float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Fit)
    *   [func (n Normal) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.LogProb)
    *   [func (n Normal) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Mean)
    *   [func (n Normal) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Median)
    *   [func (n Normal) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Mode)
    *   [func (Normal) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.NumParameters)
    *   [func (Normal) NumSuffStat() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.NumSuffStat)
    *   [func (n Normal) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Prob)
    *   [func (n Normal) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Quantile)
    *   [func (n Normal) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Rand)
    *   [func (n Normal) Score(deriv []float64, x float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Score)
    *   [func (n Normal) ScoreInput(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.ScoreInput)
    *   [func (Normal) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Skewness)
    *   [func (n Normal) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.StdDev)
    *   [func (Normal) SuffStat(suffStat, samples, weights []float64) (nSamples float64)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.SuffStat)
    *   [func (n Normal) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Survival)
    *   [func (n Normal) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Variance)

*   [type Parameter](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Parameter)
*   [type Pareto](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto)
*       *   [func (p Pareto) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.CDF)
    *   [func (p Pareto) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Entropy)
    *   [func (p Pareto) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.ExKurtosis)
    *   [func (p Pareto) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.LogProb)
    *   [func (p Pareto) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Mean)
    *   [func (p Pareto) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Median)
    *   [func (p Pareto) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Mode)
    *   [func (p Pareto) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.NumParameters)
    *   [func (p Pareto) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Prob)
    *   [func (p Pareto) Quantile(prob float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Quantile)
    *   [func (p Pareto) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Rand)
    *   [func (p Pareto) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.StdDev)
    *   [func (p Pareto) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Survival)
    *   [func (p Pareto) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Variance)

*   [type Poisson](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson)
*       *   [func (p Poisson) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.CDF)
    *   [func (p Poisson) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.ExKurtosis)
    *   [func (p Poisson) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.LogProb)
    *   [func (p Poisson) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.Mean)
    *   [func (Poisson) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.NumParameters)
    *   [func (p Poisson) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.Prob)
    *   [func (p Poisson) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.Rand)
    *   [func (p Poisson) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.Skewness)
    *   [func (p Poisson) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.StdDev)
    *   [func (p Poisson) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.Survival)
    *   [func (p Poisson) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.Variance)

*   [type Quantiler](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Quantiler)
*   [type RandLogProber](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#RandLogProber)
*   [type Rander](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Rander)
*   [type StudentsT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT)
*       *   [func (s StudentsT) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.CDF)
    *   [func (s StudentsT) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.LogProb)
    *   [func (s StudentsT) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Mean)
    *   [func (s StudentsT) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Mode)
    *   [func (StudentsT) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.NumParameters)
    *   [func (s StudentsT) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Prob)
    *   [func (s StudentsT) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Quantile)
    *   [func (s StudentsT) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Rand)
    *   [func (s StudentsT) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.StdDev)
    *   [func (s StudentsT) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Survival)
    *   [func (s StudentsT) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Variance)

*   [type Triangle](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle)
*       *   [func NewTriangle(a, b, c float64, src rand.Source) Triangle](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NewTriangle)

*       *   [func (t Triangle) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.CDF)
    *   [func (t Triangle) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Entropy)
    *   [func (Triangle) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.ExKurtosis)
    *   [func (t Triangle) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.LogProb)
    *   [func (t Triangle) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Mean)
    *   [func (t Triangle) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Median)
    *   [func (t Triangle) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Mode)
    *   [func (Triangle) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.NumParameters)
    *   [func (t Triangle) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Prob)
    *   [func (t Triangle) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Quantile)
    *   [func (t Triangle) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Rand)
    *   [func (t Triangle) Score(deriv []float64, x float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Score)
    *   [func (t Triangle) ScoreInput(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.ScoreInput)
    *   [func (t Triangle) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Skewness)
    *   [func (t Triangle) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.StdDev)
    *   [func (t Triangle) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Survival)
    *   [func (t Triangle) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Variance)

*   [type Uniform](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform)
*       *   [func (u Uniform) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.CDF)
    *   [func (u Uniform) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Entropy)
    *   [func (Uniform) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.ExKurtosis)
    *   [func (u Uniform) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.LogProb)
    *   [func (u Uniform) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Mean)
    *   [func (u Uniform) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Median)
    *   [func (Uniform) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.NumParameters)
    *   [func (u Uniform) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Prob)
    *   [func (u Uniform) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Quantile)
    *   [func (u Uniform) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Rand)
    *   [func (u Uniform) Score(deriv []float64, x float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Score)
    *   [func (u Uniform) ScoreInput(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.ScoreInput)
    *   [func (Uniform) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Skewness)
    *   [func (u Uniform) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.StdDev)
    *   [func (u Uniform) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Survival)
    *   [func (u Uniform) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Variance)

*   [type Weibull](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull)
*       *   [func (w Weibull) CDF(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.CDF)
    *   [func (w Weibull) Entropy() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Entropy)
    *   [func (w Weibull) ExKurtosis() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.ExKurtosis)
    *   [func (w Weibull) LogProb(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.LogProb)
    *   [func (w Weibull) LogSurvival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.LogSurvival)
    *   [func (w Weibull) Mean() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Mean)
    *   [func (w Weibull) Median() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Median)
    *   [func (w Weibull) Mode() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Mode)
    *   [func (Weibull) NumParameters() int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.NumParameters)
    *   [func (w Weibull) Prob(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Prob)
    *   [func (w Weibull) Quantile(p float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Quantile)
    *   [func (w Weibull) Rand() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Rand)
    *   [func (w Weibull) Score(deriv []float64, x float64) []float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Score)
    *   [func (w Weibull) ScoreInput(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.ScoreInput)
    *   [func (w Weibull) Skewness() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Skewness)
    *   [func (w Weibull) StdDev() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.StdDev)
    *   [func (w Weibull) Survival(x float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Survival)
    *   [func (w Weibull) Variance() float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Variance)

*   [Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#example-Normal)

This section is empty.

UnitNormal is an instantiation of the normal distribution with Mu = 0 and Sigma = 1.

UnitUniform is an instantiation of the uniform distribution with Min = 0 and Max = 1.

This section is empty.

AlphaStable represents an α-stable distribution with four parameters. See [https://en.wikipedia.org/wiki/Stable_distribution](https://en.wikipedia.org/wiki/Stable_distribution) for more information.

ExKurtosis returns the excess kurtosis of the distribution. ExKurtosis returns NaN when Alpha != 2.

Mean returns the mean of the probability distribution. Mean returns NaN when Alpha <= 1.

Median returns the median of the distribution. Median panics when Beta != 0, because then the mode is not analytically expressible.

Mode returns the mode of the distribution. Mode panics when Beta != 0, because then the mode is not analytically expressible.

func (a [AlphaStable](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

#### func (AlphaStable) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/alphastable.go#L73)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#AlphaStable.Rand "Go to AlphaStable.Rand")added in v0.8.0

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution. Skewness returns NaN when Alpha != 2.

StdDev returns the standard deviation of the probability distribution.

Variance returns the variance of the probability distribution. Variance returns +Inf when Alpha != 2.

Bernoulli represents a random variable whose value is 1 with probability p and value of zero with probability 1-P. The value of P must be between 0 and 1. More information at [https://en.wikipedia.org/wiki/Bernoulli_distribution](https://en.wikipedia.org/wiki/Bernoulli_distribution).

CDF computes the value of the cumulative density function at x.

Entropy returns the entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the probability distribution.

func ([Bernoulli](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability distribution at x.

Quantile returns the minimum value of x from amongst all those values whose CDF value exceeds or equals p.

#### func (Bernoulli) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/bernoulli.go#L103)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Bernoulli.Rand "Go to Bernoulli.Rand")

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Beta implements the Beta distribution, a two-parameter continuous distribution with support between 0 and 1.

The beta distribution has density function

x^(α-1) * (1-x)^(β-1) * Γ(α+β) / (Γ(α)*Γ(β))

For more information, see [https://en.wikipedia.org/wiki/Beta_distribution](https://en.wikipedia.org/wiki/Beta_distribution)

CDF computes the value of the cumulative distribution function at x.

Entropy returns the differential entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Mode returns the mode of the distribution.

Mode returns NaN if both parameters are less than or equal to 1 as a special case, 0 if only Alpha <= 1 and 1 if only Beta <= 1.

func (b [Beta](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

#### func (Beta) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/beta.go#L126)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Beta.Rand "Go to Beta.Rand")

Rand returns a random sample drawn from the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

type Bhattacharyya struct{}

Bhattacharyya is a type for computing the Bhattacharyya distance between probability distributions.

The Bhattacharyya distance is defined as

D_B = -ln(BC(l,r))
BC = \int_-∞^∞ (p(x)q(x))^(1/2) dx

Where BC is known as the Bhattacharyya coefficient. The Bhattacharyya distance is related to the Hellinger distance by

H(l,r) = sqrt(1-BC(l,r))

For more information, see

https://en.wikipedia.org/wiki/Bhattacharyya_distance

DistBeta returns the Bhattacharyya distance between Beta distributions l and r. For Beta distributions, the Bhattacharyya distance is given by

-ln(B((α_l + α_r)/2, (β_l + β_r)/2) / (B(α_l,β_l), B(α_r,β_r)))

Where B is the Beta function.

DistNormal returns the Bhattacharyya distance Normal distributions l and r. For Normal distributions, the Bhattacharyya distance is given by

s = (σ_l^2 + σ_r^2)/2
BC = 1/8 (μ_l-μ_r)^2/s + 1/2 ln(s/(σ_l*σ_r))

Binomial implements the binomial distribution, a discrete probability distribution that expresses the probability of a given number of successful Bernoulli trials out of a total of n, each with success probability p. The binomial distribution has the density function:

f(k) = (n choose k) p^k (1-p)^(n-k)

For more information, see [https://en.wikipedia.org/wiki/Binomial_distribution](https://en.wikipedia.org/wiki/Binomial_distribution).

CDF computes the value of the cumulative distribution function at x.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

func ([Binomial](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

#### func (Binomial) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/binomial.go#L76)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Binomial.Rand "Go to Binomial.Rand")

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

type Categorical struct {
	
}

Categorical is an extension of the Bernoulli distribution where x takes values {0, 1, ..., len(w)-1} where w is the weight vector. Categorical must be initialized with NewCategorical.

NewCategorical constructs a new categorical distribution where the probability that x equals i is proportional to w[i]. All of the weights must be nonnegative, and at least one of the weights must be positive.

CDF computes the value of the cumulative density function at x.

Entropy returns the entropy of the distribution.

Len returns the number of values x could possibly take (the length of the initial supplied weight vector).

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Prob computes the value of the probability density function at x.

#### func (Categorical) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/categorical.go#L109)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Categorical.Rand "Go to Categorical.Rand")

Rand returns a random draw from the categorical distribution.

Reweight sets the weight of item idx to w. The input weight must be non-negative, and after reweighting at least one of the weights must be positive.

ReweightAll resets the weights of the distribution. ReweightAll panics if len(w) != c.Len. All of the weights must be nonnegative, and at least one of the weights must be positive.

Chi implements the χ distribution, a one parameter distribution with support on the positive numbers.

The density function is given by

1/(2^{k/2-1} * Γ(k/2)) * x^{k - 1} * e^{-x^2/2}

For more information, see [https://en.wikipedia.org/wiki/Chi_distribution](https://en.wikipedia.org/wiki/Chi_distribution).

CDF computes the value of the cumulative density function at x.

Entropy returns the differential entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the distribution.

Mode returns the mode of the distribution.

Mode returns NaN if K is less than one.

func (c [Chi](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

#### func (Chi) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/chi.go#L88)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Chi.Rand "Go to Chi.Rand")added in v0.11.0

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

ChiSquared implements the χ² distribution, a one parameter distribution with support on the positive numbers.

The density function is given by

1/(2^{k/2} * Γ(k/2)) * x^{k/2 - 1} * e^{-x/2}

It is a special case of the Gamma distribution, Γ(k/2, 1/2).

For more information, see [https://en.wikipedia.org/wiki/Chi-squared_distribution](https://en.wikipedia.org/wiki/Chi-squared_distribution).

CDF computes the value of the cumulative density function at x.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Mode returns the mode of the distribution.

func (c [ChiSquared](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

#### func (ChiSquared) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/chisquared.go#L73)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#ChiSquared.Rand "Go to ChiSquared.Rand")

Rand returns a random sample drawn from the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Exponential represents the exponential distribution ([https://en.wikipedia.org/wiki/Exponential_distribution](https://en.wikipedia.org/wiki/Exponential_distribution)).

CDF computes the value of the cumulative density function at x.

ConjugateUpdate updates the parameters of the distribution from the sufficient statistics of a set of samples. The sufficient statistics, suffStat, have been observed with nSamples observations. The prior values of the distribution are those currently in the distribution, and have been observed with priorStrength samples.

For the exponential distribution, the sufficient statistic is the inverse of the mean of the samples. The prior is having seen priorStrength[0] samples with inverse mean Exponential.Rate As a result of this function, Exponential.Rate is updated based on the weighted samples, and priorStrength is modified to include the new number of samples observed.

This function panics if len(suffStat) != e.NumSuffStat() or len(priorStrength) != e.NumSuffStat().

Entropy returns the entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

func (e *[Exponential](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential)) Fit(samples, weights [][float64](https://pkg.go.dev/builtin#float64))

Fit sets the parameters of the probability distribution from the data samples x with relative weights w. If weights is nil, then all the weights are 1. If weights is not nil, then the len(weights) must equal len(samples).

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the probability distribution.

Mode returns the mode of the probability distribution.

func ([Exponential](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

func ([Exponential](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential)) NumSuffStat() [int](https://pkg.go.dev/builtin#int)

NumSuffStat returns the number of sufficient statistics for the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (Exponential) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/exponential.go#L127)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Exponential.Rand "Go to Exponential.Rand")

Rand returns a random sample drawn from the distribution.

Score returns the score function with respect to the parameters of the distribution at the input location x. The score function is the derivative of the log-likelihood at x with respect to the parameters

(∂/∂θ) log(p(x;θ))

If deriv is non-nil, len(deriv) must equal the number of parameters otherwise Score will panic, and the derivative is stored in-place into deriv. If deriv is nil a new slice will be allocated and returned.

The order is [∂LogProb / ∂Rate].

For more information, see [https://en.wikipedia.org/wiki/Score_%28statistics%29](https://en.wikipedia.org/wiki/Score_%28statistics%29).

Special cases:

Score(0) = [NaN]

ScoreInput returns the score function with respect to the input of the distribution at the input location specified by x. The score function is the derivative of the log-likelihood

(d/dx) log(p(x)) .

Special cases:

ScoreInput(0) = NaN

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

SuffStat computes the sufficient statistics of set of samples to update the distribution. The sufficient statistics are stored in place, and the effective number of samples are returned.

The exponential distribution has one sufficient statistic, the average rate of the samples.

If weights is nil, the weights are assumed to be 1, otherwise panics if len(samples) != len(weights). Panics if len(suffStat) != NumSuffStat().

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

F implements the F-distribution, a two-parameter continuous distribution with support over the positive real numbers.

The F-distribution has density function

sqrt(((d1*x)^d1) * d2^d2 / ((d1*x+d2)^(d1+d2))) / (x * B(d1/2,d2/2))

where B is the beta function.

For more information, see [https://en.wikipedia.org/wiki/F-distribution](https://en.wikipedia.org/wiki/F-distribution)

CDF computes the value of the cumulative density function at x.

ExKurtosis returns the excess kurtosis of the distribution.

ExKurtosis returns NaN if the D2 parameter is less or equal to 8.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Mean returns NaN if the D2 parameter is less than or equal to 2.

Mode returns the mode of the distribution.

Mode returns NaN if the D1 parameter is less than or equal to 2.

func (f [F](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

#### func (F) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/f.go#L91)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#F.Rand "Go to F.Rand")

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution.

Skewness returns NaN if the D2 parameter is less than or equal to 6.

StdDev returns the standard deviation of the probability distribution.

StdDev returns NaN if the D2 parameter is less than or equal to 4.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Variance returns NaN if the D2 parameter is less than or equal to 4.

Gamma implements the Gamma distribution, a two-parameter continuous distribution with support over the positive real numbers.

The gamma distribution has density function

β^α / Γ(α) x^(α-1)e^(-βx)

For more information, see [https://en.wikipedia.org/wiki/Gamma_distribution](https://en.wikipedia.org/wiki/Gamma_distribution)

CDF computes the value of the cumulative distribution function at x.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Mode returns the mode of the gamma distribution.

The mode is 0 in the special case where the Alpha (shape) parameter is less than 1.

func ([Gamma](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

#### func (Gamma) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/gamma.go#L98)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Gamma.Rand "Go to Gamma.Rand")

Rand returns a random sample drawn from the distribution.

Rand panics if either alpha or beta is <= 0.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

GumbelRight implements the right-skewed Gumbel distribution, a two-parameter continuous distribution with support over the real numbers. The right-skewed Gumbel distribution is also sometimes known as the Extreme Value distribution.

The right-skewed Gumbel distribution has density function

1/beta * exp(-(z + exp(-z)))
z = (x - mu)/beta

Beta must be greater than 0.

For more information, see [https://en.wikipedia.org/wiki/Gumbel_distribution](https://en.wikipedia.org/wiki/Gumbel_distribution).

CDF computes the value of the cumulative density function at x.

Entropy returns the differential entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the Gumbel distribution.

Mode returns the mode of the normal distribution.

func ([GumbelRight](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (GumbelRight) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/gumbel.go#L90)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#GumbelRight.Rand "Go to GumbelRight.Rand")

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

type Hellinger struct{}

Hellinger is a type for computing the Hellinger distance between probability distributions.

The Hellinger distance is defined as

H^2(l,r) = 1/2 * int_x (\sqrt(l(x)) - \sqrt(r(x)))^2 dx

and is bounded between 0 and 1. Note the above formula defines the squared Hellinger distance, while this returns the Hellinger distance itself. The Hellinger distance is related to the Bhattacharyya distance by

H^2 = 1 - exp(-D_B)

For more information, see

https://en.wikipedia.org/wiki/Hellinger_distance

DistBeta computes the Hellinger distance between Beta distributions l and r. See the documentation of Bhattacharyya.DistBeta for the distance formula.

DistNormal computes the Hellinger distance between Normal distributions l and r. See the documentation of Bhattacharyya.DistNormal for the distance formula.

InverseGamma implements the inverse gamma distribution, a two-parameter continuous distribution with support over the positive real numbers. The inverse gamma distribution is the same as the distribution of the reciprocal of a gamma distributed random variable.

The inverse gamma distribution has density function

β^α / Γ(α) x^(-α-1)e^(-β/x)

For more information, see [https://en.wikipedia.org/wiki/Inverse-gamma_distribution](https://en.wikipedia.org/wiki/Inverse-gamma_distribution)

CDF computes the value of the cumulative distribution function at x.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Mode returns the mode of the distribution.

func ([InverseGamma](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

#### func (InverseGamma) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/inversegamma.go#L98)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#InverseGamma.Rand "Go to InverseGamma.Rand")

Rand returns a random sample drawn from the distribution.

Rand panics if either alpha or beta is <= 0.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

type KullbackLeibler struct{}

KullbackLeibler is a type for computing the Kullback-Leibler divergence from l to r.

The Kullback-Leibler divergence is defined as

D_KL(l || r ) = \int_x p(x) log(p(x)/q(x)) dx

Note that the Kullback-Leibler divergence is not symmetric with respect to the order of the input arguments.

DistBeta returns the Kullback-Leibler divergence between Beta distributions l and r.

For two Beta distributions, the KL divergence is computed as

D_KL(l || r) =  log Γ(α_l+β_l) - log Γ(α_l) - log Γ(β_l)
                - log Γ(α_r+β_r) + log Γ(α_r) + log Γ(β_r)
                + (α_l-α_r)(ψ(α_l)-ψ(α_l+β_l)) + (β_l-β_r)(ψ(β_l)-ψ(α_l+β_l))

Where Γ is the gamma function and ψ is the digamma function.

DistNormal returns the Kullback-Leibler divergence between Normal distributions l and r.

For two Normal distributions, the KL divergence is computed as

D_KL(l || r) = log(σ_r / σ_l) + (σ_l^2 + (μ_l-μ_r)^2)/(2 * σ_r^2) - 0.5

Laplace represents the Laplace distribution ([https://en.wikipedia.org/wiki/Laplace_distribution](https://en.wikipedia.org/wiki/Laplace_distribution)).

CDF computes the value of the cumulative density function at x.

Entropy returns the entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

func (l *[Laplace](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace)) Fit(samples, weights [][float64](https://pkg.go.dev/builtin#float64))

Fit sets the parameters of the probability distribution from the data samples x with relative weights w. If weights is nil, then all the weights are 1. If weights is not nil, then the len(weights) must equal len(samples).

Note: Laplace distribution has no FitPrior because it has no sufficient statistics.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the LaPlace distribution.

Mode returns the mode of the LaPlace distribution.

func (l [Laplace](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (Laplace) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/laplace.go#L159)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Laplace.Rand "Go to Laplace.Rand")

Rand returns a random sample drawn from the distribution.

Score returns the score function with respect to the parameters of the distribution at the input location x. The score function is the derivative of the log-likelihood at x with respect to the parameters

(∂/∂θ) log(p(x;θ))

If deriv is non-nil, len(deriv) must equal the number of parameters otherwise Score will panic, and the derivative is stored in-place into deriv. If deriv is nil a new slice will be allocated and returned.

The order is [∂LogProb / ∂Mu, ∂LogProb / ∂Scale].

For more information, see [https://en.wikipedia.org/wiki/Score_%28statistics%29](https://en.wikipedia.org/wiki/Score_%28statistics%29).

Special cases:

Score(l.Mu) = [NaN, -1/l.Scale]

ScoreInput returns the score function with respect to the input of the distribution at the input location specified by x. The score function is the derivative of the log-likelihood

(d/dx) log(p(x)) .

Special cases:

ScoreInput(l.Mu) = NaN

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

LogNormal represents a random variable whose log is normally distributed. The probability density function is given by

1/(x σ √2π) exp(-(ln(x)-μ)^2)/(2σ^2))

CDF computes the value of the cumulative density function at x.

Entropy returns the differential entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the probability distribution.

Mode returns the mode of the probability distribution.

func ([LogNormal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (LogNormal) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/lognormal.go#L83)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogNormal.Rand "Go to LogNormal.Rand")

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

LogProber wraps the LogProb method.

Logistic implements the Logistic distribution, a two-parameter distribution with support on the real axis. Its cumulative distribution function is the logistic function.

General form of probability density function for Logistic distribution is

E(x) / (s * (1 + E(x))^2)
where E(x) = exp(-(x-μ)/s)

For more information, see [https://en.wikipedia.org/wiki/Logistic_distribution](https://en.wikipedia.org/wiki/Logistic_distribution).

CDF computes the value of the cumulative density function at x.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the distribution.

It is same as Mean for Logistic distribution.

Mode returns the mode of the distribution.

It is same as Mean for Logistic distribution.

func (l [Logistic](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Logistic)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Always returns 2.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

Skewness returns the skewness of the distribution.

Always 0 for Logistic distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

NoncentralT is the noncentral t-distribution.

See [https://en.wikipedia.org/wiki/Noncentral_t-distribution](https://en.wikipedia.org/wiki/Noncentral_t-distribution) for more details.

CDF is the cumulative distribution function of the noncentral t-distribution. This implementation is based on: Russell Lenth, Cumulative Distribution Function of the Non-Central T Distribution, Algorithm AS 243.

Mean returns the mean of the noncentral t-distribution.

Prob returns the probability density function of the noncentral t-distribution.

Quantile is the quantile function.

#### func (NoncentralT) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/noncentralt.go#L30)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#NoncentralT.Rand "Go to NoncentralT.Rand")added in v0.17.0

Rand samples from the noncentral t-distribution.

Variance returns the variance of the noncentral t-distribution.

Normal represents a normal (Gaussian) distribution ([https://en.wikipedia.org/wiki/Normal_distribution](https://en.wikipedia.org/wiki/Normal_distribution)).

Output:

mean= 2.0 ± 0.02 

CDF computes the value of the cumulative density function at x.

ConjugateUpdate updates the parameters of the distribution from the sufficient statistics of a set of samples. The sufficient statistics, suffStat, have been observed with nSamples observations. The prior values of the distribution are those currently in the distribution, and have been observed with priorStrength samples.

For the normal distribution, the sufficient statistics are the mean and uncorrected standard deviation of the samples. The prior is having seen strength[0] samples with mean Normal.Mu and strength[1] samples with standard deviation Normal.Sigma. As a result of this function, Normal.Mu and Normal.Sigma are updated based on the weighted samples, and strength is modified to include the new number of samples observed.

This function panics if len(suffStat) != n.NumSuffStat() or len(priorStrength) != n.NumSuffStat().

Entropy returns the differential entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

func (n *[Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal)) Fit(samples, weights [][float64](https://pkg.go.dev/builtin#float64))

Fit sets the parameters of the probability distribution from the data samples x with relative weights w. If weights is nil, then all the weights are 1. If weights is not nil, then the len(weights) must equal len(samples).

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the normal distribution.

Mode returns the mode of the normal distribution.

func ([Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

func ([Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal)) NumSuffStat() [int](https://pkg.go.dev/builtin#int)

NumSuffStat returns the number of sufficient statistics for the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (Normal) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/norm.go#L138)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal.Rand "Go to Normal.Rand")

Rand returns a random sample drawn from the distribution.

Score returns the score function with respect to the parameters of the distribution at the input location x. The score function is the derivative of the log-likelihood at x with respect to the parameters

(∂/∂θ) log(p(x;θ))

If deriv is non-nil, len(deriv) must equal the number of parameters otherwise Score will panic, and the derivative is stored in-place into deriv. If deriv is nil a new slice will be allocated and returned.

The order is [∂LogProb / ∂Mu, ∂LogProb / ∂Sigma].

For more information, see [https://en.wikipedia.org/wiki/Score_%28statistics%29](https://en.wikipedia.org/wiki/Score_%28statistics%29).

ScoreInput returns the score function with respect to the input of the distribution at the input location specified by x. The score function is the derivative of the log-likelihood

(d/dx) log(p(x)) .

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

func ([Normal](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Normal)) SuffStat(suffStat, samples, weights [][float64](https://pkg.go.dev/builtin#float64)) (nSamples [float64](https://pkg.go.dev/builtin#float64))

SuffStat computes the sufficient statistics of a set of samples to update the distribution. The sufficient statistics are stored in place, and the effective number of samples are returned.

The normal distribution has two sufficient statistics, the mean of the samples and the standard deviation of the samples.

If weights is nil, the weights are assumed to be 1, otherwise panics if len(samples) != len(weights). Panics if len(suffStat) != NumSuffStat().

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Parameter represents a parameter of a probability distribution

Pareto implements the Pareto (Type I) distribution, a one parameter distribution with support above the scale parameter.

The density function is given by

(α x_m^{α})/(x^{α+1}) for x >= x_m.

For more information, see [https://en.wikipedia.org/wiki/Pareto_distribution](https://en.wikipedia.org/wiki/Pareto_distribution).

CDF computes the value of the cumulative density function at x.

Entropy returns the differential entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the pareto distribution.

Mode returns the mode of the distribution.

func (p [Pareto](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (Pareto) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/pareto.go#L100)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Pareto.Rand "Go to Pareto.Rand")

Rand returns a random sample drawn from the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Poisson implements the Poisson distribution, a discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval. The poisson distribution has density function:

f(k) = λ^k / k! e^(-λ)

For more information, see [https://en.wikipedia.org/wiki/Poisson_distribution](https://en.wikipedia.org/wiki/Poisson_distribution).

CDF computes the value of the cumulative distribution function at x.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

func ([Poisson](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

#### func (Poisson) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/poisson.go#L69)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Poisson.Rand "Go to Poisson.Rand")

Rand returns a random sample drawn from the distribution.

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Quantiler wraps the Quantile method.

#### type [RandLogProber](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/interfaces.go#L22)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#RandLogProber "Go to RandLogProber")

type RandLogProber interface {
	[Rander](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Rander)
	[LogProber](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#LogProber)
}

RandLogProber is the interface that groups the Rander and LogProber methods.

#### type [Rander](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/interfaces.go#L16)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Rander "Go to Rander")

type Rander interface {
	Rand() [float64](https://pkg.go.dev/builtin#float64)
}

Rander wraps the Rand method.

StudentsT implements the three-parameter Student's T distribution, a distribution over the real numbers.

The Student's T distribution has density function

Γ((ν+1)/2) / (sqrt(νπ) Γ(ν/2) σ) (1 + 1/ν * ((x-μ)/σ)^2)^(-(ν+1)/2)

The Student's T distribution approaches the normal distribution as ν → ∞.

For more information, see [https://en.wikipedia.org/wiki/Student%27s_t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution), specifically [https://en.wikipedia.org/wiki/Student%27s_t-distribution#Non-standardized_Student.27s_t-distribution](https://en.wikipedia.org/wiki/Student%27s_t-distribution#Non-standardized_Student.27s_t-distribution) .

The standard Student's T distribution is with Mu = 0, and Sigma = 1.

CDF computes the value of the cumulative distribution function at x.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Mode returns the mode of the distribution.

func ([StudentsT](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative distribution function.

#### func (StudentsT) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/studentst.go#L117)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#StudentsT.Rand "Go to StudentsT.Rand")

Rand returns a random sample drawn from the distribution.

StdDev returns the standard deviation of the probability distribution.

The standard deviation is undefined for ν <= 1, and this returns math.NaN().

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

The variance is undefined for ν <= 1, and this returns math.NaN().

type Triangle struct {
	
}

Triangle represents a triangle distribution ([https://en.wikipedia.org/wiki/Triangular_distribution](https://en.wikipedia.org/wiki/Triangular_distribution)).

NewTriangle constructs a new triangle distribution with lower limit a, upper limit b, and mode c. Constraints are a < b and a ≤ c ≤ b. This distribution is uncommon in nature, but may be useful for simulation.

CDF computes the value of the cumulative density function at x.

Entropy returns the entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the probability distribution.

Mode returns the mode of the probability distribution.

func ([Triangle](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (Triangle) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/triangle.go#L125)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Triangle.Rand "Go to Triangle.Rand")

Rand returns a random sample drawn from the distribution.

Score returns the score function with respect to the parameters of the distribution at the input location x. The score function is the derivative of the log-likelihood at x with respect to the parameters

(∂/∂θ) log(p(x;θ))

If deriv is non-nil, len(deriv) must equal the number of parameters otherwise Score will panic, and the derivative is stored in-place into deriv. If deriv is nil a new slice will be allocated and returned.

The order is [∂LogProb / ∂Mu, ∂LogProb / ∂Sigma].

For more information, see [https://en.wikipedia.org/wiki/Score_%28statistics%29](https://en.wikipedia.org/wiki/Score_%28statistics%29).

ScoreInput returns the score function with respect to the input of the distribution at the input location specified by x. The score function is the derivative of the log-likelihood

(d/dx) log(p(x)) .

Special cases (c is the mode of the distribution):

ScoreInput(c) = NaN
ScoreInput(x) = NaN for x not in (a, b)

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Uniform represents a continuous uniform distribution ([https://en.wikipedia.org/wiki/Uniform_distribution_%28continuous%29](https://en.wikipedia.org/wiki/Uniform_distribution_%28continuous%29)).

CDF computes the value of the cumulative density function at x.

Entropy returns the entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x.

Mean returns the mean of the probability distribution.

Median returns the median of the probability distribution.

func ([Uniform](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (Uniform) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/uniform.go#L112)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Uniform.Rand "Go to Uniform.Rand")

Rand returns a random sample drawn from the distribution.

Score returns the score function with respect to the parameters of the distribution at the input location x. The score function is the derivative of the log-likelihood at x with respect to the parameters

(∂/∂θ) log(p(x;θ))

If deriv is non-nil, len(deriv) must equal the number of parameters otherwise Score will panic, and the derivative is stored in-place into deriv. If deriv is nil a new slice will be allocated and returned.

The order is [∂LogProb / ∂Mu, ∂LogProb / ∂Sigma].

For more information, see [https://en.wikipedia.org/wiki/Score_%28statistics%29](https://en.wikipedia.org/wiki/Score_%28statistics%29).

ScoreInput returns the score function with respect to the input of the distribution at the input location specified by x. The score function is the derivative of the log-likelihood

(d/dx) log(p(x)) .

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.

Weibull distribution. Valid range for x is [0,+∞).

CDF computes the value of the cumulative density function at x.

Entropy returns the entropy of the distribution.

ExKurtosis returns the excess kurtosis of the distribution.

LogProb computes the natural logarithm of the value of the probability density function at x. -Inf is returned if x is less than zero.

Special cases occur when x == 0, and the result depends on the shape parameter as follows:

If 0 < K < 1, LogProb returns +Inf.
If K == 1, LogProb returns 0.
If K > 1, LogProb returns -Inf.

LogSurvival returns the log of the survival function (complementary CDF) at x.

Mean returns the mean of the probability distribution.

Median returns the median of the normal distribution.

Mode returns the mode of the normal distribution.

The mode is NaN in the special case where the K (shape) parameter is less than 1.

func ([Weibull](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull)) NumParameters() [int](https://pkg.go.dev/builtin#int)

NumParameters returns the number of parameters in the distribution.

Prob computes the value of the probability density function at x.

Quantile returns the inverse of the cumulative probability distribution.

#### func (Weibull) [Rand](https://github.com/gonum/gonum/blob/v0.17.0/stat/distuv/weibull.go#L117)[¶](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/distuv#Weibull.Rand "Go to Weibull.Rand")

Rand returns a random sample drawn from the distribution.

Score returns the score function with respect to the parameters of the distribution at the input location x. The score function is the derivative of the log-likelihood at x with respect to the parameters

(∂/∂θ) log(p(x;θ))

If deriv is non-nil, len(deriv) must equal the number of parameters otherwise Score will panic, and the derivative is stored in-place into deriv. If deriv is nil a new slice will be allocated and returned.

The order is [∂LogProb / ∂K, ∂LogProb / ∂λ].

For more information, see [https://en.wikipedia.org/wiki/Score_%28statistics%29](https://en.wikipedia.org/wiki/Score_%28statistics%29).

Special cases:

Score(x) = [NaN, NaN] for x <= 0

ScoreInput returns the score function with respect to the input of the distribution at the input location specified by x. The score function is the derivative of the log-likelihood

(d/dx) log(p(x)) .

Special cases:

ScoreInput(x) = NaN for x <= 0

Skewness returns the skewness of the distribution.

StdDev returns the standard deviation of the probability distribution.

Survival returns the survival function (complementary CDF) at x.

Variance returns the variance of the probability distribution.
