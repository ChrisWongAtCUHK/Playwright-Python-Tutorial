# [Playwright Python Tutorial](https://www.youtube.com/playlist?list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A)
## [Automated Testing in Python with PLAYWRIGHT + PYTEST](https://www.youtube.com/watch?v=IDrTacdVNRM&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A&index=2)
```
pytest --headed --base-url https://www.saucedemo.com/
```
```
pytest --headed --base-url https://www.saucedemo.com/ --browser chromium --browser firefox
```
```
pytest --headed --base-url https://www.saucedemo.com/ --browser-channel chrome
```
```
pytest --headed --base-url https://www.saucedemo.com/ --tracing on
playwright show-trace test-results/test-saucedemo-py-test-title-chromium/trace.zip
playwright k-trace test-results/test-saucedemo-py-test-inventory-site-chromium/trace.zip
```
```
pytest --headed --base-url https://www.saucedemo.com/ --browser firefox --browser chromium --headed --slowmo 1000 --tracing on
```

## [Automated TEST generated with PLAYWRIGHT + PYTHON. IS IT POSSIBLE? 💡](https://www.youtube.com/watch?v=IRTeqUXkPbA&list=PLYDwWPRvXB8_W56h2C1z5zrlnAlvqpJ6A&index=3)
