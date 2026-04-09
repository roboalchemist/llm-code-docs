# Module: Capybara::Node::Actions
  
  
  

  

  
  
  
  
  

  
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/capybara/node/actions.rb
  
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**attach_file**(locator = nil, paths, make_visible: nil, **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a descendant file field on the page and attach a file given its path.

  

      
        
- 
  
    
      #**check**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a descendant check box and mark it as checked.

  

      
        
- 
  
    
      #**choose**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a descendant radio button and mark it as checked.

  

      
        
- 
  
    
      #**click_button**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Finds a button on the page and clicks it.

  

      
        
- 
  
    
      #**click_link**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Finds a link by id, test_id attribute, text or title and clicks it.

  

      
        
- 
  
    
      #**click_link_or_button**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
      (also: #click_on)
    
  
  
  
  
  
  
  
  

  
    

Finds a button or link and clicks it.

  

      
        
- 
  
    
      #**fill_in**([locator], with: , **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Locate a text field or text area and fill it in with the given text.

  

      
        
- 
  
    
      #**select**(value = nil, from: nil, **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

If `from` option is present, #select finds a select box, or text input with associated datalist, on the page and selects a particular option from it.

  

      
        
- 
  
    
      #**uncheck**([locator], **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a descendant check box and uncheck it.

  

      
        
- 
  
    
      #**unselect**(value = nil, from: nil, **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Find a select box on the page and unselect a particular option from it.

  

      
    

  

  
    
## Instance Method Details

    
      
  
### 
  
    
      #**attach_file**([locator], paths, **options)  ⇒ Capybara::Node::Element 
    
      #**attach_file**(paths) { ... } ⇒ Capybara::Node::Element 
    
  

  

  

  
    

Find a descendant file field on the page and attach a file given its path. There are two ways to use
#attach_file, in the first method the file field can be found via its name, id,
test_id attribute, or label text. In the case of the file field being hidden for
styling reasons the `make_visible` option can be used to temporarily change the CSS of
the file field, attach the file, and then revert the CSS back to original. If no locator is
passed this will match self or a descendant.
The second method, which is currently in beta and may be changed/removed, involves passing a block
which performs whatever actions would trigger the file chooser to appear.

```
# will attach file to a descendant file input element that has a name, id, or label_text matching 'My File'
page.attach_file('My File', '/path/to/file.png')

# will attach file to el if it's a file input element
el.attach_file('/path/to/file.png')

# will attach file to whatever file input is triggered by the block
page.attach_file('/path/to/file.png') do
  page.find('#upload_button').click
end

```

  

  
  

Overloads:
  

    
      
      
- 
        #**attach_file**([locator], paths, **options)  ⇒ Capybara::Node::Element 
        
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
  - 
      
        locator
      
      
        (String)
      
      
      
        —
        

Which field to attach the file to

      
    
  
    
  - 
      
        paths
      
      
        (String, Array<String>)
      
      
      
        —
        

The path(s) of the file(s) that will be attached

      
    
  

  
    
    
    
    
    
    
    

Options Hash (**options):
    

      
        
  - 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
  - 
          match
          (Symbol)
          
            
          
          
            — 

The matching strategy to use (:one, :first, :prefer_exact, :smart). Defaults to match.

          
        
      
        
  - 
          exact
          (Boolean)
          
            
          
          
            — 

Match the exact label name/contents or accept a partial match. Defaults to exact.

          
        
      
        
  - 
          multiple
          (Boolean)
          
            
          
          
            — 

Match field which allows multiple file selection

          
        
      
        
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
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Match fields that match the class(es) provided

          
        
      
        
  - 
          make_visible
          (true, Hash)
          
            
          
          
            — 

A Hash of CSS styles to change before attempting to attach the file, if `true`, `{ opacity: 1, display: 'block', visibility: 'visible' }` is used (may not be supported by all drivers).

          
        
      
    

  

      
    
      
      
- 
        #**attach_file**(paths) { ... } ⇒ Capybara::Node::Element 
        
  
    

  

  

Parameters:

  
    
  - 
      
        paths
      
      
        (String, Array<String>)
      
      
      
        —
        

The path(s) of the file(s) that will be attached

      
    
  

Yields:

  
    
  - 
      
      
        
      
      
      
        
        

Block whose actions will trigger the system file chooser to be shown

      
    
  

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The file field element

      
    
  

  
    
      

```

279
280
281
282
283
284
285
286
287
288
289
290
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
304
305
306
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 279

def attach_file(locator = nil, paths, make_visible: nil, **options) # rubocop:disable Style/OptionalArguments
  if locator && block_given?
    raise ArgumentError, '`#attach_file` does not support passing both a locator and a block'
  end

  Array(paths).each do |path|
    raise Capybara::FileNotFound, "cannot attach file, #{path} does not exist" unless File.exist?(path.to_s)
  end
  options[:allow_self] = true if locator.nil?

  if block_given?
    begin
      execute_script CAPTURE_FILE_ELEMENT_SCRIPT
      yield
      file_field = evaluate_script 'window._capybara_clicked_file_input'
      raise ArgumentError, "Capybara was unable to determine the file input you're attaching to" unless file_field
    rescue ::Capybara::NotSupportedByDriverError
      warn 'Block mode of `#attach_file` is not supported by the current driver - ignoring.'
    end
  end
  # Allow user to update the CSS style of the file input since they are so often hidden on a page
  if make_visible
    ff = file_field || find(:file_field, locator, **options.merge(visible: :all))
    while_visible(ff, make_visible) { |el| el.set(paths) }
  else
    (file_field || find(:file_field, locator, **options)).set(paths)
  end
end
```

    
  

    
      
  
### 
  
    #**check**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a descendant check box and mark it as checked. The check box can be found
via name, id, test_id attribute, or label text. If no locator
is provided this will match against self or a descendant.

```
# will check a descendant checkbox with a name, id, or label text matching 'German'
page.check('German')

# will check `el` if it's a checkbox element
el.check()

```

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

Which check box to check

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          option
          (String)
          
            
          
          
            — 

Value of the checkbox to select

          
        
      
        
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
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Match fields that match the class(es) provided

          
        
      
        
- 
          allow_label_click
          (Boolean, Hash)
          
            
          
          
            — 

Attempt to click the label to toggle state if element is non-visible. Defaults to automatic_label_click.
If set to a Hash it is passed as options to the `click` on the label

          
        
      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element checked or the label clicked

      
    
  

  
    
      

```

150
151
152
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 150

def check(locator = nil, **options)
  _check_with_label(:checkbox, true, locator, **options)
end
```

    
  

    
      
  
### 
  
    #**choose**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a descendant radio button and mark it as checked. The radio button can be found
via name, id, test_id attribute or label text. If no locator is
provided this will match against self or a descendant.

```
# will choose a descendant radio button with a name, id, or label text matching 'Male'
page.choose('Male')

# will choose `el` if it's a radio button element
el.choose()

```

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

Which radio button to choose

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          option
          (String)
          
            
          
          
            — 

Value of the radio_button to choose

          
        
      
        
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
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Match fields that match the class(es) provided

          
        
      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
- 
          allow_label_click
          (Boolean, Hash)
          
            
          
          
            — 

Attempt to click the label to toggle state if element is non-visible. Defaults to automatic_label_click.
If set to a Hash it is passed as options to the `click` on the label

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element chosen or the label clicked

      
    
  

  
    
      

```

122
123
124
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 122

def choose(locator = nil, **options)
  _check_with_label(:radio_button, true, locator, **options)
end
```

    
  

    
      
  
### 
  
    #**click_button**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Finds a button on the page and clicks it.
This can be any `<input>` element of type submit, reset, image, button or it can be a
`<button>` element. All buttons can be found by their id, name, test_id attribute, value, or title. `<button>` elements can also be found
by their text content, and image `<input>` elements by their alt attribute.

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

Which button to find

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

See Finders#find_button

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element clicked

      
    
  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 57

def click_button(locator = nil, **options)
  find(:button, locator, **options).click
end
```

    
  

    
      
  
### 
  
    #**click_link**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Finds a link by id, test_id attribute, text or title and clicks it. Also looks at image
alt text inside the link.

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

text, id, test_id attribute, title or nested image's alt attribute

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

See Finders#find_link

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element clicked

      
    
  

  
    
      

```

41
42
43
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 41

def click_link(locator = nil, **options)
  find(:link, locator, **options).click
end
```

    
  

    
      
  
### 
  
    #**click_link_or_button**([locator], **options)  ⇒ Capybara::Node::Element 
  

  
    Also known as:
    click_on
    
  

  

  
    

Finds a button or link and clicks it. See #click_button and
#click_link for what locator will match against for each type of element.

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

See #click_button and #click_link

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element clicked

      
    
  

  
    
      

```

25
26
27
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 25

def click_link_or_button(locator = nil, **options)
  find(:link_or_button, locator, **options).click
end
```

    
  

    
      
  
### 
  
    #**fill_in**([locator], with: , **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Locate a text field or text area and fill it in with the given text.
The field can be found via its name, id, test_id attribute, placeholder, or label text.
If no locator is provided this will operate on self or a descendant.

```
# will fill in a descendant fillable field with name, id, or label text matching 'Name'
page.fill_in 'Name', with: 'Bob'

# will fill in `el` if it's a fillable field
el.fill_in with: 'Tom'

```

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

Which field to fill in

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
    
  
    
- 
      
        with:
      
      
        (String)
      
      
        *(defaults to: )*
      
      
        —
        

The value to fill in

      
    
  

  
    
    
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
        
- 
          currently_with
          (String)
          
            
          
          
            — 

The current value property of the field to fill in

          
        
      
        
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

Match fields that match the class(es) provided

          
        
      
        
- 
          fill_options
          (Hash)
          
            
          
          
            — 

Driver specific options regarding how to fill fields (Defaults come from default_set_options)

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element filled in

      
    
  

  
    
      

```

88
89
90
91
92
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 88

def fill_in(locator = nil, with:, currently_with: nil, fill_options: {}, **find_options)
  find_options[:with] = currently_with if currently_with
  find_options[:allow_self] = true if locator.nil?
  find(:fillable_field, locator, **find_options).set(with, **fill_options)
end
```

    
  

    
      
  
### 
  
    #**select**(value = nil, from: nil, **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

If `from` option is present, #select finds a select box, or text input with associated datalist,
on the page and selects a particular option from it.
Otherwise it finds an option inside current scope and selects it.
If the select box is a multiple select, #select can be called multiple times to select more than
one option.
The select box can be found via its name, id, test_id attribute, or label text.
The option can be found by its text.

```
page.select 'March', from: 'Month'

```

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        value
      
      
        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

Which option to select

      
    
  
    
- 
      
        from
      
      
        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

The id, test_id attribute, name or label of the select box

      
    
  

  
    
    
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The option element selected

      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

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
211
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 201

def select(value = nil, from: nil, **options)
  raise ArgumentError, 'The :from option does not take an element' if from.is_a? Capybara::Node::Element

  el = from ? find_select_or_datalist_input(from, options) : self

  if el.respond_to?(:tag_name) && (el.tag_name == 'input')
    select_datalist_option(el, value)
  else
    el.find(:option, value, **options).select_option
  end
end
```

    
  

    
      
  
### 
  
    #**uncheck**([locator], **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a descendant check box and uncheck it. The check box can be found
via name, id, test_id attribute, or label text. If
no locator is provided this will match against self or a descendant.

```
# will uncheck a descendant checkbox with a name, id, or label text matching 'German'
page.uncheck('German')

# will uncheck `el` if it's a checkbox element
el.uncheck()

```

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        locator
      
      
        (String)
      
      
      
        —
        

Which check box to uncheck

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          option
          (String)
          
            
          
          
            — 

Value of the checkbox to deselect

          
        
      
        
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
          class
          (String, Array<String>, Regexp)
          
            
          
          
            — 

Match fields that match the class(es) provided

          
        
      
        
- 
          allow_label_click
          (Boolean, Hash)
          
            
          
          
            — 

Attempt to click the label to toggle state if element is non-visible. Defaults to automatic_label_click.
If set to a Hash it is passed as options to the `click` on the label

          
        
      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element unchecked or the label clicked

      
    
  

  
    
      

```

178
179
180
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 178

def uncheck(locator = nil, **options)
  _check_with_label(:checkbox, false, locator, **options)
end
```

    
  

    
      
  
### 
  
    #**unselect**(value = nil, from: nil, **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Find a select box on the page and unselect a particular option from it. If the select
box is a multiple select, #unselect can be called multiple times to unselect more than
one option. The select box can be found via its name, id, test_id attribute,
or label text.

```
page.unselect 'March', from: 'Month'

```

  

  
  
  
    

If the driver is capable of executing JavaScript, this method will wait for a set amount of time
and continuously retry finding the element until either the element is found or the time
expires. The length of time this method will wait is controlled through default_max_wait_time.

  

  

Parameters:

  
    
- 
      
        value
      
      
        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

Which option to unselect

      
    
  
    
- 
      
        from
      
      
        (String)
      
      
        *(defaults to: nil)*
      
      
        —
        

The id, test_id attribute, name or label of the select box

      
    
  

  
    
    
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          wait
          (false, true, Numeric)
          
            
          
          
            — 

Maximum time to wait for matching element to appear. Defaults to default_max_wait_time.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The option element unselected

      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

```

230
231
232
233
234
235
```

    
    
      

```
# File 'lib/capybara/node/actions.rb', line 230

def unselect(value = nil, from: nil, **options)
  raise ArgumentError, 'The :from option does not take an element' if from.is_a? Capybara::Node::Element

  scope = from ? find(:select, from, **options) : self
  scope.find(:option, value, **options).unselect_option
end
```