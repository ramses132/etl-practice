import bonobo

def generate_data():
    yield 'HoLa'
    yield 'MOndo'
    yield 'eTl'

def uppercase(x: str):
    return x.upper()

def output(x: str):
    print(x)

graph = bonobo.Graph(
        generate_data,
        uppercase,
        output
        )

if __name__ == '__main__':
    bonobo.run(graph)

