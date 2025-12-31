# Source: https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder.md.txt

# Fabric.Builder

public static class **Fabric.Builder** extends Object  
Fluent API for creating [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) instances.  

### Public Constructor Summary

|---|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#Fabric.Builder(android.content.Context))(Context context) Start building a new [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) instance. |

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [appIdentifier](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#appIdentifier(java.lang.String))(String appIdentifier) Sets the Application Identifier to build with.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [appInstallIdentifier](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#appInstallIdentifier(java.lang.String))(String appInstallIdentifier) Sets the Application Install Identifier to build with                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)                 | [build](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#build())() Build the fabric instance                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [debuggable](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#debuggable(boolean))(boolean enabled) Enable Logging                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [executorService](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#executorService(java.util.concurrent.ExecutorService))(ExecutorService executorService) *This method was deprecated. Use [threadPoolExecutor(io.fabric.sdk.android.services.concurrency.PriorityThreadPoolExecutor)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#threadPoolExecutor(io.fabric.sdk.android.services.concurrency.PriorityThreadPoolExecutor))*                                                                                                                   |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [handler](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#handler(android.os.Handler))(Handler handler) *This method was deprecated. this always uses the main handler*                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [initializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#initializationCallback(io.fabric.sdk.android.InitializationCallback<io.fabric.sdk.android.Fabric>))([InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)\<[Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)\> initializationCallback) Specify the [InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)to build with |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [kits](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#kits(io.fabric.sdk.android.Kit...))([Kit...](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) kits) Sets the [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) array to build with.                                                                                                                                                                                                                                                                             |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#logger(io.fabric.sdk.android.Logger))([Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger) logger) Sets the [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger) to build with.                                                                                                                                                                                                                                                                    |
| [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder) | [threadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#threadPoolExecutor(io.fabric.sdk.android.services.concurrency.PriorityThreadPoolExecutor))([PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) threadPoolExecutor) Sets the [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) to build with.                                                             |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Constructors

#### public
**Fabric.Builder**
(Context context)

Start building a new [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric) instance.  

##### Parameters

|---------|---|
| context |   |

## Public Methods

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**appIdentifier**
(String appIdentifier)

Sets the Application Identifier to build with.
This allows Fabric to report to another application in your organization. This must be
set to an app identifier (package name) that has already been onboarded into the Fabric
backend. This is usually your main package name
ex: "com.example" has been onboarded into fabric.io and crashes from "com.example.free"
should be reported to "com.example" as well  

##### Parameters

|---------------|---|
| appIdentifier |   |

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**appInstallIdentifier**
(String appInstallIdentifier)

Sets the Application Install Identifier to build with  

##### Parameters

|----------------------|---|
| appInstallIdentifier |   |

#### public [Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)
**build**
()

Build the fabric instance  

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**debuggable**
(boolean enabled)

Enable Logging  

##### Parameters

|---------|---|
| enabled |   |

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**executorService**
(ExecutorService executorService)


**This method was deprecated.**   
Use [threadPoolExecutor(io.fabric.sdk.android.services.concurrency.PriorityThreadPoolExecutor)](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder#threadPoolExecutor(io.fabric.sdk.android.services.concurrency.PriorityThreadPoolExecutor))  
<br />

##### Parameters

|-----------------|---|
| executorService |   |

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**handler**
(Handler handler)


**This method was deprecated.**   
this always uses the main handler  
<br />

##### Parameters

|---------|---|
| handler |   |

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**initializationCallback**
([InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)\<[Fabric](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric)\> initializationCallback)

Specify the [InitializationCallback](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/InitializationCallback)to build with  

##### Parameters

|------------------------|---|
| initializationCallback |   |

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**kits**
([Kit...](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) kits)

Sets the [Kit](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Kit) array to build with.  

##### Parameters

|------|---|
| kits |   |

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**logger**
([Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger) logger)

Sets the [Logger](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Logger) to build with.  

##### Parameters

|--------|---|
| logger |   |

#### public [Fabric.Builder](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/Fabric.Builder)
**threadPoolExecutor**
([PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) threadPoolExecutor)

Sets the [PriorityThreadPoolExecutor](https://firebase.google.com/docs/reference/android/io/fabric/sdk/android/fabric/services/concurrency/PriorityThreadPoolExecutor) to build with.  

##### Parameters

|--------------------|---|
| threadPoolExecutor |   |