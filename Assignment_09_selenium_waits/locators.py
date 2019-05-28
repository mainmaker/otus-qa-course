from selenium.webdriver.common.by import By


class AdminLocators(object):
    USERNAME = (By.ID, "input-username")
    PASSWORD = (By.ID, "input-password")
    USERNAME3 = (By.CSS_SELECTOR, "#input-username")

class DashboardLocators(object):
	SUCCESS = (By.CSS_SELECTOR, "div.alert.alert-success.alert-dismissible")
	LOGOUT = (By.CSS_SELECTOR, "i.fa.fa-sign-out")
	PENCIL = (By.CSS_SELECTOR, "i.fa.fa-pencil")
	SAVE = (By.CSS_SELECTOR, "i.fa.fa-save")
	SELECTED = (By.NAME, "selected[]")
	TRASH = (By.CSS_SELECTOR, "i.fa.fa-trash-o")
	INPUT_NAME1 = (By.ID, "input-name1")
	PLUS = (By.CSS_SELECTOR, "i.fa.fa-plus")
	INPUT_META_TITLE1 = (By.ID, "input-meta-title1")
	INPUT_MODEL = (By.ID, "input-model")
	A_PARENT_COLLAPSED = (By.CSS_SELECTOR, "a.parent.collapsed")
	A_TAG = (By.TAG_NAME, "a")
	TR_TAG = (By.TAG_NAME, "tr")
	TD_TAG = (By.TAG_NAME, "td")
	PAGINATION = (By.CSS_SELECTOR, "ul.pagination")

