from datetime import datetime

from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def test_007_create_work_package():

    work_packages_api = WorkPackagesApi(config['base_url'])

    new_work_package_subject = f"Auto Task {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

    payload = {
        "subject": new_work_package_subject,
        "startDate": datetime.now().strftime('%Y-%m-%d'),
        "_links": {
            "project": {
                "href": f"/api/v3/projects/{config['project_id']}",
                "title": config['project_name']
            },
            "type": {"href": "/api/v3/types/1", "title": "Task"},
            "assignee": {"href": None},
        }
    }

    work_package = work_packages_api.create_work_package(payload)

    assert work_package["subject"] == new_work_package_subject, f"New work package subject should be '{new_work_package_subject}'"
