# Class: EventMachine::WebSocket::Connection
  
  
  

  
  
    Inherits:
    
      Connection
      
        

          
- Object
          
            
- Connection
          
            
- EventMachine::WebSocket::Connection
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Debugger
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/connection.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ENCODING_SUPPORTED =
          
  
    

Cache encodings since it’s moderately expensive to look them up each time

  

  

        
        

```
"string".respond_to?(:force_encoding)
```

      
        UTF8 =
          
        
        

```
Encoding.find("UTF-8")
```

      
        BINARY =
          
        
        

```
Encoding.find("BINARY")
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**max_frame_size**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the maximum frame size which this connection is configured to accept.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**close**(code = nil, body = nil)  ⇒ Object 
    

    
      (also: #close_websocket)
    
  
  
  
  
  
  
  
  

  
    

Use this method to close the websocket connection cleanly This sends a close frame and waits for acknowlegement before closing the connection.

  

      
        
- 
  
    
      #**close_timeout**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**dispatch**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(options)  ⇒ Connection 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Connection.

  

      
        
- 
  
    
      #**onbinary**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**onclose**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**onerror**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**onmessage**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**onopen**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

define WebSocket callbacks.

  

      
        
- 
  
    
      #**onping**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**onpong**(&blk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ping**(body = '')  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Send a ping to the client.

  

      
        
- 
  
    
      #**pingable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Test whether the connection is pingable (i.e. the WebSocket draft in use is >= 01).

  

      
        
- 
  
    
      #**pong**(body = '')  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Send an unsolicited pong message, as allowed by the protocol.

  

      
        
- 
  
    
      #**post_init**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**receive_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**remote_ip**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the IP address for the remote peer.

  

      
        
- 
  
    
      #**send_binary**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Send a WebSocket binary frame.

  

      
        
- 
  
    
      #**send_data**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_flash_cross_domain_file**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_healthcheck_response**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_text**(data)  ⇒ Object 
    

    
      (also: #send)
    
  
  
  
  
  
  
  
  

  
    

Send a WebSocket text frame.

  

      
        
- 
  
    
      #**state**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**supports_close_codes?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_on_binary**(msg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_on_close**(event = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_on_error**(reason)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_on_message**(msg)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_on_open**(handshake)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_on_ping**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**trigger_on_pong**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**unbind**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options)  ⇒ Connection 
  

  

  

  
    

Returns a new instance of Connection.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 41

def initialize(options)
  @options = options
  @debug = options[:debug] || false
  @secure = options[:secure] || false
  @secure_proxy = options[:secure_proxy] || false
  @tls_options = options[:tls_options] || {}
  @close_timeout = options[:close_timeout]
  @outbound_limit = options[:outbound_limit] || 0

  @handler = nil

  debug [:initialize]
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**max_frame_size**  ⇒ Object 
  

  

  

  
    

Returns the maximum frame size which this connection is configured to accept. This can be set globally or on a per connection basis, and defaults to a value of 10MB if not set.

The behaviour when a too large frame is received varies by protocol, but in the newest protocols the connection will be closed with the correct close code (1009) immediately after receiving the frame header

  

  

  
    
      

```

282
283
284
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 282

def max_frame_size
  defined?(@max_frame_size) ? @max_frame_size : WebSocket.max_frame_size
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**close**(code = nil, body = nil)  ⇒ Object 
  

  
    Also known as:
    close_websocket
    
  

  

  
    

Use this method to close the websocket connection cleanly This sends a close frame and waits for acknowlegement before closing the connection

  

  

  
    
      

```

58
59
60
61
62
63
64
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 58

def close(code = nil, body = nil)
  if code && !acceptable_close_code?(code)
    raise "Application code may only use codes from 1000, 3000-4999"
  end

  close_websocket_private(code, body)
end
```

    
  

    
      
  
### 
  
    #**close_timeout**  ⇒ Object 
  

  

  

  
    
      

```

286
287
288
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 286

def close_timeout
  @close_timeout || WebSocket.close_timeout
end
```

    
  

    
      
  
### 
  
    #**dispatch**(data)  ⇒ Object 
  

  

  

  
    
      

```

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
123
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
139
140
141
142
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 112

def dispatch(data)
  if data.match(%r|^GET /healthcheck|)
    send_healthcheck_response
  elsif data.match(/\A<policy-file-request\s*\/>/)
    send_flash_cross_domain_file
  else
    @handshake ||= begin
      handshake = Handshake.new(@secure || @secure_proxy)

      handshake.callback { |upgrade_response, handler_klass|
        debug [:accepting_ws_version, handshake.protocol_version]
        debug [:upgrade_response, upgrade_response]
        self.send_data(upgrade_response)
        @handler = handler_klass.new(self, @debug)
        @handshake = nil
        trigger_on_open(handshake)
      }

      handshake.errback { |e|
        debug [:error, e]
        trigger_on_error(e)
        # Handshake errors require the connection to be aborted
        abort(:handshake_error)
      }

      handshake
    end

    @handshake.receive_data(data)
  end
end
```

    
  

    
      
  
### 
  
    #**onbinary**(&blk)  ⇒ Object 
  

  

  

  
    
      

```

13
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 13

def onbinary(&blk);   @onbinary = blk; end
```

    
  

    
      
  
### 
  
    #**onclose**(&blk)  ⇒ Object 
  

  

  

  
    
      

```

10
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 10

def onclose(&blk);    @onclose = blk;   end
```

    
  

    
      
  
### 
  
    #**onerror**(&blk)  ⇒ Object 
  

  

  

  
    
      

```

11
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 11

def onerror(&blk);    @onerror = blk;   end
```

    
  

    
      
  
### 
  
    #**onmessage**(&blk)  ⇒ Object 
  

  

  

  
    
      

```

12
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 12

def onmessage(&blk);  @onmessage = blk; end
```

    
  

    
      
  
### 
  
    #**onopen**(&blk)  ⇒ Object 
  

  

  

  
    

define WebSocket callbacks

  

  

  
    
      

```

9
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 9

def onopen(&blk);     @onopen = blk;    end
```

    
  

    
      
  
### 
  
    #**onping**(&blk)  ⇒ Object 
  

  

  

  
    
      

```

14
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 14

def onping(&blk);     @onping = blk;    end
```

    
  

    
      
  
### 
  
    #**onpong**(&blk)  ⇒ Object 
  

  

  

  
    
      

```

15
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 15

def onpong(&blk);     @onpong = blk;    end
```

    
  

    
      
  
### 
  
    #**ping**(body = '')  ⇒ Object 
  

  

  

  
    

Send a ping to the client. The client must respond with a pong.

In the case that the client is running a WebSocket draft < 01, false is returned since ping & pong are not supported

  

  

  
    
      

```

225
226
227
228
229
230
231
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 225

def ping(body = '')
  if @handler
    @handler.pingable? ? @handler.send_frame(:ping, body) && true : false
  else
    raise WebSocketError, "Cannot ping before onopen callback"
  end
end
```

    
  

    
      
  
### 
  
    #**pingable?**  ⇒ Boolean 
  

  

  

  
    

Test whether the connection is pingable (i.e. the WebSocket draft in use is >= 01)

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

249
250
251
252
253
254
255
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 249

def pingable?
  if @handler
    @handler.pingable?
  else
    raise WebSocketError, "Cannot test whether pingable before onopen callback"
  end
end
```

    
  

    
      
  
### 
  
    #**pong**(body = '')  ⇒ Object 
  

  

  

  
    

Send an unsolicited pong message, as allowed by the protocol. The client is not expected to respond to this message.

em-websocket automatically takes care of sending pong replies to incoming ping messages, as the protocol demands.

  

  

  
    
      

```

239
240
241
242
243
244
245
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 239

def pong(body = '')
  if @handler
    @handler.pingable? ? @handler.send_frame(:pong, body) && true : false
  else
    raise WebSocketError, "Cannot ping before onopen callback"
  end
end
```

    
  

    
      
  
### 
  
    #**post_init**  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 69

def post_init
  start_tls(@tls_options) if @secure
end
```

    
  

    
      
  
### 
  
    #**receive_data**(data)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 73

def receive_data(data)
  debug [:receive_data, data]

  if @handler
    @handler.receive_data(data)
  else
    dispatch(data)
  end
rescue => e
  debug [:error, e]

  # There is no code defined for application errors, so use 3000
  # (which is reserved for frameworks)
  close_websocket_private(3000, "Application error")

  # These are application errors - raise unless onerror defined
  trigger_on_error(e) || raise(e)
end
```

    
  

    
      
  
### 
  
    #**remote_ip**  ⇒ Object 
  

  

  

  
    

Returns the IP address for the remote peer

  

  

  
    
      

```

270
271
272
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 270

def remote_ip
  get_peername[2,6].unpack('nC4')[1..4].join('.')
end
```

    
  

    
      
  
### 
  
    #**send_binary**(data)  ⇒ Object 
  

  

  

  
    

Send a WebSocket binary frame.

  

  

  
    
      

```

212
213
214
215
216
217
218
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 212

def send_binary(data)
  if @handler
    @handler.send_frame(:binary, data)
  else
    raise WebSocketError, "Cannot send binary before onopen callback"
  end
end
```

    
  

    
      
  
### 
  
    #**send_data**(data)  ⇒ Object 
  

  

  

  
    
      

```

92
93
94
95
96
97
98
99
100
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 92

def send_data(data)
  if @outbound_limit > 0 &&
      get_outbound_data_size + data.bytesize > @outbound_limit
    abort(:outbound_limit_reached)
    return 0
  end

  super(data)
end
```

    
  

    
      
  
### 
  
    #**send_flash_cross_domain_file**  ⇒ Object 
  

  

  

  
    
      

```

161
162
163
164
165
166
167
168
169
170
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 161

def send_flash_cross_domain_file
  file =  '<?xml version="1.0"?><cross-domain-policy><allow-access-from domain="*" to-ports="*"/></cross-domain-policy>'
  debug [:cross_domain, file]
  send_data file

  # handle the cross-domain request transparently
  # no need to notify the user about this connection
  @onclose = nil
  close_connection_after_writing
end
```

    
  

    
      
  
### 
  
    #**send_healthcheck_response**  ⇒ Object 
  

  

  

  
    
      

```

144
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
159
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 144

def send_healthcheck_response
  debug [:healthcheck, 'OK']

  healthcheck_res = ["HTTP/1.1 200 OK"]
  healthcheck_res << "Content-Type: text/plain"
  healthcheck_res << "Content-Length: 2"

  healthcheck_res = healthcheck_res.join("\r\n") + "\r\n\r\nOK"

  send_data healthcheck_res

  # handle the healthcheck request transparently
  # no need to notify the user about this connection
  @onclose = nil
  close_connection_after_writing
end
```

    
  

    
      
  
### 
  
    #**send_text**(data)  ⇒ Object 
  

  
    Also known as:
    send
    
  

  

  
    

Send a WebSocket text frame.

A WebSocketError may be raised if the connection is in an opening or a closing state, or if the passed in data is not valid UTF-8

  

  

  
    
      

```

182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 182

def send_text(data)
  # If we're using Ruby 1.9, be pedantic about encodings
  if ENCODING_SUPPORTED
    # Also accept ascii only data in other encodings for convenience
    unless (data.encoding == UTF8 && data.valid_encoding?) || data.ascii_only?
      raise WebSocketError, "Data sent to WebSocket must be valid UTF-8 but was #{data.encoding} (valid: #{data.valid_encoding?})"
    end
    # This labels the encoding as binary so that it can be combined with
    # the BINARY framing
    data.force_encoding(BINARY)
  else
    # TODO: Check that data is valid UTF-8
  end

  if @handler
    @handler.send_text_frame(data)
  else
    raise WebSocketError, "Cannot send data before onopen callback"
  end

  # Revert data back to the original encoding (which we assume is UTF-8)
  # Doing this to avoid duping the string - there may be a better way
  data.force_encoding(UTF8) if ENCODING_SUPPORTED
  return nil
end
```

    
  

    
      
  
### 
  
    #**state**  ⇒ Object 
  

  

  

  
    
      

```

265
266
267
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 265

def state
  @handler ? @handler.state : :handshake
end
```

    
  

    
      
  
### 
  
    #**supports_close_codes?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

257
258
259
260
261
262
263
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 257

def supports_close_codes?
  if @handler
    @handler.supports_close_codes?
  else
    raise WebSocketError, "Cannot test before onopen callback"
  end
end
```

    
  

    
      
  
### 
  
    #**trigger_on_binary**(msg)  ⇒ Object 
  

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 20

def trigger_on_binary(msg)
  @onbinary.call(msg) if defined? @onbinary
end
```

    
  

    
      
  
### 
  
    #**trigger_on_close**(event = {})  ⇒ Object 
  

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 26

def trigger_on_close(event = {})
  @onclose.call(event) if defined? @onclose
end
```

    
  

    
      
  
### 
  
    #**trigger_on_error**(reason)  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
38
39
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 35

def trigger_on_error(reason)
  return false unless defined? @onerror
  @onerror.call(reason)
  true
end
```

    
  

    
      
  
### 
  
    #**trigger_on_message**(msg)  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 17

def trigger_on_message(msg)
  @onmessage.call(msg) if defined? @onmessage
end
```

    
  

    
      
  
### 
  
    #**trigger_on_open**(handshake)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 23

def trigger_on_open(handshake)
  @onopen.call(handshake) if defined? @onopen
end
```

    
  

    
      
  
### 
  
    #**trigger_on_ping**(data)  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 29

def trigger_on_ping(data)
  @onping.call(data) if defined? @onping
end
```

    
  

    
      
  
### 
  
    #**trigger_on_pong**(data)  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 32

def trigger_on_pong(data)
  @onpong.call(data) if defined? @onpong
end
```

    
  

    
      
  
### 
  
    #**unbind**  ⇒ Object 
  

  

  

  
    
      

```

102
103
104
105
106
107
108
109
110
```

    
    
      

```
# File 'lib/em-websocket/connection.rb', line 102

def unbind
  debug [:unbind, :connection]

  @handler.unbind if @handler
rescue => e
  debug [:error, e]
  # These are application errors - raise unless onerror defined
  trigger_on_error(e) || raise(e)
end
```