# Source: https://fastapi.tiangolo.com/reference/background/

# Background Tasks - `BackgroundTasks`[&para;](#background-tasks-backgroundtasks)

You can declare a parameter in a *path operation function* or dependency function with the type `BackgroundTasks`, and then you can use it to schedule the execution of background tasks after the response is sent.

You can import it directly from `fastapi`:

`from fastapi import BackgroundTasks
`

## 
``            fastapi.BackgroundTasks

[&para;](#fastapi.BackgroundTasks)

`BackgroundTasks(tasks=None)
`

              Bases: `BackgroundTasks`

A collection of background tasks that will be called after a response has been
sent to the client.

Read more about it in the
[FastAPI docs for Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).

#### Example[&para;](#fastapi.BackgroundTasks--example)

`from fastapi import BackgroundTasks, FastAPI

app = FastAPI()

def write_notification(email: str, message=""):
    with open("log.txt", mode="w") as email_file:
        content = f"notification for {email}: {message}"
        email_file.write(content)

@app.post("/send-notification/{email}")
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message="some notification")
    return {"message": "Notification sent in the background"}
`

                    Source code in `starlette/background.py`

27
28

`def __init__(self, tasks: Sequence[BackgroundTask] | None = None):
    self.tasks = list(tasks) if tasks else []
`

### 
``            func

      `instance-attribute`

[&para;](#fastapi.BackgroundTasks.func)

`func = func
`

### 
``            args

      `instance-attribute`

[&para;](#fastapi.BackgroundTasks.args)

`args = args
`

### 
``            kwargs

      `instance-attribute`

[&para;](#fastapi.BackgroundTasks.kwargs)

`kwargs = kwargs
`

### 
``            is_async

      `instance-attribute`

[&para;](#fastapi.BackgroundTasks.is_async)

`is_async = is_async_callable(func)
`

### 
``            tasks

      `instance-attribute`

[&para;](#fastapi.BackgroundTasks.tasks)

`tasks = list(tasks) if tasks else []
`

### 
``            add_task

[&para;](#fastapi.BackgroundTasks.add_task)

`add_task(func, *args, **kwargs)
`

        Add a function to be called in the background after the response is sent.

Read more about it in the
[FastAPI docs for Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).

          PARAMETER
          DESCRIPTION

                `func`

The function to call after the response is sent.

It can be a regular `def` function or an `async def` function.

                    **TYPE:**
                      `Callable[P, Any]`

              Source code in `fastapi/background.py`

39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60

`def add_task(
    self,
    func: Annotated[
        Callable[P, Any],
        Doc(
            """
            The function to call after the response is sent.

            It can be a regular `def` function or an `async def` function.
            """
        ),
    ],
    *args: P.args,
    **kwargs: P.kwargs,
) -> None:
    """
    Add a function to be called in the background after the response is sent.

    Read more about it in the
    [FastAPI docs for Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).
    """
    return super().add_task(func, *args, **kwargs)
`