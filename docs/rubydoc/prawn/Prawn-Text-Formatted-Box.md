# Class: Prawn::Text::Formatted::Box
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Text::Formatted::Box
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Wrap
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/formatted/box.rb
  
  

## Overview

  
    

Formatted text box.

Generally, one would use the #formatted_text_box convenience method. However, using `Text::Formatted::Box.new` in conjunction with ‘#render(dry_run: true)` enables one to do calculations prior to placing text on the page, or to determine how much vertical space was consumed by the printed text

  

  

  
## Direct Known Subclasses

  

Box

  
## Experimental API collapse

  

    
      
- 
  
    
      #**ascender**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The height of the ascender of the last line printed.

  

    
      
- 
  
    
      #**at**  ⇒ Array(Number, Number) 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The upper left corner of the text box.

  

    
      
- 
  
    
      #**descender**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The height of the descender of the last line printed.

  

    
      
- 
  
    
      #**leading**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The leading used during printing.

  

    
      
- 
  
    
      #**line_height**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The line height of the last line printed.

  

    
      
- 
  
    
      #**text**  ⇒ Array<Hash> 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The text that was successfully printed (or, if `:dry_run` was used, the text that would have been successfully printed).

  

    
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**available_width**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The width available at this point in the box.

  

      
        
- 
  
    
      #**draw_fragment**(fragment, accumulated_width = 0, line_width = 0, word_spacing = 0)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**everything_printed?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

True if everything printed (or, if `:dry_run` was used, everything would have been successfully printed).

  

      
        
- 
  
    
      #**height**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The height actually used during the previous #render.

  

      
        
- 
  
    
      #**initialize**(formatted_text, options = {})  ⇒ Box 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

See Prawn::Text#text_box for valid options.

  

      
        
- 
  
    
      #**line_gap**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Gap between adjacent lines of text.

  

      
        
- 
  
    
      #**nothing_printed?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

True if nothing printed (or, if `:dry_run` was used, nothing would have been successfully printed).

  

      
        
- 
  
    
      #**render**(flags = {})  ⇒ Array<Hash> 
    

    
  
  
  
  
  
  
  
  

  
    

Render text to the document based on the settings defined in constructor.

  

      
    

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      .**extensions**  ⇒ Array<Module> 
    

    
  
  
  
  
  
  
  
  

  
    

Text box extensions.

  

      
        
- 
  
    
      .**inherited**(base)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**valid_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Wrap

  

#wrap

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(formatted_text, options = {})  ⇒ Box 
  

  

  

  
    

See Prawn::Text#text_box for valid options

  

  

Parameters:

  
    
- 
      
        formatted_text
      
      
        (Array<Hash{Symbol => any}>)
      
      
      
        —
        

Formatted text is an array of hashes, where each hash defines text and format information. The following hash options are supported:

  - 

`:text` — the text to format according to the other hash options.

  - 

`:styles` — an array of styles to apply to this text. Available styles include `:bold`, `:italic`, `:underline`, `:strikethrough`, `:subscript`, and `:superscript`.

  - 

`:size` —a number denoting the font size to apply to this text.

  - 

`:character_spacing` — a number denoting how much to increase or decrease the default spacing between characters.

  - 

`:font` — the name of a font. The name must be an AFM font with the desired faces or must be a font that is already registered using Document#font_families.

  - 

`:color` — anything compatible with Graphics::Color#fill_color and Graphics::Color#stroke_color.

  - 

:link` — a URL to which to create a link. A clickable link will be created to that URL. Note that you must explicitly underline and color using the appropriate tags if you which to draw attention to the link.

  - 

`:anchor` — a destination that has already been or will be registered using ‘PDF::Core::Destinations#add_dest`. A clickable link will be created to that destination. Note that you must explicitly underline and color using the appropriate tags if you which to draw attention to the link.

  - 

`:local` — a file or application to be opened locally. A clickable link will be created to the provided local file or application. If the file is another PDF, it will be opened in a new window. Note that you must explicitly underline and color using the appropriate options if you which to draw attention to the link.

  - 

`:draw_text_callback` — if provided, this Proc will be called instead of Document#draw_text! once per fragment for every low-level addition of text to the page.

  - 

`:callback` — an object (or array of such objects) with two methods: `render_behind` and `render_in_front`, which are called immediately prior to and immediately after rendering the text fragment and which are passed the fragment as an argument.

      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  
    
- 
      
        option
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :document
          (Prawn::Document)
          
            
          
          
            — 

Owning document.

          
        
      
        
- 
          :kerning
          (Boolean)
          
            
              — default:
              value of document.default_kerning?
            
          
          
            — 

Whether or not to use kerning (if it is available with the current font).

          
        
      
        
- 
          :size
          (Number)
          
            
              — default:
              current font size
            
          
          
            — 

The font size to use.

          
        
      
        
- 
          :character_spacing
          (Number)
          
            
              — default:
              0
            
          
          
            — 

The amount of space to add to or remove from the default character spacing.

          
        
      
        
- 
          :disable_wrap_by_char
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Whether or not to prevent mid-word breaks when text does not fit in box.

          
        
      
        
- 
          :mode
          (Symbol)
          
            
              — default:
              :fill
            
          
          
            — 

The text rendering mode. See documentation for Document#text_rendering_mode for a list of valid options.

          
        
      
        
- 
          :width
          (Number)
          
            
              — default:
              bounds.right - at[0]
            
          
          
            — 

The width of the box.

          
        
      
        
- 
          :height
          (Number)
          
            
              — default:
              default_height()
            
          
          
            — 

The height of the box.

          
        
      
        
- 
          :direction
          (:ltr, :rtl)
          
            
              — default:
              value of document.text_direction
            
          
          
            — 

Direction of the text (left-to-right or right-to-left).

          
        
      
        
- 
          :fallback_fonts
          (Array<String>)
          
            
          
          
            — 

An array of font names. Each name must be the name of an AFM font or the name that was used to register a family of external fonts (see Document#font_families). If present, then each glyph will be rendered using the first font that includes the glyph, starting with the current font and then moving through `:fallback_fonts`.

          
        
      
        
- 
          :align
          (:left, :center, :right, :justify)
          
            
              — default:
              :left if direction is :ltr, :right if direction is :rtl
            
          
          
            — 

Alignment within the bounding box.

          
        
      
        
- 
          :valign
          (:top, :center, :bottom)
          
            
              — default:
              :top
            
          
          
            — 

Vertical alignment within the bounding box.

          
        
      
        
- 
          :rotate
          (Number)
          
            
          
          
            — 

The angle to rotate the text.

          
        
      
        
- 
          :rotate_around
          (Object)
          
            
          
          
            — :center, :upper_left, :upper_right, :lower_right, :lower_left

(:upper_left) The point around which to rotate the text.

          
        
      
        
- 
          :leading
          (Number)
          
            
              — default:
              value of document.default_leading
            
          
          
            — 

Additional space between lines.

          
        
      
        
- 
          :single_line
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

If true, then only the first line will be drawn.

          
        
      
        
- 
          :overflow
          (:truncate, :shrink_to_fit, :expand)
          
            
              — default:
              :truncate
            
          
          
            — 

This controls the behavior when the amount of text exceeds the available space.

          
        
      
        
- 
          :min_font_size
          (Number)
          
            
              — default:
              5
            
          
          
            — 

The minimum font size to use when `:overflow` is set to `:shrink_to_fit` (that is the font size will not be reduced to less than this value, even if it means that some text will be cut off).

          
        
      
    

  

  
    
      

```

173
174
175
176
177
178
179
180
181
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
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 173

def initialize(formatted_text, options = {})
  @inked = false
  Prawn.verify_options(valid_options, options)
  options = options.dup

  self.class.extensions.reverse_each { |e| extend(e) }

  @overflow = options[:overflow] || :truncate
  @disable_wrap_by_char = options[:disable_wrap_by_char]

  self.original_text = formatted_text
  @text = nil

  @document = options[:document]
  @direction = options[:direction] || @document.text_direction
  @fallback_fonts = options[:fallback_fonts] ||
    @document.fallback_fonts
  @at = (
    options[:at] || [@document.bounds.left, @document.bounds.top]
  ).dup
  @width = options[:width] ||
    (@document.bounds.right - @at[0])
  @height = options[:height] || default_height
  @align = options[:align] ||
    (@direction == :rtl ? :right : :left)
  @vertical_align = options[:valign] || :top
  @leading = options[:leading] || @document.default_leading
  @character_spacing = options[:character_spacing] ||
    @document.character_spacing
  @mode = options[:mode] || @document.text_rendering_mode
  @rotate = options[:rotate] || 0
  @rotate_around = options[:rotate_around] || :upper_left
  @single_line = options[:single_line]
  @draw_text_callback = options[:draw_text_callback]

  # if the text rendering mode is :unknown, force it back to :fill
  if @mode == :unknown
    @mode = :fill
  end

  if @overflow == :expand
    # if set to expand, then we simply set the bottom
    # as the bottom of the document bounds, since that
    # is the maximum we should expand to
    @height = default_height
    @overflow = :truncate
  end
  @min_font_size = options[:min_font_size] || 5
  if options[:kerning].nil?
    options[:kerning] = @document.default_kerning?
  end
  @options = {
    kerning: options[:kerning],
    size: options[:size],
    style: options[:style],
  }

  super(formatted_text, options)
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**ascender**  ⇒ Number  (readonly)
  

  

  

  
    

The height of the ascender of the last line printed.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 56

def ascender
  @ascender
end

```

    
  

    
      
      
      
  
### 
  
    #**at**  ⇒ Array(Number, Number)  (readonly)
  

  

  

  
    

The upper left corner of the text box.

  

  

Returns:

  
    
- 
      
      
        (Array(Number, Number))
      
      
      
    
  

  
    
      

```

48
49
50
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 48

def at
  @at
end

```

    
  

    
      
      
      
  
### 
  
    #**descender**  ⇒ Number  (readonly)
  

  

  

  
    

The height of the descender of the last line printed.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 60

def descender
  @descender
end

```

    
  

    
      
      
      
  
### 
  
    #**leading**  ⇒ Number  (readonly)
  

  

  

  
    

The leading used during printing.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

64
65
66
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 64

def leading
  @leading
end

```

    
  

    
      
      
      
  
### 
  
    #**line_height**  ⇒ Number  (readonly)
  

  

  

  
    

The line height of the last line printed.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

52
53
54
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 52

def line_height
  @line_height
end

```

    
  

    
      
      
      
  
### 
  
    #**text**  ⇒ Array<Hash>  (readonly)
  

  

  

  
    

The text that was successfully printed (or, if `:dry_run` was used, the text that would have been successfully printed).

  

  

Returns:

  
    
- 
      
      
        (Array<Hash>)
      
      
      
    
  

  
    
      

```

28
29
30
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 28

def text
  @text
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**extensions**  ⇒ Array<Module> 
  

  

  

  
    

Text box extensions.

Example:

“‘ruby module MyWrap

```
def wrap(array)
  initialize_wrap([{ text: 'all your base are belong to us' }])
  @line_wrap.wrap_line(
    document: @document,
    kerning: @kerning,
    width: 10000,
    arranger: @arranger
  )
  fragment = @arranger.retrieve_fragment
  format_and_draw_fragment(fragment, 0, @line_wrap.width, 0)
  []
end

```

end

Prawn::Text::Formatted::Box.extensions << MyWrap

box = Prawn::Text::Formatted::Box.new(‘hello world’) box.render(“why can’t I print anything other than” +

```
'"all your base are belong to us"?')

```

“‘

See Wrap for what is required of the wrap method if you want to override the default wrapping algorithm.

  

  

Returns:

  
    
- 
      
      
        (Array<Module>)
      
      
      
    
  

  
    
      

```

391
392
393
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 391

def self.extensions
  @extensions ||= []
end

```

    
  

    
      
  
### 
  
    .**inherited**(base)  ⇒ Object 
  

  

  

  
    
      

```

396
397
398
399
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 396

def self.inherited(base)
  super
  extensions.each { |e| base.extensions << e }
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**available_width**  ⇒ Number 
  

  

  

  
    

The width available at this point in the box.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

285
286
287
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 285

def available_width
  @width
end

```

    
  

    
      
  
### 
  
    #**draw_fragment**(fragment, accumulated_width = 0, line_width = 0, word_spacing = 0)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
        fragment
      
      
        (Prawn::Text::Formatted::Fragment)
      
      
      
    
  
    
- 
      
        accumulated_width
      
      
        (Number)
      
      
        *(defaults to: 0)*
      
      
    
  
    
- 
      
        line_width
      
      
        (Number)
      
      
        *(defaults to: 0)*
      
      
    
  
    
- 
      
        word_spacing
      
      
        (Number)
      
      
        *(defaults to: 0)*
      
      
    
  

  
    
      

```

304
305
306
307
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
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 304

def draw_fragment(
  fragment, accumulated_width = 0, line_width = 0, word_spacing = 0
)
  case @align
  when :left
    x = @at[0]
  when :center
    x = @at[0] + (@width * 0.5) - (line_width * 0.5)
  when :right
    x = @at[0] + @width - line_width
  when :justify
    x =
      if @direction == :ltr
        @at[0]
      else
        @at[0] + @width - line_width
      end
  else
    raise ArgumentError,
      'align must be one of :left, :right, :center or :justify symbols'
  end

  x += accumulated_width

  y = @at[1] + @baseline_y

  y += fragment.y_offset

  fragment.left = x
  fragment.baseline = y

  if @inked
    draw_fragment_underlays(fragment)

    @document.word_spacing(word_spacing) do
      if @draw_text_callback
        @draw_text_callback.call(
          fragment.text,
          at: [x, y],
          kerning: @kerning,
        )
      else
        @document.draw_text!(
          fragment.text,
          at: [x, y],
          kerning: @kerning,
        )
      end
    end

    draw_fragment_overlays(fragment)
  end
end

```

    
  

    
      
  
### 
  
    #**everything_printed?**  ⇒ Boolean 
  

  

  

  
    

True if everything printed (or, if `:dry_run` was used, everything would have been successfully printed).

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 42

def everything_printed?
  @everything_printed
end

```

    
  

    
      
  
### 
  
    #**height**  ⇒ Number 
  

  

  

  
    

The height actually used during the previous #render.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

292
293
294
295
296
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 292

def height
  return 0 if @baseline_y.nil? || @descender.nil?

  (@baseline_y - @descender).abs
end

```

    
  

    
      
  
### 
  
    #**line_gap**  ⇒ Number 
  

  

  

  
    

Gap between adjacent lines of text.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 69

def line_gap
  line_height - (ascender + descender)
end

```

    
  

    
      
  
### 
  
    #**nothing_printed?**  ⇒ Boolean 
  

  

  

  
    

True if nothing printed (or, if `:dry_run` was used, nothing would have been successfully printed).

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

34
35
36
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 34

def nothing_printed?
  @nothing_printed
end

```

    
  

    
      
  
### 
  
    #**render**(flags = {})  ⇒ Array<Hash> 
  

  

  

  
    

Render text to the document based on the settings defined in constructor.

In order to facilitate look-ahead calculations, this method accepts a ‘dry_run: true` option. If provided, then everything is executed as if rendering, with the exception that nothing is drawn on the page. Useful for look-ahead computations of height, unprinted text, etc.

  

  

Parameters:

  
    
- 
      
        flags
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    

Options Hash (flags):
    

      
        
- 
          :dry_run
          (Boolean)
          
            
              — default:
              false
            
          
          
            — 

Do not draw the text. Everything else is done.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Array<Hash>)
      
      
      
        —
        

A formatted text array representing any text that did not print under the current settings.

      
    
  

Raises:

  
    
- 
      
      
        (Prawn::Text::Formatted::Arranger::BadFontFamily)
      
      
      
        —
        

If no font family is defined for the current font.

      
    
  
    
- 
      
      
        (Prawn::Errors::CannotFit)
      
      
      
        —
        

If not wide enough to print any text.

      
    
  

  
    
      

```

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
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 251

def render(flags = {})
  unprinted_text = []

  @document.save_font do
    @document.character_spacing(@character_spacing) do
      @document.text_rendering_mode(@mode) do
        process_options

        text = normalized_text(flags)

        @document.font_size(@font_size) do
          shrink_to_fit(text) if @overflow == :shrink_to_fit
          process_vertical_alignment(text)
          @inked = true unless flags[:dry_run]
          unprinted_text =
            if @rotate != 0 && @inked
              render_rotated(text)
            else
              wrap(text)
            end
          @inked = false
        end
      end
    end
  end

  unprinted_text.map do |e|
    e.merge(text: @document.font.to_utf8(e[:text]))
  end
end

```

    
  

    
      
  
### 
  
    #**valid_options**  ⇒ Object 
  

  

  

  
    
      

```

402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
```

    
    
      

```
# File 'lib/prawn/text/formatted/box.rb', line 402

def valid_options
  PDF::Core::Text::VALID_OPTIONS + i[
    at
    height width
    align valign
    rotate rotate_around
    overflow min_font_size
    disable_wrap_by_char
    leading character_spacing
    mode single_line
    document
    direction
    fallback_fonts
    draw_text_callback
  ]
end

```