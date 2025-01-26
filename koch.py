import turtle


def koch_snowflake(length, level):
    if level == 0:
        turtle.forward(length)
        return
    length /= 3.0
    koch_snowflake(length, level - 1)
    turtle.left(60)
    koch_snowflake(length, level - 1)
    turtle.right(120)
    koch_snowflake(length, level - 1)
    turtle.left(60)
    koch_snowflake(length, level - 1)


def draw_snowflake(length, level):
    for _ in range(3):
        koch_snowflake(length, level)
        turtle.right(120)


if __name__ == "__main__":
    length = float(input("Length of the side: "))
    level = int(input("Recursion level: "))
    turtle.speed(0)
    draw_snowflake(length, level)
    turtle.done()
