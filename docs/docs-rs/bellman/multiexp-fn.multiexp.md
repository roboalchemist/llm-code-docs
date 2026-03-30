bellman::multiexp
# Function multiexp 
Source 

```
pub fn multiexp<Q, D, G, S>(
    pool: &Worker,
    bases: S,
    density_map: D,
    exponents: Arc<Vec<Exponent<G::Scalar>>>,
) -> Waiter<Result<G, SynthesisError>>where
    for<'a> &'a Q: QueryDensity,
    D: Send + Sync + 'static + Clone + AsRef<Q>,
    G: PrimeCurve,
    G::Scalar: PrimeFieldBits,
    S: SourceBuilder<<G as PrimeCurve>::Affine>,
```