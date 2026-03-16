# Class: Capybara::RSpecMatchers::Matchers::CountableWrappedElementMatcher
  
  
  

  
  
    Inherits:
    
      WrappedElementMatcher
      
        

          
- Object
          
            
- Base
          
            
- WrappedElementMatcher
          
            
- Capybara::RSpecMatchers::Matchers::CountableWrappedElementMatcher
          
        

        show all
      
    
  
  

  
  
  
  
  
      Includes:
      CountSugar, SpatialSugar
  
  
  

  

  
  
    Defined in:
    lib/capybara/rspec/matchers/base.rb
  
  

  
## Direct Known Subclasses

  

HaveAncestor, HaveSelector, HaveSibling, HaveText

  
## Instance Attribute Summary

  
  
### Attributes inherited from Base

  

#failure_message, #failure_message_when_negated

  
  
  
  
  
  
  
## Method Summary

  
  
### Methods included from SpatialSugar

  

#above, #below, #left_of, #near, #right_of

  
  
  
  
  
  
  
  
  
### Methods included from CountSugar

  

#at_least, #at_most, #exactly, #once, #thrice, #times, #twice

  
  
  
  
  
  
  
  
  
### Methods inherited from WrappedElementMatcher

  

#does_not_match?, #matches?

  
  
  
  
  
  
  
  
  
### Methods inherited from Base

  

#initialize

  
  
  
  
  
  
  
  
  
### Methods included from Compound

  

#and, #and_then, #or

  
  
## Constructor Details

  
    

This class inherits a constructor from Capybara::RSpecMatchers::Matchers::Base