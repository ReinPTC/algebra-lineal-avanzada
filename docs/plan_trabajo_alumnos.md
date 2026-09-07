# Guía de Estudio y Plan de Trabajo para Alumnos: Unidad 4

**Unidad de Aprendizaje:** Álgebra Lineal Avanzada  
**Institución:** Instituto Politécnico Nacional (IPN) — Escuela Superior de Física y Matemáticas (ESFM)  
**Texto Base Obligatorio:** Stephen H. Friedberg, Arnold J. Insel & Lawrence E. Spence, *Álgebra lineal* (1ra Edición en español, Publicaciones Cultural / CECSA / Prentice-Hall, México, 1982).  
**Plataforma Oficial del Curso:** Libro Digital Interactivo (`index.html` / GitHub Pages)

---

## 🎯 Objetivos de Aprendizaje de la Unidad 4

Al completar esta unidad y el estudio del Libro Digital Interactivo, el alumno será capaz de:
1. **Representar Transformaciones Lineales:** Construir matrices de transformación $[T]_\beta^\gamma$ respecto a bases ordenadas arbitrarias y aplicar matrices de cambio de base para transformaciones similares ($B = Q^{-1}AQ$).
2. **Evaluar Diagonalizabilidad:** Calcular polinomios característicos $f(t)$, eigenvalores y eigenspacios $E_\lambda = N(T - \lambda I)$, contrastando la multiplicidad geométrica ($\dim(E_\lambda)$) frente a la algebraica ($m_\lambda$) para determinar si un operador o matriz es diagonalizable.
3. **Analizar Subespacios Invariantes:** Descomponer espacios vectoriales mediante operadores restricción $T_W$, sumas directas $V = W_1 \oplus \dots \oplus W_k$ y representaciones diagonales por bloques $A_1 \oplus \dots \oplus A_k$.
4. **Dominar el Teorema de Cayley-Hamilton y Polinomio Mínimo:** Anular operadores y matrices mediante sus polinomios característicos ($f(T) = T_0$, $f(A) = O$), y calcular el polinomio mínimo $p(t)$ para verificar diagonalizabilidad por factores lineales simples.
5. **Construir la Forma Canónica de Jordan:** Determinar la forma canónica de Jordan $J$, construir diagramas de puntos (*dot diagrams*), ensamblar bases canónicas de Jordan $\beta$ formadas por ciclos de eigenvectores generalizados y calcular la matriz invertible de paso $Q$ tal que $J = Q^{-1}AQ$.

---

## 📖 Mapeo Directo: Guía de Estudio $\longleftrightarrow$ Libro Digital Interactivo

Todas las lecturas, definiciones, teoremas y ejemplos para esta unidad están integrados de manera correlativa### 🔹 Módulo 4.0.1: Bases Ordenadas y Representación Matricial (Friedberg §2.2 y §2.5)
* **Sección en Libro Digital:** `sec-4-0-1`
* **Conceptos Fundamentales:** Base ordenada ($\beta \neq \gamma$), vector coordenado $[x]_\beta$, matriz de transformación $[T]_\beta^\gamma$, y teorema de cambio de base $[T]_\beta = Q^{-1}[T]_\alpha Q$.
* **Teoremas del Libro Digital:** Teoremas 4.0.1 al 4.0.7.
* **Ejemplos Resueltos Paso a Paso:** Ejemplos 1 al 11 (Operador derivada $P_3 \to P_2$, matrices asociadas, transformaciones $\mathbb{R}^2 \to \mathbb{R}^3$, cambio de base y similaridad).
* **Herramienta Interactiva:** *Simulador Interactivo de Coordenadas y Representación Matricial*.

### 🔹 Módulo 4.0.2: Polinomios, Divisibilidad y Operadores (Friedberg §1.2 y Apéndice E)
* **Sección en Libro Digital:** `sec-4-0-2`
* **Conceptos Fundamentales:** Algoritmo de la división, teorema del factor, coprimalidad, polinomios mónicos e irreducibles, factorización única y evaluación en operadores y matrices.
* **Teoremas del Libro Digital:** Teoremas 4.0.8 al 4.0.17.
* **Ejemplos Resueltos Paso a Paso:** Ejemplos 12 al 16.

### 🔹 Módulo 4.0.3: Diagonalizabilidad, Eigenvalores y Eigenspacios (Friedberg §5.1 y §5.2)
* **Sección en Libro Digital:** `sec-4-0-3`
* **Conceptos Fundamentales:** Polinomio característico $f(t) = \det(A - tI)$, eigenvalores $\lambda$, eigenvectores, eigenspacio $E_\lambda = N(T - \lambda I)$, multiplicidad algebraica ($m_\lambda$) y geométrica ($\dim(E_\lambda)$), sumas directas $V = E_{\lambda_1} \oplus \dots \oplus E_{\lambda_k}$.
* **Teoremas del Libro Digital:** Teoremas 4.0.18 al 4.0.31 (Criterio fundamental de diagonalizabilidad).
* **Ejemplos Resueltos Paso a Paso:** Ejemplos 17 al 34 (Matrices diagonalizables vs. no diagonalizables, potencias y sistemas dinámicos).

### 🔹 Módulo 4.1: Subespacios Invariantes, Teorema de Cayley-Hamilton y Polinomio Mínimo (Friedberg §5.4, §5.5 y §5.6)
* **Sección en Libro Digital:** `tema-4-1`
* **Subespacios Invariantes (§5.4):**
  * Definición de $W$ $T$-invariante, operador restricción $T_W: W \to W$.
  * **Teoremas 4.1.1, 4.1.2 y 4.1.3:** Divisibilidad $\det(T_W - tI) \mid \det(T - tI)$, factorización en sumas directas $f(t) = f_1(t)\cdots f_k(t)$, y representación $[T]_\beta = [T_{W_1}]_{\beta_1} \oplus \dots \oplus [T_{W_k}]_{\beta_k}$.
  * **Ejemplos 35, 36 y 37:** Factorizaciones y matrices bloque diagonal en $\mathbb{R}^4$ y $M_{6 \times 6}(\mathbb{R})$.
* **El Teorema de Cayley-Hamilton (§5.5):**
  * Subespacio $T$-cíclico $C_x = \operatorname{span}(\{x, T(x), T^2(x), \dots\})$, bases cíclicas y matriz compañera $C(p)$.
  * **Teoremas 4.1.4 y 4.1.5:** **Teorema de Cayley-Hamilton** ($f(T) = T_0$ y $f(A) = O$).
  * **Ejemplos 38, 39, 40 y 41:** Verificación operacional y matricial en $M_{2 \times 2}(\mathbb{R})$ y $P_2(\mathbb{R})$.
* **El Polinomio Mínimo (§5.6):**
  * Definición de $p(t)$ (polinomio mónico de grado mínimo que anula a $T$).
  * **Teoremas 4.1.6 al 4.1.10:** Unicidad y divisibilidad $p(t) \mid f(t)$, coincidencia espectral ($f$ y $p$ tienen las mismas raíces), y **Criterio Espectral de Diagonalizabilidad** ($T$ es diagonalizable $\iff p(t)$ se escinde en factores lineales distintos).
  * **Ejemplos 42 al 47:** Cálculo de $p(t)$, operadores nilpotentes, matrices con $A^2 - 3A + 2I = O$ y $A^3 = A$.

### 🔹 Módulo 4.3: La Forma Canónica de Jordan (Friedberg §6.1 y §6.2)
* **Sección en Libro Digital:** `tema-4-3`
* **Eigenvectores Generalizados (§6.1):**
  * Bloque de Jordan $J_p(\lambda)$, eigenvector generalizado $(T - \lambda I)^p(x) = 0$, ciclo de Jordan $\gamma$, y eigenspacio generalizado $K_\lambda = \bigcup N((T - \lambda I)^p)$.
  * **Teoremas 4.3.1 al 4.3.5:** Independencia lineal de ciclos, descomposición primaria $V = K_{\lambda_1} \oplus \dots \oplus K_{\lambda_k}$, $\dim(K_{\lambda_i}) = m_i$, y estabilización en $N((T - \lambda_i I)^{m_i})$.
  * **Ejemplos 48 y 49:** Cálculo de ciclos en $\mathbb{C}^3$ y $P_2(\mathbb{C})$.
* **Forma Canónica de Jordan y Diagramas de Puntos (§6.2):**
  * Planteamiento general y convención de ordenamiento por longitudes decrecientes $p_1 \ge p_2 \ge \dots \ge p_k$.
  * **Ejemplo 50 (Ejemplo 4 Friedberg):** Estructura matricial de $A_i$ de $9 \times 9$ con 4 bloques y su diagrama de puntos.
  * **Teorema 4.3.6 (Friedberg 6.6):** Puntos en renglones y relación $\text{número de bloques} = \dim(E_{\lambda_i}) = \operatorname{nulidad}(T - \lambda_i I)$.
  * **Teorema 4.3.7 (Friedberg 6.7):** Fórmulas de rango ($r_1 = n - \operatorname{rango}(T - \lambda_i I)$, $r_j = \operatorname{rango}((T - \lambda_i I)^{j-1}) - \operatorname{rango}((T - \lambda_i I)^j)$) y **Unicidad de Jordan**.
  * Definición de Forma de Jordan de una Matriz ($J = Q^{-1}AQ$).
  * **Ejemplo 51 (Ejemplo 5 Friedberg):** Algoritmo completo de Jordan, base $\beta$ y matriz $Q$ para matriz $4 \times 4$ ($f(t) = (t-2)^3(t-3)$).
  * **Ejemplo 52 (Ejemplo 6 Friedberg):** Jordan con múltiples bloques para matriz $4 \times 4$ ($f(t) = (t-2)^2(t-4)^2$), resolución de $(A - 4I)x_1 = w$, base $\beta$ y matriz $Q$.
  * **Ejemplo 53 (Ejemplo 7 Friedberg):** Forma de Jordan del operador derivada parcial en polinomios en dos variables.
  * **Teorema 4.3.8 (Friedberg 6.8):** **Criterio Fundamental de Similaridad Matricial:**
    $$A \sim B \iff A \text{ y } B \text{ tienen exactamente la misma Forma Canónica de Jordan } J$$
  * **Ejemplo 54 (Ejemplo 8 Friedberg):** Clasificación de similaridad de matrices $3 \times 3$ mediante $J$.

---

## 📝 Banco de Tareas y Actividades de Evaluación

Los alumnos deberán resolver los siguientes problemas basándose en los procedimientos desarrollados en el Libro Digital:

1. **Subespacios Invariantes y Restricción:**
   * Siguiendo el método del **Ejemplo 35**, sea $T: \mathbb{R}^3 \to \mathbb{R}^3$ con $T(x_1, x_2, x_3) = (2x_1 + x_2, 2x_2, 3x_3)$. Demuestre que $W = \operatorname{span}(\{e_1, e_2\})$ es $T$-invariante, calcule $[T_W]_{\beta_1}$ y verifique el **Teorema 4.1.1 (Friedberg 5.24)** sobre la divisibilidad de polinomios característicos.

2. **Teorema de Cayley-Hamilton e Inversión:**
   * Siguiendo el **Ejemplo 40**, para la matriz $A = \begin{pmatrix} 1 & 4 \\ 2 & 3 \end{pmatrix}$, verifique formalmente que $f(A) = O$. Utilice dicha ecuación matricial para despejar y calcular $A^{-1}$ y $A^3$ sin realizar multiplicaciones directas repetidas.

3. **Polinomio Mínimo y Diagonalizabilidad:**
   * Siguiendo los **Ejemplos 42, 45 y 46**, determine el polinomio característico $f(t)$ y el polinomio mínimo $p(t)$ de la matriz:
     $$A = \begin{pmatrix} 3 & 0 & 0 \\ 0 & 2 & 0 \\ 0 & 1 & 2 \end{pmatrix}.$$
   * Aplique el **Teorema 4.1.10 (Friedberg 5.33)** para justificar por qué $A$ no es diagonalizable.

4. **Diagramas de Puntos y Forma Canónica de Jordan:**
   * Siguiendo el algoritmo de los **Ejemplos 50, 51 y 52**, considere una matriz $A \in M_{5 \times 5}(\mathbb{R})$ con polinomio característico $f(t) = -(t - 3)^5$. Si $\operatorname{rango}(A - 3I) = 3$ y $\operatorname{rango}((A - 3I)^2) = 1$:
     * Calcule el número de puntos en cada renglón ($r_1, r_2, r_3$) aplicando el **Teorema 4.3.7 (Friedberg 6.7)**.
     * Dibuje el diagrama de puntos.
     * Determine las longitudes de los ciclos ($p_1, p_2, \dots$) y escriba la Forma Canónica de Jordan $J$.

5. **Cálculo de Matriz de Paso $Q$:**
   * Siguiendo el desarrollo paso a paso del **Ejemplo 52**, para la matriz:
     $$A = \begin{pmatrix} 2 & -4 & 2 & 2 \\ -2 & 0 & 1 & 3 \\ -2 & -2 & 3 & 3 \\ -2 & -6 & 3 & 7 \end{pmatrix}$$
     encuentre una base canónica de Jordan $\beta$, ensamble la matriz invertible $Q$ y verifique matricialmente que $QJ = AQ$.

---

## 💻 Recomendaciones de Uso del Libro Digital

* **Estudio Activo:** Revise cada teorema y analice su aplicación en el ejemplo correspondiente del libro interactivo antes de intentar resolver los ejercicios.
* **Búsqueda Rápida:** Utilice el buscador superior de la plataforma digital para localizar instantáneamente definiciones, teoremas por su número (ej. "Teorema 4.1.5", "Teorema 4.3.8") o ejemplos (ej. "Ejemplo 52").
* **Modo Offline:** La plataforma cuenta con *Service Worker* (PWA), por lo que puede guardarse como aplicación de escritorio o móvil y consultarse sin conexión a internet.
