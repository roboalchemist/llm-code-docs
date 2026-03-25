# Class: WebsocketRails::EventQueue
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::EventQueue
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/event_queue.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**queue**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute queue.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**enqueue**(event)  ⇒ Object 
    

    
      (also: #<<)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**flush**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ EventQueue 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EventQueue.

  

      
        
- 
  
    
      #**last**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ EventQueue 
  

  

  

  
    

Returns a new instance of EventQueue.

  

  

  
    
      

```

6
7
8
```

    
    
      

```
# File 'lib/websocket_rails/event_queue.rb', line 6

def initialize
  @queue = []
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**queue**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute queue.

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/websocket_rails/event_queue.rb', line 4

def queue
  @queue
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**enqueue**(event)  ⇒ Object 
  

  
    Also known as:
    <<
    
  

  

  
    
      

```

10
11
12
```

    
    
      

```
# File 'lib/websocket_rails/event_queue.rb', line 10

def enqueue(event)
  @queue << event
end
```

    
  

    
      
  
### 
  
    #**flush**(&block)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
29
30
```

    
    
      

```
# File 'lib/websocket_rails/event_queue.rb', line 23

def flush(&block)
  unless block.nil?
    @queue.each do |item|
      block.call item
    end
  end
  @queue = []
end
```

    
  

    
      
  
### 
  
    #**last**  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/websocket_rails/event_queue.rb', line 15

def last
  @queue.last
end
```

    
  

    
      
  
### 
  
    #**size**  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/websocket_rails/event_queue.rb', line 19

def size
  @queue.size
end
```