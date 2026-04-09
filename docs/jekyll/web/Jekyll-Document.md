# Class: Jekyll::Document
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Document

        show all
      
    
  
  

  
  
  
      Extended by:
      Forwardable
  
  
  
  
  
      Includes:
      Comparable
  
    Defined in:
    lib/jekyll/document.rb
  
##

      Constant Summary
      collapse
    

    
      
        YAML_FRONT_MATTER_REGEXP =
          
        
        

```
%r!\A(---\s*\n.*?\n?)^((---|\.\.\.)\s*$\n?)!m.freeze
```

        DATELESS_FILENAME_MATCHER =
          
        
        

```
%r!^(?:.+/)*(.*)(\.[^.]+)$!.freeze
```

        DATE_FILENAME_MATCHER =
          
        
        

```
%r!^(?>.+/)*?(\d{2,4}-\d{1,2}-\d{1,2})-([^/]*)(\.[^.]+)$!.freeze
```

        SASS_FILE_EXTS =
          
        
        

```
%w(.sass .scss).freeze
```

        YAML_FILE_EXTS =
          
        
        

```
%w(.yaml .yml).freeze
```

## Instance Attribute Summary collapse

-
  
      #**collection**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute collection.

-
  
      #**content**  ⇒ Object 

Returns the value of attribute content.

-
  
      #**extname**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute extname.

-
  
      #**output**  ⇒ Object 

Returns the value of attribute output.

-
  
      #**path**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute path.

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

-
  
      #**type**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute type.

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**superdirs_regex**(dirname)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Class-wide cache to stash and retrieve regexp to detect “super-directories” of a particular Jekyll::Document object.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**<=>**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Compare this document against another document.

-
  
      #**[]**(key)  ⇒ Object 

-
  
      #**asset_file?**  ⇒ Boolean 

Determine whether the document is an asset file.

-
  
      #**basename**  ⇒ Object 

The base filename of the document.

-
  
      #**basename_without_ext**  ⇒ Object 

The base filename of the document, without the file extname.

-
  
      #**categories_from_path**(special_dir)  ⇒ Object 

Add superdirectories of the special_dir to categories.

-
  
      #**cleaned_relative_path**  ⇒ Object 

Produces a “cleaned” relative path.

-
  
      #**coffeescript_file?**  ⇒ Boolean 

Determine whether the document is a CoffeeScript file.

-
  
      #**data**  ⇒ Object 

Fetch the Document’s data.

-
  
      #**date**  ⇒ Object 

Returns the document date.

-
  
      #**destination**(base_directory)  ⇒ Object 

The full path to the output file.

-
  
      #**draft?**  ⇒ Boolean 

Returns whether the document is a draft.

-
  
      #**excerpt_separator**  ⇒ Object 

The Document excerpt_separator, from the YAML Front-Matter or site default excerpt_separator value.

-
  
      #**generate_excerpt?**  ⇒ Boolean 

Whether to generate an excerpt.

-
  
      #**id**  ⇒ Object 

-
  
      #**initialize**(path, relations = {})  ⇒ Document 

    constructor
  
  
  
  
  
  

  
    

Create a new Document.

-
  
      #**inspect**  ⇒ Object 

The inspect string for this document.

-
  
      #**merge_data!**(other, source: "YAML front matter")  ⇒ Object 

Merge some data in with this document’s data.

-
  
      #**method_missing**(method, *args, &blck)  ⇒ Object 

Override of method_missing to check in @data for the key.

-
  
      #**next_doc**  ⇒ Object 

-
  
      #**no_layout?**  ⇒ Boolean 

Determine whether the file should be rendered with a layout.

-
  
      #**output_ext**  ⇒ Object 

The output extension of the document.

-
  
      #**permalink**  ⇒ Object 

The permalink for this Document.

-
  
      #**place_in_layout?**  ⇒ Boolean 

Determine whether the file should be placed into layouts.

-
  
      #**populate_categories**  ⇒ Object 

-
  
      #**populate_tags**  ⇒ Object 

-
  
      #**previous_doc**  ⇒ Object 

-
  
      #**published?**  ⇒ Boolean 

Whether the file is published or not, as indicated in YAML front-matter.

-
  
      #**read**(opts = {})  ⇒ Object 

Read in the file and assign the content and data based on the file contents.

-
  
      #**related_posts**  ⇒ Object 

Calculate related posts.

-
  
      #**relative_path**  ⇒ Object 

The path to the document, relative to the collections_dir.

-
  
      #**render_with_liquid?**  ⇒ Boolean 

Determine whether the file should be rendered with Liquid.

-
  
      #**renderer**  ⇒ Object 

-
  
      #**respond_to_missing?**(method)  ⇒ Boolean 

-
  
      #**sass_file?**  ⇒ Boolean 

Determine whether the document is a Sass file.

-
  
      #**source_file_mtime**  ⇒ Object 

Return document file modification time in the form of a Time object.

-
  
      #**to_liquid**  ⇒ Object 

Create a Liquid-understandable version of this Document.

-
  
      #**to_s**  ⇒ Object 

The string representation for this document.

-
  
      #**trigger_hooks**(hook_name, *args)  ⇒ Object 

-
  
      #**url**  ⇒ Object 

The computed URL for the document.

-
  
      #**url_placeholders**  ⇒ Object 

Construct a Hash of key-value pairs which contain a mapping between   a key in the URL template and the corresponding value for this document.

-
  
      #**url_template**  ⇒ Object 

The URL template where the document would be accessible.

-
  
      #**write**(dest)  ⇒ Object 

Write the generated Document file to the destination directory.

-
  
      #**write?**  ⇒ Boolean 

Determine whether this document should be written.

-
  
      #**yaml_file?**  ⇒ Boolean 

Determine whether the document is a YAML file.

## Constructor Details

###
  
    #**initialize**(path, relations = {})  ⇒ Document 
  

  

  

  
    

Create a new Document.

path - the path to the file relations - a hash with keys :site and :collection, the values of which

```
are the Jekyll::Site and Jekyll::Collection to which this
Document belong.

```

Returns nothing.

```

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
62
```

```
# File 'lib/jekyll/document.rb', line 42

def initialize(path, relations = {})
  @site = relations[:site]
  @path = path
  @extname = File.extname(path)
  @collection = relations[:collection]
  @type = @collection.label.to_sym

  @has_yaml_header = nil

  if draft?
    categories_from_path("_drafts")
  else
    categories_from_path(collection.relative_directory)
  end

  data.default_proc = proc do |_, key|
    site.frontmatter_defaults.find(relative_path, type, key)
  end

  trigger_hooks(:post_init)
end
```

## Dynamic Method Handling

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
###
  
    #**method_missing**(method, *args, &blck)  ⇒ Object 
  

  

  

  
    

Override of method_missing to check in @data for the key.

```

407
408
409
410
411
412
413
414
415
```

```
# File 'lib/jekyll/document.rb', line 407

def method_missing(method, *args, &blck)
  if data.key?(method.to_s)
    Jekyll::Deprecator.deprecation_message "Document##{method} is now a key in the #data hash."
    Jekyll.logger.warn "", "Called by #{caller(1..1)[0]}."
    data[method.to_s]
  else
    super
  end
end
```

## Instance Attribute Details

###
  
    #**collection**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute collection.

```

8
9
10
```

```
# File 'lib/jekyll/document.rb', line 8

def collection
  @collection
end
```

###
  
    #**content**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute content.

```

9
10
11
```

```
# File 'lib/jekyll/document.rb', line 9

def content
  @content
end
```

###
  
    #**extname**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute extname.

```

8
9
10
```

```
# File 'lib/jekyll/document.rb', line 8

def extname
  @extname
end
```

###
  
    #**output**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute output.

```

9
10
11
```

```
# File 'lib/jekyll/document.rb', line 9

def output
  @output
end
```

###
  
    #**path**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute path.

```

8
9
10
```

```
# File 'lib/jekyll/document.rb', line 8

def path
  @path
end
```

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

8
9
10
```

```
# File 'lib/jekyll/document.rb', line 8

def site
  @site
end
```

###
  
    #**type**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute type.

```

8
9
10
```

```
# File 'lib/jekyll/document.rb', line 8

def type
  @type
end
```

## Class Method Details

###
  
    .**superdirs_regex**(dirname)  ⇒ Object 
  

  

  

  
    

Class-wide cache to stash and retrieve regexp to detect “super-directories” of a particular Jekyll::Document object.

dirname - The *special directory* for the Document.

```
e.g. "_posts" or "_drafts" for Documents from the `site.posts` collection.

```

```

27
28
29
30
```

```
# File 'lib/jekyll/document.rb', line 27

def self.superdirs_regex(dirname)
  @superdirs_regex ||= {}
  @superdirs_regex[dirname] ||= %r!#{dirname}.*!
end
```

## Instance Method Details

###
  
    #**<=>**(other)  ⇒ Object 
  

  

  

  
    

Compare this document against another document. Comparison is a comparison between the 2 paths of the documents.

Returns -1, 0, +1 or nil depending on whether this doc’s path is less than,

```
equal or greater than the other doc's path. See String#<=> for more details.

```

```

342
343
344
345
346
347
348
```

```
# File 'lib/jekyll/document.rb', line 342

def <=>(other)
  return nil unless other.respond_to?(:data)

  cmp = data["date"] <=> other.data["date"]
  cmp = path <=> other.path if cmp.nil? || cmp.zero?
  cmp
end
```

###
  
    #**[]**(key)  ⇒ Object 
  

  

  

  
    
      

```

250
251
252
```

```
# File 'lib/jekyll/document.rb', line 250

def [](key)
  data[key]
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

172
173
174
```

```
# File 'lib/jekyll/document.rb', line 172

def asset_file?
  sass_file? || coffeescript_file?
end
```

###
  
    #**basename**  ⇒ Object 
  

  

  

  
    

The base filename of the document.

Returns the base filename of the document.

```

132
133
134
```

```
# File 'lib/jekyll/document.rb', line 132

def basename
  @basename ||= File.basename(path)
end
```

###
  
    #**basename_without_ext**  ⇒ Object 
  

  

  

  
    

The base filename of the document, without the file extname.

Returns the basename without the file extname.

```

125
126
127
```

```
# File 'lib/jekyll/document.rb', line 125

def basename_without_ext
  @basename_without_ext ||= File.basename(path, ".*")
end
```

###
  
    #**categories_from_path**(special_dir)  ⇒ Object 
  

  

  

  
    

Add superdirectories of the special_dir to categories. In the case of es/_posts, ‘es’ is added as a category. In the case of _posts/es, ‘es’ is NOT added as a category.

Returns nothing.

```

426
427
428
429
430
431
432
433
434
435
436
```

```
# File 'lib/jekyll/document.rb', line 426

def categories_from_path(special_dir)
  if relative_path.start_with?(special_dir)
    superdirs = []
  else
    superdirs = relative_path.sub(Document.superdirs_regex(special_dir), "")
    superdirs = superdirs.split(File::SEPARATOR)
    superdirs.reject! { |c| c.empty? || c == special_dir || c == basename }
  end

  merge_data!({ "categories" => superdirs }, :source => "file path")
end
```

###
  
    #**cleaned_relative_path**  ⇒ Object 
  

  

  

  
    

Produces a “cleaned” relative path. The “cleaned” relative path is the relative path without the extname

```
and with the collection's directory removed as well.

```

This method is useful when building the URL of the document.

NOTE: ‘String#gsub` removes all trailing periods (in comparison to `String#chomp`)

Examples:

```
When relative_path is "_methods/site/generate...md":
  cleaned_relative_path
  # => "/site/generate"

```

Returns the cleaned relative path of the document.

```

153
154
155
156
157
158
```

```
# File 'lib/jekyll/document.rb', line 153

def cleaned_relative_path
  @cleaned_relative_path ||=
    relative_path[0..-extname.length - 1]
      .sub(collection.relative_directory, "")
      .gsub(%r!\.*\z!, "")
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

186
187
188
```

```
# File 'lib/jekyll/document.rb', line 186

def coffeescript_file?
  extname == ".coffee"
end
```

###
  
    #**data**  ⇒ Object 
  

  

  

  
    

Fetch the Document’s data.

Returns a Hash containing the data. An empty hash is returned if

```
no data was read.

```

```

68
69
70
```

```
# File 'lib/jekyll/document.rb', line 68

def data
  @data ||= {}
end
```

###
  
    #**date**  ⇒ Object 
  

  

  

  
    

Returns the document date. If metadata is not present then calculates it based on Jekyll::Site#time or the document file modification time.

Return document date string.

```

86
87
88
```

```
# File 'lib/jekyll/document.rb', line 86

def date
  data["date"] ||= (draft? ? source_file_mtime : site.time)
end
```

###
  
    #**destination**(base_directory)  ⇒ Object 
  

  

  

  
    

The full path to the output file.

base_directory - the base path of the output directory

Returns the full path to the output file of this document.

```

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
```

```
# File 'lib/jekyll/document.rb', line 259

def destination(base_directory)
  @destination ||= {}
  @destination[base_directory] ||= begin
    path = site.in_dest_dir(base_directory, URL.unescape_path(url))
    if url.end_with? "/"
      path = File.join(path, "index.html")
    else
      path << output_ext unless path.end_with? output_ext
    end
    path
  end
end
```

###
  
    #**draft?**  ⇒ Boolean 
  

  

  

  
    

Returns whether the document is a draft. This is only the case if the document is in the ‘posts’ collection but in a different directory than ‘_posts’.

Returns whether the document is a draft.

Returns:

-

        (Boolean)

```

102
103
104
105
```

```
# File 'lib/jekyll/document.rb', line 102

def draft?
  data["draft"] ||= relative_path.index(collection.relative_directory).nil? &&
    collection.label == "posts"
end
```

###
  
    #**excerpt_separator**  ⇒ Object 
  

  

  

  
    

The Document excerpt_separator, from the YAML Front-Matter or site default excerpt_separator value

Returns the document excerpt_separator

```

369
370
371
```

```
# File 'lib/jekyll/document.rb', line 369

def excerpt_separator
  @excerpt_separator ||= (data["excerpt_separator"] || site.config["excerpt_separator"]).to_s
end
```

###
  
    #**generate_excerpt?**  ⇒ Boolean 
  

  

  

  
    

Whether to generate an excerpt

Returns true if the excerpt separator is configured.

Returns:

-

        (Boolean)

```

376
377
378
```

```
# File 'lib/jekyll/document.rb', line 376

def generate_excerpt?
  !excerpt_separator.empty?
end
```

###
  
    #**id**  ⇒ Object 
  

  

  

  
    
      

```

395
396
397
```

```
# File 'lib/jekyll/document.rb', line 395

def id
  @id ||= File.join(File.dirname(url), (data["slug"] || basename_without_ext).to_s)
end
```

###
  
    #**inspect**  ⇒ Object 
  

  

  

  
    

The inspect string for this document. Includes the relative path and the collection label.

Returns the inspect string for this document.

```

326
327
328
```

```
# File 'lib/jekyll/document.rb', line 326

def inspect
  "#<#{self.class} #{relative_path} collection=#{collection.label}>"
end
```

###
  
    #**merge_data!**(other, source: "YAML front matter")  ⇒ Object 
  

  

  

  
    

Merge some data in with this document’s data.

Returns the merged data.

```

75
76
77
78
79
80
```

```
# File 'lib/jekyll/document.rb', line 75

def merge_data!(other, source: "YAML front matter")
  merge_categories!(other)
  Utils.deep_merge_hashes!(data, other)
  merge_date!(source)
  data
end
```

###
  
    #**next_doc**  ⇒ Object 
  

  

  

  
    
      

```

380
381
382
383
```

```
# File 'lib/jekyll/document.rb', line 380

def next_doc
  pos = collection.docs.index { |post| post.equal?(self) }
  collection.docs[pos + 1] if pos && pos < collection.docs.length - 1
end
```

###
  
    #**no_layout?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the file should be rendered with a layout.

Returns true if the Front Matter specifies that `layout` is set to `none`.

Returns:

-

        (Boolean)

```

204
205
206
```

```
# File 'lib/jekyll/document.rb', line 204

def no_layout?
  data["layout"] == "none"
end
```

###
  
    #**output_ext**  ⇒ Object 
  

  

  

  
    

The output extension of the document.

Returns the output extension

```

118
119
120
```

```
# File 'lib/jekyll/document.rb', line 118

def output_ext
  renderer.output_ext
end
```

###
  
    #**permalink**  ⇒ Object 
  

  

  

  
    

The permalink for this Document. Permalink is set via the data Hash.

Returns the permalink or nil if no permalink was set in the data.

```

235
236
237
```

```
# File 'lib/jekyll/document.rb', line 235

def permalink
  data && data.is_a?(Hash) && data["permalink"]
end
```

###
  
    #**place_in_layout?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the file should be placed into layouts.

Returns false if the document is set to ‘layouts: none`, or is either an

```
asset file or a yaml file. Returns true otherwise.

```

Returns:

-

        (Boolean)

```

212
213
214
```

```
# File 'lib/jekyll/document.rb', line 212

def place_in_layout?
  !(asset_file? || yaml_file? || no_layout?)
end
```

###
  
    #**populate_categories**  ⇒ Object 
  

  

  

  
    
      

```

438
439
440
441
442
443
444
445
446
447
```

```
# File 'lib/jekyll/document.rb', line 438

def populate_categories
  categories = Array(data["categories"]) + Utils.pluralized_array_from_hash(
    data, "category", "categories"
  )
  categories.map!(&:to_s)
  categories.flatten!
  categories.uniq!

  merge_data!({ "categories" => categories })
end
```

###
  
    #**populate_tags**  ⇒ Object 
  

  

  

  
    
      

```

449
450
451
452
453
454
```

```
# File 'lib/jekyll/document.rb', line 449

def populate_tags
  tags = Utils.pluralized_array_from_hash(data, "tag", "tags")
  tags.flatten!

  merge_data!({ "tags" => tags })
end
```

###
  
    #**previous_doc**  ⇒ Object 
  

  

  

  
    
      

```

385
386
387
388
```

```
# File 'lib/jekyll/document.rb', line 385

def previous_doc
  pos = collection.docs.index { |post| post.equal?(self) }
  collection.docs[pos - 1] if pos && pos.positive?
end
```

###
  
    #**published?**  ⇒ Boolean 
  

  

  

  
    

Whether the file is published or not, as indicated in YAML front-matter

Returns ‘false’ if the ‘published’ key is specified in the YAML front-matter and is ‘false’. Otherwise returns ‘true’.

Returns:

-

        (Boolean)

```

290
291
292
```

```
# File 'lib/jekyll/document.rb', line 290

def published?
  !(data.key?("published") && data["published"] == false)
end
```

###
  
    #**read**(opts = {})  ⇒ Object 
  

  

  

  
    

Read in the file and assign the content and data based on the file contents. Merge the frontmatter of the file with the frontmatter default values

Returns nothing.

```

299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
```

```
# File 'lib/jekyll/document.rb', line 299

def read(opts = {})
  Jekyll.logger.debug "Reading:", relative_path

  if yaml_file?
    @data = SafeYAML.load_file(path)
  else
    begin
      merge_defaults
      read_content(**opts)
      read_post_data
    rescue StandardError => e
      handle_read_error(e)
    end
  end
end
```

###
  
    #**related_posts**  ⇒ Object 
  

  

  

  
    

Calculate related posts.

Returns an Array of related Posts.

```

402
403
404
```

```
# File 'lib/jekyll/document.rb', line 402

def related_posts
  @related_posts ||= Jekyll::RelatedPosts.new(self).build
end
```

###
  
    #**relative_path**  ⇒ Object 
  

  

  

  
    

The path to the document, relative to the collections_dir.

Returns a String path which represents the relative path from the collections_dir to this document.

```

111
112
113
```

```
# File 'lib/jekyll/document.rb', line 111

def relative_path
  @relative_path ||= path.sub("#{site.collections_path}/", "")
end
```

###
  
    #**render_with_liquid?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the file should be rendered with Liquid.

Returns false if the document is either an asset file or a yaml file,

```
or if the document doesn't contain any Liquid Tags or Variables,
true otherwise.

```

Returns:

-

        (Boolean)

```

195
196
197
198
199
```

```
# File 'lib/jekyll/document.rb', line 195

def render_with_liquid?
  return false if data["render_with_liquid"] == false

  !(coffeescript_file? || yaml_file? || !Utils.has_liquid_construct?(content))
end
```

###
  
    #**renderer**  ⇒ Object 
  

  

  

  
    
      

```

136
137
138
```

```
# File 'lib/jekyll/document.rb', line 136

def renderer
  @renderer ||= Jekyll::Renderer.new(site, self)
end
```

###
  
    #**respond_to_missing?**(method)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

417
418
419
```

```
# File 'lib/jekyll/document.rb', line 417

def respond_to_missing?(method, *)
  data.key?(method.to_s) || super
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

179
180
181
```

```
# File 'lib/jekyll/document.rb', line 179

def sass_file?
  SASS_FILE_EXTS.include?(extname)
end
```

###
  
    #**source_file_mtime**  ⇒ Object 
  

  

  

  
    

Return document file modification time in the form of a Time object.

Return document file modification Time object.

```

93
94
95
```

```
# File 'lib/jekyll/document.rb', line 93

def source_file_mtime
  File.mtime(path)
end
```

###
  
    #**to_liquid**  ⇒ Object 
  

  

  

  
    

Create a Liquid-understandable version of this Document.

Returns a Hash representing this Document’s data.

```

318
319
320
```

```
# File 'lib/jekyll/document.rb', line 318

def to_liquid
  @to_liquid ||= Drops::DocumentDrop.new(self)
end
```

###
  
    #**to_s**  ⇒ Object 
  

  

  

  
    

The string representation for this document.

Returns the content of the document

```

333
334
335
```

```
# File 'lib/jekyll/document.rb', line 333

def to_s
  output || content || "NO CONTENT"
end
```

###
  
    #**trigger_hooks**(hook_name, *args)  ⇒ Object 
  

  

  

  
    
      

```

390
391
392
393
```

```
# File 'lib/jekyll/document.rb', line 390

def trigger_hooks(hook_name, *args)
  Jekyll::Hooks.trigger collection.label.to_sym, hook_name, self, *args if collection
  Jekyll::Hooks.trigger :documents, hook_name, self, *args
end
```

###
  
    #**url**  ⇒ Object 
  

  

  

  
    

The computed URL for the document. See ‘Jekyll::URL#to_s` for more details.

Returns the computed URL for the document.

```

242
243
244
245
246
247
248
```

```
# File 'lib/jekyll/document.rb', line 242

def url
  @url ||= URL.new(
    :template     => url_template,
    :placeholders => url_placeholders,
    :permalink    => permalink
  ).to_s
end
```

###
  
    #**url_placeholders**  ⇒ Object 
  

  

  

  
    

Construct a Hash of key-value pairs which contain a mapping between

```
a key in the URL template and the corresponding value for this document.

```

Returns the Hash of key-value pairs for replacement in the URL.

```

227
228
229
```

```
# File 'lib/jekyll/document.rb', line 227

def url_placeholders
  @url_placeholders ||= Drops::UrlDrop.new(self)
end
```

###
  
    #**url_template**  ⇒ Object 
  

  

  

  
    

The URL template where the document would be accessible.

Returns the URL template for the document.

```

219
220
221
```

```
# File 'lib/jekyll/document.rb', line 219

def url_template
  collection.url_template
end
```

###
  
    #**write**(dest)  ⇒ Object 
  

  

  

  
    

Write the generated Document file to the destination directory.

dest - The String path to the destination dir.

Returns nothing.

```

277
278
279
280
281
282
283
284
```

```
# File 'lib/jekyll/document.rb', line 277

def write(dest)
  path = destination(dest)
  FileUtils.mkdir_p(File.dirname(path))
  Jekyll.logger.debug "Writing:", path
  File.write(path, output, :mode => "wb")

  trigger_hooks(:post_write)
end
```

###
  
    #**write?**  ⇒ Boolean 
  

  

  

  
    

Determine whether this document should be written. Based on the Collection to which it belongs.

True if the document has a collection and if that collection’s #write? method returns true, and if the site’s Publisher will publish the document. False otherwise.

rubocop:disable Naming/MemoizedInstanceVariableName

Returns:

-

        (Boolean)

```

358
359
360
361
362
```

```
# File 'lib/jekyll/document.rb', line 358

def write?
  return @write_p if defined?(@write_p)

  @write_p = collection&.write? && site.publisher.publish?(self)
end
```

###
  
    #**yaml_file?**  ⇒ Boolean 
  

  

  

  
    

Determine whether the document is a YAML file.

Returns true if the extname is either .yml or .yaml, false otherwise.

Returns:

-

        (Boolean)

```

163
164
165
```

```
# File 'lib/jekyll/document.rb', line 163

def yaml_file?
  YAML_FILE_EXTS.include?(extname)
end
```
