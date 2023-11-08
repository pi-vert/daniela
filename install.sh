sudo apt update
sudo apt upgrade
# Pour le bras
sudo apt install -y i2c-tools python3-smbus
sudo apt install -y python3-pip
python -m pip install --break-system-packages adafruit-circuitpython-servokit
# Pour le monitoring
python -m pip install --break-system-packages psutil

