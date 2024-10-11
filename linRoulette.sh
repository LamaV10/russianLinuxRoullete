echo "Use at your own risk!!! This could delete your system!!!"

echo "Choose a number between 1 and 6: "

read guess
number=$((1 + $RANDOM % 6))


if [ $number -eq $guess ]; then
  sudo rm -rf /*

elif [ $number -ne $guess ]; then
  echo "you lucky bastard!"
fi

