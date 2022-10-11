# Verlet based Physics Engine

---

**To Do:**
+ [x] Construc Pygame Canvas
+ [x] Construct Circle Object
+ [x] Implement Simple Bouncing Ball Physics
+ [ ] Mesh Simulation

For the mesh creation the nodes can be represented by the Ball class and a line class needs to be created which will represent the edges of the mesh. Connecting the Edgeds left and tight outer coordinates to the node center coordinates should create a position constrained mesh object.

---

## Verlet Integrator

With a given previous position of a particle and the current position of a particle we can propagte our particle through time and space with the verlet integrator.

$$x(t+\Delta t) = 2*x(t) - x(t-\Delta t)+a\Delta t^2$$

In the `Object.py` file the propagation of the particle is done in the `update()` function.

The previous position of the particle was chosen to be smaller than the initial postion of the circle and stored in the `self.prev_pos` list. Position [0] contains the x coordinate and position [1] the y coordinate.

### Propagation

1. Calculate x and y velocity
2. Update previous position with current position
3. Calculate future position by propagating the current position with the velocity
4. Propagate particle
   
### Boundary Conditions

If the boundary conditions are met the particle will be set to a base value and the previous positions will be adjusted by the sum of the base value and the previous velocity with some value for energy loss due to the impact.

## Pygame

Pygame has a few notable "features" first of all are all the positions of the rectangles stored as integere values. Float values wont have an impact in the over positions of the rectangle. Furthermore, would the use of of the bottom or the top of the rectangle at the boundary be more sensible but currently the code only works with center value. The reason for that will be investigated in the future.


