# Class: ActionCable::Connection::StreamEventLoop
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::StreamEventLoop
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/stream_event_loop.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**attach**(io, stream)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**detach**(io, stream)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**  ⇒ StreamEventLoop 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of StreamEventLoop.

  

      
        
- 
  
    
      #**post**(task = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**stop**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**timer**(interval, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**writes_pending**(io)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**  ⇒ StreamEventLoop 
  

  

  

  
    

Returns a new instance of StreamEventLoop.

  

  

  
    
      

```

10
11
12
13
14
15
16
17
```

    
    
      

```
# File 'lib/action_cable/connection/stream_event_loop.rb', line 10

def initialize
  @nio = @executor = @thread = nil
  @map = {}
  @stopping = false
  @todo = Queue.new

  @spawn_mutex = Mutex.new
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**attach**(io, stream)  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
33
34
35
36
```

    
    
      

```
# File 'lib/action_cable/connection/stream_event_loop.rb', line 30

def attach(io, stream)
  @todo << lambda do
    @map[io] = @nio.register(io, :r)
    @map[io].value = stream
  end
  wakeup
end
```

    
  

    
      
  
### 
  
    #**detach**(io, stream)  ⇒ Object 
  

  

  

  
    
      

```

38
39
40
41
42
43
44
45
```

    
    
      

```
# File 'lib/action_cable/connection/stream_event_loop.rb', line 38

def detach(io, stream)
  @todo << lambda do
    @nio.deregister io
    @map.delete io
    io.close
  end
  wakeup
end
```

    
  

    
      
  
### 
  
    #**post**(task = nil, &block)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
```

    
    
      

```
# File 'lib/action_cable/connection/stream_event_loop.rb', line 23

def post(task = nil, &block)
  task ||= block

  spawn
  @executor << task
end
```

    
  

    
      
  
### 
  
    #**stop**  ⇒ Object 
  

  

  

  
    
      

```

56
57
58
59
```

    
    
      

```
# File 'lib/action_cable/connection/stream_event_loop.rb', line 56

def stop
  @stopping = true
  wakeup if @nio
end
```

    
  

    
      
  
### 
  
    #**timer**(interval, &block)  ⇒ Object 
  

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/action_cable/connection/stream_event_loop.rb', line 19

def timer(interval, &block)
  Concurrent::TimerTask.new(execution_interval: interval, &block).tap(&:execute)
end
```

    
  

    
      
  
### 
  
    #**writes_pending**(io)  ⇒ Object 
  

  

  

  
    
      

```

47
48
49
50
51
52
53
54
```

    
    
      

```
# File 'lib/action_cable/connection/stream_event_loop.rb', line 47

def writes_pending(io)
  @todo << lambda do
    if monitor = @map[io]
      monitor.interests = :rw
    end
  end
  wakeup
end
```