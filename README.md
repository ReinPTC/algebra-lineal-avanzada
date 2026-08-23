# Libro Digital Interactivo: Álgebra Lineal Avanzada

**Institución:** Instituto Politécnico Nacional (IPN) — Escuela Superior de Física y Matemáticas (ESFM)  
**Unidad de Aprendizaje:** Álgebra Lineal Avanzada  
**Texto Base Obligatorio:** Stephen H. Friedberg, Arnold J. Insel, Lawrence E. Spence, *Álgebra lineal* (1ra Edición, México, 1982 / Publicaciones Cultural).

---

## 🎯 Descripción del Proyecto
Este repositorio contiene la plataforma digital interactiva (Progressive Web App - PWA) y el entorno computacional de notas para el curso de **Álgebra Lineal Avanzada**, enfocado en la **Unidad 4: Similaridad y Operadores Normales**.

### Contenido y Estructura Pedagógica:
- **Tema 4.0.1 (Preliminares):** 2.2 Representación matricial de una transformación lineal (Friedberg, págs. 76–78).
  - Concepto de *Base Ordenada* y distinción formal ($\beta \neq \gamma$).
  - *Vector Coordenado* $[x]_\beta$ relativo a una base ordenada.
  - Construcción y definición formal de la matriz $[T]_\beta^\gamma$ que representa a una transformación lineal $T: V \to W$.
  - Ejemplos detallados de cálculo: Derivación polinomial $T(f)=f'$ ($P_3 \to P_2$) y transformaciones $\mathbb{R}^2 \to \mathbb{R}^3$.
- **4.1 Teorema de Cayley-Hamilton:** Polinomios característicos y anulación de operadores.
- **4.2 Similaridad y Matrices Diagonales:** Espacios unitarios, matrices unitarias y hermitianas.
- **4.3 Forma Canónica de Jordan:** Teorema espectral, subespacios $T$-invariantes, operadores nilpotentes y bloques de Jordan.
- **Visualizadores y Simuladores Interactivos:** Herramientas reactivas para cálculo de vectores coordenados y productos matriciales de transformaciones lineales.

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
