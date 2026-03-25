# Module: Kramdown::Converter::SyntaxHighlighter::Minted
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/syntax_highlighter/minted.rb
  
  

## Overview

  
    

Uses Minted to highlight code blocks and code spans.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**call**(converter, text, lang, type, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**call**(converter, text, lang, type, _opts)  ⇒ Object 
  

  

  

  
    
      

```

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
30
31
32
33
```

    
    
      

```
# File 'lib/kramdown/converter/syntax_highlighter/minted.rb', line 15

def self.call(converter, text, lang, type, _opts)
  opts = converter.options[:syntax_highlighter_opts]

  # Fallback to default language
  lang ||= opts[:default_lang]

  options = []
  options << "breaklines" if opts[:wrap]
  options << "linenos" if opts[:line_numbers]
  options << "frame=#{opts[:frame]}" if opts[:frame]

  if lang && type == :block
    "\\begin{minted}[#{options.join(',')}]{#{lang}}\n#{text}\n\\end{minted}"
  elsif lang && type == :span
    "\\mintinline{#{lang}}{#{text}}"
  else
    nil
  end
end

```