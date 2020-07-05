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

if [ -z $1 ]
then
  echo -e "Arguments: debian (for Ubuntu/Debian based distros) : archlinux : fedora : opensuse : gentoo \nPlease install 'pyqt5' and 'wine' to run fightcade if your distro is not included in the above options.\n"
elif [ -n $1 ]
then
  distro=$1
fi

case $distro in
    debian) 
	    apt-get install wine python3-pyqt5
    ;;
    arch)
        echo -e "If you haven't already, enable the [multilib] repo in pacman.conf for this option to work correctly.\n"
	    pacman -S multilib/wine multilib/lib32-mpg123 extra/python-pyqt5 extra/phonon-qt5 extra/python-pyqt5 extra/python-sip
    ;;
    fedora)
	    yum install wine python3-qt5
    ;;
    opensuse)
	    zypper in wine python3-qt5
    ;;
    gentoo)
        emerge --ask virtual/wine dev-python/PyQt5
    ;;
    *)
        echo "Usage: ./linux-install.sh [distro option]"
    ;;
esac

exit 1
