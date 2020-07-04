#!/bin/bash

# make sure this is run as root
uid=$(id -ur)
if [ "$uid" != "0" ]; then
        echo "ERROR: This script must be run as root."
	if [ -x /usr/bin/sudo ]; then
		echo "try: sudo $0"
	fi
        exit 1
fi

# ubuntu/debian based distributions
# hope this is the right pyqt5 package
if [ -x /usr/bin/apt-get ]; then
	apt-get install wine python3-pyqt5
	exit $?
fi

# archlinux
if [ -x /usr/bin/pacman ]; then
    pacman -S multilib/wine multilib/lib32-mpg123 extra/python-pyqt5 extra/phonon-qt5 extra/python-pyqt5 extra/python-sip
    exit $?
fi

# fedora (untested)
if [ -x /usr/bin/yum ]; then
    yum install wine python3-qt5
    exit $?
fi

# suse/opensuse (untested)
if [ -x /usr/bin/zypper ] ; then
    zypper in wine python3-qt5
    exit $?
fi

echo "Your distribution is not supported :("
echo "Please install 'pyqt5' and 'wine' to run fightcade."
exit 1
