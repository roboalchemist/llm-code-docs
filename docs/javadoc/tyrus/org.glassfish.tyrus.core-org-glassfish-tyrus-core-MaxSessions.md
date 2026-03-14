Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Annotation Interface MaxSessions

---

@Retention(RUNTIME)
@Target(TYPE)
public @interface MaxSessions
This annotation may be used to annotate server endpoints as a optional annotation
 to `ServerEndpoint`. When number of maximal open
 sessions is exceeded every new attempt to open session is closed with
 `CloseReason.CloseCodes.TRY_AGAIN_LATER`.
 If value less then 1 is specified, no limit will be applied.
 Annotation example:

```

 @MaxSessions(100)
 @ServerEndpoint("/limited-resources")
 public class LimitedEndpoint {
 }
 
```

 Maximal number of open sessions can be also specified programmatically
 using `TyrusServerEndpointConfig.Builder.maxSessions(int)`.

Author:
Ondrej Kosatka

-

## Required Element Summary

Required Elements

Modifier and Type
Required Element
Description
`int`
`value`

Maximal number of open sessions.

-

## Element Details

-

### value

int value
Maximal number of open sessions.

Returns:
maximal number of open sessions.
