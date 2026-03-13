# Class: WebsocketRails::Configuration
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::Configuration
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/configuration.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**allowed_origins**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**allowed_origins=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**broadcast_subscriber_events=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**broadcast_subscriber_events?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**daemonize=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**daemonize?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**keep_subscribers_when_private=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**keep_subscribers_when_private?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_internal_events=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_internal_events?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_level**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_level=**(level)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_path**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_path=**(path)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**logger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**logger=**(logger)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**redis_defaults**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**redis_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**redis_options=**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**route_block**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**route_block=**(routes)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**standalone**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**standalone=**(standalone)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**standalone_port**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**standalone_port=**(port)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**synchronize**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**synchronize=**(synchronize)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**thin_defaults**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**thin_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**thin_options=**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user_class**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user_class=**(klass)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user_identifier**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**user_identifier=**(identifier)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**allowed_origins**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 28

def allowed_origins
  # allows the value to be string or array
  [@allowed_origins].flatten.compact.uniq ||= []
end
```

    
  

    
      
  
### 
  
    #**allowed_origins=**(value)  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 33

def allowed_origins=(value)
  @allowed_origins = value
end
```

    
  

    
      
  
### 
  
    #**broadcast_subscriber_events=**(value)  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 41

def broadcast_subscriber_events=(value)
  @broadcast_subscriber_events = value
end
```

    
  

    
      
  
### 
  
    #**broadcast_subscriber_events?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 37

def broadcast_subscriber_events?
  @broadcast_subscriber_events ||= false
end
```

    
  

    
      
  
### 
  
    #**daemonize=**(value)  ⇒ Object 
  

  

  

  
    
      

```

97
98
99
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 97

def daemonize=(value)
  @daemonize = value
end
```

    
  

    
      
  
### 
  
    #**daemonize?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

93
94
95
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 93

def daemonize?
  @daemonize.nil? ? true : @daemonize
end
```

    
  

    
      
  
### 
  
    #**keep_subscribers_when_private=**(value)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 24

def keep_subscribers_when_private=(value)
  @keep_subscribers_when_private = value
end
```

    
  

    
      
  
### 
  
    #**keep_subscribers_when_private?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 20

def keep_subscribers_when_private?
  @keep_subscribers_when_private ||= false
end
```

    
  

    
      
  
### 
  
    #**log_internal_events=**(value)  ⇒ Object 
  

  

  

  
    
      

```

89
90
91
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 89

def log_internal_events=(value)
  @log_internal_events = value
end
```

    
  

    
      
  
### 
  
    #**log_internal_events?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

85
86
87
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 85

def log_internal_events?
  @log_internal_events ||= false
end
```

    
  

    
      
  
### 
  
    #**log_level**  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
56
57
58
59
60
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 53

def log_level
  @log_level ||= begin
    case Rails.env.to_sym
    when :production then :info
    when :development then :debug
    end
  end
end
```

    
  

    
      
  
### 
  
    #**log_level=**(level)  ⇒ Object 
  

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 62

def log_level=(level)
  @log_level = level
end
```

    
  

    
      
  
### 
  
    #**log_path**  ⇒ Object 
  

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 77

def log_path
  @log_path ||= "#{Rails.root}/log/websocket_rails.log"
end
```

    
  

    
      
  
### 
  
    #**log_path=**(path)  ⇒ Object 
  

  

  

  
    
      

```

81
82
83
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 81

def log_path=(path)
  @log_path = path
end
```

    
  

    
      
  
### 
  
    #**logger**  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
69
70
71
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 66

def logger
  @logger ||= begin
    logger = Logger.new(log_path)
    Logging.configure(logger)
  end
end
```

    
  

    
      
  
### 
  
    #**logger=**(logger)  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 73

def logger=(logger)
  @logger = logger
end
```

    
  

    
      
  
### 
  
    #**redis_defaults**  ⇒ Object 
  

  

  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 117

def redis_defaults
  {:host => '127.0.0.1', :port => 6379, :driver => :synchrony}
end
```

    
  

    
      
  
### 
  
    #**redis_options**  ⇒ Object 
  

  

  

  
    
      

```

109
110
111
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 109

def redis_options
  @redis_options ||= redis_defaults
end
```

    
  

    
      
  
### 
  
    #**redis_options=**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

113
114
115
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 113

def redis_options=(options = {})
  @redis_options = redis_defaults.merge(options)
end
```

    
  

    
      
  
### 
  
    #**route_block**  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 49

def route_block
  @event_routes
end
```

    
  

    
      
  
### 
  
    #**route_block=**(routes)  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 45

def route_block=(routes)
  @event_routes = routes
end
```

    
  

    
      
  
### 
  
    #**standalone**  ⇒ Object 
  

  

  

  
    
      

```

121
122
123
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 121

def standalone
  @standalone ||= false
end
```

    
  

    
      
  
### 
  
    #**standalone=**(standalone)  ⇒ Object 
  

  

  

  
    
      

```

125
126
127
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 125

def standalone=(standalone)
  @standalone = standalone
end
```

    
  

    
      
  
### 
  
    #**standalone_port**  ⇒ Object 
  

  

  

  
    
      

```

129
130
131
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 129

def standalone_port
  @standalone_port ||= '3001'
end
```

    
  

    
      
  
### 
  
    #**standalone_port=**(port)  ⇒ Object 
  

  

  

  
    
      

```

133
134
135
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 133

def standalone_port=(port)
  @standalone_port = port
end
```

    
  

    
      
  
### 
  
    #**synchronize**  ⇒ Object 
  

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 101

def synchronize
  @synchronize ||= false
end
```

    
  

    
      
  
### 
  
    #**synchronize=**(synchronize)  ⇒ Object 
  

  

  

  
    
      

```

105
106
107
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 105

def synchronize=(synchronize)
  @synchronize = synchronize
end
```

    
  

    
      
  
### 
  
    #**thin_defaults**  ⇒ Object 
  

  

  

  
    
      

```

145
146
147
148
149
150
151
152
153
154
155
156
157
158
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 145

def thin_defaults
  {
    :port => standalone_port,
    :pid => "#{Rails.root}/tmp/pids/websocket_rails.pid",
    :log => "#{Rails.root}/log/websocket_rails_server.log",
    :tag => 'websocket_rails',
    :rackup => "#{Rails.root}/config.ru",
    :threaded => false,
    :daemonize => daemonize?,
    :dirname => Rails.root,
    :max_persistent_conns => 1024,
    :max_conns => 1024
  }
end
```

    
  

    
      
  
### 
  
    #**thin_options**  ⇒ Object 
  

  

  

  
    
      

```

137
138
139
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 137

def thin_options
  @thin_options ||= thin_defaults
end
```

    
  

    
      
  
### 
  
    #**thin_options=**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

141
142
143
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 141

def thin_options=(options = {})
  @thin_options = thin_defaults.merge(options)
end
```

    
  

    
      
  
### 
  
    #**user_class**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 12

def user_class
  @user_class ||= User
end
```

    
  

    
      
  
### 
  
    #**user_class=**(klass)  ⇒ Object 
  

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 16

def user_class=(klass)
  @user_class = klass
end
```

    
  

    
      
  
### 
  
    #**user_identifier**  ⇒ Object 
  

  

  

  
    
      

```

4
5
6
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 4

def user_identifier
  @user_identifier ||= :id
end
```

    
  

    
      
  
### 
  
    #**user_identifier=**(identifier)  ⇒ Object 
  

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/websocket_rails/configuration.rb', line 8

def user_identifier=(identifier)
  @user_identifier = identifier
end
```