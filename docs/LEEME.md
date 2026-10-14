# Automatización de facturas

OCR, normalización, validación económica y conciliación con Holded.

## Qué demuestra este caso

El pipeline completo depende de Google/Azure, BigQuery y Holded. La demo ejecuta exclusivamente el control original de una línea.

**Resultado del proyecto:** Varios restaurantes y una asesoría; uso actual declarado por Ignacio.

## Probar el componente

Requiere Python 3.10 o posterior. No necesita instalar dependencias, introducir claves ni conectar una cuenta.

```sh
python3 -I demo.py
```

La demo usa datos sintéticos y rechaza conexiones de red y subprocesos. Verifica 5 comportamientos del código original. [Resultados](../verification.json).

## Recorrido del código

[source/sample.py](../source/invoice_controls.py) es la muestra ejecutable. Funciones check_line_level y approx_equal sin cambios; solo imports typing para aislarlas. [Procedencia completa](../provenance.json).

- [E01 OCR Google Document AI y procesamiento por lotes](../evidence/E01.md)
- [E02 OCR Azure, normalización, polling y retries](../evidence/E02.md)
- [E03 Validación de cabecera, IVA y suma de líneas](../evidence/E03.md)
- [E04 Integración de documentos, cuentas y conciliación con Holded](../evidence/E04.md)
- [E05 Embeddings y similitud de descripciones bancarias](../evidence/E05.md)

## Alcance

Este caso conserva una selección de una construcción mayor. Los identificadores de infraestructura y clientes se han anonimizado donde corresponde; la procedencia registra las modificaciones. Para ejecutarla completa se necesitarían sus adaptadores y servicios; esta muestra no despliega ni modifica Chals AI.

[Portada en inglés](../README.md) · [Arquitectura](architecture.md) · [Decisiones](decisions.md) · [Recorrido del código](code-tour.md).
