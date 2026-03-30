# Class: Kramdown::Parser::Html
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Parser::Html
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Parser
  
  
  

  

  
  
    Defined in:
    lib/kramdown/parser/html.rb
  
  

## Overview

  
    

Used for parsing an HTML document.

The parsing code is in the Parser module that can also be used by other parsers.

  

  

## Defined Under Namespace

  
    
      **Modules:** Constants, Parser
    
  
    
      **Classes:** ElementConverter
    
  

  
## Constant Summary

  
  
### Constants included
     from Parser

  

Parser::HTML_RAW_START

  
  
  
### Constants included
     from Constants

  

Constants::HTML_ATTRIBUTE_RE, Constants::HTML_BLOCK_ELEMENTS, Constants::HTML_CDATA_RE, Constants::HTML_COMMENT_RE, Constants::HTML_CONTENT_MODEL, Constants::HTML_CONTENT_MODEL_BLOCK, Constants::HTML_CONTENT_MODEL_RAW, Constants::HTML_CONTENT_MODEL_SPAN, Constants::HTML_DOCTYPE_RE, Constants::HTML_ELEMENT, Constants::HTML_ELEMENTS_WITHOUT_BODY, Constants::HTML_ENTITY_RE, Constants::HTML_INSTRUCTION_RE, Constants::HTML_SPAN_ELEMENTS, Constants::HTML_TAG_CLOSE_RE, Constants::HTML_TAG_RE

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#options, #root, #source, #warnings

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**parse**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the source string provided on initialization as HTML document.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Parser

  

#handle_html_start_tag, #handle_raw_html_tag, #parse_html_attributes, #parse_raw_html

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#adapt_source, #add_text, #extract_string, #initialize, parse, #warning

  
## Constructor Details

  
    

This class inherits a constructor from Kramdown::Parser::Base
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**parse**  ⇒ Object 
  

  

  

  
    

Parse the source string provided on initialization as HTML document.

  

  

  
    
      

```

593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 593

def parse
  @stack, @tree = [], @root
  @src = Kramdown::Utils::StringScanner.new(adapt_source(source))

  while true
    if (result = @src.scan(/\s*#{HTML_INSTRUCTION_RE}/o))
      @tree.children << Element.new(:xml_pi, result.strip, nil, category: :block)
    elsif (result = @src.scan(/\s*#{HTML_DOCTYPE_RE}/o))
      # ignore the doctype
    elsif (result = @src.scan(/\s*#{HTML_COMMENT_RE}/o))
      @tree.children << Element.new(:xml_comment, result.strip, nil, category: :block)
    else
      break
    end
  end

  tag_handler = lambda do |c, closed, handle_body|
    parse_raw_html(c, &tag_handler) if !closed && handle_body
  end
  parse_raw_html(@tree, &tag_handler)

  ElementConverter.convert(@tree)
end
```