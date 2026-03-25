# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/advanced-topics-pentaho-data-integration-overview/data-lineage/contribute-additional-step-and-job-entry-analyzers-to-the-pentaho-metaverse/examples/build-and-test-your-bundle.md

# Build and test your bundle

1. Build your bundle with Maven and have it installed into your local Maven repository. Once there, you can test it out in the Pentaho Server.

   ```xml
   mvn install
   ```
2. Start up Pentaho Data Integration in debug mode. Once started, `ssh` into the running karaf container. The `ssh` credentials are `karaf``/``karaf`.

   ```xml
   OPT="$OPT -Xdebug -Xnoagent -Djava.compiler=NONE -Xrunjdwp:transport=dt_socket,server=y,suspend=n,address=5005" ./spoon.sh
   # from another terminal window...
   ssh -p 8102 karaf@localhost
   # when prompted, password = karaf
   ```
3. Install your bundle from the Maven repository.

   ```xml
   # make sure the pentaho-metaverse feature is installed
   admin@root> features:list | grep pentaho-metaverse
   [installed  ] [7.1.0.0-12   ] pentaho-metaverse                      repo-0
   # install from local maven repository & start your bundle
   admin@root> install mvn:pentaho/sample-metaverse-bundle/7.1.0.0-12
   Bundle ID: 241
   admin@root> start 241
   Starting the bundle
   ```
