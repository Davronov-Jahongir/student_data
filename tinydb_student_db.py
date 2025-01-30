from tinydb import TinyDB
import tinydb
db = TinyDB('table.json')

student_data = [{
    "id": 101,
    "name": "Fridman Stefan",
    "age": 17,
    "gender": "Male",
    "contact": "+998(99)172-56-57",
    "grade_level": "Grade 10",
    "subjects": {
        "math": 99,
        "science": 99,
        "english": 29
    },
    "attendance": 92.5,
    "activities": ["ValletBall"],
    "address": {
        "street": "Bagdad 26 St",
        "city": "Samarkand",
        "state": "IL",
        "zip_code": "	140100"
    }
}]
db.insert_multiple(student_data)

print(db.all())
