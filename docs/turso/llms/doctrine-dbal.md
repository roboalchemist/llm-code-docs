# Source: https://docs.turso.tech/sdk/php/orm/doctrine-dbal.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Turso + Doctrine DBAL

> Set up Turso in your PHP + Doctrine DBAL project in minutes

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/doctrine-dbal-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=42ebe47228681e458a0f7570d61f74e5" alt="Doctrine DBAL" data-og-width="2266" width="2266" data-og-height="1190" height="1190" data-path="images/guides/doctrine-dbal-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/doctrine-dbal-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=864fd83beb681026576e3d9ee74602f3 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/doctrine-dbal-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=0351299f895b54f2ef62d4554c6f6582 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/doctrine-dbal-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=6162516596ddc4d5ece04c2bf8376b5d 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/doctrine-dbal-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=dfa7de6b4abf5c588bbcc6bd14971564 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/doctrine-dbal-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=2d3c7e020e892cefbf0940985c52b372 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/doctrine-dbal-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=7f8683ab28cc780491e0d2d29a91411b 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have an PHP Application with Doctrine DBAL

<Snippet file="install-libsql-extension-php.mdx" />

<Steps>
  <Step title="Configure database credentials">
    Get the database URL:

    ```bash  theme={null}
    turso db show --url <database-name>
    ```

    Get the database authentication token:

    ```bash  theme={null}
    turso db tokens create <database-name>
    ```

    Assign credentials to the environment variables inside `.env`.

    ```bash  theme={null}
    TURSO_DATABASE_URL=
    TURSO_AUTH_TOKEN=
    ```

    <Info>Save this later when you need to connect to **Remote** and **Embedded Replica**</Info>
  </Step>

  <Step title="Create PHP Project">
    Create new directory:

    ```bash  theme={null}
    mkdir your-awesome-php-project
    cd your-awesome-php-project
    ```
  </Step>

  <Step title="Install Turso Doctrine DBAL">
    ```bash  theme={null}
    composer require tursodatabase/turso-doctrine-dbal
    ```
  </Step>

  <Step title="Configure database connection">
    Setup the environment variable in your Laravel application, choose what the type connection you need.

    <CodeGroup>
      ```php In-Memory Only theme={null}
      $params = [
          "url"               => ":memory:",
          'driverClass'       => \Turso\Doctrine\DBAL\Driver::class,
      ];
      ```

      ```php Local Only theme={null}
      $params = [
          "url"               => "database.db",
          'driverClass'       => \Turso\Doctrine\DBAL\Driver::class,
      ];
      ```

      ```php Remote Only theme={null}
      $params = [
          "auth_token"        => getenv('TURSO_AUTH_TOKEN'),
          "sync_url"          => getenv('TURSO_DATABASE_URL'),
          'driverClass'       => \Turso\Doctrine\DBAL\Driver::class,
      ];
      ```

      ```php Embedded Replica theme={null}
      $params = [
          "url"               => "database.db",
          "auth_token"        => getenv('TURSO_AUTH_TOKEN'),
          "sync_url"          => getenv('TURSO_DATABASE_URL'),
          'driverClass'       => \Turso\Doctrine\DBAL\Driver::class,
      ];
      ```
    </CodeGroup>

    **Other environment variables (Embedded Replica Only)**

    <Expandable title="Other environment variables (Embedded Replica Only)">
      <ResponseField name="sync_interval" type="integer">
        Integer value representing synchronization interval in seconds (optional, default: `5`).
      </ResponseField>

      <ResponseField name="read_your_writes" type="boolean">
        Boolean value indicating whether to read your writes (optional, default: `true`).
      </ResponseField>

      <ResponseField name="encryption_key" type="string">
        String value for encryption purposes (optional, default: empty).
      </ResponseField>
    </Expandable>
  </Step>

  <Step title="Project Structure Example">
    ```bash  theme={null}
    src/
    ├── helpers.php
    └── Todo.php
    vendor/
    composer.json
    composer.lock
    todo            # todo executable
    ```

    Here you simple php todo cli + Doctrine BDAL

    <CodeGroup>
      ```php todo theme={null}
      #!/usr/bin/env php
      <?php

      use Turso\Todo\CLI\Todo;

      require_once __DIR__ . '/vendor/autoload.php';

      $header = 'TODO CLI + TURSO';

      echo $header . PHP_EOL;
      function main()
      {
          echo str_repeat('-', WIDTH - 18) . "  Todo CLI - " . VERSION . PHP_EOL;

          while (true) {
              echo "[L] List | [A] Add | [E] Edit | [D] Delete | [X] Exit" . PHP_EOL;
              echo "command: ";

              $choice = trim(fgets(STDIN));

              $app = new Todo();

              switch (strtolower($choice)) {
                  case 'l':
                      $app->listTodos();
                      break;
                  case 'a':
                      $app->addTodo();
                      clearScreen();
                      break;
                  case 'e':
                      $app->editTodo();
                      clearScreen();
                      break;
                  case 'd':
                      $app->deleteTodo();
                      clearScreen();
                      break;
                  case 'x':
                      exit("Goodbye!" . PHP_EOL);
                  default:
                      echo "Invalid choice." . PHP_EOL;
                      clearScreen();
              }
          }

          echo PHP_EOL;
      }

      main();
      ```

      ```php src/helpers.php theme={null}
      <?php

      use Doctrine\DBAL\Connection;
      use Doctrine\DBAL\DriverManager;

      const WIDTH = 100;
      const VERSION = '1.0.0';

      function clearScreen()
      {
          if (strtoupper(substr(PHP_OS, 0, 3)) === 'WIN') {
              system('cls');
          } else {
              system('clear');
          }
      }

      function createConnection(): Connection
      {
          $params = [
              "auth_token"        => getenv('TURSO_AUTH_TOKEN'),
              "sync_url"          => getenv('TURSO_DATABASE_URL'),
              'driverClass'       => \Turso\Doctrine\DBAL\Driver::class,
          ];

          $db = DriverManager::getConnection($params);
          
          return $db;
      }
      ```

      ```php src/Todo.php theme={null}
      <?php

      namespace Turso\Todo\CLI;

      use Doctrine\DBAL\Connection;

      class Todo
      {

          private Connection $db;

          public function __construct()
          {
              $this->db = createConnection();
          }

          public function loadTodos(): array
          {
              $sql = "SELECT * FROM todos";
              return $this->db->fetchAllAssociative($sql);
          }

          public function saveTodo(string $todo): void
          {
              $sql = "INSERT INTO todos (name) VALUES (?)";
              $this->db->executeStatement($sql, [$todo]);
          }

          public function updateTodo(int $id, string $todo): void
          {
              $sql = "UPDATE todos SET name = ? WHERE id = ?";
              $this->db->executeStatement($sql, [$todo, $id]);
          }

          public function removeTodo(int $id): void
          {
              $sql = "DELETE FROM todos WHERE id = ?";
              $this->db->executeStatement($sql, [$id]);
          }

          public function listTodos()
          {
              $todos = $this->loadTodos();
              echo "\n" . "TODO-List   " . str_repeat('-', WIDTH - 12) . "\n\n";
              if (!empty($todos)) {
                  foreach ($todos as $todo) {
                      echo sprintf("[%d] %s\n", $todo['id'], $todo['name']);
                  }
              } else {
                  echo "Nothing...\n";
              }
              echo "\n" . str_repeat('-', WIDTH) . "\n";
          }

          public function addTodo()
          {
              echo "Enter the new To-Do: ";
              $todo = trim(fgets(STDIN));
              $this->saveTodo($todo);
              echo "To-Do added.\n";
          }

          public function editTodo()
          {
              $this->listTodos();
              echo "Enter the number of the To-Do to edit: ";
              $index = intval(trim(fgets(STDIN)));

              $findTodo = $this->db->executeQuery("SELECT * FROM todos WHERE id = ?", [$index])->fetchAssociative();

              if (!empty($findTodo)) {
                  echo "Enter the new value: ";
                  $todo = trim(fgets(STDIN));
                  $this->updateTodo($findTodo['id'], $todo);
                  echo "To-Do updated.\n";
              } else {
                  echo "Invalid index.\n";
              }
          }

          public function deleteTodo()
          {
              $this->listTodos();
              echo "Enter the number of the To-Do to delete: ";
              $index = intval(trim(fgets(STDIN)));
              $findTodo = $this->db->executeQuery("SELECT * FROM todos WHERE id = ?", [$index])->fetchAssociative();
              if (!empty($findTodo)) {
                  $this->removeTodo($findTodo['id']);
                  echo "To-Do deleted.\n";
              } else {
                  echo "Invalid index.\n";
              }
          }
      }
      ```
    </CodeGroup>
  </Step>

  <Step title="Your PHP Application Ready!">
    ![PHP TODO CLI - TURSO](https://i.imgur.com/dmrPFr2.png)
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="PHP Todo CLI + Doctrine DBAL" icon="github" href="https://github.com/tursodatabase/example/php-todo-cli-doctrine-dbal/tree/master">
    See the full source code
  </Card>

  <Card title="Symfony Rest API CRUD" icon="github" href="https://github.com/tursodatabase/example/symfony7-rest-api-crud/tree/master">
    See the full source code
  </Card>
</CardGroup>
