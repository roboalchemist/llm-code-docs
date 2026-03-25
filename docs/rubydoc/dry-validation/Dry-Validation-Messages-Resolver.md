# Class: Dry::Validation::Messages::Resolver
  
    Inherits:
    
      Object
      
        

          
- Object

- Dry::Validation::Messages::Resolver

        show all
      

    Defined in:
    lib/dry/validation/messages/resolver.rb
  
## Overview

Resolve translated messages from failure arguments

## Instance Attribute Summary collapse

-
  
      #**messages**  ⇒ Object 

      readonly
    
    
  
  
  
  
  

  
    
  

    
  

  
    
##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**call**(message:, tokens:, path:, meta: EMPTY_HASH)  ⇒ Message, Message::Localized 
    

    
      (also: #[])
    
  
  
  
  
  
  
  
  

  
    

Resolve Message object from provided args and path.

-
  
      #**initialize**(messages)  ⇒ Resolver 

    constructor
  
  private

A new instance of Resolver.

-
  
      #**message**(rule, path:, tokens: EMPTY_HASH, locale: nil, full: false)  ⇒ String 

Resolve a message.

## Constructor Details

###
  
    #**initialize**(messages)  ⇒ Resolver 
  

  

  

  
    

  **This method is part of a private API.**
  You should avoid using this method if possible, as it may be removed or be changed in the future.

Returns a new instance of Resolver.

```

18
19
20
```

```
# File 'lib/dry/validation/messages/resolver.rb', line 18

def initialize(messages)
  @messages = messages
end
```

## Instance Attribute Details

###
  
    #**messages**  ⇒ Object  (readonly)
  

  

  

  
    

  

  

  
    
      

```

15
16
17
```

```
# File 'lib/dry/validation/messages/resolver.rb', line 15

def messages
  @messages
end
```

## Instance Method Details

###
  
    #**call**(message:, tokens:, path:, meta: EMPTY_HASH)  ⇒ Message, Message::Localized 
  

  
    Also known as:
    []
    
  

  

  
    

Resolve Message object from provided args and path

This is used internally by contracts when rules are applied If message argument is a Hash, then it MUST have a :text key, which value will be used as the message value

Returns:

-

        (Message, Message::Localized)

```

31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
```

```
# File 'lib/dry/validation/messages/resolver.rb', line 31

def call(message:, tokens:, path:, meta: EMPTY_HASH)
  case message
  when ::Symbol
    Message[->(**opts) { message(message, path: path, tokens: tokens, **opts) }, path, meta]
  when ::String
    Message[->(**opts) { [message_text(message, path: path, **opts), meta] }, path, meta]
  when ::Hash
    meta = message.dup
    text = meta.delete(:text) { |key|
      raise ArgumentError, <<~STR
        +message+ Hash must contain :#{key} key (#{message.inspect} given)
      STR
    }

    call(message: text, tokens: tokens, path: path, meta: meta)
  else
    raise ArgumentError, <<~STR
      +message+ must be either a Symbol, String or Hash (#{message.inspect} given)
    STR
  end
end
```

###
  
    #**message**(rule, path:, tokens: EMPTY_HASH, locale: nil, full: false)  ⇒ String 
  

  

  

  
    

Resolve a message

rubocop:disable Metrics/AbcSize rubocop:disable Metrics/PerceivedComplexity

Returns:

-

        (String)

```

62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
```

```
# File 'lib/dry/validation/messages/resolver.rb', line 62

def message(rule, path:, tokens: EMPTY_HASH, locale: nil, full: false)
  keys = path.to_a.compact
  msg_opts = tokens.merge(path: keys, locale: locale || messages.default_locale)

  if keys.empty?
    template, meta = messages["rules.#{rule}", msg_opts]
  else
    template, meta = messages[rule, msg_opts.merge(path: keys.join(DOT))]
    template, meta = messages[rule, msg_opts.merge(path: keys.last)] unless template
  end

  if !template && keys.size > 1
    non_index_keys = keys.reject { |k| k.is_a?(Integer) }
    template, meta = messages[rule, msg_opts.merge(path: non_index_keys.join(DOT))]
  end

  unless template
    raise MissingMessageError, <<~STR
      Message template for #{rule.inspect} under #{keys.join(DOT).inspect} was not found
    STR
  end

  parsed_tokens = parse_tokens(tokens)
  text = template.(template.data(parsed_tokens))

  [message_text(text, path: path, locale: locale, full: full), meta]
end
```
