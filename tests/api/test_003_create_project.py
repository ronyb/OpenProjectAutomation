from datetime import datetime

from infra.api.projects_api import ProjectsApi
from main_config import config


def test_003_create_project():

    projects_api = ProjectsApi(config['base_url'])

    new_project_name = f"Auto Project {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    new_project_identifier = f"autoproj{datetime.now().strftime('%Y%m%d%H%M%S')}"

    payload = {
        "name": new_project_name,
        "identifier": new_project_identifier,
        "status": "on track"
    }

    project = projects_api.create_project(payload)

    assert project["name"] == new_project_name, f"New project name should be '{new_project_name}'"
    assert project["identifier"] == new_project_identifier, f"New project identifier should be '{new_project_identifier}'"
