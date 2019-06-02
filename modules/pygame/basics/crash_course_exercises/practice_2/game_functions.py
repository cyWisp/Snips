import sys, pygame

def check_events(ship):
    # Watch for keyboard and mouse events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        # Ship Movement
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                ship.moving_right = True
            elif event.key == pygame.K_a:
                ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                ship.moving_right = False
            elif event.key == pygame.K_a:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    # Draw all screen elements...
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # Make the most recently drawn screen visible
    pygame.display.flip()
