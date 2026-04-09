# Module: Jekyll::Filters
  
      Includes:
      DateFilters, GroupingFilters, URLFilters
  
  
  

  

  
  
    Defined in:
    lib/jekyll/filters.rb,

  lib/jekyll/filters/url_filters.rb,
 lib/jekyll/filters/date_filters.rb,
 lib/jekyll/filters/grouping_filters.rb

## Defined Under Namespace

      **Modules:** DateFilters, GroupingFilters, URLFilters
    
  
    
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**array_to_sentence_string**(array, connector = "and")  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Join an array of things into a string by separating with commas and the word “and” for the last one.

-
  
      #**cgi_escape**(input)  ⇒ Object 

CGI escape a string for use in a URL.

-
  
      #**find**(input, property, value)  ⇒ Object 

Search an array of objects and returns the first object that has the queried attribute with the given value or returns nil otherwise.

-
  
      #**find_exp**(input, variable, expression)  ⇒ Object 

Searches an array of objects against an expression and returns the first object for which the expression evaluates to true, or returns nil otherwise.

-
  
      #**inspect**(input)  ⇒ Object 

Convert an object into its String representation for debugging.

-
  
      #**jsonify**(input)  ⇒ Object 

Convert the input into json string.

-
  
      #**markdownify**(input)  ⇒ Object 

Convert a Markdown string into HTML output.

-
  
      #**normalize_whitespace**(input)  ⇒ Object 

Replace any whitespace in the input string with a single space.

-
  
      #**number_of_words**(input, mode = nil)  ⇒ Object 

Count the number of words in the input string.

-
  
      #**pop**(array, num = 1)  ⇒ Object 

-
  
      #**push**(array, input)  ⇒ Object 

-
  
      #**sample**(input, num = 1)  ⇒ Object 

-
  
      #**sassify**(input)  ⇒ Object 

Convert a Sass string into CSS output.

-
  
      #**scssify**(input)  ⇒ Object 

Convert a Scss string into CSS output.

-
  
      #**shift**(array, num = 1)  ⇒ Object 

-
  
      #**slugify**(input, mode = nil)  ⇒ Object 

Slugify a filename or title.

-
  
      #**smartify**(input)  ⇒ Object 

Convert quotes into smart quotes.

-
  
      #**sort**(input, property = nil, nils = "first")  ⇒ Object 

Sort an array of objects.

-
  
      #**to_integer**(input)  ⇒ Object 

Convert the input into integer.

-
  
      #**unshift**(array, input)  ⇒ Object 

-
  
      #**uri_escape**(input)  ⇒ Object 

URI escape a string.

-
  
      #**where**(input, property, value)  ⇒ Object 

Filter an array of objects.

-
  
      #**where_exp**(input, variable, expression)  ⇒ Object 

Filters an array of objects against an expression.

-
  
      #**xml_escape**(input)  ⇒ Object 

XML escape a string for use.

### Methods included from DateFilters

# date_to_long_string, #date_to_rfc822, #date_to_string, #date_to_xmlschema

### Methods included from GroupingFilters

# group_by, #group_by_exp

### Methods included from URLFilters

# absolute_url, #relative_url, #strip_index

## Instance Method Details

###
  
    #**array_to_sentence_string**(array, connector = "and")  ⇒ Object 
  

  

  

  
    

Join an array of things into a string by separating with commas and the word “and” for the last one.

array - The Array of Strings to join. connector - Word used to connect the last 2 items in the array

Examples

```
array_to_sentence_string(["apples", "oranges", "grapes"])
# => "apples, oranges, and grapes"

```

Returns the formatted String.

```

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
```

```
# File 'lib/jekyll/filters.rb', line 152

def array_to_sentence_string(array, connector = "and")
  case array.length
  when 0
    ""
  when 1
    array[0].to_s
  when 2
    "#{array[0]} #{connector} #{array[1]}"
  else
    "#{array[0...-1].join(", ")}, #{connector} #{array[-1]}"
  end
end
```

###
  
    #**cgi_escape**(input)  ⇒ Object 
  

  

  

  
    

CGI escape a string for use in a URL. Replaces any special characters with appropriate %XX replacements.

input - The String to escape.

Examples

```
cgi_escape('foo,bar;baz?')
# => "foo%2Cbar%3Bbaz%3F"

```

Returns the escaped String.

```

92
93
94
```

```
# File 'lib/jekyll/filters.rb', line 92

def cgi_escape(input)
  CGI.escape(input)
end
```

###
  
    #**find**(input, property, value)  ⇒ Object 
  

  

  

  
    

Search an array of objects and returns the first object that has the queried attribute with the given value or returns nil otherwise.

input    - the object array. property - the property within each object to search by. value    - the desired value.

```
Cannot be an instance of Array nor Hash since calling #to_s on them returns
their `#inspect` string object.

```

Returns the found object or nil

rubocop:disable Metrics/CyclomaticComplexity

```

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
```

```
# File 'lib/jekyll/filters.rb', line 235

def find(input, property, value)
  return input if !property || value.is_a?(Array) || value.is_a?(Hash)
  return input unless input.respond_to?(:find)

  input    = input.values if input.is_a?(Hash)
  input_id = input.hash

  # implement a hash based on method parameters to cache the end-result for given parameters.
  @find_filter_cache ||= {}
  @find_filter_cache[input_id] ||= {}
  @find_filter_cache[input_id][property] ||= {}

  # stash or retrieve results to return
  # Since `enum.find` can return nil or false, we use a placeholder string "<__NO MATCH__>"
  #   to validate caching.
  result = @find_filter_cache[input_id][property][value] ||= input.find do |object|
    compare_property_vs_target(item_property(object, property), value)
  end || "<__NO MATCH__>"

  return nil if result == "<__NO MATCH__>"

  result
end
```

###
  
    #**find_exp**(input, variable, expression)  ⇒ Object 
  

  

  

  
    

Searches an array of objects against an expression and returns the first object for which the expression evaluates to true, or returns nil otherwise.

input - the object array variable - the variable to assign each item to in the expression expression - a Liquid comparison expression passed in as a string

Returns the found object or nil

```

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
```

```
# File 'lib/jekyll/filters.rb', line 268

def find_exp(input, variable, expression)
  return input unless input.respond_to?(:find)

  input = input.values if input.is_a?(Hash)

  condition = parse_condition(expression)
  @context.stack do
    input.find do |object|
      @context[variable] = object
      condition.evaluate(@context)
    end
  end
end
```

###
  
    #**inspect**(input)  ⇒ Object 
  

  

  

  
    

Convert an object into its String representation for debugging

input - The Object to be converted

Returns a String representation of the object.

```

371
372
373
```

```
# File 'lib/jekyll/filters.rb', line 371

def inspect(input)
  xml_escape(input.inspect)
end
```

###
  
    #**jsonify**(input)  ⇒ Object 
  

  

  

  
    

Convert the input into json string

input - The Array or Hash to be converted

Returns the converted json string

```

170
171
172
```

```
# File 'lib/jekyll/filters.rb', line 170

def jsonify(input)
  as_liquid(input).to_json
end
```

###
  
    #**markdownify**(input)  ⇒ Object 
  

  

  

  
    

Convert a Markdown string into HTML output.

input - The Markdown String to convert.

Returns the HTML formatted String.

```

16
17
18
19
20
```

```
# File 'lib/jekyll/filters.rb', line 16

def markdownify(input)
  @context.registers[:site].find_converter_instance(
    Jekyll::Converters::Markdown
  ).convert(input.to_s)
end
```

###
  
    #**normalize_whitespace**(input)  ⇒ Object 
  

  

  

  
    

Replace any whitespace in the input string with a single space

input - The String on which to operate.

Returns the formatted String

```

115
116
117
```

```
# File 'lib/jekyll/filters.rb', line 115

def normalize_whitespace(input)
  input.to_s.gsub(%r!\s+!, " ").tap(&:strip!)
end
```

###
  
    #**number_of_words**(input, mode = nil)  ⇒ Object 
  

  

  

  
    

Count the number of words in the input string.

input - The String on which to operate.

Returns the Integer word count.

```

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
# File 'lib/jekyll/filters.rb', line 124

def number_of_words(input, mode = nil)
  cjk_charset = '\p{Han}\p{Katakana}\p{Hiragana}\p{Hangul}'
  cjk_regex = %r![#{cjk_charset}]!o
  word_regex = %r![^#{cjk_charset}\s]+!o

  case mode
  when "cjk"
    input.scan(cjk_regex).length + input.scan(word_regex).length
  when "auto"
    cjk_count = input.scan(cjk_regex).length
    cjk_count.zero? ? input.split.length : cjk_count + input.scan(word_regex).length
  else
    input.split.length
  end
end
```

###
  
    #**pop**(array, num = 1)  ⇒ Object 
  

  

  

  
    
      

```

321
322
323
324
325
326
327
328
```

```
# File 'lib/jekyll/filters.rb', line 321

def pop(array, num = 1)
  return array unless array.is_a?(Array)

  num = Liquid::Utils.to_integer(num)
  new_ary = array.dup
  new_ary.pop(num)
  new_ary
end
```

###
  
    #**push**(array, input)  ⇒ Object 
  

  

  

  
    
      

```

330
331
332
333
334
335
336
```

```
# File 'lib/jekyll/filters.rb', line 330

def push(array, input)
  return array unless array.is_a?(Array)

  new_ary = array.dup
  new_ary.push(input)
  new_ary
end
```

###
  
    #**sample**(input, num = 1)  ⇒ Object 
  

  

  

  
    
      

```

355
356
357
358
359
360
361
362
363
364
```

```
# File 'lib/jekyll/filters.rb', line 355

def sample(input, num = 1)
  return input unless input.respond_to?(:sample)

  num = Liquid::Utils.to_integer(num) rescue 1
  if num == 1
    input.sample
  else
    input.sample(num)
  end
end
```

###
  
    #**sassify**(input)  ⇒ Object 
  

  

  

  
    

Convert a Sass string into CSS output.

input - The Sass String to convert.

Returns the CSS formatted String.

```

38
39
40
41
42
```

```
# File 'lib/jekyll/filters.rb', line 38

def sassify(input)
  @context.registers[:site].find_converter_instance(
    Jekyll::Converters::Sass
  ).convert(input)
end
```

###
  
    #**scssify**(input)  ⇒ Object 
  

  

  

  
    

Convert a Scss string into CSS output.

input - The Scss String to convert.

Returns the CSS formatted String.

```

49
50
51
52
53
```

```
# File 'lib/jekyll/filters.rb', line 49

def scssify(input)
  @context.registers[:site].find_converter_instance(
    Jekyll::Converters::Scss
  ).convert(input)
end
```

###
  
    #**shift**(array, num = 1)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/jekyll/filters.rb', line 338

def shift(array, num = 1)
  return array unless array.is_a?(Array)

  num = Liquid::Utils.to_integer(num)
  new_ary = array.dup
  new_ary.shift(num)
  new_ary
end
```

###
  
    #**slugify**(input, mode = nil)  ⇒ Object 
  

  

  

  
    

Slugify a filename or title.

input - The filename or title to slugify. mode - how string is slugified

Returns the given filename or title as a lowercase URL String. See Utils.slugify for more detail.

```

62
63
64
```

```
# File 'lib/jekyll/filters.rb', line 62

def slugify(input, mode = nil)
  Utils.slugify(input, :mode => mode)
end
```

###
  
    #**smartify**(input)  ⇒ Object 
  

  

  

  
    

Convert quotes into smart quotes.

input - The String to convert.

Returns the smart-quotified String.

```

27
28
29
30
31
```

```
# File 'lib/jekyll/filters.rb', line 27

def smartify(input)
  @context.registers[:site].find_converter_instance(
    Jekyll::Converters::SmartyPants
  ).convert(input.to_s)
end
```

###
  
    #**sort**(input, property = nil, nils = "first")  ⇒ Object 
  

  

  

  
    

Sort an array of objects

input - the object array property - property within each object to filter by nils (‘first’ | ‘last’) - nils appear before or after non-nil values

Returns the filtered array of objects

Raises:

-

        (ArgumentError)

```

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
312
313
314
315
316
317
318
319
```

```
# File 'lib/jekyll/filters.rb', line 301

def sort(input, property = nil, nils = "first")
  raise ArgumentError, "Cannot sort a null object." if input.nil?

  if property.nil?
    input.sort
  else
    case nils
    when "first"
      order = - 1
    when "last"
      order = + 1
    else
      raise ArgumentError, "Invalid nils order: " \
                           "'#{nils}' is not a valid nils order. It must be 'first' or 'last'."
    end

    sort_input(input, property, order)
  end
end
```

###
  
    #**to_integer**(input)  ⇒ Object 
  

  

  

  
    

Convert the input into integer

input - the object string

Returns the integer value

```

287
288
289
290
291
292
```

```
# File 'lib/jekyll/filters.rb', line 287

def to_integer(input)
  return 1 if input == true
  return 0 if input == false

  input.to_i
end
```

###
  
    #**unshift**(array, input)  ⇒ Object 
  

  

  

  
    
      

```

347
348
349
350
351
352
353
```

```
# File 'lib/jekyll/filters.rb', line 347

def unshift(array, input)
  return array unless array.is_a?(Array)

  new_ary = array.dup
  new_ary.unshift(input)
  new_ary
end
```

###
  
    #**uri_escape**(input)  ⇒ Object 
  

  

  

  
    

URI escape a string.

input - The String to escape.

Examples

```
uri_escape('foo, bar \\baz?')
# => "foo,%20bar%20%5Cbaz?"

```

Returns the escaped String.

```

106
107
108
```

```
# File 'lib/jekyll/filters.rb', line 106

def uri_escape(input)
  Addressable::URI.normalize_component(input)
end
```

###
  
    #**where**(input, property, value)  ⇒ Object 
  

  

  

  
    

Filter an array of objects

input    - the object array. property - the property within each object to filter by. value    - the desired value.

```
Cannot be an instance of Array nor Hash since calling #to_s on them returns
their `#inspect` string object.

```

Returns the filtered array of objects

```

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
# File 'lib/jekyll/filters.rb', line 183

def where(input, property, value)
  return input if !property || value.is_a?(Array) || value.is_a?(Hash)
  return input unless input.respond_to?(:select)

  input    = input.values if input.is_a?(Hash)
  input_id = input.hash

  # implement a hash based on method parameters to cache the end-result
  # for given parameters.
  @where_filter_cache ||= {}
  @where_filter_cache[input_id] ||= {}
  @where_filter_cache[input_id][property] ||= {}

  # stash or retrieve results to return
  @where_filter_cache[input_id][property][value] ||= input.select do |object|
    compare_property_vs_target(item_property(object, property), value)
  end.to_a
end
```

###
  
    #**where_exp**(input, variable, expression)  ⇒ Object 
  

  

  

  
    

Filters an array of objects against an expression

input - the object array variable - the variable to assign each item to in the expression expression - a Liquid comparison expression passed in as a string

Returns the filtered array of objects

```

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
```

```
# File 'lib/jekyll/filters.rb', line 209

def where_exp(input, variable, expression)
  return input unless input.respond_to?(:select)

  input = input.values if input.is_a?(Hash) # FIXME

  condition = parse_condition(expression)
  @context.stack do
    input.select do |object|
      @context[variable] = object
      condition.evaluate(@context)
    end
  end || []
end
```

###
  
    #**xml_escape**(input)  ⇒ Object 
  

  

  

  
    

XML escape a string for use. Replaces any special characters with appropriate HTML entity replacements.

input - The String to escape.

Examples

```
xml_escape('foo "bar" <baz>')
# => "foo "bar" <baz>"

```

Returns the escaped String.

```

77
78
79
```

```
# File 'lib/jekyll/filters.rb', line 77

def xml_escape(input)
  input.to_s.encode(:xml => :attr).gsub(%r!\A"|"\Z!, "")
end
```
