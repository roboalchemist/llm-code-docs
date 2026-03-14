# Class: Jekyll::Tags::HighlightBlock
  
    Inherits:
    
      Liquid::Block
      
        

          
- Object

- Liquid::Block

- Jekyll::Tags::HighlightBlock

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Liquid::StandardFilters
  
    Defined in:
    lib/jekyll/tags/highlight.rb
  
##

      Constant Summary
      collapse
    

    
      
        SYNTAX =
          
  
    

The regular expression syntax checker. Start with the language specifier. Follow that by zero or more space separated options that take one of three forms: name, name=value, or name=“<quoted list>”

<quoted list> is a space-separated list of numbers

```
%r!^([a-zA-Z0-9.+#_-]+)((\s+\w+(=(\w+|"([0-9]+\s)*[0-9]+"))?)*)$!.freeze

```

        LEADING_OR_TRAILING_LINE_TERMINATORS =
          
        
        

```
%r!\A(\n|\r)+|(\n|\r)+\z!.freeze

```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(tag_name, markup, tokens)  ⇒ HighlightBlock 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of HighlightBlock.

-
  
      #**render**(context)  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(tag_name, markup, tokens)  ⇒ HighlightBlock 
  

  

  

  
    

Returns a new instance of HighlightBlock.

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
```

```
# File 'lib/jekyll/tags/highlight.rb', line 15

def initialize(tag_name, markup, tokens)
  super
  if markup.strip =~ SYNTAX
    @lang = Regexp.last_match(1).downcase
    @highlight_options = parse_options(Regexp.last_match(2))
  else
    raise SyntaxError, "      Syntax Error in tag 'highlight' while parsing the following markup:\n\n      \#{markup}\n\n      Valid syntax: highlight <lang> [linenos] [mark_lines=\"3 4 5\"]\n\n      See https://jekyllrb.com/docs/liquid/tags/#code-snippet-highlighting for more details.\n    MSG\n  end\nend\n"

```

## Instance Method Details

###
  
    #**render**(context)  ⇒ Object 
  

  

  

  
    
      

```

35
36
37
38
39
40
41
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
```

```
# File 'lib/jekyll/tags/highlight.rb', line 35

def render(context)
  prefix = context["highlighter_prefix"] || ""
  suffix = context["highlighter_suffix"] || ""
  code = super.to_s.gsub(LEADING_OR_TRAILING_LINE_TERMINATORS, "")

  output =
    case context.registers[:site].highlighter
    when "rouge"
      render_rouge(code)
    when "pygments"
      render_pygments(code, context)
    else
      render_codehighlighter(code)
    end

  rendered_output = add_code_tag(output)
  prefix + rendered_output + suffix
end

```
