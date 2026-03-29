from pytest_bdd import scenarios


from tests.features.steps.login_steps import *
from tests.features.steps.inventory_steps import *
from tests.features.steps.cart_steps import *
from tests.features.steps.payment_steps import *

scenarios('features/login.feature')
scenarios('features/inventory.feature')
scenarios('features/checkout.feature')