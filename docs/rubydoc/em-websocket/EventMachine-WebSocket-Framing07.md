# Module: EventMachine::WebSocket::Framing07
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Handler07, Handler08, Handler13
  
  

  
  
    Defined in:
    lib/em-websocket/framing07.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize_framing**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**process_data**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_frame**(frame_type, application_data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**send_text_frame**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**initialize_framing**  ⇒ Object 
  

  

  

  
    
      

```

7
8
9
10
11
```

    
    
      

```
# File 'lib/em-websocket/framing07.rb', line 7

def initialize_framing
  @data = MaskedString.new
  @application_data_buffer = '' # Used for MORE frames
  @frame_type = nil
end
```

    
  

    
      
  
### 
  
    #**process_data**  ⇒ Object 
  

  

  

  
    
      

```

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
97
98
99
100
101
102
103
104
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
# File 'lib/em-websocket/framing07.rb', line 13

def process_data
  error = false

  while !error && @data.size >= 2
    pointer = 0

    fin = (@data.getbyte(pointer) & 0b10000000) == 0b10000000
    # Ignoring rsv1-3 for now
    opcode = @data.getbyte(pointer) & 0b00001111
    pointer += 1

    mask = (@data.getbyte(pointer) & 0b10000000) == 0b10000000
    length = @data.getbyte(pointer) & 0b01111111
    pointer += 1

    # raise WebSocketError, 'Data from client must be masked' unless mask

    payload_length = case length
    when 127 # Length defined by 8 bytes
      # Check buffer size
      if @data.getbyte(pointer+8-1) == nil
        debug [:buffer_incomplete, @data]
        error = true
        next
      end
      
      # Only using the last 4 bytes for now, till I work out how to
      # unpack 8 bytes. I'm sure 4GB frames will do for now :)
      l = @data.getbytes(pointer+4, 4).unpack('N').first
      pointer += 8
      l
    when 126 # Length defined by 2 bytes
      # Check buffer size
      if @data.getbyte(pointer+2-1) == nil
        debug [:buffer_incomplete, @data]
        error = true
        next
      end
      
      l = @data.getbytes(pointer, 2).unpack('n').first
      pointer += 2
      l
    else
      length
    end

    # Compute the expected frame length
    frame_length = pointer + payload_length
    frame_length += 4 if mask

    if frame_length > @connection.max_frame_size
      raise WSMessageTooBigError, "Frame length too long (#{frame_length} bytes)"
    end

    # Check buffer size
    if @data.getbyte(frame_length - 1) == nil
      debug [:buffer_incomplete, @data]
      error = true
      next
    end

    # Remove frame header
    @data.slice!(0...pointer)
    pointer = 0

    # Read application data (unmasked if required)
    @data.read_mask if mask
    pointer += 4 if mask
    application_data = @data.getbytes(pointer, payload_length)
    pointer += payload_length
    @data.unset_mask if mask
    
    # Throw away data up to pointer
    @data.slice!(0...pointer)

    frame_type = opcode_to_type(opcode)

    if frame_type == :continuation
      if !@frame_type
        raise WSProtocolError, 'Continuation frame not expected'
      end
    else # Not a continuation frame
      if @frame_type && data_frame?(frame_type)
        raise WSProtocolError, "Continuation frame expected"
      end
    end

    # Validate that control frames are not fragmented
    if !fin && !data_frame?(frame_type)
      raise WSProtocolError, 'Control frames must not be fragmented'
    end

    if !fin
      debug [:moreframe, frame_type, application_data]
      @application_data_buffer << application_data
      # The message type is passed in the first frame
      @frame_type ||= frame_type
    else
      # Message is complete
      if frame_type == :continuation
        @application_data_buffer << application_data
        message(@frame_type, '', @application_data_buffer)
        @application_data_buffer = ''
        @frame_type = nil
      else
        message(frame_type, '', application_data)
      end
    end
  end # end while
end
```

    
  

    
      
  
### 
  
    #**send_frame**(frame_type, application_data)  ⇒ Object 
  

  

  

  
    
      

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
139
140
141
142
143
144
145
146
147
148
149
150
151
152
```

    
    
      

```
# File 'lib/em-websocket/framing07.rb', line 124

def send_frame(frame_type, application_data)
  debug [:sending_frame, frame_type, application_data]

  if @state == :closing && data_frame?(frame_type)
    raise WebSocketError, "Cannot send data frame since connection is closing"
  end

  frame = ''

  opcode = type_to_opcode(frame_type)
  byte1 = opcode | 0b10000000 # fin bit set, rsv1-3 are 0
  frame << byte1

  length = application_data.size
  if length <= 125
    byte2 = length # since rsv4 is 0
    frame << byte2
  elsif length < 65536 # write 2 byte length
    frame << 126
    frame << [length].pack('n')
  else # write 8 byte length
    frame << 127
    frame << [length >> 32, length & 0xFFFFFFFF].pack("NN")
  end

  frame << application_data

  @connection.send_data(frame)
end
```

    
  

    
      
  
### 
  
    #**send_text_frame**(data)  ⇒ Object 
  

  

  

  
    
      

```

154
155
156
```

    
    
      

```
# File 'lib/em-websocket/framing07.rb', line 154

def send_text_frame(data)
  send_frame(:text, data)
end
```