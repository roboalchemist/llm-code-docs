# Class: XSD::XMLParser::Nokogiri
  
  
  

  
  
    Inherits:
    
      Parser
      
        

          
- Object
          
            
- Parser
          
            
- XSD::XMLParser::Nokogiri
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/xsd/xmlparser/nokogiri.rb
  
  

## Overview

  
    

Nokogiri XML parser for soap4r.

Nokogiri may be used as the XML parser in soap4r. Require ‘xsd/xmlparser/nokogiri’ in your soap4r applications, and soap4r will use Nokogiri as its XML parser. No other changes should be required to use Nokogiri as the XML parser.

Example (using UW ITS Web Services):

```
require 'rubygems'
require 'nokogiri'
gem 'soap4r'
require 'defaultDriver'
require 'xsd/xmlparser/nokogiri'

obj = AvlPortType.new
obj.getLatestByRoute(obj.getAgencies.first, 8).each do |bus|
  p "#{bus.routeID}, #{bus.longitude}, #{bus.latitude}"
end

```

  

  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**cdata_block**(string)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Handle cdata_blocks containing `string`.

  

      
        
- 
  
    
      #**do_parse**(string_or_readable)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Start parsing `string_or_readable`.

  

      
        
- 
  
    
      #**end_element**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Handle the end_element event with `name`.

  

      
        
- 
  
    
      #**end_element_namespace**(name, prefix = nil, uri = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Called at the end of an element `name` is the element’s name `prefix` is the namespace prefix associated with the element `uri` is the associated namespace URI.

  

      
        
- 
  
    
      #**error**(msg)  ⇒ Object 
    

    
      (also: #warning)
    
  
  
  
  
  
  
  
  

  
    

Handle errors with message `msg`.

  

      
        
- 
  
    
      #**initialize**(host, opt = {})  ⇒ Nokogiri 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new XSD parser with `host` and `opt`.

  

      
        
- 
  
    
      #**start_element**(name, attrs = [])  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Handle the start_element event with `name` and `attrs`.

  

      
        
- 
  
    
      #**start_element_namespace**(name, attrs = [], prefix = nil, uri = nil, ns = [])  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Called at the beginning of an element `name` is the element name `attrs` is a list of attributes `prefix` is the namespace prefix for the element `uri` is the associated namespace URI `ns` is a hash of namespace prefix:urls associated with the element.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(host, opt = {})  ⇒ Nokogiri 
  

  

  

  
    

Create a new XSD parser with `host` and `opt`

  

  

  
    
      

```

30
31
32
33
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 30

def initialize(host, opt = {})
  super
  @parser = ::Nokogiri::XML::SAX::Parser.new(self, @charset || "UTF-8")
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**cdata_block**(string)  ⇒ Object 
  

  

  

  
    

Handle cdata_blocks containing `string`

  

  

  
    
      

```

62
63
64
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 62

def cdata_block(string)
  characters(string)
end

```

    
  

    
      
  
### 
  
    #**do_parse**(string_or_readable)  ⇒ Object 
  

  

  

  
    

Start parsing `string_or_readable`

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 37

def do_parse(string_or_readable)
  @parser.parse(string_or_readable)
end

```

    
  

    
      
  
### 
  
    #**end_element**(name)  ⇒ Object 
  

  

  

  
    

Handle the end_element event with `name`

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 49

def end_element(name)
  super
end

```

    
  

    
      
  
### 
  
    #**end_element_namespace**(name, prefix = nil, uri = nil)  ⇒ Object 
  

  

  

  
    

Called at the end of an element `name` is the element’s name `prefix` is the namespace prefix associated with the element `uri` is the associated namespace URI

  

  

  
    
      

```

90
91
92
93
94
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 90

def end_element_namespace(name, prefix = nil, uri = nil)
  ###
  # Deal with SAX v1 interface
  end_element([prefix, name].compact.join(":"))
end

```

    
  

    
      
  
### 
  
    #**error**(msg)  ⇒ Object 
  

  
    Also known as:
    warning
    
  

  

  
    

Handle errors with message `msg`

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

55
56
57
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 55

def error(msg)
  raise ParseError, msg
end

```

    
  

    
      
  
### 
  
    #**start_element**(name, attrs = [])  ⇒ Object 
  

  

  

  
    

Handle the start_element event with `name` and `attrs`

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 43

def start_element(name, attrs = [])
  super(name, Hash[*attrs.flatten])
end

```

    
  

    
      
  
### 
  
    #**start_element_namespace**(name, attrs = [], prefix = nil, uri = nil, ns = [])  ⇒ Object 
  

  

  

  
    

Called at the beginning of an element `name` is the element name `attrs` is a list of attributes `prefix` is the namespace prefix for the element `uri` is the associated namespace URI `ns` is a hash of namespace prefix:urls associated with the element

  

  

  
    
      

```

73
74
75
76
77
78
79
80
81
82
83
```

    
    
      

```
# File 'lib/xsd/xmlparser/nokogiri.rb', line 73

def start_element_namespace(name, attrs = [], prefix = nil, uri = nil, ns = []) # rubocop:disable Metrics/ParameterLists
  ###
  # Deal with SAX v1 interface
  name = [prefix, name].compact.join(":")
  attributes = ns.map do |ns_prefix, ns_uri|
    [["xmlns", ns_prefix].compact.join(":"), ns_uri]
  end + attrs.map do |attr|
    [[attr.prefix, attr.localname].compact.join(":"), attr.value]
  end.flatten
  start_element(name, attributes)
end

```