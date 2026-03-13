# Source: https://docs.logrocket.com/docs/mobile-crash-types.md

# Mobile Crash Types

We detect and capture stack trace details for the following crash types. To see de-obfuscated stack traces, upload mapping files using instructions or [Android](https://docs.logrocket.com/reference/stack-traces-android), [iOS](https://docs.logrocket.com/reference/stack-traces-ios), and [React Native](https://docs.logrocket.com/reference/stack-traces-react-native).

**Android**

* Uncaught Exceptions (Java) ✅

**iOS**

* Uncaught Objective-C NS Exceptions ✅
* Mach Kernel Exceptions [(iOS SDK version >=1.29.0)](https://docs.logrocket.com/docs/mobile-sdk-changelog#1290-2024-01-23) ✅
  * Mach Kernel Crash Details ([iOS SDK version >=1.30.1](https://docs.logrocket.com/docs/mobile-sdk-changelog#1301-2024-01-31)) ✅
  * Note that Signal (fatal error) is captured by mach kernel exception monitoring
* C++ Exceptions ([iOS SDK version >=1.30.2](https://docs.logrocket.com/docs/mobile-sdk-changelog#1302-2024-02-02)) ✅
  * Note that C++ Crash Stack Traces are [not supported by Apple](https://developer.apple.com/documentation/xcode/addressing-language-exception-crashes).