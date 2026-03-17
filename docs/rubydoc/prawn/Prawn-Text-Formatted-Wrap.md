# Module: Prawn::Text::Formatted::Wrap
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Box
  
  

  
  
    Defined in:
    lib/prawn/text/formatted/wrap.rb
  
  

## Overview

  
    

Handles text wrapping for for formatted text.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(_array, options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrap**(array)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See the developer documentation for PDF::Core::Text#wrap.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**initialize**(_array, options)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
18
19
20
```

    
    
      

```
# File 'lib/prawn/text/formatted/wrap.rb', line 13

def initialize(_array, options)
  @line_wrap = Prawn::Text::Formatted::LineWrap.new
  @arranger = Prawn::Text::Formatted::Arranger.new(
    @document,
    kerning: options[:kerning],
  )
  @disable_wrap_by_char = options[:disable_wrap_by_char]
end

```

    
  

    
      
  
### 
  
    #**wrap**(array)  ⇒ Object 
  

  

  

  
    

See the developer documentation for PDF::Core::Text#wrap

Formatted#wrap should set the following variables:

```
<tt>@line_height</tt>::
     the height of the tallest fragment in the last printed line
<tt>@descender</tt>::
     the descender height of the tallest fragment in the last
     printed line
<tt>@ascender</tt>::
     the ascender heigth of the tallest fragment in the last
     printed line
<tt>@baseline_y</tt>::
    the baseline of the current line
<tt>@nothing_printed</tt>::
    set to true until something is printed, then false
<tt>@everything_printed</tt>::
    set to false until everything printed, then true

```

Returns any formatted text that was not printed

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/text/formatted/wrap.rb', line 42

def wrap(array)
  initialize_wrap(array)

  stop = false
  until stop
    # wrap before testing if enough height for this line because the
    # height of the highest fragment on this line will be used to
    # determine the line height
    @line_wrap.wrap_line(
      document: @document,
      kerning: @kerning,
      width: available_width,
      arranger: @arranger,
      disable_wrap_by_char: @disable_wrap_by_char,
    )

    if enough_height_for_this_line?
      move_baseline_down
      print_line
    else
      stop = true
    end

    stop ||= @single_line || @arranger.finished?
  end
  @text = @printed_lines.join("\n")
  @everything_printed = @arranger.finished?
  @arranger.unconsumed
end

```