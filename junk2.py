
dispatch = {}

def identity(x):
    'Higher-order'
    return
dispatch = {}

def identity(x):
    'Higher-order'
    return

    def register(func):
        'Higher-order'f register(func):
    'Higher-order'
    dispatch[func.__name__] = func
    return func

def run_vm(x):
    program = raw_input('Enter a program: ')
    print x,
    for command in program.split():
        x = dispatch[command](x)
        print '-->', x