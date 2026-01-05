# Source: https://docs.velodb.io/cloud/4.x/sql-manual/sql-functions/scalar-functions/string-functions/length

Version: 4.x

On this page

# LENGTH

## Description​

Returns the number of bytes in a string.

## Syntax​

    
    
    LENGTH ( <str> )  
    

## Parameters​

Parameter| Description| `<str>`| The string whose bytes need to be calculated  
---|---  
  
## Return Value​

The number of bytes in the string `<str>`.

## Example​

    
    
    SELECT LENGTH("abc"),length("中国")  
    
    
    
    +---------------+------------------+  
    | length('abc') | length('中国')   |  
    +---------------+------------------+  
    |             3 |                6 |  
    +---------------+------------------+  
    

On This Page

  * Description
  * Syntax
  * Parameters
  * Return Value
  * Example

