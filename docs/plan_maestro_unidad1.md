# Plan Maestro Curricular: Unidad 1 — Transformaciones Ortogonales y Productos Internos

**Unidad de Aprendizaje:** Álgebra Lineal Avanzada  
**Institución:** Instituto Politécnico Nacional (IPN) — Escuela Superior de Física y Matemáticas (ESFM)  
**Programa Académico:** Licenciatura en Matemática Algorítmica (Semestre III)  
**Texto Base Principal para la Unidad 1:** John T. Moore, *Elements of Linear Algebra and Matrix Theory* (McGraw-Hill, Cap. 4: Inner-Product Spaces).  
**Textos Complementarios Obligatorios:**  
1. Stephen H. Friedberg, Arnold J. Insel & Lawrence E. Spence, *Álgebra lineal* (1ra Edición en español, Publicaciones Cultural, México, 1982).  
2. Kenneth Hoffman & Ray Kunze, *Linear Algebra* (2nd Edition, Prentice-Hall, 1971).  

**Unidad de Competencia Oficial (Programa IPN, Hoja 3 de 8):**  
> *Determina transformaciones ortogonales y productos internos de los espacios vectoriales a partir de matrices definidas positivas.*

---

## 1. Mapeo Curricular Oficial del IPN $\longleftrightarrow$ Secciones del Texto Base (Moore, Cap. 4)

```
UNIDAD TEMÁTICA I: TRANSFORMACIONES ORTOGONALES Y PRODUCTOS INTERNOS (26.5 Horas Totales: 16.5 T + 3.0 P + 7.0 AA)
│
├── Tema 1.0: Espacios Euclidianos Generales (Fundamento Métrico y Geométrico)
│   └── Moore §4.2 General Euclidean Spaces (pp. 186–193)
│       ├── Axiomática formal del producto interno en espacios vectoriales reales (simetría, linealidad, positividad)
│       ├── Ejemplos canónicos y no estándar: producto euclidiano en R^n, integrales en C[a,b] y P_n, producto deformado en R^2
│       ├── Productos internos inducidos por operadores no singulares (X, Y)_T = (TX, TY)
│       ├── Longitud (norma), ángulo, ortogonalidad y distancia métrica d(α, β) = ||α - β||
│       ├── Teorema de Pitágoras generalizado (Moore Teorema 2.1)
│       ├── Desigualdad de Cauchy-Schwarz (Moore Lema)
│       └── Desigualdad del Triángulo (Moore Teorema 2.2)
│
├── Tema 1.1: Complementos Ortogonales (3.0 T, 1.0 P, 1.0 AA)
│   └── Moore §4.4 Orthogonal Complements (pp. 199–205)
│       ├── Coordenadas de Fourier relativas a bases ortonormales
│       ├── Expansiones en polinomios ortogonales de Legendre normalizados en [-1, 1]
│       ├── Definición del complemento ortogonal W^⊥ de un subespacio W
│       ├── Teorema Fundamental de Descomposición Ortogonal V = W ⊕ W^⊥ (Moore Teorema 4.1)
│       ├── Unicidad de W^⊥ y propiedad de involución (W^⊥)^⊥ = W
│       └── Proyecciones ortogonales y principio de mínima distancia (mejor aproximación)
│
├── Tema 1.2: Transformaciones y Matrices Ortogonales (4.5 T, 1.0 AA)
│   └── Moore §4.5 Orthogonal Transformations (pp. 206–212)
│       ├── Isometrías y movimientos rígidos en espacios euclidianos
│       ├── Definición de operador ortogonal: preservación de normas y productos internos (Tα, Tβ) = (α, β)
│       ├── Invertibilidad y el Grupo Ortogonal O(V) como subgrupo de GL(V)
│       ├── Caracterización Matricial de Operadores Ortogonales (Moore Teorema 5.1):
│       │   ├── Ortonormalidad de columnas en R^n
│       │   ├── A^(-1) = A^T (ortonormalidad de renglones)
│       │   └── det(A) = ±1: Clasificación en Rotaciones (det = +1) y Reflexiones (det = -1)
│       ├── Teorema de Representación Inversa de Matrices Ortogonales (Moore Teorema 5.2)
│       └── Clasificación explícita de operadores ortogonales en R y R^2
│
├── Tema 1.3: Funcionales Lineales y Operadores Adjuntos (3.0 T, 1.0 P, 2.0 AA)
│   └── Moore §4.6 Linear Functionals and Adjoints (pp. 213–220)
│       ├── Teorema de Representación de Riesz en Espacios Euclidianos (Moore Teorema 6.1)
│       ├── 1.3.1 El Operador Adjunto T*:
│       │   ├── Existencia y unicidad del operador adjunto (Moore Teorema 6.2): (Tα, β) = (α, T*β)
│       │   ├── Representación matricial en bases ortonormales: [T*]_β = [T]_β^T (Moore Teorema 6.3)
│       │   ├── Álgebra y propiedades fundamentales de los adjuntos (Moore Teorema 6.4)
│       │   └── Relaciones de ortogonalidad del núcleo e imagen: N(T*) = R(T)^⊥, R(T*) = N(T)^⊥
│       └── 1.3.2 Operadores Autoadjuntos:
│           ├── Definición T = T* y su correspondencia con matrices simétricas A = A^T
│           ├── Operadores de multiplicación y proyecciones ortogonales
│           └── Realidad de eigenvalores y ortogonalidad de eigenspacios
│
└── Tema 1.4: Productos Internos y Operadores Positivos (6.0 T, 1.0 P, 3.0 AA)
    └── Moore §4.7 Inner Products and Positive Operators (pp. 221–228)
        ├── 1.4.1 Operadores y Matrices Definidas Positivas:
        │   ├── Definición operacional de operador positivo: autoadjunto con (Tα, α) > 0 para α ≠ 0
        │   ├── Teorema de Caracterización de Productos Internos por Operadores Positivos (Moore Teorema 7.1)
        │   ├── Descomposición Cuadrática Operacional T = U* U con U invertible (Moore Teorema 7.2)
        │   ├── Formas cuadráticas asociadas X^T A X y matrices definidas positivas
        │   └── Factorización Matricial de Cholesky A = Q^T Q con Q no singular (Moore Corolario)
        ├── 1.4.2 Matrices Definidas Positivas y Definidas Negativas:
        │   ├── Espectro positivo vs. espectro negativo (criterio de eigenvalores)
        │   └── Criterio de Sylvester por determinantes de menores principales dirigentes
        ├── 1.4.3 Matrices Semidefinidas Positivas e Indefinidas:
        │   ├── Caracterización por signos de formas cuadráticas y eigenvalores mixtos
        │   └── Ejemplos geométricos y matriciales en R^2 y R^3
        └── 1.4.4 Caracterización de Productos Internos en Términos de Matrices Positivas:
            ├── Construcción general: ⟨X, Y⟩_A = Y^T A X con A simétrica y definida positiva
            ├── Matrices de Gram G = [ (v_i, v_j) ] de bases ordenadas y su positividad estricta
            └── Análisis de positividad en operadores de rotación (restricción a θ = 2kπ)
```

---

## 2. Matriz Curricular de Contenidos Teóricos y Secuencia de Teoremas

| Bloque Temático | Contenidos Teóricos Clave | Teoremas de la Secuencia Oficial | Referencia Exacta Moore / Friedberg |
| :--- | :--- | :--- | :--- |
| **Tema 1.0: Espacios Euclidianos Generales** | Axiomas de producto interno real, espacios euclidianos, productos estándar y no estándar, integrales de funciones continuas, normas $\|\alpha\|$, ángulos $\cos\theta$, métrica euclidiana $d(\alpha, \beta)$. | **Teorema 1.0.1** (Teorema de Pitágoras generalizado)<br>**Lema 1.0.1** (Desigualdad de Cauchy-Schwarz)<br>**Teorema 1.0.2** (Desigualdad del Triángulo) | Moore §4.2 (pp. 186–193)<br>Friedberg §6.1 |
| **Tema 1.1: Complementos Ortogonales** | Coordenadas respecto a bases ortonormales, polinomios de Legendre, definición del complemento ortogonal $W^\perp$, proyección ortogonal $P_W$ y teorema de mejor aproximación. | **Teorema 1.1.1** (Descomposición en Suma Directa Ortogonal $V = W \oplus W^\perp$ y unicidad de $W^\perp$)<br>**Proposición 1.1.1** (Propiedad involutiva $(W^\perp)^\perp = W$ y dimensiones) | Moore §4.4 (pp. 199–205)<br>Friedberg §6.2 |
| **Tema 1.2: Transformaciones y Matrices Ortogonales** | Isometrías, operadores que preservan longitud y producto interno, grupo ortogonal $O(V)$, matrices ortogonales ($A^T A = I$). Rotaciones y reflexiones en $\mathbb{R}^2$. | **Teorema 1.2.1** (Caracterización matricial: columnas/renglones ortonormales y $\det A = \pm 1$)<br>**Teorema 1.2.2** (Toda matriz ortogonal representa un operador ortogonal en base ortonormal) | Moore §4.5 (pp. 206–212)<br>Friedberg §6.5 |
| **Tema 1.3: Funcionales Lineales y Adjuntos** | Espacio dual $V^*$, teorema de Riesz, operador adjunto $T^*$, álgebra de adjuntos, ortogonalidad núcleo-imagen ($N(T^*) = R(T)^\perp$), operadores autoadjuntos y matrices simétricas. | **Teorema 1.3.1** (Teorema de Representación de Riesz)<br>**Teorema 1.3.2** (Existencia y Unicidad del Operador Adjunto $T^*$)<br>**Teorema 1.3.3** (Representación matricial $[T^*]_\beta = [T]_\beta^T$)<br>**Teorema 1.3.4** (Propiedades algebraicas de los adjuntos) | Moore §4.6 (pp. 213–220)<br>Friedberg §6.3 |
| **Tema 1.4: Productos Internos y Operadores Positivos** | Operadores autoadjuntos positivos, correspondencia biunívoca con productos internos, descomposición $T = U^* U$, formas cuadráticas $X^T A X$, matrices simétricas definidas positivas, factorización $A = Q^T Q$, matrices semidefinidas e indefinidas, matrices de Gram. | **Teorema 1.4.1** (Caracterización de productos internos por operadores positivos únicos $\langle \alpha, \beta \rangle = (T\alpha, \beta)$)<br>**Teorema 1.4.2** ($T$ es positivo $\iff T = U^* U$ con $U$ invertible)<br>**Corolario 1.4.1** ($A$ es positiva $\iff A = Q^T Q$ con $Q$ no singular)<br>**Teorema 1.4.3** (Criterio espectral y menores principales de Sylvester) | Moore §4.7 (pp. 221–228)<br>Friedberg §6.4 |

---

## 3. Plan de Evaluación y Actividades Docentes

1. **Sesiones Teórico-Conceptuales (16.5 Horas con Docente):**
   - Exposición rigurosa de la geometría abstracta del producto interno, deducción de desigualdades universales (Cauchy-Schwarz, Minkowski), caracterización del operador adjunto mediante Riesz y teoría espectral de operadores positivos.
2. **Talleres Prácticos y Computacionales (3.0 Horas de Práctica):**
   - Construcción de bases ortonormales mediante Gram-Schmidt, cálculo de complementos ortogonales de subespacios dados por ecuaciones o generadores, cálculo de matrices ortogonales y verificación de descomposiciones de Cholesky $A = Q^T Q$ en Python/NumPy.
3. **Aprendizaje Autónomo (7.0 Horas AA):**
   - Demostraciones analíticas de las propiedades del adjunto, resolución de ejercicios teóricos sobre matrices semidefinidas e indefinidas, y uso de los simuladores interactivos de la plataforma digital para explorar formas cuadráticas y matrices de Gram.
