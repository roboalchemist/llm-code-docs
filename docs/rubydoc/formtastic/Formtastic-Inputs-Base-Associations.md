# Module: Formtastic::Inputs::Base::Associations
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Formtastic::Inputs::Base
  
  

  
  
    Defined in:
    lib/formtastic/inputs/base/associations.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**association**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:belongs_to, etc.

  

      
        
- 
  
    
      #**association_primary_key**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**belongs_to?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**has_many?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reflection**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**association**  ⇒ Object 
  

  

  

  
    

:belongs_to, etc

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/formtastic/inputs/base/associations.rb', line 9

def association
  @association ||= association_macro_for_method(method)
end
```

    
  

    
      
  
### 
  
    #**association_primary_key**  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/formtastic/inputs/base/associations.rb', line 25

def association_primary_key
  association_primary_key_for_method(method)
end
```

    
  

    
      
  
### 
  
    #**belongs_to?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/formtastic/inputs/base/associations.rb', line 17

def belongs_to?
  association == :belongs_to
end
```

    
  

    
      
  
### 
  
    #**has_many?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/formtastic/inputs/base/associations.rb', line 21

def has_many?
  association == :has_many
end
```

    
  

    
      
  
### 
  
    #**reflection**  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/formtastic/inputs/base/associations.rb', line 13

def reflection
  @reflection ||= reflection_for(method)
end
```