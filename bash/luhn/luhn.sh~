#!/usr/bin/env bash

# The following comments should help you get started:
# - Bash is flexible. You may use functions or write a "raw" script.
#
# - Complex code can be made easier to read by breaking it up
#   into functions, however this is sometimes overkill in bash.
#
# - You can find links about good style and other resources
#   for Bash in './README.md'. It came with this exercise.
#
#   Example:
#   # other functions here
#   # ...
#   # ...
#
   main () {

        number=$(echo "$@" | tr -d ' ')
        if [ "${#number}" -eq 1 ]
        then
            echo "false"
            return
        fi            
        total=0
        for j in $(seq $(( ${#number} - 1 )) -1 0)
        do

            i=$((${#number} - 1 - $j)) # reverse index starting from zero
            digit=${number:$j:1}
            
            if ! [[ "$digit" =~ [0-9] ]]
            then
                echo false
                return
            fi
            
            if [ "$(( i % 2 ))" -ne "0" ]
            then
                double=$(( digit * 2 ))
                if [ "${double}" -gt "9" ]
                then
                    digit=$(( double - 9 ))
                else
                    digit=${double}                        
                fi                    
            fi
            
            total=$((total + digit))

        done

        if [ "$(( total % 10))" -eq "0" ]
        then
            echo "true"
        else
            echo "false"
        fi                        
   }
#
#   # call main with all of the positional arguments
   main "$@"
#

