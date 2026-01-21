# GCS Semana 2 · Baseline v1.0 (Repositorio auditable)

## Objetivo
Repositorio de ejemplo para demostrar **reproducibilidad, auditoría y trazabilidad** con:
- estructura ordenada
- commits con mensajes claros
- tag `v1.0` + Release

## Estructura
- `/docs/SRS/` Requisitos (SRS)
- `/docs/SDD/` Diseño (SDD)
- `/src/` Código mínimo
- `/tests/` Evidencias / placeholder
- `/config/` Configuración controlada (ejemplo)
- `/scripts/` Scripts auxiliares

## Ejecución (demo)
```bash
python src/hello_baseline.py report
```

## Baseline v1.0
```bash
git tag -a v1.0 -m "Baseline v1.0: SRS+SDD approved + minimal build"
git push origin v1.0
```
