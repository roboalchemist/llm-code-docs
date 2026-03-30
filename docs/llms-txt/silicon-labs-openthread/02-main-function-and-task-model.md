# Source: https://docs.silabs.com/openthread/3.0.0/openthread-with-free-rtos/02-main-function-and-task-model.md

# Main Function and Task Model

The FreeRTOS component is designed to be used along with the standard Silicon Labs main.c template. The standard main function works for both bare metal and kernel-based projects and takes care of all the required system initializations and task creation.

For OpenThread running on FreeRTOS, a single task is created that runs both the OpenThread stack and the application logic. It is not safe to call the OpenThread API from other tasks.

In a bare metal OpenThread application, application logic is placed in the `app_process_action()` callback. Instead, when running on FreeRTOS, application logic is placed in the `sl_ot_rtos_application_tick()` callback.
