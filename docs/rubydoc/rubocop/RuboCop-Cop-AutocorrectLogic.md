# Module: RuboCop::Cop::AutocorrectLogic
  
    Included in:
    Base
  
  

  
  
    Defined in:
    lib/rubocop/cop/autocorrect_logic.rb
  
## Overview

This module encapsulates the logic for autocorrect behavior for a cop.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**autocorrect?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**autocorrect_enabled?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**autocorrect_requested?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**autocorrect_with_disable_uncorrectable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**correctable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**disable_uncorrectable?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**safe_autocorrect?**  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**autocorrect?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

7
8
9
```

```
# File 'lib/rubocop/cop/autocorrect_logic.rb', line 7

def autocorrect?
  autocorrect_requested? && correctable? && autocorrect_enabled?
end
```

###
  
    #**autocorrect_enabled?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

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
```

```
# File 'lib/rubocop/cop/autocorrect_logic.rb', line 31

def autocorrect_enabled?
  # allow turning off autocorrect on a cop by cop basis
  return true unless cop_config

  # `false` is the same as `disabled` for backward compatibility.
  return false if ['disabled', false].include?(cop_config['AutoCorrect'])

  # When LSP is enabled or the `--editor-mode` option is on, it is considered as editing
  # source code, and autocorrection with `AutoCorrect: contextual` will not be performed.
  return false if contextual_autocorrect? && LSP.enabled?

  # :safe_autocorrect is a derived option based on several command-line
  # arguments - see RuboCop::Options#add_autocorrection_options
  return safe_autocorrect? if @options.fetch(:safe_autocorrect, false)

  true
end
```

###
  
    #**autocorrect_requested?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

15
16
17
```

```
# File 'lib/rubocop/cop/autocorrect_logic.rb', line 15

def autocorrect_requested?
  @options.fetch(:autocorrect, false)
end
```

###
  
    #**autocorrect_with_disable_uncorrectable?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

11
12
13
```

```
# File 'lib/rubocop/cop/autocorrect_logic.rb', line 11

def autocorrect_with_disable_uncorrectable?
  autocorrect_requested? && disable_uncorrectable? && autocorrect_enabled?
end
```

###
  
    #**correctable?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

19
20
21
```

```
# File 'lib/rubocop/cop/autocorrect_logic.rb', line 19

def correctable?
  self.class.support_autocorrect? || disable_uncorrectable?
end
```

###
  
    #**disable_uncorrectable?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

23
24
25
```

```
# File 'lib/rubocop/cop/autocorrect_logic.rb', line 23

def disable_uncorrectable?
  @options[:disable_uncorrectable] == true
end
```

###
  
    #**safe_autocorrect?**  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

27
28
29
```

```
# File 'lib/rubocop/cop/autocorrect_logic.rb', line 27

def safe_autocorrect?
  cop_config.fetch('Safe', true) && cop_config.fetch('SafeAutoCorrect', true)
end
```
