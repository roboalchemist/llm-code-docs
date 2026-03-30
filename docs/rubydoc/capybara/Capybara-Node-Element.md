# Class: Capybara::Node::Element
  
  
  

  
  
    Inherits:
    
      Base
      
        

          
- Object
          
            
- Base
          
            
- Capybara::Node::Element
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/node/element.rb
  
  

## Overview

  
    

A Element represents a single element on the page. It is possible
to interact with the contents of this element the same as with a document:

```
session = Capybara::Session.new(:rack_test, my_app)

bar = session.find('#bar')              # from Capybara::Node::Finders
bar.select('Baz', from: 'Quox')      # from Capybara::Node::Actions

```

Element also has access to HTML attributes and other properties of the
element:

```
 bar.value
 bar.text
 bar[:title]

```

  

  

  

See Also:
  

    
      
- Capybara::Node
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        STYLE_SCRIPT =
          
        
        

```
<<~JS
  (function(){
    var s = window.getComputedStyle(this);
    var result = {};
    for (var i = arguments.length; i--; ) {
      var property_name = arguments[i];
      result[property_name] = s.getPropertyValue(property_name);
    }
    return result;
  }).apply(this, arguments)
JS
```

      
    
  

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#base, #query_scope, #session

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**[]**(attribute)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Retrieve the given attribute.

  

      
        
- 
  
    
      #**allow_reload!**(idx = nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**checked?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether or not the element is checked.

  

      
        
- 
  
    
      #**click**(*modifier_keys, wait: nil, **offset)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Click the Element.

  

      
        
- 
  
    
      #**disabled?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether or not the element is disabled.

  

      
        
- 
  
    
      #**double_click**(*modifier_keys, wait: nil, **offset)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Double Click the Element.

  

      
        
- 
  
    
      #**drag_to**(node, **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Drag the element to the given other element.

  

      
        
- 
  
    
      #**drop**(*args)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Drop items on the current element.

  

      
        
- 
  
    
      #**evaluate_async_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Evaluate the given JavaScript in the context of the element and obtain the result from a callback function which will be passed as the last argument to the script.

  

      
        
- 
  
    
      #**evaluate_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Evaluate the given JS in the context of the element and return the result.

  

      
        
- 
  
    
      #**execute_script**(script, *args)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Execute the given JS in the context of the element not returning a result.

  

      
        
- 
  
    
      #**flash**  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Toggle the elements background color between white and black for a period of time.

  

      
        
- 
  
    
      #**hover**  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Hover on the Element.

  

      
        
- 
  
    
      #**initial_cache**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**initialize**(session, base, query_scope, query)  ⇒ Element 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Element.

  

      
        
- 
  
    
      #**inspect**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

A human-readable representation of the element.

  

      
        
- 
  
    
      #**multiple?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether or not the element supports multiple results.

  

      
        
- 
  
    
      #**native**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

The native element from the driver, this allows access to driver specific methods.

  

      
        
- 
  
    
      #**obscured?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether or not the element is currently in the viewport and it (or descendants) would be considered clickable at the elements center point.

  

      
        
- 
  
    
      #**path**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

An XPath expression describing where on the page the element can be found.

  

      
        
- 
  
    
      #**readonly?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether or not the element is readonly.

  

      
        
- 
  
    
      #**rect**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      #**reload**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**right_click**(*modifier_keys, wait: nil, **offset)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Right Click the Element.

  

      
        
- 
  
    
      #**scroll_to**(pos_or_el_or_x, y = nil, align: :top, offset: nil)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Scroll the page or element.

  

      
        
- 
  
    
      #**select_option**(wait: nil)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Select this node if it is an option element inside a select tag.

  

      
        
- 
  
    
      #**selected?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether or not the element is selected.

  

      
        
- 
  
    
      #**send_keys**(keys, ...)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Send Keystrokes to the Element.

  

      
        
- 
  
    
      #**set**(value, **options)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Set the value of the form element to the given value.

  

      
        
- 
  
    
      #**shadow_root**  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Return the shadow_root for the current element.

  

      
        
- 
  
    
      #**style**(*styles)  ⇒ Hash 
    

    
  
  
  
  
  
  
  
  

  
    

Retrieve the given CSS styles.

  

      
        
- 
  
    
      #**tag_name**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The tag name of the element.

  

      
        
- 
  
    
      #**text**(type = nil, normalize_ws: false)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

Retrieve the text of the element.

  

      
        
- 
  
    
      #**trigger**(event)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Trigger any event on the current element, for example mouseover or focus events.

  

      
        
- 
  
    
      #**unselect_option**(wait: nil)  ⇒ Capybara::Node::Element 
    

    
  
  
  
  
  
  
  
  

  
    

Unselect this node if it is an option element inside a multiple select tag.

  

      
        
- 
  
    
      #**value**  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

The value of the form element.

  

      
        
- 
  
    
      #**visible?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Whether or not the element is visible.

  

      
    

  

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#find_css, #find_xpath, #session_options, #synchronize, #to_capybara_node

  
  
  
  
  
  
  
  
  
### Methods included from Minitest::Expectations

  

#must_have_all_of_selectors, #must_have_ancestor, #must_have_any_of_selectors, #must_have_button, #must_have_checked_field, #must_have_content, #must_have_css, #must_have_current_path, #must_have_element, #must_have_field, #must_have_link, #must_have_none_of_selectors, #must_have_select, #must_have_selector, #must_have_sibling, #must_have_style, #must_have_table, #must_have_text, #must_have_title, #must_have_unchecked_field, #must_have_xpath, #must_match_style, #wont_have_button, #wont_have_checked_field, #wont_have_content, #wont_have_css, #wont_have_current_path, #wont_have_element, #wont_have_field, #wont_have_link, #wont_have_select, #wont_have_selector, #wont_have_table, #wont_have_text, #wont_have_title, #wont_have_unchecked_field, #wont_have_xpath

  
  
  
  
  
  
  
  
  
### Methods included from Matchers

  

#==, #assert_all_of_selectors, #assert_ancestor, #assert_any_of_selectors, #assert_matches_selector, #assert_matches_style, #assert_no_ancestor, #assert_no_selector, #assert_no_sibling, #assert_no_text, #assert_none_of_selectors, #assert_not_matches_selector, #assert_selector, #assert_sibling, #assert_style, #assert_text, #has_ancestor?, #has_button?, #has_checked_field?, #has_css?, #has_element?, #has_field?, #has_link?, #has_no_ancestor?, #has_no_button?, #has_no_checked_field?, #has_no_css?, #has_no_element?, #has_no_field?, #has_no_link?, #has_no_select?, #has_no_selector?, #has_no_sibling?, #has_no_table?, #has_no_text?, #has_no_unchecked_field?, #has_no_xpath?, #has_select?, #has_selector?, #has_sibling?, #has_style?, #has_table?, #has_text?, #has_unchecked_field?, #has_xpath?, #matches_css?, #matches_selector?, #matches_style?, #matches_xpath?, #not_matches_css?, #not_matches_selector?, #not_matches_xpath?

  
  
  
  
  
  
  
  
  
### Methods included from Actions

  

#attach_file, #check, #choose, #click_button, #click_link, #click_link_or_button, #fill_in, #select, #uncheck, #unselect

  
  
  
  
  
  
  
  
  
### Methods included from Finders

  

#all, #ancestor, #find, #find_button, #find_by_id, #find_field, #find_link, #first, #sibling

  
## Constructor Details

  
    
  
### 
  
    #**initialize**(session, base, query_scope, query)  ⇒ Element 
  

  

  

  
    

Returns a new instance of Element.

  

  

  
    
      

```

25
26
27
28
29
30
31
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 25

def initialize(session, base, query_scope, query)
  super(session, base)
  @query_scope = query_scope
  @query = query
  @allow_reload = false
  @query_idx = nil
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**[]**(attribute)  ⇒ String 
  

  

  

  
    

Retrieve the given attribute.

```
element[:title] # => HTML title attribute

```

  

  

Parameters:

  
    
- 
      
        attribute
      
      
        (Symbol)
      
      
      
        —
        

The attribute to retrieve

      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The value of the attribute

      
    
  

  
    
      

```

73
74
75
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 73

def [](attribute)
  synchronize { base[attribute] }
end
```

    
  

    
      
  
### 
  
    #**allow_reload!**(idx = nil)  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
36
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 33

def allow_reload!(idx = nil)
  @query_idx = idx
  @allow_reload = true
end
```

    
  

    
      
  
### 
  
    #**checked?**  ⇒ Boolean 
  

  

  

  
    

Whether or not the element is checked.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the element is checked

      
    
  

  
    
      

```

326
327
328
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 326

def checked?
  synchronize { base.checked? }
end
```

    
  

    
      
  
### 
  
    #**click**(*modifier_keys, wait: nil, **offset)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Click the Element.

If the driver dynamic pages (JS) and the element is currently non-interactable, this method will
continuously retry the action until either the element becomes interactable or the maximum
wait time expires.

Both x: and y: must be specified if an offset is wanted, if not specified the click will occur at the middle of the element.

  

  
  
  
    

  

  

Parameters:

  
    
- 
      
        *modifier_keys
      
      
        (:alt, :control, :meta, :shift)
      
      
      
        —
        

([]) Keys to be held down when clicking

      
    
  

  
    
    
    
    
    
    

Parameters:

  
    
- 
      
        wait
      
      
        (false, Numeric)
      
      
      
        —
        

Maximum time to wait for the action to succeed. Defaults to default_max_wait_time.

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          delay
          (Float)
          
            
          
          
            — 

Delay between the mouse down and mouse up events in seconds (0)

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

170
171
172
173
174
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 170

def click(*keys, **options)
  perform_click_action(keys, **options) do |k, opts|
    base.click(k, **opts)
  end
end
```

    
  

    
      
  
### 
  
    #**disabled?**  ⇒ Boolean 
  

  

  

  
    

Whether or not the element is disabled.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the element is disabled

      
    
  

  
    
      

```

346
347
348
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 346

def disabled?
  synchronize { base.disabled? }
end
```

    
  

    
      
  
### 
  
    #**double_click**(*modifier_keys, wait: nil, **offset)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Double Click the Element.

If the driver dynamic pages (JS) and the element is currently non-interactable, this method will
continuously retry the action until either the element becomes interactable or the maximum
wait time expires.

Both x: and y: must be specified if an offset is wanted, if not specified the click will occur at the middle of the element.

  

  
  
  
    

  

  

Parameters:

  
    
- 
      
        *modifier_keys
      
      
        (:alt, :control, :meta, :shift)
      
      
      
        —
        

([]) Keys to be held down when clicking

      
    
  

  
    
    
    
    
    
    

Parameters:

  
    
- 
      
        wait
      
      
        (false, Numeric)
      
      
      
        —
        

Maximum time to wait for the action to succeed. Defaults to default_max_wait_time.

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

197
198
199
200
201
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 197

def double_click(*keys, **options)
  perform_click_action(keys, **options) do |k, opts|
    base.double_click(k, **opts)
  end
end
```

    
  

    
      
  
### 
  
    #**drag_to**(node, **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Drag the element to the given other element.

```
source = page.find('#foo')
target = page.find('#bar')
source.drag_to(target)

```

  

  

Parameters:

  
    
- 
      
        node
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element to drag to

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

Driver specific options for dragging. May not be supported by all drivers.

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          :delay
          (Numeric)
          
            
              — default:
              0.05
            
          
          
            — 

When using Chrome/Firefox with Selenium and HTML5 dragging this is the number
of seconds between each stage of the drag.

          
        
      
        
- 
          :html5
          (Boolean)
          
            
          
          
            — 

When using Chrome/Firefox with Selenium enables to force the use of HTML5
(true) or legacy (false) dragging. If not specified the driver will attempt to
detect the correct method to use.

          
        
      
        
- 
          :drop_modifiers
          (Array<Symbol>, Symbol)
          
            
          
          
            — 

Modifier keys which should be held while the dragged element is dropped.

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The dragged element

      
    
  

  
    
      

```

418
419
420
421
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 418

def drag_to(node, **options)
  synchronize { base.drag_to(node.base, **options) }
  self
end
```

    
  

    
      
  
### 
  
    
      #**drop**(path, ...)  ⇒ Capybara::Node::Element 
    
      #**drop**(strings, ...)  ⇒ Capybara::Node::Element 
    
  

  

  

  
    

Drop items on the current element.

```
target = page.find('#foo')
target.drop('/some/path/file.csv')

```

  

  
  

Overloads:
  

    
      
      
- 
        #**drop**(path, ...)  ⇒ Capybara::Node::Element 
        
  
    

  

  

Parameters:

  
    
  - 
      
        path
      
      
        (String, #to_path)
      
      
      
        —
        

Location of the file to drop on the element

      
    
  

      
    
      
      
- 
        #**drop**(strings, ...)  ⇒ Capybara::Node::Element 
        
  
    

  

  

Parameters:

  
    
  - 
      
        strings
      
      
        (Hash)
      
      
      
        —
        

A hash of type to data to be dropped - `{ "text/url" => "https://www.google.com" }`

      
    
  

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

437
438
439
440
441
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 437

def drop(*args)
  options = args.map { |arg| arg.respond_to?(:to_path) ? arg.to_path : arg }
  synchronize { base.drop(*options) }
  self
end
```

    
  

    
      
  
### 
  
    #**evaluate_async_script**(script, *args)  ⇒ Object 
  

  

  

  
    

Evaluate the given JavaScript in the context of the element and obtain the result from a
callback function which will be passed as the last argument to the script. `this` in the
script will refer to the element this is called on.

  

  

Parameters:

  
    
- 
      
        script
      
      
        (String)
      
      
      
        —
        

A string of JavaScript to evaluate

      
    
  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

The result of the evaluated JavaScript (may be driver specific)

      
    
  

  
    
      

```

529
530
531
532
533
534
535
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 529

def evaluate_async_script(script, *args)
  session.evaluate_async_script(<<~JS, self, *args)
    (function (){
      #{script}
    }).apply(arguments[0], Array.prototype.slice.call(arguments,1));
  JS
end
```

    
  

    
      
  
### 
  
    #**evaluate_script**(script, *args)  ⇒ Object 
  

  

  

  
    

Evaluate the given JS in the context of the element and return the result. Be careful when using this with
scripts that return complex objects, such as jQuery statements. #execute_script might
be a better alternative. `this` in the script will refer to the element this is called on.

  

  

Parameters:

  
    
- 
      
        script
      
      
        (String)
      
      
      
        —
        

A string of JavaScript to evaluate

      
    
  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

The result of the evaluated JavaScript (may be driver specific)

      
    
  

  
    
      

```

512
513
514
515
516
517
518
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 512

def evaluate_script(script, *args)
  session.evaluate_script(<<~JS, self, *args)
    (function(){
      return #{script.strip}
    }).apply(arguments[0], Array.prototype.slice.call(arguments,1));
  JS
end
```

    
  

    
      
  
### 
  
    #**execute_script**(script, *args)  ⇒ Object 
  

  

  

  
    

Execute the given JS in the context of the element not returning a result. This is useful for scripts that return
complex objects, such as jQuery statements. #execute_script should be used over
#evaluate_script whenever a result is not expected or needed. `this` in the script will refer to the element this is called on.

  

  

Parameters:

  
    
- 
      
        script
      
      
        (String)
      
      
      
        —
        

A string of JavaScript to execute

      
    
  
    
- 
      
        args
      
      
        
      
      
      
        —
        

Optional arguments that will be passed to the script. Driver support for this is optional and types of objects supported may differ between drivers

      
    
  

  
    
      

```

495
496
497
498
499
500
501
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 495

def execute_script(script, *args)
  session.execute_script(<<~JS, self, *args)
    (function (){
      #{script}
    }).apply(arguments[0], Array.prototype.slice.call(arguments,1));
  JS
end
```

    
  

    
      
  
### 
  
    #**flash**  ⇒ Capybara::Node::Element 
  

  

  

  
    

Toggle the elements background color between white and black for a period of time.

  

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 542

def flash
  execute_script(<<~JS, 100)
    async function flash(el, delay){
      var old_bg = el.style.backgroundColor;
      var colors = ["black", "white"];
      for(var i=0; i<20; i++){
        el.style.backgroundColor = colors[i % colors.length];
        await new Promise(resolve => setTimeout(resolve, delay));
      }
      el.style.backgroundColor = old_bg;
    }
    flash(this, arguments[0]);
  JS

  self
end
```

    
  

    
      
  
### 
  
    #**hover**  ⇒ Capybara::Node::Element 
  

  

  

  
    

Hover on the Element.

  

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

284
285
286
287
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 284

def hover
  synchronize { base.hover }
  self
end
```

    
  

    
      
  
### 
  
    #**initial_cache**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

586
587
588
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 586

def initial_cache
  base.respond_to?(:initial_cache) ? base.initial_cache : {}
end
```

    
  

    
      
  
### 
  
    #**inspect**  ⇒ String 
  

  

  

  
    

A human-readable representation of the element.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

A string representation

      
    
  

  
    
      

```

577
578
579
580
581
582
583
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 577

def inspect
  %(#<Capybara::Node::Element tag="#{base.tag_name}" path="#{base.path}">)
rescue NotSupportedByDriverError
  %(#<Capybara::Node::Element tag="#{base.tag_name}">)
rescue *session.driver.invalid_element_errors
  %(Obsolete #<Capybara::Node::Element>)
end
```

    
  

    
      
  
### 
  
    #**multiple?**  ⇒ Boolean 
  

  

  

  
    

Whether or not the element supports multiple results.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the element supports multiple results.

      
    
  

  
    
      

```

366
367
368
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 366

def multiple?
  synchronize { base.multiple? }
end
```

    
  

    
      
  
### 
  
    #**native**  ⇒ Object 
  

  

  

  
    

Returns The native element from the driver, this allows access to driver specific methods.

  

  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

The native element from the driver, this allows access to driver specific methods

      
    
  

  
    
      

```

42
43
44
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 42

def native
  synchronize { base.native }
end
```

    
  

    
      
  
### 
  
    #**obscured?**  ⇒ Boolean 
  

  

  

  
    

Whether or not the element is currently in the viewport and it (or descendants)
would be considered clickable at the elements center point.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the elements center is obscured.

      
    
  

  
    
      

```

316
317
318
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 316

def obscured?
  synchronize { base.obscured? }
end
```

    
  

    
      
  
### 
  
    #**path**  ⇒ String 
  

  

  

  
    

An XPath expression describing where on the page the element can be found.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

An XPath expression

      
    
  

  
    
      

```

376
377
378
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 376

def path
  synchronize { base.path }
end
```

    
  

    
      
  
### 
  
    #**readonly?**  ⇒ Boolean 
  

  

  

  
    

Whether or not the element is readonly.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the element is readonly

      
    
  

  
    
      

```

356
357
358
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 356

def readonly?
  synchronize { base.readonly? }
end
```

    
  

    
      
  
### 
  
    #**rect**  ⇒ Object 
  

  

  

  
    
      

```

380
381
382
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 380

def rect
  synchronize { base.rect }
end
```

    
  

    
      
  
### 
  
    #**reload**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

560
561
562
563
564
565
566
567
568
569
570
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 560

def reload
  return self unless @allow_reload

  begin
    reloaded = @query.resolve_for(query_scope ? query_scope.reload : session)[@query_idx.to_i]
    @base = reloaded.base if reloaded
  rescue StandardError => e
    raise e unless catch_error?(e)
  end
  self
end
```

    
  

    
      
  
### 
  
    #**right_click**(*modifier_keys, wait: nil, **offset)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Right Click the Element.

If the driver dynamic pages (JS) and the element is currently non-interactable, this method will
continuously retry the action until either the element becomes interactable or the maximum
wait time expires.

Both x: and y: must be specified if an offset is wanted, if not specified the click will occur at the middle of the element.

  

  
  
  
    

  

  

Parameters:

  
    
- 
      
        *modifier_keys
      
      
        (:alt, :control, :meta, :shift)
      
      
      
        —
        

([]) Keys to be held down when clicking

      
    
  

  
    
    
    
    
    
    

Parameters:

  
    
- 
      
        wait
      
      
        (false, Numeric)
      
      
      
        —
        

Maximum time to wait for the action to succeed. Defaults to default_max_wait_time.

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

a customizable set of options

      
    
  

  
    
    
    
    
    

Options Hash (**options):
    

      
        
- 
          delay
          (Float)
          
            
          
          
            — 

Delay between the mouse down and mouse up events in seconds (0)

          
        
      
    

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

184
185
186
187
188
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 184

def right_click(*keys, **options)
  perform_click_action(keys, **options) do |k, opts|
    base.right_click(k, **opts)
  end
end
```

    
  

    
      
  
### 
  
    
      #**scroll_to**(position, offset: [0,0])  ⇒ Capybara::Node::Element 
    
      #**scroll_to**(element, align: :top)  ⇒ Capybara::Node::Element 
    
      #**scroll_to**(x, y)  ⇒ Capybara::Node::Element 
    
  

  

  

  
    

Scroll the page or element.

  

  
  

Overloads:
  

    
      
      
- 
        #**scroll_to**(position, offset: [0,0])  ⇒ Capybara::Node::Element 
        
  
    

Scroll the page or element to its top, bottom or middle.

  

  

Parameters:

  
    
  - 
      
        position
      
      
        (:top, :bottom, :center, :current)
      
      
      
    
  
    
  - 
      
        offset
      
      
        ([Integer, Integer])
      
      
        *(defaults to: [0,0])*
      
      
    
  

      
    
      
      
- 
        #**scroll_to**(element, align: :top)  ⇒ Capybara::Node::Element 
        
  
    

Scroll the page or current element until the given element is aligned at the top, bottom, or center of it.

  

  

Parameters:

  
    
  - 
      
        element
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element to be scrolled into view

      
    
  
    
  - 
      
        align
      
      
        (:top, :bottom, :center)
      
      
        *(defaults to: :top)*
      
      
        —
        

Where to align the element being scrolled into view with relation to the current page/element if possible

      
    
  

      
    
      
      
- 
        #**scroll_to**(x, y)  ⇒ Capybara::Node::Element 
        
  
    

  

  

Parameters:

  
    
  - 
      
        x
      
      
        (Integer)
      
      
      
        —
        

Horizontal scroll offset

      
    
  
    
  - 
      
        y
      
      
        (Integer)
      
      
      
        —
        

Vertical scroll offset

      
    
  

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

462
463
464
465
466
467
468
469
470
471
472
473
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 462

def scroll_to(pos_or_el_or_x, y = nil, align: :top, offset: nil)
  case pos_or_el_or_x
  when Symbol
    synchronize { base.scroll_to(nil, pos_or_el_or_x) } unless pos_or_el_or_x == :current
  when Capybara::Node::Element
    synchronize { base.scroll_to(pos_or_el_or_x.base, align) }
  else
    synchronize { base.scroll_to(nil, nil, [pos_or_el_or_x, y]) }
  end
  synchronize { base.scroll_by(*offset) } unless offset.nil?
  self
end
```

    
  

    
      
  
### 
  
    #**select_option**(wait: nil)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Select this node if it is an option element inside a select tag.

If the driver dynamic pages (JS) and the element is currently non-interactable, this method will
continuously retry the action until either the element becomes interactable or the maximum
wait time expires.

  

  

Parameters:

  
    
- 
      
        wait
      
      
        (false, Numeric)
      
      
        *(defaults to: nil)*
      
      
        —
        

Maximum time to wait for the action to succeed. Defaults to default_max_wait_time.

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

139
140
141
142
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 139

def select_option(wait: nil)
  synchronize(wait) { base.select_option }
  self
end
```

    
  

    
      
  
### 
  
    #**selected?**  ⇒ Boolean 
  

  

  

  
    

Whether or not the element is selected.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the element is selected

      
    
  

  
    
      

```

336
337
338
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 336

def selected?
  synchronize { base.selected? }
end
```

    
  

    
      
  
### 
  
    #**send_keys**(keys, ...)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Send Keystrokes to the Element.

Examples:

```
element.send_keys "foo"                     #=> value: 'foo'
element.send_keys "tet", :left, "s"         #=> value: 'test'
element.send_keys [:control, 'a'], :space   #=> value: ' ' - assuming ctrl-a selects all contents

```

Symbols supported for keys:

- :cancel

- :help

- :backspace

- :tab

- :clear

- :return

- :enter

- :shift

- :control

- :alt

- :pause

- :escape

- :space

- :page_up

- :page_down

- :end

- :home

- :left

- :up

- :right

- :down

- :insert

- :delete

- :semicolon

- :equals

- :numpad0

- :numpad1

- :numpad2

- :numpad3

- :numpad4

- :numpad5

- :numpad6

- :numpad7

- :numpad8

- :numpad9

- :multiply      - numeric keypad *

- :add           - numeric keypad +

- :separator     - numeric keypad 'separator' key ??

- :subtract      - numeric keypad -

- :decimal       - numeric keypad .

- :divide        - numeric keypad /

- :f1

- :f2

- :f3

- :f4

- :f5

- :f6

- :f7

- :f8

- :f9

- :f10

- :f11

- :f12

- :meta

- :command      - alias of :meta

  

  
  
  
    

  

  

Parameters:

  
    
- 
      
        keys
      
      
        (String, Symbol, Array<String,Symbol>)
      
      
      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

274
275
276
277
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 274

def send_keys(*args)
  synchronize { base.send_keys(*args) }
  self
end
```

    
  

    
      
  
### 
  
    #**set**(value, **options)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Set the value of the form element to the given value.

  

  

Parameters:

  
    
- 
      
        value
      
      
        (String)
      
      
      
        —
        

The new value

      
    
  
    
- 
      
        options
      
      
        (Hash)
      
      
      
        —
        

Driver specific options for how to set the value. Take default values from default_set_options.

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

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
# File 'lib/capybara/node/element.rb', line 117

def set(value, **options)
  if ENV.fetch('CAPYBARA_THOROUGH', nil) && readonly?
    raise Capybara::ReadOnlyElementError, "Attempt to set readonly element with value: #{value}"
  end

  options = session_options.default_set_options.to_h.merge(options)
  synchronize { base.set(value, **options) }
  self
end
```

    
  

    
      
  
### 
  
    #**shadow_root**  ⇒ Capybara::Node::Element 
  

  

  

  
    

Return the shadow_root for the current element

  

  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The shadow root

      
    
  

  
    
      

```

481
482
483
484
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 481

def shadow_root
  root = synchronize { base.shadow_root }
  root && Capybara::Node::Element.new(session, root, nil, nil)
end
```

    
  

    
      
  
### 
  
    #**style**(*styles)  ⇒ Hash 
  

  

  

  
    

Retrieve the given CSS styles.

```
element.style('color', 'font-size') # => Computed values of CSS 'color' and 'font-size' styles

```

  

  

Parameters:

  
    
- 
      
        styles
      
      
        (Array<String>)
      
      
      
        —
        

Names of the desired CSS properties

      
    
  

Returns:

  
    
- 
      
      
        (Hash)
      
      
      
        —
        

Hash of the CSS property names to computed values

      
    
  

Raises:

  
    
- 
      
      
        (ArgumentError)
      
      
      
    
  

  
    
      

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
96
97
98
99
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 86

def style(*styles)
  styles = styles.flatten.map(&:to_s)
  raise ArgumentError, 'You must specify at least one CSS style' if styles.empty?

  begin
    synchronize { base.style(styles) }
  rescue NotImplementedError => e
    begin
      evaluate_script(STYLE_SCRIPT, *styles)
    rescue Capybara::NotSupportedByDriverError
      raise e
    end
  end
end
```

    
  

    
      
  
### 
  
    #**tag_name**  ⇒ String 
  

  

  

  
    

Returns The tag name of the element.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The tag name of the element

      
    
  

  
    
      

```

293
294
295
296
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 293

def tag_name
  # Element type is immutable so cache it
  @tag_name ||= initial_cache[:tag_name] || synchronize { base.tag_name }
end
```

    
  

    
      
  
### 
  
    #**text**(type = nil, normalize_ws: false)  ⇒ String 
  

  

  

  
    

Retrieve the text of the element. If ignore_hidden_elements
is `true`, which it is by default, then this will return only text
which is visible. The exact semantics of this may differ between
drivers, but generally any text within elements with `display:none` is
ignored. This behaviour can be overridden by passing `:all` to this
method.

  

  

Parameters:

  
    
- 
      
        type
      
      
        (:all, :visible)
      
      
        *(defaults to: nil)*
      
      
        —
        

Whether to return only visible or all text

      
    
  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The text of the element

      
    
  

  
    
      

```

58
59
60
61
62
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 58

def text(type = nil, normalize_ws: false)
  type ||= :all unless session_options.ignore_hidden_elements || session_options.visible_text_only
  txt = synchronize { type == :all ? base.all_text : base.visible_text }
  normalize_ws ? txt.gsub(/[[:space:]]+/, ' ').strip : txt
end
```

    
  

    
      
  
### 
  
    #**trigger**(event)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Trigger any event on the current element, for example mouseover or focus
events. Not supported with the Selenium driver, and SHOULDN'T BE USED IN TESTING unless you
fully understand why you're using it, that it can allow actions a user could never
perform, and that it may completely invalidate your test.

  

  

Parameters:

  
    
- 
      
        event
      
      
        (String)
      
      
      
        —
        

The name of the event to trigger

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

394
395
396
397
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 394

def trigger(event)
  synchronize { base.trigger(event) }
  self
end
```

    
  

    
      
  
### 
  
    #**unselect_option**(wait: nil)  ⇒ Capybara::Node::Element 
  

  

  

  
    

Unselect this node if it is an option element inside a multiple select tag.

If the driver dynamic pages (JS) and the element is currently non-interactable, this method will
continuously retry the action until either the element becomes interactable or the maximum
wait time expires.

  

  

Parameters:

  
    
- 
      
        wait
      
      
        (false, Numeric)
      
      
        *(defaults to: nil)*
      
      
        —
        

Maximum time to wait for the action to succeed. Defaults to default_max_wait_time.

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Element)
      
      
      
        —
        

The element

      
    
  

  
    
      

```

150
151
152
153
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 150

def unselect_option(wait: nil)
  synchronize(wait) { base.unselect_option }
  self
end
```

    
  

    
      
  
### 
  
    #**value**  ⇒ String 
  

  

  

  
    

Returns The value of the form element.

  

  

Returns:

  
    
- 
      
      
        (String)
      
      
      
        —
        

The value of the form element

      
    
  

  
    
      

```

105
106
107
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 105

def value
  synchronize { base.value }
end
```

    
  

    
      
  
### 
  
    #**visible?**  ⇒ Boolean 
  

  

  

  
    

Whether or not the element is visible. Not all drivers support CSS, so
the result may be inaccurate.

  

  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
        —
        

Whether the element is visible

      
    
  

  
    
      

```

305
306
307
```

    
    
      

```
# File 'lib/capybara/node/element.rb', line 305

def visible?
  synchronize { base.visible? }
end
```