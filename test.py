import os
import sys
import time
import threading

CWD = os.path.dirname(os.path.realpath(__file__))
ROOT_DIR = os.path.dirname(CWD)
sys.path.append(ROOT_DIR)

from zk import ZK

ips = ["10.30.0.39","10.30.0.40","10.30.0.79","10.30.0.80","10.30.0.123","10.30.0.126","10.30.0.132","10.30.1.55","10.30.1.77","10.30.1.89","10.30.1.134","10.30.1.206","10.30.1.207","10.30.1.239","10.30.1.249","10.30.2.12","10.30.2.38","10.30.2.74","10.30.2.81","10.30.2.82","10.30.2.96","10.30.2.98","10.30.2.108","10.30.2.115","10.30.2.124","10.30.2.127","10.30.2.187","10.30.2.194","10.30.2.199","10.30.2.202","10.30.2.203","10.30.2.205","10.30.2.208","10.30.2.230","10.30.2.241","10.30.3.0","10.30.3.2","10.30.3.8","10.30.3.33","10.30.3.41","10.30.3.73","10.30.3.81","10.30.3.82","10.30.3.83","10.30.3.120","10.30.3.126","10.30.3.130","10.30.3.153","10.30.3.156","10.30.3.159","10.30.3.161","10.30.3.163","10.30.3.164","10.30.3.166","10.30.3.167","10.30.3.168","10.30.3.169","10.30.3.170","10.30.3.174","10.30.3.179","10.30.3.182","10.30.3.183","10.30.3.184","10.30.3.186","10.30.3.187","10.30.3.188","10.30.3.189","10.30.3.190","10.30.3.191","10.30.3.204"]

#ips = ['10.30.0.78']


def test_voice(ip):
    conn = None
    zk = ZK(ip, port=4370)
    try:
        conn = zk.connect()
        
        for i in range(0,65):
            print ("test_voice, %i" % i)
            zk.test_voice(i)
        # zk.test_voice(18)
        print("Voice test successful for {}".format(ip))
    except Exception as e:
        print("Error while testing voice for {}: {}".format(ip, e))
    finally:
        if conn:
            conn.disconnect()

threads = []
for ip in ips:
    thread = threading.Thread(target=test_voice, args=(ip,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All voice tests completed")
