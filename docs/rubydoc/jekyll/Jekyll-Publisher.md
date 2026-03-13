# Class: Jekyll::Publisher
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Publisher

        show all
      

    Defined in:
    lib/jekyll/publisher.rb
  
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**hidden_in_the_future?**(thing)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**initialize**(site)  ⇒ Publisher 
    

    
  
  
  
    constructor
  
  
  
  
  
  

  
    

A new instance of Publisher.

-
  
      #**publish?**(thing)  ⇒ Boolean 

## Constructor Details

###
  
    #**initialize**(site)  ⇒ Publisher 
  

  

  

  
    

Returns a new instance of Publisher.

```

5
6
7
```

```
# File 'lib/jekyll/publisher.rb', line 5

def initialize(site)
  @site = site
end
```

## Instance Method Details

###
  
    #**hidden_in_the_future?**(thing)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

13
14
15
```

```
# File 'lib/jekyll/publisher.rb', line 13

def hidden_in_the_future?(thing)
  thing.respond_to?(:date) && !@site.future && thing.date.to_i > @site.time.to_i
end
```

###
  
    #**publish?**(thing)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

9
10
11
```

```
# File 'lib/jekyll/publisher.rb', line 9

def publish?(thing)
  can_be_published?(thing) && !hidden_in_the_future?(thing)
end
```
