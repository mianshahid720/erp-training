# Copyright (c) 2023, shahid and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):
    def validate(self):
        # my_value = frappe.db.get_value('Nextash Users', self.nextash_user, ["gender", "designation"], as_dict = 1)
        # frappe.msgprint(f"{my_value}")
        
        # my_value = frappe.db.set_value('Nextash Users', self.nextash_user, {'gender': 'Male', 'designation':'Developer'})
        # my_value = frappe.db.count('Nextash Users', {"designation": "Developer"})
        data = frappe.db.sql("""
    SELECT
        name,designation
    FROM `tabNextash Users`
""", as_dict=1)
        # my_doc = frappe.get_doc("Nextash Users", "Tania")
        # my_doc.db_set('designation', "Shahid")
        frappe.msgprint(f"{data}")

        # self.members = []
        # # doc = frappe.get_doc("Nextash Users", self.nextash_user)
        # # frappe.msgprint(f"{doc.designation}")
        # docs = frappe.db.get_list("Nextash Users", filters={'gender': 'Male'}, fields = ['name','designation'], order_by= 'name asc',page_length=2)
        # frappe.msgprint(f"{docs}")
        
		
		
		
		
		# for row in docs:
        #     # frappe.msgprint(f"{row}")
        #     doc = frappe.get_doc('Nextash Users', row.name)
        #     frappe.msgprint(f"{doc.designation}")
        #     self.append("members",{
        #         "member_name": doc.name,
        #         "relation": doc.designation
		# 	})
