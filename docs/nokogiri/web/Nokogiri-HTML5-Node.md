# Module: Nokogiri::HTML5::Node
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    XML::Node
  
  

  
  
    Defined in:
    lib/nokogiri/html5/node.rb
  
  

## Overview

  
    

Since v1.12.0

💡 HTML5 functionality is not available when running JRuby.

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**fragment**(tags)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**inner_html**(options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**write_to**(io, *options) {|config| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**fragment**(tags)  ⇒ Object 
  

  

  

  
    
      

```

70
71
72
73
74
```

    
    
      

```
# File 'lib/nokogiri/html5/node.rb', line 70

def fragment(tags)
  return super unless document.is_a?(HTML5::Document)

  DocumentFragment.new(document, tags, self)
end

```

    
  

    
      
  
### 
  
    #**inner_html**(options = {})  ⇒ Object 
  

  

  

  
    
      

```

31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/nokogiri/html5/node.rb', line 31

def inner_html(options = {})
  return super unless document.is_a?(HTML5::Document)

  result = options[:preserve_newline] && prepend_newline? ? +"\n" : +""
  result << children.map { |child| child.to_html(options) }.join
  result
end

```

    
  

    
      
  
### 
  
    #**write_to**(io, *options) {|config| ... } ⇒ Object 
  

  

  

  
    

  

  

Yields:

  
    
- 
      
      
        (config)
      
      
      
    
  

  
    
      

```

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
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
```

    
    
      

```
# File 'lib/nokogiri/html5/node.rb', line 39

def write_to(io, *options)
  return super unless document.is_a?(HTML5::Document)

  options = options.first.is_a?(Hash) ? options.shift : {}
  encoding = options[:encoding] || options[0]
  if Nokogiri.jruby?
    save_options = options[:save_with] || options[1]
    indent_times = options[:indent] || 0
  else
    save_options = options[:save_with] || options[1] || XML::Node::SaveOptions::FORMAT
    indent_times = options[:indent] || 2
  end
  indent_string = (options[:indent_text] || " ") * indent_times

  config = XML::Node::SaveOptions.new(save_options.to_i)
  yield config if block_given?

  encoding = encoding.is_a?(Encoding) ? encoding.name : encoding

  config_options = config.options
  if config_options & (XML::Node::SaveOptions::AS_XML | XML::Node::SaveOptions::AS_XHTML) != 0
    # Use Nokogiri's serializing code.
    native_write_to(io, encoding, indent_string, config_options)
  else
    # Serialize including the current node.
    html = html_standard_serialize(options[:preserve_newline] || false)
    encoding ||= document.encoding || Encoding::UTF_8
    io << html.encode(encoding, fallback: lambda { |c| "&#x#{c.ord.to_s(16)};" })
  end
end

```