# Class: Nokogiri::HTML4::SAX::Parser
  
  
  

  
  
    Inherits:
    
      XML::SAX::Parser
      
        

          
- Object
          
            
- XML::SAX::Parser
          
            
- Nokogiri::HTML4::SAX::Parser
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/sax/parser.rb,

  ext/nokogiri/html4_sax_parser.c

  
  

## Overview

  
    

This parser is a SAX style parser that reads its input as it deems necessary. The parser takes a Nokogiri::XML::SAX::Document, an optional encoding, then given an HTML input, sends messages to the Nokogiri::XML::SAX::Document.

⚠ This is an HTML4 parser and so may not support some HTML5 features and behaviors.

Here is a basic usage example:

```
class MyHandler < Nokogiri::XML::SAX::Document
  def start_element name, attributes = []
    puts "found a #{name}"
  end
end

parser = Nokogiri::HTML4::SAX::Parser.new(MyHandler.new)

# Hand an IO object to the parser, which will read the HTML from the IO.
File.open(path_to_html) do |f|
  parser.parse(f)
end

```

For more information on SAX parsers, see Nokogiri::XML::SAX or the parent class Nokogiri::XML::SAX::Parser.

Also see Nokogiri::XML::SAX::Document for the available events.

  

  

  
## Constant Summary

  
  
### Constants inherited
     from XML::SAX::Parser

  

XML::SAX::Parser::ENCODINGS, XML::SAX::Parser::REVERSE_ENCODINGS

  
  
  
### Constants included
     from ClassResolver

  

ClassResolver::VALID_NAMESPACES

  
## Instance Attribute Summary

  
  
### Attributes inherited from XML::SAX::Parser

  

#document, #encoding

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods inherited from XML::SAX::Parser

  

#initialize, #parse, #parse_file, #parse_io, #parse_memory

  
  
  
  
  
  
  
  
  
### Methods included from ClassResolver

  

#related_class

  
## Constructor Details

  
    

This class inherits a constructor from Nokogiri::XML::SAX::Parser