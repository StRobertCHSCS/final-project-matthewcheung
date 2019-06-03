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
gravity = 0.13
on_plat = False


def on_update(delta_time):
    global up_pressed, down_pressed, right_pressed, left_pressed, player_x, player_y, velocity, gravity, on_plat
    if up_pressed:
        player_y += 5
    else:
        velocity = 0
    if down_pressed:
        player_y -= 5
    if right_pressed:
        player_x += 5
    if left_pressed:
        player_x -= 5

    # Gravity
    if up_pressed is True:
        velocity += gravity
        player_y -= velocity

    # Stops player from leaving the screen
    if player_y >= 575:
        player_y = 575
    if player_y <= 25:
        player_y = 25
    if player_x <= 25:
        player_x = 25
    if player_x >= 775:
        player_x = 775

    # creates boundaries for platforms
    '''
    if 280 <= player_x <= 520 and 175 <= player_y <= 225:
        if player_y == 175:
            player_y = player_y - 5
        elif player_y == 225:
            player_y = player_y + 5

         if player_x == 280:
            player_x = player_x - 5
        elif player_x == 520:
            player_x = player_x + 5
       
    '''

    if 280 <= player_x <= 520 and 171 <= player_y <= 231:
        if player_y > 170:
            player_y = 170
        if player_y < 230:
            player_y = 230

        if player_x < 280:
            player_x = 280
        if player_x > 520:
            player_x = 520


def on_draw():
    global player_x, player_y
    arcade.start_render()
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)

    # Draws platforms
    arcade.draw_rectangle_filled(400, 200, 200, 10, arcade.color.BLACK)


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
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()
