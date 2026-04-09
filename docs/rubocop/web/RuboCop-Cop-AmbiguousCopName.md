# Exception: RuboCop::Cop::AmbiguousCopName
  
    Inherits:
    
      Error
      
        

          
- Object

- StandardError

- Error

- RuboCop::Cop::AmbiguousCopName

        show all
      

    Defined in:
    lib/rubocop/cop/registry.rb
  
## Overview

Error raised when an unqualified cop name is used that could refer to two or more cops under different departments

##

      Constant Summary
      collapse
    

    
      
        MSG =
          
        
        

```
'Ambiguous cop name `%<name>s` used in %<origin>s needs ' \
'department qualifier. Did you mean %<options>s?'

```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(name, origin, badges)  ⇒ AmbiguousCopName 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AmbiguousCopName.

## Constructor Details

###
  
    #**initialize**(name, origin, badges)  ⇒ AmbiguousCopName 
  

  

  

  
    

Returns a new instance of AmbiguousCopName.

```

11
12
13
14
15
```

```
# File 'lib/rubocop/cop/registry.rb', line 11

def initialize(name, origin, badges)
  super(
    format(MSG, name: name, origin: origin, options: badges.to_a.join(' or '))
  )
end

```
