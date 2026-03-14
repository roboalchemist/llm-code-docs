# Class: ActionCable::Connection::TestRequest
  
  
  

  
  
    Inherits:
    
      ActionDispatch::TestRequest
      
        

          
- Object
          
            
- ActionDispatch::TestRequest
          
            
- ActionCable::Connection::TestRequest
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**cookie_jar**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute cookie_jar.

  

    
      
- 
  
    
      #**session**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute session.

  

    
  

  
  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**cookie_jar**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute cookie_jar.

  

  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 54

def cookie_jar
  @cookie_jar
end
```

    
  

    
      
      
      
  
### 
  
    #**session**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute session.

  

  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 54

def session
  @session
end
```