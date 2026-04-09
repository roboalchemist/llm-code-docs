# Class: Tuple
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Tuple
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/shrinks.rb
  
  

## Overview

  
    

Array where elements can be shrunk but not removed

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**array**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute array.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(i)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**[]=**(i, value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**each**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(a)  ⇒ Tuple 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Tuple.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**length**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**retry?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shrink**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**shrinkable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**size**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(a)  ⇒ Tuple 
  

  

  

  
    

Returns a new instance of Tuple.

  

  

  
    
      

```

48
49
50
51
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 48

def initialize(a)
  @array = a
  @position = a.size - 1
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**array**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute array.

  

  

  
    
      

```

81
82
83
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 81

def array
  @array
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(i)  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 53

def [](i)
  @array[i]
end
```

    
  

    
      
  
### 
  
    #**[]=**(i, value)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 57

def []=(i, value)
  @array[i] = value
end
```

    
  

    
      
  
### 
  
    #**each**(&block)  ⇒ Object 
  

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 77

def each(&block)
  @array.each(&block)
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

73
74
75
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 73

def inspect
  to_s
end
```

    
  

    
      
  
### 
  
    #**length**  ⇒ Object 
  

  

  

  
    
      

```

61
62
63
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 61

def length
  @array.length
end
```

    
  

    
      
  
### 
  
    #**retry?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

98
99
100
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 98

def retry?
  @position >= 0
end
```

    
  

    
      
  
### 
  
    #**shrink**  ⇒ Object 
  

  

  

  
    
      

```

83
84
85
86
87
88
89
90
91
92
93
94
95
96
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 83

def shrink
  shrunk = @array.dup
  while @position >= 0
    e = @array.at(@position)
    break if e.respond_to?(:shrinkable?) && e.shrinkable?

    @position -= 1
  end
  if @position >= 0
    shrunk[@position] = e.shrink
    @position -= 1
  end
  Tuple.new(shrunk)
end
```

    
  

    
      
  
### 
  
    #**shrinkable?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

102
103
104
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 102

def shrinkable?
  @array.any? { |e| e.respond_to?(:shrinkable?) && e.shrinkable? }
end
```

    
  

    
      
  
### 
  
    #**size**  ⇒ Object 
  

  

  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 65

def size
  length
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 69

def to_s
  @array.to_s.insert(1, 'T ')
end
```