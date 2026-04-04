# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md.txt

# tasks.TaskContext interface

Metadata about a call to a Task Queue function.

**Signature:**  

    export interface TaskContext 

## Properties

|                                                                     Property                                                                      |           Type           |                                                                                                                                                                Description                                                                                                                                                                 |
|---------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [auth](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextauth)                         | AuthData                 | The result of decoding and verifying an ODIC token.                                                                                                                                                                                                                                                                                        |
| [executionCount](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextexecutioncount)     | number                   | The total number of times that the task has received a response from the handler. Since Cloud Tasks deletes the task once a successful response has been received, all previous handler responses were failures. This number does not include failures due to 5XX error codes. Populated via the `X-CloudTasks-TaskExecutionCount` header. |
| [headers](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextheaders)                   | Record\<string, string\> | Raw request headers.                                                                                                                                                                                                                                                                                                                       |
| [id](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextid)                             | string                   | The "short" name of the task, or, if no name was specified at creation, a unique system-generated id. This is the "my-task-id" value in the complete task name, such as "task_name = projects/my-project-id/locations/my-location/queues/my-queue-id/tasks/my-task-id." Populated via the `X-CloudTasks-TaskName` header.                  |
| [previousResponse](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextpreviousresponse) | number                   | The HTTP response code from the previous retry. Populated via the `X-CloudTasks-TaskPreviousResponse` header                                                                                                                                                                                                                               |
| [queueName](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextqueuename)               | string                   | The name of the queue. Populated via the `X-CloudTasks-QueueName` header.                                                                                                                                                                                                                                                                  |
| [retryCount](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextretrycount)             | number                   | The number of times this task has been retried. For the first attempt, this value is 0. This number includes attempts where the task failed due to 5XX error codes and never reached the execution phase. Populated via the `X-CloudTasks-TaskRetryCount` header.                                                                          |
| [retryReason](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextretryreason)           | string                   | The reason for retrying the task. Populated via the `X-CloudTasks-TaskRetryReason` header.                                                                                                                                                                                                                                                 |
| [scheduledTime](https://firebase.google.com/docs/reference/functions/firebase-functions.tasks.taskcontext.md#taskstaskcontextscheduledtime)       | string                   | The schedule time of the task, as an RFC 3339 string in UTC time zone. Populated via the `X-CloudTasks-TaskETA` header, which uses seconds since January 1 1970.                                                                                                                                                                           |

## tasks.TaskContext.auth

The result of decoding and verifying an ODIC token.

**Signature:**  

    auth?: AuthData;

## tasks.TaskContext.executionCount

The total number of times that the task has received a response from the handler. Since Cloud Tasks deletes the task once a successful response has been received, all previous handler responses were failures. This number does not include failures due to 5XX error codes. Populated via the `X-CloudTasks-TaskExecutionCount` header.

**Signature:**  

    executionCount: number;

## tasks.TaskContext.headers

Raw request headers.

**Signature:**  

    headers?: Record<string, string>;

## tasks.TaskContext.id

The "short" name of the task, or, if no name was specified at creation, a unique system-generated id. This is the "my-task-id" value in the complete task name, such as "task_name = projects/my-project-id/locations/my-location/queues/my-queue-id/tasks/my-task-id." Populated via the `X-CloudTasks-TaskName` header.

**Signature:**  

    id: string;

## tasks.TaskContext.previousResponse

The HTTP response code from the previous retry. Populated via the `X-CloudTasks-TaskPreviousResponse` header

**Signature:**  

    previousResponse?: number;

## tasks.TaskContext.queueName

The name of the queue. Populated via the `X-CloudTasks-QueueName` header.

**Signature:**  

    queueName: string;

## tasks.TaskContext.retryCount

The number of times this task has been retried. For the first attempt, this value is 0. This number includes attempts where the task failed due to 5XX error codes and never reached the execution phase. Populated via the `X-CloudTasks-TaskRetryCount` header.

**Signature:**  

    retryCount: number;

## tasks.TaskContext.retryReason

The reason for retrying the task. Populated via the `X-CloudTasks-TaskRetryReason` header.

**Signature:**  

    retryReason?: string;

## tasks.TaskContext.scheduledTime

The schedule time of the task, as an RFC 3339 string in UTC time zone. Populated via the `X-CloudTasks-TaskETA` header, which uses seconds since January 1 1970.

**Signature:**  

    scheduledTime: string;