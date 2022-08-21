import pygame
import math

import planets.pygame_settings as setting

class Planet:

    au = 149.6e6 * 1000
    g = 6.67428e-11
    scale = 250 / au
    timestep = 3600*24

    def __init__(self, x, y, radius, color, mass, name, text):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0
        self.x_vel = 0
        self.y_vel = 0
        self.name = name
        self.text = text

    def draw(self, win):
        x = self.x * self.scale + setting.width / 2
        y = self.y * self.scale + setting.height / 2

        if len(self.orbit) > 2:
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = x * self.scale + setting.width / 2
                y = y * self.scale + setting.height / 2
                updated_points.append((x, y))

            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        planet_names = setting.font_.render(self.text, 1, setting.white)
        win.blit(planet_names, (x - planet_names.get_width() / 2, y - planet_names.get_height() - 30))

        if not self.sun:
            distance_text = setting.font_.render(f'{round(self.distance_to_sun / 1000, 1)}km', 1, setting.white)
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))
            
            center_text = setting.font_.render('Pâmela', 1, setting.black)
            center_text_rect = center_text.get_rect()
            center_text_rect.center = (setting.width / 2, setting.height / 2)
            win.blit(center_text, center_text_rect)

            sub_center_font = setting.sub_font_.render('pamervs', 1, setting.black)
            sub_center_font_rect = sub_center_font.get_rect()
            sub_center_font_rect.center = ((setting.width / 2), (setting.height / 2) + 10)
            win.blit(sub_center_font, sub_center_font_rect)
            
            invite_text = setting.font_.render(self.name, 1, setting.blue)
            win.blit(invite_text, (x - invite_text.get_width() / 2, y - invite_text.get_height() + 25))
    
    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = self.g * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force

        return force_x, force_y

    def update_position(self, planets):
        total_fx = total_fy = 0

        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.timestep
        self.y_vel += total_fy / self.mass * self.timestep

        self.x += self.x_vel * self.timestep
        self.y += self.y_vel * self.timestep
        
        self.orbit.append((self.x, self.y))