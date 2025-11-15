# url_ai_checker

Librería en Python para revisar el funcionamiento de URLs utilizando inteligencia artificial (IA). Utiliza un clasificador basado en machine learning para determinar si una URL está funcionando correctamente, además de proporcionar herramientas para gestionar colas de URLs y relaciones gráficas entre ellas.

## Instalación

```bash
pip install -e .
```

## Dependencias

- requests
- scikit-learn
- numpy
- networkx

## Uso Básico

### Revisar una URL

```python
from url_ai_checker import UrlAIChecker

checker = UrlAIChecker()
result = checker.check_url("https://www.google.com")
print(result)
# {'url': 'https://www.google.com', 'http_status': 200, 'ai_status': 'healthy'}
```

### Gestionar una Cola de URLs

```python
from url_ai_checker import UrlQueue

queue = UrlQueue()
queue.enqueue("https://example.com")
queue.enqueue("https://github.com")

while not queue.is_empty():
    url = queue.dequeue()
    print(f"Procesando: {url}")
```

### Gestionar Relaciones Gráficas entre URLs

```python
from url_ai_checker import UrlGraph

graph = UrlGraph()
graph.add_relation("https://site.com", "https://site.com/page1")
graph.add_relation("https://site.com", "https://site.com/page2")

links = graph.get_links_from("https://site.com")
print(links)  # ['https://site.com/page1', 'https://site.com/page2']
```

## API Reference

### UrlAIChecker

- `check_url(url: str) -> dict`: Revisa una URL y devuelve un diccionario con el estado HTTP y la predicción de IA.

### UrlQueue

- `enqueue(url: str)`: Agrega una URL a la cola.
- `dequeue() -> str or None`: Remueve y devuelve la primera URL de la cola.
- `is_empty() -> bool`: Verifica si la cola está vacía.

### UrlGraph

- `add_relation(src_url: str, dest_url: str)`: Agrega una relación de enlace entre dos URLs.
- `get_links_from(url: str) -> list`: Devuelve las URLs a las que apunta la URL dada.
- `get_links_to(url: str) -> list`: Devuelve las URLs que apuntan a la URL dada.

## Utilidades

### Validación de URLs

```python
from url_ai_checker.utils.helpers import validate_url

is_valid = validate_url("https://www.example.com")
print(is_valid)  # True
```

### Extracción de Características

```python
from url_ai_checker.utils.helpers import extract_url_features

features = extract_url_features("https://www.example.com/path?query=value")
print(features)
# {'length': 42, 'has_https': True, 'domain_length': 15, ...}
```

## Contribución

1. Fork el repositorio.
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`).
3. Commit tus cambios (`git commit -am 'Agrega nueva funcionalidad'`).
4. Push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

MIT
## instala la libreria (setup.py) con :
pip install .

## y ejecutala con 

python -m pytest tests/ -v

## de esta manera podriamos usar la libreria .
