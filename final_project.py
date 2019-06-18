"""
-------------------------------------------------------------------------------
Name:		final_project.py
Purpose:
My final project/CPT for Mr. Fabroa's grade 11 comp sci class
Simple platformer game

Author:		Cheung.M

Created:		17/06/2019
------------------------------------------------------------------------------
"""


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
player_x = 0
player_y = 0

# Gravity variables
velocity = 0
gravity = 0.2
on_plat = False
jumping = False
falling = False

# Menu variables
texture = arcade.load_texture("images/victory.png")
main_menu = True

# Endgame variables
victory = False
level_1 = False
level_2 = False
level_3 = False

one_start = False
two_start = False
three_start = False

l_1_plats = False
l_2_plats = False
l_3_plats = False

finish = False

# Camera variables
cam_vars = [0, 900, 0, 600]

# Level 2 variables
moving_plat = [800, 100, 150, 10]
moving_plat_2 = [1100, 375, 150, 10]
m_down = False
m_up = True

m_down_2 = True
m_up_2 = False

# Level 3 variables
blue_plat = False
red_plat = True
switch_timer = 0
switch_counter = 0


def on_update(delta_time):
    """Updates the majority of the game to run at 60 frames per second

    No parameters
    """
    global up_pressed, down_pressed, right_pressed, left_pressed, player_x, player_y

    # Left right movement
    if right_pressed:
        player_x += 5
    if left_pressed:
        player_x -= 5

    # Calling all functions
    player_start()
    jumped()
    level_switch()
    camera()


def menu():
    """Groups the shapes to draw the main menu

    No parameters
    """
    menu_text_1 = "Welcome to Bally's Quest!"
    menu_text_2 = "Click anywhere to play!"

    arcade.draw_text(menu_text_1, 150, 500, arcade.color.GREEN, 40)
    arcade.draw_text(menu_text_2, 230, 75, arcade.color.GREEN, 30)

    arcade.draw_circle_filled(400, 275, 125, arcade.color.RED)


def player_start():
    """Sets the location of where the player will start each level

    No parameters
    """
    global player_x, player_y, one_start, two_start, three_start

    if level_1 and not one_start:
        player_x = 25
        player_y = 25
        one_start = True

    if level_2 and not two_start:
        player_x = 725
        player_y = 25
        if cam_vars[0] == 700:
            two_start = True
    if level_3 and not three_start:
        player_x = 1425
        player_y = 25
        if cam_vars[0] == 1400:
            three_start = True


def level_switch():
    """Stores information on how to switch levels

    No parameters
    """
    global victory, level_1, level_2, level_3, main_menu, cam_vars, finish, one_start, two_start, three_start, l_1_plats
    global l_2_plats, l_3_plats, moving_plat, moving_plat_2, m_down, m_up, m_down_2, m_up_2, blue_plat, red_plat, \
        switch_counter, switch_timer, player_x, player_y

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

        if (2094 <= player_x <= 2156) and (305 <= player_y <= 430):
            victory = True

    if finish:
        player_x = 0
        player_y = 0
        cam_vars[0] = 0
        main_menu = True
        victory = False
        level_1 = False
        level_2 = False
        level_3 = False

        one_start = False
        two_start = False
        three_start = False

        l_1_plats = False
        l_2_plats = False
        l_3_plats = False

        finish = False

        # Camera variables
        cam_vars = [0, 900, 0, 600]

        # Level 2 variables
        moving_plat = [800, 100, 150, 10]
        moving_plat_2 = [1100, 375, 150, 10]
        m_down = False
        m_up = True

        m_down_2 = True
        m_up_2 = False

        # Level 3 variables
        blue_plat = False
        red_plat = True
        switch_timer = 0
        switch_counter = 0


def jumped():
    """Function that dictates how the player should jump

    No parameters
    """
    global on_plat, velocity, player_y, jumping, falling

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
    """Sets the camera

    No parameters
    """
    global cam_vars

    arcade.set_viewport(cam_vars[0],
                        cam_vars[1],
                        cam_vars[2],
                        cam_vars[3])


def level_1_platforms():
    """Collisions for the first level

    No parameters
    """
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
    """Collisions for the second level

    No parameters
    """
    global player_x, player_y, on_plat, moving_plat, m_down, m_up, m_down_2, m_up_2

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
    # First platform movements
    if moving_plat[1] <= 5:
        m_up = True
        m_down = False
    if moving_plat[1] >= 300:
        m_down = True
        m_up = False

    if m_up:
        moving_plat[1] += 2.5
    if m_down:
        moving_plat[1] -= 2.5

    # Second platform movements
    if moving_plat_2[1] <= 105:
        m_up_2 = True
        m_down_2 = False
    if moving_plat_2[1] >= 475:
        m_down_2 = True
        m_up_2 = False

    if m_up_2:
        moving_plat_2[1] += 2.5
    if m_down_2:
        moving_plat_2[1] -= 2.5

    # Platform collisions

    # First moving platform collisions
    # Makes sure that the player stays on the platform
    if ((700 <= player_x <= 900 and moving_plat[1] <= player_y <= moving_plat[1] + 30)
            and player_y + 1 <= moving_plat[1] + 30 and m_up):
        player_y = moving_plat[1] + 30
        on_plat = True
    # If the player bounces too high, it adjusts and still sticks them to the moving plat
    if ((700 <= player_x <= 900 and moving_plat[1] <= player_y <= moving_plat[1] + 40)
            and player_y + 1 <= moving_plat[1] + 40 and m_down):
        player_y = moving_plat[1] + 30
        on_plat = True

    if ((700 <= player_x <= 900 and moving_plat[1] - 30 <= player_y <= moving_plat[1])
            and player_y + 1 >= moving_plat[1] - 30):
        player_y = moving_plat[1] - 30

    # Second moving platform collisions
    # Makes sure that the player stays on the platform
    if ((1000 <= player_x <= 1200 and moving_plat_2[1] <= player_y <= moving_plat_2[1] + 30)
            and player_y + 1 <= moving_plat_2[1] + 30 and m_up_2):
        player_y = moving_plat_2[1] + 30
        on_plat = True
    # If the player bounces too high, it adjusts and still sticks them to the moving plat
    if ((1000 <= player_x <= 1200 and moving_plat_2[1] <= player_y <= moving_plat_2[1] + 40)
            and player_y + 1 <= moving_plat_2[1] + 40 and m_down_2):
        player_y = moving_plat_2[1] + 30
        on_plat = True

    if ((1000 <= player_x <= 1200 and moving_plat_2[1] - 30 <= player_y <= moving_plat_2[1])
            and player_y + 1 >= moving_plat_2[1] - 30):
        player_y = moving_plat_2[1] - 30

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
    """Collisions for the third level

    No parameters
    """
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
        if (1525 <= player_x <= 1675 and 200 <= player_y <= 230) and player_y + 1 >= 200:
            player_y = 200
        if (1525 <= player_x <= 1675 and 230 <= player_y <= 260) and player_y + 1 <= 260:
            player_y = 260
            on_plat = True
        
        if (1525 <= player_x <= 1675 and 200 <= player_y <= 260) and player_x + 1 <= 1525:
            player_x = 1525
        if (1525 <= player_x <= 1675 and 200 <= player_y <= 260) and player_x - 1 >= 1675:
            player_x = 1675
    
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

        # Higher blue plat collisions
        if (1800 <= player_x <= 1950 and 270 <= player_y <= 300) and player_y + 1 >= 270:
            player_y = 270
        if (1800 <= player_x <= 1950 and 300 <= player_y <= 330) and player_y - 1 <= 330:
            player_y = 330
            on_plat = True

        if (1800 <= player_x <= 1950 and 270 <= player_y <= 330) and player_x + 1 <= 1800:
            player_x = 1800
        if (1800 <= player_x <= 1950 and 270 <= player_y <= 330) and player_x - 1 >= 1950:
            player_x = 1950

    # Platform 3 Y collisions
    if (2030 <= player_x <= 2170 and 370 <= player_y <= 400) and player_y + 1 >= 370:
        player_y = 370
    if (2030 <= player_x <= 2170 and 400 <= player_y <= 430) and player_y - 1 <= 430:
        player_y = 430
        on_plat = True

    # Platform 3 X collisions
    if (2030 <= player_x <= 2170 and 370 <= player_y <= 430) and player_x + 1 <= 2030:
        player_x = 2030
    if (2030 <= player_x <= 2170 and 370 <= player_y <= 430) and player_x - 1 >= 2170:
        player_x = 2170


def on_draw():
    """Draw function that draws everything that does not need to be updated

    No parameters
    """
    global player_x, player_y, victory, level_1, level_2, cam_vars, moving_plat, l_2_plats, l_3_plats, \
        l_1_plats, texture
    arcade.start_render()

    # Draws menu
    if not level_1 and cam_vars[0] == 0:
        menu()

    # Draws level 1 platforms
    if level_1:
        l_1_plats = True

    if l_1_plats:
        # Level 1 platforms
        arcade.draw_rectangle_filled(600, 300, 100, 10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(400, 200, 150, 10, arcade.color.BLACK)
        arcade.draw_rectangle_filled(200, 100, 200, 10, arcade.color.BLACK)

        # Victory flag level 1
        arcade.draw_rectangle_filled(625, 355, 12, 100, arcade.color.DARK_BROWN)
        arcade.draw_triangle_filled(631, 405, 631, 360, 671, 382.5, arcade.color.BANANA_YELLOW)

    # Draws level 2 platforms
    if level_2 and cam_vars[0] == 700:
        l_2_plats = True

    if l_2_plats:
        # First moving plat
        arcade.draw_rectangle_filled(moving_plat[0],
                                     moving_plat[1],
                                     moving_plat[2],
                                     moving_plat[3], arcade.color.BLACK)

        # Second moving plat
        arcade.draw_rectangle_filled(moving_plat_2[0],
                                     moving_plat_2[1],
                                     moving_plat_2[2],
                                     moving_plat_2[3], arcade.color.BLACK)
        arcade.draw_rectangle_filled(1300, 300, 100, 10, arcade.color.BLACK)

        # Level 2 victory flag
        arcade.draw_rectangle_filled(1325, 355, 12, 100, arcade.color.DARK_BROWN)
        arcade.draw_triangle_filled(1331, 405, 1331, 360, 1371, 382.5, arcade.color.BANANA_YELLOW)

    # Draws level 3 platforms
    if level_3 and cam_vars[0] == 1400:
        l_3_plats = True

    if l_3_plats:

        # Victory platform
        arcade.draw_rectangle_filled(2100, 400, 100, 10, arcade.color.BLACK)

        # Draws platforms with collisions
        if red_plat:
            arcade.draw_rectangle_filled(1700, 70, 200, 10, arcade.color.RED)
            arcade.draw_rectangle_filled(1600, 230, 100, 10, arcade.color.RED)
        if blue_plat:
            arcade.draw_rectangle_filled(1900, 150, 150, 10, arcade.color.BLUE)
            arcade.draw_rectangle_filled(1875, 300, 100, 10, arcade.color.BLUE)

        # Draws outline of non-collision platforms
        arcade.draw_rectangle_outline(1700, 70, 200, 10, arcade.color.RED)
        arcade.draw_rectangle_outline(1600, 230, 100, 10, arcade.color.RED)
        arcade.draw_rectangle_outline(1900, 150, 150, 10, arcade.color.BLUE)
        arcade.draw_rectangle_outline(1875, 300, 100, 10, arcade.color.BLUE)
        
        # Level 3 victory flag
        arcade.draw_rectangle_filled(2125, 455, 12, 100, arcade.color.DARK_BROWN)
        arcade.draw_triangle_filled(2131, 505, 2131, 460, 2171, 482.5, arcade.color.BANANA_YELLOW)
      
    # Character
    if level_1:
        arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)
    if level_2 and cam_vars[0] == 700:
        arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)
    if level_3 and cam_vars[0] == 1400:
        arcade.draw_circle_filled(player_x, player_y, 25, arcade.color.RED)

    # Level end text
    endgame_text = "Congratulations!"
    endgame_text_2 = "You Won!"
    endgame_text_3 = "Click anywhere to continue"

    finish_text = "You beat the game!"
    finish_text_2 = "Click anywhere to return to start"

    # Draws level end text
    if victory:
        if level_1:
            arcade.draw_rectangle_filled(400, 300, 350, 250, arcade.color.BATTLESHIP_GREY)
            arcade.draw_text(endgame_text, 310, 390, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_2, 345, 350, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_3, 270, 200, arcade.color.PINK_LAVENDER, 18)

            arcade.draw_texture_rectangle(400, 280, texture.width / 2.3, texture.height / 2.3, texture, 0)

        if level_2:
            arcade.draw_rectangle_filled(1100, 300, 350, 250, arcade.color.BATTLESHIP_GREY)
            arcade.draw_text(endgame_text, 1010, 390, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_2, 1045, 350, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(endgame_text_3, 970, 200, arcade.color.PINK_LAVENDER, 18)

            arcade.draw_texture_rectangle(1100, 280, texture.width / 2.3, texture.height / 2.3, texture, 0)

        if level_3:
            arcade.draw_rectangle_filled(1800, 300, 350, 250, arcade.color.BATTLESHIP_GREY)
            arcade.draw_text(endgame_text, 1710, 390, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(finish_text, 1699, 350, arcade.color.YELLOW_GREEN, 20)
            arcade.draw_text(finish_text_2, 1650, 200, arcade.color.PINK_LAVENDER, 18)

            arcade.draw_texture_rectangle(1800, 280, texture.width / 2.3, texture.height / 2.3, texture, 0)


def on_key_press(key, something):
    """Overrides the windows key press commands

    :param key: what key is pressed
    """
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
    """Overrides the windows key release commands

    :param key: what key is pressed
    """
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
    """Determines if a mouse click is detected, what it should do

    :param x: The x location of the mouse press
    :param y: The y location of the mouse press
    """
    global victory, level_1, level_2, level_3, main_menu, finish

    if main_menu:
        if 0 <= x <= 800 and 0 <= y <= 600:
            level_1 = True
            main_menu = False

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
            finish = True
            victory = False


def setup():
    """Sets up the game

    No parameters
    """
    arcade.open_window(WIDTH, HEIGHT, "Final Project")
    arcade.set_background_color(arcade.color.BLUE_GRAY)
    arcade.schedule(on_update, 1/60)

    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
