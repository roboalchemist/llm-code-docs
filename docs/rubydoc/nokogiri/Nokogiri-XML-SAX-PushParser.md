# Class: Nokogiri::XML::SAX::PushParser
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::SAX::PushParser
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/sax/push_parser.rb,

  ext/nokogiri/xml_sax_push_parser.c

  
  

## Overview

  
    

PushParser can parse a document that is fed to it manually.  It must be given a SAX::Document object which will be called with SAX events as the document is being parsed.

Calling PushParser#<< writes XML to the parser, calling any SAX callbacks it can.

PushParser#finish tells the parser that the document is finished and calls the end_document SAX method.

Example:

```
parser = PushParser.new(Class.new(XML::SAX::Document) {
  def start_document
    puts "start document called"
  end
}.new)
parser << "<div>hello<"
parser << "/div>"
parser.finish

```

  

  

  
## Direct Known Subclasses

  

HTML4::SAX::PushParser

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**document**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The Nokogiri::XML::SAX::Document on which the PushParser will be operating.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**finish**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Finish the parsing.

  

      
        
- 
  
    
      #**initialize**(doc = XML::SAX::Document.new, file_name = nil, encoding = "UTF-8")  ⇒ PushParser 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Create a new PushParser with `doc` as the SAX Document, providing an optional `file_name` and `encoding`.

  

      
        
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**options=**(options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**replace_entities**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Document@Entity+Handling for an explanation of the behavior controlled by this flag.

  

      
        
- 
  
    
      #**replace_entities=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Document@Entity+Handling for an explanation of the behavior controlled by this flag.

  

      
        
- 
  
    
      #**write**(chunk, last_chunk = false)  ⇒ Object 
    

    
      (also: #<<)
    
  
  
  
  
  
  
  
  

  
    

Write a `chunk` of XML to the PushParser.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(doc = XML::SAX::Document.new, file_name = nil, encoding = "UTF-8")  ⇒ PushParser 
  

  

  

  
    

Create a new PushParser with `doc` as the SAX Document, providing an optional `file_name` and `encoding`

  

  

  
    
      

```

35
36
37
38
39
40
41
42
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/push_parser.rb', line 35

def initialize(doc = XML::SAX::Document.new, file_name = nil, encoding = "UTF-8")
  @document = doc
  @encoding = encoding
  @sax_parser = XML::SAX::Parser.new(doc)

  ## Create our push parser context
  initialize_native(@sax_parser, file_name)
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**document**  ⇒ Object 
  

  

  

  
    

The Nokogiri::XML::SAX::Document on which the PushParser will be operating

  

  

  
    
      

```

30
31
32
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/push_parser.rb', line 30

def document
  @document
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**finish**  ⇒ Object 
  

  

  

  
    

Finish the parsing.  This method is only necessary for Nokogiri::XML::SAX::Document#end_document to be called.

⚠ Note that empty documents are treated as an error when using the libxml2-based implementation (CRuby), but are fine when using the Xerces-based implementation (JRuby).

  

  

  
    
      

```

58
59
60
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/push_parser.rb', line 58

def finish
  write("", true)
end

```

    
  

    
      
  
### 
  
    #**options**  ⇒ Object 
  

  

  

  
    
      

```

103
104
105
106
107
108
109
110
111
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_push_parser.c', line 103

static VALUE
noko_xml_sax_push_parser__options_get(VALUE self)
{
  xmlParserCtxtPtr ctx;

  ctx = noko_xml_sax_push_parser_unwrap(self);

  return INT2NUM(xmlCtxtGetOptions(ctx));
}

```

    
  

    
      
  
### 
  
    #**options=**(options)  ⇒ Object 
  

  

  

  
    
      

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
123
124
125
126
127
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_push_parser.c', line 113

static VALUE
noko_xml_sax_push_parser__options_set(VALUE self, VALUE options)
{
  int error;
  xmlParserCtxtPtr ctx;

  ctx = noko_xml_sax_push_parser_unwrap(self);

  error = xmlCtxtSetOptions(ctx, (int)NUM2INT(options));
  if (error) {
    rb_raise(rb_eRuntimeError, "Cannot set XML parser context options (%x)", error);
  }

  return Qnil;
}

```

    
  

    
      
  
### 
  
    #**replace_entities**  ⇒ Object 
  

  

  

  
    

See Document@Entity+Handling for an explanation of the behavior controlled by this flag.
Returns

(Boolean) Value of the parse option. (Default `false`)

This option is perhaps misnamed by the libxml2 author, since it controls resolution and not replacement.

  

  
  

  
    
      

```

140
141
142
143
144
145
146
147
148
149
150
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_push_parser.c', line 140

static VALUE
noko_xml_sax_push_parser__replace_entities_get(VALUE self)
{
  xmlParserCtxtPtr ctxt = noko_xml_sax_push_parser_unwrap(self);

  if (xmlCtxtGetOptions(ctxt) & XML_PARSE_NOENT) {
    return Qtrue;
  } else {
    return Qfalse;
  }
}

```

    
  

    
      
  
### 
  
    #**replace_entities=**(value)  ⇒ Object 
  

  

  

  
    

See Document@Entity+Handling for an explanation of the behavior controlled by this flag.
Parameters

- 

`value` (Boolean) Whether external parsed entities will be resolved.

⚠ **It is UNSAFE to set this option to `true`** when parsing untrusted documents. The option defaults to `false` for this reason.

This option is perhaps misnamed by the libxml2 author, since it controls resolution and not replacement.

  

  
  

  
    
      

```

167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_push_parser.c', line 167

static VALUE
noko_xml_sax_push_parser__replace_entities_set(VALUE self, VALUE value)
{
  int error;
  xmlParserCtxtPtr ctxt = noko_xml_sax_push_parser_unwrap(self);

  if (RB_TEST(value)) {
    error = xmlCtxtSetOptions(ctxt, xmlCtxtGetOptions(ctxt) | XML_PARSE_NOENT);
  } else {
    error = xmlCtxtSetOptions(ctxt, xmlCtxtGetOptions(ctxt) & ~XML_PARSE_NOENT);
  }

  if (error) {
    rb_raise(rb_eRuntimeError, "failed to set parser context options (%x)", error);
  }

  return value;
}

```

    
  

    
      
  
### 
  
    #**write**(chunk, last_chunk = false)  ⇒ Object 
  

  
    Also known as:
    <<
    
  

  

  
    

Write a `chunk` of XML to the PushParser.  Any callback methods that can be called will be called immediately.

  

  

  
    
      

```

47
48
49
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/push_parser.rb', line 47

def write(chunk, last_chunk = false)
  native_write(chunk, last_chunk)
end

```