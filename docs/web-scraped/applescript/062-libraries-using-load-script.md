# Libraries using Load Script

OS X Mavericks v10.9 (AppleScript 2.3) introduces built-in support for script libraries, which are scripts containing handlers that may be shared among many scripts. Scripts that must run on older versions of the OS can share handlers between scripts usingload script, as described here.

## Saving and Loading Libraries of Handlers
In addition to defining and calling handlers within a script, you can access handlers from other scripts. To make a handler available to another script, save it as a compiled script, then use theload scriptcommand to load it in any script that needs to call the handler. You can use this technique to create libraries containing many handlers.
Note:Theload scriptcommand loads the compiled script as ascriptobject; for more information, seeScript Objects.
For example, the following script contains two handlers:areaOfCircleandfactorial:

```applescript
-- This handler computes the area of a circle from its radius.
```

```applescript
-- (The area of a circle is equal to pi times its radius squared.)
```

```applescript
on areaOfCircle from radius
```

```applescript
    -- Make sure the parameter is a real number or an integer.
```

```applescript
    if class of radius is contained by {integer, real}
```

```applescript
        return radius * radius * pi -- pi is predefined by AppleScript.
```

```applescript
    else
```

```applescript
        error "The parameter must be a real number or an integer"
```

```applescript
    end if
```

```applescript
end areaOfCircle
```

```applescript
 
```

```applescript
 
```

```applescript
-- This handler returns the factorial of a number.
```

```applescript
on factorial(x)
```

```applescript
    set returnVal to 1
```

```applescript
    if x > 1 then
```

```applescript
        repeat with n from 2 to x
```

```applescript
            set returnVal to returnVal * n
```

```applescript
        end repeat
```

```applescript
    end if
```

```applescript
    return returnVal
```

```applescript
end factorial
```

In Script Editor, save the script as a compiled Script (which has extensionscpt) or Script Bundle (extensionscptd) and name it âNumberLibâ.
After saving the script as a compiled script, other scripts can use theload scriptcommand to load it. For example, the following script loads the compiled scriptNumberLib.scpt, storing the resultingscriptobject in the variablenumberLib. It then makes handler calls within atellstatement that targets thescriptobject. The compiled script must exist in the specified location for this script to work.

```applescript
set numberLibrary to (load script file "NumberLib.scpt")
```

```applescript
 
```

```applescript
tell numberLibrary
```

```applescript
    factorial(10)             --result: 3628800
```

```applescript
    areaOfCircle from 12      --result: 452.38934211693
```

```applescript
end tell
```

Copyright © 2016 Apple Inc. All Rights Reserved.Terms of Use|Privacy Policy|  Updated: 2016-01-25