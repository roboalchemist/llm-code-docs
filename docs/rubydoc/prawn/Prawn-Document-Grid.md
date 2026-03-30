# Class: Prawn::Document::Grid
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Document::Grid
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/grid.rb
  
  

## Overview

  
    

A Grid represents the entire grid system of a Page and calculates the column width and row height of the base box.

  

  

  
## Experimental API collapse

  

    
      
- 
  
    
      #**column_gutter**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Column gutter size.

  

    
      
- 
  
    
      #**columns**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Number of columns in the grid.

  

    
      
- 
  
    
      #**gutter**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Gutter size.

  

    
      
- 
  
    
      #**pdf**  ⇒ Prawn::Document 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    
  

    
      
- 
  
    
      #**row_gutter**  ⇒ Number 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Row gutter size.

  

    
      
- 
  
    
      #**rows**  ⇒ Integer 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Number of rows in the grid.

  

    
  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**column_width**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Calculates the base width of boxes.

  

      
        
- 
  
    
      #**initialize**(pdf, options = {})  ⇒ Grid 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Grid.

  

      
        
- 
  
    
      #**row_height**  ⇒ Float 
    

    
  
  
  
  
  
  
  
  

  
    

Calculates the base height of boxes.

  

      
        
- 
  
    
      #**show_all**(color = 'CCCCCC')  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Diagnostic tool to show all of the grid boxes.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(pdf, options = {})  ⇒ Grid 
  

  

  

  
    

Returns a new instance of Grid.

  

  

Parameters:

  
    
- 
      
      
      
      
    
  
    
- 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :columns
          (Integer)
          
            
          
          
            — 

Number of columns in the grid.

          
        
      
        
- 
          :rows
          (Integer)
          
            
          
          
            — 

Number of rows in the grid.

          
        
      
        
- 
          :gutter
          (Number)
          
            
          
          
            — 

Gutter size. `:row_gutter` and `:column_gutter` are ignored if specified.

          
        
      
        
- 
          :row_gutter
          (Number)
          
            
          
          
            — 

Row gutter size.

          
        
      
        
- 
          :column_gutter
          (Number)
          
            
          
          
            — 

Column gutter size.

          
        
      
    

  

  
    
      

```

104
105
106
107
108
109
110
111
112
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 104

def initialize(pdf, options = {})
  valid_options = i[columns rows gutter row_gutter column_gutter]
  Prawn.verify_options(valid_options, options)

  @pdf = pdf
  @columns = options[:columns]
  @rows = options[:rows]
  apply_gutter(options)
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**column_gutter**  ⇒ Number  (readonly)
  

  

  

  
    

Column gutter size.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 94

def column_gutter
  @column_gutter
end

```

    
  

    
      
      
      
  
### 
  
    #**columns**  ⇒ Integer  (readonly)
  

  

  

  
    

Number of columns in the grid.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

78
79
80
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 78

def columns
  @columns
end

```

    
  

    
      
      
      
  
### 
  
    #**gutter**  ⇒ Number  (readonly)
  

  

  

  
    

Gutter size.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

86
87
88
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 86

def gutter
  @gutter
end

```

    
  

    
      
      
      
  
### 
  
    #**pdf**  ⇒ Prawn::Document  (readonly)
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 74

def pdf
  @pdf
end

```

    
  

    
      
      
      
  
### 
  
    #**row_gutter**  ⇒ Number  (readonly)
  

  

  

  
    

Row gutter size.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

90
91
92
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 90

def row_gutter
  @row_gutter
end

```

    
  

    
      
      
      
  
### 
  
    #**rows**  ⇒ Integer  (readonly)
  

  

  

  
    

Number of rows in the grid.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

82
83
84
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 82

def rows
  @rows
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**column_width**  ⇒ Float 
  

  

  

  
    

Calculates the base width of boxes.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

117
118
119
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 117

def column_width
  @column_width ||= subdivide(pdf.bounds.width, columns, column_gutter)
end

```

    
  

    
      
  
### 
  
    #**row_height**  ⇒ Float 
  

  

  

  
    

Calculates the base height of boxes.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 124

def row_height
  @row_height ||= subdivide(pdf.bounds.height, rows, row_gutter)
end

```

    
  

    
      
  
### 
  
    #**show_all**(color = 'CCCCCC')  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Diagnostic tool to show all of the grid boxes.

  

  

Parameters:

  
    
- 
      
      
      
        *(defaults to: 'CCCCCC')*
      
      
    
  

  
    
      

```

132
133
134
135
136
137
138
```

    
    
      

```
# File 'lib/prawn/grid.rb', line 132

def show_all(color = 'CCCCCC')
  rows.times do |row|
    columns.times do |column|
      pdf.grid(row, column).show(color)
    end
  end
end

```