# Class: Prawn::Font
  Abstract
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Font
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/font.rb
  
  

## Overview

  
    
  **This class is abstract.**
  

Provides font information and helper functions.

  

  

  
## Direct Known Subclasses

  

Prawn::Fonts::AFM, Prawn::Fonts::TTF

  
    
## 
      Experimental API
      collapse
    

    
      
        AFM =
          
  
    **Deprecated.** 

  

  

        
        

```
Prawn::Fonts::AFM
```

      
        TTF =
          
  
    **Deprecated.** 

  

  

        
        

```
Fonts::TTF
```

      
        DFont =
          
  
    **Deprecated.** 

  

  

        
        

```
Fonts::DFont
```

      
        TTC =
          
  
    **Deprecated.** 

  

  

        
        

```
Fonts::TTC
```

      
    
  

  
## Experimental API collapse

  

    
      
- 
  
    
      #**family**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The font family.

  

    
      
- 
  
    
      #**name**  ⇒ String 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The font name.

  

    
      
- 
  
    
      #**options**  ⇒ Hash 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The options hash used to initialize the font.

  

    
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      .**font_format**(src, options)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Guesses font format.

  

      
        
- 
  
    
      .**load**(document, src, options = {})  ⇒ Prawn::Fonts::Font 
    

    
  
  
  
  
  
  
  
  

  
    

Shortcut interface for constructing a font object.

  

      
        
- 
  
    
      #**add_to_current_page**(subset)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Registers the given subset of the current font with the current PDF page.

  

      
        
- 
  
    
      #**ascender**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The size of the font ascender in PDF points.

  

      
        
- 
  
    
      #**descender**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The size of the font descender in PDF points.

  

      
        
- 
  
    
      #**eql?**(other)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Compliments the #hash implementation.

  

      
        
- 
  
    
      #**hash**  ⇒ Integer 
    

    
  
  
  
  
  
  
  
  

  
    

Return a hash (as in ‘Object#hash`) for the font.

  

      
        
- 
  
    
      #**height**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Gets height of current font in PDF points at current font size.

  

      
        
- 
  
    
      #**height_at**(size)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Gets height of font in PDF points at the given font size.

  

      
        
- 
  
    
      #**identifier_for**(subset)  ⇒ Symbol 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(document, name, options = {})  ⇒ Font 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Font.

  

      
        
- 
  
    
      #**inspect**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Returns a string containing a human-readable representation of this font.

  

      
        
- 
  
    
      #**line_gap**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The size of the recommended gap between lines of text in PDF points.

  

      
        
- 
  
    
      #**normalize_encoding**(string)  ⇒ String 
    

    
  
  
  
  
  
  abstract
  
  

  
    

Normalizes the encoding of the string to an encoding supported by the font.

  

      
        
- 
  
    
      #**normalize_encoding!**(str)  ⇒ String 
    

    
  
  
  
  
  
  
  deprecated
  

  
    **Deprecated.** 
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, name, options = {})  ⇒ Font 
  

  

  

  
    

Returns a new instance of Font.

  

  

Parameters:

  
    
- 
      
        document
      
      
        (Prawn::Document)
      
      
      
    
  
    
- 
      
        name
      
      
        (String)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :family
          (String)
          
            
          
          
        
      
        
- 
          :subset
          (Boolean)
          
            
              — default:
              true
            
          
          
        
      
    

  

  
    
      

```

412
413
414
415
416
417
418
419
420
421
422
423
424
425
```

    
    
      

```
# File 'lib/prawn/font.rb', line 412

def initialize(document, name, options = {})
  @document = document
  @name = name
  @options = options

  @family = options[:family]

  @identifier = generate_unique_id

  @references = {}
  @subset_name_cache = {}

  @full_font_embedding = options.key?(:subset) && !options[:subset]
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**family**  ⇒ String  (readonly)
  

  

  

  
    

The font family.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

359
360
361
```

    
    
      

```
# File 'lib/prawn/font.rb', line 359

def family
  @family
end
```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ String  (readonly)
  

  

  

  
    

The font name.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

355
356
357
```

    
    
      

```
# File 'lib/prawn/font.rb', line 355

def name
  @name
end
```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Hash  (readonly)
  

  

  

  
    

The options hash used to initialize the font.

  

  

Returns:

  
    
- 
      
      
        (Hash)
      
      
      
    
  

  
    
      

```

363
364
365
```

    
    
      

```
# File 'lib/prawn/font.rb', line 363

def options
  @options
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**font_format**(src, options)  ⇒ String 
  

  

  

  
    

Guesses font format.

  

  

Parameters:

  
    
- 
      
        src
      
      
        (String, IO)
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :format
          (String)
          
            
          
          
        
      
    

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

394
395
396
397
398
399
400
401
402
403
404
```

    
    
      

```
# File 'lib/prawn/font.rb', line 394

def self.font_format(src, options)
  return options.fetch(:format, 'ttf') if src.respond_to?(:read)

  case src.to_s
  when /\.ttf$/i then 'ttf'
  when /\.otf$/i then 'otf'
  when /\.dfont$/i then 'dfont'
  when /\.ttc$/i then 'ttc'
  else 'afm'
  end
end
```

    
  

    
      
  
### 
  
    .**load**(document, src, options = {})  ⇒ Prawn::Fonts::Font 
  

  

  

  
    

Shortcut interface for constructing a font object. Filenames of the form ‘*.ttf` will call TTF.new, `*.otf` calls OTF.new, `*.dfont` calls DFont.new, `*.ttc` goes to TTC.new, and anything else will be passed through to AFM.new.

  

  

Parameters:

  
    
- 
      
        document
      
      
        (Prawn::Document)
      
      
      
        —
        

owning document

      
    
  
    
- 
      
        src
      
      
        (String)
      
      
      
        —
        

font file path

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :family
          (String)
          
            
          
          
        
      
        
- 
          :style
          (Symbol)
          
            
          
          
        
      
    

  

Returns:

  
    
- 
      
      
        (Prawn::Fonts::Font)
      
      
      
    
  

  
    
      

```

377
378
379
380
381
382
383
384
385
```

    
    
      

```
# File 'lib/prawn/font.rb', line 377

def self.load(document, src, options = {})
  case font_format(src, options)
  when 'ttf' then TTF.new(document, src, options)
  when 'otf' then Fonts::OTF.new(document, src, options)
  when 'dfont' then DFont.new(document, src, options)
  when 'ttc' then TTC.new(document, src, options)
  else AFM.new(document, src, options)
  end
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_to_current_page**(subset)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Registers the given subset of the current font with the current PDF page. This is safe to call multiple times for a given font and subset, as it will only add the font the first time it is called.

  

  

Parameters:

  
    
- 
      
        subset
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

496
497
498
499
```

    
    
      

```
# File 'lib/prawn/font.rb', line 496

def add_to_current_page(subset)
  @references[subset] ||= register(subset)
  @document.state.page.fonts[identifier_for(subset)] = @references[subset]
end
```

    
  

    
      
  
### 
  
    #**ascender**  ⇒ Number 
  

  

  

  
    

The size of the font ascender in PDF points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

430
431
432
```

    
    
      

```
# File 'lib/prawn/font.rb', line 430

def ascender
  @ascender / 1000.0 * size
end
```

    
  

    
      
  
### 
  
    #**descender**  ⇒ Number 
  

  

  

  
    

The size of the font descender in PDF points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

437
438
439
```

    
    
      

```
# File 'lib/prawn/font.rb', line 437

def descender
  -@descender / 1000.0 * size
end
```

    
  

    
      
  
### 
  
    #**eql?**(other)  ⇒ Boolean 
  

  

  

  
    

Compliments the #hash implementation.

  

  

Parameters:

  
    
- 
      
        other
      
      
        (Object)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

532
533
534
535
```

    
    
      

```
# File 'lib/prawn/font.rb', line 532

def eql?(other)
  self.class == other.class && name == other.name &&
    family == other.family && size == other.size
end
```

    
  

    
      
  
### 
  
    #**hash**  ⇒ Integer 
  

  

  

  
    

Return a hash (as in ‘Object#hash`) for the font. This is required since font objects are used as keys in hashes that cache certain values.

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

524
525
526
```

    
    
      

```
# File 'lib/prawn/font.rb', line 524

def hash
  [self.class, name, family].hash
end
```

    
  

    
      
  
### 
  
    #**height**  ⇒ Number 
  

  

  

  
    

Gets height of current font in PDF points at current font size.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

486
487
488
```

    
    
      

```
# File 'lib/prawn/font.rb', line 486

def height
  height_at(size)
end
```

    
  

    
      
  
### 
  
    #**height_at**(size)  ⇒ Number 
  

  

  

  
    

Gets height of font in PDF points at the given font size.

  

  

Parameters:

  
    
- 
      
        size
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

478
479
480
481
```

    
    
      

```
# File 'lib/prawn/font.rb', line 478

def height_at(size)
  @normalized_height ||= (@ascender - @descender + @line_gap) / 1000.0
  @normalized_height * size
end
```

    
  

    
      
  
### 
  
    #**identifier_for**(subset)  ⇒ Symbol 
  

  

  

  
    

  

  

Parameters:

  
    
- 
      
        subset
      
      
        (Integer)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
    
  

  
    
      

```

504
505
506
507
508
509
510
511
```

    
    
      

```
# File 'lib/prawn/font.rb', line 504

def identifier_for(subset)
  @subset_name_cache[subset] ||=
    if full_font_embedding
      @identifier.to_sym
    else
      :"#{@identifier}.#{subset}"
    end
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ String 
  

  

  

  
    

Returns a string containing a human-readable representation of this font.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

516
517
518
```

    
    
      

```
# File 'lib/prawn/font.rb', line 516

def inspect
  "#{self.class.name}< #{name}: #{size} >"
end
```

    
  

    
      
  
### 
  
    #**line_gap**  ⇒ Number 
  

  

  

  
    

The size of the recommended gap between lines of text in PDF points

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

444
445
446
```

    
    
      

```
# File 'lib/prawn/font.rb', line 444

def line_gap
  @line_gap / 1000.0 * size
end
```

    
  

    
      
  
### 
  
    #**normalize_encoding**(string)  ⇒ String 
  

  

  

  
    
  **This method is abstract.**
  

Normalizes the encoding of the string to an encoding supported by the font. The string is expected to be UTF-8 going in. It will be re-encoded and the new string will be returned.

  

  

Parameters:

  
    
- 
      
        string
      
      
        (String)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

Raises:

  
    
- 
      
      
        (NotImplementedError)
      
      
      
    
  

  
    
      

```

456
457
458
459
```

    
    
      

```
# File 'lib/prawn/font.rb', line 456

def normalize_encoding(_string)
  raise NotImplementedError,
    'subclasses of Prawn::Font must implement #normalize_encoding'
end
```

    
  

    
      
  
### 
  
    #**normalize_encoding!**(str)  ⇒ String 
  

  

  

  
    **Deprecated.** 

  
    **Note:**
    

This method doesn’t mutate its argument any more.

  

Destructive version of #normalize_encoding; normalizes the encoding of a string in place.

  

  

Parameters:

  
    
- 
      
        str
      
      
        (String)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

469
470
471
472
```

    
    
      

```
# File 'lib/prawn/font.rb', line 469

def normalize_encoding!(str)
  warn('Font#normalize_encoding! is deprecated. Please use non-mutating version Font#normalize_encoding instead.')
  str.dup.replace(normalize_encoding(str))
end
```