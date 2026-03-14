# Class: EventMachine::WebSocket::MaskedString
  
  
  

  
  
    Inherits:
    
      String
      
        

          
- Object
          
            
- String
          
            
- EventMachine::WebSocket::MaskedString
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/em-websocket/masking04.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**getbyte**(index)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**getbytes**(start_index, count)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**read_mask**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Read a 4 bit XOR mask - further requested bytes will be unmasked.

  

      
        
- 
  
    
      #**unset_mask**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Removes the mask, behaves like a normal string again.

  

      
    

  

  
  
  
  
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**getbyte**(index)  ⇒ Object 
  

  

  

  
    
      

```

18
19
20
21
22
23
24
25
```

    
    
      

```
# File 'lib/em-websocket/masking04.rb', line 18

def getbyte(index)
  if defined?(@masking_key) && @masking_key
    masked_char = super
    masked_char ? masked_char ^ @masking_key.getbyte(index % 4) : nil
  else
    super
  end
end
```

    
  

    
      
  
### 
  
    #**getbytes**(start_index, count)  ⇒ Object 
  

  

  

  
    
      

```

27
28
29
30
31
32
33
34
```

    
    
      

```
# File 'lib/em-websocket/masking04.rb', line 27

def getbytes(start_index, count)
  data = ''
  data.force_encoding('ASCII-8BIT') if data.respond_to?(:force_encoding)
  count.times do |i|
    data << getbyte(start_index + i)
  end
  data
end
```

    
  

    
      
  
### 
  
    #**read_mask**  ⇒ Object 
  

  

  

  
    

Read a 4 bit XOR mask - further requested bytes will be unmasked

  

  

  
    
      

```

5
6
7
8
9
10
11
```

    
    
      

```
# File 'lib/em-websocket/masking04.rb', line 5

def read_mask
  if respond_to?(:encoding) && encoding.name != "ASCII-8BIT"
    raise "MaskedString only operates on BINARY strings"
  end
  raise "Too short" if bytesize < 4 # TODO - change
  @masking_key = String.new(self[0..3])
end
```

    
  

    
      
  
### 
  
    #**unset_mask**  ⇒ Object 
  

  

  

  
    

Removes the mask, behaves like a normal string again

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/em-websocket/masking04.rb', line 14

def unset_mask
  @masking_key = nil
end
```