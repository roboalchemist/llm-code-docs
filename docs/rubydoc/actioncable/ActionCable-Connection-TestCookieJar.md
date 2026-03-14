# Class: ActionCable::Connection::TestCookieJar
  
  
  

  
  
    Inherits:
    
      TestCookies
      
        

          
- Object
          
            
- ActiveSupport::HashWithIndifferentAccess
          
            
- TestCookies
          
            
- ActionCable::Connection::TestCookieJar
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/test_case.rb
  
  

## Overview

  
    

We don’t want to use the whole “encryption stack” for connection unit-tests, but we want to make sure that users test against the correct types of cookies (i.e. signed or encrypted or plain)

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**encrypted**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**signed**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from TestCookies

  

#[]=

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**encrypted**  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 48

def encrypted
  @encrypted ||= TestCookies.new
end
```

    
  

    
      
  
### 
  
    #**signed**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/action_cable/connection/test_case.rb', line 44

def signed
  @signed ||= TestCookies.new
end
```