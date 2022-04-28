#HWiNFO to influxDB 2
#Revision 1.00 28/04/2022

####Python Dependancies
#pip install influxdb_client

###Other Depenendencices
#Remote Sensor Monitor
#https://www.hwinfo.com/forum/threads/introducing-remote-sensor-monitor-a-restful-web-server.1025/

#HWiNFO PRO
#You must have HWiNFO pro - as the normal HWiNFO only gives shared memory support for 12 hrs and then resets.
#This is not an issue but it means that you have to constantly enable it every 12hrs and restart the Remote Sensor Monitor below.


####################################################################################################
# Import modules
####################################################################################################

import requests
import time
from datetime import datetime
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS



####################################################################################################
# Variables to Set
####################################################################################################

# InfluxDB Database Details
token = "5Bn-0sJQIPMmq28lUXyfmBSWQjEJMj0qHgWRSz-5Ku2-er52wrxRWl7Yr1Sum7qIG8GbMEw4zuPFdv7Y6BkooA=="   ##sampledb
org = "yourinfluxDBorghere"
bucket = "yourbuckernamehere"
db_url = "http://192.168.1.100:8086"

# Variables of PC
sample_time = 10 # in seconds
poll_ip = "http://192.168.1.101:55555"  #ip address of PC you are hosting
device_id = "nameforyourdevicehere"

####################################################################################################
#Functions start here
####################################################################################################

#test html webserver is up
def init():
    try:
        hwinfo = requests.get(poll_ip)
        print("Remote Sensor Moniter is reachable")
    except:
        print("Unable to conact Remote Sensor Moniter web server. Check both Remote Sensor Moniter and HWiNFO are running.")
        exit()


#####Polling function
def poll(): 
 
    try:        
        hwinfo_web_data = requests.get(poll_ip)
    except:
        print(datetime.now(), " Error! Unable to conact Remote Sensor Moniter web server. Check both Remote Sensor Moniter and HWiNFO are running.")
        return

    try:    
        data=hwinfo_web_data.json()                
        process_data(data,write_api)      
    except AssertionError as error:
        print(error)
        return

#########Process data
def process_data(data,write_api):
    for a in data:   
        sensorclass=a['SensorClass']
        sensorname=a['SensorName']
        sensorvalue=a['SensorValue']

        #parse to format accepted by influxDB
        influxdata=str(device_id+",Measurement=" + sensorclass.replace(" ", "_")+" "+str(sensorname.replace(" ", "_"))+"="+str(sensorvalue))

        #Write to influxDB
        try:
            write_api.write(bucket, org, influxdata)
        except:
            print(datetime.now(), " Error! Could not write to database")
            return
    print(datetime.now(), ": Successfully posted data to server.")



####################################################################################################
#Main Script Starts here
####################################################################################################
print("starting....")
client = InfluxDBClient(url=db_url, token=token)
write_api = client.write_api(write_options=SYNCHRONOUS)
init()
while True:    
    poll()
    time.sleep(sample_time - time.monotonic() % sample_time)


        
