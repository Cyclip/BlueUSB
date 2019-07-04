<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="icon.png" alt="Logo" width="100" height="80">
  </a>

  <h3 align="center">BlueUSB</h3>

  <p align="center">
    Fake Blue Screen of Death because, why not?
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About

BlueUSB is an opensource tool to generate fake BSoDs, probably as an evil prank. It supports **Windows Only** and only tested on Windows. A list of features:

* Autodetects the Windows version and displays the correct type of BSoD
* Suspends as much running processes as possible to give a good illusion - quite evil.
  * If you don't like the sound of that, it also has nice mode which disables this.
* "Nice mode" which disables suspending processes and also has a timer to remove the BSoD
* Force a specific type of Windows Version
  * You can have a Windows 10 blue screen on a Windows 8.1 computer if you wanted to
* Windows 7, Windows 8/8.1 and Windows 10 have their own BSoDs
* Windows 10 allows for a customm "return code".
* Easy-to-use generator that generates the file as an EXE.
* Export exe directly to the USB drive, or just keep it as a folder
  * Automatically executes the BSoD right when its plugged in
  * Or take the exe and use it however you want
* Quite lightweight - if you use the Python ZIP/RAR
  * The generator is only 39kb, and the output is only *7kb*
  * The exe generator will be quite massive, and .rar is better.
* Free minecraft account inside
  * *(jk no)*

### Built With
BlueUSB is built with stuff
* [Python](https://www.python.org/)
* [Qt](https://www.qt.io/)
* [PyQt](https://pypi.org/project/PyQt5/)

<!-- GETTING STARTED -->
## Getting Started

There are 2 editions - Python & EXE. Python has the raw code in it and it's smaller. EXE is compiled but larger.
Choose a specfic edition and follow.

<details>
  <summary>Python (rar/zip)</summary>
  
  ### Prerequisites

  This is an example of how to list things you need to use the software and how to      install them.
  * npm
  ```sh
  npm install npm@latest -g
  ```

  ### Installation

  1. Get a free API Key at [https://example.com](https://example.com)
  2. Clone the repo
  ```sh
  git clone https:://github.com/your_username_/Project-Name.git
  ```
  3. Install NPM packages
  ```sh
  npm install
  ```
  4. Enter your API in `config.js`
  ```JS
  const API_KEY = 'ENTER YOUR API';
  ```
    ```
</details>





<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@your_twitter](https://twitter.com/your_username) - email@example.com

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Img Shields](https://shields.io)
* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[build-shield]: https://img.shields.io/badge/build-passing-brightgreen.svg?style=flat-square
[build-url]: #
[contributors-shield]: https://img.shields.io/badge/contributors-1-orange.svg?style=flat-square
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[license-shield]: https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square
[license-url]: https://choosealicense.com/licenses/mit
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: https://raw.githubusercontent.com/othneildrew/Best-README-Template/master/screenshot.png
