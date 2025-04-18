import pickle
import os
import logging
from flask import current_app

logger = logging.getLogger(__name__)
_model = None


def get_model():
    """
    Singleton pattern to load and cache the ML model
    Returns the model instance or None if loading fails
    """
    global _model

    if _model is not None:
        return _model

    try:
        model_path = current_app.config['MODEL_PATH']
        with open(model_path, 'rb') as model_file:
            _model = pickle.load(model_file)
        logger.info(f"Model loaded successfully from {model_path}")
        return _model
    except Exception as e:
        logger.error(f"Failed to load model: {str(e)}")
        return None