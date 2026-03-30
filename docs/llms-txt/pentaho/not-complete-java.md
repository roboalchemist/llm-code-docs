# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/not-complete-java.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/not-complete-java.md

# Not complete Java

Janino and this step do not need the complete Java class. It only needs the class body (such as the imports, constructors, and methods). The step does not need the full class declaration. This step was designed with this approach, over the definition of the full class, to hide technical details and methods for ease of use.

You enter your main code into the [Processor](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class/process-rows), which defines the `processRow()` method. In PDI, the following imports are already a part of the Processor code:

* `org.pentaho.di.trans.steps.userdefinedjavaclass.*`
* `org.pentaho.di.trans.step.*`
* `org.pentaho.di.core.row.*`
* `org.pentaho.di.core.*`
* `org.pentaho.di.core.exception.*`

The imports listed above are only a part of the Processor code. They are not a part of any code blocks you might enter into additional [Class code tabs](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class).

If you need to add other imports to your Processor code, include them at the very top of the code you will create for this step, as shown in the following example:

```java
import java.util.*;
```

Janino, essentially a Java complier, only supports a sub-set of the Java 1.8.x specification. To see a complete list of the features and limitations, see the [Janino](http://janino-compiler.github.io/janino/) homepage.
