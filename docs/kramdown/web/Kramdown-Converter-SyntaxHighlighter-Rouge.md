# Module: Kramdown::Converter::SyntaxHighlighter::Rouge
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/syntax_highlighter/rouge.rb
  
  

## Overview

  
    

Uses Rouge which is CSS-compatible to Pygments to highlight code blocks and code spans.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**call**(converter, text, lang, type, call_opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**formatter_class**(opts = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**normalize_keys**(hash)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**options**(converter, type)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**prepare_options**(converter)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**call**(converter, text, lang, type, call_opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/syntax_highlighter/rouge.rb', line 24

def self.call(converter, text, lang, type, call_opts)
  opts = options(converter, type)
  call_opts[:default_lang] = opts[:default_lang]
  return nil unless lang || opts[:default_lang] || opts[:guess_lang]

  lexer = ::Rouge::Lexer.find_fancy(lang || opts[:default_lang], text)
  return nil if opts[:disable] || !lexer || (lexer.tag == "plaintext" && !opts[:guess_lang])

  opts[:css_class] ||= 'highlight' # For backward compatibility when using Rouge 2.0
  formatter = formatter_class(opts).new(opts)
  formatter.format(lexer.lex(text))
end

```

    
  

    
      
  
### 
  
    .**formatter_class**(opts = {})  ⇒ Object 
  

  

  

  
    
      

```

68
69
70
71
72
73
74
75
76
77
78
79
80
81
```

    
    
      

```
# File 'lib/kramdown/converter/syntax_highlighter/rouge.rb', line 68

def self.formatter_class(opts = {})
  case formatter = opts[:formatter]
  when Class
    formatter
  when /\A[[:upper:]][[:alnum:]_]*\z/
    ::Rouge::Formatters.const_get(formatter, false)
  else
    # Available in Rouge 2.0 or later
    ::Rouge::Formatters::HTMLLegacy
  end
rescue NameError
  # Fallback to Rouge 1.x
  ::Rouge::Formatters::HTML
end

```

    
  

    
      
  
### 
  
    .**normalize_keys**(hash)  ⇒ Object 
  

  

  

  
    
      

```

60
61
62
63
64
65
66
```

    
    
      

```
# File 'lib/kramdown/converter/syntax_highlighter/rouge.rb', line 60

def self.normalize_keys(hash)
  return if hash.empty?

  hash.keys.each do |k|
    hash[k.kind_of?(String) ? Kramdown::Options.str_to_sym(k) : k] = hash.delete(k)
  end
end

```

    
  

    
      
  
### 
  
    .**options**(converter, type)  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
40
```

    
    
      

```
# File 'lib/kramdown/converter/syntax_highlighter/rouge.rb', line 37

def self.options(converter, type)
  prepare_options(converter)
  converter.data[:syntax_highlighter_rouge][type]
end

```

    
  

    
      
  
### 
  
    .**prepare_options**(converter)  ⇒ Object 
  

  

  

  
    
      

```

42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
```

    
    
      

```
# File 'lib/kramdown/converter/syntax_highlighter/rouge.rb', line 42

def self.prepare_options(converter)
  return if converter.data.key?(:syntax_highlighter_rouge)

  cache = converter.data[:syntax_highlighter_rouge] = {}

  opts = converter.options[:syntax_highlighter_opts].dup

  span_opts = opts.delete(:span)&.dup || {}
  block_opts = opts.delete(:block)&.dup || {}
  normalize_keys(span_opts)
  normalize_keys(block_opts)

  cache[:span] = opts.merge(span_opts)
  cache[:span][:wrap] = false

  cache[:block] = opts.merge(block_opts)
end

```