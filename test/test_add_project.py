import random
import string
from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


# def test_add_project(app):
#     old_projects = app.project.get_list()
#     project = random_string("project_name_", 15)
#     app.project.create(project)
#     new_projects = app.project.get_list()
#     old_projects.append(Project(name=project, id=app.project.find_id_by_name(project)))
#     assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def test_add_project(app, config):
    project = random_string("project_name_", 15)
    old_projects = app.soap.get_project_list(config["web"]["username"], config["web"]["password"], config["web"]["baseURL"])
    app.project.create(project)
    new_projects = app.soap.get_project_list(config["web"]["username"], config["web"]["password"], config["web"]["baseURL"])
    added_project = sorted(new_projects, key=Project.id_or_max)[-1]
    old_projects.append(added_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)