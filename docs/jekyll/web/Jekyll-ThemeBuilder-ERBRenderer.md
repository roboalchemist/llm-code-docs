# Class: Jekyll::ThemeBuilder::ERBRenderer
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::ThemeBuilder::ERBRenderer

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
    Defined in:
    lib/jekyll/theme_builder.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(theme_builder)  ⇒ ERBRenderer 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ERBRenderer.

-
  
      #**jekyll_version_with_minor**  ⇒ Object 

-
  
      #**render**(contents)  ⇒ Object 

-
  
      #**theme_directories**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(theme_builder)  ⇒ ERBRenderer 
  

  

  

  
    

Returns a new instance of ERBRenderer.

```

104
105
106
```

```
# File 'lib/jekyll/theme_builder.rb', line 104

def initialize(theme_builder)
  @theme_builder = theme_builder
end
```

## Instance Method Details

###
  
    #**jekyll_version_with_minor**  ⇒ Object 
  

  

  

  
    
      

```

108
109
110
```

```
# File 'lib/jekyll/theme_builder.rb', line 108

def jekyll_version_with_minor
  Jekyll::VERSION.split(".").take(2).join(".")
end
```

###
  
    #**render**(contents)  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
```

```
# File 'lib/jekyll/theme_builder.rb', line 116

def render(contents)
  ERB.new(contents).result binding
end
```

###
  
    #**theme_directories**  ⇒ Object 
  

  

  

  
    
      

```

112
113
114
```

```
# File 'lib/jekyll/theme_builder.rb', line 112

def theme_directories
  SCAFFOLD_DIRECTORIES
end
```
