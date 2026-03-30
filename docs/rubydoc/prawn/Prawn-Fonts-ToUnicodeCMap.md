# Class: Prawn::Fonts::ToUnicodeCMap
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Fonts::ToUnicodeCMap
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/to_unicode_cmap.rb
  
  

## Overview

  
    

This class generates ToUnicode CMap for embedde TrueType/OpenType fonts. It’s a separate format and is somewhat complicated so it has its own place.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**generate**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Generate CMap.

  

      
        
- 
  
    
      #**initialize**(mapping, code_space_size = nil)  ⇒ ToUnicodeCMap 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

mapping is expected to be a hash with keys being character codes (in broad sense, as used in the showing operation strings) and values being Unicode code points.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(mapping, code_space_size = nil)  ⇒ ToUnicodeCMap 
  

  

  

  
    

mapping is expected to be a hash with keys being character codes (in broad sense, as used in the showing operation strings) and values being Unicode code points.

  

  

  
    
      

```

14
15
16
17
```

    
    
      

```
# File 'lib/prawn/fonts/to_unicode_cmap.rb', line 14

def initialize(mapping, code_space_size = nil)
  @mapping = mapping
  @code_space_size = code_space_size
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**generate**  ⇒ String 
  

  

  

  
    

Generate CMap.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/fonts/to_unicode_cmap.rb', line 22

def generate
  chunks = []

  # Header
  chunks << "    /CIDInit /ProcSet findresource begin\n    12 dict begin\n    begincmap\n    /CIDSystemInfo 3 dict dup begin\n      /Registry (Adobe) def\n      /Ordering (UCS) def\n      /Supplement 0 def\n    end def\n    /CMapName /Adobe-Identity-UCS def\n    /CMapType 2 def\n  HEADER\n\n  max_glyph_index = mapping.keys.max\n  # Range\n  code_space_size = (max_glyph_index.bit_length / 8.0).ceil\n\n  used_code_space_size = @code_space_size || code_space_size\n\n  # In CMap codespaces are not sequentional, they're ranges in\n  # a multi-dimentional space. Each byte is considered separately. So we\n  # have to maximally extend the lower bytes in order to allow for\n  # continuos mapping.\n  # We only keep the highest byte because usually it's lower than\n  # maximally allowed and we don't want to cover that unused space.\n  code_space_max = max_glyph_index | ('ff' * (code_space_size - 1)).to_i(16)\n\n  chunks << '1 begincodespacerange'\n  chunks << format(\"<%0\#{used_code_space_size * 2}X><%0\#{used_code_space_size * 2}X>\", 0, code_space_max)\n  chunks << 'endcodespacerange'\n\n  # Mapping\n  all_spans = mapping_spans(mapping.reject { |gid, cid| gid.zero? || (0xd800..0xdfff).cover?(cid) })\n\n  short_spans, long_spans = all_spans.partition { |span| span[0] == :short }\n\n  long_spans\n    .each_slice(100) do |spans|\n      chunks << \"\#{spans.length} beginbfrange\"\n\n      spans.each do |type, span|\n        # rubocop: disable Lint/FormatParameterMismatch # false positive\n        case type\n        when :fully_sorted\n          chunks << format(\n            \"<%0\#{code_space_size * 2}X><%0\#{code_space_size * 2}X><%s>\",\n            span.first[0],\n            span.last[0],\n            span.first[1].chr(::Encoding::UTF_16BE).unpack1('H*'),\n          )\n        when :index_sorted\n          chunks << format(\n            \"<%0\#{code_space_size * 2}X><%0\#{code_space_size * 2}X>[%s]\",\n            span.first[0],\n            span.last[0],\n            span.map { |_, cid| \"<\#{cid.chr(::Encoding::UTF_16BE).unpack1('H*')}>\" }.join(''),\n          )\n        end\n        # rubocop: enable Lint/FormatParameterMismatch\n      end\n\n      chunks << 'endbfrange'\n    end\n\n  short_spans\n    .map { |_type, slice| slice.flatten(1) }\n    .each_slice(100) do |mapping|\n      chunks << \"\#{mapping.length} beginbfchar\"\n      chunks.concat(\n        mapping.map { |(gid, cid)|\n          # rubocop: disable Lint/FormatParameterMismatch # false positive\n          format(\n            \"<%0\#{code_space_size * 2}X><%s>\",\n            gid,\n            cid.chr(::Encoding::UTF_16BE).unpack1('H*'),\n          )\n          # rubocop: enable Lint/FormatParameterMismatch\n        },\n      )\n      chunks << 'endbfchar'\n    end\n\n  # Footer\n  chunks << <<~FOOTER.chomp\n    endcmap\n    CMapName currentdict /CMap defineresource pop\n    end\n    end\n  FOOTER\n\n  chunks.join(\"\\n\")\nend\n".chomp

```