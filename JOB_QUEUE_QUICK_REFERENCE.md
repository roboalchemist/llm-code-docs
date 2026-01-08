# Job Queue and Task Queue Quick Reference Guide

Fast lookup guide for choosing a job queue system by language and use case.

---

## Quick Selection by Language

### Python
```
🏆 Production Default: Celery (distributed, broker-agnostic) or RQ (simple, Redis)
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **Celery** | RabbitMQ/Redis | Large distributed systems; scheduling | Medium |
| 2 | **RQ** | Redis | Simple background jobs; small teams | Low |
| 3 | **Dramatiq** | Redis/RabbitMQ | Reliable workers; lighter Celery | Low |
| 4 | **Django Q** | Redis/RabbitMQ/DB | Django projects; cron jobs | Low |
| 5 | **Huey** | Redis | Lightweight; async tasks | Low |

**Quick Start Code Pattern:**
```python
# Celery
from celery import Celery
app = Celery('tasks', broker='redis://localhost')
@app.task
def add(x, y):
    return x + y

# RQ
from rq import Queue
q = Queue(connection=redis.from_url('redis://'))
job = q.enqueue(function, args)
```

---

### JavaScript / Node.js
```
🏆 Production Default: BullMQ (feature-rich, production-grade)
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **BullMQ** | Redis | Production systems; advanced features | Low |
| 2 | **Agenda** | MongoDB | Recurring jobs; persistence | Low |
| 3 | **Bull** | Redis | Legacy projects; predecessor to BullMQ | Low |
| 4 | **Kue** | Redis | Job management UI; older projects | Low |

**Quick Start Code Pattern:**
```javascript
// BullMQ
import { Queue, Worker } from 'bullmq';
const myQueue = new Queue('myqueue', { connection });
await myQueue.add('jobName', { data }, { delay: 5000 });

// Agenda
const agenda = new Agenda({ db: { address: 'mongodb://localhost' } });
agenda.define('email', async (job) => { /* ... */ });
await agenda.start();
```

---

### Ruby
```
🏆 Production Default: Sidekiq (fast, standard in Rails ecosystem)
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **Sidekiq** | Redis | Rails projects; high volume | Low |
| 2 | **Resque** | Redis | Simpler alternative; older projects | Low |
| 3 | **Delayed Job** | Database | No external dependencies | Low |
| 4 | **Good Job** | PostgreSQL | Rails 6+; async jobs | Low |
| 5 | **Que** | PostgreSQL | High-performance pure Ruby | Low |

**Quick Start Code Pattern:**
```ruby
# Sidekiq with Rails
class MyWorker
  include Sidekiq::Worker
  def perform(args)
    # Job logic
  end
end
MyWorker.perform_async(args)

# Delayed Job
MyClass.delay.do_something(arg)
```

---

### Java
```
🏆 Production Default: Spring Batch (enterprise standard) + Quartz (scheduling)
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **Spring Batch** | Database | Enterprise; large batch jobs | High |
| 2 | **Quartz** | Database | Job scheduling; cron-like | Medium |
| 3 | **Apache Camel** | JMS/AMQP | Integration; message routing | High |
| 4 | **Flowable** | Database | Complex workflows; BPMN | High |
| 5 | **Temporal** | Custom | Durable workflows; microservices | Medium |

**Quick Start Code Pattern:**
```java
// Spring Batch
@Configuration
@EnableBatchProcessing
public class BatchConfiguration { /* ... */ }

// Quartz
JobDetail job = JobBuilder.newJob(MyJob.class).build();
Trigger trigger = TriggerBuilder.newTrigger()
    .withSchedule(CronScheduleBuilder.cronSchedule("0 0 * * * ?"))
    .build();
scheduler.scheduleJob(job, trigger);
```

---

### Go
```
🏆 Production Default: Asynq (simple, Redis) or River (PostgreSQL, modern)
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **Asynq** | Redis | Simple distributed tasks; priorities | Low |
| 2 | **River** | PostgreSQL | Modern; transaction-safe; multiple queues | Low |
| 3 | **Machinery** | Redis/RabbitMQ | Broker-agnostic; Celery-like | Low |
| 4 | **jobqueue** | MySQL/In-Memory | Custom concurrency control | Medium |
| 5 | **NATS JetStream** | NATS | Lightweight; low-latency | Medium |

**Quick Start Code Pattern:**
```go
// Asynq
c := asynq.NewClient(asynq.RedisClientOpt{Addr: "localhost:6379"})
task := asynq.NewTask("send_email", payload)
info, err := c.Enqueue(task)

// River
ctx := context.Background()
client, err := river.NewClient(riverdriver.New(dbPool), &river.Config{...})
_, err = client.Insert(ctx, &EmailJob{...}, nil)
```

---

### Rust
```
🏆 Production Default: brokkr (Redis) or custom Tokio-based systems
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **brokkr** | Redis | Distributed tasks; simple integration | Low |
| 2 | **job_queue** | MySQL/PostgreSQL | Database-backed; async | Medium |
| 3 | **Aide-De-Camp** | Custom | Complex type systems | High |
| 4 | **redis-rs** | Redis | Custom queue implementations | Medium |
| 5 | **lapin** | RabbitMQ | AMQP-based; low-level control | High |

**Quick Start Code Pattern:**
```rust
// brokkr (conceptual - check docs for actual API)
use brokkr::Queue;
let queue = Queue::new("redis://localhost");
queue.enqueue(job).await?;

// Custom Tokio channels
let (tx, rx) = tokio::sync::mpsc::channel(100);
tokio::spawn(async move { /* process from rx */ });
```

---

### PHP
```
🏆 Production Default: Laravel Queue (with Horizon) or Symfony Messenger
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **Laravel Queue** | Redis/Database/SQS | Laravel projects; excellent dashboard (Horizon) | Low |
| 2 | **Symfony Messenger** | AMQP/Doctrine/Redis | Symfony projects; flexible transports | Medium |
| 3 | **Enqueue** | RabbitMQ/Redis/SQS | Framework-agnostic; multiple backends | Medium |
| 4 | **Pheanstalk** | Beanstalk | Beanstalk queuing; lightweight | Low |
| 5 | **Bernard** | Redis/AMQP | Multi-backend flexibility | Medium |

**Quick Start Code Pattern:**
```php
// Laravel Queue
Queue::push(new ProcessPodcast($podcast));
// With Horizon dashboard
// php artisan horizon

// Symfony Messenger
$messenger->dispatch(new MyMessage());
```

---

### C# / .NET
```
🏆 Production Default: Hangfire (versatile, simple) or NServiceBus (enterprise)
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **Hangfire** | SQL Server/Redis | Simple setup; great dashboard | Low |
| 2 | **NServiceBus** | RabbitMQ/MSMQ | Enterprise messaging; sagas | High |
| 3 | **MassTransit** | RabbitMQ/Other | Distributed systems; flexible | Medium |
| 4 | **Rebus** | RabbitMQ/MSMQ | Lightweight service bus | Medium |

**Quick Start Code Pattern:**
```csharp
// Hangfire
BackgroundJob.Enqueue(() => Console.WriteLine("Background job"));
RecurringJob.AddOrUpdate(() => Console.WriteLine("Recurring"), Cron.Daily);

// NServiceBus
var endpoint = Endpoint.Create(endpointConfiguration);
await endpoint.Send(new MyMessage());
```

---

### Elixir
```
🏆 Production Default: Oban (PostgreSQL, modern, reliable)
```
| Priority | System | Backend | Best For | Learning Curve |
|----------|--------|---------|----------|-----------------|
| 1 | **Oban** | PostgreSQL | Modern Elixir projects; durable; scheduled | Medium |
| 2 | **Exq** | Redis | Sidekiq-compatible; high throughput | Medium |
| 3 | **Verk** | Redis | Redis-based; reliable | Medium |
| 4 | **Broadway** | Kafka/SQS/External | Data pipelines; parallel processing | High |
| 5 | **Rihanna** | PostgreSQL | Advisory locks; lightweight | Medium |

**Quick Start Code Pattern:**
```elixir
# Oban
defmodule MyApp.Workers.MyWorker do
  use Oban.Worker, queue: :default
  @impl Oban.Worker
  def perform(%Job{args: args}) do
    :ok
  end
end

Oban.insert(MyApp.Workers.MyWorker.new(%{"key" => "value"}))
```

---

## Multi-Language Solutions

### For Polyglot Teams

| System | Languages | Complexity | Setup |
|--------|-----------|-----------|-------|
| **Faktory** | Ruby, Go, Elixir, more | Low | Standalone server; language clients |
| **Temporal** | Java, Go, Python, TypeScript, Ruby | Medium | API-based; multi-language SDKs |
| **Kafka** | Any (protocol-based) | High | Distributed; excellent for scale |
| **RabbitMQ** | Any (AMQP/protocols) | Medium | Message broker; mature |
| **Gearman** | Java, PHP, Python, Ruby, C++, Go | Medium | Distributed; protocol-based |

---

## Quick Decision Tree

```
START
  ├─ How much scale do you need?
  │  ├─ Small (< 1k jobs/min) → Use simple: RQ, Huey, Good Job, queue_classic
  │  ├─ Medium (1k-100k jobs/min) → Use production: Celery, Sidekiq, BullMQ, Oban
  │  └─ Large (> 100k jobs/min) → Use enterprise: Kafka, RabbitMQ, Temporal
  │
  ├─ Do you need scheduling (cron jobs)?
  │  ├─ Yes → Celery, Django Q, Sidekiq, Hangfire, Oban, Agenda, Quartz
  │  └─ No → Any system works
  │
  ├─ Is persistence critical (durability)?
  │  ├─ Yes → Spring Batch, Oban, Flowable, Temporal, Good Job, Delayed Job
  │  └─ No → RQ, BullMQ, Huey, Sidekiq (with proper Redis persistence)
  │
  ├─ Do you need multi-language support?
  │  ├─ Yes → Faktory, Temporal, Kafka, RabbitMQ, Gearman, Beanstalk
  │  └─ No → Use language-specific solution
  │
  ├─ Complex workflows with state management?
  │  ├─ Yes → Temporal, Activiti, Flowable, Airflow
  │  └─ No → Simple task queue
  │
  └─ How much ops overhead can you handle?
     ├─ Minimal → Google Cloud Tasks, AWS SQS, Hangfire, Laravel Queue
     ├─ Moderate → Celery, RQ, Sidekiq, BullMQ, Oban
     └─ High → Kafka, RabbitMQ, Kubernetes-based systems
```

---

## Backend Comparison

### Redis
- **Pros**: Fast, simple, widely available
- **Cons**: Ephemeral (risk of job loss), single-node bottleneck
- **Best For**: Simple tasks, small teams, high speed requirements
- **Default Use**: RQ, BullMQ, Sidekiq, Celery, Asynq, Huey

### PostgreSQL / Database
- **Pros**: Durable, ACID transactions, backups, existing infrastructure
- **Cons**: Slower than Redis, polling overhead, schema management
- **Best For**: Production reliability, complex systems, multi-queue scenarios
- **Default Use**: Oban, River, Good Job, queue_classic, Spring Batch, Temporal (often)

### RabbitMQ
- **Pros**: Reliable, pub/sub patterns, clustering, durable, enterprise-grade
- **Cons**: Complex, operational overhead, slower than Redis
- **Best For**: Complex routing, multi-team coordination, enterprise needs
- **Default Use**: Celery, Dramatiq, Symfony Messenger, Enqueue, NServiceBus

### Kafka / Event Streaming
- **Pros**: Massive scale, durable, replay-able, streaming capabilities
- **Cons**: Overkill for simple tasks, operational complexity
- **Best For**: Big data, event sourcing, microservices, analytics pipelines
- **Default Use**: Kafka Streams, Kafka itself, Broadway

### Cloud Services (SQS, Cloud Tasks, Service Bus)
- **Pros**: Fully managed, auto-scaling, no ops burden
- **Cons**: Limited customization, potential vendor lock-in, cost surprises
- **Best For**: Serverless, small startups, minimal ops teams
- **Default Use**: Google Cloud Tasks, AWS SQS, Azure Service Bus

---

## Common Patterns

### Pattern: "Fire and Forget"
Task doesn't need response. Simple background processing.
```
→ RQ, Huey, BullMQ, Sidekiq, queue_classic, Asynq
```

### Pattern: "Scheduled / Recurring"
Cron-like jobs at specific times.
```
→ Celery (beat), Django Q, Sidekiq (schedule), Oban, Quartz, Hangfire
```

### Pattern: "Reliable Delivery"
Job MUST execute at least once; durability critical.
```
→ Celery (RabbitMQ), Oban, Good Job, Spring Batch, Temporal, Flowable, NServiceBus
```

### Pattern: "Exactly-Once"
Job must execute exactly once (no duplicates).
```
→ Temporal, SQS (FIFO), Advanced message deduplication (custom implementation)
```

### Pattern: "Complex Workflows"
Multiple steps, conditional logic, state management.
```
→ Temporal, Activiti, Flowable, Airflow, Prefect, Dagster
```

### Pattern: "Real-Time Streaming"
Continuous data processing; event streaming.
```
→ Kafka, Pulsar, Kafka Streams, RabbitMQ (fanout), Broadway, NATS JetStream
```

### Pattern: "Microservices"
Inter-service communication; loosely coupled.
```
→ RabbitMQ, Kafka, Temporal, NServiceBus, MassTransit, NATS
```

---

## Migration Paths

```
Your Current → Next Step → Production Ready

Home-grown queue → RQ/Huey (Python) or BullMQ (Node.js)
                ↓
Simple queue → Celery (Python) or Sidekiq (Ruby)
           ↓
Scaling issues → Add Kafka/RabbitMQ, or switch to cloud services
           ↓
Complex workflows → Temporal or Airflow
```

---

## Performance Benchmarks (Rough)

| System | Throughput (jobs/sec) | Latency | Persistence |
|--------|----------------------|---------|-------------|
| **BullMQ** | 10,000+ | < 10ms | Optional |
| **Sidekiq** | 50,000+ | < 5ms | Redis |
| **Celery + Redis** | 10,000+ | 10-50ms | Broker-based |
| **RQ** | 1,000-5,000 | 20-100ms | Redis |
| **Oban** | 10,000+ | 50-100ms | PostgreSQL |
| **Kafka** | 1,000,000+ | 1-10ms | Broker |
| **RabbitMQ** | 50,000+ | 10-50ms | Broker |

*Benchmarks are approximate and vary by configuration, hardware, and workload.*

---

## Monitoring and Observability

| System | Built-in Dashboard | Logging | Metrics |
|--------|-------------------|---------|---------|
| Hangfire | ✅ Excellent | ✅ Yes | ✅ Yes |
| Horizon (Laravel) | ✅ Excellent | ✅ Yes | ✅ Yes |
| Sidekiq | ⚠️ Web UI | ✅ Yes | ⚠️ Limited |
| BullMQ | ⚠️ Community tools | ✅ Yes | ✅ Yes |
| Celery Flower | ⚠️ Community (Flower) | ✅ Yes | ✅ Yes |
| Temporal UI | ✅ Excellent | ✅ Yes | ✅ Yes |
| Kafka UI | ⚠️ Community tools | ✅ Yes | ✅ Yes |
| RabbitMQ | ✅ Management UI | ✅ Yes | ✅ Yes |

---

## Cost Considerations

| System | License | Hosting | Typical Cost |
|--------|---------|---------|--------------|
| Redis-based queues | Free (OSS) | Self-hosted or managed | Low to Medium |
| Celery/RQ | Free | Self-hosted | Low |
| Kafka | Free | Self-hosted or managed (Confluent) | Medium to High |
| RabbitMQ | Free | Self-hosted or managed | Medium |
| Cloud Services (SQS, Tasks) | Proprietary | Cloud | Medium (consumption-based) |
| Temporal | Free (OSS) or Temporal Cloud | Self-hosted or managed | Low to Medium |
| Hangfire | Free or Pro | Self-hosted | Low to Medium |

---

Last Updated: 2026-01-01
