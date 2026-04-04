# Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin

Title: combin package - gonum.org/v1/gonum/stat/combin - Go Packages

URL Source: https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin

Markdown Content:
Package combin implements routines involving combinatorics (permutations, combinations, etc.).

*   [func Binomial(n, k int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#Binomial)
*   [func Card(dims []int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#Card)
*   [func Cartesian(lens []int) [][]int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#Cartesian)
*   [func CombinationIndex(comb []int, n, k int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CombinationIndex)
*   [func Combinations(n, k int) [][]int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#Combinations)
*   [func GeneralizedBinomial(n, k float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#GeneralizedBinomial)
*   [func IdxFor(sub, dims []int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#IdxFor)
*   [func IndexToCombination(dst []int, idx, n, k int) []int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#IndexToCombination)
*   [func IndexToPermutation(dst []int, idx, n, k int) []int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#IndexToPermutation)
*   [func LogGeneralizedBinomial(n, k float64) float64](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#LogGeneralizedBinomial)
*   [func NumPermutations(n, k int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#NumPermutations)
*   [func PermutationIndex(perm []int, n, k int) int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#PermutationIndex)
*   [func Permutations(n, k int) [][]int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#Permutations)
*   [func SubFor(sub []int, idx int, dims []int) []int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#SubFor)
*   [type CartesianGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CartesianGenerator)
*       *   [func NewCartesianGenerator(lens []int) *CartesianGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#NewCartesianGenerator)

*       *   [func (g *CartesianGenerator) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CartesianGenerator.Next)
    *   [func (g *CartesianGenerator) Product(dst []int) []int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CartesianGenerator.Product)

*   [type CombinationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CombinationGenerator)
*       *   [func NewCombinationGenerator(n, k int) *CombinationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#NewCombinationGenerator)

*       *   [func (c *CombinationGenerator) Combination(dst []int) []int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CombinationGenerator.Combination)
    *   [func (c *CombinationGenerator) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CombinationGenerator.Next)

*   [type PermutationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#PermutationGenerator)
*       *   [func NewPermutationGenerator(n, k int) *PermutationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#NewPermutationGenerator)

*       *   [func (p *PermutationGenerator) Next() bool](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#PermutationGenerator.Next)
    *   [func (p *PermutationGenerator) Permutation(dst []int) []int](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#PermutationGenerator.Permutation)

*   [Cartesian](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-Cartesian)
*   [CartesianGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-CartesianGenerator)
*   [CombinationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-CombinationGenerator)
*   [Combinations](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-Combinations)
*   [Combinations (Index)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-Combinations-Index)
*   [IndexToCombination](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-IndexToCombination)
*   [IndexToPermutation](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-IndexToPermutation)
*   [PermutationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-PermutationGenerator)
*   [Permutations](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-Permutations)
*   [Permutations (Index)](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#example-Permutations-Index)

This section is empty.

This section is empty.

Binomial returns the binomial coefficient of (n,k), also commonly referred to as "n choose k".

The binomial coefficient, C(n,k), is the number of unordered combinations of k elements in a set that is n elements big, and is defined as

C(n,k) = n!/((n-k)!k!)

n and k must be non-negative with n >= k, otherwise Binomial will panic. No check is made for overflow.

Card computes the cardinality of the multi-dimensional space whose dimensions have size specified by dims All length values must be positive, otherwise this will panic.

func Cartesian(lens [][int](https://pkg.go.dev/builtin#int)) [][][int](https://pkg.go.dev/builtin#int)

Cartesian returns the Cartesian product of the slices in data. The Cartesian product of two sets is the set of all combinations of the items. For example, given the input

[]int{2, 3, 1}

the returned matrix will be

[ 0 0 0 ]
[ 0 1 0 ]
[ 0 2 0 ]
[ 1 0 0 ]
[ 1 1 0 ]
[ 1 2 0 ]

Cartesian panics if any of the provided lengths are less than 1.

Output:

Generate Cartesian products for given lengths: 0 [0 0 0] 1 [0 0 1] 2 [0 0 2] 3 [0 1 0] 4 [0 1 1] 5 [0 1 2] 

func CombinationIndex(comb [][int](https://pkg.go.dev/builtin#int), n, k [int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

CombinationIndex returns the index of the given combination.

The functions CombinationIndex and IndexToCombination define a bijection between the integers and the Binomial(n, k) number of possible combinations. CombinationIndex returns the inverse of IndexToCombination.

CombinationIndex panics if comb is not a sorted combination of the first [0,n) integers, if n or k are negative, or if k is greater than n.

func Combinations(n, k [int](https://pkg.go.dev/builtin#int)) [][][int](https://pkg.go.dev/builtin#int)

Combinations generates all of the combinations of k elements from a set of size n. The returned slice has length Binomial(n,k) and each inner slice has length k.

n and k must be non-negative with n >= k, otherwise Combinations will panic.

CombinationGenerator may alternatively be used to generate the combinations iteratively instead of collectively, or IndexToCombination for random access.

Output:

Generate list: 0 [0 1 2] 1 [0 1 3] 2 [0 1 4] 3 [0 2 3] 4 [0 2 4] 5 [0 3 4] 6 [1 2 3] 7 [1 2 4] 8 [1 3 4] 9 [2 3 4] 

Output:

ab ac ad ae bc bd be cd ce de 

GeneralizedBinomial returns the generalized binomial coefficient of (n, k), defined as

Γ(n+1) / (Γ(k+1) Γ(n-k+1))

where Γ is the Gamma function. GeneralizedBinomial is useful for continuous relaxations of the binomial coefficient, or when the binomial coefficient value may overflow int. In the latter case, one may use math/big for an exact computation.

n and k must be non-negative with n >= k, otherwise GeneralizedBinomial will panic.

func IdxFor(sub, dims [][int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

IdxFor converts a multi-dimensional index into a linear index for a multi-dimensional space. sub specifies the index for each dimension, and dims specifies the size of each dimension. IdxFor is the inverse of SubFor. IdxFor panics if any of the entries of sub are negative, any of the entries of dim are non-positive, or if sub[i] >= dims[i] for any i.

func IndexToCombination(dst [][int](https://pkg.go.dev/builtin#int), idx, n, k [int](https://pkg.go.dev/builtin#int)) [][int](https://pkg.go.dev/builtin#int)

IndexToCombination returns the combination corresponding to the given index.

The functions CombinationIndex and IndexToCombination define a bijection between the integers and the Binomial(n, k) number of possible combinations. IndexToCombination returns the inverse of CombinationIndex (up to the order of the elements).

The combination is stored in-place into dst if dst is non-nil, otherwise a new slice is allocated and returned.

IndexToCombination panics if n or k are negative, if k is greater than n, or if idx is not in [0, Binomial(n,k)-1]. IndexToCombination will also panic if dst is non-nil and len(dst) is not k.

Output:

0 [0 1 2] 0 1 [0 1 3] 1 2 [0 1 4] 2 3 [0 2 3] 3 4 [0 2 4] 4 5 [0 3 4] 5 6 [1 2 3] 6 7 [1 2 4] 7 8 [1 3 4] 8 9 [2 3 4] 9 

func IndexToPermutation(dst [][int](https://pkg.go.dev/builtin#int), idx, n, k [int](https://pkg.go.dev/builtin#int)) [][int](https://pkg.go.dev/builtin#int)

IndexToPermutation returns the permutation corresponding to the given index.

The functions PermutationIndex and IndexToPermutation define a bijection between the integers and the NumPermutations(n, k) number of possible permutations. IndexToPermutation returns the inverse of PermutationIndex.

The permutation is stored in-place into dst if dst is non-nil, otherwise a new slice is allocated and returned.

IndexToPermutation panics if n or k are negative, if k is greater than n, or if idx is not in [0, NumPermutations(n,k)-1]. IndexToPermutation will also panic if dst is non-nil and len(dst) is not k.

Output:

0 [0 1 2] 0 1 [0 2 1] 1 2 [1 0 2] 2 3 [1 2 0] 3 4 [2 0 1] 4 5 [2 1 0] 5 6 [0 1 3] 6 7 [0 3 1] 7 8 [1 0 3] 8 9 [1 3 0] 9 10 [3 0 1] 10 11 [3 1 0] 11 12 [0 2 3] 12 13 [0 3 2] 13 14 [2 0 3] 14 15 [2 3 0] 15 16 [3 0 2] 16 17 [3 2 0] 17 18 [1 2 3] 18 19 [1 3 2] 19 20 [2 1 3] 20 21 [2 3 1] 21 22 [3 1 2] 22 23 [3 2 1] 23 

LogGeneralizedBinomial returns the log of the generalized binomial coefficient. See GeneralizedBinomial for more information.

func NumPermutations(n, k [int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

NumPermutations returns the number of permutations when selecting k objects from a set of n objects when the selection order matters. No check is made for overflow.

NumPermutations panics if either n or k is negative, or if k is greater than n.

func PermutationIndex(perm [][int](https://pkg.go.dev/builtin#int), n, k [int](https://pkg.go.dev/builtin#int)) [int](https://pkg.go.dev/builtin#int)

PermutationIndex returns the index of the given permutation.

The functions PermutationIndex and IndexToPermutation define a bijection between the integers and the NumPermutations(n, k) number of possible permutations. PermutationIndex returns the inverse of IndexToPermutation.

PermutationIndex panics if perm is not a permutation of k of the first [0,n) integers, if n or k are negative, or if k is greater than n.

func Permutations(n, k [int](https://pkg.go.dev/builtin#int)) [][][int](https://pkg.go.dev/builtin#int)

Permutations generates all of the permutations of k elements from a set of size n. The returned slice has length NumPermutations(n, k) and each inner slice has length k.

n and k must be non-negative with n >= k, otherwise Permutations will panic.

PermutationGenerator may alternatively be used to generate the permutations iteratively instead of collectively, or IndexToPermutation for random access.

Output:

Generate list: 0 [0 1 2] 1 [0 2 1] 2 [1 0 2] 3 [1 2 0] 4 [2 0 1] 5 [2 1 0] 6 [0 1 3] 7 [0 3 1] 8 [1 0 3] 9 [1 3 0] 10 [3 0 1] 11 [3 1 0] 12 [0 2 3] 13 [0 3 2] 14 [2 0 3] 15 [2 3 0] 16 [3 0 2] 17 [3 2 0] 18 [1 2 3] 19 [1 3 2] 20 [2 1 3] 21 [2 3 1] 22 [3 1 2] 23 [3 2 1] 

Output:

ab ba ac ca ad da bc cb bd db cd dc 

SubFor returns the multi-dimensional subscript for the input linear index to the multi-dimensional space. dims specifies the size of each dimension, and idx specifies the linear index. SubFor is the inverse of IdxFor.

If sub is non-nil the result is stored in-place into sub, and SubFor will panic if len(sub) != len(dims). If sub is nil a new slice of the appropriate length is allocated. SubFor panics if idx < 0 or if idx is greater than or equal to the product of the dimensions.

type CartesianGenerator struct {
	
}

CartesianGenerator iterates over a Cartesian product set.

Output:

Generate products for given lengths: 0 [0 0 0] 1 [0 0 1] 2 [0 0 2] 3 [0 1 0] 4 [0 1 1] 5 [0 1 2] 

func NewCartesianGenerator(lens [][int](https://pkg.go.dev/builtin#int)) *[CartesianGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CartesianGenerator)

NewCartesianGenerator returns a CartesianGenerator for iterating over Cartesian products which are generated on the fly. All values in lens must be positive, otherwise this will panic.

Next moves to the next product of the Cartesian set. It returns false if the generator reached the end of the Cartesian set end.

Product generates one product of the Cartesian set according to the current index which is increased by Next(). Next needs to be called at least one time before this method, otherwise it will panic.

type CombinationGenerator struct {
	
}

CombinationGenerator generates combinations iteratively. The Combinations function may be called to generate all combinations collectively.

Output:

0 [0 1 2] 1 [0 1 3] 2 [0 1 4] 3 [0 2 3] 4 [0 2 4] 5 [0 3 4] 6 [1 2 3] 7 [1 2 4] 8 [1 3 4] 9 [2 3 4] 

func NewCombinationGenerator(n, k [int](https://pkg.go.dev/builtin#int)) *[CombinationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#CombinationGenerator)

NewCombinationGenerator returns a CombinationGenerator for generating the combinations of k elements from a set of size n.

n and k must be non-negative with n >= k, otherwise NewCombinationGenerator will panic.

Combination returns the current combination. If dst is non-nil, it must have length k and the result will be stored in-place into dst. If dst is nil a new slice will be allocated and returned. If all of the combinations have already been constructed (Next() returns false), Combination will panic.

Next must be called to initialize the first value before calling Combination or Combination will panic. The value returned by Combination is only changed during calls to Next.

Next advances the iterator if there are combinations remaining to be generated, and returns false if all combinations have been generated. Next must be called to initialize the first value before calling Combination or Combination will panic. The value returned by Combination is only changed during calls to Next.

type PermutationGenerator struct {
	
}

PermutationGenerator generates permutations iteratively. The Permutations function may be called to generate all permutations collectively.

Output:

0 [0 1 2] 1 [0 2 1] 2 [1 0 2] 3 [1 2 0] 4 [2 0 1] 5 [2 1 0] 6 [0 1 3] 7 [0 3 1] 8 [1 0 3] 9 [1 3 0] 10 [3 0 1] 11 [3 1 0] 12 [0 2 3] 13 [0 3 2] 14 [2 0 3] 15 [2 3 0] 16 [3 0 2] 17 [3 2 0] 18 [1 2 3] 19 [1 3 2] 20 [2 1 3] 21 [2 3 1] 22 [3 1 2] 23 [3 2 1] 

func NewPermutationGenerator(n, k [int](https://pkg.go.dev/builtin#int)) *[PermutationGenerator](https://pkg.go.dev/gonum.org/v1/gonum@v0.17.0/stat/combin#PermutationGenerator)

NewPermutationGenerator returns a PermutationGenerator for generating the permutations of k elements from a set of size n.

n and k must be non-negative with n >= k, otherwise NewPermutationGenerator will panic.

Next advances the iterator if there are permutations remaining to be generated, and returns false if all permutations have been generated. Next must be called to initialize the first value before calling Permutation or Permutation will panic. The value returned by Permutation is only changed during calls to Next.

Permutation returns the current permutation. If dst is non-nil, it must have length k and the result will be stored in-place into dst. If dst is nil a new slice will be allocated and returned. If all of the permutations have already been constructed (Next() returns false), Permutation will panic.

Next must be called to initialize the first value before calling Permutation or Permutation will panic. The value returned by Permutation is only changed during calls to Next.
