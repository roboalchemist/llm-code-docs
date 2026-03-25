# Module: UTF8Util
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/vendor/utf8_util.rb
  
  

  
    
## 
      Constant Summary
      collapse
    

    
      
        REPLACEMENT_CHAR =
          
  
    

use ‘?’ intsead of the unicode replace char, since that is 3 bytes and can increase the string size if it’s done a lot

  

  

        
        

```
"?"

```

      
    
  

  
    
## 
      Class Method Summary
      collapse
    

    

      
        
- 
  
    
      .**clean**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Replace invalid UTF-8 character sequences with a replacement character.

  

      
        
- 
  
    
      .**clean!**(str)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Replace invalid UTF-8 character sequences with a replacement character.

  

      
    

  

  
    
## Class Method Details

    
      
  
### 
  
    .**clean**(str)  ⇒ Object 
  

  

  

  
    

Replace invalid UTF-8 character sequences with a replacement character

Returns a copy of this String as valid UTF-8.

  

  

  
    
      

```

17
18
19
```

    
    
      

```
# File 'lib/resque/vendor/utf8_util.rb', line 17

def self.clean(str)
  clean!(str.dup)
end

```

    
  

    
      
  
### 
  
    .**clean!**(str)  ⇒ Object 
  

  

  

  
    

Replace invalid UTF-8 character sequences with a replacement character

Returns self as valid UTF-8.

  

  

  
    
      

```

9
10
11
12
```

    
    
      

```
# File 'lib/resque/vendor/utf8_util.rb', line 9

def self.clean!(str)
  return str if str.encoding.to_s == "UTF-8"
  str.force_encoding("binary").encode("UTF-8", :invalid => :replace, :undef => :replace, :replace => REPLACEMENT_CHAR)
end

```