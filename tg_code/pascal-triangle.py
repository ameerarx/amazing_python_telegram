# Треугольник Паскаля
n = 13
data = [0] * (n + 1)
data[n // 2] = 1
print(data)

while data[0] == 0:
    for i in range(n // 2):
        data[i] += data[i + 1]
    print(str(
        list(
          filter(
              lambda x: x != 0, data
          )
          )
    ).center(n * 3))
