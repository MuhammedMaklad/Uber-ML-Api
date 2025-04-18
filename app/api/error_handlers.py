from flask import jsonify, request
from app.api import main_blueprint
import logging

logger = logging.getLogger(__name__)

@main_blueprint.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors"""
    logger.warning(f"404 error: {request.path}")
    return jsonify({
        'message': "Page not found",
        'error': str(error)
    }), 404

@main_blueprint.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    logger.error(f"500 error: {str(error)}")
    return jsonify({
        'message': "Internal server error",
        'error': str(error)
    }), 500

@main_blueprint.errorhandler(400)
def bad_request(error):
    """Handle 400 errors"""
    logger.warning(f"400 error: {str(error)}")
    return jsonify({
        'message': "Bad request",
        'error': str(error)
    }), 400