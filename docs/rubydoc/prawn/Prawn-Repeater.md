# Class: Prawn::Repeater
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Repeater
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/repeater.rb
  
  

## Overview

  
    

Repeater object.

  

  

  
## Experimental API collapse

  

    
      
- 
  
    
      .**count**  ⇒ Integer 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Repeater counter.

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**initialize**(document, page_filter, dynamic = false, &block)  ⇒ Repeater 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Repeater.

  

      
        
- 
  
    
      #**match?**(page_number)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Should this repeater run on this page?.

  

      
        
- 
  
    
      #**run**(page_number)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Run repeater.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, page_filter, dynamic = false, &block)  ⇒ Repeater 
  

  

  

  
    

Returns a new instance of Repeater.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/prawn/repeater.rb', line 105

def initialize(document, page_filter, dynamic = false, &block)
  @document = document
  @page_filter = page_filter
  @dynamic = dynamic
  @stamp_name = "prawn_repeater(#{Repeater.count})"
  @document.create_stamp(@stamp_name, &block) unless dynamic
  @block = block if dynamic
  @graphic_state = document.state.page.graphic_state.dup

  Repeater.count += 1
end

```

    
  

  

  
    
## Class Attribute Details

    
      
      
      
  
### 
  
    .**count**  ⇒ Integer 
  

  

  

  
    

Repeater counter.

It’s not an exact number of repeaters but a counter used to generate unique repeater stamp names.

  

  

Returns:

  
    
- 
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

98
99
100
```

    
    
      

```
# File 'lib/prawn/repeater.rb', line 98

def count
  @count ||= 0
end

```

    
  

    
  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

103
104
105
```

    
    
      

```
# File 'lib/prawn/repeater.rb', line 103

def name
  @name
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**match?**(page_number)  ⇒ Boolean 
  

  

  

  
    

Should this repeater run on this page?

  

  

Parameters:

  
    
- 
      
        page_number
      
      
        (Integer)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

121
122
123
```

    
    
      

```
# File 'lib/prawn/repeater.rb', line 121

def match?(page_number)
  @document.page_match?(@page_filter, page_number)
end

```

    
  

    
      
  
### 
  
    #**run**(page_number)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Run repeater.

  

  

Parameters:

  
    
- 
      
        page_number
      
      
        (Integer)
      
      
      
    
  

  
    
      

```

129
130
131
132
133
134
135
136
137
138
```

    
    
      

```
# File 'lib/prawn/repeater.rb', line 129

def run(page_number)
  if !@dynamic
    @document.stamp(@stamp_name) if match?(page_number)
  elsif @block && match?(page_number)
    @document.save_graphics_state(@graphic_state) do
      @document.__send__(:freeze_stamp_graphics)
      @block.call
    end
  end
end

```