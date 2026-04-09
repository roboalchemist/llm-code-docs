# Class: SimpleForm::Wrappers::Many
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- SimpleForm::Wrappers::Many
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/wrappers/many.rb
  
  

## Overview

  
    

A wrapper is an object that holds several components and render them. A component may be any object that responds to `render`. This API allows inputs/components to be easily wrapped, removing the need to modify the code only to wrap input in an extra tag.

`Many` represents a wrapper around several components at the same time. It may optionally receive a namespace, allowing it to be configured on demand on input generation.

  

  

  
## Direct Known Subclasses

  

Root, Single

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**components**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute components.

  

    
      
- 
  
    
      #**defaults**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute defaults.

  

    
      
- 
  
    
      #**namespace**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute namespace.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(namespace, components, defaults = {})  ⇒ Many 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Many.

  

      
        
- 
  
    
      #**render**(input)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(namespace, components, defaults = {})  ⇒ Many 
  

  

  

  
    

Returns a new instance of Many.

  

  

  
    
      

```

15
16
17
18
19
20
21
```

    
    
      

```
# File 'lib/simple_form/wrappers/many.rb', line 15

def initialize(namespace, components, defaults = {})
  @namespace  = namespace
  @components = components
  @defaults   = defaults
  @defaults[:tag]   = :div unless @defaults.key?(:tag)
  @defaults[:class] = Array(@defaults[:class])
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**components**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute components.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/simple_form/wrappers/many.rb', line 13

def components
  @components
end
```

    
  

    
      
      
      
  
### 
  
    #**defaults**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute defaults.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/simple_form/wrappers/many.rb', line 13

def defaults
  @defaults
end
```

    
  

    
      
      
      
  
### 
  
    #**namespace**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute namespace.

  

  

  
    
      

```

13
14
15
```

    
    
      

```
# File 'lib/simple_form/wrappers/many.rb', line 13

def namespace
  @namespace
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find**(name)  ⇒ Object 
  

  

  

  
    
      

```

36
37
38
39
40
41
42
43
44
45
46
47
48
```

    
    
      

```
# File 'lib/simple_form/wrappers/many.rb', line 36

def find(name)
  return self if namespace == name

  @components.each do |c|
    if c.is_a?(Symbol)
      return nil if c == namespace
    elsif value = c.find(name)
      return value
    end
  end

  nil
end
```

    
  

    
      
  
### 
  
    #**render**(input)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
29
30
31
32
33
34
```

    
    
      

```
# File 'lib/simple_form/wrappers/many.rb', line 23

def render(input)
  content = "".html_safe
  options = input.options

  components.each do |component|
    next if options[component.namespace] == false
    rendered = component.render(input)
    content.safe_concat rendered.to_s if rendered
  end

  wrap(input, options, content)
end
```