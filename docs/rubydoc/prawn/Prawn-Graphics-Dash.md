# Module: Prawn::Graphics::Dash
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Prawn::Graphics
  
  

  
  
    Defined in:
    lib/prawn/graphics/dash.rb
  
  

## Overview

  
    

Implements stroke dashing.

  

  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**dash**(length = nil, options = {})  ⇒ Object 
    

    
      (also: #dash=)
    
  
  
  
  
  
  
  
  

  
    

Get or set stroke dash pattern.

  

      
        
- 
  
    
      #**dashed?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns `true` when stroke is dashed, `false` otherwise.

  

      
        
- 
  
    
      #**undash**  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Stops dashing, restoring solid stroked lines and curves.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**dash**  ⇒ Hash{:dash => Number, Array<Number>, :space => Number, nil, :phase => Number} 
    
      #**dash**(length, options = {})  ⇒ void 
    
  

  
    Also known as:
    dash=
    
  

  

  
    

Get or set stroke dash pattern.

  

  
  

Overloads:
  

    
      
      
- 
        #**dash**  ⇒ Hash{:dash => Number, Array<Number>, :space => Number, nil, :phase => Number} 
        
  
    

Returns the current dash pattern.

  

  

Returns:

  
    
  - 
      
      
      
      
    
  

      
    
      
      
- 
        #**dash**(length, options = {})  ⇒ void 
        
  
    

This method returns an undefined value.

Sets the dash pattern for stroked lines and curves.

Integers or Floats may be used for length and the option values. Dash units are in PDF points (1/72 inch).

  

  

Parameters:

  
    
  - 
      
      
      
      
        
        

    - 

If `length` is a Number (Integer or Float), it specifies the length of the dash and of the gap. The length of the gap can be customized by setting the `:space` option.

Examples:

length = 3 : 3 on, 3 off, 3 on, 3 off, …

length = 3, :space = 2 : 3 on, 2 off, 3 on, 2 off, …

    - 

If `length` is an array, it specifies the lengths of alternating dashes and gaps. The numbers must be non-negative and not all zero. The `:space` option is ignored in this case.

Examples:

length = [2, 1] : 2 on, 1 off, 2 on, 1 off, …

length = [3, 1, 2, 3] : 3 on, 1 off, 2 on, 3 off, 3 on, 1 off, …

length = [3, 0, 1] : 3 on, 0 off, 1 on, 3 off, 0 on, 1 off, …

      
    
  
    
  - 
      
      
      
        *(defaults to: {})*
      
      
    
  

  
    
    
    
    
    

Options Hash (options):
    

      
        
  - 
          :space
          (Number)
          
            
          
          
            — 

The space between the dashes (only used when `length` is not an array).

          
        
      
        
  - 
          :phase
          (Number)
          
            
              — default:
              0
            
          
          
            — 

The distance into the dash pattern at which to start the dash. For example, a phase of 0 starts at the beginning of the dash; whereas, if the phase is equal to the length of the dash, then stroking will begin at the beginning of the space.

          
        
      
    

  

      
    
  

  
    
      

```

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
71
72
73
74
75
76
77
78
79
80
81
```

    
    
      

```
# File 'lib/prawn/graphics/dash.rb', line 59

def dash(length = nil, options = {})
  return current_dash_state if length.nil?

  length = Array(length)

  if length.all?(&:zero?)
    raise ArgumentError,
      'Zero length dashes are invalid. Call #undash to disable dashes.'
  elsif length.any?(&:negative?)
    raise ArgumentError,
      'Negative numbers are not allowed for dash lengths.'
  end

  length = length.first if length.length == 1

  self.current_dash_state = {
    dash: length,
    space: length.is_a?(Array) ? nil : options[:space] || length,
    phase: options[:phase] || 0,
  }

  write_stroke_dash
end

```

    
  

    
      
  
### 
  
    #**dashed?**  ⇒ Boolean 
  

  

  

  
    

Returns `true` when stroke is dashed, `false` otherwise.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

96
97
98
```

    
    
      

```
# File 'lib/prawn/graphics/dash.rb', line 96

def dashed?
  current_dash_state != undashed_setting
end

```

    
  

    
      
  
### 
  
    #**undash**  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Stops dashing, restoring solid stroked lines and curves.

  

  

  
    
      

```

88
89
90
91
```

    
    
      

```
# File 'lib/prawn/graphics/dash.rb', line 88

def undash
  self.current_dash_state = undashed_setting
  write_stroke_dash
end

```