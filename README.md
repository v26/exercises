# exercises
Example modules

# files
Configuration file: /etc/file_distributor/config.ini
Service file: /lib/systemd/system/file_distributor.service
Script file: /usr/sbin/file_distributor.py

# After cloning repo setup <dirs> in <config.ini>:
  in
  out

# When done with configuration file setup script with following commands:
chmod +x file_distributor_setup.sh
sudo bash file_distributor_setup.sh

# Commands to control script:
sudo systemctl stop file_distributor.service          #To stop running service 
sudo systemctl start file_distributor.service         #To start running service 
sudo systemctl restart file_distributor.service       #To restart running service 
