# Class: Jekyll::Converter
  
    Inherits:
    
      Plugin
      
        

          
- Object

- Plugin

- Jekyll::Converter

        show all
      

    Defined in:
    lib/jekyll/converter.rb
  
## Direct Known Subclasses

Jekyll::Converters::Identity, Jekyll::Converters::Markdown, Jekyll::Converters::SmartyPants

## Constant Summary

### Constants inherited

     from Plugin

Plugin::PRIORITIES

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**highlighter_prefix**(highlighter_prefix = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Public: Get or set the highlighter prefix.

-
  
      .**highlighter_suffix**(highlighter_suffix = nil)  ⇒ Object 

Public: Get or set the highlighter suffix.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**highlighter_prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the highlighter prefix.

-
  
      #**highlighter_suffix**  ⇒ Object 

Get the highlighter suffix.

-
  
      #**initialize**(config = {})  ⇒ Converter 

    constructor
  
  
  
  
  
  

  
    

Initialize the converter.

### Methods inherited from Plugin

# <=>, <=>, catch_inheritance, descendants, inherited, priority, safe

## Constructor Details

###
  
    #**initialize**(config = {})  ⇒ Converter 
  

  

  

  
    

Initialize the converter.

Returns an initialized Converter.

```

36
37
38
```

```
# File 'lib/jekyll/converter.rb', line 36

def initialize(config = {})
  @config = config
end
```

## Class Method Details

###
  
    .**highlighter_prefix**(highlighter_prefix = nil)  ⇒ Object 
  

  

  

  
    

Public: Get or set the highlighter prefix. When an argument is specified, the prefix will be set. If no argument is specified, the current prefix will be returned.

highlighter_prefix - The String prefix (default: nil).

Returns the String prefix.

```

12
13
14
15
16
17
```

```
# File 'lib/jekyll/converter.rb', line 12

def self.highlighter_prefix(highlighter_prefix = nil)
  unless defined?(@highlighter_prefix) && highlighter_prefix.nil?
    @highlighter_prefix = highlighter_prefix
  end
  @highlighter_prefix
end
```

###
  
    .**highlighter_suffix**(highlighter_suffix = nil)  ⇒ Object 
  

  

  

  
    

Public: Get or set the highlighter suffix. When an argument is specified, the suffix will be set. If no argument is specified, the current suffix will be returned.

highlighter_suffix - The String suffix (default: nil).

Returns the String suffix.

```

26
27
28
29
30
31
```

```
# File 'lib/jekyll/converter.rb', line 26

def self.highlighter_suffix(highlighter_suffix = nil)
  unless defined?(@highlighter_suffix) && highlighter_suffix.nil?
    @highlighter_suffix = highlighter_suffix
  end
  @highlighter_suffix
end
```

## Instance Method Details

###
  
    #**highlighter_prefix**  ⇒ Object 
  

  

  

  
    

Get the highlighter prefix.

Returns the String prefix.

```

43
44
45
```

```
# File 'lib/jekyll/converter.rb', line 43

def highlighter_prefix
  self.class.highlighter_prefix
end
```

###
  
    #**highlighter_suffix**  ⇒ Object 
  

  

  

  
    

Get the highlighter suffix.

Returns the String suffix.

```

50
51
52
```

```
# File 'lib/jekyll/converter.rb', line 50

def highlighter_suffix
  self.class.highlighter_suffix
end
```
