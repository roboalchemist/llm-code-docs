# Class: RuboCop::Cop::AnnotationComment
  
    Inherits:
    
      Object
      
        

          
- Object

- RuboCop::Cop::AnnotationComment

        show all
      

    Defined in:
    lib/rubocop/cop/mixin/annotation_comment.rb
  
## Overview

Representation of an annotation comment in source code (eg. ‘# TODO: blah blah blah`).

## Instance Attribute Summary collapse

-
  
      #**colon**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute colon.

-
  
      #**comment**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute comment.

-
  
      #**keyword**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute keyword.

-
  
      #**margin**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute margin.

-
  
      #**note**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute note.

-
  
      #**space**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    

Returns the value of attribute space.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**annotation?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**bounds**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Returns the range bounds for just the annotation.

-
  
      #**correct?**(colon:)  ⇒ Boolean 

-
  
      #**initialize**(comment, keywords)  ⇒ AnnotationComment 

    constructor
  
  
  
  
  
  

  
    

A new instance of AnnotationComment.

## Constructor Details

###
  
    #**initialize**(comment, keywords)  ⇒ AnnotationComment 
  

  

  

  
    

Returns a new instance of AnnotationComment.

Parameters:

-

        comment

        (Parser::Source::Comment)
      
      
      
    
  
    
-

        keywords
      
      
        (Array<String>)
      
      
      
    
  

  
    
      

```

11
12
13
14
15
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 11

def initialize(comment, keywords)
  @comment = comment
  @keywords = keywords
  @margin, @keyword, @colon, @space, @note = split_comment(comment)
end

```

## Instance Attribute Details

###
  
    #**colon**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute colon.

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 7

def colon
  @colon
end

```

###
  
    #**comment**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute comment.

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 7

def comment
  @comment
end

```

###
  
    #**keyword**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute keyword.

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 7

def keyword
  @keyword
end

```

###
  
    #**margin**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute margin.

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 7

def margin
  @margin
end

```

###
  
    #**note**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute note.

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 7

def note
  @note
end

```

###
  
    #**space**  ⇒ Object  (readonly)
  

  

  

  
    

Returns the value of attribute space.

```

7
8
9
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 7

def space
  @space
end

```

## Instance Method Details

###
  
    #**annotation?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

17
18
19
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 17

def annotation?
  keyword_appearance? && !just_keyword_of_sentence?
end

```

###
  
    #**bounds**  ⇒ Object 
  

  

  

  
    

Returns the range bounds for just the annotation

```

29
30
31
32
33
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 29

def bounds
  start = comment.source_range.begin_pos + margin.length
  length = [keyword, colon, space].reduce(0) { |len, elem| len + elem.to_s.length }
  [start, start + length]
end

```

###
  
    #**correct?**(colon:)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

21
22
23
24
25
26
```

```
# File 'lib/rubocop/cop/mixin/annotation_comment.rb', line 21

def correct?(colon:)
  return false unless keyword && space && note
  return false unless keyword == keyword.upcase

  self.colon.nil? == !colon
end

```
