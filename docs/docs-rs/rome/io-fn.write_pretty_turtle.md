rome::io
# Function write_pretty_turtle 
Source 

```
pub fn write_pretty_turtle<'g, G, W>(
    namespaces: &Namespaces,
    graph: &'g G,
    writer: &mut W,
) -> Result<()>where
    G: Graph<'g> + 'g,
    <G as Graph<'g>>::BlankNodePtr: Display,
    W: Write,
```