# Class: SimpleForm::Wrappers::Builder
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- SimpleForm::Wrappers::Builder
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/simple_form/wrappers/builder.rb
  
  

## Overview

  
    

Provides the builder syntax for components. The builder provides three methods `use`, `optional` and `wrapper` and they allow the following invocations:

```
config.wrappers do |b|
  # Use a single component
  b.use :html5

  # Use the component, but do not automatically lookup. It will only be triggered when
  # :placeholder is explicitly set.
  b.optional :placeholder

  # Use a component with specific wrapper options
  b.use :error, wrap_with: { tag: "span", class: "error" }

  # Use a set of components by wrapping them in a tag+class.
  b.wrapper tag: "div", class: "another" do |ba|
    ba.use :label
    ba.use :input
  end

  # Use a set of components by wrapping them in a tag+class.
  # This wrapper is identified by :label_input, which means it can
  # be turned off on demand with `f.input :name, label_input: false`
  b.wrapper :label_input, tag: "div", class: "another" do |ba|
    ba.use :label
    ba.use :input
  end
end

```

The builder also accepts default options at the root level. This is usually used if you want a component to be disabled by default:

```
config.wrappers hint: false do |b|
  b.use :hint
  b.use :label_input
end

```

In the example above, hint defaults to false, which means it won’t automatically do the lookup anymore. It will only be triggered when :hint is explicitly set.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(options)  ⇒ Builder 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Builder.

  

      
        
- 
  
    
      #**optional**(name, options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**to_a**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**use**(name, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**wrapper**(name, options = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options)  ⇒ Builder 
  

  

  

  
    

Returns a new instance of Builder.

  

  

  
    
      

```

44
45
46
47
```

    
    
      

```
# File 'lib/simple_form/wrappers/builder.rb', line 44

def initialize(options)
  @options    = options
  @components = []
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**optional**(name, options = {}, &block)  ⇒ Object 
  

  

  

  
    
      

```

57
58
59
60
```

    
    
      

```
# File 'lib/simple_form/wrappers/builder.rb', line 57

def optional(name, options = {}, &block)
  @options[name] = false
  use(name, options)
end
```

    
  

    
      
  
### 
  
    #**to_a**  ⇒ Object 
  

  

  

  
    
      

```

75
76
77
```

    
    
      

```
# File 'lib/simple_form/wrappers/builder.rb', line 75

def to_a
  @components
end
```

    
  

    
      
  
### 
  
    #**use**(name, options = {})  ⇒ Object 
  

  

  

  
    
      

```

49
50
51
52
53
54
55
```

    
    
      

```
# File 'lib/simple_form/wrappers/builder.rb', line 49

def use(name, options = {})
  if options && wrapper = options[:wrap_with]
    @components << Single.new(name, wrapper, options.except(:wrap_with))
  else
    @components << Leaf.new(name, options)
  end
end
```

    
  

    
      
  
### 
  
    #**wrapper**(name, options = nil)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/simple_form/wrappers/builder.rb', line 62

def wrapper(name, options = nil)
  if block_given?
    name, options = nil, name if name.is_a?(Hash)
    builder = self.class.new(@options)
    options ||= {}
    options[:tag] = :div if options[:tag].nil?
    yield builder
    @components << Many.new(name, builder.to_a, options)
  else
    raise ArgumentError, "A block is required as argument to wrapper"
  end
end
```