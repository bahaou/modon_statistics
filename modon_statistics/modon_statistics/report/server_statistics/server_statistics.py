# Copyright (c) 2022, baha and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns=get_columns(filters)
	data=get_data(filters)
	return columns, data



def get_data(filters):
	servers=frappe.db.get_list("Server Statistics",fields=["*"])
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
			"label": _("Erpnext Version"),
			"fieldname": "erpnext_version",
			"fieldtype": "Data",
			"width": 145,
		},
		{
			"label": _("Users"),
			"fieldname": "total_users",
			"fieldtype": "Int",
			"width": 100,
		},
		{
			"label": _("Active Users Last Month"),
			"fieldname": "active_users_last_month",
			"fieldtype": "Int",
			"width": 100,
		},
		{
			"label": _("Sales Invoices"),
			"fieldname": "total_sales_invoices",
			"fieldtype": "Int",
			"width": 100,
		},
		{
			"label": _("Sales Invoices Last Month"),
			"fieldname": "sales_invoices_last_month",
			"fieldtype": "Int",
			"width": 100,
		},
		{
			"label": _("Purchase Invoices"),
			"fieldname": "total_purchase_invoices",
			"fieldtype": "Int",
			"width": 100,
		},
		{
			"label": _("Purchase Invoices Last Month"),
			"fieldname": "purchase_invoices_last_month",
			"fieldtype": "Int",
			"width": 100,
		},
		{
			"label": _("Work Orders"),
			"fieldname": "total_work_orders",
			"fieldtype": "Int",
			"width": 100,
		},
		{
			"label": _("Work Orders Last Month"),
			"fieldname": "work_orders_last_month",
			"fieldtype": "Int",
			"width": 101,
		}

	]
	return(columns)
