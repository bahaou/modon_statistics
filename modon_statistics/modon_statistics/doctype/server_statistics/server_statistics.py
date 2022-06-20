# Copyright (c) 2022, baha and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import requests
from frappe.utils.password import get_decrypted_password
from datetime import date
class ServerStatistics(Document):
	pass



@frappe.whitelist()
def sync(server=None):
	today=date.today()
	last_month=frappe.utils.add_to_date(today,months=-1)
	last_month=last_month.strftime("%Y-%m-%d")
	today=today.strftime("%Y-%m-%d")
	if server:
		servers=[{"name":server}]
	else:
		servers=frappe.db.get_list("Server")
	for s in servers:
		print(s)
		s=s["name"]
		if frappe.db.exists("Server Statistics",s):
			doc=frappe.get_doc("Server Statistics",s)
		else:
			doc=frappe.new_doc("Server Statistics")
			doc.server=s
		
		doc_url=str(frappe.db.get_value("Server",s,"url"))
		doc.url=doc_url
		doc_url=doc_url.replace("https","http")
		if not 'http' in doc_url:
			doc_url='http://'+doc_url
		api_key = str(frappe.db.get_value("Server",s,"api_key")).replace(" ","")
		api_secret=str(get_decrypted_password("Server",s,"api_secret")).replace(" ","")
		headers =   { 'Authorization': "token "+api_key+":"+api_secret }

		url = doc_url+"/api/resource/Activity Log?filters=[[\"creation\",\">\",\""+today+"\"]]&limit_page_length=0"
		response = requests.request("Post", url, headers=headers)
		today_activity=len(response.json()["data"])
		doc.activity_today=today_activity
		#version and apps
		url = doc_url+"/api/method/frappe.utils.change_log.get_versions"
		response = requests.request("Post", url, headers=headers)
		apps=""
		try:
			doc.erpnext_version=response.json()["message"]["erpnext"]["version"] + " (" +  response.json()["message"]["erpnext"]["branch"] + ")"
		except:
			pass
		try:
			app_list=response.json()["message"]
			app_list_names=list(app_list.keys())
			for app in app_list:
				apps+=app+" ("+app_list[app]["version"]+") "
			dpc.installed_apps=apps
		except:
			pass
		#active users
		url = doc_url+"/api/resource/User?limit_page_length=0&filters=[[\"enabled\",\"=\",\"1\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.total_users=len(response.json()["data"])
		#active users last month
		url = doc_url+"/api/resource/User?limit_page_length=0&filters=[[\"enabled\",\"=\",\"1\"],[\"last_active\",\">\",\""+last_month+"\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.active_users_last_month=len(response.json()["data"])	
		#sales invoices	
		url = doc_url+"/api/resource/Sales Invoice?limit_page_length=0&filters=[[\"docstatus\",\"=\",\"1\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.total_sales_invoices=len(response.json()["data"])
  		#sales invoices	last month
		url = doc_url+"/api/resource/Sales Invoice?limit_page_length=0&filters=[[\"docstatus\",\"=\",\"1\"],[\"modified\",\">\",\""+last_month+"\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.sales_invoices_last_month=len(response.json()["data"])
		#purchase invoices
		url = doc_url+"/api/resource/Purchase Invoice?limit_page_length=0&filters=[[\"docstatus\",\"=\",\"1\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.total_purchase_invoices=len(response.json()["data"])
		#purchase invoices last month
		url = doc_url+"/api/resource/Purchase Invoice?limit_page_length=0&filters=[[\"docstatus\",\"=\",\"1\"],[\"modified\",\">\",\""+last_month+"\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.purchase_invoices_last_month=len(response.json()["data"])
		#work orders
		url = doc_url+"/api/resource/Work Order?limit_page_length=0&filters=[[\"docstatus\",\"=\",\"1\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.total_work_orders=len(response.json()["data"])
		#work orders last month
		url = doc_url+"/api/resource/Work Order?limit_page_length=0&filters=[[\"docstatus\",\"=\",\"1\"],[\"modified\",\">\",\""+last_month+"\"]]"
		response = requests.request("Post", url, headers=headers)
		doc.work_orders_last_month=len(response.json()["data"])

		doc.save()
	frappe.db.commit()


