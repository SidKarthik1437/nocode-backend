import operator


# idx = {
#     'basicArithmetic': [[i for i in dir(globals()['basicArithmetic']()) if '__' not in i]]
# }

idx = ['basicArithmetic']


def generate_index(module_name):
    return [i for i in dir(globals()[module_name]())
            if not i.startswith('__')]


def fetch(type):
    for cls in idx:
        if type in generate_index(cls):
            return getattr(globals()[cls](), type)


class basicArithmetic():
    def add(self, inputs):
        return operator.add(*inputs)

    def sub(self, *inputs):
        return operator.sub(*inputs)

    def mul(self, *inputs):
        return operator.mul(*inputs)

    def div(self, *inputs):
        return operator.truediv(*inputs)
