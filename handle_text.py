

class TextHandle():
    def __init__(self, font, color, screen):
        self.font = font
        self.color = color 
        self.screen = screen
    
    def display_text(self, text, position_attribute):
        text_surface = self.font.render(text, True, self.color)
        text_rect = text_surface.get_rect()
        setattr(text_rect, position_attribute, getattr(self.screen.get_rect(), position_attribute))
        self.screen.blit(text_surface, text_rect)