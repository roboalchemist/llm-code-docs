# Source: https://docs.pentaho.com/install/9.3-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-another-cache-framework/use-a-custom-segmentcache-spi.md

# Source: https://docs.pentaho.com/install/10.2-install/multidimensional-data-modeling-in-pentaho/mondrian-cache-control/switch-to-another-cache-framework/use-a-custom-segmentcache-spi.md

# Use a Custom SegmentCache SPI

If you want to develop your own implementation of the **SegmentCache SPI**, you will have to follow the basic plan presented in this article.

Perform the following steps to develop your implementation:

1. Create a Java class that implements **mondrian.spi.SegmentCache**.
2. Compile your class and make it available in Mondrian’s classpath.
3. Edit `mondrian.properties` and set **mondrian.olap.SegmentCache** to your class name.
4. Start the Pentaho Server or Mondrian engine.

This is only a high-level overview. If you need more specific advice, contact your Pentaho support representative and inquire about developer assistance.
