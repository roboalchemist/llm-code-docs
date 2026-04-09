# Class: WebsocketRails::UserManager::MissingConnection
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::UserManager::MissingConnection
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/user_manager.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**identifier**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute identifier.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**connected?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(identifier)  ⇒ MissingConnection 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of MissingConnection.

  

      
        
- 
  
    
      #**nil?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_message**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(identifier)  ⇒ MissingConnection 
  

  

  

  
    

Returns a new instance of MissingConnection.

  

  

  
    
      

```

253
254
255
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 253

def initialize(identifier)
  @user_identifier = identifier.to_s
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**identifier**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute identifier.

  

  

  
    
      

```

251
252
253
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 251

def identifier
  @identifier
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**connected?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

257
258
259
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 257

def connected?
  false
end
```

    
  

    
      
  
### 
  
    #**nil?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

269
270
271
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 269

def nil?
  true
end
```

    
  

    
      
  
### 
  
    #**send_message**(*args)  ⇒ Object 
  

  

  

  
    
      

```

265
266
267
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 265

def send_message(*args)
  false
end
```

    
  

    
      
  
### 
  
    #**user**  ⇒ Object 
  

  

  

  
    
      

```

261
262
263
```

    
    
      

```
# File 'lib/websocket_rails/user_manager.rb', line 261

def user
  nil
end
```