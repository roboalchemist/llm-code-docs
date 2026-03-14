# Class: Pod::Generator::ModuleMap::Header
  
  
  

  
  
    Inherits:
    
      Struct
      
        

          
- Object
          
            
- Struct
          
            
- Pod::Generator::ModuleMap::Header
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/cocoapods/generator/module_map.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**exclude**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute exclude.

  

    
      
- 
  
    
      #**mtime**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute mtime.

  

    
      
- 
  
    
      #**path**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute path.

  

    
      
- 
  
    
      #**private**  ⇒ Object 
    

    
      (also: #private?)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute private.

  

    
      
- 
  
    
      #**size**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute size.

  

    
      
- 
  
    
      #**textual**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute textual.

  

    
      
- 
  
    
      #**umbrella**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute umbrella.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**attrs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**exclude**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute exclude

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

the current value of exclude

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 15

def exclude
  @exclude
end
```

    
  

    
      
      
      
  
### 
  
    #**mtime**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute mtime

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

the current value of mtime

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 15

def mtime
  @mtime
end
```

    
  

    
      
      
      
  
### 
  
    #**path**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute path

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

the current value of path

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 15

def path
  @path
end
```

    
  

    
      
      
      
  
### 
  
    #**private**  ⇒ Object 
  

  
    Also known as:
    private?
    
  

  

  
    

Returns the value of attribute private

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

the current value of private

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 15

def private
  @private
end
```

    
  

    
      
      
      
  
### 
  
    #**size**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute size

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

the current value of size

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 15

def size
  @size
end
```

    
  

    
      
      
      
  
### 
  
    #**textual**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute textual

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

the current value of textual

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 15

def textual
  @textual
end
```

    
  

    
      
      
      
  
### 
  
    #**umbrella**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute umbrella

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

the current value of umbrella

      
    
  

  
    
      

```

15
16
17
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 15

def umbrella
  @umbrella
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**attrs**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
32
33
34
35
36
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 29

def attrs
  attrs = {
    'size' => size,
    'mtime' => mtime,
  }.reject { |_k, v| v.nil? }
  return nil if attrs.empty?
  attrs.to_s
end
```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/cocoapods/generator/module_map.rb', line 17

def to_s
  [
    (:private if private?),
    (:textual if textual),
    (:umbrella if umbrella),
    (:exclude if exclude),
    'header',
    %("#{path.to_s.gsub('"', '\"')}"),
    attrs,
  ].compact.join(' ')
end
```