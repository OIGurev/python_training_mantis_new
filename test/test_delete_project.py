import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def check_empty_filling(app):
    if len(app.project.get_list()) == 0:
        app.project.create(random_string("project_name_", 15))


def test_del_project(app):
    check_empty_filling(app)
    old_projects = app.project.get_list()
    random_project = random.choice(old_projects)
    app.project.delete(random_project.id)
    new_projects = app.project.get_list()
    old_projects.remove(random_project)
    assert old_projects == new_projects
