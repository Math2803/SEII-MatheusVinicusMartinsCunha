#/bin/bash

showuptime(){
	up=$(uptime -p | cut -c4-)
	since=$(uptime -s)
	cat << EOF
------
THIS IS MACHINE HAS BEEN UP FOR ${up}
It has been running since ${since}
-------
EOF
}

showuptime
