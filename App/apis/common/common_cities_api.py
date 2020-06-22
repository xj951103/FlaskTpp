from flask_restful import Resource, fields, marshal
from App.models.common.common_cities_model import City, Letter
from App.apis.api_constant import HTTP_SUCCESS

city_fields = {
    "id": fields.Integer(attribute="c_id"),
    "parentId": fields.Integer(attribute="c_parent_id"),
    "regionName": fields.String(attribute="c_region_name"),
    "cityCode": fields.Integer(attribute="c_city_code"),
    "pinYin": fields.String(attribute="c_pinyin"),
}


class CitiesResource(Resource):
    def get(self):
        letters_cities = {}
        letters = Letter.query.all()
        letters_cities_fields = {}
        for letter in letters:
            letter_cities = City.query.filter_by(letter_id=letter.id)
            letters_cities[letter.letter] = letter_cities
            letters_cities_fields[letter.letter] = fields.List(fields.Nested(city_fields))

        data = {
            "msg": "Get Success",
            "status": HTTP_SUCCESS,
            "data": marshal(letters_cities, letters_cities_fields)
        }

        return data
