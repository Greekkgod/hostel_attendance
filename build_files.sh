echo "Building the project..."
python -m pip install -r requirements.txt

echo "Collect Static..."
# Use a dummy database URL to prevent SQLite errors during collectstatic
export DATABASE_URL="postgresql://dummy:dummy@dummy:5432/dummy"
python manage.py collectstatic --noinput --clear

echo "Running Migrations..."
python manage.py migrate --noinput
