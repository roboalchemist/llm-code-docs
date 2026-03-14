rome::io
# Function write_turtle 
Source 

```
pub fn write_turtle<'g, G, T, I, W>(
    namespaces: &Namespaces,
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