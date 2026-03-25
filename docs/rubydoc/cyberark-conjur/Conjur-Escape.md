# Module: Conjur::Escape
  
    Included in:
    API, Id
  
  

  
  
    Defined in:
    lib/conjur/escape.rb
  
## Overview

Provides helpers for escaping url components.

The helpers are added as both class and isntance methods.

## Defined Under Namespace

      **Modules:** ClassMethods
    
  
    
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**fully_escape**(str)  ⇒ String 
    

    
  
  
  
  
  
  
  
  

  
    

URL escape the entire string.

-
  
      #**path_escape**(str)  ⇒ String 

Escape a URI path component.

-
  
      #**query_escape**(str)  ⇒ String 

Escape a URI query value.

## Instance Method Details

###
  
    #**fully_escape**(str)  ⇒ String 
  

  

  

  
    

URL escape the entire string.  This is essentially the same as calling `CGI.escape str`.

#### Examples

```
fully_escape 'foo/bar@baz'
# => "foo%2Fbar%40baz"

```

Parameters:

-

        str

        (String)
      
      
      
        —
        

the string to escape

Returns:

-

        (String)

        —
        

the escaped string

See Also:
  
- Conjur::Escape::ClassMethods#fully_escape

```

102
103
104
```

```
# File 'lib/conjur/escape.rb', line 102

def fully_escape(str)
  self.class.fully_escape str
end

```

###
  
    #**path_escape**(str)  ⇒ String 
  

  

  

  
    

Escape a URI path component.

This method simply calls Conjur::Escape::ClassMethods#path_or_query_escape.

Parameters:

-

        str

        (String)
      
      
      
        —
        

the string to escape

Returns:

-

        (String)

        —
        

the escaped string

See Also:
  
- Conjur::Escape::ClassMethods#path_or_query_escape

```

113
114
115
```

```
# File 'lib/conjur/escape.rb', line 113

def path_escape(str)
  self.class.path_escape str
end

```

###
  
    #**query_escape**(str)  ⇒ String 
  

  

  

  
    

Escape a URI query value.

This method simply calls Conjur::Escape::ClassMethods#path_or_query_escape.

Parameters:

-

        str

        (String)
      
      
      
        —
        

the string to escape

Returns:

-

        (String)

        —
        

the escaped string

See Also:
  
- Conjur::Escape::ClassMethods#path_or_query_escape

```

125
126
127
```

```
# File 'lib/conjur/escape.rb', line 125

def query_escape(str)
  self.class.query_escape str
end

```
