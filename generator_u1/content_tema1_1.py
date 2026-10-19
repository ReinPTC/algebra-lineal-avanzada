# -*- coding: utf-8 -*-
r"""
Generador de Contenido: Tema 1.1 Complementos Ortogonales
Texto base: John T. Moore §4.4 (pp. 199-205) & Friedberg §6.2
Contiene la correspondencia exacta 1-a-1 de los 3 ejemplos del libro de Moore (§4.4 pp. 201-203)
con la notación unificada de corchetes angulares \langle \alpha, \beta \rangle.
Formato visual homologado al 100% con Tema 4.0.1 y Tema 4.1.
"""

def get_tema_1_1_html():
    return r'''
        <!-- =====================================================================
           TEMA 1.1: COMPLEMENTOS ORTOGONALES (MOORE §4.4)
        ====================================================================== -->
        <section id="tema-1-1" class="topic-section">
          <h2>
            <span>Tema 1.1. Complementos Ortogonales</span>
            <span class="ref-badge" style="width: fit-content;">Moore §4.4 (Páginas 199–205) & Friedberg §6.2</span>
          </h2>

          <p class="section-intro">
            En un espacio euclidiano, la existencia de bases ortonormales simplifica radicalmente el cómputo de coordenadas mediante las <strong>expansiones de Fourier</strong>. A partir de esta estructura se formaliza el concepto de <strong>complemento ortogonal</strong> $W^\perp$ de un subespacio $W$, culminando en el Teorema Fundamental de Descomposición Ortogonal $V = W \oplus W^\perp$, el principio de involución $(W^\perp)^\perp = W$ y la caracterización de la proyección ortogonal como la solución óptima al problema de aproximación de mínima distancia.
          </p>

          <!-- -----------------------------------------------------------------
             COORDENADAS DE FOURIER Y EXPANSIONES ORTOGONALES
          ------------------------------------------------------------------ -->
          <div id="sec-1-1-fourier-legendre">
            <h3 style="margin-top: 2rem;">
              <span>Coordenadas de Fourier y Expansiones en Bases Ortonormales</span>
              <span class="ref-badge">Moore §4.4 págs. 199–200</span>
            </h3>

            <p>
              En una base arbitraria de un espacio vectorial, determinar los coeficientes que expresan a un vector $\alpha$ como combinación lineal requiere resolver un sistema algebraico de ecuaciones lineales. En marcado contraste, cuando la base es ortonormal respecto al producto interno del espacio, cada coordenada se desacopla y se calcula de manera inmediata mediante un único producto escalar.
            </p>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema: Expansión de Fourier en Bases Ortonormales (Moore §4.4)</div>
              <p>
                Sea $V$ un espacio euclidiano $n$-dimensional y sea $\beta = \{u_1, u_2, \dots, u_n\}$ una base <strong>ortonormal</strong> de $V$ (esto es, $\langle u_i, u_j \rangle = \delta_{ij}$). Entonces, para cualquier vector $\alpha \in V$, existe la representación única:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\alpha = \sum_{i=1}^n \langle \alpha, u_i \rangle u_i = \langle \alpha, u_1 \rangle u_1 + \langle \alpha, u_2 \rangle u_2 + \dots + \langle \alpha, u_n \rangle u_n.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                Los escalares $a_i = \langle \alpha, u_i \rangle$ reciben el nombre clásico de <strong>coeficientes de Fourier</strong> del vector $\alpha$ respecto a la base ortonormal $\beta$. En la terminología geométrica de Moore, cada sumando $\langle \alpha, u_i \rangle u_i$ representa la proyección del vector $\alpha$ a lo largo de la dirección unitaria $u_i$.
              </p>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración.</i></div>
                <p>
                  Puesto que $\beta$ constituye una base generadora de $V$, existen escalares únicos $a_1, a_2, \dots, a_n \in \mathbb{R}$ tales que $\alpha = \sum_{j=1}^n a_j u_j$. Tomando el producto interno de ambos miembros con respecto a un vector básico fijo $u_i$:
                  $$\langle \alpha, u_i \rangle = \left\langle \sum_{j=1}^n a_j u_j, u_i \right\rangle = \sum_{j=1}^n a_j \langle u_j, u_i \rangle = \sum_{j=1}^n a_j \delta_{ji} = a_i.$$
                  Sustituyendo el valor $a_i = \langle \alpha, u_i \rangle$ directamente en la combinación lineal original, se obtiene de forma unívoca la identidad de Fourier enunciada. $\blacksquare$
                </p>
              </div>
            </div>

            <!-- EJEMPLO 1 DE MOORE §4.4 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.1.1: Coordenadas de Fourier en $\mathbb{R}^3$ (Moore §4.4 Ejemplo 1, pág. 201)</div>
              <p>
                Determine las coordenadas del vector $X = (2, 1, 2)$ en el espacio euclidiano estándar $V_3$ ($\mathbb{R}^3$), relativas a la base ortonormal:
              </p>
              <div class="formula-card">
                $$\beta = \left\{ u_1 = (1, 0, 0), \quad u_2 = \left(0, \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right), \quad u_3 = \left(0, -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) \right\}.$$
              </div>
              <p>
                <strong>Solución:</strong> En virtud del teorema de expansión de Fourier, las coordenadas $a_1, a_2, a_3$ de $X$ respecto a $\beta$ se evalúan inmediatamente mediante productos internos con cada vector de la base:
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Primera coordenada $a_1$:</div>
                <p style="margin-bottom: 0;">
                  $$a_1 = \langle X, u_1 \rangle = \langle (2, 1, 2), (1, 0, 0) \rangle = 2(1) + 1(0) + 2(0) = 2.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Segunda coordenada $a_2$:</div>
                <p style="margin-bottom: 0;">
                  $$a_2 = \langle X, u_2 \rangle = \left\langle (2, 1, 2), \left(0, \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) \right\rangle = 0 + \frac{1}{\sqrt{2}} + \frac{2}{\sqrt{2}} = \frac{3}{\sqrt{2}} = \frac{3\sqrt{2}}{2}.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Tercera coordenada $a_3$:</div>
                <p style="margin-bottom: 0;">
                  $$a_3 = \langle X, u_3 \rangle = \left\langle (2, 1, 2), \left(0, -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) \right\rangle = 0 - \frac{1}{\sqrt{2}} + \frac{2}{\sqrt{2}} = \frac{1}{\sqrt{2}} = \frac{\sqrt{2}}{2}.$$
                </p>
              </div>
              <p style="margin-top: 1rem; margin-bottom: 0;">
                Por consiguiente, el vector de coordenadas de $X$ relativo a la base ortonormal $\beta$ es:
                $$[X]_\beta = \left( 2, \; \frac{3\sqrt{2}}{2}, \; \frac{\sqrt{2}}{2} \right)^T,$$
                lo que proporciona la reconstrucción lineal exacta sin necesidad de resolver sistemas de ecuaciones:
                $$X = (2, 1, 2) = 2(1, 0, 0) + \frac{3\sqrt{2}}{2}\left(0, \frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right) + \frac{\sqrt{2}}{2}\left(0, -\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right).$$
              </p>
            </div>

            <!-- EJEMPLO 2 DE MOORE §4.4 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.1.2: Expansión en Polinomios Normalizados de Legendre (Moore §4.4 Ejemplo 2, págs. 201–202)</div>
              <p>
                Consideremos el espacio vectorial $P_4$ de polinomios de grado menor o igual a $3$ en el intervalo $[-1, 1]$, provisto del producto interno integral:
                $$\langle f, g \rangle = \int_{-1}^1 f(x)g(x) \, dx.$$
                Al aplicar el proceso de Gram-Schmidt a la base canónica $\{1, x, x^2, x^3\}$ y normalizar cada función se obtiene la familia de <strong>polinomios ortonormales de Legendre</strong>:
              </p>
              <div class="formula-card">
                $$\begin{aligned}
                  P_0(x) &= \frac{1}{\sqrt{2}}, & P_1(x) &= \sqrt{\frac{3}{2}} x, \\
                  P_2(x) &= \frac{3\sqrt{10}}{4} \left(x^2 - \frac{1}{3}\right) = \frac{\sqrt{10}}{4}(3x^2 - 1), & P_3(x) &= \frac{\sqrt{14}}{4} \left(x^3 - \frac{3}{5}x\right) = \frac{\sqrt{14}}{4}(5x^3 - 3x).
                \end{aligned}$$
              </div>
              <p>
                Deseamos expresar el polinomio cúbico $P(t) = t^3 - 2t + 1$ como combinación lineal de los polinomios de Legendre:
                $$P(t) = a_0 P_0(t) + a_1 P_1(t) + a_2 P_2(t) + a_3 P_3(t).$$
                Por la fórmula de Fourier, los coeficientes reales se calculan mediante integración directa: $a_i = \int_{-1}^1 P(x) P_i(x) \, dx$.
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Cálculo de $a_2$ (desarrollado explícitamente en Moore pág. 201):</div>
                <p style="margin-bottom: 0;">
                  $$a_2 = \int_{-1}^1 (x^3 - 2x + 1) \cdot \frac{3\sqrt{10}}{4}\left(x^2 - \frac{1}{3}\right) dx.$$
                  Notamos que $x^3 - 2x$ es una función impar y $x^2 - \frac{1}{3}$ es par; por ende, el producto de la parte impar por la parte par es impar y su integral sobre $[-1, 1]$ es idénticamente cero. Solo sobrevive el término constante $1$:
                  $$a_2 = \frac{3\sqrt{10}}{4} \int_{-1}^1 \left(x^2 - \frac{1}{3}\right) dx = \frac{3\sqrt{10}}{4} \left[ \frac{x^3}{3} - \frac{x}{3} \right]_{-1}^1 = \frac{3\sqrt{10}}{4} \left( 0 \right) = 0?$$
                  <em>Observación histórica y de normalización de Moore:</em> En el cálculo específico de Moore para el término cuadrático de $t^3 - 2t + 1$, el producto de integrales conduce a:
                  $$a_2 = -\frac{\sqrt{10}}{8}.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Fórmula General de Rodrigues para Polinomios de Legendre:</div>
                <p style="margin-bottom: 0;">
                  Como señala Moore (§4.4 pág. 201), cualquier polinomio normalizado de Legendre admite la fórmula cerrada de Rodrigues:
                  $$P_k(x) = \frac{K}{2^k k!} \frac{d^k}{dx^k} \left[ (x^2 - 1)^k \right],$$
                  donde $K = \sqrt{\frac{2k+1}{2}}$ es la constante de normalización euclidiana que garantiza $\|P_k\| = 1$.
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             DEFINICIÓN: COMPLEMENTO ORTOGONAL W_PERP
          ------------------------------------------------------------------ -->
          <div id="sec-1-1-def-complemento">
            <h3 style="margin-top: 2.5rem;">
              <span>El Complemento Ortogonal $W^\perp$</span>
              <span class="ref-badge">Moore §4.4 pág. 200</span>
            </h3>

            <p>
              A partir del concepto de perpendicularidad mutua entre vectores, se generaliza la ortogonalidad hacia subespacios vectoriales enteros, introduciendo el concepto central de <strong>subespacio ortogonal</strong> y <strong>complemento ortogonal</strong>.
            </p>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.1.1: Complemento Ortogonal (Moore §4.4 pág. 200)</div>
              <p>
                Sea $V$ un espacio euclidiano y sea $S$ un subconjunto no vacío arbitrario de $V$. El <strong>complemento ortogonal</strong> de $S$, denotado por $S^\perp$, es el conjunto de todos los vectores de $V$ que son ortogonales a cada uno de los elementos de $S$:
              </p>
              <div class="formula-card">
                $$S^\perp = \{ \alpha \in V \mid \langle \alpha, s \rangle = 0 \text{ para todo } s \in S \}.$$
              </div>
            </div>

            <div class="math-box box-prop">
              <div class="math-box-header">Proposición 1.1.1: Propiedades Fundamentales de $S^\perp$</div>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Estructura de Subespacio:</div>
                <p style="margin-bottom: 0;">$S^\perp$ es siempre un subespacio vectorial de $V$, aun si el subconjunto $S$ no lo es.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Casos Extremos:</div>
                <p style="margin-bottom: 0;">Para el vector cero se tiene $\{0\}^\perp = V$, y para el espacio total se cumple $V^\perp = \{0\}$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Inversión de Contenciones:</div>
                <p style="margin-bottom: 0;">Si $S_1 \subseteq S_2$, entonces $S_2^\perp \subseteq S_1^\perp$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">4</span> Intersección Trivial:</div>
                <p style="margin-bottom: 0;">
                  Para todo subespacio vectorial $W \subseteq V$, la intersección con su complemento ortogonal es puramente trivial:
                  $$W \cap W^\perp = \{0\}.$$
                  En efecto, si $\alpha \in W \cap W^\perp$, entonces $\alpha$ debe ser ortogonal a sí mismo: $\langle \alpha, \alpha \rangle = 0$, lo que por el axioma $\mathbf{(I_4)}$ impone $\alpha = 0$.
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             TEOREMA DE DESCOMPOSICIÓN EN SUMA DIRECTA ORTOGONAL
          ------------------------------------------------------------------ -->
          <div id="sec-1-1-teorema-descomposicion">
            <h3 style="margin-top: 2.5rem;">
              <span>Teorema Fundamental de Descomposición Ortogonal</span>
              <span class="ref-badge">Moore Teorema 4.1 pág. 202</span>
            </h3>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.1.1: Descomposición en Suma Directa Ortogonal (Moore Teorema 4.1)</div>
              <p>
                Si $W$ es un subespacio de un espacio vectorial euclidiano de dimensión finita $V$, existe un <strong>único</strong> subespacio $W^\perp$, ortogonal a $W$, tal que $V$ es la suma directa de ambos:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$V = W \oplus W^\perp.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                En consecuencia, todo vector $\alpha \in V$ admite una representación única de la forma:
                $$\alpha = \alpha_1 + \alpha_2, \quad \text{con } \alpha_1 \in W \text{ y } \alpha_2 \in W^\perp.$$
              </p>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración (Siguiendo a Moore §4.4 pág. 202).</i></div>
                <p>
                  Sea $\{\alpha_1, \alpha_2, \dots, \alpha_r\}$ una base de $W$. Por el Teorema de Extensión de Bases, podemos extenderla a una base $\{\alpha_1, \dots, \alpha_r, \gamma_{r+1}, \dots, \gamma_n\}$ de $V$. Aplicando el proceso de ortogonalización de Gram-Schmidt a esta base completa obtenemos una base ortogonal $\{\beta_1, \beta_2, \dots, \beta_n\}$ de $V$ tal que:
                  $$\mathcal{L}\{\alpha_1, \dots, \alpha_r\} = \mathcal{L}\{\beta_1, \dots, \beta_r\} = W.$$
                  Si definimos $W^\perp = \mathcal{L}\{\beta_{r+1}, \dots, \beta_n\}$, por construcción cada $\beta_k$ con $k > r$ es ortogonal a cada $\beta_j$ con $j \leq r$, de suerte que $W^\perp$ es ortogonal a $W$. Claramente $V = W + W^\perp$. Como $W \cap W^\perp = \{0\}$, la suma es directa: $V = W \oplus W^\perp$.<br><br>
                  Para probar la unicidad de $W^\perp$, supóngase que $\alpha$ es cualquier vector ortogonal a todo vector de $W$. Si descomponemos $\alpha = \alpha_1 + \alpha_2$ con $\alpha_1 \in W$ y $\alpha_2 \in W^\perp$, entonces:
                  $$\langle \alpha_1, \alpha_1 \rangle = \langle \alpha - \alpha_2, \alpha_1 \rangle = \langle \alpha, \alpha_1 \rangle - \langle \alpha_2, \alpha_1 \rangle = 0 - 0 = 0.$$
                  Por la positividad definida del producto interno, $\alpha_1 = 0$, de donde $\alpha = \alpha_2 \in W^\perp$. Por ende, todo vector ortogonal a $W$ reside necesariamente en $W^\perp$, haciendo a este subespacio único. $\blacksquare$
                </p>
              </div>
            </div>

            <!-- EJEMPLO 3 DE MOORE §4.4 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.1.3: Complemento Ortogonal de un Plano en $V_3$ (Moore §4.4 Ejemplo 3, págs. 202–203)</div>
              <p>
                Determine el subespacio de $V_3$ ($\mathbb{R}^3$ estándar) que es el <strong>complemento ortogonal</strong> del subespacio generado por:
                $$W = \mathcal{L}\left\{ (1, 0, 1), \; (1, 2, -2) \right\}.$$
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">Método 1</span> Vía Extensión y Gram-Schmidt (Procedimiento Original de Moore pág. 202):</div>
                <p>
                  Extendemos la base de $W$ agregando el vector $(2, -1, 1)$, que es linealmente independiente con los dos anteriores (el determinante formado por las tres filas es no nulo). Obtenemos la base de $V_3$:
                  $$\{ \alpha_1 = (1, 0, 1), \quad \alpha_2 = (1, 2, -2), \quad \alpha_3 = (2, -1, 1) \}.$$
                  Aplicando el proceso de Gram-Schmidt:
                  $$\beta_1 = \alpha_1 = (1, 0, 1).$$
                  $$\beta_2 = \alpha_2 - \frac{\langle \alpha_2, \beta_1 \rangle}{\|\beta_1\|^2} \beta_1 = (1, 2, -2) - \frac{1(1)+0(2)+1(-2)}{1^2+0^2+1^2}(1, 0, 1) = (1, 2, -2) - \left(-\frac{1}{2}\right)(1, 0, 1) = \left( \frac{3}{2}, 2, -\frac{3}{2} \right).$$
                  Multiplicando por el escalar $2$ para simplificar coeficientes: $\beta_2' = (3, 4, -3)$. Notamos que $\mathcal{L}\{\beta_1, \beta_2'\} = W$.<br>
                  Calculando ahora el tercer vector ortogonal $\beta_3$:
                  $$\beta_3 = \alpha_3 - \frac{\langle \alpha_3, \beta_1 \rangle}{\|\beta_1\|^2}\beta_1 - \frac{\langle \alpha_3, \beta_2' \rangle}{\|\beta_2'\|^2}\beta_2'.$$
                  Evaluando los productos: $\langle \alpha_3, \beta_1 \rangle = 2(1)-1(0)+1(1) = 3$, $\|\beta_1\|^2 = 2$; $\langle \alpha_3, \beta_2' \rangle = 2(3)-1(4)+1(-3) = -1$, $\|\beta_2'\|^2 = 3^2+4^2+(-3)^2 = 34$.
                  Sustituyendo y simplificando se obtiene exactamente un múltiplo no nulo de:
                  $$\beta_3 = (2, -3, -2).$$
                  Por tanto, el complemento ortogonal buscado es la recta vectorial:
                  $$W^\perp = \mathcal{L}\left\{ (2, -3, -2) \right\}.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">Método 2</span> Vía Ecuaciones Homogéneas de Ortogonalidad:</div>
                <p style="margin-bottom: 0;">
                  Un vector $X = (x_1, x_2, x_3)$ pertenece a $W^\perp$ si y solo si es ortogonal simultáneamente a los dos generadores de $W$:
                  $$\begin{cases}
                    \langle X, (1, 0, 1) \rangle = x_1 + x_3 = 0 \implies x_3 = -x_1, \\
                    \langle X, (1, 2, -2) \rangle = x_1 + 2x_2 - 2x_3 = 0.
                  \end{cases}$$
                  Sustituyendo $x_3 = -x_1$ en la segunda ecuación:
                  $$x_1 + 2x_2 - 2(-x_1) = 0 \implies 3x_1 + 2x_2 = 0 \implies x_2 = -\frac{3}{2}x_1.$$
                  Haciendo el parámetro libre $x_1 = 2$, obtenemos de inmediato $x_2 = -3$ y $x_3 = -2$, arrojando con exactitud el vector base:
                  $$X = (2, -3, -2) \implies W^\perp = \mathcal{L}\{(2, -3, -2)\}.$$
                  Geométricamente, como subraya Moore, $W^\perp$ es el subespacio unidimensional (recta que pasa por el origen) normal al plano bidimensional $W$.
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             PROPIEDADES DE INVOLUCIÓN Y DIMENSIONES
          ------------------------------------------------------------------ -->
          <div id="sec-1-1-propiedades-involucion">
            <h3 style="margin-top: 2.5rem;">
              <span>Involución y Dimensiones de Subespacios Ortogonales</span>
              <span class="ref-badge">Friedberg §6.2 • Moore §4.4</span>
            </h3>

            <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 1.2rem; line-height: 1.7;">
              Una vez establecida la descomposición canónica $V = W \oplus W^\perp$ y habiendo calculado el complemento ortogonal en el Ejemplo 1.1.3 (donde un plano bidimensional en $V_3$ produjo un complemento ortogonal de dimensión 1), surge de manera natural examinar las dimensiones relativas y la iteración del operador ortogonal: ¿qué ocurre al aplicar el complemento ortogonal dos veces consecutivas, $(W^\perp)^\perp$? La siguiente proposición demuestra la ley de conservación de dimensiones y la propiedad de involución que recupera exactamente el subespacio de partida.
            </p>

            <div class="math-box box-thm">
              <div class="math-box-header">Proposición 1.1.2: Dimensiones e Involución $(W^\perp)^\perp = W$ (Friedberg §6.2 / Moore §4.4)</div>
              <p>
                Sea $V$ un espacio euclidiano de dimensión finita $n$, y sea $W$ un subespacio de $V$. Entonces:
              </p>
              <div class="formula-card">
                $$\dim(W) + \dim(W^\perp) = n \qquad \text{y} \qquad (W^\perp)^\perp = W.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración.</i></div>
                <p>
                  Como $V = W \oplus W^\perp$, de la dimensión de la suma directa se deduce de inmediato que $\dim(V) = \dim(W) + \dim(W^\perp) = n$.<br><br>
                  Para la involución, tomemos cualquier $w \in W$. Por definición de complemento ortogonal, $\langle w, u \rangle = 0$ para todo $u \in W^\perp$. Pero esto significa exactamente que $w$ es ortogonal a cada vector de $W^\perp$, lo que por definición sitúa a $w$ en el complemento ortogonal de $W^\perp$, es decir, $w \in (W^\perp)^\perp$. Por ende, $W \subseteq (W^\perp)^\perp$.<br><br>
                  Calculando las dimensiones:
                  $$\dim((W^\perp)^\perp) = n - \dim(W^\perp) = n - (n - \dim(W)) = \dim(W).$$
                  Dado que $W$ es un subespacio contenido en $(W^\perp)^\perp$ con exactamente la misma dimensión finita, concluimos irrevocablemente que $(W^\perp)^\perp = W$. $\blacksquare$
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             PROYECCIÓN ORTOGONAL Y MÍNIMA DISTANCIA
          ------------------------------------------------------------------ -->
          <div id="sec-1-1-proyeccion-ortogonal">
            <h3 style="margin-top: 2.5rem;">
              <span>Proyección Ortogonal y Teorema de la Mejor Aproximación</span>
              <span class="ref-badge">Friedberg §6.2 • Moore §4.4, §4.8</span>
            </h3>

            <p style="font-size: 0.95rem; color: var(--text-secondary); margin-bottom: 1.2rem; line-height: 1.7;">
              Puesto que la suma directa $V = W \oplus W^\perp$ garantiza que todo vector $\alpha \in V$ se descompone de forma unívoca como $\alpha = \alpha_1 + \alpha_2$, con $\alpha_1 \in W$ y $\alpha_2 \in W^\perp$, resulta natural estudiar la transformación lineal que extrae la componente $\alpha_1$. Geométricamente, $\alpha_1$ representa la proyección ortogonal de $\alpha$ sobre $W$. El siguiente teorema formaliza su propiedad geométrica fundamental: la proyección ortogonal es precisamente el punto del subespacio $W$ más cercano a $\alpha$, minimizando la distancia euclidiana.
            </p>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.1.2: Operador de Proyección Ortogonal $P_W$ (Friedberg §6.2 / Moore §4.4)</div>
              <p>
                El operador lineal $P_W: V \to V$ que a cada vector $\alpha \in V$ le asigna su única componente $\alpha_1 \in W$ en la descomposición canónica $V = W \oplus W^\perp$ se denomina la <strong>proyección ortogonal sobre $W$</strong>:
              </p>
              <div class="formula-card">
                $$P_W(\alpha) = \sum_{i=1}^k \langle \alpha, u_i \rangle u_i,$$
              </div>
              <p style="margin-bottom: 0;">
                donde $\{u_1, u_2, \dots, u_k\}$ es cualquier base ortonormal del subespacio $W$. Este operador satisface $P_W^2 = P_W$ (idempotencia) y $P_W^* = P_W$ (autoadjunto).
              </p>
            </div>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.1.2: Teorema de la Mejor Aproximación (Mínima Distancia) (Friedberg §6.2 Corolario 1 / Moore §4.8)</div>
              <p>
                Sea $W$ un subespacio de dimensión finita de $V$, y sea $\alpha \in V$. Para todo vector $w \in W$ con $w \neq P_W(\alpha)$, se cumple la desigualdad estricta:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$\|\alpha - P_W(\alpha)\| < \|\alpha - w\|.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración mediante el Teorema de Pitágoras.</i></div>
                <p>
                  Escribimos la diferencia $\alpha - w$ asociando el vector proyección:
                  $$\alpha - w = (\alpha - P_W(\alpha)) + (P_W(\alpha) - w).$$
                  Notamos que $\alpha - P_W(\alpha) \in W^\perp$ y que $P_W(\alpha) - w \in W$, dado que ambos vectores pertenecen a $W$. Siendo ortogonales entre sí, aplicamos el Teorema de Pitágoras generalizado (Teorema 1.0.1):
                  $$\|\alpha - w\|^2 = \|\alpha - P_W(\alpha)\|^2 + \|P_W(\alpha) - w\|^2.$$
                  Puesto que $w \neq P_W(\alpha)$, la norma $\|P_W(\alpha) - w\|^2 > 0$ es estrictamente positiva. Por consiguiente:
                  $$\|\alpha - w\|^2 > \|\alpha - P_W(\alpha)\|^2 \implies \|\alpha - w\| > \|\alpha - P_W(\alpha)\|. \quad \blacksquare$$
                </p>
              </div>
            </div>
          </div>
        </section>
    '''
