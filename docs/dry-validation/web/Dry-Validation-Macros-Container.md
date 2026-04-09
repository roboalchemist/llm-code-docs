# Class: Dry::Validation::Macros::Container
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Macros::Container

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Core::Container::Mixin
  
    Defined in:
    lib/dry/validation/macros.rb
  
## Overview

Registry for macros

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**register**(name, *args, &block)  ⇒ self 
    

    
  
  
  
  
  
  
  
  

  
    

Register a new macro.

## Instance Method Details

###
  
    #**register**(name, *args, &block)  ⇒ self 
  

  

  

  
    

Register a new macro

#### Examples

#####

in a contract class

```
class MyContract < Dry::Validation::Contract
  register_macro(:even_numbers) do
    key.failure('all numbers must be even') unless values[key_name].all?(&:even?)
  end
end
```

Parameters:

-

        name

        (Symbol)
      
      
      
        —
        

The name of the macro

Returns:

-

        (self)

```

58
59
60
61
62
```

```
# File 'lib/dry/validation/macros.rb', line 58

def register(name, *args, &block)
  macro = Macro.new(name, args: args, block: block)
  super(name, macro, call: false, &nil)
  self
end
```
