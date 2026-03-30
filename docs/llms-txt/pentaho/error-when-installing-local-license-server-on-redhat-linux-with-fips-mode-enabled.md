# Source: https://docs.pentaho.com/install/10.2-install/pentaho-installation-overview-cp/installation-and-upgrade-issues/error-when-installing-local-license-server-on-redhat-linux-with-fips-mode-enabled.md

# Error when installing local license server on Redhat Linux in FIPS mode

If you are installing a local license server on Redhat Linux with FIPS mode enabled you might see the following error:

```
$ sudo ./install-systemd.sh
Exception in thread "main" java.lang.reflect.InvocationTargetException
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
        at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:77)
        at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
        at java.base/java.lang.reflect.Method.invoke(Method.java:569)
        at org.springframework.boot.loader.launch.Launcher.launch(Launcher.java:102)
        at org.springframework.boot.loader.launch.Launcher.launch(Launcher.java:64)
        at org.springframework.boot.loader.launch.JarLauncher.main(JarLauncher.java:40)
Caused by: java.lang.ExceptionInInitializerError
        at com.flexnet.lm.a.h.<clinit>(SourceFile:27)
        at com.flexnet.lm.binary.PublisherIdentityRecord.a(SourceFile:426)
        at com.flexnet.lm.binary.PublisherIdentityRecord.<init>(SourceFile:36)
        at com.flexnet.lm.binary.PublisherSettingsRecord.getPublisherIdentity(SourceFile:78)
        at com.flexnet.glservice.PublisherConfigurationReader.e(PublisherConfigurationReader.java:44)
        at com.flexnet.glservice.PublisherConfigurationReader.l(PublisherConfigurationReader.java:10)
        at com.flexnet.glservice.main.b.<init>(b.java:371)
        at com.flexnet.glservice.main.Main.main(Main.java:100)
        ... 7 more
Caused by: java.lang.RuntimeException: java.security.NoSuchAlgorithmException: SHA1PRNG SecureRandom not available
        at com.flexnet.lm.a.d.<clinit>(SourceFile:37)
        ... 15 more
Caused by: java.security.NoSuchAlgorithmException: SHA1PRNG SecureRandom not available
        at java.base/sun.security.jca.GetInstance.getInstance(GetInstance.java:159)
        at java.base/java.security.SecureRandom.getInstance(SecureRandom.java:387)
        at com.flexnet.lm.a.d.<clinit>(SourceFile:33)
        ... 15 more
./install-functions.sh: line 281: error: command not found
Terminated
```

To fix this error, configure Java as described in the following articles:

* [Configuring Red Hat build of OpenJDK 11 on RHEL with FIPS](https://docs.redhat.com/en/documentation/red_hat_build_of_openjdk/11/html-single/configuring_red_hat_build_of_openjdk_11_on_rhel_with_fips/index)
* [Configuring Red Hat build of OpenJDK 17 on RHEL with FIPS](https://docs.redhat.com/en/documentation/red_hat_build_of_openjdk/17/html-single/configuring_red_hat_build_of_openjdk_17_on_rhel_with_fips/index#proc-providing-feedback-on-redhat-documentation)
