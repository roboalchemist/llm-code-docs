# Module: Kramdown::Converter
  
  
  

  

  
  
  
      Extended by:
      Utils::Configurable
  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter.rb,

  lib/kramdown/converter/man.rb,
 lib/kramdown/converter/toc.rb,
 lib/kramdown/converter/base.rb,
 lib/kramdown/converter/html.rb,
 lib/kramdown/converter/latex.rb,
 lib/kramdown/converter/hash_ast.rb,
 lib/kramdown/converter/kramdown.rb,
 lib/kramdown/converter/remove_html_tags.rb,
 lib/kramdown/converter/syntax_highlighter.rb

  
  

## Overview

  
    

This module contains all available converters, i.e. classes that take a root Element and convert it to a specific output format. The result is normally a string. For example, the Converter::Html module converts an element tree into valid HTML.

Converters use the Base class for common functionality (like applying a template to the output) - see its API documentation for how to create a custom converter class.

  

  

## Defined Under Namespace

  
    
      **Modules:** MathEngine, SyntaxHighlighter
    
  
    
      **Classes:** Base, HashAST, Html, Kramdown, Latex, Man, RemoveHtmlTags, Toc
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        HashAst =
          
        
        

```
HashAST

```

      
    
  

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from Utils::Configurable

  

configurable