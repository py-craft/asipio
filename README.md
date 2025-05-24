# aiovoip

![Python 3.11](https://img.shields.io/badge/python-3.11-blue?logo=python)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue?logo=python)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue?logo=python)

**aiovoip** is a modern, asynchronous SIP (Session Initiation Protocol) library for Python. It was forked from the deprecated [aiosip](https://github.com/Eyepea/aiosip) project (eaf8504), with the goal of revitalizing and maintaining a clean, bug-fixed, and feature-rich codebase and in the future to implement other protocols in VoIP field.

The uniqueness of this library lies in its fully asynchronous design, allowing for efficient handling of SIP messages and calls without blocking the main thread. This makes it ideal for applications that require real-time communication, but at the same time, able to handle hundreds of thousands of SIP messages per second, without asynchronous behavior this would be challenging for Python to achieve.


> ⚠️ **Warning:** This library is in an early stage of development. Use at your own risk, and always pick the specific version of the library.

## Features

- Fully asynchronous SIP implementation
- Clean and modernized codebase
- Ongoing maintenance and feature development
- Python 3.11, 3.12, and 3.13 compatibility

## Python Compatibility

`aiovoip` is tested and works with:
- Python **3.11**
- Python **3.12**
- Python **3.13**

## Installation

You can install `aiovoip` using pip:

```bash
pip install aiovoip
```

Refer to the [examples](./examples/) for guidance on usage.


## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

## Contributing

We welcome and appreciate all contributions! Please read the [CONTRIBUTING](CONTRIBUTING.md) guide for information on how to get involved—whether you're reporting a bug, suggesting an improvement, enhancing documentation.


## Sponsors

<a href="https://codeff.nl" target="_blank" title="Codeff"><img src="https://www.codeff.nl/static/images/Og-Project.png" width="200"></a>
