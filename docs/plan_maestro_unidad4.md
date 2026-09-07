# Plan Maestro Curricular: Unidad 4 — Similaridad y la Forma Canónica de Jordan

**Unidad de Aprendizaje:** Álgebra Lineal Avanzada  
**Institución:** Instituto Politécnico Nacional (IPN) — Escuela Superior de Física y Matemáticas (ESFM)  
**Texto Base Oficial:** Stephen H. Friedberg, Arnold J. Insel & Lawrence E. Spence, *Álgebra lineal* (1ra Edición en español, Publicaciones Cultural / CECSA / Prentice-Hall, México, 1982).  
**Unidad de Competencia:** Analiza y construye las representaciones canónicas de operadores lineales y matrices en espacios de dimensión finita, determinando la estructura espectral, diagonalizabilidad, subespacios invariantes, anulación mediante el Teorema de Cayley-Hamilton, polinomio mínimo y la descomposición canónica de Jordan.

---

## 1. Mapeo Oficial: Temario del IPN $\longleftrightarrow$ Capítulos y Secciones de Friedberg

```
UNIDAD 4: SIMILARIDAD Y FORMA CANÓNICA DE JORDAN
├── 4.0 Preliminares: Representación Matricial y Diagonalizabilidad
│   ├── 4.0.1 Bases ordenadas y representación matricial [T]_β^γ (Friedberg §2.2, pp. 76–83)
│   ├── 4.0.2 Eigenvalores, eigenvectores y eigenspacios E_λ (Friedberg §5.1, pp. 245–259)
│   └── 4.0.3 Criterios de diagonalizabilidad y sumas directas (Friedberg §5.2, pp. 263–277)
│
├── 4.1 Teorema de Cayley-Hamilton y Polinomio Mínimo
│   ├── 4.1.1 Subespacios T-invariantes y suma directa de matrices (Friedberg §5.4, pp. 297–304)
│   ├── 4.1.2 Subespacios cíclicos y Teorema de Cayley-Hamilton (Friedberg §5.5, pp. 305–310)
│   └── 4.1.3 Polinomio mínimo y criterio de factores lineales distintos (Friedberg §5.6, pp. 311–318)
│
├── 4.2 Similaridad y Matrices Diagonales en Espacios Complejos
│   └── (Programado temáticamente para articulación con Operadores Normales y Teorema Espectral en Unidad 5)
│
└── 4.3 La Forma Canónica de Jordan
    ├── 4.3.1 Eigenvectores generalizados, ciclos y eigenspacios K_λ (Friedberg §6.1, pp. 327–342)
    └── 4.3.2 Diagramas de puntos, unicidad de Jordan y matriz de paso Q (Friedberg §6.2, pp. 339–359)
```

---

## 2. Matriz Curricular de Contenidos Teóricos y Secuencia de Teoremas

| Bloque Temático | Contenidos Teóricos Clave | Teoremas de la Secuencia Oficial | Referencia Exacta Friedberg (1ra Ed.) |
| :--- | :--- | :--- | :--- |
| **4.0.1 Representación Matricial** | Bases ordenadas $\beta, \gamma$, vector coordenado $[x]_\beta$, matriz de transformación $[T]_\beta^\gamma$, cambio de base y matrices similares $B = Q^{-1}AQ$. | Teoremas 4.0.1 al 4.0.7 (Álgebra matricial y cambios de base) | §2.2 (pp. 76–83), §2.5 (pp. 100–108) |
| **4.0.2 Polinomios y Operadores** | Aritmética de polinomios, algoritmo de la división, polinomios irreducibles, factorización única y evaluación en operadores $f(T)$ y matrices $f(A)$. | Teoremas 4.0.8 al 4.0.17 (Álgebra de polinomios y evaluación operacional) | §1.2, Apéndice E (pp. 410–418) |
| **4.0.3 Diagonalización** | Polinomio característico $f(t)=\det(A-tI)$, espectro $\sigma(T)$, eigenspacio $E_\lambda=N(T-\lambda I)$, criterios de diagonalización y sumas directas $V = E_{\lambda_1} \oplus \dots \oplus E_{\lambda_k}$. | Teoremas 4.0.18 al 4.0.31 (Criterios y teorema fundamental de diagonalizabilidad) | §5.1 (pp. 245–259), §5.2 (pp. 263–277) |
| **4.1.1 Subespacios Invariantes** | Subespacio $T$-invariante $W$, operador restricción $T_W: W \to W$, suma directa de operadores y matrices por bloques $A_1 \oplus \dots \oplus A_k$. | **Teorema 4.1.1** ($\det(T_W-tI)\mid \det(T-tI)$), **Teorema 4.1.2** ($f(t)=\prod f_i(t)$), **Teorema 4.1.3** ($[T]_\beta = \bigoplus [T_{W_i}]_{\beta_i}$) | §5.4 (pp. 297–304) |
| **4.1.2 Teorema de Cayley-Hamilton** | Subespacio $T$-cíclico $C_x = \operatorname{span}(\{T^j(x)\})$, base cíclica, matriz compañera $C(p)$, evaluación polinomial de operadores y matrices. | **Teorema 4.1.4** ($f_{T_W}(t)=(-1)^k p(t)$), **Teorema 4.1.5** (**Teorema de Cayley-Hamilton**: $f(T)=T_0$ y $f(A)=O$) | §5.5 (pp. 305–310) |
| **4.1.3 Polinomio Mínimo** | Polinomio mónico generador del ideal anulador $p(t)$, raíces de $p(t)$, grado en espacios cíclicos, y prueba espectral de diagonalizabilidad. | **Teorema 4.1.6** ($p\mid f$), **Teorema 4.1.7** ($p_T = p_{[T]_\beta}$), **Teorema 4.1.8** (coincidencia de raíces), **Teorema 4.1.9** ($\deg(p)=\dim(V)$), **Teorema 4.1.10** (diagonalizable $\iff p(t)$ producto de factores lineales simples) | §5.6 (pp. 311–318) |
| **4.3.1 Eigenvectores Generalizados** | Bloque de Jordan $J_p(\lambda)$, eigenvector generalizado $(T-\lambda I)^p(x)=0$, ciclo de Jordan $\gamma$, eigenspacio generalizado $K_\lambda$. | **Teorema 4.3.1** (Independencia de ciclos), **Teorema 4.3.2** ($K_\lambda$ subespacio), **Teorema 4.3.3** (Independencia espectral), **Teorema 4.3.4** (Existencia de base de Jordan), **Teorema 4.3.5** (Descomposición primaria $V=\bigoplus K_{\lambda_i}$) | §6.1 (pp. 327–342) |
| **4.3.2 Forma Canónica de Jordan** | Diagramas de puntos (*Dot Diagrams*), longitudes decrecientes $p_1 \ge \dots \ge p_k$, algoritmos de cálculo de rangos, base canónica $\beta$ y matriz de paso $Q$. | **Teorema 4.3.6** (Puntos = $\operatorname{nulidad}((T-\lambda I)^r)$), **Teorema 4.3.7** (Fórmulas de rango y Unicidad de Jordan), **Teorema 4.3.8** (**Criterio Fundamental de Similaridad**: $A \sim B \iff J_A = J_B$) | §6.2 (pp. 339–359) |

---

## 3. Plan de Evaluación y Actividades Docentes

1. **Sesiones Teórico-Conceptuales:**
   - Exposición sistemática de los conceptos y teoremas sin demostración pesada en clase, priorizando el significado operacional, geométrico y algebraico.
2. **Talleres de Cálculo Matricial y Computacional:**
   - Cálculo manual y algorítmico del polinomio mínimo $p(t)$, verificación de Cayley-Hamilton para matrices $3 \times 3$ y $4 \times 4$, y construcción completa de diagramas de puntos de Jordan.
3. **Prácticas Interactivas:**
   - Uso de la plataforma web interactiva del curso (`index.html`) para visualizar transformaciones, multiplicidades y diagramas de puntos en tiempo real.

---

## 4. Bibliografía Oficial del IPN

1. **Friedberg, S. H., Insel, A. J. & Spence, L. E. (1982)**. *Álgebra lineal* (1ra edición en español). Publicaciones Cultural / CECSA / Prentice-Hall, México. **(Texto Base Obligatorio)**.
2. **Hoffman, K. & Kunze, R. (1971)**. *Linear Algebra* (2nd ed.), Prentice-Hall.
3. **Lang, S. (1987)**. *Linear Algebra* (3rd ed.), Springer-Verlag.
4. **Strang, G. (2016)**. *Introduction to Linear Algebra* (5th ed.), Wellesley-Cambridge Press.
5. **Axler, S. (2015)**. *Linear Algebra Done Right* (3rd ed.), Springer.
