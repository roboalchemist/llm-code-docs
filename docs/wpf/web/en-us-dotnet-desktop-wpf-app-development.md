# Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/

Title: Application Development - WPF

URL Source: https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/

Markdown Content:
[](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/) Windows Presentation Foundation (WPF) is a presentation framework that can be used to develop the following types of applications:

*   Standalone Applications (traditional style Windows applications built as executable assemblies that are installed to and run from the client computer).

*   XAML browser applications (XBAPs) (applications composed of navigation pages that are built as executable assemblies and hosted by Web browsers such as Microsoft Internet Explorer or Mozilla Firefox).

*   Custom Control Libraries (non-executable assemblies containing reusable controls).

*   Class Libraries (non-executable assemblies that contain reusable classes).

Note

Using WPF types in a Windows service is strongly discouraged. If you attempt to use these features in a Windows service, they may not work as expected.

To build this set of applications, WPF implements a host of services. This topic provides an overview of these services and where to find more information.

Executable WPF applications commonly require a core set of functionality that includes the following:

*   Creating and managing common application infrastructure (including creating an entry point method and a Windows message loop to receive system and input messages).

*   Tracking and interacting with the lifetime of an application.

*   Retrieving and processing command-line parameters.

*   Sharing application-scope properties and UI resources.

*   Detecting and processing unhandled exceptions.

*   Returning exit codes.

*   Managing windows in standalone applications.

*   Tracking navigation in XAML browser applications (XBAPs), and standalone applications with navigation windows and frames.

Warning

XBAPs require legacy browsers to operate, such as Internet Explorer and old versions of Firefox. These older browsers are usually unsupported on Windows 10 and Windows 11. Modern browsers no longer support the technology required for XBAP apps due to security risks. Plugins that enable XBAPs are no longer supported. For more information, see [Frequently asked questions about WPF browser-hosted applications (XBAP)](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/xbap-faq). 

These capabilities are implemented by the [Application](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application) class, which you add to your applications using an _application definition_.

For more information, see [Application Management Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/application-management-overview).

WPF extends the core support in the Microsoft .NET Framework for embedded resources with support for three kinds of non-executable data files: resource, content, and data. For more information, see [WPF Application Resource, Content, and Data Files](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/wpf-application-resource-content-and-data-files).

A key component of the support for WPF non-executable data files is the ability to identify and load them using a unique URI. For more information, see [Pack URIs in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/pack-uris-in-wpf).

Users interact with WPF standalone applications through windows. The purpose of a window is to host application content and expose application functionality that usually allows users to interact with the content. In WPF, windows are encapsulated by the [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) class, which supports:

*   Creating and showing windows.

*   Establishing owner/owned window relationships.

*   Configuring window appearance (for example, size, location, icons, title bar text, border).

*   Tracking and interacting with the lifetime of a window.

For more information, see [WPF Windows Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/).

[Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) supports the ability to create a special type of window known as a dialog box. Both modal and modeless types of dialog boxes can be created.

For convenience, and the benefits of reusability and a consistent user experience across applications, WPF exposes three of the common Windows dialog boxes: [OpenFileDialog](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.openfiledialog), [SaveFileDialog](https://learn.microsoft.com/en-us/dotnet/api/microsoft.win32.savefiledialog), and [PrintDialog](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.printdialog).

A message box is a special type of dialog box for showing important textual information to users, and for asking simple Yes/No/OK/Cancel questions. You use the [MessageBox](https://learn.microsoft.com/en-us/dotnet/api/system.windows.messagebox) class to create and show message boxes.

For more information, see [Dialog Boxes Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/windows/dialog-boxes-overview).

WPF supports Web-style navigation using pages ([Page](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.page)) and hyperlinks ([Hyperlink](https://learn.microsoft.com/en-us/dotnet/api/system.windows.documents.hyperlink)). Navigation can be implemented in a variety of ways that include the following:

*   Standalone pages that are hosted in a Web browser.

*   Pages compiled into an XBAP that is hosted in a Web browser.

*   Pages compiled into a standalone application and hosted by a navigation window ([NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow)).

*   Pages that are hosted by a frame ([Frame](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.frame)), which may be hosted in a standalone page, or a page compiled into either an XBAP or a standalone application.

To facilitate navigation, WPF implements the following:

*   [NavigationService](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationservice), the shared navigation engine for processing navigation requests that is used by [Frame](https://learn.microsoft.com/en-us/dotnet/api/system.windows.controls.frame), [NavigationWindow](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.navigationwindow), and XBAPs to support intra-application navigation.

*   Navigation methods to initiate navigation.

*   Navigation events to track and interact with navigation lifetime.

*   Remembering back and forward navigation using a journal, which can also be inspected and manipulated.

For information, see [Navigation Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/navigation-overview).

WPF also supports a special type of navigation known as structured navigation. Structured navigation can be used to call one or more pages that return data in a structured and predictable way that is consistent with calling functions. This capability depends on the [PageFunction<T>](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.pagefunction-1) class, which is described further in [Structured Navigation Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/structured-navigation-overview). [PageFunction<T>](https://learn.microsoft.com/en-us/dotnet/api/system.windows.navigation.pagefunction-1) also serves to simplify the creation of complex navigation topologies, which are described in [Navigation Topologies Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/navigation-topologies-overview).

XBAPs can be hosted in Microsoft Internet Explorer or Firefox. Each hosting model has its own set of considerations and constraints that are covered in [Hosting](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/hosting-wpf-applications).

Although simple WPF applications can be built from a command prompt using command-line compilers, WPF integrates with Visual Studio to provide additional support that simplified the development and build process. For more information, see [Building a WPF Application](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/building-a-wpf-application-wpf).

Depending on the type of application you build, there are one or more deployment options to choose from. For more information, see [Deploying a WPF Application](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/deploying-a-wpf-application-wpf).

| Title | Description |
| --- | --- |
| [Application Management Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/application-management-overview) | Provides an overview of the [Application](https://learn.microsoft.com/en-us/dotnet/api/system.windows.application) class including managing application lifetime, windows, application resources, and navigation. |
| [Windows in WPF](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/windows-in-wpf-applications) | Provides details of managing windows in your application including how to use the [Window](https://learn.microsoft.com/en-us/dotnet/api/system.windows.window) class and dialog boxes. |
| [Navigation Overview](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/navigation-overview) | Provides an overview of managing navigation between pages of your application. |
| [Hosting](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/hosting-wpf-applications) | Provides an overview of XAML browser applications (XBAPs). |
| [Build and Deploy](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/app-development/building-and-deploying-wpf-applications) | Describes how to build and deploy your WPF application. |
| [Introduction to WPF in Visual Studio](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/create-app-visual-studio) | Describes the main features of WPF. |
| [Walkthrough: My first WPF desktop application](https://learn.microsoft.com/en-us/dotnet/desktop/wpf/get-started/walkthrough-my-first-wpf-desktop-application) | A walkthrough that shows how to create a WPF application using page navigation, layout, controls, images, styles, and binding. |
