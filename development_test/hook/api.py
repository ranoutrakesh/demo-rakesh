import frappe
from frappe.auth import LoginManager

@frappe.whitelist(allow_guest=True)
def get_plan_list():
    try:    
        plan_list = frappe.get_list("SAAS Plan", fields=("plan_name", "currency"))
        return plan_list
    except Exception as e:
        return {"msg":"ERROR in SAAS Plan"}          


@frappe.whitelist(allow_guest=True)
def create_subscription(subc={}):
    try:
        subscription = frappe.get_doc({
        "doctype": "SAAS Subscription",
        "customer": subc.get("customer"),
        "date": subc.get("date"),
        "plan": subc.get("plan"),
        "amount":subc.get("amount")
        })
        subscription.insert()
        return{
            "success_key":1,
            "subs":"Subscription created successfully"
        }
    except Exception as e:
        return {"msg":"Error while creating SAAS Subscription"} 
    
@frappe.whitelist(allow_guest=True)
def login_user(password, email=None):
    try:
        login_manager = LoginManager()
        login_manager.authenticate(email, password)
        login_manager.post_login()
        return {
            "Msg":"Login Successfully"
        }
    except Exception as e:
        return {"msg":"Error While Login"}             
    