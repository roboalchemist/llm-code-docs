# Class: Kramdown::Parser::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Kramdown::Parser::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/parser/base.rb
  
  

## Overview

  
    

## Base class for parsers

This class serves as base class for parsers. It provides common methods that can/should be used by all parsers, especially by those using StringScanner(Kramdown) for parsing.

A parser object is used as a throw-away object, i.e. it is only used for storing the needed state information during parsing. Therefore one can’t instantiate a parser object directly but only use the Base::parse method.

## Implementing a parser

Implementing a new parser is rather easy: just derive a new class from this class and put it in the Kramdown::Parser module – the latter is needed so that the auto-detection of the new parser works correctly. Then you need to implement the `#parse` method which has to contain the parsing code.

Have a look at the Base::parse, Base::new and Base#parse methods for additional information!

  

  

  
## Direct Known Subclasses

  

Html, Kramdown

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The hash with the parsing options.

  

    
      
- 
  
    
      #**root**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The root element of element tree that is created from the source string.

  

    
      
- 
  
    
      #**source**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The original source string.

  

    
      
- 
  
    
      #**warnings**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The array with the parser warnings.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**parse**(source, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the `source` string into an element tree, possibly using the parsing `options`, and return the root element of the element tree and an array with warning messages.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**adapt_source**(source)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Modify the string `source` to be usable by the parser (unifies line ending characters to `\n` and makes sure `source` ends with a new line character).

  

      
        
- 
  
    
      #**add_text**(text, tree = @tree, type = @text_type)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This helper method adds the given `text` either to the last element in the `tree` if it is a `type` element or creates a new text element with the given `type`.

  

      
        
- 
  
    
      #**extract_string**(range, strscan)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Extract the part of the StringScanner `strscan` backed string specified by the `range`.

  

      
        
- 
  
    
      #**initialize**(source, options)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize the parser object with the `source` string and the parsing `options`.

  

      
        
- 
  
    
      #**parse**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse the source string into an element tree.

  

      
        
- 
  
    
      #**warning**(text)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add the given warning `text` to the warning array.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(source, options)  ⇒ Base 
  

  

  

  
    

Initialize the parser object with the `source` string and the parsing `options`.

The @root element, the @warnings array and @text_type (specifies the default type for newly created text nodes) are automatically initialized.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 52

def initialize(source, options)
  @source = source
  @options = Kramdown::Options.merge(options)
  @root = Element.new(:root, nil, nil, encoding: (source.encoding rescue nil), location: 1,
                      options: {}, abbrev_defs: {}, abbrev_attr: {})

  @root.options[:abbrev_defs].default_proc = @root.options[:abbrev_attr].default_proc =
    lambda do |h, k|
      k_mod = k.gsub(/[\s\p{Z}]+/, " ")
      k != k_mod ? h[k_mod] : nil
    end
  @warnings = []
  @text_type = :text
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

The hash with the parsing options.

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 37

def options
  @options
end

```

    
  

    
      
      
      
  
### 
  
    #**root**  ⇒ Object  (readonly)
  

  

  

  
    

The root element of element tree that is created from the source string.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 46

def root
  @root
end

```

    
  

    
      
      
      
  
### 
  
    #**source**  ⇒ Object  (readonly)
  

  

  

  
    

The original source string.

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 43

def source
  @source
end

```

    
  

    
      
      
      
  
### 
  
    #**warnings**  ⇒ Object  (readonly)
  

  

  

  
    

The array with the parser warnings.

  

  

  
    
      

```

40
41
42
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 40

def warnings
  @warnings
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**parse**(source, options = {})  ⇒ Object 
  

  

  

  
    

Parse the `source` string into an element tree, possibly using the parsing `options`, and return the root element of the element tree and an array with warning messages.

Initializes a new instance of the calling class and then calls the `#parse` method that must be implemented by each subclass.

  

  

  
    
      

```

73
74
75
76
77
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 73

def self.parse(source, options = {})
  parser = new(source, options)
  parser.parse
  [parser.root, parser.warnings]
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**adapt_source**(source)  ⇒ Object 
  

  

  

  
    

Modify the string `source` to be usable by the parser (unifies line ending characters to `\n` and makes sure `source` ends with a new line character).

  

  

  
    
      

```

97
98
99
100
101
102
103
104
105
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 97

def adapt_source(source)
  unless source.valid_encoding?
    raise "The source text contains invalid characters for the used encoding #{source.encoding}"
  end
  source = source.encode('UTF-8')
  source.gsub!(/\r\n?/, "\n")
  source.chomp!
  source << "\n"
end

```

    
  

    
      
  
### 
  
    #**add_text**(text, tree = @tree, type = @text_type)  ⇒ Object 
  

  

  

  
    

This helper method adds the given `text` either to the last element in the `tree` if it is a `type` element or creates a new text element with the given `type`.

  

  

  
    
      

```

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
# File 'lib/kramdown/parser/base.rb', line 109

def add_text(text, tree = @tree, type = @text_type)
  last = tree.children.last
  if last && last.type == type
    last.value << text
  elsif !text.empty?
    location = (last && last.options[:location] || tree.options[:location])
    tree.children << Element.new(type, text, nil, location: location)
  end
end

```

    
  

    
      
  
### 
  
    #**extract_string**(range, strscan)  ⇒ Object 
  

  

  

  
    

Extract the part of the StringScanner `strscan` backed string specified by the `range`. This method works correctly under Ruby 1.8 and Ruby 1.9.

  

  

  
    
      

```

121
122
123
124
125
126
127
128
129
130
131
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 121

def extract_string(range, strscan)
  result = nil
  begin
    enc = strscan.string.encoding
    strscan.string.force_encoding('ASCII-8BIT')
    result = strscan.string[range].force_encoding(enc)
  ensure
    strscan.string.force_encoding(enc)
  end
  result
end

```

    
  

    
      
  
### 
  
    #**parse**  ⇒ Object 
  

  

  

  
    

Parse the source string into an element tree.

The parsing code should parse the source provided in @source and build an element tree the root of which should be @root.

This is the only method that has to be implemented by sub-classes!

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

85
86
87
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 85

def parse
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**warning**(text)  ⇒ Object 
  

  

  

  
    

Add the given warning `text` to the warning array.

  

  

  
    
      

```

90
91
92
93
```

    
    
      

```
# File 'lib/kramdown/parser/base.rb', line 90

def warning(text)
  @warnings << text
  # TODO: add position information
end

```