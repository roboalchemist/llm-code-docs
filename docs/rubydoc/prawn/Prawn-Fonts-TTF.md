# Class: Prawn::Fonts::TTF
  
  
  

  
  
    Inherits:
    
      Prawn::Font
      
        

          
- Object
          
            
- Prawn::Font
          
            
- Prawn::Fonts::TTF
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/fonts/ttf.rb
  
  

## Overview

  
    
  
    **Note:**
    

You shouldn’t use this class directly.

  

TrueType font.

  

  

  
## Direct Known Subclasses

  

DFont, OTF, TTC

## Defined Under Namespace

  
    
  
    
      **Classes:** Error, FullFontSubsetsCollection, NoPostscriptName, NoUnicodeCMap
    
  

  
## Constant Summary

  
  
### Constants inherited
     from Prawn::Font

  

Prawn::Font::AFM, Prawn::Font::DFont, Prawn::Font::TTC, Prawn::Font::TTF

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**subsets**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute subsets.

  

    
      
- 
  
    
      #**ttf**  ⇒ TTFunk::File 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

TTFunk font.

  

    
  

  
  
  
### Attributes inherited from Prawn::Font

  

#family, #name, #options

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**basename**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Base name of the font.

  

      
        
- 
  
    
      #**bbox**  ⇒ Array(Number, Number, Number, Number) 
    

    
  
  
  
  
  
  
  
  

  
    

The font bbox.

  

      
        
- 
  
    
      #**cap_height**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**character_count**(str)  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the number of characters in `str` (a UTF-8-encoded string).

  

      
        
- 
  
    
      #**compute_width_of**(string, options = {})  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Compute width of a string at the specified size, optionally with kerning applied.

  

      
        
- 
  
    
      #**encode_text**(text, options = {})  ⇒ Array<Array(0, (String, Array)>] 
    

    
  
  
  
  
  
  
  
  

  
    

Perform any changes to the string that need to happen before it is rendered to the canvas.

  

      
        
- 
  
    
      #**family_class**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**glyph_present?**(char)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this font has a glyph for the character?.

  

      
        
- 
  
    
      #**has_kerning_data?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this font contain kerning data.

  

      
        
- 
  
    
      #**initialize**(document, name, options = {})  ⇒ TTF 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of TTF.

  

      
        
- 
  
    
      #**italic_angle**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**normalize_encoding**(text)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Normlize text to a compatible encoding.

  

      
        
- 
  
    
      #**pdf_flags**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**script?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**serif?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**stem_v**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_utf8**(text)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Encode text to UTF-8.

  

      
        
- 
  
    
      #**unicode?**  ⇒ true 
    

    
  
  
  
  
  
  
  
  

  
    

Does this font support Unicode?.

  

      
        
- 
  
    
      #**x_height**  ⇒ number 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Prawn::Font

  

#add_to_current_page, #ascender, #descender, #eql?, font_format, #hash, #height, #height_at, #identifier_for, #inspect, #line_gap, load, #normalize_encoding!

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, name, options = {})  ⇒ TTF 
  

  

  

  
    

Returns a new instance of TTF.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
        
        

font file path

      
    
  
    
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
153
154
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 134

def initialize(document, name, options = {})
  super

  @ttf = read_ttf_file
  @subsets =
    if full_font_embedding
      FullFontSubsetsCollection.new(@ttf)
    else
      TTFunk::SubsetCollection.new(@ttf)
    end
  @italic_angle = nil

  @attributes = {}
  @bounding_boxes = {}
  @char_widths = {}
  @has_kerning_data = @ttf.kerning.exists? && @ttf.kerning.tables.any?

  @ascender = Integer(@ttf.ascent * scale_factor)
  @descender = Integer(@ttf.descent * scale_factor)
  @line_gap = Integer(@ttf.line_gap * scale_factor)
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**subsets**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute subsets.

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 58

def subsets
  @subsets
end

```

    
  

    
      
      
      
  
### 
  
    #**ttf**  ⇒ TTFunk::File  (readonly)
  

  

  

  
    

TTFunk font.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 57

def ttf
  @ttf
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**basename**  ⇒ String 
  

  

  

  
    

Base name of the font.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

240
241
242
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 240

def basename
  @basename ||= @ttf.name.postscript_name
end

```

    
  

    
      
  
### 
  
    #**bbox**  ⇒ Array(Number, Number, Number, Number) 
  

  

  

  
    

The font bbox.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

184
185
186
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 184

def bbox
  @bbox ||= @ttf.bbox.map { |i| Integer(i * scale_factor) }
end

```

    
  

    
      
  
### 
  
    #**cap_height**  ⇒ Number 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

272
273
274
275
276
277
278
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 272

def cap_height
  @cap_height ||=
    begin
      height = (@ttf.os2.exists? && @ttf.os2.cap_height) || 0
      height.zero? ? @ascender : height
    end
end

```

    
  

    
      
  
### 
  
    #**character_count**(str)  ⇒ Integer 
  

  

  

  
    

Returns the number of characters in `str` (a UTF-8-encoded string).

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

354
355
356
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 354

def character_count(str)
  str.length
end

```

    
  

    
      
  
### 
  
    #**compute_width_of**(string, options = {})  ⇒ Number 
  

  

  

  
    

Compute width of a string at the specified size, optionally with kerning applied.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

**must** be encoded as UTF-8

      
    
  
    
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
174
175
176
177
178
179
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 164

def compute_width_of(string, options = {})
  scale = (options[:size] || size) / 1000.0
  if options[:kerning]
    kern(string).reduce(0) { |s, r|
      if r.is_a?(Numeric)
        s - r
      else
        r.reduce(s) { |a, e| a + character_width_by_code(e) }
      end
    } * scale
  else
    string.codepoints.reduce(0) { |s, r|
      s + character_width_by_code(r)
    } * scale
  end
end

```

    
  

    
      
  
### 
  
    #**encode_text**(text, options = {})  ⇒ Array<Array(0, (String, Array)>] 
  

  

  

  
    

Perform any changes to the string that need to happen before it is rendered to the canvas. Returns an array of subset “chunks”, where the even-numbered indices are the font subset number, and the following entry element is either a string or an array (for kerned text).

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

must be in UTF-8 encoding

      
    
  
    
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

204
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
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 204

def encode_text(text, options = {})
  text = text.chomp

  if options[:kerning]
    last_subset = nil
    kern(text).reduce([]) do |result, element|
      if element.is_a?(Numeric)
        unless result.last[1].is_a?(Array)
          result.last[1] = [result.last[1]]
        end
        result.last[1] << element
        result
      else
        encoded = @subsets.encode(element)

        if encoded.first[0] == last_subset
          result.last[1] << encoded.first[1]
          encoded.shift
        end

        if encoded.any?
          last_subset = encoded.last[0]
          result + encoded
        else
          result
        end
      end
    end
  else
    @subsets.encode(text.unpack('U*'))
  end
end

```

    
  

    
      
  
### 
  
    #**family_class**  ⇒ Number 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

290
291
292
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 290

def family_class
  @family_class ||= ((@ttf.os2.exists? && @ttf.os2.family_class) || 0) >> 8
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

345
346
347
348
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 345

def glyph_present?(char)
  code = char.codepoints.first
  cmap[code].positive?
end

```

    
  

    
      
  
### 
  
    #**has_kerning_data?**  ⇒ Boolean 
  

  

  

  
    

Does this font contain kerning data.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

191
192
193
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 191

def has_kerning_data? # rubocop: disable Naming/PredicateName
  @has_kerning_data
end

```

    
  

    
      
  
### 
  
    #**italic_angle**  ⇒ Number 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
264
265
266
267
268
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 254

def italic_angle
  return @italic_angle if @italic_angle

  if @ttf.postscript.exists?
    raw = @ttf.postscript.italic_angle
    hi = raw >> 16
    low = raw & 0xFF
    hi = -((hi ^ 0xFFFF) + 1) if hi & 0x8000 != 0
    @italic_angle = Float("#{hi}.#{low}")
  else
    @italic_angle = 0
  end

  @italic_angle
end

```

    
  

    
      
  
### 
  
    #**normalize_encoding**(text)  ⇒ String 
  

  

  

  
    

Normlize text to a compatible encoding.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

325
326
327
328
329
330
331
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 325

def normalize_encoding(text)
  text.encode(::Encoding::UTF_8)
rescue StandardError
  raise Prawn::Errors::IncompatibleStringEncoding,
    "Encoding #{text.encoding} can not be transparently converted to UTF-8. " \
      'Please ensure the encoding of the string you are attempting to use is set correctly'
end

```

    
  

    
      
  
### 
  
    #**pdf_flags**  ⇒ Integer 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

308
309
310
311
312
313
314
315
316
317
318
319
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 308

def pdf_flags
  @pdf_flags ||=
    begin
      flags = 0
      flags |= 0x0001 if @ttf.postscript.fixed_pitch?
      flags |= 0x0002 if serif?
      flags |= 0x0008 if script?
      flags |= 0x0040 if italic_angle != 0
      # Assume the font contains at least some non-latin characters
      flags | 0x0004
    end
end

```

    
  

    
      
  
### 
  
    #**script?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

302
303
304
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 302

def script?
  @script ||= family_class == 10
end

```

    
  

    
      
  
### 
  
    #**serif?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

296
297
298
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 296

def serif?
  @serif ||= [1, 2, 3, 4, 5, 7].include?(family_class)
end

```

    
  

    
      
  
### 
  
    #**stem_v**  ⇒ Number 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

248
249
250
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 248

def stem_v
  0
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

337
338
339
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 337

def to_utf8(text)
  text.encode('UTF-8')
end

```

    
  

    
      
  
### 
  
    #**unicode?**  ⇒ true 
  

  

  

  
    

Does this font support Unicode?

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

63
64
65
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 63

def unicode?
  true
end

```

    
  

    
      
  
### 
  
    #**x_height**  ⇒ number 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

282
283
284
285
286
```

    
    
      

```
# File 'lib/prawn/fonts/ttf.rb', line 282

def x_height
  # FIXME: seems like if os2 table doesn't exist, we could
  # just find the height of the lower-case 'x' glyph?
  (@ttf.os2.exists? && @ttf.os2.x_height) || 0
end

```