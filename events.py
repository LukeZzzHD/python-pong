import pygame   # Import the pygame library, here we need it to access the keys that the user pressed

# All these functions take a pygame event as a parameter.
# Every function will return True if a specific key is pressed.
# For example:
# The user presses W. Then the function key_is_W will return True.
# Because event.type is equal to pygame.K_w

def key_is_pressed(event):
    return event.type == pygame.KEYDOWN

def  key_is_released(event):
    return event.type == pygame.KEYUP

def key_is_W(event):
    return event.key == pygame.K_w

def  key_is_S(event):
    return event.key == pygame.K_s

def key_is_ArrowUP(event):
    return event.key == pygame.K_UP

def key_is_ArrowDown(event):
    return event.key == pygame.K_DOWN

def key_is_Space(event):
    return event.key == pygame.K_SPACE

def user_closed_window(event):
    return event.type == pygame.QUIT