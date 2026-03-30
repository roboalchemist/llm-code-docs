# Exception: Prawn::Text::Formatted::Arranger::BadFontFamily
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Prawn::Text::Formatted::Arranger::BadFontFamily
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/formatted/arranger.rb
  
  

## Overview

  
    

You’re getting this because a font doesn’t have a family name.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(message = 'Bad font family')  ⇒ BadFontFamily 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BadFontFamily.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(message = 'Bad font family')  ⇒ BadFontFamily 
  

  

  

  
    

Returns a new instance of BadFontFamily.

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 29

def initialize(message = 'Bad font family')
  super
end

```