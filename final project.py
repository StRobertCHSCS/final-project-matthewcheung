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


def platforms():
    global player_x, player_y, on_plat

    # Stops player from leaving the screen
    if player_y >= 575:
        player_y = 575
    if player_y <= 25:
        player_y = 25
        on_plat = True
    else:
        on_plat = False

    if player_x <= 25:
        player_x = 25
    if player_x >= 775:
        player_x = 775

    # Platform collisions
    if (480 <= player_x <= 720 and 270 <= player_y <= 300) and player_y + 1 >= 270:
        player_y = 270
    if (480 <= player_x <= 720 and 300 <= player_y <= 330) and player_y - 1 <= 330:
        player_y = 330
        on_plat = True
    else:
        on_plat = False

    if (480 <= player_x <= 720 and 270 <= player_y <= 330) and player_x + 1 <= 480:
        player_x = 480
    if (480 <= player_x <= 720 and 270 <= player_y <= 330) and player_x - 1 >= 720:
        player_x = 720

    if (280 <= player_x <= 520 and 170 <= player_y <= 200) and player_y + 1 >= 170:
        player_y = 170
    if (280 <= player_x <= 520 and 200 <= player_y <= 230) and player_y - 1 <= 230:
        player_y = 230
        on_plat = True
    else:
        on_plat = False

    if (280 <= player_x <= 520 and 170 <= player_y <= 230) and player_x + 1 <= 280:
        player_x = 280
    if (280 <= player_x <= 520 and 170 <= player_y <= 230) and player_x - 1 >= 520:
        player_x = 520

    if (80 <= player_x <= 320 and 70 <= player_y <= 100) and player_y + 1 >= 70:
        player_y = 70
    if (80 <= player_x <= 320 and 100 <= player_y <= 130) and player_y - 1 <= 130:
        player_y = 130
        on_plat = True
    else:
        on_plat = False

    if (80 <= player_x <= 320 and 70 <= player_y <= 130) and player_x + 1 <= 80:
        player_x = 80
    if (80 <= player_x <= 320 and 70 <= player_y <= 130) and player_x - 1 >= 320:
        player_x = 320


'''
for i in range(len(amount_of_plats):
    if (left_edge <= player_x <= right_edge and bottom_plat <= player_y <= top_plat) and player_y + 1 >= bottom_plat:
        player_y = bottom_plat
'''


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


def on_draw():
    global player_x, player_y
    arcade.start_render()
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)

    arcade.draw_rectangle_filled(600, 300, 200, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(400, 200, 200, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(200, 100, 200, 10, arcade.color.BLACK)


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
