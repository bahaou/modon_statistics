# Copyright (c) 2022, baha and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns=get_columns(filters)
	data=get_data(filters)
	return columns, data

def get_data(filters):
	servers=frappe.db.get_list("Server",fields=["*"])
	data=[]
	for s in servers:
		link="<a href='"+s["url"]+"'>"+s["name"]+"</a>"
		s["name1"]=link
		link="<a href='"+s["rdp"]+"'>rdp</a>"
		s["rdp1"]=link
		data.append(s)
	return(data)

def get_columns(filters):
	columns=[
		{
			"label": _("Server"),
			"fieldname": "name1",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("rdp"),
			"fieldname": "rdp1",
			"fieldtype": "Data",
			"width": 50,
		},
		{
			"label": _("Owner"),
			"fieldname": "customer",
			"fieldtype": "Data",
			"width": 170,
		},
		{
			"label": _("Email"),
			"fieldname": "email",
			"fieldtype": "Data",
			"width": 180,
		},
		{
			"label": _("Mobile"),
			"fieldname": "mobile",
			"fieldtype": "Data",
			"width": 150,
		},
		{
			"label": _("Contract Ends"),
			"fieldname": "contract_ends",
			"fieldtype": "Date",
			"width": 150,
		}
		
		]
	return columns
