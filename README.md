# Algebra & Trigonometry


## 0. Environtment Setting

### 0.1 Jupyter Lab Installation
- Install python at [python.org](https://python.org)
- Install following python modules from the terminal
    - `pip install sympy`
    - `pip install numpy`
    - `pip install matplotlib`
    - `pip install jupyterlab`
    - `pip install qtconsole`
    - `pip install ipywidgets`
    - `pip install ipympl`
- Run `jupyter-lab` from the terminal
    - `jupyter-lab`

### 0.2 Interactive Matplotlib 
- Test the following code from `jupyter-lab` in one cell.

```
%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

y = [1, 4, 9, 16, 25,36,49, 64]
x1 = [1, 16, 30, 42,55, 68, 77,88]
x2 = [1,6,12,18,28, 40, 52, 65]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
l1=ax.plot(x1, y,'ys-')
l2=ax.plot(x2, y,'go--') 
ax.legend(labels=('tv', 'Smartphone'), loc='upper left')
plt.savefig("sales.png")
```




## 1. Prerequisites

### 1.1 Real Numbers: Algebra Essentials

- The natural number set
$$\mathbb{N} = \lbrace 1, 2, 3,  \dots \rbrace$$

- The whole number set
$$\mathbb{W} = \lbrace 0, 1, 2, 3, \dots \rbrace = \lbrace 0 \rbrace \cup \mathbb{N}$$

- The integer set
$$\mathbb{Z} = \lbrace \dots, -3, 2, 1, 0, 1, 2, 3,  \dots \rbrace$$

- The rational number set
$$\mathbb{Q} = \big\lbrace \frac{p}{q} \;\vert\; p, q \in \mathbb{Z}, q \neq 0 \big\rbrace$$

- A raltional number can be either a termnating decimal or a repeating decimal.

- The irrational number set
$$\mathbb{Q}^{\prime} = \lbrace h \;\vert\; h \not\in \mathbb{Q} \rbrace$$

- A irrational number is neither a terminating nor a repeating decimal.

- The real number set: $\mathbb{R} = \mathbb{Q} \cup \mathbb{Q}^{\prime}$

- The real number line: by Cantor-Dedekind axiom, any real number corresponds to a unique position on the number line. 

- The exponential notation $a^n$ where $a \in \mathbb{R}$ (the base) and $n \in \mathbb{N}$ (the exponent)
$$ a^n = \underbrace{a \cdot a \cdot \cdots \cdot a}_{n \text{ times}} $$

- The commutative property of addition
$$ a + b = b + a $$

- The commutative property of multiplication
$$ a \cdot b = b \cdot a $$

- The associative property of addition
$$ a + (b + c) = (a + b) + c $$

- The associative property of multiplication
$$ a (b c) = a (b c) $$

- The distributive property
$$ a \cdot (b + c) = a \cdot b + a \cdot c $$

- the order of operations

- The identity property of addition
$$ a + 0 = a $$

- The identity property of multiplication
$$ a \cdot 1 = a $$

- The inverse property of addition
$$ a + (-a) = 0 $$
    - The subtraction as the addition of the inverse: $a - b = a + (-b)$.

- The inverse property of multiplication where $a \neq 0$
$$ a \cdot \dfrac{1}{a} = 1 $$
    - The division as the multiplication of the inverse: $ a \div b = a \cdot \dfrac{1}{b}$ for $b \neq 0$. 

- A constant, a variable, an algebraic expresstion 

- An equation, a formula

- 🎯 `jupyter-lab` practice
    - Use `sympy`'s `simplify()`.
    - See **Sympy Tutorial**: 12. SymPy ― Simplification 



### 1.2 Exponents and Scientific Notation

- The product rule of exponents where $a \in \mathbb{R}$, $m, n \in \mathbb{N}$
$$ a^{m} \cdot a^{n} = a^{m + n} $$

- The quotient rule of exponent where $a \in \mathbb{R}$ and $a \neq 0$, $m, n \in \mathbb{N}$ and $m > n$
$$ \dfrac{a^m}{a^n} = a^{m - n} $$

- The power rule of exponents where $a \in \mathbb{R}$  
$$ (a^m)^n  =a^{m \cdot n} $$

- The zero exponent rule of exponents where $a \in \mathbb{R}$ and $a \neq 0$
$$ a^0 = 1 $$

- The negative rule of exponents where $a \in \mathbb{R}$ and $a \neq 0$, $n \in \mathbb{N}$
$$ a^{-n} = \dfrac{1}{a^n} $$

- The power of a product rule of exponents where $a, b \in \mathbb{R}$, $n \in \mathbb{Z}$
$$ (ab)^n = a^n b^n $$

- The power of a quotient rule of exponents where $a, b \in \mathbb{R}$ and $b \neq 0$, $n \in \mathbb{Z}$
$$ \left( \dfrac{a}{b} \right)^n = \dfrac{a^n}{b^n}  $$

- `sympy` practice
    - Use `sympy`'s `powsimp()`, and so on.
    - See **Sympy Tutorial**: 12. SymPy ― Simplification 



### 1.3 Radicals and Rational Expressions

- The principal square root of $a$ where $a \in \mathbb{R}_{+}$ (the nonnegative real number set)
$$ \sqrt{a} $$

- The product rule for simplifying square roots where $a, b \in \mathbb{R}_{+}$
$$ \sqrt{ab} = \sqrt{a} \cdot \sqrt{b} $$

- The quotient rule for simplifying square roots where $a, b \in \mathbb{R}_{+}$ and $b \neq 0$
$$ \sqrt{\dfrac{a}{b}} = \dfrac{\sqrt{a}}{\sqrt{b}} $$

- It's good to know that for $a \in \mathbb{R}$
$$ \sqrt{a^2} = \vert a \vert = \begin{cases} a, \;a \geq 0 \\ -a, \;a < 0 \end{cases} $$

- The principal $n$th root of $a$ where $n \in \mathbb{N}$ and $n \geq 2$
$$ \sqrt[n]{a} $$
and $a \in \mathbb{R}_{+}$ when $n$ is even, $a \in \mathbb{R}$ when $n$ is odd.  

- The rational exponent where $a \in \mathbb{R}_{+}$, $m, n \in \mathbb{N}$ and $n \geq 2$
$$ a^{\frac{m}{n}} = \left( \sqrt[n]{a} \right)^m = \sqrt[n]{a^m} $$

- 🎯 `jupyter-lab` practice
    - Use `sympy`'s `Rational()`, and so on.
    - See **Sympy Tutorial**: 4. SymPy ― Numbers




### 1.4 Polynomials

- Polynomials
$$ a_n x^n + a_{n - 1} x^{n - 1} + \cdots + a_1 x + a_0 $$

- Perfect square trinomials
$$ (x + a)^2 = (x + a) (x + a) = x^2 + 2x + a^2 $$


- Difference of squares
$$ (a + b)(a - b) = a^2 - b^2 $$

- 🎯 `jupyter-lab` practice
    - Use `sympy`'s `factor()`, `expand()`.
    - See **Sympy Tutorial**: 12. SymPy ― Simplification 



### 1.5 Factoring Polynomials

- The greatest common factor (GCF): the largest polynomial that divides evenly into the 
polynomials.

- Factoring a trinomial with leading coefficient 1
$$ x^2 + bx + c = (x + p)(x + q) $$
where $pq = c$ and $p + q = b$ for $a, b \in \mathbb{Z}$

- Factor by grouping
$$ a x^2 + bx + c = (a^{\prime} x + b^{\prime})(c^{\prime} x + d^{\prime}) $$
where $a = a^{\prime} c^{\prime}$, $b = a^{\prime}d^{\prime} + b^{\prime}c^{\prime}$, $c = b^{\prime}d^{\prime}$.

- Perfect square trinomials
$$ a^2 + 2ab + b^2 = (a + b)^2 $$

- Differences of squares
$$ a^2 - b^2 = (a + b)(a - b) $$

- Sum of cubes
$$ a^3 + b^3 = (a + b)(a^2 - ab + b^2) $$

- Difference of cubes
$$ a^3 - b^3 = (a - b)(a^2 + ab + b^2) $$

- 🎯 `jupyter-lab` practice
    - Use `sympy`'s `factor()`, `expand()`.
    - See **Sympy Tutorial**: 12. SymPy ― Simplification 




### 1.6 Rational Expressions

- The least common denominator (LCD): the smallest multiple that the denominators have in common

- 🎯 `jupyter-lab` practice
    - Use `sympy`'s `cancel()`.
    - See **Sympy Tutorial**: 12. SymPy ― Simplification 





## 2. Equations and Inequalities


### 2.1 The Rectangular Coordinate Systems and Graphs

- The Cartesian (or rectangular) coordinate system 
    - A two-dimensional plane
    - $x$-axis (horizontal), $y$-axis (vertical)
    - A point in the plane corresponds to an ordered pair $(x, y)$
    - An equation like $y = 2x - 1$ means the collection of all $(x, y)$ that satisfies the equation.

- 🎯 `jupyter-lab` practice
    - See **Matplotlib Tutorial**: 6. Matplotlib – Simple Plot

```
%matplotlib widget
import matplotlib.pyplot as plt

x = [-3, -2, -1, 0, 1, 2, 3, 4] 
y = [-7, -5, -3, -1, 1, 3, 5, 7]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x, y)
ax.axhline(0, color='gray')
ax.axvline(0, color='gray')
plt.xlim([-5, 5])
plt.ylim([-7, 7])
plt.title("Example 2. Figure 6")
```

- The $x$-intercept: set $y = 0$ and solve the equation with respect to $x$
- The $y$-intercept: set $y = 0$ and solve the equation with respect to $x$

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 6. SymPy ― Substitution
    - See **Sympy Tutorial**: 18. SymPy ― Solver

```
from sympy import symbols, Eq, solveset

x, y = symbols('x, y')

expr = Eq(y, -3*x - 4)
expr

expr1 = expr.subs(y, 0)
expr1

x_intercept = solveset(expr1, x)
x_intercept

expr2 = expr.subs(x, 0)
expr2

y_intercept = solveset(expr2, y)
y_intercept
```

- The distance formula: given endpoints $(x_1, y_1)$ and $(x_2, y_2)$, the distance between two points
$$ d = \sqrt{ (x_2 - x_1)^2 + (y_2 - y_1)^2 } $$

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 3. SymPy ― Symbolic Computation

```
from sympy import symbols, sqrt

x1, x2, y1, y2 = symbols('x1, x2, y1, y2')

x1 = -3
y1 = -1
x2 = 2
y2 = 3

d = sqrt( (x2 - x1)**2 + (y2 - y1)**2 )
d
```

- The midpoint fomula: given endpoints $(x_1, y_1)$ and $(x_2, y_2)$, the midpoint is 
$$ \left( \dfrac{x_1 + x_2}{2}, \dfrac{y_1 + y_2}{2} \right) $$

- 🎯 `jupyter-lab` practice
    - See **Matplotlib Tutorial**: 8. Matplotlib – Object-oriented Interface

```
%matplotlib widget
import matplotlib.pyplot as plt

x1, x2, y1, y2 = -3, 2, -1, 3
xm, ym = (x1 + x2)/2, (y1 + y2)/2

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot([x1, x2], [y1, y2])
ax.scatter([x1, x2], [y1, y2])
ax.scatter(xm, ym)
plt.title("Figure 16")
```




### 2.2 Linear Equations in One Variable

- The linear equation in one variable
$$ ax + b = 0 $$
where $a, b \in \mathbb{R}$ and $a \neq 0$.

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 6. SymPy ― Substitution
    - See **Sympy Tutorial**: 18. SymPy ― Solver

```
from sympy import symbols, Eq, solveset
x = symbols('x')
solveset( Eq( 4*(x -3) + 12, 15 - 5*(x + 6) ), x )
```

- The rational equation: the variable appears in the denominators

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 4. SymPy ― Numbers

```
# Example 5
from sympy import symbols, Rational, Eq, solveset
x = symbols('x')
solveset( Eq( 1/x, Rational(1,10) - 3/(4*x)), x ) 
```

- The slope of a line, $m$, for given two points, $(x_1, y_1)$ and $(x_2, y_2)$
$$ m = \dfrac{y_2 - y_1}{x_2 - x_1} $$

- The point-slope formula: the line of slope $m$ that passes $(x_1, y_1)$
$$ y − y_1 = m(x − x_1)  $$

- The vertical line
$$ x = c $$

- The horizontal line
$$ y = c $$

- The line in the standard form
$$ ax + by = c $$

- The parallel lines: the same slope and different $y$-intercepts

- The Lines that are perpendicular intersect to form a $90^\circ$-angle
$$ m_1 \cdot m_2 = -1 $$
where $m_1$ and $m_2$ are the slopes.

- 🎯 `jupyter-lab` practice
    - See **Matplotlib Tutorial**: 6. Matplotlib – Simple Plot

```
# Figure 5
%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-7, 7, 0.01)
y1 = 3*x - 1
y2 = (-1/3)*x - 2

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x, y1, x, y2)
plt.gca().set_aspect('equal', adjustable='box')
```



### 2.3 Models and Applications
> Homework





### 2.4 Complex Numbers

- The imaginary unit number
$$ i = \sqrt{-1} $$
such that 
$$ i^2 = \left( \sqrt{-1} \right)^2 = -1 $$

- The pure imaginary number
$$b i$$
where $b \in \mathbb{R}$, such as $3i, -i, \sqrt{2}i$ and so on.

- The complex number
$$ a + bi $$
where $a \in \mathbb{R}$ is the real part and $b \in \mathbb{R}$ is the imaginary part.

- The complex number set
$$ \mathbb{C} = \lbrace z \;\vert\; z = a + bi \rbrace $$
where $a,b \in \mathbb{R}, i = \sqrt{-1}$.

- The real number set $\mathbb{R}$ is a subset of the complex number set $\mathbb{C}$, that is $\mathbb{R} \subset \mathbb{C}$.

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 4. SymPy ― Numbers
    - See **Sympy Tutorial**: 16. SymPy ― Function class

```
from sympy import sqrt, re, im

i = sqrt(-1)
i

i**2

a, b = 4, 5
z = a + b*i
z

re(z)

im(z)
```

- The complex number $a + bi$ is represented as a point $(a, b)$ in the complex plane just like $(x, y)$ in the $xy$-plane.

- 🎯 `jupyter-lab` practice
    - See **Matplotlib Tutorial**: 6. Matplotlib – Simple Plot

```
import matplotlib.pyplot as plt
import numpy as np

# numpy uses j as the imaginary unit
data = np.array([1+2j, 2-4j, -2j, -4, 4+1j, 3+8j, -2-6j, 5])

x = data.real
y = data.imag
  
plt.plot(x, y, 'g*')
plt.ylabel('Imaginary')
plt.xlabel('Real')
```

- The addition of $a + bi$ and $c + di$
$$ (a + bi) + (c + di) = (a + c) + (b + d)i $$

- The subtraction of $a + bi$ and $c + di$
$$ (a + bi) - (c + di) = (a - c) + (b - d)i $$

- The product of $a + bi$ and $c + di$
$$(a + bi)(c + di) = (ac − bd) + (ad + bc)i^2$$

- The complex conjugate of $(a + bi)$
$$ a - bi $$

- the product of $(a + bi)$ and $(a - bi)$
$$(a + bi)(a - bi) = a^2 + b^2 $$

- the division of $(c + di)$ by $(a + bi)$
$$ \dfrac{c + di}{a + bi} = \dfrac{(ac + bd) + (ad - bc)i}{a^2 + b^2} $$
where $a, b \neq 0$.

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 12. SymPy ― Simplification

```
from sympy import sqrt, simplify

a, b, c, d = 1, 2, 3, 4
i = sqrt(-1)

z1 = a + b*i
z1

z2 = c + d*i
z2

z1 + z2

z1 - z2

simplify(z1 * z2)

simplify(z2 / z1)

conjugate(z1)

conjugate(z2)

i**3

i**4

i**5
```



### 2.5 Quadratic Equations

- The zero-product property
$$ \text{if } a \cdot b = 0, \text{ then } a = 0 \text{ or } b = 0 $$
where $a, b \in \mathbb{R}$ or they can be mathematical expressions.

- The quadratic equation
$$ ax^2 + bx + c = 0 $$
where $a, b, c \in \mathbb{R}$ and $a \neq 0$.

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 18. SymPy ― Solvers

```
from sympy import symbols, factor, Eq, solveset

x = symbols('x')
expr = x**2 + x - 6
expr

factor(expr)

equation = Eq(expr, 0)
equation

solveset(equation)
```

- 🎯 `jupyter-lab` practice
    - See **Matplotlib Tutorial**: 6. Matplotlib – Simple Plot
    
```
%matplotlib widget
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-6, 6, 0.01)
y = x**2 + x - 6

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(x, y)
plt.title("Figure 2")
plt.gca().set_aspect('equal', adjustable='box')
plt.xlim(-6, 6)
plt.ylim(-7, 7)
```

- The square root property
$$ \text{if } x^2 = k, \text{ then } x = \pm\sqrt{k} $$
where $k \in \mathbb{R}$ and $k \neq 0$.

- Completing the square: adjust the quadratic equation to make a perfect square trinomial on one side of the equal sign
$$ (ax + b)^2 = k $$


- The quadratic formula: for $ax^2 + bx + c = 0$, the solutions are
$$ x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$
where $a, b, c \in mathbb{R}$ and $a \neq 0$.

- 🎯 `jupyter-lab` practice
    - See **Sympy Tutorial**: 18. SymPy ― Solvers

```
from sympy import symbols, Eq, solveset

x = symbols('x')
expr = x**2 + x - 6
expr

eqn = Eq(x**2 + 5*x + 1, 0)
eqn

solutions = solveset(eqn)
solutions

ordered_solutions = list(solutions)
ordered_solutions

x1 = ordered_solutions[0]
x1

x2 = ordered_solutions[1]
x2
```



### 2.6 Other Types of Equations

### 2.7 Linear Inequalities and Absolute Value Inequaltities





## 3. Functions

### 3.1 Functions and Function Notations

### 3.2 Domain and Range

### 3.3 Rate of Change and Behavior of Graphs

### 3.4 Composition of Functions

### 3.5 Transformation of Functions

### 3.6 Absolute Value Functions

### 3.7 Inverse Functions

### Chapter 3 Review
### Chapter 3 Review Excercises
### Chapter 3 Practical Test



## 4. Linear Functions

### 4.1 Linear Functions

### 4.2 Modeling with Linear Functions

### 4.3 Fitting Linear Models to Data

### Chapter 4 Review
### Chapter 4 Review Excercises
### Chapter 4 Practical Test



## 5. Polynomial and Rational Functions

### 5.1 Quadratic Functions

### 5.2 Power Functions and Polynomial Functions

### 5.3 Graphs of Polynomial Functions

### 5.4 Dividing Polynomials

### 5.5 Zeros of Polynomial Functions

### 5.6 Rational Functions

### 5.7 Inverses and Radical Functions

### 5.8 Modeling Using Variation


### Chapter 5 Review
### Chapter 5 Review Excercises
### Chapter 5 Practical Test


## 6. Exponential and Logarithmic Functions

### 6.1 Exponential Functions

### 6.2 Graphs of Exponential Functions

### 6.3 Logarithmic Functions

### 6.4 Graphs of Logarithmic Functions

### 6.5 Logarithmic Properties

### 6.6 Exponential and Logarithmic Equations

### 6.7 Exponential and Logarithmic Models

### 6.8 Fitting Exponential Models to Data

### Chapter 6 Review
### Chapter 6 Review Excercises
### Chapter 6 Practical Test


## 7. The Unit Circle: Sine and Cosine Functions

### 7.1 Angles

### 7.2 Right Triangle Trigonometry

### 7.3 Unit Circle

### 7.4 The Other Trigonometric Functions

### Chapter 7 Review
### Chapter 7 Review Excercises
### Chapter 7 Practical Test


## 8. Periodic Functions

### 8.1 Graphs of the Sine and Cosine Functions

### 8.2 Graphs of Other Trigonometric Functions

### 8.3 Inverse Trigonometric Functions

### Chapter 8 Review
### Chapter 8 Review Excercises
### Chapter 8 Practical Test


## 9. Trigonometric Identities and Equations

### 9.1 Solving Trigonometric Equations with Identities

### 9.2 Sum and Difference Identities

### 9.3 Double-Angle, Half-Angle, and Reduction Formulas

### 9.4 Sum-to-Product and Product-to-Sum Formulas

### 9.5 Solving Trigonometric Equations

### Chapter 9 Review
### Chapter 9 Review Excercises
### Chapter 9 Practical Test



## 10. Further Applications of Trigonometry

### 10.1 Non-right Triangles: Law of Sines

### 10.2 Non-right Triangles: Law of Cosines

### 10.3 Polar Coordinates

### 10.4 Polar Coordinates: Graphs

### 10.5 Polar Form of Complex Numbers

### 10.6 Parametric Equations

### 10.7 Parametric Equations: Graphs

### 10.8 Vectors


### Chapter 10 Review
### Chapter 10 Review Excercises
### Chapter 10 Practical Test


## 11. Systems of Equations and Inequalities

### 11.1 Systems of Linear Equations: Two Variables

### 11.2 Systems of Linear Equations: Three Variables

### 11.3 Systems of Nonlinear Equations and Inequalities: Two Variables

### 11.4 Partial Fractions

### 11.5 Matrices and Matrix Operations

### 11.6 Solving Systems with Gaussian Elimination

### 11.7 Solving Systems with Inverses

### 11.8 Solving Systems with Cramer's Rule

### Chapter 11 Review
### Chapter 11 Review Excercises
### Chapter 11 Practical Test


## 12. Analytic Geometry

### 12.1 The Ellipse

### 12.2 The Hyperbola

### 12.3 The Parabola

### 12.4 Rotation of Axis

### 12.5 Conic Sections in Polar Coordinates

### Chapter 12 Review
### Chapter 12 Review Excercises
### Chapter 12 Practical Test



## 13. Sequences, Probability and Counting Theory

### 13.1 Sequences and Their Notations

### 13.2 Arithmetic Sequences

### 13.3 Geometric Sequences

### 13.4 Series and Their Notations

### 13.5 Counting Principles

### 13.6 Binomial Theorem

### 13.7 Probability

### Chapter 13 Review
### Chapter 13 Review Excercises
### Chapter 13 Practical Test
