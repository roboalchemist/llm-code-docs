# Class: Capybara::Node::Base
  
  
  

  
  
    Inherits:
    
      Object
      
        

          
- Object
          
            
- Capybara::Node::Base
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Minitest::Expectations, Actions, Finders, Matchers
  
  
  

  

  
  
    Defined in:
    lib/capybara/node/base.rb,

  lib/capybara/minitest/spec.rb

  
  

## Overview

  
    

A Base represents either an element on a page through the subclass
Element or a document through Document.

Both types of Node share the same methods, used for interacting with the
elements on the page. These methods are divided into three categories,
finders, actions and matchers. These are found in the modules
Finders, Actions and Matchers
respectively.

A Session exposes all methods from Document directly:

```
session = Capybara::Session.new(:rack_test, my_app)
session.visit('/')
session.fill_in('Foo', with: 'Bar')    # from Capybara::Node::Actions
bar = session.find('#bar')                # from Capybara::Node::Finders
bar.select('Baz', from: 'Quox')        # from Capybara::Node::Actions
session.has_css?('#foobar')               # from Capybara::Node::Matchers

```

  

  

  
## Direct Known Subclasses

  

Document, Element

  
## Instance Attribute Summary collapse

  

    
      
- 
  
    
      #**base**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute base.

  

    
      
- 
  
    
      #**query_scope**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute query_scope.

  

    
      
- 
  
    
      #**session**  ⇒ Object 
    

    
  
  
  
  
    
      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute session.

  

    
  

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**find_css**(css, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**find_xpath**(xpath, **options)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**initialize**(session, base)  ⇒ Base 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Base.

  

      
        
- 
  
    
      #**reload**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

overridden in subclasses, e.g.

  

      
        
- 
  
    
      #**session_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      #**synchronize**(seconds = nil, errors: nil)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

This method is Capybara's primary defence against asynchronicity problems.

  

      
        
- 
  
    
      #**to_capybara_node**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
  
  
  
  
  
  
  
  
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
  
    #**initialize**(session, base)  ⇒ Base 
  

  

  

  
    

Returns a new instance of Base.

  

  

  
    
      

```

32
33
34
35
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 32

def initialize(session, base)
  @session = session
  @base = base
end

```

    
  

  

  
    
## Instance Attribute Details

    
      
      
      
  
### 
  
    #**base**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute base.

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 26

def base
  @base
end

```

    
  

    
      
      
      
  
### 
  
    #**query_scope**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute query_scope.

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 26

def query_scope
  @query_scope
end

```

    
  

    
      
      
      
  
### 
  
    #**session**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute session.

  

  

  
    
      

```

26
27
28
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 26

def session
  @session
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**find_css**(css, **options)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

106
107
108
109
110
111
112
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 106

def find_css(css, **options)
  if base.method(:find_css).arity == 1
    base.find_css(css)
  else
    base.find_css(css, **options)
  end
end

```

    
  

    
      
  
### 
  
    #**find_xpath**(xpath, **options)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

115
116
117
118
119
120
121
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 115

def find_xpath(xpath, **options)
  if base.method(:find_xpath).arity == 1
    base.find_xpath(xpath)
  else
    base.find_xpath(xpath, **options)
  end
end

```

    
  

    
      
  
### 
  
    #**reload**  ⇒ Object 
  

  

  

  
    

overridden in subclasses, e.g. Capybara::Node::Element

  

  

  
    
      

```

38
39
40
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 38

def reload
  self
end

```

    
  

    
      
  
### 
  
    #**session_options**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

  
    
      

```

124
125
126
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 124

def session_options
  session.config
end

```

    
  

    
      
  
### 
  
    #**synchronize**(seconds = nil, errors: nil)  ⇒ Object 
  

  

  

  
    

This method is Capybara's primary defence against asynchronicity
problems. It works by attempting to run a given block of code until it
succeeds. The exact behaviour of this method depends on a number of
factors. Basically there are certain exceptions which, when raised
from the block, instead of bubbling up, are caught, and the block is
re-run.

Certain drivers, such as RackTest, have no support for asynchronous
processes, these drivers run the block, and any error raised bubbles up
immediately. This allows faster turn around in the case where an
expectation fails.

Only exceptions that are ElementNotFound or any subclass
thereof cause the block to be rerun. Drivers may specify additional
exceptions which also cause reruns. This usually occurs when a node is
manipulated which no longer exists on the page. For example, the
Selenium driver specifies
`Selenium::WebDriver::Error::ObsoleteElementError`.

As long as any of these exceptions are thrown, the block is re-run,
until a certain amount of time passes. The amount of time defaults to
Capybara.default_max_wait_time and can be overridden through the `seconds`
argument. This time is compared with the system time to see how much
time has passed. On rubies/platforms which don't support access to a monotonic process clock
if the return value of `Time.now` is stubbed out, Capybara will raise `Capybara::FrozenInTime`.

  

  

Parameters:

  
    
- 
      
        seconds
      
      
        (Integer)
      
      
        *(defaults to: nil)*
      
      
        —
        

(current sessions default_max_wait_time) Maximum number of seconds to retry this block

      
    
  
    
- 
      
        errors
      
      
        (Array<Exception>)
      
      
        *(defaults to: nil)*
      
      
        —
        

(driver.invalid_element_errors +
[Capybara::ElementNotFound]) exception types that cause the block to be rerun

      
    
  

Returns:

  
    
- 
      
      
        (Object)
      
      
      
        —
        

The result of the given block

      
    
  

Raises:

  
    
- 
      
      
        (Capybara::FrozenInTime)
      
      
      
        —
        

If the return value of `Time.now` appears stuck

      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 76

def synchronize(seconds = nil, errors: nil)
  return yield if session.synchronized

  seconds = session_options.default_max_wait_time if [nil, true].include? seconds
  interval = session_options.default_retry_interval
  session.synchronized = true
  timer = Capybara::Helpers.timer(expire_in: seconds)
  begin
    yield
  rescue StandardError => e
    session.raise_server_error!
    raise e unless catch_error?(e, errors)

    if driver.wait?
      raise e if timer.expired?

      sleep interval
      reload if session_options.automatic_reload
    else
      old_base = @base
      reload if session_options.automatic_reload
      raise e if old_base == @base
    end
    retry
  ensure
    session.synchronized = false
  end
end

```

    
  

    
      
  
### 
  
    #**to_capybara_node**  ⇒ Object 
  

  

  

  
    
      

```

128
129
130
```

    
    
      

```
# File 'lib/capybara/node/base.rb', line 128

def to_capybara_node
  self
end

```