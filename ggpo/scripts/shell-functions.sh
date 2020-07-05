#!/bin/sh
find_python() {

	python -V 2>&1 |grep "^Python 3\." >/dev/null
	if [ $? -eq 0 ]; then
		PYTHON=python3
	else
		python2 -V 2>&1 |grep "^Python 3\." >/dev/null
		if [ $? -eq 0 ]; then
			PYTHON=python3.8
		else
			python2.7 -V 2>&1 |grep "^Python 3\." >/dev/null
			if [ $? -eq 0 ]; then
				PYTHON=python3.7
			else
				python2.6 -V 2>&1 |grep "^Python 3\." >/dev/null
				if [ $? -eq 0 ]; then
					PYTHON=python3.6
				fi
			fi
		fi
	fi
	if [ -z "${PYTHON}" ]; then
		echo "ERROR: can't find python 3.x"
		exit 1
	fi
}
