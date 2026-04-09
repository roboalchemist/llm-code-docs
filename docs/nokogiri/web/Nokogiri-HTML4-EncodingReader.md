# Class: Nokogiri::HTML4::EncodingReader
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::HTML4::EncodingReader
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/encoding_reader.rb
  
  

## Overview

  
    

:nodoc: all

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** EncodingFound, JumpSAXHandler, SAXHandler
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**encoding_found**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

This method is used by the C extension so that Nokogiri::HTML4::Document#read_io() does not leak memory when EncodingFound is raised.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**detect_encoding**(chunk)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(io)  ⇒ EncodingReader 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of EncodingReader.

  

      
        
- 
  
    
      #**read**(len)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(io)  ⇒ EncodingReader 
  

  

  

  
    

Returns a new instance of EncodingReader.

  

  

  
    
      

```

82
83
84
85
86
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 82

def initialize(io)
  @io = io
  @firstchunk = nil
  @encoding_found = nil
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**encoding_found**  ⇒ Object  (readonly)
  

  

  

  
    

This method is used by the C extension so that Nokogiri::HTML4::Document#read_io() does not leak memory when EncodingFound is raised.

  

  

  
    
      

```

91
92
93
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 91

def encoding_found
  @encoding_found
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**detect_encoding**(chunk)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 59

def self.detect_encoding(chunk)
  (m = chunk.match(/\A(<\?xml[ \t\r\n][^>]*>)/)) &&
    (return Nokogiri.XML(m[1]).encoding)

  if Nokogiri.jruby?
    (m = chunk.match(/(<meta\s)(.*)(charset\s*=\s*([\w-]+))(.*)/i)) &&
      (return m[4])
    catch(:encoding_found) do
      Nokogiri::HTML4::SAX::Parser.new(JumpSAXHandler.new(:encoding_found)).parse(chunk)
      nil
    end
  else
    handler = SAXHandler.new
    parser = Nokogiri::HTML4::SAX::PushParser.new(handler)
    begin
      parser << chunk
    rescue
      Nokogiri::SyntaxError
    end
    handler.encoding
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**read**(len)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/nokogiri/html4/encoding_reader.rb', line 93

def read(len)
  # no support for a call without len

  unless @firstchunk
    (@firstchunk = @io.read(len)) || return

    # This implementation expects that the first call from
    # htmlReadIO() is made with a length long enough (~1KB) to
    # achieve advanced encoding detection.
    if (encoding = EncodingReader.detect_encoding(@firstchunk))
      # The first chunk is stored for the next read in retry.
      raise @encoding_found = EncodingFound.new(encoding)
    end
  end
  @encoding_found = nil

  ret = @firstchunk.slice!(0, len)
  if (len -= ret.length) > 0
    (rest = @io.read(len)) && ret << (rest)
  end
  if ret.empty?
    nil
  else
    ret
  end
end
```