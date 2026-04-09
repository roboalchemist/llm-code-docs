# Docmost Documentation

**Source:** https://docmost.com/docs and https://github.com/docmost/docmost

## Overview

Docmost is an open-source collaborative wiki and documentation software, serving as a self-hosted alternative to Notion and Confluence. It provides real-time collaboration, rich document editing, and comprehensive permission management.

### Key Features

- **Real-time Collaboration**: Multiple users can edit documents simultaneously with live cursor tracking
- **Rich Text Editor**: Support for formatting, code blocks, and embeds
- **Diagrams Support**:
  - Draw.io integration
  - Excalidraw for sketches
  - Mermaid diagrams
- **Spaces**: Organize documentation into logical spaces
- **Permissions Management**: Fine-grained access control at space and document level
- **Groups**: Organize users into logical groups
- **Comments**: Collaborative commenting on documents
- **Page History**: Track and restore previous versions
- **Full-Text Search**: Powered by Algolia for fast searching
- **File Attachments**: Attach files directly to documents
- **Embeds**: Support for Airtable, Loom, Miro, and more
- **Multi-language Support**: 10+ language translations

## Getting Started

### Installation

Docmost can be deployed in multiple ways:

#### 1. Docker Compose (Recommended)

```bash
git clone https://github.com/docmost/docmost.git
cd docmost
docker-compose up -d
```

#### 2. Manual Installation

Requires:
- Node.js 18+
- PostgreSQL or SQLite
- Redis (optional)

### System Requirements

- **CPU**: 1+ core recommended
- **RAM**: 512MB minimum, 2GB+ recommended
- **Storage**: Depends on usage (100GB for typical enterprise deployment)
- **Database**: PostgreSQL recommended for production
- **OS**: Linux, macOS, or Windows

### Docker Setup

The project includes a `docker-compose.yml` for quick deployment:

```yaml
version: '3.8'
services:
  docmost:
    image: docmost/docmost:latest
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://user:password@db:5432/docmost
      REDIS_URL: redis://redis:6379
    depends_on:
      - db
      - redis
```

## Configuration

### Environment Variables

Key environment variables for configuration:

- `DATABASE_URL`: Database connection string
- `REDIS_URL`: Redis connection (optional)
- `JWT_SECRET`: Secret for JWT tokens
- `NEXTAUTH_SECRET`: NextAuth configuration
- `NEXTAUTH_URL`: Authentication URL
- `FILE_UPLOAD_MAX_SIZE`: Maximum file upload size
- `ALLOWED_ORIGINS`: CORS allowed origins

### Database Setup

Docmost supports:
- PostgreSQL (recommended for production)
- SQLite (suitable for development/small deployments)

#### PostgreSQL Setup

```bash
createdb docmost
createuser docmost -P
psql docmost -f /path/to/docmost/migrations.sql
```

#### SQLite Setup

SQLite is configured automatically and stores data in `./data/docmost.db` by default.

## Architecture

### Technology Stack

**Frontend:**
- React with TypeScript
- Next.js for server-side rendering
- TailwindCSS for styling
- Editor.js for document editing
- Real-time collaboration via WebSocket

**Backend:**
- Node.js runtime
- Express.js web framework
- PostgreSQL/SQLite database
- Redis for caching and real-time features
- S3-compatible storage for file uploads

### Project Structure

```
docmost/
├── apps/
│   ├── client/          # Next.js frontend application
│   └── server/          # Express.js backend API
├── packages/
│   ├── ee/             # Enterprise Edition features
│   ├── shared/         # Shared utilities and types
│   └── ...
├── docker-compose.yml
└── package.json
```

## User Guide

### Creating Spaces

Spaces are top-level containers for organizing documents:

1. Click "Create Space" in the sidebar
2. Enter space name and description
3. Configure initial permissions
4. Invite team members

### Document Management

#### Creating Documents

1. Navigate to desired space
2. Click "New Document" or use the "+" button
3. Enter document title
4. Start editing with rich text editor

#### Editing Documents

- **Text Formatting**: Bold, italic, underline, strikethrough
- **Lists**: Ordered and unordered lists
- **Code Blocks**: Syntax-highlighted code with language selection
- **Tables**: Insertable tables with formatting
- **Headings**: Hierarchical heading support (H1-H6)
- **Links**: Internal and external links
- **Images**: Embed images from URLs or upload locally
- **Embeds**: Integrate external content

#### Version Control

Every document automatically tracks changes:
- Access document history from the menu
- View changes by date and author
- Restore to any previous version
- Compare versions side-by-side

### Permissions and Access Control

#### Permission Levels

- **Owner**: Full control over space
- **Editor**: Can create and modify documents
- **Commenter**: Can view and comment on documents
- **Viewer**: Read-only access

#### Sharing

1. Open document or space settings
2. Click "Share"
3. Select sharing method:
   - Direct user/group invitation
   - Public link (with optional expiration)
   - Domain-based access

### Search

Docmost provides full-text search powered by Algolia:

1. Use search icon in top navigation
2. Enter search query
3. Results show matching documents and snippets
4. Click result to navigate to document

## API Reference

### Authentication

All API requests require authentication via JWT token:

```bash
Authorization: Bearer <jwt_token>
```

### Document Endpoints

#### Get Document

```
GET /api/documents/:id
```

Response:
```json
{
  "id": "doc_123",
  "title": "Document Title",
  "content": "...",
  "createdAt": "2024-01-01T00:00:00Z",
  "updatedAt": "2024-01-01T00:00:00Z",
  "spaceId": "space_123",
  "createdBy": "user_123"
}
```

#### Create Document

```
POST /api/documents
```

Request body:
```json
{
  "title": "New Document",
  "spaceId": "space_123",
  "content": "..."
}
```

#### Update Document

```
PUT /api/documents/:id
```

Request body:
```json
{
  "title": "Updated Title",
  "content": "..."
}
```

#### Delete Document

```
DELETE /api/documents/:id
```

### Space Endpoints

#### List Spaces

```
GET /api/spaces
```

#### Get Space

```
GET /api/spaces/:id
```

#### Create Space

```
POST /api/spaces
```

Request body:
```json
{
  "name": "Engineering",
  "description": "Engineering documentation"
}
```

#### Update Space

```
PUT /api/spaces/:id
```

#### Delete Space

```
DELETE /api/spaces/:id
```

### User Endpoints

#### Get Current User

```
GET /api/users/me
```

#### List Users

```
GET /api/users
```

#### Invite User

```
POST /api/users/invite
```

Request body:
```json
{
  "email": "user@example.com",
  "spaceId": "space_123",
  "role": "editor"
}
```

## Development

### Prerequisites

- Node.js 18+
- pnpm (package manager)
- PostgreSQL or SQLite
- Redis (optional)

### Setup Development Environment

```bash
# Clone repository
git clone https://github.com/docmost/docmost.git
cd docmost

# Install dependencies
pnpm install

# Copy environment file
cp .env.example .env

# Configure database (update .env with your settings)
DATABASE_URL=postgresql://user:password@localhost:5432/docmost

# Run database migrations
pnpm run db:migrate

# Start development servers
pnpm run dev
```

### Development Server Ports

- Frontend: http://localhost:3000
- Backend API: http://localhost:3001
- Database: localhost:5432

### Running Tests

```bash
# Run all tests
pnpm run test

# Run tests in watch mode
pnpm run test:watch

# Run specific test file
pnpm run test -- path/to/test.spec.ts
```

### Building for Production

```bash
# Build all applications
pnpm run build

# Build specific app
pnpm run build --scope=@docmost/server

# Build Docker image
docker build -t docmost:latest .
```

## Deployment

### Docker Deployment

#### Using Docker Compose

The repository includes `docker-compose.yml` for complete stack deployment including PostgreSQL and Redis.

#### Custom Docker Setup

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN pnpm install
RUN pnpm run build
EXPOSE 3000
CMD ["pnpm", "start"]
```

### Environment Setup for Production

```bash
# Security
NEXTAUTH_SECRET=<random-secret>
JWT_SECRET=<random-secret>

# Database
DATABASE_URL=postgresql://user:password@prod-db:5432/docmost

# Email (for notifications)
SMTP_HOST=smtp.example.com
SMTP_PORT=587
SMTP_USER=alerts@example.com
SMTP_PASSWORD=password

# Storage
FILE_UPLOAD_PATH=/var/docmost/uploads
FILE_UPLOAD_MAX_SIZE=104857600  # 100MB

# URLs
NEXTAUTH_URL=https://docmost.example.com
ALLOWED_ORIGINS=https://docmost.example.com
```

### Reverse Proxy Configuration

#### Nginx

```nginx
server {
    listen 443 ssl http2;
    server_name docmost.example.com;

    ssl_certificate /etc/letsencrypt/live/docmost.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/docmost.example.com/privkey.pem;

    location / {
        proxy_pass http://localhost:3000;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # WebSocket support
    location /_next/webpack-hmr {
        proxy_pass http://localhost:3000/_next/webpack-hmr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }
}
```

#### Caddy

```
docmost.example.com {
    reverse_proxy localhost:3000 {
        header_up X-Real-IP {remote_host}
        header_up X-Forwarded-For {remote_host}
        header_up X-Forwarded-Proto {scheme}
    }
}
```

## Security

### Best Practices

1. **Database Security**
   - Use strong passwords
   - Enable SSL/TLS for database connections
   - Run database on isolated network

2. **API Security**
   - Require HTTPS only
   - Implement rate limiting
   - Use strong JWT secrets (32+ characters)
   - Enable CORS restrictions

3. **Authentication**
   - Use strong passwords (enforce 12+ characters)
   - Enable two-factor authentication when available
   - Regular security audits
   - Monitor access logs

4. **File Uploads**
   - Limit file size (default 100MB)
   - Validate file types
   - Store uploads outside web root
   - Consider S3 for scalability

### Backup and Recovery

#### Backup Strategy

```bash
# Database backup
pg_dump -h localhost -U docmost docmost > backup.sql

# File attachments backup
tar -czf attachments-backup.tar.gz /var/docmost/uploads

# Full system backup
tar -czf docmost-backup-$(date +%Y%m%d).tar.gz   /var/docmost/   /etc/docmost/
```

#### Restore Procedure

```bash
# Restore database
psql -h localhost -U docmost docmost < backup.sql

# Restore files
tar -xzf attachments-backup.tar.gz -C /

# Restart service
systemctl restart docmost
```

## Troubleshooting

### Common Issues

#### Database Connection Error

```
Error: connect ECONNREFUSED 127.0.0.1:5432
```

**Solution:**
- Verify PostgreSQL is running: `systemctl status postgresql`
- Check DATABASE_URL in .env
- Ensure database and user are created

#### Port Already in Use

```
Error: listen EADDRINUSE: address already in use :::3000
```

**Solution:**
```bash
# Find process using port
lsof -i :3000

# Kill process
kill -9 <PID>
```

#### Memory Issues

If experiencing out-of-memory errors:

```bash
# Increase Node.js memory
NODE_OPTIONS=--max-old-space-size=4096 pnpm start

# Scale Redis
redis-cli CONFIG SET maxmemory 2gb
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

#### File Upload Failures

- Check disk space: `df -h`
- Verify upload directory permissions: `chmod 755 /var/docmost/uploads`
- Check file upload size limit in .env
- Review application logs for specific errors

### Performance Optimization

1. **Database Optimization**
   - Create indexes on frequently queried fields
   - Use connection pooling
   - Regular VACUUM and ANALYZE

2. **Caching**
   - Enable Redis caching
   - Use CDN for static assets
   - Implement page caching strategies

3. **Frontend Optimization**
   - Code splitting
   - Image optimization
   - Lazy loading

## Contributing

### Development Workflow

1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Make changes and test thoroughly
4. Submit pull request with clear description
5. Code review before merge

### Code Style

- Follow existing code conventions
- Use TypeScript for type safety
- ESLint configuration for JavaScript/TypeScript
- Prettier for code formatting

### Setting up Development Environment

See "Development" section above for detailed setup instructions.

## Enterprise Edition

Docmost offers enterprise features under an enterprise license, including:

- Advanced permission management
- SSO/SAML integration
- Custom branding
- Advanced analytics
- Dedicated support

Enterprise features are located in:
- `apps/server/src/ee`
- `apps/client/src/ee`
- `packages/ee`

For enterprise licensing inquiries, contact the Docmost team.

## Community and Support

- **Website**: https://docmost.com
- **GitHub**: https://github.com/docmost/docmost
- **Twitter/X**: @DocmostHQ
- **Discussions**: GitHub Discussions on the repository
- **Cloud Version**: https://docmost.com/pricing

## License

Docmost core is licensed under AGPL 3.0. Enterprise features are available under a separate enterprise license.

```
AGPL 3.0 License - See LICENSE file in repository
```

Enterprise license terms are defined in `packages/ee/License`.

## Changelog

### Recent Versions

Consult the [GitHub Releases](https://github.com/docmost/docmost/releases) for detailed changelog and release notes.

### Version Support

- Latest version: Fully supported
- Previous version: Supported for security patches
- Older versions: Community support only

## Roadmap

Check the [GitHub Issues](https://github.com/docmost/docmost/issues) and [Discussions](https://github.com/docmost/docmost/discussions) for upcoming features and development plans.
