# Class: WebsocketRails::ConnectionAdapters::Http::DeferrableBody
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::ConnectionAdapters::Http::DeferrableBody
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      EM::Deferrable
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/connection_adapters/http.rb
  
  

## Overview

  
    

From [thin_async](github.com/macournoyer/thin_async)

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**chunk**(*chunks)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Enqueue a chunk of content to be flushed to stream at a later time.

  

      
        
- 
  
    
      #**close!**(flush = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**each**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

When rack attempts to iterate over `body`, save the block, and execute at a later time when ‘@queue` has elements.

  

      
        
- 
  
    
      #**empty?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(chunks = [])  ⇒ DeferrableBody 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of DeferrableBody.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(chunks = [])  ⇒ DeferrableBody 
  

  

  

  
    

Returns a new instance of DeferrableBody.

  

  

Parameters:

  
    
- 
      
        chunks
      
      
        
      
      
        *(defaults to: [])*
      
      
        —
        

  - 

object that responds to each. holds initial chunks of content

      
    
  

  
    
      

```

73
74
75
76
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 73

def initialize(chunks = [])
  @queue = []
  chunks.each {|c| chunk(c)}
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**chunk**(*chunks)  ⇒ Object 
  

  

  

  
    

Enqueue a chunk of content to be flushed to stream at a later time

  

  

  
    
      

```

79
80
81
82
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 79

def chunk(*chunks)
  @queue += chunks
  schedule_dequeue
end
```

    
  

    
      
  
### 
  
    #**close!**(flush = true)  ⇒ Object 
  

  

  

  
    
      

```

95
96
97
98
99
100
101
102
103
104
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 95

def close!(flush = true)
  EM.next_tick {
    if !flush || empty?
      succeed
    else
      schedule_dequeue
      close!(flush)
    end
  }
end
```

    
  

    
      
  
### 
  
    #**each**(&blk)  ⇒ Object 
  

  

  

  
    

When rack attempts to iterate over `body`, save the block, and execute at a later time when ‘@queue` has elements

  

  

  
    
      

```

86
87
88
89
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 86

def each(&blk)
  @body_callback = blk
  schedule_dequeue
end
```

    
  

    
      
  
### 
  
    #**empty?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

91
92
93
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 91

def empty?
  @queue.empty?
end
```