from flask import Flask, Blueprint
from flask_restplus import Api, Resource
from waitress import serve

app = Flask(__name__)
rpApi = Api(app=app, version='1.0', title='My Blog API',
          description='A simple demonstration of a Flask RestPlus powered API')

@rpApi.route("/hello")
class RestPlusDemo(Resource):
    def get(self):  # Create GET endpoint
        return {'hello': 'world'}


ns_category = rpApi.namespace('blog/categories', description='Operations related to blog categories')
@ns_category.route('/')
class CategoryCollection(Resource):
    def get(self):
        """Returns list of blog categories."""
        return {'category': 'AAA'}

    @rpApi.response(201, 'Category successfully created.')
    def post(self):
        """Creates a new blog category."""
        return None, 201

rpApi.add_namespace(ns_category)
serve(app)
