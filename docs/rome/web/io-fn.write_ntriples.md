rome::io
# Function write_ntriples 
Source 

```
pub fn write_ntriples<'g, G, T, I, W>(
    triples: I,
    graph: &'g G,
    writer: &mut W,
) -> Result<()>where
    T: Triple<'g, G::BlankNodePtr, G::IRIPtr, G::LiteralPtr> + 'g,
    G: Graph<'g> + 'g,
    <G as Graph<'g>>::BlankNodePtr: Display,
    I: Iterator<Item = T>,
    W: Write,
```