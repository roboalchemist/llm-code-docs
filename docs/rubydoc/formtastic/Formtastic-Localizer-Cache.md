# Class: Formtastic::Localizer::Cache
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Formtastic::Localizer::Cache
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/formtastic/localizer.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**cache**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**clear!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**get**(key)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**has_key?**(key)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**set**(key, result)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**cache**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 41

def cache
  @cache ||= {}
end
```

    
  

    
      
  
### 
  
    #**clear!**  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 45

def clear!
  cache.clear
end
```

    
  

    
      
  
### 
  
    #**get**(key)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 29

def get(key)
  cache[key]
end
```

    
  

    
      
  
### 
  
    #**has_key?**(key)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 33

def has_key?(key)
  cache.has_key?(key)
end
```

    
  

    
      
  
### 
  
    #**set**(key, result)  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/formtastic/localizer.rb', line 37

def set(key, result)
  cache[key] = result
end
```