#!/bin/bash
cp file_distributor.service /lib/systemd/system/file_distributor.service
cp file_distributor.py /usr/sbin/file_distributor.py
mkdir -p /etc/file_distributor
cp config.ini /etc/file_distributor/config.ini
systemctl daemon-reload
systemctl enable file_distributor.service
systemctl start file_distributor.service