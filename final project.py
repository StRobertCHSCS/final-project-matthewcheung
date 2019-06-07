import arcade


WIDTH = 800
HEIGHT = 600

# Starting position
player_x = 25
player_y = 25

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

# Gravity variables
velocity = 0
gravity = 0.2
on_plat = False
jumping = False


def on_update(delta_time):
    global up_pressed, down_pressed, right_pressed, left_pressed, player_x, player_y, velocity, gravity
    if down_pressed:
        player_y -= 5
    if right_pressed:
        player_x += 5
    if left_pressed:
        player_x -= 5
    '''
    # Gravity
    if up_pressed:
        velocity += gravity
        player_y -= velocity
    '''

    jumped()
    platforms()
    end_goal()


def platforms():
    global player_x, player_y, on_plat

    # Stops player from leaving the screen
    if player_y + 1 >= 575:
        player_y = 575
    if player_y - 1 <= 25:
        player_y = 25
        on_plat = True
    else:
        on_plat = False

    if player_x - 1 <= 25:
        player_x = 25
    if player_x + 1 >= 775:
        player_x = 775

    # Platform collisions
    # Platform 3 Y collisions
    if (530 <= player_x <= 670 and 270 <= player_y <= 300) and player_y + 1 >= 270:
        player_y = 270
    if (530 <= player_x <= 670 and 300 <= player_y <= 330) and player_y - 1 <= 330:
        player_y = 330
        on_plat = True

    # Platform 3 X collisions
    if (530 <= player_x <= 670 and 270 <= player_y <= 330) and player_x + 1 <= 480:
        player_x = 480
    if (530 <= player_x <= 670 and 270 <= player_y <= 330) and player_x - 1 >= 720:
        player_x = 720

    # Platform 2 Y collisions
    if (305 <= player_x <= 495 and 170 <= player_y <= 200) and player_y + 1 >= 170:
        player_y = 170
    if (305 <= player_x <= 495 and 200 <= player_y <= 230) and player_y - 1 <= 230:
        player_y = 230
        on_plat = True

    # Platform 2 X collisions
    if (305 <= player_x <= 495 and 170 <= player_y <= 230) and player_x + 1 <= 280:
        player_x = 280
    if (305 <= player_x <= 495 and 170 <= player_y <= 230) and player_x - 1 >= 520:
        player_x = 520
    '''
    # Platform 1 Y collisions
    if (80 <= player_x <= 320 and 70 <= player_y <= 100) and player_y + 1 >= 70:
        player_y = 70
    if (80 <= player_x <= 320 and 100 <= player_y <= 130) and player_y - 1 <= 130:
        player_y = 130
        on_plat = True

    # Platform 1 X collisions
    if (80 <= player_x <= 320 and 70 <= player_y <= 130) and player_x + 1 <= 80:
        player_x = 80
    if (80 <= player_x <= 320 and 70 <= player_y <= 130) and player_x - 1 >= 320:
        player_x = 320
    '''

'''
for i in range(len(amount_of_plats):
    if (left_edge <= player_x <= right_edge and bottom_plat <= player_y <= top_plat) and player_y + 1 >= bottom_plat:
        player_y = bottom_plat
'''


def platform_collisions(x, y):
    global player_y, player_x, on_plat

    # Platform 1 Y collisions
    if (x <= player_x <= x + 240 and y <= player_y <= y + 30) and player_y + 1 >= y:
        player_y = y
    if (x <= player_x <= x + 240 and y + 30 <= player_y <= y + 60) and player_y - 1 <= y + 60:
        player_y = y + 60
        on_plat = True

    # Platform 1 X collisions
    if (x <= player_x <= x + 240 and y <= player_y <= y + 60) and player_x + 1 <= x:
        player_x = x
    if (x <= player_x <= x + 240 and y <= player_y <= y + 60) and player_x - 1 >= x + 240:
        player_x = x + 240


def jumped():
    global on_plat, velocity, player_y, jumping

    if up_pressed:
        jumping = True

    if jumping:
        player_y += 8
        velocity += gravity
        player_y -= velocity
        if velocity >= 20:
            velocity = 20

    if on_plat:
        velocity = 0
        jumping = False

    if not on_plat and not jumping:
        velocity += 0.3
        velocity += gravity
        player_y -= velocity
        if velocity >= 20:
            velocity = 20


def end_goal():
    if (594 <= player_x <= 656) and (305 <= player_y <= 430):
        print("you win!")


def on_draw():
    global player_x, player_y
    arcade.start_render()

    # Platforms
    arcade.draw_rectangle_filled(600, 300, 100, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(400, 200, 150, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(200, 100, 200, 10, arcade.color.BLACK)

    platform_collisions(80, 70)

    # Victory flag
    arcade.draw_rectangle_filled(625, 355, 12, 100, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(631, 405, 631, 360, 671, 382.5, arcade.color.BANANA_YELLOW)

    # Character
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)


def on_key_press(key, something):
    global up_pressed, down_pressed, right_pressed, left_pressed
    if key == arcade.key.W:
        up_pressed = True
    if key == arcade.key.S:
        down_pressed = True
    if key == arcade.key.D:
        right_pressed = True
    if key == arcade.key.A:
        left_pressed = True


def on_key_release(key, something):
    global up_pressed, down_pressed, right_pressed, left_pressed
    if key == arcade.key.W:
        up_pressed = False
    if key == arcade.key.S:
        down_pressed = False
    if key == arcade.key.D:
        right_pressed = False
    if key == arcade.key.A:
        left_pressed = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Final Project")
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
