# Source: https://firebase.google.com/docs/functions/schedule-functions.md.txt

<br />

If you want to schedule functions to run at specified times, use the`onSchedule`handler provided by`firebase-functions/v2/scheduler`. These functions use[Cloud Scheduler](https://cloud.google.com/scheduler/)to invoke function logic at the times or intervals that you define.

## Before you begin

Though scheduled functions are billed, you can expect the overall cost to be manageable, as eachCloud Schedulerjob costs $0.10 (USD) per month, and there is an allowance of three jobs per Google account, at no charge. Use the Blaze[pricing calculator](https://firebase.google.com/pricing#blaze-calculator)to generate a cost estimate based on your projected usage.

TheCloud SchedulerAPI must be enabled for your project. It should already be enabled for most Firebase projects; you can verify in the[Google Cloud console](https://console.cloud.google.com/).

## Write a scheduled function

InCloud Functions for Firebase, scheduling logic resides in your functions code, with no special deploy-time requirements. For example, to clean up inactive user accounts once daily, you could write a function starting with the following import statements:  

### Node.js

    // The Cloud Functions for Firebase SDK to set up triggers and logging.
    const {onSchedule} = require("firebase-functions/scheduler");
    const {logger} = require("firebase-functions");

    // The Firebase Admin SDK to delete inactive users.
    const admin = require("firebase-admin");
    admin.initializeApp();

    // The es6-promise-pool to limit the concurrency of promises.
    const PromisePool = require("es6-promise-pool").default;
    // Maximum concurrent account deletions.
    const MAX_CONCURRENT = 3;  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/delete-unused-accounts-cron/functions/index.js#L20-L31

### Python

    # The Cloud Functions for Firebase SDK to set up triggers and logging.
    from firebase_functions import scheduler_fn

    # The Firebase Admin SDK to delete users.
    import firebase_admin
    from firebase_admin import auth

    firebase_admin.initialize_app()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/delete-unused-accounts-cron/functions/main.py#L19-L26

Then, you could use`onSchedule`to start aCloud Schedulertask:  

### Node.js

    // Run once a day at midnight, to clean up the users
    // Manually run the task here https://console.cloud.google.com/cloudscheduler
    exports.accountcleanup = onSchedule("every day 00:00", async (event) => {
      // Fetch all user details.
      const inactiveUsers = await getInactiveUsers();

      // Use a pool so that we delete maximum `MAX_CONCURRENT` users in parallel.
      const promisePool = new PromisePool(
          () => deleteInactiveUser(inactiveUsers),
          MAX_CONCURRENT,
      );
      await promisePool.start();

      logger.log("User cleanup finished");
    });  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Node/delete-unused-accounts-cron/functions/index.js#L35-L49

### Python

    # Run once a day at midnight, to clean up inactive users.
    # Manually run the task here https://console.cloud.google.com/cloudscheduler
    @scheduler_fn.on_schedule(schedule="every day 00:00")
    def accountcleanup(event: scheduler_fn.ScheduledEvent) -> None:
        """Delete users who've been inactive for 30 days or more."""
        user_page: auth.ListUsersPage | None = auth.list_users()
        while user_page is not None:
            inactive_uids = [
                user.uid for user in user_page.users if is_inactive(user, timedelta(days=30))
            ]
            auth.delete_users(inactive_uids)
            user_page = user_page.get_next_page()  
    https://github.com/firebase/functions-samples/blob/a6ae4cbd3cf2fff3e2b97538081140ad9befd5d8/Python/delete-unused-accounts-cron/functions/main.py#L31-L42

Both Unix Crontab andApp Enginesyntax are supported byCloud Scheduler. For example, to use Crontab, do something like this:  

### Node.js

    exports.scheduledFunctionCrontab = onSchedule("5 11 * * *", async (event) => {
      // ...
    });

### Python

    @scheduler_fn.on_schedule(schedule="5 11 * * *")

| **Important:** Depending on how you design your scheduling logic, a function may be triggered multiple times, with the next instance running while the previous instance is still executing.

## Deploy a scheduled function

When you deploy a scheduled function, a scheduler job and an HTTP function are created automatically. TheFirebaseCLI echoes the function name, and you can view the job and the function in the[Google Cloud console](https://console.cloud.google.com/project/_/cloudscheduler). The topic is named according to the following convention:

**firebase-schedule-<var translate="no">function_name</var>-<var translate="no">region</var>**

For example:

**firebase-schedule-accountcleanup-us-east1.**

At the scheduled time, the default compute service account invokes the associated HTTP function. This means that only the associatedCloud Schedulerjob has permission to run the function.
| **Important:** Make sure you do not manually delete or modify the function or scheduler job in the console. Doing this could cause errors in the execution of your scheduled function.