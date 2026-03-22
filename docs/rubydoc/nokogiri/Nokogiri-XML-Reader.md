# Class: Nokogiri::XML::Reader
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::Reader
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Enumerable
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/reader.rb,

  ext/nokogiri/xml_reader.c

  
  

## Overview

  
    

The Reader parser allows you to effectively pull parse an XML document.  Once instantiated, call Nokogiri::XML::Reader#each to iterate over each node.

Nokogiri::XML::Reader parses an XML document similar to the way a cursor would move. The Reader is given an XML document, and yields nodes to an each block.

The Reader parser might be good for when you need the speed and low memory usage of a SAX parser, but do not want to write a SAX::Document handler.

Here is an example of usage:

```
reader = Nokogiri::XML::Reader.new <<~XML
  <x xmlns:tenderlove='http://tenderlovemaking.com/'>
    <tenderlove:foo awesome='true'>snuggles!</tenderlove:foo>
  </x>
XML

reader.each do |node|
  # node is an instance of Nokogiri::XML::Reader
  puts node.name
end

```

⚠ Nokogiri::XML::Reader#each can only be called once! Once the cursor moves through the entire document, you must parse the document again. It may be better to capture all information you need during a single iteration.

⚠ libxml2 does not support error recovery in the Reader parser. The `RECOVER` ParseOption is ignored. If a syntax error is encountered during parsing, an exception will be raised.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        TYPE_NONE =
          
        
        

```
0
```

      
        TYPE_ELEMENT =
          
  
    

Element node type

  

  

        
        

```
1
```

      
        TYPE_ATTRIBUTE =
          
  
    

Attribute node type

  

  

        
        

```
2
```

      
        TYPE_TEXT =
          
  
    

Text node type

  

  

        
        

```
3
```

      
        TYPE_CDATA =
          
  
    

CDATA node type

  

  

        
        

```
4
```

      
        TYPE_ENTITY_REFERENCE =
          
  
    

Entity Reference node type

  

  

        
        

```
5
```

      
        TYPE_ENTITY =
          
  
    

Entity node type

  

  

        
        

```
6
```

      
        TYPE_PROCESSING_INSTRUCTION =
          
  
    

PI node type

  

  

        
        

```
7
```

      
        TYPE_COMMENT =
          
  
    

Comment node type

  

  

        
        

```
8
```

      
        TYPE_DOCUMENT =
          
  
    

Document node type

  

  

        
        

```
9
```

      
        TYPE_DOCUMENT_TYPE =
          
  
    

Document Type node type

  

  

        
        

```
10
```

      
        TYPE_DOCUMENT_FRAGMENT =
          
  
    

Document Fragment node type

  

  

        
        

```
11
```

      
        TYPE_NOTATION =
          
  
    

Notation node type

  

  

        
        

```
12
```

      
        TYPE_WHITESPACE =
          
  
    

Whitespace node type

  

  

        
        

```
13
```

      
        TYPE_SIGNIFICANT_WHITESPACE =
          
  
    

Significant Whitespace node type

  

  

        
        

```
14
```

      
        TYPE_END_ELEMENT =
          
  
    

Element end node type

  

  

        
        

```
15
```

      
        TYPE_END_ENTITY =
          
  
    

Entity end node type

  

  

        
        

```
16
```

      
        TYPE_XML_DECLARATION =
          
  
    

XML Declaration node type

  

  

        
        

```
17
```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**errors**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

A list of errors encountered while parsing.

  

    
      
- 
  
    
      #**source**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The XML source.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**from_io**(io, url = nil, encoding = nil, options = 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new Reader to parse an IO stream.

  

      
        
- 
  
    
      .**from_memory**(string, url = nil, encoding = nil, options = 0)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Create a new Reader to parse a String.

  

      
        
- 
  
    
      .**new**(string_or_io, url_ = nil, encoding_ = nil, options_ = ParseOptions::STRICT, url: url_, encoding: encoding_, options: options_) {|options| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   Reader.new(input) { |options| … } → Reader   Reader.new(input, url:, encoding:, options:) { |options| … } → Reader.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**attribute**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the value of attribute named `name`.

  

      
        
- 
  
    
      #**attribute_at**(index)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the value of attribute at `index`.

  

      
        
- 
  
    
      #**attribute_count**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the number of attributes for the current node.

  

      
        
- 
  
    
      #**attribute_hash**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq: attribute_hash() → Hash<String ⇒ String>.

  

      
        
- 
  
    
      #**attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the attributes and namespaces of the current node as a Hash.

  

      
        
- 
  
    
      #**attributes?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this node have attributes?.

  

      
        
- 
  
    
      #**base_uri**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

base_uri.

  

      
        
- 
  
    
      #**default?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Was an attribute generated from the default value in the DTD or schema?.

  

      
        
- 
  
    
      #**depth**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the depth of the node.

  

      
        
- 
  
    
      #**each**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Move the cursor through the document yielding the cursor to the block.

  

      
        
- 
  
    
      #**empty_element?**(#)  ⇒ Boolean 
    

    
      (also: #self_closing?)
    
  
  
  
  
  
  
  
  

  
    

Returns true if the current node is empty, otherwise false.

  

      
        
- 
  
    
      #**encoding**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**inner_xml**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Read the contents of the current node, including child nodes and markup.

  

      
        
- 
  
    
      #**lang**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the xml:lang scope within which the node resides.

  

      
        
- 
  
    
      #**local_name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the local name of the node.

  

      
        
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the name of the node.

  

      
        
- 
  
    
      #**namespace_uri**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the URI defining the namespace associated with the node.

  

      
        
- 
  
    
      #**namespaces**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get a hash of namespaces for this Node.

  

      
        
- 
  
    
      #**node_type**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the type of readers current node.

  

      
        
- 
  
    
      #**outer_xml**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Read the current node and its contents, including child nodes and markup.

  

      
        
- 
  
    
      #**prefix**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the shorthand reference to the namespace associated with the node.

  

      
        
- 
  
    
      #**read**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Move the Reader forward through the XML document.

  

      
        
- 
  
    
      #**state**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the state of the reader.

  

      
        
- 
  
    
      #**value**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the text value of the node if present.

  

      
        
- 
  
    
      #**value?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this node have a text value?.

  

      
        
- 
  
    
      #**xml_version**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the XML version of the document being read.

  

      
    

  

  
  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**errors**  ⇒ Object 
  

  

  

  
    

A list of errors encountered while parsing

  

  

  
    
      

```

74
75
76
```

    
    
      

```
# File 'lib/nokogiri/xml/reader.rb', line 74

def errors
  @errors
end
```

    
  

    
      
      
      
  
### 
  
    #**source**  ⇒ Object  (readonly)
  

  

  

  
    

The XML source

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/nokogiri/xml/reader.rb', line 77

def source
  @source
end
```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**from_io**(io, url = nil, encoding = nil, options = 0)  ⇒ Object 
  

  

  

  
    

Create a new Reader to parse an IO stream.

  

  
  

  
    
      

```

660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 660

static VALUE
from_io(int argc, VALUE *argv, VALUE klass)
{
  /* TODO: deprecate this method, since Reader.new can handle both memory and IO. It can then
   * become private. */
  VALUE rb_io, rb_url, encoding, rb_options;
  xmlTextReaderPtr reader;
  const char *c_url      = NULL;
  const char *c_encoding = NULL;
  int c_options           = 0;
  VALUE rb_reader, args[3];

  rb_scan_args(argc, argv, "13", &rb_io, &rb_url, &encoding, &rb_options);

  if (!RTEST(rb_io)) { rb_raise(rb_eArgError, "io cannot be nil"); }
  if (RTEST(rb_url)) { c_url = StringValueCStr(rb_url); }
  if (RTEST(encoding)) { c_encoding = StringValueCStr(encoding); }
  if (RTEST(rb_options)) { c_options = (int)NUM2INT(rb_options); }

  reader = xmlReaderForIO(
             (xmlInputReadCallback)noko_io_read,
             (xmlInputCloseCallback)noko_io_close,
             (void *)rb_io,
             c_url,
             c_encoding,
             c_options
           );

  if (reader == NULL) {
    xmlFreeTextReader(reader);
    rb_raise(rb_eRuntimeError, "couldn't create a parser");
  }

  rb_reader = TypedData_Wrap_Struct(klass, &xml_text_reader_type, reader);
  args[0] = rb_io;
  args[1] = rb_url;
  args[2] = encoding;
  rb_obj_call_init(rb_reader, 3, args);

  return rb_reader;
}
```

    
  

    
      
  
### 
  
    .**from_memory**(string, url = nil, encoding = nil, options = 0)  ⇒ Object 
  

  

  

  
    

Create a new Reader to parse a String.

  

  
  

  
    
      

```

613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 613

static VALUE
from_memory(int argc, VALUE *argv, VALUE klass)
{
  /* TODO: deprecate this method, since Reader.new can handle both memory and IO. It can then
   * become private. */
  VALUE rb_buffer, rb_url, encoding, rb_options;
  xmlTextReaderPtr reader;
  const char *c_url      = NULL;
  const char *c_encoding = NULL;
  int c_options           = 0;
  VALUE rb_reader, args[3];

  rb_scan_args(argc, argv, "13", &rb_buffer, &rb_url, &encoding, &rb_options);

  if (!RTEST(rb_buffer)) { rb_raise(rb_eArgError, "string cannot be nil"); }
  if (RTEST(rb_url)) { c_url = StringValueCStr(rb_url); }
  if (RTEST(encoding)) { c_encoding = StringValueCStr(encoding); }
  if (RTEST(rb_options)) { c_options = (int)NUM2INT(rb_options); }

  reader = xmlReaderForMemory(
             StringValuePtr(rb_buffer),
             (int)RSTRING_LEN(rb_buffer),
             c_url,
             c_encoding,
             c_options
           );

  if (reader == NULL) {
    xmlFreeTextReader(reader);
    rb_raise(rb_eRuntimeError, "couldn't create a parser");
  }

  rb_reader = TypedData_Wrap_Struct(klass, &xml_text_reader_type, reader);
  args[0] = rb_buffer;
  args[1] = rb_url;
  args[2] = encoding;
  rb_obj_call_init(rb_reader, 3, args);

  return rb_reader;
}
```

    
  

    
      
  
### 
  
    .**new**(string_or_io, url_ = nil, encoding_ = nil, options_ = ParseOptions::STRICT, url: url_, encoding: encoding_, options: options_) {|options| ... } ⇒ Object 
  

  

  

  
    

:call-seq:

```
Reader.new(input) { |options| ... } → Reader
Reader.new(input, url:, encoding:, options:) { |options| ... } → Reader

```

Create a new Reader to parse an XML document.
Required Parameters

- 

`input` (String | IO): The XML document to parse.

Optional Parameters

- 

`url:` (String) The base URL of the document.

- 

`encoding:` (String) The name of the encoding of the document.

- 

`options:` (Integer | ParseOptions) Options to control the parser behavior. Defaults to `ParseOptions::STRICT`.

Yields

If present, the block will be passed a Nokogiri::XML::ParseOptions object to modify before the fragment is parsed. See Nokogiri::XML::ParseOptions for more information.

  

  

Yields:

  
    
- 
      
      
        (options)
      
      
      
    
  

  
    
      

```

99
100
101
102
103
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
# File 'lib/nokogiri/xml/reader.rb', line 99

def self.new(
  string_or_io,
  url_ = nil, encoding_ = nil, options_ = ParseOptions::STRICT,
  url: url_, encoding: encoding_, options: options_
)
  options = Nokogiri::XML::ParseOptions.new(options) if Integer === options
  yield options if block_given?

  if string_or_io.respond_to?(:read)
    return Reader.from_io(string_or_io, url, encoding, options.to_i)
  end

  Reader.from_memory(string_or_io, url, encoding, options.to_i)
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**attribute**(name)  ⇒ Object 
  

  

  

  
    

Get the value of attribute named `name`

  

  
  

  
    
      

```

266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 266

static VALUE
reader_attribute(VALUE self, VALUE name)
{
  xmlTextReaderPtr reader;
  xmlChar *value ;
  VALUE rb_value;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);

  if (NIL_P(name)) { return Qnil; }
  name = StringValue(name) ;

  value = xmlTextReaderGetAttribute(reader, (xmlChar *)StringValueCStr(name));
  if (value == NULL) { return Qnil; }

  rb_value = NOKOGIRI_STR_NEW2(value);
  xmlFree(value);
  return rb_value;
}
```

    
  

    
      
  
### 
  
    #**attribute_at**(index)  ⇒ Object 
  

  

  

  
    

Get the value of attribute at `index`

  

  
  

  
    
      

```

237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 237

static VALUE
attribute_at(VALUE self, VALUE index)
{
  xmlTextReaderPtr reader;
  xmlChar *value;
  VALUE rb_value;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);

  if (NIL_P(index)) { return Qnil; }
  index = rb_Integer(index);

  value = xmlTextReaderGetAttributeNo(
            reader,
            (int)NUM2INT(index)
          );
  if (value == NULL) { return Qnil; }

  rb_value = NOKOGIRI_STR_NEW2(value);
  xmlFree(value);
  return rb_value;
}
```

    
  

    
      
  
### 
  
    #**attribute_count**  ⇒ Object 
  

  

  

  
    

Get the number of attributes for the current node

  

  
  

  
    
      

```

292
293
294
295
296
297
298
299
300
301
302
303
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 292

static VALUE
attribute_count(VALUE self)
{
  xmlTextReaderPtr reader;
  int count;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  count = xmlTextReaderAttributeCount(reader);
  if (count == -1) { return Qnil; }

  return INT2NUM(count);
}
```

    
  

    
      
  
### 
  
    #**attribute_hash**  ⇒ Object 
  

  

  

  
    

:call-seq: attribute_hash() → Hash<String ⇒ String>

Get the attributes of the current node as a Hash of names and values.

See related: #attributes and #namespaces

  

  

  
    
      

```

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
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 182

static VALUE
rb_xml_reader_attribute_hash(VALUE rb_reader)
{
  VALUE rb_attributes = rb_hash_new();
  xmlTextReaderPtr c_reader;
  xmlNodePtr c_node;
  xmlAttrPtr c_property;
  VALUE rb_errors;

  TypedData_Get_Struct(rb_reader, xmlTextReader, &xml_text_reader_type, c_reader);

  if (!has_attributes(c_reader)) {
    return rb_attributes;
  }

  rb_errors = rb_funcall(rb_reader, rb_intern("errors"), 0);

  xmlSetStructuredErrorFunc((void *)rb_errors, noko__error_array_pusher);
  c_node = xmlTextReaderExpand(c_reader);
  xmlSetStructuredErrorFunc(NULL, NULL);

  if (c_node == NULL) {
    if (RARRAY_LEN(rb_errors) > 0) {
      VALUE rb_error = rb_ary_entry(rb_errors, 0);
      VALUE exception_message = rb_funcall(rb_error, rb_intern("to_s"), 0);
      rb_exc_raise(rb_class_new_instance(1, &exception_message, cNokogiriXmlSyntaxError));
    }
    return Qnil;
  }

  c_property = c_node->properties;
  while (c_property != NULL) {
    VALUE rb_name = NOKOGIRI_STR_NEW2(c_property->name);
    VALUE rb_value = Qnil;
    xmlChar *c_value = xmlNodeGetContent((xmlNode *)c_property);

    if (c_value) {
      rb_value = NOKOGIRI_STR_NEW2(c_value);
      xmlFree(c_value);
    }

    rb_hash_aset(rb_attributes, rb_name, rb_value);

    c_property = c_property->next;
  }

  return rb_attributes;
}
```

    
  

    
      
  
### 
  
    #**attributes**  ⇒ Object 
  

  

  

  
    

Get the attributes and namespaces of the current node as a Hash.

This is the union of Reader#attribute_hash and Reader#namespaces
Returns

(Hash<String, String>) Attribute names and values, and namespace prefixes and hrefs.

  

  

  
    
      

```

126
127
128
```

    
    
      

```
# File 'lib/nokogiri/xml/reader.rb', line 126

def attributes
  attribute_hash.merge(namespaces)
end
```

    
  

    
      
  
### 
  
    #**attributes?**  ⇒ Boolean 
  

  

  

  
    

Does this node have attributes?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

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
132
133
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 121

static VALUE
attributes_eh(VALUE self)
{
  xmlTextReaderPtr reader;
  int eh;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  eh = has_attributes(reader);
  if (eh == 0) { return Qfalse; }
  if (eh == 1) { return Qtrue; }

  return Qnil;
}
```

    
  

    
      
  
### 
  
    #**base_uri**  ⇒ Object 
  

  

  

  
    

base_uri

Get the xml:base of the node

  

  

  
    
      

```

463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 463

static VALUE
rb_xml_reader_base_uri(VALUE rb_reader)
{
  VALUE rb_base_uri;
  xmlTextReaderPtr c_reader;
  xmlChar *c_base_uri;

  TypedData_Get_Struct(rb_reader, xmlTextReader, &xml_text_reader_type, c_reader);

  c_base_uri = xmlTextReaderBaseUri(c_reader);
  if (c_base_uri == NULL) {
    return Qnil;
  }

  rb_base_uri = NOKOGIRI_STR_NEW2(c_base_uri);
  xmlFree(c_base_uri);

  return rb_base_uri;
}
```

    
  

    
      
  
### 
  
    #**default?**  ⇒ Boolean 
  

  

  

  
    

Was an attribute generated from the default value in the DTD or schema?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

81
82
83
84
85
86
87
88
89
90
91
92
93
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 81

static VALUE
default_eh(VALUE self)
{
  xmlTextReaderPtr reader;
  int eh;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  eh = xmlTextReaderIsDefault(reader);
  if (eh == 0) { return Qfalse; }
  if (eh == 1) { return Qtrue; }

  return Qnil;
}
```

    
  

    
      
  
### 
  
    #**depth**  ⇒ Object 
  

  

  

  
    

Get the depth of the node

  

  
  

  
    
      

```

311
312
313
314
315
316
317
318
319
320
321
322
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 311

static VALUE
depth(VALUE self)
{
  xmlTextReaderPtr reader;
  int depth;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  depth = xmlTextReaderDepth(reader);
  if (depth == -1) { return Qnil; }

  return INT2NUM(depth);
}
```

    
  

    
      
  
### 
  
    #**each**  ⇒ Object 
  

  

  

  
    

Move the cursor through the document yielding the cursor to the block

  

  

  
    
      

```

132
133
134
135
136
```

    
    
      

```
# File 'lib/nokogiri/xml/reader.rb', line 132

def each
  while (cursor = read)
    yield cursor
  end
end
```

    
  

    
      
  
### 
  
    #**empty_element?**(#)  ⇒ Boolean 
  

  
    Also known as:
    self_closing?
    
  

  

  
    

Returns true if the current node is empty, otherwise false.

  

  
  
  
    

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

708
709
710
711
712
713
714
715
716
717
718
719
720
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 708

static VALUE
empty_element_p(VALUE self)
{
  xmlTextReaderPtr reader;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);

  if (xmlTextReaderIsEmptyElement(reader)) {
    return Qtrue;
  }

  return Qfalse;
}
```

    
  

    
      
  
### 
  
    #**encoding**  ⇒ Object 
  

  

  

  
    
      

```

722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 722

static VALUE
rb_xml_reader_encoding(VALUE rb_reader)
{
  xmlTextReaderPtr c_reader;
  const char *parser_encoding;
  VALUE constructor_encoding;

  TypedData_Get_Struct(rb_reader, xmlTextReader, &xml_text_reader_type, c_reader);
  parser_encoding = (const char *)xmlTextReaderConstEncoding(c_reader);
  if (parser_encoding) {
    return NOKOGIRI_STR_NEW2(parser_encoding);
  }

  constructor_encoding = rb_iv_get(rb_reader, "@encoding");
  if (RTEST(constructor_encoding)) {
    return constructor_encoding;
  }

  return Qnil;
}
```

    
  

    
      
  
### 
  
    #**inner_xml**  ⇒ Object 
  

  

  

  
    

Read the contents of the current node, including child nodes and markup. Returns a utf-8 encoded string.

  

  
  

  
    
      

```

562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 562

static VALUE
inner_xml(VALUE self)
{
  xmlTextReaderPtr reader;
  xmlChar *value;
  VALUE str;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);

  value = xmlTextReaderReadInnerXml(reader);

  str = Qnil;
  if (value) {
    str = NOKOGIRI_STR_NEW2((char *)value);
    xmlFree(value);
  }

  return str;
}
```

    
  

    
      
  
### 
  
    #**lang**  ⇒ Object 
  

  

  

  
    

Get the xml:lang scope within which the node resides.

  

  
  

  
    
      

```

349
350
351
352
353
354
355
356
357
358
359
360
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 349

static VALUE
lang(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *lang;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  lang = (const char *)xmlTextReaderConstXmlLang(reader);
  if (lang == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(lang);
}
```

    
  

    
      
  
### 
  
    #**local_name**  ⇒ Object 
  

  

  

  
    

Get the local name of the node

  

  
  

  
    
      

```

425
426
427
428
429
430
431
432
433
434
435
436
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 425

static VALUE
local_name(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *name;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  name = (const char *)xmlTextReaderConstLocalName(reader);
  if (name == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(name);
}
```

    
  

    
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

Get the name of the node. Returns a utf-8 encoded string.

  

  
  

  
    
      

```

444
445
446
447
448
449
450
451
452
453
454
455
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 444

static VALUE
name(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *name;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  name = (const char *)xmlTextReaderConstName(reader);
  if (name == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(name);
}
```

    
  

    
      
  
### 
  
    #**namespace_uri**  ⇒ Object 
  

  

  

  
    

Get the URI defining the namespace associated with the node

  

  
  

  
    
      

```

406
407
408
409
410
411
412
413
414
415
416
417
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 406

static VALUE
namespace_uri(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *uri;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  uri = (const char *)xmlTextReaderConstNamespaceUri(reader);
  if (uri == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(uri);
}
```

    
  

    
      
  
### 
  
    #**namespaces**  ⇒ Object 
  

  

  

  
    

Get a hash of namespaces for this Node

  

  
  

  
    
      

```

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
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 141

static VALUE
rb_xml_reader_namespaces(VALUE rb_reader)
{
  VALUE rb_namespaces = rb_hash_new() ;
  xmlTextReaderPtr c_reader;
  xmlNodePtr c_node;
  VALUE rb_errors;

  TypedData_Get_Struct(rb_reader, xmlTextReader, &xml_text_reader_type, c_reader);

  if (! has_attributes(c_reader)) {
    return rb_namespaces ;
  }

  rb_errors = rb_funcall(rb_reader, rb_intern("errors"), 0);

  xmlSetStructuredErrorFunc((void *)rb_errors, noko__error_array_pusher);
  c_node = xmlTextReaderExpand(c_reader);
  xmlSetStructuredErrorFunc(NULL, NULL);

  if (c_node == NULL) {
    if (RARRAY_LEN(rb_errors) > 0) {
      VALUE rb_error = rb_ary_entry(rb_errors, 0);
      VALUE exception_message = rb_funcall(rb_error, rb_intern("to_s"), 0);
      rb_exc_raise(rb_class_new_instance(1, &exception_message, cNokogiriXmlSyntaxError));
    }
    return Qnil;
  }

  Nokogiri_xml_node_namespaces(c_node, rb_namespaces);

  return rb_namespaces ;
}
```

    
  

    
      
  
### 
  
    #**node_type**  ⇒ Object 
  

  

  

  
    

Get the type of readers current node

  

  
  

  
    
      

```

503
504
505
506
507
508
509
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 503

static VALUE
node_type(VALUE self)
{
  xmlTextReaderPtr reader;
  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  return INT2NUM(xmlTextReaderNodeType(reader));
}
```

    
  

    
      
  
### 
  
    #**outer_xml**  ⇒ Object 
  

  

  

  
    

Read the current node and its contents, including child nodes and markup. Returns a utf-8 encoded string.

  

  
  

  
    
      

```

589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 589

static VALUE
outer_xml(VALUE self)
{
  xmlTextReaderPtr reader;
  xmlChar *value;
  VALUE str = Qnil;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);

  value = xmlTextReaderReadOuterXml(reader);

  if (value) {
    str = NOKOGIRI_STR_NEW2((char *)value);
    xmlFree(value);
  }
  return str;
}
```

    
  

    
      
  
### 
  
    #**prefix**  ⇒ Object 
  

  

  

  
    

Get the shorthand reference to the namespace associated with the node.

  

  
  

  
    
      

```

387
388
389
390
391
392
393
394
395
396
397
398
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 387

static VALUE
prefix(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *prefix;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  prefix = (const char *)xmlTextReaderConstPrefix(reader);
  if (prefix == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(prefix);
}
```

    
  

    
      
  
### 
  
    #**read**  ⇒ Object 
  

  

  

  
    

Move the Reader forward through the XML document.

  

  
  

  
    
      

```

517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 517

static VALUE
read_more(VALUE rb_reader)
{
  xmlTextReaderPtr c_reader;
  libxmlStructuredErrorHandlerState handler_state;

  TypedData_Get_Struct(rb_reader, xmlTextReader, &xml_text_reader_type, c_reader);

  VALUE rb_errors = rb_funcall(rb_reader, rb_intern("errors"), 0);
  noko__structured_error_func_save_and_set(&handler_state, (void *)rb_errors, noko__error_array_pusher);

  int status = xmlTextReaderRead(c_reader);

  noko__structured_error_func_restore(&handler_state);

  xmlDocPtr c_document = xmlTextReaderCurrentDoc(c_reader);
  if (c_document && c_document->encoding == NULL) {
    VALUE constructor_encoding = rb_iv_get(rb_reader, "@encoding");
    if (RTEST(constructor_encoding)) {
      c_document->encoding = xmlStrdup(BAD_CAST StringValueCStr(constructor_encoding));
    } else {
      rb_iv_set(rb_reader, "@encoding", NOKOGIRI_STR_NEW2("UTF-8"));
      c_document->encoding = xmlStrdup(BAD_CAST "UTF-8");
    }
  }

  if (status == 1) { return rb_reader; }
  if (status == 0) { return Qnil; }

  /* if we're here, there was an error */
  VALUE exception = rb_funcall(cNokogiriXmlSyntaxError, rb_intern("aggregate"), 1, rb_errors);
  if (RB_TEST(exception)) {
    rb_exc_raise(exception);
  } else {
    rb_raise(rb_eRuntimeError, "Error pulling: %d", status);
  }
}
```

    
  

    
      
  
### 
  
    #**state**  ⇒ Object 
  

  

  

  
    

Get the state of the reader

  

  
  

  
    
      

```

489
490
491
492
493
494
495
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 489

static VALUE
state(VALUE self)
{
  xmlTextReaderPtr reader;
  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  return INT2NUM(xmlTextReaderReadState(reader));
}
```

    
  

    
      
  
### 
  
    #**value**  ⇒ Object 
  

  

  

  
    

Get the text value of the node if present. Returns a utf-8 encoded string.

  

  
  

  
    
      

```

368
369
370
371
372
373
374
375
376
377
378
379
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 368

static VALUE
value(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *value;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  value = (const char *)xmlTextReaderConstValue(reader);
  if (value == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(value);
}
```

    
  

    
      
  
### 
  
    #**value?**  ⇒ Boolean 
  

  

  

  
    

Does this node have a text value?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

101
102
103
104
105
106
107
108
109
110
111
112
113
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 101

static VALUE
value_eh(VALUE self)
{
  xmlTextReaderPtr reader;
  int eh;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  eh = xmlTextReaderHasValue(reader);
  if (eh == 0) { return Qfalse; }
  if (eh == 1) { return Qtrue; }

  return Qnil;
}
```

    
  

    
      
  
### 
  
    #**xml_version**  ⇒ Object 
  

  

  

  
    

Get the XML version of the document being read

  

  
  

  
    
      

```

330
331
332
333
334
335
336
337
338
339
340
341
```

    
    
      

```
# File 'ext/nokogiri/xml_reader.c', line 330

static VALUE
xml_version(VALUE self)
{
  xmlTextReaderPtr reader;
  const char *version;

  TypedData_Get_Struct(self, xmlTextReader, &xml_text_reader_type, reader);
  version = (const char *)xmlTextReaderConstXmlVersion(reader);
  if (version == NULL) { return Qnil; }

  return NOKOGIRI_STR_NEW2(version);
}
```