# Exception: Prawn::Fonts::TTF::NoUnicodeCMap
  
  
  

  
  
    Inherits:
    
      Error
      
        

          
- Object
          
            
- StandardError
          
            
- Error
          
            
- Prawn::Fonts::TTF::NoUnicodeCMap
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/ttf.rb
  
  

## Overview

  
    

Signals absence of a Unicode character map in the font.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_MESSAGE =
          
        
        

```
'No unicode cmap found in font'

```

      
        MESSAGE_WITH_FONT =
          
        
        

```
'No unicode cmap found in font %<font>s'

```

      
    
  

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods inherited from Error

  

#initialize

  
  
## Constructor Details

  
    

This class inherits a constructor from Prawn::Fonts::TTF::Error