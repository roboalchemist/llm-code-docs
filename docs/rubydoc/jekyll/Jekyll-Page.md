# Class: Jekyll::Page
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Page

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Convertible
  
    Defined in:
    lib/jekyll/page.rb
  
## Direct Known Subclasses

PageWithoutAFile

##

      Constant Summary
      collapse
    

    
      
        ATTRIBUTES_FOR_LIQUID =
          
  
    

Attributes for Liquid templates

```
%w(
  content
  dir
  excerpt
  name
  path
  url
).freeze
```

        HTML_EXTENSIONS =
          
  
    

A set of extensions that are considered HTML or HTML-like so we should not alter them,  this includes .xhtml through XHTM5.

```
%w(
  .html
  .xhtml
  .htm
).freeze
```

## Instance Attribute Summary collapse

-
  
      #**basename**  ⇒ Object 

Returns the value of attribute basename.

-
  
      #**content**  ⇒ Object 

Returns the value of attribute content.

-
  
      #**data**  ⇒ Object 

Returns the value of attribute data.

-
  
      #**dir**  ⇒ Object 

The generated directory into which the page will be placed upon generation.

-
  
      #**ext**  ⇒ Object 

      (also: #extname)
    
  
  
  
  
    
    
  
  
  
  
  

  
    

Returns the value of attribute ext.

-
  
      #**name**  ⇒ Object 

Returns the value of attribute name.

-
  
      #**output**  ⇒ Object 

Returns the value of attribute output.

-
  
      #**pager**  ⇒ Object 

Returns the value of attribute pager.

-
  
      #**site**  ⇒ Object 

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**destination**(dest)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Obtain destination path.

-
  
      #**excerpt**  ⇒ Object 

-
  
      #**excerpt_separator**  ⇒ Object 

-
  
      #**generate_excerpt?**  ⇒ Boolean 

-
  
      #**html?**  ⇒ Boolean 

Returns the Boolean of whether this Page is HTML or not.

-
  
      #**index?**  ⇒ Boolean 

Returns the Boolean of whether this Page is an index file or not.

-
  
      #**initialize**(site, base, dir, name)  ⇒ Page 

    constructor
  
  
  
  
  
  

  
    

Initialize a new Page.

-
  
      #**inspect**  ⇒ Object 

Returns the object as a debug String.

-
  
      #**path**  ⇒ Object 

The path to the source file.

-
  
      #**permalink**  ⇒ Object 

The full path and filename of the post.

-
  
      #**process**(name)  ⇒ Object 

Extract information from the page filename.

-
  
      #**relative_path**  ⇒ Object 

The path to the page source file, relative to the site source.

-
  
      #**render**(layouts, site_payload)  ⇒ Object 

Add any necessary layouts to this post.

-
  
      #**template**  ⇒ Object 

The template of the permalink.

-
  
      #**trigger_hooks**(hook_name, *args)  ⇒ Object 

-
  
      #**url**  ⇒ Object 

The generated relative url of this page.

-
  
      #**url_placeholders**  ⇒ Object 

Returns a hash of URL placeholder names (as symbols) mapping to the desired placeholder replacements.

-
  
      #**write?**  ⇒ Boolean 

### Methods included from Convertible

# [], #asset_file?, #coffeescript_file?, #converters, #do_layout, #hook_owner, #invalid_layout?, #output_ext, #place_in_layout?, #published?, #read_yaml, #render_all_layouts, #render_liquid, #render_with_liquid?, #renderer, #sass_file?, #to_liquid, #to_s, #transform, #type, #validate_data!, #validate_permalink!, #write

## Constructor Details

###
  
    #**initialize**(site, base, dir, name)  ⇒ Page 
  

  

  

  
    

Initialize a new Page.

site - The Site object. base - The String path to the source. dir  - The String path between the source and the file. name - The String filename of the file.

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
```

```
# File 'lib/jekyll/page.rb', line 37

def initialize(site, base, dir, name)
  @site = site
  @base = base
  @dir  = dir
  @name = name
  @path = if site.in_theme_dir(base) == base # we're in a theme
            site.in_theme_dir(base, dir, name)
          else
            site.in_source_dir(base, dir, name)
          end

  process(name)
  read_yaml(PathManager.join(base, dir), name)
  generate_excerpt if site.config["page_excerpts"]

  data.default_proc = proc do |_, key|
    site.frontmatter_defaults.find(relative_path, type, key)
  end

  Jekyll::Hooks.trigger :pages, :post_init, self
end
```

## Instance Attribute Details

###
  
    #**basename**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute basename.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def basename
  @basename
end
```

###
  
    #**content**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute content.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def content
  @content
end
```

###
  
    #**data**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute data.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def data
  @data
end
```

###
  
    #**dir**  ⇒ Object 
  

  

  

  
    

The generated directory into which the page will be placed upon generation. This is derived from the permalink or, if permalink is absent, will be ‘/’

Returns the String destination directory.

```

64
65
66
```

```
# File 'lib/jekyll/page.rb', line 64

def dir
  url.end_with?("/") ? url : url_dir
end
```

###
  
    #**ext**  ⇒ Object 
  

  
    Also known as:
    extname
    
  

  

  
    

Returns the value of attribute ext.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def ext
  @ext
end
```

###
  
    #**name**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute name.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def name
  @name
end
```

###
  
    #**output**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute output.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def output
  @output
end
```

###
  
    #**pager**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute pager.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def pager
  @pager
end
```

###
  
    #**site**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute site.

```

8
9
10
```

```
# File 'lib/jekyll/page.rb', line 8

def site
  @site
end
```

## Instance Method Details

###
  
    #**destination**(dest)  ⇒ Object 
  

  

  

  
    

Obtain destination path.

dest - The String path to the destination dir.

Returns the destination file path String.

```

153
154
155
156
157
158
159
160
161
```

```
# File 'lib/jekyll/page.rb', line 153

def destination(dest)
  @destination ||= {}
  @destination[dest] ||= begin
    path = site.in_dest_dir(dest, URL.unescape_path(url))
    path = File.join(path, "index") if url.end_with?("/")
    path << output_ext unless path.end_with? output_ext
    path
  end
end
```

###
  
    #**excerpt**  ⇒ Object 
  

  

  

  
    
      

```

190
191
192
193
194
```

```
# File 'lib/jekyll/page.rb', line 190

def excerpt
  return @excerpt if defined?(@excerpt)

  @excerpt = data["excerpt"] ? data["excerpt"].to_s : nil
end
```

###
  
    #**excerpt_separator**  ⇒ Object 
  

  

  

  
    
      

```

186
187
188
```

```
# File 'lib/jekyll/page.rb', line 186

def excerpt_separator
  @excerpt_separator ||= (data["excerpt_separator"] || site.config["excerpt_separator"]).to_s
end
```

###
  
    #**generate_excerpt?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

196
197
198
```

```
# File 'lib/jekyll/page.rb', line 196

def generate_excerpt?
  !excerpt_separator.empty? && instance_of?(Jekyll::Page) && html?
end
```

###
  
    #**html?**  ⇒ Boolean 
  

  

  

  
    

Returns the Boolean of whether this Page is HTML or not.

Returns:

-

        (Boolean)

```

169
170
171
```

```
# File 'lib/jekyll/page.rb', line 169

def html?
  HTML_EXTENSIONS.include?(output_ext)
end
```

###
  
    #**index?**  ⇒ Boolean 
  

  

  

  
    

Returns the Boolean of whether this Page is an index file or not.

Returns:

-

        (Boolean)

```

174
175
176
```

```
# File 'lib/jekyll/page.rb', line 174

def index?
  basename == "index"
end
```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

Returns the object as a debug String.

```

164
165
166
```

```
# File 'lib/jekyll/page.rb', line 164

def inspect
  "#<#{self.class} @relative_path=#{relative_path.inspect}>"
end
```

###
  
    #**path**  ⇒ Object 
  

  

  

  
    

The path to the source file

Returns the path to the source file

```

139
140
141
```

```
# File 'lib/jekyll/page.rb', line 139

def path
  data.fetch("path") { relative_path }
end
```

###
  
    #**permalink**  ⇒ Object 
  

  

  

  
    

The full path and filename of the post. Defined in the YAML of the post body.

Returns the String permalink or nil if none has been set.

```

72
73
74
```

```
# File 'lib/jekyll/page.rb', line 72

def permalink
  data.nil? ? nil : data["permalink"]
end
```

###
  
    #**process**(name)  ⇒ Object 
  

  

  

  
    

Extract information from the page filename.

name - The String filename of the page file.

NOTE: ‘String#gsub` removes all trailing periods (in comparison to `String#chomp`) Returns nothing.

```

116
117
118
119
120
121
```

```
# File 'lib/jekyll/page.rb', line 116

def process(name)
  return unless name

  self.ext = File.extname(name)
  self.basename = name[0..-ext.length - 1].gsub(%r!\.*\z!, "")
end
```

###
  
    #**relative_path**  ⇒ Object 
  

  

  

  
    

The path to the page source file, relative to the site source

```

144
145
146
```

```
# File 'lib/jekyll/page.rb', line 144

def relative_path
  @relative_path ||= PathManager.join(@dir, @name).delete_prefix("/")
end
```

###
  
    #**render**(layouts, site_payload)  ⇒ Object 
  

  

  

  
    

Add any necessary layouts to this post

layouts      - The Hash of => “layout”. site_payload - The site payload Hash.

Returns String rendered page.

```

129
130
131
132
133
134
```

```
# File 'lib/jekyll/page.rb', line 129

def render(layouts, site_payload)
  site_payload["page"] = to_liquid
  site_payload["paginator"] = pager.to_liquid

  do_layout(site_payload, layouts)
end
```

###
  
    #**template**  ⇒ Object 
  

  

  

  
    

The template of the permalink.

Returns the template String.

```

79
80
81
82
83
84
85
86
87
```

```
# File 'lib/jekyll/page.rb', line 79

def template
  if !html?
    "/:path/:basename:output_ext"
  elsif index?
    "/:path/"
  else
    Utils.add_permalink_suffix("/:path/:basename", site.permalink_style)
  end
end
```

###
  
    #**trigger_hooks**(hook_name, *args)  ⇒ Object 
  

  

  

  
    
      

```

178
179
180
```

```
# File 'lib/jekyll/page.rb', line 178

def trigger_hooks(hook_name, *args)
  Jekyll::Hooks.trigger :pages, hook_name, self, *args
end
```

###
  
    #**url**  ⇒ Object 
  

  

  

  
    

The generated relative url of this page. e.g. /about.html.

Returns the String url.

```

92
93
94
95
96
97
98
```

```
# File 'lib/jekyll/page.rb', line 92

def url
  @url ||= URL.new(
    :template     => template,
    :placeholders => url_placeholders,
    :permalink    => permalink
  ).to_s
end
```

###
  
    #**url_placeholders**  ⇒ Object 
  

  

  

  
    

Returns a hash of URL placeholder names (as symbols) mapping to the desired placeholder replacements. For details see “url.rb”

```

102
103
104
105
106
107
108
```

```
# File 'lib/jekyll/page.rb', line 102

def url_placeholders
  {
    :path       => @dir,
    :basename   => basename,
    :output_ext => output_ext,
  }
end
```

###
  
    #**write?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

182
183
184
```

```
# File 'lib/jekyll/page.rb', line 182

def write?
  true
end
```
