# Class: WebsocketRails::ControllerFactory
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::ControllerFactory
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/controller_factory.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**controller_stores**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute controller_stores.

  

    
      
- 
  
    
      #**dispatcher**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute dispatcher.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(dispatcher)  ⇒ ControllerFactory 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ControllerFactory.

  

      
        
- 
  
    
      #**new_for_event**(event, controller_class, method)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

TODO: Add deprecation notice for user defined instance variables.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(dispatcher)  ⇒ ControllerFactory 
  

  

  

  
    

Returns a new instance of ControllerFactory.

  

  

  
    
      

```

6
7
8
9
10
```

    
    
      

```
# File 'lib/websocket_rails/controller_factory.rb', line 6

def initialize(dispatcher)
  @dispatcher = dispatcher
  @controller_stores = {}
  @initialized_controllers = {}
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**controller_stores**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute controller_stores.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/websocket_rails/controller_factory.rb', line 4

def controller_stores
  @controller_stores
end
```

    
  

    
      
      
      
  
### 
  
    #**dispatcher**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute dispatcher.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/websocket_rails/controller_factory.rb', line 4

def dispatcher
  @dispatcher
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**new_for_event**(event, controller_class, method)  ⇒ Object 
  

  

  

  
    

TODO: Add deprecation notice for user defined instance variables.

  

  

  
    
      

```

14
15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/websocket_rails/controller_factory.rb', line 14

def new_for_event(event, controller_class, method)
  controller_class = reload!(controller_class)
  controller = controller_class.new

  prepare(controller, event, method)

  controller
end
```