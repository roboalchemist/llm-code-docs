# Source: https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/user-availability-insights/the-user-insights-report.md

# The User Insights Report

### User Insights Report <a href="#user-insights-report" id="user-insights-report"></a>

As part of the Insights feature, a standard report is available that summarizes you or your team's availability data. It shows:

* Planned leave data
* Non-working days
* Trend of duration of activities
* Overall sentiment
* Sentiment trend

<figure><img src="https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FtJZmEB1yEvgdwNTOZ7On%2Fimage.png?alt=media&#x26;token=fd3f70cc-9ab5-4e98-aaa5-b2ebb435b179" alt=""><figcaption></figcaption></figure>

More information about these visuals can be seen in the table below:

| Report Visual                | Description                                                                                                                                                                                                          | Logic                                                                                                                                                                                                                                                                                                                                                                                                                                        | Filters Applicable |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| Leaves                       | Shows the Daily/Weekly/Monthly trend of planned leave count by the user. If the logged in user is a team manager then it will also show leave count for their team members.                                          | 1. Count all rows where Work Day Type = "Leave" 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                                   | Date, User name    |
| Non-working days             | Shows the Daily/Weekly/Monthly trend of non working days count for the user. If the logged in user is a team manager then it will also show non working days count for their team members.                           | 1. Count all rows where Work Day Type = "WeekOff" 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                                 | Date, User name    |
| Avg. duration trend (in hrs) | Shows the average Daily/Weekly/Monthly trend of various durations entered by the user. If the logged in user is a team manager then it will also show average durations for their team members.                      | 1. Calculate the average of DurationSpentInEnate, AdHocDuration, DowntimeDuration, FeedbackDuration, MeetingDuration, DurationSpentOutsideEnate, TrainingDuration by excluding any WeekOff and leaves 2. DurationSpentInEnate is calculated as total duration recorded in packet activities by each user on each day where activity type in (2,3) 3. Filter the rows for the "logged in user" and any user whose manager is "logged in user" | Date, User name    |
| Overall sentiment            | Shows the overall percentage share of each sentiment opted by the user. If the logged in user is a team manager then it will also show the percentage share of sentiments for their team members.                    | 1. Calculate the count of sentiments for each sentiment type 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                      | Date, User name    |
| Sentiment trend              | Shows the Daily/Weekly/Monthly trend of percentage share of sentiment entered by the user. If the logged in user is a team manager then it will also show the percentage share of sentiments for their team members. | 1. Calculate the count of sentiments for each sentiment type 2. Filter the rows for the "logged in user" and any user whose manager is "logged in user"                                                                                                                                                                                                                                                                                      | Date, User name    |

#### Available Datasets

The Team View Report contains the following available data sets:

| Table          | Fields                            | Description                                                                                          |
| -------------- | --------------------------------- | ---------------------------------------------------------------------------------------------------- |
| Date           | Date                              | Day of the week in DDMM Format                                                                       |
| Date           | Week                              | Week of the year                                                                                     |
| Date           | Month                             | Month of the Year in MMYY format                                                                     |
| Date           | Year                              | Calendar Year                                                                                        |
| Sentiment type | Sentiment                         | Sentiments options (Excellent, Very Good, Good, Bad, Worse). It will be none if not entered.         |
| Insights       | Avg. other hours                  | Avg. hours spent on ad hoc tasks                                                                     |
| Insights       | Avg. contractual break hours      | Avg. hours spent on breaks                                                                           |
| Insights       | Avg. idle hours                   | Avg. hours spent on system downtime                                                                  |
| Insights       | Avg. feedback/1-2-1 hours         | Avg. hours spent on feedback sessions                                                                |
| Insights       | Avg. work performed within Enate  | Avg. hours spent in Enate (on cases, actions or tickets)                                             |
| Insights       | Avg. work performed outside Enate | Avg. value added hours spent outside the Enate                                                       |
| Insights       | Avg. meeting hours                | Avg. hours spent on meetings                                                                         |
| Insights       | Avg. training hours               | Avg. hours spent on training sessions                                                                |
| Insights       | Avg. working hours                | Avg. working hours                                                                                   |
| Insights       | Other hours                       | Total hours spent on adhoc tasks                                                                     |
| Insights       | Contractual break hours           | Total hours spent on breaks                                                                          |
| Insights       | Downtime hours                    | Total hours spent on system downtime                                                                 |
| Insights       | Feedback/1-2-1 hours              | Total hours spent on feedback sessions                                                               |
| Insights       | Work performed within Enate       | Total hours spent in Enate (specifically on Cases, Actions or Tickets)                               |
| Insights       | Work performed outside Enate      | Total value-added hours spent outside the Enate                                                      |
| Insights       | Leaves count                      | Planned leave count for the user(s)                                                                  |
| Insights       | Meeting hours                     | Total hours spent on meetings                                                                        |
| Insights       | Non-working days count            | Non-working day count for the user(s) includes holidays weekends etc                                 |
| Insights       | Sentiment count                   | Count of sentiments entered by user(s) for a particular day                                          |
| Insights       | Training hours                    | Total hours spent on training sessions                                                               |
| Insights       | Working hours                     | Total working hours                                                                                  |
| Insights       | Comment                           | Comments added by user for the sentiment chosen                                                      |
| Insights       | Insights date                     | Date when the durations/sentiments captured from the user                                            |
| Users          | Email address                     | Email address of the user(s)                                                                         |
| Users          | User name                         | Full name of the user(s)                                                                             |
| WorkDay type   | Work day                          | Type of the day (Working, Non-working Day, Leave). It will be none if nothing is chosen by the user. |
