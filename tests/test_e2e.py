from pytest_bdd import scenarios


from tests.steps.login_steps import *
from tests.steps.inventory_steps import *

scenarios('features/login.feature')
scenarios('features/inventory.feature')
