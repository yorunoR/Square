#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER developer WITH PASSWORD 'secret' LOGIN;
    ALTER USER developer CREATEDB CREATEROLE;
EOSQL

psql -v ON_ERROR_STOP=1 --username "developer" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE DATABASE square_dev;
EOSQL

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "square_dev" <<-EOSQL
    CREATE EXTENSION IF NOT EXISTS vector;
EOSQL
