from datetime import datetime

from infra.api.projects_api import ProjectsApi
from main_config import config


def test_002_update_project():

    projects_api = ProjectsApi(config['base_url'])

    project_id = config['project_id']
    new_description = f"Description update time: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

    payload = {
        "_links": {},
        "description": {
            "raw": new_description
        }
    }

    project = projects_api.update_project(project_id, payload)

    assert project["description"]["raw"] == new_description, f"New project description should be: {new_description}"

