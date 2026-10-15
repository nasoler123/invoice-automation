# Automatización de facturas

**Automatización de facturas que dos restaurantes siguen utilizando cada mes**

*Un caso de Chals AI — construido por Ignacio Soler.*

Construí un flujo de procesamiento de facturas que combina extracción de documentos, validación económica y preparación contable para Holded.

Construí este proyecto yo solo, de principio a fin, utilizando herramientas de IA para toda la programación. Me encargué de la definición del producto, las decisiones técnicas, la implementación, la integración y la validación.

[Ver el flujo](#ver-el-flujo) · [Explorar la implementación](#explorar-la-implementación) · [Probar el componente](#probar-el-componente) · [English](../README.md)

## Qué construí

- Extracción mediante OCR y normalización de la información de las facturas.
- Controles de impuestos, totales y campos obligatorios.
- Asignación de proveedores y cuentas, preparación del registro en Holded y búsqueda de coincidencias en descripciones bancarias para apoyar la conciliación.

**Estado:** Construido en 2024–2025; activo en octubre de 2026. **Dos restaurantes lo utilizan cada mes.**

Uso comunicado por el fundador el 15 de octubre de 2026. El volumen de facturas y el ahorro de tiempo no se han cuantificado.

## Ver el flujo

**Factura → extracción → validación → preparación contable → apoyo a la conciliación.**

![Arquitectura de Automatización de facturas](overview.svg)

## Explorar la implementación

El componente ejecutable contiene los controles originales de impuestos y totales de una línea de factura. Los extractos de código documentan el trabajo más amplio: OCR, normalización, BigQuery, integración con Holded y similitud de descripciones bancarias.

| Recurso | Qué puedes consultar |
|---|---|
| [invoice_controls.py](../source/invoice_controls.py) | Componente original ejecutable |
| [demo.py](../demo.py) | Datos sintéticos y 5 comportamientos comprobados |
| [Arquitectura](architecture.md) | Sistema completo y alcance de la muestra |
| [Decisiones de diseño](decisions.md) | Decisiones y referencias al código |
| [Recorrido del código](code-tour.md) | 5 extractos seleccionados de la implementación |
| [Procedencia](../provenance.json) | Rutas originales, commits, hashes y modificaciones documentadas |

<details>
<summary>Ver los extractos seleccionados</summary>

- [E01 OCR Google Document AI y procesamiento por lotes](../evidence/E01.md)
- [E02 OCR Azure, normalización, polling y retries](../evidence/E02.md)
- [E03 Validación de cabecera, IVA y suma de líneas](../evidence/E03.md)
- [E04 Integración de documentos, cuentas y conciliación con Holded](../evidence/E04.md)
- [E05 Embeddings y similitud de descripciones bancarias](../evidence/E05.md)

</details>

**Tecnologías del proyecto:** Python · Google Document AI · Azure Document Intelligence · BigQuery · Holded · embeddings.

Este caso público incluye código original seleccionado y una muestra ejecutable aislada con datos sintéticos. Las integraciones de producción y los datos de clientes se mantienen privados. Las rutas originales, commits, hashes y modificaciones se registran en [provenance.json](../provenance.json).

## Probar el componente

Ejecuta localmente los controles originales de impuestos y totales de una línea de factura con datos sintéticos. Requiere **Python 3.10 o posterior**, sin instalar dependencias ni conectar una cuenta. Ejecuta estos comandos desde la terminal:

```sh
git clone https://github.com/nasoler123/invoice-automation.git
cd invoice-automation
python3 -I demo.py
python3 verify.py
```

Resultados esperados:

- Una línea coherente supera la validación.
- Un IVA incorrecto, un total incorrecto y los campos ausentes fallan por motivos distintos.
- Los importes cero son entradas válidas.

La muestra funciona sin conexión y rechaza conexiones de red y subprocesos externos. `verify.py` comprueba enlaces locales, igualdad de instrucciones, hash del código, patrones de credenciales y coincidencia con los resultados registrados de las comprobaciones del componente. [Resultados registrados](../verification.json).

## Más proyectos de Chals AI

Estos proyectos recogen mi trabajo en automatización de negocio, software financiero, agentes de IA e infraestructura de datos.

[Data Platform and MCP](https://github.com/nasoler123/data-platform-mcp) · [Financial Modeling SaaS](https://github.com/nasoler123/financial-modeling-saas) · [AI Agent Harness](https://github.com/nasoler123/ai-agent-harness)

[Ignacio Soler](https://github.com/nasoler123) · [LinkedIn](https://www.linkedin.com/in/ignacio-soler-esteban/)
