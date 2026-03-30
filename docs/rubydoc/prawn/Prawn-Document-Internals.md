# Module: Prawn::Document::Internals
  
  
  

  

  
  
  
      Extended by:
      Forwardable
  
  
  
  
  

  
  
    Included in:
    Prawn::Document
  
  

  
  
    Defined in:
    lib/prawn/document/internals.rb
  
  

## Overview

  
    

This module exposes a few low-level PDF features for those who want to extend Prawn’s core functionality.  If you are not comfortable with low level PDF functionality as defined by Adobe’s specification, chances are you won’t need anything you find here.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**renderer**  ⇒ PDF::Core::Renderer 
    

    
  
  
  
  
  
  
  
  

  
    

Document renderer.

  

      
        
- 
  
    
      #**restore_graphics_state**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Restore graphic state.

  

      
        
- 
  
    
      #**save_graphics_state**(state = nil) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Save current graphics state.

  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**renderer**  ⇒ PDF::Core::Renderer 
  

  

  

  
    

Document renderer.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/prawn/document/internals.rb', line 71

def renderer
  @renderer ||= PDF::Core::Renderer.new(state)
end

```

    
  

    
      
  
### 
  
    #**restore_graphics_state**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Restore graphic state.

  

  

  
    
      

```

38
39
40
41
```

    
    
      

```
# File 'lib/prawn/document/internals.rb', line 38

def restore_graphics_state
  restore_transformation_stack
  renderer.restore_graphics_state
end

```

    
  

    
      
  
### 
  
    #**save_graphics_state**(state = nil) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Save current graphics state.

  

  

Yields:

  
    
- 
      
      
        
      
      
      
        
        

Restores graphic state after the block.

      
    
  

  
    
      

```

29
30
31
32
33
```

    
    
      

```
# File 'lib/prawn/document/internals.rb', line 29

def save_graphics_state(state = nil, &block)
  save_transformation_stack
  renderer.save_graphics_state(state, &block)
  restore_transformation_stack if block
end

```