 # Proyecto de Monitoreo con Prometheus y Grafana

Autores: Maira Balanta y Natalia Cajiao
 Descripción

Este proyecto consiste en implementar un sistema básico de monitoreo usando Docker, Prometheus, Node Exporter y Grafana, con el fin de visualizar métricas del sistema Linux y generar alertas simples.

 ¿Qué aprendimos al integrar Docker, AWS y Prometheus?

Aprendimos cómo ejecutar servicios de monitoreo de manera aislada usando Docker, cómo exponerlos en una máquina virtual en AWS y cómo Prometheus recolecta métricas en tiempo real. También entendimos cómo Grafana usa esos datos para visualizarlos de forma clara.

 ¿Qué fue lo más desafiante y cómo lo resolveríamos en un entorno real?

Lo más difícil fue la configuración de redes y puertos entre cada servicio (Prometheus, Node Exporter y Grafana).
En un entorno real lo resolveríamos usando:

documentación clara de red,

reglas de seguridad bien definidas,

automatización con Docker Compose o infraestructura como código.

 ¿Qué beneficio aporta la observabilidad en el ciclo DevOps?

La observabilidad permite detectar problemas rápido, entender el estado del sistema en tiempo real y mejorar la estabilidad del servicio. En DevOps ayuda a reducir fallos, acelerar la respuesta a incidentes y optimizar el rendimiento.
