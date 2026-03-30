# Class: Kramdown::Converter::Html
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Converter::Html
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Parser::Html::Constants, Utils::Html
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/html.rb
  
  

## Overview

  
    

Converts a Kramdown::Document to HTML.

You can customize the HTML converter by sub-classing it and overriding the `convert_NAME` methods. Each such method takes the following parameters:
`el`

The element of type `NAME` to be converted.
`indent`

A number representing the current amount of spaces for indent (only used for block-level elements).

The return value of such a method has to be a string containing the element `el` formatted as HTML element.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ENTITY_NBSP =
          
  
    

:nodoc:

  

  

        
        

```
::Kramdown::Utils::Entities.entity('nbsp')

```

      
        TYPOGRAPHIC_SYMS =
          
        
        

```
{
  mdash: [::Kramdown::Utils::Entities.entity('mdash')],
  ndash: [::Kramdown::Utils::Entities.entity('ndash')],
  hellip: [::Kramdown::Utils::Entities.entity('hellip')],
  laquo_space: [::Kramdown::Utils::Entities.entity('laquo'),
                ::Kramdown::Utils::Entities.entity('nbsp')],
  raquo_space: [::Kramdown::Utils::Entities.entity('nbsp'),
                ::Kramdown::Utils::Entities.entity('raquo')],
  laquo: [::Kramdown::Utils::Entities.entity('laquo')],
  raquo: [::Kramdown::Utils::Entities.entity('raquo')],
}

```

      
        FOOTNOTE_BACKLINK_FMT =
          
        
        

```
"%s<a href=\"#fnref:%s\" class=\"reversefootnote\" role=\"doc-backlink\">%s</a>"

```

      
    
  

  
  
  
### Constants included
     from Parser::Html::Constants

  

Parser::Html::Constants::HTML_ATTRIBUTE_RE, Parser::Html::Constants::HTML_BLOCK_ELEMENTS, Parser::Html::Constants::HTML_CDATA_RE, Parser::Html::Constants::HTML_COMMENT_RE, Parser::Html::Constants::HTML_CONTENT_MODEL, Parser::Html::Constants::HTML_CONTENT_MODEL_BLOCK, Parser::Html::Constants::HTML_CONTENT_MODEL_RAW, Parser::Html::Constants::HTML_CONTENT_MODEL_SPAN, Parser::Html::Constants::HTML_DOCTYPE_RE, Parser::Html::Constants::HTML_ELEMENT, Parser::Html::Constants::HTML_ELEMENTS_WITHOUT_BODY, Parser::Html::Constants::HTML_ENTITY_RE, Parser::Html::Constants::HTML_INSTRUCTION_RE, Parser::Html::Constants::HTML_SPAN_ELEMENTS, Parser::Html::Constants::HTML_TAG_CLOSE_RE, Parser::Html::Constants::HTML_TAG_RE

  
  
  
### Constants included
     from Utils::Html

  

Utils::Html::ESCAPE_ALL_RE, Utils::Html::ESCAPE_ATTRIBUTE_RE, Utils::Html::ESCAPE_MAP, Utils::Html::ESCAPE_RE_FROM_TYPE, Utils::Html::ESCAPE_TEXT_RE, Utils::Html::REDUNDANT_LINE_BREAK_REGEX

  
  
  
### Constants inherited
     from Base

  

Base::SMART_QUOTE_INDICES

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**indent**  ⇒ Object 
    

    
  
  
  
  
    
    
  
  
  
  
  

  
    

The amount of indentation used when nesting HTML tags.

  

    
  

  
  
  
### Attributes inherited from Base

  

#data, #options, #root, #warnings

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**add_syntax_highlighter_to_class_attr**(attr, lang = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add the syntax highlighter name to the ‘class’ attribute of the given attribute hash.

  

      
        
- 
  
    
      #**convert**(el, indent = -@indent))  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Dispatch the conversion of the element `el` to a `convert_TYPE` method using the `type` of the element.

  

      
        
- 
  
    
      #**convert_a**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_abbreviation**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_blank**(_el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_blockquote**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_br**(_el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_codeblock**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_codespan**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_comment**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_dl**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_dt**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_em**(el, indent)  ⇒ Object 
    

    
      (also: #convert_strong)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_entity**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_footnote**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_header**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_hr**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_html_element**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_img**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_li**(el, indent)  ⇒ Object 
    

    
      (also: #convert_dd)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_math**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_p**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_raw**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_root**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_smart_quote**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_standalone_image**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Helper method used by `convert_p` to convert a paragraph that only contains a single :img element.

  

      
        
- 
  
    
      #**convert_table**(el, indent)  ⇒ Object 
    

    
      (also: #convert_thead, #convert_tbody, #convert_tfoot, #convert_tr)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_td**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_text**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_typographic_sym**(el, _indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

:nodoc:.

  

      
        
- 
  
    
      #**convert_ul**(el, indent)  ⇒ Object 
    

    
      (also: #convert_ol)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_xml_comment**(el, indent)  ⇒ Object 
    

    
      (also: #convert_xml_pi)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**fix_for_toc_entry**(elements)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Fixes the elements for use in a TOC entry.

  

      
        
- 
  
    
      #**footnote_content**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return an HTML ordered list with the footnote content for the used footnotes.

  

      
        
- 
  
    
      #**format_as_block_html**(name, attr, body, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Format the given element as block HTML.

  

      
        
- 
  
    
      #**format_as_indented_block_html**(name, attr, body, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Format the given element as block HTML with a newline after the start tag and indentation before the end tag.

  

      
        
- 
  
    
      #**format_as_span_html**(name, attr, body)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Format the given element as span HTML.

  

      
        
- 
  
    
      #**generate_toc_tree**(toc, type, attr)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Generate and return an element tree for the table of contents.

  

      
        
- 
  
    
      #**initialize**(root, options)  ⇒ Html 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize the HTML converter with the given Kramdown document `doc`.

  

      
        
- 
  
    
      #**inner**(el, indent)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the converted content of the children of `el` as a string.

  

      
        
- 
  
    
      #**obfuscate**(text)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Obfuscate the `text` by using HTML entities.

  

      
        
- 
  
    
      #**remove_footnotes**(elements)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Remove all footnotes from the given elements.

  

      
        
- 
  
    
      #**unwrap_links**(elements)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Remove all link elements by unwrapping them.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
### Methods included from Utils::Html

  

#entity_to_str, #escape_html, #fix_cjk_line_break, #html_attributes

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

apply_template, #apply_template_after?, #apply_template_before?, #basic_generate_id, convert, #extract_code_language, #extract_code_language!, #format_math, #generate_id, get_template, #highlight_code, #in_toc?, #output_header_level, #smart_quote_entity, #warning

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root, options)  ⇒ Html 
  

  

  

  
    

Initialize the HTML converter with the given Kramdown document `doc`.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 39

def initialize(root, options)
  super
  @footnote_counter = @footnote_start = @options[:footnote_nr]
  @footnotes = []
  @footnotes_by_name = {}
  @footnote_location = nil
  @toc = []
  @toc_code = nil
  @indent = 2
  @stack = []

  # stash string representation of symbol to avoid allocations from multiple interpolations.
  @highlighter_class = " highlighter-#{options[:syntax_highlighter]}"
  @dispatcher = Hash.new {|h, k| h[k] = :"convert_#{k}" }
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**indent**  ⇒ Object 
  

  

  

  
    

The amount of indentation used when nesting HTML tags.

  

  

  
    
      

```

36
37
38
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 36

def indent
  @indent
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**add_syntax_highlighter_to_class_attr**(attr, lang = nil)  ⇒ Object 
  

  

  

  
    

Add the syntax highlighter name to the ‘class’ attribute of the given attribute hash. And overwrites or add a “language-LANG” part using the `lang` parameter if `lang` is not nil.

  

  

  
    
      

```

417
418
419
420
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 417

def add_syntax_highlighter_to_class_attr(attr, lang = nil)
  (attr['class'] = (attr['class'] || '') + @highlighter_class).lstrip!
  attr['class'].sub!(/\blanguage-\S+|(^)/) { "language-#{lang}#{$1 ? ' ' : ''}" } if lang
end

```

    
  

    
      
  
### 
  
    #**convert**(el, indent = -@indent))  ⇒ Object 
  

  

  

  
    

Dispatch the conversion of the element `el` to a `convert_TYPE` method using the `type` of the element.

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 57

def convert(el, indent = -@indent)
  send(@dispatcher[el.type], el, indent)
end

```

    
  

    
      
  
### 
  
    #**convert_a**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

283
284
285
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 283

def convert_a(el, indent)
  format_as_span_html("a", el.attr, inner(el, indent))
end

```

    
  

    
      
  
### 
  
    #**convert_abbreviation**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

377
378
379
380
381
382
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 377

def convert_abbreviation(el, _indent)
  title = @root.options[:abbrev_defs][el.value]
  attr = @root.options[:abbrev_attr][el.value].dup
  attr['title'] = title unless title.empty?
  format_as_span_html("abbr", attr, el.value)
end

```

    
  

    
      
  
### 
  
    #**convert_blank**(_el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 77

def convert_blank(_el, _indent)
  "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_blockquote**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

145
146
147
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 145

def convert_blockquote(el, indent)
  format_as_indented_block_html("blockquote", el.attr, inner(el, indent), indent)
end

```

    
  

    
      
  
### 
  
    #**convert_br**(_el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

279
280
281
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 279

def convert_br(_el, _indent)
  "<br />"
end

```

    
  

    
      
  
### 
  
    #**convert_codeblock**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

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
133
134
135
136
137
138
139
140
141
142
143
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 115

def convert_codeblock(el, indent)
  attr = el.attr.dup
  lang = extract_code_language!(attr)
  hl_opts = {}
  highlighted_code = highlight_code(el.value, el.options[:lang] || lang, :block, hl_opts)

  if highlighted_code
    add_syntax_highlighter_to_class_attr(attr, lang || hl_opts[:default_lang])
    "#{' ' * indent}<div#{html_attributes(attr)}>#{highlighted_code}#{' ' * indent}</div>\n"
  else
    result = escape_html(el.value)
    result.chomp!
    if el.attr['class'].to_s =~ /\bshow-whitespaces\b/
      result.gsub!(/(?:(^[ \t]+)|([ \t]+$)|([ \t]+))/) do |m|
        suffix = ($1 ? '-l' : ($2 ? '-r' : ''))
        m.scan(/./).map do |c|
          case c
          when "\t" then "<span class=\"ws-tab#{suffix}\">\t</span>"
          when " " then "<span class=\"ws-space#{suffix}\">⋅</span>"
          end
        end.join
      end
    end
    code_attr = {}
    code_attr['class'] = "language-#{lang}" if lang
    "#{' ' * indent}<pre#{html_attributes(attr)}>" \
      "<code#{html_attributes(code_attr)}>#{result}\n</code></pre>\n"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_codespan**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

291
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
# File 'lib/kramdown/converter/html.rb', line 291

def convert_codespan(el, _indent)
  attr = el.attr.dup
  lang = extract_code_language(attr)
  hl_opts = {}
  result = highlight_code(el.value, lang, :span, hl_opts)
  if result
    add_syntax_highlighter_to_class_attr(attr, lang || hl_opts[:default_lang])
  else
    result = escape_html(el.value)
  end

  format_as_span_html('code', attr, result)
end

```

    
  

    
      
  
### 
  
    #**convert_comment**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

271
272
273
274
275
276
277
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 271

def convert_comment(el, indent)
  if el.options[:category] == :block
    "#{' ' * indent}<!-- #{el.value} -->\n"
  else
    "<!-- #{el.value} -->"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_dl**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

185
186
187
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 185

def convert_dl(el, indent)
  format_as_indented_block_html("dl", el.attr, inner(el, indent), indent)
end

```

    
  

    
      
  
### 
  
    #**convert_dt**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 201

def convert_dt(el, indent)
  attr = el.attr.dup
  @stack.last.options[:ial][:refs].each do |ref|
    if ref =~ /\Aauto_ids(?:-([\w-]+))?/
      attr['id'] = "#{$1}#{basic_generate_id(el.options[:raw_text])}".lstrip
      break
    end
  end if !attr['id'] && @stack.last.options[:ial] && @stack.last.options[:ial][:refs]
  format_as_block_html("dt", attr, inner(el, indent), indent)
end

```

    
  

    
      
  
### 
  
    #**convert_em**(el, indent)  ⇒ Object 
  

  
    Also known as:
    convert_strong
    
  

  

  
    
      

```

331
332
333
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 331

def convert_em(el, indent)
  format_as_span_html(el.type, el.attr, inner(el, indent))
end

```

    
  

    
      
  
### 
  
    #**convert_entity**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

336
337
338
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 336

def convert_entity(el, _indent)
  entity_to_str(el.value, el.options[:original])
end

```

    
  

    
      
  
### 
  
    #**convert_footnote**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

305
306
307
308
309
310
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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 305

def convert_footnote(el, _indent)
  repeat = ''
  name = @options[:footnote_prefix] + el.options[:name]
  if (footnote = @footnotes_by_name[name])
    number = footnote[2]
    repeat = ":#{footnote[3] += 1}"
  else
    number = @footnote_counter
    @footnote_counter += 1
    @footnotes << [name, el.value, number, 0]
    @footnotes_by_name[name] = @footnotes.last
  end
  formatted_link_text = sprintf(@options[:footnote_link_text], number)
  "<sup id=\"fnref:#{name}#{repeat}\">" \
    "<a href=\"#fn:#{name}\" class=\"footnote\" rel=\"footnote\" role=\"doc-noteref\">" \
    "#{formatted_link_text}</a></sup>"
end

```

    
  

    
      
  
### 
  
    #**convert_header**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/kramdown/converter/html.rb', line 149

def convert_header(el, indent)
  attr = el.attr.dup
  if @options[:auto_ids] && !attr['id']
    attr['id'] = generate_id(el.options[:raw_text])
  end

  if @options[:header_links] && attr['id'].to_s.length > 0
    link = Element.new(:a, nil, nil)
    link.attr['href'] = "##{attr['id']}"
    el.children.unshift(link)
  end

  @toc << [el.options[:level], attr['id'], el.children] if attr['id'] && in_toc?(el)
  level = output_header_level(el.options[:level])
  format_as_block_html("h#{level}", attr, inner(el, indent), indent)
end

```

    
  

    
      
  
### 
  
    #**convert_hr**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

166
167
168
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 166

def convert_hr(el, indent)
  "#{' ' * indent}<hr#{html_attributes(el.attr)} />\n"
end

```

    
  

    
      
  
### 
  
    #**convert_html_element**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

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
230
231
232
233
234
235
236
237
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 212

def convert_html_element(el, indent)
  res = inner(el, indent)
  if el.options[:category] == :span
    "<#{el.value}#{html_attributes(el.attr)}" + \
      (res.empty? && HTML_ELEMENTS_WITHOUT_BODY.include?(el.value) ? " />" : ">#{res}</#{el.value}>")
  else
    output = +''
    if @stack.last.type != :html_element || @stack.last.options[:content_model] != :raw
      output << ' ' * indent
    end
    output << "<#{el.value}#{html_attributes(el.attr)}"
    if el.options[:is_closed] && el.options[:content_model] == :raw
      output << " />"
    elsif !res.empty? && el.options[:content_model] != :block
      output << ">#{res}</#{el.value}>"
    elsif !res.empty?
      output << ">\n#{res.chomp}\n" << ' ' * indent << "</#{el.value}>"
    elsif HTML_ELEMENTS_WITHOUT_BODY.include?(el.value)
      output << " />"
    else
      output << "></#{el.value}>"
    end
    output << "\n" if @stack.last.type != :html_element || @stack.last.options[:content_model] != :raw
    output
  end
end

```

    
  

    
      
  
### 
  
    #**convert_img**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

287
288
289
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 287

def convert_img(el, _indent)
  "<img#{html_attributes(el.attr)} />"
end

```

    
  

    
      
  
### 
  
    #**convert_li**(el, indent)  ⇒ Object 
  

  
    Also known as:
    convert_dd
    
  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 189

def convert_li(el, indent)
  output = ' ' * indent << "<#{el.type}" << html_attributes(el.attr) << ">"
  res = inner(el, indent)
  if el.children.empty? || (el.children.first.type == :p && el.children.first.options[:transparent])
    output << res << (res.match?(/\n\Z/) ? ' ' * indent : '')
  else
    output << "\n" << res << ' ' * indent
  end
  output << "</#{el.type}>\n"
end

```

    
  

    
      
  
### 
  
    #**convert_math**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

363
364
365
366
367
368
369
370
371
372
373
374
375
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 363

def convert_math(el, indent)
  if (result = format_math(el, indent: indent))
    result
  else
    attr = el.attr.dup
    attr['class'] = "#{attr['class']} kdmath".lstrip
    if el.options[:category] == :block
      format_as_block_html('div', attr, "$$\n#{el.value}\n$$", indent)
    else
      format_as_span_html('span', attr, "$#{el.value}$")
    end
  end
end

```

    
  

    
      
  
### 
  
    #**convert_p**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 86

def convert_p(el, indent)
  if el.options[:transparent]
    inner(el, indent)
  elsif el.children.size == 1 && el.children.first.type == :img &&
      el.children.first.options[:ial]&.[](:refs)&.include?('standalone')
    convert_standalone_image(el, indent)
  else
    format_as_block_html("p", el.attr, inner(el, indent), indent)
  end
end

```

    
  

    
      
  
### 
  
    #**convert_raw**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

323
324
325
326
327
328
329
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 323

def convert_raw(el, _indent)
  if !el.options[:type] || el.options[:type].empty? || el.options[:type].include?('html')
    el.value + (el.options[:category] == :block ? "\n" : '')
  else
    ''
  end
end

```

    
  

    
      
  
### 
  
    #**convert_root**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

384
385
386
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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 384

def convert_root(el, indent)
  result = inner(el, indent)
  if @footnote_location
    result.sub!(/#{@footnote_location}/, footnote_content.gsub(/\\/, "\\\\\\\\"))
  else
    result << footnote_content
  end
  if @toc_code
    toc_tree = generate_toc_tree(@toc, @toc_code[0], @toc_code[1] || {})
    text = toc_tree.children.empty? ? '' : convert(toc_tree, 0)
    result.sub!(/#{@toc_code.last}/, text.gsub(/\\/, "\\\\\\\\"))
  end
  result
end

```

    
  

    
      
  
### 
  
    #**convert_smart_quote**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

359
360
361
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 359

def convert_smart_quote(el, _indent)
  entity_to_str(smart_quote_entity(el))
end

```

    
  

    
      
  
### 
  
    #**convert_standalone_image**(el, indent)  ⇒ Object 
  

  

  

  
    

Helper method used by `convert_p` to convert a paragraph that only contains a single :img element.

  

  

  
    
      

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
113
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 99

def convert_standalone_image(el, indent)
  figure_attr = el.attr.dup
  image_attr = el.children.first.attr.dup

  if image_attr.key?('class') && !figure_attr.key?('class')
    figure_attr['class'] = image_attr.delete('class')
  end
  if image_attr.key?('id') && !figure_attr.key?('id')
    figure_attr['id'] = image_attr.delete('id')
  end

  body = "#{' ' * (indent + @indent)}<img#{html_attributes(image_attr)} />\n" \
    "#{' ' * (indent + @indent)}<figcaption>#{image_attr['alt']}</figcaption>\n"
  format_as_indented_block_html("figure", figure_attr, body, indent)
end

```

    
  

    
      
  
### 
  
    #**convert_table**(el, indent)  ⇒ Object 
  

  
    Also known as:
    convert_thead, convert_tbody, convert_tfoot, convert_tr
    
  

  

  
    
      

```

249
250
251
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 249

def convert_table(el, indent)
  format_as_indented_block_html(el.type, el.attr, inner(el, indent), indent)
end

```

    
  

    
      
  
### 
  
    #**convert_td**(el, indent)  ⇒ Object 
  

  

  

  
    
      

```

259
260
261
262
263
264
265
266
267
268
269
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 259

def convert_td(el, indent)
  res = inner(el, indent)
  type = (@stack[-2].type == :thead ? :th : :td)
  attr = el.attr
  alignment = @stack[-3].options[:alignment][@stack.last.children.index(el)]
  if alignment != :default
    attr = el.attr.dup
    attr['style'] = (attr.key?('style') ? "#{attr['style']}; " : '') + "text-align: #{alignment}"
  end
  format_as_block_html(type, attr, res.empty? ? entity_to_str(ENTITY_NBSP) : res, indent)
end

```

    
  

    
      
  
### 
  
    #**convert_text**(el, _indent)  ⇒ Object 
  

  

  

  
    
      

```

81
82
83
84
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 81

def convert_text(el, _indent)
  escaped = escape_html(el.value, :text)
  @options[:remove_line_breaks_for_cjk] ? fix_cjk_line_break(escaped) : escaped
end

```

    
  

    
      
  
### 
  
    #**convert_typographic_sym**(el, _indent)  ⇒ Object 
  

  

  

  
    

:nodoc:

  

  

  
    
      

```

351
352
353
354
355
356
357
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 351

def convert_typographic_sym(el, _indent)
  if (result = @options[:typographic_symbols][el.value])
    escape_html(result, :text)
  else
    TYPOGRAPHIC_SYMS[el.value].map {|e| entity_to_str(e) }.join
  end
end

```

    
  

    
      
  
### 
  
    #**convert_ul**(el, indent)  ⇒ Object 
  

  
    Also known as:
    convert_ol
    
  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 173

def convert_ul(el, indent)
  if !@toc_code && el.options.dig(:ial, :refs)&.include?('toc')
    @toc_code = [el.type, el.attr, ZERO_TO_ONETWENTYEIGHT.map { rand(36).to_s(36) }.join]
    @toc_code.last
  elsif !@footnote_location && el.options.dig(:ial, :refs)&.include?('footnotes')
    @footnote_location = ZERO_TO_ONETWENTYEIGHT.map { rand(36).to_s(36) }.join
  else
    format_as_indented_block_html(el.type, el.attr, inner(el, indent), indent)
  end
end

```

    
  

    
      
  
### 
  
    #**convert_xml_comment**(el, indent)  ⇒ Object 
  

  
    Also known as:
    convert_xml_pi
    
  

  

  
    
      

```

239
240
241
242
243
244
245
246
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 239

def convert_xml_comment(el, indent)
  if el.options[:category] == :block &&
      (@stack.last.type != :html_element || @stack.last.options[:content_model] != :raw)
    ' ' * indent << el.value << "\n"
  else
    el.value
  end
end

```

    
  

    
      
  
### 
  
    #**fix_for_toc_entry**(elements)  ⇒ Object 
  

  

  

  
    

Fixes the elements for use in a TOC entry.

  

  

  
    
      

```

461
462
463
464
465
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 461

def fix_for_toc_entry(elements)
  remove_footnotes(elements)
  unwrap_links(elements)
  elements
end

```

    
  

    
      
  
### 
  
    #**footnote_content**  ⇒ Object 
  

  

  

  
    

Return an HTML ordered list with the footnote content for the used footnotes.

  

  

  
    
      

```

496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 496

def footnote_content
  ol = Element.new(:ol)
  ol.attr['start'] = @footnote_start if @footnote_start != 1
  i = 0
  backlink_text = escape_html(@options[:footnote_backlink], :text)
  while i < @footnotes.length
    name, data, _, repeat = *@footnotes[i]
    li = Element.new(:li, nil, 'id' => "fn:#{name}")
    li.children = Marshal.load(Marshal.dump(data.children))

    para = nil
    if li.children.last.type == :p || @options[:footnote_backlink_inline]
      parent = li
      while !parent.children.empty? && ![:p, :header].include?(parent.children.last.type)
        parent = parent.children.last
      end
      para = parent.children.last
      insert_space = true
    end

    unless para
      li.children << (para = Element.new(:p))
      insert_space = false
    end

    unless @options[:footnote_backlink].empty?
      nbsp = entity_to_str(ENTITY_NBSP)
      value = sprintf(FOOTNOTE_BACKLINK_FMT, (insert_space ? nbsp : ''), name, backlink_text)
      para.children << Element.new(:raw, value)
      (1..repeat).each do |index|
        value = sprintf(FOOTNOTE_BACKLINK_FMT, nbsp, "#{name}:#{index}",
                        "#{backlink_text}<sup>#{index + 1}</sup>")
        para.children << Element.new(:raw, value)
      end
    end

    ol.children << Element.new(:raw, convert(li, 4))
    i += 1
  end
  if ol.children.empty?
    ''
  else
    format_as_indented_block_html('div', {class: "footnotes", role: "doc-endnotes"}, convert(ol, 2), 0)
  end
end

```

    
  

    
      
  
### 
  
    #**format_as_block_html**(name, attr, body, indent)  ⇒ Object 
  

  

  

  
    

Format the given element as block HTML.

  

  

  
    
      

```

405
406
407
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 405

def format_as_block_html(name, attr, body, indent)
  "#{' ' * indent}<#{name}#{html_attributes(attr)}>#{body}</#{name}>\n"
end

```

    
  

    
      
  
### 
  
    #**format_as_indented_block_html**(name, attr, body, indent)  ⇒ Object 
  

  

  

  
    

Format the given element as block HTML with a newline after the start tag and indentation before the end tag.

  

  

  
    
      

```

411
412
413
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 411

def format_as_indented_block_html(name, attr, body, indent)
  "#{' ' * indent}<#{name}#{html_attributes(attr)}>\n#{body}#{' ' * indent}</#{name}>\n"
end

```

    
  

    
      
  
### 
  
    #**format_as_span_html**(name, attr, body)  ⇒ Object 
  

  

  

  
    

Format the given element as span HTML.

  

  

  
    
      

```

400
401
402
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 400

def format_as_span_html(name, attr, body)
  "<#{name}#{html_attributes(attr)}>#{body}</#{name}>"
end

```

    
  

    
      
  
### 
  
    #**generate_toc_tree**(toc, type, attr)  ⇒ Object 
  

  

  

  
    

Generate and return an element tree for the table of contents.

  

  

  
    
      

```

423
424
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
437
438
439
440
441
442
443
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
456
457
458
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 423

def generate_toc_tree(toc, type, attr)
  sections = Element.new(type, nil, attr.dup)
  sections.attr['id'] ||= 'markdown-toc'
  stack = []
  toc.each do |level, id, children|
    li = Element.new(:li, nil, nil, level: level)
    li.children << Element.new(:p, nil, nil, transparent: true)
    a = Element.new(:a, nil)
    a.attr['href'] = "##{id}"
    a.attr['id'] = "#{sections.attr['id']}-#{id}"
    a.children.concat(fix_for_toc_entry(Marshal.load(Marshal.dump(children))))
    li.children.last.children << a
    li.children << Element.new(type)

    success = false
    until success
      if stack.empty?
        sections.children << li
        stack << li
        success = true
      elsif stack.last.options[:level] < li.options[:level]
        stack.last.children.last.children << li
        stack << li
        success = true
      else
        item = stack.pop
        item.children.pop if item.children.last.children.empty?
      end
    end
  end
  until stack.empty?
    item = stack.pop
    item.children.pop if item.children.last.children.empty?
  end
  sections
end

```

    
  

    
      
  
### 
  
    #**inner**(el, indent)  ⇒ Object 
  

  

  

  
    

Return the converted content of the children of `el` as a string. The parameter `indent` has to be the amount of indentation used for the element `el`.

Pushes `el` onto the @stack before converting the child elements and pops it from the stack afterwards.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 66

def inner(el, indent)
  result = +''
  indent += @indent
  @stack.push(el)
  el.children.each do |inner_el|
    result << send(@dispatcher[inner_el.type], inner_el, indent)
  end
  @stack.pop
  result
end

```

    
  

    
      
  
### 
  
    #**obfuscate**(text)  ⇒ Object 
  

  

  

  
    

Obfuscate the `text` by using HTML entities.

  

  

  
    
      

```

484
485
486
487
488
489
490
491
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 484

def obfuscate(text)
  result = +''
  text.each_byte do |b|
    result << (b > 128 ? b.chr : sprintf("&#%03d;", b))
  end
  result.force_encoding(text.encoding)
  result
end

```

    
  

    
      
  
### 
  
    #**remove_footnotes**(elements)  ⇒ Object 
  

  

  

  
    

Remove all footnotes from the given elements.

  

  

  
    
      

```

476
477
478
479
480
481
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 476

def remove_footnotes(elements)
  elements.delete_if do |c|
    remove_footnotes(c.children)
    c.type == :footnote
  end
end

```

    
  

    
      
  
### 
  
    #**unwrap_links**(elements)  ⇒ Object 
  

  

  

  
    

Remove all link elements by unwrapping them.

  

  

  
    
      

```

468
469
470
471
472
473
```

    
    
      

```
# File 'lib/kramdown/converter/html.rb', line 468

def unwrap_links(elements)
  elements.map! do |c|
    unwrap_links(c.children)
    c.type == :a ? c.children : c
  end.flatten!
end

```