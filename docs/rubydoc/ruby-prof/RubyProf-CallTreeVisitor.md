# Class: RubyProf::CallTreeVisitor
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- RubyProf::CallTreeVisitor
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/ruby-prof/call_tree_visitor.rb
  
  

## Overview

  
    

The call info visitor class does a depth-first traversal across a list of call infos. At each call_tree node, the visitor executes the block provided in the #visit method. The block is passed two parameters, the event and the call_tree instance. Event will be either :enter or :exit.

```
visitor = RubyProf::CallTreeVisitor.new(result.threads.first.call_tree)

method_names = Array.new

visitor.visit do |call_tree, event|
  method_names << call_tree.target.full_name if event == :enter
end

puts method_names

```

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(call_tree, max_depth: nil)  ⇒ CallTreeVisitor 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CallTreeVisitor.

  

      
        
- 
  
    
      #**visit**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(call_tree, max_depth: nil)  ⇒ CallTreeVisitor 
  

  

  

  
    

Returns a new instance of CallTreeVisitor.

  

  

  
    
      

```

18
19
20
21
```

    
    
      

```
# File 'lib/ruby-prof/call_tree_visitor.rb', line 18

def initialize(call_tree, max_depth: nil)
  @call_tree = call_tree
  @max_depth = max_depth
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**visit**(&block)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/ruby-prof/call_tree_visitor.rb', line 23

def visit(&block)
  visit_call_tree(@call_tree, 0, &block)
end
```