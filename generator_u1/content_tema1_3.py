# -*- coding: utf-8 -*-
r"""
Generador de Contenido: Tema 1.3 Funcionales Lineales y Operadores Adjuntos
Texto base: John T. Moore §4.6 (pp. 213-220) & Friedberg §6.3
Contiene la correspondencia exacta 1-a-1 de los 5 ejemplos del libro de Moore (§4.6 pp. 214-216)
con la notación unificada de corchetes angulares \langle \alpha, \beta \rangle.
Formato visual homologado al 100% con Tema 4.0.1 y Tema 4.1.
"""

def get_tema_1_3_html():
    return r'''
        <!-- =====================================================================
           TEMA 1.3: FUNCIONALES LINEALES Y ADJUNTOS (MOORE §4.6)
        ====================================================================== -->
        <section id="tema-1-3" class="topic-section">
          <h2>
            <span>Tema 1.3. Funcionales Lineales y Operadores Adjuntos</span>
            <span class="ref-badge" style="width: fit-content;">Moore §4.6 (Páginas 213–220) & Friedberg §6.3</span>
          </h2>

          <p class="section-intro">
            El espacio dual de un espacio euclidiano exhibe una estructura canónica revelada por el <strong>Teorema de Representación de Riesz</strong>: todo funcional lineal es expresable como el producto interno contra un vector fijo y unívoco. Esta correspondencia fundamenta la existencia y unicidad del <strong>operador adjunto</strong> $T^*$, su vínculo directo con la transpuesta matricial en bases ortonormales ($[T^*]_\beta = [T]_\beta^T$), las relaciones fundamentales de ortogonalidad del núcleo e imagen, y los operadores autoadjuntos o simétricos.
          </p>

          <!-- -----------------------------------------------------------------
             TEOREMA DE REPRESENTACIÓN DE RIESZ
          ------------------------------------------------------------------ -->
          <div id="sec-1-3-teorema-riesz">
            <h3 style="margin-top: 2rem;">
              <span>El Teorema de Representación de Riesz</span>
              <span class="ref-badge">Moore Teorema 6.1 pág. 214</span>
            </h3>

            <p>
              Un funcional lineal sobre un espacio vectorial $V$ es una transformación lineal $f: V \to \mathbb{R}$. En un espacio euclidiano de dimensión finita, el producto interno permite "capturar" todo funcional lineal a través de un vector geométrico del propio espacio.
            </p>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.3.1: Teorema de Representación de Riesz (Moore Teorema 6.1)</div>
              <p>
                Sea $V$ un espacio euclidiano de dimensión finita con producto interno $\langle \cdot, \cdot \rangle$. Si $f: V \to \mathbb{R}$ es cualquier funcional lineal sobre $V$, entonces existe un <strong>único vector</strong> $\beta \in V$ tal que:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$f(\alpha) = \langle \alpha, \beta \rangle \quad \text{para todo } \alpha \in V.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración constructiva (Moore §4.6 pág. 214).</i></div>
                <p>
                  Sea $\{u_1, u_2, \dots, u_n\}$ una base ortonormal de $V$. Por la fórmula de Fourier, todo vector $\alpha \in V$ se descompone como $\alpha = \sum_{i=1}^n \langle \alpha, u_i \rangle u_i$. Aplicando la linealidad de $f$:
                  $$f(\alpha) = f\left(\sum_{i=1}^n \langle \alpha, u_i \rangle u_i\right) = \sum_{i=1}^n \langle \alpha, u_i \rangle f(u_i) = \left\langle \alpha, \sum_{i=1}^n f(u_i) u_i \right\rangle.$$
                  Definiendo el vector $\beta = \sum_{i=1}^n f(u_i) u_i \in V$, se cumple $f(\alpha) = \langle \alpha, \beta \rangle$ para todo $\alpha \in V$.<br><br>
                  Para la unicidad, supóngase que existe otro vector $\gamma \in V$ tal que $f(\alpha) = \langle \alpha, \gamma \rangle$ para todo $\alpha \in V$. Entonces $\langle \alpha, \beta \rangle - \langle \alpha, \gamma \rangle = \langle \alpha, \beta - \gamma \rangle = 0$ para todo $\alpha$. Tomando en particular $\alpha = \beta - \gamma$:
                  $$\langle \beta - \gamma, \beta - \gamma \rangle = 0 \implies \beta - \gamma = 0 \implies \gamma = \beta. \quad \blacksquare$$
                </p>
              </div>
            </div>

            <!-- EJEMPLO 1 DE MOORE §4.6 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.3.1: Funcional Determinado por un Vector en $V_3$ (Moore §4.6 Ejemplo 1, pág. 214)</div>
              <p>
                Sea $Y = (1, 2, 3)$ un vector fijo en el espacio euclidiano estándar $V_3$ ($\mathbb{R}^3$). Para cualquier vector arbitrario $X = (x_1, x_2, x_3) \in V_3$, definimos el funcional lineal:
              </p>
              <div class="formula-card">
                $$f_Y(X) = \langle X, Y \rangle = x_1(1) + x_2(2) + x_3(3) = x_1 + 2x_2 + 3x_3.$$
              </div>
              <p>
                Este es el funcional lineal en $V_3$ determinado por $Y$. En particular, si evaluamos en el vector $X = (-1, 0, 1)$:
                $$f_Y(X) = \langle (-1, 0, 1), (1, 2, 3) \rangle = -1(1) + 0(2) + 1(3) = -1 + 0 + 3 = 2.$$
              </p>
            </div>

            <!-- EJEMPLO 2 DE MOORE §4.6 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.3.2: Reconstrucción del Vector Representador de Riesz (Moore §4.6 Ejemplo 2, pág. 214)</div>
              <p>
                Sea $\{X_1, X_2, X_3\}$ una base ortonormal de $V_3$, dada por:
              </p>
              <div class="formula-card">
                $$X_1 = \left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right), \quad X_2 = \left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right), \quad X_3 = (0, 0, 1).$$
              </div>
              <p>
                Sea $f$ un funcional lineal sobre $V_3$ cuyos valores sobre los vectores de la base son:
                $$f(X_1) = 2, \quad f(X_2) = -1, \quad f(X_3) = 1.$$
                Determine el vector $Y \in V_3$ tal que $f(X) = \langle X, Y \rangle$ para todo $X \in V_3$.
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">Solución</span> Aplicación de la fórmula constructiva de Riesz:</div>
                <p style="margin-bottom: 0;">
                  Por la demostración del Teorema de Riesz (Teorema 1.3.1), el vector representador $Y$ viene dado directamente por la combinación de los valores del funcional con la base ortonormal:
                  $$\begin{aligned}
                    Y &= f(X_1)X_1 + f(X_2)X_2 + f(X_3)X_3 \\
                    &= 2X_1 - X_2 + X_3 \\
                    &= 2\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right) - \left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}, 0\right) + (0, 0, 1) \\
                    &= \left(\frac{2}{\sqrt{2}} + \frac{1}{\sqrt{2}}, \; \frac{2}{\sqrt{2}} - \frac{1}{\sqrt{2}}, \; 0 + 0 + 1\right) \\
                    &= \left(\frac{3}{\sqrt{2}}, \; \frac{1}{\sqrt{2}}, \; 1\right).
                  \end{aligned}$$
                  Podemos verificar inmediatamente: $\langle X_1, Y \rangle = \frac{3}{2} + \frac{1}{2} + 0 = 2 = f(X_1)$, $\langle X_2, Y \rangle = -\frac{3}{2} + \frac{1}{2} + 0 = -1 = f(X_2)$ y $\langle X_3, Y \rangle = 1 = f(X_3)$.
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             1.3.1 OPERADOR ADJUNTO T*
          ------------------------------------------------------------------ -->
          <div id="sec-1-3-1-operador-adjunto">
            <h3 style="margin-top: 2.5rem;">
              <span>1.3.1 El Operador Adjunto $T^*$</span>
              <span class="ref-badge">Moore Teorema 6.2 pág. 215</span>
            </h3>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.3.2: Existencia y Unicidad del Operador Adjunto (Moore Teorema 6.2)</div>
              <p>
                Sea $V$ un espacio euclidiano de dimensión finita y sea $T: V \to V$ un operador lineal. Existe un <strong>único operador lineal</strong> $T^*: V \to V$ (llamado el <em>adjunto</em> de $T$) que satisface:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\langle T(\alpha), \beta \rangle = \langle \alpha, T^*(\beta) \rangle \quad \text{para todos } \alpha, \beta \in V.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración mediante el Teorema de Riesz (Moore §4.6 pág. 215).</i></div>
                <p>
                  Fijado un vector arbitrario $\beta \in V$, la aplicación $\alpha \mapsto \langle T(\alpha), \beta \rangle$ define un funcional lineal sobre $V$, pues:
                  $$\langle T(c_1 \alpha_1 + c_2 \alpha_2), \beta \rangle = \langle c_1 T(\alpha_1) + c_2 T(\alpha_2), \beta \rangle = c_1 \langle T(\alpha_1), \beta \rangle + c_2 \langle T(\alpha_2), \beta \rangle.$$
                  Por el Teorema de Riesz (Teorema 1.3.1), existe un único vector en $V$, que denotamos por $\beta' = T^*(\beta)$, tal que $\langle T(\alpha), \beta \rangle = \langle \alpha, \beta' \rangle$ para todo $\alpha \in V$. Esto define unívocamente la correspondencia $\beta \mapsto T^*(\beta)$.<br><br>
                  Para verificar que $T^*$ es lineal, tomemos $\beta, \gamma \in V$ y escalares $a, b \in \mathbb{R}$:
                  $$\begin{aligned}
                    \langle \alpha, T^*(a\beta + b\gamma) \rangle &= \langle T(\alpha), a\beta + b\gamma \rangle = a\langle T(\alpha), \beta \rangle + b\langle T(\alpha), \gamma \rangle \\
                    &= a\langle \alpha, T^*(\beta) \rangle + b\langle \alpha, T^*(\gamma) \rangle = \langle \alpha, a T^*(\beta) + b T^*(\gamma) \rangle.
                  \end{aligned}$$
                  Como esta igualdad se cumple para todo $\alpha \in V$, se concluye que $T^*(a\beta + b\gamma) = a T^*(\beta) + b T^*(\gamma)$, demostrando la linealidad estricta de $T^*$. $\blacksquare$
                </p>
              </div>
            </div>

            <!-- EJEMPLO 3 DE MOORE §4.6 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.3.3: Operador Adjunto en $V_3$ (Moore §4.6 Ejemplo 3, pág. 215)</div>
              <p>
                Sea $T$ el operador lineal definido en el espacio euclidiano estándar $V_3$ ($\mathbb{R}^3$) mediante:
                $$T(a, b, c) = (a + b, \; b, \; a + b + c), \quad \text{para todo } (a, b, c) \in V_3.$$
                Determine explícitamente su operador adjunto $T^*$.
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">Solución</span> Aplicación de la identidad definitoria $\langle T(\alpha), \beta \rangle = \langle \alpha, T^*(\beta) \rangle$:</div>
                <p>
                  Sea $(x, y, z) \in V_3$ un vector fijo. Por la definición del adjunto se requiere que:
                  $$\langle T(a, b, c), (x, y, z) \rangle = \langle (a, b, c), T^*(x, y, z) \rangle.$$
                  Desarrollando el primer miembro con el producto punto estándar:
                  $$\begin{aligned}
                    \langle T(a, b, c), (x, y, z) \rangle &= \langle (a + b, \; b, \; a + b + c), \; (x, y, z) \rangle \\
                    &= (a + b)x + by + (a + b + c)z \\
                    &= ax + bx + by + az + bz + cz.
                  \end{aligned}$$
                  Agrupando ahora los términos en función de los componentes $a, b, c$ del vector original:
                  $$\begin{aligned}
                    &= a(x + z) + b(x + y + z) + c(z) \\
                    &= \langle (a, b, c), \; (x + z, \; x + y + z, \; z) \rangle.
                  \end{aligned}$$
                  Puesto que $(a, b, c)$ y $(x, y, z)$ son vectores arbitrarios de $V_3$, concluimos que:
                  $$T^*(x, y, z) = (x + z, \; x + y + z, \; z).$$
                </p>
              </div>
            </div>

            <!-- EJEMPLO 4 DE MOORE §4.6 -->
            <div class="math-box box-ex" style="margin-top: 1.5rem;">
              <div class="math-box-header">Ejemplo 1.3.4: Adjunto del Operador Derivación en Espacios de Polinomios (Moore §4.6 Ejemplo 4, págs. 215–216)</div>
              <p>
                Sea $V = P_2[0, 1]$ el espacio euclidiano de polinomios reales de grado $\leq 2$ en la variable $t$, provisto del producto interno integral:
                $$\langle f, g \rangle = \int_0^1 f(x)g(x) \, dx.$$
                Si $D: V \to V$ es el operador diferencial ordinario tal que $Df = f'$, determine el operador adjunto $D^*$.
              </p>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Integración por partes:</div>
                <p>
                  Por definición de adjunto, $\langle f, D^* g \rangle = \langle Df, g \rangle$. Evaluando la integral mediante integración por partes:
                  $$\langle Df, g \rangle = \int_0^1 f'(x)g(x) \, dx = [f(x)g(x)]_0^1 - \int_0^1 f(x)g'(x) \, dx = f(1)g(1) - f(0)g(0) - \langle f, Dg \rangle.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Representación de los funcionales de frontera mediante Riesz:</div>
                <p>
                  Los términos de frontera $f \mapsto f(1)$ y $f \mapsto f(0)$ son funcionales lineales en $V$. Por el Teorema de Riesz (Teorema 1.3.1), existen vectores únicos $h_1, h_2 \in V$ tales que $f(1) = \langle f, h_1 \rangle$ y $f(0) = \langle f, h_2 \rangle$.<br>
                  Ortogonalizando la base $\{1, t, t^2\}$ por Gram-Schmidt en $[0, 1]$ se obtienen los polinomios ortonormales $\{\alpha_1, \alpha_2, \alpha_3\}$ con $\alpha_1 = 1$, $\alpha_2 = 2\sqrt{3}t - \sqrt{3}$, $\alpha_3 = 6\sqrt{5}t^2 - 6\sqrt{5}t + \sqrt{5}$. Evaluando $h_1(t) = \sum \alpha_i(1)\alpha_i(t)$ y $h_2(t) = \sum \alpha_i(0)\alpha_i(t)$ (Moore pág. 216):
                  $$h_1(t) = 30t^2 - 24t + 3, \qquad h_2(t) = 30t^2 - 36t + 9.$$
                </p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Expresión explícita del operador adjunto:</div>
                <p style="margin-bottom: 0;">
                  Sustituyendo en la identidad integral:
                  $$\langle f, D^* g \rangle = g(1)\langle f, h_1 \rangle - g(0)\langle f, h_2 \rangle - \langle f, Dg \rangle = \langle f, \; g(1)h_1 - g(0)h_2 - Dg \rangle.$$
                  Haciendo el cambio de variable simbólica de la función a $f$:
                  $$D^*f(t) = (30t^2 - 24t + 3)f(1) - (30t^2 - 36t + 9)f(0) - f'(t).$$
                  En el caso especial de funciones que se anulan en la frontera, $f(0) = f(1) = 0$, el adjunto coincide exactamente con el opuesto de la derivada: $D^*f(t) = -f'(t)$.
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             REPRESENTACIÓN MATRICIAL DEL ADJUNTO: [T*] = [T]^T
          ------------------------------------------------------------------ -->
          <div id="sec-1-3-1-matriz-adjunto">
            <h3 style="margin-top: 2.5rem;">
              <span>Representación Matricial del Adjunto: $[T^*]_\beta = [T]_\beta^T$</span>
              <span class="ref-badge">Moore §4.6 pág. 216 & Teorema 6.3</span>
            </h3>

            <!-- EJEMPLO 5 DE MOORE §4.6 -->
            <div class="math-box box-ex">
              <div class="math-box-header">Ejemplo 1.3.5: El Adjunto desde la Perspectiva Matricial (Moore §4.6 Ejemplo 5, pág. 216)</div>
              <p>
                Consideremos el operador lineal $T$ en el espacio euclidiano $V_n$ desde el punto de vista de su matriz representante relativa a una base ortonormal. Si $X$ es un vector arbitrario de $V_n$ escrito como matriz columna, entonces $TX = AX$, donde $A$ es la matriz que representa a $T$.<br>
                Recordando que la regla para calcular el producto interno en presencia de una base ortonormal es invariante e igual a $\langle X, Y \rangle = Y^T X$, se tiene:
              </p>
              <div class="formula-card">
                $$\langle TX, Y \rangle = \langle AX, Y \rangle = Y^T (AX) = (A^T Y)^T X = \langle X, A^T Y \rangle.$$
              </div>
              <p style="margin-bottom: 0;">
                Por consiguiente, para todo $Y \in V_n$, se deduce de inmediato que $T^* Y = A^T Y$. La conclusión fundamental observada por Moore es que <strong>la matriz que representa a $T^*$ es exactamente la transpuesta $A^T$ de la matriz que representa a $T$</strong>.
              </p>
            </div>

            <div class="math-box box-thm" style="margin-top: 1.5rem;">
              <div class="math-box-header">Teorema 1.3.3: Matriz del Adjunto en Base Ortonormal (Moore Teorema 6.3)</div>
              <p>
                Sea $V$ un espacio euclidiano de dimensión finita y sea $\beta = \{u_1, u_2, \dots, u_n\}$ una base <strong>ortonormal</strong> de $V$. Si $A = [T]_\beta$ es la matriz de $T$ en $\beta$, entonces:
              </p>
              <div class="formula-card" style="font-size: 1.25rem;">
                $$[T^*]_\beta = [T]_\beta^T = A^T.$$
              </div>

              <div class="proof-card">
                <div class="proof-header"><i>Demostración formal.</i></div>
                <p>
                  Sean $A = (a_{ij}) = [T]_\beta$ y $B = (b_{ij}) = [T^*]_\beta$. Dado que $\beta$ es ortonormal, las entradas de las matrices representantes vienen dadas por los coeficientes de Fourier:
                  $$a_{ij} = \langle T(u_j), u_i \rangle, \qquad b_{ij} = \langle T^*(u_j), u_i \rangle.$$
                  Por la propiedad definitoria del operador adjunto:
                  $$b_{ij} = \langle T^*(u_j), u_i \rangle = \langle u_i, T^*(u_j) \rangle = \langle T(u_i), u_j \rangle = a_{ji}.$$
                  Como $b_{ij} = a_{ji}$ para todos $i, j \in \{1, \dots, n\}$, concluimos que $B = A^T$. $\blacksquare$
                </p>
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             PROPIEDADES ALGEBRAICAS Y ORTOGONALIDAD NÚCLEO-IMAGEN
          ------------------------------------------------------------------ -->
          <div id="sec-1-3-1-propiedades-adjuntos">
            <h3 style="margin-top: 2.5rem;">
              <span>Álgebra de Adjuntos & Ortogonalidad Núcleo-Imagen</span>
              <span class="ref-badge">Moore Teorema 6.4 págs. 217–219</span>
            </h3>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema 1.3.4: Propiedades Algebraicas del Operador Adjunto</div>
              <div class="step-card">
                <div class="step-card-title"><span class="step-badge">1</span> Linealidad:</div>
                <p style="margin-bottom: 0;">$(S + T)^* = S^* + T^*$ y $(cT)^* = cT^*$ para todo escalar $c \in \mathbb{R}$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">2</span> Inversión en la Composición:</div>
                <p style="margin-bottom: 0;">$(ST)^* = T^* S^*$.</p>
              </div>
              <div class="step-card" style="margin-top: 0.6rem;">
                <div class="step-card-title"><span class="step-badge">3</span> Involución e Identidad:</div>
                <p style="margin-bottom: 0;">$(T^*)^* = T$, $I_V^* = I_V$, $0^* = 0$, y si $T$ es invertible, $(T^*)^{-1} = (T^{-1})^*$.</p>
              </div>
            </div>

            <div class="math-box box-thm">
              <div class="math-box-header">Teorema Fundamental: Relaciones de Ortogonalidad de Subespacios</div>
              <p>
                Para cualquier operador lineal $T: V \to V$ en un espacio euclidiano de dimensión finita:
              </p>
              <div class="formula-card" style="font-size: 1.15rem;">
                $$\ker(T^*) = (\operatorname{Im}(T))^\perp \qquad \text{y} \qquad \operatorname{Im}(T^*) = (\ker(T))^\perp.$$
              </div>
            </div>
          </div>

          <!-- -----------------------------------------------------------------
             1.3.2 OPERADORES AUTOADJUNTOS
          ------------------------------------------------------------------ -->
          <div id="sec-1-3-2-operadores-autoadjuntos">
            <h3 style="margin-top: 2.5rem;">
              <span>1.3.2 Operadores Autoadjuntos y Matrices Simétricas</span>
              <span class="ref-badge">Moore §4.6 págs. 219–220</span>
            </h3>

            <div class="math-box box-def">
              <div class="math-box-header">Definición 1.3.1: Operador Autoadjunto / Simétrico</div>
              <p>
                Un operador lineal $T: V \to V$ en un espacio euclidiano se denomina <strong>autoadjunto</strong> (o <em>simétrico</em>) si es igual a su propio adjunto:
              </p>
              <div class="formula-card">
                $$T^* = T \quad \iff \quad \langle T(\alpha), \beta \rangle = \langle \alpha, T(\beta) \rangle \quad \text{para todos } \alpha, \beta \in V.$$
              </div>
              <p style="margin-top: 0.75rem; margin-bottom: 0;">
                En cualquier base ortonormal $\beta$, $[T]_\beta = [T]_\beta^T$; es decir, la matriz que representa a un operador autoadjunto es necesariamente una <strong>matriz real simétrica</strong> ($A = A^T$).
              </p>
            </div>
          </div>
        </section>
    '''
