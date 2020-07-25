from behave import *
from demo import *


@Given('I have a positive integer {i:d}')
def step_impl(context, i):
    context.i = i


@When('the integer is a multiple of 5 or contains 5 {b:d}')
def step_impl(context, b):
    context.b = buzz(context.i)
    assert context.b == b


@Then('I should print Buzz')
def step_impl(context):
    pass
