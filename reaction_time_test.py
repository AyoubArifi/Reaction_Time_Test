import pygame
import sys
import random
import time
import csv  

pygame.init()

window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
clock = pygame.time.Clock()

WHITE =(255, 255, 255)
RED =(255, 0, 0)
GREEN =(0, 255, 0)
BLACK =(0, 0, 0)
GRAY =(200, 200, 200)
DARK_GRAY =(100, 100, 100)

font =pygame.font.Font(None, 60)
small_font =pygame.font.Font(None, 40)

radius =80
reaction_times = []

MAX_TRIALS =40
trial_count =0

def get_participant_name():
    user_text = ''
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_text.strip(): 
                    input_active = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode 

        window.fill(WHITE)

        instruction = small_font.render("Enter your name and press \"ENTER\":", True, BLACK)
        instruction_rect = instruction.get_rect(center=(window.get_width() // 2, window.get_height() // 2 - 100))
        window.blit(instruction, instruction_rect)

        input_rect = pygame.Rect(window.get_width() // 2 - 300, window.get_height() // 2, 600, 60)
        pygame.draw.rect(window, GRAY, input_rect)
        pygame.draw.rect(window, DARK_GRAY, input_rect, 4)

        text_surface = small_font.render(user_text, True, BLACK)
        text_rect = text_surface.get_rect(center=input_rect.center)
        window.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(60)

    return user_text.strip()

def show_start_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        window.fill(WHITE)
        text = small_font.render("Press \"Space\" to start.", True, BLACK)
        text_rect = text.get_rect(center=(window.get_width() // 2, window.get_height() // 2))
        window.blit(text, text_rect)
        pygame.display.update()
        clock.tick(60)

def show_end_screen():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                waiting = False

        window.fill(WHITE)
        text1 = small_font.render("Test is finished.", True, BLACK)
        text1_rect = text1.get_rect(center=(window.get_width() // 2, window.get_height() // 2 - 20))
        window.blit(text1, text1_rect)

        text2 = small_font.render("Press \"ESC\" to close the window", True, BLACK)
        text2_rect = text2.get_rect(center=(window.get_width() // 2, window.get_height() // 2 + 20))
        window.blit(text2, text2_rect)

        pygame.display.update()
        clock.tick(60)

participant_name = get_participant_name()
show_start_screen()

running = True
test_completed = False
while running and not test_completed:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
            break
        if event.type == pygame.QUIT:
            running = False
            break

    if not running:
        break

    delay = random.uniform(1, 3)
    start_delay = time.time()
    space_pressed_early = False
    early_press_time = 0

    while time.time() - start_delay < delay and running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space_pressed_early = True
                    early_press_time = time.time()
                elif event.key == pygame.K_ESCAPE:
                    running = False

        window.fill(WHITE)
        pygame.display.update()
        clock.tick(60)

    if not running:
        break

    import pygame.gfxdraw
    center_x = window.get_width() // 2
    center_y = window.get_height() // 2
    start_time = time.time()

    if space_pressed_early:
        reaction_time = early_press_time - start_time
        reaction_times.append(reaction_time)
        print(f"Reaction Time: {reaction_time:.3f} seconds (Early!)")
    else:
        waiting = True
        while waiting and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    waiting = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        reaction_time = time.time() - start_time
                        reaction_times.append(reaction_time)
                        print(f"Reaction Time: {reaction_time:.3f} seconds")
                        waiting = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                        waiting = False

            window.fill(WHITE)
            pygame.gfxdraw.aacircle(window, center_x, center_y, radius, RED)
            pygame.gfxdraw.filled_circle(window, center_x, center_y, radius, RED)
            pygame.display.update()
            clock.tick(60)
    trial_count += 1

    if 'reaction_time' in locals():
        show_time = True
        show_start = time.time()
        while show_time and running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    show_time = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                    show_time = False

            if time.time() - show_start > 0.5:
                show_time = False
                continue

            window.fill(WHITE)
            color = GREEN if reaction_time >= 0 else BLACK
            text = font.render(f"{reaction_time:.3f}s", True, color)
            text_rect = text.get_rect(center=(center_x, center_y))
            window.blit(text, text_rect)
            pygame.display.update()
            clock.tick(60)
    if trial_count >= MAX_TRIALS:
        test_completed = True

if test_completed:
    show_end_screen()

filename = f"{participant_name}_reaction_times.csv"
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Trial', 'Reaction Time (s)'])
    for i, rt in enumerate(reaction_times, 1):
        writer.writerow([i, rt])

pygame.quit()
sys.exit()