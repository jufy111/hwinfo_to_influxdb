# HWiNFO to influxDB 2
Revision 1.00 28/04/2022

This program does not have to run on the localhost that HWiNFO is running on. I personally have a Docker container running it on my NAS, where the influxDB is also installed. I'll get around to uploading the Docker container to DockerHub eventually.
The script itself pushes directly to influxDB. It does not require telegraf.


## --------Python Dependancies------------
Tested with Python 3.9, I cant comment on compatibility of other versions but there is no reason to beleive that it won't work on other versions.
```
pip install influxdb_client
```
## Other Depenendencices
#### Remote Sensor Monitor
[Download Link](https://www.hwinfo.com/files/RemoteSensorMonitor/Remote.Sensor.Monitor.v.2.1.0.zip)  
(https://www.hwinfo.com/forum/threads/introducing-remote-sensor-monitor-a-restful-web-server.1025/)  
This program post the HWiNFO data to a html webserver in JSON format

#### HWiNFO PRO
Allthough I have only tested with the pro version, I did see the following comment [here](https://www.reddit.com/r/NiceHash/comments/mmnuxf/update_how_to_make_the_pi_rig_monitor/?utm_source=share&utm_medium=web2x&context=3).

>"You must have HWiNFO pro - as the normal HWiNFO only gives shared memory support for 12 hrs and then resets. This is not an issue but it means that you have to constantly enable it every 12hrs and restart the Remote Sensor Monitor below."
