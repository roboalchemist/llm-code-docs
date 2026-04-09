# Class: Nokogiri::HTML4::ElementDescription
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Nokogiri::HTML4::ElementDescription
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/nokogiri/html4/element_description.rb,

  lib/nokogiri/html4/element_description_defaults.rb,
 ext/nokogiri/html4_element_description.c

  
  

## Defined Under Namespace

  
    
  
    
      **Classes:** Desc
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        DefaultDescriptions =
          
  
    

This is filled in down below.

  

  

        
        

```
{}

```

      
        FONTSTYLE =
          
  
    

Attributes defined and categorized

  

  

        
        

```
["tt", "i", "b", "u", "s", "strike", "big", "small"]

```

      
        PHRASE =
          
        
        

```
[
  "em",
  "strong",
  "dfn",
  "code",
  "samp",
  "kbd",
  "var",
  "cite",
  "abbr",
  "acronym",
]

```

      
        SPECIAL =
          
        
        

```
[
  "a",
  "img",
  "applet",
  "embed",
  "object",
  "font",
  "basefont",
  "br",
  "script",
  "map",
  "q",
  "sub",
  "sup",
  "span",
  "bdo",
  "iframe",
]

```

      
        PCDATA =
          
        
        

```
[]

```

      
        HEADING =
          
        
        

```
["h1", "h2", "h3", "h4", "h5", "h6"]

```

      
        LIST =
          
        
        

```
["ul", "ol", "dir", "menu"]

```

      
        FORMCTRL =
          
        
        

```
["input", "select", "textarea", "label", "button"]

```

      
        BLOCK =
          
        
        

```
[
  HEADING,
  LIST,
  "pre",
  "p",
  "dl",
  "div",
  "center",
  "noscript",
  "noframes",
  "blockquote",
  "form",
  "isindex",
  "hr",
  "table",
  "fieldset",
  "address",
]

```

      
        INLINE =
          
        
        

```
[PCDATA, FONTSTYLE, PHRASE, SPECIAL, FORMCTRL]

```

      
        FLOW =
          
        
        

```
[BLOCK, INLINE]

```

      
        MODIFIER =
          
        
        

```
[]

```

      
        EMPTY =
          
        
        

```
[]

```

      
        HTML_FLOW =
          
        
        

```
FLOW

```

      
        HTML_INLINE =
          
        
        

```
INLINE

```

      
        HTML_PCDATA =
          
        
        

```
PCDATA

```

      
        HTML_CDATA =
          
        
        

```
HTML_PCDATA

```

      
        COREATTRS =
          
        
        

```
["id", "class", "style", "title"]

```

      
        I18N =
          
        
        

```
["lang", "dir"]

```

      
        EVENTS =
          
        
        

```
[
  "onclick",
  "ondblclick",
  "onmousedown",
  "onmouseup",
  "onmouseover",
  "onmouseout",
  "onkeypress",
  "onkeydown",
  "onkeyup",
]

```

      
        ATTRS =
          
        
        

```
[COREATTRS, I18N, EVENTS]

```

      
        CELLHALIGN =
          
        
        

```
["align", "char", "charoff"]

```

      
        CELLVALIGN =
          
        
        

```
["valign"]

```

      
        HTML_ATTRS =
          
        
        

```
ATTRS

```

      
        CORE_I18N_ATTRS =
          
        
        

```
[COREATTRS, I18N]

```

      
        CORE_ATTRS =
          
        
        

```
COREATTRS

```

      
        I18N_ATTRS =
          
        
        

```
I18N

```

      
        A_ATTRS =
          
        
        

```
[
  ATTRS,
  "charset",
  "type",
  "name",
  "href",
  "hreflang",
  "rel",
  "rev",
  "accesskey",
  "shape",
  "coords",
  "tabindex",
  "onfocus",
  "onblur",
]

```

      
        TARGET_ATTR =
          
        
        

```
["target"]

```

      
        ROWS_COLS_ATTR =
          
        
        

```
["rows", "cols"]

```

      
        ALT_ATTR =
          
        
        

```
["alt"]

```

      
        SRC_ALT_ATTRS =
          
        
        

```
["src", "alt"]

```

      
        HREF_ATTRS =
          
        
        

```
["href"]

```

      
        CLEAR_ATTRS =
          
        
        

```
["clear"]

```

      
        INLINE_P =
          
        
        

```
[INLINE, "p"]

```

      
        FLOW_PARAM =
          
        
        

```
[FLOW, "param"]

```

      
        APPLET_ATTRS =
          
        
        

```
[
  COREATTRS,
  "codebase",
  "archive",
  "alt",
  "name",
  "height",
  "width",
  "align",
  "hspace",
  "vspace",
]

```

      
        AREA_ATTRS =
          
        
        

```
[
  "shape",
  "coords",
  "href",
  "nohref",
  "tabindex",
  "accesskey",
  "onfocus",
  "onblur",
]

```

      
        BASEFONT_ATTRS =
          
        
        

```
["id", "size", "color", "face"]

```

      
        QUOTE_ATTRS =
          
        
        

```
[ATTRS, "cite"]

```

      
        BODY_CONTENTS =
          
        
        

```
[FLOW, "ins", "del"]

```

      
        BODY_ATTRS =
          
        
        

```
[ATTRS, "onload", "onunload"]

```

      
        BODY_DEPR =
          
        
        

```
[
  "background",
  "bgcolor",
  "text",
  "link",
  "vlink",
  "alink",
]

```

      
        BUTTON_ATTRS =
          
        
        

```
[
  ATTRS,
  "name",
  "value",
  "type",
  "disabled",
  "tabindex",
  "accesskey",
  "onfocus",
  "onblur",
]

```

      
        COL_ATTRS =
          
        
        

```
[ATTRS, "span", "width", CELLHALIGN, CELLVALIGN]

```

      
        COL_ELT =
          
        
        

```
["col"]

```

      
        EDIT_ATTRS =
          
        
        

```
[ATTRS, "datetime", "cite"]

```

      
        COMPACT_ATTRS =
          
        
        

```
[ATTRS, "compact"]

```

      
        DL_CONTENTS =
          
        
        

```
["dt", "dd"]

```

      
        COMPACT_ATTR =
          
        
        

```
["compact"]

```

      
        LABEL_ATTR =
          
        
        

```
["label"]

```

      
        FIELDSET_CONTENTS =
          
        
        

```
[FLOW, "legend"]

```

      
        FONT_ATTRS =
          
        
        

```
[COREATTRS, I18N, "size", "color", "face"]

```

      
        FORM_CONTENTS =
          
        
        

```
[
  HEADING,
  LIST,
  INLINE,
  "pre",
  "p",
  "div",
  "center",
  "noscript",
  "noframes",
  "blockquote",
  "isindex",
  "hr",
  "table",
  "fieldset",
  "address",
]

```

      
        FORM_ATTRS =
          
        
        

```
[
  ATTRS,
  "method",
  "enctype",
  "accept",
  "name",
  "onsubmit",
  "onreset",
  "accept-charset",
]

```

      
        FRAME_ATTRS =
          
        
        

```
[
  COREATTRS,
  "longdesc",
  "name",
  "src",
  "frameborder",
  "marginwidth",
  "marginheight",
  "noresize",
  "scrolling",
]

```

      
        FRAMESET_ATTRS =
          
        
        

```
[COREATTRS, "rows", "cols", "onload", "onunload"]

```

      
        FRAMESET_CONTENTS =
          
        
        

```
["frameset", "frame", "noframes"]

```

      
        HEAD_ATTRS =
          
        
        

```
[I18N, "profile"]

```

      
        HEAD_CONTENTS =
          
        
        

```
[
  "title",
  "isindex",
  "base",
  "script",
  "style",
  "meta",
  "link",
  "object",
]

```

      
        HR_DEPR =
          
        
        

```
["align", "noshade", "size", "width"]

```

      
        VERSION_ATTR =
          
        
        

```
["version"]

```

      
        HTML_CONTENT =
          
        
        

```
["head", "body", "frameset"]

```

      
        IFRAME_ATTRS =
          
        
        

```
[
  COREATTRS,
  "longdesc",
  "name",
  "src",
  "frameborder",
  "marginwidth",
  "marginheight",
  "scrolling",
  "align",
  "height",
  "width",
]

```

      
        IMG_ATTRS =
          
        
        

```
[
  ATTRS,
  "longdesc",
  "name",
  "height",
  "width",
  "usemap",
  "ismap",
]

```

      
        EMBED_ATTRS =
          
        
        

```
[
  COREATTRS,
  "align",
  "alt",
  "border",
  "code",
  "codebase",
  "frameborder",
  "height",
  "hidden",
  "hspace",
  "name",
  "palette",
  "pluginspace",
  "pluginurl",
  "src",
  "type",
  "units",
  "vspace",
  "width",
]

```

      
        INPUT_ATTRS =
          
        
        

```
[
  ATTRS,
  "type",
  "name",
  "value",
  "checked",
  "disabled",
  "readonly",
  "size",
  "maxlength",
  "src",
  "alt",
  "usemap",
  "ismap",
  "tabindex",
  "accesskey",
  "onfocus",
  "onblur",
  "onselect",
  "onchange",
  "accept",
]

```

      
        PROMPT_ATTRS =
          
        
        

```
[COREATTRS, I18N, "prompt"]

```

      
        LABEL_ATTRS =
          
        
        

```
[ATTRS, "for", "accesskey", "onfocus", "onblur"]

```

      
        LEGEND_ATTRS =
          
        
        

```
[ATTRS, "accesskey"]

```

      
        ALIGN_ATTR =
          
        
        

```
["align"]

```

      
        LINK_ATTRS =
          
        
        

```
[
  ATTRS,
  "charset",
  "href",
  "hreflang",
  "type",
  "rel",
  "rev",
  "media",
]

```

      
        MAP_CONTENTS =
          
        
        

```
[BLOCK, "area"]

```

      
        NAME_ATTR =
          
        
        

```
["name"]

```

      
        ACTION_ATTR =
          
        
        

```
["action"]

```

      
        BLOCKLI_ELT =
          
        
        

```
[BLOCK, "li"]

```

      
        META_ATTRS =
          
        
        

```
[I18N, "http-equiv", "name", "scheme"]

```

      
        CONTENT_ATTR =
          
        
        

```
["content"]

```

      
        TYPE_ATTR =
          
        
        

```
["type"]

```

      
        NOFRAMES_CONTENT =
          
        
        

```
["body", FLOW, MODIFIER]

```

      
        OBJECT_CONTENTS =
          
        
        

```
[FLOW, "param"]

```

      
        OBJECT_ATTRS =
          
        
        

```
[
  ATTRS,
  "declare",
  "classid",
  "codebase",
  "data",
  "type",
  "codetype",
  "archive",
  "standby",
  "height",
  "width",
  "usemap",
  "name",
  "tabindex",
]

```

      
        OBJECT_DEPR =
          
        
        

```
["align", "border", "hspace", "vspace"]

```

      
        OL_ATTRS =
          
        
        

```
["type", "compact", "start"]

```

      
        OPTION_ELT =
          
        
        

```
["option"]

```

      
        OPTGROUP_ATTRS =
          
        
        

```
[ATTRS, "disabled"]

```

      
        OPTION_ATTRS =
          
        
        

```
[ATTRS, "disabled", "label", "selected", "value"]

```

      
        PARAM_ATTRS =
          
        
        

```
["id", "value", "valuetype", "type"]

```

      
        WIDTH_ATTR =
          
        
        

```
["width"]

```

      
        PRE_CONTENT =
          
        
        

```
[
  PHRASE,
  "tt",
  "i",
  "b",
  "u",
  "s",
  "strike",
  "a",
  "br",
  "script",
  "map",
  "q",
  "span",
  "bdo",
  "iframe",
]

```

      
        SCRIPT_ATTRS =
          
        
        

```
["charset", "src", "defer", "event", "for"]

```

      
        LANGUAGE_ATTR =
          
        
        

```
["language"]

```

      
        SELECT_CONTENT =
          
        
        

```
["optgroup", "option"]

```

      
        SELECT_ATTRS =
          
        
        

```
[
  ATTRS,
  "name",
  "size",
  "multiple",
  "disabled",
  "tabindex",
  "onfocus",
  "onblur",
  "onchange",
]

```

      
        STYLE_ATTRS =
          
        
        

```
[I18N, "media", "title"]

```

      
        TABLE_ATTRS =
          
        
        

```
[
  ATTRS,
  "summary",
  "width",
  "border",
  "frame",
  "rules",
  "cellspacing",
  "cellpadding",
  "datapagesize",
]

```

      
        TABLE_DEPR =
          
        
        

```
["align", "bgcolor"]

```

      
        TABLE_CONTENTS =
          
        
        

```
[
  "caption",
  "col",
  "colgroup",
  "thead",
  "tfoot",
  "tbody",
  "tr",
]

```

      
        TR_ELT =
          
        
        

```
["tr"]

```

      
        TALIGN_ATTRS =
          
        
        

```
[ATTRS, CELLHALIGN, CELLVALIGN]

```

      
        TH_TD_DEPR =
          
        
        

```
["nowrap", "bgcolor", "width", "height"]

```

      
        TH_TD_ATTR =
          
        
        

```
[
  ATTRS,
  "abbr",
  "axis",
  "headers",
  "scope",
  "rowspan",
  "colspan",
  CELLHALIGN,
  CELLVALIGN,
]

```

      
        TEXTAREA_ATTRS =
          
        
        

```
[
  ATTRS,
  "name",
  "disabled",
  "readonly",
  "tabindex",
  "accesskey",
  "onfocus",
  "onblur",
  "onselect",
  "onchange",
]

```

      
        TR_CONTENTS =
          
        
        

```
["th", "td"]

```

      
        BGCOLOR_ATTR =
          
        
        

```
["bgcolor"]

```

      
        LI_ELT =
          
        
        

```
["li"]

```

      
        UL_DEPR =
          
        
        

```
["type", "compact"]

```

      
        DIR_ATTR =
          
        
        

```
["dir"]

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**[]**(tag_name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get ElementDescription for `tag_name`.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**block?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this element a block element?.

  

      
        
- 
  
    
      #**default_sub_element**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The default sub element for this element.

  

      
        
- 
  
    
      #**deprecated?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this element deprecated?.

  

      
        
- 
  
    
      #**deprecated_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A list of deprecated attributes for this element.

  

      
        
- 
  
    
      #**description**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The description for this element.

  

      
        
- 
  
    
      #**empty?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this an empty element?.

  

      
        
- 
  
    
      #**implied_end_tag?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Can the end tag be implied for this tag?.

  

      
        
- 
  
    
      #**implied_start_tag?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Can the start tag be implied for this tag?.

  

      
        
- 
  
    
      #**inline?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Is this element an inline element?.

  

      
        
- 
  
    
      #**inspect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Inspection information.

  

      
        
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Get the tag name for this ElementDescription.

  

      
        
- 
  
    
      #**optional_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A list of optional attributes for this element.

  

      
        
- 
  
    
      #**required_attributes**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A list of required attributes for this element.

  

      
        
- 
  
    
      #**save_end_tag?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Should the end tag be saved?.

  

      
        
- 
  
    
      #**sub_elements**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

A list of allowed sub elements for this element.

  

      
        
- 
  
    
      #**to_s**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert this description to a string.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**[]**(tag_name)  ⇒ Object 
  

  

  

  
    

Get ElementDescription for `tag_name`

  

  
  

  
    
      

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
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 266

static VALUE
get_description(VALUE klass, VALUE tag_name)
{
  const htmlElemDesc *description = htmlTagLookup(
                                      (const xmlChar *)StringValueCStr(tag_name)
                                    );

  if (NULL == description) { return Qnil; }
  return TypedData_Wrap_Struct(klass, &html_elem_desc_type, DISCARD_CONST_QUAL(void *, description));
}

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**block?**  ⇒ Boolean 
  

  

  

  
    

Is this element a block element?

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

8
9
10
```

    
    
      

```
# File 'lib/nokogiri/html4/element_description.rb', line 8

def block?
  !inline?
end

```

    
  

    
      
  
### 
  
    #**default_sub_element**  ⇒ Object 
  

  

  

  
    

The default sub element for this element

  

  
  

  
    
      

```

94
95
96
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 94

def default_sub_element
  default_desc&.defaultsubelt
end

```

    
  

    
      
  
### 
  
    #**deprecated?**  ⇒ Boolean 
  

  

  

  
    

Is this element deprecated?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

170
171
172
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 170

def deprecated?
  default_desc&.depr
end

```

    
  

    
      
  
### 
  
    #**deprecated_attributes**  ⇒ Object 
  

  

  

  
    

A list of deprecated attributes for this element

  

  
  

  
    
      

```

42
43
44
45
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 42

def deprecated_attributes
  d = default_desc
  d ? d.attrs_depr : []
end

```

    
  

    
      
  
### 
  
    #**description**  ⇒ Object 
  

  

  

  
    

The description for this element

  

  
  

  
    
      

```

139
140
141
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 139

def description
  default_desc&.desc
end

```

    
  

    
      
  
### 
  
    #**empty?**  ⇒ Boolean 
  

  

  

  
    

Is this an empty element?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

186
187
188
189
190
191
192
193
194
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 186

static VALUE
empty_eh(VALUE self)
{
  const htmlElemDesc *description;
  TypedData_Get_Struct(self, htmlElemDesc, &html_elem_desc_type, description);

  if (description->empty) { return Qtrue; }
  return Qfalse;
}

```

    
  

    
      
  
### 
  
    #**implied_end_tag?**  ⇒ Boolean 
  

  

  

  
    

Can the end tag be implied for this tag?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

218
219
220
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 218

def implied_end_tag?
  default_desc&.endTag
end

```

    
  

    
      
  
### 
  
    #**implied_start_tag?**  ⇒ Boolean 
  

  

  

  
    

Can the start tag be implied for this tag?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

234
235
236
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 234

def implied_start_tag?
  default_desc&.startTag
end

```

    
  

    
      
  
### 
  
    #**inline?**  ⇒ Boolean 
  

  

  

  
    

Is this element an inline element?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

154
155
156
157
158
159
160
161
162
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 154

static VALUE
inline_eh(VALUE self)
{
  const htmlElemDesc *description;
  TypedData_Get_Struct(self, htmlElemDesc, &html_elem_desc_type, description);

  if (description->isinline) { return Qtrue; }
  return Qfalse;
}

```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

Inspection information

  

  

  
    
      

```

20
21
22
```

    
    
      

```
# File 'lib/nokogiri/html4/element_description.rb', line 20

def inspect
  "#<#{self.class.name}: #{name} #{description}>"
end

```

    
  

    
      
  
### 
  
    #**name**  ⇒ Object 
  

  

  

  
    

Get the tag name for this ElementDescription

  

  
  

  
    
      

```

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
# File 'ext/nokogiri/html4_element_description.c', line 250

static VALUE
name(VALUE self)
{
  const htmlElemDesc *description;
  TypedData_Get_Struct(self, htmlElemDesc, &html_elem_desc_type, description);

  if (NULL == description->name) { return Qnil; }
  return NOKOGIRI_STR_NEW2(description->name);
}

```

    
  

    
      
  
### 
  
    #**optional_attributes**  ⇒ Object 
  

  

  

  
    

A list of optional attributes for this element

  

  
  

  
    
      

```

68
69
70
71
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 68

def optional_attributes
  d = default_desc
  d ? d.attrs_opt : []
end

```

    
  

    
      
  
### 
  
    #**required_attributes**  ⇒ Object 
  

  

  

  
    

A list of required attributes for this element

  

  
  

  
    
      

```

16
17
18
19
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 16

def required_attributes
  d = default_desc
  d ? d.attrs_req : []
end

```

    
  

    
      
  
### 
  
    #**save_end_tag?**  ⇒ Boolean 
  

  

  

  
    

Should the end tag be saved?

  

  
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

202
203
204
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 202

def save_end_tag?
  default_desc&.saveEndTag
end

```

    
  

    
      
  
### 
  
    #**sub_elements**  ⇒ Object 
  

  

  

  
    

A list of allowed sub elements for this element.

  

  
  

  
    
      

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
128
129
130
131
```

    
    
      

```
# File 'ext/nokogiri/html4_element_description.c', line 113

static VALUE
sub_elements(VALUE self)
{
  const htmlElemDesc *description;
  VALUE list;
  int i;

  TypedData_Get_Struct(self, htmlElemDesc, &html_elem_desc_type, description);

  list = rb_ary_new();

  if (NULL == description->subelts) { return list; }

  for (i = 0; description->subelts[i]; i++) {
    rb_ary_push(list, NOKOGIRI_STR_NEW2(description->subelts[i]));
  }

  return list;
}

```

    
  

    
      
  
### 
  
    #**to_s**  ⇒ Object 
  

  

  

  
    

Convert this description to a string

  

  

  
    
      

```

14
15
16
```

    
    
      

```
# File 'lib/nokogiri/html4/element_description.rb', line 14

def to_s
  "#{name}: #{description}"
end

```