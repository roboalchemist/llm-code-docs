# Module: Kramdown::Utils::Html
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Converter::Html, Converter::Kramdown, Parser::Kramdown
  
  

  
  
    Defined in:
    lib/kramdown/utils/html.rb
  
  

## Overview

  
    

Provides convenience methods for HTML related tasks.

**Note** that this module has to be mixed into a class that has a @root (containing an element of type :root) and an @options (containing an options hash) instance variable so that some of the methods can work correctly.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ESCAPE_MAP =
          
  
    

:stopdoc:

  

  

        
        

```
{
  '<' => '<',
  '>' => '>',
  '&' => '&',
  '"' => '"',
}

```

      
        ESCAPE_ALL_RE =
          
        
        

```
/<|>|&/

```

      
        ESCAPE_TEXT_RE =
          
        
        

```
Regexp.union(REXML::Parsers::BaseParser::REFERENCE_RE, /<|>|&/)

```

      
        ESCAPE_ATTRIBUTE_RE =
          
        
        

```
Regexp.union(REXML::Parsers::BaseParser::REFERENCE_RE, /<|>|&|"/)

```

      
        ESCAPE_RE_FROM_TYPE =
          
        
        

```
{all: ESCAPE_ALL_RE, text: ESCAPE_TEXT_RE, attribute: ESCAPE_ATTRIBUTE_RE}

```

      
        REDUNDANT_LINE_BREAK_REGEX =
          
        
        

```
/([\p{Han}\p{Hiragana}\p{Katakana}]+)\n([\p{Han}\p{Hiragana}\p{Katakana}]+)/u

```

      
    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**entity_to_str**(e, original = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert the entity `e` to a string.

  

      
        
- 
  
    
      #**escape_html**(str, type = :all)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Escape the special HTML characters in the string `str`.

  

      
        
- 
  
    
      #**fix_cjk_line_break**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**html_attributes**(attr)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the HTML representation of the attributes `attr`.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**entity_to_str**(e, original = nil)  ⇒ Object 
  

  

  

  
    

Convert the entity `e` to a string. The optional parameter `original` may contain the original representation of the entity.

This method uses the option `entity_output` to determine the output form for the entity.

  

  

  
    
      

```

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
39
40
41
```

    
    
      

```
# File 'lib/kramdown/utils/html.rb', line 27

def entity_to_str(e, original = nil)
  entity_output = @options[:entity_output]

  if entity_output == :as_char &&
      (c = e.char.encode(@root.options[:encoding]) rescue nil) &&
      ((c = e.char) == '"' || !ESCAPE_MAP.key?(c))
    c
  elsif (entity_output == :as_input || entity_output == :as_char) && original
    original
  elsif (entity_output == :symbolic || ESCAPE_MAP.key?(e.char)) && !e.name.nil?
    "&#{e.name};"
  else # default to :numeric
    "&##{e.code_point};"
  end
end

```

    
  

    
      
  
### 
  
    #**escape_html**(str, type = :all)  ⇒ Object 
  

  

  

  
    

Escape the special HTML characters in the string `str`. The parameter `type` specifies what is escaped: :all - all special HTML characters except the quotation mark as well as entities, :text - all special HTML characters except the quotation mark but no entities and :attribute - all special HTML characters including the quotation mark but no entities.

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/kramdown/utils/html.rb', line 69

def escape_html(str, type = :all)
  str.gsub(ESCAPE_RE_FROM_TYPE[type]) {|m| ESCAPE_MAP[m] || m }
end

```

    
  

    
      
  
### 
  
    #**fix_cjk_line_break**(str)  ⇒ Object 
  

  

  

  
    
      

```

74
75
76
77
78
```

    
    
      

```
# File 'lib/kramdown/utils/html.rb', line 74

def fix_cjk_line_break(str)
  while str.gsub!(REDUNDANT_LINE_BREAK_REGEX, '\1\2')
  end
  str
end

```

    
  

    
      
  
### 
  
    #**html_attributes**(attr)  ⇒ Object 
  

  

  

  
    

Return the HTML representation of the attributes `attr`.

  

  

  
    
      

```

44
45
46
47
48
49
50
```

    
    
      

```
# File 'lib/kramdown/utils/html.rb', line 44

def html_attributes(attr)
  return '' if attr.empty?

  attr.map do |k, v|
    v.nil? || (k == 'id' && v.strip.empty?) ? '' : " #{k}=\"#{escape_html(v.to_s, :attribute)}\""
  end.join
end

```