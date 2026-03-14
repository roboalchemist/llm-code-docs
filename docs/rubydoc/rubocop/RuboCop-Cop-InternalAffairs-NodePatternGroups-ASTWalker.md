# Class: RuboCop::Cop::InternalAffairs::NodePatternGroups::ASTWalker
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::InternalAffairs::NodePatternGroups::ASTWalker

        show all
      

    Defined in:
    lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_walker.rb
  
## Overview

Walks an AST that has been processed by `InternalAffairs::NodePatternGroups::Processor` in order to find `node_type` and `node_sequence` nodes that can be replaced with a node group in `InternalAffairs/NodePatternGroups`.

Calling ‘ASTWalker#walk` sets `node_groups` with an array of `NodeGroup` structs that contain metadata about nodes that can be replaced, including location data. That metadata is used by the cop to register offenses and perform corrections.

## Defined Under Namespace

      **Classes:** NodeGroup
    
  
## Instance Attribute Summary collapse

-
  
      #**node_groups**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute node_groups.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**  ⇒ ASTWalker 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ASTWalker.

-
  
      #**on_union**(node)  ⇒ Object 

Search `union` nodes for `node_type` and `node_sequence` nodes that can be collapsed into a node group.

-
  
      #**reset!**  ⇒ Object 

-
  
      #**walk**(node)  ⇒ Object 

Recursively walk the AST in a depth-first manner.

## Constructor Details

###
  
    #**initialize**  ⇒ ASTWalker 
  

  

  

  
    

Returns a new instance of ASTWalker.

```

30
31
32
```

```
# File 'lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_walker.rb', line 30

def initialize
  reset!
end
```

## Instance Attribute Details

###
  
    #**node_groups**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute node_groups.

```

38
39
40
```

```
# File 'lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_walker.rb', line 38

def node_groups
  @node_groups
end
```

## Instance Method Details

###
  
    #**on_union**(node)  ⇒ Object 
  

  

  

  
    

Search `union` nodes for `node_type` and `node_sequence` nodes that can be collapsed into a node group.

-

`node_type` nodes are nodes with no further configuration (ie. `send`)

-

`node_sequence` nodes are nodes with further configuration (ie. ‘(send …)`)

Each group of types that can be collapsed will have a `NodeGroup` record added to `node_groups`, which is then used by the cop.

```

59
60
61
62
63
64
65
66
67
68
69
70
71
```

```
# File 'lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_walker.rb', line 59

def on_union(node)
  all_node_types = each_child_node(node, :node_type, :node_sequence).to_a

  each_node_group(all_node_types) do |group_name, node_types|
    next unless sequences_match?(node_types)

    node_groups << node_group_data(
      group_name, node, node_types,
      all_node_types.index(node_types.first),
      (node.children - node_types).any?
    )
  end
end
```

###
  
    #**reset!**  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
```

```
# File 'lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_walker.rb', line 34

def reset!
  @node_groups = []
end
```

###
  
    #**walk**(node)  ⇒ Object 
  

  

  

  
    

Recursively walk the AST in a depth-first manner. Only `union` nodes are handled further.

```

42
43
44
45
46
47
48
49
50
```

```
# File 'lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_walker.rb', line 42

def walk(node)
  return if node.nil?

  on_union(node) if node.type == :union

  node.child_nodes.each do |child|
    walk(child)
  end
end
```
