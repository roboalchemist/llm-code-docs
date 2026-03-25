# Class: Capybara::Server::Checker
  
  
  Private

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Server::Checker
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/server/checker.rb
  
  

  
    

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        TRY_HTTPS_ERRORS =
          
  
    

  **This constant is part of a private API.**
  You should avoid using this constant if possible, as it may be removed or be changed in the future.

  

  

        
        

```
[EOFError, Net::ReadTimeout, Errno::ECONNRESET].freeze
```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(host, port)  ⇒ Checker 
    

    
  
  
  
    constructor
  
  
  
  
  
  private

  
    

A new instance of Checker.

  

      
        
- 
  
    
      #**request**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**ssl?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(host, port)  ⇒ Checker 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Checker.

  

  

  
    
      

```

8
9
10
11
```

    
    
      

```
# File 'lib/capybara/server/checker.rb', line 8

def initialize(host, port)
  @host, @port = host, port
  @ssl = false
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**request**(&block)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

13
14
15
16
17
18
19
```

    
    
      

```
# File 'lib/capybara/server/checker.rb', line 13

def request(&block)
  ssl? ? https_request(&block) : http_request(&block)
rescue *TRY_HTTPS_ERRORS
  res = https_request(&block)
  @ssl = true
  res
end
```

    
  

    
      
  
### 
  
    #**ssl?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/capybara/server/checker.rb', line 21

def ssl?
  @ssl
end
```