# Manimations

Some experiments with manim math animations.

## Dependencies

-   [manim](https://www.manim.community/)
-   [numpy](https://numpy.org/)
-   recommended (optional): [Manim Sideview](https://marketplace.visualstudio.com/items?itemName=Rickaym.manim-sideview) VS Code Extension

## Build & Run

to enter venv: `source env/bin/activate`
to leave venv: `deactivate`

to build the animation: `manim -pql <filename>.py <ClassName>`
for example: `manim -pql hermite2.py HermiteCurve`

this will build an .mp4 file of the specified animation

## Disclaimer

No warranties provided. Code may not work. It is very likely that there are better ways to implement the same animations - this is the way it worked for me.
