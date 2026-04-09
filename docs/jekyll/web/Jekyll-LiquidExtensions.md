# Module: Jekyll::LiquidExtensions
  
    Defined in:
    lib/jekyll/liquid_extensions.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**lookup_variable**(context, variable)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Lookup a Liquid variable in the given context.

## Instance Method Details

###
  
    #**lookup_variable**(context, variable)  ⇒ Object 
  

  

  

  
    

Lookup a Liquid variable in the given context.

context  - the Liquid context in question. variable - the variable name, as a string.

Returns the value of the variable in the context

```
or the variable name if not found.

```

```

12
13
14
15
16
17
18
19
20
```

```
# File 'lib/jekyll/liquid_extensions.rb', line 12

def lookup_variable(context, variable)
  lookup = context

  variable.split(".").each do |value|
    lookup = lookup[value]
  end

  lookup || variable
end
```
