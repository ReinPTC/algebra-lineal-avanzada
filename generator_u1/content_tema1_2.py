# -*- coding: utf-8 -*-
r"""
Generador de Contenido: Tema 1.2 Transformaciones y Matrices Ortogonales
Texto base: John T. Moore §4.5 (pp. 206-212) & Friedberg §6.5
Contiene la correspondencia exacta 1-a-1 de los 2 ejemplos canónicos del libro de Moore (§4.5 pp. 209-211)
con la notación unificada de corchetes angulares \langle \alpha, \beta \rangle.
Formato visual homologado al 100% con Tema 4.0.1 y Tema 4.1.
"""

def get_tema_1_2_html():
    return r'''
        <!-- =====================================================================
           TEMA 1.2: TRANSFORMACIONES Y MATRICES ORTOGONALES (MOORE §4.5)
        ====================================================================== -->
        <section id="tema-1-2" class="topic-section">
          <h2>
            <span>Tema 1.2. Transformaciones y Matrices Ortogonales</span>
            <span class="ref-badge" style="width: fit-content;">Moore §4.5 (Páginas 206–212) & Friedberg §6.5</span>
          </h2>

          <p class="section-intro">
            Una transformación geométrica que preserva distancias y ángulos en un espacio euclidiano constituye una <strong>isometría</strong> (movimiento rígido). En esta sección formalizamos axiomáticamente los <strong>operadores ortogonales</strong>, demostramos su equivalencia con la conservación de normas mediante la identidad de polarización, establecemos su caracterización matricial $A^T A = I_n$ y su clasificación según $\det(A) = \pm 1$ (rotaciones y reflexiones), integrando los desarrollos originales de Moore en 1D y 2D junto con un simulador interactivo reactivo.
          </p>

          <!-- -----------------------------------------------------------------
             ISOMETRÍAS Y DEFINICIÓN DE OPERADOR ORTOGONAL
          ------------------------------------------------------------------ -->
          <div id="sec-1-2-def-operador-ortogonal">
            <h3 style="margin-top: 2rem;">
              <span>Isometrías y Definición de Operador Ortogonal</span>
              <span class="ref-badge">Moore §4.5 pág. 206</span>
            </h3>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.2.1: Operador Ortogonal (Moore §4.5)</div>
              <p>
                Sea $V$ un espacio euclidiano. Un operador lineal $T: V \to V$ se denomina <strong>operador ortogonal</strong> (o <em>transformación ortogonal</em>) si preserva el producto interno de todos los pares de vectores:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\langle T(\alpha), T(\beta) \rangle = \langle \alpha, \beta \rangle \quad \text{para todos } \alpha, \beta \in V.$$
              </div>
            </div>

            <div class="math-box box-prop">
              <div class="math-box-header">Proposición 1.2.1: Equivalencia Fundamental (Preservación de Norma $\iff$ Preservación de Producto)</div>
              <p>
                Un operador lineal $T: V \to V$ es ortogonal si y sólo si preserva las longitudes euclidianas de todos los vectores:
              </p>
              <div class="formula-card">
                $$\|T(\alpha)\| = \|\alpha\| \quad \text{para todo } \alpha \in V.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración mediante la Identidad de Polarización Real.</i></div>
                <p>
                  $(\implies)$ Si $T$ es ortogonal, entonces $\|T(\alpha)\|^2 = \langle T(\alpha), T(\alpha) \rangle = \langle \alpha, \alpha \rangle = \|\alpha\|^2$, por lo que tomando la raíz cuadrada no negativa se concluye $\|T(\alpha)\| = \|\alpha\|$.<br><br>
                  $(\impliedby)$ Supongamos que $\|T(\gamma)\| = \|\gamma\|$ para todo $\gamma \in V$. Recordemos la <strong>identidad de polarización real</strong>, deducible de los axiomas del producto interno:
                  $$\langle \alpha, \beta \rangle = \frac{1}{4}\left(\|\alpha + \beta\|^2 - \|\alpha - \beta\|^2\right).$$
                  Aplicando esta identidad directamente a las imágenes $T(\alpha)$ y $T(\beta)$ y usando la linealidad $T(\alpha \pm \beta) = T(\alpha) \pm T(\beta)$:
                  $$\begin{aligned}
                    \langle T(\alpha), T(\beta) \rangle &= \frac{1}{4}\left(\|T(\alpha) + T(\beta)\|^2 - \|T(\alpha) - T(\beta)\|^2\right) \\
                    &= \frac{1}{4}\left(\|T(\alpha + \beta)\|^2 - \|T(\alpha - \beta)\|^2\right) \\
                    &= \frac{1}{4}\left(\|\alpha + \beta\|^2 - \|\alpha - \beta\|^2\right) = \langle \alpha, \beta \rangle. \quad \blacksquare
                  \end{aligned}$$
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             CARACTERIZACIÓN MATRICIAL Y MATRICES ORTOGONALES
          ------------------------------------------------------------------ -->
          <div id="sec-1-2-teorema-caracterizacion">
            <h3 style="margin-top: 2.5rem;">
              <span>Caracterización Matricial de los Operadores Ortogonales</span>
              <span class="ref-badge">Moore Teorema 5.1 pág. 207</span>
            </h3>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.2.1: Caracterización de Operadores Ortogonales (Moore Teorema 5.1)</div>
              <p>
                Sea $V$ un espacio euclidiano $n$-dimensional, sea $T: V \to V$ un operador lineal y sea $\beta = \{u_1, u_2, \dots, u_n\}$ una base ortonormal de $V$. Sea $A = [T]_\beta = (a_{ij})$ la matriz de representación de $T$ en $\beta$. Las siguientes afirmaciones son lógicamente equivalentes:
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Operador Isométrico:</div>
                <p style="margin-bottom: 0;">$T$ es un operador ortogonal sobre $V$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Conservación de Bases Ortonormales:</div>
                <p style="margin-bottom: 0;">$\{T(u_1), T(u_2), \dots, T(u_n)\}$ es una base ortonormal de $V$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Columnas Ortonormales en $\mathbb{R}^n$:</div>
                <p style="margin-bottom: 0;">Los vectores columna de la matriz $A$ son mutuamente ortonormales: $\sum_{k=1}^n a_{ki} a_{kj} = \delta_{ij}$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">4</span> Matriz Ortogonal Transpuesta-Inversa:</div>
                <p style="margin-bottom: 0;">$A^T A = I_n$, lo cual equivale a $A^{-1} = A^T$ y consecuentemente $A A^T = I_n$ (filas ortonormales).</p>
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración.</i></div>
                <p>
                  La entrada en la posición $(i, j)$ de la matriz producto $A^T A$ es el producto interno usual en $\mathbb{R}^n$ entre la columna $i$ y la columna $j$ de $A$. Dado que $\beta$ es una base ortonormal, este producto coincide exactamente con $\langle T(u_i), T(u_j) \rangle$:
                  $$(A^T A)_{ij} = \langle [T(u_i)]_\beta, [T(u_j)]_\beta \rangle = \langle T(u_i), T(u_j) \rangle.$$
                  Por lo tanto, $A^T A = I_n$ si y solo si $\langle T(u_i), T(u_j) \rangle = \delta_{ij} = \langle u_i, u_j \rangle$, lo que demuestra la equivalencia completa. $\blacksquare$
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             DEFINICIÓN: MATRIZ ORTOGONAL Y GRUPO O(n)
          ------------------------------------------------------------------ -->
          <div id="sec-1-2-def-matriz-ortogonal">
            <h3 style="margin-top: 2.5rem;">
              <span>Matrices Ortogonales y Clasificación por Determinante $\det A = \pm 1$</span>
              <span class="ref-badge">Moore §4.5 pág. 208</span>
            </h3>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.2.2: Matriz Ortogonal y Grupo $O(n)$</div>
              <p>
                Una matriz real $A \in M_{n \times n}(\mathbb{R})$ se denomina <strong>ortogonal</strong> si $A^T A = I_n$. El conjunto de todas las matrices ortogonales de orden $n$ forma un grupo bajo la multiplicación matricial, denominado el <strong>grupo ortogonal</strong> $O(n)$.
              </p>
              <div class="formula-card">
                $$\det(A^T A) = \det(A^T)\det(A) = [\det(A)]^2 = \det(I_n) = 1 \implies \det(A) = \pm 1.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                - <strong>Rotaciones puras (ortogonales propias):</strong> $\det(A) = +1$ (Grupo especial ortogonal $SO(n)$). Preservan la orientación del espacio.<br>
                - <strong>Reflexiones / Inversiones (ortogonales impropias):</strong> $\det(A) = -1$. Invierten la orientación espacial.
              </p>
            </div>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.2.2: Teorema de Representación Inversa (Moore Teorema 5.2 pág. 208)</div>
              <p>
                Sea $V$ un espacio euclidiano de dimensión $n$ provisto de una base ortonormal $\beta$. Toda matriz ortogonal $A \in O(n)$ representa a un <strong>único operador ortogonal</strong> $T: V \to V$ tal que $[T]_\beta = A$.
              </p>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             EJEMPLOS ORIGINALES DE MOORE §4.5 (1D Y 2D)
          ------------------------------------------------------------------ -->
          <div id="sec-1-2-clasificacion-r2">
            <h3 style="margin-top: 2.5rem;">
              <span>Los Ejemplos Canónicos de Moore: Operadores Ortogonales en 1D y 2D</span>
              <span class="ref-badge">Moore §4.5 págs. 209–211</span>
            </h3>

            <!-- EJEMPLO 1 DE MOORE §4.5 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.2.1: Operadores Ortogonales en Espacios Unidimensionales (Moore §4.5 Ejemplo 1, pág. 209)</div>
              <p>
                Sea $T$ un operador ortogonal sobre un espacio euclidiano de dimensión uno $V$, generado por un único vector no nulo $\alpha$ ($V = \mathcal{L}\{\alpha\}$).
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Condición de Escalar Propio:</div>
                <p>
                  Puesto que $V$ es de dimensión uno, la imagen de $\alpha$ debe ser un múltiplo escalar de $\alpha$:
                  $$T(\alpha) = \lambda \alpha \quad \text{para algún número real } \lambda \in \mathbb{R}.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Imposición de Isometría:</div>
                <p>
                  Como $T$ preserva el producto interno, se tiene $\langle T(\alpha), T(\alpha) \rangle = \langle \alpha, \alpha \rangle$. Sustituyendo $T(\alpha) = \lambda \alpha$:
                  $$\langle \lambda \alpha, \lambda \alpha \rangle = \lambda^2 \langle \alpha, \alpha \rangle = \langle \alpha, \alpha \rangle.$$
                  Puesto que $\alpha \neq 0$, por el axioma de positividad $\langle \alpha, \alpha \rangle > 0$. Dividiendo entre esta cantidad:
                  $$\lambda^2 = 1 \implies \lambda = \pm 1.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Conclusión y Significado Geométrico:</div>
                <p style="margin-bottom: 0;">
                  Existen únicamente <strong>dos posibilidades</strong> para un operador ortogonal en dimensión uno:
                  $$\begin{aligned}
                    \mathbf{(i)} & \quad T(\beta) = \beta \quad \text{para todo } \beta \in V \quad \text{(Operador Identidad } I\text{)} \\
                    \mathbf{(ii)} & \quad T(\beta) = -\beta \quad \text{para todo } \beta \in V \quad \text{(Inversión de sentido / Reflexión)}
                  \end{aligned}$$
                  El primero conserva la orientación ($\det = +1$), mientras que el segundo invierte geométricamente la dirección de cada vector ($\det = -1$).
                </p>
              </div>
            </div>

            <!-- EJEMPLO 2 DE MOORE §4.5 -->
            <div class="math-box box-ex" style="margin-top: 2rem;">
              <div class="math-box-header">Ejemplo 1.2.2: Clasificación Completa de Operadores Ortogonales en $\mathbb{R}^2$ (Moore §4.5 Ejemplo 2, págs. 209–211)</div>
              <p>
                Consideremos ahora todas las posibilidades para un operador ortogonal $T$ sobre un espacio euclidiano bidimensional $V$ provisto de una base ortonormal. Sea
                $$A = \begin{pmatrix} a & c \\ b & d \end{pmatrix}$$
                la matriz que representa a $T$. Dado que $A$ es ortogonal, $\det(A) = \pm 1$. Moore analiza con todo rigor ambos casos deduciendo su forma canónica a partir de la fórmula de cofactores de la inversa:
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">Caso (i)</span> Rotación Pura ($\det A = +1$):</div>
                <p>
                  Si $\det A = ad - bc = 1$, la condición de ortogonalidad exige $A^{-1} = A^T$:
                  $$\begin{pmatrix} a & c \\ b & d \end{pmatrix}^{-1} = \begin{pmatrix} a & b \\ c & d \end{pmatrix}.$$
                  Aplicando la fórmula de cofactores para la inversa de orden $2 \times 2$:
                  $$\begin{pmatrix} a & c \\ b & d \end{pmatrix}^{-1} = \frac{1}{\det A}\begin{pmatrix} d & -c \\ -b & a \end{pmatrix} = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix}.$$
                  Igualando término a término con $A^T$:
                  $$\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} d & -c \\ -b & a \end{pmatrix} \implies d = a \quad \text{y} \quad c = -b.$$
                  Por ende, la matriz adquiere la forma $A = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$, con la restricción $a^2 + b^2 = 1$.<br>
                  Puesto que $a^2 + b^2 = 1$, siempre existe un único ángulo real $\theta \in [0, 2\pi)$ tal que $a = \cos\theta$ y $b = \sin\theta$. La matriz resulta ser la rotación estándar:
                  $$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad \begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}.$$
                  Geométricamente, $T$ representa una <strong>rotación del plano</strong> a través de un ángulo de $\theta$ radianes en sentido antihorario.
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">Caso (ii)</span> Reflexión Especular ($\det A = -1$):</div>
                <p style="margin-bottom: 0;">
                  Si $\det A = ad - bc = -1$, la fórmula de la inversa por cofactores proporciona:
                  $$A^{-1} = \frac{1}{-1}\begin{pmatrix} d & -c \\ -b & a \end{pmatrix} = \begin{pmatrix} -d & c \\ b & -a \end{pmatrix}.$$
                  Igualando con la transpuesta $A^T = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
                  $$\begin{pmatrix} a & b \\ c & d \end{pmatrix} = \begin{pmatrix} -d & c \\ b & -a \end{pmatrix} \implies d = -a \quad \text{y} \quad c = b.$$
                  La matriz resultante es simétrica: $A = \begin{pmatrix} a & b \\ b & -a \end{pmatrix}$ con $a^2 + b^2 = 1$.<br>
                  Sustituyendo $a = \cos\theta$ y $b = \sin\theta$:
                  $$S_\theta = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}, \qquad \begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}.$$
                  Como demuestra Moore (§4.5 pág. 210, Fig. 24), este operador satisface $S_\theta^2 = I_2$ y representa la <strong>reflexión del plano respecto a una recta</strong> que pasa por el origen formando un ángulo de $\theta/2$ radianes con el semieje positivo de las $x$.
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             SIMULADOR INTERACTIVO: ISOMETRÍAS Y ROTACIONES EN R^2
          ------------------------------------------------------------------ -->
          <div id="sec-1-2-simulador-rotaciones" class="interactive-container">
            <div class="interactive-header">
              <div class="interactive-title">
                <span>🎮</span> Simulador Interactivo 2: Explorador de Transformaciones Ortogonales en $\mathbb{R}^2$
              </div>
              <span class="ref-badge">Moore §4.5 • Teorema 1.2.1</span>
            </div>

            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1rem;">
              Selecciona el tipo de isometría (Rotación $R_\theta$ o Reflexión $S_\theta$), ajusta el ángulo $\theta$ y un vector de prueba $\alpha = (x, y)^T$. Observa en tiempo real la matriz $A$, $\det(A) = \pm 1$ y la preservación rigurosa de longitudes:
            </p>

            <div class="interactive-input-row">
              <label style="font-size: 0.85rem; font-weight: 600;">Tipo:</label>
              <select id="ortho-type" class="interactive-num-input" style="width: 140px; padding: 0.35rem;">
                <option value="rotation">Rotación R_θ</option>
                <option value="reflection">Reflexión S_θ</option>
              </select>

              <label style="font-size: 0.85rem; font-weight: 600;">Ángulo θ (°):</label>
              <input type="number" id="ortho-theta" class="interactive-num-input" value="45" step="15" min="0" max="360">

              <label style="font-size: 0.85rem; font-weight: 600;">$x$:</label>
              <input type="number" id="ortho-x" class="interactive-num-input" value="3" step="0.5">

              <label style="font-size: 0.85rem; font-weight: 600;">$y$:</label>
              <input type="number" id="ortho-y" class="interactive-num-input" value="4" step="0.5">

              <button id="btn-ortho-preset-45" class="preset-btn">Rot 45°</button>
              <button id="btn-ortho-preset-90" class="preset-btn">Rot 90°</button>
              <button id="btn-ortho-preset-ref" class="preset-btn">Reflex 60°</button>
            </div>

            <div class="matrix-result-box">
              <div id="ortho-matrix-display" style="text-align: center; margin-bottom: 0.75rem; font-size: 1.15rem;"></div>
              <div id="ortho-properties-display" style="text-align: center; margin-bottom: 0.75rem; color: var(--text-secondary); line-height: 1.8;"></div>
              <div id="ortho-vector-display" style="text-align: center; font-size: 1.1rem; color: var(--accent-color);"></div>
            </div>
          </div>
        </section>
    '''
