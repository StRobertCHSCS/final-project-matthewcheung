import arcade


WIDTH = 800
HEIGHT = 600

# start player position in middle of window
player_x = 20
player_y = 40

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

# gravity variables
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


    #gravity
    if up_pressed is True and on_plat is False:
        velocity += gravity
        player_y -= velocity


    # stops player from leaving the screen
    if player_y >= 575:
        player_y = 575
    if player_y <= 25:
        player_y = 25
    if player_x <= 25:
        player_x = 25
    if player_x >= 775:
        player_x = 775

    # creates boundaries for platforms
    if 280 <= player_x <= 520 and 175 <= player_y <= 225:
        if player_y > 175:
            player_y = 175
            on_plat = True
        elif player_y < 225:
            player_y = 225
            on_plat = True

        if player_x > 280:
            player_x = 280
            on_plat = True
        elif player_x < 520:
            player_x = 520
            on_plat = True

    else:
        on_plat = False







def on_draw():
    global player_x, player_y
    arcade.start_render()
    # Draw in here...
    arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.BLUE)

    # Draw platforms
    arcade.draw_rectangle_filled(400, 200, 200, 10, arcade.color.BLACK)


def on_key_press(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed
    if key == arcade.key.W:
        up_pressed = True
    if key == arcade.key.S:
        down_pressed = True
    if key == arcade.key.D:
        right_pressed = True
    if key == arcade.key.A:
        left_pressed = True

def on_key_release(key, modifiers):
    global up_pressed, down_pressed, right_pressed, left_pressed
    if key == arcade.key.W:
        up_pressed = False
    if key == arcade.key.S:
        down_pressed = False
    if key == arcade.key.D:
        right_pressed = False
    if key == arcade.key.A:
        left_pressed = False


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()