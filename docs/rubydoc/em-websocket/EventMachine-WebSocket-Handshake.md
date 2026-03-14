# Class: EventMachine::WebSocket::Handshake
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- EventMachine::WebSocket::Handshake
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      EM::Deferrable
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/handshake.rb
  
  

## Overview

  
    

Resposible for creating the server handshake response

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**parser**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute parser.

  

    
      
- 
  
    
      #**protocol_version**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute protocol_version.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**headers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the WebSocket upgrade headers as a hash.

  

      
        
- 
  
    
      #**headers_downcased**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The same as headers, except that the hash keys are downcased.

  

      
        
- 
  
    
      #**initialize**(secure)  ⇒ Handshake 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Unfortunately drafts 75 & 76 require knowledge of whether the connection is being terminated as ws/wss in order to generate the correct handshake response.

  

      
        
- 
  
    
      #**origin**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the WebSocket origin header if provided.

  

      
        
- 
  
    
      #**path**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the request path (excluding any query params).

  

      
        
- 
  
    
      #**query**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**query_string**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the query params as a string foo=bar&baz=…

  

      
        
- 
  
    
      #**receive_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**secure?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(secure)  ⇒ Handshake 
  

  

  

  
    

Unfortunately drafts 75 & 76 require knowledge of whether the connection is being terminated as ws/wss in order to generate the correct handshake response

  

  

  
    
      

```

16
17
18
19
20
21
22
23
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 16

def initialize(secure)
  @parser = Http::Parser.new
  @secure = secure

  @parser.on_headers_complete = proc { |headers|
    @headers = Hash[headers.map { |k,v| [k.downcase, v] }]
  }
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**parser**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute parser.

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 11

def parser
  @parser
end
```

    
  

    
      
      
      
  
### 
  
    #**protocol_version**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute protocol_version.

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 11

def protocol_version
  @protocol_version
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**headers**  ⇒ Object 
  

  

  

  
    

Returns the WebSocket upgrade headers as a hash.

Keys are strings, unmodified from the request.

  

  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 39

def headers
  @parser.headers
end
```

    
  

    
      
  
### 
  
    #**headers_downcased**  ⇒ Object 
  

  

  

  
    

The same as headers, except that the hash keys are downcased

  

  

  
    
      

```

45
46
47
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 45

def headers_downcased
  @headers
end
```

    
  

    
      
  
### 
  
    #**origin**  ⇒ Object 
  

  

  

  
    

Returns the WebSocket origin header if provided

  

  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 66

def origin
  @headers["origin"] || @headers["sec-websocket-origin"] || nil
end
```

    
  

    
      
  
### 
  
    #**path**  ⇒ Object 
  

  

  

  
    

Returns the request path (excluding any query params)

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 51

def path
  @path
end
```

    
  

    
      
  
### 
  
    #**query**  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 60

def query
  Hash[query_string.split('&').map { |c| c.split('=', 2) }]
end
```

    
  

    
      
  
### 
  
    #**query_string**  ⇒ Object 
  

  

  

  
    

Returns the query params as a string foo=bar&baz=…

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 56

def query_string
  @query_string
end
```

    
  

    
      
  
### 
  
    #**receive_data**(data)  ⇒ Object 
  

  

  

  
    
      

```

25
26
27
28
29
30
31
32
33
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 25

def receive_data(data)
  @parser << data

  if defined? @headers
    process(@headers, @parser.upgrade_data)
  end
rescue HTTP::Parser::Error => e
  fail(HandshakeError.new("Invalid HTTP header: #{e.message}"))
end
```

    
  

    
      
  
### 
  
    #**secure?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

70
71
72
```

    
    
      

```
# File 'lib/em-websocket/handshake.rb', line 70

def secure?
  @secure
end
```