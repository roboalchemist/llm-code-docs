# Class: Kramdown::Document
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Kramdown::Document
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/document.rb
  
  

## Overview

  
    

The main interface to kramdown.

This class provides a one-stop-shop for using kramdown to convert text into various output formats. Use it like this:

```
require 'kramdown'
doc = Kramdown::Document.new('This *is* some kramdown text')
puts doc.to_html

```

The #to_html method is a shortcut for using the Converter::Html class. See #method_missing for more information.

The second argument to the ::new method is an options hash for customizing the behaviour of the used parser and the converter. See ::new for more information!

  

  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The options hash which holds the options for parsing/converting the Kramdown document.

  

    
      
- 
  
    
      #**root**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The root Element of the element tree.

  

    
      
- 
  
    
      #**warnings**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

An array of warning messages.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**initialize**(source, options = {})  ⇒ Document 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new Kramdown document from the string `source` and use the provided `options`.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**method_missing**(id, *attr, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Check if a method is invoked that begins with `to_` and if so, try to instantiate a converter class (i.e. a class in the Kramdown::Converter module) and use it for converting the document.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(source, options = {})  ⇒ Document 
  

  

  

  
    

Create a new Kramdown document from the string `source` and use the provided `options`. The options that can be used are defined in the Options module.

The special options key :input can be used to select the parser that should parse the `source`. It has to be the name of a class in the Kramdown::Parser module. For example, to select the kramdown parser, one would set the :input key to `Kramdown`. If this key is not set, it defaults to `Kramdown`.

The `source` is immediately parsed by the selected parser so that the root element is immediately available and the output can be generated.

  

  

  
    
      

```

96
97
98
99
100
101
102
103
104
105
106
107
```

    
    
      

```
# File 'lib/kramdown/document.rb', line 96

def initialize(source, options = {})
  @options = Options.merge(options).freeze
  parser = (@options[:input] || 'kramdown').to_s
  parser = parser[0..0].upcase + parser[1..-1]
  try_require('parser', parser)
  if Parser.const_defined?(parser)
    @root, @warnings = Parser.const_get(parser).parse(source, @options)
  else
    raise Kramdown::Error, "kramdown has no parser to handle the specified " \
      "input format: #{@options[:input]}"
  end
end

```

    
  

  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(id, *attr, &block)  ⇒ Object 
  

  

  

  
    

Check if a method is invoked that begins with `to_` and if so, try to instantiate a converter class (i.e. a class in the Kramdown::Converter module) and use it for converting the document.

For example, `to_html` would instantiate the Kramdown::Converter::Html class.

  

  

  
    
      

```

113
114
115
116
117
118
119
120
121
122
```

    
    
      

```
# File 'lib/kramdown/document.rb', line 113

def method_missing(id, *attr, &block)
  if id.to_s =~ /^to_(\w+)$/ && (name = Utils.camelize($1)) &&
      try_require('converter', name) && Converter.const_defined?(name)
    output, warnings = Converter.const_get(name).convert(@root, @options)
    @warnings.concat(warnings)
    output
  else
    super
  end
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

The options hash which holds the options for parsing/converting the Kramdown document.

  

  

  
    
      

```

80
81
82
```

    
    
      

```
# File 'lib/kramdown/document.rb', line 80

def options
  @options
end

```

    
  

    
      
      
      
  
### 
  
    #**root**  ⇒ Object 
  

  

  

  
    

The root Element of the element tree. It is immediately available after the ::new method has been called.

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/kramdown/document.rb', line 77

def root
  @root
end

```

    
  

    
      
      
      
  
### 
  
    #**warnings**  ⇒ Object  (readonly)
  

  

  

  
    

An array of warning messages. It is filled with warnings during the parsing phase (i.e. in ::new) and the conversion phase.

  

  

  
    
      

```

84
85
86
```

    
    
      

```
# File 'lib/kramdown/document.rb', line 84

def warnings
  @warnings
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/kramdown/document.rb', line 124

def inspect # :nodoc:
  "<KD:Document: options=#{@options.inspect} root=#{@root.inspect} warnings=#{@warnings.inspect}>"
end

```