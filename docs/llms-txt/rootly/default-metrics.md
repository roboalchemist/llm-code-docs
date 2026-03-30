# Source: https://docs.rootly.com/metrics/default-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Default Metrics

> Comprehensive overview of built-in metrics and dashboards including MTTD, MTTA, MTTR, incident breakdowns, and alert analytics.

## Overview

### Number of incidents 

| Title       | # of Incidents                                                     |
| :---------- | :----------------------------------------------------------------- |
| Description | -                                                                  |
| Type        | Aggregate value                                                    |
| Collection  | Incidents                                                          |
| Filter by   | Kind > is > Normal  Kind > is > Normal sub  Kind > is > Backfilled |
| Operation   | Count                                                              |
| Key         | Results                                                            |

### **Number of Retrospectives**

| Title       | # of Retrospectives                                                                        |
| :---------- | :----------------------------------------------------------------------------------------- |
| Description | -                                                                                          |
| Type        | Aggregate value                                                                            |
| Collection  | Retrospectives                                                                             |
| Filter by   | Incident Kind > = > Normal  Incident Kind > = > Normal sub  Incident Kind > = > Backfilled |
| Operation   | Count                                                                                      |
| Key         | Results                                                                                    |

### **Number of Action items**

| Title       | # of Action Items |
| :---------- | :---------------- |
| Description | -                 |
| Type        | Aggregate value   |
| Collection  | Action Items      |
| Filter by   | -                 |
| Operation   | Count             |
| Key         | Results           |

### **Mean Time to Detection MTTD**

| Title       | MTTD (Mean Time To Detection)                                   |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Aggregate value                                                 |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Operation   | Average                                                         |
| Key         | Time to Detected                                                |

### **Mean Time to Acknowledge MTTA**

| Title       | MTTA (Mean Time To Acknowledge)                                 |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Aggregate value                                                 |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Operation   | Average                                                         |
| Key         | Time to Acknowledge                                             |

### **Mean Time ot Mitigation MTTM**

| Title       | MTTM (Mean Time To Mitigation)                                  |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Aggregate value                                                 |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Operation   | Average                                                         |
| Key         | Time to In Triage                                               |

### **Mean Time to Resolution MTTR**

| Title       | MTTR (Mean Time To Resolution)                                  |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Aggregate value                                                 |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Operation   | Average                                                         |
| Key         | Time to Resolved                                                |

### **Incidents/Severity**

| Title       | Incidents/Severity                                              |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Line Chart or Pie Chart                                         |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Group by    | Severity                                                        |
| Operation   | Count                                                           |
| Key         | Results                                                         |
| Legend      | Include groups without values                                   |

### **Incidents/Environment**

| Title       | Incidents/Environment                                           |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Line Chart or Pie Chart                                         |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Group by    | Environments                                                    |
| Operation   | Count                                                           |
| Key         | Results                                                         |
| Legend      | Include groups without values                                   |

### **Incidents/Service**

| Title       | Incidents/Service                                               |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Line Chart or Pie Chart                                         |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Group by    | Services                                                        |
| Operation   | Count                                                           |
| Key         | Results                                                         |
| Legend      | Include groups without values                                   |

### **Incidents/Functionality**

| Title       | Incidents/Functionality                                         |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Line Chart or Pie Chart                                         |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Group by    | Functionalities                                                 |
| Operation   | Count                                                           |
| Key         | Results                                                         |
| Legend      | Include groups without values                                   |

### **Incidents/Type**

| Title       | Incidents/Functionality                                         |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Line Chart or Pie Chart                                         |
| Collection  | Incidents                                                       |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Group by    | Functionalities                                                 |
| Operation   | Count                                                           |
| Key         | Results                                                         |
| Legend      | Include groups without values                                   |

### **Incident Retrospectives/Causes**

| Title       | Incident Retrospectives/Cause                                   |
| :---------- | :-------------------------------------------------------------- |
| Description | -                                                               |
| Type        | Line Chart or Pie Chart                                         |
| Collection  | Retrospectives                                                  |
| Filter by   | Kind > = > Normal  Kind > = > Normal sub  Kind > = > Backfilled |
| Group by    | Causes                                                          |
| Operation   | Count                                                           |
| Key         | Results                                                         |
| Legend      | Include groups without values                                   |

## Workload Dashboard

### **Hours Worked (Using resolution time)**

| Title       | Hours Worked (Using resolution time)                               |
| :---------- | :----------------------------------------------------------------- |
| Description | -                                                                  |
| Type        | Column Chart                                                       |
| Collection  | Incidents                                                          |
| Filter by   | Kind > is > Normal  Kind > is > Normal sub  Kind > is > Backfilled |
| Group by    | -                                                                  |
| Operation   | Sum                                                                |
| Key         | Hours worked until resolved                                        |

### **Hours Worked by Incident (Using resolution time)**

| Title       | Hours Worked by Incident (Using resolution time)                   |
| :---------- | :----------------------------------------------------------------- |
| Description | -                                                                  |
| Type        | Table                                                              |
| Collection  | Incidents                                                          |
| Filter by   | Kind > is > Normal  Kind > is > Normal sub  Kind > is > Backfilled |

### **Hours Worked by User (Using resolution time)**

| Title       | Hours Worked by User (Using resolution time) |
| :---------- | :------------------------------------------- |
| Description | -                                            |
| Type        | Table                                        |
| Collection  | Users                                        |
| Filter by   | -                                            |

## Alerts Dashboard

### **Total Alerts**

| Title        | Total Alerts |
| :----------- | :----------- |
| Description  | -            |
| Type         | Line Chart   |
| Collection   | Alerts       |
| Series Label | -            |
| Filter by    | -            |
| Group by     | -            |
| Operation    | Count        |
| Key          | Results      |

### **Mean Time to Acknowledge**

| Title        | Mean Time to Acknowledge |
| :----------- | :----------------------- |
| Description  | -                        |
| Type         | Line Chart               |
| Collection   | Alerts                   |
| Series Label | -                        |
| Filter by    | -                        |
| Group by     | -                        |
| Operation    | Average                  |
| Key          | Acknowledge Time         |

### **Mean Time to Resolve**

| Title        | Mean Time to Resolve |
| :----------- | :------------------- |
| Description  | -                    |
| Type         | Line Chart           |
| Collection   | Alerts               |
| Series Label | MTTR                 |
| Filter by    | -                    |
| Group by     | -                    |
| Operation    | Average              |
| Key          | Resolution time      |

### **Mean Time to Acknowledge by Responder**

| Title        | MTTA by Responder |
| :----------- | :---------------- |
| Description  | -                 |
| Type         | Line Chart        |
| Collection   | Alerts            |
| Series Label | -                 |
| Filter by    | -                 |
| Group by     | Responders        |
| Operation    | Average           |
| Key          | Acknowledge time  |

### **Mean Time to Respond by Service**

| Title        | MTTR by Service |
| :----------- | :-------------- |
| Description  | -               |
| Type         | Line Chart      |
| Collection   | Alerts          |
| Series Label | -               |
| Filter by    | -               |
| Group by     | Services        |
| Operation    | Average         |
| Key          | Resolution time |

### **Mean Time Between Failure**

| Title        | Mean Time between Failure |
| :----------- | :------------------------ |
| Description  | -                         |
| Type         | Line Chart                |
| Collection   | Alerts                    |
| Series Label | -                         |
| Filter by    | -                         |
| Group by     | -                         |
| Operation    | Average                   |
| Key          | Time between failure      |

### **Acknowledge Rate**

| Title        | Acknowledge Rate                  |
| :----------- | :-------------------------------- |
| Description  | Percentage of alerts acknowledged |
| Type         | Line Chart                        |
| Collection   | Acknowledge Rate                  |
| Series Label | -                                 |
| Filter by    | -                                 |
| Group by     | -                                 |
| Operation    | Average                           |
| Key          | Acknowledge Rate                  |

### **Alerts by Source**

| Title        | Alerts by Source              |
| :----------- | :---------------------------- |
| Description  |                               |
| Type         | Line Chart/ Pie chart         |
| Collection   | Alerts                        |
| Series Label | -                             |
| Filter by    | -                             |
| Group by     | Source                        |
| Operation    | Count                         |
| Key          | Results                       |
| Legend       | Include groups without values |

### **Alerts by Responder**

| Title        | Alerts by Responder |
| :----------- | :------------------ |
| Description  | -                   |
| Type         | Pie chart           |
| Collection   | Alerts              |
| Series Label | -                   |
| Filter by    | -                   |
| Group by     | Responders          |
| Operation    | Count               |
| Key          | Results             |
| Legend       | -                   |

### **Response Effort**

| Title        | Response Effort                                        |
| :----------- | :----------------------------------------------------- |
| Description  | The sum of time between acknowledgment and resolution. |
| Type         | Line Chart                                             |
| Collection   | Alerts                                                 |
| Series Label | Response Effort                                        |
| Filter by    | Status > = > Resolved                                  |
| Group by     | -                                                      |
| Operation    | Sum                                                    |
| Key          | Resolve Time                                           |
| Legend       | -                                                      |

### **Alerts by Urgency**

| Title        | Alerts by Urgency             |
| :----------- | :---------------------------- |
| Description  | -                             |
| Type         | Line Chart                    |
| Collection   | Alerts                        |
| Series Label | Alerts                        |
| Filter by    | -                             |
| Group by     | Alert Urgency                 |
| Operation    | Count                         |
| Key          | Results                       |
| Legend       | Include groups without values |

### **Alerts by Escalation Policy**

| Title        | Alerts by Escalation Policy |
| :----------- | :-------------------------- |
| Description  | -                           |
| Type         | Pie Chart                   |
| Collection   | Alerts                      |
| Series Label | -                           |
| Filter by    | -                           |
| Group by     | Escalation Policies         |
| Operation    | Count                       |
| Key          | Results                     |
| Legend       | -                           |

### **Alerts by Service**

| Title        | Alerts by Service    |
| :----------- | :------------------- |
| Description  | -                    |
| Type         | Line Chart/Pie Chart |
| Collection   | Alerts               |
| Series Label | -                    |
| Filter by    | -                    |
| Group by     | Services             |
| Operation    | Count                |
| Key          | Results              |
| Legend       | -                    |


Built with [Mintlify](https://mintlify.com).