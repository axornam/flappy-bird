def draw_text(text, font, screen, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
