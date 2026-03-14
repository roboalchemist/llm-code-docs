# Class: Jekyll::Plugin
  
    Inherits:
    
      Object
      
        

          
- Object

- Jekyll::Plugin

        show all
      

    Defined in:
    lib/jekyll/plugin.rb
  
## Direct Known Subclasses

Converter

##

      Constant Summary
      collapse
    

    
      
        PRIORITIES =
          
        
        

```
{
  :low     => -10,
  :highest => 100,
  :lowest  => -100,
  :normal  => 0,
  :high    => 10,
}.freeze
```

##

      Class Method Summary
      collapse
    

    

      
        
-
  
      .**<=>**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Spaceship is priority [higher -> lower].

-
  
      .**catch_inheritance**(const)  ⇒ Object 

-
  
      .**descendants**  ⇒ Object 

-
  
      .**inherited**(const)  ⇒ Object 

-
  
      .**priority**(priority = nil)  ⇒ Object 

Get or set the priority of this plugin.

-
  
      .**safe**(safe = nil)  ⇒ Object 

Get or set the safety of this plugin.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**<=>**(other)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    

Spaceship is priority [higher -> lower].

-
  
      #**initialize**(config = {})  ⇒ Plugin 

    constructor
  
  
  
  
  
  

  
    

Initialize a new plugin.

## Constructor Details

###
  
    #**initialize**(config = {})  ⇒ Plugin 
  

  

  

  
    

Initialize a new plugin. This should be overridden by the subclass.

config - The Hash of configuration options.

Returns a new instance.

```

88
89
90
```

```
# File 'lib/jekyll/plugin.rb', line 88

def initialize(config = {})
  # no-op for default
end
```

## Class Method Details

###
  
    .**<=>**(other)  ⇒ Object 
  

  

  

  
    

Spaceship is priority [higher -> lower]

other - The class to be compared.

Returns -1, 0, 1.

```

70
71
72
```

```
# File 'lib/jekyll/plugin.rb', line 70

def self.<=>(other)
  PRIORITIES[other.priority] <=> PRIORITIES[priority]
end
```

###
  
    .**catch_inheritance**(const)  ⇒ Object 
  

  

  

  
    
      

```

23
24
25
26
27
28
```

```
# File 'lib/jekyll/plugin.rb', line 23

def self.catch_inheritance(const)
  const.define_singleton_method :inherited do |const_|
    (@children ||= Set.new).add const_
    yield const_ if block_given?
  end
end
```

###
  
    .**descendants**  ⇒ Object 
  

  

  

  
    
      

```

32
33
34
35
36
37
```

```
# File 'lib/jekyll/plugin.rb', line 32

def self.descendants
  @children ||= Set.new
  out = @children.map(&:descendants)
  out << self unless superclass == Plugin
  Set.new(out).flatten
end
```

###
  
    .**inherited**(const)  ⇒ Object 
  

  

  

  
    
      

```

15
16
17
18
19
```

```
# File 'lib/jekyll/plugin.rb', line 15

def self.inherited(const)
  catch_inheritance(const) do |const_|
    catch_inheritance(const_)
  end
end
```

###
  
    .**priority**(priority = nil)  ⇒ Object 
  

  

  

  
    

Get or set the priority of this plugin. When called without an argument it returns the priority. When an argument is given, it will set the priority.

priority - The Symbol priority (default: nil). Valid options are:

```
:lowest, :low, :normal, :high, :highest

```

Returns the Symbol priority.

```

47
48
49
50
51
```

```
# File 'lib/jekyll/plugin.rb', line 47

def self.priority(priority = nil)
  @priority ||= nil
  @priority = priority if priority && PRIORITIES.key?(priority)
  @priority || :normal
end
```

###
  
    .**safe**(safe = nil)  ⇒ Object 
  

  

  

  
    

Get or set the safety of this plugin. When called without an argument it returns the safety. When an argument is given, it will set the safety.

safe - The Boolean safety (default: nil).

Returns the safety Boolean.

```

60
61
62
63
```

```
# File 'lib/jekyll/plugin.rb', line 60

def self.safe(safe = nil)
  @safe = safe unless defined?(@safe) && safe.nil?
  @safe || false
end
```

## Instance Method Details

###
  
    #**<=>**(other)  ⇒ Object 
  

  

  

  
    

Spaceship is priority [higher -> lower]

other - The class to be compared.

Returns -1, 0, 1.

```

79
80
81
```

```
# File 'lib/jekyll/plugin.rb', line 79

def <=>(other)
  self.class <=> other.class
end
```
