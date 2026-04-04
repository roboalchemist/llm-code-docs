# Source: https://docs.velodb.io/cloud/4.x/sql-manual/sql-functions/scalar-functions/string-functions/concat

Version: 4.x

On this page

# CONCAT

## Description​

Concatenates multiple strings. Special cases:

  * If any of the parameter values ​​is NULL, the result returned is NULL

## Syntax​

    
    
    CONCAT ( <expr> [ , <expr> ... ] )  
    

## Parameters​

Parameter| Description| `<expr>`| The strings to be concatenated  
---|---  
  
## Return value​

Parameter list `<expr>` The strings to be concatenated. Special cases:

  * If any of the parameter values ​​is NULL, the result returned is NULL

## Example​

    
    
    SELECT  CONCAT("a", "b"),CONCAT("a", "b", "c"),CONCAT("a", null, "c")  
    
    
    
    +------------------+-----------------------+------------------------+  
    | concat('a', 'b') | concat('a', 'b', 'c') | concat('a', NULL, 'c') |  
    +------------------+-----------------------+------------------------+  
    | ab               | abc                   | NULL                   |  
    +------------------+-----------------------+------------------------+  
    

On This Page

  * Description
  * Syntax
  * Parameters
  * Return value
  * Example

