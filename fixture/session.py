class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_xpath("//input[@value='Войти']").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Войти']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//a[contains(@href, '#')])[2]").click()
        wd.find_element_by_xpath("//a[contains(@href, '/logout_page.php')]").click()
        wd.find_element_by_name("username")

    def is_logged_in(self):
        wd = self.app.wd
        n = wd.find_elements_by_xpath("(//a[contains(@href, '#')])[2]")
        return len(n) > 0

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_css_selector("span.user-info").text

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)