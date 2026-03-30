# Source: https://learn.microsoft.com/en-us/dotnet/framework/windows-services/walkthrough-creating-a-windows-service-application-in-the-component-designer

Title: Tutorial: Create a Windows service app - .NET Framework

URL Source: https://learn.microsoft.com/en-us/dotnet/framework/windows-services/walkthrough-creating-a-windows-service-application-in-the-component-designer

Markdown Content:
This article demonstrates how to create a .NET Framework Windows service app in Visual Studio. The service simply writes messages to an event log.

To begin, create the project and set the values that are required for the service to function correctly.

1. From the Visual Studio **File** menu, select **New**>**Project** (or press Ctrl+Shift+N) to open the **New Project** window.

2. Find and select the **Windows Service (.NET Framework)** project template.

Note

If you don't see the **Windows Service** template, you might need to install the **.NET desktop development** workload using Visual Studio Installer.
3.   For **Project name**, enter _MyNewService_, and then select **Create**.

The **Design** tab appears (**Service1.cs [Design]** or **Service1.vb [Design]**).

The project template includes a component class named `Service1` that inherits from [System.ServiceProcess.ServiceBase](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase). It includes much of the basic service code, such as the code to start the service.

Rename the service from **Service1** to **MyNewService**.

1. In **Solution Explorer**, select **Service1.cs** or **Service1.vb**, and choose **Rename** from the shortcut menu. Rename the file to **MyNewService.cs** or **MyNewService.vb**, and then press Enter.

A pop-up window appears asking whether you would like to rename all references to the code element _Service1_.

1. In the pop-up window, select **Yes**.

![Image 1: Rename prompt](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/media/windows-service-rename.png)

1. Select **Save All** from the **File** menu.

In this section, you add a custom event log to the Windows service. The [EventLog](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.eventlog) component is an example of the type of component you can add to a Windows service.

1. In the **Toolbox** window, expand **Components**, and then drag the **EventLog** component to the **Service1.cs [Design]** or **Service1.vb [Design]** designer.

Tip

If you don't see the Toolbox window, select **View**>**Toolbox**.
2.   In **Solution Explorer**, from the shortcut menu for **MyNewService.cs** or **MyNewService.vb**, choose **View Code**.

1. Define a custom event log.

For C#, edit the existing `MyNewService()` constructor as shown in the following code snippet. For Visual Basic, add the `New()` constructor as shown in the following code snippet.

```
public MyNewService()
{
    InitializeComponent();
    eventLog1 = new EventLog();
    if (!EventLog.SourceExists("MySource"))
    {
        EventLog.CreateEventSource("MySource", "MyNewLog");
    }
    eventLog1.Source = "MySource";
    eventLog1.Log = "MyNewLog";
}
```
1. If it doesn't already exist, add a `using` directive to **MyNewService.cs**, or an `Imports` statement to **MyNewService.vb**, for the [System.Diagnostics](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics) namespace:

```
using System.Diagnostics;
```
1. Select **Save All** from the **File** menu.

In the code editor for **MyNewService.cs** or **MyNewService.vb**, locate the [OnStart](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.onstart) method. Visual Studio automatically created an empty method definition when you created the project. Add code that writes an entry to the event log when the service starts:

```
protected override void OnStart(string[] args)
{
    eventLog1.WriteEntry("In OnStart.");
}
```

Because a service application is designed to be long-running, it usually polls or monitors the system, which you set up in the [OnStart](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.onstart) method. The `OnStart` method must return to the operating system after the service's operation has begun so that the system isn't blocked.

To set up a simple polling mechanism, use the [System.Timers.Timer](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer) component. The timer raises an [Elapsed](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer.elapsed#system-timers-timer-elapsed) event at regular intervals, at which time your service can do its monitoring. You use the [Timer](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer) component as follows:

* Set the properties of the [Timer](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer) component in the `MyNewService.OnStart` method.
* Start the timer by calling the [Start](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer.start) method.

1. Add a `using` directive to **MyNewService.cs**, or an `Imports` statement to **MyNewService.vb**, for the [System.Timers](https://learn.microsoft.com/en-us/dotnet/api/system.timers) namespace:

```
using System.Timers;
```
1. Add the following code in the `MyNewService.OnStart` event to set up the polling mechanism:

```
// Set up a timer that triggers every minute.
Timer timer = new Timer
{
    Interval = 60000 // 60 seconds
};
timer.Elapsed += new ElapsedEventHandler(this.OnTimer);
timer.Start();
```
1. In the `MyNewService` class, add a member variable. It contains the identifier of the next event to write into the event log:

```
private int eventId = 1;
```
1. In the `MyNewService` class, add the `OnTimer` method to handle the [Timer.Elapsed](https://learn.microsoft.com/en-us/dotnet/api/system.timers.timer.elapsed#system-timers-timer-elapsed) event:

```
public void OnTimer(object sender, ElapsedEventArgs args)
{
    // TODO: Insert monitoring activities here.
    eventLog1.WriteEntry("Monitoring the System", EventLogEntryType.Information, eventId++);
}
```

Instead of running all your work on the main thread, you can run tasks by using background worker threads. For more information, see [System.ComponentModel.BackgroundWorker](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.backgroundworker).

Insert a line of code in the [OnStop](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.onstop) method that adds an entry to the event log when the service is stopped:

```
protected override void OnStop()
{
    eventLog1.WriteEntry("In OnStop.");
}
```

You can override the [OnPause](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.onpause), [OnContinue](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.oncontinue), and [OnShutdown](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.onshutdown) methods to define additional processing for your component.

The following code shows how you can override the [OnContinue](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.oncontinue) method in the `MyNewService` class:

```
protected override void OnContinue()
{
    eventLog1.WriteEntry("In OnContinue.");
}
```

Services report their status to the [Service Control Manager](https://learn.microsoft.com/en-us/windows/desktop/Services/service-control-manager) so that a user can tell whether a service is functioning correctly. By default, a service that inherits from [ServiceBase](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase) reports a limited set of status settings, which include `SERVICE_STOPPED`, `SERVICE_PAUSED`, and `SERVICE_RUNNING`. If a service takes a while to start up, it's useful to report a `SERVICE_START_PENDING` status.

You can implement the `SERVICE_START_PENDING` and `SERVICE_STOP_PENDING` status settings by adding code that calls the Windows [SetServiceStatus](https://learn.microsoft.com/en-us/windows/desktop/api/winsvc/nf-winsvc-setservicestatus) function.

1. Add a `using` directive to **MyNewService.cs**, or an `Imports` statement to **MyNewService.vb**, for the [System.Runtime.InteropServices](https://learn.microsoft.com/en-us/dotnet/api/system.runtime.interopservices) namespace:

```
using System.Runtime.InteropServices;
```
1. Add the following enumeration and structure to **MyNewService.cs**, or **MyNewService.vb**, to declare the `ServiceState` values and to add a structure for the status, which you'll use in a platform invoke call:

```
public enum ServiceState
{
    SERVICE_STOPPED = 0x00000001,
    SERVICE_START_PENDING = 0x00000002,
    SERVICE_STOP_PENDING = 0x00000003,
    SERVICE_RUNNING = 0x00000004,
    SERVICE_CONTINUE_PENDING = 0x00000005,
    SERVICE_PAUSE_PENDING = 0x00000006,
    SERVICE_PAUSED = 0x00000007,
}

[StructLayout(LayoutKind.Sequential)]
public struct ServiceStatus
{
    public int dwServiceType;
    public ServiceState dwCurrentState;
    public int dwControlsAccepted;
    public int dwWin32ExitCode;
    public int dwServiceSpecificExitCode;
    public int dwCheckPoint;
    public int dwWaitHint;
};
```

Note

The Service Control Manager uses the `dwWaitHint` and `dwCheckpoint` members of the [SERVICE_STATUS structure](https://learn.microsoft.com/en-us/windows/win32/api/winsvc/ns-winsvc-service_status) to determine how much time to wait for a Windows service to start or shut down. If your `OnStart` and `OnStop` methods run long, your service can request more time by calling `SetServiceStatus` again with an incremented `dwCheckPoint` value.
3.   In the `MyNewService` class, declare the [SetServiceStatus](https://learn.microsoft.com/en-us/windows/desktop/api/winsvc/nf-winsvc-setservicestatus) function by using [platform invoke](https://learn.microsoft.com/en-us/dotnet/framework/interop/consuming-unmanaged-dll-functions):

```
[DllImport("advapi32.dll", SetLastError = true)]
private static extern bool SetServiceStatus(System.IntPtr handle, ref ServiceStatus serviceStatus);
```
1. To implement the `SERVICE_START_PENDING` status, add the following code to the beginning of the [OnStart](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.onstart) method:

```
// Update the service state to Start Pending.
ServiceStatus serviceStatus = new ServiceStatus
{
    dwCurrentState = ServiceState.SERVICE_START_PENDING,
    dwWaitHint = 100000
};
SetServiceStatus(this.ServiceHandle, ref serviceStatus);
```
1. Add code to the end of the `OnStart` method to set the status to `SERVICE_RUNNING`:

```
// Update the service state to Running.
serviceStatus.dwCurrentState = ServiceState.SERVICE_RUNNING;
SetServiceStatus(this.ServiceHandle, ref serviceStatus);
```
1. (Optional) If [OnStop](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicebase.onstop) is a long-running method, repeat this procedure in the `OnStop` method. Implement the `SERVICE_STOP_PENDING` status and return the `SERVICE_STOPPED` status before the `OnStop` method exits.

For example:

```
// Update the service state to Stop Pending.
ServiceStatus serviceStatus = new ServiceStatus
{
    dwCurrentState = ServiceState.SERVICE_STOP_PENDING,
    dwWaitHint = 100000
};
SetServiceStatus(this.ServiceHandle, ref serviceStatus);

// Update the service state to Stopped.
serviceStatus.dwCurrentState = ServiceState.SERVICE_STOPPED;
SetServiceStatus(this.ServiceHandle, ref serviceStatus);
```

Before you run a Windows service, you need to install it, which registers it with the Service Control Manager. Add installers to your project to handle the registration details.

1. In **Solution Explorer**, from the shortcut menu for **MyNewService.cs** or **MyNewService.vb**, choose **View Designer**.

2. In the **Design** view, select the background area, then choose **Add Installer** from the shortcut menu.

By default, Visual Studio adds a component class named `ProjectInstaller`, which contains two installers, to your project. These installers are for your service and for the service's associated process.

1. In the **Design** view for **ProjectInstaller**, select **serviceInstaller1** for a C# project, or **ServiceInstaller1** for a Visual Basic project, then choose **Properties** from the shortcut menu.

2. In the **Properties** window, set the [ServiceName](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceinstaller.servicename#system-serviceprocess-serviceinstaller-servicename) property to **MyNewService**.

3. Add text to the [Description](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceinstaller.description#system-serviceprocess-serviceinstaller-description) property, such as _A sample service_.

This text appears in the **Description** column of the **Services** window and describes the service to the user.

![Image 2: Service description in the Services window.](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/media/windows-service-description.png)

1. Add text to the [DisplayName](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceinstaller.displayname#system-serviceprocess-serviceinstaller-displayname) property. For example, _MyNewService Display Name_.

This text appears in the **Display Name** column of the **Services** window. This name can be different from the [ServiceName](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceinstaller.servicename#system-serviceprocess-serviceinstaller-servicename) property, which is the name the system uses (for example, the name you use for the `net start` command to start your service).

1. Set the [StartType](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceinstaller.starttype#system-serviceprocess-serviceinstaller-starttype) property to [Automatic](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicestartmode#system-serviceprocess-servicestartmode-automatic) from the drop-down list.

2. When you're finished, the **Properties** windows should look like the following figure:

![Image 3: Installer Properties for a Windows service](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/media/windows-service-installer-properties.png)

1. In the **Design** view for **ProjectInstaller**, choose **serviceProcessInstaller1** for a C# project, or **ServiceProcessInstaller1** for a Visual Basic project, then choose **Properties** from the shortcut menu. Set the [Account](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceprocessinstaller.account#system-serviceprocess-serviceprocessinstaller-account) property to [LocalSystem](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceaccount#system-serviceprocess-serviceaccount-localsystem) from the drop-down list.

This setting installs the service and runs it by using the local system account.

Important

The [LocalSystem](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceaccount#system-serviceprocess-serviceaccount-localsystem) account has broad permissions, including the ability to write to the event log. Use this account with caution, because it might increase your risk of attacks from malicious software. For other tasks, consider using the [LocalService](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceaccount#system-serviceprocess-serviceaccount-localservice) account, which acts as a non-privileged user on the local computer and presents anonymous credentials to any remote server. However, this example fails if you try to use the [LocalService](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.serviceaccount#system-serviceprocess-serviceaccount-localservice) account, because it needs permission to write to the event log.

For more information about installers, see [How to: Add installers to your service application](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-add-installers-to-your-service-application).

Note

Before you decide to add startup parameters, consider whether it's the best way to pass information to your service. Although they're easy to use and parse, and a user can easily override them, they might be harder for a user to discover and use without documentation. Generally, if your service requires more than just a few startup parameters, you should use the registry or a configuration file instead.

A Windows service can accept command-line arguments, also known as _startup parameters_. When you add code to process startup parameters, a user can start your service with their own custom startup parameters in the service properties window. However, these startup parameters aren't persisted the next time the service starts.

To set startup parameters permanently, set them in the registry. Each Windows service has a registry entry under the **HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services** subkey. Under each service's subkey, use the **Parameters** subkey to store information that your service can access. You can use application configuration files for a Windows service the same way you do for other types of programs. For sample code, see [ConfigurationManager.AppSettings](https://learn.microsoft.com/en-us/dotnet/api/system.configuration.configurationmanager.appsettings#system-configuration-configurationmanager-appsettings).

1. In **MyNewService.cs**, or **MyNewService.vb**, change the `MyNewService` constructor to accept and process an input parameter:

```
public MyNewService(string[] args)
{
    InitializeComponent();

    string eventSourceName = "MySource";
    string logName = "MyNewLog";

    if (args.Length > 0)
    {
        eventSourceName = args[0];
    }

    if (args.Length > 1)
    {
        logName = args[1];
    }

    eventLog1 = new EventLog();

    if (!EventLog.SourceExists(eventSourceName))
    {
        EventLog.CreateEventSource(eventSourceName, logName);
    }

    eventLog1.Source = eventSourceName;
    eventLog1.Log = logName;
}
```

This code sets the event source and log name according to the startup parameters that the user supplies. If no arguments are supplied, it uses default values.

1. Select **Program.cs**, or **MyNewService.Designer.vb**, then choose **View Code** from the shortcut menu. In the `Main` method, change the code to add an input parameter and pass it to the service constructor:

```
static void Main(string[] args)
{
    ServiceBase[] ServicesToRun;
    ServicesToRun = new ServiceBase[]
    {
        new MyNewService(args)
    };
    ServiceBase.Run(ServicesToRun);
}
```
1. To specify the command-line arguments, add the following code to the `ProjectInstaller` class in **ProjectInstaller.cs**, or **ProjectInstaller.vb**:

```
protected override void OnBeforeInstall(IDictionary savedState)
{
    string parameter = "MySource1\" \"MyLogFile1";
    Context.Parameters["assemblypath"] = "\"" + Context.Parameters["assemblypath"] + "\" \"" + parameter + "\"";
    base.OnBeforeInstall(savedState);
}
```

Typically, this value contains the full path to the executable for the Windows service. For the service to start up correctly, the user must supply quotation marks for the path and each individual parameter. A user can change the parameters in the **ImagePath** registry entry to change the startup parameters for the Windows service. However, a better way is to change the value programmatically and expose the functionality in a user-friendly way, such as by using a management or configuration utility.

1. In **Solution Explorer**, choose **Properties** from the shortcut menu for the **MyNewService** project.

2. On the **Application** tab, in the **Startup object** list, choose **MyNewService.Program** (or **Sub Main** for Visual Basic projects).

3. To build the project, in **Solution Explorer**, choose **Build** from the shortcut menu for your project (or press Ctrl+Shift+B).

Now that you've built the Windows service, you can install it. To install a Windows service, you must have administrator credentials on the computer where it's installed.

1. Open [Developer Command Prompt for Visual Studio](https://learn.microsoft.com/en-us/visualstudio/ide/reference/command-prompt-powershell) with administrative credentials.

2. In **Developer Command Prompt for Visual Studio**, navigate to the folder that contains your project's output (by default, the _\bin\Debug_ subdirectory of your project).

3. Enter the following command:

```
installutil MyNewService.exe
```

If the service installs successfully, the command reports success.

If the system can't find _installutil.exe_, make sure that it exists on your computer. This tool is installed with .NET Framework to the folder _%windir%\Microsoft.NET\Framework[64]\<framework version>_.

If the **installutil.exe** process fails, check the install log to find out why. By default, the log is in the same folder as the service executable. The installation can fail if:

    *   The [RunInstallerAttribute](https://learn.microsoft.com/en-us/dotnet/api/system.componentmodel.runinstallerattribute) class isn't present on the `ProjectInstaller` class.
    *   The attribute isn't set to `true`.
    *   The `ProjectInstaller` class isn't defined as `public`.
    *   You didn't open Developer Command Prompt for VS as administrator.

For more information, see [How to: Install and uninstall services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-install-and-uninstall-services).

1. In Windows, open the **Services** desktop app: Press Windows+R to open the **Run** box, enter _services.msc_, and then press Enter or select **OK**.

You should see your service listed in **Services**, displayed alphabetically by the display name that you set for it.

![Image 4: MyNewService in the Services window.](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/media/windowsservices-serviceswindow.png)

1. To start the service, choose **Start** from the service's shortcut menu.

2. To stop the service, choose **Stop** from the service's shortcut menu.

3. (Optional) From the command line, use the commands **net start <service name>** and **net stop <service name>** to start and stop your service.

4. In Windows, open the **Event Viewer** desktop app: Enter _Event Viewer_ in the Windows search bar, and then select **Event Viewer** from the search results.

Tip

In Visual Studio, you can access event logs by opening **Server Explorer** from the **View** menu (or press Ctrl+Alt+S) and expanding the **Event Logs** node for the local computer.
2.   In **Event Viewer**, expand **Applications and Services Logs**.

1. Locate the listing for **MyNewLog** (or **MyLogFile1** if you followed the procedure to add command-line arguments) and expand it. You should see the entries for the two actions (start and stop) that your service performed.

![Image 5: Use the Event Viewer to see the event log entries](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/media/windows-service-event-viewer.png)

If you no longer need the Windows service app, you can remove it.

1. Open **Developer Command Prompt for Visual Studio** with administrative credentials.

2. In the **Developer Command Prompt for Visual Studio** window, navigate to the folder that contains your project's executable.

3. Enter the following command:

```
installutil.exe /u MyNewService.exe
```

If the service uninstalls successfully, the command reports that your service was successfully removed. For more information, see [How to: Install and uninstall services](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-install-and-uninstall-services).

Now that you've created the service, you can:

* Create a standalone setup program for others to use to install your Windows service. Use the [WiX Toolset](https://wixtoolset.org/) to create an installer for a Windows service. For other ideas, see [Create an installer package](https://learn.microsoft.com/en-us/visualstudio/deployment/deploying-applications-services-and-components#create-an-installer-package-windows-desktop).

* Explore the [ServiceController](https://learn.microsoft.com/en-us/dotnet/api/system.serviceprocess.servicecontroller) component, which enables you to send commands to the service you've installed.

* Instead of creating the event log when the application runs, use an installer to create an event log when you install the application. The event log is deleted by the installer when you uninstall the application. For more information, see [EventLogInstaller](https://learn.microsoft.com/en-us/dotnet/api/system.diagnostics.eventloginstaller).

* [Windows service applications](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/)
* [Introduction to Windows service applications](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/introduction-to-windows-service-applications)
* [How to: Debug Windows service applications](https://learn.microsoft.com/en-us/dotnet/framework/windows-services/how-to-debug-windows-service-applications)
* [Services (Windows)](https://learn.microsoft.com/en-us/windows/desktop/Services/services)
