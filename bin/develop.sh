# if has --start argument
#   start develop server

if [ "$1" = "--start" ]; then
  echo "Starting develop..."
  # Collect python requirements.
  python -m pipreqs.pipreqs ./server --force
  docker-compose -f docker-compose.yml build
  docker-compose -f docker-compose.yml up
  docker exec -it server python manage.py collectstatic --noinput
elif [ "$1" = "--stop" ]; then
  echo "Stopping develop...."
  docker-compose -f docker-compose.yml down
  kill $(ps aux | grep 'node ./bin/develop.js' | awk '{print $2}')
else
  echo "Usage: ./develop.sh [--start|--stop]"
fi