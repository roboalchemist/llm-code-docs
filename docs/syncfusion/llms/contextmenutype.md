# Source: https://docs.syncfusion.com/wpf/classic/schedule/contextmenutype.md

# ContextMenuType in WPF Schedule (Classic)

The collection of MenuItem elements can be organized by ContextMenuType property.
{% tabs %}
{% highlight html %}



	<Schedule:SfSchedule x:Name="schedule"   ScheduleType="Week" ContextMenuType="RadialMenu">

	</Schedule:SfSchedule>

{% endhighlight  %}


{% highlight c# %}



SfSchedule schedule = new SfSchedule();

schedule.ScheduleType = ScheduleType.Week;

schedule.EnableTouch = true;  

this.grid.Children.Add(schedule);



{% endhighlight  %}
{% endtabs %}

![ContextMenuTypeimg1](ContextMenuType_images/ContextMenuType_img1.png)



![ContextMenuTypeimg2](ContextMenuType_images/ContextMenuType_img2.png)





