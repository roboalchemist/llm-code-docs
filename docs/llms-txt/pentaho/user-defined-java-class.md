# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/user-defined-java-class.md

# User Defined Java Class

You can use the User Defined Java Class step to enter your own Java class to drive the functionality of a complete step. You can program your own plugin into a step, yet the goal of this step is not to do full-scale Java development inside of a step. A whole plugin system is available to help with that part (see the **Administer Pentaho Data Integration and Analytics** document). The goal is for you to just define Java methods and logic. For this step, the [Janino](https://janino-compiler.github.io/janino/apidocs/) project libraries are used to compile Java code in the form of classes at runtime.
