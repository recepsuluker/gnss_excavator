#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/bagger/gnss/src/nmea_tcp_driver"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/bagger/gnss/install/lib/python3/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/bagger/gnss/install/lib/python3/dist-packages:/home/bagger/gnss/build/lib/python3/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/bagger/gnss/build" \
    "/home/bagger/software/venv/bin/python3" \
    "/home/bagger/gnss/src/nmea_tcp_driver/setup.py" \
     \
    build --build-base "/home/bagger/gnss/build/nmea_tcp_driver" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/bagger/gnss/install" --install-scripts="/home/bagger/gnss/install/bin"
