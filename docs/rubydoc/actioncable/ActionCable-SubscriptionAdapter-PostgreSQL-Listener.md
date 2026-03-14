# Class: ActionCable::SubscriptionAdapter::PostgreSQL::Listener
  
  
  

  
  
    Inherits:
    
      SubscriberMap
      
        

          
- Object
          
            
- SubscriberMap
          
            
- ActionCable::SubscriptionAdapter::PostgreSQL::Listener
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/postgresql.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_channel**(channel, on_success)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(adapter, event_loop)  ⇒ Listener 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Listener.

  

      
        
- 
  
    
      #**invoke_callback**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**listen**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_channel**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shutdown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from SubscriberMap

  

#add_subscriber, #broadcast, #remove_subscriber

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(adapter, event_loop)  ⇒ Listener 
  

  

  

  
    

Returns a new instance of Listener.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 75

def initialize(adapter, event_loop)
  super()

  @adapter = adapter
  @event_loop = event_loop
  @queue = Queue.new

  @thread = Thread.new do
    Thread.current.abort_on_exception = true
    listen
  end
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_channel**(channel, on_success)  ⇒ Object 
  

  

  

  
    
      

```

119
120
121
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 119

def add_channel(channel, on_success)
  @queue.push([:listen, channel, on_success])
end
```

    
  

    
      
  
### 
  
    #**invoke_callback**  ⇒ Object 
  

  

  

  
    
      

```

127
128
129
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 127

def invoke_callback(*)
  @event_loop.post { super }
end
```

    
  

    
      
  
### 
  
    #**listen**  ⇒ Object 
  

  

  

  
    
      

```

88
89
90
91
92
93
94
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
105
106
107
108
109
110
111
112
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 88

def listen
  @adapter.with_subscriptions_connection do |pg_conn|
    catch :shutdown do
      loop do
        until @queue.empty?
          action, channel, callback = @queue.pop(true)

          case action
          when :listen
            pg_conn.exec("LISTEN #{pg_conn.escape_identifier channel}")
            @event_loop.post(&callback) if callback
          when :unlisten
            pg_conn.exec("UNLISTEN #{pg_conn.escape_identifier channel}")
          when :shutdown
            throw :shutdown
          end
        end

        pg_conn.wait_for_notify(1) do |chan, pid, message|
          broadcast(chan, message)
        end
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**remove_channel**(channel)  ⇒ Object 
  

  

  

  
    
      

```

123
124
125
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 123

def remove_channel(channel)
  @queue.push([:unlisten, channel])
end
```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    
      

```

114
115
116
117
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/postgresql.rb', line 114

def shutdown
  @queue.push([:shutdown])
  Thread.pass while @thread.alive?
end
```