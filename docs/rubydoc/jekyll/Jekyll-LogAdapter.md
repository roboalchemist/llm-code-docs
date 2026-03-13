# Class: Jekyll::LogAdapter
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::LogAdapter

        show all
      

    Defined in:
    lib/jekyll/log_adapter.rb
  
##

      Constant Summary
      collapse
    

    
      
        LOG_LEVELS =
          
        
        

```
{
  :debug => ::Logger::DEBUG,
  :info  => ::Logger::INFO,
  :warn  => ::Logger::WARN,
  :error => ::Logger::ERROR,
}.freeze

```

## Instance Attribute Summary collapse

-
  
      #**level**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute level.

-
  
      #**messages**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute messages.

-
  
      #**writer**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute writer.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**abort_with**(topic, message = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Public: Print an error message and immediately abort the process.

-
  
      #**adjust_verbosity**(options = {})  ⇒ Object 

-
  
      #**debug**(topic, message = nil, &block)  ⇒ Object 

Public: Print a debug message.

-
  
      #**error**(topic, message = nil, &block)  ⇒ Object 

Public: Print an error message.

-
  
      #**formatted_topic**(topic, colon = false)  ⇒ Object 

Internal: Format the topic.

-
  
      #**info**(topic, message = nil, &block)  ⇒ Object 

Public: Print a message.

-
  
      #**initialize**(writer, level = :info)  ⇒ LogAdapter 

    constructor
  
  
  
  
  
  

  
    

Public: Create a new instance of a log writer.

-
  
      #**log_level=**(level)  ⇒ Object 

Public: Set the log level on the writer.

-
  
      #**message**(topic, message = nil)  ⇒ Object 

Internal: Build a topic method.

-
  
      #**warn**(topic, message = nil, &block)  ⇒ Object 

Public: Print a message.

-
  
      #**write**(level_of_message, topic, message = nil, &block)  ⇒ Object 

Internal: Log a message.

-
  
      #**write_message?**(level_of_message)  ⇒ Boolean 

Internal: Check if the message should be written given the log level.

## Constructor Details

###
  
    #**initialize**(writer, level = :info)  ⇒ LogAdapter 
  

  

  

  
    

Public: Create a new instance of a log writer

writer - Logger compatible instance log_level - (optional, symbol) the log level

Returns nothing

```

20
21
22
23
24
```

```
# File 'lib/jekyll/log_adapter.rb', line 20

def initialize(writer, level = :info)
  @messages = []
  @writer = writer
  self.log_level = level
end

```

## Instance Attribute Details

###
  
    #**level**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute level.

```

5
6
7
```

```
# File 'lib/jekyll/log_adapter.rb', line 5

def level
  @level
end

```

###
  
    #**messages**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute messages.

```

5
6
7
```

```
# File 'lib/jekyll/log_adapter.rb', line 5

def messages
  @messages
end

```

###
  
    #**writer**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute writer.

```

5
6
7
```

```
# File 'lib/jekyll/log_adapter.rb', line 5

def writer
  @writer
end

```

## Instance Method Details

###
  
    #**abort_with**(topic, message = nil, &block)  ⇒ Object 
  

  

  

  
    

Public: Print an error message and immediately abort the process

topic - the topic of the message, e.g. “Configuration file”, “Deprecation”, etc. message - the message detail (can be omitted)

Returns nothing

```

95
96
97
98
```

```
# File 'lib/jekyll/log_adapter.rb', line 95

def abort_with(topic, message = nil, &block)
  error(topic, message, &block)
  abort
end

```

###
  
    #**adjust_verbosity**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/jekyll/log_adapter.rb', line 38

def adjust_verbosity(options = {})
  # Quiet always wins.
  if options[:quiet]
    self.log_level = :error
  elsif options[:verbose]
    self.log_level = :debug
  end
  debug "Logging at level:", LOG_LEVELS.key(writer.level).to_s
  debug "Jekyll Version:", Jekyll::VERSION
end

```

###
  
    #**debug**(topic, message = nil, &block)  ⇒ Object 
  

  

  

  
    

Public: Print a debug message

topic - the topic of the message, e.g. “Configuration file”, “Deprecation”, etc. message - the message detail

Returns nothing

```

55
56
57
```

```
# File 'lib/jekyll/log_adapter.rb', line 55

def debug(topic, message = nil, &block)
  write(:debug, topic, message, &block)
end

```

###
  
    #**error**(topic, message = nil, &block)  ⇒ Object 
  

  

  

  
    

Public: Print an error message

topic - the topic of the message, e.g. “Configuration file”, “Deprecation”, etc. message - the message detail

Returns nothing

```

85
86
87
```

```
# File 'lib/jekyll/log_adapter.rb', line 85

def error(topic, message = nil, &block)
  write(:error, topic, message, &block)
end

```

###
  
    #**formatted_topic**(topic, colon = false)  ⇒ Object 
  

  

  

  
    

Internal: Format the topic

topic - the topic of the message, e.g. “Configuration file”, “Deprecation”, etc. colon -

Returns the formatted topic statement

```

123
124
125
```

```
# File 'lib/jekyll/log_adapter.rb', line 123

def formatted_topic(topic, colon = false)
  "#{topic}#{colon ? ": " : " "}".rjust(20)
end

```

###
  
    #**info**(topic, message = nil, &block)  ⇒ Object 
  

  

  

  
    

Public: Print a message

topic - the topic of the message, e.g. “Configuration file”, “Deprecation”, etc. message - the message detail

Returns nothing

```

65
66
67
```

```
# File 'lib/jekyll/log_adapter.rb', line 65

def info(topic, message = nil, &block)
  write(:info, topic, message, &block)
end

```

###
  
    #**log_level=**(level)  ⇒ Object 
  

  

  

  
    

Public: Set the log level on the writer

level - (symbol) the log level

Returns nothing

```

31
32
33
34
35
36
```

```
# File 'lib/jekyll/log_adapter.rb', line 31

def log_level=(level)
  writer.level = level if level.is_a?(Integer) && level.between?(0, 3)
  writer.level = LOG_LEVELS[level] ||
    raise(ArgumentError, "unknown log level")
  @level = level
end

```

###
  
    #**message**(topic, message = nil)  ⇒ Object 
  

  

  

  
    

Internal: Build a topic method

topic - the topic of the message, e.g. “Configuration file”, “Deprecation”, etc. message - the message detail

Returns the formatted message

Raises:

-

        (ArgumentError)

```

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
```

```
# File 'lib/jekyll/log_adapter.rb', line 106

def message(topic, message = nil)
  raise ArgumentError, "block or message, not both" if block_given? && message

  message = yield if block_given?
  message = message.to_s.gsub(%r!\s+!, " ")
  topic = formatted_topic(topic, block_given?)
  out = topic + message
  messages << out
  out
end

```

###
  
    #**warn**(topic, message = nil, &block)  ⇒ Object 
  

  

  

  
    

Public: Print a message

topic - the topic of the message, e.g. “Configuration file”, “Deprecation”, etc. message - the message detail

Returns nothing

```

75
76
77
```

```
# File 'lib/jekyll/log_adapter.rb', line 75

def warn(topic, message = nil, &block)
  write(:warn, topic, message, &block)
end

```

###
  
    #**write**(level_of_message, topic, message = nil, &block)  ⇒ Object 
  

  

  

  
    

Internal: Log a message.

level_of_message - the Symbol level of message, one of :debug, :info, :warn, :error topic - the String topic or full message message - the String message (optional) block - a block containing the message (optional)

Returns false if the message was not written, otherwise returns the value of calling the appropriate writer method, e.g. writer.info.

```

145
146
147
148
149
```

```
# File 'lib/jekyll/log_adapter.rb', line 145

def write(level_of_message, topic, message = nil, &block)
  return false unless write_message?(level_of_message)

  writer.public_send(level_of_message, message(topic, message, &block))
end

```

###
  
    #**write_message?**(level_of_message)  ⇒ Boolean 
  

  

  

  
    

Internal: Check if the message should be written given the log level.

level_of_message - the Symbol level of message, one of :debug, :info, :warn, :error

Returns whether the message should be written.

Returns:

-

        (Boolean)

```

132
133
134
```

```
# File 'lib/jekyll/log_adapter.rb', line 132

def write_message?(level_of_message)
  LOG_LEVELS.fetch(level) <= LOG_LEVELS.fetch(level_of_message)
end

```
