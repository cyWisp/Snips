import sys, pygame

def check_events():
    # Respond to keypresses and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, ship):
    # Redraw the screen during each pass through the loop
    screen.fill(settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()