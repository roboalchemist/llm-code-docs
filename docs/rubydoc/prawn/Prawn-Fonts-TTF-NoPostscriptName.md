# Exception: Prawn::Fonts::TTF::NoPostscriptName
  
  
  

  
  
    Inherits:
    
      Error
      
        

          
- Object
          
            
- StandardError
          
            
- Error
          
            
- Prawn::Fonts::TTF::NoPostscriptName
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/ttf.rb
  
  

## Overview

  
    

Signals absense of a PostScript font name.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_MESSAGE =
          
        
        

```
'Can not detect a postscript name'

```

      
        MESSAGE_WITH_FONT =
          
        
        

```
'Can not detect a postscript name in font %<font>s'

```

      
    
  

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods inherited from Error

  

#initialize

  
  
## Constructor Details

  
    

This class inherits a constructor from Prawn::Fonts::TTF::Error