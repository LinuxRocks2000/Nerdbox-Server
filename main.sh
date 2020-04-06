if [ $UID == 0 ]; then
  sudo python3 webserver/main.py &
else
  printf "You do not have root"
  sleep 1
  printf "\rCheck out the errors"
  sleep 1
  printf "\rThis is going to be funny"
  sleep 1
  printf "\r3...                        "
  sleep 1
  printf "\r2...                               "
  sleep 1
  printf "\r1...                               "
  sleep 1
  echo "\nWatch the world die"
  python3 webserver/main.py &
fi
