from pytest_bdd import scenarios


from tests.features.steps.login_steps import *
from tests.features.steps.inventory_steps import *

scenarios('features/login.feature')
scenarios('features/inventory.feature')
