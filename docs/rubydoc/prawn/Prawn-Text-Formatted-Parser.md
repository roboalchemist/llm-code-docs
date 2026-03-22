# Class: Prawn::Text::Formatted::Parser
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Prawn::Text::Formatted::Parser
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/text/formatted/parser.rb
  
  

## Overview

  
    

Implements a bi-directional parser between a subset of html and formatted text arrays.

  

  

  
    
## 
      Extension API
      collapse
    

    
      
        PARSER_REGEX =
          
  
    

Parser regular expression.

  

  

        
        

```
begin
  regex_string =
    "\n|" \
      '<b>|</b>|' \
      '<i>|</i>|' \
      '<u>|</u>|' \
      '<strikethrough>|</strikethrough>|' \
      '<sub>|</sub>|' \
      '<sup>|</sup>|' \
      '<link[^>]*>|</link>|' \
      '<color[^>]*>|</color>|' \
      '<font[^>]*>|</font>|' \
      '<strong>|</strong>|' \
      '<em>|</em>|' \
      '<a[^>]*>|</a>|' \
      "[^<\n]+"
  Regexp.new(regex_string, Regexp::MULTILINE)
end

```

      
        ESCAPE_CHARS =
          
  
    

Escaped characters.

  

  

        
        

```
{
  '&' => '&',
  '>' => '>',
  '<' => '<',
}.freeze

```

      
        UNESCAPE_CHARS =
          
        
        

```
ESCAPE_CHARS.invert.freeze

```

      
    
  

  
    
## 
      Extension API
      collapse
    

    

      
        
- 
  
    
      .**array_from_tokens**(tokens)  ⇒ Array<Hash> 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**array_paragraphs**(array)  ⇒ Array<Array<Hash>> 
    

    
  
  
  
  
  
  
  
  

  
    

Break text into paragraphs.

  

      
        
- 
  
    
      .**escape**(text)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Escape characters that can interfere with inline format parsing.

  

      
        
- 
  
    
      .**format**(string, *_args)  ⇒ Array<Hash> 
    

    
  
  
  
  
  
  
  
  

  
    

Parse formatted string.

  

      
        
- 
  
    
      .**to_string**(array)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Serialize text fragments to an inline format string.

  

      
        
- 
  
    
      .**unescape**(text)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Unescape characters that can interfere with inline format parsing.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**array_from_tokens**(tokens)  ⇒ Array<Hash> 
  

  

  

  
    

  

  

Parameters:

  
    
- 
      
        tokens
      
      
        (Array<String>)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Array<Hash>)
      
      
      
    
  

  
    
      

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
259
260
261
262
263
264
```

    
    
      

```
# File 'lib/prawn/text/formatted/parser.rb', line 151

def self.array_from_tokens(tokens)
  array = []
  styles = []
  colors = []
  link = nil
  anchor = nil
  local = nil
  fonts = []
  sizes = []
  character_spacings = []

  tokens.each do |token|
    case token
    when '<b>', '<strong>'
      styles << :bold
    when '<i>', '<em>'
      styles << :italic
    when '<u>'
      styles << :underline
    when '<strikethrough>'
      styles << :strikethrough
    when '<sub>'
      styles << :subscript
    when '<sup>'
      styles << :superscript
    when '</b>', '</strong>'
      styles.delete(:bold)
    when '</i>', '</em>'
      styles.delete(:italic)
    when '</u>'
      styles.delete(:underline)
    when '</strikethrough>'
      styles.delete(:strikethrough)
    when '</sub>'
      styles.delete(:subscript)
    when '</sup>'
      styles.delete(:superscript)
    when '</link>', '</a>'
      link = nil
      anchor = nil
      local = nil
    when '</color>'
      colors.pop
    when '</font>'
      fonts.pop
      sizes.pop
      character_spacings.pop
    when /^<link[^>]*>$/, /^<a[^>]*>$/
      matches = /href="([^"]*)"/.match(token) ||
        /href='([^']*)'/.match(token)
      link = matches[1] unless matches.nil?

      matches = /anchor="([^"]*)"/.match(token) ||
        /anchor='([^']*)'/.match(token)
      anchor = matches[1] unless matches.nil?

      matches = /local="([^"]*)"/.match(token) ||
        /local='([^']*)'/.match(token)
      local = matches[1] unless matches.nil?
    when /^<color[^>]*>$/
      matches = /rgb="#?([^"]*)"/.match(token) ||
        /rgb='#?([^']*)'/.match(token)
      colors << matches[1] if matches

      match = /c="#?([^"]*)"/.match(token) ||
        /c='#?([^']*)'/.match(token)
      c = Integer(match[1], 10) unless match.nil?
      match = /m="#?([^"]*)"/.match(token) ||
        /m='#?([^']*)'/.match(token)
      m = Integer(match[1], 10) unless match.nil?
      match = /y="#?([^"]*)"/.match(token) ||
        /y='#?([^']*)'/.match(token)
      y = Integer(match[1], 10) unless match.nil?
      match = /k="#?([^"]*)"/.match(token) ||
        /k='#?([^']*)'/.match(token)
      k = Integer(match[1], 10) unless match.nil?
      colors << [c, m, y, k] if [c, m, y, k].all?

      # intend to support rgb="#ffffff" or rgb='#ffffff',
      # r="255" g="255" b="255" or r='255' g='255' b='255',
      # and c="100" m="100" y="100" k="100" or
      # c='100' m='100' y='100' k='100'
      # color = { :rgb => "#ffffff" }
      # color = { :r => 255, :g => 255, :b => 255 }
      # color = { :c => 100, :m => 100, :y => 100, :k => 100 }
    when /^<font[^>]*>$/
      matches = /name="([^"]*)"/.match(token) ||
        /name='([^']*)'/.match(token)
      fonts << matches[1] unless matches.nil?

      matches = /size="([^"]*)"/.match(token) ||
        /size='([^']*)'/.match(token)
      sizes << Float(matches[1]) unless matches.nil?

      matches = /character_spacing="([^"]*)"/.match(token) ||
        /character_spacing='([^']*)'/.match(token)
      character_spacings << Float(matches[1]) unless matches.nil?
    else
      string = unescape(token)
      array << {
        text: string,
        styles: styles.dup,
        color: colors.last,
        local: local,
        link: link,
        anchor: anchor,
        font: fonts.last,
        size: sizes.last,
        character_spacing: character_spacings.last,
      }
    end
  end
  array
end

```

    
  

    
      
  
### 
  
    .**array_paragraphs**(array)  ⇒ Array<Array<Hash>> 
  

  

  

  
    

Break text into paragraphs.

  

  

Parameters:

  
    
- 
      
        array
      
      
        (Array<Hash>)
      
      
      
        —
        

Text fragments.

      
    
  

Returns:

  
    
- 
      
      
        (Array<Array<Hash>>)
      
      
      
        —
        

Pragraphs of text fragments.

      
    
  

  
    
      

```

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
144
145
146
```

    
    
      

```
# File 'lib/prawn/text/formatted/parser.rb', line 125

def self.array_paragraphs(array)
  paragraphs = []
  paragraph = []
  previous_string = "\n"
  scan_pattern = /[^\n]+|\n/
  array.each do |hash|
    hash[:text].scan(scan_pattern).each do |string|
      if string == "\n"
        if previous_string == "\n"
          paragraph << hash.dup.merge(text: "\n")
        end
        paragraphs << paragraph unless paragraph.empty?
        paragraph = []
      else
        paragraph << hash.dup.merge(text: string)
      end
      previous_string = string
    end
  end
  paragraphs << paragraph unless paragraph.empty?
  paragraphs
end

```

    
  

    
      
  
### 
  
    .**escape**(text)  ⇒ String 
  

  

  

  
    

Escape characters that can interfere with inline format parsing.

  

  

Parameters:

  
    
- 
      
        text
      
      
        (String)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

270
271
272
```

    
    
      

```
# File 'lib/prawn/text/formatted/parser.rb', line 270

def self.escape(text)
  text.gsub(Regexp.union(ESCAPE_CHARS.keys), ESCAPE_CHARS)
end

```

    
  

    
      
  
### 
  
    .**format**(string, *_args)  ⇒ Array<Hash> 
  

  

  

  
    

Parse formatted string.

  

  

Parameters:

  
    
- 
      
        string
      
      
        (String)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Array<Hash>)
      
      
      
        —
        

Text fragments.

      
    
  

  
    
      

```

48
49
50
51
```

    
    
      

```
# File 'lib/prawn/text/formatted/parser.rb', line 48

def self.format(string, *_args)
  tokens = string.gsub(%r{<br\s*/?>}, "\n").scan(PARSER_REGEX)
  array_from_tokens(tokens)
end

```

    
  

    
      
  
### 
  
    .**to_string**(array)  ⇒ String 
  

  

  

  
    

Serialize text fragments to an inline format string.

  

  

Parameters:

  
    
- 
      
        array
      
      
        (Array<Hash>)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

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
110
111
112
113
114
115
116
117
118
```

    
    
      

```
# File 'lib/prawn/text/formatted/parser.rb', line 57

def self.to_string(array)
  prefixes = {
    bold: '<b>',
    italic: '<i>',
    underline: '<u>',
    strikethrough: '<strikethrough>',
    subscript: '<sub>',
    superscript: '<sup>',
  }
  suffixes = {
    bold: '</b>',
    italic: '</i>',
    underline: '</u>',
    strikethrough: '</strikethrough>',
    subscript: '</sub>',
    superscript: '</sup>',
  }
  array
    .map { |hash|
      prefix = ''
      suffix = ''
      hash[:styles]&.each do |style|
        prefix += prefixes[style]
        suffix = suffixes[style] + suffix
      end

      font = hash[:font] ? " name='#{hash[:font]}'" : nil
      size = hash[:size] ? " size='#{hash[:size]}'" : nil
      character_spacing =
        if hash[:character_spacing]
          " character_spacing='#{hash[:character_spacing]}'"
        end
      if font || size || character_spacing
        prefix += "<font#{font}#{size}#{character_spacing}>"
        suffix = '</font>'
      end

      link = hash[:link] ? " href='#{hash[:link]}'" : nil
      anchor = hash[:anchor] ? " anchor='#{hash[:anchor]}'" : nil
      if link || anchor
        prefix += "<link#{link}#{anchor}>"
        suffix = '</link>'
      end

      if hash[:color]
        prefix +=
          if hash[:color].is_a?(Array)
            "<color c='#{hash[:color][0]}' " \
              "m='#{hash[:color][1]}' " \
              "y='#{hash[:color][2]}' " \
              "k='#{hash[:color][3]}'>"
          else
            "<color rgb='#{hash[:color]}'>"
          end
        suffix = '</color>'
      end

      string = escape(hash[:text])
      prefix + string + suffix
    }
    .join
end

```

    
  

    
      
  
### 
  
    .**unescape**(text)  ⇒ String 
  

  

  

  
    

Unescape characters that can interfere with inline format parsing.

  

  

Parameters:

  
    
- 
      
        text
      
      
        (String)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
    
  

  
    
      

```

278
279
280
```

    
    
      

```
# File 'lib/prawn/text/formatted/parser.rb', line 278

def self.unescape(text)
  text.gsub(Regexp.union(UNESCAPE_CHARS.keys), UNESCAPE_CHARS)
end

```