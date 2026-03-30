# Source: https://docs.silabs.com/openthread/3.0.0/using-co-processor-communication-daemon/05-considerations.md

# Considerations

- The SPI driver uses a **sysfs** class GPIO as a chip select. Make sure the daemon has the proper permissions to access this GPIO.
- If the provided GPIO for the SPI chip select is already used by another driver, it needs to be deactivated and enabled as standard GPIO. In Linux this is usually done via the device tree.
- CPCd uses Unix sockets to exchange information with the Linux applications that use the CPC library. These sockets are stored under /etc/cpcd. Only users with the appropriate permissions should be able to access these sockets. CPCd inherits the permission of the user who starts the CPC daemon.
- Make sure no other application is using the serial bus at the same time as CPCd.
- Sensitive information can be exposed when tracing to a file is enable. Only enable tracing during development, for debugging purposes only. Refer to the TRACE_TO_FILE and STDOUT_TRACE configurations.