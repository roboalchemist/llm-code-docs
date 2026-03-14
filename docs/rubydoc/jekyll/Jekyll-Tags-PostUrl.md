# Class: Jekyll::Tags::PostUrl
  
    Inherits:
    
      Liquid::Tag
      
        

          
- Object

- Liquid::Tag

- Jekyll::Tags::PostUrl

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      Filters::URLFilters
  
    Defined in:
    lib/jekyll/tags/post_url.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(tag_name, post, tokens)  ⇒ PostUrl 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of PostUrl.

-
  
      #**render**(context)  ⇒ Object 

### Methods included from Filters::URLFilters

# absolute_url, #relative_url, #strip_index

## Constructor Details

###
  
    #**initialize**(tag_name, post, tokens)  ⇒ PostUrl 
  

  

  

  
    

Returns a new instance of PostUrl.

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
```

```
# File 'lib/jekyll/tags/post_url.rb', line 61

def initialize(tag_name, post, tokens)
  super
  @orig_post = post.strip
  begin
    @post = PostComparer.new(@orig_post)
  rescue StandardError => e
    raise Jekyll::Errors::PostURLError, "      Could not parse name of post \"\#{@orig_post}\" in tag 'post_url'.\n       Make sure the post exists and the name is correct.\n       \#{e.class}: \#{e.message}\n    MSG\n  end\nend\n"

```

## Instance Method Details

###
  
    #**render**(context)  ⇒ Object 
  

  

  

  
    

Raises:

-

```

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
```

```
# File 'lib/jekyll/tags/post_url.rb', line 75

def render(context)
  @context = context
  site = context.registers[:site]

  site.posts.docs.each do |document|
    return relative_url(document) if @post == document
  end

  # New matching method did not match, fall back to old method
  # with deprecation warning if this matches

  site.posts.docs.each do |document|
    next unless @post.deprecated_equality document

    Jekyll::Deprecator.deprecation_message(
      "A call to '{% post_url #{@post.name} %}' did not match a post using the new " \
      "matching method of checking name (path-date-slug) equality. Please make sure " \
      "that you change this tag to match the post's name exactly."
    )
    return relative_url(document)
  end

  raise Jekyll::Errors::PostURLError, "    Could not find post \"\#{@orig_post}\" in tag 'post_url'.\n    Make sure the post exists and the name is correct.\n  MSG\nend\n"

```
