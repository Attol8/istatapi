# How to contribute

## Development setup

`istatapi` is built with [nbdev](https://nbdev.fast.ai/): the source of truth is the notebooks in `nbs/`, and the Python modules under `istatapi/` are auto-generated.

```bash
git clone https://github.com/Attol8/istatapi
cd istatapi
pip install -e . nbdev
nbdev-install-hooks
```

`nbdev-install-hooks` installs git hooks that strip notebook metadata on commit (prevents noisy diffs and merge conflicts).

## Making changes

1. Edit the relevant notebook in `nbs/` (not the `.py` files directly).
2. Regenerate the modules and tests: `nbdev-export`.
3. Run the test suite: `nbdev-test`.
4. Rebuild the docs locally to preview: `nbdev-docs` (output goes to `_docs/`).

## Tests

Tests live inline in the notebooks (cells using `fastcore.test` helpers like `test_eq`, `test_fail`). When fixing a bug, add a cell that fails without your patch and passes with it.

Run them all with:

```bash
nbdev-test
```

## CI and deployment

Two GitHub Actions workflows run on every push to `main`:

- **CI** (`.github/workflows/test.yaml`) — installs the package on Python 3.10/3.11/3.12 and runs a smoke test against the live ISTAT endpoint.
- **Deploy to GitHub Pages** (`.github/workflows/deploy.yaml`) — runs `nbdev-docs` and pushes the rendered site to the `gh-pages` branch. The published site lives at https://attol8.github.io/istatapi/.

Pull requests run CI too; deploy only fires from `main`.

## PR submission

* Keep each PR focused on one change. Don't bundle unrelated fixes.
* Don't mix style-only edits with functional ones — they make review hard.
* Include a test that demonstrates the fix or new behavior.
* Reference the issue number in the description if applicable.

## Reporting bugs

* Search existing issues first.
* If filing a new one: include a minimal repro, the full traceback, and your environment (Python version, `istatapi` version).
