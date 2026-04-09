# Module: Rantly::Check
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/spec.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**check**(n = 100, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**sample**(n = 100, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**check**(n = 100, &block)  ⇒ Object 
  

  

  

  
    
      

```

3
4
5
```

    
    
      

```
# File 'lib/rantly/spec.rb', line 3

def check(n = 100, &block)
  Rantly.gen.each(n, &block)
end

```

    
  

    
      
  
### 
  
    #**sample**(n = 100, &block)  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
```

    
    
      

```
# File 'lib/rantly/spec.rb', line 7

def sample(n = 100, &block)
  Rantly.gen.map(n, &block)
end

```