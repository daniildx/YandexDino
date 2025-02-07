import pygame
import sys

pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("YandexDino.ru ")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Шрифты
font = pygame.font.Font(None, 45)

# Функция для отображения текста
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

# Функция для обработки меню
def menu():
    while True:
        screen.fill(WHITE)

        draw_text("Yandex Dino", font, BLACK, screen, WIDTH // 2, HEIGHT // 6)

        # Кнопки
        play_button = pygame.Rect(WIDTH // 4, HEIGHT // 3, WIDTH // 2, 50)
        exit_button = pygame.Rect(WIDTH // 4, HEIGHT // 3 + 60, WIDTH // 2, 50)
        developers_button = pygame.Rect(WIDTH // 4, HEIGHT // 3 + 120, WIDTH // 2, 50)
        help_button = pygame.Rect(WIDTH // 4, HEIGHT // 3 + 180, WIDTH // 2, 50)
        about_button = pygame.Rect(WIDTH // 4, HEIGHT // 3 + 240, WIDTH // 2, 50)

        pygame.draw.rect(screen, BLUE, play_button)
        pygame.draw.rect(screen, BLUE, exit_button)
        pygame.draw.rect(screen, BLUE, developers_button)
        pygame.draw.rect(screen, BLUE, help_button)
        pygame.draw.rect(screen, BLUE, about_button)

        draw_text("Играть", font, WHITE, screen, WIDTH // 2, HEIGHT // 3 + 25)
        draw_text("Выход", font, WHITE, screen, WIDTH // 2, HEIGHT // 3 + 85)
        draw_text("Разработчики", font, WHITE, screen, WIDTH // 2, HEIGHT // 3 + 145)
        draw_text("Помощь", font, WHITE, screen, WIDTH // 2, HEIGHT // 3 + 205)
        draw_text("Об игре", font, WHITE, screen, WIDTH // 2, HEIGHT // 3 + 265)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    # Запуск игры
                    import dino
                    dino.run()
                elif exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()
                elif developers_button.collidepoint(event.pos):
                    show_developers()
                elif help_button.collidepoint(event.pos):
                    show_help()
                elif about_button.collidepoint(event.pos):
                    show_about()

        pygame.display.flip()

# Функции для вывода информации
def show_developers():
    while True:
        screen.fill(WHITE)
        draw_text("Дикунов Даниил и Марк Дорошенко", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_back_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(event.pos):
                return

        pygame.display.flip()

def show_help():
    while True:
        screen.fill(WHITE)
        draw_text("Telegram: Даниил-@yhppkh, Марк-@balance0811", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_back_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(event.pos):
                return

        pygame.display.flip()

def show_about():
    while True:
        screen.fill(WHITE)
        draw_text("Хорошей игры!!!", font, BLACK, screen, WIDTH // 2, HEIGHT // 2)
        draw_back_button()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(event.pos):
                return

        pygame.display.flip()

def draw_back_button():
    global back_button
    back_button = pygame.Rect(WIDTH // 4, HEIGHT // 3 + 300, WIDTH // 2, 50)
    pygame.draw.rect(screen, BLUE, back_button)
    draw_text("Назад", font, WHITE, screen, WIDTH // 2, HEIGHT // 3 + 325)

# Запуск меню
menu()