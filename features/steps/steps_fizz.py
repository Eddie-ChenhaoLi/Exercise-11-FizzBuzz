from behave import *
from demo import *


@Given('I have a positive integer {i:d}')
def step_impl(context, i):
    #TODO