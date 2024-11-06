# models.py
import datetime

class User:
    def __init__(self, name, photo_url, birth_date):
        self.name = name
        self.photo_url = photo_url
        self.birth_date = birth_date

class Comment:
    def __init__(self, user_name, comment, published_at):
        self.user_name = user_name
        self.comment = comment
        self.published_at = published_at

class Post:
    def __init__(self, post_photo_url, published_at, content, users, comments):
        self.post_photo_url = post_photo_url
        self.published_at = published_at
        self.content = content
        self.users = users
        self.comments = comments

class Resennia:
    def __init__(self, published_at, content, users):
        self.published_at = published_at
        self.content = content
        self.users = users

class IdType:
    def __init__(self, id, description):
        self.id = id
        self.description = description

class LibroDeReclamaciones:
    def __init__(self, name, last_name, id_type, department, province, phone_number, mail, message):
        self.name = name
        self.last_name = last_name
        self.id_type = id_type
        self.department = department
        self.province = province
        self.phone_number = phone_number
        self.mail = mail
        self.message = message