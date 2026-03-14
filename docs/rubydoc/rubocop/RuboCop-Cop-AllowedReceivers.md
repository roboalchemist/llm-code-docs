# Module: RuboCop::Cop::AllowedReceivers
  
    Included in:
    Lint::UselessDefaultValueArgument, Style::CollectionCompact, Style::HashEachMethods
  
  

  
  
    Defined in:
    lib/rubocop/cop/mixin/allowed_receivers.rb
  
## Overview

This module encapsulates the ability to allow certain receivers in a cop.

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**allowed_receiver?**(receiver)  ⇒ Boolean 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**allowed_receivers**  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
        
-
  
      #**receiver_name**(receiver)  ⇒ Object 
    

    
  
  
  
  
  
  
  
  

  
    
  

      
    

  

  
    
## Instance Method Details

###
  
    #**allowed_receiver?**(receiver)  ⇒ Boolean 
  

  

  

  
    

Returns:

-

        (Boolean)

```

7
8
9
10
11
```

```
# File 'lib/rubocop/cop/mixin/allowed_receivers.rb', line 7

def allowed_receiver?(receiver)
  receiver_name = receiver_name(receiver)

  allowed_receivers.include?(receiver_name)
end
```

###
  
    #**allowed_receivers**  ⇒ Object 
  

  

  

  
    
      

```

29
30
31
```

```
# File 'lib/rubocop/cop/mixin/allowed_receivers.rb', line 29

def allowed_receivers
  cop_config.fetch('AllowedReceivers', [])
end
```

###
  
    #**receiver_name**(receiver)  ⇒ Object 
  

  

  

  
    
      

```

13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
```

```
# File 'lib/rubocop/cop/mixin/allowed_receivers.rb', line 13

def receiver_name(receiver)
  if receiver.receiver && !receiver.receiver.const_type?
    return receiver_name(receiver.receiver)
  end

  if receiver.send_type?
    if receiver.receiver
      "#{receiver_name(receiver.receiver)}.#{receiver.method_name}"
    else
      receiver.method_name.to_s
    end
  else
    receiver.source
  end
end
```
