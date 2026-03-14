# Module: EventMachine::WebSocket::MessageProcessor03
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Handler03, Handler05
  
  

  
  
    Defined in:
    lib/em-websocket/message_processor_03.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**message**(message_type, extension_data, application_data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**pingable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Ping & Pong supported.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**message**(message_type, extension_data, application_data)  ⇒ Object 
  

  

  

  
    
      

```

6
7
8
9
10
11
12
13
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
# File 'lib/em-websocket/message_processor_03.rb', line 6

def message(message_type, extension_data, application_data)
  case message_type
  when :close
    @close_info = {
      :code => 1005,
      :reason => "",
      :was_clean => true,
    }
    if @state == :closing
      # TODO: Check that message body matches sent data
      # We can close connection immediately since there is no more data
      # is allowed to be sent or received on this connection
      @connection.close_connection
    else
      # Acknowlege close
      # The connection is considered closed
      send_frame(:close, application_data)
      @connection.close_connection_after_writing
    end
  when :ping
    # Pong back the same data
    send_frame(:pong, application_data)
    @connection.trigger_on_ping(application_data)
  when :pong
    @connection.trigger_on_pong(application_data)
  when :text
    if application_data.respond_to?(:force_encoding)
      application_data.force_encoding("UTF-8")
    end
    @connection.trigger_on_message(application_data)
  when :binary
    @connection.trigger_on_binary(application_data)
  end
end
```

    
  

    
      
  
### 
  
    #**pingable?**  ⇒ Boolean 
  

  

  

  
    

Ping & Pong supported

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/em-websocket/message_processor_03.rb', line 42

def pingable?
  true
end
```