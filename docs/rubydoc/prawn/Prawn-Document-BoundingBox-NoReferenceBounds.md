# Exception: Prawn::Document::BoundingBox::NoReferenceBounds
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Prawn::Document::BoundingBox::NoReferenceBounds
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/document/bounding_box.rb
  
  

## Overview

  
    

Indicates absence of a reference bounding box of a fixed height.

  

  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**initialize**(message = "Can't find reference bounds: my parent is unset")  ⇒ NoReferenceBounds 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of NoReferenceBounds.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(message = "Can't find reference bounds: my parent is unset")  ⇒ NoReferenceBounds 
  

  

  

  
    

Returns a new instance of NoReferenceBounds.

  

  

  
    
      

```

246
247
248
```

    
    
      

```
# File 'lib/prawn/document/bounding_box.rb', line 246

def initialize(message = "Can't find reference bounds: my parent is unset")
  super
end

```