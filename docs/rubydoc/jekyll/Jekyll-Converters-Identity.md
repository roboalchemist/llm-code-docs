# Class: Jekyll::Converters::Identity
  
    Inherits:
    
      Jekyll::Converter
      
        

          
- Object

- Plugin

- Jekyll::Converter

- Jekyll::Converters::Identity

        show all
      

    Defined in:
    lib/jekyll/converters/identity.rb
  
## Overview

Identity converter. Returns same content as given. For more info on converters see jekyllrb.com/docs/plugins/converters/

## Constant Summary

### Constants inherited

     from Plugin

Plugin::PRIORITIES

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**convert**(content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Logic to do the content conversion.

-
  
      #**matches**(_ext)  ⇒ Object 

Public: Does the given extension match this converter’s list of acceptable extensions? Takes one argument: the file’s extension (including the dot).

-
  
      #**output_ext**(ext)  ⇒ Object 

Public: The extension to be given to the output file (including the dot).

### Methods inherited from Jekyll::Converter

highlighter_prefix, #highlighter_prefix, highlighter_suffix, #highlighter_suffix, #initialize

### Methods inherited from Plugin

# <=>, <=>, catch_inheritance, descendants, inherited, #initialize, priority, safe

## Constructor Details

This class inherits a constructor from Jekyll::Converter
  
## Instance Method Details

###
  
    #**convert**(content)  ⇒ Object 
  

  

  

  
    

Logic to do the content conversion.

content - String content of file (without front matter).

Returns a String of the converted content.

```

36
37
38
```

```
# File 'lib/jekyll/converters/identity.rb', line 36

def convert(content)
  content
end

```

###
  
    #**matches**(_ext)  ⇒ Object 
  

  

  

  
    

Public: Does the given extension match this converter’s list of acceptable extensions? Takes one argument: the file’s extension (including the dot).

_ext - The String extension to check (not relevant here)

Returns true since it always matches.

```

18
19
20
```

```
# File 'lib/jekyll/converters/identity.rb', line 18

def matches(_ext)
  true
end

```

###
  
    #**output_ext**(ext)  ⇒ Object 
  

  

  

  
    

Public: The extension to be given to the output file (including the dot).

ext - The String extension or original file.

Returns The String output file extension.

```

27
28
29
```

```
# File 'lib/jekyll/converters/identity.rb', line 27

def output_ext(ext)
  ext
end

```
