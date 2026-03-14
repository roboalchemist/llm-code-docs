# Class: Kramdown::JekyllDocument
  
    Inherits:
    
      Document
      
        

          
- Object

- Document

- Kramdown::JekyllDocument

        show all
      

    Defined in:
    lib/jekyll/converters/markdown/kramdown_parser.rb
  
## Overview

A Kramdown::Document subclass meant to optimize memory usage from initializing a kramdown document for parsing.

The optimization is by using the same options Hash (and its derivatives) for converting all Markdown documents in a Jekyll site.

## Class Attribute Summary collapse

-
  
      .**options**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

-
  
      .**parser**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute parser.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**setup**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The implementation is basically the core logic in Kramdown::Document#initialize.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(source, options = {})  ⇒ JekyllDocument 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of JekyllDocument.

-
  
      #**to_html**  ⇒ Object 

Use Kramdown::Converter::Html class to convert this document into HTML.

## Constructor Details

###
  
    #**initialize**(source, options = {})  ⇒ JekyllDocument 
  

  

  

  
    

Returns a new instance of JekyllDocument.

```

50
51
52
53
54
55
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 50

def initialize(source, options = {})
  JekyllDocument.setup(options)

  @options = JekyllDocument.options
  @root, @warnings = JekyllDocument.parser.parse(source, @options)
end
```

## Class Attribute Details

###
  
    .**options**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute options.

```

11
12
13
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 11

def options
  @options
end
```

###
  
    .**parser**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute parser.

```

11
12
13
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 11

def parser
  @parser
end
```

## Class Method Details

###
  
    .**setup**(options)  ⇒ Object 
  

  

  

  
    

The implementation is basically the core logic in Kramdown::Document#initialize

rubocop:disable Naming/MemoizedInstanceVariableName

```

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
30
31
32
33
34
35
36
37
38
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 16

def setup(options)
  @cache ||= {}

  # reset variables on a subsequent set up with a different options Hash
  unless @cache[:id] == options.hash
    @options = @parser = nil
    @cache[:id] = options.hash
  end

  @options ||= Options.merge(options).freeze
  @parser  ||= begin
    parser_name = (@options[:input] || "kramdown").to_s
    parser_name = parser_name[0..0].upcase + parser_name[1..-1]
    try_require("parser", parser_name)

    if Parser.const_defined?(parser_name)
      Parser.const_get(parser_name)
    else
      raise Kramdown::Error, "kramdown has no parser to handle the specified " \
                             "input format: #{@options[:input]}"
    end
  end
end
```

## Instance Method Details

###
  
    #**to_html**  ⇒ Object 
  

  

  

  
    

Use Kramdown::Converter::Html class to convert this document into HTML.

The implementation is basically an optimized version of core logic in Kramdown::Document#method_missing from kramdown-2.1.0.

```

61
62
63
64
65
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 61

def to_html
  output, warnings = Kramdown::Converter::Html.convert(@root, @options)
  @warnings.concat(warnings)
  output
end
```
