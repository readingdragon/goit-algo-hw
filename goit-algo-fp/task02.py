# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

import turtle

def initialize_turtle():
    ttl = turtle.Turtle()
    ttl.speed(0)
    ttl.left(90)
    ttl.up()
    ttl.backward(200)
    ttl.down()
    return ttl

def draw_tree(ttl, branch_length, angle, level, color):
    if level == 0 or branch_length < 1:
        return
    ttl.color(color)
    ttl.forward(branch_length)
    ttl.left(angle)

    next_color = (color[0] * 1, color[1] * 0.9, color[2] * 0.8)
    draw_tree(ttl, branch_length * 0.7, angle, level - 1, next_color)

    ttl.right(2 * angle)
    draw_tree(ttl, branch_length * 0.7, angle, level - 1, next_color)

    ttl.left(angle)
    ttl.backward(branch_length)


def main():
    screen = turtle.Screen()
    screen.bgcolor("#333333")

    ttl = initialize_turtle()
    level = int(input("Введіть рівень рекурсії: "))

    start_color = (1.0, 1.0, 0.0)
    screen.colormode(1.0)
    
    draw_tree(ttl, 100, 30, level, start_color)
    screen.exitonclick()


if __name__ == "__main__":
    main()