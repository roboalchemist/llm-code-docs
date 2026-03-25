# Module: Kramdown
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Parser::Kramdown
  
  

  
  
    Defined in:
    lib/kramdown/error.rb,

  lib/kramdown/utils.rb,
 lib/kramdown/parser.rb,
 lib/kramdown/element.rb,
 lib/kramdown/options.rb,
 lib/kramdown/version.rb,
 lib/kramdown/document.rb,
 lib/kramdown/converter.rb,
 lib/kramdown/utils/html.rb,
 lib/kramdown/parser/base.rb,
 lib/kramdown/parser/html.rb,
 lib/kramdown/converter/man.rb,
 lib/kramdown/converter/toc.rb,
 lib/kramdown/converter/base.rb,
 lib/kramdown/converter/html.rb,
 lib/kramdown/utils/entities.rb,
 lib/kramdown/converter/latex.rb,
 lib/kramdown/parser/kramdown.rb,
 lib/kramdown/parser/markdown.rb,
 lib/kramdown/utils/lru_cache.rb,
 lib/kramdown/utils/unidecoder.rb,
 lib/kramdown/converter/hash_ast.rb,
 lib/kramdown/converter/kramdown.rb,
 lib/kramdown/utils/configurable.rb,
 lib/kramdown/parser/kramdown/eob.rb,
 lib/kramdown/parser/kramdown/html.rb,
 lib/kramdown/parser/kramdown/link.rb,
 lib/kramdown/parser/kramdown/list.rb,
 lib/kramdown/parser/kramdown/math.rb,
 lib/kramdown/utils/string_scanner.rb,
 lib/kramdown/parser/kramdown/table.rb,
 lib/kramdown/parser/kramdown/header.rb,
 lib/kramdown/parser/kramdown/autolink.rb,
 lib/kramdown/parser/kramdown/codespan.rb,
 lib/kramdown/parser/kramdown/emphasis.rb,
 lib/kramdown/parser/kramdown/footnote.rb,
 lib/kramdown/parser/kramdown/codeblock.rb,
 lib/kramdown/parser/kramdown/paragraph.rb,
 lib/kramdown/converter/remove_html_tags.rb,
 lib/kramdown/parser/kramdown/blank_line.rb,
 lib/kramdown/parser/kramdown/blockquote.rb,
 lib/kramdown/parser/kramdown/extensions.rb,
 lib/kramdown/parser/kramdown/line_break.rb,
 lib/kramdown/parser/kramdown/html_entity.rb,
 lib/kramdown/converter/syntax_highlighter.rb,
 lib/kramdown/parser/kramdown/abbreviation.rb,
 lib/kramdown/parser/kramdown/smart_quotes.rb,
 lib/kramdown/parser/kramdown/escaped_chars.rb,
 lib/kramdown/parser/kramdown/block_boundary.rb,
 lib/kramdown/parser/kramdown/horizontal_rule.rb,
 lib/kramdown/parser/kramdown/typographic_symbol.rb

  
  

## Overview

  
    

– Copyright © 2009-2026 Thomas Leitner <[email protected]>

This file is part of kramdown which is licensed under the MIT. ++

  

  

## Defined Under Namespace

  
    
      **Modules:** Converter, Options, Parser, Utils
    
  
    
      **Classes:** Document, Element, Error
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
  
    

The kramdown version.

  

  

        
        

```
'2.5.2'

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**data_dir**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the data directory for kramdown.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**data_dir**  ⇒ Object 
  

  

  

  
    

Return the data directory for kramdown.

  

  

  
    
      

```

49
50
51
52
53
54
55
56
57
```

    
    
      

```
# File 'lib/kramdown/document.rb', line 49

def self.data_dir
  unless defined?(@data_dir)
    require 'rbconfig'
    @data_dir = File.expand_path(File.join(File.dirname(__FILE__), '..', '..', 'data', 'kramdown'))
    @data_dir = File.expand_path(File.join(RbConfig::CONFIG["datadir"], "kramdown")) unless File.exist?(@data_dir)
    raise "kramdown data directory not found! This is a bug, please report it!" unless File.directory?(@data_dir)
  end
  @data_dir
end

```