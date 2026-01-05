# Source: https://docs.velodb.io/cloud/4.x/sql-manual/sql-functions/scalar-functions/numeric-functions/acos

Version: 4.x

On this page

# ACOS

## Description​

Returns the arc cosine of `x`, or `NULL` if `x` is not in the range `-1` to
`1`.

## Syntax​

    
    
    ACOS(<x>)  
    

## Parameters​

Parameter| Description| `<x>`| The value for which the acos value is to be
calculated  
---|---  
  
## Return Value​

The acos value of parameter `x`.

## Example​

    
    
    select acos(1);  
    
    
    
    +-----------+  
    | acos(1.0) |  
    +-----------+  
    |         0 |  
    +-----------+  
    
    
    
    select acos(0);  
    
    
    
    +--------------------+  
    | acos(0.0)          |  
    +--------------------+  
    | 1.5707963267948966 |  
    +--------------------+  
    
    
    
    select acos(-2);  
    
    
    
    +------------+  
    | acos(-2.0) |  
    +------------+  
    |        nan |  
    +------------+  
    

On This Page

  * Description
  * Syntax
  * Parameters
  * Return Value
  * Example

