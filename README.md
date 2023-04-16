# TestTrack

## Start cluster
```bash
docker-compose up -d
```

# Swagger docs
- Open http://localhost:8000/docs

# PgAdmin
- Open http://localhost:5050/
- Use credentials `pgadmin4@pgadmin.org:admin`
- Create new server connection to `postgresql://postgres:postgres@db:5432/test_db`

## Stop cluster
```bash
docker-compose down
```

# Initial configuration
## Install environment
```bash
pipenv install
```
## Install alembic (skip this step if already installed)
```bash
brew install alembic
pip3 install alembic
```
## Stop local Postgres server (skip this step if already stopped)
```bash
brew services stop postgresql
```

# Initial build (reference information)
## Build base image
```bash
docker-compose build
```
# Init alembic
```bash
alembic init alembic
```
## Create db model (if alembic/versions is empty)
```bash
docker-compose run web alembic revision --autogenerate -m "First migration"
```
## Apply migrations (if alembic/versions is empty)
```bash
docker-compose run web alembic upgrade head
```

## Resart cluster
```bash
docker-compose restart
```

# Debug
## Run bash into web container
```bash
docker-compose exec web bash
```
## Connect to db
```bash
docker-compose exec db psql --username=postgres --dbname=test_db
```
