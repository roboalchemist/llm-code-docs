### Overview ¶

Package parseutil contains utilities built on top of the parse package.

### Index ¶

-
        func FindLeafNode(n parse.Node, p int) parse.Node

-
        func Wordify(src string) []string

### Constants ¶

This section is empty.

### Variables ¶

This section is empty.

### Functions ¶

####

      func FindLeafNode ¶
  
    
  

    
    
      

```
func FindLeafNode(n parse.Node, p int) parse.Node
```

FindLeafNode finds the leaf node at a specific position. It returns nil if
position is out of bound.

####

      func Wordify ¶
  
    
  

    
    
      

```
func Wordify(src string) []string
```

Wordify turns a piece of source code into words.

### Types ¶

This section is empty.
