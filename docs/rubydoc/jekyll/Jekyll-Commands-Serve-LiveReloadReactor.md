# Class: Jekyll::Commands::Serve::LiveReloadReactor
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Commands::Serve::LiveReloadReactor

        show all
      

    Defined in:
    lib/jekyll/commands/serve/live_reload_reactor.rb
  
## Instance Attribute Summary collapse

-
  
      #**started_event**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute started_event.

-
  
      #**stopped_event**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute stopped_event.

-
  
      #**thread**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute thread.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**handle_websockets_event**(websocket)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**  ⇒ LiveReloadReactor 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of LiveReloadReactor.

-
  
      #**reload**(pages)  ⇒ Object 

For a description of the protocol see feedback.livereload.com/knowledgebase/articles/86174-livereload-protocol.

-
  
      #**running?**  ⇒ Boolean 

-
  
      #**start**(opts)  ⇒ Object 

-
  
      #**stop**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**  ⇒ LiveReloadReactor 
  

  

  

  
    

Returns a new instance of LiveReloadReactor.

```

13
14
15
16
17
18
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 13

def initialize
  @websockets = []
  @connections_count = 0
  @started_event = Utils::ThreadEvent.new
  @stopped_event = Utils::ThreadEvent.new
end
```

## Instance Attribute Details

###
  
    #**started_event**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute started_event.

```

11
12
13
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 11

def started_event
  @started_event
end
```

###
  
    #**stopped_event**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute stopped_event.

```

11
12
13
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 11

def stopped_event
  @stopped_event
end
```

###
  
    #**thread**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute thread.

```

11
12
13
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 11

def thread
  @thread
end
```

## Instance Method Details

###
  
    #**handle_websockets_event**(websocket)  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
36
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 31

def handle_websockets_event(websocket)
  websocket.onopen { |handshake| connect(websocket, handshake) }
  websocket.onclose { disconnect(websocket) }
  websocket.onmessage { |msg| print_message(msg) }
  websocket.onerror { |error| log_error(error) }
end
```

###
  
    #**reload**(pages)  ⇒ Object 
  

  

  

  
    

For a description of the protocol see feedback.livereload.com/knowledgebase/articles/86174-livereload-protocol

```

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
77
78
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 67

def reload(pages)
  pages.each do |p|
    json_message = JSON.dump(
      :command => "reload",
      :path    => p.url,
      :liveCSS => true
    )

    Jekyll.logger.debug "LiveReload:", "Reloading URL #{p.url.inspect}"
    @websockets.each { |ws| ws.send(json_message) }
  end
end
```

###
  
    #**running?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

27
28
29
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 27

def running?
  EM.reactor_running?
end
```

###
  
    #**start**(opts)  ⇒ Object 
  

  

  

  
    
      

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
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 38

def start(opts)
  @thread = Thread.new do
    # Use epoll if the kernel supports it
    EM.epoll
    EM.run do
      EM.error_handler { |e| log_error(e) }

      EM.start_server(
        opts["host"],
        opts["livereload_port"],
        HttpAwareConnection,
        opts
      ) do |ws|
        handle_websockets_event(ws)
      end

      # Notify blocked threads that EventMachine has started or shutdown
      EM.schedule { @started_event.set }
      EM.add_shutdown_hook { @stopped_event.set }

      Jekyll.logger.info "LiveReload address:",
                         "http://#{opts["host"]}:#{opts["livereload_port"]}"
    end
  end
  @thread.abort_on_exception = true
end
```

###
  
    #**stop**  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
23
24
25
```

```
# File 'lib/jekyll/commands/serve/live_reload_reactor.rb', line 20

def stop
  # There is only one EventMachine instance per Ruby process so stopping
  # it here will stop the reactor thread we have running.
  EM.stop if EM.reactor_running?
  Jekyll.logger.debug "LiveReload Server:", "halted"
end
```
