# Class: Nokogiri::XML::ParseOptions
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::ParseOptions
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/parse_options.rb
  
  

## Overview

  
    

Options that control the parsing behavior for XML::Document, XML::DocumentFragment, HTML4::Document, HTML4::DocumentFragment, XSLT::Stylesheet, and XML::Schema.

These options directly expose libxml2’s parse options, which are all boolean in the sense that an option is “on” or “off”.

💡 Note that HTML5 parsing has a separate, orthogonal set of options due to the nature of the HTML5 specification. See Nokogiri::HTML5.

⚠ Not all parse options are supported on JRuby. Nokogiri will attempt to invoke the equivalent behavior in Xerces/NekoHTML on JRuby when it’s possible.

## Setting and unsetting parse options

You can build your own combinations of parse options by using any of the following methods:
ParseOptions method chaining

Every option has an equivalent method in lowercase. You can chain these methods together to set various combinations.

```
# Set the HUGE & PEDANTIC options
po = Nokogiri::XML::ParseOptions.new.huge.pedantic
doc = Nokogiri::XML::Document.parse(xml, nil, nil, po)

```

Every option has an equivalent `no{option}` method in lowercase. You can call these methods on an instance of ParseOptions to unset the option.

```
# Set the HUGE & PEDANTIC options
po = Nokogiri::XML::ParseOptions.new.huge.pedantic

# later we want to modify the options
po.nohuge # Unset the HUGE option
po.nopedantic # Unset the PEDANTIC option

```

💡 Note that some options begin with “no” leading to the logical but perhaps unintuitive double negative:

```
po.nocdata # Set the NOCDATA parse option
po.nonocdata # Unset the NOCDATA parse option

```

💡 Note that negation is not available for STRICT, which is itself a negation of all other features.
Using Ruby Blocks

Most parsing methods will accept a block for configuration of parse options, and we recommend chaining the setter methods:

```
doc = Nokogiri::XML::Document.parse(xml) { |config| config.huge.pedantic }

```

ParseOptions constants

You can also use the constants declared under Nokogiri::XML::ParseOptions to set various combinations. They are bits in a bitmask, and so can be combined with bitwise operators:

```
po = Nokogiri::XML::ParseOptions.new(Nokogiri::XML::ParseOptions::HUGE | Nokogiri::XML::ParseOptions::PEDANTIC)
doc = Nokogiri::XML::Document.parse(xml, nil, nil, po)

```

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        STRICT =
          
  
    

Strict parsing

  

  

        
        

```
0
```

      
        RECOVER =
          
  
    

Recover from errors. On by default for XML::Document, XML::DocumentFragment, HTML4::Document, HTML4::DocumentFragment, XSLT::Stylesheet, and XML::Schema.

  

  

        
        

```
1 << 0
```

      
        NOENT =
          
  
    

Substitute entities. Off by default.

⚠ This option enables entity substitution, contrary to what the name implies.

⚠ **It is UNSAFE to set this option** when parsing untrusted documents.

  

  

        
        

```
1 << 1
```

      
        DTDLOAD =
          
  
    

Load external subsets. On by default for XSLT::Stylesheet.

⚠ **It is UNSAFE to set this option** when parsing untrusted documents.

  

  

        
        

```
1 << 2
```

      
        DTDATTR =
          
  
    

Default DTD attributes. On by default for XSLT::Stylesheet.

  

  

        
        

```
1 << 3
```

      
        DTDVALID =
          
  
    

Validate with the DTD. Off by default.

  

  

        
        

```
1 << 4
```

      
        NOERROR =
          
  
    

Suppress error reports. On by default for HTML4::Document and HTML4::DocumentFragment

  

  

        
        

```
1 << 5
```

      
        NOWARNING =
          
  
    

Suppress warning reports. On by default for HTML4::Document and HTML4::DocumentFragment

  

  

        
        

```
1 << 6
```

      
        PEDANTIC =
          
  
    

Enable pedantic error reporting. Off by default.

  

  

        
        

```
1 << 7
```

      
        NOBLANKS =
          
  
    

Remove blank nodes. Off by default.

  

  

        
        

```
1 << 8
```

      
        SAX1 =
          
  
    

Use the SAX1 interface internally. Off by default.

  

  

        
        

```
1 << 9
```

      
        XINCLUDE =
          
  
    

Implement XInclude substitution. Off by default.

  

  

        
        

```
1 << 10
```

      
        NONET =
          
  
    

Forbid network access. On by default for XML::Document, XML::DocumentFragment, HTML4::Document, HTML4::DocumentFragment, XSLT::Stylesheet, and XML::Schema.

⚠ **It is UNSAFE to unset this option** when parsing untrusted documents.

  

  

        
        

```
1 << 11
```

      
        NODICT =
          
  
    

Do not reuse the context dictionary. Off by default.

  

  

        
        

```
1 << 12
```

      
        NSCLEAN =
          
  
    

Remove redundant namespaces declarations. Off by default.

  

  

        
        

```
1 << 13
```

      
        NOCDATA =
          
  
    

Merge CDATA as text nodes. On by default for XSLT::Stylesheet.

  

  

        
        

```
1 << 14
```

      
        NOXINCNODE =
          
  
    

Do not generate XInclude START/END nodes. Off by default.

  

  

        
        

```
1 << 15
```

      
        COMPACT =
          
  
    

Compact small text nodes. Off by default.

⚠ No modification of the DOM tree is allowed after parsing. libxml2 may crash if you try to modify the tree.

  

  

        
        

```
1 << 16
```

      
        OLD10 =
          
  
    

Parse using XML-1.0 before update 5. Off by default

  

  

        
        

```
1 << 17
```

      
        NOBASEFIX =
          
  
    

Do not fixup XInclude xml:base uris. Off by default

  

  

        
        

```
1 << 18
```

      
        HUGE =
          
  
    

Relax any hardcoded limit from the parser. Off by default.

⚠ **It is UNSAFE to set this option** when parsing untrusted documents.

  

  

        
        

```
1 << 19
```

      
        BIG_LINES =
          
  
    

Support line numbers up to `long int` (default is a `short int`). On by default for for XML::Document, XML::DocumentFragment, HTML4::Document, HTML4::DocumentFragment, XSLT::Stylesheet, and XML::Schema.

  

  

        
        

```
1 << 22
```

      
        DEFAULT_XML =
          
  
    

The options mask used by default for parsing XML::Document and XML::DocumentFragment

  

  

        
        

```
RECOVER | NONET | BIG_LINES
```

      
        DEFAULT_XSLT =
          
  
    

The options mask used by default used for parsing XSLT::Stylesheet

  

  

        
        

```
RECOVER | NONET | NOENT | DTDLOAD | DTDATTR | NOCDATA | BIG_LINES
```

      
        DEFAULT_HTML =
          
  
    

The options mask used by default used for parsing HTML4::Document and HTML4::DocumentFragment

  

  

        
        

```
RECOVER | NOERROR | NOWARNING | NONET | BIG_LINES
```

      
        DEFAULT_SCHEMA =
          
  
    

The options mask used by default used for parsing XML::Schema

  

  

        
        

```
NONET | BIG_LINES
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
      (also: #to_i)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute options.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(options = STRICT)  ⇒ ParseOptions 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of ParseOptions.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**strict**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**strict?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(options = STRICT)  ⇒ ParseOptions 
  

  

  

  
    

Returns a new instance of ParseOptions.

  

  

  
    
      

```

165
166
167
```

    
    
      

```
# File 'lib/nokogiri/xml/parse_options.rb', line 165

def initialize(options = STRICT)
  @options = options
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**options**  ⇒ Object 
  

  
    Also known as:
    to_i
    
  

  

  
    

Returns the value of attribute options.

  

  

  
    
      

```

163
164
165
```

    
    
      

```
# File 'lib/nokogiri/xml/parse_options.rb', line 163

def options
  @options
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    
      

```

198
199
200
```

    
    
      

```
# File 'lib/nokogiri/xml/parse_options.rb', line 198

def ==(other)
  other.to_i == to_i
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    
      

```

204
205
206
207
208
209
210
```

    
    
      

```
# File 'lib/nokogiri/xml/parse_options.rb', line 204

def inspect
  options = []
  self.class.constants.each do |k|
    options << k.downcase if send(:"#{k.downcase}?")
  end
  super.sub(/>$/, " " + options.join(", ") + ">")
end
```

    
  

    
      
  
### 
  
    #**strict**  ⇒ Object 
  

  

  

  
    
      

```

189
190
191
192
```

    
    
      

```
# File 'lib/nokogiri/xml/parse_options.rb', line 189

def strict
  @options &= ~RECOVER
  self
end
```

    
  

    
      
  
### 
  
    #**strict?**  ⇒ Boolean 
  

  

  

  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

194
195
196
```

    
    
      

```
# File 'lib/nokogiri/xml/parse_options.rb', line 194

def strict?
  @options & RECOVER == STRICT
end
```