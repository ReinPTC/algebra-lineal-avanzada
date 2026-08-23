# Guía de Estudio y Plan de Trabajo para Alumnos: Unidad 4

**Unidad de Aprendizaje:** Álgebra Lineal Avanzada  
**Institución:** Instituto Politécnico Nacional (IPN) — Escuela Superior de Física y Matemáticas (ESFM)  
**Texto Base Obligatorio:** Stephen H. Friedberg, Arnold J. Insel & Lawrence E. Spence, *Álgebra lineal* (1ra Edición en español, Publicaciones Cultural / CECSA / Prentice-Hall, México, 1982).  

---

## 🎯 Objetivos de Aprendizaje de la Unidad 4

Al finalizar esta unidad, el alumno será capaz de:
1. Representar transformaciones lineales mediante matrices relativas a bases ordenadas arbitrarias y calcular matrices de cambio de base.
2. Determinar si un operador lineal o matriz es diagonalizable calculando sus multiplicidades algebraicas y geométricas, y construyendo bases de eigenvectores.
3. Descomponer espacios vectoriales en subespacios $T$-invariantes y representar operadores en sumas directas de bloques diagonales.
4. Aplicar el **Teorema de Cayley-Hamilton** para anular matrices y operadores, y calcular el **polinomio mínimo** $p(t)$.
5. Determinar la **Forma Canónica de Jordan** $J$ de cualquier matriz u operador cuyo polinomio característico se escinda, utilizando diagramas de puntos (*dot diagrams*), construyendo bases canónicas de Jordan $\beta$ formadas por ciclos de eigenvectores generalizados y hallando la matriz invertible de paso $Q$ tal que $J = Q^{-1}AQ$.

---

## 📅 Cronograma y Ruta de Estudio Semanal

| Sesión | Tema Principal | Secciones Friedberg | Teoremas Clave | Entregables y Prácticas |
| :---: | :--- | :--- | :--- | :--- |
| **1** | **Bases ordenadas y Representación Matricial** | §2.2 (pp. 76–83), §2.5 (pp. 100–108) | Teoremas 1 al 14 | Cálculo de $[T]_\beta^\gamma$ para operadores diferenciales e integrales en $P_n(\mathbb{R})$. |
| **2** | **Diagonalizabilidad y Eigenspacios** | §5.1 (pp. 245–259), §5.2 (pp. 263–277) | Teoremas 15 al 31 | Determinación de multiplicidades algebraicas $m_\lambda$ y geométricas $\dim(E_\lambda)$. |
| **3** | **Subespacios Invariantes y Restricciones** | §5.4 (pp. 297–304) | Teoremas 32 al 34 | Descomposición en sumas directas $V = W_1 \oplus \dots \oplus W_k$ y matrices por bloques. |
| **4** | **Subespacios Cíclicos y Cayley-Hamilton** | §5.5 (pp. 305–310) | Teoremas 35 y 36 | Verificación de $f(A) = O$ y cálculo de inversas de matrices mediante $A^{-1} = -\frac{1}{a_0}(A^{n-1} + \dots + a_1 I)$. |
| **5** | **Polinomio Mínimo y Criterio de Diagonalización** | §5.6 (pp. 311–318) | Teoremas 37 al 41 | Cálculo de $p(t)$ a partir de $f(t)$ y verificación de diagonalizabilidad mediante raíces simples. |
| **6** | **Eigenvectores Generalizados y Ciclos** | §6.1 (pp. 327–342) | Teoremas 42 al 46 | Construcción de eigenspacios generalizados $K_\lambda$ y ciclos $\gamma = \{(T-\lambda I)^{p-1}x, \dots, x\}$. |
| **7** | **Diagramas de Puntos y Forma Canónica de Jordan** | §6.2 (pp. 339–359) | Teoremas 47 al 49 | Construcción de $J$, diagramas de puntos, base $\beta$ y matriz invertible $Q$ tal que $J = Q^{-1}AQ$. |

---

## 📝 Ejercicios Seleccionados de Friedberg para Tareas

### Bloque 1: Subespacios Invariantes y Cayley-Hamilton (§5.4 y §5.5)
1. Sea $T: \mathbb{R}^3 \to \mathbb{R}^3$ definido por $T(a, b, c) = (a + b, b + c, 0)$. Demuestre que $W = \operatorname{span}(\{e_1, e_2\})$ es $T$-invariante y calcule el polinomio característico de $T_W$.
2. Utilice el Teorema de Cayley-Hamilton para calcular $A^4$ y $A^{-1}$ para la matriz:
   $$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}.$$
3. Demuestre que si $T^2 = T$ (operador de proyección), entonces el polinomio mínimo de $T$ es $p(t) = t(t - 1)$ (si $T \neq 0$ y $T \neq I$).

### Bloque 2: Polinomio Mínimo (§5.6)
4. Calcule el polinomio característico y el polinomio mínimo de la matriz:
   $$A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}.$$
   ¿Es $A$ diagonalizable? Justifique su respuesta mediante el Teorema 41 (Friedberg 5.33).
5. Demuestre que si $A^k = O$ para algún $k \ge 1$ (matriz nilpotente), entonces $p(t) = t^m$ para algún $m \le k$, y el único eigenvalor de $A$ es $\lambda = 0$.

### Bloque 3: Forma Canónica de Jordan (§6.1 y §6.2)
6. Para la matriz:
   $$A = \begin{pmatrix} 3 & 1 & -2 \\ -1 & 0 & 5 \\ -1 & -1 & 4 \end{pmatrix}$$
   calcule su polinomio característico, los eigenspacios generalizados $K_\lambda$, el diagrama de puntos de cada eigenvalor y su Forma Canónica de Jordan $J$.
7. Halle una base canónica de Jordan $\beta$ y una matriz invertible $Q$ tal que $J = Q^{-1}AQ$ para la matriz:
   $$A = \begin{pmatrix} 2 & -4 & 2 & 2 \\ -2 & 0 & 1 & 3 \\ -2 & -2 & 3 & 3 \\ -2 & -6 & 3 & 7 \end{pmatrix}.$$
8. Dadas las matrices $3 \times 3$:
   $$A = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 1 \\ 0 & 0 & 2 \end{pmatrix}, \qquad B = \begin{pmatrix} 2 & 1 & 0 \\ 0 & 2 & 0 \\ 0 & 0 & 2 \end{pmatrix}$$
   explique por qué $A$ y $B$ tienen el mismo polinomio característico y el mismo polinomio mínimo pero **no son similares**.

---

## 💻 Herramientas Computacionales y Plataforma Interactiva

Se recomienda a los alumnos hacer uso continuo de la plataforma web interactiva del curso (`index.html`) para:
- Explorar visualmente los diagramas de puntos de Jordan.
- Interactuar con los simuladores de bases ordenadas y transformaciones lineales.
- Contrastar cálculos analíticos manuales con las soluciones paso a paso detalladas en los Ejemplos 50 a 54.
