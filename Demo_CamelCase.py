import camelcase
from camelcase import CamelCase

c = camelcase.CamelCase()
text = "'it's camelcase demo using external package in python"
print(c.hump(text))