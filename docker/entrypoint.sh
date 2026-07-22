#!/bin/sh
set -e

echo "Waiting for database..."
python - << 'PYEOF'
import os, time, sys
import psycopg
url = os.environ.get("DATABASE_URL", "")
if url:
    for _ in range(30):
        try:
            psycopg.connect(url.replace("postgres://", "postgresql://"))
            break
        except Exception:
            time.sleep(1)
    else:
        sys.exit("Database never became available")
PYEOF

python manage.py migrate --noinput
python manage.py collectstatic --noinput

exec "$@"
