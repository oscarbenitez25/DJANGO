# 📝 Django Blog

Aplicació web tipus blog desenvolupada amb Django com a projecte pràctic del mòdul M485 — Programació (BLOC 6).

## 🎯 Objectiu

Crear una aplicació web completa que permeti:

- Veure els darrers posts a la pàgina principal
- Navegar pel llistat complet de posts
- Llegir el detall de cada post
- Explorar els autors i els seus posts publicats
- Filtrar posts per etiquetes (tags)

## 🛠️ Tecnologies utilitzades

- **Python 3.11**
- **Django 4.2**
- **Bootstrap 5** (via `django-bootstrap5`)
- **SQLite** (base de dades en desenvolupament)
- **GitHub Actions** (integració contínua / CI)

## 📁 Estructura del projecte

```
my_site/
├── .github/
│   └── workflows/
│       └── django.yml         # CI amb GitHub Actions
├── blog/
│   ├── fixtures/
│   │   └── initial_data.json  # Dades inicials (5 autors, 5 tags, 15 posts)
│   ├── migrations/            # Migracions de la base de dades
│   ├── static/blog/
│   │   ├── css/styles.css     # Estils personalitzats
│   │   └── images/            # Imatges estàtiques
│   ├── templates/blog/
│   │   ├── base.html          # Plantilla base amb navbar i footer
│   │   ├── index.html         # Pàgina principal
│   │   ├── post_list.html     # Llistat de posts
│   │   ├── post_detail.html   # Detall d'un post
│   │   ├── authors_list.html  # Llistat d'autors
│   │   ├── author_detail.html # Detall d'un autor
│   │   ├── tag_list.html      # Llistat de tags
│   │   ├── tag_post.html      # Posts filtrats per tag
│   │   ├── 404.html           # Pàgina d'error 404
│   │   └── includes/
│   │       └── post.html      # Card reutilitzable de post
│   ├── admin.py
│   ├── apps.py
│   ├── models.py              # Models: Post, Author, Tag
│   ├── tests.py               # Tests unitaris
│   ├── urls.py                # Rutes de l'app blog
│   └── views.py               # Vistes
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Instal·lació ràpida

### 1. Clonar el repositori

```bash
git clone https://github.com/oscarbenitez25/DJANGO.git
cd DJANGO
```

### 2. Crear i activar l'entorn virtual

```bash
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3. Instal·lar dependències

```bash
pip install -r requirements.txt
```

### 4. Aplicar les migracions

```bash
python manage.py migrate
```

### 5. Carregar les dades inicials

```bash
python manage.py loaddata blog/fixtures/initial_data.json
```

### 6. Crear un superusuari (per accedir al panell d'administració)

```bash
python manage.py createsuperuser
```

## ▶️ Execució del projecte

```bash
python manage.py runserver
```

L'aplicació estarà disponible a: **http://127.0.0.1:8000**

## 🌐 Rutes disponibles

| URL | Descripció |
|-----|------------|
| `/` | Pàgina principal amb els 3 darrers posts |
| `/posts` | Llistat complet de posts (ordenats per data descendent) |
| `/posts/<slug>` | Detall d'un post |
| `/authors` | Llistat de tots els autors |
| `/authors/<id>` | Detall d'un autor i els seus posts |
| `/tags` | Llistat de totes les etiquetes |
| `/tags/<id>` | Posts filtrats per etiqueta |
| `/admin/` | Panell d'administració de Django |

## 🗄️ Models

### `Post`
| Camp | Tipus | Descripció |
|------|-------|------------|
| `title` | `CharField` | Títol del post (mínim 5 caràcters) |
| `excerpt` | `CharField` | Resum breu (mínim 10 caràcters) |
| `image` | `CharField` | Nom de la imatge associada |
| `date` | `DateField` | Data de publicació |
| `slug` | `SlugField` | URL amigable (únic) |
| `content` | `TextField` | Contingut complet (mínim 20 caràcters) |
| `author` | `ForeignKey` | Relació amb `Author` (un a molts) |
| `tags` | `ManyToManyField` | Relació amb `Tag` (molts a molts) |

### `Author`
| Camp | Tipus | Descripció |
|------|-------|------------|
| `first_name` | `CharField` | Nom de l'autor |
| `last_name` | `CharField` | Cognom de l'autor |
| `email` | `EmailField` | Adreça de correu electrònic (única) |

### `Tag`
| Camp | Tipus | Descripció |
|------|-------|------------|
| `caption` | `CharField` | Nom de l'etiqueta (únic) |

### Relacions entre models

```
Author ──< Post >── Tag
(1:N)          (N:M)
```

- Un **Author** pot tenir molts **Posts** (relació un a molts).
- Un **Post** pot tenir moltes **Tags**, i una **Tag** pot pertànyer a molts **Posts** (relació molts a molts).

## 🧪 Tests unitaris

Per executar tots els tests:

```bash
python manage.py test
```

Els tests cobreixen:
- **Models**: creació correcta, mètode `__str__`, unicitat de camps, relacions entre models
- **URLs**: codis d'estat HTTP, vistes resoltes, plantilles utilitzades
- **Vistes**: context passat a les plantilles, comportament en cas de 404, nombre de resultats retornats

## 🤖 Integració contínua amb GitHub Actions

El fitxer `.github/workflows/django.yml` s'executa automàticament en cada `push` i `pull request` a la branca principal. Els passos que realitza són:

1. Clonar el repositori
2. Instal·lar Python 3.11
3. Instal·lar les dependències del projecte
4. Aplicar les migracions
5. Executar tots els tests unitaris

## 👑 Panell d'administració

Accedeix a `/admin/` amb el superusuari creat per:

- Afegir, editar i eliminar posts, autors i tags
- Gestionar les relacions entre models
- Carregar imatges i dades de prova

## 📚 Documentació dels mòduls (Pydoc)

La documentació dels fitxers `.py` del projecte ha estat generada automàticament amb **Pydoc** mitjançant una GitHub Action i es publica a GitHub Pages.

🔗 [Veure documentació dels mòduls](https://oscarbenitez25.github.io/DJANGO/)
