# Class: RuboCop::Cop::InternalAffairs::NodePatternGroups::ASTProcessor
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::InternalAffairs::NodePatternGroups::ASTProcessor

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      AST::Processor::Mixin
  
    Defined in:
    lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_processor.rb
  
## Overview

AST Processor for NodePattern ASTs, for use with `InternalAffairs/NodePatternGroups`.

Looks for sequences and subsequences where the first item is a `node_type` node, and converts them to `node_sequence` nodes (not a true `RuboCop::AST::NodePattern` node type).

The resulting AST will be walked by `InternalAffairs::NodePatternGroups::ASTWalker` in order to find node types in a `union` node that can be rewritten as a node group.

NOTE: The `on_*` methods in this class relate not to the normal node types but rather to the Node Pattern node types. Not every node type is handled.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**handler_missing**(node)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**on_sequence**(node)  ⇒ Object 
    

    
      (also: #on_subsequence)
    
  
  
  
  
  
  
  
  

  
    

Look for `sequence` and `subsequence` nodes that contain a `node_type` node as their first child.

## Instance Method Details

###
  
    #**handler_missing**(node)  ⇒ Object 
  

  

  

  
    
      

```

22
23
24
```

```
# File 'lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_processor.rb', line 22

def handler_missing(node)
  node.updated(nil, process_children(node))
end

```

###
  
    #**on_sequence**(node)  ⇒ Object 
  

  
    Also known as:
    on_subsequence
    
  

  

  
    

Look for `sequence` and `subsequence` nodes that contain a `node_type` node as their first child. These are rewritten as `node_sequence` nodes so that it is possible to compare nodes while looking for replacement candidates for node groups. This is necessary so that extended patterns can be matched and replaced. ie. ‘_:foo …) (csend_ :foo …)` can become `(call _ :foo …)`

```

31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
```

```
# File 'lib/rubocop/cop/internal_affairs/node_pattern_groups/ast_processor.rb', line 31

def on_sequence(node)
  first_child = node.child

  if first_child.type == :node_type
    children = [first_child.child, *process_children(node, 1..)]

    # The `node_sequence` node contains the `node_type` symbol as its first child,
    # followed by all the other nodes contained in the `sequence` node.
    # The location is copied from the sequence, so that the entire sequence can
    # eventually be corrected in the cop.
    n(:node_sequence, children, location: node.location)
  else
    node.updated(nil, process_children(node))
  end
end

```
