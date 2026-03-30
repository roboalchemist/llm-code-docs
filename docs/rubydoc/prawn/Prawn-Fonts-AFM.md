# Class: Prawn::Fonts::AFM
  
  
  

  
  
    Inherits:
    
      Prawn::Font
      
        

          
- Object
          
            
- Prawn::Font
          
            
- Prawn::Fonts::AFM
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/afm.rb
  
  

## Overview

  
    
  
    **Note:**
    

You shouldn’t use this class directly.

  

AFM font. AFM stands for Adobe Font Metrics. It’s not a complete font, it doesn’t provide actual glyph outlines. It only contains glyph metrics to make text layout possible. AFM is used for PDF built-in fonts. Those fonts are supposed to be present on the target system making it possible to save a little bit of space by not embedding the fonts. A file that uses these fonts can not be read on a system that doesn’t have these fonts installed.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        BUILT_INS =
          
  
    

List of PDF built-in fonts.

  

  

        
        

```
%w[
  Courier Helvetica Times-Roman Symbol ZapfDingbats
  Courier-Bold Courier-Oblique Courier-BoldOblique
  Times-Bold Times-Italic Times-BoldItalic
  Helvetica-Bold Helvetica-Oblique Helvetica-BoldOblique
].freeze

```

      
    
  

  
  
  
### Constants inherited
     from Prawn::Font

  

Prawn::Font::AFM, Prawn::Font::DFont, Prawn::Font::TTC, Prawn::Font::TTF

  
## Class Attribute Summary collapse

  

    
      
- 
  
    
      .**hide_m17n_warning**  ⇒ Boolean 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Prawn would warn you if you’re using non-ASCII glyphs with AFM fonts as not all implementations provide those glyphs.

  

    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**attributes**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    
  

    
  

  
  
  
### Attributes inherited from Prawn::Font

  

#family, #name, #options

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**font_data**  ⇒ SynchronizedCache 
    

    
  
  
  
  
  
  
  
  

  
    

Parsed AFM data cache.

  

      
        
- 
  
    
      .**metrics_path**  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

Paths to look for AFM files at.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**bbox**  ⇒ Array(Number, Number, Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

The font bbox.

  

      
        
- 
  
    
      #**character_count**(str)  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the number of characters in `str` (a WinAnsi-encoded string).

  

      
        
- 
  
    
      #**compute_width_of**(string, options = {})  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Compute width of a string at the specified size, optionally with kerning applied.

  

      
        
- 
  
    
      #**encode_text**(text, options = {})  ⇒ Array<Array(0, (String, Array)>] 
    

    
  
  
  
  
  
  
  
  

  
    

Perform any changes to the string that need to happen before it is rendered to the canvas.

  

      
        
- 
  
    
      #**glyph_present?**(char)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this font has a glyph for the character?.

  

      
        
- 
  
    
      #**has_kerning_data?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this font contain kerning data.

  

      
        
- 
  
    
      #**initialize**(document, name, options = {})  ⇒ AFM 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of AFM.

  

      
        
- 
  
    
      #**normalize_encoding**(text)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Built-in fonts only work with WinAnsi encoding, so translate the string.

  

      
        
- 
  
    
      #**to_utf8**(text)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Encode text to UTF-8.

  

      
        
- 
  
    
      #**unicode?**  ⇒ false 
    

    
  
  
  
  
  
  
  
  

  
    

Does this font support Unicode?.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Prawn::Font

  

#add_to_current_page, #ascender, #descender, #eql?, font_format, #hash, #height, #height_at, #identifier_for, #inspect, #line_gap, load, #normalize_encoding!

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, name, options = {})  ⇒ AFM 
  

  

  

  
    

Returns a new instance of AFM.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :family
          (String)
          
            
          
          
        
      
        
- 
          :style
          (Symbol)
          
            
          
          
        
      
    

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 75

def initialize(document, name, options = {})
  name ||= options[:family]
  unless BUILT_INS.include?(name)
    raise Prawn::Errors::UnknownFont,
      "#{name} (#{options[:style] || 'normal'}) is not a known font."
  end

  super

  file_name = @name.dup
  file_name << '.afm' unless /\.afm$/.match?(file_name)
  file_name = find_font(file_name) unless file_name[0] == '/'

  font_data = self.class.font_data[file_name] ||= parse_afm(file_name)
  @glyph_widths = font_data[:glyph_widths]
  @glyph_table = font_data[:glyph_table]
  @bounding_boxes = font_data[:bounding_boxes]
  @kern_pairs = font_data[:kern_pairs]
  @kern_pair_table = font_data[:kern_pair_table]
  @attributes = font_data[:attributes]

  @ascender = Integer(@attributes.fetch('ascender', '0'), 10)
  @descender = Integer(@attributes.fetch('descender', '0'), 10)
  @line_gap = Float(bbox[3] - bbox[1]) - (@ascender - @descender)
end

```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**hide_m17n_warning**  ⇒ Boolean 
  

  

  

  
    

Prawn would warn you if you’re using non-ASCII glyphs with AFM fonts as not all implementations provide those glyphs. This attribute suppresses that warning.

  

  

Returns:

  
    
- 
      
      
      
      
        
        

(false)

      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 23

def hide_m17n_warning
  @hide_m17n_warning
end

```

    
  

    
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**attributes**  ⇒ Object  (readonly)
  

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 61

def attributes
  @attributes
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**font_data**  ⇒ SynchronizedCache 
  

  

  

  
    

Parsed AFM data cache.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 66

def self.font_data
  @font_data ||= SynchronizedCache.new
end

```

    
  

    
      
  
### 
  
    .**metrics_path**  ⇒ Array<String> 
  

  

  

  
    

Paths to look for AFM files at.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 46

def self.metrics_path
  @metrics_path ||=
    if ENV['METRICS']
      ENV['METRICS'].split(':')
    else
      [
        '.', '/usr/lib/afm',
        '/usr/local/lib/afm',
        '/usr/openwin/lib/fonts/afm',
        "#{Prawn::DATADIR}/fonts",
      ]
    end
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**bbox**  ⇒ Array(Number, Number, Number, Number) 
  

  

  

  
    

The font bbox.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

104
105
106
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 104

def bbox
  @bbox ||= @attributes['fontbbox'].split(/\s+/).map { |e| Integer(e) }
end

```

    
  

    
      
  
### 
  
    #**character_count**(str)  ⇒ Integer 
  

  

  

  
    

Returns the number of characters in `str` (a WinAnsi-encoded string).

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

165
166
167
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 165

def character_count(str)
  str.length
end

```

    
  

    
      
  
### 
  
    #**compute_width_of**(string, options = {})  ⇒ Number 
  

  

  

  
    

Compute width of a string at the specified size, optionally with kerning applied.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

**must** be encoded as WinAnsi

      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :size
          (Number)
          
            
          
          
        
      
        
- 
          :kerning
          (Boolean)
          
            
              — default:
              false
            
          
          
        
      
    

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 116

def compute_width_of(string, options = {})
  scale = (options[:size] || size) / 1000.0

  if options[:kerning]
    strings, numbers = kern(string).partition { |e| e.is_a?(String) }
    total_kerning_offset = numbers.sum
    (unscaled_width_of(strings.join) - total_kerning_offset) * scale
  else
    unscaled_width_of(string) * scale
  end
end

```

    
  

    
      
  
### 
  
    #**encode_text**(text, options = {})  ⇒ Array<Array(0, (String, Array)>] 
  

  

  

  
    

Perform any changes to the string that need to happen before it is rendered to the canvas. Returns an array of subset “chunks”, where each chunk is an array of two elements. The first element is the font subset number, and the second is either a string or an array (for kerned text).

For Adobe fonts, there is only ever a single subset, so the first element of the array is `0`, and the second is the string itself (or an array, if kerning is performed).

The `text` argument must be in WinAnsi encoding (cp1252).

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :kerning
          (Boolean)
          
            
          
          
        
      
    

  

Returns:

  
    
- 
      
      
      
      
        
        

Array<Array(0, (String, Array)>]

      
    
  

  
    
      

```

185
186
187
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 185

def encode_text(text, options = {})
  [[0, options[:kerning] ? kern(text) : text]]
end

```

    
  

    
      
  
### 
  
    #**glyph_present?**(char)  ⇒ Boolean 
  

  

  

  
    

Does this font has a glyph for the character?

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

193
194
195
196
197
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 193

def glyph_present?(char)
  !normalize_encoding(char).nil?
rescue Prawn::Errors::IncompatibleStringEncoding
  false
end

```

    
  

    
      
  
### 
  
    #**has_kerning_data?**  ⇒ Boolean 
  

  

  

  
    

Does this font contain kerning data.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

131
132
133
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 131

def has_kerning_data? # rubocop: disable Naming/PredicateName
  @kern_pairs.any?
end

```

    
  

    
      
  
### 
  
    #**normalize_encoding**(text)  ⇒ String 
  

  

  

  
    

Built-in fonts only work with WinAnsi encoding, so translate the string. Changes the encoding in-place, so the argument itself is replaced with a string in WinAnsi encoding.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 141

def normalize_encoding(text)
  text.encode('windows-1252')
rescue ::Encoding::InvalidByteSequenceError,
       ::Encoding::UndefinedConversionError

  raise Prawn::Errors::IncompatibleStringEncoding,
    "Your document includes text that's not compatible with the " \
      "Windows-1252 character set.\n" \
      'If you need full UTF-8 support, use external fonts instead of ' \
      "PDF's built-in fonts.\n"
end

```

    
  

    
      
  
### 
  
    #**to_utf8**(text)  ⇒ String 
  

  

  

  
    

Encode text to UTF-8.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

157
158
159
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 157

def to_utf8(text)
  text.encode('UTF-8')
end

```

    
  

    
      
  
### 
  
    #**unicode?**  ⇒ false 
  

  

  

  
    

Does this font support Unicode?

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

39
40
41
```

    
    
      

```
# File 'lib/prawn/fonts/afm.rb', line 39

def unicode?
  false
end

```