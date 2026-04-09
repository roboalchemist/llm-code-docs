# Module: Conjur::Escape::ClassMethods
  
    Included in:
    API::Router
  
  

  
  
    Defined in:
    lib/conjur/escape.rb
  
  

  
    
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
  
      #**path_or_query_escape**(str)  ⇒ String 

Escape a path or query value.

-
  
      #**query_escape**(str)  ⇒ String 

Escape a URI query value.

## Instance Method Details

###
  
    #**fully_escape**(str)  ⇒ String 
  

  

  

  
    

URL escape the entire string.  This is essentially the same as calling `CGI.escape str`,
and then substituting `%20` for `+`.

#### Examples

```
fully_escape 'foo/bar@baz'
# => "foo%2Fbar%40baz"

```

```
fully_escape 'test/Domain Controllers'
# => "test%2FDomain%20Controllers"

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

```

41
42
43
44
45
```

```
# File 'lib/conjur/escape.rb', line 41

def fully_escape(str)
  # CGI escape uses + for spaces, which our services don't support :-(
  # We just gsub it.
  CGI.escape(str.to_s).gsub('+', '%20')
end

```

###
  
    #**path_escape**(str)  ⇒ String 
  

  

  

  
    

Escape a URI path component.

This method simply calls #path_or_query_escape.

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
  
- #path_or_query_escape

```

55
56
57
```

```
# File 'lib/conjur/escape.rb', line 55

def path_escape(str)
  path_or_query_escape str
end

```

###
  
    #**path_or_query_escape**(str)  ⇒ String 
  

  

  

  
    

Escape a path or query value.

This method is *similar* to `URI.escape`, but it has several important differences:

- If a falsey value is given, the string `"false"` is returned.

- If the value given responds to `#id`, the value returned by `str.id` is escaped instead.

- The value is escaped without modifying `':'` or `'/'`.

Parameters:

-

        str

        (String, FalseClass, NilClass, #id)
      
      
      
        —
        

the value to escape

Returns:

-

        (String)

        —
        

the value escaped as described

```

79
80
81
82
83
84
85
```

```
# File 'lib/conjur/escape.rb', line 79

def path_or_query_escape(str)
  return "false" unless str
  str = str.id if str.respond_to?(:id)
  # Leave colons and forward slashes alone
  require 'addressable/uri'
  Addressable::URI.encode(str.to_s)
end

```

###
  
    #**query_escape**(str)  ⇒ String 
  

  

  

  
    

Escape a URI query value.

This method simply calls #path_or_query_escape.

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
  
- #path_or_query_escape

```

66
67
68
```

```
# File 'lib/conjur/escape.rb', line 66

def query_escape(str)
  path_or_query_escape str
end

```
