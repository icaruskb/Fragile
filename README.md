# Fragile
Learning pygame 
----------------------------------


# Collision example that isn't being used
#================================================================================================================================================================
            #img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            #if img_r.colliderect(self.collision_area):
            #    pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            #else:
            #    pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)
            #Easier way to do it is pygame.Rect(*self.img_pos, *self.img.get_size()) <-- gets pointer value and adjusts collision from there.
#================================================================================================================================================================