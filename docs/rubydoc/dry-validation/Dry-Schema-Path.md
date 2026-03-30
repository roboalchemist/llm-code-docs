# Class: Dry::Schema::Path
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Schema::Path

        show all
      

    Defined in:
    lib/dry/validation/schema_ext.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**expand**  ⇒ Object 
    

    
  
  private

-
  
      #**multi_value?**  ⇒ Boolean 

  private

## Instance Method Details

###
  
    #**expand**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

14
15
16
```

```
# File 'lib/dry/validation/schema_ext.rb', line 14

def expand
  to_a[0..-2].product(last).map { |spec| self.class[spec] }
end
```

###
  
    #**multi_value?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns:

-

        (Boolean)

```

9
10
11
```

```
# File 'lib/dry/validation/schema_ext.rb', line 9

def multi_value?
  last.is_a?(::Array)
end
```
