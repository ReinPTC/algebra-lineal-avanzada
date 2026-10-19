# -*- coding: utf-8 -*-
"""
Generador Maestro y Ensamblador de la Unidad 1 en index.html
Inserta o actualiza todo el contenido estructurado de Unidad 1
(Hero Banner, Temas 1.0, 1.1, 1.2, 1.3, 1.4 y Banco de Ejercicios)
inmediatamente después de Unidad 4, antes de la Bibliografía Oficial.
"""

import os
from generator_u1.content_tema1_0 import get_tema_1_0_html
from generator_u1.content_tema1_1 import get_tema_1_1_html
from generator_u1.content_tema1_2 import get_tema_1_2_html
from generator_u1.content_tema1_3 import get_tema_1_3_html
from generator_u1.content_tema1_4 import get_tema_1_4_html
from generator_u1.content_ejercicios import get_ejercicios_u1_html

def get_intro_banner():
    return """<!-- =====================================================================
           UNIDAD 1: HERO BANNER & INTRODUCCIÓN GENERAL
        ====================================================================== -->
        <section id="intro-u1" class="hero-banner">
          <span class="hero-tag">Módulo Curricular • Unidad Temática I</span>
          <h2 class="hero-title" style="font-size: 2.1rem; margin-top: 0.25rem;">
            Unidad 1: Transformaciones Ortogonales y Productos Internos
          </h2>
          <div class="hero-meta">
            <div>
              <strong>🎯 Unidad de Competencia Oficial (IPN - ESFM):</strong> Determina transformaciones ortogonales y productos internos de los espacios vectoriales a partir de matrices definidas positivas.
            </div>
            <div>
              <strong>⏱️ Carga Horaria Curricular:</strong> 16.5 h Teoría • 3.0 h Práctica • 7.0 h Aprendizaje Autónomo (Total: 26.5 h).
            </div>
            <div>
              <strong>📖 Textos Base:</strong> John T. Moore, <em>Elements of Linear Algebra and Matrix Theory</em> (Cap. 4: Inner-Product Spaces) • Stephen H. Friedberg et al., <em>Álgebra lineal</em> (Cap. 6: Espacios con producto interno).
            </div>
          </div>
          <p style="margin-top: 1rem; font-size: 0.95rem; line-height: 1.7; color: var(--text-secondary); text-align: justify;">
            En esta unidad se profundiza en la estructura métrica y geométrica de los espacios vectoriales reales. Partiendo de la generalización del producto punto ordinario hacia formas bilineales simétricas definidas positivas (productos internos), se deducen rigurosamente las nociones universales de longitud de vectores, ángulos no dirigidos, ortogonalidad y complementos ortogonales. Sobre este andamiaje métrico se estudian las isometrías del espacio —las transformaciones ortogonales— y su representación mediante matrices ortogonales, desembocando en la dualidad de funcionales lineales (Teorema de Riesz), los operadores adjuntos y la caracterización espectral y matricial completa de los productos internos a través de matrices simétricas definidas positivas y la descomposición cuadrática de Cholesky.
          </p>
        </section>
"""

def main():
    print("Iniciando ensamble de Unidad 1 en index.html...")
    with open('index.html', 'r', encoding='utf-8') as f:
        html = f.read()

    start_marker = "<!-- =====================================================================\n           UNIDAD 1: HERO BANNER & INTRODUCCIÓN GENERAL"
    end_marker = "<!-- =====================================================================\n           BIBLIOGRAFÍA OFICIAL IPN & TEXTO BASE"

    start_idx = html.find(start_marker)
    end_idx = html.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("No se encontraron los marcadores de delimitación de Unidad 1 en index.html.")

    full_u1_body = (
        get_intro_banner() + "\n" +
        get_tema_1_0_html() + "\n" +
        get_tema_1_1_html() + "\n" +
        get_tema_1_2_html() + "\n" +
        get_tema_1_3_html() + "\n" +
        get_tema_1_4_html() + "\n"
        # Banco de ejercicios ocultado por solicitud del usuario:
        # get_ejercicios_u1_html() + "\n"
    )

    new_html = html[:start_idx] + full_u1_body + html[end_idx:]

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"¡Éxito! index.html actualizado correctamente. Nuevo tamaño: {len(new_html)} bytes.")

if __name__ == '__main__':
    main()
