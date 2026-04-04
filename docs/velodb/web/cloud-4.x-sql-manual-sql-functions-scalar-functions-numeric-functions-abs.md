# Source: https://docs.velodb.io/cloud/4.x/sql-manual/sql-functions/scalar-functions/numeric-functions/abs

Version: 4.x

On this page

# ABS

## Description​

Returns the absolute value of `x`

## Syntax​

    
    
    ABS(<x>)   
    

## Parameters​

Parameter| Description| `<x>`| The value for which the absolute value is to be
calculated  
---|---  
  
## Return Value​

The absolute value of parameter `x`.

## Example​

    
    
    select abs(-2);  
    
    
    
    +---------+  
    | abs(-2) |  
    +---------+  
    |       2 |  
    +---------+  
    
    
    
    select abs(3.254655654);  
    
    
    
    +------------------+  
    | abs(3.254655654) |  
    +------------------+  
    |      3.254655654 |  
    +------------------+  
    
    
    
    select abs(-3254654236547654354654767);  
    
    
    
    +---------------------------------+  
    | abs(-3254654236547654354654767) |  
    +---------------------------------+  
    | 3254654236547654354654767       |  
    +---------------------------------+  
    

On This Page

  * Description
  * Syntax
  * Parameters
  * Return Value
  * Example

