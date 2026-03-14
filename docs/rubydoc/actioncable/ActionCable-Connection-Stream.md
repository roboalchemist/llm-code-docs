# Class: ActionCable::Connection::Stream
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- ActionCable::Connection::Stream
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/connection/stream.rb
  
  

## Overview

  
    

– This class is heavily based on faye-websocket-ruby

Copyright © 2010-2015 James Coglan

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**close**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**each**(&callback)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**flush_write_buffer**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**hijack_rack_socket**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(event_loop, socket)  ⇒ Stream 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**receive**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shutdown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**write**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(event_loop, socket)  ⇒ Stream 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

12
13
14
15
16
17
18
19
20
21
22
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 12

def initialize(event_loop, socket)
  @event_loop    = event_loop
  @socket_object = socket
  @stream_send   = socket.env["stream.send"]

  @rack_hijack_io = nil
  @write_lock = Mutex.new

  @write_head = nil
  @write_buffer = Queue.new
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**close**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 28

def close
  shutdown
  @socket_object.client_gone
end
```

    
  

    
      
  
### 
  
    #**each**(&callback)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 24

def each(&callback)
  @stream_send ||= callback
end
```

    
  

    
      
  
### 
  
    #**flush_write_buffer**  ⇒ Object 
  

  

  

  
    
      

```

72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 72

def flush_write_buffer
  @write_lock.synchronize do
    loop do
      if @write_head.nil?
        return true if @write_buffer.empty?
        @write_head = @write_buffer.pop
      end

      written = @rack_hijack_io.write_nonblock(@write_head, exception: false)
      case written
      when :wait_writable
        return false
      when @write_head.bytesize
        @write_head = nil
      else
        @write_head = @write_head.byteslice(written, @write_head.bytesize)
        return false
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**hijack_rack_socket**  ⇒ Object 
  

  

  

  
    
      

```

98
99
100
101
102
103
104
105
106
107
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 98

def hijack_rack_socket
  return unless @socket_object.env["rack.hijack"]

  # This should return the underlying io according to the SPEC:
  @rack_hijack_io = @socket_object.env["rack.hijack"].call
  # Retain existing behavior if required:
  @rack_hijack_io ||= @socket_object.env["rack.hijack_io"]

  @event_loop.attach(@rack_hijack_io, self)
end
```

    
  

    
      
  
### 
  
    #**receive**(data)  ⇒ Object 
  

  

  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 94

def receive(data)
  @socket_object.parse(data)
end
```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 33

def shutdown
  clean_rack_hijack
end
```

    
  

    
      
  
### 
  
    #**write**(data)  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
```

    
    
      

```
# File 'lib/action_cable/connection/stream.rb', line 37

def write(data)
  if @stream_send
    return @stream_send.call(data)
  end

  if @write_lock.try_lock
    begin
      if @write_head.nil? && @write_buffer.empty?
        written = @rack_hijack_io.write_nonblock(data, exception: false)

        case written
        when :wait_writable
          # proceed below
        when data.bytesize
          return data.bytesize
        else
          @write_head = data.byteslice(written, data.bytesize)
          @event_loop.writes_pending @rack_hijack_io

          return data.bytesize
        end
      end
    ensure
      @write_lock.unlock
    end
  end

  @write_buffer << data
  @event_loop.writes_pending @rack_hijack_io

  data.bytesize
rescue EOFError, Errno::ECONNRESET
  @socket_object.client_gone
end
```