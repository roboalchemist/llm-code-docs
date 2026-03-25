# Module: Prawn::View
  
  
  

  

  
  
  
  
  

  

  
  
    Defined in:
    lib/prawn/view.rb
  
  

## Overview

  
    

This mixin allows you to create modular Prawn code without the need to create subclasses of Document.

“‘ruby class Greeter

```
include Prawn::View

# Optional override: allows you to set document options or even use
# a custom document class
def document
  @document ||= Prawn::Document.new(page_size: 'A4')
end

def initialize(name)
  @name = name
end

def say_hello
  text "Hello, #{@name}!"
end

def say_goodbye
  font("Courier") do
    text "Goodbye, #{@name}!"
  end
end

```

end

greeter = Greeter.new(“Gregory”)

greeter.say_hello greeter.say_goodbye

greeter.save_as(“greetings.pdf”) “‘

The short story about why you should use this mixin rather than creating subclasses of `Prawn::Document` is that it helps prevent accidental conflicts between your code and Prawn’s code.

Here’s the slightly longer story…

By using composition rather than inheritance under the hood, this mixin allows you to keep your state separate from `Prawn::Document`‘s state, and also will prevent unexpected method name collisions due to late binding effects.

This mixin is mostly meant for extending Prawn’s functionality with your own additions, but you can also use it to replace or wrap existing Prawn methods. Calling `super` will still work as expected, and alternatively you can explicitly call `document.some_method` to delegate to Prawn where needed.

  

  

  
    
## 
      Experimental API
      collapse
    

    

      
        
- 
  
    
      #**document**  ⇒ Prawn::Dcoument 
    

    
  
  
  
  
  
  
  
  

  
    

Lazily instantiates a `Prawn::Document` object.

  

      
        
- 
  
    
      #**method_missing**(method_name, *args, **kwargs, &block)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Delegates all unhandled calls to object returned by #document method.

  

      
        
- 
  
    
      #**respond_to_missing?**(method_name, _include_all = false)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    

Does this object respond to the specified message?.

  

      
        
- 
  
    
      #**save_as**(filename)  ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Syntatic sugar that calls `document.render_file` under the hood.

  

      
        
- 
  
    
      #**update** { ... } ⇒ void 
    

    
  
  
  
  
  
  
  
  

  
    

Syntactic sugar that uses `instance_eval` under the hood to provide a block-based DSL.

  

      
    

  

  
## Dynamic Method Handling

  

    This class handles dynamic methods through the method_missing method
    
  
  
    
  
### 
  
    #**method_missing**(method_name, *args, **kwargs, &block)  ⇒ Object 
  

  

  

  
    

Delegates all unhandled calls to object returned by #document method.

  

  

Parameters:

  
    
- 
      
        method_name
      
      
        (Symbol)
      
      
      
    
  
    
- 
      
        args
      
      
        (Array)
      
      
      
        —
        

Positional arguments.

      
    
  
    
- 
      
        kwargs
      
      
        (Hash)
      
      
      
        —
        

Keyword arguments.

      
    
  
    
- 
      
        block
      
      
        (Proc)
      
      
      
    
  

  
    
      

```

75
76
77
78
79
```

    
    
      

```
# File 'lib/prawn/view.rb', line 75

def method_missing(method_name, *args, **kwargs, &block)
  return super unless document.respond_to?(method_name)

  document.public_send(method_name, *args, **kwargs, &block)
end
```

    
  

  

  
    
## Instance Method Details

    
      
  
### 
  
    #**document**  ⇒ Prawn::Dcoument 
  

  

  

  
    

Lazily instantiates a `Prawn::Document` object.

You can also redefine this method in your own classes to use a custom document class.

  

  

Returns:

  
    
- 
      
      
        (Prawn::Dcoument)
      
      
      
    
  

  
    
      

```

65
66
67
```

    
    
      

```
# File 'lib/prawn/view.rb', line 65

def document
  @document ||= Prawn::Document.new
end
```

    
  

    
      
  
### 
  
    #**respond_to_missing?**(method_name, _include_all = false)  ⇒ Boolean 
  

  

  

  
    

Does this object respond to the specified message?

  

  

Parameters:

  
    
- 
      
        method_name
      
      
        (Symbol)
      
      
      
    
  
    
- 
      
        _include_all
      
      
        (Boolean)
      
      
        *(defaults to: false)*
      
      
    
  

Returns:

  
    
- 
      
      
        (Boolean)
      
      
      
    
  

  
    
      

```

86
87
88
```

    
    
      

```
# File 'lib/prawn/view.rb', line 86

def respond_to_missing?(method_name, _include_all = false)
  document.respond_to?(method_name) || super
end
```

    
  

    
      
  
### 
  
    #**save_as**(filename)  ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Syntatic sugar that calls `document.render_file` under the hood.

  

  
  
    
#### Examples:

    
      
      

```
greeter.save_as("greetings.pdf")
```

    
  

Parameters:

  
    
- 
      
        filename
      
      
        (String)
      
      
      
    
  

  
    
      

```

112
113
114
```

    
    
      

```
# File 'lib/prawn/view.rb', line 112

def save_as(filename)
  document.render_file(filename)
end
```

    
  

    
      
  
### 
  
    #**update** { ... } ⇒ void 
  

  

  

  
    

This method returns an undefined value.

Syntactic sugar that uses `instance_eval` under the hood to provide a block-based DSL.

  

  
  
    
#### Examples:

    
      
      

```
greeter.update do
  say_hello
  say_goodbye
end
```

    
  

Yields:

  
    
- 
      
      
        
      
      
      
    
  

  
    
      

```

101
102
103
```

    
    
      

```
# File 'lib/prawn/view.rb', line 101

def update(&block)
  instance_eval(&block)
end
```