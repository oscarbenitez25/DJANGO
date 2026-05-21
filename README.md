# 📝 Django Blog

Aplicació web tipus blog desenvolupada amb Django com a projecte pràctic del curs.

## 🎯 Objectiu

Crear una aplicació web completa que permeti:

- Veure els darrers posts a la pàgina principal
- Navegar pel llistat complet de posts
- Llegir el detall de cada post
- Explorar els autors i els seus posts
- Filtrar posts per tags

## 🛠️ Tecnologies

- **Python 3.11**
- **Django 4.2**
- **Bootstrap 5** (via django-bootstrap5)
- **SQLite** (base de dades en desenvolupament)
- **GitHub Actions** (CI/CD)

## 📁 Estructura del projecte

```
my_site/
├── .github/
│   └── workflows/
│       └── django.yml        # CI/CD amb GitHub Actions
├── blog/
│   ├── fixtures/
│   │   └── initial_data.json # Dades inicials (5 autors, 5 tags, 15 posts)
│   ├── migrations/           # Migracions de la base de dades
│   ├── static/blog/
│   │   ├── css/styles.css    # Estils personalitzats
│   │   └── images/           # Imatges
│   ├── templates/blog/
│   │   ├── base.html         # Template base amb navbar i footer
│   │   ├── index.html        # Pàgina principal
│   │   ├── post_list.html    # Llistat de posts
│   │   ├── post_detail.html  # Detall d'un post
│   │   ├── authors_list.html # Llistat d'autors
│   │   ├── author_detail.html# Detall d'un autor
│   │   ├── tag_list.html     # Llistat de tags
│   │   ├── tag_post.html     # Posts per tag
│   │   ├── 404.html          # Pàgina d'error 404
│   │   └── includes/
│   │       └── post.html     # Card reutilitzable de post
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Models: Post, Author, Tag
│   ├── tests.py              # Tests unitaris
│   ├── urls.py               # Rutes de l'app blog
│   └── views.py              # Vistes
├── my_site/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
└── README.md
```

## 🚀 Instal·lació

1. **Clonar el repositori**

```bash
git clone https://github.com/usuari/my_site.git
cd my_site
```

2. **Crear i activar entorn virtual**

```bash
python -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows
```

3. **Instal·lar dependències**

```bash
pip install -r requirements.txt
```

4. **Aplicar migracions**

```bash
python manage.py migrate
```

5. **Carregar dades inicials**

```bash
python manage.py loaddata blog/fixtures/initial_data.json
```

6. **Crear superusuari** (per accedir a l'admin)

```bash
python manage.py createsuperuser
```

## ▶️ Execució

```bash
python manage.py runserver
```

L'aplicació estarà disponible a: **http://127.0.0.1:8000**

## 🌐 Rutes disponibles

| URL | Descripció |
|-----|-----------|
| `/` | Pàgina principal amb els 3 darrers posts |
| `/posts` | Llistat de tots els posts |
| `/posts/<slug>` | Detall d'un post |
| `/authors` | Llistat d'autors |
| `/authors/<id>` | Detall d'un autor i els seus posts |
| `/tags` | Llistat de tags |
| `/tags/<tag>` | Posts filtrats per tag |
| `/admin/` | Panell d'administració |

## 🗄️ Models

### Post
- `title` — Títol del post (CharField, min 5 caràcters)
- `excerpt` — Resum breu (CharField, min 10 caràcters)
- `image` — Imatge (ImageField, opcional)
- `date` — Data de publicació (DateField, auto)
- `slug` — URL amigable (SlugField, únic)
- `content` — Contingut complet (TextField, min 20 caràcters)
- `author` — Autor (ForeignKey → Author)
- `tags` — Tags (ManyToManyField → Tag)

### Author
- `first_name` — Nom (CharField)
- `last_name` — Cognom (CharField)
- `email` — Correu electrònic (EmailField, únic)

### Tag
- `caption` — Nom del tag (CharField, únic)

## 🧪 Tests

Executar tots els tests:

```bash
python manage.py test
```

Els tests cobreixen:
- **Models**: creació, `__str__`, unicitat, relacions
- **URLs**: status codes, vistes resoltes, templates usats
- **Vistes**: context passat, comportament 404, nombre de resultats

## 🤖 GitHub Actions (CI/CD)

El workflow `.github/workflows/django.yml` s'executa automàticament en cada push i pull request:

1. Clona el repositori
2. Instal·la Python 3.11
3. Instal·la les dependències
4. Aplica les migracions
5. Executa els tests

## 👑 Panell d'Administració

Accedeix a `/admin/` amb el superusuari per:
- Afegir, editar i eliminar posts
- Gestionar autors i tags
- Visualitzar les relacions entre models