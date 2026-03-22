# Class: Kramdown::Utils::StringScanner
  
  
  

  
  
    Inherits:
    
      StringScanner
      
        

          
- Object
          
            
- StringScanner
          
            
- Kramdown::Utils::StringScanner
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/utils/string_scanner.rb
  
  

## Overview

  
    

This patched StringScanner adds line number information for current scan position and a start_line_number override for nested StringScanners.

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**start_line_number**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The start line number.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**current_line_number**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the line number for current charpos.

  

      
        
- 
  
    
      #**initialize**(string, start_line_number = 1)  ⇒ StringScanner 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Takes the start line number as optional second argument.

  

      
        
- 
  
    
      #**pos=**(pos)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Sets the byte position of the scan pointer.

  

      
        
- 
  
    
      #**revert_pos**(data)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Revert the position to one saved by #save_pos.

  

      
        
- 
  
    
      #**save_pos**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return information needed to revert the byte position of the string scanner in a performant way.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(string, start_line_number = 1)  ⇒ StringScanner 
  

  

  

  
    

Takes the start line number as optional second argument.

Note: The original second argument is no longer used so this should be safe.

  

  

  
    
      

```

26
27
28
29
30
31
```

    
    
      

```
# File 'lib/kramdown/utils/string_scanner.rb', line 26

def initialize(string, start_line_number = 1)
  super(string)
  @start_line_number = start_line_number || 1
  @previous_pos = 0
  @previous_line_number = @start_line_number
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**start_line_number**  ⇒ Object  (readonly)
  

  

  

  
    

The start line number. Used for nested StringScanners that scan a sub-string of the source document. The kramdown parser uses this, e.g., for span level parsers.

  

  

  
    
      

```

21
22
23
```

    
    
      

```
# File 'lib/kramdown/utils/string_scanner.rb', line 21

def start_line_number
  @start_line_number
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**current_line_number**  ⇒ Object 
  

  

  

  
    

Returns the line number for current charpos.

NOTE: Requires that all line endings are normalized to ‘n’

NOTE: Normally we’d have to add one to the count of newlines to get the correct line number. However we add the one indirectly by using a one-based start_line_number.

  

  

  
    
      

```

67
68
69
70
71
72
73
74
75
76
```

    
    
      

```
# File 'lib/kramdown/utils/string_scanner.rb', line 67

def current_line_number
  # Not using string[@previous_pos..best_pos].count('\n') because it is slower
  strscan = ::StringScanner.new(string)
  strscan.pos = @previous_pos
  old_pos = pos + 1
  @previous_line_number += 1 while strscan.skip_until(/\n/) && strscan.pos <= old_pos

  @previous_pos = (eos? ? pos : pos + 1)
  @previous_line_number
end

```

    
  

    
      
  
### 
  
    #**pos=**(pos)  ⇒ Object 
  

  

  

  
    

Sets the byte position of the scan pointer.

Note: This also resets some internal variables, so always use pos= when setting the position and don’t use any other method for that!

  

  

  
    
      

```

37
38
39
40
41
42
43
```

    
    
      

```
# File 'lib/kramdown/utils/string_scanner.rb', line 37

def pos=(pos)
  if self.pos > pos
    @previous_line_number = @start_line_number
    @previous_pos = 0
  end
  super
end

```

    
  

    
      
  
### 
  
    #**revert_pos**(data)  ⇒ Object 
  

  

  

  
    

Revert the position to one saved by #save_pos.

  

  

  
    
      

```

56
57
58
59
```

    
    
      

```
# File 'lib/kramdown/utils/string_scanner.rb', line 56

def revert_pos(data)
  self.pos = data[0]
  @previous_pos, @previous_line_number = data[1], data[2]
end

```

    
  

    
      
  
### 
  
    #**save_pos**  ⇒ Object 
  

  

  

  
    

Return information needed to revert the byte position of the string scanner in a performant way.

The returned data can be fed to #revert_pos to revert the position to the saved one.

Note: Just saving #pos won’t be enough.

  

  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/kramdown/utils/string_scanner.rb', line 51

def save_pos
  [pos, @previous_pos, @previous_line_number]
end

```