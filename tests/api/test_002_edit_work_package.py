

from datetime import datetime

from infra.api.work_packages_api import WorkPackagesApi
from main_config import config


def test_002_edit_work_package():

    work_package_id = 38

    work_packages_api = WorkPackagesApi(config['base_url'])
    work_package = work_packages_api.get_work_package(work_package_id)

    new_description = f"Description update time: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"

    payload = {
        "lockVersion": work_package["lockVersion"],
        "_links": {},
        "description": {
                "raw": new_description
            }
        }

    work_package = work_packages_api.edit_work_package(38, payload)

    assert work_package["description"]["raw"] == new_description, f"Description should be: '{new_description}'"
