# Class: Nokogiri::XML::ElementContent
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::ElementContent
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      PP::Node
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/element_content.rb,

  ext/nokogiri/xml_element_content.c

  
  

## Overview

  
    

Represents the allowed content in an Element Declaration inside a DTD:

```
<?xml version="1.0"?><?TEST-STYLE PIDATA?>
<!DOCTYPE staff SYSTEM "staff.dtd" [
   <!ELEMENT div1 (head, (p | list | note)*, div2*)>
]>
</root>

```

ElementContent represents the binary tree inside the <!ELEMENT> tag shown above that lists the possible content for the div1 tag.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        PCDATA =
          
  
    

Possible definitions of type

  

  

        
        

```
1

```

      
        ELEMENT =
          
        
        

```
2

```

      
        SEQ =
          
        
        

```
3

```

      
        OR =
          
        
        

```
4

```

      
        ONCE =
          
  
    

Possible content occurrences

  

  

        
        

```
1

```

      
        OPT =
          
        
        

```
2

```

      
        MULT =
          
        
        

```
3

```

      
        PLUS =
          
        
        

```
4

```

      
    
  

  
  
  
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
  
    
      #**children**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the children of this ElementContent node.

  

      
        
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    Returns

The content element’s `name`.

  

      
        
- 
  
    
      #**occur**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    Returns

The content element’s `occur` flag.

  

      
        
- 
  
    
      #**prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    Returns

The content element’s namespace `prefix`.

  

      
        
- 
  
    
      #**type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    Returns

The content element’s `type`.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from PP::Node

  

#inspect, #pretty_print

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**document**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute document.

  

  

  
    
      

```

31
32
33
```

    
    
      

```
# File 'lib/nokogiri/xml/element_content.rb', line 31

def document
  @document
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**children**  ⇒ Object 
  

  

  

  
    

Get the children of this ElementContent node

  

  

  
    
      

```

35
36
37
```

    
    
      

```
# File 'lib/nokogiri/xml/element_content.rb', line 35

def children
  [c1, c2].compact
end

```

    
  

    
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    Returns

The content element’s `name`

  

  

  
    
      

```

16
17
18
19
20
21
22
23
24
```

    
    
      

```
# File 'ext/nokogiri/xml_element_content.c', line 16

static VALUE
get_name(VALUE self)
{
  xmlElementContentPtr elem;
  TypedData_Get_Struct(self, xmlElementContent, &xml_element_content_type, elem);

  if (!elem->name) { return Qnil; }
  return NOKOGIRI_STR_NEW2(elem->name);
}

```

    
  

    
      
  
### 
  
    #**occur**  ⇒ Object 
  

  

  

  
    Returns

The content element’s `occur` flag. Possible values are `ONCE`, `OPT`, `MULT` or `PLUS`.

  

  

  
    
      

```

73
74
75
76
77
78
79
80
```

    
    
      

```
# File 'ext/nokogiri/xml_element_content.c', line 73

static VALUE
get_occur(VALUE self)
{
  xmlElementContentPtr elem;
  TypedData_Get_Struct(self, xmlElementContent, &xml_element_content_type, elem);

  return INT2NUM(elem->ocur);
}

```

    
  

    
      
  
### 
  
    #**prefix**  ⇒ Object 
  

  

  

  
    Returns

The content element’s namespace `prefix`.

  

  

  
    
      

```

88
89
90
91
92
93
94
95
96
97
```

    
    
      

```
# File 'ext/nokogiri/xml_element_content.c', line 88

static VALUE
get_prefix(VALUE self)
{
  xmlElementContentPtr elem;
  TypedData_Get_Struct(self, xmlElementContent, &xml_element_content_type, elem);

  if (!elem->prefix) { return Qnil; }

  return NOKOGIRI_STR_NEW2(elem->prefix);
}

```

    
  

    
      
  
### 
  
    #**type**  ⇒ Object 
  

  

  

  
    Returns

The content element’s `type`. Possible values are `PCDATA`, `ELEMENT`, `SEQ`, or `OR`.

  

  

  
    
      

```

32
33
34
35
36
37
38
39
```

    
    
      

```
# File 'ext/nokogiri/xml_element_content.c', line 32

static VALUE
get_type(VALUE self)
{
  xmlElementContentPtr elem;
  TypedData_Get_Struct(self, xmlElementContent, &xml_element_content_type, elem);

  return INT2NUM(elem->type);
}

```