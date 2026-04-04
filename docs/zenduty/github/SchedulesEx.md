---
id: SchedulesEx
title: Schedules Examples
---
## Example 1

Weekday evenings and Weekends divided between a team of 2.

### Ex 1: Visualization

* User 1 is on call on Mondays and Tuesdays from 5 pm to 8 am
* User 2 is on call on Wednesdays and Thursdays from 5pm to 8 am
* User 1 is on call from 5pm on Friday to 8 am on Monday
* User 1 is on call on Mondays and Tuesdays from 5 pm to 8 am.
* User 2 is on call on Wednesdays and Thursdays from 5pm to 8 am
* User 2 is on call from 5pm on Friday to 8 am on Monday

### Ex 1: Configuration

**Layer 1: Weekday Layer**

* Set the shift length to **2 Days**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order
* Add Layer Restrictions:
 	* Monday 5:00 pm to Tuesday 8:00 am
 	* Tuesday 5:00 pm to Wednesday 8:00 am
 	* Wednesday 5:00 pm to Thursday 8:00 am
 	* Thursday 5:00 pm to Friday 8:00 am

![](/img/schedules/1_1.png)

**Layer 2: Weekend Layer**

* Set the shift length to **1 Week**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order
* Add Layer Restrictions:
 	* Friday 5:00 pm to Monday 8:00 am

![](/img/schedules/1_2.png)

### Ex 1: Final Schedule

![](/img/schedules/1_3.png)

## Example 2

6 users alternate shift every week. One week, they work Mondays, Wednesdays and Fridays (MWF). The next week, they work Sundays, Tuesdays, Thursdays and Saturdays (STTS). There are a total of two six-week rotations, as everyone rotates through the MWF schedule, and one staggered by three weeks, where they work through STTS.

### Ex 2: Vizualization

* User 1 is on call on MWF from 12 am to 12 am in week 1
* User 4 is on call on STTS from 12 am to 12 am in week 1
* User 2 is on call on MWF from 12 am to 12 am in week 2
* User 5 is on call on STTS from 12 am to 12 am in week 2
* User 3 is on call on MWF from 12 am to 12 am in week 3
* User 6 is on call on STTS from 12 am to 12 am in week 3
* User 4 is on call on MWF from 12 am to 12 am in week 4
* User 6 is on call on STTS from 12 am to 12 am in week 4
* User 5 is on call on MWF from 12 am to 12 am in week 5
* User 1 is on call on STTS from 12 am to 12 am in week 5

### Ex 2: Configuration

**Layer 1: Mondays, Wednesdays, Fridays (MWF)**

* Set the shift length to **1 Week**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order 1-6
* Add Layer Restrictions:
 	* Monday 12:00 am to Tuesday 12:00 am
 	* Wednesday 12:00 am to Thursday 12:00 am
 	* Friday 12:00 am to Saturday 12:00 am

![](/img/schedules/2_1.png)

**Layer 2: Sundays, Tuesdays, Thursdays, Saturdays (STTS)**

* Set the shift length to **1 Week**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order 1-6
* Add Layer Restrictions:
 	* Tuesday 12:00 am to Wednesday 12:00 am
 	* Thursday 12:00 am to Friday 12:00 am
 	* Saturday 12:00 am to Monday 12:00 am

![](/img/schedules/2_2.png)

### Ex 2: Final Schedule

![](/img/schedules/2_3.png)

## Example 3

6 users with different shifts throughout the week

### Ex 3: Vizualization

* Monday: User 1 for 8 hours, User 2 for 8 hours and User 3 for 8 hours
* Tuesday: User 4 (6 hours), User 2 (6 hours) and User 3 for 12 hours
* Wednesday: User 1 (8 hours), User 2 (8 hours) and User 3 (8 hours)
* Thursday: User 4 (6 hours), User 2 (6 hours) and User 3 for 12 hours
* Friday to Sunday: User 5 (12 hours), User 6 (12 hours)

### Ex 3: Configuration

**Layer 1: Mondays and Wednesdays**

* Set the shift length to **8 Hours**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order 1-3
* Add Layer Restrictions:
 	* Monday 12:00 am to Tuesday 12:00 am
 	* Wednesday 12:00 am to Thursday 12:00 am

![](/img/schedules/3_1.png)

**Layer 2: Tuesdays and Thursdays**

* Set the shift length to **6 Hours**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order 4,2,3,3
* Add Layer Restrictions:
 	* Tuesday 12:00 am to Wednesday 12:00 am
 	* Thursday 12:00 am to Friday 12:00 am

![](/img/schedules/3_2.png)

**Layer 3: Fridays, Saturdays, Sundays**

* Set the shift length to **12 Hours**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order 5-6
* Add Layer Restrictions:
 	* Friday 12:00 am to Monday 12:00 am

![](/img/schedules/3_3.png)

### Ex 3: Final Schedule

![](/img/schedules/3_4.png)

## Example 4

6 users in the rotation with 2 users on call at all times

### Ex 4: Vizualization

* Users 1 and 2 are on call from 8 am to 8 pm from Mon-Thu
* Users 3 and 4 are on call from 8 pm to 8 am from Mon-Thu
* Users 5 and 6 are on call all of Friday-Sun

### Ex 4: Configuration

**Layer 1: Day and Night - 1**

* Set the shift length to **12 Hours**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order 1, 3
* Add Layer Restrictions:
 	* Monday 8:00 am to Friday 8:00 am
 
![](/img/schedules/4_1.png)

**Layer 1: Day and Night - 2**

* Set the shift length to **12 Hours**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the users in order 3, 4
* Add Layer Restrictions:
 	* Monday 8:00 am to Friday 8:00 am

![](/img/schedules/4_2.png)

**Layer 3: Fridays-Sundays - 1**

* Set the shift length to **1 Week**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the user: 5
* Add Layer Restrictions:
 	* Friday 8:00 am to Monday 8:00 am

![](/img/schedules/4_3.png)

**Layer 3: Fridays-Sundays - 1**

* Set the shift length to **1 Week**
* Set a start and end time for this rotation (this month/quarter/year/custom)
* Add the user: 6
* Add Layer Restrictions:
 	* Friday 8:00 am to Monday 8:00 am

![](/img/schedules/4_4.png)

### Ex 4: Final Schedule

![](/img/schedules/4_5.png)
