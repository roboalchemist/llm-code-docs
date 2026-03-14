# Class: Jekyll::Tags::IncludeTag
  
    Inherits:
    
      Liquid::Tag
      
        

          
- Object

- Liquid::Tag

- Jekyll::Tags::IncludeTag

        show all
      

    Defined in:
    lib/jekyll/tags/include.rb
  
## Direct Known Subclasses

IncludeRelativeTag, OptimizedIncludeTag

##

      Constant Summary
      collapse
    

    
      
        VALID_SYNTAX =
          
        
        

```
%r!
  ([\w-]+)\s*=\s*
  (?:"([^"\\]*(?:\\.[^"\\]*)*)"|'([^'\\]*(?:\\.[^'\\]*)*)'|([\w.-]+))
!x.freeze
```

        VARIABLE_SYNTAX =
          
        
        

```
%r!
  (?<variable>[^{]*(\{\{\s*[\w\-.]+\s*(\|.*)?\}\}[^\s{}]*)+)
  (?<params>.*)
!mx.freeze
```

        FULL_VALID_SYNTAX =
          
        
        

```
%r!\A\s*(?:#{VALID_SYNTAX}(?=\s|\z)\s*)*\z!.freeze
```

        VALID_FILENAME_CHARS =
          
        
        

```
%r!^[\w/.\-()+~\#@]+$!.freeze
```

        INVALID_SEQUENCES =
          
        
        

```
%r![./]{2,}!.freeze
```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**add_include_to_dependency**(site, path, context)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**file_read_opts**(context)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Grab file read opts in the context.

-
  
      #**initialize**(tag_name, markup, tokens)  ⇒ IncludeTag 

    constructor
  
  
  
  
  
  

  
    

A new instance of IncludeTag.

-
  
      #**load_cached_partial**(path, context)  ⇒ Object 

-
  
      #**locate_include_file**(context, file, safe)  ⇒ Object 

-
  
      #**outside_site_source?**(path, dir, safe)  ⇒ Boolean 

-
  
      #**parse_params**(context)  ⇒ Object 

-
  
      #**read_file**(file, context)  ⇒ Object 

This method allows to modify the file content by inheriting from the class.

-
  
      #**realpath_prefixed_with?**(path, dir)  ⇒ Boolean 

-
  
      #**render**(context)  ⇒ Object 

-
  
      #**render_variable**(context)  ⇒ Object 

Render the variable if required.

-
  
      #**syntax_example**  ⇒ Object 

-
  
      #**tag_includes_dirs**(context)  ⇒ Object 

-
  
      #**valid_include_file?**(path, dir, safe)  ⇒ Boolean 

-
  
      #**validate_file_name**(file)  ⇒ Object 

-
  
      #**validate_params**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(tag_name, markup, tokens)  ⇒ IncludeTag 
  

  

  

  
    

Returns a new instance of IncludeTag.

```

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
31
```

```
# File 'lib/jekyll/tags/include.rb', line 19

def initialize(tag_name, markup, tokens)
  super
  markup  = markup.strip
  matched = markup.match(VARIABLE_SYNTAX)
  if matched
    @file = matched["variable"].strip
    @params = matched["params"].strip
  else
    @file, @params = markup.split(%r!\s+!, 2)
  end
  validate_params if @params
  @tag_name = tag_name
end
```

## Instance Method Details

###
  
    #**add_include_to_dependency**(site, path, context)  ⇒ Object 
  

  

  

  
    
      

```

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
# File 'lib/jekyll/tags/include.rb', line 131

def add_include_to_dependency(site, path, context)
  if context.registers[:page]&.key?("path")
    site.regenerator.add_dependency(
      site.in_source_dir(context.registers[:page]["path"]),
      path
    )
  end
end
```

###
  
    #**file_read_opts**(context)  ⇒ Object 
  

  

  

  
    

Grab file read opts in the context

```

84
85
86
```

```
# File 'lib/jekyll/tags/include.rb', line 84

def file_read_opts(context)
  context.registers[:site].file_read_opts
end
```

###
  
    #**load_cached_partial**(path, context)  ⇒ Object 
  

  

  

  
    
      

```

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
154
155
156
157
158
```

```
# File 'lib/jekyll/tags/include.rb', line 140

def load_cached_partial(path, context)
  context.registers[:cached_partials] ||= {}
  cached_partial = context.registers[:cached_partials]

  if cached_partial.key?(path)
    cached_partial[path]
  else
    unparsed_file = context.registers[:site]
      .liquid_renderer
      .file(path)
    begin
      cached_partial[path] = unparsed_file.parse(read_file(path, context))
    rescue Liquid::Error => e
      e.template_name = path
      e.markup_context = "included " if e.markup_context.nil?
      raise e
    end
  end
end
```

###
  
    #**locate_include_file**(context, file, safe)  ⇒ Object 
  

  

  

  
    

Raises:

-

        (IOError)

```

97
98
99
100
101
102
103
104
```

```
# File 'lib/jekyll/tags/include.rb', line 97

def locate_include_file(context, file, safe)
  includes_dirs = tag_includes_dirs(context)
  includes_dirs.each do |dir|
    path = PathManager.join(dir, file)
    return path if valid_include_file?(path, dir.to_s, safe)
  end
  raise IOError, could_not_locate_message(file, includes_dirs, safe)
end
```

###
  
    #**outside_site_source?**(path, dir, safe)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

164
165
166
```

```
# File 'lib/jekyll/tags/include.rb', line 164

def outside_site_source?(path, dir, safe)
  safe && !realpath_prefixed_with?(path, dir)
end
```

###
  
    #**parse_params**(context)  ⇒ Object 
  

  

  

  
    
      

```

37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
```

```
# File 'lib/jekyll/tags/include.rb', line 37

def parse_params(context)
  params = {}
  @params.scan(VALID_SYNTAX) do |key, d_quoted, s_quoted, variable|
    value = if d_quoted
              d_quoted.include?('\\"') ? d_quoted.gsub('\\"', '"') : d_quoted
            elsif s_quoted
              s_quoted.include?("\\'") ? s_quoted.gsub("\\'", "'") : s_quoted
            elsif variable
              context[variable]
            end

    params[key] = value
  end
  params
end
```

###
  
    #**read_file**(file, context)  ⇒ Object 
  

  

  

  
    

This method allows to modify the file content by inheriting from the class.

```

175
176
177
```

```
# File 'lib/jekyll/tags/include.rb', line 175

def read_file(file, context)
  File.read(file, **file_read_opts(context))
end
```

###
  
    #**realpath_prefixed_with?**(path, dir)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

168
169
170
171
172
```

```
# File 'lib/jekyll/tags/include.rb', line 168

def realpath_prefixed_with?(path, dir)
  File.exist?(path) && File.realpath(path).start_with?(dir)
rescue StandardError
  false
end
```

###
  
    #**render**(context)  ⇒ Object 
  

  

  

  
    
      

```

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
118
119
120
121
122
123
124
125
126
127
128
129
```

```
# File 'lib/jekyll/tags/include.rb', line 106

def render(context)
  site = context.registers[:site]

  file = render_variable(context) || @file
  validate_file_name(file)

  path = locate_include_file(context, file, site.safe)
  return unless path

  add_include_to_dependency(site, path, context)

  partial = load_cached_partial(path, context)

  context.stack do
    context["include"] = parse_params(context) if @params
    begin
      partial.render!(context)
    rescue Liquid::Error => e
      e.template_name = path
      e.markup_context = "included " if e.markup_context.nil?
      raise e
    end
  end
end
```

###
  
    #**render_variable**(context)  ⇒ Object 
  

  

  

  
    

Render the variable if required

```

89
90
91
```

```
# File 'lib/jekyll/tags/include.rb', line 89

def render_variable(context)
  Liquid::Template.parse(@file).render(context) if VARIABLE_SYNTAX.match?(@file)
end
```

###
  
    #**syntax_example**  ⇒ Object 
  

  

  

  
    
      

```

33
34
35
```

```
# File 'lib/jekyll/tags/include.rb', line 33

def syntax_example
  "{% #{@tag_name} file.ext param='value' param2='value' %}"
end
```

###
  
    #**tag_includes_dirs**(context)  ⇒ Object 
  

  

  

  
    
      

```

93
94
95
```

```
# File 'lib/jekyll/tags/include.rb', line 93

def tag_includes_dirs(context)
  context.registers[:site].includes_load_paths.freeze
end
```

###
  
    #**valid_include_file?**(path, dir, safe)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

160
161
162
```

```
# File 'lib/jekyll/tags/include.rb', line 160

def valid_include_file?(path, dir, safe)
  !outside_site_source?(path, dir, safe) && File.file?(path)
end
```

###
  
    #**validate_file_name**(file)  ⇒ Object 
  

  

  

  
    
      

```

53
54
55
56
57
58
59
60
61
62
63
64
65
66
```

```
# File 'lib/jekyll/tags/include.rb', line 53

def validate_file_name(file)
  if INVALID_SEQUENCES.match?(file) || !VALID_FILENAME_CHARS.match?(file)
    raise ArgumentError, <<~MSG
      Invalid syntax for include tag. File contains invalid characters or sequences:

        #{file}

      Valid syntax:

        #{syntax_example}

    MSG
  end
end
```

###
  
    #**validate_params**  ⇒ Object 
  

  

  

  
    
      

```

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
```

```
# File 'lib/jekyll/tags/include.rb', line 68

def validate_params
  unless FULL_VALID_SYNTAX.match?(@params)
    raise ArgumentError, <<~MSG
      Invalid syntax for include tag:

      #{@params}

      Valid syntax:

      #{syntax_example}

    MSG
  end
end
```
