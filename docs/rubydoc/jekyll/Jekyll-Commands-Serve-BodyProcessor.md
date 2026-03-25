# Class: Jekyll::Commands::Serve::BodyProcessor
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Commands::Serve::BodyProcessor

        show all
      

    Defined in:
    lib/jekyll/commands/serve/servlet.rb
  
## Overview

This class inserts the LiveReload script tags into HTML as it is served

##

      Constant Summary
      collapse
    

    
      
        HEAD_TAG_REGEX =
          
        
        

```
%r!<head>|<head[^(er)][^<]*>!.freeze
```

## Instance Attribute Summary collapse

-
  
      #**content_length**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute content_length.

-
  
      #**livereload_added**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute livereload_added.

-
  
      #**new_body**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute new_body.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(body, options)  ⇒ BodyProcessor 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of BodyProcessor.

-
  
      #**livereload_args**  ⇒ Object 

-
  
      #**process!**  ⇒ Object 

rubocop:disable Metrics/MethodLength.

-
  
      #**processed?**  ⇒ Boolean 

-
  
      #**template**  ⇒ Object 

rubocop:enable Metrics/MethodLength.

## Constructor Details

###
  
    #**initialize**(body, options)  ⇒ BodyProcessor 
  

  

  

  
    

Returns a new instance of BodyProcessor.

```

50
51
52
53
54
```

```
# File 'lib/jekyll/commands/serve/servlet.rb', line 50

def initialize(body, options)
  @body = body
  @options = options
  @processed = false
end
```

## Instance Attribute Details

###
  
    #**content_length**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute content_length.

```

48
49
50
```

```
# File 'lib/jekyll/commands/serve/servlet.rb', line 48

def content_length
  @content_length
end
```

###
  
    #**livereload_added**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute livereload_added.

```

48
49
50
```

```
# File 'lib/jekyll/commands/serve/servlet.rb', line 48

def livereload_added
  @livereload_added
end
```

###
  
    #**new_body**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute new_body.

```

48
49
50
```

```
# File 'lib/jekyll/commands/serve/servlet.rb', line 48

def new_body
  @new_body
end
```

## Instance Method Details

###
  
    #**livereload_args**  ⇒ Object 
  

  

  

  
    
      

```

113
114
115
116
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
# File 'lib/jekyll/commands/serve/servlet.rb', line 113

def livereload_args
  # XHTML standard requires ampersands to be encoded as entities when in
  # attributes. See http://stackoverflow.com/a/2190292
  src = ""
  if @options["livereload_min_delay"]
    src += "&mindelay=#{@options["livereload_min_delay"]}"
  end
  if @options["livereload_max_delay"]
    src += "&maxdelay=#{@options["livereload_max_delay"]}"
  end
  src += "&port=#{@options["livereload_port"]}" if @options["livereload_port"]
  src
end
```

###
  
    #**process!**  ⇒ Object 
  

  

  

  
    

rubocop:disable Metrics/MethodLength

```

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
```

```
# File 'lib/jekyll/commands/serve/servlet.rb', line 61

def process!
  @new_body = []
  # @body will usually be a File object but Strings occur in rare cases
  if @body.respond_to?(:each)
    begin
      @body.each { |line| @new_body << line.to_s }
    ensure
      @body.close
    end
  else
    @new_body = @body.lines
  end

  @content_length = 0
  @livereload_added = false

  @new_body.each do |line|
    if !@livereload_added && line["<head"]
      line.gsub!(HEAD_TAG_REGEX) do |match|
        %(#{match}#{template.result(binding)})
      end

      @livereload_added = true
    end

    @content_length += line.bytesize
    @processed = true
  end
  @new_body = @new_body.join
end
```

###
  
    #**processed?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

56
57
58
```

```
# File 'lib/jekyll/commands/serve/servlet.rb', line 56

def processed?
  @processed
end
```

###
  
    #**template**  ⇒ Object 
  

  

  

  
    

rubocop:enable Metrics/MethodLength

```

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
```

```
# File 'lib/jekyll/commands/serve/servlet.rb', line 93

def template
  # Unclear what "snipver" does. Doc at
  # https://github.com/livereload/livereload-js states that the recommended
  # setting is 1.

  # Complicated JavaScript to ensure that livereload.js is loaded from the
  # same origin as the page.  Mostly useful for dealing with the browser's
  # distinction between 'localhost' and 127.0.0.1
  @template ||= ERB.new(<<~TEMPLATE)
    <script>
      document.write(
        '<script src="' + location.protocol + '//' +
        (location.host || 'localhost').split(':')[0] +
        ':<%=@options["livereload_port"] %>/livereload.js?snipver=1<%= livereload_args %>"' +
        '></' +
        'script>');
    </script>
  TEMPLATE
end
```
