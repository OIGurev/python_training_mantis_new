import random
import string
from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    old_projects = app.project.get_list()
    project = random_string("project_name_", 15)
    app.project.create(project)
    new_projects = app.project.get_list()
    old_projects.append(Project(name=project, id=app.project.find_id_by_name(project)))
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)