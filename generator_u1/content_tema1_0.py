# -*- coding: utf-8 -*-
r"""
Generador de Contenido: Tema 1.0 Espacios Euclidianos Generales
Texto base: John T. Moore §4.2 (pp. 186-193) & Friedberg §6.1
Contiene la correspondencia exacta 1-a-1 de los 6 ejemplos del libro de Moore (§4.2 pp. 187-189)
con las definiciones completas de norma, ángulo, validez geométrica, distancia, ortogonalidad y subespacios ortogonales,
con la notación unificada de corchetes angulares \langle \alpha, \beta \rangle.
"""

def get_tema_1_0_html():
    return r'''
        <!-- =====================================================================
           TEMA 1.0: ESPACIOS EUCLIDIANOS GENERALES (MOORE §4.2)
        ====================================================================== -->
        <section id="tema-1-0" class="topic-section">
          <h2>
            <span>Tema 1.0. Espacios Euclidianos Generales</span>
            <span class="ref-badge" style="width: fit-content;">Moore §4.2 (Páginas 186–193) & Friedberg §6.1</span>
          </h2>

          <p class="section-intro">
            En el álgebra lineal elemental se estudia el producto punto ordinario en los espacios geométricos $\mathbb{R}^2$ y $\mathbb{R}^3$, el cual permite medir longitudes y verificar perpendicularidad. En esta sección generalizamos axiomáticamente esta noción métrica a espacios vectoriales reales arbitrarios mediante el concepto de <strong>producto interno</strong> (o <em>producto escalar</em>), dando origen a los <strong>espacios euclidianos</strong>. A partir de esta estructura se deducen con absoluto rigor matemático la norma inducida, el ángulo entre vectores, la ortogonalidad, los subespacios ortogonales, el Teorema de Pitágoras generalizado, la distancia métrica, la fundamental Desigualdad de Cauchy-Schwarz y la Desigualdad del Triángulo.
          </p>

          <!-- -----------------------------------------------------------------
             DEFINICIÓN: PRODUCTO INTERNO REAL Y ESPACIO EUCLIDIANO
          ------------------------------------------------------------------ -->
          <div id="sec-1-0-def-producto-interno">
            <h3 style="margin-top: 2rem;">
              <span>Axiomática del Producto Interno Real</span>
              <span class="ref-badge">Moore §4.2 pág. 186</span>
            </h3>

            <p>
              Sea $V$ un espacio vectorial sobre el campo de los números reales $\mathbb{R}$. La noción axiomática asigna a cada par de vectores un número real que preserva simetría, bilinealidad y una propiedad de positividad estricta para vectores no nulos.
            </p>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.0.1: Producto Interno Real & Espacio Euclidiano (Moore §4.2)</div>
              <p>
                Sea $V$ un espacio vectorial real. Un <strong>producto interno</strong> (o <em>producto escalar</em>) en $V$ es una función que asigna a cada par ordenado de vectores $\alpha, \beta \in V$ un número real denotado por $\langle \alpha, \beta \rangle$, tal que para todos los vectores $\alpha, \beta, \gamma \in V$ y cualquier escalar $c \in \mathbb{R}$, se satisfacen los siguientes cuatro axiomas fundamentales:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\begin{aligned}
                  \mathbf{(I_1)} & \quad \langle \alpha, \beta \rangle = \langle \beta, \alpha \rangle && \text{(Simetría o Conmutatividad)} \\
                  \mathbf{(I_2)} & \quad \langle \alpha + \beta, \gamma \rangle = \langle \alpha, \gamma \rangle + \langle \beta, \gamma \rangle && \text{(Aditividad en el primer argumento)} \\
                  \mathbf{(I_3)} & \quad \langle c\alpha, \beta \rangle = c\langle \alpha, \beta \rangle && \text{(Homogeneidad en el primer argumento)} \\
                  \mathbf{(I_4)} & \quad \langle \alpha, \alpha \rangle \geq 0, \quad \text{y} \quad \langle \alpha, \alpha \rangle = 0 \iff \alpha = 0 && \text{(Positividad definida o No degeneración)}
                \end{aligned}$$
              </div>
              <p style="margin-top: 1rem; margin-bottom: 0;">
                Un espacio vectorial real provisto de un producto interno específico se denomina <strong>espacio euclidiano</strong> (o <em>espacio con producto interno real</em>). Si la dimensión de $V$ es finita e igual a $n$, se denomina espacio euclidiano $n$-dimensional.
              </p>
            </div>

            <div class="math-box box-prop">
              <div class="math-box-header">Proposición 1.0.1: Bilinealidad Inmediata y Ortogonalidad con el Cero</div>
              <p>
                Como consecuencia directa de los axiomas $\mathbf{(I_1)}$, $\mathbf{(I_2)}$ e $\mathbf{(I_3)}$, el producto interno es lineal también respecto a la segunda componente:
              </p>
              <div class="formula-card">
                $$\langle \alpha, \beta + \gamma \rangle = \langle \alpha, \beta \rangle + \langle \alpha, \gamma \rangle, \qquad \langle \alpha, c\beta \rangle = c\langle \alpha, \beta \rangle.$$
              </div>
              <p style="margin-bottom: 0;">
                Además, para el vector cero $\mathbf{0} \in V$, se cumple $\langle \alpha, \mathbf{0} \rangle = \langle \mathbf{0}, \alpha \rangle = 0$ para todo $\alpha \in V$.
              </p>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             LOS EJEMPLOS ORIGINALES DE MOORE §4.2 (1 a 5)
          ------------------------------------------------------------------ -->
          <div id="sec-1-0-ejemplos-espacios">
            <h3 style="margin-top: 2.5rem;">
              <span>Los Ejemplos Canónicos de Moore: Espacios Euclidianos Fundamentales</span>
              <span class="ref-badge">Moore §4.2 págs. 187–188</span>
            </h3>

            <!-- EJEMPLO 1 DE MOORE §4.2 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.0.1: El Espacio de Funciones Continuas $C[a, b]$ (Moore §4.2 Ejemplo 1, pág. 187)</div>
              <p>
                Sea $V = C[a, b]$ el espacio vectorial de todas las funciones reales continuas definidas en el intervalo cerrado $[a, b]$, con $a < b$. Para cualesquiera dos funciones $f, g \in C[a, b]$, definimos:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\langle f, g \rangle = \int_a^b f(x)g(x) \, dx.$$
              </div>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Verificación de Simetría $\mathbf{(I_1)}$:</div>
                <p>$\langle f, g \rangle = \int_a^b f(x)g(x)dx = \int_a^b g(x)f(x)dx = \langle g, f \rangle$, por conmutatividad del producto puntual.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Linealidad en el primer argumento $\mathbf{(I_2)}$ y $\mathbf{(I_3)}$:</div>
                <p>Por la linealidad de la integral de Riemann: $\int_a^b (c_1 f_1 + c_2 f_2)g \, dx = c_1 \int_a^b f_1 g \, dx + c_2 \int_a^b f_2 g \, dx$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Positividad Definida $\mathbf{(I_4)}$:</div>
                <p style="margin-bottom: 0;">
                  Para cualquier $f$, $[f(x)]^2 \geq 0$, de modo que $\langle f, f \rangle = \int_a^b [f(x)]^2 dx \geq 0$. Si $f$ es continua y $\int_a^b [f(x)]^2 dx = 0$, por el teorema fundamental del cálculo para funciones continuas no negativas, se deduce forzosamente que $f(x) = 0$ para todo $x \in [a, b]$, es decir, $f \equiv \mathbf{0}$.
                </p>
              </div>
            </div>

            <!-- EJEMPLO 2 DE MOORE §4.2 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.0.2: Espacio de Polinomios $P_n$ (Moore §4.2 Ejemplo 2, pág. 187)</div>
              <p>
                Consideremos el espacio vectorial $V = P_n$ de todos los polinomios reales de grado menor o igual a $n-1$, restringidos al intervalo cerrado $[a, b]$.
              </p>
              <p style="margin-bottom: 0;">
                Como todo polinomio es una función continua en $[a, b]$, $P_n$ es un subespacio vectorial de $C[a, b]$. Por ende, la misma regla integral
                $$\langle p, q \rangle = \int_a^b p(x)q(x) \, dx$$
                define un producto interno legítimo sobre $P_n$, convirtiéndolo en un espacio euclidiano de dimensión finita $n$.
              </p>
            </div>

            <!-- EJEMPLO 3 DE MOORE §4.2 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.0.3: Producto Interno No Estándar en $\mathbb{R}^2$ (Moore §4.2 Ejemplo 3, págs. 187–188)</div>
              <p>
                En el espacio vectorial ordinario $V_2$ ($\mathbb{R}^2$), consideremos los vectores $X = (x_1, x_2)$ e $Y = (y_1, y_2)$. Definimos la regla:
              </p>
              <div class="formula-card">
                $$\langle X, Y \rangle = x_1 y_1 - x_2 y_1 - x_1 y_2 + 2x_2 y_2.$$
              </div>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Simetría y Bilinealidad:</div>
                <p>Intercambiando los roles de $X$ e $Y$: $\langle Y, X \rangle = y_1 x_1 - y_2 x_1 - y_1 x_2 + 2y_2 x_2 = \langle X, Y \rangle$. La linealidad respecto a sumas y productos por escalar es inmediata por distributividad algebraica.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Positividad Definida mediante Completación de Cuadrados:</div>
                <p style="margin-bottom: 0;">
                  Para evaluar $\langle X, X \rangle$, hacemos $Y = X$:
                  $$\langle X, X \rangle = x_1^2 - 2x_1 x_2 + 2x_2^2 = (x_1^2 - 2x_1 x_2 + x_2^2) + x_2^2 = (x_1 - x_2)^2 + x_2^2.$$
                  Como es la suma de dos cuadrados reales:
                  $$\langle X, X \rangle \geq 0.$$
                  Además, $\langle X, X \rangle = 0 \iff (x_1 - x_2)^2 + x_2^2 = 0 \iff x_2 = 0 \text{ y } x_1 - x_2 = 0 \iff x_1 = 0 \text{ y } x_2 = 0 \iff X = (0, 0)$.
                  Por lo tanto, la regla satisface todos los axiomas y dota a $\mathbb{R}^2$ de una métrica euclidiana distinta de la estándar.
                </p>
              </div>
            </div>

            <!-- EJEMPLO 4 DE MOORE §4.2 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.0.4: Productos Internos Inducidos por Transformaciones Lineales No Singulares (Moore §4.2 Ejemplo 4, pág. 188)</div>
              <p>
                Sean $V$ y $W$ dos espacios vectoriales reales arbitrarios, y sea $T: V \to W$ una <strong>transformación lineal no singular</strong> ($\ker(T) = \{0\}$). Supongamos que en el espacio codominio $W$ ya existe un producto interno conocido $\langle \cdot, \cdot \rangle_W$.
              </p>
              <p>
                Entonces, es posible inducir un nuevo producto interno sobre el espacio de partida $V$, denotado por $\langle \cdot, \cdot \rangle_T$, definiendo para cualesquiera $\alpha, \beta \in V$:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\langle \alpha, \beta \rangle_T = \langle T(\alpha), T(\beta) \rangle_W.$$
              </div>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">Demostración</span> Verificación de los axiomas:</div>
                <p style="margin-bottom: 0;">
                  - $\mathbf{(I_1)}$ Simetría: $\langle \alpha, \beta \rangle_T = \langle T\alpha, T\beta \rangle_W = \langle T\beta, T\alpha \rangle_W = \langle \beta, \alpha \rangle_T$.<br>
                  - $\mathbf{(I_2)-(I_3)}$ Bilinealidad: $\langle c\alpha_1 + \alpha_2, \beta \rangle_T = \langle T(c\alpha_1 + \alpha_2), T\beta \rangle_W = \langle cT\alpha_1 + T\alpha_2, T\beta \rangle_W = c\langle \alpha_1, \beta \rangle_T + \langle \alpha_2, \beta \rangle_T$.<br>
                  - $\mathbf{(I_4)}$ Positividad estricta: $\langle \alpha, \alpha \rangle_T = \langle T\alpha, T\alpha \rangle_W \geq 0$. Además, $\langle \alpha, \alpha \rangle_T = 0 \iff \langle T\alpha, T\alpha \rangle_W = 0 \iff T\alpha = 0$. Como $T$ es <em>no singular</em>, $T\alpha = 0 \iff \alpha = 0$. $\blacksquare$
                </p>
              </div>
            </div>

            <!-- EJEMPLO 5 DE MOORE §4.2 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.0.5: Producto Interno con Función de Peso en $C[a, b]$ (Moore §4.2 Ejemplo 5, pág. 188)</div>
              <p>
                Consideremos el espacio $V = W = C[a, b]$ del Ejemplo 1.0.1 sobre un intervalo $[a, b]$ con $0 < a < b$. Definimos el operador $T: V \to V$ mediante la multiplicación polinomial:
              </p>
              <div class="formula-card">
                $$(Tf)(x) = x^2 f(x) \quad \text{para todo } x \in [a, b].$$
              </div>
              <p>
                Dado que $x \in [a, b]$ con $a > 0$, $x^2 \neq 0$ en todo el intervalo, por lo que $Tf = 0 \implies x^2 f(x) = 0 \implies f(x) \equiv 0$, lo que prueba que $T$ es <strong>no singular</strong>. Aplicando la construcción general del Ejemplo 1.0.4 al producto integral del Ejemplo 1.0.1, definimos el producto interno inducido:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\langle f, g \rangle_T = \int_a^b [(Tf)(x)] [(Tg)(x)] \, dx = \int_a^b [x^2 f(x)] [x^2 g(x)] \, dx = \int_a^b f(x) g(x) x^4 \, dx.$$
              </div>
              <p style="margin-bottom: 0;">
                Esto dota a $C[a, b]$ de un producto interno ponderado con función de peso estrictamente positiva $w(x) = x^4$.
              </p>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             DEFINICIONES COMPLETAS DE NORMA, ÁNGULO Y VALIDEZ GEOMÉTRICA
          ------------------------------------------------------------------ -->
          <div id="sec-1-0-norma-angulo">
            <h3 style="margin-top: 2.5rem;">
              <span>Longitud (Norma), Ángulo y Validez Geométrica</span>
              <span class="ref-badge">Moore §4.2 págs. 188–190</span>
            </h3>

            <p>
              Como observa Moore (§4.2 pág. 188), las definiciones elementales de <em>longitud</em> y <em>ángulo</em> desarrolladas en la geometría tridimensional ordinaria pueden extenderse formalmente a cualquier espacio euclidiano arbitrario provisto de un producto interno $\langle \cdot, \cdot \rangle$.
            </p>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.0.2: Longitud o Norma Inducida (Moore §4.2 pág. 188)</div>
              <p>
                Sea $V$ un espacio euclidiano. Para cualquier vector $\alpha \in V$, la <strong>longitud</strong> o <strong>norma</strong> de $\alpha$, denotada por $\|\alpha\|$ (o $|\alpha|$ en la notación clásica de Moore), se define como la raíz cuadrada no negativa de su producto interno consigo mismo:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$\|\alpha\| = \langle \alpha, \alpha \rangle^{1/2} = \sqrt{\langle \alpha, \alpha \rangle}.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                Un vector $\alpha$ se dice <strong>unitario</strong> si su norma es igual a la unidad: $\|\alpha\| = 1$. Todo vector no nulo $\alpha \neq 0$ puede normalizarse multiplicándolo por el inverso multiplicativo de su norma: $u = \frac{1}{\|\alpha\|} \alpha$, verificando $\|u\| = 1$.
              </p>
            </div>

            <div class="math-box box-def" style="margin-top: 1.5rem;">
              <div class="math-box-header">Definición 1.0.3: Ángulo entre Vectores en un Espacio Euclidiano (Moore §4.2 pág. 188)</div>
              <p>
                Sean $\alpha$ y $\beta$ dos vectores no nulos ($\alpha \neq 0$, $\beta \neq 0$) de un espacio euclidiano $V$. El <strong>ángulo</strong> $\theta$ comprendido entre $\alpha$ y $\beta$ se define formalmente como el único número real $\theta \in [0, \pi]$ tal que:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$\cos \theta = \frac{\langle \alpha, \beta \rangle}{\|\alpha\| \, \|\beta\|}.$$
              </div>
            </div>

            <div class="step-card" style="margin-top: 1.5rem;">
              <div class="step-card-title"><span class="step-badge">Discusión</span> El "Sentido Geométrico" de las Definiciones (Moore §4.2 pág. 189):</div>
              <p>
                Surge de manera natural la interrogante formulada por Moore: <em>¿tienen estas definiciones formales un auténtico sentido geométrico?</em> La respuesta es afirmativa con fundamento riguroso:
              </p>
              <ul style="margin-top: 0.5rem; line-height: 1.8;">
                <li>En $V_1$, $V_2$ y $V_3$ con el producto interno usual, las definiciones coinciden exactamente con la geometría euclidiana intuitiva de la recta, el plano y el espacio tridimensional.</li>
                <li>En los espacios coordenados $n$-dimensionales $V_n$ ($n > 3$), la geometría es una extensión formal directa del espacio tridimensional que preserva de manera coherente todas las relaciones métricas.</li>
                <li>En espacios euclidianos generales abstractos (como espacios de funciones continuas o polinomios), el uso de este vocabulario geométrico queda plenamente legitimado porque se demuestran formalmente dos de los teoremas pilares de la geometría euclidiana clásica: el <strong>Teorema de Pitágoras</strong> y la <strong>Desigualdad del Triángulo</strong>, garantizados por la <strong>Desigualdad de Cauchy-Schwarz</strong> (la cual asegura que el cociente $\frac{\langle \alpha, \beta \rangle}{\|\alpha\|\|\beta\|}$ siempre pertenezca al intervalo $[-1, 1]$, haciendo que el ángulo $\theta$ esté siempre bien definido).</li>
              </ul>
            </div>

            <div class="math-box box-def" style="margin-top: 1.5rem;">
              <div class="math-box-header">Definición 1.0.4: Vectores Ortogonales (Moore §4.2 págs. 189–190)</div>
              <p>
                Dos vectores $\alpha$ y $\beta$ de un espacio euclidiano $V$ son <strong>ortogonales</strong> (o <em>perpendiculares</em>), denotado $\alpha \perp \beta$, si su producto interno es idénticamente nulo:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\alpha \perp \beta \iff \langle \alpha, \beta \rangle = 0.$$
              </div>
              <p style="margin-top: 0.5rem; margin-bottom: 0;">
                Obsérvese que para vectores no nulos, $\langle \alpha, \beta \rangle = 0$ equivale exactamente a $\cos \theta = 0$, lo que corresponde al ángulo perpendicular $\theta = \frac{\pi}{2}$ radianes ($90^\circ$). El vector cero $\mathbf{0}$ es ortogonal a todo vector del espacio.
              </p>
            </div>

            <!-- EJEMPLO 6 DE MOORE §4.2 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.0.6: Determinación de Vectores Ortogonales en $V_3$ (Moore §4.2 Ejemplo 6, pág. 189)</div>
              <p>
                Determine todos los vectores del espacio euclidiano estándar $V_3$ ($\mathbb{R}^3$) que son ortogonales al vector dado:
                $$\alpha_0 = (2, -1, 1).$$
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Planteamiento de la Ecuación de Ortogonalidad:</div>
                <p>
                  Sea $X = (x, y, z)$ un vector genérico en $V_3$. La condición de ortogonalidad con el producto interno usual impone:
                  $$\langle X, \alpha_0 \rangle = \langle (x, y, z), (2, -1, 1) \rangle = 0 \iff 2x - y + z = 0.$$
                  Por ende, todos los vectores buscados son exactamente el conjunto solución de esta ecuación lineal homogénea.
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Estructura y Dimensión del Espacio Solución:</div>
                <p>
                  Despejando la variable $x$ en términos de los dos parámetros libres $y$ y $z$:
                  $$x = \frac{y}{2} - \frac{z}{2}.$$
                  Asignando valores a los parámetros libres:
                  $$\begin{aligned}
                    \text{Para } y = 2, \; z = 0 &\implies x = 1 \implies X_1 = (1, 2, 0), \\
                    \text{Para } y = 0, \; z = 2 &\implies x = -1 \implies X_2 = (-1, 0, 2).
                  \end{aligned}$$
                  Estos dos vectores son linealmente independientes (ninguno es múltiplo del otro) y satisfacen la ecuación:
                  $$2(1) - (2) + 0 = 0, \qquad 2(-1) - (0) + 2 = 0.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Conclusión y Subespacio Generado:</div>
                <p style="margin-bottom: 0;">
                  El conjunto de vectores ortogonales a $(2, -1, 1)$ constituye un subespacio vectorial de $V_3$ de dimensión 2 (un plano geométrico que pasa por el origen), expresable como la envolvente lineal:
                  $$W = \mathcal{L}\left\{ (1, 2, 0), \; (-1, 0, 2) \right\}.$$
                </p>
              </div>
            </div>

            <!-- DEFINICIÓN DE SUBESPACIOS ORTOGONALES (MOORE PÁG. 189) -->
            <div class="math-box box-def" style="margin-top: 1.5rem;">
              <div class="math-box-header">Definición 1.0.5: Subespacios Ortogonales (Moore §4.2 pág. 189)</div>
              <p>
                Si $W_1$ y $W_2$ son subespacios vectoriales de un espacio euclidiano $V$, se dice que $W_1$ y $W_2$ son <strong>subespacios ortogonales</strong>, denotado $W_1 \perp W_2$, si cada vector de $W_1$ es ortogonal a cada vector de $W_2$:
              </p>
              <div class="formula-card">
                $$W_1 \perp W_2 \iff \langle w_1, w_2 \rangle = 0 \quad \text{para todo } w_1 \in W_1 \text{ y todo } w_2 \in W_2.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                En concordancia con el Ejemplo 1.0.6, Moore concluye formalmente que la recta vectorial $\mathcal{L}\{(2, -1, 1)\}$ y el plano vectorial $\mathcal{L}\{(1, 2, 0), (-1, 0, 2)\}$ constituyen <strong>subespacios ortogonales</strong> de $V_3$.
              </p>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             TEOREMA DE PITÁGORAS GENERALIZADO
          ------------------------------------------------------------------ -->
          <div id="sec-1-0-teorema-pitagoras">
            <h3 style="margin-top: 2.5rem;">
              <span>Teorema de Pitágoras Generalizado</span>
              <span class="ref-badge">Moore Teorema 2.1 pág. 190</span>
            </h3>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.0.1: Teorema de Pitágoras Generalizado (Moore Teorema 2.1)</div>
              <p>
                Si $\alpha$ y $\beta$ son vectores ortogonales en un espacio euclidiano $V$, entonces:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$\|\alpha + \beta\|^2 = \|\alpha\|^2 + \|\beta\|^2.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración (Moore §4.2 pág. 190).</i></div>
                <p>
                  La hipótesis de ortogonalidad establece que $\langle \alpha, \beta \rangle = \langle \beta, \alpha \rangle = 0$. Por la definición de norma y las propiedades distributivas del producto interno:
                  $$\begin{aligned}
                    \|\alpha + \beta\|^2 &= \langle \alpha + \beta, \alpha + \beta \rangle \\
                    &= \langle \alpha, \alpha \rangle + \langle \alpha, \beta \rangle + \langle \beta, \alpha \rangle + \langle \beta, \beta \rangle \\
                    &= \langle \alpha, \alpha \rangle + 0 + 0 + \langle \beta, \beta \rangle \\
                    &= \|\alpha\|^2 + \|\beta\|^2. \quad \blacksquare
                  \end{aligned}$$
                </p>
              </div>
            </div>

            <div class="math-box box-prop" style="margin-top: 1.5rem;">
              <div class="math-box-header">Corolario 1.0.1: Extensión Inductiva a $k$ Vectores Ortogonales (Moore pág. 190)</div>
              <p>
                Si $\{\alpha_1, \alpha_2, \dots, \alpha_k\}$ es un conjunto de vectores mutuamente ortogonales en $V$ ($\langle \alpha_i, \alpha_j \rangle = 0$ para todo $i \neq j$), entonces:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\left\|\sum_{i=1}^k \alpha_i\right\|^2 = \sum_{i=1}^k \|\alpha_i\|^2.$$
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             DISTANCIA EUCLIDIANA Y DESIGUALDAD DE CAUCHY-SCHWARZ
          ------------------------------------------------------------------ -->
          <div id="sec-1-0-distancia-schwarz">
            <h3 style="margin-top: 2.5rem;">
              <span>Distancia Métrica & Desigualdad de Cauchy-Schwarz</span>
              <span class="ref-badge">Moore págs. 190–191</span>
            </h3>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.0.6: Distancia entre Vectores (Moore §4.2 pág. 190)</div>
              <p>
                En la geometría ordinaria, la distancia entre dos puntos es la longitud del segmento rectilíneo que los une. De manera análoga, en cualquier espacio euclidiano $V$, la <strong>distancia</strong> entre dos vectores $\alpha$ y $\beta$ se define como:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$d(\alpha, \beta) = \|\alpha - \beta\| = \sqrt{\langle \alpha - \beta, \alpha - \beta \rangle}.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                <em>Propiedad Pitagórica Notable:</em> Si $\alpha$ y $\beta$ son vectores ortogonales ($\alpha \perp \beta$), entonces:
                $$\|\alpha - \beta\|^2 = \|\alpha\|^2 + \|\beta\|^2 = \|\alpha + \beta\|^2 \implies \|\alpha - \beta\| = \|\alpha + \beta\|.$$
              </p>
            </div>

            <div class="math-box box-thm" style="margin-top: 1.5rem;">
              <div class="math-box-header">Lema 1.0.1: Desigualdad de Cauchy-Schwarz (Moore Lema §4.2 pág. 191)</div>
              <p>
                Para cualesquiera dos vectores $\alpha, \beta$ en un espacio euclidiano $V$, se satisface la desigualdad:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$|\langle \alpha, \beta \rangle| \leq \|\alpha\| \, \|\beta\|, \qquad \text{o equivalentemente} \qquad \langle \alpha, \beta \rangle^2 \leq \|\alpha\|^2 \|\beta\|^2.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                La igualdad se cumple si y sólo si el conjunto $\{\alpha, \beta\}$ es linealmente dependiente (uno es múltiplo escalar del otro).
              </p>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración (Método cuadrático de Moore §4.2 pág. 191).</i></div>
                <p>
                  Consideremos el vector $\alpha - b\beta$ para cualquier número real $b \in \mathbb{R}$. Por el axioma de positividad $\mathbf{(I_4)}$, su producto interno consigo mismo es siempre no negativo:
                  $$\langle \alpha - b\beta, \; \alpha - b\beta \rangle \geq 0.$$
                  Desarrollando esta expresión mediante bilinealidad:
                  $$b^2 \langle \beta, \beta \rangle - 2b\langle \alpha, \beta \rangle + \langle \alpha, \alpha \rangle \geq 0.$$
                  El miembro izquierdo es un polinomio cuadrático en la variable real $b$: $A b^2 + B b + C \geq 0$, con $A = \|\beta\|^2$, $B = -2\langle \alpha, \beta \rangle$ y $C = \|\alpha\|^2$. Dado que este polinomio cuadrático nunca toma valores estrictamente negativos para ningún valor de $b$, su discriminante $\Delta = B^2 - 4AC$ debe ser necesariamente menor o igual a cero:
                  $$\Delta = [-2\langle \alpha, \beta \rangle]^2 - 4 \|\beta\|^2 \|\alpha\|^2 = 4\left( \langle \alpha, \beta \rangle^2 - \|\alpha\|^2 \|\beta\|^2 \right) \leq 0.$$
                  Dividiendo entre 4 y transponiendo el término:
                  $$\langle \alpha, \beta \rangle^2 \leq \|\alpha\|^2 \|\beta\|^2 \implies |\langle \alpha, \beta \rangle| \leq \|\alpha\| \, \|\beta\|. \quad \blacksquare$$
                </p>
              </div>
            </div>

            <p style="margin-top: 1rem;">
              <strong>Justificación de la definición de ángulo:</strong> Moore enfatiza que este lema responde categóricamente a la pregunta de si la definición $\cos \theta = \frac{\langle \alpha, \beta \rangle}{\|\alpha\| \|\beta\|}$ tiene sentido real. En efecto, de $|\langle \alpha, \beta \rangle| \leq \|\alpha\| \|\beta\|$ se deduce que:
              $$-1 \leq \frac{\langle \alpha, \beta \rangle}{\|\alpha\| \, \|\beta\|} \leq 1,$$
              lo que garantiza sin ambigüedades que siempre existe un único ángulo geométrico $\theta \in [0, \pi]$ que satisface la ecuación trigonométrica.
            </p>
          </div>

          <!-- -----------------------------------------------------------------
             DESIGUALDAD DEL TRIÁNGULO (MINKOWSKI)
          ------------------------------------------------------------------ -->
          <div id="sec-1-0-teorema-triangulo">
            <h3 style="margin-top: 2.5rem;">
              <span>Desigualdad del Triángulo</span>
              <span class="ref-badge">Moore Teorema 2.2 pág. 191</span>
            </h3>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.0.2: Desigualdad del Triángulo (Moore Teorema 2.2)</div>
              <p>
                Si $\alpha$ y $\beta$ son vectores arbitrarios de un espacio euclidiano $V$, entonces:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$\|\alpha + \beta\| \leq \|\alpha\| + \|\beta\|.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración (Moore §4.2 pág. 191).</i></div>
                <p>
                  Sabemos a partir de las propiedades del producto interno que:
                  $$\|\alpha + \beta\|^2 = \langle \alpha + \beta, \alpha + \beta \rangle = \langle \alpha, \alpha \rangle + 2\langle \alpha, \beta \rangle + \langle \beta, \beta \rangle.$$
                  Por la Desigualdad de Cauchy-Schwarz, $\langle \alpha, \beta \rangle \leq |\langle \alpha, \beta \rangle| \leq \|\alpha\| \|\beta\|$. Por lo tanto:
                  $$\begin{aligned}
                    \|\alpha + \beta\|^2 &\leq \|\alpha\|^2 + 2\|\alpha\| \|\beta\| + \|\beta\|^2 \\
                    &= (\|\alpha\| + \|\beta\|)^2.
                  \end{aligned}$$
                  Extrayendo la raíz cuadrada no negativa en ambos miembros de la desigualdad:
                  $$\|\alpha + \beta\| \leq \|\alpha\| + \|\beta\|. \quad \blacksquare$$
                </p>
              </div>
            </div>
          </div>
        </section>
    '''
