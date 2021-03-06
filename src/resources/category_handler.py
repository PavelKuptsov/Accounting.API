from flask import request, jsonify
from flask_restful import abort

from config import auth
from resources.base_handler import BaseHandler


class CategoryHandler(BaseHandler):

    @auth.login_required
    def get(self, category_id):
        category = self.repository.categories.category_get(category_id)
        return jsonify(category)

    @auth.login_required
    def put(self, category_id):
        parent_category_id = request.get_json().get('parent_category_id')
        name = request.get_json().get('name')

        parent_category = self.repository.categories.category_get(parent_category_id)
        category = self.repository.categories.category_get(category_id)
        if category.type_id != parent_category.type_id:
            abort(400, error='You cannot change type of category')
        result = self.repository.categories.category_change(category_id, name, parent_category_id)
        return result

    @auth.login_required
    def delete(self, category_id):
        transactions = self.repository.transactions.transactions_search_by_category_id(category_id)
        if transactions:
            abort(400, error='Cannot delete category which has transactions')
        result = self.repository.categories.category_delete(category_id)
        return result
