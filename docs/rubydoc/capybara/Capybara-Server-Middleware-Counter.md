# Class: Capybara::Server::Middleware::Counter
  
  
  Private

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Server::Middleware::Counter
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/server/middleware.rb
  
  

  
    

  **This class is part of a private API.**
  You should avoid using this class if possible, as it may be removed or be changed in the future.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**decrement**(uri)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**increment**(uri)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ Counter 
    

    
  
  
  
    constructor
  
  
  
  
  
  private

  
    

A new instance of Counter.

  

      
        
- 
  
    
      #**positive?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ Counter 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Counter.

  

  

  
    
      

```

7
8
9
10
```

    
    
      

```
# File 'lib/capybara/server/middleware.rb', line 7

def initialize
  @value = []
  @mutex = Mutex.new
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**decrement**(uri)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/capybara/server/middleware.rb', line 16

def decrement(uri)
  @mutex.synchronize { @value.delete_at(@value.index(uri) || - 1) }
end
```

    
  

    
      
  
### 
  
    #**increment**(uri)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/capybara/server/middleware.rb', line 12

def increment(uri)
  @mutex.synchronize { @value.push(uri) }
end
```

    
  

    
      
  
### 
  
    #**positive?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/capybara/server/middleware.rb', line 20

def positive?
  @mutex.synchronize { @value.length.positive? }
end
```

    
  

    
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/capybara/server/middleware.rb', line 24

def value
  @mutex.synchronize { @value.dup }
end
```