# PHINOX — Django Foundation (Phase 1)

Production-grade Django scaffold for the PHINOX e-commerce platform, built against
the Stitch UI export. See `IMPLEMENTATION_PLAN.md` for full architecture, database,
API, security, and deployment planning.

## What's in Phase 1

- Django project (`config/`) with split settings (`base`/`dev`/`staging`/`prod`)
- 14 apps scaffolded under `apps/` (`__init__.py` + `apps.py` only — **no models,
  no business logic** — that's later phases)
- Template inheritance chain: `base.html` → `base_standard.html` /
  `base_checkout.html` → real pages
- Two pages ported **verbatim** from the Stitch export: `core/404.html` and
  `pages/contact.html` (see IMPLEMENTATION_PLAN.md §6.2 for why these two, and only
  these two, are included in an otherwise "no page conversion" phase)
- Reusable component partials (`templates/core/components/`) for the TopAppBar
  variants, Bottom Nav Dock, Orange Lock Stitch, shader background, etc.
- Docker + docker-compose (web, PostgreSQL, Redis, Celery worker, Celery beat)
- `requirements/{base,dev,prod}.txt`, `.env.example`, `.gitignore`, `.dockerignore`
- `package.json` + `tailwind.config.js` for the future production Tailwind CLI build
  (**not yet wired in** — current templates still use the Stitch CDN script for
  pixel-fidelity; see comments in those files)

## Known, disclosed deviations from the raw Stitch HTML

These do not change layout, spacing, color, typography, or interaction — only
markup-level cleanup required to make the files valid Django templates:

1. **`data-alt` → `alt`/`aria-hidden`** on the two decorative background images (404
   hero texture, Contact map). The Stitch export used a non-standard `data-alt`
   attribute that has no real accessibility effect; this is now a proper `alt` (map
   image) or `aria-hidden="true"` (purely decorative 404 texture). Zero visual change.
2. **Duplicate Material Symbols stylesheet `<link>`** (present twice in every source
   page) was not de-duplicated in the ported templates — kept as-is as it's harmless
   and preserves "don't change anything" as literally as possible.
3. Everything else — every Tailwind class, every inline `<style>`/`<script>` block,
   every copy string, every color, every spacing value — is unchanged.

## Explicitly NOT done in Phase 1

Per your instructions: no models, no migrations beyond the empty `migrations/`
package, no authentication, no payments, no cart, no orders, no Checkout page
templating, no Home/PLP/PDP (not supplied by Stitch yet — see plan §5).

## Running it

```bash
cp .env.example .env      # then fill in real values
docker compose -f docker/docker-compose.yml up --build
```

Or locally without Docker:

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements/dev.txt
cp .env.example .env
python manage.py migrate   # no-op beyond Django's own built-in tables — no app models yet
python manage.py runserver
```

Visit `/contact/` and any bad URL (to see the custom 404) to verify the ported pages
render pixel-for-pixel against the Stitch source.

## Open questions blocking later phases

See IMPLEMENTATION_PLAN.md §5 — none of them block Phase 1, but Phase 2/3 shouldn't
start until at least #5, #6, and #7 (the two-token-family question, the 404 radius
bug, and the missing `touch-target-min` value) are confirmed by you.
