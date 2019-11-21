# File distributor module
The script checks a given directory for new files matching a pattern,
and if found moves them to an appropriate directory according to a date
parsed from the file name. If no target directory found it is created.

# Files
Configuration file: /etc/file_distributor/config.ini<br />
Service file: /lib/systemd/system/file_distributor.service<br />
Script file: /usr/sbin/file_distributor.py<br />

# After cloning repo setup <dirs> in <config.ini>:
in<br />
out<br />

# When done with configuration file setup script with following commands:
chmod +x file_distributor_setup.sh<br />
sudo bash file_distributor_setup.sh<br />

# Commands to control script:
sudo systemctl status file_distributor.service        #To check service state <br />
sudo systemctl stop file_distributor.service          #To stop running service <br />
sudo systemctl start file_distributor.service         #To start running service <br />
sudo systemctl restart file_distributor.service       #To restart running service <br />
