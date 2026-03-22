# Class: Prawn::Text::Formatted::Arranger
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Text::Formatted::Arranger
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/formatted/arranger.rb
  
  

## Overview

  
    

D data structure for 2-stage processing of lines of formatted text.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** BadFontFamily, NotFinalized
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**consumed**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute consumed.

  

    
      
- 
  
    
      #**current_format_state**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute current_format_state.

  

    
      
- 
  
    
      #**finalized**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute finalized.

  

    
      
- 
  
    
      #**fragments**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute fragments.

  

    
      
- 
  
    
      #**max_ascender**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute max_ascender.

  

    
      
- 
  
    
      #**max_descender**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute max_descender.

  

    
      
- 
  
    
      #**max_line_height**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute max_line_height.

  

    
      
- 
  
    
      #**unconsumed**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The following present only for testing purposes.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**apply_color_and_font_settings**(fragment) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Apply color and font settings.

  

      
        
- 
  
    
      #**apply_font_settings**(fragment = nil) { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Apply font settings.

  

      
        
- 
  
    
      #**finalize_line**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Finish laying out current line.

  

      
        
- 
  
    
      #**finished?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Were all fragments processed?.

  

      
        
- 
  
    
      #**font_style**(styles)  ⇒ Symbol 
    

    
  
  
  
  
  
  
  
  

  
    

Get font variant from fragment styles.

  

      
        
- 
  
    
      #**format_array=**(array)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Set new fragment array.

  

      
        
- 
  
    
      #**initialize**(document, options = {})  ⇒ Arranger 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Arranger.

  

      
        
- 
  
    
      #**initialize_line**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Prepare for new line layout.

  

      
        
- 
  
    
      #**line**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Line text.

  

      
        
- 
  
    
      #**line_width**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Line width.

  

      
        
- 
  
    
      #**next_string**  ⇒ String? 
    

    
  
  
  
  
  
  
  
  

  
    

Get the next unprocessed string.

  

      
        
- 
  
    
      #**preview_next_string**  ⇒ String? 
    

    
  
  
  
  
  
  
  
  

  
    

Get the next unprocessed string keeping it in the queue.

  

      
        
- 
  
    
      #**repack_unretrieved**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Repack remaining fragments.

  

      
        
- 
  
    
      #**retrieve_fragment**  ⇒ Prawn::Text::Formatted::Fragment 
    

    
  
  
  
  
  
  
  
  

  
    

Get the next fragment.

  

      
        
- 
  
    
      #**space_count**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Number of spaces in the text.

  

      
        
- 
  
    
      #**update_last_string**(printed, unprinted, normalized_soft_hyphen = nil)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Update last fragment’s text.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, options = {})  ⇒ Arranger 
  

  

  

  
    

Returns a new instance of Arranger.

  

  

  
    
      

```

45
46
47
48
49
50
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 45

def initialize(document, options = {})
  @document = document
  @fragments = []
  @unconsumed = []
  @kerning = options[:kerning]
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**consumed**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute consumed.

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 38

def consumed
  @consumed
end

```

    
  

    
      
      
      
  
### 
  
    #**current_format_state**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute current_format_state.

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 43

def current_format_state
  @current_format_state
end

```

    
  

    
      
      
      
  
### 
  
    #**finalized**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute finalized.

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 37

def finalized
  @finalized
end

```

    
  

    
      
      
      
  
### 
  
    #**fragments**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute fragments.

  

  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 42

def fragments
  @fragments
end

```

    
  

    
      
      
      
  
### 
  
    #**max_ascender**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute max_ascender.

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 36

def max_ascender
  @max_ascender
end

```

    
  

    
      
      
      
  
### 
  
    #**max_descender**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute max_descender.

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 35

def max_descender
  @max_descender
end

```

    
  

    
      
      
      
  
### 
  
    #**max_line_height**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute max_line_height.

  

  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 34

def max_line_height
  @max_line_height
end

```

    
  

    
      
      
      
  
### 
  
    #**unconsumed**  ⇒ Object  (readonly)
  

  

  

  
    

The following present only for testing purposes

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 41

def unconsumed
  @unconsumed
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**apply_color_and_font_settings**(fragment) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Apply color and font settings.

  

  

Parameters:

  
    
- 
      
        fragment
      
      
        (Prawn::Text::Formatted::Fragment)
      
      
      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 191

def apply_color_and_font_settings(fragment, &block)
  if fragment.color
    original_fill_color = @document.fill_color
    original_stroke_color = @document.stroke_color
    @document.fill_color(*fragment.color)
    @document.stroke_color(*fragment.color)
    apply_font_settings(fragment, &block)
    @document.stroke_color = original_stroke_color
    @document.fill_color = original_fill_color
  else
    apply_font_settings(fragment, &block)
  end
end

```

    
  

    
      
  
### 
  
    #**apply_font_settings**(fragment = nil) { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Apply font settings.

  

  

Parameters:

  
    
- 
      
        fragment
      
      
        (Prawn::Text::Formatted::Fragment)
      
      
        *(defaults to: nil)*
      
      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 210

def apply_font_settings(fragment = nil, &block)
  if fragment.nil?
    font = current_format_state[:font]
    size = current_format_state[:size]
    character_spacing = current_format_state[:character_spacing] ||
      @document.character_spacing
    styles = current_format_state[:styles]
  else
    font = fragment.font
    size = fragment.size
    character_spacing = fragment.character_spacing
    styles = fragment.styles
  end
  font_style = font_style(styles)

  @document.character_spacing(character_spacing) do
    if font || font_style != :normal
      raise BadFontFamily unless @document.font.family

      @document.font(
        font || @document.font.family, style: font_style,
      ) do
        apply_font_size(size, styles, &block)
      end
    else
      apply_font_size(size, styles, &block)
    end
  end
end

```

    
  

    
      
  
### 
  
    #**finalize_line**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Finish laying out current line.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 101

def finalize_line
  @finalized = true

  omit_trailing_whitespace_from_line_width
  @fragments = []
  @consumed.each do |hash|
    text = hash[:text]
    format_state = hash.dup
    format_state.delete(:text)
    fragment = Prawn::Text::Formatted::Fragment.new(
      text,
      format_state,
      @document,
    )
    @fragments << fragment
    self.fragment_measurements = fragment
    self.line_measurement_maximums = fragment
  end
end

```

    
  

    
      
  
### 
  
    #**finished?**  ⇒ Boolean 
  

  

  

  
    

Were all fragments processed?

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

151
152
153
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 151

def finished?
  @unconsumed.empty?
end

```

    
  

    
      
  
### 
  
    #**font_style**(styles)  ⇒ Symbol 
  

  

  

  
    

Get font variant from fragment styles.

  

  

Parameters:

  
    
- 
      
        styles
      
      
        (Array<Symbol>)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
    
  

  
    
      

```

295
296
297
298
299
300
301
302
303
304
305
306
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 295

def font_style(styles)
  styles = Array(styles)
  if styles.include?(:bold) && styles.include?(:italic)
    :bold_italic
  elsif styles.include?(:bold)
    :bold
  elsif styles.include?(:italic)
    :italic
  else
    :normal
  end
end

```

    
  

    
      
  
### 
  
    #**format_array=**(array)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Set new fragment array.

  

  

Parameters:

  
    
- 
      
        array
      
      
        (Array<Hash>)
      
      
      
    
  

  
    
      

```

125
126
127
128
129
130
131
132
133
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 125

def format_array=(array)
  initialize_line
  @unconsumed = []
  array.each do |hash|
    hash[:text].scan(/[^\n]+|\n/) do |line|
      @unconsumed << hash.merge(text: line)
    end
  end
end

```

    
  

    
      
  
### 
  
    #**initialize_line**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Prepare for new line layout.

  

  

  
    
      

```

138
139
140
141
142
143
144
145
146
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 138

def initialize_line
  @finalized = false
  @max_line_height = 0
  @max_descender = 0
  @max_ascender = 0

  @consumed = []
  @fragments = []
end

```

    
  

    
      
  
### 
  
    #**line**  ⇒ String 
  

  

  

  
    

Line text.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (NotFinalized)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 84

def line
  unless finalized
    raise NotFinalized.new(method: 'line')
  end

  @fragments.map { |fragment|
    begin
      fragment.text.dup.encode(::Encoding::UTF_8)
    rescue ::Encoding::InvalidByteSequenceError, ::Encoding::UndefinedConversionError
      fragment.text.dup.force_encoding(::Encoding::UTF_8)
    end
  }.join
end

```

    
  

    
      
  
### 
  
    #**line_width**  ⇒ Number 
  

  

  

  
    

Line width.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (NotFinalized)
      
      
      
    
  

  
    
      

```

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
# File 'lib/prawn/text/formatted/arranger.rb', line 70

def line_width
  unless finalized
    raise raise NotFinalized.new(method: 'line_width')
  end

  @fragments.reduce(0) do |sum, fragment|
    sum + fragment.width
  end
end

```

    
  

    
      
  
### 
  
    #**next_string**  ⇒ String? 
  

  

  

  
    

Get the next unprocessed string.

  

  

Returns:

  
    
- 
      
      
        (String, nil)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (NotFinalized)
      
      
      
    
  

  
    
      

```

159
160
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
171
172
173
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 159

def next_string
  if finalized
    raise NotFinalized.new(method: 'next_string')
  end

  next_unconsumed_hash = @unconsumed.shift

  if next_unconsumed_hash
    @consumed << next_unconsumed_hash.dup
    @current_format_state = next_unconsumed_hash.dup
    @current_format_state.delete(:text)

    next_unconsumed_hash[:text]
  end
end

```

    
  

    
      
  
### 
  
    #**preview_next_string**  ⇒ String? 
  

  

  

  
    

Get the next unprocessed string keeping it in the queue.

  

  

Returns:

  
    
- 
      
      
        (String, nil)
      
      
      
    
  

  
    
      

```

178
179
180
181
182
183
184
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 178

def preview_next_string
  next_unconsumed_hash = @unconsumed.first

  if next_unconsumed_hash
    next_unconsumed_hash[:text]
  end
end

```

    
  

    
      
  
### 
  
    #**repack_unretrieved**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Repack remaining fragments.

  

  

  
    
      

```

280
281
282
283
284
285
286
287
288
289
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 280

def repack_unretrieved
  new_unconsumed = []
  # rubocop: disable Lint/AssignmentInCondition
  while fragment = retrieve_fragment
    # rubocop: enable Lint/AssignmentInCondition
    fragment.include_trailing_white_space!
    new_unconsumed << fragment.format_state.merge(text: fragment.text)
  end
  @unconsumed = new_unconsumed.concat(@unconsumed)
end

```

    
  

    
      
  
### 
  
    #**retrieve_fragment**  ⇒ Prawn::Text::Formatted::Fragment 
  

  

  

  
    

Get the next fragment.

  

  

Returns:

  
    
- 
      
      
        (Prawn::Text::Formatted::Fragment)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (NotFinalized)
      
      
      
    
  

  
    
      

```

269
270
271
272
273
274
275
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 269

def retrieve_fragment
  unless finalized
    raise NotFinalized, 'Lines must be finalized before fragments can be retrieved'
  end

  @fragments.shift
end

```

    
  

    
      
  
### 
  
    #**space_count**  ⇒ Integer 
  

  

  

  
    

Number of spaces in the text.

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (NotFinalized)
      
      
      
    
  

  
    
      

```

56
57
58
59
60
61
62
63
64
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 56

def space_count
  unless finalized
    raise NotFinalized.new(method: 'space_count')
  end

  @fragments.reduce(0) do |sum, fragment|
    sum + fragment.space_count
  end
end

```

    
  

    
      
  
### 
  
    #**update_last_string**(printed, unprinted, normalized_soft_hyphen = nil)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Update last fragment’s text.

  

  

Parameters:

  
    
- 
      
        printed
      
      
        (String)
      
      
      
    
  
    
- 
      
        unprinted
      
      
        (String)
      
      
      
    
  
    
- 
      
        normalized_soft_hyphen
      
      
        (Boolean)
      
      
        *(defaults to: nil)*
      
      
    
  

  
    
      

```

246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263
```

    
    
      

```
# File 'lib/prawn/text/formatted/arranger.rb', line 246

def update_last_string(printed, unprinted, normalized_soft_hyphen = nil)
  return if printed.nil?

  if printed.empty?
    @consumed.pop
  else
    @consumed.last[:text] = printed
    if normalized_soft_hyphen
      @consumed.last[:normalized_soft_hyphen] = normalized_soft_hyphen
    end
  end

  unless unprinted.empty?
    @unconsumed.unshift(@current_format_state.merge(text: unprinted))
  end

  load_previous_format_state if printed.empty?
end

```