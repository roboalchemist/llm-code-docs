# Source: https://docs.syncfusion.com/uwp/picker/timepicker.md

# Time Picker in UWP Picker (SfPicker)

We have demonstratedÂ how to createÂ TimePickerÂ using Picker controlÂ in the following steps.

**Step** **1** **:**Â We have created customÂ class named as âCustomTimePickerâ. This class should inherit fromÂ SfPickerÂ control.

{% highlight c# %}

    using Syncfusion.UI.Xaml.Controls.Input;
    using Windows.UI.Xaml;

    namespace TimePickerSample
  
        {    
    
         public class CustomTimePicker : SfPicker
   
           {

           }
   
        }

{% endhighlight %}

**Step** **2** **:**Â After that create fourÂ ObservableCollectionÂ withÂ object type inÂ TimePickerÂ class.

**Collection** **details** **:**

Time Collection,Â MinuteÂ Collection,Â Hour Collection andÂ FormatÂ Collection.

TimeÂ Collection->We have added all the three collections.

MinuteÂ Collection -> We have addedÂ minutes from 0 to 59.

Hour Collection -> We have added hours from 1 to 12.

Format Collection -> We have added two format AM and PM.

The below code demonstratesÂ TimeÂ collection creation.

{% highlight C# %}

    using Syncfusion.UI.Xaml.Controls.Input;
    using Windows.UI.Xaml;

    namespace TimePickerSample
  
     {    

      public class CustomTimePicker : SfPicker        
  
      {

        public ObservableCollection<string> Headers;
       
        public CustomTimePicker()
  
        {
  
            Headers = new ObservableCollection<string>();
            
            Headers.Add("Hour");
           
            Headers.Add("Minute");
           
            Headers.Add("Format");
            
            Header = "Time Picker";

            this.ColumnHeaderText = Headers;
            	
        }
  
      }
  
     }

{% endhighlight %}

**Step** **3** **:**Â We haveÂ defined each column headers âHOURâ, âMINUTEâ and âFORMATâ usingÂ ColumnHeaderTextÂ property ofÂ SfPickerÂ control. The below code demonstrates how to define header for each column ofÂ SfPickerÂ control.

{% highlight c# %}

    using Syncfusion.UI.Xaml.Controls.Input;
    using Windows.UI.Xaml;

    namespace TimePickerSample
   
    {    
 
     public class CustomTimePicker : SfPicker        
   
      {
      
        public ObservableCollection<string> Headers;
       
          public CustomTimePicker()
   
          {
   
            Headers = new ObservableCollection<string>();
            
            Headers.Add("Hour");
           
            Headers.Add("Minute");
           
            Headers.Add("Format");
            
            Header = "Time Picker";

            this.ColumnHeaderText = Headers;
            	
          }
   
       }
   
    }

{% endhighlight %}

**Step** **4** **:**Â Finally we have enabledÂ SfPickerÂ footer, header and Column header usingÂ ShowFooter, ShowHeaderÂ andÂ ShowColumnHeaderÂ properties.

{% highlight c# %}

    using Syncfusion.UI.Xaml.Controls.Input;
    using Windows.UI.Xaml;

    namespace TimePickerSample
 
    {    
 
      public CustomTimePicker()        
 
      {

        ShowFooter = true;

        ShowHeader = true;

        ShowColumnHeader = true;

      }
 
    }

{% endhighlight %}

**Step** **5** **:**Â We have added theÂ TimePickerÂ control in MainPage page. Please refer the below code snippets.

{% tabs %}

{% highlight xaml %}

    <Page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"

    x:Class="TimePickerSample.MainPage"

    xmlns:local="using:TimePickerSample"

    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"

    xmlns:input="using:Syncfusion.UI.Xaml.Controls.Input">

    <Grid>

        <Button Click="Button_Click" Height="50" VerticalAlignment="Bottom" HorizontalAlignment="Center" Content="Show TimePicker" Width="200" />

        <local:CustomTimePicker x:Name="date" ColumnHeaderHeight="40" HorizontalAlignment="Center" VerticalAlignment="Center"  PickerMode="Dialog" Height="400" Width="400"  SelectedItem="{Binding SelectedTime,Mode=TwoWay}"/>

    </Grid>

    </Page>

{% endhighlight %}

{% highlight c# %}

    using Syncfusion.UI.Xaml.Controls.Input;
    using Windows.UI.Xaml;

    namespace TimePickerSample
 
    {    

      public sealed partial class MainPage : Page
 
      {

        public MainPage()
 
        {
 
            this.InitializeComponent();
 
            DateTimeViewModel datetime view model = new DateTimeViewModel();
 
            this.DataContext = datetime view model;       
            
         }

        private void Button_Click(object sender, RoutedEventArgs e)
 
        {
 
            date.IsOpen = !date.IsOpen;
 
        }
        
      }
 
    }
    
{% endhighlight %}

{% endtabs %}

Screen shot for the above codes.

![TimePicker](images/TimePicker.png)

We have attachedÂ TimePickerÂ sample for reference. Please download the sample from the following link.

Sample link:Â [TimePicker](http://www.syncfusion.com/downloads/support/directtrac/general/TIMEPI~21534601253.ZIP)
