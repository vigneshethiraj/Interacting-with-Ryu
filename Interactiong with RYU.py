# -*- coding: utf-8 -*-
"""
Interacting with Ryu SDN Controller
This program is used to view the list of switches connected to Ryu, view and modify flow tables
on the switches.
@author: Vignesh Ethiraj
"""

import requests


def get_list_of_switches():
    
    ''' to get list of switches present in the network'''
    
    url = "http://" + str(controller_ip) + ":8080/stats/switches"
    response = requests.request("GET", url)    
    return (response.text)

def get_desc_of_switch(dpid):
        
    ''' to get the description of selected switch, require datapath id to be 
    passed as input'''
    
    url = "http://" + str(controller_ip) + ":8080/stats/desc/" + str(dpid)    
    response = requests.request("GET", url)    
    return (response.text)

def get_flow_table_of_switch(dpid):
    
    '''to get the flow entries present in the selected switch, require 
    datapath id to be passed as input'''
    
    url = "http://" + str(controller_ip) + ":8080/stats/flow/" + str(dpid) 
    response = requests.request("GET", url).json()
    length = len(response[str(dpid)])
    print("Table_ID" + "               " + "Match Fields" + "                                                     " + "Priority" + "    " + "Action" + "     " + "cookie")
    for i in range (0,length):
        Table_ID=response[str(dpid)][i]["table_id"]
        Priority=response[str(dpid)][i]["priority"]
        Match=response[str(dpid)][i]["match"]
        Action=response[str(dpid)][i]["actions"]
        cookie=response[str(dpid)][i]["cookie"]
        print("       " + str(Table_ID) + "  " + str(Match) + "   " + str(Priority) + "    " + str(Action) + "     " + str(cookie))
    return 

def add_flow_entry(dpid):
    
    '''
    to add a flow entry, requires dpid, match, actions, priority, cookie as input
    '''
    
    url = "http://" + str(controller_ip) + ":8080/stats/flowentry/add"  
    
    #Change the below line to add the desired flow entry
    payload = {"dpid":1,"cookie": 41,"priority": 40000,"match": {"in_port": 2},"actions": []}
    
    headers = {'Content-Type': "application/json"}    
    response = requests.request("POST", url, data=str(payload), headers=headers)    
    return (response)

def delete_flow_entry():
    
    '''to remove a flow entry'''
    
    url = "http://" + str(controller_ip) + ":8080/stats/flowentry/delete_strict" 
                         
    #Change the below line to remove the desired flow entry                         
    payload = {"dpid":1,"cookie": 41,"priority": 40000,"match": {"in_port": 2},"actions": []}
    
    headers = {'Content-Type': "application/json"}    
    response = requests.request("POST", url, data=str(payload), headers=headers)    
    return (response)


controller_ip = input("Enter controller IP: ")
