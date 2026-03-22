# Module: Kramdown::Parser
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/parser.rb,

  lib/kramdown/parser/base.rb,
 lib/kramdown/parser/html.rb,
 lib/kramdown/parser/kramdown.rb,
 lib/kramdown/parser/markdown.rb,
 lib/kramdown/parser/kramdown/eob.rb,
 lib/kramdown/parser/kramdown/html.rb,
 lib/kramdown/parser/kramdown/link.rb,
 lib/kramdown/parser/kramdown/list.rb,
 lib/kramdown/parser/kramdown/math.rb,
 lib/kramdown/parser/kramdown/table.rb,
 lib/kramdown/parser/kramdown/header.rb,
 lib/kramdown/parser/kramdown/autolink.rb,
 lib/kramdown/parser/kramdown/codespan.rb,
 lib/kramdown/parser/kramdown/emphasis.rb,
 lib/kramdown/parser/kramdown/footnote.rb,
 lib/kramdown/parser/kramdown/codeblock.rb,
 lib/kramdown/parser/kramdown/paragraph.rb,
 lib/kramdown/parser/kramdown/blank_line.rb,
 lib/kramdown/parser/kramdown/blockquote.rb,
 lib/kramdown/parser/kramdown/extensions.rb,
 lib/kramdown/parser/kramdown/line_break.rb,
 lib/kramdown/parser/kramdown/html_entity.rb,
 lib/kramdown/parser/kramdown/abbreviation.rb,
 lib/kramdown/parser/kramdown/smart_quotes.rb,
 lib/kramdown/parser/kramdown/escaped_chars.rb,
 lib/kramdown/parser/kramdown/block_boundary.rb,
 lib/kramdown/parser/kramdown/horizontal_rule.rb,
 lib/kramdown/parser/kramdown/typographic_symbol.rb

  
  

## Overview

  
    

This module contains all available parsers. A parser takes an input string and converts the string to an element tree.

New parsers should be derived from the Base class which provides common functionality - see its API documentation for how to create a custom converter class.

  

  

## Defined Under Namespace

  
    
  
    
      **Classes:** Base, Html, Kramdown, Markdown