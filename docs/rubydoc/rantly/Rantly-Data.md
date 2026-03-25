# Module: Rantly::Data
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Rantly
  
  

  
  
    Defined in:
    lib/rantly/data.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**email**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**password**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**email**  ⇒ Object 
  

  

  

  
    
      

```

2
3
4
```

    
    
      

```
# File 'lib/rantly/data.rb', line 2

def email
  "#{string(:alnum)}@#{string(:alnum)}.#{sized(3) { string(:alpha) }}".downcase
end
```

    
  

    
      
  
### 
  
    #**password**  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/rantly/data.rb', line 6

def password
  sized(8) { string(:alnum) }
end
```