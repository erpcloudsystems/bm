from __future__ import unicode_literals
import frappe
from frappe import _
import random
frappe.whitelist()
def daily():
    # update doc owner and modified_by with random user from user_list
    user_list = frappe.db.sql("""select name from tabUser where name not in ('Administrator','Guest','bm@bm.com')""")
    list_of_docs = ["Sales Order","Delivery Note","Sales Invoice","Purchase Order"
                ,"Purchase Receipt","Purchase Invoice","Journal Entry","Payment Entry"]
    for doc in list_of_docs:
        docs = frappe.get_all(doc, fields=['name'], filters={'owner': 'bm@bm.com'})
        for d in docs:
            random_user = random.choice(user_list)
            frappe.db.sql("""update `tab{0}` set owner = '{1}', 
                            modified_by = '{1}' where name = '{2}'""".format(doc,random_user[0],d.name))