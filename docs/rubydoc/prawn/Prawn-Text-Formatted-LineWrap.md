# Class: Prawn::Text::Formatted::LineWrap
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Text::Formatted::LineWrap
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/formatted/line_wrap.rb
  
  

## Overview

  
    

Implements individual line wrapping of formatted text.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**space_count**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The number of spaces in the last wrapped line.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**paragraph_finished?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether this line is the last line in the paragraph.

  

      
        
- 
  
    
      #**tokenize**(fragment)  ⇒ Array<String> 
    

    
  
  
  
  
  
  
  
  

  
    

Break the fragment into tokens.

  

      
        
- 
  
    
      #**width**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The width of the last wrapped line.

  

      
        
- 
  
    
      #**wrap_line**(options)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Work in conjunction with the Arranger defined in the `:arranger` option to determine what formatted text will fit within the width defined by the `:width` option.

  

      
    

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**space_count**  ⇒ Integer  (readonly)
  

  

  

  
    

The number of spaces in the last wrapped line.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

19
20
21
```

    
    
      

```
# File 'lib/prawn/text/formatted/line_wrap.rb', line 19

def space_count
  @space_count
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**paragraph_finished?**  ⇒ Boolean 
  

  

  

  
    

Whether this line is the last line in the paragraph.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

24
25
26
```

    
    
      

```
# File 'lib/prawn/text/formatted/line_wrap.rb', line 24

def paragraph_finished?
  @newline_encountered || next_string_newline? || @arranger.finished?
end

```

    
  

    
      
  
### 
  
    #**tokenize**(fragment)  ⇒ Array<String> 
  

  

  

  
    

Break the fragment into tokens.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

32
33
34
```

    
    
      

```
# File 'lib/prawn/text/formatted/line_wrap.rb', line 32

def tokenize(fragment)
  fragment.scan(scan_pattern(fragment.encoding))
end

```

    
  

    
      
  
### 
  
    #**width**  ⇒ Number 
  

  

  

  
    

The width of the last wrapped line.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/prawn/text/formatted/line_wrap.rb', line 13

def width
  @accumulated_width || 0
end

```

    
  

    
      
  
### 
  
    #**wrap_line**(options)  ⇒ String 
  

  

  

  
    

Work in conjunction with the Arranger defined in the `:arranger` option to determine what formatted text will fit within the width defined by the `:width` option.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  

  
    
    
    

Options Hash (options):
    

      
        
- 
          :document
          (Prawn::Document)
          
            
          
          
        
      
        
- 
          :kerning
          (Boolean)
          
            
          
          
        
      
        
- 
          :width
          (Number)
          
            
          
          
        
      
        
- 
          :disable_wrap_by_char
          (Boolean)
          
            
          
          
        
      
        
- 
          :arranger
          (Prawn::Text::Formatted::Arranger)
          
            
          
          
        
      
    

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text/formatted/line_wrap.rb', line 47

def wrap_line(options)
  initialize_line(options)

  # rubocop: disable Lint/AssignmentInCondition
  while fragment = @arranger.next_string
    # rubocop: enable Lint/AssignmentInCondition
    @fragment_output = +''

    fragment.lstrip! if first_fragment_on_this_line?(fragment)
    next if empty_line?(fragment)

    unless apply_font_settings_and_add_fragment_to_line(fragment)
      break
    end
  end
  @arranger.finalize_line
  @accumulated_width = @arranger.line_width
  @space_count = @arranger.space_count
  @arranger.line
end

```