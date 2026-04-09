# Class: Nokogiri::XML::SAX::ParserContext
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::XML::SAX::ParserContext
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/xml/sax/parser_context.rb,

  ext/nokogiri/xml_sax_parser_context.c

  
  

## Overview

  
    

Context object to invoke the XML SAX parser on the SAX::Document handler.

💡 This class is usually not instantiated by the user. Use Nokogiri::XML::SAX::Parser instead.

  

  

  
## Direct Known Subclasses

  

HTML4::SAX::ParserContext, HTML::SAX::ParserContext

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**file**(input, encoding = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   file(path)   file(path, encoding).

  

      
        
- 
  
    
      .**io**(input, encoding = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   io(input)   io(input, encoding).

  

      
        
- 
  
    
      .**memory**(input, encoding = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   memory(input)   memory(input, encoding).

  

      
        
- 
  
    
      .**native_file**(rb_path, rb_encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**native_io**(rb_io, rb_encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**native_memory**(rb_input, rb_encoding)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      .**new**(input, encoding = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:call-seq:   new(input)   new(input, encoding).

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**column**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    Returns

(Integer) the column number of the column being currently parsed.

  

      
        
- 
  
    
      #**line**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    Returns

(Integer) the line number of the line being currently parsed.

  

      
        
- 
  
    
      #**parse_with**(sax_handler)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Use `sax_handler` and parse the current document.

  

      
        
- 
  
    
      #**recovery**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Inspect whether this parser will recover from parsing errors.

  

      
        
- 
  
    
      #**recovery=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Controls whether this parser will recover from parsing errors.

  

      
        
- 
  
    
      #**replace_entities**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Document@Entity+Handling for an explanation of the behavior controlled by this flag.

  

      
        
- 
  
    
      #**replace_entities=**(value)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Document@Entity+Handling for an explanation of the behavior controlled by this flag.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**file**(input, encoding = nil)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
file(path)
file(path, encoding)

```

Create a parser context for the file at `path`.
Parameters

- 

`path` (String) The path to the input file

- 

`encoding` (optional) (Encoding, String) The `Encoding` to use, or the name of an encoding to use (default `nil`, encoding will be autodetected)

Returns

Nokogiri::XML::SAX::ParserContext

💡 Calling this method directly is discouraged. Use Nokogiri::XML::SAX::Parser.parse_file which is more convenient for most use cases.

  

  

  
    
      

```

97
98
99
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/parser_context.rb', line 97

def file(input, encoding = nil)
  native_file(input, resolve_encoding(encoding))
end

```

    
  

    
      
  
### 
  
    .**io**(input, encoding = nil)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
io(input)
io(input, encoding)

```

Create a parser context for an `input` IO which will assume `encoding`
Parameters

- 

`io` (IO) The readable IO object from which to read input

- 

`encoding` (optional) (Encoding) The `Encoding` to use, or the name of an encoding to use (default `nil`, encoding will be autodetected)

Returns

Nokogiri::XML::SAX::ParserContext

💡 Calling this method directly is discouraged. Use Nokogiri::XML::SAX::Parser parse methods which are more convenient for most use cases.

  

  

  
    
      

```

56
57
58
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/parser_context.rb', line 56

def io(input, encoding = nil)
  native_io(input, resolve_encoding(encoding))
end

```

    
  

    
      
  
### 
  
    .**memory**(input, encoding = nil)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
memory(input)
memory(input, encoding)

```

Create a parser context for the `input` String.
Parameters

- 

`input` (String) The input string to be parsed.

- 

`encoding` (optional) (Encoding, String) The `Encoding` to use, or the name of an encoding to use (default `nil`, encoding will be autodetected)

Returns

Nokogiri::XML::SAX::ParserContext

💡 Calling this method directly is discouraged. Use Nokogiri::XML::SAX::Parser parse methods which are more convenient for most use cases.

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/parser_context.rb', line 77

def memory(input, encoding = nil)
  native_memory(input, resolve_encoding(encoding))
end

```

    
  

    
      
  
### 
  
    .**native_file**(rb_path, rb_encoding)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

112
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
128
129
130
131
132
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 112

static VALUE
noko_xml_sax_parser_context_s_native_file(VALUE rb_class, VALUE rb_path, VALUE rb_encoding)
{
  if (!NIL_P(rb_encoding) && !rb_obj_is_kind_of(rb_encoding, rb_cEncoding)) {
    rb_raise(rb_eTypeError, "argument must be an Encoding object");
  }

  xmlParserCtxtPtr c_context = xmlCreateFileParserCtxt(StringValueCStr(rb_path));
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
  
    .**native_io**(rb_io, rb_encoding)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

78
79
80
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
94
95
96
97
98
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
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 78

static VALUE
noko_xml_sax_parser_context_s_native_io(VALUE rb_class, VALUE rb_io, VALUE rb_encoding)
{
  if (!rb_respond_to(rb_io, id_read)) {
    rb_raise(rb_eTypeError, "argument expected to respond to :read");
  }

  if (!NIL_P(rb_encoding) && !rb_obj_is_kind_of(rb_encoding, rb_cEncoding)) {
    rb_raise(rb_eTypeError, "argument must be an Encoding object");
  }

  xmlParserCtxtPtr c_context =
    xmlCreateIOParserCtxt(NULL, NULL,
                          (xmlInputReadCallback)noko_io_read,
                          (xmlInputCloseCallback)noko_io_close,
                          (void *)rb_io, XML_CHAR_ENCODING_NONE);
  if (!c_context) {
    rb_raise(rb_eRuntimeError, "failed to create xml sax parser context");
  }

  noko_xml_sax_parser_context_set_encoding(c_context, rb_encoding);

  if (c_context->sax) {
    xmlFree(c_context->sax);
    c_context->sax = NULL;
  }

  VALUE rb_context = noko_xml_sax_parser_context_wrap(rb_class, c_context);
  rb_iv_set(rb_context, "@input", rb_io);

  return rb_context;
}

```

    
  

    
      
  
### 
  
    .**native_memory**(rb_input, rb_encoding)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

135
136
137
138
139
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
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 135

static VALUE
noko_xml_sax_parser_context_s_native_memory(VALUE rb_class, VALUE rb_input, VALUE rb_encoding)
{
  Check_Type(rb_input, T_STRING);
  if (!(int)RSTRING_LEN(rb_input)) {
    rb_raise(rb_eRuntimeError, "input string cannot be empty");
  }

  if (!NIL_P(rb_encoding) && !rb_obj_is_kind_of(rb_encoding, rb_cEncoding)) {
    rb_raise(rb_eTypeError, "argument must be an Encoding object");
  }

  xmlParserCtxtPtr c_context =
    xmlCreateMemoryParserCtxt(StringValuePtr(rb_input), (int)RSTRING_LEN(rb_input));
  if (!c_context) {
    rb_raise(rb_eRuntimeError, "failed to create xml sax parser context");
  }

  noko_xml_sax_parser_context_set_encoding(c_context, rb_encoding);

  if (c_context->sax) {
    xmlFree(c_context->sax);
    c_context->sax = NULL;
  }

  VALUE rb_context = noko_xml_sax_parser_context_wrap(rb_class, c_context);
  rb_iv_set(rb_context, "@input", rb_input);

  return rb_context;
}

```

    
  

    
      
  
### 
  
    .**new**(input, encoding = nil)  ⇒ Object 
  

  

  

  
    

:call-seq:

```
new(input)
new(input, encoding)

```

Create a parser context for an IO or a String. This is a shorthand method for ParserContext.io and ParserContext.memory.
Parameters

- 

`input` (IO, String) A String or a readable IO object

- 

`encoding` (optional) (Encoding) The `Encoding` to use, or the name of an encoding to use (default `nil`, encoding will be autodetected)

If `input` quacks like a readable IO object, this method forwards to ParserContext.io, otherwise it forwards to ParserContext.memory.
Returns

Nokogiri::XML::SAX::ParserContext

  

  

  
    
      

```

31
32
33
34
35
36
37
```

    
    
      

```
# File 'lib/nokogiri/xml/sax/parser_context.rb', line 31

def new(input, encoding = nil)
  if [:read, :close].all? { |x| input.respond_to?(x) }
    io(input, encoding)
  else
    memory(input, encoding)
  end
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**column**  ⇒ Object 
  

  

  

  
    Returns

(Integer) the column number of the column being currently parsed.

  

  
  

  
    
      

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
304
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 292

static VALUE
noko_xml_sax_parser_context__column(VALUE rb_context)
{
  xmlParserCtxtPtr ctxt = noko_xml_sax_parser_context_unwrap(rb_context);
  xmlParserInputPtr io;

  io = ctxt->input;
  if (io) {
    return INT2NUM(io->col);
  }

  return Qnil;
}

```

    
  

    
      
  
### 
  
    #**line**  ⇒ Object 
  

  

  

  
    Returns

(Integer) the line number of the line being currently parsed.

  

  
  

  
    
      

```

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
285
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 273

static VALUE
noko_xml_sax_parser_context__line(VALUE rb_context)
{
  xmlParserInputPtr io;
  xmlParserCtxtPtr ctxt = noko_xml_sax_parser_context_unwrap(rb_context);

  io = ctxt->input;
  if (io) {
    return INT2NUM(io->line);
  }

  return Qnil;
}

```

    
  

    
      
  
### 
  
    #**parse_with**(sax_handler)  ⇒ Object 
  

  

  

  
    

Use `sax_handler` and parse the current document

💡 Calling this method directly is discouraged. Use Nokogiri::XML::SAX::Parser methods which are more convenient for most use cases.

  

  
  

  
    
      

```

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
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 175

static VALUE
noko_xml_sax_parser_context__parse_with(VALUE rb_context, VALUE rb_sax_parser)
{
  xmlParserCtxtPtr c_context;
  xmlSAXHandlerPtr sax;

  if (!rb_obj_is_kind_of(rb_sax_parser, cNokogiriXmlSaxParser)) {
    rb_raise(rb_eArgError, "argument must be a Nokogiri::XML::SAX::Parser");
  }

  c_context = noko_xml_sax_parser_context_unwrap(rb_context);
  sax = noko_xml_sax_parser_unwrap(rb_sax_parser);

  c_context->sax = sax;
  c_context->userData = c_context; /* so we can use libxml2/SAX2.c handlers if we want to */
  c_context->_private = (void *)rb_sax_parser;

  xmlSetStructuredErrorFunc(NULL, NULL);

  /* although we're calling back into Ruby here, we don't need to worry about exceptions, because we
   * don't have any cleanup to do. The only memory we need to free is handled by
   * xml_sax_parser_context_type_free */
  xmlParseDocument(c_context);

  return Qnil;
}

```

    
  

    
      
  
### 
  
    #**recovery**  ⇒ Object 
  

  

  

  
    

Inspect whether this parser will recover from parsing errors. If set to `true`, the parser will invoke the SAX::Document#error callback and continue processing the file. If set to `false`, the parser will stop processing the file on the first parsing error.
Returns

(Boolean) Whether this parser will recover from parsing errors.

Default is `false` for XML and `true` for HTML.

  

  
  

  
    
      

```

359
360
361
362
363
364
365
366
367
368
369
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 359

static VALUE
noko_xml_sax_parser_context__recovery_get(VALUE rb_context)
{
  xmlParserCtxtPtr ctxt = noko_xml_sax_parser_context_unwrap(rb_context);

  if (xmlCtxtGetOptions(ctxt) & XML_PARSE_RECOVER) {
    return Qtrue;
  } else {
    return Qfalse;
  }
}

```

    
  

    
      
  
### 
  
    #**recovery=**(value)  ⇒ Object 
  

  

  

  
    

Controls whether this parser will recover from parsing errors. If set to `true`, the parser will invoke the SAX::Document#error callback and continue processing the file. If set to `false`, the parser will stop processing the file on the first parsing error.
Parameters

- 

`value` (Boolean) Recover from parsing errors. (Default is `false` for XML and `true` for HTML.)

Returns

(Boolean) The passed `value`.
Example

Because this class is generally not instantiated directly, you would typically set this option via the block argument to Nokogiri::XML::SAX::Parser.parse et al:

```
parser = Nokogiri::XML::SAX::Parser.new(document_handler)
parser.parse(xml) do |ctx|
  ctx.recovery = true
end

```

  

  
  

  
    
      

```

328
329
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
342
343
344
345
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 328

static VALUE
noko_xml_sax_parser_context__recovery_set(VALUE rb_context, VALUE rb_value)
{
  int error;
  xmlParserCtxtPtr ctxt = noko_xml_sax_parser_context_unwrap(rb_context);

  if (RB_TEST(rb_value)) {
    error = xmlCtxtSetOptions(ctxt, xmlCtxtGetOptions(ctxt) | XML_PARSE_RECOVER);
  } else {
    error = xmlCtxtSetOptions(ctxt, xmlCtxtGetOptions(ctxt) & ~XML_PARSE_RECOVER);
  }

  if (error) {
    rb_raise(rb_eRuntimeError, "failed to set parser context options (%x)", error);
  }

  return rb_value;
}

```

    
  

    
      
  
### 
  
    #**replace_entities**  ⇒ Object 
  

  

  

  
    

See Document@Entity+Handling for an explanation of the behavior controlled by this flag.
Returns

(Boolean) Value of the parse option. (Default `false`)

This option is perhaps misnamed by the libxml2 author, since it controls resolution and not replacement.

  

  
  

  
    
      

```

256
257
258
259
260
261
262
263
264
265
266
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 256

static VALUE
noko_xml_sax_parser_context__replace_entities_get(VALUE rb_context)
{
  xmlParserCtxtPtr ctxt = noko_xml_sax_parser_context_unwrap(rb_context);

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
Example

Because this class is generally not instantiated directly, you would typically set this option via the block argument to Nokogiri::XML::SAX::Parser.parse et al:

```
parser = Nokogiri::XML::SAX::Parser.new(document_handler)
parser.parse(xml) do |ctx|
  ctx.replace_entities = true # this is UNSAFE for untrusted documents!
end

```

  

  
  

  
    
      

```

226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
```

    
    
      

```
# File 'ext/nokogiri/xml_sax_parser_context.c', line 226

static VALUE
noko_xml_sax_parser_context__replace_entities_set(VALUE rb_context, VALUE rb_value)
{
  int error;
  xmlParserCtxtPtr ctxt = noko_xml_sax_parser_context_unwrap(rb_context);

  if (RB_TEST(rb_value)) {
    error = xmlCtxtSetOptions(ctxt, xmlCtxtGetOptions(ctxt) | XML_PARSE_NOENT);
  } else {
    error = xmlCtxtSetOptions(ctxt, xmlCtxtGetOptions(ctxt) & ~XML_PARSE_NOENT);
  }

  if (error) {
    rb_raise(rb_eRuntimeError, "failed to set parser context options (%x)", error);
  }

  return rb_value;
}

```