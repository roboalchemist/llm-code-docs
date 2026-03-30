# Source: https://doc.keepnetlabs.com/next-generation-product/platform/reports/gamification-report.md

# Gamification Report

The **Gamification Report** motivates users to actively engage in phishing simulations (Phishing, Callback, Vishing, Smishing, Quishing) and security awareness training by using a points system. Users earn points for positive actions and lose points for risky behaviors, helping to improve security awareness.

The feature includes a leaderboard to display top performers, with Gold, Silver, and Bronze badges for the top three. It also provides a live ranking view and an all-time top 10 list, making it easy for administrators to monitor progress and recognize achievements, fostering a more security-conscious workplace.

## How to Access Gamification Report

* Log in to the platform.
* Go to **Reports > Gamification Report** page from the left-hand menu to access the report.

## How to Understand Gamification Report

The **Gamification** **Report** comprises several key components:

* **Leaderboard:** Displays user rankings based on points accumulated through actions in simulations and training.
  * **Top Performers:** Highlights the top three users for a chosen timeframe, awarding **Gold**, **Silver**, and **Bronze** badges accordingly. These are your top three most security-aware users.
  * **Ongoing Period Ranking:** Provides a live ranking table of users in the selected date range period, detailing rank, name, email, department, performance, total points.
* **Details:** Click the "Details" button to view a user's statistics. Use filters like **Activity** **Type**, **Product**, or **Difficulty** **Level** to find specific information.
* **Date Range:** Select a specific timeframe for viewing user performance data for that period.
* **Filtering and Sorting:** The leaderboard table supports search, filtering, and sorting functionalities, allowing administrators to view specific groups or individuals.
* **Export Options:** Download the leaderboard data in CSV, Excel, or PDF formats for further analysis.

## Understanding Points and Performance Calculations

The **Gamification Report** awards points for positive actions and deducts points for risky actions. This scoring system applies across different simulation types (Phishing, Callback, Vishing, Smishing, Quishing) and Security Awareness Training.

{% hint style="info" %}
**Mark as Test:** Gamification points and leaderboard rankings do **not** include actions from campaigns or training reports marked as **Mark as Test**. Test campaigns and test enrollments are excluded from point and statistics calculations.
{% endhint %}

### Simulations Scoring

Each simulation type has specific actions with associated points based on the difficulty level (Easy, Medium, Hard):

1. **Phishing Simulation**
   * **No Response**: 0 points.
   * **Opened Email**: 0 points.
   * **Clicked Link**:
     * Easy: -200 points
     * Medium: -100 points
     * Hard: -50 points
   * **Submitted Data**:
     * Easy: -400 points
     * Medium: -200 points
     * Hard: -100 points
   * **Opened Attachment**:
     * Easy: -300 points
     * Medium: -150 points
     * Hard: -75 points
   * **Submitted MFA Code**:
     * Easy: -400 points
     * Medium: -200 points
     * Hard: -100 points
2. **Callback Simulation**
   * **No Response**: 0 points.
   * **Opened Email**: 0 points.
   * **Called Back**:
     * Easy: -200 points
     * Medium: -100 points
     * Hard: -50 points
   * **Entered Digits** (in response to the call):
     * Easy: -300 points
     * Medium: -150 points
     * Hard: -75 points
3. **Vishing Simulation**
   * **No Response**: 0 points.
   * **Answered Call**:
     * Easy: -100 points
     * Medium: -50 points
     * Hard: -25 points
   * **Vished** (followed scam instructions):
     * Easy: -300 points
     * Medium: -150 points
     * Hard: -75 points
4. **Smishing Simulation**
   * **No Response**: 0 points.
   * **Clicked Link**:
     * Easy: -200 points
     * Medium: -100 points
     * Hard: -50 points
   * **Submitted Data**:
     * Easy: -300 points
     * Medium: -150 points
     * Hard: -75 points
   * **Submitted MFA Code**:
     * Easy: -400 points
     * Medium: -200 points
     * Hard: -100 points
5. **Quishing (QR Code Phishing)**
   * **No Response**: 0 points.
   * **Scanned QR Link**:
     * Easy: -200 points
     * Medium: -100 points
     * Hard: -50 points
   * **Submitted Data**:
     * Easy: -300 points
     * Medium: -150 points
     * Hard: -75 points
   * **Submitted MFA Code**:
     * Easy: -400 points
     * Medium: -200 points
     * Hard: -100 points
   * **Incident Responder (an employee reports an email)**
     * Reported Malicious email: +500 points
     * Reported Phishing email: +500 points

When a user **reports a real (non-simulated) email** and an analyst **confirms it as Phishing or Malicious** in **Incident Responder**, the user receives **+500 points**. These points are shown in the **Gamification Report > User Timeline** within the Activity Timeline card for that user, so both admins and users can see that secure reporting behavior was recognized.

### Security Awareness Training Scoring

1. **No Response**: 0 points.
2. **Opened Email** (but did not click): -100 points.
3. **Clicked Training Link**: +50 points.
4. **Completed Training**: +100 points.
5. **Passed Exam**: +200 points.
6. **Failed Exam**: -150 points.
7. **Joined Training within 24 Hours**: +100 extra points.
8. **Joined 1-3 Days After Invitation**: 0 points.
9. **Joined After 3 Days**: -50 points.

### Reporting Phishing Emails Scoring

If users report suspicious emails promptly, they receive additional points based on the time taken to report:

| Time Taken           | Easy Points | Medium Points | Hard Points |
| -------------------- | ----------- | ------------- | ----------- |
| **Within 5 Minutes** | +100        | +200          | +400        |
| **5-10 Minutes**     | +75         | +150          | +300        |
| **After 10 Minutes** | +50         | +100          | +200        |

### Performance Percentage Calculation

The **Performance Percentage** helps to measure a user’s performance based on the points they have earned compared to the maximum points they could have achieved.

The formula is:

Performance Percentage = (Total Points Earned / Total Possible Points) \* 100

* **Total Points Earned**: The total points the user has scored from their actions in simulations and training.
* **Total Possible Points**: The highest possible points the user could have earned from all the simulations they participated in.

**Special Rules**:

* If the user’s **Total Points** are negative, their **Performance Percentage** is set to 0%.
* If the user’s **Total Points** are positive, the percentage is calculated using the formula above.

**Interpreting the Performance Percentage**:

* **80% or higher**: This is considered good performance.
* **Below 50%**: This suggests the user may need more training.

For more information, please contact [support](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk).

## Tutorial Video

This tutorial provides a detailed description of the Gamification Report product. You can understand the basic functions of the Gamification Report page and use the Gamification Report by following this tutorial.

{% embed url="<https://youtu.be/lDRdN1czw74>" %}

## FAQ

### Q: I don't see total target users in my gamification report; why is that?

A: The "No Response" users are not shown on the gamification report. The users who had interaction with the simulation and training are shown on the report as explained in the document.

### Q: Can I see deleted training enrollment statistics in the Gamification Report?

**A:** No. Enrollments that have been deleted and moved to the Trash page are no longer displayed or included in the timeline metrics of the Gamification Report.
