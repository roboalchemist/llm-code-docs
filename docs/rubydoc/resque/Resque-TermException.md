# Exception: Resque::TermException
  
  
  

  
  
    Inherits:
    
      SignalException
      
        

          
- Object
          
            
- SignalException
          
            
- Resque::TermException
          
        

        show all
      
    
  
  

  
  
  
  
  

  

  
  
    Defined in:
    lib/resque/errors.rb
  
  

## Overview

  
    

Raised when child process is TERM’d so job can rescue this to do shutdown work.