# Package org.apache.cxf.continuations

---

package org.apache.cxf.continuations

- 

Related Packages

Package
Description
org.apache.cxf

Contains the Bus, which is the central touch point of CXF, and its related classes.

- 

Class
Description
Continuation

Represents transport-neutral suspended invocation instances
 or continuations

ContinuationCallback

Callback that receives continuation status updates.

ContinuationProvider

Provides transport-neutral support for creating suspended invocation primitives
 or continuations

SuspendedInvocationException

Represents transport-specific exceptions which are used to indicate that
 a given invocation was suspended