bellman
# Trait ConstraintSystem 
Source 

```
pub trait ConstraintSystem<Scalar: PrimeField>: Sized {
    type Root: ConstraintSystem<Scalar>;

    // Required methods
    fn alloc<F, A, AR>(
        &mut self,
        annotation: A,
        f: F,
    ) -> Result<Variable, SynthesisError>
       where F: FnOnce() -> Result<Scalar, SynthesisError>,
             A: FnOnce() -> AR,
             AR: Into<String>;
    fn alloc_input<F, A, AR>(
        &mut self,
        annotation: A,
        f: F,
    ) -> Result<Variable, SynthesisError>
       where F: FnOnce() -> Result<Scalar, SynthesisError>,
             A: FnOnce() -> AR,
             AR: Into<String>;
    fn enforce<A, AR, LA, LB, LC>(&mut self, annotation: A, a: LA, b: LB, c: LC)
       where A: FnOnce() -> AR,
             AR: Into<String>,
             LA: FnOnce(LinearCombination<Scalar>) -> LinearCombination<Scalar>,
             LB: FnOnce(LinearCombination<Scalar>) -> LinearCombination<Scalar>,
             LC: FnOnce(LinearCombination<Scalar>) -> LinearCombination<Scalar>;
    fn push_namespace<NR, N>(&mut self, name_fn: N)
       where NR: Into<String>,
             N: FnOnce() -> NR;
    fn pop_namespace(&mut self);
    fn get_root(&mut self) -> &mut Self::Root;

    // Provided methods
    fn one() -> Variable { ... }
    fn namespace<NR, N>(
        &mut self,
        name_fn: N,
    ) -> Namespace<'_, Scalar, Self::Root>
       where NR: Into<String>,
             N: FnOnce() -> NR { ... }
}
```

## Required Associated Types§