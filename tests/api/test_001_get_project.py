from infra.api.projects_api import ProjectsApi
from main_config import config


def test_001_get_project():

    projects_api = ProjectsApi(config['base_url'])

    project_id = config['project_id']
    expected_project_name = "TestProject1"
    expected_project_description = "This is the first test project"

    project = projects_api.get_project(project_id)

    assert project["name"] == expected_project_name, f"Project name should be '{expected_project_name}'"
    assert project["description"]["raw"] == expected_project_description, f"Project description should be '{expected_project_description}'"
