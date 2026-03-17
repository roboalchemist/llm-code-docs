# Class: Kramdown::Converter::Kramdown
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Kramdown::Converter::Kramdown
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Utils::Html
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/kramdown.rb
  
  

## Overview

  
    

Converts an element tree to the kramdown format.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        ESCAPED_CHAR_RE =
          
        
        

```
/(\$\$|[\\*_`\[\]{"'|])|^ {0,3}(:)/

```

      
        HTML_TAGS_WITH_BODY =
          
        
        

```
%w[div script iframe textarea th td]

```

      
        TYPOGRAPHIC_SYMS =
          
        
        

```
{
  mdash: '---', ndash: '--', hellip: '...',
  laquo_space: '<< ', raquo_space: ' >>',
  laquo: '<<', raquo: '>>'
}

```

      
    
  

  
  
  
### Constants included
     from Utils::Html

  

Utils::Html::ESCAPE_ALL_RE, Utils::Html::ESCAPE_ATTRIBUTE_RE, Utils::Html::ESCAPE_MAP, Utils::Html::ESCAPE_RE_FROM_TYPE, Utils::Html::ESCAPE_TEXT_RE, Utils::Html::REDUNDANT_LINE_BREAK_REGEX

  
  
  
### Constants inherited
     from Base

  

Base::SMART_QUOTE_INDICES

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#data, #options, #root, #warnings

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**convert**(el, opts = {indent: 0})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_a**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_abbreviation**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_blank**(_el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_blockquote**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_br**(_el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_codeblock**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_codespan**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_comment**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_dd**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_dt**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_em**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_entity**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_footnote**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_header**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_hr**(_el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_html_element**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_img**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_li**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_math**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_p**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_raw**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_root**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_smart_quote**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_strong**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_table**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_tbody**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_td**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_text**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_tfoot**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_thead**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_tr**(el, opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_typographic_sym**(el, _opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_ul**(el, opts)  ⇒ Object 
    

    
      (also: #convert_ol, #convert_dl)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**convert_xml_comment**(el, _opts)  ⇒ Object 
    

    
      (also: #convert_xml_pi)
    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**create_abbrev_defs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**create_footnote_defs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**create_link_defs**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**ial_for_element**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the IAL containing the attributes of the element `el`.

  

      
        
- 
  
    
      #**initialize**(root, options)  ⇒ Kramdown 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Kramdown.

  

      
        
- 
  
    
      #**inner**(el, opts = {indent: 0})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**parse_title**(attr)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods included from Utils::Html

  

#entity_to_str, #escape_html, #fix_cjk_line_break, #html_attributes

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

apply_template, #apply_template_after?, #apply_template_before?, #basic_generate_id, convert, #extract_code_language, #extract_code_language!, #format_math, #generate_id, get_template, #highlight_code, #in_toc?, #output_header_level, #smart_quote_entity, #warning

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root, options)  ⇒ Kramdown 
  

  

  

  
    

Returns a new instance of Kramdown.

  

  

  
    
      

```

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
# File 'lib/kramdown/converter/kramdown.rb', line 24

def initialize(root, options)
  super
  @linkrefs = []
  @footnotes = []
  @abbrevs = []
  @stack = []
  @list_indent = @options[:list_indent]
  @list_spacing = ' ' * (@list_indent - 2)
end

```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**convert**(el, opts = {indent: 0})  ⇒ Object 
  

  

  

  
    
      

```

34
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
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 34

def convert(el, opts = {indent: 0})
  res = send("convert_#{el.type}", el, opts)
  res = res.dup if res.frozen?
  if ![:html_element, :li, :dt, :dd, :td].include?(el.type) && (ial = ial_for_element(el))
    res << ial
    res << "\n\n" if el.block?
  elsif [:ul, :dl, :ol, :codeblock].include?(el.type) && opts[:next] &&
      ([el.type, :codeblock].include?(opts[:next].type) ||
       (opts[:next].type == :blank && opts[:nnext] &&
        [el.type, :codeblock].include?(opts[:nnext].type)))
    res << "^\n\n"
  elsif el.block? &&
      ![:li, :dd, :dt, :td, :th, :tr, :thead, :tbody, :tfoot, :blank].include?(el.type) &&
      (el.type != :html_element || @stack.last.type != :html_element) &&
      (el.type != :p || !el.options[:transparent]) &&
      !([:ul, :dl, :ol].include?(el.type) && @stack.last.type == :li)
    res << "\n"
  end
  res
end

```

    
  

    
      
  
### 
  
    #**convert_a**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 296

def convert_a(el, opts)
  if el.attr['href'].empty?
    "[#{inner(el, opts)}]()"
  elsif el.attr['href'] =~ /^(?:http|ftp)/ || el.attr['href'].count("()") > 0
    index = if (link_el = @linkrefs.find {|c| c.attr['href'] == el.attr['href'] })
              @linkrefs.index(link_el) + 1
            else
              @linkrefs << el
              @linkrefs.size
            end
    "[#{inner(el, opts)}][#{index}]"
  else
    title = parse_title(el.attr['title'])
    "[#{inner(el, opts)}](#{el.attr['href']}#{title})"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_abbreviation**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

382
383
384
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 382

def convert_abbreviation(el, _opts)
  el.value
end

```

    
  

    
      
  
### 
  
    #**convert_blank**(_el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 71

def convert_blank(_el, _opts)
  ""
end

```

    
  

    
      
  
### 
  
    #**convert_blockquote**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

111
112
113
114
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 111

def convert_blockquote(el, opts)
  opts[:indent] += 2
  inner(el, opts).chomp.split("\n").map {|l| "> #{l}" }.join("\n") << "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_br**(_el, opts)  ⇒ Object 
  

  

  

  
    
      

```

292
293
294
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 292

def convert_br(_el, opts)
  opts[:in_header] ? "<br />" : "  \n"
end

```

    
  

    
      
  
### 
  
    #**convert_codeblock**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

107
108
109
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 107

def convert_codeblock(el, _opts)
  el.value.split("\n").map {|l| l.empty? ? "    " : "    #{l}" }.join("\n") + "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_codespan**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

329
330
331
332
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 329

def convert_codespan(el, _opts)
  delim = (el.value.scan(/`+/).max || '') + '`'
  "#{delim}#{' ' if delim.size > 1}#{el.value}#{' ' if delim.size > 1}#{delim}"
end

```

    
  

    
      
  
### 
  
    #**convert_comment**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

284
285
286
287
288
289
290
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 284

def convert_comment(el, _opts)
  if el.options[:category] == :block
    "{::comment}\n#{el.value}\n{:/}\n"
  else
    "{::comment}#{el.value}{:/}"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_dd**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 163

def convert_dd(el, opts)
  sym, width = ": " + @list_spacing, (el.children.first && el.children.first.type == :codeblock ? 4 : @list_indent)
  if (ial = ial_for_element(el))
    sym << ial << " "
  end

  opts[:indent] += width
  text = inner(el, opts)
  newlines = text.scan(/\n*\Z/).first
  first, *last = text.split("\n")
  last = last.map {|l| " " * width + l }.join("\n")
  text = first.to_s + (last.empty? ? "" : "\n") + last + newlines
  text.chomp! if text =~ /\n\n\Z/ && opts[:next] && opts[:next].type == :dd
  text << "\n" if text !~ /\n\n\Z/ && opts[:next] && opts[:next].type == :dt
  text << "\n" if el.children.empty?
  if el.children.first && el.children.first.type == :p && !el.children.first.options[:transparent]
    "\n#{sym}#{text}"
  elsif el.children.first && el.children.first.type == :codeblock
    "#{sym}\n    #{text}"
  else
    "#{sym}#{text}"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_dt**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

187
188
189
190
191
192
193
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 187

def convert_dt(el, opts)
  result = +''
  if (ial = ial_for_element(el))
    result << ial << " "
  end
  result << inner(el, opts) << "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_em**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

351
352
353
354
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 351

def convert_em(el, opts)
  "*#{inner(el, opts)}*" +
    (opts[:next] && [:em, :strong].include?(opts[:next].type) && !ial_for_element(el) ? '{::}' : '')
end

```

    
  

    
      
  
### 
  
    #**convert_entity**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

361
362
363
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 361

def convert_entity(el, _opts)
  entity_to_str(el.value, el.options[:original])
end

```

    
  

    
      
  
### 
  
    #**convert_footnote**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

334
335
336
337
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 334

def convert_footnote(el, _opts)
  @footnotes << [el.options[:name], el.value]
  "[^#{el.options[:name]}]"
end

```

    
  

    
      
  
### 
  
    #**convert_header**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

116
117
118
119
120
121
122
123
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 116

def convert_header(el, opts)
  opts[:in_header] = true
  res = +''
  res << "#{'#' * output_header_level(el.options[:level])} #{inner(el, opts)}"
  res[-1, 1] = "\\#" if res[-1] == '#'
  res << "   {##{el.attr['id']}}" if el.attr['id'] && !el.attr['id'].strip.empty?
  res << "\n"
end

```

    
  

    
      
  
### 
  
    #**convert_hr**(_el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

125
126
127
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 125

def convert_hr(_el, _opts)
  "* * *\n"
end

```

    
  

    
      
  
### 
  
    #**convert_html_element**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

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
230
231
232
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 200

def convert_html_element(el, opts)
  markdown_attr = el.options[:category] == :block && el.children.any? do |c|
    c.type != :html_element &&
      (c.type != :p || !c.options[:transparent] ||
       c.children.any? {|t| !HTML_ELEMENT_TYPES.member?(t.type) }) &&
      c.block?
  end
  opts[:force_raw_text] = true if %w[script pre code].include?(el.value)
  opts[:raw_text] = opts[:force_raw_text] || opts[:block_raw_text] || \
    (el.options[:category] != :span && !markdown_attr)
  opts[:block_raw_text] = true if el.options[:category] == :block && opts[:raw_text]
  res = inner(el, opts)
  if el.options[:category] == :span
    "<#{el.value}#{html_attributes(el.attr)}" + \
      (!res.empty? || HTML_TAGS_WITH_BODY.include?(el.value) ? ">#{res}</#{el.value}>" : " />")
  else
    output = +''
    attr = el.attr.dup
    attr['markdown'] = '1' if markdown_attr
    output << "<#{el.value}#{html_attributes(attr)}"
    if !res.empty? && el.options[:content_model] != :block
      output << ">#{res}</#{el.value}>"
    elsif !res.empty?
      output << ">\n#{res}" << "</#{el.value}>"
    elsif HTML_TAGS_WITH_BODY.include?(el.value)
      output << "></#{el.value}>"
    else
      output << " />"
    end
    output << "\n" if @stack.last.type != :html_element || @stack.last.options[:content_model] != :raw
    output
  end
end

```

    
  

    
      
  
### 
  
    #**convert_img**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

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
323
324
325
326
327
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 313

def convert_img(el, _opts)
  alt_text = el.attr['alt'].to_s.gsub(ESCAPED_CHAR_RE) { $1 ? "\\#{$1}" : $2 }
  src = el.attr['src'].to_s
  if src.empty?
    "![#{alt_text}]()"
  else
    title = parse_title(el.attr['title'])
    link = if src.count("()") > 0
             "<#{src}>"
           else
             src
           end
    "![#{alt_text}](#{link}#{title})"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_li**(el, opts)  ⇒ Object 
  

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 135

def convert_li(el, opts)
  sym, width = if @stack.last.type == :ul
                 ['* ' + @list_spacing, el.children.first && el.children.first.type == :codeblock ? 4 : @list_indent]
               else
                 ["#{opts[:index] + 1}.".ljust(4), 4]
               end
  if (ial = ial_for_element(el))
    sym << ial << " "
  end

  opts[:indent] += width
  text = inner(el, opts)
  newlines = text.scan(/\n*\Z/).first
  first, *last = text.split("\n")
  last = last.map {|l| " " * width + l }.join("\n")
  text = (first.nil? ? "\n" : first + (last.empty? ? "" : "\n") + last + newlines)
  if el.children.first && el.children.first.type == :p && !el.children.first.options[:transparent]
    res = +"#{sym}#{text}"
    res << "^\n" if el.children.size == 1 && @stack.last.children.last == el &&
      (@stack.last.children.any? {|c| !c.children.first || c.children.first.type != :p } || @stack.last.children.size == 1)
    res
  elsif el.children.first && el.children.first.type == :codeblock
    "#{sym}\n    #{text}"
  else
    "#{sym}#{text}"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_math**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

378
379
380
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 378

def convert_math(el, _opts)
  "$$#{el.value}$$" + (el.options[:category] == :block ? "\n" : '')
end

```

    
  

    
      
  
### 
  
    #**convert_p**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 92

def convert_p(el, opts)
  w = @options[:line_width] - opts[:indent].to_s.to_i
  first, second, *rest = inner(el, opts).strip.gsub(/(.{1,#{w}})( +|$\n?)/, "\\1\n").split(/\n/)
  first&.gsub!(/^(?:(#|>)|(\d+)\.(\s)|([+-]\s))/) { $1 || $4 ? "\\#{$1 || $4}" : "#{$2}\\.#{$3}" }
  second&.gsub!(/^([=-]+\s*?)$/, "\\\1")
  res = [first, second, *rest].compact.join("\n") + "\n"
  res.gsub!(/^ {0,3}:/, "\\:")
  if el.children.length == 1 && el.children.first.type == :math
    res = "\\#{res}"
  elsif res.start_with?('\$$') && res.end_with?("\\$$\n")
    res.sub!(/^\\\$\$/, '\$\$')
  end
  res
end

```

    
  

    
      
  
### 
  
    #**convert_raw**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

339
340
341
342
343
344
345
346
347
348
349
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 339

def convert_raw(el, _opts)
  attr = (el.options[:type] || []).join(' ')
  attr = " type=\"#{attr}\"" unless attr.empty?
  if @stack.last.type == :html_element
    el.value
  elsif el.options[:category] == :block
    "{::nomarkdown#{attr}}\n#{el.value}\n{:/}\n"
  else
    "{::nomarkdown#{attr}}#{el.value}{:/}"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_root**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

386
387
388
389
390
391
392
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 386

def convert_root(el, opts)
  res = inner(el, opts)
  res << create_link_defs
  res << create_footnote_defs
  res << create_abbrev_defs
  res
end

```

    
  

    
      
  
### 
  
    #**convert_smart_quote**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

374
375
376
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 374

def convert_smart_quote(el, _opts)
  el.value.to_s.match?(/[rl]dquo/) ? "\"" : "'"
end

```

    
  

    
      
  
### 
  
    #**convert_strong**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

356
357
358
359
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 356

def convert_strong(el, opts)
  "**#{inner(el, opts)}**" +
    (opts[:next] && [:em, :strong].include?(opts[:next].type) && !ial_for_element(el) ? '{::}' : '')
end

```

    
  

    
      
  
### 
  
    #**convert_table**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

244
245
246
247
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 244

def convert_table(el, opts)
  opts[:alignment] = el.options[:alignment]
  inner(el, opts)
end

```

    
  

    
      
  
### 
  
    #**convert_tbody**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

265
266
267
268
269
270
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 265

def convert_tbody(el, opts)
  res = +''
  res << inner(el, opts)
  res << '|' << '-' * 10 << "\n" if opts[:next] && opts[:next].type == :tbody
  res
end

```

    
  

    
      
  
### 
  
    #**convert_td**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

280
281
282
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 280

def convert_td(el, opts)
  inner(el, opts)
end

```

    
  

    
      
  
### 
  
    #**convert_text**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

77
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
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 77

def convert_text(el, opts)
  if opts[:raw_text] || (@stack.last.type == :html_element && @stack.last.options[:content_model] == :raw)
    el.value
  else
    result = el.value.gsub(/\A\n/) do
      opts[:prev] && opts[:prev].type == :br ? '' : "\n"
    end
    result.gsub!(/\s+/, ' ') unless el.options[:cdata]
    result.gsub!(ESCAPED_CHAR_RE) do
      $1 || !opts[:prev] || opts[:prev].type == :br ? "\\#{$1 || $2}" : $&
    end
    result
  end
end

```

    
  

    
      
  
### 
  
    #**convert_tfoot**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

272
273
274
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 272

def convert_tfoot(el, opts)
  "|#{'=' * 10}\n#{inner(el, opts)}"
end

```

    
  

    
      
  
### 
  
    #**convert_thead**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

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
259
260
261
262
263
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 249

def convert_thead(el, opts)
  rows = inner(el, opts)
  if opts[:alignment].all?(:default)
    "#{rows}|#{'-' * 10}\n"
  else
    "#{rows}| " + opts[:alignment].map do |a|
      case a
      when :left then ":-"
      when :right then "-:"
      when :center then ":-:"
      when :default then "-"
      end
    end.join(' ') << "\n"
  end
end

```

    
  

    
      
  
### 
  
    #**convert_tr**(el, opts)  ⇒ Object 
  

  

  

  
    
      

```

276
277
278
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 276

def convert_tr(el, opts)
  "| #{el.children.map {|c| convert(c, opts) }.join(' | ')} |\n"
end

```

    
  

    
      
  
### 
  
    #**convert_typographic_sym**(el, _opts)  ⇒ Object 
  

  

  

  
    
      

```

370
371
372
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 370

def convert_typographic_sym(el, _opts)
  TYPOGRAPHIC_SYMS[el.value]
end

```

    
  

    
      
  
### 
  
    #**convert_ul**(el, opts)  ⇒ Object 
  

  
    Also known as:
    convert_ol, convert_dl
    
  

  

  
    
      

```

129
130
131
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 129

def convert_ul(el, opts)
  inner(el, opts).sub(/\n+\Z/, "\n")
end

```

    
  

    
      
  
### 
  
    #**convert_xml_comment**(el, _opts)  ⇒ Object 
  

  
    Also known as:
    convert_xml_pi
    
  

  

  
    
      

```

234
235
236
237
238
239
240
241
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 234

def convert_xml_comment(el, _opts)
  if el.options[:category] == :block &&
      (@stack.last.type != :html_element || @stack.last.options[:content_model] != :raw)
    el.value + "\n"
  else
    el.value.dup
  end
end

```

    
  

    
      
  
### 
  
    #**create_abbrev_defs**  ⇒ Object 
  

  

  

  
    
      

```

413
414
415
416
417
418
419
420
421
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 413

def create_abbrev_defs
  return '' unless @root.options[:abbrev_defs]
  res = +''
  @root.options[:abbrev_defs].each do |name, text|
    res << "*[#{name}]: #{text}\n"
    res << ial_for_element(Element.new(:unused, nil, @root.options[:abbrev_attr][name])).to_s << "\n\n"
  end
  res
end

```

    
  

    
      
  
### 
  
    #**create_footnote_defs**  ⇒ Object 
  

  

  

  
    
      

```

404
405
406
407
408
409
410
411
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 404

def create_footnote_defs
  res = +''
  @footnotes.each do |name, data|
    res << "[^#{name}]:\n"
    res << inner(data).chomp.split("\n").map {|l| "    #{l}" }.join("\n") + "\n\n"
  end
  res
end

```

    
  

    
      
  
### 
  
    #**create_link_defs**  ⇒ Object 
  

  

  

  
    
      

```

394
395
396
397
398
399
400
401
402
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 394

def create_link_defs
  res = +''
  res << "\n\n" unless @linkrefs.empty?
  @linkrefs.each_with_index do |el, i|
    title = parse_title(el.attr['title'])
    res << "[#{i + 1}]: #{el.attr['href']}#{title}\n"
  end
  res
end

```

    
  

    
      
  
### 
  
    #**ial_for_element**(el)  ⇒ Object 
  

  

  

  
    

Return the IAL containing the attributes of the element `el`.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 424

def ial_for_element(el)
  res = el.attr.map do |k, v|
    next if [:img, :a].include?(el.type) && ['href', 'src', 'alt', 'title'].include?(k)
    next if el.type == :header && k == 'id' && !v.strip.empty?
    if v.nil?
      ''
    elsif k == 'class' && !v.empty? && !v.index(/[.#]/)
      " " + v.split(/\s+/).map {|w| ".#{w}" }.join(" ")
    elsif k == 'id' && !v.strip.empty?
      " ##{v}"
    else
      " #{k}=\"#{v}\""
    end
  end.compact.join
  res = "toc" + (res.strip.empty? ? '' : " #{res}") if (el.type == :ul || el.type == :ol) &&
    el.options.dig(:ial, :refs)&.include?('toc')
  res = "footnotes" + (res.strip.empty? ? '' : " #{res}") if (el.type == :ul || el.type == :ol) &&
    el.options.dig(:ial, :refs)&.include?('footnotes')
  if el.type == :dl && el.options[:ial] && el.options[:ial][:refs]
    auto_ids = el.options[:ial][:refs].select {|ref| ref.start_with?('auto_ids') }.join(" ")
    res = auto_ids << (res.strip.empty? ? '' : " #{res}") unless auto_ids.empty?
  end
  res.strip.empty? ? nil : "{:#{res}}"
end

```

    
  

    
      
  
### 
  
    #**inner**(el, opts = {indent: 0})  ⇒ Object 
  

  

  

  
    
      

```

55
56
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
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 55

def inner(el, opts = {indent: 0})
  @stack.push(el)
  result = +''
  el.children.each_with_index do |inner_el, index|
    options = opts.dup
    options[:index] = index
    options[:prev] = (index == 0 ? nil : el.children[index - 1])
    options[:pprev] = (index <= 1 ? nil : el.children[index - 2])
    options[:next] = (index == el.children.length - 1 ? nil : el.children[index + 1])
    options[:nnext] = (index >= el.children.length - 2 ? nil : el.children[index + 2])
    result << convert(inner_el, options)
  end
  @stack.pop
  result
end

```

    
  

    
      
  
### 
  
    #**parse_title**(attr)  ⇒ Object 
  

  

  

  
    
      

```

449
450
451
```

    
    
      

```
# File 'lib/kramdown/converter/kramdown.rb', line 449

def parse_title(attr)
  attr.to_s.empty? ? '' : ' "' + attr.gsub(/"/, '"') + '"'
end

```