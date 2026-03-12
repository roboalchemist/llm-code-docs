# Source: https://doc.keepnetlabs.com/next-generation-product/platform/reports/security-growth-employee-dashboard.md

# Security Growth Employee Dashboard

This dashboard gives every employee a personal view of their security awareness progress. The **Security Growth Employee Dashboard** lets employees see their training enrollments, points, rank, badges, phishing performance and certificates all in one place.

## 1. Benefits for Your Organization and Employees

**For your organization**

* Increases completion of security training
* Makes security performance transparent for everyone
* Reduces support questions like “Which trainings do I still owe? Where are my certificates?”
* Supports global teams with multi-language support (EN, TR, DE, FR, ES, …)

**For employees**

* One place to see all assigned trainings and due items
* Overview of reporting phishing simulation emails
* Clear points, rank and badges to understand performance
* Easy access to certificates
* Dashboard in their preferred language

## 2. How Employees Access Dashboard

1. Go to [**https://dash.keepnetlabs.com/users-dashboard-login**](https://dash.keepnetlabs.com/users-dashboard-login)
2. Enter work email address
3. Choose sign-in method:
   * **SSO/SAML** (if your organization uses it), or
   * **Continue with Email**
4. If using email login, open the email **“Security Growth Login”** and click **“Login to Platform”**
5. The dashboard opens in the browser

## 3. What Employees See – Field by Field

This section explains every card and table on the Security Growth Dashboard so admins know **what each number means** and **how to use it**.

### 3.1 Overall Performance

**Card title:** *Overall Performance – Track your performance, points, and rank for the last 30 days.*

* **Performance (%)**
  * **What it is:** A single score for the last 30 days (e.g. `41%`).
  * **What it means:** Overall security behaviour, combining training, phishing, and other scored actions. Higher = better.
* **Points**
  * **What it is:** Total points the user has earned.
  * **What it means:** The user's current total points from the leaderboard activities. [The user can earn more ](https://doc.keepnetlabs.com/next-generation-product/platform/reports/gamification-report)if the user doesn't open or fail to complete simulations, complete the training and such other actions.
* **Rank**
  * **What it is:** The user’s position compared to others (1 = top performer).
  * **What it means:** Shows how this user compares to the other three employees with good performance at the same company.
* **See Ranking Details**
  * Opens the **Leaderboard** area to see where these numbers sit among all users.

### 3.2 Recent Badges

**Card title:** *Recent Badges – View your last 3 badges earned from your actions and behaviours.*

Each badge tile shows:

* **Badge name & icon** – e.g., *Perfect Score*, *Zero Click Champion*.
* **Earned on \[date]** – the date the badge was awarded.

**See All Badges** scrolls to the **Your Badges** section where all possible badges are listed.

Use this to see which positive behaviours are being rewarded (e.g. perfect exam scores, reporting phishing).

### 3.3 Your Learning

**Card title:** *Your Learning – See all your completed and assigned trainings in one place.*

**Table columns:**

* **Training Material Name:** The title of the assigned training.
* **Start Date:** The date the training became available/assigned.
* **Training Status**
  * *Not Started* – user has never opened it.
  * *Not Completed* – opened but not finished.
  * *Completed* – finished according to completion rules.
* **Certificate**
  * *Available* – this training provides a certificate when completed.
  * *Not Available* – no certificate for this training item.
* **Points:** Points that can be earned or already earned for this training (e.g., `50`).
* **Actions (▶ icon):** Opens the completed training or click to resume not completed/not started training.

This table is the user’s personal “training backlog” and helps you answer “Which training I have completed and not completed yet?”.

#### 3.4 Your Phishing Test Results

**Card title:** *Your Phishing Test Results – Overview of your phishing activity results from the last 30 days.*

This section has **three cards**:

1. **Reported Phishing Emails (e.g. 0/39)**
   * **Left number:** how many simulated phishing emails the user **correctly reported**.
   * **Right number:** how many simulated phishing emails the user **received**.
   * Message below (e.g. *“No points earned for your reported emails yet”*) explains current point impact.
2. **Phishing Simulations (e.g. 39/39)**
   * Shows the total simulations and how many were **missed/not reported**.
   * Message below (e.g. *“E.g: You lost -7000 points for missed reported emails.”*) shows penalty points for risky behaviour (clicking, submitting data, not reporting).
3. **Detection Accuracy (e.g. 0% success rate)**
   * Approximate logic: **Detection Accuracy ≈ reported simulations / total delivered simulations for this user.**
   * Message below compares to the previous period (e.g. *“unchanged from last month”*).

Quickly tells if you are **catching** phishing simulations or consistently failing them.

### 3.5 Leaderboard

**Card title:** *Leaderboard – Employee performance rankings over the last 30 days.*

Two parts:

1. **Top 3 cards (Gold / Silver / Bronze)**
   * Show the three highest-scoring users with name, email, and performance.
2. **Leaderboard table**
   * **Rank** – position in the list.
   * **First Name / Last Name** – user’s name.
   * **Email** – user’s email.
   * **Department** – department info from user profile.
   * **Performance** – same percentage concept as Overall Performance.
   * **Total Points** – points behind the rank.
   * The logged-in user is marked with **“You”**, so you can find your current rank easily compared to top performers.

Good for spotting top performers and comparing departments or individuals.

### 3.6 Your Activity Timeline

**Card title:** *Your Activity Timeline – A timeline of your recent activities and their outcomes from the last 30 days.*

Each row is a time-stamped event, such as:

* **Email Sent** – an enrollment or reminder email was sent to the user.
* **Email Opened** – user opened the training or phishing email.
* **Clicked Training** – user clicked into a training; the text explains points gained/lost, category, and timing.

Right-hand side: **date & time (UTC)** of the event.

**Load More Activities** shows older items.

Use this to see your activities such as opening, clicking the simulation or completing/not completing training and many more activities. This page will also show you how many points you lost or earned based on your actions.

### 3.7 Your Certificates

**Card title:** *Your Certificates – See all your earned and pending certificates in one place.*

**Table columns:**

* **Certificate Name** – name of the certificate.
* **Certificate Date** – issue date / completion date.
* **Training Status** – *Not Started*, *Not Completed*, or *Completed*.
* **Actions**
  * **Download (⬇)** – download the certificate PDF (for completed trainings with certificates).
  * **Play (▶)** – open the related training and complete it to earn the certificate.

### 3.8 Your Badges

**Card title:** *Your Badges – See all your earned and available badges in one place.*

Each badge tile shows:

* **Name & icon** – e.g., *First Training Completed*, *Zero Click Champion*.
* **Earned on \[date]** – if the badge is earned.
* **Not earned yet** – shown in grey for badges not yet achieved.

You can see which behaviours of yours are rewarded for and which achievements you can still work towards to achieve the badges.

### 3.9 Profile panel & Language selector

**Profile panel (person icon, top-right):**

* Name: Your name/surname
* Email: Your email address
* Department: Your department name
* Phone Number: Your phone number
* Preferred Language: Your preferred language
* **Logout** button: Click to sign out from the dashboard

**Language selector (dropdown):**

* Lets the user switch the entire dashboard UI to a supported language\
  (e.g. English (UK/US), Turkish, Deutsch, Français, Español).

## 4. How to Announce It to Employees

You can use this short template to announce this dashboard to your employees via email.

> **Subject:** Your Security Growth Dashboard is Live
>
> Dear Colleagues,
>
> You now have access to your **Security Growth Dashboard**, where you can see your security trainings, points, rank, phishing results and certificates all in one place.
>
> To access it:
>
> 1. Go to [**https://dash.keepnetlabs.com/users-dashboard-login**](https://dash.keepnetlabs.com/users-dashboard-login)
> 2. Enter your work email and follow the sign-in steps
> 3. Open the **“Security Growth Login”** email and click **“Login to Platform”**
>
> You can change the dashboard language from the top-right menu after logged in to dashboard.
>
> Thank you for helping to strengthen our security culture.

***

## 5. FAQs

### **Q: Do test campaigns count on my dashboard?**

A: No. Campaigns or training enrollments marked as **Mark as Test** are not included in your phishing test results, points, or leaderboard. Only non-test data is shown.

### **Q: Do employees need a new password?**

A: No. They either use SSO/SAML or a one-time email login link.

### **Q: Can employees see other people’s details?**

A: No. Each user only sees their own detailed data. Leaderboards show limited info for rankings only.

### **Q: What if the email doesn’t arrive?**

A: Ask them to check spam/junk and confirm they used their registered work email. If it still fails, contact [Keepnet Support](https://doc.keepnetlabs.com/resources/keepnet-support-help-desk).
