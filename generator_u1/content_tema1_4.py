# -*- coding: utf-8 -*-
r"""
Generador de Contenido: Tema 1.4 Productos Internos y Operadores Positivos
Texto base: John T. Moore §4.7 (pp. 221-228) & Friedberg §6.4
Contiene la correspondencia exacta 1-a-1 de los 4 ejemplos canónicos del libro de Moore (§4.7 pp. 225-226)
con la notación unificada de corchetes angulares \langle \alpha, \beta \rangle.
Formato visual homologado al 100% con Tema 4.0.1 y Tema 4.1.
"""

def get_tema_1_4_html():
    return r'''
        <!-- =====================================================================
           TEMA 1.4: PRODUCTOS INTERNOS Y OPERADORES POSITIVOS (MOORE §4.7)
        ====================================================================== -->
        <section id="tema-1-4" class="topic-section">
          <h2>
            <span>Tema 1.4. Productos Internos y Operadores Positivos</span>
            <span class="ref-badge" style="width: fit-content;">Moore §4.7 (Páginas 221–228) & Friedberg §6.4</span>
          </h2>

          <p class="section-intro">
            Abordamos el núcleo central de la unidad de competencia oficial del IPN: la caracterización completa de los productos internos a partir de <strong>operadores positivos</strong> y <strong>matrices simétricas definidas positivas</strong>. Estudiamos la descomposición cuadrática $T = U^* U$, la factorización matricial de Cholesky $A = Q^T Q$, los criterios de Sylvester y espectral, la clasificación de formas cuadráticas, los cuatro ejemplos canónicos de Moore §4.7 y matrices de Gram, complementado con un simulador reactivo.
          </p>

          <!-- -----------------------------------------------------------------
             1.4.1 OPERADORES Y MATRICES DEFINIDAS POSITIVAS
          ------------------------------------------------------------------ -->
          <div id="sec-1-4-1-operadores-positivos">
            <h3 style="margin-top: 2rem;">
              <span>1.4.1 Operadores y Matrices Definidas Positivas</span>
              <span class="ref-badge">Moore §4.7 pág. 221</span>
            </h3>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.4.1: Operador Positivo / Definido Positivo (Moore §4.7)</div>
              <p>
                Sea $V$ un espacio euclidiano con producto interno $\langle \cdot, \cdot \rangle$. Un operador lineal $T: V \to V$ se denomina <strong>positivo</strong> (o <em>definido positivo</em>) si satisface las siguientes dos condiciones:
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Autoadjunto / Simétrico:</div>
                <p style="margin-bottom: 0;">$T^* = T$, es decir, $\langle T(\alpha), \beta \rangle = \langle \alpha, T(\beta) \rangle$ para todos $\alpha, \beta \in V$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Positividad Estricta:</div>
                <p style="margin-bottom: 0;">$\langle T(\alpha), \alpha \rangle > 0$ para todo vector no nulo $\alpha \in V$, $\alpha \neq 0$.</p>
              </div>
            </div>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.4.1: Caracterización de Productos Internos por Operadores Positivos (Moore Teorema 7.1)</div>
              <p>
                Sea $V$ un espacio euclidiano con producto interno estándar $\langle \cdot, \cdot \rangle$.
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">Ida</span> Si $T$ es positivo:</div>
                <p style="margin-bottom: 0;">La asignación $\langle \alpha, \beta \rangle_T = \langle T(\alpha), \beta \rangle$ define un nuevo producto interno admisible sobre $V$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">Recíproco</span> Unicidad por Riesz:</div>
                <p style="margin-bottom: 0;">
                  Para <em>cualquier</em> producto interno $\langle \cdot, \cdot \rangle'$ sobre $V$ (de dimensión finita), existe un <strong>único operador positivo</strong> $T: V \to V$ tal que $\langle \alpha, \beta \rangle' = \langle T(\alpha), \beta \rangle$ para todos $\alpha, \beta \in V$.
                </p>
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración.</i></div>
                <p>
                  Para el recíproco, para cada vector $\beta \in V$ fijo, la aplicación $\alpha \mapsto \langle \alpha, \beta \rangle'$ es un funcional lineal sobre $V$. Por el Teorema de Representación de Riesz (Teorema 1.3.1), existe un único vector $S(\beta) \in V$ tal que $\langle \alpha, \beta \rangle' = \langle \alpha, S(\beta) \rangle = \langle S(\beta), \alpha \rangle$. La linealidad de $\langle \cdot, \cdot \rangle'$ en el segundo argumento asegura que $S$ es una transformación lineal. Por la simetría de ambos productos internos:
                  $$\langle \alpha, S(\beta) \rangle = \langle \alpha, \beta \rangle' = \langle \beta, \alpha \rangle' = \langle \beta, S(\alpha) \rangle = \langle S(\alpha), \beta \rangle,$$
                  lo que demuestra que $S^* = S$ (autoadjunto). Finalmente, para cualquier $\alpha \neq 0$:
                  $$\langle S(\alpha), \alpha \rangle = \langle \alpha, \alpha \rangle' > 0,$$
                  por el axioma $\mathbf{(I_4)}$ del producto $\langle \cdot, \cdot \rangle'$. Concluimos que $T = S$ es el operador positivo unívocamente determinado. $\blacksquare$
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             DESCOMPOSICIÓN CUADRÁTICA Y FACTORIZACIÓN CHOLESKY
          ------------------------------------------------------------------ -->
          <div id="sec-1-4-1-descomposicion-cuadratica">
            <h3 style="margin-top: 2.5rem;">
              <span>Descomposición Cuadrática y Factorización de Cholesky</span>
              <span class="ref-badge">Moore Teorema 7.2 & Corolario págs. 222–224</span>
            </h3>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.4.2: Descomposición Cuadrática $T = U^* U$ (Moore Teorema 7.2)</div>
              <p>
                Un operador lineal $T: V \to V$ en un espacio euclidiano de dimensión finita es positivo si y sólo si existe un operador lineal invertible $U: V \to V$ tal que:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$T = U^* U.$$
              </div>
            </div>

            <div class="math-box box-cor">
              <div class="math-box-header">Corolario 1.4.1: Factorización de Cholesky Matricial $A = Q^T Q$ (Moore pág. 224)</div>
              <p>
                Una matriz real $A$ es <strong>positiva</strong> (simétrica y definida positiva) si y sólo si existe una matriz no singular $Q$ tal que:
              </p>
              <div class="formula-card">
                $$A = Q^T Q.$$
              </div>
              <p style="margin-bottom: 0;">
                Este resultado proporciona un método directo y universal para la construcción de operadores positivos y productos internos.
              </p>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             LOS 4 EJEMPLOS CANÓNICOS DE MOORE §4.7 (PÁGS. 225-226)
          ------------------------------------------------------------------ -->
          <div id="sec-1-4-ejemplos-moore">
            <h3 style="margin-top: 2.5rem;">
              <span>Los Ejemplos Canónicos de Moore: Operadores Positivos y Formas Cuadráticas</span>
              <span class="ref-badge">Moore §4.7 págs. 225–226</span>
            </h3>

            <!-- EJEMPLO 1 DE MOORE §4.7 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.4.1: Matriz Identidad y Producto Interno Estándar (Moore §4.7 Ejemplo 1, pág. 225)</div>
              <p>
                Es evidente que la matriz identidad $I = I_n$ de cualquier orden es positiva ($I^T = I$, y para todo $X \neq 0$, $X^T I X = X^T X > 0$). Por consiguiente, puede utilizarse para definir una forma cuadrática positiva o un producto interno sobre cualquier espacio de dimensión adecuada:
              </p>
              <div class="formula-card">
                $$Y^T I X = Y^T X = \begin{pmatrix} y_1 & y_2 & \dots & y_n \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} = x_1 y_1 + x_2 y_2 + \dots + x_n y_n.$$
              </div>
              <p>
                La forma cuadrática representada por $I$ es:
                $$q(X) = X^T X = x_1^2 + x_2^2 + \dots + x_n^2 > 0 \quad (\forall X \neq 0).$$
              </p>
              <p style="margin-bottom: 0;">
                Esta forma cuadrática inducida por $I$ es estrictamente positiva, y el producto interno asociado en $V_n$ es el producto interno estándar ordinario. Si $X$ y $Y$ son vectores de coordenadas (relativos a una base ortonormal) en cualquier espacio euclidiano abstracto $V$, el operador lineal $T$ definido en $V$ por la matriz $I$ es exactamente el <strong>operador identidad</strong> $T = I_V$.
              </p>
            </div>

            <!-- EJEMPLO 2 DE MOORE §4.7 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.4.2: Construcción de Producto $A$-Interno vía $A = Q^T Q$ (Moore §4.7 Ejemplo 2, págs. 225–226)</div>
              <p>
                Para construir un ejemplo no trivial de producto interno matricial ($A$-inner product), seleccionamos una matriz no singular arbitraria $Q$ y aplicamos el Corolario 1.4.1. Sea:
              </p>
              <div class="formula-card">
                $$Q = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix}.$$
              </div>
              <p>
                Verificamos fácilmente que $\det(Q) = 1(1 - 2) + 1(0 - 1) = -2 \neq 0$, por lo que $Q$ es no singular. Calculamos la matriz positiva $A = Q^T Q$:
              </p>
              <div class="formula-card">
                $$A = Q^T Q = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 2 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 2 \\ 1 & 1 & 1 \end{pmatrix} = \begin{pmatrix} 2 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 6 \end{pmatrix}.$$
              </div>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Expresión Bilineal del Producto $A$-Interno:</div>
                <p>
                  Si $X = (x_1, x_2, x_3)^T$ y $Y = (y_1, y_2, y_3)^T$, el producto interno inducido por $A$ viene dado por $\langle X, Y \rangle_A = Y^T A X$:
                  $$\begin{aligned}
                    \langle X, Y \rangle_A &= \begin{pmatrix} y_1 & y_2 & y_3 \end{pmatrix} \begin{pmatrix} 2 & 1 & 2 \\ 1 & 2 & 3 \\ 2 & 3 & 6 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix} \\
                    &= 2x_1 y_1 + x_1 y_2 + 2x_1 y_3 + x_2 y_1 + 2x_2 y_2 + 3x_2 y_3 + 2x_3 y_1 + 3x_3 y_2 + 6x_3 y_3.
                  \end{aligned}$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Forma Cuadrática Estrictamente Positiva:</div>
                <p style="margin-bottom: 0;">
                  Haciendo $Y = X$, la forma cuadrática representada por $A$ es:
                  $$q(X) = X^T A X = 2x_1^2 + 2x_2^2 + 6x_3^2 + 2x_1 x_2 + 4x_1 x_3 + 6x_2 x_3.$$
                  Como $A = Q^T Q$, tenemos $X^T A X = (QX)^T (QX) = \|QX\|^2$. Dado que $Q$ es no singular, $QX = 0 \iff X = 0$; por ende, $\|QX\|^2 > 0$ para todo $X \neq 0$. Nuevamente, si $X$ y $Y$ son coordenadas relativas a una base ortonormal, esto define un $T$-producto interno $\langle T(\alpha), \beta \rangle$ en cualquier espacio tridimensional.
                </p>
              </div>
            </div>

            <!-- EJEMPLO 3 DE MOORE §4.7 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.4.3: Simetría Sin Positividad: Caso Indefinido (Moore §4.7 Ejemplo 3, pág. 226)</div>
              <p>
                Consideremos la matriz simétrica:
                $$A = \begin{pmatrix} 2 & 3 \\ 3 & -4 \end{pmatrix}.$$
                La matriz $A$ es evidentemente simétrica ($A = A^T$). Sin embargo, evaluemos su forma cuadrática asociada para un vector genérico $X = (x_1, x_2)^T \in V_2$:
              </p>
              <div class="formula-card">
                $$X^T A X = \begin{pmatrix} x_1 & x_2 \end{pmatrix} \begin{pmatrix} 2 & 3 \\ 3 & -4 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \end{pmatrix} = 2x_1^2 + 6x_1 x_2 - 4x_2^2.$$
              </div>
              <p>
                Tomando en particular el vector $x_1 = 1$ y $x_2 = -1$:
                $$X^T A X = 2(1)^2 + 6(1)(-1) - 4(-1)^2 = 2 - 6 - 4 = -8 < 0.$$
              </p>
              <p style="margin-bottom: 0;">
                Por lo tanto, aunque $A$ es perfectamente simétrica, <strong>no es una matriz positiva</strong> (es indefinida), y bajo ninguna circunstancia puede representar una forma cuadrática positiva ni definir un operador positivo o un producto interno.
              </p>
            </div>

            <!-- EJEMPLO 4 DE MOORE §4.7 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.4.4: ¿Cuándo es Positivo un Operador de Rotación en $V_2$? (Moore §4.7 Ejemplo 4, pág. 226)</div>
              <p>
                Analicemos las condiciones bajo las cuales un operador de rotación en $V_2$ ($\mathbb{R}^2$) califica como operador positivo. Asumimos la base canónica ortonormal $\{E_1, E_2\}$ y el producto interno estándar, donde el operador de rotación $T$ está definido por:
                $$T(x, y) = (x\cos\theta - y\sin\theta, \; x\sin\theta + y\cos\theta).$$
                Su matriz asociada respecto a la base ortonormal $\{E_1, E_2\}$ es:
              </p>
              <div class="formula-card">
                $$A = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
              </div>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Exigencia de Simetría ($A = A^T$):</div>
                <p>
                  Uno de los requerimientos ineludibles para que $T$ sea un operador positivo es que su matriz asociada sea simétrica:
                  $$\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \implies -\sin\theta = \sin\theta \implies \sin\theta = 0.$$
                  Esto impone inmediatamente que $\theta = n\pi$ para algún entero $n \in \mathbb{Z}$.
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Forma Cuadrática y Positividad Estricta:</div>
                <p>
                  Con $\sin\theta = 0$, la matriz se reduce a $A = \begin{pmatrix} \cos\theta & 0 \\ 0 & \cos\theta \end{pmatrix} = (\cos\theta) I_2$. La forma cuadrática representada es:
                  $$X^T A X = (x_1^2 + x_2^2)\cos\theta.$$
                  Esta forma cuadrática es positiva definida si y sólo si $\cos\theta > 0$.<br>
                  Dado que $\theta = n\pi$, $\cos(n\pi) = (-1)^n > 0$ se cumple exclusivamente cuando $n$ es un número entero <strong>par</strong> ($n = 2k$):
                  $$\theta = 2k\pi \quad (k \in \mathbb{Z}).$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Conclusión Geométrica:</div>
                <p style="margin-bottom: 0;">
                  La rotación a través de un ángulo $\theta$ es un operador positivo si y sólo si $\theta$ es un múltiplo entero de $2\pi$. Es decir, el único operador de rotación que es positivo en $\mathbb{R}^2$ es el <strong>operador identidad</strong> $T = I$.
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             1.4.2 CRITERIOS DE SYLVESTER Y ESPECTRAL
          ------------------------------------------------------------------ -->
          <div id="sec-1-4-2-positivas-negativas">
            <h3 style="margin-top: 2.5rem;">
              <span>1.4.2 Criterios de Sylvester, Espectral y Clasificación de Formas Cuadráticas</span>
              <span class="ref-badge">Friedberg §6.4, §6.8 • Moore Cap. 5</span>
            </h3>

            <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 1.2rem; line-height: 1.7;">
              En los ejemplos anteriores observamos que la simetría de una matriz $A = A^T$ es una condición necesaria pero no suficiente para asegurar la positividad de la forma cuadrática $X^T A X > 0$ (como evidenció la matriz simétrica indefinida del Ejemplo 1.4.3). Mientras que en orden $2 \times 2$ es factible descubrir contraejemplos vectoriales por inspección directa, en dimensiones superiores se requiere un procedimiento analítico sistemático y computable. Los dos métodos fundamentales para determinar concluyentemente si una matriz simétrica es estrictamente positiva (y por ende capaz de definir un producto interno) son el <strong>criterio espectral</strong> (signos de los eigenvalores) y el <strong>criterio de menores principales de Sylvester</strong> (signos de los determinantes líderes).
            </p>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.4.3: Criterios Espectral y de Menores Principales de Sylvester (Friedberg §6.8 / Moore Cap. 5)</div>
              <p>
                Sea $A = A^T \in M_{n \times n}(\mathbb{R})$ una matriz real simétrica:
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Criterio Espectral:</div>
                <p style="margin-bottom: 0;">$A > 0 \iff$ todos sus eigenvalores son estrictamente positivos ($\lambda_i > 0$). $A < 0 \iff \lambda_i < 0$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Criterio de Menores Principales de Sylvester:</div>
                <p style="margin-bottom: 0;">
                  Sean $\Delta_k = \det(A_{1..k, 1..k})$ los determinantes de las submatrices principales líderes ($k = 1, \dots, n$):<br>
                  • <strong>Definida Positiva ($A > 0$):</strong> $\Delta_1 > 0, \; \Delta_2 > 0, \; \dots, \; \Delta_n > 0$ (todos estrictamente positivos).<br>
                  • <strong>Definida Negativa ($A < 0$):</strong> $\Delta_1 < 0, \; \Delta_2 > 0, \; \Delta_3 < 0, \; \dots, \; (-1)^k \Delta_k > 0$ (alternancia estricta de signos comenzando en negativo).
                </p>
              </div>
            </div>

            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Tabla Comparativa de Formas Cuadráticas en $\mathbb{R}^2$</div>
              <table style="width: 100%; border-collapse: collapse; margin-top: 0.75rem; font-size: 0.95rem;">
                <thead>
                  <tr style="border-bottom: 2px solid var(--border-color); text-align: left;">
                    <th style="padding: 0.6rem;">Matriz $A$</th>
                    <th style="padding: 0.6rem;">Forma Cuadrática $q(X)$</th>
                    <th style="padding: 0.6rem;">Eigenvalores</th>
                    <th style="padding: 0.6rem;">Menores $\Delta_k$</th>
                    <th style="padding: 0.6rem;">Clasificación</th>
                  </tr>
                </thead>
                <tbody style="line-height: 1.7;">
                  <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.6rem;">$\begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$</td>
                    <td style="padding: 0.6rem;">$2x_1^2 + 2x_1 x_2 + 2x_2^2$</td>
                    <td style="padding: 0.6rem;">$\lambda_1=3, \lambda_2=1$</td>
                    <td style="padding: 0.6rem;">$\Delta_1=2, \Delta_2=3$</td>
                    <td style="padding: 0.6rem; color: #10b981; font-weight: bold;">Definida Positiva</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.6rem;">$\begin{pmatrix} -3 & 1 \\ 1 & -2 \end{pmatrix}$</td>
                    <td style="padding: 0.6rem;">$-3x_1^2 + 2x_1 x_2 - 2x_2^2$</td>
                    <td style="padding: 0.6rem;">$\lambda_i < 0$</td>
                    <td style="padding: 0.6rem;">$\Delta_1=-3, \Delta_2=5$</td>
                    <td style="padding: 0.6rem; color: #ef4444; font-weight: bold;">Definida Negativa</td>
                  </tr>
                  <tr style="border-bottom: 1px solid var(--border-color);">
                    <td style="padding: 0.6rem;">$\begin{pmatrix} 1 & -2 \\ -2 & 4 \end{pmatrix}$</td>
                    <td style="padding: 0.6rem;">$(x_1 - 2x_2)^2$</td>
                    <td style="padding: 0.6rem;">$\lambda_1=5, \lambda_2=0$</td>
                    <td style="padding: 0.6rem;">$\Delta_1=1, \Delta_2=0$</td>
                    <td style="padding: 0.6rem; color: #f59e0b; font-weight: bold;">Semidefinida Positiva</td>
                  </tr>
                  <tr>
                    <td style="padding: 0.6rem;">$\begin{pmatrix} 1 & 3 \\ 3 & 1 \end{pmatrix}$</td>
                    <td style="padding: 0.6rem;">$x_1^2 + 6x_1 x_2 + x_2^2$</td>
                    <td style="padding: 0.6rem;">$\lambda_1=4, \lambda_2=-2$</td>
                    <td style="padding: 0.6rem;">$\Delta_1=1, \Delta_2=-8$</td>
                    <td style="padding: 0.6rem; color: #8b5cf6; font-weight: bold;">Indefinida</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             1.4.4 CARACTERIZACIÓN DE PRODUCTOS INTERNOS Y MATRICES DE GRAM
          ------------------------------------------------------------------ -->
          <div id="sec-1-4-4-matrices-gram">
            <h3 style="margin-top: 2.5rem;">
              <span>1.4.4 Caracterización Matricial & Matrices de Gram</span>
              <span class="ref-badge">Moore §4.7 • Friedberg §6.8</span>
            </h3>

            <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 1.2rem; line-height: 1.7;">
              Una vez clasificada la positividad de las matrices simétricas, podemos enunciar el resultado que culmina esta unidad: una forma bilineal en $\mathbb{R}^n$ induce un producto interno si y sólo si su matriz representante es simétrica y estrictamente definida positiva. Aplicando este principio de forma constructiva a una base ordenada arbitraria de un espacio euclidiano, la matriz de productos internos mutuos de los vectores base —denominada la <strong>matriz de Gram</strong>— resulta ser siempre simétrica y definida positiva, proveyendo la regla universal para calcular productos internos y longitudes en coordenadas generales.
            </p>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.4.4: Equivalencia Matricial de Productos Internos (Moore §4.7 / Friedberg §6.8)</div>
              <p>
                Una forma bilineal $\langle X, Y \rangle = Y^T A X$ en $\mathbb{R}^n$ define un producto interno si y sólo si la matriz $A$ es <strong>simétrica y estrictamente definida positiva</strong>.
              </p>
              <p style="margin-bottom: 0;">
                Asimismo, para cualquier base $\beta = \{v_1, \dots, v_n\}$ de un espacio euclidiano, la matriz de Gram $G = (\langle v_i, v_j \rangle)$ es simétrica y estrictamente definida positiva ($\det(G) > 0$).
              </p>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             SIMULADOR INTERACTIVO: MATRICES DEFINIDAS POSITIVAS Y PRODUCTO A-INTERNO
          ------------------------------------------------------------------ -->
          <div id="sec-1-4-simulador-positivas" class="interactive-container">
            <div class="interactive-header">
              <div class="interactive-title">
                <span>🎮</span> Simulador Interactivo 3: Matrices Definidas Positivas & Producto $A$-Interno
              </div>
              <span class="ref-badge">Moore §4.7 • Teorema 1.4.1</span>
            </div>

            <p style="font-size: 0.88rem; color: var(--text-secondary); margin-bottom: 1rem;">
              Ingresa los coeficientes de la matriz simétrica $A = \begin{pmatrix} a & b \\ b & d \end{pmatrix}$ y evalúa el criterio de Sylvester ($\Delta_1, \Delta_2$), eigenvalores, factorización de Cholesky $A = Q^T Q$ y el producto interno inducido $\langle X, Y \rangle_A = X^T A Y$:
            </p>

            <div class="interactive-input-row">
              <label style="font-size: 0.85rem; font-weight: 600;">$a$:</label>
              <input type="number" id="pos-mat-a" class="interactive-num-input" value="3" step="0.5">

              <label style="font-size: 0.85rem; font-weight: 600;">$b$ (cruzado):</label>
              <input type="number" id="pos-mat-b" class="interactive-num-input" value="1" step="0.5">

              <label style="font-size: 0.85rem; font-weight: 600;">$d$:</label>
              <input type="number" id="pos-mat-d" class="interactive-num-input" value="2" step="0.5">

              <button id="btn-pos-preset-defpos" class="preset-btn">Def. Positiva</button>
              <button id="btn-pos-preset-defneg" class="preset-btn">Def. Negativa</button>
              <button id="btn-pos-preset-indef" class="preset-btn">Indefinida</button>
            </div>

            <div class="interactive-input-row" style="margin-top: 0.5rem;">
              <span style="font-size: 0.82rem; font-weight: bold; color: var(--text-secondary);">Vectores de prueba:</span>
              <label style="font-size: 0.82rem;">$X=(x_1, x_2)$:</label>
              <input type="number" id="pos-x1" class="interactive-num-input" value="1" style="width: 55px;" step="1">
              <input type="number" id="pos-x2" class="interactive-num-input" value="2" style="width: 55px;" step="1">

              <label style="font-size: 0.82rem; margin-left: 0.5rem;">$Y=(y_1, y_2)$:</label>
              <input type="number" id="pos-y1" class="interactive-num-input" value="-1" style="width: 55px;" step="1">
              <input type="number" id="pos-y2" class="interactive-num-input" value="1" style="width: 55px;" step="1">
            </div>

            <div class="matrix-result-box">
              <div id="pos-matrix-display" style="text-align: center; margin-bottom: 0.75rem; font-size: 1.15rem;"></div>
              <div id="pos-sylvester-display" style="text-align: center; margin-bottom: 0.75rem; line-height: 1.8;"></div>
              <div id="pos-cholesky-display" style="text-align: center; font-size: 1.05rem; color: var(--accent-color);"></div>
              <div id="pos-inner-display" style="text-align: center; margin-top: 0.75rem; font-weight: 600; color: var(--thm-border);"></div>
            </div>
          </div>
        </section>
    '''
