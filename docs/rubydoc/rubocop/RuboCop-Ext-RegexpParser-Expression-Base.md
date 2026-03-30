# Module: RuboCop::Ext::RegexpParser::Expression::Base
  
    Defined in:
    lib/rubocop/ext/regexp_parser.rb
  
## Overview

Add `expression` and `loc` to all `regexp_parser` nodes

## Instance Attribute Summary collapse

-
  
      #**origin**  ⇒ Object 

Returns the value of attribute origin.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**expression**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Shortcut to `loc.expression`.

-
  
      #**loc**  ⇒ Object 

E.g.

## Instance Attribute Details

###
  
    #**origin**  ⇒ Object 
  

  

  

  
    

Returns the value of attribute origin.

```

23
24
25
```

```
# File 'lib/rubocop/ext/regexp_parser.rb', line 23

def origin
  @origin
end
```

## Instance Method Details

###
  
    #**expression**  ⇒ Object 
  

  

  

  
    

Shortcut to `loc.expression`

```

26
27
28
```

```
# File 'lib/rubocop/ext/regexp_parser.rb', line 26

def expression
  @expression ||= origin.adjust(begin_pos: ts, end_pos: ts + full_length)
end
```

###
  
    #**loc**  ⇒ Object 
  

  

  

  
    

E.g.

```
[a-z]{2,}
^^^^^^^^^ expression
     ^^^^ quantifier
^^^^^     body
^         begin
    ^     end

```

Please open issue if you need other locations

```

44
45
46
```

```
# File 'lib/rubocop/ext/regexp_parser.rb', line 44

def loc
  @loc ||= Map.new(expression, **build_location)
end
```
