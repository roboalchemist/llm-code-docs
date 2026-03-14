# Module: ActionCable::Connection::Callbacks::ClassMethods
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/callbacks.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**after_command**(*methods, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**around_command**(*methods, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**before_command**(*methods, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**after_command**(*methods, &block)  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
```

    
    
      

```
# File 'lib/action_cable/connection/callbacks.rb', line 47

def after_command(*methods, &block)
  set_callback(:command, :after, *methods, &block)
end
```

    
  

    
      
  
### 
  
    #**around_command**(*methods, &block)  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/action_cable/connection/callbacks.rb', line 51

def around_command(*methods, &block)
  set_callback(:command, :around, *methods, &block)
end
```

    
  

    
      
  
### 
  
    #**before_command**(*methods, &block)  ⇒ Object 
  

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/action_cable/connection/callbacks.rb', line 43

def before_command(*methods, &block)
  set_callback(:command, :before, *methods, &block)
end
```