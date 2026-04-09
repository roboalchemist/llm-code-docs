# Class: Capybara::Selector::Definition
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Selector::Definition
          
        

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/selector/definition.rb
  
  

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**expressions**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute expressions.

  

    
      
- 
  
    
      #**name**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**css**(*allowed_filters, &block)  ⇒ #call 
    

    
  
  
  
  
  
  
  
  

  
    

Define a selector by a CSS selector.

  

      
        
- 
  
    
      #**custom_filters**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_format**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**default_visibility**(fallback = Capybara.ignore_hidden_elements, options = {})  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**describe_all_expression_filters**(**opts)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**describe_expression_filters**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**describe_node_filters**(&block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**description**(options)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Description of the selector when used with the options passed.

  

      
        
- 
  
    
      #**expression_filter**(name, *types, matcher: nil, **options, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**expression_filters**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**filter_set**(name, filters_to_use = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**initialize**(name, locator_type: nil, raw_locator: false, supports_exact: nil, &block)  ⇒ Definition 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Definition.

  

      
        
- 
  
    
      #**label**(label = nil)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Set/get a descriptive label for the selector.

  

      
        
- 
  
    
      #**locator_filter**(*types, **options, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**locator_types**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**match** {|locator| ... } ⇒ #call 
    

    
  
  
  
  
  
  
  
  

  
    

Automatic selector detection.

  

      
        
- 
  
    
      #**match?**(locator)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Should this selector be used for the passed in locator.

  

      
        
- 
  
    
      #**node_filter**(name, *types, options = {}, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**node_filters**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**raw_locator?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**supports_exact?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**visible**(default_visibility = nil, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Set the default visibility mode that should be used if no visible option is passed when using the selector.

  

      
        
- 
  
    
      #**xpath**(*allowed_filters, &block)  ⇒ #call 
    

    
  
  
  
  
  
  
  
  

  
    

Define a selector by an xpath expression.

  

      
    

  

  
  
## Constructor Details

  
    
  
### 
  
    #**initialize**(name, locator_type: nil, raw_locator: false, supports_exact: nil, &block)  ⇒ Definition 
  

  

  

  
    

Returns a new instance of Definition.

  

  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 16

def initialize(name, locator_type: nil, raw_locator: false, supports_exact: nil, &block)
  @name = name
  @filter_set = Capybara::Selector::FilterSet.add(name)
  @match = nil
  @label = nil
  @failure_message = nil
  @expressions = {}
  @expression_filters = {}
  @locator_filter = nil
  @default_visibility = nil
  @locator_type = locator_type
  @raw_locator = raw_locator
  @supports_exact = supports_exact
  instance_eval(&block)
end
```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**expressions**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute expressions.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 12

def expressions
  @expressions
end
```

    
  

    
      
      
      
  
### 
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

  

  

  
    
      

```

12
13
14
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 12

def name
  @name
end
```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**css**(*expression_filters) {|locator, options| ... } ⇒ #call 
    
      #**css**  ⇒ #call 
    
  

  

  

  
    

Define a selector by a CSS selector

  

  
  

Overloads:
  

    
      
      
- 
        #**css**(*expression_filters) {|locator, options| ... } ⇒ #call 
        
  
    

  

  

Parameters:

  
    
  - 
      
        expression_filters
      
      
        (Array<Symbol>)
      
      
      
        —
        

([])  Names of filters that can be implemented via this CSS selector

      
    
  

Yields:

  
    
  - 
      
      
        (locator, options)
      
      
      
        —
        

The block to use to generate the CSS selector

      
    
  

Yield Parameters:

  
    
  - 
      
        locator
      
      
        (String)
      
      
      
        —
        

The locator string passed to the query

      
    
  
    
  - 
      
        options
      
      
        (Hash)
      
      
      
        —
        

The options hash passed to the query

      
    
  

Yield Returns:

  
    
  - 
      
      
        (#to_s)
      
      
      
        —
        

An object that can produce a CSS selector

      
    
  

      
    
      
  

Returns:

  
    
- 
      
      
        (#call)
      
      
      
        —
        

The block that will be called to generate the CSS selector

      
    
  

  
    
      

```

77
78
79
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 77

def css(*allowed_filters, &block)
  expression(:css, allowed_filters, &block)
end
```

    
  

    
      
  
### 
  
    #**custom_filters**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 32

def custom_filters
  warn "Deprecated: Selector#custom_filters is not valid when same named expression and node filter exist - don't use"
  node_filters.merge(expression_filters).freeze
end
```

    
  

    
      
  
### 
  
    #**default_format**  ⇒ Object 
  

  

  

  
    
      

```

236
237
238
239
240
241
242
243
244
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 236

def default_format
  return nil if @expressions.keys.empty?

  if @expressions.size == 1
    @expressions.keys.first
  else
    :xpath
  end
end
```

    
  

    
      
  
### 
  
    #**default_visibility**(fallback = Capybara.ignore_hidden_elements, options = {})  ⇒ Object 
  

  

  

  
    
      

```

217
218
219
220
221
222
223
224
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 217

def default_visibility(fallback = Capybara.ignore_hidden_elements, options = {})
  vis = if @default_visibility.respond_to?(:call)
    @default_visibility.call(options)
  else
    @default_visibility
  end
  vis.nil? ? fallback : vis
end
```

    
  

    
      
  
### 
  
    #**describe_all_expression_filters**(**opts)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/capybara/selector/definition.rb', line 190

def describe_all_expression_filters(**opts)
  expression_filters.map do |ef_name, ef|
    if ef.matcher?
      handled_custom_options(ef, opts).map { |option, value| " with #{ef_name}[#{option} => #{value}]" }.join
    elsif opts.key?(ef_name)
      " with #{ef_name} #{opts[ef_name]}"
    end
  end.join
end
```

    
  

    
      
  
### 
  
    #**describe_expression_filters**(&block)  ⇒ Object 
  

  

  

  
    
      

```

180
181
182
183
184
185
186
187
188
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 180

def describe_expression_filters(&block)
  if block
    describe(:expression_filters, &block)
  else
    describe(:expression_filters) do |**options|
      describe_all_expression_filters(**options)
    end
  end
end
```

    
  

    
      
  
### 
  
    #**describe_node_filters**(&block)  ⇒ Object 
  

  

  

  
    
      

```

200
201
202
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 200

def describe_node_filters(&block)
  describe(:node_filters, &block)
end
```

    
  

    
      
  
### 
  
    #**description**(options)  ⇒ String 
  

  

  

  
    

Returns Description of the selector when used with the options passed.

  

  

Parameters:

  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

The options of the query used to generate the description

      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

Description of the selector when used with the options passed

      
    
  

  
    
      

```

116
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 116

def_delegator :@filter_set, :description
```

    
  

    
      
  
### 
  
    #**expression_filter**(name, *types, matcher: nil, **options, &block)  ⇒ Object 
  

  

  

  
    

  

  

Parameters:

  
    
- 
      
        name
      
      
        (Symbol, Regexp)
      
      
      
        —
        

The filter name

      
    
  
    
- 
      
        matcher
      
      
        (Regexp)
      
      
        *(defaults to: nil)*
      
      
        —
        

(nil)   A Regexp used to check whether a specific option is handled by this filter

      
    
  
    
- 
      
        types
      
      
        (Array<Symbol>)
      
      
      
        —
        

The types of the filter - currently valid types are [:boolean]

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

({})      Options of the filter

      
    
  

  
    
    
    
    
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :valid_values
          (Array<>)
          
            
          
          
            — 

Valid values for this filter

          
        
      
        
- 
          :default
          (Object)
          
            
          
          
            — 

The default value of the filter (if any)

          
        
      
        
- 
          :skip_if
          (Object)
          
            
          
          
            — 

Value of the filter that will cause it to be skipped

          
        
      
        
- 
          :matcher
          (Regexp)
          
            
              — default:
              nil
            
          
          
            — 

A Regexp used to check whether a specific option is handled by this filter.  If not provided the filter will be used for options matching the filter name.

          
        
      
    

  
    
    

  
    
      

```

166
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 166

def_delegators :@filter_set, :node_filter, :expression_filter, :filter
```

    
  

    
      
  
### 
  
    #**expression_filters**  ⇒ Object 
  

  

  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 41

def expression_filters
  @filter_set.expression_filters
end
```

    
  

    
      
  
### 
  
    #**filter_set**(name, filters_to_use = nil)  ⇒ Object 
  

  

  

  
    
      

```

174
175
176
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 174

def filter_set(name, filters_to_use = nil)
  @filter_set.import(name, filters_to_use)
end
```

    
  

    
      
  
### 
  
    
      #**label**(label)  ⇒ String 
    
      #**label**  ⇒ String 
    
  

  

  

  
    

Set/get a descriptive label for the selector

  

  
  

Overloads:
  

    
      
      
- 
        #**label**(label)  ⇒ String 
        
  
    

  

  

Parameters:

  
    
  - 
      
        label
      
      
        (String)
      
      
      
        —
        

A descriptive label for this selector - used in error messages

      
    
  

      
    
      
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The currently set label

      
    
  

  
    
      

```

104
105
106
107
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 104

def label(label = nil)
  @label = label if label
  @label
end
```

    
  

    
      
  
### 
  
    #**locator_filter**(*types, **options, &block)  ⇒ Object 
  

  

  

  
    
      

```

168
169
170
171
172
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 168

def locator_filter(*types, **options, &block)
  types.each { |type| options[type] = true }
  @locator_filter = Capybara::Selector::Filters::LocatorFilter.new(block, **options) if block
  @locator_filter
end
```

    
  

    
      
  
### 
  
    #**locator_types**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

247
248
249
250
251
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 247

def locator_types
  return nil unless @locator_type

  Array(@locator_type)
end
```

    
  

    
      
  
### 
  
    #**match** {|locator| ... } ⇒ #call 
  

  

  

  
    

Automatic selector detection

  

  

Yields:

  
    
- 
      
      
        (locator)
      
      
      
        —
        

This block takes the passed in locator string and returns whether or not it matches the selector

      
    
  

Yield Parameters:

  
    
- 
      
        ,
      
      
        (String)
      
      
      
        —
        

locator      The locator string used to determine if it matches the selector

      
    
  

Yield Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether this selector matches the locator string

      
    
  

Returns:

  
    
- 
      
      
        (#call)
      
      
      
        —
        

The block that will be used to detect selector match

      
    
  

  
    
      

```

90
91
92
93
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 90

def match(&block)
  @match = block if block
  @match
end
```

    
  

    
      
  
### 
  
    #**match?**(locator)  ⇒ Boolean 
  

  

  

  
    

Should this selector be used for the passed in locator

This is used by the automatic selector selection mechanism when no selector type is passed to a selector query

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

The locator passed to the query

      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether or not to use this selector

      
    
  

  
    
      

```

127
128
129
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 127

def match?(locator)
  @match&.call(locator)
end
```

    
  

    
      
  
### 
  
    #**node_filter**(name, *types, options = {}, &block)  ⇒ Object 
  

  

  

  
    

  

  

Parameters:

  
    
- 
      
        name
      
      
        (Symbol, Regexp)
      
      
      
        —
        

The filter name

      
    
  
    
- 
      
        types
      
      
        (Array<Symbol>)
      
      
      
        —
        

The types of the filter - currently valid types are [:boolean]

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
        *(defaults to: {})*
      
      
        —
        

({})      Options of the filter

      
    
  

  
    
    
    
    
    
    
    

Options Hash (options):
    

      
        
- 
          :valid_values
          (Array<>)
          
            
          
          
            — 

Valid values for this filter

          
        
      
        
- 
          :default
          (Object)
          
            
          
          
            — 

The default value of the filter (if any)

          
        
      
        
- 
          :skip_if
          (Object)
          
            
          
          
            — 

Value of the filter that will cause it to be skipped

          
        
      
        
- 
          :matcher
          (Regexp)
          
            
              — default:
              nil
            
          
          
            — 

A Regexp used to check whether a specific option is handled by this filter.  If not provided the filter will be used for options matching the filter name.

          
        
      
    

  
    
    

  
    
      

```

```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 131

```

    
  

    
      
  
### 
  
    #**node_filters**  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 37

def node_filters
  @filter_set.node_filters
end
```

    
  

    
      
  
### 
  
    #**raw_locator?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

227
228
229
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 227

def raw_locator?
  !!@raw_locator
end
```

    
  

    
      
  
### 
  
    #**supports_exact?**  ⇒ Boolean 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

232
233
234
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 232

def supports_exact?
  @supports_exact
end
```

    
  

    
      
  
### 
  
    #**visible**(default_visibility = nil, &block)  ⇒ Object 
  

  

  

  
    

Set the default visibility mode that should be used if no visible option is passed when using the selector.
If not specified will default to the behavior indicated by Capybara.ignore_hidden_elements

  

  

Parameters:

  
    
- 
      
        default_visibility
      
      
        (Symbol)
      
      
        *(defaults to: nil)*
      
      
        —
        

Only find elements with the specified visibility:

  - :all - finds visible and invisible elements.

  - :hidden - only finds invisible elements.

  - :visible - only finds visible elements.

      
    
  

  
    
      

```

213
214
215
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 213

def visible(default_visibility = nil, &block)
  @default_visibility = block || default_visibility
end
```

    
  

    
      
  
### 
  
    
      #**xpath**(*expression_filters) {|locator, options| ... } ⇒ #call 
    
      #**xpath**  ⇒ #call 
    
  

  

  

  
    

Define a selector by an xpath expression

  

  
  

Overloads:
  

    
      
      
- 
        #**xpath**(*expression_filters) {|locator, options| ... } ⇒ #call 
        
  
    

  

  

Parameters:

  
    
  - 
      
        expression_filters
      
      
        (Array<Symbol>)
      
      
      
        —
        

([])  Names of filters that are implemented via this expression, if not specified the names of any keyword parameters in the block will be used

      
    
  

Yields:

  
    
  - 
      
      
        (locator, options)
      
      
      
        —
        

The block to use to generate the XPath expression

      
    
  

Yield Parameters:

  
    
  - 
      
        locator
      
      
        (String)
      
      
      
        —
        

The locator string passed to the query

      
    
  
    
  - 
      
        options
      
      
        (Hash)
      
      
      
        —
        

The options hash passed to the query

      
    
  

Yield Returns:

  
    
  - 
      
      
        (#to_xpath, #to_s)
      
      
      
        —
        

An object that can produce an xpath expression

      
    
  

      
    
      
  

Returns:

  
    
- 
      
      
        (#call)
      
      
      
        —
        

The block that will be called to generate the XPath expression

      
    
  

  
    
      

```

59
60
61
```

    
    
      

```
# File 'lib/capybara/selector/definition.rb', line 59

def xpath(*allowed_filters, &block)
  expression(:xpath, allowed_filters, &block)
end
```