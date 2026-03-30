# Source: https://docs.syncfusion.com/wpf/olap-common/how-to/host-bi-silverlight-component-in-aspnet-mvc-web-project.md

# Host BI Silverlight component in ASP.NET MVC Web Project

The following steps explain how to add the Silverlight components in MVC project:

1. Open Visual Studio IDE.
2. Go to FileNewProject and create a new Silverlight application. 

   A dialog window opens as shown below: 

   ![Host-BI-Silverlight-component-image1](Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_images/Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_img1.png)





3. Select _Silverlight Application_ from the New Project dialog window and click OK.



   The New Silverlight Application dialog opens as shown in the following screenshot:

   ![Host-BI-Silverlight-component-image2](Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_images/Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_img2.png)



   The Solution Explorer window shows the Silverlight application with MVC project.

   ![Host-BI-Silverlight-component-image3](Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_images/Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_img3.png)





4. Double-click to open the Main.xaml which is found under the Silverlight project in Solution Explorer as shown below:

   ![Host-BI-Silverlight-component-image4](Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_images/Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_img4.png)



5. 	Drag and drop the OlapGrid from the toolbox to the MainPage.xaml.Â 

   ![Host-BI-Silverlight-component-image5](Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_images/Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_img5.png)





6. Add the following two assemblies as references to the web project:
   * Syncfusion.Olap.Base
   * Syncfusion.OlapSilverlight.BaseWrapper



7. Add a WCF Service to the web project by right-clicking the Project   Add New Item  WCF Service. 
8. Name the service as OlapManager and delete the IOlapManager.cs file as the service has to be inherited with the IOlapDataProvider.



   ![Host-BI-Silverlight-component-image6](Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_images/Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_img6.png)





9. Inherit the newly added WCF service with the IOlapDataProvider and explicitly implement the IOlapDataProvider.
10. The connection to the database is done with the help of the WCF service. The service has to be created and instantiated as described in the below code snippet.


 
     The WCF Service has to implement the IOlapDataProvider interface. To implement this interface, you require the OlapDataProvider, which can be instantiated by passing the connection string.

     The interface can be implemented as shown in the following code snippet:



    ~~~csharp

		public class OlapManager : IOlapDataProvider

		{

		Â Â Â Â Â Â Â  Syncfusion.OlapSilverlight.Manager.OlapDataProvider dataManager;



		Â Â Â Â Â Â Â  /// <summary>

		Â Â Â Â Â Â Â  /// Initializes a new instance of the <see cref="OlapManager"/> class.

		Â Â Â Â Â Â Â  /// </summary>

		Â Â Â Â Â Â Â  public OlapManager()

		Â Â Â Â Â Â Â  {

		Â Â Â Â Â Â Â Â Â Â Â  string connectionString = "DataSource=localhost;Initial Catalog=Adventure Works DW";

		Â Â Â Â Â Â Â Â Â Â Â  // Instantiating the OlapDataProvider with connection string.

		Â Â Â Â Â Â Â Â Â Â Â  dataManager = new OlapDataProvider(connectionString);

		Â Â Â Â Â Â Â  }

		Â Â Â Â Â Â Â Â  #region IOlapDataProvider Members

		Â Â Â Â Â Â Â Â  /// <summary>

		Â Â Â Â Â Â Â  /// Executing the CellSet by passing OlapReport.

		Â Â Â Â Â Â Â  /// </summary>

		Â Â Â Â Â Â Â  /// <param name="report">The report.</param>

		Â Â Â Â Â Â Â  /// <returns> The CellSet </returns>

		Â Â Â Â Â Â Â  public Syncfusion.OlapSilverlight.Data.CellSet ExecuteOlapReport(Syncfusion.OlapSilverlight.Reports.OlapReport report)

		Â Â Â Â Â Â Â  {

		Â Â Â Â Â Â Â Â Â Â Â  Syncfusion.OlapSilverlight.Data.CellSet cellSet = this.dataManager.ExecuteOlapReport(report);

		Â Â Â Â Â Â Â Â Â Â Â  // Closing the provider connection.

		Â Â Â Â Â Â Â Â Â Â Â  this.dataManager.DataProvider.CloseConnection();

		Â Â Â Â Â Â Â Â Â Â Â  return cellSet;

		Â Â Â Â Â Â Â  }

		Â Â Â Â Â Â Â Â  /// <summary>

		Â Â Â Â Â Â Â  /// Executing the CellSet by passing MDX Query.

		Â Â Â Â Â Â Â  /// </summary>

		Â Â Â Â Â Â Â  /// <param name="mdxQuery">The MDX query.</param>

		Â Â Â Â Â Â Â  /// <returns> The CellSet </returns>

		Â Â Â Â Â Â Â  public Syncfusion.OlapSilverlight.Data.CellSet ExecuteMdxQuery(string mdxQuery)

		Â Â Â Â Â Â Â  {

		Â Â Â Â Â Â Â Â Â Â Â  Syncfusion.OlapSilverlight.Data.CellSet cellSet = this.dataManager.ExecuteMdxQuery(mdxQuery);

		Â Â Â Â Â Â Â Â Â Â Â  // Closing the provider connection.

		Â Â Â Â Â Â Â Â Â Â Â  this.dataManager.DataProvider.CloseConnection();

		Â Â Â Â Â Â Â Â Â Â Â  return cellSet;

		Â Â Â Â Â Â Â  }



		Â Â Â Â Â Â Â  public MemberCollection GetChildMembers(string memberUniqueName, string cubeName)

		Â Â Â Â Â Â Â  {

		Â Â Â Â Â Â Â Â Â Â Â  throw new NotImplementedException();

		Â Â Â Â Â Â Â  }

		Â Â Â Â Â Â Â Â  public CubeSchema GetCubeSchema(string cubeName)

		Â Â Â Â Â Â Â  {

		Â Â Â Â Â Â Â Â Â Â Â  throw new NotImplementedException();

		Â Â Â Â Â Â Â  }

		Â Â Â Â Â Â Â Â  public CubeInfoCollection GetCubes()

		Â Â Â Â Â Â Â  {

		Â Â Â Â Â Â Â Â Â Â Â  throw new NotImplementedException();

		Â Â Â Â Â Â Â  }

		Â Â Â Â Â Â Â Â  public MemberCollection GetLevelMembers(string levelUniqueName, string cubeName)

		Â Â Â Â Â Â Â  {

		Â Â Â Â Â Â Â Â Â Â Â  throw new NotImplementedException();

		Â Â Â Â Â Â Â  }

		Â Â Â Â Â Â Â Â  #endregion

		}Â 
		
    ~~~

    ~~~vbnet


		Â Public Class OlapManager

		Â Â Â Â Â  Â Implements IOlapDataProvider

		Â Â Â Â Â Â Â Â Â Â Â  Private dataManager As Syncfusion.OlapSilverlight.Manager.OlapDataProvider

		Â Â Â Â Â Â Â Â Â Â Â Â  ''' <summary>

		Â Â Â Â Â Â Â Â Â Â Â  ''' Initializes a new instance of the <see cref="OlapManager"/> class.

		Â Â Â Â Â Â Â Â Â Â Â  ''' </summary>

		Â Â Â Â Â Â Â Â Â Â Â  Public Sub New()

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Dim connectionString As String = "DataSource=localhost;Initial Catalog=Adventure Works DW"

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  ' Instantiating the OlapDataProvider with connection string

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  dataManager = New OlapDataProvider(connectionString)

		Â Â Â Â Â Â Â Â Â Â Â  End Sub

		Â Â Â Â Â Â Â Â Â Â Â Â  #Region "IOlapDataProvider Members"

		Â Â Â Â Â Â Â Â Â Â Â Â  ''' <summary>

		Â Â Â Â Â Â Â Â Â Â Â  ''' Executing the CellSet by passing OlapReport

		Â Â Â Â Â Â Â Â Â Â Â  ''' </summary>

		Â Â Â Â Â Â Â Â Â Â Â  ''' <param name="report">The report.</param>

		Â Â Â Â Â Â Â Â Â Â Â  ''' <returns></returns>

		Â Â Â Â Â Â Â Â Â Â Â  Public Function ExecuteOlapReport(ByVal report As Syncfusion.OlapSilverlight.Reports.OlapReport) As Syncfusion.OlapSilverlight.Data.CellSet

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Dim cellSet As Syncfusion.OlapSilverlight.Data.CellSet = Me.dataManager.ExecuteOlapReport(report)

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  ' Closing the provider connection

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Me.dataManager.DataProvider.CloseConnection()

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Return cellSet

		Â Â Â Â Â Â Â Â Â Â Â  End Function

		Â Â Â Â Â Â Â Â Â Â Â Â  ''' <summary>

		Â Â Â Â Â Â Â Â Â Â Â  ''' Executing the CellSet by passing MDX Query

		Â Â Â Â Â Â Â Â Â Â Â  ''' </summary>

		Â Â Â Â Â Â Â Â Â Â Â  ''' <param name="mdxQuery">The MDX query.</param>

		Â Â Â Â Â Â Â Â Â Â Â  ''' <returns> The CellSet </returns>

		Â Â Â Â Â Â Â Â Â Â Â  Public Function ExecuteMdxQuery(ByVal mdxQuery As String) As Syncfusion.OlapSilverlight.Data.CellSet

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Dim cellSet As Syncfusion.OlapSilverlight.Data.CellSet = Me.dataManager.ExecuteMdxQuery(mdxQuery)

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  'Closing the provider connection.

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Me.dataManager.DataProvider.CloseConnection()

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Return cellSet

		Â Â Â Â Â Â Â Â Â Â Â  End Function



		Â Â Â Â Â Â Â Â Â Â Â  Public Function GetChildMembers(ByVal memberUniqueName As String, ByVal cubeName As String) As MemberCollection

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Throw New NotImplementedException()

		Â Â Â Â Â Â Â Â Â Â Â  End Function



		Â Â Â Â Â Â Â Â Â Â Â  Public Function GetCubeSchema(ByVal cubeName As String) As CubeSchema

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Throw New NotImplementedException()

		Â Â Â Â Â Â Â Â Â Â Â  End Function



		Â Â Â Â Â Â Â Â Â Â Â  Public Function GetCubes() As CubeInfoCollection

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Throw New NotImplementedException()

		Â Â Â Â Â Â Â Â Â Â Â  End Function



		Â Â Â Â Â Â Â Â Â Â Â  Public Function GetLevelMembers(ByVal levelUniqueName As String, ByVal cubeName As String) As MemberCollection

		Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Throw New NotImplementedException()

		Â Â Â Â Â Â Â Â Â Â Â  End Function



		Â Â Â Â Â Â Â Â Â Â Â  #End Region

		Â End ClassÂ 

    ~~~

11. Include the custom binding and the service endpoint address in the Web.Config file under the ServiceModel section.



    ~~~xaml

			Â Â Â Â Â Â <!--Binding-->

			Â Â Â Â Â Â <bindings>

			Â Â Â Â Â Â Â Â <customBinding>

			Â Â Â Â Â Â Â Â Â Â <bindingÂ name="binaryHttpBinding">

			Â Â Â Â Â Â Â Â Â Â Â Â <binaryMessageEncoding/>

			Â Â Â Â Â Â Â Â Â Â Â Â <httpTransportÂ maxReceivedMessageSize="2147483647"/>

			Â Â Â Â Â Â Â Â Â Â </binding>
			Â Â Â Â Â Â Â Â </customBinding>

			Â Â Â Â Â Â </bindings> 

			Â Â Â Â Â Â <!âEndpoint Address-->

			Â Â Â Â Â Â <services>

			Â Â Â Â Â Â Â Â <serviceÂ name="SilverlightApplication1.Web.OlapManager"Â >

			Â Â Â Â Â Â Â Â Â Â <endpointÂ address="binary"Â binding="customBinding"Â bindingConfiguration="binaryHttpBinding"Â contract="Syncfusion.OlapSilverlight.Manager.IOlapDataProvider">
			Â Â Â Â Â Â Â Â Â Â </endpoint>

			Â Â Â Â Â Â Â Â </service>

			Â Â Â Â Â Â </services>Â 

    ~~~

12. Add the System.ServiceModel assembly as a reference for the Silverlight project.
13. Add the following namespace in MainPage.xaml.cs:
    * System.ServiceModel
    * System.ServiceModel.Channels
    * ï Syncfusion.OlapSilverlight.Reports
    * ï Syncfusion.Silverlight.Grid
    * ï Syncfusion.OlapSilverlight.Manager
    * ï Syncfusion.OlapSilverlight.Engine



14. Instantiate the service from MainPage.xaml.cs which is in the Silverlight Project.
15. Declare the IOlapDataProvider for service instantiation.


    ~~~csharp


				Â //Â DeclaringÂ theÂ IOlapDataProviderÂ forÂ serviceÂ instantiation.
				Â IOlapDataProviderÂ DataProviderÂ =Â null;Â 

    ~~~

    ~~~vbnet

				'Declaring the IOlapDataProvider for service instantiation.

				Dim DataProvider As IOlapDataProvider = NothingÂ 

    ~~~

16. Specify the custom binding and instantiate the DataProvider from the ChannelFactory.Â Â Â 



    ~~~csharp

				privateÂ voidÂ InitializeConnection()
				{

				Â Â Â Â Â Â System.ServiceModel.Channels.BindingÂ customBindingÂ =Â newÂ CustomBinding(newÂ BinaryMessageEncodingBindingElement(),Â newÂ HttpTransportBindingElementÂ {Â MaxReceivedMessageSizeÂ =Â 2147483647Â });

				Â Â Â Â Â Â Â Â Â Â Â Â EndpointAddressÂ addressÂ =Â newÂ EndpointAddress(newÂ Uri(App.Current.Host.SourceÂ +Â "../../../../OlapManager.svc/binary"));

				Â Â Â Â Â ChannelFactory<IOlapDataProvider>Â clientChannelÂ =Â newÂ ChannelFactory<IOlapDataProvider>(customBinding,Â address);
				Â Â Â Â Â DataProviderÂ =Â clientChannel.CreateChannel();
				}Â 


    ~~~

    ~~~vbnet
				Private Sub InitializeConnection()

				Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Dim customBinding As System.ServiceModel.Channels.Binding = New CustomBinding(New BinaryMessageEncodingBindingElement(), New HttpTransportBindingElement With {.MaxReceivedMessageSize = 2147483647})

				Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Dim address As EndpointAddress = New EndpointAddress(New Uri(App.Current.Host.Source & "../../../../OlapManager.svc/binary"))

				Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  Dim clientChannel As ChannelFactory(Of IOlapDataProvider) = New ChannelFactory(Of IOlapDataProvider)(customBinding, address)

				Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â  DataProvider = clientChannel.CreateChannel()

				End SubÂ 


    ~~~


17. Create the Report.



     For creating reports there is a report object called OlapReport. The OlapReport object contains CategoricalItems, SeriesItems, SlicerItems, and FilterItems.

     The OlapReport is associated with the OlapDataManager as the current report property. When a report is set to the current report, an event triggers and the control renders based on the current report that is set. 



18. Bind the data to OlapGridData. 



    ~~~csharp

		privateÂ voidÂ MainPage_Loaded(objectÂ sender,Â RoutedEventArgsÂ e)
		{
		Â Â Â  //Â InitializeÂ theÂ serviceÂ connection.
		Â Â Â  this.InitializeConnection();
		Â Â Â Â //Â InstantiatingÂ theÂ OlapDataManager.
		Â Â Â  OlapDataManagerÂ m_OlapDataManagerÂ =newÂ OlapDataManager();
		Â Â Â Â //Â SpecifyingÂ theÂ DataProviderÂ forÂ OlapDataManager.
		Â Â Â Â m_OlapDataManager.DataProviderÂ =Â this.DataProvider;
		Â Â Â Â //Â SetÂ currentÂ reportÂ forÂ OlapDataManager.
		Â Â Â Â m_OlapDataManager.SetCurrentReport(CreateOlapReport());
		Â Â Â Â //Â SpecifyingÂ theÂ OlapDataManagerÂ forÂ OlapGrid.
		Â Â Â Â this.olapGrid1.OlapDataManagerÂ =Â m_OlapDataManager;
		Â Â Â Â //Â DataÂ Binding.
		Â Â Â  this.olapGrid1.DataBind();
		}Â 


    ~~~

    ~~~vbnet
   
		Private Sub MainPage_Loaded(ByVal sender As Object, ByVal e As RoutedEventArgs)

		Â Â Â Â Â  'Initialize the service connection.

		Â Â Â Â Â  Me.InitializeConnection()

		Â Â Â Â Â  'Instantiating the OlapDataManager.

		Â Â Â Â Â  Dim m_OlapDataManager As OlapDataManager = New OlapDataManager()

		Â Â Â Â Â  'Specifying the DataProvider for OlapDataManager.

		Â Â Â Â Â  m_OlapDataManager.DataProvider = Me.DataProvider

		Â Â Â Â Â  'Set current report for OlapDataManager.

		Â Â Â Â Â  m_OlapDataManager.SetCurrentReport(CreateOlapReport())

		Â Â Â Â Â  ' Specifying the OlapDataManager for OlapGrid.

		Â Â Â Â Â  Me.olapGrid1.OlapDataManager = m_OlapDataManager

		Â Â Â Â Â  ' Data Binding.

		Â Â Â Â Â  Me.olapGrid1.DataBind()

		End SubÂ 

    ~~~

     [Click here for Sample Report](http://help.syncfusion.com/UG/Business%20Intelligence/OLAP%20Grid/Silverlight/documents/731olapreportwithsimpledimensionsandmeasure.htm)



     ![Host-BI-Silverlight-component-image7](Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_images/Host-BI-Silverlight-component-in-ASPNET-MVC-Web-Pr_img7.png)


   


