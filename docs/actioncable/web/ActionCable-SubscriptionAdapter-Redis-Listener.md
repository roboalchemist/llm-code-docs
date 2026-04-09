# Class: ActionCable::SubscriptionAdapter::Redis::Listener
  
  
  

  
  
    Inherits:
    
      SubscriberMap
      
        

          
- Object
          
            
- SubscriberMap
          
            
- ActionCable::SubscriptionAdapter::Redis::Listener
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/action_cable/subscription_adapter/redis.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** SubscribedClient
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_channel**(channel, on_success)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(adapter, config_options, event_loop)  ⇒ Listener 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Listener.

  

      
        
- 
  
    
      #**invoke_callback**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**listen**(conn)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_channel**(channel)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shutdown**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from SubscriberMap

  

#add_subscriber, #broadcast, #remove_subscriber

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(adapter, config_options, event_loop)  ⇒ Listener 
  

  

  

  
    

Returns a new instance of Listener.

  

  

  
    
      

```

68
69
70
71
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
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 68

def initialize(adapter, config_options, event_loop)
  super()

  @adapter = adapter
  @event_loop = event_loop

  @subscribe_callbacks = Hash.new { |h, k| h[k] = [] }
  @subscription_lock = Mutex.new

  @reconnect_attempt = 0
  # Use the same config as used by Redis conn
  @reconnect_attempts = config_options.fetch(:reconnect_attempts, 1)
  @reconnect_attempts = Array.new(@reconnect_attempts, 0) if @reconnect_attempts.is_a?(Integer)

  @subscribed_client = nil

  @when_connected = []

  @thread = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_channel**(channel, on_success)  ⇒ Object 
  

  

  

  
    
      

```

141
142
143
144
145
146
147
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 141

def add_channel(channel, on_success)
  @subscription_lock.synchronize do
    ensure_listener_running
    @subscribe_callbacks[channel] << on_success
    when_connected { @subscribed_client.subscribe(channel) }
  end
end
```

    
  

    
      
  
### 
  
    #**invoke_callback**  ⇒ Object 
  

  

  

  
    
      

```

155
156
157
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 155

def invoke_callback(*)
  @event_loop.post { super }
end
```

    
  

    
      
  
### 
  
    #**listen**(conn)  ⇒ Object 
  

  

  

  
    
      

```

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
113
114
115
116
117
118
119
120
121
122
123
124
125
126
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 89

def listen(conn)
  conn.without_reconnect do
    original_client = extract_subscribed_client(conn)

    conn.subscribe("_action_cable_internal") do |on|
      on.subscribe do |chan, count|
        @subscription_lock.synchronize do
          if count == 1
            @reconnect_attempt = 0
            @subscribed_client = original_client

            until @when_connected.empty?
              @when_connected.shift.call
            end
          end

          if callbacks = @subscribe_callbacks[chan]
            next_callback = callbacks.shift
            @event_loop.post(&next_callback) if next_callback
            @subscribe_callbacks.delete(chan) if callbacks.empty?
          end
        end
      end

      on.message do |chan, message|
        broadcast(chan, message)
      end

      on.unsubscribe do |chan, count|
        if count == 0
          @subscription_lock.synchronize do
            @subscribed_client = nil
          end
        end
      end
    end
  end
end
```

    
  

    
      
  
### 
  
    #**remove_channel**(channel)  ⇒ Object 
  

  

  

  
    
      

```

149
150
151
152
153
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 149

def remove_channel(channel)
  @subscription_lock.synchronize do
    when_connected { @subscribed_client.unsubscribe(channel) }
  end
end
```

    
  

    
      
  
### 
  
    #**shutdown**  ⇒ Object 
  

  

  

  
    
      

```

128
129
130
131
132
133
134
135
136
137
138
139
```

    
    
      

```
# File 'lib/action_cable/subscription_adapter/redis.rb', line 128

def shutdown
  @subscription_lock.synchronize do
    return if @thread.nil?

    when_connected do
      @subscribed_client.unsubscribe
      @subscribed_client = nil
    end
  end

  Thread.pass while @thread.alive?
end
```