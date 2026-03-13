# Class: Jekyll::Converters::Markdown::KramdownParser
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Converters::Markdown::KramdownParser

        show all
      

    Defined in:
    lib/jekyll/converters/markdown/kramdown_parser.rb
  
##

      Constant Summary
      collapse
    

    
      
        CODERAY_DEFAULTS =
          
        
        

```
{
  "css"               => "style",
  "bold_every"        => 10,
  "line_numbers"      => "inline",
  "line_number_start" => 1,
  "tab_width"         => 4,
  "wrap"              => "div",
}.freeze
```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**convert**(content)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(config)  ⇒ KramdownParser 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of KramdownParser.

-
  
      #**setup**  ⇒ Object 

Setup and normalize the configuration:   * Create Kramdown if it doesn’t exist.

## Constructor Details

###
  
    #**initialize**(config)  ⇒ KramdownParser 
  

  

  

  
    

Returns a new instance of KramdownParser.

```

84
85
86
87
88
89
90
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 84

def initialize(config)
  @main_fallback_highlighter = config["highlighter"] || "rouge"
  @config = config["kramdown"] || {}
  @highlighter = nil
  setup
  load_dependencies
end
```

## Instance Method Details

###
  
    #**convert**(content)  ⇒ Object 
  

  

  

  
    
      

```

108
109
110
111
112
113
114
115
116
117
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 108

def convert(content)
  document = Kramdown::JekyllDocument.new(content, @config)
  html_output = document.to_html
  if @config["show_warnings"]
    document.warnings.each do |warning|
      Jekyll.logger.warn "Kramdown warning:", warning
    end
  end
  html_output
end
```

###
  
    #**setup**  ⇒ Object 
  

  

  

  
    

Setup and normalize the configuration:

```
* Create Kramdown if it doesn't exist.
* Set syntax_highlighter, detecting enable_coderay and merging
    highlighter if none.
* Merge kramdown[coderay] into syntax_highlighter_opts stripping coderay_.
* Make sure `syntax_highlighter_opts` exists.

```

```

99
100
101
102
103
104
105
106
```

```
# File 'lib/jekyll/converters/markdown/kramdown_parser.rb', line 99

def setup
  @config["syntax_highlighter"] ||= highlighter
  @config["syntax_highlighter_opts"] ||= {}
  @config["syntax_highlighter_opts"]["default_lang"] ||= "plaintext"
  @config["syntax_highlighter_opts"]["guess_lang"] = @config["guess_lang"]
  @config["coderay"] ||= {} # XXX: Legacy.
  modernize_coderay_config
end
```
