# LOBE-AI-Gait-Detector
Using microsoft lobe hat from adafruit and raspberry pi4 to detect abnormal gait



## Setup PiOS using the latest image of Raspberry Pi OS Lite
    Follow this link 
    https://www.raspberrypi.com/software/

###### Enable SSH on pi during installation
###### On your terminal, type in this next line to find the IP address of you pi
    ping -c 3 raspberrypi.local
###### Log in via ssh using, default user is pi and password is raspberry
    ssh pi@"ip address goes here"
###### Update PiOS
###### First Type
    sudo apt-get update
###### Then Type
    sudo apt-get upgrade
###### Then Type
    sudo apt-get -y upgrade


###### Setup Software 
###### Install Python
-    ###### First Type
    sudo apt-get install python3-pip
-    ###### Then Type
    sudo pip3 install --upgrade setuptools
###### Installing Blinka 
-    ###### First Type
    cd ~
-    ###### Then Type
    sudo pip3 install --upgrade adafruit-python-shell
-    ###### Then Type
    wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
-    ###### Then Type
    sudo python3 raspi-blinka.py
###### Select yes to reboot

###### Installing DotStar library. This step is to install circuit python support
-    ###### Type
    pip3 install --upgrade adafruit-circuitpython-dotstar adafruit-circuitpython-motor adafruit-circuitpython-bmp280

###### Installing Audio/Voice Support
-    ###### First Type
    cd ~
-    ###### Then Type
    sudo apt-get install -y git
-    ###### Then Type
    git clone https://github.com/HinTak/seeed-voicecard
-    ###### Then Type
    cd seeed-voicecard
-    ###### Then Type
    git checkout v5.9
    sudo ./install.sh
-    ###### Reboot Your Pi 
    sudo reboot
-    ###### After reboot, open terminal and run:
    sudo aplay -l


###### Check for camera, if using raspberry pi directly
-    ###### First Type
    libcamera-hello -t 0
-    ###### If running via ssh and run into what():  failed to import fd 19 ERROR
   libcamera-hello --qt-preview
