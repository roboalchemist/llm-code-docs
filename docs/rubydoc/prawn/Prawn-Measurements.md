# Module: Prawn::Measurements
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Numeric
  
  

  
  
    Defined in:
    lib/prawn/measurements.rb
  
  

## Overview

  
    

Distance unit conversions between metric, imperial, and PDF.

  

  

  
    
## 
      Stable API
      collapse
    

    

      
        
- 
  
    
      #**cm2mm**(cm)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert centimeter to millimeters.

  

      
        
- 
  
    
      #**cm2pt**(cm)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert centimeters to points.

  

      
        
- 
  
    
      #**dm2mm**(dm)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert decimeters to millimeters.

  

      
        
- 
  
    
      #**dm2pt**(dm)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert decimeters to points.

  

      
        
- 
  
    
      #**ft2in**(ft)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert feet to inches.

  

      
        
- 
  
    
      #**ft2pt**(ft)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert feet to points.

  

      
        
- 
  
    
      #**in2pt**(inch)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert inches to points.

  

      
        
- 
  
    
      #**m2mm**(m)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert meters to millimeters.

  

      
        
- 
  
    
      #**m2pt**(m)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert meters to points.

  

      
        
- 
  
    
      #**mm2pt**(mm)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert millimeters to points.

  

      
        
- 
  
    
      #**pt2mm**(pt)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert points to millimeters.

  

      
        
- 
  
    
      #**pt2pt**(pt)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert points to points.

  

      
        
- 
  
    
      #**yd2in**(yd)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert yards to inches.

  

      
        
- 
  
    
      #**yd2pt**(yd)  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert yards to points.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**cm2mm**(cm)  ⇒ Number 
  

  

  

  
    

Convert centimeter to millimeters.

  

  

Parameters:

  
    
- 
      
        cm
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 15

def cm2mm(cm)
  cm * 10
end
```

    
  

    
      
  
### 
  
    #**cm2pt**(cm)  ⇒ Number 
  

  

  

  
    

Convert centimeters to points.

  

  

Parameters:

  
    
- 
      
        cm
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

100
101
102
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 100

def cm2pt(cm)
  mm2pt(cm2mm(cm))
end
```

    
  

    
      
  
### 
  
    #**dm2mm**(dm)  ⇒ Number 
  

  

  

  
    

Convert decimeters to millimeters.

  

  

Parameters:

  
    
- 
      
        dm
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

23
24
25
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 23

def dm2mm(dm)
  dm * 100
end
```

    
  

    
      
  
### 
  
    #**dm2pt**(dm)  ⇒ Number 
  

  

  

  
    

Convert decimeters to points.

  

  

Parameters:

  
    
- 
      
        dm
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

108
109
110
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 108

def dm2pt(dm)
  mm2pt(dm2mm(dm))
end
```

    
  

    
      
  
### 
  
    #**ft2in**(ft)  ⇒ Number 
  

  

  

  
    

Convert feet to inches.

  

  

Parameters:

  
    
- 
      
        ft
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 42

def ft2in(ft)
  ft * 12
end
```

    
  

    
      
  
### 
  
    #**ft2pt**(ft)  ⇒ Number 
  

  

  

  
    

Convert feet to points.

  

  

Parameters:

  
    
- 
      
        ft
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

76
77
78
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 76

def ft2pt(ft)
  in2pt(ft2in(ft))
end
```

    
  

    
      
  
### 
  
    #**in2pt**(inch)  ⇒ Number 
  

  

  

  
    

Convert inches to points.

  

  

Parameters:

  
    
- 
      
        inch
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

68
69
70
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 68

def in2pt(inch)
  inch * 72
end
```

    
  

    
      
  
### 
  
    #**m2mm**(m)  ⇒ Number 
  

  

  

  
    

Convert meters to millimeters.

  

  

Parameters:

  
    
- 
      
        m
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 31

def m2mm(m)
  m * 1000
end
```

    
  

    
      
  
### 
  
    #**m2pt**(m)  ⇒ Number 
  

  

  

  
    

Convert meters to points.

  

  

Parameters:

  
    
- 
      
        m
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

116
117
118
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 116

def m2pt(m)
  mm2pt(m2mm(m))
end
```

    
  

    
      
  
### 
  
    #**mm2pt**(mm)  ⇒ Number 
  

  

  

  
    

Convert millimeters to points.

  

  

Parameters:

  
    
- 
      
        mm
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

92
93
94
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 92

def mm2pt(mm)
  mm * (72 / 25.4)
end
```

    
  

    
      
  
### 
  
    #**pt2mm**(pt)  ⇒ Number 
  

  

  

  
    

Convert points to millimeters.

  

  

Parameters:

  
    
- 
      
        pt
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 124

def pt2mm(pt)
  pt * 1 / mm2pt(1) # (25.4 / 72)
end
```

    
  

    
      
  
### 
  
    #**pt2pt**(pt)  ⇒ Number 
  

  

  

  
    

Convert points to points. For completeness.

  

  

Parameters:

  
    
- 
      
        pt
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 60

def pt2pt(pt)
  pt
end
```

    
  

    
      
  
### 
  
    #**yd2in**(yd)  ⇒ Number 
  

  

  

  
    

Convert yards to inches.

  

  

Parameters:

  
    
- 
      
        yd
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

50
51
52
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 50

def yd2in(yd)
  yd * 36
end
```

    
  

    
      
  
### 
  
    #**yd2pt**(yd)  ⇒ Number 
  

  

  

  
    

Convert yards to points.

  

  

Parameters:

  
    
- 
      
        yd
      
      
        (Number)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

84
85
86
```

    
    
      

```
# File 'lib/prawn/measurements.rb', line 84

def yd2pt(yd)
  in2pt(yd2in(yd))
end
```