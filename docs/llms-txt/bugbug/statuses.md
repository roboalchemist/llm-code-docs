# Source: https://docs.bugbug.io/running-tests/statuses.md

# Statuses

When you run a test, you will see one of the following statuses:

### Test passed

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FTnYdtUoAUgqOvE5gWcQ8%2FScreenshot%202022-04-11%20at%2017.59.23.png?alt=media\&token=b267fbf9-452c-4808-825b-1a7c47057cd5)&#x20;

Everything worked as it should

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MKixgeBPbLvnD0l1eiV%2F-MMDDkyLR29CghHPRNnB%2F-MMDFTD5fAs-HhT7DMJW%2FScreenshot%202020-11-16%20at%2000.33.22.png?alt=media\&token=c761b425-4791-40ef-9a90-23640b0cd1a5)

### Test failed

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FWE6t2PANQIiRsVQzwXYR%2FScreenshot%202022-04-11%20at%2017.59.34.png?alt=media\&token=d9c6b2b3-772e-43be-87d1-ac5ced342c95)

The test has not finished because an assertion failed or it was not possible to continue running the test steps and the test finished because of the [timeout](https://docs.bugbug.io/preventing-failed-tests/timeout).

You will get additional error information when this happens and tips on what to do to fix it.

Learn more on how to [debug and modify a step](https://docs.bugbug.io/debugging-tests).

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FN95fsW44SEozToyA84rl%2FScreenshot%202022-04-11%20at%2017.54.21.png?alt=media\&token=135b4813-b6ca-43d6-8e0d-9f3947cd0de9)

### Test passed but some waiting conditions were skipped

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FC2lXfvvmcitqOIMHwcyu%2FScreenshot%202022-04-11%20at%2017.59.19.png?alt=media\&token=4dc50070-1cf7-4729-ab9d-8f63656be3b0)&#x20;

This status is indicated by a green circle that's empty inside.

This is a unique BugBug feature for preventing failed tests. This indicates that the user is able to finish your test, but you can take a look at the reason for skipped [waiting conditions](https://docs.bugbug.io/preventing-failed-tests/waiting-conditions) just to make sure that your tests are in a good condition.

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FRYPY0BHacucKtrvnH0M7%2FScreenshot%202022-04-11%20at%2017.55.51.png?alt=media\&token=e5fd992e-22ca-42d9-9360-14a10b72631c)

### Test error / crashed

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FidZQ2QiqrT2nDkmjoXdf%2FScreenshot%202022-04-11%20at%2018.00.47.png?alt=media\&token=2a95018f-6d21-473f-8145-a0e12133341e)

The test encountered an error, which is not a result of the test steps, ex. internal server error, BugBug extension error, etc. This is most likely caused by a bug - please contact us if you see this status often.

### Test paused for debugging

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FwYl7wXuG4TXehSExdHfh%2FScreenshot%202022-04-12%20at%2010.58.47.png?alt=media\&token=7d8977ad-98f3-4360-8cb5-c1a49130f015)

You used a [breakpoint](https://docs.bugbug.io/debugging-tests/breakpoint-run-step-by-step) or paused the test in the middle of execution using "Pause" button

### Test stopped

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FUSZIYgOmuJis6bt9ClH9%2FScreenshot%202022-04-12%20at%2011.00.02.png?alt=media\&token=e17d03a3-9f90-4e24-ba92-1ff5b6c2fbaf)

You stopped the test before it finished running, before it reached a conclusion.

### Test running

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FU2cuozFzTskMVzUvcD8h%2FScreenshot%202022-04-12%20at%2011.01.37.png?alt=media\&token=790e9bcd-059d-42cb-b38c-9a04ebccb538)

Test is running, execution in progress
