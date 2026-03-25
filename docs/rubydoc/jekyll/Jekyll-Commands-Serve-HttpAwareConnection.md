# Class: Jekyll::Commands::Serve::HttpAwareConnection
  
    Inherits:
    
      EventMachine::WebSocket::Connection
      
        

          
- Object

- EventMachine::WebSocket::Connection

- Jekyll::Commands::Serve::HttpAwareConnection

        show all
      

    Defined in:
    lib/jekyll/commands/serve/websockets.rb
  
## Overview

The LiveReload protocol requires the server to serve livereload.js over HTTP despite the fact that the protocol itself uses WebSockets.  This custom connection class addresses the dual protocols that the server needs to understand.

## Instance Attribute Summary collapse

-
  
      #**reload_body**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute reload_body.

-
  
      #**reload_size**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute reload_size.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**dispatch**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

rubocop:disable Metrics/MethodLength.

-
  
      #**initialize**(_opts)  ⇒ HttpAwareConnection 

    constructor
  
  
  
  
  
  

  
    

A new instance of HttpAwareConnection.

## Constructor Details

###
  
    #**initialize**(_opts)  ⇒ HttpAwareConnection 
  

  

  

  
    

Returns a new instance of HttpAwareConnection.

```

14
15
16
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
36
37
38
39
```

```
# File 'lib/jekyll/commands/serve/websockets.rb', line 14

def initialize(_opts)
  # If EventMachine SSL support on Windows ever gets better, the code below will
  # set up the reactor to handle SSL
  #
  # @ssl_enabled = opts["ssl_cert"] && opts["ssl_key"]
  # if @ssl_enabled
  #   em_opts[:tls_options] = {
  #   :private_key_file => Jekyll.sanitized_path(opts["source"], opts["ssl_key"]),
  #   :cert_chain_file  => Jekyll.sanitized_path(opts["source"], opts["ssl_cert"])
  #   }
  #   em_opts[:secure] = true
  # end

  # This is too noisy even for --verbose, but uncomment if you need it for
  # a specific WebSockets issue.  Adding ?LR-verbose=true onto the URL will
  # enable logging on the client side.
  # em_opts[:debug] = true

  em_opts = {}
  super(em_opts)

  reload_file = File.join(Serve.singleton_class::LIVERELOAD_DIR, "livereload.js")

  @reload_body = File.read(reload_file)
  @reload_size = @reload_body.bytesize
end
```

## Instance Attribute Details

###
  
    #**reload_body**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute reload_body.

```

12
13
14
```

```
# File 'lib/jekyll/commands/serve/websockets.rb', line 12

def reload_body
  @reload_body
end
```

###
  
    #**reload_size**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute reload_size.

```

12
13
14
```

```
# File 'lib/jekyll/commands/serve/websockets.rb', line 12

def reload_size
  @reload_size
end
```

## Instance Method Details

###
  
    #**dispatch**(data)  ⇒ Object 
  

  

  

  
    

rubocop:disable Metrics/MethodLength

```

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
71
72
73
74
75
76
```

```
# File 'lib/jekyll/commands/serve/websockets.rb', line 42

def dispatch(data)
  parser = Http::Parser.new
  parser << data

  # WebSockets requests will have a Connection: Upgrade header
  if parser.http_method != "GET" || parser.upgrade?
    super
  elsif parser.request_url.start_with?("/livereload.js")
    headers = [
      "HTTP/1.1 200 OK",
      "Content-Type: application/javascript",
      "Content-Length: #{reload_size}",
      "",
      "",
    ].join("\r\n")
    send_data(headers)

    # stream_file_data would free us from keeping livereload.js in memory
    # but JRuby blocks on that call and never returns
    send_data(reload_body)
    close_connection_after_writing
  else
    body = "This port only serves livereload.js over HTTP.\n"
    headers = [
      "HTTP/1.1 400 Bad Request",
      "Content-Type: text/plain",
      "Content-Length: #{body.bytesize}",
      "",
      "",
    ].join("\r\n")
    send_data(headers)
    send_data(body)
    close_connection_after_writing
  end
end
```
