from http import HTTPStatus

from infra.api.rest_client import RestClient


# https://docs.openproject.org/api/endpoints/projects/
class ProjectsApi(RestClient):

    def __init__(self, base_url):
        super().__init__(base_url)

    # GET /api/v3/projects/{id}
    def get_project(self, project_id, expected_response_status_code: int = HTTPStatus.OK):
        response = self.get(path=f"/api/v3/projects/{project_id}", expected_response_status_code=expected_response_status_code)
        return response.json()

    # POST /api/v3/projects
    def create_project(self, payload):
        response = self.post(path=f"/api/v3/projects", payload=payload, expected_response_status_code=201)
        return response.json()

    # PATCH /api/v3/projects/{id}
    def update_project(self, project_id, payload):
        response = self.patch(path=f"/api/v3/projects/{project_id}", payload=payload)
        return response.json()

    # DELETE /api/v3/projects/{id}
    def delete_project(self, project_id):
        response = self.delete(path=f"/api/v3/projects/{project_id}", expected_response_status_code=204)