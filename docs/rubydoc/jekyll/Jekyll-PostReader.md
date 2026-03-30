# Class: Jekyll::PostReader
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::PostReader

        show all
      

    Defined in:
    lib/jekyll/readers/post_reader.rb
  
## Instance Attribute Summary collapse

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

-
  
      #**unfiltered_content**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute unfiltered_content.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(site)  ⇒ PostReader 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of PostReader.

-
  
      #**read_content**(dir, magic_dir, matcher)  ⇒ Object 

Read all the content files from <source>/<dir>/magic_dir   and return them with the type klass.

-
  
      #**read_drafts**(dir)  ⇒ Object 

Read all the files in <source>/<dir>/_drafts and create a new Document object with each one.

-
  
      #**read_posts**(dir)  ⇒ Object 

Read all the files in <source>/<dir>/_posts and create a new Document object with each one.

-
  
      #**read_publishable**(dir, magic_dir, matcher)  ⇒ Object 

Read all the files in <source>/<dir>/<magic_dir> and create a new Document object with each one insofar as it matches the regexp matcher.

## Constructor Details

###
  
    #**initialize**(site)  ⇒ PostReader 
  

  

  

  
    

Returns a new instance of PostReader.

```

7
8
9
```

```
# File 'lib/jekyll/readers/post_reader.rb', line 7

def initialize(site)
  @site = site
end

```

## Instance Attribute Details

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

5
6
7
```

```
# File 'lib/jekyll/readers/post_reader.rb', line 5

def site
  @site
end

```

###
  
    #**unfiltered_content**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute unfiltered_content.

```

5
6
7
```

```
# File 'lib/jekyll/readers/post_reader.rb', line 5

def unfiltered_content
  @unfiltered_content
end

```

## Instance Method Details

###
  
    #**read_content**(dir, magic_dir, matcher)  ⇒ Object 
  

  

  

  
    

Read all the content files from <source>/<dir>/magic_dir

```
and return them with the type klass.

```

dir - The String relative path of the directory to read. magic_dir - The String relative directory to <dir>,

```
looks for content here.

```

klass - The return type of the content.

Returns klass type of content files

```

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
# File 'lib/jekyll/readers/post_reader.rb', line 52

def read_content(dir, magic_dir, matcher)
  @site.reader.get_entries(dir, magic_dir).map do |entry|
    next unless matcher.match?(entry)

    path = @site.in_source_dir(File.join(dir, magic_dir, entry))
    Document.new(path,
                 :site       => @site,
                 :collection => @site.posts)
  end.tap(&:compact!)
end

```

###
  
    #**read_drafts**(dir)  ⇒ Object 
  

  

  

  
    

Read all the files in <source>/<dir>/_drafts and create a new Document object with each one.

dir - The String relative path of the directory to read.

Returns nothing.

```

17
18
19
```

```
# File 'lib/jekyll/readers/post_reader.rb', line 17

def read_drafts(dir)
  read_publishable(dir, "_drafts", Document::DATELESS_FILENAME_MATCHER)
end

```

###
  
    #**read_posts**(dir)  ⇒ Object 
  

  

  

  
    

Read all the files in <source>/<dir>/_posts and create a new Document object with each one.

dir - The String relative path of the directory to read.

Returns nothing.

```

27
28
29
```

```
# File 'lib/jekyll/readers/post_reader.rb', line 27

def read_posts(dir)
  read_publishable(dir, "_posts", Document::DATE_FILENAME_MATCHER)
end

```

###
  
    #**read_publishable**(dir, magic_dir, matcher)  ⇒ Object 
  

  

  

  
    

Read all the files in <source>/<dir>/<magic_dir> and create a new Document object with each one insofar as it matches the regexp matcher.

dir - The String relative path of the directory to read.

Returns nothing.

```

37
38
39
40
41
```

```
# File 'lib/jekyll/readers/post_reader.rb', line 37

def read_publishable(dir, magic_dir, matcher)
  read_content(dir, magic_dir, matcher)
    .tap { |docs| docs.each(&:read) }
    .select { |doc| processable?(doc) }
end

```
