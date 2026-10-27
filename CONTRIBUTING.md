# Contributing

Thanks for helping improve Mastermind Simulations. Contributions should make the learning activities clearer, more accessible, or more reliable for students and teachers.

## Before you start

- Search the [existing issues](https://github.com/gosafoosei/Mastermind/issues) and, when available, the [Projects board](https://github.com/gosafoosei/Mastermind/projects) before starting larger work.
- For a bug, use the **Bug report** issue form and include steps to reproduce, expected and actual results, and browser/device details.
- For a new idea, use the **Feature request** form to explain the learning need and how success can be checked.
- If no live board exists yet, follow [.github/PROJECT_BOARD.md](.github/PROJECT_BOARD.md) to configure it. Add accepted issues to the board once it is available.
- Avoid including student names, personal information, or other private classroom data in issues, screenshots, or commits.

## Make a change

1. Fork the repository and create a focused branch from `main`.
2. Keep the four labs usable with keyboard, touch, and mouse input; use local assets so the offline package continues to work.
3. If you change Tailwind classes or configuration, run `npm ci` and `npm run build:css`.
4. Run the site with `npm run serve`. Check the affected lab, its navigation, and the browser console. For layout changes, check a narrow phone width and a desktop width.
5. If your change affects the offline files, run `npm run package:offline` and confirm the ZIP contains the updated files.
6. Open a pull request against `main`. Describe the student-facing change and list the checks you performed; include a screenshot for visual changes.

## Content and assets

Only contribute content and assets that you created or are permitted to redistribute. Keep applicable credit and license notices with third-party material. Do not assume that the MIT source-code license applies to images, PDFs, scans, the logo, or the anatomical model; see [THIRD-PARTY-NOTICES.txt](THIRD-PARTY-NOTICES.txt).
