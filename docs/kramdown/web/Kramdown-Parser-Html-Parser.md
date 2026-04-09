# Module: Kramdown::Parser::Html::Parser
  
  
  

  

  
  
  
  
  
      Includes:
      Constants
  
  
  

  
  
    Included in:
    Kramdown::Parser::Html, Kramdown
  
  

  
  
    Defined in:
    lib/kramdown/parser/html.rb
  
  

## Overview

  
    

Contains the parsing methods. This module can be mixed into any parser to get HTML parsing functionality. The only thing that must be provided by the class are instance variable parsing.

  

  

  
    
## 
      Constant Summary
      collapse
    

    
      
        HTML_RAW_START =
          
  
    

:nodoc:

  

  

        
        

```
/(?=<(#{REXML::Parsers::BaseParser::UNAME_STR}|\/|!--|\?|!\[CDATA\[))/

```

      
    
  

  
  
  
### Constants included
     from Constants

  

Constants::HTML_ATTRIBUTE_RE, Constants::HTML_BLOCK_ELEMENTS, Constants::HTML_CDATA_RE, Constants::HTML_COMMENT_RE, Constants::HTML_CONTENT_MODEL, Constants::HTML_CONTENT_MODEL_BLOCK, Constants::HTML_CONTENT_MODEL_RAW, Constants::HTML_CONTENT_MODEL_SPAN, Constants::HTML_DOCTYPE_RE, Constants::HTML_ELEMENT, Constants::HTML_ELEMENTS_WITHOUT_BODY, Constants::HTML_ENTITY_RE, Constants::HTML_INSTRUCTION_RE, Constants::HTML_SPAN_ELEMENTS, Constants::HTML_TAG_CLOSE_RE, Constants::HTML_TAG_RE

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**handle_html_start_tag**(line = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Process the HTML start tag that has already be scanned/checked via @src.

  

      
        
- 
  
    
      #**handle_raw_html_tag**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Handle the raw HTML tag at the current position.

  

      
        
- 
  
    
      #**parse_html_attributes**(str, line = nil, in_html_tag = true)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parses the given string for HTML attributes and returns the resulting hash.

  

      
        
- 
  
    
      #**parse_raw_html**(el, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Parse raw HTML from the current source position, storing the found elements in `el`.

  

      
    

  

  
  
  
  
  
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**handle_html_start_tag**(line = nil)  ⇒ Object 
  

  

  

  
    

Process the HTML start tag that has already be scanned/checked via @src.

Does the common processing steps and then yields to the caller for further processing (first parameter is the created element; the second parameter is `true` if the HTML element is already closed, ie. contains no body; the third parameter specifies whether the body - and the end tag - need to be handled in case closed=false).

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 88

def handle_html_start_tag(line = nil) # :yields: el, closed, handle_body
  name = @src[1]
  name.downcase! if HTML_ELEMENT[name.downcase]
  closed = !@src[4].nil?
  attrs = parse_html_attributes(@src[2], line, HTML_ELEMENT[name])

  el = Element.new(:html_element, name, attrs, category: :block)
  el.options[:location] = line if line
  @tree.children << el

  if !closed && HTML_ELEMENTS_WITHOUT_BODY.include?(el.value)
    closed = true
  end
  if name == 'script' || name == 'style'
    handle_raw_html_tag(name)
    yield(el, false, false)
  else
    yield(el, closed, true)
  end
end

```

    
  

    
      
  
### 
  
    #**handle_raw_html_tag**(name)  ⇒ Object 
  

  

  

  
    

Handle the raw HTML tag at the current position.

  

  

  
    
      

```

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
# File 'lib/kramdown/parser/html.rb', line 128

def handle_raw_html_tag(name)
  curpos = @src.pos
  if @src.scan_until(/(?=<\/#{name}\s*>)/mi)
    add_text(extract_string(curpos...@src.pos, @src), @tree.children.last, :raw)
    @src.scan(HTML_TAG_CLOSE_RE)
  else
    add_text(@src.rest, @tree.children.last, :raw)
    @src.terminate
    warning("Found no end tag for '#{name}' - auto-closing it")
  end
end

```

    
  

    
      
  
### 
  
    #**parse_html_attributes**(str, line = nil, in_html_tag = true)  ⇒ Object 
  

  

  

  
    

Parses the given string for HTML attributes and returns the resulting hash.

If the optional `line` parameter is supplied, it is used in warning messages.

If the optional `in_html_tag` parameter is set to `false`, attributes are not modified to contain only lowercase letters.

  

  

  
    
      

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
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 115

def parse_html_attributes(str, line = nil, in_html_tag = true)
  attrs = {}
  str.scan(HTML_ATTRIBUTE_RE).each do |attr, val, _sep, quoted_val|
    attr.downcase! if in_html_tag
    if attrs.key?(attr)
      warning("Duplicate HTML attribute '#{attr}' on line #{line || '?'} - overwriting previous one")
    end
    attrs[attr] = val || quoted_val || ""
  end
  attrs
end

```

    
  

    
      
  
### 
  
    #**parse_raw_html**(el, &block)  ⇒ Object 
  

  

  

  
    

Parse raw HTML from the current source position, storing the found elements in `el`. Parsing continues until one of the following criteria are fulfilled:

- 

The end of the document is reached.

- 

The matching end tag for the element `el` is found (only used if `el` is an HTML element).

When an HTML start tag is found, processing is deferred to #handle_html_start_tag, providing the block given to this method.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/parser/html.rb', line 151

def parse_raw_html(el, &block)
  @stack.push(@tree)
  @tree = el

  done = false
  while !@src.eos? && !done
    if (result = @src.scan_until(HTML_RAW_START))
      add_text(result, @tree, :text)
      line = @src.current_line_number
      if (result = @src.scan(HTML_COMMENT_RE))
        @tree.children << Element.new(:xml_comment, result, nil, category: :block, location: line)
      elsif (result = @src.scan(HTML_INSTRUCTION_RE))
        @tree.children << Element.new(:xml_pi, result, nil, category: :block, location: line)
      elsif @src.scan(HTML_CDATA_RE)
        @tree.children << Element.new(:text, @src[1], nil, cdata: true, location: line)
      elsif @src.scan(HTML_TAG_RE)
        if method(:handle_html_start_tag).arity.abs >= 1
          handle_html_start_tag(line, &block)
        else
          handle_html_start_tag(&block) # DEPRECATED: method needs to accept line number in 2.0
        end
      elsif @src.scan(HTML_TAG_CLOSE_RE)
        if @tree.value == (HTML_ELEMENT[@tree.value] ? @src[1].downcase : @src[1])
          done = true
        else
          add_text(@src.matched, @tree, :text)
          warning("Found invalidly used HTML closing tag for '#{@src[1]}' on " \
                  "line #{line} - ignoring it")
        end
      else
        add_text(@src.getch, @tree, :text)
      end
    else
      add_text(@src.rest, @tree, :text)
      @src.terminate
      if @tree.type == :html_element
        warning("Found no end tag for '#{@tree.value}' on line " \
                "#{@tree.options[:location]} - auto-closing it")
      end
      done = true
    end
  end

  @tree = @stack.pop
end

```