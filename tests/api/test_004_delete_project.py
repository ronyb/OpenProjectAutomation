import time
from datetime import datetime

from infra.api.projects_api import ProjectsApi
from main_config import config


def test_004_delete_project():

    projects_api = ProjectsApi(config['base_url'])

    # Step 1 - Create a new project
    new_project_name = f"Auto Project {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
    new_project_identifier = f"autoproj{datetime.now().strftime('%Y%m%d%H%M%S')}"

    payload = {
        "name": new_project_name,
        "identifier": new_project_identifier,
        "status": "on track"
    }

    project = projects_api.create_project(payload)
    new_project_id = project["id"]

    # Step 2 - Delete the newly created project
    projects_api.delete_project(new_project_id)

    # Step 3 - Verify respose 404 when trying to get the deleted project
    print("Sleep 5 seconds before validating deletion")
    time.sleep(5)
    projects_api.get_project(new_project_id, expected_response_status_code=404)
