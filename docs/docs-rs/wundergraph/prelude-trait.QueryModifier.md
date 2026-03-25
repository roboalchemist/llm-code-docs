wundergraph::prelude
# Trait QueryModifier 
Source 

```
pub trait QueryModifier<L, DB>: WundergraphContext + Sizedwhere
    L: LoadingHandler<DB, Self>,
    DB: Backend + ApplyOffset + 'static,{
    // Required method
    fn modify_query<'a>(
        &self,
        select: &LookAheadSelection<'_, WundergraphScalarValue>,
        query: BoxedQuery<'a, L, DB, Self>,
    ) -> Result<BoxedQuery<'a, L, DB, Self>>;
}
```

## Required Methods§