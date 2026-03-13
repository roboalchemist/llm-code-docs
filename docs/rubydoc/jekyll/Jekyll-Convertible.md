# Module: Jekyll::Convertible
  
    Included in:
    Layout, Page
  
  

  
  
    Defined in:
    lib/jekyll/convertible.rb
  
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**[]**(property)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Accessor for data properties by Liquid.

-
  
      #**asset_file?**  ⇒ Boolean 

Determine whether the document is an asset file.

-
  
      #**coffeescript_file?**  ⇒ Boolean 

Determine whether the document is a CoffeeScript file.

-
  
      #**converters**  ⇒ Object 

Determine which converter to use based on this convertible’s extension.

-
  
      #**do_layout**(payload, layouts)  ⇒ Object 

Add any necessary layouts to this convertible document.

-
  
      #**hook_owner**  ⇒ Object 

returns the owner symbol for hook triggering.

-
  
      #**invalid_layout?**(layout)  ⇒ Boolean 

Checks if the layout specified in the document actually exists.

-
  
      #**output_ext**  ⇒ Object 

Determine the extension depending on content_type.

-
  
      #**place_in_layout?**  ⇒ Boolean 

Determine whether the file should be placed into layouts.

-
  
      #**published?**  ⇒ Boolean 

Whether the file is published or not, as indicated in YAML front-matter.

-
  
      #**read_yaml**(base, name, opts = {})  ⇒ Object 

Read the YAML frontmatter.

-
  
      #**render_all_layouts**(layouts, payload, info)  ⇒ Object 

Recursively render layouts.

-
  
      #**render_liquid**(content, payload, info, path)  ⇒ Object 

Render Liquid in the content.

-
  
      #**render_with_liquid?**  ⇒ Boolean 

Determine whether the file should be rendered with Liquid.

-
  
      #**renderer**  ⇒ Object 

-
  
      #**sass_file?**  ⇒ Boolean 

Determine whether the document is a Sass file.

-
  
      #**to_liquid**(attrs = nil)  ⇒ Object 

Convert this Convertible’s data to a Hash suitable for use by Liquid.

-
  
      #**to_s**  ⇒ Object 

Returns the contents as a String.

-
  
      #**transform**  ⇒ Object 

Transform the contents based on the content type.

-
  
      #**type**  ⇒ Object 

The type of a document,   i.e., its classname downcase’d and to_sym’d.

-
  
      #**validate_data!**(filename)  ⇒ Object 

rubocop:enable Metrics/AbcSize.

-
  
      #**validate_permalink!**(filename)  ⇒ Object 

-
  
      #**write**(dest)  ⇒ Object 

Write the generated page file to the destination directory.

## Instance Method Details

###
  
    #**[]**(property)  ⇒ Object 
  

  

  

  
    

Accessor for data properties by Liquid.

property - The String name of the property to retrieve.

Returns the String value or nil if the property isn’t included.

```

235
236
237
238
239
240
241
```

```
# File 'lib/jekyll/convertible.rb', line 235

def [](property)
  if self.class::ATTRIBUTES_FOR_LIQUID.include?(property)
    send(property)
  else
    data[property]
  end
end
```

###
  
    #**asset_file?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the document is an asset file. Asset files include CoffeeScript files and Sass/SCSS files.

Returns true if the extname belongs to the set of extensions

```
that asset files use.

```

Returns:

-

        (Boolean)

```

141
142
143
```

```
# File 'lib/jekyll/convertible.rb', line 141

def asset_file?
  sass_file? || coffeescript_file?
end
```

###
  
    #**coffeescript_file?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the document is a CoffeeScript file.

Returns true if extname == .coffee, false otherwise.

Returns:

-

        (Boolean)

```

155
156
157
```

```
# File 'lib/jekyll/convertible.rb', line 155

def coffeescript_file?
  ext == ".coffee"
end
```

###
  
    #**converters**  ⇒ Object 
  

  

  

  
    

Determine which converter to use based on this convertible’s extension.

Returns the Converter instance.

```

96
97
98
```

```
# File 'lib/jekyll/convertible.rb', line 96

def converters
  renderer.converters
end
```

###
  
    #**do_layout**(payload, layouts)  ⇒ Object 
  

  

  

  
    

Add any necessary layouts to this convertible document.

payload - The site payload Drop or Hash. layouts - A Hash of => “layout”.

Returns nothing.

```

205
206
207
208
209
210
211
212
213
214
215
```

```
# File 'lib/jekyll/convertible.rb', line 205

def do_layout(payload, layouts)
  self.output = renderer.tap do |doc_renderer|
    doc_renderer.layouts = layouts
    doc_renderer.payload = payload
  end.run

  Jekyll.logger.debug "Post-Render Hooks:", relative_path
  Jekyll::Hooks.trigger hook_owner, :post_render, self
ensure
  @renderer = nil # this will allow the modifications above to disappear
end
```

###
  
    #**hook_owner**  ⇒ Object 
  

  

  

  
    

returns the owner symbol for hook triggering

```

132
133
134
```

```
# File 'lib/jekyll/convertible.rb', line 132

def hook_owner
  :pages if is_a?(Page)
end
```

###
  
    #**invalid_layout?**(layout)  ⇒ Boolean 
  

  

  

  
    

Checks if the layout specified in the document actually exists

layout - the layout to check

Returns true if the layout is invalid, false if otherwise

Returns:

-

        (Boolean)

```

181
182
183
```

```
# File 'lib/jekyll/convertible.rb', line 181

def invalid_layout?(layout)
  !data["layout"].nil? && layout.nil? && !(is_a? Jekyll::Excerpt)
end
```

###
  
    #**output_ext**  ⇒ Object 
  

  

  

  
    

Determine the extension depending on content_type.

Returns the String extension for the output file.

```
e.g. ".html" for an HTML output file.

```

```

88
89
90
```

```
# File 'lib/jekyll/convertible.rb', line 88

def output_ext
  renderer.output_ext
end
```

###
  
    #**place_in_layout?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the file should be placed into layouts.

Returns false if the document is an asset file or if the front matter

```
specifies `layout: none`

```

Returns:

-

        (Boolean)

```

172
173
174
```

```
# File 'lib/jekyll/convertible.rb', line 172

def place_in_layout?
  !(asset_file? || no_layout?)
end
```

###
  
    #**published?**  ⇒ Boolean 
  

  

  

  
    

Whether the file is published or not, as indicated in YAML front-matter

Returns:

-

        (Boolean)

```

25
26
27
```

```
# File 'lib/jekyll/convertible.rb', line 25

def published?
  !(data.key?("published") && data["published"] == false)
end
```

###
  
    #**read_yaml**(base, name, opts = {})  ⇒ Object 
  

  

  

  
    

Read the YAML frontmatter.

base - The String path to the dir containing the file. name - The String filename of the file. opts - optional parameter to File.read, default at site configs

Returns nothing. rubocop:disable Metrics/AbcSize

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
# File 'lib/jekyll/convertible.rb', line 37

def read_yaml(base, name, opts = {})
  filename = @path || site.in_source_dir(base, name)
  Jekyll.logger.debug "Reading:", relative_path

  begin
    self.content = File.read(filename, **Utils.merged_file_read_opts(site, opts))
    if content =~ Document::YAML_FRONT_MATTER_REGEXP
      self.content = Regexp.last_match.post_match
      self.data = SafeYAML.load(Regexp.last_match(1))
    end
  rescue Psych::SyntaxError => e
    Jekyll.logger.warn "YAML Exception reading #{filename}: #{e.message}"
    raise e if site.config["strict_front_matter"]
  rescue StandardError => e
    Jekyll.logger.warn "Error reading file #{filename}: #{e.message}"
    raise e if site.config["strict_front_matter"]
  end

  self.data ||= {}

  validate_data! filename
  validate_permalink! filename

  self.data
end
```

###
  
    #**render_all_layouts**(layouts, payload, info)  ⇒ Object 
  

  

  

  
    

Recursively render layouts

layouts - a list of the layouts payload - the payload for Liquid info    - the info for Liquid

Returns nothing

```

192
193
194
195
196
197
```

```
# File 'lib/jekyll/convertible.rb', line 192

def render_all_layouts(layouts, payload, info)
  renderer.layouts = layouts
  self.output = renderer.place_in_layouts(output, payload, info)
ensure
  @renderer = nil # this will allow the modifications above to disappear
end
```

###
  
    #**render_liquid**(content, payload, info, path)  ⇒ Object 
  

  

  

  
    

Render Liquid in the content

content - the raw Liquid content to render payload - the payload for Liquid info    - the info for Liquid

Returns the converted content

```

107
108
109
```

```
# File 'lib/jekyll/convertible.rb', line 107

def render_liquid(content, payload, info, path)
  renderer.render_liquid(content, payload, info, path)
end
```

###
  
    #**render_with_liquid?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the file should be rendered with Liquid.

Returns true if the file has Liquid Tags or Variables, false otherwise.

Returns:

-

        (Boolean)

```

162
163
164
165
166
```

```
# File 'lib/jekyll/convertible.rb', line 162

def render_with_liquid?
  return false if data["render_with_liquid"] == false

  Jekyll::Utils.has_liquid_construct?(content)
end
```

###
  
    #**renderer**  ⇒ Object 
  

  

  

  
    
      

```

243
244
245
```

```
# File 'lib/jekyll/convertible.rb', line 243

def renderer
  @renderer ||= Jekyll::Renderer.new(site, self)
end
```

###
  
    #**sass_file?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the document is a Sass file.

Returns true if extname == .sass or .scss, false otherwise.

Returns:

-

        (Boolean)

```

148
149
150
```

```
# File 'lib/jekyll/convertible.rb', line 148

def sass_file?
  Jekyll::Document::SASS_FILE_EXTS.include?(ext)
end
```

###
  
    #**to_liquid**(attrs = nil)  ⇒ Object 
  

  

  

  
    

Convert this Convertible’s data to a Hash suitable for use by Liquid.

Returns the Hash representation of this Convertible.

```

114
115
116
117
118
119
120
121
```

```
# File 'lib/jekyll/convertible.rb', line 114

def to_liquid(attrs = nil)
  further_data = \
    (attrs || self.class::ATTRIBUTES_FOR_LIQUID).each_with_object({}) do |attribute, hsh|
      hsh[attribute] = send(attribute)
    end

  Utils.deep_merge_hashes defaults, Utils.deep_merge_hashes(data, further_data)
end
```

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    

Returns the contents as a String.

```

20
21
22
```

```
# File 'lib/jekyll/convertible.rb', line 20

def to_s
  content || ""
end
```

###
  
    #**transform**  ⇒ Object 
  

  

  

  
    

Transform the contents based on the content type.

Returns the transformed contents.

```

80
81
82
```

```
# File 'lib/jekyll/convertible.rb', line 80

def transform
  renderer.convert(content)
end
```

###
  
    #**type**  ⇒ Object 
  

  

  

  
    

The type of a document,

```
i.e., its classname downcase'd and to_sym'd.

```

Returns the type of self.

```

127
128
129
```

```
# File 'lib/jekyll/convertible.rb', line 127

def type
  :pages if is_a?(Page)
end
```

###
  
    #**validate_data!**(filename)  ⇒ Object 
  

  

  

  
    

rubocop:enable Metrics/AbcSize

```

64
65
66
67
68
69
```

```
# File 'lib/jekyll/convertible.rb', line 64

def validate_data!(filename)
  unless self.data.is_a?(Hash)
    raise Errors::InvalidYAMLFrontMatterError,
          "Invalid YAML front matter in #{filename}"
  end
end
```

###
  
    #**validate_permalink!**(filename)  ⇒ Object 
  

  

  

  
    
      

```

71
72
73
74
75
```

```
# File 'lib/jekyll/convertible.rb', line 71

def validate_permalink!(filename)
  if self.data["permalink"] == ""
    raise Errors::InvalidPermalinkError, "Invalid permalink in #{filename}"
  end
end
```

###
  
    #**write**(dest)  ⇒ Object 
  

  

  

  
    

Write the generated page file to the destination directory.

dest - The String path to the destination dir.

Returns nothing.

```

222
223
224
225
226
227
228
```

```
# File 'lib/jekyll/convertible.rb', line 222

def write(dest)
  path = destination(dest)
  FileUtils.mkdir_p(File.dirname(path))
  Jekyll.logger.debug "Writing:", path
  File.write(path, output, :mode => "wb")
  Jekyll::Hooks.trigger hook_owner, :post_write, self
end
```
