# Class: Jekyll::RelatedPosts
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::RelatedPosts

        show all
      

    Defined in:
    lib/jekyll/related_posts.rb
  
## Class Attribute Summary collapse

-
  
      .**lsi**  ⇒ Object 

Returns the value of attribute lsi.

## Instance Attribute Summary collapse

-
  
      #**post**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute post.

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**build**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**build_index**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(post)  ⇒ RelatedPosts 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of RelatedPosts.

-
  
      #**lsi_related_posts**  ⇒ Object 

-
  
      #**most_recent_posts**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(post)  ⇒ RelatedPosts 
  

  

  

  
    

Returns a new instance of RelatedPosts.

```

11
12
13
14
15
```

```
# File 'lib/jekyll/related_posts.rb', line 11

def initialize(post)
  @post = post
  @site = post.site
  Jekyll::External.require_with_graceful_fail("classifier-reborn") if site.lsi
end
```

## Class Attribute Details

###
  
    .**lsi**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute lsi.

```

6
7
8
```

```
# File 'lib/jekyll/related_posts.rb', line 6

def lsi
  @lsi
end
```

## Instance Attribute Details

###
  
    #**post**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute post.

```

9
10
11
```

```
# File 'lib/jekyll/related_posts.rb', line 9

def post
  @post
end
```

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

9
10
11
```

```
# File 'lib/jekyll/related_posts.rb', line 9

def site
  @site
end
```

## Instance Method Details

###
  
    #**build**  ⇒ Object 
  

  

  

  
    
      

```

17
18
19
20
21
22
23
24
25
26
```

```
# File 'lib/jekyll/related_posts.rb', line 17

def build
  return [] unless site.posts.docs.size > 1

  if site.lsi
    build_index
    lsi_related_posts
  else
    most_recent_posts
  end
end
```

###
  
    #**build_index**  ⇒ Object 
  

  

  

  
    
      

```

28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
```

```
# File 'lib/jekyll/related_posts.rb', line 28

def build_index
  self.class.lsi ||= begin
    lsi = ClassifierReborn::LSI.new(:auto_rebuild => false)
    Jekyll.logger.info("Populating LSI...")

    site.posts.docs.each do |x|
      lsi.add_item(x)
    end

    Jekyll.logger.info("Rebuilding index...")
    lsi.build_index
    Jekyll.logger.info("")
    lsi
  end
end
```

###
  
    #**lsi_related_posts**  ⇒ Object 
  

  

  

  
    
      

```

44
45
46
```

```
# File 'lib/jekyll/related_posts.rb', line 44

def lsi_related_posts
  self.class.lsi.find_related(post, 11)
end
```

###
  
    #**most_recent_posts**  ⇒ Object 
  

  

  

  
    
      

```

48
49
50
```

```
# File 'lib/jekyll/related_posts.rb', line 48

def most_recent_posts
  @most_recent_posts ||= (site.posts.docs.last(11).reverse! - [post]).first(10)
end
```
