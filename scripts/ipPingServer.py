#!/usr/bin/python

import time
import BaseHTTPServer
import os
import time
import sys
#import html
#from terminaltables import AsciiTable
import process_topology as topo

links_file_name = ""
if topo.RUN_IN_ONL == 1:
  links_file_name = '../linksList'
else:
  links_file_name = '../linksList.testbed'

# Each
HOST_NAME = '128.252.153.28' # !!!REMEMBER TO CHANGE THIS!!!
PORT_NUMBER = 8080

#key format: /name/prefix-192.168.1.1 (neighbor IP address)
key_id = dict()
id_key = dict()
id_rtt = dict()
table_data = [["Link ID", "Prefix-IP Pair", "RTT (ms)"]]

update = 0
last_update = 0

def populate_id_rtt_table():
  f = open(links_file_name, 'r')
  for line in f:
    line = line.rstrip()
    comps = line.split(" ")
    key = topo.site_prefix2site[comps[1]] + " --> " + topo.ip_prefix2site[comps[2]]
    link_id = comps[0]
    key_id[key] = link_id
    id_key[int(link_id)] = key
    id_rtt[int(link_id)] = 0

def dump_rtt():
  processed = dict()
  #for link_id in range(1, len(id_rtt)):
  for link_id in id_rtt:
    key = id_key[link_id]
    if key not in processed:
      one_line = []
      one_line.append("{:<3}".format(str(link_id)))
      one_line.append("{:<20}".format(id_key[link_id].upper()))
      one_line.append("{:<10}".format(str(id_rtt[link_id])))

      #r_key = key.split(" --> ")[1] + " --> " + key.split(" --> ")[0]
      #r_id = int(key_id[r_key])
      #one_line.append("{:<3}".format(str(r_id)))
      #one_line.append("{:<20}".format(id_key[r_id].upper()))
      #one_line.append("{:<10}".format(str(id_rtt[r_id])))

      processed[key] = 1
      #processed[r_key] = 1

      id_rtt[link_id] = 0
      #id_rtt[r_id] = 0

      print one_line
      #table_data.append(one_line)
      #table = AsciiTable(table_data)
  #print table.table

header = """ <!DOCTYPE html>
<html lang="en">
<head>
  <title>Bootstrap Example</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js"></script>
  <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
</head>
<body>
 
<div class="container">
  <table class="table table-hover">
    <thead>
      <tr>
        <th class="col-sm-1">Link ID</th>
        <th class="col-sm-1">Link</th>
        <th class="col-sm-4">RTT</th>
      </tr>
    </thead>
"""
 
tailer = """ </table>
</div>
"""
 
def dump_rtt_html():
  table_code = ""
  table_code += '<tbody>\n'
  for link_id in range(0,140):
    if link_id in id_rtt:
      table_code += '<tr>\n'
      table_code += '<td>'+str(link_id)+'</td><td>'+id_key[link_id]+'</td><td>'+str(id_rtt[link_id])+'</td>'+"\n"
      table_code += '</tr>\n'
  table_code += '</tbody>\n'

  return table_code

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  def do_HEAD(s):
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
  def do_GET(s):
    """Respond to a GET request."""
    if "/ipPing/" in s.path:
      msg = s.path.split("/ipPing/")[1]
      comps = msg.split("&")
      comps.pop(-1) # remove the last element

      for comp in comps:
        key = comp.split("+")[0]
        if key[0] != '/':
          key = "/" + key
        rtt = comp.split("+")[1]

        key_0 = key.split(":")[0]
        key_1 = key.split(":")[1]

        key_0 = topo.site_prefix2site[key_0]
        key_1 = topo.ip_prefix2site[key_1]

        key = key_0 + " --> " + key_1
        link_id = key_id[key]
        #print "link_id: ", link_id, " key: ", key
        id_rtt[int(link_id)] = rtt

      global update
      update = update + 1
      if update > 200:
      #if update > 10:
        os.system('clear')
        dump_rtt()
        update = 0

    if "/get_ip_rtt.html" in s.path:
      s.send_response(200)
      s.send_header("Content-type", "text/html")
      s.end_headers()

      s.wfile.write(header)
      s.wfile.write(dump_rtt_html())
      s.wfile.write(tailer)

if __name__ == '__main__':

  populate_id_rtt_table()

  server_class = BaseHTTPServer.HTTPServer
  httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
  print time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER)
  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass
  httpd.server_close()
  print time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER)

