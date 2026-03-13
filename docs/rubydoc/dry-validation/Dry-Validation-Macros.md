# Module: Dry::Validation::Macros
  
    Defined in:
    lib/dry/validation/macros.rb
  
## Overview

API for registering and accessing Rule macros

API:

-

public

## Defined Under Namespace

      **Modules:** Registrar
    
  
    
      **Classes:** Container
    
  

  
    
##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**[]**(name)  ⇒ Proc 
    

    
  
  
  
  
  
  
  
  

  
    

Return a registered macro.

-
  
      .**container**  ⇒ Object 

  private

-
  
      .**register**  ⇒ Macros 

Register a global macro.

## Class Method Details

###
  
    .**[]**(name)  ⇒ Proc 
  

  

  

  
    

Return a registered macro

Parameters:

-

The name of the macro

Returns:

-

API:

-

public

```

72
73
74
```

```
# File 'lib/dry/validation/macros.rb', line 72

def self.[](name)
  container[name]
end
```

###
  
    .**container**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

API:

-

private

```

89
90
91
```

```
# File 'lib/dry/validation/macros.rb', line 89

def self.container
  @container ||= Container.new
end
```

###
  
    .**register**  ⇒ Macros 
  

  

  

  
    

Register a global macro

Returns:

-

See Also:
  
- Dry::Validation::Macros::Container#register

API:

-

public

```

83
84
85
86
```

```
# File 'lib/dry/validation/macros.rb', line 83

def self.register(...)
  container.register(...)
  self
end
```
