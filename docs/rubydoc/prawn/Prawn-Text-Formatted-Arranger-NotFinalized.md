# Exception: Prawn::Text::Formatted::Arranger::NotFinalized
  
  
  

  
  
    Inherits:
    
      StandardError
      
        

          
- Object
          
            
- StandardError
          
            
- Prawn::Text::Formatted::Arranger::NotFinalized
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/formatted/arranger.rb
  
  

## Overview

  
    

You’re getting this because you’re trying to get some information from the arranger before it finished processing text.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DEFAULT_MESSAGE =
          
        
        

```
'Lines must be finalized'

```

      
        MESSAGE_WITH_METHOD =
          
        
        

```
'Lines must be finalized before calling #%<method>s'

```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(message = DEFAULT_MESSAGE, method: nil)  ⇒ NotFinalized 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of NotFinalized.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(message = DEFAULT_MESSAGE, method: nil)  ⇒ NotFinalized 
  

  

  

  
    

Returns a new instance of NotFinalized.

  

  

  
    
      

```

18
19
20
21
22
23
24
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 18

def initialize(message = DEFAULT_MESSAGE, method: nil)
  if method && message == DEFAULT_MESSAGE
    super(format(MESSAGE_WITH_METHOD, method: method))
  else
    super(message)
  end
end

```