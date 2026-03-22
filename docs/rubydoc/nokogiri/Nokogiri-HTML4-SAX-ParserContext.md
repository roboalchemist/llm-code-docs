# Class: Nokogiri::HTML4::SAX::ParserContext
  
  
  

  
  
    Inherits:
    
      XML::SAX::ParserContext
      
        

          
- Object
          
            
- XML::SAX::ParserContext
          
            
- Nokogiri::HTML4::SAX::ParserContext
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/sax/parser_context.rb,

  ext/nokogiri/html4_sax_parser_context.c

  
  

## Overview

  
    

Context object to invoke the HTML4 SAX parser on the SAX::Document handler.

💡 This class is usually not instantiated by the user. Use Nokogiri::HTML4::SAX::Parser instead.

  

  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**native_file**(rb_filename, rb_encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**native_memory**(rb_input, rb_encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**parse_with**(rb_sax_parser)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from XML::SAX::ParserContext

  

#column, file, io, #line, memory, native_io, new, #recovery, #recovery=, #replace_entities, #replace_entities=

  
    
## Class Method Details

    
      
  
### 
  
    .**native_file**(rb_filename, rb_encoding)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

35
36
37
38
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
```

    
    
      

```
# File 'ext/nokogiri/html4_sax_parser_context.c', line 35

static VALUE
noko_html4_sax_parser_context_s_native_file(VALUE rb_class, VALUE rb_filename, VALUE rb_encoding)
{
  if (!NIL_P(rb_encoding) && !rb_obj_is_kind_of(rb_encoding, rb_cEncoding)) {
    rb_raise(rb_eTypeError, "argument must be an Encoding object");
  }

  htmlParserCtxtPtr c_context = htmlCreateFileParserCtxt(StringValueCStr(rb_filename), NULL);
  if (!c_context) {
    rb_raise(rb_eRuntimeError, "failed to create xml sax parser context");
  }

  noko_xml_sax_parser_context_set_encoding(c_context, rb_encoding);

  if (c_context->sax) {
    xmlFree(c_context->sax);
    c_context->sax = NULL;
  }

  return noko_xml_sax_parser_context_wrap(rb_class, c_context);
}

```

    
  

    
      
  
### 
  
    .**native_memory**(rb_input, rb_encoding)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
```

    
    
      

```
# File 'ext/nokogiri/html4_sax_parser_context.c', line 6

static VALUE
noko_html4_sax_parser_context_s_native_memory(VALUE rb_class, VALUE rb_input, VALUE rb_encoding)
{
  Check_Type(rb_input, T_STRING);
  if (!(int)RSTRING_LEN(rb_input)) {
    rb_raise(rb_eRuntimeError, "input string cannot be empty");
  }

  if (!NIL_P(rb_encoding) && !rb_obj_is_kind_of(rb_encoding, rb_cEncoding)) {
    rb_raise(rb_eTypeError, "argument must be an Encoding object");
  }

  htmlParserCtxtPtr c_context =
    htmlCreateMemoryParserCtxt(StringValuePtr(rb_input), (int)RSTRING_LEN(rb_input));
  if (!c_context) {
    rb_raise(rb_eRuntimeError, "failed to create xml sax parser context");
  }

  noko_xml_sax_parser_context_set_encoding(c_context, rb_encoding);

  if (c_context->sax) {
    xmlFree(c_context->sax);
    c_context->sax = NULL;
  }

  return noko_xml_sax_parser_context_wrap(rb_class, c_context);
}

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**parse_with**(rb_sax_parser)  ⇒ Object 
  

  

  

  
    
      

```

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
69
70
71
72
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
```

    
    
      

```
# File 'ext/nokogiri/html4_sax_parser_context.c', line 57

static VALUE
noko_html4_sax_parser_context__parse_with(VALUE rb_context, VALUE rb_sax_parser)
{
  htmlParserCtxtPtr ctxt;
  htmlSAXHandlerPtr sax;

  if (!rb_obj_is_kind_of(rb_sax_parser, cNokogiriXmlSaxParser)) {
    rb_raise(rb_eArgError, "argument must be a Nokogiri::XML::SAX::Parser");
  }

  ctxt = noko_xml_sax_parser_context_unwrap(rb_context);
  sax = noko_xml_sax_parser_unwrap(rb_sax_parser);

  ctxt->sax = sax;
  ctxt->userData = ctxt; /* so we can use libxml2/SAX2.c handlers if we want to */
  ctxt->_private = (void *)rb_sax_parser;

  xmlSetStructuredErrorFunc(NULL, NULL);

  /* although we're calling back into Ruby here, we don't need to worry about exceptions, because we
   * don't have any cleanup to do. The only memory we need to free is handled by
   * xml_sax_parser_context_type_free */
  htmlParseDocument(ctxt);

  return Qnil;
}

```