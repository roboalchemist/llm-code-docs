# Module: Dry::Validation::Macros::Registrar
  
    Included in:
    Dry::Validation, Contract::ClassInterface
  
  

  
  
    Defined in:
    lib/dry/validation/macros.rb
  
  

  
    

  

  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**register_macro**  ⇒ self 
    

    
  
  
  
  
  
  
  
  

  
    

Register a macro.

## Instance Method Details

###
  
    #**register_macro**  ⇒ self 
  

  

  

  
    

Register a macro

#### Examples

#####

register a global macro

```
Dry::Validation.register_macro(:even_numbers) do
  key.failure('all numbers must be even') unless values[key_name].all?(&:even?)
end
```

#####

register a contract macro

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

-

        args

        (Array)
      
      
      
        —
        

Optional default positional arguments for the macro

Returns:

-

        (self)

See Also:
  
- Dry::Validation::Macro

```

32
33
34
35
```

```
# File 'lib/dry/validation/macros.rb', line 32

def register_macro(...)
  macros.register(...)
  self
end
```
