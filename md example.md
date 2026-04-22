# 📊 Crypto Price Tracker (Django + CoinGecko)

## 📌 Descripción

Aplicación web desarrollada en Django que consume la API de CoinGecko para obtener precios históricos de criptomonedas, almacenarlos en una base de datos y visualizarlos mediante gráficos.

El sistema permite trabajar con múltiples activos (ej: BTC) y múltiples monedas (ej: USD, CLP), manteniendo una estructura de datos flexible y escalable.

---

## ⚙️ Tecnologías utilizadas

* Python 3.x
* Django
* Django REST Framework
* PostgreSQL
* Plotly

---

## 🚀 Instalación

### 1. Clonar repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos

Editar `settings.py` con tus credenciales de PostgreSQL.

Luego ejecutar:

```bash
python manage.py migrate
```

### 5. Ejecutar servidor

```bash
python manage.py runserver
```

Acceder en:

```
http://127.0.0.1:8000/
```

---

## 📊 Uso

* El sistema obtiene datos históricos de precios desde la API de CoinGecko.
* Los datos se almacenan en la base de datos local.
* Se visualizan mediante gráficos interactivos (Plotly).
* Por defecto, se muestran precios diarios de Bitcoin en un rango de hasta 364 días.

---

## 🧠 Decisiones de diseño

### 1. Modelado de datos

Se separaron las entidades en tres modelos principales:

* `Activo` (ej: BTC)
* `Moneda` (ej: USD, CLP)
* `Precio` (relación entre activo, moneda y tiempo)

Esto permite:

* soportar múltiples criptomonedas
* soportar múltiples monedas fiat
* evitar duplicación de datos

---

### 2. Precisión de datos

Se utiliza `DecimalField` para almacenar precios, evitando errores de precisión asociados a `FloatField`.

---

### 3. Manejo del tiempo

Los datos de la API incluyen timestamps en milisegundos (UTC), los cuales se convierten a `DateTime` antes de almacenarse.

Esto permite:

* mantener consistencia temporal
* soportar diferentes niveles de granularidad en el futuro

---

### 4. Unicidad de datos

Se define una restricción única sobre:

```
(activo, moneda, fecha)
```

Esto evita duplicados y permite usar estrategias eficientes de inserción/actualización.

---

### 5. Inserción de datos

Se utilizan operaciones en lote (`bulk_create`) para mejorar el rendimiento al guardar múltiples registros.

---

## 🔧 Posibles mejoras

* Soporte para múltiples criptomonedas en el frontend
* Filtros por rango de fechas
* Cacheo de respuestas de la API
* Tareas programadas (cron / Celery) para actualización automática
* Tests unitarios

---

## 🧪 Tests

```bash
python manage.py test
```

---

## 📌 Notas

Este proyecto fue desarrollado con foco en:

* modelado correcto de datos
* integración con APIs externas
* separación clara de responsabilidades

No busca ser un sistema completo de producción, sino una base sólida y extensible.

---
