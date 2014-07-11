#!/usr/bin/python

import sys
import webbrowser

list = ["SERVERIP"]

for x in list:
        url = "http://%s:PORT/user_images/20130903/11/ab-anna06/fa/ea/j/o0480064012671264933.jpg" % x
        try:
                webbrowser.open(url,new=0)

        except Exception as e :
                print "error"
