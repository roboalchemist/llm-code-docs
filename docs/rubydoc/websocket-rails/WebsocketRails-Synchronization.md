# Class: WebsocketRails::Synchronization
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::Synchronization
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/synchronization.rb
  
  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**all_users**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**destroy_user**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**find_user**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**publish**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**register_user**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**shutdown!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**singleton**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**synchronize!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**all_users**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**destroy_user**(identifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**find_user**(identifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**generate_server_token**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**publish**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**register_server**(token)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**register_user**(connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remove_server**(token)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ruby_redis**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**server_token**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shutdown!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**synchronize!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_incoming**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
    
## Class Method Details

    
      
  
### 
  
    .**all_users**  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 8

def self.all_users
  singleton.all_users
end
```

    
  

    
      
  
### 
  
    .**destroy_user**(connection)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 20

def self.destroy_user(connection)
  singleton.destroy_user connection
end
```

    
  

    
      
  
### 
  
    .**find_user**(connection)  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 12

def self.find_user(connection)
  singleton.find_user connection
end
```

    
  

    
      
  
### 
  
    .**publish**(event)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 24

def self.publish(event)
  singleton.publish event
end
```

    
  

    
      
  
### 
  
    .**redis**  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 36

def self.redis
  singleton.redis
end
```

    
  

    
      
  
### 
  
    .**register_user**(connection)  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 16

def self.register_user(connection)
  singleton.register_user connection
end
```

    
  

    
      
  
### 
  
    .**shutdown!**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 32

def self.shutdown!
  singleton.shutdown!
end
```

    
  

    
      
  
### 
  
    .**singleton**  ⇒ Object 
  

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 40

def self.singleton
  @singleton ||= new
end
```

    
  

    
      
  
### 
  
    .**synchronize!**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 28

def self.synchronize!
  singleton.synchronize!
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**all_users**  ⇒ Object 
  

  

  

  
    
      

```

171
172
173
174
175
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 171

def all_users
  Fiber.new do
    redis.hgetall('websocket_rails.users')
  end.resume
end
```

    
  

    
      
  
### 
  
    #**destroy_user**(identifier)  ⇒ Object 
  

  

  

  
    
      

```

158
159
160
161
162
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 158

def destroy_user(identifier)
  Fiber.new do
    redis.hdel 'websocket_rails.users', identifier
  end.resume
end
```

    
  

    
      
  
### 
  
    #**find_user**(identifier)  ⇒ Object 
  

  

  

  
    
      

```

164
165
166
167
168
169
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 164

def find_user(identifier)
  Fiber.new do
    raw_user = redis.hget('websocket_rails.users', identifier)
    raw_user ? JSON.parse(raw_user) : nil
  end.resume
end
```

    
  

    
      
  
### 
  
    #**generate_server_token**  ⇒ Object 
  

  

  

  
    
      

```

129
130
131
132
133
134
135
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 129

def generate_server_token
  begin
    token = SecureRandom.urlsafe_base64
  end while redis.sismember("websocket_rails.active_servers", token)

  token
end
```

    
  

    
      
  
### 
  
    #**publish**(event)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 60

def publish(event)
  Fiber.new do
    event.server_token = server_token
    redis.publish "websocket_rails.events", event.serialize
  end.resume
end
```

    
  

    
      
  
### 
  
    #**redis**  ⇒ Object 
  

  

  

  
    
      

```

46
47
48
49
50
51
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 46

def redis
  @redis ||= begin
    redis_options = WebsocketRails.config.redis_options
    EM.reactor_running? ? Redis.new(redis_options) : ruby_redis
  end
end
```

    
  

    
      
  
### 
  
    #**register_server**(token)  ⇒ Object 
  

  

  

  
    
      

```

137
138
139
140
141
142
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 137

def register_server(token)
  Fiber.new do
    redis.sadd "websocket_rails.active_servers", token
    info "Server Registered: #{token}"
  end.resume
end
```

    
  

    
      
  
### 
  
    #**register_user**(connection)  ⇒ Object 
  

  

  

  
    
      

```

150
151
152
153
154
155
156
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 150

def register_user(connection)
  Fiber.new do
    id = connection.user_identifier
    user = connection.user
    redis.hset 'websocket_rails.users', id, user.as_json(root: false).to_json
  end.resume
end
```

    
  

    
      
  
### 
  
    #**remove_server**(token)  ⇒ Object 
  

  

  

  
    
      

```

144
145
146
147
148
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 144

def remove_server(token)
  ruby_redis.srem "websocket_rails.active_servers", token
  info "Server Removed: #{token}"
  EM.stop
end
```

    
  

    
      
  
### 
  
    #**ruby_redis**  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
56
57
58
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 53

def ruby_redis
  @ruby_redis ||= begin
    redis_options = WebsocketRails.config.redis_options.merge(:driver => :ruby)
    Redis.new(redis_options)
  end
end
```

    
  

    
      
  
### 
  
    #**server_token**  ⇒ Object 
  

  

  

  
    
      

```

67
68
69
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 67

def server_token
  @server_token
end
```

    
  

    
      
  
### 
  
    #**shutdown!**  ⇒ Object 
  

  

  

  
    
      

```

125
126
127
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 125

def shutdown!
  remove_server(server_token)
end
```

    
  

    
      
  
### 
  
    #**synchronize!**  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/websocket_rails/synchronization.rb', line 71

def synchronize!
  unless @synchronizing
    @server_token = generate_server_token
    register_server(@server_token)

    synchro = Fiber.new do
      fiber_redis = Redis.connect(WebsocketRails.config.redis_options)
      fiber_redis.subscribe "websocket_rails.events" do |on|

        on.message do |_, encoded_event|
          event = Event.new_from_json(encoded_event, nil)

          # Do nothing if this is the server that sent this event.
          next if event.server_token == server_token

          # Ensure an event never gets triggered twice. Events added to the
          # redis queue from other processes may not have a server token
          # attached.
          event.server_token = server_token if event.server_token.nil?

          trigger_incoming event
        end
      end

      info "Beginning Synchronization"
    end

    @synchronizing = true

    EM.next_tick { synchro.resume }

    trap('TERM') do
      Thread.new { shutdown! }
    end
    trap('INT') do
      Thread.new { shutdown! }
    end
    trap('QUIT') do
      Thread.new { shutdown! }
    end
  end
end
```

    
  

    
      
  
### 
  
    #**trigger_incoming**(event)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/websocket_rails/synchronization.rb', line 114

def trigger_incoming(event)
  case
  when event.is_channel?
    WebsocketRails[event.channel].trigger_event(event)
  when event.is_user?
    connection = WebsocketRails.users[event.user_id.to_s]
    return if connection.nil?
    connection.trigger event
  end
end
```