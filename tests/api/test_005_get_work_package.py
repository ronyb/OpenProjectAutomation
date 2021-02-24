from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def test_005_get_work_package():

    work_package_id = 38
    expected_work_package_type = "Task"
    expected_work_package_subject = "My Task 1"

    work_packages_api = WorkPackagesApi(config['base_url'])
    work_package = work_packages_api.get_work_package(work_package_id)

    actual_work_package_type = work_package["_embedded"]["type"]["name"]
    actual_work_package_subject = work_package["subject"]

    assert actual_work_package_subject == expected_work_package_subject, f"Work package subject should be '{expected_work_package_subject}'"
    assert actual_work_package_type == expected_work_package_type, f"Work package type should be '{expected_work_package_type}'"
