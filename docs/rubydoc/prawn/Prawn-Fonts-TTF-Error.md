# Exception: Prawn::Fonts::TTF::Error
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Prawn::Fonts::TTF::Error
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/ttf.rb
  
  

## Overview

  
    

TrueType font error.

  

  

  
## Direct Known Subclasses

  

NoPostscriptName, NoUnicodeCMap

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_MESSAGE =
          
        
        

```
'TTF font error'

```

      
        MESSAGE_WITH_FONT =
          
        
        

```
'TTF font error in font %<font>s'

```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(message = DEFAULT_MESSAGE, font: nil)  ⇒ Error 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Error.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(message = DEFAULT_MESSAGE, font: nil)  ⇒ Error 
  

  

  

  
    

Returns a new instance of Error.

  

  

  
    
      

```

28
29
30
31
32
33
34
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 28

def initialize(message = DEFAULT_MESSAGE, font: nil)
  if font && message == DEFAULT_MESSAGE
    super(format(MESSAGE_WITH_FONT, font: font))
  else
    super(message)
  end
end

```