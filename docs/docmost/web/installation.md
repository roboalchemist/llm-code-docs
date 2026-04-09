# Docmost Installation Guide

## Quick Start with Docker Compose

The easiest way to get started with Docmost is using Docker Compose:

```bash
git clone https://github.com/docmost/docmost.git
cd docmost
docker-compose up -d
```

Access Docmost at `http://localhost:3000`

## Manual Installation (Linux/macOS)

### Prerequisites

- Node.js 18 or higher
- pnpm package manager
- PostgreSQL 12+ or SQLite
- Redis (optional but recommended)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/docmost/docmost.git
cd docmost
```

2. Install dependencies:
```bash
pnpm install
```

3. Create environment file:
```bash
cp .env.example .env
```

4. Configure database in `.env`:
```
DATABASE_URL=postgresql://user:password@localhost:5432/docmost
```

5. Run migrations:
```bash
pnpm run migrate
```

6. Start the application:
```bash
pnpm run dev
```

Application will be available at `http://localhost:3000`

## Docker Installation

### Using Official Images

```bash
docker run -d \
  -p 3000:3000 \
  -e DATABASE_URL=postgresql://user:password@db:5432/docmost \
  -e REDIS_URL=redis://redis:6379 \
  docmost/docmost:latest
```

### Building Custom Image

```bash
git clone https://github.com/docmost/docmost.git
cd docmost
docker build -t docmost:custom .
docker run -d -p 3000:3000 docmost:custom
```

## Post-Installation

### Initial Setup

1. Access http://localhost:3000
2. Create admin account
3. Configure basic settings
4. Create first space

### Database Initialization

Docmost automatically runs migrations on first startup. For manual migration:

```bash
pnpm run db:migrate
```

## Production Deployment

See the Deployment section in the comprehensive documentation for production setup with proper security, SSL, and scaling considerations.
