# Class: Kramdown::Converter::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Kramdown::Converter::Base
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/kramdown/converter/base.rb
  
  

## Overview

  
    

## Base class for converters

This class serves as base class for all converters. It provides methods that can/should be used by all converters (like #generate_id) as well as common functionality that is automatically applied to the result (for example, embedding the output into a template).

A converter object is used as a throw-away object, i.e. it is only used for storing the needed state information during conversion. Therefore one can’t instantiate a converter object directly but only use the Base::convert method.

## Implementing a converter

Implementing a new converter is rather easy: just derive a new class from this class and put it in the Kramdown::Converter module (the latter is only needed if auto-detection should work properly). Then you need to implement the #convert method which has to contain the conversion code for converting an element and has to return the conversion result.

The actual transformation of the document tree can be done in any way. However, writing one method per element type is a straight forward way to do it - this is how the Html and Latex converters do the transformation.

Have a look at the Base::convert method for additional information!

  

  

  
## Direct Known Subclasses

  

HashAST, Html, Kramdown, Latex, Man, RemoveHtmlTags, Toc

  
    
## 
      Constant Summary
      collapse
    

    
      
        SMART_QUOTE_INDICES =
          
  
    

:nodoc:

  

  

        
        

```
{lsquo: 0, rsquo: 1, ldquo: 2, rdquo: 3}

```

      
    
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**data**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Can be used by a converter for storing arbitrary information during the conversion process.

  

    
      
- 
  
    
      #**options**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The hash with the conversion options.

  

    
      
- 
  
    
      #**root**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The root element that is converted.

  

    
      
- 
  
    
      #**warnings**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

The warnings array.

  

    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**apply_template**(converter, body)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Apply the `template` using `body` as the body string.

  

      
        
- 
  
    
      .**convert**(tree, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert the element tree `tree` and return the resulting conversion object (normally a string) and an array with warning messages.

  

      
        
- 
  
    
      .**get_template**(template)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the template specified by `template`.

  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**apply_template_after?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns whether the template should be applied after the conversion of the tree.

  

      
        
- 
  
    
      #**apply_template_before?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Returns whether the template should be applied before the conversion of the tree.

  

      
        
- 
  
    
      #**basic_generate_id**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The basic version of the ID generator, without any special provisions for empty or unique IDs.

  

      
        
- 
  
    
      #**convert**(_el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Convert the element `el` and return the resulting object.

  

      
        
- 
  
    
      #**extract_code_language**(attr)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Extract the code block/span language from the attributes.

  

      
        
- 
  
    
      #**extract_code_language!**(attr)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See #extract_code_language.

  

      
        
- 
  
    
      #**format_math**(el, opts = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Format the given math element with the math engine configured through the option ‘math_engine’.

  

      
        
- 
  
    
      #**generate_id**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Generate an unique alpha-numeric ID from the the string `str` for use as a header ID.

  

      
        
- 
  
    
      #**highlight_code**(text, lang, type, opts = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Highlight the given `text` in the language `lang` with the syntax highlighter configured through the option ‘syntax_highlighter’.

  

      
        
- 
  
    
      #**in_toc?**(el)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Return `true` if the header element `el` should be used for the table of contents (as specified by the `toc_levels` option).

  

      
        
- 
  
    
      #**initialize**(root, options)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

Initialize the converter with the given `root` element and `options` hash.

  

      
        
- 
  
    
      #**output_header_level**(level)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the output header level given a level.

  

      
        
- 
  
    
      #**smart_quote_entity**(el)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Return the entity that represents the given smart_quote element.

  

      
        
- 
  
    
      #**warning**(text)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add the given warning `text` to the warning array.

  

      
    

  

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(root, options)  ⇒ Base 
  

  

  

  
    

Initialize the converter with the given `root` element and `options` hash.

  

  

  
    
      

```

55
56
57
58
59
60
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 55

def initialize(root, options)
  @options = options
  @root = root
  @data = {}
  @warnings = []
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**data**  ⇒ Object  (readonly)
  

  

  

  
    

Can be used by a converter for storing arbitrary information during the conversion process.

  

  

  
    
      

```

43
44
45
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 43

def data
  @data
end

```

    
  

    
      
      
      
  
### 
  
    #**options**  ⇒ Object  (readonly)
  

  

  

  
    

The hash with the conversion options.

  

  

  
    
      

```

46
47
48
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 46

def options
  @options
end

```

    
  

    
      
      
      
  
### 
  
    #**root**  ⇒ Object  (readonly)
  

  

  

  
    

The root element that is converted.

  

  

  
    
      

```

49
50
51
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 49

def root
  @root
end

```

    
  

    
      
      
      
  
### 
  
    #**warnings**  ⇒ Object  (readonly)
  

  

  

  
    

The warnings array.

  

  

  
    
      

```

52
53
54
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 52

def warnings
  @warnings
end

```

    
  

    
  

  
    
## Class Method Details

    
      
  
### 
  
    .**apply_template**(converter, body)  ⇒ Object 
  

  

  

  
    

Apply the `template` using `body` as the body string.

The template is evaluated using ERB and the body is available in the @body instance variable and the converter object in the @converter instance variable.

  

  

  
    
      

```

130
131
132
133
134
135
136
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 130

def self.apply_template(converter, body) # :nodoc:
  erb = ERB.new(get_template(converter.options[:template]))
  obj = Object.new
  obj.instance_variable_set(:@converter, converter)
  obj.instance_variable_set(:@body, body)
  erb.result(obj.instance_eval { binding })
end

```

    
  

    
      
  
### 
  
    .**convert**(tree, options = {})  ⇒ Object 
  

  

  

  
    

Convert the element tree `tree` and return the resulting conversion object (normally a string) and an array with warning messages. The parameter `options` specifies the conversion options that should be used.

Initializes a new instance of the calling class and then calls the #convert method with `tree` as parameter.

If the `template` option is specified and non-empty, the template is evaluate with ERB before and/or after the tree conversion depending on the result of #apply_template_before? and #apply_template_after?. If the template is evaluated before, an empty string is used for the body; if evaluated after, the result is used as body. See ::apply_template.

The template resolution is done in the following way (for the converter ConverterName):

- 

Look in the current working directory for the template.

- 

Append `.converter_name` (e.g. `.html`) to the template name and look for the resulting file in the current working directory (the form `.convertername` is deprecated).

- 

Append `.converter_name` to the template name and look for it in the kramdown data directory (the form `.convertername` is deprecated).

- 

Check if the template name starts with ‘string://’ and if so, strip this prefix away and use the rest as template.

  

  

  
    
      

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
114
115
116
117
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 101

def self.convert(tree, options = {})
  converter = new(tree, ::Kramdown::Options.merge(options.merge(tree.options[:options] || {})))

  if !converter.options[:template].empty? && converter.apply_template_before?
    apply_template(converter, '')
  end
  result = converter.convert(tree)
  if result.respond_to?(:encode!) && result.encoding != Encoding::BINARY
    result.encode!(tree.options[:encoding] ||
                   (raise ::Kramdown::Error, "Missing encoding option on root element"))
  end
  if !converter.options[:template].empty? && converter.apply_template_after?
    result = apply_template(converter, result)
  end

  [result, converter.warnings]
end

```

    
  

    
      
  
### 
  
    .**get_template**(template)  ⇒ Object 
  

  

  

  
    

Return the template specified by `template`.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 139

def self.get_template(template) # :nodoc:
  format_ext = '.' + ::Kramdown::Utils.snake_case(name.split("::").last)
  shipped = File.join(::Kramdown.data_dir, template + format_ext)
  if File.exist?(template)
    File.read(template)
  elsif File.exist?(template + format_ext)
    File.read(template + format_ext)
  elsif File.exist?(shipped)
    File.read(shipped)
  elsif template.start_with?('string://')
    template.delete_prefix("string://")
  else
    raise "The specified template file #{template} does not exist"
  end
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**apply_template_after?**  ⇒ Boolean 
  

  

  

  
    

Returns whether the template should be applied after the conversion of the tree.

Defaults to true.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

73
74
75
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 73

def apply_template_after?
  true
end

```

    
  

    
      
  
### 
  
    #**apply_template_before?**  ⇒ Boolean 
  

  

  

  
    

Returns whether the template should be applied before the conversion of the tree.

Defaults to false.

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

66
67
68
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 66

def apply_template_before?
  false
end

```

    
  

    
      
  
### 
  
    #**basic_generate_id**(str)  ⇒ Object 
  

  

  

  
    

The basic version of the ID generator, without any special provisions for empty or unique IDs.

  

  

  
    
      

```

237
238
239
240
241
242
243
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 237

def basic_generate_id(str)
  gen_id = str.gsub(/^[^a-zA-Z]+/, '')
  gen_id.tr!('^a-zA-Z0-9 -', '')
  gen_id.tr!(' ', '-')
  gen_id.downcase!
  gen_id
end

```

    
  

    
      
  
### 
  
    #**convert**(_el)  ⇒ Object 
  

  

  

  
    

Convert the element `el` and return the resulting object.

This is the only method that has to be implemented by sub-classes!

  

  

Raises:

  
    
- 
      
      
      
      
    
  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 122

def convert(_el)
  raise NotImplementedError
end

```

    
  

    
      
  
### 
  
    #**extract_code_language**(attr)  ⇒ Object 
  

  

  

  
    

Extract the code block/span language from the attributes.

  

  

  
    
      

```

174
175
176
177
178
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 174

def extract_code_language(attr)
  if attr['class'] && attr['class'] =~ /\blanguage-\S+/
    attr['class'].scan(/\blanguage-(\S+)/).first.first
  end
end

```

    
  

    
      
  
### 
  
    #**extract_code_language!**(attr)  ⇒ Object 
  

  

  

  
    

See #extract_code_language

**Warning**: This version will modify the given attributes if a language is present.

  

  

  
    
      

```

183
184
185
186
187
188
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 183

def extract_code_language!(attr)
  lang = extract_code_language(attr)
  attr['class'] = attr['class'].sub(/\blanguage-\S+/, '').strip if lang
  attr.delete('class') if lang && attr['class'].empty?
  lang
end

```

    
  

    
      
  
### 
  
    #**format_math**(el, opts = {})  ⇒ Object 
  

  

  

  
    

Format the given math element with the math engine configured through the option ‘math_engine’.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 206

def format_math(el, opts = {})
  return nil unless @options[:math_engine]

  engine = ::Kramdown::Converter.math_engine(@options[:math_engine])
  if engine
    engine.call(self, el, opts)
  else
    warning("The configured math engine #{@options[:math_engine]} is not available.")
    nil
  end
end

```

    
  

    
      
  
### 
  
    #**generate_id**(str)  ⇒ Object 
  

  

  

  
    

Generate an unique alpha-numeric ID from the the string `str` for use as a header ID.

Uses the option `auto_id_prefix`: the value of this option is prepended to every generated ID.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 222

def generate_id(str)
  str = ::Kramdown::Utils::Unidecoder.decode(str) if @options[:transliterated_header_ids]
  gen_id = basic_generate_id(str)
  gen_id = 'section' if gen_id.empty?
  @used_ids ||= {}
  if @used_ids.key?(gen_id)
    gen_id += "-#{@used_ids[gen_id] += 1}"
  else
    @used_ids[gen_id] = 0
  end
  @options[:auto_id_prefix] + gen_id
end

```

    
  

    
      
  
### 
  
    #**highlight_code**(text, lang, type, opts = {})  ⇒ Object 
  

  

  

  
    

Highlight the given `text` in the language `lang` with the syntax highlighter configured through the option ‘syntax_highlighter’.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 192

def highlight_code(text, lang, type, opts = {})
  return nil unless @options[:syntax_highlighter]

  highlighter = ::Kramdown::Converter.syntax_highlighter(@options[:syntax_highlighter])
  if highlighter
    highlighter.call(self, text, lang, type, opts)
  else
    warning("The configured syntax highlighter #{@options[:syntax_highlighter]} is not available.")
    nil
  end
end

```

    
  

    
      
  
### 
  
    #**in_toc?**(el)  ⇒ Boolean 
  

  

  

  
    

Return `true` if the header element `el` should be used for the table of contents (as specified by the `toc_levels` option).

  

  

Returns:

  
    
- 
      
      
      
      
    
  

  
    
      

```

162
163
164
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 162

def in_toc?(el)
  @options[:toc_levels].include?(el.options[:level]) && (el.attr['class'] || '') !~ /\bno_toc\b/
end

```

    
  

    
      
  
### 
  
    #**output_header_level**(level)  ⇒ Object 
  

  

  

  
    

Return the output header level given a level.

Uses the `header_offset` option for adjusting the header level.

  

  

  
    
      

```

169
170
171
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 169

def output_header_level(level)
  [[level + @options[:header_offset], 6].min, 1].max
end

```

    
  

    
      
  
### 
  
    #**smart_quote_entity**(el)  ⇒ Object 
  

  

  

  
    

Return the entity that represents the given smart_quote element.

  

  

  
    
      

```

248
249
250
251
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 248

def smart_quote_entity(el)
  res = @options[:smart_quotes][SMART_QUOTE_INDICES[el.value]]
  ::Kramdown::Utils::Entities.entity(res)
end

```

    
  

    
      
  
### 
  
    #**warning**(text)  ⇒ Object 
  

  

  

  
    

Add the given warning `text` to the warning array.

  

  

  
    
      

```

156
157
158
```

    
    
      

```
# File 'lib/kramdown/converter/base.rb', line 156

def warning(text)
  @warnings << text
end

```