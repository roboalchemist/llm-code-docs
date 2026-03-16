# Module: Capybara::Node::Finders
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Base, Simple
  
  

  
  
    Defined in:
    lib/capybara/node/finders.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**all**([kind = Capybara.default_selector], locator = nil, **options)  ⇒ Capybara::Result 
    

    
      (also: #find_all)
    
  
  
  
  
  
  
  
  

  
    

Find all elements on the page matching the given selector and options.

  

      
        
- 
  
    
      #**ancestor**(*args, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find an Element based on the given arguments that is also an ancestor of the element called on.

  

      
        
- 
  
    
      #**find**(*args, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find an Element based on the given arguments.

  

      
        
- 
  
    
      #**find_button**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a button on the page.

  

      
        
- 
  
    
      #**find_by_id**(id, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a element on the page, given its id.

  

      
        
- 
  
    
      #**find_field**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a form field on the page.

  

      
        
- 
  
    
      #**find_link**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a link on the page.

  

      
        
- 
  
    
      #**first**([kind], locator, options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find the first element on the page matching the given selector and options.

  

      
        
- 
  
    
      #**sibling**(*args, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find an Element based on the given arguments that is also a sibling of the element called on.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**all**([kind = Capybara.default_selector], locator = nil, **options)  ⇒ Capybara::Result 
    
      #**all**([kind = Capybara.default_selector], locator = nil, **options) {|element| ... } ⇒ Capybara::Result 
    
  

  
    Also known as:
    find_all
    
  

  

  
    

Find all elements on the page matching the given selector
and options.

Both XPath and CSS expressions are supported, but Capybara
does not try to automatically distinguish between them. The
following statements are equivalent:

```
page.all(:css, 'a#person_123')
page.all(:xpath, './/a[@id="person_123"]')

```

If the type of selector is left out, Capybara uses
default_selector. It's set to `:css` by default.

```
page.all("a#person_123")

Capybara.default_selector = :xpath
page.all('.//a[@id="person_123"]')

```

The set of found elements can further be restricted by specifying
options. It's possible to select elements by their text or visibility:

```
page.all('a', text: 'Home')
page.all('#menu li', visible: true)

```

By default Capybara's waiting behavior will wait up to default_max_wait_time
seconds for matching elements to be available and then return an empty result if none
are available. It is possible to set expectations on the number of results located and
Capybara will raise an exception if the number of elements located don't satisfy the
specified conditions. The expectations can be set using:

```
page.assert_selector('p#foo', count: 4)
page.assert_selector('p#foo', maximum: 10)
page.assert_selector('p#foo', minimum: 1)
page.assert_selector('p#foo', between: 1..10)

```

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  

Overloads:
  

    
      
      
      
- 
        #**all**([kind = Capybara.default_selector], locator = nil, **options) {|element| ... } ⇒ Capybara::Result 
        
  
    

  

  

Yield Parameters:

  
    
  - 
      
        element
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element being considered for inclusion in the results

      
    
  

Yield Returns:

  
    
  - 
      
      
        (Boolean)
      
      
      
        —
        

Should the element be considered in the results?

      
    
  

      
    
  

  
    
    
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          text
          (String, Regexp)
          
            
          
          
            — 

Only find elements which contain this text or match this regexp

          
        
      
        
- 
          exact_text
          (String, Regexp, String)
          
            
          
          
            — 

When String the elements contained text must match exactly, when Boolean controls whether the `text` option must match exactly.
Defaults to exact_text.

          
        
      
        
- 
          normalize_ws
          (Boolean)
          
            
          
          
            — 

Whether the `text`/`exact_text` options are compared against element text with whitespace normalized or as returned by the driver.
Defaults to default_normalize_ws.

          
        
      
        
- 
          visible
          (Boolean, Symbol)
          
            
          
          
            — 

Only find elements with the specified visibility. Defaults to behavior indicated by ignore_hidden_elements.

  - true - only finds visible elements.

  - false - finds invisible *and* visible elements.

  - :all - same as false; finds visible and invisible elements.

  - :hidden - only finds invisible elements.

  - :visible - same as true; only finds visible elements.

          
        
      
        
- 
          obscured
          (Boolean)
          
            
          
          
            — 

Only find elements with the specified obscured state:

  - true - only find elements whose centerpoint is not in the viewport or is obscured by another non-descendant element.

  - false - only find elements whose centerpoint is in the viewport and is not obscured by other non-descendant elements.

          
        
      
        
- 
          id
          (String, Regexp)
          
            
          
          
            — 

Only find elements with an id that matches the value passed

          
        
      
        
- 
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Only find elements with matching class/classes.

  - Absence of a class can be checked by prefixing the class name with `!`

  - 

If you need to check for existence of a class name that starts with `!` then prefix with `!!`

class:['a', '!b', '!!!c'] # limit to elements with class 'a' and '!c' but not class 'b'

          
        
      
        
- 
          style
          (String, Regexp, Hash)
          
            
          
          
            — 

Only find elements with matching style. String and Regexp will be checked against text of the elements `style` attribute, while a Hash will be compared against the elements full style

          
        
      
        
- 
          exact
          (Boolean)
          
            
          
          
            — 

Control whether `is` expressions in the given XPath match exactly or partially. Defaults to exact.

          
        
      
        
- 
          match
          (Symbol)
          
            
          
          
            — 

The matching strategy to use. Defaults to match.

          
        
      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
- 
          count
          (Integer)
          
            
          
          
            — 

Exact number of matches that are expected to be found

          
        
      
        
- 
          maximum
          (Integer)
          
            
          
          
            — 

Maximum number of matches that are expected to be found

          
        
      
        
- 
          minimum
          (Integer)
          
            
          
          
            — 

Minimum number of matches that are expected to be found

          
        
      
        
- 
          between
          (Range)
          
            
          
          
            — 

Number of matches found must be within the given range

          
        
      
        
- 
          allow_reload
          (Boolean)
          
            
          
          
            — 

Beta feature - May be removed in any version.
When `true` allows elements to be reloaded if they become stale. This is an advanced behavior and should only be used
if you fully understand the potential ramifications. The results can be confusing on dynamic pages. Defaults to `false`

          
        
      
    

  

Raises:

  
    
- 
      
      
      
      
        
        

The number of elements found doesn't match the specified conditions

      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 257

def all(*args, allow_reload: false, **options, &optional_filter_block)
  minimum_specified = options_include_minimum?(options)
  options = { minimum: 1 }.merge(options) unless minimum_specified
  options[:session_options] = session_options
  query = Capybara::Queries::SelectorQuery.new(*args, **options, &optional_filter_block)
  result = nil
  begin
    synchronize(query.wait) do
      result = query.resolve_for(self)
      result.allow_reload! if allow_reload
      raise Capybara::ExpectationNotMet, result.failure_message unless result.matches_count?

      result
    end
  rescue Capybara::ExpectationNotMet
    raise if minimum_specified || (result.compare_count == 1)

    Result.new([], nil)
  end
end

```

    
  

    
      
  
### 
  
    #**ancestor**(*args, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find an Element based on the given arguments that is also an ancestor of the element called on.
#ancestor will raise an error if the element is not found.

#ancestor takes the same options as #find.

```
element.ancestor('#foo').find('.bar')
element.ancestor(:xpath, './/div[contains(., "bar")]')
element.ancestor('ul', text: 'Quox').click_link('Delete')

```

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  
    
    

Raises:

  
    
- 
      
      
      
      
        
        

If the element can't be found before time expires

      
    
  

  
    
      

```

81
82
83
84
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 81

def ancestor(*args, **options, &optional_filter_block)
  options[:session_options] = session_options
  synced_resolve Capybara::Queries::AncestorQuery.new(*args, **options, &optional_filter_block)
end

```

    
  

    
      
  
### 
  
    #**find**(*args, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find an Element based on the given arguments. #find will raise an error if the element
is not found.

```
page.find('#foo').find('.bar')
page.find(:xpath, './/div[contains(., "bar")]')
page.find('li', text: 'Quox').click_link('Delete')

```

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
- 
          text
          (String, Regexp)
          
            
          
          
            — 

Only find elements which contain this text or match this regexp

          
        
      
        
- 
          exact_text
          (String, Regexp, String)
          
            
          
          
            — 

When String the elements contained text must match exactly, when Boolean controls whether the `text` option must match exactly.
Defaults to exact_text.

          
        
      
        
- 
          normalize_ws
          (Boolean)
          
            
          
          
            — 

Whether the `text`/`exact_text` options are compared against element text with whitespace normalized or as returned by the driver.
Defaults to default_normalize_ws.

          
        
      
        
- 
          visible
          (Boolean, Symbol)
          
            
          
          
            — 

Only find elements with the specified visibility. Defaults to behavior indicated by ignore_hidden_elements.

  - true - only finds visible elements.

  - false - finds invisible *and* visible elements.

  - :all - same as false; finds visible and invisible elements.

  - :hidden - only finds invisible elements.

  - :visible - same as true; only finds visible elements.

          
        
      
        
- 
          obscured
          (Boolean)
          
            
          
          
            — 

Only find elements with the specified obscured state:

  - true - only find elements whose centerpoint is not in the viewport or is obscured by another non-descendant element.

  - false - only find elements whose centerpoint is in the viewport and is not obscured by other non-descendant elements.

          
        
      
        
- 
          id
          (String, Regexp)
          
            
          
          
            — 

Only find elements with an id that matches the value passed

          
        
      
        
- 
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Only find elements with matching class/classes.

  - Absence of a class can be checked by prefixing the class name with `!`

  - 

If you need to check for existence of a class name that starts with `!` then prefix with `!!`

class:['a', '!b', '!!!c'] # limit to elements with class 'a' and '!c' but not class 'b'

          
        
      
        
- 
          style
          (String, Regexp, Hash)
          
            
          
          
            — 

Only find elements with matching style. String and Regexp will be checked against text of the elements `style` attribute, while a Hash will be compared against the elements full style

          
        
      
        
- 
          exact
          (Boolean)
          
            
          
          
            — 

Control whether `is` expressions in the given XPath match exactly or partially. Defaults to exact.

          
        
      
        
- 
          match
          (Symbol)
          
            
          
          
            — 

The matching strategy to use. Defaults to match.

          
        
      
    

  
    
    

Raises:

  
    
- 
      
      
      
      
        
        

If the element can't be found before time expires

      
    
  

  
    
      

```

51
52
53
54
55
56
57
58
59
60
61
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 51

def find(*args, **options, &optional_filter_block)
  options[:session_options] = session_options
  count_options = options.slice(*Capybara::Queries::BaseQuery::COUNT_KEYS)
  unless count_options.empty?
    Capybara::Helpers.warn(
      "'find' does not support count options (#{count_options}) ignoring. " \
      "Called from: #{Capybara::Helpers.filter_backtrace(caller)}"
    )
  end
  synced_resolve Capybara::Queries::SelectorQuery.new(*args, **options, &optional_filter_block)
end

```

    
  

    
      
  
### 
  
    #**find_button**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a button on the page.
This can be any `<input>` element of type submit, reset, image, button or it can be a
`<button>` element. All buttons can be found by their id, name, test_id attribute, value, or title.
`<button>` elements can also be found by their text content, and image `<input>` elements by their alt attribute.

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
- 
          disabled
          (Boolean, Symbol)
          
            
              — default:
              false
            
          
          
            — 

Match disabled button?

  - true - only finds a disabled button

  - false - only finds an enabled button

  - :all - finds either an enabled or disabled button

          
        
      
        
- 
          id
          (String, Regexp)
          
            
          
          
            — 

Match buttons with the id provided

          
        
      
        
- 
          name
          (String)
          
            
          
          
            — 

Match buttons with the name provided

          
        
      
        
- 
          title
          (String)
          
            
          
          
            — 

Match buttons with the title provided

          
        
      
        
- 
          value
          (String)
          
            
          
          
            — 

Match buttons with the value provided

          
        
      
        
- 
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Match buttons that match the class(es) provided

          
        
      
    

  

  
    
      

```

184
185
186
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 184

def find_button(locator = nil, **options, &optional_filter_block)
  find(:button, locator, **options, &optional_filter_block)
end

```

    
  

    
      
  
### 
  
    #**find_by_id**(id, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a element on the page, given its id.

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  
    
    

  
    
      

```

198
199
200
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 198

def find_by_id(id, **options, &optional_filter_block)
  find(:id, id, **options, &optional_filter_block)
end

```

    
  

    
      
  
### 
  
    #**find_field**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a form field on the page. The field can be found by its name, id or label text.

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
- 
          checked
          (Boolean)
          
            
          
          
            — 

Match checked field?

          
        
      
        
- 
          unchecked
          (Boolean)
          
            
          
          
            — 

Match unchecked field?

          
        
      
        
- 
          disabled
          (Boolean, Symbol)
          
            
              — default:
              false
            
          
          
            — 

Match disabled field?

  - true - only finds a disabled field

  - false - only finds an enabled field

  - :all - finds either an enabled or disabled field

          
        
      
        
- 
          readonly
          (Boolean)
          
            
          
          
            — 

Match readonly field?

          
        
      
        
- 
          with
          (String, Regexp)
          
            
          
          
            — 

Value of field to match on

          
        
      
        
- 
          type
          (String)
          
            
          
          
            — 

Type of field to match on

          
        
      
        
- 
          multiple
          (Boolean)
          
            
          
          
            — 

Match fields that can have multiple values?

          
        
      
        
- 
          id
          (String, Regexp)
          
            
          
          
            — 

Match fields that match the id attribute

          
        
      
        
- 
          name
          (String)
          
            
          
          
            — 

Match fields that match the name attribute

          
        
      
        
- 
          placeholder
          (String)
          
            
          
          
            — 

Match fields that match the placeholder attribute

          
        
      
        
- 
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Match fields that match the class(es) passed

          
        
      
    

  

  
    
      

```

135
136
137
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 135

def find_field(locator = nil, **options, &optional_filter_block)
  find(:field, locator, **options, &optional_filter_block)
end

```

    
  

    
      
  
### 
  
    #**find_link**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a link on the page. The link can be found by its id or text.

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
- 
          href
          (String, Regexp, nil)
          
            
          
          
            — 

Value to match against the links href, if `nil` finds link placeholders (`<a>` elements with no href attribute), if `false` ignores the href

          
        
      
        
- 
          id
          (String, Regexp)
          
            
          
          
            — 

Match links with the id provided

          
        
      
        
- 
          title
          (String)
          
            
          
          
            — 

Match links with the title provided

          
        
      
        
- 
          alt
          (String)
          
            
          
          
            — 

Match links with a contained img element whose alt matches

          
        
      
        
- 
          download
          (String, Boolean)
          
            
          
          
            — 

Match links with the download provided

          
        
      
        
- 
          target
          (String)
          
            
          
          
            — 

Match links with the target provided

          
        
      
        
- 
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Match links that match the class(es) provided

          
        
      
    

  

  
    
      

```

157
158
159
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 157

def find_link(locator = nil, **options, &optional_filter_block)
  find(:link, locator, **options, &optional_filter_block)
end

```

    
  

    
      
  
### 
  
    #**first**([kind], locator, options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find the first element on the page matching the given selector
and options. By default #first will wait up to default_max_wait_time
seconds for matching elements to appear and then raise an error if no matching
element is found, or `nil` if the provided count options allow for empty results.

  

  
  

Raises:

  
    
- 
      
      
      
      
        
        

If element(s) matching the provided options can't be found before time expires

      
    
  

  
    
      

```

293
294
295
296
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 293

def first(*args, **options, &optional_filter_block)
  options = { minimum: 1 }.merge(options) unless options_include_minimum?(options)
  all(*args, **options, &optional_filter_block).first
end

```

    
  

    
      
  
### 
  
    #**sibling**(*args, **options, &optional_filter_block)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find an Element based on the given arguments that is also a sibling of the element called on.
#sibling will raise an error if the element is not found.

#sibling takes the same options as #find.

```
element.sibling('#foo').find('.bar')
element.sibling(:xpath, './/div[contains(., "bar")]')
element.sibling('ul', text: 'Quox').click_link('Delete')

```

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  
  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  
    
    

Raises:

  
    
- 
      
      
      
      
        
        

If the element can't be found before time expires

      
    
  

  
    
      

```

104
105
106
107
```

    
    
      

```
# File 'lib/capybara/node/finders.rb', line 104

def sibling(*args, **options, &optional_filter_block)
  options[:session_options] = session_options
  synced_resolve Capybara::Queries::SiblingQuery.new(*args, **options, &optional_filter_block)
end

```