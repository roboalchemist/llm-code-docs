# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class/logging.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/abort/logging.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class/general-user-defined-java-class/class-code-user-defined-java-class/logging.md

# Logging

You need to implement logging in your defined step if you want PDI to log data actions from your class, such as read, write, output, or update data. The following code is an example of how to implement logging:

```java
putRow( data.outputMeta, r );

if ( checkFeedback( getLinesOutput() ) ) {
  if ( log.isBasic() ) {
    logBasic( "Have I got rows for you! " + getLinesOutput() );
  }
}
```
