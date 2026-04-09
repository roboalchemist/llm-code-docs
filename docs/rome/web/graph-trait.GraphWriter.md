rome::graph
# Trait GraphWriter 
Source 

```
pub trait GraphWriter<'g> {
    type BlankNode: Clone;
    type IRI: Clone;
    type Literal;
    type Datatype: Clone;
    type Language;
    type Graph: Graph<'g>;

}
```

## Required Associated Types§