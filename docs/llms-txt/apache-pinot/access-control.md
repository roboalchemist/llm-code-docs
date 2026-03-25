# Source: https://docs.pinot.apache.org/release-0.4.0/operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-0.9.0/operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-0.10.0/operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-0.11.0/operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-0.12.0/operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-0.12.1/operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-1.0.0/for-operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-1.1.0/for-operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-1.2.0/for-operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-1.3.0/for-operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/release-1.4.0/for-operators/operating-pinot/access-control.md

# Source: https://docs.pinot.apache.org/operators/operating-pinot/access-control.md

# Access Control

Access control can be set up at various points in Pinot, such as controller endpoints and broker query endpoints. By default we will use [AllowAllAccessFactory](https://github.com/apache/pinot/blob/master/pinot-controller/src/main/java/org/apache/pinot/controller/api/access/AllowAllAccessFactory.java) and hence not be enforcing any access controls. You can add access control by implementing the [AccessControlFactory](https://github.com/apache/pinot/blob/master/pinot-controller/src/main/java/org/apache/pinot/controller/api/access/AccessControlFactory.java) interface.

The access control factory can be configured in the controller configs by setting the fully qualified class name of the AccessControlFactory in the property `controller.admin.access.control.factory.class`

The access control factory can be configured in the broker configs by setting the fully qualified class name of the AccessControlFactory in the property `pinot.broker.access.control.class`. Any other properties required for initializing the factory can be set in the broker configs as properties with the prefix `pinot.broker.access.control`.
