# Class: Numeric
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Numeric
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Prawn::Measurements
  
  
  

  

  
  
    Defined in:
    lib/prawn/measurement_extensions.rb
  
  

## Overview

  
    

Core extensions for Prawn::Measurements.

This mainly enables measurements DSL.

You have to explicitly require “prawn/measurement_extensions” to enable these.

“‘ruby require ’prawn/measurement_extensions’

12.mm 2.cm 0.5.in 4.yd + 2.ft “‘

  

  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**cm**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from centimeters to points.

  

      
        
- 
  
    
      #**dm**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from decimeters to points.

  

      
        
- 
  
    
      #**ft**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from feet to points.

  

      
        
- 
  
    
      #**in**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from inches to points.

  

      
        
- 
  
    
      #**m**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from meters to points.

  

      
        
- 
  
    
      #**mm**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from millimeters to points.

  

      
        
- 
  
    
      #**pt**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from points to points.

  

      
        
- 
  
    
      #**yd**  ⇒ Number 
    

    
  
  
  
  
  
  
  
  

  
    

Convert from yards to points.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Prawn::Measurements

  

#cm2mm, #cm2pt, #dm2mm, #dm2pt, #ft2in, #ft2pt, #in2pt, #m2mm, #m2pt, #mm2pt, #pt2mm, #pt2pt, #yd2in, #yd2pt

  
    
## Instance Method Details

    
      
  
### 
  
    #**cm**  ⇒ Number 
  

  

  

  
    

Convert from centimeters to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 37

def cm
  cm2pt(self)
end

```

    
  

    
      
  
### 
  
    #**dm**  ⇒ Number 
  

  

  

  
    

Convert from decimeters to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 44

def dm
  dm2pt(self)
end

```

    
  

    
      
  
### 
  
    #**ft**  ⇒ Number 
  

  

  

  
    

Convert from feet to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

72
73
74
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 72

def ft
  ft2pt(self)
end

```

    
  

    
      
  
### 
  
    #**in**  ⇒ Number 
  

  

  

  
    

Convert from inches to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 58

def in
  in2pt(self)
end

```

    
  

    
      
  
### 
  
    #**m**  ⇒ Number 
  

  

  

  
    

Convert from meters to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

51
52
53
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 51

def m
  m2pt(self)
end

```

    
  

    
      
  
### 
  
    #**mm**  ⇒ Number 
  

  

  

  
    

Convert from millimeters to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 30

def mm
  mm2pt(self)
end

```

    
  

    
      
  
### 
  
    #**pt**  ⇒ Number 
  

  

  

  
    

Convert from points to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

79
80
81
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 79

def pt
  pt2pt(self)
end

```

    
  

    
      
  
### 
  
    #**yd**  ⇒ Number 
  

  

  

  
    

Convert from yards to points.

  

  

Returns:

  
    
- 
      
      
        (Number)
      
      
      
    
  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/prawn/measurement_extensions.rb', line 65

def yd
  yd2pt(self)
end

```