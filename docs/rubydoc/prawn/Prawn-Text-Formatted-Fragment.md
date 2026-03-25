# Class: Prawn::Text::Formatted::Fragment
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Text::Formatted::Fragment
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/formatted/fragment.rb
  
  

## Overview

  
    

Prawn::Text::Formatted::Fragment is a state store for a formatted text fragment. It does not render anything.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**ascender**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute ascender.

  

    
      
- 
  
    
      #**baseline**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute baseline.

  

    
      
- 
  
    
      #**descender**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute descender.

  

    
      
- 
  
    
      #**format_state**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute format_state.

  

    
      
- 
  
    
      #**left**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute left.

  

    
      
- 
  
    
      #**line_height**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute line_height.

  

    
      
- 
  
    
      #**text**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute text.

  

    
      
- 
  
    
      #**width**  ⇒ Number 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Width of fragment.

  

    
      
- 
  
    
      #**word_spacing**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute word_spacing.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**absolute_bottom**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute vertical coordinate of the bottom side of the fragment.

  

      
        
- 
  
    
      #**absolute_bottom_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute coordinates of the bottom left corner of the fragment.

  

      
        
- 
  
    
      #**absolute_bottom_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute coordinates of the bottom right corner of the fragment.

  

      
        
- 
  
    
      #**absolute_bounding_box**  ⇒ Array(Number, Number, Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Fragment bounding box, relative to the containing page.

  

      
        
- 
  
    
      #**absolute_left**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute horizontal coordinate of the left side of the fragment.

  

      
        
- 
  
    
      #**absolute_right**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute horizontal coordinate of the right side of the fragment.

  

      
        
- 
  
    
      #**absolute_top**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute vertical coordinate of the top side of the fragment.

  

      
        
- 
  
    
      #**absolute_top_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute coordinates of the top left corner of the fragment.

  

      
        
- 
  
    
      #**absolute_top_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Absolute coordinates of the top right corner of the fragment.

  

      
        
- 
  
    
      #**anchor**  ⇒ PDF::Core::Reference, ... 
    

    
  
  
  
  
  
  
  
  

  
    

Anchor.

  

      
        
- 
  
    
      #**bottom**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Vertical coordinate of the bottom side of the fragment.

  

      
        
- 
  
    
      #**bottom_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Coordinates of the bottom left corner of the fragment.

  

      
        
- 
  
    
      #**bottom_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Coordinates of the bottom right corner of the fragment.

  

      
        
- 
  
    
      #**bounding_box**  ⇒ Array(Number, Number, Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Fragment bounding box, relative to the containing bounding box.

  

      
        
- 
  
    
      #**callback_objects**  ⇒ Array 
    

    
  
  
  
  
  
  
  
  

  
    

Callbacks.

  

      
        
- 
  
    
      #**character_spacing**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Character spacing.

  

      
        
- 
  
    
      #**color**  ⇒ Color 
    

    
  
  
  
  
  
  
  
  

  
    

Fragment color.

  

      
        
- 
  
    
      #**default_direction=**(direction)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Set default text direction.

  

      
        
- 
  
    
      #**direction**  ⇒ :ltr, :rtl 
    

    
  
  
  
  
  
  
  
  

  
    

Text direction.

  

      
        
- 
  
    
      #**font**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Fragment font name.

  

      
        
- 
  
    
      #**height**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Height of fragment.

  

      
        
- 
  
    
      #**include_trailing_white_space!**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Keep trailing spaces.

  

      
        
- 
  
    
      #**initialize**(text, format_state, document)  ⇒ Fragment 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Fragment.

  

      
        
- 
  
    
      #**link**  ⇒ String? 
    

    
  
  
  
  
  
  
  
  

  
    

Fragment link.

  

      
        
- 
  
    
      #**local**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Local destination.

  

      
        
- 
  
    
      #**right**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Horizontal coordinate of the right side of the fragment.

  

      
        
- 
  
    
      #**size**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Font size.

  

      
        
- 
  
    
      #**space_count**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Number of spaces in the text.

  

      
        
- 
  
    
      #**strikethrough_points**  ⇒ Array(Array(Number, Number), Array(Number, Number)) 
    

    
  
  
  
  
  
  
  
  

  
    

Strikethrough endpoints.

  

      
        
- 
  
    
      #**styles**  ⇒ Array<Symbol> 
    

    
  
  
  
  
  
  
  
  

  
    

Fragment font styles.

  

      
        
- 
  
    
      #**subscript?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this a subscript fragment?.

  

      
        
- 
  
    
      #**superscript?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this a superscript fragment?.

  

      
        
- 
  
    
      #**top**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Vertical coordinate of the top side of the fragment.

  

      
        
- 
  
    
      #**top_left**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Coordinates of the top left corner of the fragment.

  

      
        
- 
  
    
      #**top_right**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

Coordinates of the top right corner of the fragment.

  

      
        
- 
  
    
      #**underline_points**  ⇒ Array(Array(Number, Number), Array(Number, Number)) 
    

    
  
  
  
  
  
  
  
  

  
    

Underline endpoints.

  

      
        
- 
  
    
      #**y_offset**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Vertical offset of the fragment.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(text, format_state, document)  ⇒ Fragment 
  

  

  

  
    

Returns a new instance of Fragment.

  

  

Parameters:

  
    
- 
      
        text
      
      
        (String)
      
      
      
    
  
    
- 
      
        format_state
      
      
        (Hash{Symbol => any})
      
      
      
    
  
    
- 
      
        document
      
      
        (Prawn::Documnt)
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 24

def initialize(text, format_state, document)
  @format_state = format_state
  @document = document
  @word_spacing = 0

  # keep the original value of "text", so we can reinitialize @text if
  # formatting parameters like text direction are changed
  @original_text = text
  @text = process_text(@original_text)
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**ascender**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute ascender.

  

  

  
    
      

```

16
17
18
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 16

def ascender
  @ascender
end

```

    
  

    
      
      
      
  
### 
  
    #**baseline**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute baseline.

  

  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 19

def baseline
  @baseline
end

```

    
  

    
      
      
      
  
### 
  
    #**descender**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute descender.

  

  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 15

def descender
  @descender
end

```

    
  

    
      
      
      
  
### 
  
    #**format_state**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute format_state.

  

  

  
    
      

```

11
12
13
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 11

def format_state
  @format_state
end

```

    
  

    
      
      
      
  
### 
  
    #**left**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute left.

  

  

  
    
      

```

18
19
20
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 18

def left
  @left
end

```

    
  

    
      
      
      
  
### 
  
    #**line_height**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute line_height.

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 14

def line_height
  @line_height
end

```

    
  

    
      
      
      
  
### 
  
    #**text**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute text.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 12

def text
  @text
end

```

    
  

    
      
      
      
  
### 
  
    #**width**  ⇒ Number 
  

  

  

  
    

Width of fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

38
39
40
41
42
43
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 38

def width
  if @word_spacing.zero? then @width
  else
    @width + (@word_spacing * space_count)
  end
end

```

    
  

    
      
      
      
  
### 
  
    #**word_spacing**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute word_spacing.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 17

def word_spacing
  @word_spacing
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**absolute_bottom**  ⇒ Number 
  

  

  

  
    

Absolute vertical coordinate of the bottom side of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

289
290
291
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 289

def absolute_bottom
  absolute_bounding_box[1]
end

```

    
  

    
      
  
### 
  
    #**absolute_bottom_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute coordinates of the bottom left corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

310
311
312
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 310

def absolute_bottom_left
  [absolute_left, absolute_bottom]
end

```

    
  

    
      
  
### 
  
    #**absolute_bottom_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute coordinates of the bottom right corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

317
318
319
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 317

def absolute_bottom_right
  [absolute_right, absolute_bottom]
end

```

    
  

    
      
  
### 
  
    #**absolute_bounding_box**  ⇒ Array(Number, Number, Number, Number) 
  

  

  

  
    

Fragment bounding box, relative to the containing page.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number, Number, Number))
      
      
      
    
  

  
    
      

```

87
88
89
90
91
92
93
94
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 87

def absolute_bounding_box
  box = bounding_box
  box[0] += @document.bounds.absolute_left
  box[2] += @document.bounds.absolute_left
  box[1] += @document.bounds.absolute_bottom
  box[3] += @document.bounds.absolute_bottom
  box
end

```

    
  

    
      
  
### 
  
    #**absolute_left**  ⇒ Number 
  

  

  

  
    

Absolute horizontal coordinate of the left side of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

268
269
270
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 268

def absolute_left
  absolute_bounding_box[0]
end

```

    
  

    
      
  
### 
  
    #**absolute_right**  ⇒ Number 
  

  

  

  
    

Absolute horizontal coordinate of the right side of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

275
276
277
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 275

def absolute_right
  absolute_bounding_box[2]
end

```

    
  

    
      
  
### 
  
    #**absolute_top**  ⇒ Number 
  

  

  

  
    

Absolute vertical coordinate of the top side of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

282
283
284
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 282

def absolute_top
  absolute_bounding_box[3]
end

```

    
  

    
      
  
### 
  
    #**absolute_top_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute coordinates of the top left corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

296
297
298
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 296

def absolute_top_left
  [absolute_left, absolute_top]
end

```

    
  

    
      
  
### 
  
    #**absolute_top_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Absolute coordinates of the top right corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

303
304
305
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 303

def absolute_top_right
  [absolute_right, absolute_top]
end

```

    
  

    
      
  
### 
  
    #**anchor**  ⇒ PDF::Core::Reference, ... 
  

  

  

  
    

Anchor.

  

  

Returns:

  
    
- 
      
      
        (PDF::Core::Reference, Array, Hash)
      
      
      
    
  

  
    
      

```

129
130
131
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 129

def anchor
  @format_state[:anchor]
end

```

    
  

    
      
  
### 
  
    #**bottom**  ⇒ Number 
  

  

  

  
    

Vertical coordinate of the bottom side of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

233
234
235
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 233

def bottom
  baseline - descender
end

```

    
  

    
      
  
### 
  
    #**bottom_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Coordinates of the bottom left corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

261
262
263
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 261

def bottom_left
  [left, bottom]
end

```

    
  

    
      
  
### 
  
    #**bottom_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Coordinates of the bottom right corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

254
255
256
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 254

def bottom_right
  [right, bottom]
end

```

    
  

    
      
  
### 
  
    #**bounding_box**  ⇒ Array(Number, Number, Number, Number) 
  

  

  

  
    

Fragment bounding box, relative to the containing bounding box.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number, Number, Number))
      
      
      
    
  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 80

def bounding_box
  [left, bottom, right, top]
end

```

    
  

    
      
  
### 
  
    #**callback_objects**  ⇒ Array 
  

  

  

  
    

Callbacks.

  

  

Returns:

  
    
- 
      
      
        (Array)
      
      
      
    
  

  
    
      

```

205
206
207
208
209
210
211
212
213
214
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 205

def callback_objects
  callback = @format_state[:callback]
  if callback.nil?
    []
  elsif callback.is_a?(Array)
    callback
  else
    [callback]
  end
end

```

    
  

    
      
  
### 
  
    #**character_spacing**  ⇒ Number 
  

  

  

  
    

Character spacing.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

164
165
166
167
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 164

def character_spacing
  @format_state[:character_spacing] ||
    @document.character_spacing
end

```

    
  

    
      
  
### 
  
    #**color**  ⇒ Color 
  

  

  

  
    

Fragment color.

  

  

Returns:

  
    
- 
      
      
        (Color)
      
      
      
    
  

  
    
      

```

143
144
145
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 143

def color
  @format_state[:color]
end

```

    
  

    
      
  
### 
  
    #**default_direction=**(direction)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Set default text direction.

  

  

Parameters:

  
    
- 
      
        direction
      
      
        (:ltr, :rtl)
      
      
      
    
  

  
    
      

```

180
181
182
183
184
185
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 180

def default_direction=(direction)
  unless @format_state[:direction]
    @format_state[:direction] = direction
    @text = process_text(@original_text)
  end
end

```

    
  

    
      
  
### 
  
    #**direction**  ⇒ :ltr, :rtl 
  

  

  

  
    

Text direction.

  

  

Returns:

  
    
- 
      
      
        (:ltr, :rtl)
      
      
      
    
  

  
    
      

```

172
173
174
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 172

def direction
  @format_state[:direction]
end

```

    
  

    
      
  
### 
  
    #**font**  ⇒ String 
  

  

  

  
    

Fragment font name.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

150
151
152
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 150

def font
  @format_state[:font]
end

```

    
  

    
      
  
### 
  
    #**height**  ⇒ Number 
  

  

  

  
    

Height of fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 48

def height
  top - bottom
end

```

    
  

    
      
  
### 
  
    #**include_trailing_white_space!**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Keep trailing spaces.

  

  

  
    
      

```

190
191
192
193
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 190

def include_trailing_white_space!
  @format_state.delete(:exclude_trailing_white_space)
  @text = process_text(@original_text)
end

```

    
  

    
      
  
### 
  
    #**link**  ⇒ String? 
  

  

  

  
    

Fragment link.

  

  

Returns:

  
    
- 
      
      
        (String, nil)
      
      
      
    
  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 122

def link
  @format_state[:link]
end

```

    
  

    
      
  
### 
  
    #**local**  ⇒ String 
  

  

  

  
    

Local destination.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

136
137
138
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 136

def local
  @format_state[:local]
end

```

    
  

    
      
  
### 
  
    #**right**  ⇒ Number 
  

  

  

  
    

Horizontal coordinate of the right side of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

219
220
221
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 219

def right
  left + width
end

```

    
  

    
      
  
### 
  
    #**size**  ⇒ Number 
  

  

  

  
    

Font size.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

157
158
159
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 157

def size
  @format_state[:size]
end

```

    
  

    
      
  
### 
  
    #**space_count**  ⇒ Integer 
  

  

  

  
    

Number of spaces in the text.

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

198
199
200
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 198

def space_count
  @text.count(' ')
end

```

    
  

    
      
  
### 
  
    #**strikethrough_points**  ⇒ Array(Array(Number, Number), Array(Number, Number)) 
  

  

  

  
    

Strikethrough endpoints.

  

  

Returns:

  
    
- 
      
      
        (Array(Array(Number, Number), Array(Number, Number)))
      
      
      
    
  

  
    
      

```

107
108
109
110
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 107

def strikethrough_points
  y = baseline + (ascender * 0.3)
  [[left, y], [right, y]]
end

```

    
  

    
      
  
### 
  
    #**styles**  ⇒ Array<Symbol> 
  

  

  

  
    

Fragment font styles.

  

  

Returns:

  
    
- 
      
      
        (Array<Symbol>)
      
      
      
    
  

  
    
      

```

115
116
117
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 115

def styles
  @format_state[:styles] || []
end

```

    
  

    
      
  
### 
  
    #**subscript?**  ⇒ Boolean 
  

  

  

  
    

Is this a subscript fragment?

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 55

def subscript?
  styles.include?(:subscript)
end

```

    
  

    
      
  
### 
  
    #**superscript?**  ⇒ Boolean 
  

  

  

  
    

Is this a superscript fragment?

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 62

def superscript?
  styles.include?(:superscript)
end

```

    
  

    
      
  
### 
  
    #**top**  ⇒ Number 
  

  

  

  
    

Vertical coordinate of the top side of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

226
227
228
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 226

def top
  baseline + ascender
end

```

    
  

    
      
  
### 
  
    #**top_left**  ⇒ Array(Number, Number) 
  

  

  

  
    

Coordinates of the top left corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

240
241
242
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 240

def top_left
  [left, top]
end

```

    
  

    
      
  
### 
  
    #**top_right**  ⇒ Array(Number, Number) 
  

  

  

  
    

Coordinates of the top right corner of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

247
248
249
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 247

def top_right
  [right, top]
end

```

    
  

    
      
  
### 
  
    #**underline_points**  ⇒ Array(Array(Number, Number), Array(Number, Number)) 
  

  

  

  
    

Underline endpoints.

  

  

Returns:

  
    
- 
      
      
        (Array(Array(Number, Number), Array(Number, Number)))
      
      
      
    
  

  
    
      

```

99
100
101
102
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 99

def underline_points
  y = baseline - 1.25
  [[left, y], [right, y]]
end

```

    
  

    
      
  
### 
  
    #**y_offset**  ⇒ Number 
  

  

  

  
    

Vertical offset of the fragment.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

69
70
71
72
73
74
75
```

    
    
      

```
# File 'lib/prawn/text/formatted/fragment.rb', line 69

def y_offset
  if subscript? then -descender
  elsif superscript? then 0.85 * ascender
  else
    0
  end
end

```