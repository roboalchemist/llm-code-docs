# Source: https://docs.syncfusion.com/wpf/classic/schedule/resources.md

# Resources in WPF Schedule (Classic)

The Scheduler allows to define resources that can be assigned to appointments. Resources let you associate additional information with your appointments. The schedule can group appointments based on the resources associated with them. Appointments will be grouped based on the resource associated with them only when both theÂ [Resource](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.SfSchedule.html#Syncfusion_UI_Xaml_Schedule_SfSchedule_Resource)Â andÂ [ScheduleResourceTypeCollection](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.SfSchedule.html#Syncfusion_UI_Xaml_Schedule_SfSchedule_ScheduleResourceTypeCollection)Â properties are set, and also when theÂ valueÂ set for aÂ `Resource`Â matches with any types specified in theÂ `ScheduleResourceTypeCollection`Â property.
For example, end user can create appointments for different doctors.

{% tabs %}
{% highlight xaml %}
<Schedule:SfScheduleÂ Name="Schedule1"Â ScheduleType="Week" Background="WhiteSmoke"Â Resource="Doctors" >
Â Â Â Â <Schedule:SfSchedule.ScheduleResourceTypeCollectionÂ >
Â Â Â Â Â Â Â Â <Schedule:ResourceTypeÂ TypeName="Doctors">
Â Â Â Â Â Â Â Â Â Â Â Â <Schedule:ResourceÂ Â Â DisplayName="Dr.Jacob John, M.D " ResourceName="Dr.Jacob"/>
Â Â Â Â Â Â Â Â Â Â Â Â <Schedule:ResourceÂ Â DisplayName="Dr.Darsy Mascio, M.D" ResourceName="Dr.Darsy"/>
Â Â Â Â Â Â Â Â </Schedule:ResourceType>
Â Â Â Â </Schedule:SfSchedule.ScheduleResourceTypeCollection>
</Schedule:SfSchedule>
{% endhighlight  %}
{% highlight c# %}
ScheduleAppointmentÂ app =Â newÂ ScheduleAppointment() { StartTime = currentDate, EndTime = currentDate.AddHours(ran.Next(0, 2)), Subject = subject[count % subject.Length], Location =Â "Chennai", AppointmentBackground = brush[m % 3] };
app.ResourceCollection.Add(newÂ Resource() { ResourceName ="Dr.Jacob", TypeName =Â "Doctors"Â });
ScheduleAppointmentÂ app1 =Â newÂ ScheduleAppointment() { StartTime = nextDate, EndTime = nextDate.AddHours(ran.Next(0, 2)), Subject = subject[count % subject.Length], Location =Â "Chennai", AppointmentBackground = brush[(m + 2) % 3] };
app1.ResourceCollection.Add(newÂ Resource() { ResourceName ="Dr.Darsy", TypeName =Â "Doctors"Â });
Schedule1.Appointments.Add(app);
Schedule1.Appointments.Add(app1);
{% endhighlight  %}
{% endtabs %}

![WPF Scheduler workweek view with resource](Resources_images/workweek-view-with-resources.jpeg)

![WPF Scheduler month view with resource](Resources_images/month-view-with-resources.jpeg)

![WPF Scheduler timeline view with resource](Resources_images/timeline-view-with-resources.jpeg)

## Creating Resource for Schedule

Let's see the stepsÂ toÂ add resources in Scheduler.

The first step is set the [Resource](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.SfSchedule.html#Syncfusion_UI_Xaml_Schedule_SfSchedule_Resource) in Scheduler

{% tabs %}
{% highlight xaml %}

<schedule:SfSchedule  Resource="Doctors" >
    ...
</schedule:SfSchedule>
{% endhighlight  %}
{% endtabs %}

After this, we need to create aÂ [ScheduleResourceTypeCollection](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.SfSchedule.html#Syncfusion_UI_Xaml_Schedule_SfSchedule_ScheduleResourceTypeCollection), to assign theÂ [ResourceType](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.ResourceType.html):

{% tabs %}
{% highlight xaml %}
<schedule:SfSchedule Resource="Doctors"  >
    ...
    <schedule:SfSchedule.ScheduleResourceTypeCollection>
        ...
    </schedule:SfSchedule.ScheduleResourceTypeCollection>
</schedule:SfSchedule>
{% endhighlight  %}
{% endtabs %}


## Adding ResourceType to a resource collection

After Creating the `ScheduleResourceTypeCollection` add the [ResourceType](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.ResourceType.html), here we create the example for `ResourceType` as Doctors.

{% tabs %}
{% highlight xaml %}
<schedule:SfSchedule  Resource="Doctors" >
    <schedule:SfSchedule.ScheduleResourceTypeCollection >
        <schedule:ResourceType TypeName="Doctors">
        . . .
        </schedule:ResourceType>
    </schedule:SfSchedule.ScheduleResourceTypeCollection>
</schedule:SfSchedule>
{% endhighlight  %}
{% endtabs %}

## Adding a Resource to a ResourceType 

The next step is create and assignÂ resourcesÂ to `ResourceType`.

{% tabs %}
{% highlight xaml  %}
<schedule:SfSchedule  Resource="Doctors" >
    <schedule:SfSchedule.ScheduleResourceTypeCollection >
        <schedule:ResourceType TypeName="Doctors">
            <schedule:Resource   DisplayName="Dr.Jacob John, M.D " ResourceName="Dr.Jacob"/>
            <schedule:Resource  DisplayName="Dr.Darsy Mascio, M.D" ResourceName="Dr.Darsy"/>
         </schedule:ResourceType>
     </schedule:SfSchedule.ScheduleResourceTypeCollection>
</schedule:SfSchedule>
{% endhighlight  %}
{% endtabs %}

## Creating appointments by specifying the resource

You can add an appointments to group of added resources.

{% tabs %}
{% highlight c# %}
ScheduleAppointmentÂ app =Â newÂ ScheduleAppointment() { StartTime = currentDate, EndTime = currentDate.AddHours(ran.Next(0, 2)), Subject = subject[count % subject.Length], Location =Â "Chennai", AppointmentBackground = brush[m % 3] };
app.ResourceCollection.Add(newÂ Resource() { ResourceName ="Dr.Jacob", TypeName =Â "Doctors"Â });
ScheduleAppointmentÂ app1 =Â newÂ ScheduleAppointment() { StartTime = nextDate, EndTime = nextDate.AddHours(ran.Next(0, 2)), Subject = subject[count % subject.Length], Location =Â "Chennai", AppointmentBackground = brush[(m + 2) % 3] };
app1.ResourceCollection.Add(newÂ Resource() { ResourceName ="Dr.Darsy", TypeName =Â "Doctors"Â });
Schedule1.Appointments.Add(app);
Schedule1.Appointments.Add(app1);
{% endhighlight  %}
{% endtabs %}

## Adding Resources in code behind

Refer to the following code to add a resources in the code behind

{% tabs %}
{% highlight c# %}
SfSchedule schedule = new SfSchedule();
schedule.ScheduleType = ScheduleType.Week;
schedule.DayHeaderOrder = DayHeaderOrder.OrderByDate;
ResourceType resourceType = new ResourceType { TypeName = "Doctor" };
resourceType.ResourceCollection.Add(new Resource { DisplayName = "Dr.Jacob", ResourceName = "Dr.Jacob", });
resourceType.ResourceCollection.Add(new Resource { DisplayName = "Dr.Darsy", ResourceName = "Dr.Darsy" });
schedule.ScheduleResourceTypeCollection = new ObservableCollection<ResourceType> { resourceType };
schedule.Resource = "Doctor";
this.grid.Children.Add(schedule);
{% endhighlight %}
{% endtabs %}

## SubResource Support

This feature enables users to view appointments based on their subcategory only in day and week views. Using this feature, the end user can group appointments under various subcategories (resources). 

#### DayHeaderOrder property

[DayHeaderOrder](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.SfSchedule.html#Syncfusion_UI_Xaml_Schedule_SfSchedule_DayHeaderOrder) property is used to set the order by which resources have to be displayed

<table>
<tr>
<th>
Property</th><th>
Description</th></tr>
<tr>
<td>
SubResourceType</td><td>
Gets or sets the ResourceType value which is a SubResource type of its parent Resource type.</td></tr>
</table>

{% tabs %}
{% highlight xaml %}
<schedule:SfScheduleÂ x:Name="schedule1"Â ScheduleType="Week"
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Resource="Hospital"Â DayHeaderOrder="OrderByDate">
Â Â Â Â <schedule:SfSchedule.ScheduleResourceTypeCollection>
Â Â Â Â Â Â Â Â Â <schedule:ResourceTypeÂ TypeName="Hospital">
Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceType.ResourceCollection>
 Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceÂ DisplayName="Apollo Hospital"ResourceName="ApolloHospital"/>
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceÂ DisplayName="Malar Hospital"ResourceName="MalarHospital"/>
Â Â Â Â Â Â Â Â Â Â Â Â Â Â </schedule:ResourceType.ResourceCollection>
 Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceType.SubResourceType>
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceTypeÂ TypeName="Department">
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceType.ResourceCollection>
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceÂ DisplayName="Eye Department" ResourceName="Eye"/>
 Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â <schedule:ResourceÂ DisplayName="Heart Department"Â ResourceName="Heart"/>
         Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </schedule:ResourceType.ResourceCollection>
 Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â </schedule:ResourceType>
Â Â Â Â Â Â Â Â Â Â Â Â Â Â </schedule:ResourceType.SubResourceType>
Â Â Â Â Â Â Â Â  </schedule:ResourceType>
Â Â Â  </schedule:SfSchedule.ScheduleResourceTypeCollection>
</schedule:SfSchedule>
{% endhighlight  %}
{% highlight c# %}
SfSchedule schedule = new SfSchedule();
schedule.ScheduleType = ScheduleType.Week;
schedule.DayHeaderOrder = DayHeaderOrder.OrderByDate;
ResourceType resourceType = new ResourceType { TypeName = "Hospital" };
ResourceType subResourceType = new ResourceType { TypeName = "Department" };
resourceType.ResourceCollection.Add(new Resource { DisplayName = "Apollo Hospital", ResourceName = "ApolloHospital", });
resourceType.ResourceCollection.Add(new Resource { DisplayName = "Malar Hospital", ResourceName = "MalarHospital" });
subResourceType.ResourceCollection.Add(new Resource { DisplayName = "Eye Department", ResourceName = "Eye" });
subResourceType.ResourceCollection.Add(new Resource { DisplayName = "Heart Department", ResourceName = "Heart" });
schedule.ScheduleResourceTypeCollection = new ObservableCollection<ResourceType> { resourceType };
schedule.ScheduleResourceTypeCollection = new ObservableCollection<ResourceType> { subResourceType };
schedule.Resource = "Hospital";
schedule.Resource = "Department";
this.grid.Children.Add(schedule);
{% endhighlight  %}
{% endtabs %}

![WPF Scheduler with subresources](Resources_images/subresources.png)

## Number of Resources in Day View

This feature supports to display `N` number of resources in the Schedule view. You can achieve this by specifying the count of resources that needs to be displayed per view. This support is offered for `Day` view alone.

This support can be enabled by using property [DayViewColumnCount](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.SfSchedule.html#Syncfusion_UI_Xaml_Schedule_SfSchedule_DayViewColumnCount)Â inÂ `SfSchedule`. By default, its value is âzeroâ.

<table>
<tr>
<th>
Property</th><th>
Type</th><th>
Description</th></tr>
<tr>
<td>
DayViewColumnCount</td><td>
int</td><td>
Gets or sets a value to specify the number of resources that need to be shown in the view.</td></tr>
</table>

#### Example:

In the following code example, [DayViewColumnCount](https://help.syncfusion.com/cr/wpf/Syncfusion.UI.Xaml.Schedule.SfSchedule.html#Syncfusion_UI_Xaml_Schedule_SfSchedule_DayViewColumnCount) is âtwoâ, so the Scheduler displays two resources in the view. This count is maintained while scrolling to view the other resources.

{% tabs %}
{% highlight xaml %}
<syncfusion:SfScheduleÂ x:Name="Schedule"Â ScheduleType="Day"
Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Â Resource="Doctors"Â DayViewColumnCount="2">
Â Â Â Â <syncfusion:SfSchedule.ScheduleResourceTypeCollection>
Â Â Â Â Â Â Â Â <syncfusion:ResourceTypeÂ TypeName="Doctors">
Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:ResourceÂ ResourceName="Res1"Â DisplayName="Heart Treatments"/>
Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:ResourceÂ ResourceName="Res2"Â DisplayName="Cancer Treatments"/>
Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:ResourceÂ ResourceName="Res3"Â DisplayName="Diabetic Treatments"/>
Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:ResourceÂ ResourceName="Res4"Â DisplayName="Eye Treatments"/>
Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:ResourceÂ ResourceName="Res5"Â DisplayName="Psychology Treatments"/>
Â Â Â Â Â Â Â Â Â Â Â Â <syncfusion:ResourceÂ ResourceName="Res6"Â DisplayName="Dermatology Treatments"/>
Â Â Â Â Â Â Â Â </syncfusion:ResourceType>
Â Â Â Â </syncfusion:SfSchedule.ScheduleResourceTypeCollection>
</syncfusion:SfSchedule>
{% endhighlight  %}
{% highlight c# %}
SfSchedule schedule = new SfSchedule();
schedule.ScheduleType = ScheduleType.Day;
schedule.DayViewColumnCount = 0;
ResourceType resourceType = new ResourceType { TypeName = "Doctors" };
resourceType.ResourceCollection.Add(new Resource { ResourceName = "Res1", DisplayName = "Heart Treatments" });
resourceType.ResourceCollection.Add(new Resource { ResourceName = "Res2", DisplayName = "Cancer Treatments" });
resourceType.ResourceCollection.Add(new Resource { ResourceName = "Res3", DisplayName = "Diabetic Treatments" });
resourceType.ResourceCollection.Add(new Resource { ResourceName = "Res4", DisplayName = "Eye Treatments" });
resourceType.ResourceCollection.Add(new Resource { ResourceName = "Res5", DisplayName = "Psychology Treatments" });
resourceType.ResourceCollection.Add(new Resource { ResourceName = "Res6", DisplayName = "Dermatology Treatments" });
schedule.ScheduleResourceTypeCollection = new ObservableCollection<ResourceType> { resourceType };
schedule.Resource = "Doctors";
this.grid.Children.Add(schedule); 
{% endhighlight  %}
{% endtabs %}

The following screenshot shows a view with default value ofÂ `DayViewColumnCount`Â property set to âZeroâ.


![WPF Scheduler dayviewcolumnt with default value](Resources_images/default-value-of-dayviewcolumncount.png)

The following screenshot shows a view with default value ofÂ `DayViewColumnCount`Â property set to âTwoâ.

![WPF Scheduler dayviewcolumnt with custom value](Resources_images/dayviewcolumncount-settings.png)