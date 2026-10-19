# -*- coding: utf-8 -*-
"""
Generador de Contenido: Banco de Ejercicios y Problemas de la Unidad 1
Basado en Moore Cap. 4 y programa ESFM-IPN.
Formato visual homologado al 100% con Tema 4.0.1 y Tema 4.1.
Usa raw string r'''...''' para preservar intactas todas las barras invertidas de KaTeX.
"""

def get_ejercicios_u1_html():
    return r'''
        <!-- =====================================================================
           BANCO DE PROBLEMAS Y EJERCICIOS: UNIDAD 1 (ESFM - IPN)
        ====================================================================== -->
        <section id="sec-1-ejercicios-unidad-1" class="topic-section">
          <h2>
            <span>Banco de Ejercicios y Problemas: Unidad 1</span>
            <span class="ref-badge" style="width: fit-content;">ESFM — IPN • Evaluación & Taller Práctico</span>
          </h2>

          <p class="section-intro">
            Conjunto exhaustivo de problemas teórico-demostrativos y numérico-computacionales para consolidar la unidad de competencia en transformaciones ortogonales y productos internos.
          </p>

          <!-- BLOQUE 1: ESPACIOS EUCLIDIANOS GENERALES -->
          <div class="math-box box-ex">
            <div class="math-box-header">Bloque I: Espacios Euclidianos Generales y Desigualdades (Moore §4.2)</div>
            <ol style="line-height: 1.8; padding-left: 1.5rem;">
              <li>
                <strong>Identidad del Paralelogramo:</strong> Demuestre que en todo espacio euclidiano real $V$, cualesquiera vectores $\alpha, \beta \in V$ satisfacen:
                $$\|\alpha + \beta\|^2 + \|\alpha - \beta\|^2 = 2\|\alpha\|^2 + 2\|\beta\|^2.$$
                Demuestre además que la norma proviene de un producto interno si y sólo si satisface la identidad del paralelogramo (Teorema de Jordan-von Neumann).
              </li>
              <li>
                <strong>Identidad de Polarización Real:</strong> Pruebe que para todo par de vectores en un espacio euclidiano real:
                $$\langle \alpha, \beta \rangle = \frac{1}{4} \left( \|\alpha + \beta\|^2 - \|\alpha - \beta\|^2 \right).$$
              </li>
              <li>
                <strong>Verificación de Positividad en Formas Bilineales:</strong> Determine si la asignación
                $$\langle \alpha, \beta \rangle = x_1 y_1 - 2x_1 y_2 - 2x_2 y_1 + 5x_2 y_2$$
                define un producto interno en $\mathbb{R}^2$. En caso afirmativo, calcule la norma de $\alpha = (3, 1)^T$ y el ángulo entre $\alpha = (1, 0)^T$ y $\beta = (0, 1)^T$ en esta métrica.
              </li>
              <li>
                <strong>Producto Interno en Matrices $M_{n \times n}(\mathbb{R})$:</strong> Pruebe que la traza define un producto interno sobre el espacio de matrices cuadradas mediante $\langle A, B \rangle = \operatorname{tr}(B^T A) = \sum_{i=1}^n \sum_{j=1}^n a_{ij} b_{ij}$. Calcule la norma de la matriz de permutación $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$.
              </li>
            </ol>
          </div>

          <!-- BLOQUE 2: COMPLEMENTOS ORTOGONALES Y PROYECCIÓN -->
          <div class="math-box box-ex">
            <div class="math-box-header">Bloque II: Complementos Ortogonales y Proyecciones (Moore §4.4)</div>
            <ol style="line-height: 1.8; padding-left: 1.5rem;">
              <li>
                En $\mathbb{R}^4$ con el producto euclidiano usual, sea $W = \operatorname{span}\{(1, 1, 0, 1)^T, (2, 1, 1, 0)^T\}$.
                <ul style="margin-top: 0.25rem;">
                  <li>Determine una base ortonormal para $W$.</li>
                  <li>Encuentre una base ortonormal para el complemento ortogonal $W^\perp$.</li>
                  <li>Calcule la proyección ortogonal del vector $\alpha = (1, 2, 3, 4)^T$ sobre $W$ y sobre $W^\perp$, y verifique que $\alpha = P_W(\alpha) + P_{W^\perp}(\alpha)$.</li>
                  <li>Calcule la distancia euclidiana de $\alpha$ al subespacio $W$: $d(\alpha, W) = \|\alpha - P_W(\alpha)\|$.</li>
                </ul>
              </li>
              <li>
                Sean $W_1$ y $W_2$ subespacios de dimensión finita de un espacio euclidiano $V$. Demuestre rigurosamente las siguientes identidades de dualidad ortogonal:
                $$(W_1 + W_2)^\perp = W_1^\perp \cap W_2^\perp, \qquad (W_1 \cap W_2)^\perp = W_1^\perp + W_2^\perp.$$
              </li>
            </ol>
          </div>

          <!-- BLOQUE 3: OPERADORES Y MATRICES ORTOGONALES -->
          <div class="math-box box-ex">
            <div class="math-box-header">Bloque III: Operadores y Matrices Ortogonales (Moore §4.5)</div>
            <ol style="line-height: 1.8; padding-left: 1.5rem;">
              <li>
                Considere la matriz $A = \frac{1}{3} \begin{pmatrix} 2 & 1 & 2 \\ -2 & 2 & 1 \\ -1 & -2 & 2 \end{pmatrix}$.
                <ul style="margin-top: 0.25rem;">
                  <li>Compruebe analíticamente que $A^T A = I_3$.</li>
                  <li>Calcule $\det(A)$ y determine si representa una rotación propia o una rotación con reflexión.</li>
                  <li>Si es una rotación pura, determine el eje invariante de rotación resolviendo $(A - I)X = 0$ y el ángulo de giro $\theta$ a partir de la traza: $\operatorname{tr}(A) = 1 + 2\cos \theta$.</li>
                </ul>
              </li>
              <li>
                Demuestre que si $\lambda$ es un eigenvalor real de una matriz ortogonal $A$, entonces forzosamente $\lambda = 1$ o $\lambda = -1$.
              </li>
            </ol>
          </div>

          <!-- BLOQUE 4: OPERADORES ADJUNTOS Y POSITIVOS -->
          <div class="math-box box-ex">
            <div class="math-box-header">Bloque IV: Operadores Adjuntos y Matrices Definidas Positivas (Moore §4.6 & §4.7)</div>
            <ol style="line-height: 1.8; padding-left: 1.5rem;">
              <li>
                Sea $T: V \to V$ un operador lineal en un espacio euclidiano. Demuestre que:
                <ul style="margin-top: 0.25rem;">
                  <li>$T^* T$ y $T T^*$ son operadores autoadjuntos y semidefinidos positivos.</li>
                  <li>$\ker(T^* T) = \ker(T)$ y $\operatorname{rango}(T^* T) = \operatorname{rango}(T)$.</li>
                  <li>$T^* T$ es estrictamente positivo si y sólo si $T$ es invertible.</li>
                </ul>
              </li>
              <li>
                <strong>Criterio de Sylvester y Factorización de Cholesky:</strong> Considere la matriz simétrica:
                $$A = \begin{pmatrix} 4 & 2 & -2 \\ 2 & 10 & 2 \\ -2 & 2 & 6 \end{pmatrix}.$$
                <ul style="margin-top: 0.25rem;">
                  <li>Calcule los menores principales dirigentes $\Delta_1, \Delta_2, \Delta_3$ y confirme que $A$ es definida positiva.</li>
                  <li>Encuentre explícitamente una matriz triangular superior $Q$ con diagonal positiva tal que $A = Q^T Q$.</li>
                  <li>Use la matriz $A$ para calcular el producto interno inducido $\langle X, Y \rangle_A = X^T A Y$ para $X = (1, 0, -1)^T$ y $Y = (2, 1, 0)^T$.</li>
                </ul>
              </li>
              <li>
                <strong>Positividad en Operadores Ortogonales:</strong> Sea $T$ una transformación ortogonal en un espacio euclidiano. Demuestre que si $T$ es además un operador positivo, entonces forzosamente $T = I$ (el operador identidad).
              </li>
            </ol>
          </div>
        </section>
    '''
