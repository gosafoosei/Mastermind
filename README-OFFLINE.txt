MASTERMIND SIMULATIONS — OFFLINE SITE PACKAGE

START HERE (Windows)
1. Extract the entire ZIP to a folder.
2. Double-click START-OFFLINE-SITE.bat.
3. The site opens at http://127.0.0.1:8000 and runs locally without an internet connection.

Python 3 must be installed. If the launcher reports that Python is missing, install Python 3 and try again. Keep the launcher console open while using the site; close it to stop the local server.

You may also run a local server from this folder with:
  python -m http.server 8000 --bind 127.0.0.1
Then open http://127.0.0.1:8000/index.html.

The model, JavaScript libraries, icon fonts, Tailwind stylesheet, lesson diagrams, scanned pages, and PDFs are included. Do not open index.html directly as a file: browsers block local 3D model loading from file URLs.

For a school network, an IT administrator can copy this folder to an internal web server. Keep the relative folder structure intact.
