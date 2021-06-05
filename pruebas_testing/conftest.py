import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, ProductFactory

from django.contrib.auth.models import User

""" Cuando tengo que usar fixtures con varias pruebas, 
tengo que crear un nuevo archivo llamado: conftest.py  
ahi voy a meter los fixtures y pytest me lo va a reconocer
automaticamente."""
# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     print('create-user')
#     return user

# Factory
# @pytest.fixture()
# def new_user_factory(db):
#     def create_app_user(
#         username: str,
#         password: str = None,
#         first_name: str = "firstname",
#         last_name: str = "lastname",
#         email: str = "test@test.com",
#         is_staff: str = False,
#         is_superuser: str = False,
#         is_active: str = True,
#     ):
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active,
#         )
#         return user
#     return create_app_user

# @pytest.fixture
# def new_user(db, new_user_factory):
#     return new_user_factory("Test_user","password","MyName")

# @pytest.fixture
# def new_user2(db, new_user_factory):
#     return new_user_factory("Test_user","password", "MyName", is_staff="True")

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)