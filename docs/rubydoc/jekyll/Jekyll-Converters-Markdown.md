# Class: Jekyll::Converters::Markdown
  
    Inherits:
    
      Jekyll::Converter
      
        

          
- Object

- Plugin

- Jekyll::Converter

- Jekyll::Converters::Markdown

        show all
      

    Defined in:
    lib/jekyll/converters/markdown.rb,

  lib/jekyll/converters/markdown/kramdown_parser.rb

## Overview

Markdown converter. For more info on converters see jekyllrb.com/docs/plugins/converters/

## Defined Under Namespace

      **Classes:** KramdownParser
    
  
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
  
      #**extname_list**  ⇒ Object 

-
  
      #**get_processor**  ⇒ Object 

RuboCop does not allow reader methods to have names starting with `get_` To ensure compatibility, this check has been disabled on this method.

-
  
      #**matches**(ext)  ⇒ Object 

Does the given extension match this converter’s list of acceptable extensions? Takes one argument: the file’s extension (including the dot).

-
  
      #**output_ext**(_ext)  ⇒ Object 

Public: The extension to be given to the output file (including the dot).

-
  
      #**setup**  ⇒ Object 

-
  
      #**third_party_processors**  ⇒ Object 

Public: A list of processors that you provide via plugins.

-
  
      #**valid_processors**  ⇒ Object 

Public: Provides you with a list of processors comprised of the ones we support internally and the ones that you have provided to us (if they’re whitelisted for use in safe mode).

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

83
84
85
86
87
88
```

```
# File 'lib/jekyll/converters/markdown.rb', line 83

def convert(content)
  setup
  @cache.getset(content) do
    @parser.convert(content)
  end
end

```

###
  
    #**extname_list**  ⇒ Object 
  

  

  

  
    
      

```

90
91
92
```

```
# File 'lib/jekyll/converters/markdown.rb', line 90

def extname_list
  @extname_list ||= @config["markdown_ext"].split(",").map! { |e| ".#{e.downcase}" }
end

```

###
  
    #**get_processor**  ⇒ Object 
  

  

  

  
    

RuboCop does not allow reader methods to have names starting with `get_` To ensure compatibility, this check has been disabled on this method

rubocop:disable Naming/AccessorMethodName

```

35
36
37
38
39
40
41
```

```
# File 'lib/jekyll/converters/markdown.rb', line 35

def get_processor
  case @config["markdown"].downcase
  when "kramdown" then KramdownParser.new(@config)
  else
    custom_processor
  end
end

```

###
  
    #**matches**(ext)  ⇒ Object 
  

  

  

  
    

Does the given extension match this converter’s list of acceptable extensions? Takes one argument: the file’s extension (including the dot).

ext - The String extension to check.

Returns true if it matches, false otherwise.

```

65
66
67
```

```
# File 'lib/jekyll/converters/markdown.rb', line 65

def matches(ext)
  extname_list.include?(ext.downcase)
end

```

###
  
    #**output_ext**(_ext)  ⇒ Object 
  

  

  

  
    

Public: The extension to be given to the output file (including the dot).

ext - The String extension or original file.

Returns The String output file extension.

```

74
75
76
```

```
# File 'lib/jekyll/converters/markdown.rb', line 74

def output_ext(_ext)
  ".html"
end

```

###
  
    #**setup**  ⇒ Object 
  

  

  

  
    
      

```

12
13
14
15
16
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
28
29
```

```
# File 'lib/jekyll/converters/markdown.rb', line 12

def setup
  return if @setup ||= false

  unless (@parser = get_processor)
    if @config["safe"]
      Jekyll.logger.warn "Build Warning:", "Custom processors are not loaded in safe mode"
    end

    Jekyll.logger.error "Markdown processor:",
                        "#{@config["markdown"].inspect} is not a valid Markdown processor."
    Jekyll.logger.error "", "Available processors are: #{valid_processors.join(", ")}"
    Jekyll.logger.error ""
    raise Errors::FatalException, "Invalid Markdown processor given: #{@config["markdown"]}"
  end

  @cache = Jekyll::Cache.new("Jekyll::Converters::Markdown")
  @setup = true
end

```

###
  
    #**third_party_processors**  ⇒ Object 
  

  

  

  
    

Public: A list of processors that you provide via plugins.

Returns an array of symbols

```

55
56
57
```

```
# File 'lib/jekyll/converters/markdown.rb', line 55

def third_party_processors
  self.class.constants - [:KramdownParser, :PRIORITIES]
end

```

###
  
    #**valid_processors**  ⇒ Object 
  

  

  

  
    

Public: Provides you with a list of processors comprised of the ones we support internally and the ones that you have provided to us (if they’re whitelisted for use in safe mode).

Returns an array of symbols.

```

48
49
50
```

```
# File 'lib/jekyll/converters/markdown.rb', line 48

def valid_processors
  [:kramdown] + third_party_processors
end

```
