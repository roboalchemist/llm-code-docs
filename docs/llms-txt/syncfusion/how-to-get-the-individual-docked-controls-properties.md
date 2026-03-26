# Source: https://docs.syncfusion.com/windowsforms/docking-manager/faq/general/how-to-get-the-individual-docked-controls-properties.md

# How to get the individual Docked control's properties?

To check whether a control is floating or docked, you could use the code snippet given below.

{% tabs %}

{% highlight C# %}

this.dockingManager1.IsFloating(this.listBox1);

{% endhighlight %}


{% highlight VB %}


Me.dockingManager1.IsFloating(this.listBox1);

{% endhighlight %}

{% endtabs %}

### To get the Dock location

1. Add a list view and a docking manager in your form.
2. Enable the list view as a docked control.

{% capture codesnippet1 %}
{% tabs %}

{% highlight C# %}

this.dockingManager1.SetEnableDocking(this.listView1,true);

{% endhighlight %}


{% highlight VB %}


Me.dockingManager1.SetEnableDocking(Me.listView1, True)

{% endhighlight %}

{% endtabs %}
{% endcapture %}
{{ codesnippet1 | OrderList_Indent_Level_1 }}  

3. Now add the below given code in your form's constructor.

{% capture codesnippet2 %}
{% tabs %}

{% highlight C# %}

//listView1 is the dockable control. We could get it's dock properties by accessing DockHost and DockHostController.

Syncfusion.Windows.Forms.Tools.DockHost dockHost = this.listView1.Parent as Syncfusion.Windows.Forms.Tools.DockHost;

Syncfusion.Windows.Forms.Tools.DockHostController dockHostController = dockHost.InternalController as

Syncfusion.Windows.Forms.Tools.DockHostController;


//The DockInfo object will give all the information about docked control.

Syncfusion.Windows.Forms.Tools.DockInfo dockInfo = dockHostController.GetSerCurrentDI();

MessageBox.Show(dockInfo.dStyle.ToString() + dockHostController.LayoutRect.ToString());

{% endhighlight %}


{% highlight VB %}


' listView1 is the dockable control. We could get it's dock properties by accessing DockHost and DockHostController.

DimÂ dockHostÂ AsÂ Syncfusion.Windows.Forms.Tools.DockHost =Â CType(IIf(TypeOf Me.listView1.ParentÂ IsÂ Syncfusion.Windows.Forms.Tools.DockHost,Â Me.listView1.Parent,Nothing), Syncfusion.Windows.Forms.Tools.DockHost)

DimÂ dockHostControllerÂ AsÂ Syncfusion.Windows.Forms.Tools.DockHostController =Â CType(IIf(TypeOf dockHost.InternalControllerÂ IsÂ Syncfusion.Windows.Forms.Tools.DockHostController, dockHost.InternalController,Â Nothing), Syncfusion.Windows.Forms.Tools.DockHostController)


' The DockInfo object will give all the information about docked control.

DimÂ dockInfoÂ AsÂ Syncfusion.Windows.Forms.Tools.DockInfo = dockHostController.GetSerCurrentDI()

MessageBox.Show((dockInfo.dStyle.ToString + dockHostController.LayoutRect.ToString))

{% endhighlight %}

{% endtabs %}
{% endcapture %}
{{ codesnippet2 | OrderList_Indent_Level_1 }}

4. Before closing a docked / floating control, access the controlâs parent and cast this to type Syncfusion.Windows.Forms.Tools.DockHost.Â 
5. Now access the DockHost's InternalController and get itâs current serialization info by using the GetSerCurrInfo() method. This will fetch an object of typeÂ Syncfusion.Windows.Forms.Tools.DockInfo. TheÂ DockInfo.DockingStyleÂ member gives the dock position of the particular control with respect to the host form and the DockInfo.rcDockAreaÂ member returns the control bounds.Â 
6. If the control is floating, then DockingStyle will be equal to Syncfusion.Windows.Forms.Tools.DockingStyle.Fill. You can serialize this information against the controlâs name and later upon loading, appropriately use either the DockingManager.DockControl() / FloatControl() method, based on the serialized DockingStyle and control's bounds values, to set the controlâs dock state.


