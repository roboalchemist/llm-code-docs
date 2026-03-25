verify::serde
# Trait Spans 
Source 

```
pub trait Spans: Clone + Default {
    type Span: Span;

    // Required methods
    fn key<S: ?Sized + Serialize>(&mut self, key: &S) -> NewSpan<Self::Span>;
    fn value<S: ?Sized + Serialize>(&mut self, value: &S) -> NewSpan<Self::Span>;
    fn unit(&mut self) -> NewSpan<Self::Span>;
    fn map_start(&mut self) -> NewSpan<Self::Span>;
    fn map_end(&mut self) -> NewSpan<Self::Span>;
    fn seq_start(&mut self) -> NewSpan<Self::Span>;
    fn seq_end(&mut self) -> NewSpan<Self::Span>;
    fn descend(&self) -> Self;
}
```
Available on **crate feature `serde`** only.
## Required Associated Types§