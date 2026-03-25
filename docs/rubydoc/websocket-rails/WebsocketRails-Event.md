# Class: WebsocketRails::Event
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- WebsocketRails::Event
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      Logging, StaticEvents
  
  
  
  
  
      Includes:
      Logging
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/event.rb
  
  

## Overview

  
    

Contains all of the relevant information for incoming and outgoing events. All events except for channel events will have a connection object associated.

Events require an event name and hash of options:

:data => The data object will be passed to any callback functions bound on the client side.

You can also pass a Hash of options to specify:

:connection => Connection that will be receiving or that sent this event.

:namespace => The namespace this event is under. Will default to :global If the namespace is nested under multiple levels pass them as an array. For instance, if the namespace route looks like the following:

```
namespace :products do
  namespace :hats do
    # events
  end
end

```

Then you would pass the namespace argument as [:products,:hats]

:channel => The name of the channel that this event is destined for.

  

  

  
## Direct Known Subclasses

  

SpecHelperEvent

## Defined Under Namespace

  
    
  
    
      **Classes:** UnknownDataType
    
  

  
## Constant Summary

  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**channel**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute channel.

  

    
      
- 
  
    
      #**connection**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute connection.

  

    
      
- 
  
    
      #**data**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute data.

  

    
      
- 
  
    
      #**id**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute id.

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
      
- 
  
    
      #**namespace**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute namespace.

  

    
      
- 
  
    
      #**result**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute result.

  

    
      
- 
  
    
      #**server_token**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute server_token.

  

    
      
- 
  
    
      #**success**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute success.

  

    
      
- 
  
    
      #**token**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute token.

  

    
      
- 
  
    
      #**user_id**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute user_id.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**log_header**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**new_from_json**(encoded_data, connection)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**as_json**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**encoded_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(event_name, options = {})  ⇒ Event 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Event.

  

      
        
- 
  
    
      #**is_channel?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**is_internal?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**is_invalid?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**is_user?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**serialize**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

color_for_level, colorize, configure, log, log_data?, log_event, log_event?, log_event_end, log_event_start, log_exception, log_header, log_level, wrap

  
  
  
  
  
  
  
  
  
### Methods included from StaticEvents

  

new_on_close, new_on_error, new_on_invalid_event_received, new_on_open, new_on_ping

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(event_name, options = {})  ⇒ Event 
  

  

  

  
    

Returns a new instance of Event.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 105

def initialize(event_name, options={})
  case event_name
  when String
    namespace   = event_name.split('.')
    @name       = namespace.pop.to_sym
  when Symbol
    @name       = event_name
    namespace   = [:global]
  end
  @id           = options[:id]
  @data         = options[:data].is_a?(Hash) ? options[:data].with_indifferent_access : options[:data]
  @channel      = options[:channel].to_sym rescue options[:channel].to_s.to_sym if options[:channel]
  @token        = options[:token] if options[:token]
  @connection   = options[:connection]
  @server_token = options[:server_token]
  @user_id      = options[:user_id]
  @namespace    = validate_namespace( options[:namespace] || namespace )
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**channel**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute channel.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 101

def channel
  @channel
end
```

    
  

    
      
      
      
  
### 
  
    #**connection**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute connection.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 101

def connection
  @connection
end
```

    
  

    
      
      
      
  
### 
  
    #**data**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute data.

  

  

  
    
      

```

103
104
105
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 103

def data
  @data
end
```

    
  

    
      
      
      
  
### 
  
    #**id**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute id.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 101

def id
  @id
end
```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 101

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**namespace**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute namespace.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 101

def namespace
  @namespace
end
```

    
  

    
      
      
      
  
### 
  
    #**result**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute result.

  

  

  
    
      

```

103
104
105
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 103

def result
  @result
end
```

    
  

    
      
      
      
  
### 
  
    #**server_token**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute server_token.

  

  

  
    
      

```

103
104
105
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 103

def server_token
  @server_token
end
```

    
  

    
      
      
      
  
### 
  
    #**success**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute success.

  

  

  
    
      

```

103
104
105
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 103

def success
  @success
end
```

    
  

    
      
      
      
  
### 
  
    #**token**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute token.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 101

def token
  @token
end
```

    
  

    
      
      
      
  
### 
  
    #**user_id**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute user_id.

  

  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 101

def user_id
  @user_id
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**log_header**  ⇒ Object 
  

  

  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 66

def self.log_header
  "Event"
end
```

    
  

    
      
  
### 
  
    .**new_from_json**(encoded_data, connection)  ⇒ Object 
  

  

  

  
    
      

```

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
88
89
90
91
92
93
94
95
96
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 70

def self.new_from_json(encoded_data, connection)
  case encoded_data
  when String
    event_name, data = JSON.parse encoded_data

    unless event_name.is_a?(String) && data.is_a?(Hash)
      raise UnknownDataType
    end

    data = data.merge(:connection => connection).with_indifferent_access
    Event.new event_name, data
    # when Array
    # TODO: Handle file
    #File.open("/tmp/test#{rand(100)}.jpg", "wb") do |file|
    #  encoded_data.each do |byte|
    #    file << byte.chr
    #  end
    #end
  else
    raise UnknownDataType
  end
rescue JSON::ParserError, UnknownDataType => ex
  warn "Invalid Event Received: #{ex}"
  debug "Event Data: #{encoded_data}"
  log_exception(ex)
  Event.new_on_invalid_event_received(connection, nil)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**as_json**  ⇒ Object 
  

  

  

  
    
      

```

124
125
126
127
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
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 124

def as_json
  [
    encoded_name,
    {
      :id => id,
      :channel => channel,
      :user_id => user_id,
      :data => data,
      :success => success,
      :result => result,
      :token => token,
      :server_token => server_token
    }
  ]
end
```

    
  

    
      
  
### 
  
    #**encoded_name**  ⇒ Object 
  

  

  

  
    
      

```

164
165
166
167
168
169
170
171
172
173
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 164

def encoded_name
  if namespace.size > 1
    child_namespace = namespace.dup[1..-1]
    child_namespace << name
    combined_name = child_namespace.join('.')
  else
    combined_name = name
  end
  combined_name
end
```

    
  

    
      
  
### 
  
    #**is_channel?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

144
145
146
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 144

def is_channel?
  !@channel.nil?
end
```

    
  

    
      
  
### 
  
    #**is_internal?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

156
157
158
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 156

def is_internal?
  namespace.include?(:websocket_rails)
end
```

    
  

    
      
  
### 
  
    #**is_invalid?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

152
153
154
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 152

def is_invalid?
  name == :invalid_event
end
```

    
  

    
      
  
### 
  
    #**is_user?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

148
149
150
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 148

def is_user?
  !@user_id.nil? && !is_channel?
end
```

    
  

    
      
  
### 
  
    #**serialize**  ⇒ Object 
  

  

  

  
    
      

```

140
141
142
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 140

def serialize
  as_json.to_json
end
```

    
  

    
      
  
### 
  
    #**trigger**  ⇒ Object 
  

  

  

  
    
      

```

160
161
162
```

    
    
      

```
# File 'lib/websocket_rails/event.rb', line 160

def trigger
  connection.trigger self if connection
end
```