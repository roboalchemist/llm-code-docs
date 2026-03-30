# Class: Nokogiri::XML::Schema
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::Schema
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/schema.rb,

  ext/nokogiri/xml_schema.c

  
  

## Overview

  
    

Nokogiri::XML::Schema is used for validating XML against an XSD schema definition.

⚠ Since v1.11.0, Schema treats inputs as **untrusted** by default, and so external entities are not resolved from the network (`http://` or `ftp://`). When parsing a trusted document, the caller may turn off the `NONET` option via the ParseOptions to (re-)enable external entity resolution over a network connection.

🛡 Before v1.11.0, documents were “trusted” by default during schema parsing which was counter to Nokogiri’s “untrusted by default” security policy.

**Example:** Determine whether an XML document is valid.

```
schema = Nokogiri::XML::Schema.new(File.read(XSD_FILE))
doc = Nokogiri::XML::Document.parse(File.read(XML_FILE))
schema.valid?(doc) # Boolean

```

**Example:** Validate an XML document against an XSD schema, and capture any errors that are found.

```
schema = Nokogiri::XML::Schema.new(File.read(XSD_FILE))
doc = Nokogiri::XML::Document.parse(File.read(XML_FILE))
errors = schema.validate(doc) # Array<SyntaxError>

```

**Example:** Validate an XML document using a Document containing an XSD schema definition.

```
schema_doc = Nokogiri::XML::Document.parse(File.read(RELAX_NG_FILE))
schema = Nokogiri::XML::Schema.from_document(schema_doc)
doc = Nokogiri::XML::Document.parse(File.read(XML_FILE))
schema.valid?(doc) # Boolean

```

  

  

  
## Direct Known Subclasses

  

RelaxNG

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The errors found while parsing the XSD.

  

    
      
- 
  
    
      #**parse_options**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The options used to parse the schema.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**from_document**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   from_document(input) → Nokogiri::XML::Schema   from_document(input, parse_options) → Nokogiri::XML::Schema.

  

      
        
- 
  
    
      .**new**(input, parse_options_ = ParseOptions::DEFAULT_SCHEMA, parse_options: parse_options_)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   new(input) → Nokogiri::XML::Schema   new(input, parse_options) → Nokogiri::XML::Schema.

  

      
        
- 
  
    
      .**read_memory**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   read_memory(input) → Nokogiri::XML::Schema   read_memory(input, parse_options) → Nokogiri::XML::Schema.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**valid?**(input)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: valid?(input) → Boolean.

  

      
        
- 
  
    
      #**validate**(input)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: validate(input) → Array<SyntaxError>.

  

      
    

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    

The errors found while parsing the XSD
Returns

Array<Nokogiri::XML::SyntaxError>

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/nokogiri/xml/schema.rb', line 49

def errors
  @errors
end
```

    
  

    
      
      
      
  
### 
  
    #**parse_options**  ⇒ Object 
  

  

  

  
    

The options used to parse the schema
Returns

Nokogiri::XML::ParseOptions

  

  

  
    
      

```

54
55
56
```

    
    
      

```
# File 'lib/nokogiri/xml/schema.rb', line 54

def parse_options
  @parse_options
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**from_document**(*args)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
from_document(input) → Nokogiri::XML::Schema
from_document(input, parse_options) → Nokogiri::XML::Schema

```

Parse an XSD schema definition from a Document to create a new Nokogiri::XML::Schema
Parameters

- 

`input` (XML::Document) A document containing the XSD schema definition

- 

`parse_options` (Nokogiri::XML::ParseOptions) Defaults to Nokogiri::XML::ParseOptions::DEFAULT_SCHEMA

Returns

Nokogiri::XML::Schema

  

  

  
    
      

```

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
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
```

    
    
      

```
# File 'ext/nokogiri/xml_schema.c', line 169

static VALUE
noko_xml_schema_s_from_document(int argc, VALUE *argv, VALUE rb_class)
{
  /* TODO: deprecate this method and put file-or-string logic into .new so that becomes the
   * preferred entry point, and this can become a private method */
  VALUE rb_document;
  VALUE rb_parse_options;
  VALUE rb_schema;
  xmlDocPtr c_document;
  xmlSchemaParserCtxtPtr c_parser_context;
  int defensive_copy_p = 0;

  rb_scan_args(argc, argv, "11", &rb_document, &rb_parse_options);

  if (!rb_obj_is_kind_of(rb_document, cNokogiriXmlNode)) {
    rb_raise(rb_eTypeError,
             "expected parameter to be a Nokogiri::XML::Document, received %"PRIsVALUE,
             rb_obj_class(rb_document));
  }

  if (!rb_obj_is_kind_of(rb_document, cNokogiriXmlDocument)) {
    xmlNodePtr deprecated_node_type_arg;
    NOKO_WARN_DEPRECATION("Passing a Node as the first parameter to Schema.from_document is deprecated. Please pass a Document instead. This will become an error in Nokogiri v1.17.0."); // TODO: deprecated in v1.15.3, remove in v1.17.0
    Noko_Node_Get_Struct(rb_document, xmlNode, deprecated_node_type_arg);
    c_document = deprecated_node_type_arg->doc;
  } else {
    c_document = noko_xml_document_unwrap(rb_document);
  }

  if (noko_xml_document_has_wrapped_blank_nodes_p(c_document)) {
    // see https://github.com/sparklemotion/nokogiri/pull/2001
    c_document = xmlCopyDoc(c_document, 1);
    defensive_copy_p = 1;
  }

  c_parser_context = xmlSchemaNewDocParserCtxt(c_document);
  rb_schema = xml_schema_parse_schema(rb_class, c_parser_context, rb_parse_options);

  if (defensive_copy_p) {
    xmlFreeDoc(c_document);
    c_document = NULL;
  }

  return rb_schema;
}
```

    
  

    
      
  
### 
  
    .**new**(input, parse_options_ = ParseOptions::DEFAULT_SCHEMA, parse_options: parse_options_)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
new(input) → Nokogiri::XML::Schema
new(input, parse_options) → Nokogiri::XML::Schema

```

Parse an XSD schema definition from a String or IO to create a new Nokogiri::XML::Schema
Parameters

- 

`input` (String | IO) XSD schema definition

- 

`parse_options` (Nokogiri::XML::ParseOptions) Defaults to Nokogiri::XML::ParseOptions::DEFAULT_SCHEMA

Returns

Nokogiri::XML::Schema

  

  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/nokogiri/xml/schema.rb', line 69

def self.new(input, parse_options_ = ParseOptions::DEFAULT_SCHEMA, parse_options: parse_options_)
  from_document(Nokogiri::XML::Document.parse(input), parse_options)
end
```

    
  

    
      
  
### 
  
    .**read_memory**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
read_memory(input) → Nokogiri::XML::Schema
read_memory(input, parse_options) → Nokogiri::XML::Schema

```

Convenience method for Nokogiri::XML::Schema.new

  

  

  
    
      

```

78
79
80
81
```

    
    
      

```
# File 'lib/nokogiri/xml/schema.rb', line 78

def self.read_memory(...)
  # TODO deprecate this method
  new(...)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**valid?**(input)  ⇒ Boolean 
  

  

  

  
    

:call-seq: valid?(input) → Boolean

Validate `input` and return a Boolean indicating whether the document is valid
Parameters

- 

`input` (Nokogiri::XML::Document | String) A parsed document, or a string containing a local filename.

Returns

Boolean

**Example:** Validate an existing XML::Document

```
schema = Nokogiri::XML::Schema.new(File.read(XSD_FILE))
return unless schema.valid?(document)

```

**Example:** Validate an XML document on disk

```
schema = Nokogiri::XML::Schema.new(File.read(XSD_FILE))
return unless schema.valid?("/path/to/file.xml")

```

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

135
136
137
```

    
    
      

```
# File 'lib/nokogiri/xml/schema.rb', line 135

def valid?(input)
  validate(input).empty?
end
```

    
  

    
      
  
### 
  
    #**validate**(input)  ⇒ Object 
  

  

  

  
    

:call-seq: validate(input) → Array<SyntaxError>

Validate `input` and return any errors that are found.
Parameters

- 

`input` (Nokogiri::XML::Document | String) A parsed document, or a string containing a local filename.

Returns

Array<SyntaxError>

**Example:** Validate an existing XML::Document, and capture any errors that are found.

```
schema = Nokogiri::XML::Schema.new(File.read(XSD_FILE))
errors = schema.validate(document)

```

**Example:** Validate an XML document on disk, and capture any errors that are found.

```
schema = Nokogiri::XML::Schema.new(File.read(XSD_FILE))
errors = schema.validate("/path/to/file.xml")

```

  

  

  
    
      

```

104
105
106
107
108
109
110
111
112
```

    
    
      

```
# File 'lib/nokogiri/xml/schema.rb', line 104

def validate(input)
  if input.is_a?(Nokogiri::XML::Document)
    validate_document(input)
  elsif File.file?(input)
    validate_file(input)
  else
    raise ArgumentError, "Must provide Nokogiri::XML::Document or the name of an existing file"
  end
end
```