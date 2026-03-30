# Class: RuboCop::Cop::AlignmentCorrector
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::AlignmentCorrector

        show all
      
    
  
  

  
  
  
      Extended by:
      Alignment, RangeHelp
  
    Defined in:
    lib/rubocop/cop/correctors/alignment_corrector.rb
  
## Overview

This class does autocorrection of nodes that should just be moved to the left or to the right, amount being determined by the instance variable column_delta.

## Constant Summary

### Constants included

     from RangeHelp

RangeHelp::BYTE_ORDER_MARK, RangeHelp::NOT_GIVEN

### Constants included

     from Alignment

RuboCop::Cop::Alignment::SPACE

## Class Attribute Summary collapse

-
  
      .**processed_source**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute processed_source.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**align_end**(corrector, processed_source, node, align_to)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      .**correct**(corrector, processed_source, node, column_delta)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
    
## Class Attribute Details

###
  
    .**processed_source**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute processed_source.

```

13
14
15
```

```
# File 'lib/rubocop/cop/correctors/alignment_corrector.rb', line 13

def processed_source
  @processed_source
end

```

## Class Method Details

###
  
    .**align_end**(corrector, processed_source, node, align_to)  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/rubocop/cop/correctors/alignment_corrector.rb', line 32

def align_end(corrector, processed_source, node, align_to)
  @processed_source = processed_source
  whitespace = whitespace_range(node)
  column = alignment_column(align_to)
  indentation = indentation_string(column)

  if whitespace.source.strip.empty?
    corrector.replace(whitespace, indentation)
  else
    corrector.insert_after(whitespace, "\n#{indentation}")
  end
end

```

###
  
    .**correct**(corrector, processed_source, node, column_delta)  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
```

```
# File 'lib/rubocop/cop/correctors/alignment_corrector.rb', line 15

def correct(corrector, processed_source, node, column_delta)
  return unless node

  @processed_source = processed_source
  # Disable autocorrection for tabs as it requires special handling
  return if using_tabs?

  expr = node.respond_to?(:loc) ? node.source_range : node
  return if block_comment_within?(expr)

  taboo_ranges = inside_string_ranges(node)

  each_line(expr) do |line_begin_pos|
    autocorrect_line(corrector, line_begin_pos, expr, column_delta, taboo_ranges)
  end
end

```
