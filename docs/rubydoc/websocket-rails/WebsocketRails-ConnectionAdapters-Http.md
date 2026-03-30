# Class: WebsocketRails::ConnectionAdapters::Http
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- WebsocketRails::ConnectionAdapters::Http
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/websocket_rails/connection_adapters/http.rb
  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** DeferrableBody
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        TERM =
          
        
        

```
"\r\n".freeze
```

      
        TAIL =
          
        
        

```
"0#{TERM}#{TERM}".freeze
```

      
        HttpHeaders =
          
        
        

```
{
  'Content-Type'      => 'text/json',
  'Transfer-Encoding' => 'chunked'
}
```

      
    
  

  
  
  
### Constants included
     from Logging

  

Logging::ANSI, Logging::LOGGABLE_DATA

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**headers**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute headers.

  

    
  

  
  
  
### Attributes inherited from Base

  

#data_store, #dispatcher, #env, #id, #pong, #queue, #request

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**accepts?**(env)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**close!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(env, dispatcher)  ⇒ Http 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Http.

  

      
        
- 
  
    
      #**send**(message)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#connected?, #controller_delegate, #enqueue, #flush, inherited, #inspect, #on_close, #on_error, #on_message, #on_open, #rack_response, #send_message, #to_s, #trigger, #user, #user_connection?, #user_identifier

  
  
  
  
  
  
  
  
  
### Methods included from Logging

  

#color_for_level, #colorize, configure, #log, #log_data?, #log_event, #log_event?, #log_event_end, #log_event_start, #log_exception, #log_header, log_level, #wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(env, dispatcher)  ⇒ Http 
  

  

  

  
    

Returns a new instance of Http.

  

  

  
    
      

```

17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 17

def initialize(env,dispatcher)
  super
  @body = DeferrableBody.new
  @headers = HttpHeaders

  define_deferrable_callbacks

  origin = "#{request.protocol}#{request.raw_host_with_port}"
  @headers.merge!({'Access-Control-Allow-Origin' => origin}) if WebsocketRails.config.allowed_origins.include?(origin)
  # IE < 10.0 hack
  # XDomainRequest will not bubble up notifications of download progress in the first 2kb of the response
  # http://blogs.msdn.com/b/ieinternals/archive/2010/04/06/comet-streaming-in-internet-explorer-with-xmlhttprequest-and-xdomainrequest.aspx
  @body.chunk(encode_chunk(" " * 2048))

  EM.next_tick do
    @env['async.callback'].call [200, @headers, @body]
    on_open
  end
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**headers**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute headers.

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 15

def headers
  @headers
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**accepts?**(env)  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 11

def self.accepts?(env)
  true
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**close!**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 41

def close!
  @body.close!
end
```

    
  

    
      
  
### 
  
    #**send**(message)  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/websocket_rails/connection_adapters/http.rb', line 37

def send(message)
  @body.chunk encode_chunk( message )
end
```