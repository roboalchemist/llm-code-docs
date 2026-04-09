# Class: Nokogiri::XML::RelaxNG
  
  
  

  
  
    Inherits:
    
      Schema
      
        

          
- Object
          
            
- Schema
          
            
- Nokogiri::XML::RelaxNG
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/relax_ng.rb,

  ext/nokogiri/xml_relax_ng.c

  
  

## Overview

  
    

Nokogiri::XML::RelaxNG is used for validating XML against a RELAX NG schema definition.

🛡 **Do not use this class for untrusted schema documents.** RELAX NG input is always treated as **trusted**, meaning that the underlying parsing libraries **will access network resources**. This is counter to Nokogiri’s “untrusted by default” security policy, but is an unfortunate limitation of the underlying libraries.

**Example:** Determine whether an XML document is valid.

```
schema = Nokogiri::XML::RelaxNG.new(File.read(RELAX_NG_FILE))
doc = Nokogiri::XML::Document.parse(File.read(XML_FILE))
schema.valid?(doc) # Boolean

```

**Example:** Validate an XML document against a RelaxNG schema, and capture any errors that are found.

```
schema = Nokogiri::XML::RelaxNG.new(File.open(RELAX_NG_FILE))
doc = Nokogiri::XML::Document.parse(File.open(XML_FILE))
errors = schema.validate(doc) # Array<SyntaxError>

```

**Example:** Validate an XML document using a Document containing a RELAX NG schema definition.

```
schema_doc = Nokogiri::XML::Document.parse(File.read(RELAX_NG_FILE))
schema = Nokogiri::XML::RelaxNG.from_document(schema_doc)
doc = Nokogiri::XML::Document.parse(File.open(XML_FILE))
schema.valid?(doc) # Boolean

```

  

  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Schema

  

#errors, #parse_options

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**from_document**(*args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   from_document(document) → Nokogiri::XML::RelaxNG   from_document(document, parse_options) → Nokogiri::XML::RelaxNG.

  

      
        
- 
  
    
      .**new**(input, parse_options_ = ParseOptions::DEFAULT_SCHEMA, options: parse_options_)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   new(input) → Nokogiri::XML::RelaxNG   new(input, options:) → Nokogiri::XML::RelaxNG.

  

      
        
- 
  
    
      .**read_memory**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   read_memory(input) → Nokogiri::XML::RelaxNG   read_memory(input, options:) → Nokogiri::XML::RelaxNG.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Schema

  

#valid?, #validate

  
    
## Class Method Details

    
      
  
### 
  
    .**from_document**(*args)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
from_document(document) 
```

Parse a RELAX NG schema definition from a Document to create a new Nokogiri::XML::RelaxNG.
Parameters

- 

`document` (XML::Document) A document containing the RELAX NG schema definition

- 

`parse_options` (Nokogiri::XML::ParseOptions) Defaults to ParseOptions::DEFAULT_SCHEMA ⚠ Unused

Returns

Nokogiri::XML::RelaxNG

⚠ `parse_options` is currently unused by this method and is present only as a placeholder for future functionality.

  

  

  
    
      

```

120
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
132
133
134
135
136
137
138
```

    
    
      

```
# File 'ext/nokogiri/xml_relax_ng.c', line 120

static VALUE
noko_xml_relax_ng_s_from_document(int argc, VALUE *argv, VALUE rb_class)
{
  /* TODO: deprecate this method and put file-or-string logic into .new so that becomes the
   * preferred entry point, and this can become a private method */
  VALUE rb_document;
  VALUE rb_parse_options;
  xmlDocPtr c_document;
  xmlRelaxNGParserCtxtPtr c_parser_context;

  rb_scan_args(argc, argv, "11", &rb_document, &rb_parse_options);

  c_document = noko_xml_document_unwrap(rb_document);
  c_document = c_document->doc; /* In case someone passes us a node. ugh. */

  c_parser_context = xmlRelaxNGNewDocParserCtxt(c_document);

  return _noko_xml_relax_ng_parse_schema(rb_class, c_parser_context, rb_parse_options);
}

```

    
  

    
      
  
### 
  
    .**new**(input, parse_options_ = ParseOptions::DEFAULT_SCHEMA, options: parse_options_)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
new(input) 
```

Parse a RELAX NG schema definition from a String or IO to create a new Nokogiri::XML::RelaxNG.
Parameters

- 

`input` (String | IO) RELAX NG schema definition

- 

`options:` (Nokogiri::XML::ParseOptions) Defaults to Nokogiri::XML::ParseOptions::DEFAULT_SCHEMA ⚠ Unused

Returns

Nokogiri::XML::RelaxNG

⚠ `parse_options` is currently unused by this method and is present only as a placeholder for future functionality.

Also see convenience method Nokogiri::XML::RelaxNG()

  

  

  
    
      

```

60
61
62
```

    
    
      

```
# File 'lib/nokogiri/xml/relax_ng.rb', line 60

def self.new(input, parse_options_ = ParseOptions::DEFAULT_SCHEMA, options: parse_options_)
  from_document(Nokogiri::XML::Document.parse(input), options)
end

```

    
  

    
      
  
### 
  
    .**read_memory**  ⇒ Object 
  

  

  

  
    

:call-seq:

```
read_memory(input) 
```

Convenience method for Nokogiri::XML::RelaxNG.new.

  

  

  
    
      

```

69
70
71
72
```

    
    
      

```
# File 'lib/nokogiri/xml/relax_ng.rb', line 69

def self.read_memory(...)
  # TODO deprecate this method
  new(...)
end

```