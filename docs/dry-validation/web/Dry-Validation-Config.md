# Class: Dry::Validation::Config
  
    Inherits:
    
      Schema::Config
      
        

          
- Object

- Schema::Config

- Dry::Validation::Config

        show all
      

    Defined in:
    lib/dry/validation/config.rb
  
## Overview

Configuration for contracts

See Also:
  
- Dry::Validation::Contract#config

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**dup**  ⇒ Object 
    

    
  
  private

## Instance Method Details

###
  
    #**dup**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

14
15
16
17
18
```

```
# File 'lib/dry/validation/config.rb', line 14

def dup
  config = super
  config.macros = macros.dup
  config
end
```
