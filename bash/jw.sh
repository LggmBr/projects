#! /bin/bash

echo 'Just write, type "/end" to quit.'
while true; do
  read -r line
  if [[ ${line::1} == "/" ]]; then
    case "$line" in
      "/end") break
      ;;
      "/help") echo 'Just write, type "/end" to quit.'
      ;;
      *) echo "Command not found!!"
      ;;
    esac
    
    break 
  else
    echo $line >> $1.md
  fi
done
