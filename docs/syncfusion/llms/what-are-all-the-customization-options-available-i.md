# Source: https://docs.syncfusion.com/windowsforms/messagebox/faq/what-are-all-the-customization-options-available-i.md

# What are all the customization options available in MessageBoxAdv?

MessageBoxAdv appearance can be customized using the following options.

<table>
<tr>
<th>
Properties</th><th>
Description</th></tr>
<tr>
<td>
ApplyAeroTheme</td><td>
Gets or sets to Force the OS Aero theme look and feel when Office2007Visual style is enabled. This does not work for XP and lower OS versions.</td></tr>
<tr>
<td>
CaptionAlign</td><td>
Gets or sets the title alignment, that is not applicable when enabling ApplyAeroTheme property in Default Style.</td></tr>
<tr>
<td>
DropShadow</td><td>
Gets or sets whether to show the DropShadow effect.</td></tr>
<tr>
<td>
MaximumSize</td><td>
Gets or sets the Maximum Size.</td></tr>
<tr>
<td>
MessageBoxStyle</td><td>
Gets or sets a value indicating the style used for drawing the control.</td></tr>
<tr>
<td>
MetroColorTable</td><td>
Gets or sets the MetroStyleColorTable.</td></tr>
<tr>
<td>
Office2007Theme</td><td>
Gets or sets the Office2007 theme.</td></tr>
</table>



{% tabs %}

{% highlight C# %}

//To disable the Aero theme

MessageBoxAdv.ApplyAeroTheme = false;

//To set the Caption alignment

MessageBoxAdv.CaptionAlign = HorizontalAlignment.Right;

//To show the shadow effect

MessageBoxAdv.DropShadow = true;

//To set the Maximum size 

MessageBoxAdv.MaximumSize = new System.Drawing.Size(520, Screen.PrimaryScreen.WorkingArea.Size.Height);

//To set the Style

MessageBoxAdv.MessageBoxStyle = MessageBoxAdv.Style.Metro;

//To assign the MetroColorTable

MessageBoxAdv.MetroColorTable = new MetroStyleColorTable();

//To set the Office2007 color scheme

MessageBoxAdv.Office2007Theme = Office2007Theme.Blue;

{% endhighlight %}

{% highlight VB %}

'ToÂ disableÂ theÂ AeroÂ theme

MessageBoxAdv.ApplyAeroThemeÂ =Â false

'ToÂ setÂ theÂ CaptionÂ alignment

MessageBoxAdv.CaptionAlignÂ =Â HorizontalAlignment.Right

'ToÂ showÂ theÂ shadowÂ effect

MessageBoxAdv.DropShadowÂ =Â true

'ToÂ setÂ theÂ MaximumÂ size

MessageBoxAdv.MaximumSizeÂ =Â NewÂ System.Drawing.Size(520,Â Screen.PrimaryScreen.WorkingArea.Size.Height)

'ToÂ setÂ theÂ MessageBoxAdvÂ Style

MessageBoxAdv.MessageBoxStyleÂ =Â MessageBoxAdv.Style.Metro

'ToÂ assignÂ theÂ MetroColorTable

MessageBoxAdv.MetroColorTableÂ =Â NewÂ MetroStyleColorTable

'ToÂ setÂ theÂ Office2007Â colorÂ scheme

MessageBoxAdv.Office2007ThemeÂ =Â Office2007Theme.Blue

{% endhighlight %}

{% endtabs %}

