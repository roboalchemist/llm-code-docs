# Module: Prawn::Text
  
  
  

  

  
  
  
  
  
      Includes:
      PDF::Core::Text, Formatted
  
  
  

  
  
    Included in:
    Document
  
  

  
  
    Defined in:
    lib/prawn/text.rb,

  lib/prawn/text/box.rb,
 lib/prawn/text/formatted.rb,
 lib/prawn/text/formatted/box.rb,
 lib/prawn/text/formatted/wrap.rb,
 lib/prawn/text/formatted/parser.rb,
 lib/prawn/text/formatted/arranger.rb,
 lib/prawn/text/formatted/fragment.rb,
 lib/prawn/text/formatted/line_wrap.rb

  
  

## Overview

  
    

rubocop: disable Style/Documentation

  

  

## Defined Under Namespace

  
    
      **Modules:** Formatted
    
  
    
      **Classes:** Box
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        NBSP =
          
  
    

No-Break Space

  

  

        
        

```
"\u00A0"

```

      
        ZWSP =
          
  
    

Zero Width Space (indicate word boundaries without a space)

  

  

        
        

```
"\u200B"

```

      
        SHY =
          
  
    

Soft Hyphen (invisible, except when causing a line break)

  

  

        
        

```
"\u00AD"

```

      
    
  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**draw_text**(text, options)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws text on the page, beginning at the point specified by the `:at` option the string is assumed to be pre-formatted to properly fit the page.

  

      
        
- 
  
    
      #**draw_text!**(text, options)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Low level text placement method.

  

      
        
- 
  
    
      #**formatted_text**(array, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws formatted text to the page.

  

      
        
- 
  
    
      #**height_of**(string, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Gets height of text in PDF points.

  

      
        
- 
  
    
      #**height_of_formatted**(array, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Gets height of formatted text in PDF points.

  

      
        
- 
  
    
      #**text**(string, options = {})  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Draws text on the page.

  

      
        
- 
  
    
      #**text_box**(string, options = {})  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Draws the requested text into a box.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Formatted

  

#formatted_text_box

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**draw_text**(text, options)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws text on the page, beginning at the point specified by the `:at` option the string is assumed to be pre-formatted to properly fit the page.

“‘ruby pdf.draw_text “Hello World”, at: [100, 100] pdf.draw_text “Goodbye World”, at: [50,50], size: 16 “`

If your font contains kerning pair data that Prawn can parse, the text will be kerned by default. You can disable kerning by including a `false` `:kerning` option. If you want to disable kerning on an entire document, set ‘default_kerning = false` for that document

#### Text Positioning Details

Prawn will position your text by the left-most edge of its baseline, and flow along a single line. (This means that `:align` will not work)

#### Rotation

Text can be rotated before it is placed on the canvas by specifying the `:rotate` option with a given angle. Rotation occurs counter-clockwise.

#### Encoding

Note that strings passed to this function should be encoded as UTF-8. If you get unexpected characters appearing in your rendered document, check this.

If the current font is a built-in one, although the string must be encoded as UTF-8, only characters that are available in WinAnsi are allowed.

If an empty box is rendered to your PDF instead of the character you wanted it usually means the current font doesn’t include that character.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :at
          (Array(Number, Number))
          
            
          
          
            — 

**Required**. The position at which to start the text.

          
        
      
        
- 
          :kerning
          (Boolean)
          
            
              — default:
              value of default_kerning?
            
          
          
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
          :style
          (Symbol)
          
            
              — default:
              current style
            
          
          
            — 

The style to use. The requested style must be part of the current font family.

          
        
      
        
- 
          :rotate
          (Number)
          
            
          
          
            — 

The angle to which to rotate text.

          
        
      
    

  

Raises:

  
    
- 
      
      
      
      
        
        

If `:at` option is omitted or ‘:align</tt> option is included.

      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text.rb', line 345

def draw_text(text, options)
  options = inspect_options_for_draw_text(options.dup)

  # dup because normalize_encoding changes the string
  text = text.to_s.dup
  save_font do
    process_text_options(options)
    text = font.normalize_encoding(text)
    font_size(options[:size]) { draw_text!(text, options) }
  end
end

```

    
  

    
      
  
### 
  
    #**draw_text!**(text, options)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Low level text placement method.

All font and size alterations should already be set.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :at
          (Array(Number, Number))
          
            
          
          
            — 

The position at which to start the text.

          
        
      
        
- 
          :kerning
          (Boolean)
          
            
          
          
            — 

Whether or not to use kerning (if it is available with the current font).

          
        
      
        
- 
          :size
          (Number)
          
            
          
          
            — 

The font size to use.

          
        
      
        
- 
          :style
          (Symbol)
          
            
          
          
            — 

The style to use. The requested style must be part of the current font family.

          
        
      
        
- 
          :rotate
          (Number)
          
            
          
          
            — 

The angle to which to rotate text.

          
        
      
    

  

  
    
      

```

375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
```

    
    
      

```
# File 'lib/prawn/text.rb', line 375

def draw_text!(text, options)
  unless font.unicode? || font.class.hide_m17n_warning || text.ascii_only?
    warn(
      "PDF's built-in fonts have very limited support for " \
        "internationalized text.\nIf you need full UTF-8 support, " \
        "consider using an external font instead.\n\nTo disable this " \
        "warning, add the following line to your code:\n" \
        "Prawn::Fonts::AFM.hide_m17n_warning = true\n",
    )

    font.class.hide_m17n_warning = true
  end

  x, y = map_to_absolute(options[:at])
  add_text_content(text, x, y, options)
end

```

    
  

    
      
  
### 
  
    #**formatted_text**(array, options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws formatted text to the page.

Formatted text is an array of hashes, where each hash defines text and format information.

  

  
  
    
#### Examples:

    
      
      

```
text([{ :text => "hello" },
      { :text => "world",
        :size => 24,
        :styles => [:bold, :italic] }])

```

    
  

Parameters:

  
    
- 
      
      
      
      
        
        

array of text fragments. See Prawn::Text::Formatted#formatted_text_box for more information on the structure of this array.

      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  
    
- 
      
      
      
      
        
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :inline_format
          (Boolean)
          
            
          
          
            — 

If `true`, then the string parameter is interpreted as a HTML-esque string that recognizes the following tags (assuming the default text formatter is used):

  - 

“Prawn::Text.::.language-html — bold style.

  - 

“Prawn::Text.::.language-html — italic style.

  - 

‘<u></u>`Prawn::Text.::.language-html — underline.

  - 

‘<strikethrough></strikethrough>`Prawn::Text.::.language-html — strikethrough.

  - 

‘<sub></sub>`Prawn::Text.::.language-html — subscript.

  - 

‘<sup></sup>`Prawn::Text.::.language-html — superscript.

  - 

‘<font></font>`Prawn::Text.::.language-html — with the following attributes (using double or single quotes):

    - 

‘name=“Helvetica”`Prawn::Text.::.language-html — the font. The font name must be an AFM font with the desired faces or must be a font that is already registered using Document#font_families.

    - 

‘size=“24”`Prawn::Text.::.language-html — attribute for setting size.

    - 

‘character_spacing=“2.5”`Prawn::Text.::.language-html — character spacing.

  - 

‘<color></color>`Prawn::Text.::.language-html — text color

    - 

‘rgb=“ffffff”`Prawn::Text.::.language-html or `rgb=“#ffffff”`Prawn::Text.::.language-html — RGB color

    - 

‘c=“100” m=“100” y=“100” k=“100”`Prawn::Text.::.language-html — CMYK color

  - 

‘<link></link>`Prawn::Text.::.language-html - link, with the following attributes:

    - 

‘href=“example.com”`Prawn::Text.::.language-html — an external link. Note that you must explicitly underline and color using the appropriate tags if you which to draw attention to the link.

          
        
      
        
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
              current ofnt size
            
          
          
            — 

The font size to use.

          
        
      
        
- 
          :color
          (Color)
          
            
          
          
        
      
        
- 
          :character_spacing
          (Number)
          
            
              — default:
              0
            
          
          
            — 

The amount of space to add to or remove from the default character spacing.

          
        
      
        
- 
          :style
          (Symbol)
          
            
              — default:
              current style
            
          
          
            — 

The style to use. The requested style must be part of the current font family.

          
        
      
        
- 
          :indent_paragraphs
          (Number)
          
            
          
          
            — 

The amount to indent the first line of each paragraph. Omit this option if you do not want indenting.

          
        
      
        
- 
          :direction
          (:ltr, :rtl)
          
            
              — default:
              value of document.text_direction
            
          
          
            — 

Direction of the text.

          
        
      
        
- 
          :fallback_fonts
          (Array<String>)
          
            
          
          
            — 

An array of font names. Each name must be the name of an AFM font or the name that was used to register a family of TTF fonts (see Document#font_families). If present, then each glyph will be rendered using the first font that includes the glyph, starting with the current font and then moving through `:fallback_fonts`.

          
        
      
        
- 
          :valign
          (:top, :center, :bottom)
          
            
              — default:
              :top
            
          
          
            — 

Vertical alignment within the bounding box.

          
        
      
        
- 
          :leading
          (Object)
          
            
              — default:
              Number
            
          
          
            — 

(value of document.default_leading) Additional space between lines.

          
        
      
        
- 
          :final_gap
          (Boolean)
          
            
              — default:
              true
            
          
          
            — 

If `true`, then the space between each line is included below the last line; otherwise, Document#y is placed just below the descender of the last line printed.

          
        
      
        
- 
          :mode
          (Symbol)
          
            
              — default:
              :fill
            
          
          
            — 

The text rendering mode to use. Use this to specify if the text should render with the fill color, stroke color or both.

  - 

`:fill` - fill text (default)

  - 

`:stroke` - stroke text

  - 

`:fill_stroke` - fill, then stroke text

  - 

`:invisible` - invisible text

  - 

`:fill_clip` - fill text then add to path for clipping

  - 

`:stroke_clip` - stroke text then add to path for clipping

  - 

`:fill_stroke_clip` - fill then stroke text, then add to path for clipping

  - 

`:clip` - add text to path for clipping

          
        
      
    

  

Raises:

  
    
- 
      
      
      
      
        
        

if `:at` option included

      
    
  
    
- 
      
      
      
      
        
        

if not wide enough to print any text

      
    
  

  

See Also:
  

    
      
- for a list of valid text rendering modes.
    
  

  
    
      

```

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
281
282
283
284
285
286
287
288
289
290
291
292
```

    
    
      

```
# File 'lib/prawn/text.rb', line 263

def formatted_text(array, options = {})
  options = inspect_options_for_text(options.dup)

  color = options.delete(:color)
  if color
    array =
      array.map { |fragment|
        fragment[:color] ? fragment : fragment.merge(color: color)
      }
  end

  if @indent_paragraphs
    text_formatter.array_paragraphs(array).each do |paragraph|
      remaining_text = draw_indented_formatted_line(paragraph, options)

      if @no_text_printed && !@all_text_printed
        @bounding_box.move_past_bottom
        remaining_text = draw_indented_formatted_line(paragraph, options)
      end

      unless @all_text_printed
        remaining_text = fill_formatted_text_box(remaining_text, options)
        draw_remaining_formatted_text_on_new_pages(remaining_text, options)
      end
    end
  else
    remaining_text = fill_formatted_text_box(array, options)
    draw_remaining_formatted_text_on_new_pages(remaining_text, options)
  end
end

```

    
  

    
      
  
### 
  
    #**height_of**(string, options = {})  ⇒ void 
  

  

  

  
    
  
    **Note:**
    

This method takes the same options as #text, *except* `:indent_paragraphs`.

  

This method returns an undefined value.

Gets height of text in PDF points.

  

  
  
    
#### Examples:

    
      
      

```
text_height = height_of("hello\nworld")

```

    
  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  
    
- 
      
      
      
      
        
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :inline_format
          (Boolean)
          
            
          
          
            — 

If `true`, then the string parameter is interpreted as a HTML-esque string that recognizes the following tags (assuming the default text formatter is used):

  - 

“Prawn::Text.::.language-html — bold style.

  - 

“Prawn::Text.::.language-html — italic style.

  - 

‘<u></u>`Prawn::Text.::.language-html — underline.

  - 

‘<strikethrough></strikethrough>`Prawn::Text.::.language-html — strikethrough.

  - 

‘<sub></sub>`Prawn::Text.::.language-html — subscript.

  - 

‘<sup></sup>`Prawn::Text.::.language-html — superscript.

  - 

‘<font></font>`Prawn::Text.::.language-html — with the following attributes (using double or single quotes):

    - 

‘name=“Helvetica”`Prawn::Text.::.language-html — the font. The font name must be an AFM font with the desired faces or must be a font that is already registered using Document#font_families.

    - 

‘size=“24”`Prawn::Text.::.language-html — attribute for setting size.

    - 

‘character_spacing=“2.5”`Prawn::Text.::.language-html — character spacing.

  - 

‘<color></color>`Prawn::Text.::.language-html — text color

    - 

‘rgb=“ffffff”`Prawn::Text.::.language-html or `rgb=“#ffffff”`Prawn::Text.::.language-html — RGB color

    - 

‘c=“100” m=“100” y=“100” k=“100”`Prawn::Text.::.language-html — CMYK color

  - 

‘<link></link>`Prawn::Text.::.language-html - link, with the following attributes:

    - 

‘href=“example.com”`Prawn::Text.::.language-html — an external link. Note that you must explicitly underline and color using the appropriate tags if you which to draw attention to the link.

          
        
      
        
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
              current ofnt size
            
          
          
            — 

The font size to use.

          
        
      
        
- 
          :color
          (Color)
          
            
          
          
        
      
        
- 
          :character_spacing
          (Number)
          
            
              — default:
              0
            
          
          
            — 

The amount of space to add to or remove from the default character spacing.

          
        
      
        
- 
          :style
          (Symbol)
          
            
              — default:
              current style
            
          
          
            — 

The style to use. The requested style must be part of the current font family.

          
        
      
        
- 
          :direction
          (:ltr, :rtl)
          
            
              — default:
              value of document.text_direction
            
          
          
            — 

Direction of the text.

          
        
      
        
- 
          :fallback_fonts
          (Array<String>)
          
            
          
          
            — 

An array of font names. Each name must be the name of an AFM font or the name that was used to register a family of TTF fonts (see Document#font_families). If present, then each glyph will be rendered using the first font that includes the glyph, starting with the current font and then moving through `:fallback_fonts`.

          
        
      
        
- 
          :valign
          (:top, :center, :bottom)
          
            
              — default:
              :top
            
          
          
            — 

Vertical alignment within the bounding box.

          
        
      
        
- 
          :leading
          (Object)
          
            
              — default:
              Number
            
          
          
            — 

(value of document.default_leading) Additional space between lines.

          
        
      
        
- 
          :final_gap
          (Boolean)
          
            
              — default:
              true
            
          
          
            — 

If `true`, then the space between each line is included below the last line; otherwise, Document#y is placed just below the descender of the last line printed.

          
        
      
        
- 
          :mode
          (Symbol)
          
            
              — default:
              :fill
            
          
          
            — 

The text rendering mode to use. Use this to specify if the text should render with the fill color, stroke color or both.

  - 

`:fill` - fill text (default)

  - 

`:stroke` - stroke text

  - 

`:fill_stroke` - fill, then stroke text

  - 

`:invisible` - invisible text

  - 

`:fill_clip` - fill text then add to path for clipping

  - 

`:stroke_clip` - stroke text then add to path for clipping

  - 

`:fill_stroke_clip` - fill then stroke text, then add to path for clipping

  - 

`:clip` - add text to path for clipping

          
        
      
    

  

Raises:

  
    
- 
      
      
      
      
        
        

if `:at` option included

      
    
  
    
- 
      
      
      
      
        
        

if not wide enough to print any text

      
    
  
    
- 
      
      
      
      
        
        

if `:indent_paragraphs` option included.

      
    
  

  

See Also:
  

    
      
- for a list of valid text rendering modes.
    
      
- #height_of_formatted
    
  

  
    
      

```

480
481
482
```

    
    
      

```
# File 'lib/prawn/text.rb', line 480

def height_of(string, options = {})
  height_of_formatted([{ text: string }], options)
end

```

    
  

    
      
  
### 
  
    #**height_of_formatted**(array, options = {})  ⇒ void 
  

  

  

  
    
  
    **Note:**
    

This method takes the same options as #text, *except* `:indent_paragraphs`.

  

This method returns an undefined value.

Gets height of formatted text in PDF points.

  

  
  
    
#### Examples:

    
      
      

```
height_of_formatted([{ :text => "hello" },
                     { :text => "world",
                       :size => 24,
                       :styles => [:bold, :italic] }])

```

    
  

Parameters:

  
    
- 
      
      
      
      
        
        

text fragments.

      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  
    
- 
      
      
      
      
        
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :inline_format
          (Boolean)
          
            
          
          
            — 

If `true`, then the string parameter is interpreted as a HTML-esque string that recognizes the following tags (assuming the default text formatter is used):

  - 

“Prawn::Text.::.language-html — bold style.

  - 

“Prawn::Text.::.language-html — italic style.

  - 

‘<u></u>`Prawn::Text.::.language-html — underline.

  - 

‘<strikethrough></strikethrough>`Prawn::Text.::.language-html — strikethrough.

  - 

‘<sub></sub>`Prawn::Text.::.language-html — subscript.

  - 

‘<sup></sup>`Prawn::Text.::.language-html — superscript.

  - 

‘<font></font>`Prawn::Text.::.language-html — with the following attributes (using double or single quotes):

    - 

‘name=“Helvetica”`Prawn::Text.::.language-html — the font. The font name must be an AFM font with the desired faces or must be a font that is already registered using Document#font_families.

    - 

‘size=“24”`Prawn::Text.::.language-html — attribute for setting size.

    - 

‘character_spacing=“2.5”`Prawn::Text.::.language-html — character spacing.

  - 

‘<color></color>`Prawn::Text.::.language-html — text color

    - 

‘rgb=“ffffff”`Prawn::Text.::.language-html or `rgb=“#ffffff”`Prawn::Text.::.language-html — RGB color

    - 

‘c=“100” m=“100” y=“100” k=“100”`Prawn::Text.::.language-html — CMYK color

  - 

‘<link></link>`Prawn::Text.::.language-html - link, with the following attributes:

    - 

‘href=“example.com”`Prawn::Text.::.language-html — an external link. Note that you must explicitly underline and color using the appropriate tags if you which to draw attention to the link.

          
        
      
        
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
              current ofnt size
            
          
          
            — 

The font size to use.

          
        
      
        
- 
          :color
          (Color)
          
            
          
          
        
      
        
- 
          :character_spacing
          (Number)
          
            
              — default:
              0
            
          
          
            — 

The amount of space to add to or remove from the default character spacing.

          
        
      
        
- 
          :style
          (Symbol)
          
            
              — default:
              current style
            
          
          
            — 

The style to use. The requested style must be part of the current font family.

          
        
      
        
- 
          :direction
          (:ltr, :rtl)
          
            
              — default:
              value of document.text_direction
            
          
          
            — 

Direction of the text.

          
        
      
        
- 
          :fallback_fonts
          (Array<String>)
          
            
          
          
            — 

An array of font names. Each name must be the name of an AFM font or the name that was used to register a family of TTF fonts (see Document#font_families). If present, then each glyph will be rendered using the first font that includes the glyph, starting with the current font and then moving through `:fallback_fonts`.

          
        
      
        
- 
          :valign
          (:top, :center, :bottom)
          
            
              — default:
              :top
            
          
          
            — 

Vertical alignment within the bounding box.

          
        
      
        
- 
          :leading
          (Object)
          
            
              — default:
              Number
            
          
          
            — 

(value of document.default_leading) Additional space between lines.

          
        
      
        
- 
          :final_gap
          (Boolean)
          
            
              — default:
              true
            
          
          
            — 

If `true`, then the space between each line is included below the last line; otherwise, Document#y is placed just below the descender of the last line printed.

          
        
      
        
- 
          :mode
          (Symbol)
          
            
              — default:
              :fill
            
          
          
            — 

The text rendering mode to use. Use this to specify if the text should render with the fill color, stroke color or both.

  - 

`:fill` - fill text (default)

  - 

`:stroke` - stroke text

  - 

`:fill_stroke` - fill, then stroke text

  - 

`:invisible` - invisible text

  - 

`:fill_clip` - fill text then add to path for clipping

  - 

`:stroke_clip` - stroke text then add to path for clipping

  - 

`:fill_stroke_clip` - fill then stroke text, then add to path for clipping

  - 

`:clip` - add text to path for clipping

          
        
      
    

  

Raises:

  
    
- 
      
      
      
      
        
        

if `:at` option included

      
    
  
    
- 
      
      
      
      
        
        

if not wide enough to print any text

      
    
  
    
- 
      
      
      
      
        
        

if `:indent_paragraphs` option included.

      
    
  

  

See Also:
  

    
      
- for a list of valid text rendering modes.
    
      
- #height_of
    
  

  
    
      

```

575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
```

    
    
      

```
# File 'lib/prawn/text.rb', line 575

def height_of_formatted(array, options = {})
  if options[:indent_paragraphs]
    raise NotImplementedError,
      ':indent_paragraphs option not available with height_of'
  end
  process_final_gap_option(options)
  box = Text::Formatted::Box.new(
    array,
    options.merge(height: 100_000_000, document: self),
  )
  box.render(dry_run: true)

  height = box.height
  height += box.line_gap + box.leading if @final_gap
  height
end

```

    
  

    
      
  
### 
  
    #**text**(string, options = {})  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Draws text on the page.

If you want text to flow onto a new page or between columns, this is the method to use. If, instead, you want to place bounded text outside of the flow of a document (for captions, labels, charts, etc.), use Box or its convenience method #text_box.

Prawn attempts to wrap the text to fit within your current bounding box (or `margin_box` if no bounding box is being used).  Text will flow onto the next page when it reaches the bottom of the bounding box. Text wrap in Prawn does not re-flow line breaks, so if you want fully automated text wrapping, be sure to remove newlines before attempting to draw your string.

#### Examples

“‘ruby pdf.text “Will be wrapped when it hits the edge of your bounding box” pdf.text “This will be centered”, align: :center pdf.text “This will be right aligned”, align: :right pdf.text “This *includes **inline*** <font size=’24’>formatting</font>”, inline_format: true “‘

If your font contains kerning pair data that Prawn can parse, the text will be kerned by default. You can disable kerning by including a `false` `:kerning` option. If you want to disable kerning on an entire document, set ‘default_kerning = false` for that document.

#### Text Positioning Details

The text is positioned at `font.ascender` below the baseline, making it easy to use this method within bounding boxes and spans.

#### Encoding

Note that strings passed to this function should be encoded as UTF-8. If you get unexpected characters appearing in your rendered document, check this.

If the current font is a built-in one, although the string must be encoded as UTF-8, only characters that are available in WinAnsi are allowed.

If an empty box is rendered to your PDF instead of the character you wanted it usually means the current font doesn’t include that character.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  
    
- 
      
      
      
      
        
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :inline_format
          (Boolean)
          
            
          
          
            — 

If `true`, then the string parameter is interpreted as a HTML-esque string that recognizes the following tags (assuming the default text formatter is used):

  - 

“Prawn::Text.::.language-html — bold style.

  - 

“Prawn::Text.::.language-html — italic style.

  - 

‘<u></u>`Prawn::Text.::.language-html — underline.

  - 

‘<strikethrough></strikethrough>`Prawn::Text.::.language-html — strikethrough.

  - 

‘<sub></sub>`Prawn::Text.::.language-html — subscript.

  - 

‘<sup></sup>`Prawn::Text.::.language-html — superscript.

  - 

‘<font></font>`Prawn::Text.::.language-html — with the following attributes (using double or single quotes):

    - 

‘name=“Helvetica”`Prawn::Text.::.language-html — the font. The font name must be an AFM font with the desired faces or must be a font that is already registered using Document#font_families.

    - 

‘size=“24”`Prawn::Text.::.language-html — attribute for setting size.

    - 

‘character_spacing=“2.5”`Prawn::Text.::.language-html — character spacing.

  - 

‘<color></color>`Prawn::Text.::.language-html — text color

    - 

‘rgb=“ffffff”`Prawn::Text.::.language-html or `rgb=“#ffffff”`Prawn::Text.::.language-html — RGB color

    - 

‘c=“100” m=“100” y=“100” k=“100”`Prawn::Text.::.language-html — CMYK color

  - 

‘<link></link>`Prawn::Text.::.language-html - link, with the following attributes:

    - 

‘href=“example.com”`Prawn::Text.::.language-html — an external link. Note that you must explicitly underline and color using the appropriate tags if you which to draw attention to the link.

          
        
      
        
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
              current ofnt size
            
          
          
            — 

The font size to use.

          
        
      
        
- 
          :color
          (Color)
          
            
          
          
        
      
        
- 
          :character_spacing
          (Number)
          
            
              — default:
              0
            
          
          
            — 

The amount of space to add to or remove from the default character spacing.

          
        
      
        
- 
          :style
          (Symbol)
          
            
              — default:
              current style
            
          
          
            — 

The style to use. The requested style must be part of the current font family.

          
        
      
        
- 
          :indent_paragraphs
          (Number)
          
            
          
          
            — 

The amount to indent the first line of each paragraph. Omit this option if you do not want indenting.

          
        
      
        
- 
          :direction
          (:ltr, :rtl)
          
            
              — default:
              value of document.text_direction
            
          
          
            — 

Direction of the text.

          
        
      
        
- 
          :fallback_fonts
          (Array<String>)
          
            
          
          
            — 

An array of font names. Each name must be the name of an AFM font or the name that was used to register a family of TTF fonts (see Document#font_families). If present, then each glyph will be rendered using the first font that includes the glyph, starting with the current font and then moving through `:fallback_fonts`.

          
        
      
        
- 
          :valign
          (:top, :center, :bottom)
          
            
              — default:
              :top
            
          
          
            — 

Vertical alignment within the bounding box.

          
        
      
        
- 
          :leading
          (Object)
          
            
              — default:
              Number
            
          
          
            — 

(value of document.default_leading) Additional space between lines.

          
        
      
        
- 
          :final_gap
          (Boolean)
          
            
              — default:
              true
            
          
          
            — 

If `true`, then the space between each line is included below the last line; otherwise, Document#y is placed just below the descender of the last line printed.

          
        
      
        
- 
          :mode
          (Symbol)
          
            
              — default:
              :fill
            
          
          
            — 

The text rendering mode to use. Use this to specify if the text should render with the fill color, stroke color or both.

  - 

`:fill` - fill text (default)

  - 

`:stroke` - stroke text

  - 

`:fill_stroke` - fill, then stroke text

  - 

`:invisible` - invisible text

  - 

`:fill_clip` - fill text then add to path for clipping

  - 

`:stroke_clip` - stroke text then add to path for clipping

  - 

`:fill_stroke_clip` - fill then stroke text, then add to path for clipping

  - 

`:clip` - add text to path for clipping

          
        
      
    

  

Raises:

  
    
- 
      
      
      
      
        
        

if `:at` option included

      
    
  
    
- 
      
      
      
      
        
        

if not wide enough to print any text

      
    
  

  

See Also:
  

    
      
- for a list of valid text rendering modes.
    
  

  
    
      

```

151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
```

    
    
      

```
# File 'lib/prawn/text.rb', line 151

def text(string, options = {})
  return false if string.nil?

  # we modify the options. don't change the user's hash
  options = options.dup

  p = options[:inline_format]
  if p
    p = [] unless p.is_a?(Array)
    options.delete(:inline_format)
    array = text_formatter.format(string, *p)
  else
    array = [{ text: string }]
  end

  formatted_text(array, options)
end

```

    
  

    
      
  
### 
  
    #**text_box**(string, options = {})  ⇒ String 
  

  

  

  
    

Draws the requested text into a box.

When the text overflows the rectangle, you shrink to fit, or truncate the text. Text boxes are independent of the document y position.

#### Encoding

Note that strings passed to this function should be encoded as UTF-8. If you get unexpected characters appearing in your rendered document, check this.

If the current font is a built-in one, although the string must be encoded as UTF-8, only characters that are available in WinAnsi are allowed.

If an empty box is rendered to your PDF instead of the character you wanted it usually means the current font doesn’t include that character.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  
    
- 
      
      
      
      
        
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
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

          
        
      
    

  

Returns:

  
    
- 
      
      
      
      
        
        

Any text that did not print under the current settings.

      
    
  

Raises:

  
    
- 
      
      
      
      
        
        

If not wide enough to print any text.

      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text/box.rb', line 83

def text_box(string, options = {})
  options = options.dup
  options[:document] = self

  box =
    if options[:inline_format]
      p = options.delete(:inline_format)
      p = [] unless p.is_a?(Array)
      array = text_formatter.format(string, *p)
      Text::Formatted::Box.new(array, options)
    else
      Text::Box.new(string, options)
    end

  box.render
end

```