# Module: SimpleForm::MapType
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    FormBuilder
  
  

  
  
    Defined in:
    lib/simple_form/map_type.rb
  
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**extended**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**map_type**(*types)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**extended**(base)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
```

    
    
      

```
# File 'lib/simple_form/map_type.rb', line 6

def self.extended(base)
  base.class_attribute :mappings
  base.mappings = {}
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**map_type**(*types)  ⇒ Object 
  

  

  

  
    

  

  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

11
12
13
14
15
```

    
    
      

```
# File 'lib/simple_form/map_type.rb', line 11

def map_type(*types)
  map_to = types.extract_options![:to]
  raise ArgumentError, "You need to give :to as option to map_type" unless map_to
  self.mappings = mappings.merge types.each_with_object({}) { |t, m| m[t] = map_to }
end
```