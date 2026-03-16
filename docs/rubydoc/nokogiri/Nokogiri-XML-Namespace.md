# Class: Nokogiri::XML::Namespace
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::Namespace
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      PP::Node
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/namespace.rb,

  ext/nokogiri/xml_namespace.c

  
  

  
## Constant Summary

  
  
### Constants included
     from PP::Node

  

PP::Node::COLLECTIONS

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**document**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute document.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**deconstruct_keys**(keys)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash.

  

      
        
- 
  
    
      #**href**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   href() → String.

  

      
        
- 
  
    
      #**prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   prefix() → String or nil.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from PP::Node

  

#inspect, #pretty_print

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**document**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute document.

  

  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/nokogiri/xml/namespace.rb', line 8

def document
  @document
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**deconstruct_keys**(keys)  ⇒ Object 
  

  

  

  
    

:call-seq: deconstruct_keys(array_of_names) → Hash

```
Returns a hash describing the Namespace, to use in pattern matching.

Valid keys and their values:
- +prefix+ → (String, nil) The namespace's prefix, or +nil+ if there is no prefix (e.g., default namespace).
- +href+ → (String) The namespace's URI

*Example*

  doc = Nokogiri::XML.parse(<<~XML)
    <?xml version="1.0"?>
    <root xmlns="http://nokogiri.org/ns/default" xmlns:noko="http://nokogiri.org/ns/noko">
      <child1 foo="abc" noko:bar="def"/>
      <noko:child2 foo="qwe" noko:bar="rty"/>
    </root>
  XML

  doc.root.elements.first.namespace
  # => #(Namespace:0x35c { href = "http://nokogiri.org/ns/default" })

  doc.root.elements.first.namespace.deconstruct_keys([:prefix, :href])
  # => {:prefix=>nil, :href=>"http://nokogiri.org/ns/default"}

  doc.root.elements.last.namespace
  # => #(Namespace:0x370 {
  #      prefix = "noko",
  #      href = "http://nokogiri.org/ns/noko"
  #      })

  doc.root.elements.last.namespace.deconstruct_keys([:prefix, :href])
  # => {:prefix=>"noko", :href=>"http://nokogiri.org/ns/noko"}

Since v1.14.0

```

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/nokogiri/xml/namespace.rb', line 46

def deconstruct_keys(keys)
  { prefix: prefix, href: href }
end
```

    
  

    
      
  
### 
  
    #**href**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
href() → String

```

Returns the URI reference for this Namespace.

**Example**

```
doc = Nokogiri::XML.parse(<<~XML)
  <?xml version="1.0"?>
  <root xmlns="http://nokogiri.org/ns/default" xmlns:noko="http://nokogiri.org/ns/noko">
    <child1 foo="abc" noko:bar="def"/>
    <noko:child2 foo="qwe" noko:bar="rty"/>
  </root>
XML

doc.root.elements.first.namespace.href
# => "http://nokogiri.org/ns/default"

doc.root.elements.last.namespace.href
# => "http://nokogiri.org/ns/noko"

```

  

  

  
    
      

```

126
127
128
129
130
131
132
133
134
135
```

    
    
      

```
# File 'ext/nokogiri/xml_namespace.c', line 126

static VALUE
href(VALUE self)
{
  xmlNsPtr ns;

  Noko_Namespace_Get_Struct(self, xmlNs, ns);
  if (!ns->href) { return Qnil; }

  return NOKOGIRI_STR_NEW2(ns->href);
}
```

    
  

    
      
  
### 
  
    #**prefix**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
prefix() → String or nil

```

Return the prefix for this Namespace, or `nil` if there is no prefix (e.g., default namespace).

**Example**

```
doc = Nokogiri::XML.parse(<<~XML)
  <?xml version="1.0"?>
  <root xmlns="http://nokogiri.org/ns/default" xmlns:noko="http://nokogiri.org/ns/noko">
    <child1 foo="abc" noko:bar="def"/>
    <noko:child2 foo="qwe" noko:bar="rty"/>
  </root>
XML

doc.root.elements.first.namespace.prefix
# => nil

doc.root.elements.last.namespace.prefix
# => "noko"

```

  

  

  
    
      

```

93
94
95
96
97
98
99
100
101
102
```

    
    
      

```
# File 'ext/nokogiri/xml_namespace.c', line 93

static VALUE
prefix(VALUE self)
{
  xmlNsPtr ns;

  Noko_Namespace_Get_Struct(self, xmlNs, ns);
  if (!ns->prefix) { return Qnil; }

  return NOKOGIRI_STR_NEW2(ns->prefix);
}
```