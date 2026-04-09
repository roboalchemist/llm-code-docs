# Class: Dry::Validation::MessageSet
  
    Inherits:
    
      Schema::MessageSet
      
        

          
- Object

- Schema::MessageSet

- Dry::Validation::MessageSet

        show all
      

    Defined in:
    lib/dry/validation/message_set.rb
  
## Overview

MessageSet is a specialized message set for handling validation messages

## Instance Attribute Summary collapse

-
  
      #**locale**  ⇒ Symbol 

      readonly
    
    
  
  
  
  
  

  
    

Configured locale.

-
  
      #**source_messages**  ⇒ Array<Message, Message::Localized, Schema::Message> 

      readonly
    
    
  
  private

Return the source set of messages used to produce final evaluated messages.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**add**(message)  ⇒ MessageSet 
    

    
  
  private

Add a new message.

-
  
      #**filter**(*predicates)  ⇒ MessageSet 

Filter message set using provided predicates.

-
  
      #**freeze**  ⇒ Object 

  private

-
  
      #**initialize**(messages, options = EMPTY_HASH)  ⇒ MessageSet 

    constructor
  
  private

A new instance of MessageSet.

-
  
      #**with**(other, new_options = EMPTY_HASH)  ⇒ MessageSet 

  private

Return a new message set using updated options.

## Constructor Details

###
  
    #**initialize**(messages, options = EMPTY_HASH)  ⇒ MessageSet 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of MessageSet.

```

26
27
28
29
30
```

```
# File 'lib/dry/validation/message_set.rb', line 26

def initialize(messages, options = EMPTY_HASH)
  @locale = options[:locale]
  @source_messages = options.fetch(:source) { messages.dup }
  super
end
```

## Instance Attribute Details

###
  
    #**locale**  ⇒ Symbol  (readonly)
  

  

  

  
    

Configured locale

Returns:

-

        (Symbol)

```

23
24
25
```

```
# File 'lib/dry/validation/message_set.rb', line 23

def locale
  @locale
end
```

###
  
    #**source_messages**  ⇒ Array<Message, Message::Localized, Schema::Message>  (readonly)
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Return the source set of messages used to produce final evaluated messages

Returns:

-

        (Array<Message, Message::Localized, Schema::Message>)

```

16
17
18
```

```
# File 'lib/dry/validation/message_set.rb', line 16

def source_messages
  @source_messages
end
```

## Instance Method Details

###
  
    #**add**(message)  ⇒ MessageSet 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Add a new message

This is used when result is being prepared

Returns:

-

        (MessageSet)

```

53
54
55
56
57
58
```

```
# File 'lib/dry/validation/message_set.rb', line 53

def add(message)
  @empty = nil
  source_messages << message
  messages << message
  self
end
```

###
  
    #**filter**(*predicates)  ⇒ MessageSet 
  

  

  

  
    

Filter message set using provided predicates

This method is open to any predicate because messages can be anything that implements Message API, thus they can implement whatever predicates you may need.

#### Examples

#####

get a list of base messages

```
message_set = contract.(input).errors
message_set.filter(:base?)
```

Parameters:

-

        predicates

        (Array<Symbol>)
      
      
      
    
  
Returns:

-

        (MessageSet)

```

75
76
77
78
79
80
```

```
# File 'lib/dry/validation/message_set.rb', line 75

def filter(*predicates)
  messages = select { |msg|
    predicates.all? { |predicate| msg.respond_to?(predicate) && msg.public_send(predicate) }
  }
  self.class.new(messages)
end
```

###
  
    #**freeze**  ⇒ Object 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

```

83
84
85
86
87
88
89
90
91
```

```
# File 'lib/dry/validation/message_set.rb', line 83

def freeze
  source_messages.select { |err| err.respond_to?(:evaluate) }.each do |err|
    idx = messages.index(err) || source_messages.index(err)
    msg = err.evaluate(locale: locale, full: options[:full])
    messages[idx] = msg
  end
  to_h
  self
end
```

###
  
    #**with**(other, new_options = EMPTY_HASH)  ⇒ MessageSet 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Return a new message set using updated options

Returns:

-

        (MessageSet)

```

37
38
39
40
41
42
43
44
```

```
# File 'lib/dry/validation/message_set.rb', line 37

def with(other, new_options = EMPTY_HASH)
  return self if new_options.empty? && other.eql?(messages)

  self.class.new(
    other | select { |err| err.is_a?(Message) },
    options.merge(source: source_messages, **new_options)
  ).freeze
end
```
