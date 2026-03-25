# Class: Prawn::Document::ColumnBox
  
  
  

  
  
    Inherits:
    
      BoundingBox
      
        

          
- Object
          
            
- BoundingBox
          
            
- Prawn::Document::ColumnBox
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/document/column_box.rb
  
  

## Overview

  
    

Implements the necessary functionality to allow #column_box to work.

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from BoundingBox

  

#document, #parent, #total_left_padding, #total_right_padding

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**add_left_padding**(left_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**add_right_padding**(right_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**bare_column_width**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The column width, not the width of the whole box, before left and/or right padding.

  

      
        
- 
  
    
      #**initialize**(document, parent, point, options = {})  ⇒ ColumnBox 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ColumnBox.

  

      
        
- 
  
    
      #**left**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Relative position of the left edge of the current column.

  

      
        
- 
  
    
      #**left_side**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

x coordinate of the left edge of the current column.

  

      
        
- 
  
    
      #**move_past_bottom**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Moves to the next column or starts a new page if currently positioned at the rightmost column.

  

      
        
- 
  
    
      #**right**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Relative position of the right edge of the current column.

  

      
        
- 
  
    
      #**right_side**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

x coordinate of the right edge of the current column.

  

      
        
- 
  
    
      #**subtract_left_padding**(left_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**subtract_right_padding**(right_padding)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**width**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

The column width after padding.

  

      
        
- 
  
    
      #**width_of_column**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Column width including the spacer.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from BoundingBox

  

#absolute_bottom, #absolute_bottom_left, #absolute_bottom_right, #absolute_left, #absolute_right, #absolute_top, #absolute_top_left, #absolute_top_right, #anchor, #bottom, #bottom_left, #bottom_right, #deep_copy, #height, #indent, #reference_bounds, restore_deep_copy, #stretchy?, #top, #top_left, #top_right

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(document, parent, point, options = {})  ⇒ ColumnBox 
  

  

  

  
    

Returns a new instance of ColumnBox.

  

  

Parameters:

  
    
- 
      
        point
      
      
        (Array(Number, Number))
      
      
      
    
  
    
- 
      
        options
      
      
        (Hash{Symbol => any})
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :width
          (Number)
          
            
          
          
            — 

width of the new column box, must be specified.

          
        
      
        
- 
          :height
          (Number)
          
            
          
          
            — 

height of the new column box, stretchy box if omitted.

          
        
      
        
- 
          :columns
          (Integer)
          
            
              — default:
              3
            
          
          
        
      
        
- 
          :spacer
          (Number)
          
            
              — default:
              font_size
            
          
          
        
      
        
- 
          :reflow_margins
          (Boolean)
          
            
              — default:
              false
            
          
          
        
      
    

  

  
    
      

```

68
69
70
71
72
73
74
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 68

def initialize(document, parent, point, options = {})
  super
  @columns = options[:columns] || 3
  @spacer = options[:spacer] || @document.font_size
  @current_column = 0
  @reflow_margins = options[:reflow_margins]
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_left_padding**(left_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
        left_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

149
150
151
152
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 149

def add_left_padding(left_padding)
  @total_left_padding += left_padding
  @x += left_padding
end
```

    
  

    
      
  
### 
  
    #**add_right_padding**(right_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
        right_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

165
166
167
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 165

def add_right_padding(right_padding)
  @total_right_padding += right_padding
end
```

    
  

    
      
  
### 
  
    #**bare_column_width**  ⇒ Number 
  

  

  

  
    

The column width, not the width of the whole box, before left and/or right padding.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 80

def bare_column_width
  (@width - (@spacer * (@columns - 1))) / @columns
end
```

    
  

    
      
  
### 
  
    #**left**  ⇒ Number 
  

  

  

  
    

Relative position of the left edge of the current column.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

109
110
111
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 109

def left
  width_of_column * @current_column
end
```

    
  

    
      
  
### 
  
    #**left_side**  ⇒ Number 
  

  

  

  
    

x coordinate of the left edge of the current column.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

102
103
104
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 102

def left_side
  absolute_left + (width_of_column * @current_column)
end
```

    
  

    
      
  
### 
  
    #**move_past_bottom**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Moves to the next column or starts a new page if currently positioned at the rightmost column.

  

  

  
    
      

```

132
133
134
135
136
137
138
139
140
141
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 132

def move_past_bottom
  @current_column = (@current_column + 1) % @columns
  @document.y = @y
  if @current_column.zero?
    if @reflow_margins
      @y = @parent.absolute_top
    end
    @document.start_new_page
  end
end
```

    
  

    
      
  
### 
  
    #**right**  ⇒ Number 
  

  

  

  
    

Relative position of the right edge of the current column.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 124

def right
  left + width
end
```

    
  

    
      
  
### 
  
    #**right_side**  ⇒ Number 
  

  

  

  
    

x coordinate of the right edge of the current column.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

116
117
118
119
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 116

def right_side
  columns_from_right = @columns - (1 + @current_column)
  absolute_right - (width_of_column * columns_from_right)
end
```

    
  

    
      
  
### 
  
    #**subtract_left_padding**(left_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
        left_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

157
158
159
160
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 157

def subtract_left_padding(left_padding)
  @total_left_padding -= left_padding
  @x -= left_padding
end
```

    
  

    
      
  
### 
  
    #**subtract_right_padding**(right_padding)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

  

  

Parameters:

  
    
- 
      
        right_padding
      
      
        (Number)
      
      
      
    
  

  
    
      

```

172
173
174
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 172

def subtract_right_padding(right_padding)
  @total_right_padding -= right_padding
end
```

    
  

    
      
  
### 
  
    #**width**  ⇒ Number 
  

  

  

  
    

The column width after padding. Used to calculate how long a line of text can be.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

88
89
90
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 88

def width
  bare_column_width - (@total_left_padding + @total_right_padding)
end
```

    
  

    
      
  
### 
  
    #**width_of_column**  ⇒ Number 
  

  

  

  
    

Column width including the spacer.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

95
96
97
```

    
    
      

```
# File 'lib/prawn/document/column_box.rb', line 95

def width_of_column
  bare_column_width + @spacer
end
```