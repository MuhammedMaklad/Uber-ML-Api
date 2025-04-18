
from flask import Blueprint, request, jsonify
from flask import render_template, abort
import logging

router = Blueprint('main', __name__)


@router.route('/', methods=['GET'])
def index():
    return jsonify({
        'message':"Muhammed on do code"
    }), 200

@router.errorhandler(404)
def page_not_found(error):
    return jsonify({
        'message':"Page not found",
    }), 404