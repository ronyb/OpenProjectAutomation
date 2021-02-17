from http import HTTPStatus

from infra.api.rest_client import RestClient


# https://docs.openproject.org/api/endpoints/work-packages
class WorkPackagesApi(RestClient):

    def __init__(self, base_url):
        super().__init__(base_url)

    # GET /api/v3/work_packages/{id}
    def get_work_package(self, work_package_id, expected_response_status_code: int = HTTPStatus.OK):
        response = self.get(path=f"/api/v3/work_packages/{work_package_id}", expected_response_status_code=expected_response_status_code)
        return response.json()

    # PATCH /api/v3/work_packages/{id}
    def edit_work_package(self, work_package_id, payload):
        response = self.patch(path=f"/api/v3/work_packages/{work_package_id}", payload=payload)
        return response.json()

    # POST /api/v3/work_packages
    def create_work_package(self, payload):
        response = self.post(path=f"/api/v3/work_packages", payload=payload, expected_response_status_code=201)
        return response.json()

    # DELETE /api/v3/work_packages/{id}
    def delete_work_package(self, work_package_id):
        response = self.delete(path=f"/api/v3/work_packages/{work_package_id}", expected_response_status_code=204)
