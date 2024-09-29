# py-attractors
Some attractors

## Chaos Theory in plain words

*Chaos theory* is about studying dynamics systems which can be described in a deterministic way and yet exhibit great variability when slightly changing initial conditions.

Some of those systems, despite their chaotic nature, display patterns and repeating behaviours.

## Lorenz attractor

Lorenz attractor is described by the following equations:

$$
\begin{cases}
\frac{dx}{dt} = \sigma (y - x) \\
\frac{dy}{dt} = x (\rho - z) - y \\
\frac{dz}{dt} = xy - \beta z
\end{cases}
$$

Where:
- $\sigma$ is the Prandtl number
- $\rho$ is the Rayleigh number
- $\beta$ is a number related to the geometry of the system