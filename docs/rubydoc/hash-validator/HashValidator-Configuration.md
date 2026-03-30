# Class: HashValidator::Configuration
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- HashValidator::Configuration
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/hash_validator/configuration.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_validator**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_validator**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_validator**(*args)  ⇒ Object 
  

  

  

  
    
      

```

5
6
7
```

    
    
      

```
# File 'lib/hash_validator/configuration.rb', line 5

def add_validator(*args)
  HashValidator.add_validator(*args)
end
```

    
  

    
      
  
### 
  
    #**remove_validator**(name)  ⇒ Object 
  

  

  

  
    
      

```

9
10
11
```

    
    
      

```
# File 'lib/hash_validator/configuration.rb', line 9

def remove_validator(name)
  HashValidator.remove_validator(name)
end
```