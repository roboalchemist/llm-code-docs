# Class: Jekyll::Cleaner
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Cleaner

        show all
      

    Defined in:
    lib/jekyll/cleaner.rb
  
## Overview

Handles the cleanup of a site’s destination before it is built.

##

      Constant Summary
      collapse
    

    
      
        HIDDEN_FILE_REGEX =
          
        
        

```
%r!/\.{1,2}$!.freeze
```

## Instance Attribute Summary collapse

-
  
      #**site**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute site.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**cleanup!**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Cleans up the site’s destination directory.

-
  
      #**initialize**(site)  ⇒ Cleaner 

    constructor
  
  
  
  
  
  

  
    

A new instance of Cleaner.

## Constructor Details

###
  
    #**initialize**(site)  ⇒ Cleaner 
  

  

  

  
    

Returns a new instance of Cleaner.

```

9
10
11
```

```
# File 'lib/jekyll/cleaner.rb', line 9

def initialize(site)
  @site = site
end
```

## Instance Attribute Details

###
  
    #**site**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute site.

```

7
8
9
```

```
# File 'lib/jekyll/cleaner.rb', line 7

def site
  @site
end
```

## Instance Method Details

###
  
    #**cleanup!**  ⇒ Object 
  

  

  

  
    

Cleans up the site’s destination directory

```

14
15
16
17
```

```
# File 'lib/jekyll/cleaner.rb', line 14

def cleanup!
  FileUtils.rm_rf(obsolete_files)
  FileUtils.rm_rf(metadata_file) unless @site.incremental?
end
```
