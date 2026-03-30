# Module: Capybara
  
  
  

  

  
  
  
      Extended by:
      DSL, Forwardable
  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara.rb,

  lib/capybara/dsl.rb,
 lib/capybara/config.rb,
 lib/capybara/result.rb,
 lib/capybara/server.rb,
 lib/capybara/window.rb,
 lib/capybara/helpers.rb,
 lib/capybara/session.rb,
 lib/capybara/version.rb,
 lib/capybara/minitest.rb,
 lib/capybara/node/base.rb,
 lib/capybara/driver/node.rb,
 lib/capybara/node/simple.rb,
 lib/capybara/node/actions.rb,
 lib/capybara/node/element.rb,
 lib/capybara/node/finders.rb,
 lib/capybara/selector/css.rb,
 lib/capybara/minitest/spec.rb,
 lib/capybara/node/document.rb,
 lib/capybara/node/matchers.rb,
 lib/capybara/rspec/matchers.rb,
 lib/capybara/server/checker.rb,
 lib/capybara/session/config.rb,
 lib/capybara/session/matchers.rb,
 lib/capybara/spec/spec_helper.rb,
 lib/capybara/selector/selector.rb,
 lib/capybara/server/middleware.rb,
 lib/capybara/queries/base_query.rb,
 lib/capybara/queries/text_query.rb,
 lib/capybara/queries/match_query.rb,
 lib/capybara/queries/style_query.rb,
 lib/capybara/queries/title_query.rb,
 lib/capybara/rspec/matchers/base.rb,
 lib/capybara/selector/definition.rb,
 lib/capybara/selector/filter_set.rb,
 lib/capybara/queries/sibling_query.rb,
 lib/capybara/rspec/matcher_proxies.rb,
 lib/capybara/selector/filters/base.rb,
 lib/capybara/selenium/patches/logs.rb,
 lib/capybara/node/document_matchers.rb,
 lib/capybara/queries/ancestor_query.rb,
 lib/capybara/queries/selector_query.rb,
 lib/capybara/registration_container.rb,
 lib/capybara/rspec/matchers/compound.rb,
 lib/capybara/rspec/matchers/have_text.rb,
 lib/capybara/selenium/extensions/find.rb,
 lib/capybara/rspec/matchers/have_title.rb,
 lib/capybara/server/animation_disabler.rb,
 lib/capybara/node/whitespace_normalizer.rb,
 lib/capybara/queries/current_path_query.rb,
 lib/capybara/rspec/matchers/count_sugar.rb,
 lib/capybara/rspec/matchers/match_style.rb,
 lib/capybara/rspec/matchers/match_style.rb,
 lib/capybara/selenium/extensions/scroll.rb,
 lib/capybara/rspec/matchers/have_sibling.rb,
 lib/capybara/queries/active_element_query.rb,
 lib/capybara/rspec/matchers/become_closed.rb,
 lib/capybara/rspec/matchers/have_ancestor.rb,
 lib/capybara/rspec/matchers/have_selector.rb,
 lib/capybara/rspec/matchers/spatial_sugar.rb,
 lib/capybara/selector/filters/node_filter.rb,
 lib/capybara/selector/regexp_disassembler.rb,
 lib/capybara/rspec/matchers/match_selector.rb,
 lib/capybara/selector/builders/css_builder.rb,
 lib/capybara/selenium/patches/is_displayed.rb,
 lib/capybara/selector/builders/xpath_builder.rb,
 lib/capybara/selector/filters/locator_filter.rb,
 lib/capybara/rspec/matchers/have_current_path.rb,
 lib/capybara/selector/filters/expression_filter.rb,
 lib/capybara/selenium/patches/persistent_client.rb

  
  

## Defined Under Namespace

  
    
      **Modules:** DSL, DSLRSpecProxyInstaller, Driver, Helpers, Minitest, Node, Queries, RSpecMatcherProxies, RSpecMatcherProxyInstaller, RSpecMatchers, RackTest, Selenium, SessionMatchers, SpecHelper
    
  
    
      **Classes:** Ambiguous, CapybaraError, Config, DriverNotFoundError, ElementNotFound, ExpectationNotMet, FileNotFound, FrozenInTime, InfiniteRedirectError, ModalNotFound, NotSupportedByDriverError, ReadOnlyElementError, ReadOnlySessionConfig, RegistrationContainer, Result, ScopeError, Selector, Server, Session, SessionConfig, UnselectNotAllowed, Window, WindowError
    
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        VERSION =
          
        
        

```
'3.40.0'
```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**add_selector**(name, **options) { ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Add a new selector to Capybara.

  

      
        
- 
  
    
      .**always_include_port**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**app**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**app_host**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**configure** {|config| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Configure Capybara to suit your needs.

  

      
        
- 
  
    
      .**current_driver**  ⇒ Symbol 
    

    
      (also: mode)
    
  
  
  
  
  
  
  
  

  
    

The name of the driver currently in use.

  

      
        
- 
  
    
      .**current_driver=**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**current_session**  ⇒ Capybara::Session 
    

    
  
  
  
  
  
  
  
  

  
    

The current Session based on what is set as Capybara.app and Capybara.current_driver.

  

      
        
- 
  
    
      .**default_driver**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**default_max_wait_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**default_selector**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**drivers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**HTML**(html)  ⇒ Nokogiri::HTML::Document 
    

    
  
  
  
  
  
  
  
  

  
    

Parse raw html into a document using Nokogiri, and adjust textarea contents as defined by the spec.

  

      
        
- 
  
    
      .**javascript_driver**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**modify_selector**(name) { ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Modify a selector previously created by Capybara.add_selector.

  

      
        
- 
  
    
      .**register_driver**(name) {|app| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a new driver for Capybara.

  

      
        
- 
  
    
      .**register_server**(name) {|app, port, host| ... } ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Register a new server for Capybara.

  

      
        
- 
  
    
      .**reset_sessions!**  ⇒ Object 
    

    
      (also: reset!)
    
  
  
  
  
  
  
  
  

  
    

Reset sessions, cleaning out the pool of sessions.

  

      
        
- 
  
    
      .**reuse_server**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**run_default_server**(app, port)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Runs Capybara's default server for the given application and port under most circumstances you should not have to call this method manually.

  

      
        
- 
  
    
      .**server**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**servers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**session_name**  ⇒ Symbol 
    

    
  
  
  
  
  
  
  
  

  
    

The current session name.

  

      
        
- 
  
    
      .**session_name=**(name)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**session_options**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
- 
  
    
      .**string**(html)  ⇒ Capybara::Node::Simple 
    

    
  
  
  
  
  
  
  
  

  
    

Wraps the given string, which should contain an HTML document or fragment in a Node::Simple which exposes all Node::Matchers, Node::Finders and Node::DocumentMatchers.

  

      
        
- 
  
    
      .**threadsafe**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**use_default_driver**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Use the default driver as the current driver.

  

      
        
- 
  
    
      .**use_html5_parsing**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

See Capybara.configure.

  

      
        
- 
  
    
      .**using_driver**(driver)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Yield a block using a specific driver.

  

      
        
- 
  
    
      .**using_session**(name_or_session, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Yield a block using a specific session name or Session instance.

  

      
        
- 
  
    
      .**using_wait_time**(seconds)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Yield a block using a specific wait time.

  

      
    

  

  
  
  
  
  
  
  
  
  
  
### Methods included from DSL

  

extended, included, page, using_session, using_wait_time

  
  
  
  
  
  
  
  
  
### Methods included from DSLRSpecProxyInstaller

  

prepended

  
    
## Class Method Details

    
      
  
### 
  
    .**add_selector**(name, **options) { ... } ⇒ Object 
  

  

  

  
    

Add a new selector to Capybara. Selectors can be used by various methods in Capybara
to find certain elements on the page in a more convenient way. For example adding a
selector to find certain table rows might look like this:

```
Capybara.add_selector(:row) do
  xpath { |num| ".//tbody/tr[#{num}]" }
end

```

This makes it possible to use this selector in a variety of ways:

```
find(:row, 3)
page.find('table#myTable').find(:row, 3).text
page.find('table#myTable').has_selector?(:row, 3)
within(:row, 3) { expect(page).to have_content('$100.000') }

```

Here is another example:

```
Capybara.add_selector(:id) do
  xpath { |id| XPath.descendant[XPath.attr(:id) == id.to_s] }
end

```

Note that this particular selector already ships with Capybara.

  

  

Parameters:

  
    
- 
      
        name
      
      
        (Symbol)
      
      
      
        —
        

The name of the selector to add

      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
        
        

A block executed in the context of the new Selector

      
    
  

  
    
      

```

182
183
184
```

    
    
      

```
# File 'lib/capybara.rb', line 182

def add_selector(name, **options, &block)
  Capybara::Selector.add(name, **options, &block)
end
```

    
  

    
      
  
### 
  
    .**always_include_port**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/capybara.rb', line 57

SessionConfig::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**app**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara.rb', line 44

Config::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**app_host**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/capybara.rb', line 57

SessionConfig::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**configure** {|config| ... } ⇒ Object 
  

  

  

  
    

Configure Capybara to suit your needs.

```
Capybara.configure do |config|
  config.run_server = false
  config.app_host   = 'http://www.google.com'
end

```

#### Configurable options

- **use_html5_parsing** (Boolean = `false`) - When Nokogiri >= 1.12.0 or `nokogumbo` is installed, whether HTML5 parsing will be used for HTML strings.

- **always_include_port** (Boolean = `false`) - Whether the Rack server's port should automatically be inserted into every visited URL
unless another port is explicitly specified.

- **app_host** (String, `nil`) - The default host to use when giving a relative URL to visit, must be a valid URL e.g. `http://www.example.com`.

- **asset_host** (String = `nil`) - Where dynamic assets are hosted - will be prepended to relative asset locations if present.

- **automatic_label_click** (Boolean = `false`) - Whether Element#choose, Element#check,
Element#uncheck will attempt to click the associated `<label>` element if the checkbox/radio button are non-visible.

- **automatic_reload** (Boolean = `true`) - Whether to automatically reload elements as Capybara is waiting.

- **default_max_wait_time** (Numeric = `2`) - The maximum number of seconds to wait for asynchronous processes to finish.

- **default_normalize_ws** (Boolean = `false`) - Whether text predicates and matchers use normalize whitespace behavior.

- **default_retry_interval** (Numeric = `0.01`) - The number of seconds to delay the next check in asynchronous processes.

- **default_selector** (`:css`, `:xpath` = `:css`) - Methods which take a selector use the given type by default. See also Selector.

- **default_set_options** (Hash = `{}`) - The default options passed to Element#set.

- **enable_aria_label** (Boolean = `false`) - Whether fields, links, and buttons will match against `aria-label` attribute.

- **enable_aria_role** (Boolean = `false`) - Selectors will check for relevant aria role (currently only `button`).

- **exact** (Boolean = `false`) - Whether locators are matched exactly or with substrings. Only affects selector conditions
written using the `XPath#is` method.

- **exact_text** (Boolean = `false`) - Whether the text matchers and `:text` filter match exactly or on substrings.

- **ignore_hidden_elements** (Boolean = `true`) - Whether to ignore hidden elements on the page.

- **match** (`:one`, `:first`, `:prefer_exact`, `:smart` = `:smart`) - The matching strategy to find nodes.

- **predicates_wait** (Boolean = `true`) - Whether Capybara's predicate matchers use waiting behavior by default.

- **raise_server_errors** (Boolean = `true`) - Should errors raised in the server be raised in the tests?

- **reuse_server** (Boolean = `true`) - Whether to reuse the server thread between multiple sessions using the same app object.

- **run_server** (Boolean = `true`) - Whether to start a Rack server for the given Rack app.

- **save_path** (String = `Dir.pwd`) - Where to put pages saved through save_page, save_screenshot,
save_and_open_page, or save_and_open_screenshot.

- **server** (Symbol = `:default` (which uses puma)) - The name of the registered server to use when running the app under test.

- **server_port** (Integer) - The port Capybara will run the application server on, if not specified a random port will be used.

- **server_host** (String = "127.0.0.1") - The IP address Capybara will bind the application server to. If the test application is to be accessed from an external host, you will want to change this to "0.0.0.0" or to a more specific IP address that your test client can reach.

- **server_errors** (Array<Class> = `[Exception]`) - Error classes that should be raised in the tests if they are raised in the server
and raise_server_errors is `true`.

- **test_id** (Symbol, String, `nil` = `nil`) - Optional attribute to match locator against with built-in selectors along with id.

- **threadsafe** (Boolean = `false`) - Whether sessions can be configured individually.

- **w3c_click_offset** (Boolean = 'true') - Whether click offsets should be from element center (true) or top left (false)

#### DSL Options

When using `capybara/dsl`, the following options are also available:

- **default_driver** (Symbol = `:rack_test`) - The name of the driver to use by default.

- **javascript_driver** (Symbol = `:selenium`) - The name of a driver to use for JavaScript enabled tests.

  

  

Yields:

  
    
- 
      
      
        (config)
      
      
      
    
  

  
    
      

```

114
115
116
```

    
    
      

```
# File 'lib/capybara.rb', line 114

def configure
  yield config
end
```

    
  

    
      
  
### 
  
    .**current_driver**  ⇒ Symbol 
  

  
    Also known as:
    mode
    
  

  

  
    

Returns The name of the driver currently in use.

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
        —
        

The name of the driver currently in use

      
    
  

  
    
      

```

261
262
263
264
265
266
267
```

    
    
      

```
# File 'lib/capybara.rb', line 261

def current_driver
  if threadsafe
    Thread.current.thread_variable_get :capybara_current_driver
  else
    @current_driver
  end || default_driver
end
```

    
  

    
      
  
### 
  
    .**current_driver=**(name)  ⇒ Object 
  

  

  

  
    
      

```

270
271
272
273
274
275
276
```

    
    
      

```
# File 'lib/capybara.rb', line 270

def current_driver=(name)
  if threadsafe
    Thread.current.thread_variable_set :capybara_current_driver, name
  else
    @current_driver = name
  end
end
```

    
  

    
      
  
### 
  
    .**current_session**  ⇒ Capybara::Session 
  

  

  

  
    

The current Session based on what is set as app and current_driver.

  

  

Returns:

  
    
- 
      
      
        (Capybara::Session)
      
      
      
        —
        

The currently used session

      
    
  

  
    
      

```

316
317
318
```

    
    
      

```
# File 'lib/capybara.rb', line 316

def current_session
  specified_session || session_pool["#{current_driver}:#{session_name}:#{app.object_id}"]
end
```

    
  

    
      
  
### 
  
    .**default_driver**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara.rb', line 44

Config::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**default_max_wait_time**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/capybara.rb', line 57

SessionConfig::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**default_selector**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

57
58
59
```

    
    
      

```
# File 'lib/capybara.rb', line 57

SessionConfig::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**drivers**  ⇒ Object 
  

  

  

  
    
      

```

204
205
206
```

    
    
      

```
# File 'lib/capybara.rb', line 204

def drivers
  @drivers ||= RegistrationContainer.new
end
```

    
  

    
      
  
### 
  
    .**HTML**(html)  ⇒ Nokogiri::HTML::Document 
  

  

  

  
    

Parse raw html into a document using Nokogiri, and adjust textarea contents as defined by the spec.

  

  

Parameters:

  
    
- 
      
        html
      
      
        (String)
      
      
      
        —
        

The raw html

      
    
  

Returns:

  
    
- 
      
      
        (Nokogiri::HTML::Document)
      
      
      
        —
        

HTML document

      
    
  

  
    
      

```

390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
```

    
    
      

```
# File 'lib/capybara.rb', line 390

def HTML(html) # rubocop:disable Naming/MethodName
  # Nokogiri >= 1.12.0 or Nokogumbo installed and allowed for use
  html_parser, using_html5 = if defined?(Nokogiri::HTML5) && Capybara.use_html5_parsing
    [Nokogiri::HTML5, true]
  else
    [defined?(Nokogiri::HTML4) ? Nokogiri::HTML4 : Nokogiri::HTML, false]
  end

  html_parser.parse(html).tap do |document|
    document.xpath('//template').each do |template|
      # template elements content is not part of the document
      template.inner_html = ''
    end
    document.xpath('//textarea').each do |textarea|
      # The Nokogiri HTML5 parser already returns spec compliant contents
      textarea['_capybara_raw_value'] = using_html5 ? textarea.content : textarea.content.delete_prefix("\n")
    end
  end
end
```

    
  

    
      
  
### 
  
    .**javascript_driver**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara.rb', line 44

Config::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**modify_selector**(name) { ... } ⇒ Object 
  

  

  

  
    

Modify a selector previously created by add_selector.
For example, adding a new filter to the :button selector to filter based on
button style (a class) might look like this

```
Capybara.modify_selector(:button) do
  filter (:btn_style, valid_values: [:primary, :secondary]) { |node, style| node[:class].split.include? "btn-#{style}" }
end

```

  

  

Parameters:

  
    
- 
      
        name
      
      
        (Symbol)
      
      
      
        —
        

The name of the selector to modify

      
    
  

Yields:

  
    
- 
      
      
        
      
      
      
        
        

A block executed in the context of the existing Selector

      
    
  

  
    
      

```

200
201
202
```

    
    
      

```
# File 'lib/capybara.rb', line 200

def modify_selector(name, &block)
  Capybara::Selector.update(name, &block)
end
```

    
  

    
      
  
### 
  
    .**register_driver**(name) {|app| ... } ⇒ Object 
  

  

  

  
    

Register a new driver for Capybara.

```
Capybara.register_driver :rack_test do |app|
  Capybara::RackTest::Driver.new(app)
end

```

  

  

Parameters:

  
    
- 
      
        name
      
      
        (Symbol)
      
      
      
        —
        

The name of the new driver

      
    
  

Yields:

  
    
- 
      
      
        (app)
      
      
      
        —
        

This block takes a rack app and returns a Capybara driver

      
    
  

Yield Parameters:

  
    
- 
      
        app
      
      
        (<Rack>)
      
      
      
        —
        

The rack application that this driver runs against. May be nil.

      
    
  

Yield Returns:

  
    
- 
      
      
        (Capybara::Driver::Base)
      
      
      
        —
        

A Capybara driver instance

      
    
  

  
    
      

```

131
132
133
```

    
    
      

```
# File 'lib/capybara.rb', line 131

def register_driver(name, &block)
  drivers.send(:register, name, block)
end
```

    
  

    
      
  
### 
  
    .**register_server**(name) {|app, port, host| ... } ⇒ Object 
  

  

  

  
    

Register a new server for Capybara.

```
Capybara.register_server :webrick do |app, port, host|
  require 'rack/handler/webrick'
  Rack::Handler::WEBrick.run(app, ...)
end

```

  

  

Parameters:

  
    
- 
      
        name
      
      
        (Symbol)
      
      
      
        —
        

The name of the new driver

      
    
  

Yields:

  
    
- 
      
      
        (app, port, host)
      
      
      
        —
        

This block takes a rack app and a port and returns a rack server listening on that port

      
    
  

Yield Parameters:

  
    
- 
      
        app
      
      
        (<Rack>)
      
      
      
        —
        

The rack application that this server will contain.

      
    
  
    
- 
      
        port
      
      
        
      
      
      
        —
        

The port number the server should listen on

      
    
  
    
- 
      
        host
      
      
        
      
      
      
        —
        

The host/ip to bind to

      
    
  

  
    
      

```

150
151
152
```

    
    
      

```
# File 'lib/capybara.rb', line 150

def register_server(name, &block)
  servers.send(:register, name.to_sym, block)
end
```

    
  

    
      
  
### 
  
    .**reset_sessions!**  ⇒ Object 
  

  
    Also known as:
    reset!
    
  

  

  
    

Reset sessions, cleaning out the pool of sessions. This will remove any session information such
as cookies.

  

  

  
    
      

```

325
326
327
328
```

    
    
      

```
# File 'lib/capybara.rb', line 325

def reset_sessions!
  # reset in reverse so sessions that started servers are reset last
  session_pool.reverse_each { |_mode, session| session.reset! }
end
```

    
  

    
      
  
### 
  
    .**reuse_server**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara.rb', line 44

Config::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**run_default_server**(app, port)  ⇒ Object 
  

  

  

  
    

Runs Capybara's default server for the given application and port
under most circumstances you should not have to call this method
manually.

  

  

Parameters:

  
    
- 
      
        app
      
      
        (Rack Application)
      
      
      
        —
        

The rack application to run

      
    
  
    
- 
      
        port
      
      
        (Integer)
      
      
      
        —
        

The port to run the application on

      
    
  

  
    
      

```

253
254
255
```

    
    
      

```
# File 'lib/capybara.rb', line 253

def run_default_server(app, port)
  servers[:puma].call(app, port, server_host)
end
```

    
  

    
      
  
### 
  
    .**server**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara.rb', line 44

Config::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**servers**  ⇒ Object 
  

  

  

  
    
      

```

208
209
210
```

    
    
      

```
# File 'lib/capybara.rb', line 208

def servers
  @servers ||= RegistrationContainer.new
end
```

    
  

    
      
  
### 
  
    .**session_name**  ⇒ Symbol 
  

  

  

  
    

The current session name.

  

  

Returns:

  
    
- 
      
      
        (Symbol)
      
      
      
        —
        

The name of the currently used session.

      
    
  

  
    
      

```

337
338
339
340
341
342
343
344
```

    
    
      

```
# File 'lib/capybara.rb', line 337

def session_name
  if threadsafe
    Thread.current.thread_variable_get(:capybara_session_name) ||
      Thread.current.thread_variable_set(:capybara_session_name, :default)
  else
    @session_name ||= :default
  end
end
```

    
  

    
      
  
### 
  
    .**session_name=**(name)  ⇒ Object 
  

  

  

  
    
      

```

346
347
348
349
350
351
352
```

    
    
      

```
# File 'lib/capybara.rb', line 346

def session_name=(name)
  if threadsafe
    Thread.current.thread_variable_set :capybara_session_name, name
  else
    @session_name = name
  end
end
```

    
  

    
      
  
### 
  
    .**session_options**  ⇒ Object 
  

  

  

  
    
      

```

410
411
412
```

    
    
      

```
# File 'lib/capybara.rb', line 410

def session_options
  config.session_options
end
```

    
  

    
      
  
### 
  
    .**string**(html)  ⇒ Capybara::Node::Simple 
  

  

  

  
    

Wraps the given string, which should contain an HTML document or fragment
in a Capybara::Node::Simple which exposes all Capybara::Node::Matchers,
Capybara::Node::Finders and Capybara::Node::DocumentMatchers. This allows you to query
any string containing HTML in the exact same way you would query the current document in a Capybara
session.

  

  
  
    
#### Examples:

    
      
        
##### 

A single element

      
      

```
node = Capybara.string('<a href="foo">bar</a>')
anchor = node.first('a')
anchor[:href] #=> 'foo'
anchor.text #=> 'bar'
```

    
      
        
##### 

Multiple elements

      
      

```
node = Capybara.string <<-HTML
  <ul>
    <li id="home">Home</li>
    <li id="projects">Projects</li>
  </ul>
HTML

node.find('#projects').text # => 'Projects'
node.has_selector?('li#home', text: 'Home')
node.has_selector?('#projects')
node.find('ul').find('li:first-child').text # => 'Home'
```

    
  

Parameters:

  
    
- 
      
        html
      
      
        (String)
      
      
      
        —
        

An html fragment or document

      
    
  

Returns:

  
    
- 
      
      
        (Capybara::Node::Simple)
      
      
      
        —
        

A node which has Capybara's finders and matchers

      
    
  

  
    
      

```

240
241
242
```

    
    
      

```
# File 'lib/capybara.rb', line 240

def string(html)
  Capybara::Node::Simple.new(html)
end
```

    
  

    
      
  
### 
  
    .**threadsafe**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara.rb', line 44

Config::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**use_default_driver**  ⇒ Object 
  

  

  

  
    

Use the default driver as the current driver

  

  

  
    
      

```

282
283
284
```

    
    
      

```
# File 'lib/capybara.rb', line 282

def use_default_driver
  self.current_driver = nil
end
```

    
  

    
      
  
### 
  
    .**use_html5_parsing**  ⇒ Object 
  

  

  

  
    

See configure

  

  

  
    
      

```

44
45
46
```

    
    
      

```
# File 'lib/capybara.rb', line 44

Config::OPTIONS.each do |method|
  def_delegators :config, method, "#{method}="
end
```

    
  

    
      
  
### 
  
    .**using_driver**(driver)  ⇒ Object 
  

  

  

  
    

Yield a block using a specific driver

  

  

  
    
      

```

290
291
292
293
294
295
296
```

    
    
      

```
# File 'lib/capybara.rb', line 290

def using_driver(driver)
  previous_driver = Capybara.current_driver
  Capybara.current_driver = driver
  yield
ensure
  self.current_driver = previous_driver
end
```

    
  

    
      
  
### 
  
    .**using_session**(name_or_session, &block)  ⇒ Object 
  

  

  

  
    

Yield a block using a specific session name or Session instance.

  

  

  
    
      

```

358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
```

    
    
      

```
# File 'lib/capybara.rb', line 358

def using_session(name_or_session, &block)
  previous_session = current_session
  previous_session_info = {
    specified_session: specified_session,
    session_name: session_name,
    current_driver: current_driver,
    app: app
  }
  self.specified_session = self.session_name = nil
  if name_or_session.is_a? Capybara::Session
    self.specified_session = name_or_session
  else
    self.session_name = name_or_session
  end

  if block.arity.zero?
    yield
  else
    yield current_session, previous_session
  end
ensure
  self.session_name, self.specified_session = previous_session_info.values_at(:session_name, :specified_session)
  self.current_driver, self.app = previous_session_info.values_at(:current_driver, :app) if threadsafe
end
```

    
  

    
      
  
### 
  
    .**using_wait_time**(seconds)  ⇒ Object 
  

  

  

  
    

Yield a block using a specific wait time

  

  

  
    
      

```

302
303
304
305
306
307
308
```

    
    
      

```
# File 'lib/capybara.rb', line 302

def using_wait_time(seconds)
  previous_wait_time = Capybara.default_max_wait_time
  Capybara.default_max_wait_time = seconds
  yield
ensure
  Capybara.default_max_wait_time = previous_wait_time
end
```