# Verlet based Physics Engine

---

**To Do:**
+ [x] Construc Pygame Canvas
+ [x] Construct Circle Object
+ [x] Implement Simple Bouncing Ball Physics
+ [ ] Mesh Simulation

---

## Verlet Integrator

With a given previous position of a particle and the current position of a particle we can propagte our particle through time and space with the verlet integrator.

$$x(t+\Delta t) = 2*x(t) - x(t-\Delta t)+a\Delta t^2$$

In the `Object.py` file the propagation of the particle is done in the `update()` function.

```python
def update(self):
    v_y = int(self.rect.centery - self.prev_pos[1])
    v_x = int(self.rect.centerx - self.prev_pos[0])
    self.prev_pos[0] = self.rect.centerx
    self.prev_pos[1] = self.rect.centery
    p_y = self.rect.centery + v_y
    p_x = self.rect.centerx + v_x
    p_y += self.acc
    self.rect.center=(p_x,p_y)
```

The previous position of the particle are stored in a list `self.prev_pos` with `self.prev_pos[0]` being the x position
and `self.prev_pos[1]` the y position. The verlet algorithm is implemented over several steps. First `v_y` and `v_x`
are calculated which is given as the change in x/y position over a given timestep (`clock.tick(60)`). This can be added to
the current position which is further summed with the acceleration yielding the next position. In the next step
the prev_position list will be updated as well as the current position of our particle.
The previous can be chosen to be smaller than the initial position to give the particles 
an inital velocity.

Splitting the verlet algorithm that way makes it possible to adjust for the boundary constraints in the later step.

As shown below:

```python
def update(self):
    
    [...]
    
    if self.rect.centery + self.radius>= self.screen.get_height()-self.radius:
    self.rect.centery = self.screen.get_height()-self.radius
    self.prev_pos[1] = self.rect.centery + v_y*0.9
    if self.rect.centery - self.radius <= 0 + self.radius:
    self.rect.centery = 0+self.radius
    self.prev_pos[1] = self.rect.centery + v_y*0.9
```

### Propagation

1. Calculate x and y velocity
2. Update previous position with current position
3. Calculate future position by propagating the current position with the velocity
4. Propagate particle
   
### Boundary Conditions

If the boundary conditions are met the particle will be set to a base value and the previous positions will be adjusted by the sum of the base value and the previous velocity with some value for energy loss due to the impact.

## Pygame

Pygame has a few notable "features". First of all are the positions of the rectangles stored as integere values. Float values wont have an impact in the over positions of the rectangle. Furthermore, would the use of of the bottom or the top of the rectangle at the boundary be more sensible but currently the code only works with center value. The reason for that will be investigated in the future.


