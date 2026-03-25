rome::graph
# Trait Graph 
Source 

```
pub trait Graph<'g> {
    type BlankNodePtr: BlankNodePtr<'g> + Ord + Clone + 'g;
    type IRIPtr: IRIPtr<'g> + Ord + Clone + 'g;
    type LiteralPtr: LiteralPtr<'g> + Ord + Clone;
    type SPOTriple: Triple<'g, Self::BlankNodePtr, Self::IRIPtr, Self::LiteralPtr> + Ord + Clone;
    type SPOIter: SortedIterator<Item = Self::SPOTriple>;
    type SPORangeIter: SortedIterator<Item = Self::SPOTriple>;
    type OPSTriple: Triple<'g, Self::BlankNodePtr, Self::IRIPtr, Self::LiteralPtr> + Ord + Clone;
    type OPSRangeIter: SortedIterator<Item = Self::OPSTriple>;

    // Required methods
    fn iter(&'g self) -> Self::SPOIter;
    fn find_datatype<'a>(
        &'g self,
        datatype: &'a str,
    ) -> Option<<Self::LiteralPtr as LiteralPtr<'g>>::DatatypePtr>;
    fn find_iri<'a>(&'g self, iri: &'a str) -> Option<Self::IRIPtr>;
    fn find_literal<'a>(
        &'g self,
        literal: &'a str,
        datatype: &'a str,
        language: Option<&'a str>,
    ) -> Option<Self::LiteralPtr>;
    fn iter_s(
        &'g self,
        subject: &BlankNodeOrIRI<'g, Self::BlankNodePtr, Self::IRIPtr>,
    ) -> Self::SPORangeIter;
    fn iter_s_p(
        &'g self,
        subject: &BlankNodeOrIRI<'g, Self::BlankNodePtr, Self::IRIPtr>,
        predicate: &Self::IRIPtr,
    ) -> Self::SPORangeIter;
    fn iter_o(
        &'g self,
        object: &Resource<'g, Self::BlankNodePtr, Self::IRIPtr, Self::LiteralPtr>,
    ) -> Self::OPSRangeIter;
    fn iter_o_p(
        &'g self,
        object: &Resource<'g, Self::BlankNodePtr, Self::IRIPtr, Self::LiteralPtr>,
        predicate: &Self::IRIPtr,
    ) -> Self::OPSRangeIter;
    fn empty_spo_range(&'g self) -> Self::SPORangeIter;
    fn empty_ops_range(&'g self) -> Self::OPSRangeIter;
}
```

## Required Associated Types§