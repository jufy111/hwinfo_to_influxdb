# HWiNFO to influxDB (2.00+)  
Revision 1.00 28/04/2022  
Initial push

## Description and general notes
The python script pulls HWiNFO via Remote Sensor Monitor and posts it to innfluxDB (version 2 and above only).  
  
This program does not have to run on the localhost that HWiNFO is running on. I personally have a Docker container running it on my NAS, where the influxDB is also installed. I'll get around to uploading the Docker container to DockerHub eventually.
The script itself pushes directly to influxDB. It does not require telegraf.


## --------Python Dependancies------------
Tested with Python 3.9, I can't comment on the compatibility of other versions but there is no reason to believe that it won't work on other versions.
```
pip install influxdb_client
```
## Other Dependencies
#### Remote Sensor Monitor
(https://www.hwinfo.com/forum/threads/introducing-remote-sensor-monitor-a-restful-web-server.1025/)  
>Remote Sensor Monitor is a Windows console application designed to present various hardware sensor parameters reported by HWiNFO / GPU-Z / AIDA64 / Open Hardware Monitor as a JSON string and make it available over the network. Enabling GPU-Z, HWiNFO and AIDA64 requires the programs to be running the background. The minimum supported versions are: GPU-Z: 0.7.4, HWiNFO: 4.30, AIDA64: 4.00.2706. Open Hardware Monitor sensors can be reported only if OpenHardwareMonitorLib.dll is present in the same folder as that of the application. Once the web server starts up, the JSON string is available at http://<IP>:<PORT> ; The reported parameters can be filtered / configured via the web interface at http://<IP>:<PORT>/config ; The program requires administrative privileges in order to open and close the applicable port in the firewall when necessary.  
  
[Download Link](https://www.hwinfo.com/files/RemoteSensorMonitor/Remote.Sensor.Monitor.v.2.1.0.zip)  

  To launch from the command line 
  ```
  Remote Sensor Monitor.exe --hwinfo=1 --gpuz=0 --aida64=0 --ohm=0
  ```
  
  
#### HWiNFO PRO
Although I have only tested with the pro version, I did see the following comment [here](https://www.reddit.com/r/NiceHash/comments/mmnuxf/update_how_to_make_the_pi_rig_monitor/?utm_source=share&utm_medium=web2x&context=3).

>"You must have HWiNFO pro - as the normal HWiNFO only gives shared memory support for 12 hrs and then resets. This is not an issue but it means that you have to constantly enable it every 12hrs and restart the Remote Sensor Monitor below."
