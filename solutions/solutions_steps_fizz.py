from behave import *
from demo import *


@Given('I have a positive integer {i:d}')
def step_impl(context, i):
    context.i = i


@When('the integer is a multiple of 3 or contains 3 {b:d}')
def step_impl(context, b):
    context.b = fizz(context.i)
    assert context.b == b


@Then('I should print Fizz')
def step_impl(context):
    pass
