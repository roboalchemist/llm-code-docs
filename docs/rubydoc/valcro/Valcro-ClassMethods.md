# Module: Valcro::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/valcro.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**validate**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validates_with**(validator_class)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validation_blocks**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**validators**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**validate**(&block)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/valcro.rb', line 57

def validate(&block)
  validation_blocks << block
end
```

    
  

    
      
  
### 
  
    #**validates_with**(validator_class)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/valcro.rb', line 45

def validates_with(validator_class)
  validators << validator_class
end
```

    
  

    
      
  
### 
  
    #**validation_blocks**  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/valcro.rb', line 53

def validation_blocks
  @validation_blocks ||= []
end
```

    
  

    
      
  
### 
  
    #**validators**  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/valcro.rb', line 49

def validators
  @validators ||= []
end
```