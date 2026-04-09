# Class: Deflating
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Deflating
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/rantly/shrinks.rb
  
  

## Overview

  
    

Array where the elements that can’t be shrunk are removed

  

  

  
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
  
    
      #**initialize**(a)  ⇒ Deflating 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Deflating.

  

      
        
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
  
    #**initialize**(a)  ⇒ Deflating 
  

  

  

  
    

Returns a new instance of Deflating.

  

  

  
    
      

```

109
110
111
112
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 109

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

142
143
144
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 142

def array
  @array
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(i)  ⇒ Object 
  

  

  

  
    
      

```

114
115
116
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 114

def [](i)
  @array[i]
end

```

    
  

    
      
  
### 
  
    #**[]=**(i, value)  ⇒ Object 
  

  

  

  
    
      

```

118
119
120
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 118

def []=(i, value)
  @array[i] = value
end

```

    
  

    
      
  
### 
  
    #**each**(&block)  ⇒ Object 
  

  

  

  
    
      

```

138
139
140
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 138

def each(&block)
  @array.each(&block)
end

```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

134
135
136
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 134

def inspect
  to_s
end

```

    
  

    
      
  
### 
  
    #**length**  ⇒ Object 
  

  

  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 122

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

158
159
160
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 158

def retry?
  @position >= 0
end

```

    
  

    
      
  
### 
  
    #**shrink**  ⇒ Object 
  

  

  

  
    
      

```

144
145
146
147
148
149
150
151
152
153
154
155
156
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 144

def shrink
  shrunk = @array.dup
  if @position >= 0
    e = @array.at(@position)
    if e.respond_to?(:shrinkable?) && e.shrinkable?
      shrunk[@position] = e.shrink
    else
      shrunk.delete_at(@position)
    end
    @position -= 1
  end
  Deflating.new(shrunk)
end

```

    
  

    
      
  
### 
  
    #**shrinkable?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

162
163
164
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 162

def shrinkable?
  !@array.empty?
end

```

    
  

    
      
  
### 
  
    #**size**  ⇒ Object 
  

  

  

  
    
      

```

126
127
128
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 126

def size
  length
end

```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

130
131
132
```

    
    
      

```
# File 'lib/rantly/shrinks.rb', line 130

def to_s
  @array.to_s.insert(1, 'D ')
end

```