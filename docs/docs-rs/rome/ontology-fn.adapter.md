rome::ontology
# Function adapter 
Source 

```
pub fn adapter<'g, G>(graph: &'g G) -> OntologyAdapter<'g, G>where
    G: Graph<'g>,
```