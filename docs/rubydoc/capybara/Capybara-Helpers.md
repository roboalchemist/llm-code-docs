# Module: Capybara::Helpers
  
  
  Private

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/capybara/helpers.rb
  
  

## Overview

  
    

  **This module is part of a private API.**
  You should avoid using this module if possible, as it may be removed or be changed in the future.

  

  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

## Defined Under Namespace

  
    
  
    
      **Classes:** Timer
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**declension**(singular, plural, count)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    

A poor man's `pluralize`.

  

      
        
- 
  
    
      .**filter_backtrace**(trace)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      .**inject_asset_host**(html, host: Capybara.asset_host)  ⇒ String 
    

    
  
  
  
  
  
  
  
  private

  
    

Injects a `<base>` tag into the given HTML code, pointing to asset_host.

  

      
        
- 
  
    
      .**normalize_whitespace**(text)  ⇒ String 
    

    
  
  
  
  
  
  
  deprecated
  private

  
    **Deprecated.** 
  

      
        
- 
  
    
      .**timer**(expire_in:)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
        
- 
  
    
      .**to_regexp**(text, exact: false, all_whitespace: false, options: nil)  ⇒ Regexp 
    

    
  
  
  
  
  
  
  
  private

  
    

Escapes any characters that would have special meaning in a regexp if text is not a regexp.

  

      
        
- 
  
    
      .**warn**(message, uplevel: 1)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  
    
## 
      Instance Method Summary
      collapse
    

    

      
        
- 
  
    
      #**monotonic_time**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  private

  
    
  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**declension**(singular, plural, count)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

A poor man's `pluralize`. Given two declensions, one singular and one
plural, as well as a count, this will pick the correct declension. This
way we can generate grammatically correct error message.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

The singular form of the word

      
    
  
    
- 
      
      
      
      
        
        

The plural form of the word

      
    
  
    
- 
      
      
      
      
        
        

The number of items

      
    
  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

69
70
71
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 69

def declension(singular, plural, count)
  count == 1 ? singular : plural
end

```

    
  

    
      
  
### 
  
    .**filter_backtrace**(trace)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

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
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 73

def filter_backtrace(trace)
  return 'No backtrace' unless trace

  filter = %r{lib/capybara/|lib/rspec/|lib/minitest/|delegate.rb}
  new_trace = trace.take_while { |line| line !~ filter }
  new_trace = trace.grep_v(filter) if new_trace.empty?
  new_trace = trace.dup if new_trace.empty?

  new_trace.first.split(':in ', 2).first
end

```

    
  

    
      
  
### 
  
    .**inject_asset_host**(html, host: Capybara.asset_host)  ⇒ String 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Injects a `<base>` tag into the given HTML code, pointing to
asset_host.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

HTML code to inject into

      
    
  
    
- 
      
      
      
        *(defaults to: Capybara.asset_host)*
      
      
        
        

(Capybara.asset_host) The host from which assets should be loaded

      
    
  

Returns:

  
    
- 
      
      
      
      
        
        

The modified HTML code

      
    
  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

50
51
52
53
54
55
56
57
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 50

def inject_asset_host(html, host: Capybara.asset_host)
  if host && Nokogiri::HTML(html).css('base').empty?
    html.match(/<head[^<]*?>/) do |m|
      return html.clone.insert m.end(0), "<base href='#{host}' />"
    end
  end
  html
end

```

    
  

    
      
  
### 
  
    .**normalize_whitespace**(text)  ⇒ String 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

**Deprecated.** 

Normalizes whitespace space by stripping leading and trailing
whitespace and replacing sequences of whitespace characters
with a single space.

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

Text to normalize

      
    
  

Returns:

  
    
- 
      
      
      
      
        
        

Normalized text

      
    
  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

17
18
19
20
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 17

def normalize_whitespace(text)
  Capybara::Helpers.warn 'DEPRECATED: Capybara::Helpers::normalize_whitespace is deprecated, please update your driver'
  text.to_s.gsub(/[[:space:]]+/, ' ').strip
end

```

    
  

    
      
  
### 
  
    .**timer**(expire_in:)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

98
99
100
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 98

def timer(expire_in:)
  Timer.new(expire_in)
end

```

    
  

    
      
  
### 
  
    .**to_regexp**(text, exact: false, all_whitespace: false, options: nil)  ⇒ Regexp 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Escapes any characters that would have special meaning in a regexp
if text is not a regexp

  

  

Parameters:

  
    
- 
      
      
      
      
        
        

Text to escape

      
    
  
    
- 
      
      
      
        *(defaults to: false)*
      
      
        
        

(false) Whether or not this should be an exact text match

      
    
  
    
- 
      
      
      
        *(defaults to: nil)*
      
      
        
        

Options passed to Regexp.new when creating the Regexp

      
    
  

Returns:

  
    
- 
      
      
      
      
        
        

Regexp to match the passed in text and options

      
    
  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

32
33
34
35
36
37
38
39
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 32

def to_regexp(text, exact: false, all_whitespace: false, options: nil)
  return text if text.is_a?(Regexp)

  escaped = Regexp.escape(text)
  escaped = escaped.gsub('\\ ', '[[:blank:]]') if all_whitespace
  escaped = "\\A#{escaped}\\z" if exact
  Regexp.new(escaped, options)
end

```

    
  

    
      
  
### 
  
    .**warn**(message, uplevel: 1)  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

84
85
86
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 84

def warn(message, uplevel: 1)
  Kernel.warn(message, uplevel: uplevel)
end

```

    
  

    
  

  
    
## Instance Method Details

    
      
  
### 
  
    #**monotonic_time**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

  

  

API:

  
    
- 
      
      
      
      
        
        

private

      
    
  

  
    
      

```

89
```

    
    
      

```
# File 'lib/capybara/helpers.rb', line 89

def monotonic_time; Process.clock_gettime Process::CLOCK_MONOTONIC_RAW; end

```