import logging
import json
from flask import request
from airflow.api_connexion import security
from airflow.utils.session import NEW_SESSION, provide_session
from airflow.www.app import csrf
from airflow_xtended_api.api.app import blueprint
from airflow_xtended_api.api.response import ApiResponse

@blueprint.route("/sem/inference", methods=["POST"])
@csrf.exempt
@provide_session
@security.requires_access_dag("GET")
def run_inference(session=NEW_SESSION):
    """Perform inference and return dummy data

    args:
        model_id: ID of the model to use for inference
        data: Data to perform inference on
    """
    logging.info("Executing custom 'run_inference' function")

    # Get parameters from request
    model_id = request.form.get("model_id")
    if model_id is None:
        return ApiResponse.bad_request("Model ID is required")

    data = request.form.get("data")
    if data is None:
        return ApiResponse.bad_request("Data is required")

    model_id = model_id.strip()
    data = data.strip()

    # Check if the model exists (dummy check for this example)
    if model_id not in ["model1", "model2"]:
        return ApiResponse.bad_request("The Model ID '" + str(model_id) + "' does not exist")

    # Perform dummy inference
    dummy_result = {
        "model_id": model_id,
        "input_data": data,
        "prediction": "dummy_prediction"
    }

    return ApiResponse.success(dummy_result)
