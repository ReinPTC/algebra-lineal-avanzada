/* ==============================================================================
   Herramientas Interactivas y Calculadores de Álgebra Lineal Avanzada
   ESFM — IPN • Unidad 4: Similaridad y Operadores Normales
   Tema 4.0.1: 2.2 Representación matricial de una transformación lineal
============================================================================== */

window.InteractiveTools = {
  // 1. Explorador y Calculador de Vector Coordenado [x]_beta (Ejemplo 16)
  initCoordinateVectorTool: function () {
    const a0Input = document.getElementById('coord-a0');
    const a1Input = document.getElementById('coord-a1');
    const a2Input = document.getElementById('coord-a2');
    const polyDisplay = document.getElementById('coord-poly-display');
    const vectorDisplay = document.getElementById('coord-vector-display');
    const expansionDisplay = document.getElementById('coord-expansion-display');

    if (!a0Input || !a1Input || !a2Input) return;

    function update() {
      const a0 = parseFloat(a0Input.value) || 0;
      const a1 = parseFloat(a1Input.value) || 0;
      const a2 = parseFloat(a2Input.value) || 0;

      // Formatear polinomio f(x)
      let polyStr = '';
      if (a0 !== 0 || (a1 === 0 && a2 === 0)) polyStr += `${a0}`;
      
      if (a1 !== 0) {
        const sign = a1 > 0 ? (polyStr ? ' + ' : '') : (polyStr ? ' - ' : '-');
        const absVal = Math.abs(a1) === 1 ? '' : Math.abs(a1);
        polyStr += `${sign}${absVal}x`;
      }

      if (a2 !== 0) {
        const sign = a2 > 0 ? (polyStr ? ' + ' : '') : (polyStr ? ' - ' : '-');
        const absVal = Math.abs(a2) === 1 ? '' : Math.abs(a2);
        polyStr += `${sign}${absVal}x^2`;
      }

      if (polyDisplay) {
        polyDisplay.innerHTML = `$$f(x) = ${polyStr}$$`;
      }

      if (vectorDisplay) {
        vectorDisplay.innerHTML = `$$[f]_\\beta = \\begin{pmatrix} ${a0} \\\\ ${a1} \\\\ ${a2} \\end{pmatrix}$$`;
      }

      if (expansionDisplay) {
        expansionDisplay.innerHTML = `$$f(x) = (${a0})\\cdot 1 + (${a1})\\cdot x + (${a2})\\cdot x^2$$`;
      }

      if (window.triggerKaTeX) window.triggerKaTeX();
    }

    [a0Input, a1Input, a2Input].forEach(inp => inp.addEventListener('input', update));

    // Preset buttons
    const btnEx16 = document.getElementById('btn-preset-ex16');
    if (btnEx16) {
      btnEx16.addEventListener('click', () => {
        a0Input.value = 4;
        a1Input.value = 6;
        a2Input.value = -7;
        update();
      });
    }

    const btnCustom1 = document.getElementById('btn-preset-coord1');
    if (btnCustom1) {
      btnCustom1.addEventListener('click', () => {
        a0Input.value = 2;
        a1Input.value = -3;
        a2Input.value = 5;
        update();
      });
    }

    const btnCustom2 = document.getElementById('btn-preset-coord2');
    if (btnCustom2) {
      btnCustom2.addEventListener('click', () => {
        a0Input.value = -8;
        a1Input.value = 0;
        a2Input.value = 1;
        update();
      });
    }

    update();
  },

  // 2. Calculador Interactivo de la Matriz de Derivación T: P3(R) -> P2(R) (Ejemplo 17)
  initDerivativeMatrixTool: function () {
    const c0Input = document.getElementById('deriv-c0');
    const c1Input = document.getElementById('deriv-c1');
    const c2Input = document.getElementById('deriv-c2');
    const c3Input = document.getElementById('deriv-c3');

    const fxDisplay = document.getElementById('deriv-fx-display');
    const fprimeDisplay = document.getElementById('deriv-fprime-display');
    const multDisplay = document.getElementById('deriv-mult-display');

    if (!c0Input || !c1Input || !c2Input || !c3Input) return;

    function update() {
      const c0 = parseFloat(c0Input.value) || 0;
      const c1 = parseFloat(c1Input.value) || 0;
      const c2 = parseFloat(c2Input.value) || 0;
      const c3 = parseFloat(c3Input.value) || 0;

      // Derivada f'(x) = c1 + 2*c2*x + 3*c3*x^2
      const d0 = c1;
      const d1 = 2 * c2;
      const d2 = 3 * c3;

      if (fxDisplay) {
        fxDisplay.innerHTML = `$$f(x) = ${c0} + ${c1}x + ${c2}x^2 + ${c3}x^3 \\implies [f]_\\beta = \\begin{pmatrix} ${c0} \\\\ ${c1} \\\\ ${c2} \\\\ ${c3} \\end{pmatrix}$$`;
      }

      if (fprimeDisplay) {
        fprimeDisplay.innerHTML = `$$f'(x) = ${d0} + ${d1}x + ${d2}x^2 \\implies [f']_\\gamma = \\begin{pmatrix} ${d0} \\\\ ${d1} \\\\ ${d2} \\end{pmatrix}$$`;
      }

      if (multDisplay) {
        multDisplay.innerHTML = `$$\\underbrace{\\begin{pmatrix} 0 & 1 & 0 & 0 \\\\ 0 & 0 & 2 & 0 \\\\ 0 & 0 & 0 & 3 \\end{pmatrix}}_{[T]_\\beta^\\gamma} \\underbrace{\\begin{pmatrix} ${c0} \\\\ ${c1} \\\\ ${c2} \\\\ ${c3} \\end{pmatrix}}_{[f]_\\beta} = \\begin{pmatrix} 0(${c0}) + 1(${c1}) + 0(${c2}) + 0(${c3}) \\\\ 0(${c0}) + 0(${c1}) + 2(${c2}) + 0(${c3}) \\\\ 0(${c0}) + 0(${c1}) + 0(${c2}) + 3(${c3}) \\end{pmatrix} = \\underbrace{\\begin{pmatrix} ${d0} \\\\ ${d1} \\\\ ${d2} \\end{pmatrix}}_{[T(f)]_\\gamma}$$`;
      }

      if (window.triggerKaTeX) window.triggerKaTeX();
    }

    [c0Input, c1Input, c2Input, c3Input].forEach(inp => inp.addEventListener('input', update));

    const btnPresetEx17 = document.getElementById('btn-preset-ex17');
    if (btnPresetEx17) {
      btnPresetEx17.addEventListener('click', () => {
        c0Input.value = 5;
        c1Input.value = -3;
        c2Input.value = 4;
        c3Input.value = 2;
        update();
      });
    }

    const btnPresetEx22 = document.getElementById('btn-preset-ex22');
    if (btnPresetEx22) {
      btnPresetEx22.addEventListener('click', () => {
        c0Input.value = 2;
        c1Input.value = -4;
        c2Input.value = 1;
        c3Input.value = 3;
        update();
      });
    }

    const btnPresetEx30 = document.getElementById('btn-preset-ex30');
    if (btnPresetEx30) {
      btnPresetEx30.addEventListener('click', () => {
        c0Input.value = 2;
        c1Input.value = 1;
        c2Input.value = -3;
        c3Input.value = 5;
        update();
      });
    }

    update();
  },

  // 3. Calculador de Transformación Lineal T: R^2 -> R^3 (Ejemplo 18)
  initLinearTransformR2R3Tool: function () {
    const a1Input = document.getElementById('r2r3-a1');
    const a2Input = document.getElementById('r2r3-a2');
    const directDisplay = document.getElementById('r2r3-direct-display');
    const matrixMultDisplay = document.getElementById('r2r3-matrix-display');

    if (!a1Input || !a2Input) return;

    function update() {
      const a1 = parseFloat(a1Input.value) || 0;
      const a2 = parseFloat(a2Input.value) || 0;

      // T(a1, a2) = (a1 + 3a2, 0, 2a1 - 4a2)
      const y1 = a1 + 3 * a2;
      const y2 = 0;
      const y3 = 2 * a1 - 4 * a2;

      if (directDisplay) {
        directDisplay.innerHTML = `$$T(${a1}, ${a2}) = (${a1} + 3(${a2}),\\ 0,\\ 2(${a1}) - 4(${a2})) = (${y1},\\ ${y2},\\ ${y3})$$`;
      }

      if (matrixMultDisplay) {
        matrixMultDisplay.innerHTML = `$$[T]_\\beta^\\gamma [x]_\\beta = \\begin{pmatrix} 1 & 3 \\\\ 0 & 0 \\\\ 2 & -4 \\end{pmatrix} \\begin{pmatrix} ${a1} \\\\ ${a2} \\end{pmatrix} = \\begin{pmatrix} 1(${a1}) + 3(${a2}) \\\\ 0(${a1}) + 0(${a2}) \\\\ 2(${a1}) - 4(${a2}) \\end{pmatrix} = \\begin{pmatrix} ${y1} \\\\ ${y2} \\\\ ${y3} \\end{pmatrix} = [T(x)]_\\gamma$$`;
      }

      if (window.triggerKaTeX) window.triggerKaTeX();
    }

    [a1Input, a2Input].forEach(inp => inp.addEventListener('input', update));

    const btnPresetE1 = document.getElementById('btn-preset-e1');
    if (btnPresetE1) {
      btnPresetE1.addEventListener('click', () => {
        a1Input.value = 1;
        a2Input.value = 0;
        update();
      });
    }

    const btnPresetE2 = document.getElementById('btn-preset-e2');
    if (btnPresetE2) {
      btnPresetE2.addEventListener('click', () => {
        a1Input.value = 0;
        a2Input.value = 1;
        update();
      });
    }

    const btnPresetCustom = document.getElementById('btn-preset-r2r3-custom');
    if (btnPresetCustom) {
      btnPresetCustom.addEventListener('click', () => {
        a1Input.value = 3;
        a2Input.value = -2;
        update();
      });
    }

    update();
  },

  // 4. Calculador de Transformación de Multiplicación por la Izquierda L_A (Ejemplo 6)
  initLeftMultiplicationTool: function () {
    const x1Input = document.getElementById('la-x1');
    const x2Input = document.getElementById('la-x2');
    const x3Input = document.getElementById('la-x3');
    const display = document.getElementById('la-display');

    if (!x1Input || !x2Input || !x3Input || !display) return;

    function update() {
      const x1 = parseFloat(x1Input.value) || 0;
      const x2 = parseFloat(x2Input.value) || 0;
      const x3 = parseFloat(x3Input.value) || 0;

      // A = [1 2 1; 0 1 2]
      const y1 = 1 * x1 + 2 * x2 + 1 * x3;
      const y2 = 0 * x1 + 1 * x2 + 2 * x3;

      display.innerHTML = `$$L_A(x) = Ax = \\begin{pmatrix} 1 & 2 & 1 \\\\ 0 & 1 & 2 \\end{pmatrix} \\begin{pmatrix} ${x1} \\\\ ${x2} \\\\ ${x3} \\end{pmatrix} = \\begin{pmatrix} 1(${x1}) + 2(${x2}) + 1(${x3}) \\\\ 0(${x1}) + 1(${x2}) + 2(${x3}) \\end{pmatrix} = \\begin{pmatrix} ${y1} \\\\ ${y2} \\end{pmatrix}$$`;

      if (window.triggerKaTeX) window.triggerKaTeX();
    }

    [x1Input, x2Input, x3Input].forEach(inp => inp.addEventListener('input', update));

    const btnPresetEx23 = document.getElementById('btn-preset-ex23');
    if (btnPresetEx23) {
      btnPresetEx23.addEventListener('click', () => {
        x1Input.value = 1;
        x2Input.value = 3;
        x3Input.value = -1;
        update();
      });
    }

    const btnPresetLAE1 = document.getElementById('btn-preset-la-e1');
    if (btnPresetLAE1) {
      btnPresetLAE1.addEventListener('click', () => {
        x1Input.value = 1;
        x2Input.value = 0;
        x3Input.value = 0;
        update();
      });
    }

    const btnPresetLAE2 = document.getElementById('btn-preset-la-e2');
    if (btnPresetLAE2) {
      btnPresetLAE2.addEventListener('click', () => {
        x1Input.value = 0;
        x2Input.value = 1;
        x3Input.value = 0;
        update();
      });
    }

    const btnPresetLAE3 = document.getElementById('btn-preset-la-e3');
    if (btnPresetLAE3) {
      btnPresetLAE3.addEventListener('click', () => {
        x1Input.value = 0;
        x2Input.value = 0;
        x3Input.value = 1;
        update();
      });
    }

    update();
  },

  // 5. Simulador Interactivo de Transformaciones Ortogonales en R^2 (Unidad 1 - Tema 1.2)
  initOrthogonalTransformTool: function () {
    const typeSelect = document.getElementById('ortho-type');
    const thetaInput = document.getElementById('ortho-theta');
    const xInput = document.getElementById('ortho-x');
    const yInput = document.getElementById('ortho-y');

    const matrixDisplay = document.getElementById('ortho-matrix-display');
    const propertiesDisplay = document.getElementById('ortho-properties-display');
    const vectorDisplay = document.getElementById('ortho-vector-display');

    if (!typeSelect || !thetaInput || !xInput || !yInput) return;

    function update() {
      const type = typeSelect.value;
      const deg = parseFloat(thetaInput.value) || 0;
      const rad = (deg * Math.PI) / 180;
      const x = parseFloat(xInput.value) || 0;
      const y = parseFloat(yInput.value) || 0;

      const cosT = Math.cos(rad);
      const sinT = Math.sin(rad);

      let a, b, c, d, detVal, typeName;

      if (type === 'rotation') {
        a = cosT;
        b = -sinT;
        c = sinT;
        d = cosT;
        detVal = 1;
        typeName = `Rotación antihoraria R_{${deg}^\\circ}`;
      } else {
        a = cosT;
        b = sinT;
        c = sinT;
        d = -cosT;
        detVal = -1;
        typeName = `Reflexión especular S_{${deg}^\\circ}`;
      }

      const tx = a * x + b * y;
      const ty = c * x + d * y;

      const normOrig = Math.sqrt(x * x + y * y);
      const normTrans = Math.sqrt(tx * tx + ty * ty);

      if (matrixDisplay) {
        matrixDisplay.innerHTML = `$$A = \\begin{pmatrix} ${a.toFixed(4)} & ${b.toFixed(4)} \\\\ ${c.toFixed(4)} & ${d.toFixed(4)} \\end{pmatrix}, \\quad \\det(A) = ${detVal > 0 ? '+1' : '-1'}$$`;
      }

      if (propertiesDisplay) {
        propertiesDisplay.innerHTML = `
          <strong>Tipo:</strong> ${typeName} • <strong>Ortogonalidad:</strong> $A^T A = I_2$<br>
          <strong>Columnas ortonormales:</strong> $\|C_1\| = 1.0000$, $\|C_2\| = 1.0000$, $C_1 \\cdot C_2 = 0.0000$
        `;
      }

      if (vectorDisplay) {
        vectorDisplay.innerHTML = `$$T\\begin{pmatrix} ${x} \\\\ ${y} \\end{pmatrix} = \\begin{pmatrix} ${tx.toFixed(3)} \\\\ ${ty.toFixed(3)} \\end{pmatrix}, \\quad \\|\\alpha\\| = ${normOrig.toFixed(3)}, \\quad \\|T\\alpha\\| = ${normTrans.toFixed(3)}$$`;
      }

      if (window.triggerKaTeX) window.triggerKaTeX();
    }

    [typeSelect, thetaInput, xInput, yInput].forEach(elem => elem.addEventListener('input', update));

    const btn45 = document.getElementById('btn-ortho-preset-45');
    if (btn45) {
      btn45.addEventListener('click', () => {
        typeSelect.value = 'rotation';
        thetaInput.value = 45;
        xInput.value = 3;
        yInput.value = 4;
        update();
      });
    }

    const btn90 = document.getElementById('btn-ortho-preset-90');
    if (btn90) {
      btn90.addEventListener('click', () => {
        typeSelect.value = 'rotation';
        thetaInput.value = 90;
        xInput.value = 2;
        yInput.value = 1;
        update();
      });
    }

    const btnRef = document.getElementById('btn-ortho-preset-ref');
    if (btnRef) {
      btnRef.addEventListener('click', () => {
        typeSelect.value = 'reflection';
        thetaInput.value = 60;
        xInput.value = 1;
        yInput.value = 2;
        update();
      });
    }

    update();
  },

  // 6. Simulador Interactivo de Matrices Positivas & Producto A-Interno (Unidad 1 - Tema 1.4)
  initPositiveMatrixTool: function () {
    const aInput = document.getElementById('pos-mat-a');
    const bInput = document.getElementById('pos-mat-b');
    const dInput = document.getElementById('pos-mat-d');

    const x1Input = document.getElementById('pos-x1');
    const x2Input = document.getElementById('pos-x2');
    const y1Input = document.getElementById('pos-y1');
    const y2Input = document.getElementById('pos-y2');

    const matDisplay = document.getElementById('pos-matrix-display');
    const sylvesterDisplay = document.getElementById('pos-sylvester-display');
    const choleskyDisplay = document.getElementById('pos-cholesky-display');
    const innerDisplay = document.getElementById('pos-inner-display');

    if (!aInput || !bInput || !dInput) return;

    function update() {
      const a = parseFloat(aInput.value) || 0;
      const b = parseFloat(bInput.value) || 0;
      const d = parseFloat(dInput.value) || 0;

      const x1 = parseFloat(x1Input.value) || 0;
      const x2 = parseFloat(x2Input.value) || 0;
      const y1 = parseFloat(y1Input.value) || 0;
      const y2 = parseFloat(y2Input.value) || 0;

      const delta1 = a;
      const delta2 = a * d - b * b;

      // Eigenvalores de matriz simétrica 2x2: tr = a + d, det = delta2
      const tr = a + d;
      const disc = Math.max(0, tr * tr - 4 * delta2);
      const l1 = (tr + Math.sqrt(disc)) / 2;
      const l2 = (tr - Math.sqrt(disc)) / 2;

      let clasificacion = '';
      let colorClass = '#10b981';
      let esDefPos = false;

      if (delta1 > 0 && delta2 > 0) {
        clasificacion = 'Definida Positiva (Admite Producto Interno)';
        colorClass = '#10b981';
        esDefPos = true;
      } else if (delta1 < 0 && delta2 > 0) {
        clasificacion = 'Definida Negativa';
        colorClass = '#ef4444';
      } else if (delta2 === 0 && (delta1 >= 0 && d >= 0)) {
        clasificacion = 'Semidefinida Positiva';
        colorClass = '#f59e0b';
      } else if (delta2 < 0) {
        clasificacion = 'Indefinida (Signos Opuestos)';
        colorClass = '#8b5cf6';
      } else {
        clasificacion = 'Semidefinida / Indefinida';
        colorClass = '#f59e0b';
      }

      if (matDisplay) {
        matDisplay.innerHTML = `$$A = \\begin{pmatrix} ${a} & ${b} \\\\ ${b} & ${d} \\end{pmatrix}$$`;
      }

      if (sylvesterDisplay) {
        sylvesterDisplay.innerHTML = `
          <strong>Menores de Sylvester:</strong> $\\Delta_1 = ${delta1}$, $\\Delta_2 = \\det(A) = ${delta2.toFixed(3)}$<br>
          <strong>Eigenvalores:</strong> $\\lambda_1 = ${l1.toFixed(3)}, \\lambda_2 = ${l2.toFixed(3)}$<br>
          <span style="color: ${colorClass}; font-weight: bold; font-size: 1.05rem;">Clasificación: ${clasificacion}</span>
        `;
      }

      if (choleskyDisplay) {
        if (esDefPos) {
          const q11 = Math.sqrt(a);
          const q12 = b / q11;
          const q22Sq = d - q12 * q12;
          const q22 = Math.sqrt(Math.max(0, q22Sq));
          choleskyDisplay.innerHTML = `$$A = Q^T Q \\quad \\text{con} \\quad Q = \\begin{pmatrix} ${q11.toFixed(3)} & ${q12.toFixed(3)} \\\\ 0 & ${q22.toFixed(3)} \\end{pmatrix}$$`;
        } else {
          choleskyDisplay.innerHTML = `<em>No admite factorización de Cholesky con diagonal real positiva (no es definida positiva).</em>`;
        }
      }

      // Cálculo del producto interno A: <X, Y>_A = X^T A Y
      // Y = (y1, y2)^T, A*Y = (a*y1 + b*y2, b*y1 + d*y2)^T
      const ay1 = a * y1 + b * y2;
      const ay2 = b * y1 + d * y2;
      const innerProd = x1 * ay1 + x2 * ay2;

      // Normas inducidas por A
      const normXSq = x1 * (a * x1 + b * x2) + x2 * (b * x1 + d * x2);
      const normXStr = normXSq > 0 ? Math.sqrt(normXSq).toFixed(3) : 'No definida';

      if (innerDisplay) {
        innerDisplay.innerHTML = `$$\\langle X, Y \\rangle_A = X^T A Y = ${innerProd.toFixed(3)}, \\quad \\|X\\|_A = ${normXStr}$$`;
      }

      if (window.triggerKaTeX) window.triggerKaTeX();
    }

    [aInput, bInput, dInput, x1Input, x2Input, y1Input, y2Input].forEach(elem => elem.addEventListener('input', update));

    const btnPos = document.getElementById('btn-pos-preset-defpos');
    if (btnPos) {
      btnPos.addEventListener('click', () => {
        aInput.value = 3;
        bInput.value = 1;
        dInput.value = 2;
        update();
      });
    }

    const btnNeg = document.getElementById('btn-pos-preset-defneg');
    if (btnNeg) {
      btnNeg.addEventListener('click', () => {
        aInput.value = -3;
        bInput.value = 1;
        dInput.value = -2;
        update();
      });
    }

    const btnIndef = document.getElementById('btn-pos-preset-indef');
    if (btnIndef) {
      btnIndef.addEventListener('click', () => {
        aInput.value = 1;
        bInput.value = 3;
        dInput.value = 1;
        update();
      });
    }

    update();
  }
};

