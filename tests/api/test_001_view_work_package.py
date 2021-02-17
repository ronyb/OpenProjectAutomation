import requests
from main_config import config
from requests.auth import HTTPBasicAuth


# https://docs.openproject.org/api/endpoints/work-packages/#work-packages-work-package
# GET /api/v3/work_packages/{id}{?notify}
def test_001_view_work_package():

    basic_auth = HTTPBasicAuth(config['open_project']['basic_auth']['username'], config['open_project']['basic_auth']['password'])

    work_package_id = 38
    expected_work_package_type = "Task"
    expected_work_package_subject = "My Task 1"

    url = f"{config['open_project']['base_url']}/api/v3/work_packages/{work_package_id}"

    response = requests.get(url, auth=basic_auth).json()

    actual_work_package_type = response["_embedded"]["type"]["name"]
    actual_work_package_subject = response["subject"]

    print(f"Response: Work package type = '{actual_work_package_type}'; subject = '{actual_work_package_subject}'")

    assert actual_work_package_subject == expected_work_package_subject, f"Work package subject should be '{expected_work_package_subject}'"
    assert actual_work_package_type == expected_work_package_type, f"Work package type should be '{expected_work_package_type}'"
