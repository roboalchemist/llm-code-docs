# Module: Kramdown::Parser::Html::Constants
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Converter::Html, ElementConverter, Parser
  
  

  
  
    Defined in:
    lib/kramdown/parser/html.rb
  
  

## Overview

  
    

Contains all constants that are used when parsing.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        HTML_DOCTYPE_RE =
          
  
    

:stopdoc: The following regexps are based on the ones used by REXML, with some slight modifications.

  

  

        
        

```
/<!DOCTYPE.*?>/im
```

      
        HTML_COMMENT_RE =
          
        
        

```
/<!--(.*?)-->/m
```

      
        HTML_INSTRUCTION_RE =
          
        
        

```
/<\?(.*?)\?>/m
```

      
        HTML_CDATA_RE =
          
        
        

```
/<!\[CDATA\[(.*?)\]\]>/m
```

      
        HTML_ATTRIBUTE_RE =
          
        
        

```
/\s*(#{REXML::Parsers::BaseParser::UNAME_STR})(?:\s*=\s*(?:(\p{Word}+)|("|')(.*?)\3))?/m
```

      
        HTML_TAG_RE =
          
        
        

```
/<((?>#{REXML::Parsers::BaseParser::UNAME_STR}))\s*((?>\s+#{REXML::Parsers::BaseParser::UNAME_STR}(?:\s*=\s*(?:\p{Word}+|("|').*?\3))?)*)\s*(\/)?>/m
```

      
        HTML_TAG_CLOSE_RE =
          
        
        

```
/<\/(#{REXML::Parsers::BaseParser::UNAME_STR})\s*>/m
```

      
        HTML_ENTITY_RE =
          
        
        

```
/&([\w:][\w.:-]*);|&#(\d+);|&\#x([0-9a-fA-F]+);/
```

      
        HTML_CONTENT_MODEL_BLOCK =
          
        
        

```
%w[address applet article aside blockquote body
dd details div dl fieldset figure figcaption
footer form header hgroup iframe li main
map menu nav noscript object section summary td]
```

      
        HTML_CONTENT_MODEL_SPAN =
          
        
        

```
%w[a abbr acronym b bdo big button cite caption del dfn dt em
h1 h2 h3 h4 h5 h6 i ins label legend optgroup p q rb rbc
rp rt rtc ruby select small span strong sub sup th tt]
```

      
        HTML_CONTENT_MODEL_RAW =
          
        
        

```
%w[script style math option textarea pre code kbd samp var]
```

      
        HTML_CONTENT_MODEL =
          
  
    

The following elements are also parsed as raw since they need child elements that cannot be expressed using kramdown syntax: colgroup table tbody thead tfoot tr ul ol

  

  

        
        

```
Hash.new {|h, k| h[k] = :raw }
```

      
        HTML_SPAN_ELEMENTS =
          
  
    

Some HTML elements like script belong to both categories (i.e. are valid in block and span HTML) and don’t appear therefore! script, textarea

  

  

        
        

```
%w[a abbr acronym b big bdo br button cite code del dfn em i img input
ins kbd label mark option q rb rbc rp rt rtc ruby samp select small
span strong sub sup time tt u var]
```

      
        HTML_BLOCK_ELEMENTS =
          
        
        

```
%w[address article aside applet body blockquote caption col colgroup
dd div dl dt fieldset figcaption footer form h1 h2 h3 h4 h5 h6
header hgroup hr html head iframe legend menu li main map nav ol
optgroup p pre section summary table tbody td th thead tfoot tr ul]
```

      
        HTML_ELEMENTS_WITHOUT_BODY =
          
        
        

```
%w[area base br col command embed hr img input keygen link
meta param source track wbr]
```

      
        HTML_ELEMENT =
          
        
        

```
Hash.new(false)
```