# Class: Jekyll::CollectionReader
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::CollectionReader

        show all
      

    Defined in:
    lib/jekyll/readers/collection_reader.rb
  
##

      Constant Summary
      collapse
    

    
      
        SPECIAL_COLLECTIONS =
          
        
        

```
%w(posts data).freeze
```

## Instance Attribute Summary collapse

-
  
      #**content**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute content.

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**initialize**(site)  ⇒ CollectionReader 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of CollectionReader.

-
  
      #**read**  ⇒ Object 

Read in all collections specified in the configuration.

## Constructor Details

###
  
    #**initialize**(site)  ⇒ CollectionReader 
  

  

  

  
    

Returns a new instance of CollectionReader.

```

9
10
11
12
```

```
# File 'lib/jekyll/readers/collection_reader.rb', line 9

def initialize(site)
  @site = site
  @content = {}
end
```

## Instance Attribute Details

###
  
    #**content**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute content.

```

7
8
9
```

```
# File 'lib/jekyll/readers/collection_reader.rb', line 7

def content
  @content
end
```

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

7
8
9
```

```
# File 'lib/jekyll/readers/collection_reader.rb', line 7

def site
  @site
end
```

## Instance Method Details

###
  
    #**read**  ⇒ Object 
  

  

  

  
    

Read in all collections specified in the configuration

Returns nothing.

```

17
18
19
20
21
```

```
# File 'lib/jekyll/readers/collection_reader.rb', line 17

def read
  site.collections.each_value do |collection|
    collection.read unless SPECIAL_COLLECTIONS.include?(collection.label)
  end
end
```
