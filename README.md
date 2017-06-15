# lparser-python
A turtle graphics parser/visualizer for 2D L-Systems written in python 3 and QT 5.

## Usage
Simply run `python3 lparseqt.py`.

## Sample L-Systems

### Hilbert Curve
    Axiom: -BF+AFA+FB-
    Variables:
    A=-BF+AFA+FB-
    B=+AF-BFB-FA+

### Koch Curve
    Axiom: FA
    Variables: A=A+FA-FA-FA+FA

### Sierpinski's Arrowhead Approximation
    Axiom: FA
    Variables:
    A=+FB-FA-FB+
    B=-FA+FB+FA-
