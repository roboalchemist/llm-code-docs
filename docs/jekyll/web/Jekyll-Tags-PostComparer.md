# Class: Jekyll::Tags::PostComparer
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Tags::PostComparer

        show all
      

    Defined in:
    lib/jekyll/tags/post_url.rb
  
##

      Constant Summary
      collapse
    

    
      
        MATCHER =
          
        
        

```
%r!^(.+/)*(\d+-\d+-\d+)-(.*)$!.freeze
```

## Instance Attribute Summary collapse

-
  
      #**date**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute date.

-
  
      #**name**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute name.

-
  
      #**path**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute path.

-
  
      #**slug**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute slug.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**==**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**deprecated_equality**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(name)  ⇒ PostComparer 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of PostComparer.

-
  
      #**post_date**  ⇒ Object 

## Constructor Details

###
  
    #**initialize**(name)  ⇒ PostComparer 
  

  

  

  
    

Returns a new instance of PostComparer.

```

10
11
12
13
14
15
16
17
18
19
20
21
```

```
# File 'lib/jekyll/tags/post_url.rb', line 10

def initialize(name)
  @name = name

  all, @path, @date, @slug = *name.sub(%r!^/!, "").match(MATCHER)
  unless all
    raise Jekyll::Errors::InvalidPostNameError,
          "'#{name}' does not contain valid date and/or title."
  end

  basename_pattern = "#{date}-#{Regexp.escape(slug)}\\.[^.]+"
  @name_regex = %r!^_posts/#{path}#{basename_pattern}|^#{path}_posts/?#{basename_pattern}!
end
```

## Instance Attribute Details

###
  
    #**date**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute date.

```

8
9
10
```

```
# File 'lib/jekyll/tags/post_url.rb', line 8

def date
  @date
end
```

###
  
    #**name**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute name.

```

8
9
10
```

```
# File 'lib/jekyll/tags/post_url.rb', line 8

def name
  @name
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
# File 'lib/jekyll/tags/post_url.rb', line 8

def path
  @path
end
```

###
  
    #**slug**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute slug.

```

8
9
10
```

```
# File 'lib/jekyll/tags/post_url.rb', line 8

def slug
  @slug
end
```

## Instance Method Details

###
  
    #**==**(other)  ⇒ Object 
  

  

  

  
    
      

```

30
31
32
```

```
# File 'lib/jekyll/tags/post_url.rb', line 30

def ==(other)
  other.relative_path.match(@name_regex)
end
```

###
  
    #**deprecated_equality**(other)  ⇒ Object 
  

  

  

  
    
      

```

34
35
36
37
38
39
```

```
# File 'lib/jekyll/tags/post_url.rb', line 34

def deprecated_equality(other)
  slug == post_slug(other) &&
    post_date.year  == other.date.year &&
    post_date.month == other.date.month &&
    post_date.day   == other.date.day
end
```

###
  
    #**post_date**  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
```

```
# File 'lib/jekyll/tags/post_url.rb', line 23

def post_date
  @post_date ||= Utils.parse_date(
    date,
    "'#{date}' does not contain valid date and/or title."
  )
end
```
