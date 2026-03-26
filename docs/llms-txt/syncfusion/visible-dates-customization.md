# Source: https://docs.syncfusion.com/wpf/classic/schedule/visible-dates-customization.md

# Visible-Dates-customization in WPF Schedule (Classic)

All views in the schedule have their own number of visible dates. The SfSchedule control allows users to view multiple dates in the day and time line views.

If users want to view particular dates in a single view, users can provide a DateTime collection to theÂ ScheduleDateRangeÂ property to view the particular dates in the day and time line view types.

{% highlight c# %}


ObservableCollection<DateTime> visibleDates =Â newObservableCollection<DateTime>();

Â Â Â Â Â Â Â Â Â Â Â Â DateTimeÂ Date1 =Â newÂ DateTime(2013, 9, 1);

Â Â Â Â Â Â Â Â Â Â Â Â DateTimeÂ Date2 =Â newÂ DateTime(2013, 9, 22);

Â Â Â Â Â Â Â Â Â Â Â  visibleDates.Add(Date1);

Â Â Â Â Â Â Â Â Â Â Â  visibleDates.Add(Date2);

Â Â Â Â Â Â Â Â Â Â Â Â SfScheduleÂ schedule =Â newÂ SfSchedule();

Â Â Â Â Â Â Â Â Â Â Â  schedule.ScheduleDateRange= visibleDates;

{% endhighlight %}

![Multiple dates visbiled](Visible-Dates-customization_images/Visible-Dates-customization_img1.jpeg)





![Single date visible](Visible-Dates-customization_images/Visible-Dates-customization_img2.jpeg)



