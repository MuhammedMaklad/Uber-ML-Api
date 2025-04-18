from flask import request, jsonify
import numpy as np
from app.api import main_blueprint
from app.models.ml_model import get_model
import logging

logger = logging.getLogger(__name__)


@main_blueprint.route('/', methods=['GET'])
def index():
    """Root endpoint returning a simple status message"""
    return jsonify({
        'message': "API is running"
    }), 200


@main_blueprint.route('/predict', methods=['POST'])
def predict():
    """Endpoint for making predictions based on input data"""
    model = get_model()
    if not model:
        logger.error("Prediction attempted but model is not loaded")
        return jsonify({
            'message': "Model not available",
            'error': "Server configuration error"
        }), 500

    try:
        # Check if form data exists
        if not request.form or len(request.form) == 0:
            logger.warning("Prediction request missing form values")
            return jsonify({
                'message': "Missing values",
                'error': "No form data provided"
            }), 400

        # Log incoming data
        logger.info(f"Received prediction request with data: {dict(request.form)}")

        # Convert form values to integers
        try:
            int_features = [int(x) for x in request.form.values()]
        except ValueError:
            logger.warning("Invalid input: non-integer values provided")
            return jsonify({
                'message': "Invalid input",
                'error': "All values must be integers"
            }), 400

        # Make prediction
        final_features = [np.array(int_features)]
        prediction = model.predict(final_features)
        output = round(prediction[0])

        logger.info(f"Prediction successful: {output}")

        return jsonify({
            "message": "Operation completed successfully",
            "prediction": output
        }), 200

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({
            'message': "Prediction failed",
            'error': str(e)
        }), 500