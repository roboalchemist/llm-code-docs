# Module: WebsocketRails::Logging
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Channel, ConnectionAdapters::Base, ConnectionManager, Dispatcher, Event, Event, EventMap::Namespace, InternalController, Synchronization
  
  

  
  
    Defined in:
    lib/websocket_rails/logging.rb
  
  

## Defined Under Namespace

  
    
      **Modules:** Format
    
  
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        LOGGABLE_DATA =
          
  
    

Logging module heavily influenced by Travis-Support library

  

  

        
        

```
[
  String,
  Hash,
  ActiveSupport::HashWithIndifferentAccess
]
```

      
        ANSI =
          
        
        

```
{
  :red    => 31,
  :green  => 32,
  :yellow => 33,
  :cyan   => 36
}
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**configure**(logger)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**log_level**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**color_for_level**(level)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**colorize**(color, text)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log**(level, message, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_data?**(event)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_event**(event, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_event?**(event)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_event_end**(event, time)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_event_start**(event)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_exception**(exception)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**log_header**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrap**(level, object, message, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**configure**(logger)  ⇒ Object 
  

  

  

  
    
      

```

24
25
26
27
28
29
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 24

def configure(logger)
  logger.tap do
    logger.formatter = proc { |*args| Format.format(*args) }
    logger.level = Logger.const_get(log_level.to_s.upcase)
  end
end
```

    
  

    
      
  
### 
  
    .**log_level**  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 31

def log_level
  WebsocketRails.config.log_level || :debug
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**color_for_level**(level)  ⇒ Object 
  

  

  

  
    
      

```

107
108
109
110
111
112
113
114
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 107

def color_for_level(level)
  case level
  when :info then :green
  when :debug then :yellow
  else
    :red
  end
end
```

    
  

    
      
  
### 
  
    #**colorize**(color, text)  ⇒ Object 
  

  

  

  
    
      

```

103
104
105
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 103

def colorize(color, text)
  "\e[#{ANSI[color]}m#{text}\e[0m"
end
```

    
  

    
      
  
### 
  
    #**log**(level, message, options = {})  ⇒ Object 
  

  

  

  
    
      

```

45
46
47
48
49
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 45

def log(level, message, options = {})
  message.chomp.split("\n").each do |line|
    logger.send(level, wrap(level, self, line, options || {}))
  end
end
```

    
  

    
      
  
### 
  
    #**log_data?**(event)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 82

def log_data?(event)
  LOGGABLE_DATA.include?(event.data.class)
end
```

    
  

    
      
  
### 
  
    #**log_event**(event, &block)  ⇒ Object 
  

  

  

  
    
      

```

63
64
65
66
67
68
69
70
71
72
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 63

def log_event(event, &block)
  log_event_start(event) if log_event?(event)
  start_time = Time.now
  block.call
  total_time = Time.now - start_time
  log_event_end(event, total_time) if log_event?(event)
rescue Exception => ex
  log_exception(ex)
  raise
end
```

    
  

    
      
  
### 
  
    #**log_event?**(event)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

74
75
76
77
78
79
80
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 74

def log_event?(event)
  if event.is_internal?
    WebsocketRails.config.log_internal_events?
  else
    true
  end
end
```

    
  

    
      
  
### 
  
    #**log_event_end**(event, time)  ⇒ Object 
  

  

  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 59

def log_event_end(event, time)
  info "Event #{event.encoded_name} Finished in #{time.to_f.to_d.to_s} seconds\n\n"
end
```

    
  

    
      
  
### 
  
    #**log_event_start**(event)  ⇒ Object 
  

  

  

  
    
      

```

51
52
53
54
55
56
57
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 51

def log_event_start(event)
  message = "Started Event: #{event.encoded_name}\n"
  message << "#{colorize(:cyan, "Name:")} #{event.encoded_name}\n"
  message << "#{colorize(:cyan, "Data:")} #{event.data.inspect}\n" if log_data?(event)
  message << "#{colorize(:cyan, "Connection:")} #{event.connection}\n\n"
  info message
end
```

    
  

    
      
  
### 
  
    #**log_exception**(exception)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 86

def log_exception(exception)
  logger.error(wrap(:error, self, "#{exception.class.name}: #{exception.message}"))
  exception.backtrace.each { |line| logger.error(wrap(:error, self, line)) } if exception.backtrace
  logger << "\n"
rescue Exception => ex
  puts '--- FATAL ---'
  puts 'an exception occured while logging an exception'
  puts ex.message, ex.backtrace
  puts exception.message, exception.backtrace
end
```

    
  

    
      
  
### 
  
    #**log_header**  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 116

def log_header
  self.class.name.split('::').last
end
```

    
  

    
      
  
### 
  
    #**wrap**(level, object, message, options = {})  ⇒ Object 
  

  

  

  
    
      

```

97
98
99
100
101
```

    
    
      

```
# File 'lib/websocket_rails/logging.rb', line 97

def wrap(level, object, message, options = {})
  header = options[:header] || object.log_header
  color = color_for_level(level)
  "[#{colorize(color, header)}] #{message.chomp}"
end
```