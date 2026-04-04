# Source: https://docs.aws.amazon.com/braket/latest/developerguide/llms.txt

# Amazon Braket Developer Guide

> Provides a conceptual overview of Amazon Braket, and detailed information about how to design and create quantum tasks, test them on quantum simulators, and then run them on a quantum computer.

- [Quotas](https://docs.aws.amazon.com/braket/latest/developerguide/braket-quotas.html)
- [Document history](https://docs.aws.amazon.com/braket/latest/developerguide/doc-history.html)

## [What is Amazon Braket?](https://docs.aws.amazon.com/braket/latest/developerguide/what-is-braket.html)

- [How it works](https://docs.aws.amazon.com/braket/latest/developerguide/braket-how-it-works.html): Learn about the processing of quantum tasks with Amazon Braket
- [Amazon Braket terms and concepts](https://docs.aws.amazon.com/braket/latest/developerguide/braket-terms.html): The following terms and concepts are used in Braket:
- [Cost tracking and saving](https://docs.aws.amazon.com/braket/latest/developerguide/braket-pricing.html): With Amazon Braket, you have access to quantum computing resources on demand without upfront commitment.
- [API references and repos](https://docs.aws.amazon.com/braket/latest/developerguide/braket-references.html): Amazon Braket provides APIs, SDKs, and a command line interface that you can use to create and manage notebook instances and train and deploy models.
- [Supported regions and devices](https://docs.aws.amazon.com/braket/latest/developerguide/braket-devices.html): In Amazon Braket, a device represents a QPU or simulator that you can call to run quantum tasks.


## [Getting started](https://docs.aws.amazon.com/braket/latest/developerguide/braket-get-started.html)

- [Enable Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-enable-overview.html): You can enable Amazon Braket in your account through the AWS console.
- [Create an Amazon Braket notebook instance](https://docs.aws.amazon.com/braket/latest/developerguide/braket-get-started-create-notebook.html): Amazon Braket provides fully-managed Jupyter notebooks to get you started.
- [(Advanced) Create a Braket notebook using CloudFormation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-cloudformation.html): Learn how to create an Amazon Braket notebook using CloudFormation


## [Build](https://docs.aws.amazon.com/braket/latest/developerguide/braket-build.html)

### [Building your first circuit](https://docs.aws.amazon.com/braket/latest/developerguide/braket-get-started-run-circuit.html)

This page provides a tutorial on constructing and running a basic quantum circuit using the Amazon Braket Python SDK.

- [Building your first quantum algorithms](https://docs.aws.amazon.com/braket/latest/developerguide/braket-explore-algorithm-library.html): The Amazon Braket algorithm library is a catalog of pre-built quantum algorithms written in Python.
- [Constructing circuits in the SDK](https://docs.aws.amazon.com/braket/latest/developerguide/braket-constructing-circuit.html): This section provides examples of defining a circuit, viewing available gates, extending a circuit, and viewing gates that each device supports.
- [Inspecting the circuit](https://docs.aws.amazon.com/braket/latest/developerguide/braket-inspecting-circut.html): Quantum circuits in Amazon Braket have a pseudo-time concept called Moments.
- [List of result types](https://docs.aws.amazon.com/braket/latest/developerguide/braket-result-types.html): Amazon Braket can return different types of results when a circuit is measured using ResultType.
- [Getting Expert advice](https://docs.aws.amazon.com/braket/latest/developerguide/braket-expert-advice.html): Connect with quantum computing experts directly in the Braket management console to get additional guidance around your workloads.

### [(Advanced) Run your circuits with OpenQASM 3.0](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm.html)

This user guide provides information about the subset of OpenQASM 3.0 supported by Braket.

- [What OpenQASM features does Braket support?](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-supported-features.html): The following section lists the OpenQASM 3.0 data types, statements, and pragma instructions supported by Braket.
- [Create and submit an example OpenQASM 3.0 quantum task](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-create-submit-task.html): You can use the Amazon Braket Python SDK, Boto3, or the AWS CLI to submit OpenQASM 3.0 quantum tasks to an Amazon Braket device.
- [Support for OpenQASM on different Braket devices](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-device-support.html): For devices supporting OpenQASM 3.0, the action field supports a new action through the GetDevice response.
- [Simulate noise](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-noise-simulation.html): To simulate noise with OpenQASM3, you use pragma instructions to add noise operators.
- [Qubit rewiring](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-rewire-qubits.html): Amazon Braket supports the physical qubit notation within OpenQASM on Rigetti devices.
- [Verbatim compilation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-verbatim-compilation.html): When you run a quantum circuit on quantum computers from Rigetti, and IonQ, you can direct the compiler to run your circuits exactly as defined.
- [Computing gradients](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-computing-gradients.html): Amazon Braket supports computing gradients on both on demand and local simulators in shots equal 0 exact mode using the adjoint differentiation method.
- [Measuring specific qubits](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm-measure-qubits.html): The local state vector simulator and local density matrix simulator support submitting OpenQASM programs where a subset of the circuit qubits can be measured.
- [(Advanced) Explore Experimental Capabilities](https://docs.aws.amazon.com/braket/latest/developerguide/braket-experimental-capabilities.html): Experimental capabilities provide access to hardware with limited availability and emergent new software features.

### [(Advanced) Pulse control on Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-pulse-control.html)

Pulses are the analog signals that control the qubits in a quantum computer.

- [Working with Hello Pulse](https://docs.aws.amazon.com/braket/latest/developerguide/braket-hello-pulse.html): In this section, you will learn how to characterize and construct a single qubit gate directly using pulse on a Rigetti device.
- [Accessing native gates using pulses](https://docs.aws.amazon.com/braket/latest/developerguide/braket-native-gate-pulse.html): Researchers often need to know exactly how the native gates supported by a particular QPU are implemented as pulses.

### [(Advanced) Analog Hamiltonian Simulation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-analog-hamiltonian-simulation.html)

The Hamiltonian of a system encodes its energy levels and the effects of external forces, which together govern the time evolution of its states.

- [Hello AHS: Run your first Analog Hamiltonian Simulation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-get-started-hello-ahs.html): This section provides information on running your first Analog Hamiltonian Simulation.
- [Submit an analog program using QuEra Aquila](https://docs.aws.amazon.com/braket/latest/developerguide/braket-quera-submitting-analog-program-aquila.html): This page provides comprehensive documentation on the capabilities of the Aquila machine from QuEra.

### [(Advanced) Working with AWS Boto3](https://docs.aws.amazon.com/braket/latest/developerguide/braket-using-boto3.html)

Boto3 is the AWS SDK for Python.

- [Turn on the Amazon Braket Boto3 client](https://docs.aws.amazon.com/braket/latest/developerguide/braket-using-boto3-client.html): To use Boto3 with Amazon Braket, you must import Boto3 and then define a client that you use to connect to the Amazon Braket API.
- [Configure AWS CLI profiles for Boto3 and the Braket SDK](https://docs.aws.amazon.com/braket/latest/developerguide/braket-using-boto3-profiles.html): The Amazon Braket SDK relies upon the default AWS CLI credentials, unless you explicitly specify otherwise.


## [Test](https://docs.aws.amazon.com/braket/latest/developerguide/braket-test.html)

### [Submitting quantum tasks to simulators](https://docs.aws.amazon.com/braket/latest/developerguide/braket-submit-tasks-simulators.html)

Amazon Braket provides access to several simulators that can test your quantum tasks.

- [About embedded simulators](https://docs.aws.amazon.com/braket/latest/developerguide/embedded-simulator.html): Embedded simulators are embedded within the algorithm code in the same container and running the simulation on the hybrid job instance directly.
- [Compare simulators](https://docs.aws.amazon.com/braket/latest/developerguide/choose-a-simulator.html): This section helps you select the Amazon Braket simulator that is best suited for your quantum task by describing some concepts, limitations, and use cases.
- [Example quantum tasks on Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-submit-tasks-to-braket.html): This section guides you through the various stages of running an example quantum task.
- [Testing a quantum task with the local simulator](https://docs.aws.amazon.com/braket/latest/developerguide/braket-send-to-local-simulator.html): You can send quantum tasks directly to a local simulator for rapid prototyping and testing.
- [Local quantum device emulator](https://docs.aws.amazon.com/braket/latest/developerguide/braket-local-emulator.html): Test your quantum programs on a local emulator before running them on quantum hardware.


## [Run](https://docs.aws.amazon.com/braket/latest/developerguide/braket-using.html)

### [Submitting quantum tasks to QPUs](https://docs.aws.amazon.com/braket/latest/developerguide/braket-submit-tasks.html)

Amazon Braket provides access to several devices that can run quantum tasks.

- [Example: Submitting a quantum task to a QPU](https://docs.aws.amazon.com/braket/latest/developerguide/braket-submit-to-qpu.html): Amazon Braket allows you to run a quantum circuit on a QPU device.
- [Inspecting compiled circuits](https://docs.aws.amazon.com/braket/latest/developerguide/braket-compiled-circuits-inspecting.html): When running a circuit on a hardware device, it must be compiled into an acceptable format, like transpiling it to native gates supported by the QPU.
- [Running multiple programs](https://docs.aws.amazon.com/braket/latest/developerguide/braket-batching-tasks.html): Amazon Braket offers two approaches for running multiple quantum programs efficiently, program sets and quantum task batching.

### [When will my quantum task run?](https://docs.aws.amazon.com/braket/latest/developerguide/braket-task-when.html)

When you submit a circuit, Braket sends it to the device you specify.

- [Set up email or SMS notifications](https://docs.aws.amazon.com/braket/latest/developerguide/status-change-notifications-in-email-or-sms.html): Amazon Braket sends events to Amazon EventBridge when the availability of a QPU changes or when the state of your quantum task changes.

### [(Advanced) Working with reservations](https://docs.aws.amazon.com/braket/latest/developerguide/braket-reservations.html)

Reservations give you exclusive access to the quantum device of your choice.

- [How to create a reservation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-create-a-reservation.html): To create a reservation, contact the Braket team by following these steps:
- [Running quantum tasks during a reservation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-run-quantum-task-with-reservation.html): After obtaining a valid reservation ARN from Create a reservation, you can create quantum tasks to run during the reservation.
- [Running hybrid jobs during a reservation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-run-hybrid-jobs-with-reservation.html): Once you have a Python function to run as a hybrid job, run the job in a reservation.
- [What happens at the end of your reservation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-end-of-reservation.html): After your reservation ends, you no longer have dedicated access to the device.
- [Cancel or reschedule an existing reservation](https://docs.aws.amazon.com/braket/latest/developerguide/braket-cancel-reservation.html): You can cancel your reservation no less than 48 hours before the scheduled reservation start time.

### [(Advanced) Error mitigation techniques](https://docs.aws.amazon.com/braket/latest/developerguide/braket-error-mitigation.html)

Learn the techniques for quantum error mitigation with Amazon Braket.

- [Error mitigation techniques on IonQ devices](https://docs.aws.amazon.com/braket/latest/developerguide/error-mitigation-ionq.html): Error mitigation involves running multiple physical circuits and combining their measurements to give an improved result.


## [Amazon Braket Hybrid Jobs](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs.html)

- [Key concepts](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-concepts.html): In addition to the file or files that makes up your complete algorithm script, your hybrid job can have additional inputs and outputs.
- [Prerequisites](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-prerequisites.html): Before you run your first hybrid job, you must ensure that you have sufficient permissions to proceed with this task.

### [Create a Hybrid Job](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-first.html)

This section shows you how to create a Hybrid Job using a Python script.

- [Run your local code as a hybrid job](https://docs.aws.amazon.com/braket/latest/developerguide/braket-hybrid-job-decorator.html): Amazon Braket Hybrid Jobs enable orchestrated hybrid quantum-classical algorithms, combining Amazon EC2 resources with Amazon Braket QPU access.
- [Using the API with Hybrid Jobs](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-api.html): You can access and interact with Amazon Braket Hybrid Jobs directly using the API.
- [Create and debug a hybrid job with local mode](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-local-mode.html): If you are building a new hybrid algorithm, local mode helps you to debug and test your algorithm script.
- [Cancel a Hybrid Job](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-cancel.html): You may need to cancel a hybrid job in a non-terminal state.

### [Customizing your Hybrid Job](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-customize.html)

Learn how to customize your Amazon Braket Hybrid job.

### [Define the environment for your algorithm script](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-script-environment.html)

Amazon Braket supports environments defined by containers for your algorithm script.

### [Bring your own container (BYOC)](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-byoc.html)

Braket Hybrid Jobs supports running hybrid jobs with your own custom Docker container image, or bring your own container.

- [Recipe for bringing your own container](https://docs.aws.amazon.com/braket/latest/developerguide/bring-own-container-recipe.html): This section provides a comprehensive step-by-step guide on how to bring your own container to the Braket Hybrid Jobs feature.
- [Running Braket hybrid jobs in your own container](https://docs.aws.amazon.com/braket/latest/developerguide/running-hybrid-jobs-in-own-container.html): You can use a QPU, an on-demand simulator, or run your code locally on the classical processor available with Braket Hybrid Jobs.
- [Using hyperparameters](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-hyperparameters.html): You can define hyperparameters needed by your algorithm, such as the learning rate or step size, when you create a hybrid job.
- [Configure your hybrid job instance](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-configure-job-instance-for-script.html): This page discusses how to configure the hybrid job instance used to run your algorithm script in Amazon Braket.
- [Using parametric compilation to speed up Hybrid Jobs](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-parametric-compilation.html): Amazon Braket supports parametric compilation on certain QPUs.

### [(Advanced) PennyLane with Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/hybrid.html)

Hybrid algorithms are algorithms that contain both classical and quantum instructions.

- [Using Hybrid Jobs and PennyLane to run a QAOA algorithm](https://docs.aws.amazon.com/braket/latest/developerguide/braket-jobs-run-qaoa-algorithm.html): In this section, you will use what you have learned to write a hybrid program using PennyLane with parametric compilation.
- [Run hybrid workloads with PennyLane embedded simulators](https://docs.aws.amazon.com/braket/latest/developerguide/pennylane-embedded-simulators.html): Lets look at how you can use embedded simulators from PennyLane on Amazon Braket Hybrid Jobs to run hybrid workloads.
- [(Advanced) CUDA-Q with Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-using-cuda-q.html): NVIDIA's CUDA-Q is a software library designed for programming hybrid quantum algorithms that combine CPUs, GPUs, and Quantum processing units (QPUs).


## [Troubleshooting](https://docs.aws.amazon.com/braket/latest/developerguide/braket-troubleshooting.html)

- [Troubleshooting Python 3.12 Upgrade](https://docs.aws.amazon.com/braket/latest/developerguide/braket-troubleshooting-python312.html): Effective January 21, 2026, Amazon Braket upgrades the Python runtime from 3.10 to 3.12 for all Notebook Instances and managed container images.
- [Troubleshooting OpenQASM](https://docs.aws.amazon.com/braket/latest/developerguide/braket-troubleshooting-openqasm.html): This section provides troubleshooting pointers that might be useful when encountering errors using OpenQASM 3.0.


## [Security](https://docs.aws.amazon.com/braket/latest/developerguide/security.html)

### [Managing access to Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-manage-access.html)

This chapter describes the permissions that are required to run Amazon Braket, or to restrict the access of specific users and roles.

- [AWS managed policies](https://docs.aws.amazon.com/braket/latest/developerguide/security-iam-aws-managed-policies.html): Learn about AWS managed policies for Amazon Braket, and recent changes to those policies.
- [Restrict user access to certain devices](https://docs.aws.amazon.com/braket/latest/developerguide/restrict-access.html): To restrict user access for certain Braket devices, you can add a deny permissions policy to a specific IAM role.
- [Restrict user access to certain notebook instances](https://docs.aws.amazon.com/braket/latest/developerguide/restrict-access-notebook-instances.html): To restrict access for certain users to specific Braket notebook instances, you can add a deny permissions policy to a specific role, user, or group.
- [Restrict user access to certain S3 buckets](https://docs.aws.amazon.com/braket/latest/developerguide/restrict-access-s3-buckets.html): To restrict access for certain users to specific Amazon S3 buckets, you can add a deny policy to a specific role, user, or group.
- [Service-linked role](https://docs.aws.amazon.com/braket/latest/developerguide/braket-slr.html): Learn about the service-linked role for Amazon Braket.
- [Compliance validation](https://docs.aws.amazon.com/braket/latest/developerguide/compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Infrastructure Security](https://docs.aws.amazon.com/braket/latest/developerguide/infrastructure-security.html): Learn about how Amazon Braket isolates service traffic.
- [Third Party Security](https://docs.aws.amazon.com/braket/latest/developerguide/third-party-security.html): Learn about the security of Amazon Braket third party hardware providers.
- [VPC endpoints (PrivateLink)](https://docs.aws.amazon.com/braket/latest/developerguide/braket-privatelink.html): You can establish a private connection between your VPC and Amazon Braket by creating an interface VPC endpoint.


## [Logging and monitoring](https://docs.aws.amazon.com/braket/latest/developerguide/braket-monitor-tasks.html)

- [Tracking quantum tasks from the Amazon Braket SDK](https://docs.aws.amazon.com/braket/latest/developerguide/braket-monitor-tasks-sdk.html): The command device.run defines a quantum task with a unique quantum task ID.
- [Monitoring quantum tasks through the Amazon Braket console](https://docs.aws.amazon.com/braket/latest/developerguide/braket-monitor-console.html): Amazon Braket offers a convenient way of monitoring the quantum task through the Amazon Braket console.

### [Tagging resources](https://docs.aws.amazon.com/braket/latest/developerguide/braket-tagging-resources.html)

A tag is a custom attribute label that you assign or that AWS assigns to an AWS resource.

- [Tagging restrictions](https://docs.aws.amazon.com/braket/latest/developerguide/tag-restrictions.html): The following basic restrictions apply to tags on Amazon Braket resources:
- [Managing tags in Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/tag-managing.html): You can view, add, modify, list, and delete tags through the Amazon Braket console, the Amazon Braket API, or the AWS CLI.
- [Example of AWS CLI tagging in Amazon Braket](https://docs.aws.amazon.com/braket/latest/developerguide/braket-tags-example.html): When you are working with the AWS CLI, the following code is an example command that shows how to create a tag that applies to a quantum task you create.
- [Monitoring your quantum tasks with EventBridge](https://docs.aws.amazon.com/braket/latest/developerguide/braket-monitor-eventbridge.html): Learn about monitoring Amazon Braket with Amazon EventBridge.
- [Monitoring your metrics with CloudWatch](https://docs.aws.amazon.com/braket/latest/developerguide/braket-monitor-metrics.html): Learn about Amazon Braket metrics and logs in Amazon CloudWatch.
- [Logging your quantum tasks with CloudTrail](https://docs.aws.amazon.com/braket/latest/developerguide/braket-ctlogs.html): Learn about logging Amazon Braket API activity using CloudTrail.
- [(Advanced) Logging](https://docs.aws.amazon.com/braket/latest/developerguide/braket-monitor-logging.html): These advanced logging techniques allow you to see the background polling and create a record for later debugging.
