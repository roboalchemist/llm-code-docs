# Module: Conjur::LogSource
  
    Included in:
    API, BaseObject
  
  

  
  
    Defined in:
    lib/conjur/log_source.rb
  
## Overview

This module provides logging support for actions taken by the Conjur API.

#### Examples

```
class Example
  include LogSource

  def something_interesting param
    log{|l| l << "doing something interesting with #{param}"}

    # Do something interesting...
  end

end
# ...

Example.new.something_interesting 'foo'
# will log:
# [admin] doing something interesting with foo
```

##

      Instance Method Summary
      collapse
    

    

      
        
-
  
      #**log** {|logger| ... } 
    

    
  
  
  
  
  
  
  
  

  
    

Yield a logger to the block.

## Instance Method Details

###
  
    #**log** {|logger| ... } 
  

  

  

  
    

This method returns an undefined value.

Yield a logger to the block.  You should use the `<<` method to write to the
logger so that you don't send newlines or formatting.  The block will only be called
if Conjur.log is not nil.

The log format is `"[<username>]<messages logged in block>\n"`.

Yield Parameters:

-

        logger

        (#<<)
      
      
      
        —
        

a logger to write messages

```

50
51
52
53
54
55
56
57
58
```

```
# File 'lib/conjur/log_source.rb', line 50

def log(&block)
  if Conjur.log
    Conjur.log << "["
    Conjur.log << username
    Conjur.log << "] "
    yield Conjur.log
    Conjur.log << "\n"
  end
end
```
