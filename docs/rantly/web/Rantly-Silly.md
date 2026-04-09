# Module: Rantly::Silly
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/silly.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** Love
    
  
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**love_letter**(n)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**love_letter**(n)  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/rantly/silly.rb', line 4

def love_letter(n)
  Rantly.new.extend(Rantly::Silly::Love).value { letter(n) }
end
```