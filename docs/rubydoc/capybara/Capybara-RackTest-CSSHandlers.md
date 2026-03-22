# Class: Capybara::RackTest::CSSHandlers
  
  
  

  
  
    Inherits:
    
      BasicObject
      
    
  
  

  
  
  
  
  
      Includes:
      Kernel
  
  
  

  

  
  
    Defined in:
    lib/capybara/rack_test/css_handlers.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**disabled**(list)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**enabled**(list)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**disabled**(list)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/capybara/rack_test/css_handlers.rb', line 6

def disabled(list)
  list.find_all { |node| node.has_attribute? 'disabled' }
end
```

    
  

    
      
  
### 
  
    #**enabled**(list)  ⇒ Object 
  

  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/capybara/rack_test/css_handlers.rb', line 10

def enabled(list)
  list.find_all { |node| !node.has_attribute? 'disabled' }
end
```