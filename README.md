# Libro Digital Interactivo: Álgebra Lineal Avanzada

**Institución:** Instituto Politécnico Nacional (IPN) — Escuela Superior de Física y Matemáticas (ESFM)  
**Unidad de Aprendizaje:** Álgebra Lineal Avanzada  
**Texto Base Obligatorio:** Stephen H. Friedberg, Arnold J. Insel, Lawrence E. Spence, *Álgebra lineal* (1ra Edición, México, 1982 / Publicaciones Cultural).

---

## 🎯 Descripción del Proyecto
Este repositorio contiene la plataforma digital interactiva (Progressive Web App - PWA) y el entorno computacional de notas para el curso de **Álgebra Lineal Avanzada** de la Escuela Superior de Física y Matemáticas (ESFM — IPN).

### Unidades Disponibles:

#### 📐 Unidad 1: Transformaciones Ortogonales y Productos Internos (IPN - ESFM)
*Texto base: John T. Moore, Elements of Linear Algebra and Matrix Theory (Cap. 4) & Friedberg (Cap. 6)*
- **Tema 1.0 (Espacios Euclidianos Generales):** Axiomas del producto interno real, espacios $C[a, b]$ y deformados en $\mathbb{R}^2$, productos inducidos por operadores $(X, Y)_T = (TX, TY)$, norma, ortogonalidad, Teorema de Pitágoras generalizado, Desigualdad de Cauchy-Schwarz y Desigualdad del Triángulo (Minkowski).
- **Tema 1.1 (Complementos Ortogonales):** Expansión de Fourier en bases ortonormales, polinomios de Legendre, definición y propiedades del complemento ortogonal $W^\perp$, Teorema de Descomposición $V = W \oplus W^\perp$, involución $(W^\perp)^\perp = W$, proyecciones ortogonales $P_W$ y teorema de mejor aproximación.
- **Tema 1.2 (Transformaciones y Matrices Ortogonales):** Isometrías rígidas, operadores ortogonales, caracterización matricial $A^T A = I_n$, determinante $\det(A) = \pm 1$, Teorema de representación inversa, clasificación en $\mathbb{R}^2$ (rotaciones y reflexiones) y **Simulador Interactivo de Isometrías en $\mathbb{R}^2$**.
- **Tema 1.3 (Funcionales Lineales y Adjuntos):** Teorema de Representación de Riesz, definición y existencia del operador adjunto $T^*$, representación matricial en bases ortonormales $[T^*]_\beta = [T]_\beta^T$, álgebra de adjuntos, teorema de ortogonalidad núcleo-imagen ($\ker(T^*) = (\operatorname{Im} T)^\perp$) y operadores autoadjuntos.
- **Tema 1.4 (Productos Internos y Operadores Positivos):** Caracterización de productos internos por operadores positivos $\langle \alpha, \beta \rangle = (T\alpha, \beta)$, descomposición cuadrática $T = U^* U$, factorización de Cholesky $A = Q^T Q$, matrices simétricas definidas positivas y negativas (Criterio de Sylvester por menores principales dirigentes), matrices semidefinidas e indefinidas, matrices de Gram y **Simulador Interactivo de Matrices Positivas & Producto $A$-Interno**.
- **Banco de Problemas y Ejercicios U1:** Problemas teórico-demostrativos y talleres computacionales por cada tema.

#### 🔄 Unidad 4: Similaridad y Operadores Normales
*Texto base: Stephen H. Friedberg et al., Álgebra lineal (Cap. 2 & Cap. 5)*
- **Tema 4.0.1 (Preliminares):** 2.2 Representación matricial de una transformación lineal. Base ordenada, vector coordenado $[x]_\beta$, matriz $[T]_\beta^\gamma$, ejemplos de derivación y multiplicaciones matriciales.
- **4.1 Teorema de Cayley-Hamilton:** Polinomios característicos y anulación de operadores.
- **4.2 Similaridad y Matrices Diagonales:** Espacios unitarios, matrices unitarias y hermitianas.
- **4.3 Forma Canónica de Jordan:** Teorema espectral, subespacios $T$-invariantes, operadores nilpotentes y bloques de Jordan.

---

## 📁 Estructura del Repositorio

```
Algebra-Lineal-Avanzada/
│
├── index.html                   # Aplicación Web Interactiva Principal (PWA)
├── manifest.json                # Web App Manifest (PWA instalable)
├── sw.js                        # Service Worker para funcionamiento 100% offline
├── requirements.txt             # Dependencias de Python (NumPy, SciPy, Matplotlib, SymPy)
│
├── css/
│   └── main.css                 # Sistema de diseño, temas dark/light, tarjetas matemáticas
│
├── js/
│   ├── app.js                   # Lógica de navegación, búsqueda en tiempo real y temas
│   └── interactive_tools.js     # Simuladores y calculadores de Álgebra Lineal Avanzada
│
└── Material U4/
    └── U4.JPG                   # Temario Oficial de la Unidad IV (IPN)
```

---

## 🚀 Despliegue y Ejecución en Servidor Local

Para visualizar el libro interactivo en el navegador de manera local:

1. Inicia un servidor HTTP local en Python:
```bash
python -m http.server 8000
```
2. Abre en tu navegador la URL:
```
http://localhost:8000
```

---

## 📚 Bibliografía Oficial del IPN

1. **Friedberg, S. H., Insel, A. J. & Spence, L. E. (1982)**. *Álgebra lineal* (1ra ed. en español), Publicaciones Cultural / CECSA / Prentice-Hall, México. *(Texto Base Obligatorio)*.
2. **Hoffman, K. & Kunze, R. (1971)**. *Linear Algebra* (2nd ed.), Prentice-Hall.
3. **Lang, S. (1987)**. *Linear Algebra* (3rd ed.), Springer.
4. **Strang, G. (2016)**. *Introduction to Linear Algebra* (5th ed.), Wellesley-Cambridge Press.
5. **Axler, S. (2015)**. *Linear Algebra Done Right* (3rd ed.), Springer.
