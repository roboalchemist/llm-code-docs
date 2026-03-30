# Class: Jekyll::PageReader
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::PageReader

        show all
      

    Defined in:
    lib/jekyll/readers/page_reader.rb
  
## Instance Attribute Summary collapse

-
  
      #**dir**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute dir.

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
  
      #**initialize**(site, dir)  ⇒ PageReader 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of PageReader.

-
  
      #**read**(files)  ⇒ Object 

Create a new `Jekyll::Page` object for each entry in a given array.

## Constructor Details

###
  
    #**initialize**(site, dir)  ⇒ PageReader 
  

  

  

  
    

Returns a new instance of PageReader.

```

7
8
9
10
11
```

```
# File 'lib/jekyll/readers/page_reader.rb', line 7

def initialize(site, dir)
  @site = site
  @dir = dir
  @unfiltered_content = []
end

```

## Instance Attribute Details

###
  
    #**dir**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute dir.

```

5
6
7
```

```
# File 'lib/jekyll/readers/page_reader.rb', line 5

def dir
  @dir
end

```

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

5
6
7
```

```
# File 'lib/jekyll/readers/page_reader.rb', line 5

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
# File 'lib/jekyll/readers/page_reader.rb', line 5

def unfiltered_content
  @unfiltered_content
end

```

## Instance Method Details

###
  
    #**read**(files)  ⇒ Object 
  

  

  

  
    

Create a new `Jekyll::Page` object for each entry in a given array.

files - An array of file names inside ‘@dir`

Returns an array of publishable `Jekyll::Page` objects.

```

18
19
20
21
22
23
```

```
# File 'lib/jekyll/readers/page_reader.rb', line 18

def read(files)
  files.each do |page|
    @unfiltered_content << Page.new(@site, @site.source, @dir, page)
  end
  @unfiltered_content.select { |page| site.publisher.publish?(page) }
end

```
