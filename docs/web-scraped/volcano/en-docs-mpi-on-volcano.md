# Source: https://volcano.sh/en/docs/mpi_on_volcano/

Title: MPI on Volcano | Volcano

URL Source: https://volcano.sh/en/docs/mpi_on_volcano/

Published Time: 2021-04-07T00:00:00+00:00

Markdown Content:
Last updated on Jul 31, 2021

### HPC introduction[](https://volcano.sh/en/docs/mpi_on_volcano/#hpc-introduction)

High Performance Computing (HPC) refers to the use of aggregated Computing power to handle data-intensive Computing tasks that cannot be performed by standard workstations.

HPC = PBS + Maui + OpenMPI[1]

*   PBS：Resource manager, which is responsible for managing resources for all nodes in the cluster
*   Maui：Third-party task scheduler, support resource reservation, support various complex priority policies, support preemption, etc.
*   OpenMPI：The upper communication environment, taking into account the functions of communication library, compilation and distributed start task.

### openMPI introduction[](https://volcano.sh/en/docs/mpi_on_volcano/#openmpi-introduction)

The OpenMPI project is an open source messaging interface implementation developed and maintained by a coalition of academic, research, and industry partners. Through it we can carry on the parallelization program design.

### How is opensMPI implemented[](https://volcano.sh/en/docs/mpi_on_volcano/#how-is-opensmpi-implemented)

Here is a simple 4-thread MPI program example.

![Image 1: image](https://volcano.sh/img/mpi1.png)

#### The working principle of MPI[](https://volcano.sh/en/docs/mpi_on_volcano/#the-working-principle-of-mpi)

### MPI on Volcano[](https://volcano.sh/en/docs/mpi_on_volcano/#mpi-on-volcano)

Create `mpi-example.yaml`.

```
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: lm-mpi-job
spec:
  minAvailable: 3
  schedulerName: volcano
  plugins:
    ssh: []
    svc: []
  tasks:
    - replicas: 1
      name: mpimaster
      policies:
        - event: TaskCompleted
          action: CompleteJob
      template:
        spec:
          containers:
            - command:
                - /bin/sh
                - -c
                - |
                  MPI_HOST=`cat /etc/volcano/mpiworker.host | tr "\n" ","`;
                  mkdir -p /var/run/sshd; /usr/sbin/sshd;
                  mpiexec --allow-run-as-root --host ${MPI_HOST} -np 2 mpi_hello_world > /home/re;
              image: volcanosh/example-mpi:0.0.1
              name: mpimaster
              ports:
                - containerPort: 22
                  name: mpijob-port
              workingDir: /home
          restartPolicy: OnFailure
    - replicas: 2
      name: mpiworker
      template:
        spec:
          containers:
            - command:
                - /bin/sh
                - -c
                - |
                  mkdir -p /var/run/sshd; /usr/sbin/sshd -D;
              image: volcanosh/example-mpi:0.0.1
              name: mpiworker
              ports:
                - containerPort: 22
                  name: mpijob-port
              workingDir: /home
          restartPolicy: OnFailure
---
```

Delopy `mpi-example.yaml`.

```
kubectl apply -f mpi-example.yaml
```

View job performance under the cluster.

```
kubectl get pod
```
