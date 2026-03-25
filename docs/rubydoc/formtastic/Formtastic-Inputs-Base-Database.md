# Module: Formtastic::Inputs::Base::Database
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/database.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**column**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**column?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**column**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
```

    
    
      

```
# File 'lib/formtastic/inputs/base/database.rb', line 7

def column
  if object.respond_to?(:column_for_attribute)
    object.column_for_attribute(method)
  end
end
```

    
  

    
      
  
### 
  
    #**column?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/formtastic/inputs/base/database.rb', line 13

def column?
  !column.nil?
end
```