# Source: https://docs.logrocket.com/reference/android-capturing-logs.md

# Capture Application Logs

Surface application logs in LogRocket sessions

As with network requests, the LogRocket Android SDK does not automatically capture logs from the `android.util.Log` interface. Logs can be manually registered to the session using the `com.logrocket.core.Logger` utility:

```java
import com.logrocket.core.Logger;

Logger.e(String tag, String msg);
Logger.w(String tag, String msg);
Logger.i(String tag, String msg);
Logger.d(String tag, String msg);
Logger.captureException(Throwable error);
```