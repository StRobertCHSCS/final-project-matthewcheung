import arcade

# Screen variables
WIDTH = 800
HEIGHT = 600

# Variables to record if certain keys are being pressed.
up_pressed = False
down_pressed = False
left_pressed = False
right_pressed = False

# Player variables
player_x = 25
player_y = 25

# Gravity variables
velocity = 0
gravity = 0.2
on_plat = False
jumping = False

# Endgame variables
victory = False
level_1 = True
level_2 = False
level_3 = False
level_4 = False

one_start = False
two_start = False
three_start = False
four_start = False

l2_plats = False
l3_plats = False

# Camera variables
cam_vars = [0, 800, 0, 600]

# Level 2 variables
moving_plat = [1000, 100, 150, 10]
m_down = False
m_up = True

# Level 3 variables
blue_plat = False
red_plat = True
switch_timer = 0
switch_counter = 0


def on_update(delta_time):
    global up_pressed, down_pressed, right_pressed, left_pressed, player_x, player_y

    # Left right movement
    if right_pressed:
        player_x += 5
    if left_pressed:
        player_x -= 5

    # Calling all functions



    jumped()
    end_goal()
    camera()




def end_goal():
    global victory, level_1, level_2

    if level_1:
        level_1_platforms()

        if (594 <= player_x <= 656) and (305 <= player_y <= 430):
            victory = True

    if level_2:
        level_1 = False
        if not cam_vars[0] >= 700:
            cam_vars[0] += 5
            cam_vars[1] += 5

        if cam_vars[0] == 700:
            level_2_platforms()

        if (1294 <= player_x <= 1356) and (305 <= player_y <= 430):
            victory = True

    if level_3:
        level_2 = False
        if not cam_vars[0] >= 1400:
            cam_vars[0] += 5
            cam_vars[1] += 5

        if cam_vars[0] == 1400:
            level_3_platforms()

        if (1994 <= player_x <= 2056) and (305 <= player_y <= 430):
            victory = True


def level_1_platforms():
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


def level_2_platforms():
    global player_x, player_y, on_plat, moving_plat, m_down, m_up

    # Stops player from leaving the screen
    if player_y + 1 >= 1275:
        player_y = 1275
    if player_y - 1 <= 25:
        player_y = 25
        on_plat = True
    else:
        on_plat = False

    if player_x - 1 <= 725:
        player_x = 725

    if player_x + 1 >= 1475:
        player_x = 1475

    # Moving platform movements
    if moving_plat[1] <= 5:
        m_up = True
        m_down = False
    if moving_plat[1] >= 375:
        m_down = True
        m_up = False

    if m_up:
        moving_plat[1] += 2.5
    if m_down:
        moving_plat[1] -= 2.5

    # Platform collisions

    # Moving platform collisions
    if ((900 <= player_x <= 1100 and moving_plat[1] <= player_y <= moving_plat[1] + 30)
            and player_y + 1 <= moving_plat[1] + 30 and m_up):
        player_y = moving_plat[1] + 30
        on_plat = True
    if ((900 <= player_x <= 1100 and moving_plat[1] <= player_y <= moving_plat[1] + 40)
            and player_y + 1 <= moving_plat[1] + 40 and m_down):
        player_y = moving_plat[1] + 30
        on_plat = True

    if ((900 <= player_x <= 1100 and moving_plat[1] - 30 <= player_y <= moving_plat[1])
            and player_y + 1 >= moving_plat[1] - 30):
        player_y = moving_plat[1] - 30

    # Platform 2 Y collisions
    if (1230 <= player_x <= 1370 and 270 <= player_y <= 300) and player_y + 1 >= 270:
        player_y = 270
    if (1230 <= player_x <= 1370 and 300 <= player_y <= 330) and player_y - 1 <= 330:
        player_y = 330
        on_plat = True

    # Platform 2 X collisions
    if (1230 <= player_x <= 1370 and 270 <= player_y <= 330) and player_x + 1 <= 1180:
        player_x = 1180
    if (1230 <= player_x <= 1370 and 270 <= player_y <= 330) and player_x - 1 >= 1420:
        player_x = 1420


def level_3_platforms():
    global player_y, player_x, on_plat, switch_timer, switch_counter, red_plat, blue_plat

    # Stops player from leaving the screen
    if player_y + 1 >= 1975:
        player_y = 1975
    if player_y - 1 <= 25:
        player_y = 25
        on_plat = True
    else:
        on_plat = False

    if player_x - 1 <= 1425:
        player_x = 1425
    if player_x + 1 >= 2175:
        player_x = 2175

    # Alternating platform code
    switch_timer += 1
    if switch_timer >= 120:
        switch_timer = 0
        switch_counter += 1

    if switch_counter % 2 == 0:
        red_plat = True
        blue_plat = False

    if switch_counter % 2 == 1:
        blue_plat = True
        red_plat = False

    # Switching platform collisions
    if red_plat:
        # Lower red plat collisions
        if (1575 <= player_x <= 1825 and 40 <= player_y <= 70) and player_y + 1 >= 40:
            player_y = 40
        if (1575 <= player_x <= 1825 and 70 <= player_y <= 100) and player_y - 1 <= 100:
            player_y = 100
            on_plat = True

        if (1575 <= player_x <= 1825 and 40 <= player_y <= 100) and player_x + 1 <= 1570:
            player_x = 1570
        if (1575 <= player_x <= 1825 and 40 <= player_y <= 100) and player_y - 1 >= 1830:
            player_x = 1830

        # Higher red plat collisions
        if (1475 <= player_x <= 1725 and 200 <= player_y <= 230) and player_y + 1 >= 200:
            player_y = 200
        if (1475 <= player_x <= 1725 and 230 <= player_y <= 260) and player_y + 1 <= 260:
            player_y = 260
            on_plat = True

        if (1475 <= player_x <= 1725 and 200 <= player_y <= 260) and player_x + 1 <= 1470:
            player_x = 1470
        if (1475 <= player_x <= 1725 and 200 <= player_y <= 260) and player_x - 1 >= 1730:
            player_x = 1730

    if blue_plat:
        # Lower blue plat collisions
        if (1800 <= player_x <= 2000 and 120 <= player_y <= 150) and player_y + 1 >= 120:
            player_y = 120
        if (1800 <= player_x <= 2000 and 150 <= player_y <= 180) and player_y - 1 <= 180:
            player_y = 180
            on_plat = True

        if (1800 <= player_x <= 2000 and 120 <= player_y <= 180) and player_x + 1 <= 1800:
            player_x = 1800
        if (1800 <= player_x <= 2000 and 120 <= player_y <= 180) and player_x - 1 >= 2000:
            player_x = 2000

    '''
    arcade.draw_rectangle_outline(1700, 70, 200, 10, arcade.color.RED)
    arcade.draw_rectangle_outline(1600, 230, 100, 10, arcade.color.RED)
    arcade.draw_rectangle_outline(1900, 150, 150, 10, arcade.color.BLUE)
    '''

    # Platform 3 Y collisions
    if (1930 <= player_x <= 2070 and 270 <= player_y <= 300) and player_y + 1 >= 270:
        player_y = 270
    if (1930 <= player_x <= 2070 and 300 <= player_y <= 330) and player_y - 1 <= 330:
        player_y = 330
        on_plat = True

    # Platform 3 X collisions
    if (1930 <= player_x <= 2070 and 270 <= player_y <= 330) and player_x + 1 <= 1930:
        player_x = 1930
    if (1930 <= player_x <= 2070 and 270 <= player_y <= 330) and player_x - 1 >= 2070:
        player_x = 2070


def jumped():
    global on_plat, velocity, player_y, jumping

    if up_pressed:
        jumping = True

    if jumping:
        player_y += 7
        velocity += gravity
        player_y -= velocity
        if velocity >= 20:
            velocity = 20

    if on_plat:
        velocity = 0
        jumping = False

    if not on_plat and not jumping:
        velocity += 0.2
        velocity += gravity
        player_y -= velocity
        if velocity >= 20:
            velocity = 20


def camera():
    global cam_vars

    arcade.set_viewport(cam_vars[0],
                        cam_vars[1],
                        cam_vars[2],
                        cam_vars[3])


def on_draw():
    global player_x, player_y, victory, level_1, level_2, cam_vars, moving_plat, l2_plats, l3_plats
    arcade.start_render()

    # Draws level 1 platforms
    arcade.draw_rectangle_filled(600, 300, 100, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(400, 200, 150, 10, arcade.color.BLACK)
    arcade.draw_rectangle_filled(200, 100, 200, 10, arcade.color.BLACK)
    # Victory flag level 1
    arcade.draw_rectangle_filled(625, 355, 12, 100, arcade.color.DARK_BROWN)
    arcade.draw_triangle_filled(631, 405, 631, 360, 671, 382.5, arcade.color.BANANA_YELLOW)

    # Draws level 2 platforms





    # Character
    if level_1:
        arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)


    # Level end text
    endgame_text = "Congratulations!"
    endgame_text_2 = "You Won!"
    endgame_text_3 = "Click anywhere to continue"

    # Draws level end text
    if victory:
        if level_1:
            arcade.draw_rectangle_filled(400, 300, 350, 250, arcade.color.BATTLESHIP_GREY)
            arcade.draw_text(endgame_text, 290, 390, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_2, 340, 350, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_3, 240, 200, arcade.color.PINK_LAVENDER, 18)

        if level_2:
            arcade.draw_rectangle_filled(1100, 300, 350, 250, arcade.color.BATTLESHIP_GREY)
            arcade.draw_text(endgame_text, 990, 390, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_2, 1040, 350, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_3, 940, 200, arcade.color.PINK_LAVENDER, 18)


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


def on_mouse_press(x, y, something, something_2):
    global victory, level_1, level_2, level_3, level_4

    if victory and level_1:
        if 0 <= x <= 800 and 0 <= y <= 600:
            level_2 = True
            victory = False

    if victory and level_2:
        if 0 <= x <= 800 and 0 <= y <= 600:
            level_3 = True
            victory = False

    if victory and level_3:
        if 0 <= x <= 800 and 0 <= y <= 600:
            level_4 = True
            victory = False


def setup():
    arcade.open_window(WIDTH, HEIGHT, "Final Project")
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.schedule(on_update, 1 / 60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
