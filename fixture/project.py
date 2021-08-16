from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def go_to_manage_projects_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(
                wd.find_elements_by_xpath("//button[@type='submit']")) > 0):
            wd.find_element_by_css_selector("i.menu-icon.fa.fa-gears").click()
            wd.find_element_by_link_text(u"Manage Projects").click()

    def return_to_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and len(
                wd.find_elements_by_by_xpath("//button[@type='submit']")) > 0):
            wd.find_element_by_css_selector("i.menu-icon.fa.fa-gears").click()
            wd.find_element_by_link_text(u"Manage Projects").click()

    def fill_project_form(self, project):
        self.change_field_value("name", project)
        #self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, project):
        wd = self.app.wd
        self.go_to_manage_projects_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath(u"//input[@value='Add Project']").click()
        self.return_to_project_page()
        self.project_cache = None

    def delete(self, project_id):
        wd = self.app.wd
        self.go_to_manage_projects_page()
        self.find_name_by_id(project_id)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None



    project_cache = None


    def get_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.go_to_manage_projects_page()
            self.project_cache = []
            for element in wd.find_elements_by_xpath("//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"):
                name = element.find_element_by_css_selector("td:nth-child(1)").text
                id_not_fetched = element.find_element_by_css_selector('a[href ^= "manage_proj_edit_page.php?project_id="]').get_attribute("href")
                id = id_not_fetched.replace("http://localhost/mantisbt-2.24.4/manage_proj_edit_page.php?project_id=", "")
                description = element.find_element_by_css_selector("td:nth-child(5)").text
                self.project_cache.append(Project(name=name, description=description, id=id))
        return list(self.project_cache)

    def find_id_by_name(self, project):
        wd = self.app.wd
        rows = wd.find_elements_by_xpath(
            "//tr[contains(@class, 'row-')][not(contains(@class, 'category'))][not(ancestor::a)]")
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].find_element_by_tag_name("a").text
            id = cells[0].find_element_by_tag_name("a").get_attribute("href").split("=", 1)[1]
            if name == project:
                return id

    def find_name_by_id(self, project_id):
        wd = self.app.wd
        wd.find_element_by_css_selector('a[href ^= "manage_proj_edit_page.php?project_id='+str(project_id)+'"]').click()